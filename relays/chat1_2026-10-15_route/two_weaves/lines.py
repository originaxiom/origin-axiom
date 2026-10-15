# the flat torsion lines a signed thread eps*gamma fixes: coker(eps*gamma - I) = Z/d1 + Z/d2 (Smith form); chat1, 2026-10-15
import numpy as np, math, json
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()
L = Matrix([[1,0],[1,1]]); R = Matrix([[1,1],[0,1]])
def mat(w):
    M = Matrix.eye(2)
    for ch in w: M = M * (L if ch == "L" else R)
    return M
import pathlib
adm = json.load(open(pathlib.Path(__file__).resolve().parents[2] / "chat1_2026-10-14_step3" / "lift_cells.json"))["per thread"]
rows = []
for w in (x for x in lyndon(8) if len(x) >= 2):
    M = mat(w); t = M.trace()
    a = any(adm[w][c].get("admitted") for c in ("C3/E4","C3/THETA2","C3/ORTH","C2/E4"))   # LIFT's admission, sign-blind (the thread frame's geodesic)
    for eps in (1, -1):
        S = smith_normal_form(eps * M - Matrix.eye(2), domain=ZZ)
        d1, d2 = abs(S[0,0]), abs(S[1,1])
        # fixed points of eps*gamma on (Q/Z)^2 of exact order N exist iff N | d2 (the larger invariant factor)
        Ns = [N for N in range(2, 13) if d2 % N == 0]
        rows.append((("+" if eps == 1 else "-") + w, int(t), int(d1), int(d2), Ns, a))
for r in rows: print(f"{r[0]:10s} t={r[1]:3d} coker(eps gamma - I)=Z/{r[2]}+Z/{r[3]}  line orders 2..12 fixed: {r[4]}  admitted(any rank-2 cell)={r[5]}")
allowed = {N: [r[0] for r in rows if N in r[4] and r[5]] for N in (5,7,8,9,10,11,12)}
print("admitted signed threads carrying a fixed line of order N in {5,7,...,12}:", allowed)
g = Matrix([[2,1],[1,1]])     # = R.L, the root in the RL marking (this script's mat('LR') is L.R = [[1,1],[1,2]])
for eps in (1, -1):
    fx = [(x, y) for x in range(5) for y in range(5) if (x, y) != (0, 0)
          and all(v % 5 == 0 for v in (eps * g - Matrix.eye(2)) * Matrix([x, y]))]
    print(f"the root in the RL marking, sign {eps:+d}: fixed points of order 5, (a, b)/5:", fx)
# the record's root +LR (here L.R = [[1,1],[1,2]] in this script's convention): lines closing exactly, and up to w -> -w, for every order N <= 40
gR = mat("LR")
for N in range(2, 41):
    pts = [(x, y) for x in range(N) for y in range(N) if (x, y) != (0, 0)]
    ex = [p for p in pts if all(v % N == 0 for v in (gR - Matrix.eye(2)) * Matrix(p))]
    cj = [p for p in pts if all(v % N == 0 for v in (gR + Matrix.eye(2)) * Matrix(p))]
    if ex or cj:
        print(f"+LR (L.R marking), N = {N}: closing exactly {len(ex)}, closing up to w -> -w {len(cj)}" + (f": {cj}" if N == 5 else " (the same four order-5 points, embedded)"))
