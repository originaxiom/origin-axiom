"""B1963, part 3 (main, 2026-11-19; data-free): the height window of part 2 at other columns x = Re tau.

EXPECTATIONS, written before the run (main, 2026-11-19), after part 2 (whose window at x = 0.13 is: aligned
charge-consistent mixing only at height 1.0, hierarchy h >= 3.9e-3; deranged at every point from height 3):
 Z1  at x in {0, 0.25, 0.5}, no (point, height) with height >= 1.5 has m_cc >= 0.9; prior 0.6.
 Z2  at every column, every point is deranged (m_cc < 0.1) at heights 4 and 6; prior 0.7.
 Z3  over all columns and heights, no case has m_cc >= 0.9 and h <= 1e-3 (three orders); prior 0.7.
    python3 -B columns.py > columns_run.txt"""
import sys, pathlib
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import height_window as HW
if __name__ == "__main__":
    pts = [(Fr(i, n), Fr(j, n)) for n in (5, 7) for i in range(n) for j in range(n) if (i, j) != (0, 0)]
    both = []
    for x in ("0", "0.25", "0.5"):
        for y in ("1.0", "1.5", "2.0", "3.0", "4.0", "6.0"):
            rows = [(p, HW.point(x, y, *p)) for p in pts]; rows = [(p, r) for p, r in rows if r]
            al = [(p, r) for p, r in rows if r[0] >= 0.9]; dr = [r for p, r in rows if r[0] < 0.1]
            print("x %4s height %4s: %2d points; aligned %2d, deranged %2d, partial %2d; h min %.1e; over the aligned: %s" % (
                x, y, len(rows), len(al), len(dr), len(rows) - len(al) - len(dr), min(r[2] for p, r in rows), ("min %.1e" % min(r[2] for p, r in al)) if al else "none"))
            both += [(x, y, p, r) for p, r in al if r[2] <= 1e-3]
    print("aligned charge-consistent mixing with three orders of hierarchy (h <= 1e-3): %d cases %s" % (len(both), [(x, y, str(p[0]) + "," + str(p[1]), round(r[0], 3), "%.1e" % r[2]) for x, y, p, r in both[:10]]))
