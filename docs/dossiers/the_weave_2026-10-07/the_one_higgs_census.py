"""W90: one Higgs, three sectors. B1657's two vacuum laws with one Higgs defect shared by every sector, against
HZ2021's mass ratios at M_Z. The rule (W90_RULE.md) was committed before this script; the premises, the hand work
seen before it and the priors are there.

  conjugate vacuum: {m2/m3, m1/m3} = {|d_a|, |d_s|}         -> A = |d_a| lies in the x2 band or the x1 band
  parallel vacuum:  m2/m3 = |d_a + d_s|/4, m1/m3 = |d_a d_s|/4 -> some S in 4(x2 band), P in 4(x1 band) with
                                                                |A - P/A| <= S <= A + P/A
  d_s and every phase free, sector by sector; A the same in every sector (the up quarks see the conjugate Higgs,
  same modulus).

  H1  the sector sets at k = 0 (closed form; the grid agrees)
  H2  k = 2: no assignment of the two vacua to the three sectors has a common A
  H3  k = 2: up and leptons have no common A in any assignment
  H4  k = 2: down and leptons: only (parallel, conjugate) survives, and it contains m_mu/m_tau
  H5  k = 2: up and down: only (parallel, conjugate) survives

Run: python3 the_one_higgs_census.py  ->  the_one_higgs_census.json beside it.
"""
import json
import math
from itertools import combinations, product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_one_higgs_census.json"
SECTORS = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "leptons": ("e", "mu", "tau")}
VACUA = ("parallel", "conjugate")
GRID = np.logspace(-8, 0, 2_000_001)


def data():
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    return hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]


def band(m, s, num, den, k):
    return ((m[num] - k * s[num]) / (m[den] + k * s[den]), (m[num] + k * s[num]) / (m[den] - k * s[den]))


def bands(m, s, sector, k):
    f1, f2, f3 = SECTORS[sector]
    return band(m, s, f2, f3, k), band(m, s, f1, f3, k)


# ----------------------------------------------------------------------------------------------- the sets
def closed_parallel(S, P):
    """{A > 0 : |A - P/A| <= S <= A + P/A} for one S and one P, as intervals"""
    lo, hi = (-S + math.sqrt(S * S + 4 * P)) / 2, (S + math.sqrt(S * S + 4 * P)) / 2
    if S * S < 4 * P:
        return [(lo, hi)]
    r1, r2 = (S - math.sqrt(S * S - 4 * P)) / 2, (S + math.sqrt(S * S - 4 * P)) / 2
    out = [(lo, min(hi, r1)), (max(lo, r2), hi)]
    return [iv for iv in out if iv[0] <= iv[1]]


def mask(vacuum, x2, x1, A=GRID):
    if vacuum == "conjugate":                       # widened by one grid step, so a k = 0 point is not lost
        e = A[1] / A[0] - 1
        return (((A >= x2[0] * (1 - e)) & (A <= x2[1] * (1 + e)))
                | ((A >= x1[0] * (1 - e)) & (A <= x1[1] * (1 + e))))
    Sm, Sp, Pm, Pp = 4 * x2[0], 4 * x2[1], 4 * x1[0], 4 * x1[1]
    lo = np.maximum.reduce([np.full_like(A, Pm), A * (A - Sp), A * (Sm - A)])
    hi = np.minimum(Pp, A * (A + Sp))
    return lo <= hi


def intervals(mk, A=GRID):
    if not mk.any():
        return []
    d = np.diff(mk.astype(np.int8))
    starts = list(np.where(d == 1)[0] + 1) + ([0] if mk[0] else [])
    ends = list(np.where(d == -1)[0]) + ([len(mk) - 1] if mk[-1] else [])
    return [(float(A[a]), float(A[b])) for a, b in zip(sorted(starts), sorted(ends))]


def main():
    m, s = data()
    out = {"status": "W90: one Higgs, three sectors (script committed before its one run)",
           "data": "HZ2021 at M_Z (received/HZ2021_running_masses_MZ.json)",
           "grid": "2e6 + 1 log-spaced points, 1e-8 to 1"}
    masks, sets = {}, {}
    for k in (0, 2, 3):
        for sec in SECTORS:
            x2, x1 = bands(m, s, sec, k)
            for vac in VACUA:
                masks[(k, sec, vac)] = mask(vac, x2, x1)
                sets[f"k={k}|{sec}|{vac}"] = {"x2 band": x2, "x1 band": x1, "A": intervals(masks[(k, sec, vac)])}
    out["sector sets"] = sets
    closed = {}
    for sec in SECTORS:
        x2, x1 = bands(m, s, sec, 0)
        closed[sec] = closed_parallel(4 * x2[0], 4 * x1[0])
    out["parallel sets, k = 0, closed form"] = closed
    step = GRID[1] / GRID[0] - 1
    grid_ok = all(len(closed[sec]) == len(sets[f"k=0|{sec}|parallel"]["A"]) and all(
        abs(g[0] / c[0] - 1) <= 2 * step and abs(g[1] / c[1] - 1) <= 2 * step
        for g, c in zip(sets[f"k=0|{sec}|parallel"]["A"], closed[sec])) for sec in SECTORS)
    want = {"up": [(0.0018, 0.0024), (0.0124, 0.0165)], "down": [(0.034, 0.109)],
            "leptons": [(0.0047, 0.0049), (0.231, 0.240)]}
    h1 = grid_ok and all(len(closed[sec]) == len(want[sec]) and all(
        abs(c[0] / w[0] - 1) <= 0.02 and abs(c[1] / w[1] - 1) <= 0.02 for c, w in zip(closed[sec], want[sec]))
        for sec in SECTORS)
    out["H1"] = {"grid agrees with the closed form": bool(grid_ok), "relative grid step": step, "holds": bool(h1)}
    census = {}
    for k in (0, 2, 3):
        for assign in product(VACUA, repeat=3):
            mk = np.logical_and.reduce([masks[(k, sec, v)] for sec, v in zip(SECTORS, assign)])
            census[f"k={k}|three|" + ",".join(assign)] = intervals(mk)
        for (a, b) in combinations(SECTORS, 2):
            for assign in product(VACUA, repeat=2):
                mk = masks[(k, a, assign[0])] & masks[(k, b, assign[1])]
                census[f"k={k}|{a}+{b}|" + ",".join(assign)] = intervals(mk)
    out["census"] = census

    def alive(prefix):
        return [key.split("|")[2] for key, iv in census.items() if key.startswith(prefix) and iv]

    out["H2"] = {"surviving at k=2": alive("k=2|three|"), "holds": not alive("k=2|three|")}
    out["H3"] = {"surviving at k=2": alive("k=2|up+leptons|"), "holds": not alive("k=2|up+leptons|")}
    dl = alive("k=2|down+leptons|")
    ratio = m["mu"] / m["tau"]
    contains = any(a <= ratio <= b for a, b in census.get("k=2|down+leptons|parallel,conjugate", []))
    out["H4"] = {"surviving at k=2": dl, "m_mu/m_tau": ratio, "contained": bool(contains),
                 "holds": dl == ["parallel,conjugate"] and bool(contains)}
    ud = alive("k=2|up+down|")
    out["H5"] = {"surviving at k=2": ud, "holds": ud == ["parallel,conjugate"]}
    out["k=3 verdict"] = {"three sectors surviving": alive("k=3|three|"),
                          "pairs surviving": {p: alive(f"k=3|{p}|") for p in ("up+down", "up+leptons",
                                                                              "down+leptons")}}
    out["cells"] = {h: out[h]["holds"] for h in ("H1", "H2", "H3", "H4", "H5")}
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
