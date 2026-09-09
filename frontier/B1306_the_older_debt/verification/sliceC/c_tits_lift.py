"""C7 -- fc R66: the Tits lift of w_3 (the seat's word of length 24 in the simple reflections of E6, Bourbaki labels) in main's own exact e6 (B351):
n_i = exp(ad e_i) exp(ad e_{-i}) exp(ad e_i) as exact 78 x 78 matrices; N = n_6 n_2 n_4 ... ; targets: N^3 = I (order 3) and eigenvalue multiplicities
(24, 27, 27) for (1, omega, omega-bar)."""
import sys, json, time
from fractions import Fraction as Fr
sys.path.insert(0, "<repo>/frontier/B351_exact_e6_chevalley")
import exact_e6 as X
import sympy as sp
DIM = X.DIM; RIDX = X.RIDX
def ad(idx):
    M = [[Fr(0)] * DIM for _ in range(DIM)]
    for j in range(DIM):
        for kk, c in X.BRACKET[(idx, j)].items(): M[kk][j] += c
    return M
def mm(A, B):
    n = len(A); Bt = list(zip(*B)); return [[sum(a * b for a, b in zip(row, col)) for col in Bt] for row in A]
def madd(A, B): return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]
def mscale(A, c): return [[a * c for a in r] for r in A]
I = [[Fr(int(i == j)) for j in range(DIM)] for i in range(DIM)]
def expo(N):
    N2 = mm(N, N); N3 = mm(N2, N); N4 = mm(N3, N); assert all(x == 0 for r in N4 for x in r), "ad e not nilpotent of degree <= 4"
    return madd(madd(madd(I, N), mscale(N2, Fr(1, 2))), mscale(N3, Fr(1, 6)))
t0 = time.time(); n = {}
for i in range(6):
    a = tuple(1 if kk == i else 0 for kk in range(6)); e = 6 + RIDX[a]; f = 6 + RIDX[tuple(-x for x in a)]
    Ee, Ef = expo(ad(e)), expo(ad(f)); n[i + 1] = mm(mm(Ee, Ef), Ee)
print(f"lifts of the six simple reflections built [{time.time()-t0:.0f}s]", flush=True)
word = [6, 2, 4, 5, 3, 4, 1, 3, 2, 4, 5, 6, 2, 4, 5, 3, 4, 1, 3, 2, 4, 5, 3, 4]
N = I
for s in word: N = mm(N, n[s])
print(f"word of length {len(word)} multiplied [{time.time()-t0:.0f}s]", flush=True)
N2 = mm(N, N); N3 = mm(N2, N); order3 = (N3 == I); order6 = (mm(N3, N3) == I)
Ms = sp.Matrix(DIM, DIM, lambda i, j: sp.Rational(N[i][j].numerator, N[i][j].denominator))
r1 = (Ms - sp.eye(DIM)).rank(); m1 = DIM - r1
Q = sp.Matrix(DIM, DIM, lambda i, j: sp.Rational(N2[i][j].numerator, N2[i][j].denominator)) + Ms + sp.eye(DIM); mw = DIM - Q.rank()
print("N^3 = I:", order3, " N^6 = I:", order6, " multiplicity of eigenvalue 1:", m1, " dim ker(N^2+N+1) (omega + omega-bar):", mw, " (seat: 24 and 27+27)")
# a control: each lift acts on the Cartan as the reflection and has order dividing 4 there
ctrl = all(mm(mm(n[i], n[i]), mm(n[i], n[i])) == I for i in (1, 2))
ok = order3 and m1 == 24 and mw == 54
json.dump(dict(order3=order3, order6=order6, mult_1=m1, mult_omega_pair=mw, control_n_i_order4=ctrl, ok=ok), open("c_tits_lift.json", "w"), indent=1)
print("C7:", "PASS" if ok else "FAIL", f"[{time.time()-t0:.0f}s]")
