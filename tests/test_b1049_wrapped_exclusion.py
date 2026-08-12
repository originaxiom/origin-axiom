"""B1049 locks — the wrapped-exclusion defect and the pre-commit blind spot."""
import importlib.util as ilu
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _load(rel, name):
    spec = ilu.spec_from_file_location(name, ROOT / rel)
    m = ilu.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_all_checks_pass():
    R = json.loads(_read("frontier/B1049_the_wrapped_exclusion/results.json"))
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 24


def test_block_filtering_beats_line_filtering_on_a_synthetic_case():
    """The defect, reduced to four lines so the lock does not depend on the live document."""
    MB = _load("scripts/checks/md_blocks.py", "_mb")
    doc = ("- opening line naming **B1043** which authored this bullet\n"
           "  and a continuation line citing B141 that the author token does not reach\n"
           "\n"
           "- an unrelated bullet citing B999\n")
    rx = re.compile(r"\bB1043\b")
    per_line = "\n".join(ln for ln in doc.splitlines() if not rx.search(ln))
    assert "B141" in per_line          # the bug
    assert "B141" not in MB.drop_blocks(doc, rx)     # the fix
    assert "B999" in MB.drop_blocks(doc, rx)         # ...and it drops only the authored block


def test_every_block_line_is_preserved_exactly_once():
    """A filter that loses or duplicates lines would corrupt every measurement built on it."""
    MB = _load("scripts/checks/md_blocks.py", "_mb")
    for f in CURATED + ["docs/BANKING_PROTOCOL.md"]:
        t = _read(f)
        flat = [ln for _, lns in MB.blocks(t) for ln in lns]
        assert flat == t.splitlines(), f


def test_the_four_consumers_use_the_shared_module():
    for rel in ("frontier/B1031_generation_rung/verify.py",
                "frontier/B1032_across_breakings_route/verify.py",
                "frontier/B1037_band_B100_dispositioned/verify.py",
                "frontier/B1048_the_seam_cluster_closed/verify.py"):
        assert "_MB.drop_blocks" in _read(rel), rel
    mod = _read("scripts/checks/md_blocks.py")
    for c in ("B1031", "B1032", "B1037", "B1048"):
        assert c in mod, c          # a shared module that does not name its consumers is a shadow


def test_b1037s_band_count_is_37_again():
    R = json.loads(_read("frontier/B1037_band_B100_dispositioned/results.json"))
    assert R["checks"]["the_band_carries_37_debt_rows"]["pass"] is True
    assert R["checks"]["the_band_carries_37_debt_rows"]["n"] == 37


def test_the_retraction_sweep_sees_uncommitted_files():
    """The blind spot that let B1048 bank two live uses of phrases it had just registered."""
    rs = _load("scripts/checks/retraction_sweep.py", "_rs")
    listed = set(rs._tracked_md())
    both = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "*.md"],
                          cwd=ROOT, capture_output=True, text=True).stdout.split("\n")
    assert listed == {p for p in both if p.strip()}
    assert rs.sweep() == []


def test_the_protocol_carries_the_measured_figures():
    bp = re.sub(r"\s+", " ", _read("docs/BANKING_PROTOCOL.md"))
    assert "48 minutes, measured 2026-08-12 on an UNCONTENDED box" in bp
    assert "A RUN AGAINST A MOVING TREE DISCHARGES NOTHING EITHER" in bp
    assert "the next full suite returned **five failures**" in bp
