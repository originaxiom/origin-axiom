"""B1963 (main, 2026-11-19; data-free): is the reading's conjugation a generation 3-cycle at every point, or only at order 5?

B1946 found, at the 24 points of order 5 and height 30 only, that S -> S~ acts on each sector's left-singular basis as a
permutation of the generations: a 3-cycle at every up point and at 22 of 24 down points (a transposition at 2).  So the
charge-consistent readings (S~ up with S down, or the mirror) derange the cusp mixing there.  If the 3-cycle holds at
every point of every order, the charge rule forces a permuted mixing on the whole family of frame C, high in the cusp;
if it is special to order 5, the menu of points could be reduced by principle to where it fails.

Frame C's own code (B1945's split, B1946's unitary), x = 0.13, unchanged.  Points (i/n, j/n) != (0, 0) for
n in ORDERS; heights 30 and 60.

EXPECTATIONS, written before the first run (main, 2026-11-19):
 X1  at height 30, |U(S)^H U(S~)| is a 0/1 pattern (to 1e-6) at every non-degenerate point of every order, in both
     sectors; prior 0.6.
 X2  among those patterns the 3-cycles are the majority at every order, in both sectors; prior 0.5.
 X3  the charge-consistent pairs (S~, S) and (S, S~) are deranged (smallest diagonal |V| < 0.1) at every non-degenerate
     point at height 30; prior 0.6.
 X4  (S, S) is aligned (smallest diagonal |V| >= 0.9) at every non-degenerate point at height 30; prior 0.5.
 X5  heights 30 and 60 give the same classification at every point; prior 0.8.
A point is DEGENERATE when a sector's coupling, for either reading, has a singular value below 10^-(dps - 5) of its largest,
dps the working precision frame C's code sets (30 + 2y digits): below that the singular basis is not fixed.  Such points
are counted and set aside, not classified.
AMENDED 2026-11-19 before the second run: the first run set every point aside (all 295, order 5's 24 included, which
B1946 classifies cleanly) because its screen was 1e-30, which the frame's natural hierarchy at height 30 (about 1e-65)
crosses.  The run is kept as conjugation_cycle_run_VOID_threshold_bug.txt.  The expectations X1 to X5 are unchanged.
Control: order 5 must have no degenerate point.
    python3 -B conjugation_cycle.py > conjugation_cycle_run.txt"""
import sys, pathlib
from fractions import Fraction as Fr
from collections import Counter
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
ORDERS = (2, 3, 4, 5, 6, 7, 8, 10)
PERMS = {
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)): "identity",
    ((0, 1, 0), (0, 0, 1), (1, 0, 0)): "3-cycle", ((0, 0, 1), (1, 0, 0), (0, 1, 0)): "3-cycle",
}


def kind(W):
    A = [[float(abs(W[r, c])) for c in range(3)] for r in range(3)]
    if max(min(abs(a - 1), abs(a)) for row in A for a in row) > 1e-6:
        return "not a 0/1 pattern"
    P = tuple(tuple(int(round(a)) for a in row) for row in A)
    return PERMS.get(P, "transposition")


def degenerate(Y):
    s = sorted(mp.svd_c(Y, compute_uv=False), key=lambda v: float(v))
    return s[0] < mp.mpf(10) ** (-(mp.mp.dps - 5)) * s[2]


def classify(y, n):
    out = {"deg": 0, "up": Counter(), "down": Counter(), "mixed_deranged": 0, "mixed_not": 0, "SS_aligned": 0, "SS_not": 0, "pts": {}}
    for i in range(n):
        for j in range(n):
            if (i, j) == (0, 0): continue
            a, b = Fr(i, n), Fr(j, n)
            Y = {sec: DL.parts("0.13", y, a, b, sec)[2] for sec in ("up", "down")}
            if any(degenerate(Y[sec][r]) for sec in ("up", "down") for r in ("S", "St")):
                out["deg"] += 1; out["pts"][(i, j)] = "degenerate"; continue
            U = {(sec, r): CM.U_of(Y[sec][r]) for sec in ("up", "down") for r in ("S", "St")}
            ks = []
            for sec in ("up", "down"):
                k = kind(U[(sec, "S")].H * U[(sec, "St")]); out[sec][k] += 1; ks.append(k)
            dmix = min(min(float(abs((U[("up", ru)].H * U[("down", rd)])[k, k])) for k in range(3)) for ru, rd in (("St", "S"), ("S", "St")))
            dss = min(float(abs((U[("up", "S")].H * U[("down", "S")])[k, k])) for k in range(3))
            out["mixed_deranged" if dmix < 0.1 else "mixed_not"] += 1
            out["SS_aligned" if dss >= 0.9 else "SS_not"] += 1
            out["pts"][(i, j)] = (ks[0], ks[1], dmix < 0.1, dss >= 0.9)
    return out


if __name__ == "__main__":
    res = {}
    for y in (30.0, 60.0):
        for n in ORDERS:
            r = classify(y, n); res[(y, n)] = r
            print("height %4.1f  order %2d: %3d points, %2d degenerate; up %s; down %s; charge-consistent pairs deranged at %d, not at %d; (S, S) aligned at %d, not at %d" % (
                y, n, n * n - 1, r["deg"], dict(r["up"]), dict(r["down"]), r["mixed_deranged"], r["mixed_not"], r["SS_aligned"], r["SS_not"]))
    same = sum(res[(30.0, n)]["pts"][p] == res[(60.0, n)]["pts"][p] for n in ORDERS for p in res[(30.0, n)]["pts"])
    tot = sum(len(res[(30.0, n)]["pts"]) for n in ORDERS)
    print("heights 30 and 60 classify alike at %d of %d points" % (same, tot))
    for n in ORDERS:
        odd = [(p, v) for p, v in sorted(res[(30.0, n)]["pts"].items()) if v != "degenerate" and (not v[2] or not v[3] or "not a 0/1" in v[0] + v[1])]
        if odd: print("order %d, height 30, points off the pattern: %s" % (n, odd[:12]))
