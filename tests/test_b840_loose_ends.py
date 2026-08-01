"""B840 — locks the three dispositions and, above all, the R1 vacuity fix."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _v(slug):
    return json.loads((ROOT / "frontier" / slug / "arc_verdict.json").read_text(encoding="utf-8"))


def test_all_three_loose_ends_now_carry_a_findings_document_and_verdict():
    for slug in ("B499_wild_census", "B557_escalator_campaign", "B590_revival_remainders"):
        assert (ROOT / "frontier" / slug / "FINDINGS.md").is_file(), slug
        assert (ROOT / "frontier" / slug / "arc_verdict.json").is_file(), slug


def test_b499_is_OPEN_because_it_never_ran():
    v = _v("B499_wild_census")
    assert v["verdict"] == "OPEN"
    assert "never executed" in v["claim_one_line"]


def test_b557_carries_both_halves():
    v = _v("B557_escalator_campaign")
    assert v["verdict"] == "PROVED"
    c = v["claim_one_line"]
    assert "ESTABLISHED" in c and "UNSETTLED" in c
    assert "FORCED at rung 1" in c, "E2's deflationary result is the load-bearing one"


def test_the_polish_is_no_longer_underdetermined():
    """The vacuity fix: 9 trace equations (18 real) + 4 gauge = 22, matching 22 unknowns."""
    src = (ROOT / "frontier" / "B590_revival_remainders"
           / "s031_m3_sealing.py").read_text(encoding="utf-8")
    assert "zc[3].real - 1" in src and "zc[4].real - 1" in src, "the exact torus gauge must remain"
    # the phrase SHOULD survive -- in the comment that documents the bug for the next reader
    assert "cannot solve underdetermined" in src, "the diagnosis comment must stay"
    assert "mp.nstr(z.real, 50)" not in src, "no 50-digit truncation may remain in either classifier"
    assert "mp.nstr(z.real, 70)" in src, "in_field must match POWERS' precision"


def test_b590_records_the_vacuity_as_the_finding():
    f = " ".join((ROOT / "frontier" / "B590_revival_remainders"
                  / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "VACUOUS" in f
    assert "nothing was ever tested" in f.lower()
    assert "m=1 does not seal" in f, "the honest post-fix state must be recorded"
