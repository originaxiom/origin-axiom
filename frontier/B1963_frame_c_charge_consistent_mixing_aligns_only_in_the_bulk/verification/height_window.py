"""B1963, part 2 (main, 2026-11-19; data-free): is there a height where a charge-consistent reading leaves the cusp mixing
aligned AND the couplings carry a hierarchy?

Frame C's code, unchanged.  Points: the 24 of order 5 and the 48 of order 7.  Column x = 0.13 (B1946's), heights
y in HEIGHTS; and the control tau = i (x = 0, y = 1), where S~ = S (B1946's addendum), so the charge-consistent pair
equals (S, S) there.
Per point and height: m_cc, the smallest diagonal |V| over the two charge-consistent pairs (the worse of the two), and
the hierarchy h = min over the two sectors of s_min/s_max (reading S for down, S~ for up; the record's practice).

EXPECTATIONS, written before the run (main, 2026-11-19):
 Y1  the control tau = i: m_cc equals (S, S)'s smallest diagonal at every point to 1e-20; prior 0.95.
 Y2  at every height >= 2, m_cc < 0.1 at every point (deranged); prior 0.6.
 Y3  no (point, height) has m_cc >= 0.9 and h <= 1e-2 together (no aligned charge-consistent mixing with a hierarchy of
     two orders); prior 0.7.
 Y4  where m_cc >= 0.9 at all, h > 0.1 (little hierarchy); prior 0.5.
A point whose coupling is degenerate at the working precision is set aside, as in conjugation_cycle.py.
    python3 -B height_window.py > height_window_run.txt"""
import sys, pathlib
from fractions import Fraction as Fr
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp
HEIGHTS = ("1.0", "1.2", "1.5", "2.0", "2.5", "3.0", "4.0", "6.0", "10.0")


def degenerate(Y):
    s = sorted(mp.svd_c(Y, compute_uv=False), key=lambda v: float(v))
    return s[0] < mp.mpf(10) ** (-(mp.mp.dps - 5)) * s[2]


def point(x, y, a, b):
    Y = {sec: DL.parts(x, float(y), a, b, sec)[2] for sec in ("up", "down")}
    if any(degenerate(Y[sec][r]) for sec in ("up", "down") for r in ("S", "St")): return None
    U = {(sec, r): CM.U_of(Y[sec][r]) for sec in ("up", "down") for r in ("S", "St")}
    dg = lambda V: min(float(abs(V[k, k])) for k in range(3))
    mcc = min(dg(U[("up", ru)].H * U[("down", rd)]) for ru, rd in (("St", "S"), ("S", "St")))
    mss = dg(U[("up", "S")].H * U[("down", "S")])
    sv = lambda M: sorted(float(v) for v in mp.svd_c(M, compute_uv=False))
    h = min(sv(Y["up"]["St"])[0] / sv(Y["up"]["St"])[2], sv(Y["down"]["S"])[0] / sv(Y["down"]["S"])[2])
    return mcc, mss, h


if __name__ == "__main__":
    pts = [(Fr(i, n), Fr(j, n)) for n in (5, 7) for i in range(n) for j in range(n) if (i, j) != (0, 0)]
    worst = 0.0
    for (a, b) in pts:
        r = point("0", "1.0", a, b)
        if r: worst = max(worst, abs(r[0] - r[1]))
    print("control tau = i: largest |m_cc - m_SS| over %d points: %.2e" % (len(pts), worst))
    both = []
    for y in HEIGHTS:
        rows = [(p, point("0.13", y, *p)) for p in pts]; rows = [(p, r) for p, r in rows if r]
        al = [(p, r) for p, r in rows if r[0] >= 0.9]; dr = [(p, r) for p, r in rows if r[0] < 0.1]
        hal = [r[2] for p, r in al]
        print("height %5s: %2d points; charge-consistent mixing aligned at %2d, deranged at %2d, partial at %2d; hierarchy h over all: min %.1e, median %.1e; over the aligned: %s" % (
            y, len(rows), len(al), len(dr), len(rows) - len(al) - len(dr), min(r[2] for p, r in rows), sorted(r[2] for p, r in rows)[len(rows) // 2],
            ("min %.1e" % min(hal)) if hal else "none"))
        both += [(y, p, r) for p, r in al if r[2] <= 1e-2]
    print("aligned charge-consistent mixing with a hierarchy of two orders (h <= 1e-2): %d cases %s" % (len(both), [(y, str(p[0]) + "," + str(p[1]), round(r[0], 3), "%.1e" % r[2]) for y, p, r in both[:10]]))
