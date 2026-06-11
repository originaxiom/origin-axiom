"""Guard tests for the flagship preprint (papers/flagship).

These do not rebuild the PDF; they enforce the honesty machinery and hygiene that
make the integrative draft legitimate:
  * the GATED headline (SL(4) L=-M^4 / the A_n family) is flagged in the abstract
    and in the knot section, never asserted as settled-novel;
  * the firewall reading is present (a FORCED bridge, a confirmed wall, and the
    structural sharpening kept POSTULATED);
  * no AI-model attribution appears anywhere in the artifact;
  * the figure harness is importable and the expected outputs exist.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FLAG = ROOT / "papers" / "flagship"

AI_LABEL_RE = re.compile(
    r"Chat[- ]?[12]\b|3-?chat|3-?voice|three[- ]voice|Opus 4|Claude|ChatGPT|GPT-4",
    re.IGNORECASE,
)

EXPECTED_FIGS = [
    "fig01_metallic_means", "fig02_fricke_cubic", "fig03_trace_map_dynamics",
    "fig04_dickson_tower", "fig05_opposition_involution", "fig06_apolynomial_sl2",
    "fig07_sl3_character_variety", "fig08_an_family_slope_rank",
    "fig09_sl4_stratification", "fig10_chirality_census", "fig11_cantor_spectrum",
    "fig12_bridge_and_wall",
]


def test_flagship_exists():
    assert (FLAG / "main.tex").is_file()
    assert (FLAG / "refs.bib").is_file()
    assert (FLAG / "figures" / "gen_figures.py").is_file()


def test_gated_headline_flagged():
    abstract = (FLAG / "main.tex").read_text(encoding="utf-8")
    knot = (FLAG / "sections" / "05_the_knot.tex").read_text(encoding="utf-8")
    # the abstract must flag the SL(4)/A_n result GATED
    assert "\\sGated" in abstract, "abstract must carry the GATED badge"
    assert "L=-M^4" in abstract or "L=-M^4" in abstract.replace(" ", "")
    # the knot section must carry the gate and the de-risk-not-close caveat
    assert "\\sGated" in knot
    assert "de-risk" in knot.lower()
    assert "specialist" in knot.lower()
    # the family must be flagged as conjecture, not established for all n
    assert "conjecture" in knot.lower()


def test_firewall_reading_present():
    bridge = (FLAG / "sections" / "07_bridge_and_wall.tex").read_text(encoding="utf-8")
    assert "\\sForced" in bridge, "the bridge must be tagged FORCED"
    assert "\\sPost" in bridge, "the structural sharpening must stay POSTULATED"
    # the wall must be present as a result, and the rhyme distinction named
    assert "wall" in bridge.lower()
    assert "rhyme" in bridge.lower()
    assert "dimensionless" in bridge.lower()


def test_no_ai_labels_in_flagship():
    offenders = []
    for pat in ("*.tex", "*.md", "*.py", "*.bib"):
        for path in FLAG.rglob(pat):
            m = AI_LABEL_RE.search(path.read_text(encoding="utf-8"))
            if m:
                offenders.append(f"{path.relative_to(ROOT)}: {m.group(0)!r}")
    assert offenders == [], offenders


def test_figure_harness_importable_and_outputs_exist():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "gen_figures", FLAG / "figures" / "gen_figures.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # one callable per expected figure
    for name in (f"fig{str(i).zfill(2)}" for i in range(1, 13)):
        assert hasattr(mod, name), f"missing figure function {name}"
    # the committed outputs exist (so the paper builds without re-running)
    out = FLAG / "figures" / "out"
    for fig in EXPECTED_FIGS:
        assert (out / f"{fig}.pdf").is_file(), f"missing {fig}.pdf"
