"""B1648 -- the scope repairs are on the pages: GENESIS v1.44 built from the received v1.43; the five verdict files and
THE_WEAVE carry their scope; the addenda exist; the bite -- the amendment refuses a source that is not v1.43."""
import glob, json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
A = pathlib.Path(__file__).resolve().parents[1]


def _claim(b):
    return json.load(open(glob.glob(str(ROOT / "frontier" / ("%s_*" % b) / "arc_verdict.json"))[0]))


def test_genesis_v1_44_is_the_amendment():
    assert subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"]).returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "- **v1.44 · 2026-10-14 · main B1648.**" in g
    assert "[v1.44] Scoped (Review 63, B1648; B1629's addendum of 2026-10-09)" in g
    assert "The owner's tagging of the unit (v1.39) is the owner's ruling" in g
    assert "The agreement with the ruled moves was checked at Δ⁴ alone" in g


def test_the_verdict_files_and_the_weave_carry_their_scope():
    tag = "[Scoped at Review 63 (B1648, 2026-10-14):"
    for b in ("B1630", "B1636", "B1638", "B1641"):
        assert tag in _claim(b)["claim_one_line"], b
    d = _claim("B1634")
    assert "not forced" in d["scope"]["hypotheses"] and "forced by the lifts" not in d["scope"]["hypotheses"]
    assert "are post-seal (P2-P6" in d["claim_one_line"]
    assert "*(Scoped at Review 63: where the inner automorphisms act." in (ROOT / "docs" / "THE_WEAVE.md").read_text(encoding="utf-8")
    for b, f in (("B1630", "ADDENDUM_2026-10-14_scoped_at_review_63.md"), ("B1631", "ADDENDUM_2026-10-14_what_the_tagging_rested_on.md"),
                 ("B1641", "ADDENDUM_2026-10-14_scoped_at_review_63.md")):
        assert glob.glob(str(ROOT / "frontier" / ("%s_*" % b) / f)), (b, f)


def test_bite_the_amendment_refuses_another_source(tmp_path):
    src = (A / "adoption" / "amend.py").read_text(encoding="utf-8")
    bad = tmp_path / "GENESIS_v1_43_main.md"; bad.write_text("not v1.43\n", encoding="utf-8")
    ns = {"__name__": "x", "__file__": str(A / "adoption" / "amend.py")}
    exec(compile(src, "amend", "exec"), ns); ns["SRC"] = str(bad)
    try:
        ns["build"](); raised = False
    except AssertionError:
        raised = True
    assert raised
