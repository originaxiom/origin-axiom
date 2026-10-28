"""B1799 -- the neutrino's self-pairing at the canonical end.  The committed runs: R1 = 0 and an exactly symmetric coupling
for both self-pairings; no exact det M zero for either on the 286 census lines at three points; the Dirac sector's zeros
exactly on B1716's law's 54 lines; the referee's CP-line zeros of the Weinberg pair and its residue identity."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1799_the_neutrinos_self_pairing_at_the_canonical_end" / "verification"


def test_the_census():
    m = json.loads((V / "majorana.json").read_text(encoding="utf-8"))
    for k in ("nucnuc", "LL"):
        assert m[k]["max_R1_rel"] < 1e-15 and m[k]["exact_zero_rows"] == 0 and m[k]["max_asym"] < 1e-15
    assert m["LL"]["n"] == 858 and m["Lnuc"]["exact_zero_rows"] == 162


def test_the_law():
    run = (V / "law_check_run.txt").read_text(encoding="utf-8")
    assert "exact zeros on 54 lines" in run and "agrees on 858 of 858 rows, disagrees on 0" in run
    assert "slope-2/5 lines: Dirac exact zeros on 0 rows of 90" in run


def test_the_referee():
    names = [p.name for p in (V / "referee").glob("r*_run.txt")]
    assert len(names) >= 11
