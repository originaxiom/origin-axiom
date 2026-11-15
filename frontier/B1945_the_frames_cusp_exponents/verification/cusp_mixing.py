"""B1945: frame C's mixing high in the cusp, point by point (main, 2026-11-15; data-free). At each of the 24 points the
full |V| = |U_u^H U_d| (columns ascending, as B1940's frame_mp) for both reading pairs; agy-exp's diagnosis (relayed
by the author, harvest row 1830) recomputed on main's code: |V| a permutation with |V_33| -> 0.
Usage: python3 cusp_mixing.py <Im tau> <Re tau>"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import determinant_law as DL
from fractions import Fraction as Fr
from collections import Counter
mp = DL.mp
def U_of(Y):
    Uu, Sv, Vv = mp.svd_c(Y); order = sorted(range(3), key=lambda i: -Sv[i])
    return mp.matrix([[Uu[r, order[2 - c]] for c in range(3)] for r in range(3)])      # columns ascending, as frame_mp
if __name__ == "__main__":
    y = float(sys.argv[1]); x = sys.argv[2]
    pats = Counter(); worst33 = 0
    for i in range(5):
        for j in range(5):
            if (i, j) == (0, 0): continue
            a, b = Fr(i, 5), Fr(j, 5)
            _, _, Yu, *_ = DL.parts(x, y, a, b, "up"); _, _, Yd, *_ = DL.parts(x, y, a, b, "down")
            for ru, rd in (("St", "S"), ("S", "St")):
                V = U_of(Yu[ru]).H * U_of(Yd[rd]); A = [[float(abs(V[r, c])) for c in range(3)] for r in range(3)]
                worst33 = max(worst33, A[2][2])
                pats[(ru, rd, i, tuple(tuple(round(v, 2) for v in row) for row in A))] += 1
    for k, n in sorted(pats.items()): print(n, "x", k)
    print("y = %s: largest |V_33| over the 24 points and both readings: %.2e" % (y, worst33))
