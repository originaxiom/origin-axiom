"""CLOSING AN OBJECTION TO ADDENDUM 4: B641 grades Re(A/zeta), and this arc dropped the /zeta.

The objection is real and had to be answered, not waved at. B641's tone is Re(A/zeta) with
zeta = sqrt(det M|sector) (b641_verify.py: `Modd = -M; d = det(Modd); zeta = sqrt(d);
vals.append(mp.re(A/zeta))`). Since |zeta| = 1, A/zeta = A*conj(zeta), so the graded form is
Sym(Re(conj(zeta) B)) -- a DIFFERENT quadratic form from Sym(Re B), which is what addenda 2-4 used.
A phase rotation changes a real part, so the gcd(m,15) law and the C6 containment could both have
been artifacts of the missing normalisation.

THEY ARE NOT, and the reason is an identity rather than a coincidence: zeta = 1 on every metallic
word, so B641's twist is the IDENTITY there.

    det(R^m L^m) = det(T)^m . det(S^-1 T^-1 S)^m = det(T)^m . det(T)^-m = 1   for every m,
    and this holds on every invariant subspace, since restrictions multiply the same way.
    det(C|even) = det(I_4) = 1        det(C|odd) = det(-I_2) = (-1)^2 = 1
    => det((C R^m L^m)|sector) = 1    => zeta = sqrt(1) = 1.

B641 needed the twist because it ranged over all 360 group elements, where det is a general root of
unity. On the 15 metallic words it is vacuous. Verified exactly below, both ways.
"""
import importlib.util, os, math
import sympy as sp
from sympy import Rational as Q

HERE = os.path.dirname(os.path.abspath(__file__))
sp2 = importlib.util.spec_from_file_location("exact60", os.path.join(HERE, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(X)
S, T, W, red, conj, mmul = X.S, X.T, X.W, X.red, X.conj, X.mmul
N = 6; ix = {w: i for i, w in enumerate(W)}; I6 = sp.eye(N)
def cmat(A): return sp.Matrix(A.rows, A.cols, lambda i, j: conj(A[i, j]))
C = sp.zeros(N, N)
for i, w in enumerate(W): C[ix[(w[1], w[0])], i] = 1
Cm = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
R = T; L = mmul(mmul(cmat(S), cmat(T)), S)
def mpow(A, k):
    P = I6
    for _ in range(k): P = mmul(P, A)
    return P

# (a) the algebraic reason: det(T) . det(L) = 1 exactly
dT = red(sp.expand(T.det()))
dL = red(sp.expand(L.det()))
prod = red(sp.expand(dT * dL))
print("=" * 76)
print("(a) THE IDENTITY:  det(T) . det(L) = 1   =>   det(R^m L^m) = 1 for every m")
print("=" * 76)
print(f"  det(T)          = {sp.sstr(dT)}")
print(f"  det(L)          = {sp.sstr(dL)}")
print(f"  det(T).det(L)   = {sp.sstr(sp.simplify(prod))}")
assert sp.simplify(prod - 1) == 0, "det(T).det(L) must be exactly 1"
print("  [PASS] exactly 1, so det(R^m L^m) = det(T)^m det(L)^m = 1 for every m")

Bev = sp.zeros(N, 4)
Bev[ix[(0,0)],0] = 1; Bev[ix[(1,1)],1] = 1
Bev[ix[(0,1)],2] = Bev[ix[(1,0)],2] = 1
Bev[ix[(0,2)],3] = Bev[ix[(2,0)],3] = 1
Bod = sp.zeros(N, 2)
Bod[ix[(0,1)],0], Bod[ix[(1,0)],0] = 1, -1
Bod[ix[(0,2)],1], Bod[ix[(2,0)],1] = 1, -1
print()
print("  det(C|even) = det(I_4) = 1 ;  det(C|odd) = det(-I_2) = +1  (C = +1 on even, -1 on odd)")
assert Cm * Bev == Bev and Cm * Bod == -Bod

# (b) the restricted determinant, computed exactly for every m on both sectors
def restrict(M6, B):
    """exact restriction: B has one weight per column with a 0/1 (or +-1) pattern, so solve B X = M6 B"""
    rows = [next(i for i in range(N) if B[i, j] != 0) for j in range(B.cols)]
    Mb = sp.Matrix(N, B.cols, lambda i, j: red(sp.expand(sum(M6[i, t] * B[t, j] for t in range(N)))))
    Xm = sp.Matrix(B.cols, B.cols, lambda a, b: red(sp.expand(Mb[rows[a], b] * Q(1, B[rows[a], a]))))
    # confirm the restriction really is a restriction
    lhs = Mb
    rhs = sp.Matrix(N, B.cols, lambda i, j: red(sp.expand(sum(B[i, t] * Xm[t, j] for t in range(B.cols)))))
    assert sp.simplify(lhs - rhs) == sp.zeros(N, B.cols), "not an invariant subspace"
    return Xm

print()
print("=" * 76)
print("(b) det((C R^m L^m)|sector), exactly, for all 15 words")
print("=" * 76)
bad = []
for m in range(1, 16):
    Wd = mmul(Cm, mmul(mpow(R, m), mpow(L, m)))
    for name, B in (("even", Bev), ("odd", Bod)):
        d = red(sp.expand(restrict(Wd, B).det()))
        if sp.simplify(d - 1) != 0: bad.append((m, name, d))
    print(f"  m={m:2d}: det|even = 1 ?  det|odd = 1 ?  both -> {'OK' if not any(b[0]==m for b in bad) else 'FAIL'}")
assert not bad, bad
print()
print("  [PASS] det = 1 EXACTLY on both sectors for all 15 metallic words")
print("  => zeta = sqrt(1) = 1, so B641's /zeta twist is the IDENTITY on the metallic words,")
print("     and Sym(Re(conj(zeta) B)) = Sym(Re B). Addenda 2-4's quantity IS B641's quantity here.")
print("     The objection is CLOSED BY AN IDENTITY, not by a numerical coincidence.")
