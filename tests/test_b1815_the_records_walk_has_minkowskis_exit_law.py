"""B1815 -- the walk's exit law nu_p = (1-p) M + p F_*M: the reduced identities exactly on rationals, and the committed checks."""
import json, pathlib
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1815_the_records_walk_has_minkowskis_exit_law_exactly" / "verification"


def _q(x):                       # Minkowski's ? on [0, 1] (Stern-Brocot), exact on rationals
    if x in (0, 1): return F(x)
    lo, hi, ylo, yhi = (0, 1), (1, 1), F(0), F(1)
    while True:
        m = F(lo[0] + hi[0], lo[1] + hi[1]); ym = (ylo + yhi) / 2
        if x == m: return ym
        if x < m: hi, yhi = (m.numerator, m.denominator), ym
        else: lo, ylo = (m.numerator, m.denominator), ym


def test_the_two_symmetries_the_proof_rests_on():
    for x in (F(1, 3), F(2, 7), F(5, 13), F(8, 21), F(3, 10)):
        assert _q(1 - x) == 1 - _q(x)                         # x -> 1 - x on [0, 1]
    for y in (F(2, 5), F(3, 7), F(9, 4)):                      # M on [0, inf] via y -> y/(1+y) in [0,1]: the swap y -> 1/y is x -> 1 - x
        x = y / (1 + y); x2 = (1 / y) / (1 + 1 / y)
        assert _q(x2) == 1 - _q(x)


def test_the_committed_checks():
    a = json.loads((V / "exit_law_check.json").read_text(encoding="utf-8"))
    for p in ("0.1", "0.25", "0.5", "0.75"):
        r = a["p = %s" % p]; assert abs(r["P(xi > 0)"] - r["1 - p"]) < 0.01 and r["control: KS(walk, M)"] > 0.09
    b = json.loads((V / "exit_law_check_seed2.json").read_text(encoding="utf-8"))
    assert b["KS(walk, (1-p)M + p(-M))"] < b["5% critical value 1.36 sqrt(2/N)"]
    out = (V / "referee" / "main_rerun" / "exact_stationarity_out.txt").read_text(encoding="utf-8")
    assert out.count("claimed law: max |defect| = 0 ") == 7
