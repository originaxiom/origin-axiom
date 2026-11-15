"""B1945 section 3c: frame C's cusp mixing at every point of exact order N (10 or 15, P-845's two levels), both reading pairs
(main, 2026-11-15; data-free). Usage: python3 levels_mixing.py <N> <Im tau>"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import determinant_law as DL, cusp_mixing as CM
from fractions import Fraction as Fr
from math import gcd
from collections import Counter
mp = DL.mp
def points(N):
    return [(Fr(i, N), Fr(j, N)) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N]


if __name__ == "__main__":
  N = int(sys.argv[1]); y = float(sys.argv[2])
  pts = points(N)
  pats = Counter(); v33 = []
  for a, b in pts:
    _, _, Yu, *_ = DL.parts("0.13", y, a, b, "up"); _, _, Yd, *_ = DL.parts("0.13", y, a, b, "down")
    for ru, rd in (("St", "S"), ("S", "St")):
        V = CM.U_of(Yu[ru]).H * CM.U_of(Yd[rd]); A = [[float(abs(V[r, c])) for c in range(3)] for r in range(3)]
        v33.append(A[2][2]); pats[(ru, rd, tuple(tuple(round(v, 1) for v in row) for row in A))] += 1
  print("order %d: %d points of exact order; |V_33| at height %s: min %.2e, max %.2e" % (N, len(pts), y, min(v33), max(v33)))
  for k, n in sorted(pats.items(), key=lambda t: -t[1])[:12]: print("  %3d x %s" % (n, k))
