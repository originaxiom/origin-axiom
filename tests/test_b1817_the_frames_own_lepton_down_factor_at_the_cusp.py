"""B1817 -- the frame's own lepton/down factor at the cusp: the equal-exponent slopes (B1788's closed form, exact), the
committed map's integer census (4 and 1/4 only, at every N_c), and the referee's scans regenerated on main."""
import json, pathlib, re
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1817_the_frames_own_lepton_down_factor_at_the_cusp" / "verification"


def _nn(x): x = x % 1; return min(x, 1 - x)
def _e2(qL, qR, a): return F(1, 2) - (_nn(2 * qL * a) + _nn(2 * qR * a)) / 2
def _ch(nc): return {"Q": 1, "u": -(nc + 1), "d": nc - 1, "L": -nc, "e": 2 * nc}


def test_the_equal_exponent_slopes_and_the_charge_algebra():
    for nc, n in ((3, 31), (2, 39), (4, 39), (5, 31)):
        q = _ch(nc)
        s = [F(j, N) for N in range(1, 31) for j in range(N // 2 + 1) if F(j, N).denominator == N and _e2(q["Q"], q["d"], F(j, N)) == _e2(q["L"], q["e"], F(j, N))]
        assert len(s) == n
        assert q["L"] == -nc * q["Q"] and q["Q"] + q["d"] == q["L"] + q["e"] == nc       # L/Q = -N_c; both pairs' totals N_c
        assert (F(q["e"], q["d"]) == nc) == (nc == 3)                                     # e/d = 2N_c/(N_c - 1) is N_c only at 3
    assert F(1, 10) in [F(j, N) for N in range(1, 31) for j in range(N // 2 + 1) if _e2(1, 2, F(j, N)) == _e2(-3, 6, F(j, N))]
    assert _e2(1, 2, F(1, 7)) != _e2(-3, 6, F(1, 7))                                       # the referee's unequal spot-check


def test_the_integer_census_is_4_and_a_quarter_at_every_n_c():
    s = json.loads((V / "a1_cusp_map_summary.json").read_text(encoding="utf-8"))
    hits = s["integer limits (b-independent, Im 12, L_max)"]
    assert set(hits) == {"N_c 2", "N_c 3", "N_c 4", "N_c 5"}
    for k, v in hits.items():
        vals = {x.split(": ")[1] for x in v}
        assert vals == {"4", "1/4"}, (k, vals)
    # the integer does not move with N_c: the same {4, 1/4} at N_c = 2, 3, 4, 5 (equal to N_c only at 4, by coincidence)
    assert all({x.split(": ")[1] for x in v} == {"4", "1/4"} for v in hits.values()) and "3" not in {x.split(": ")[1] for x in hits["N_c 3"]}
    rows = [json.loads(l) for l in (V / "a1_cusp_map.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(rows) == 840 and not any("error" in r for r in rows)
    r = {(x["nc"], x["alpha"], x["b"], x["Im"]): x for x in rows}
    assert abs(r[(3, "1/10", 0.137, 12.0)]["L_max|S"]["R2"] - 4) < 0.01 and abs(r[(3, "2/5", 0.311, 12.0)]["L_max|S"]["R2"] - 1) < 1e-3
    assert abs(r[(3, "1/8", 0.137, 12.0)]["L_max|S"]["R2"] / r[(3, "1/8", 0.311, 12.0)]["L_max|S"]["R2"] - 1) < 1e-4   # a true line constant
    assert abs(r[(3, "1/12", 0.137, 12.0)]["L_max|S"]["R2"] / r[(3, "1/12", 0.311, 12.0)]["L_max|S"]["R2"] - 1) > 0.3  # b-dependent


def test_the_referees_scans_regenerated_on_main():
    M = V / "referee" / "main_rerun"
    b = (M / "o_b.txt").read_text(encoding="utf-8")
    vals = [float(x) for x in re.findall(r"^3 1/12 b=\S+ R2 S=(\S+)", b, re.M)]
    assert len(vals) == 10 and max(vals) - min([v for v in vals if v > 0]) > 2                # 1/12: a function of b
    assert re.search(r"^3 5/12 b=0\.050 R2 S=\S+ St=3\.0", b, re.M)                           # 3 on a continuum of b
    c = (M / "o_c.txt").read_text(encoding="utf-8")
    s = [float(x) for x in re.findall(r"2/23 Nc3 Im \d+ S=(\S+)", c)]
    assert s[:6] == sorted(s[:6]) and s[5] > 3.4                                               # 2/23 unconverged at Im 20
