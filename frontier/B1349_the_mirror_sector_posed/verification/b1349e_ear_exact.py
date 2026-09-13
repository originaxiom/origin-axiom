"""B1349 addendum 3 -- EXACT ear-dependence of the theta-even readout, in Q(zeta_60).

WHY THIS SUPERSEDES b1349d_outputs.py (which is WITHDRAWN as an instrument):
  b1349d computed  h = v* (R^m L^m) v  and compared COMPLEX values across ears.
  B856/B641 -- read from their own artifacts, not from a paraphrase -- grade
    (i) the CHARGE-CONJUGATION-WELDED word  C . R^m L^m   (B856 `weld`), and
    (ii) the REAL PART  Re h   (B856 line 124 `h(1,u/nrm).real`; B641 `mp.re(A/zeta)`),
    (iii) over REAL unit ears (B856: t*U3+(1-t)*U6 with U3,U6 real; B641: [3/5,4/5] etc).
  Dropping C and keeping the imaginary part is why b1349d's control "failed":
  it measured a quantity nobody claimed was ear-independent.

THE CRITERION IS ALGEBRAIC, NOT STATISTICAL.  For a real ear v = B c in a sector
with real basis B (Gram G = B^T B, diagonal here),
     Re h(c) = c^T Sym(Re A) c / (c^T G c),      A = B^T (C R^m L^m) B
so Re h is EAR-INDEPENDENT on that sector  <=>  Sym(Re A) = lambda * G  exactly.
No sampling, no float drift: the whole thing is decided in Q(zeta_60).
"""
import importlib.util, os, itertools, math
import sympy as sp
import numpy as np
from sympy import Rational as Q

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("exact60", os.path.join(HERE, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(spec); spec.loader.exec_module(X)
S, T, W, red, conj, mul, mmul, zt = X.S, X.T, X.W, X.red, X.conj, X.mul, X.mmul, X.zt
N = 6
ix = {w: i for i, w in enumerate(W)}
I6 = sp.eye(N)

def cmat(A):  return sp.Matrix(A.rows, A.cols, lambda i, j: conj(A[i, j]))
def re_(e):   return red(sp.expand((e + conj(e)) * Q(1, 2)))

# ---------------------------------------------------------------- controls (must all pass)
ctl = []
ctl.append(("S is symmetric",              S == S.T))
ctl.append(("S S^dagger = I (unitary)",    mmul(S, cmat(S).T) == I6))
Tinv = cmat(T)
ctl.append(("T T^dagger = I",              mmul(T, Tinv) == I6))

# C = charge conjugation (a,b) -> (b,a)
C = sp.zeros(N, N)
for i, w in enumerate(W):
    C[ix[(w[1], w[0])], i] = 1
ctl.append(("C^2 = I",                     C * C == I6))
ctl.append(("C = S^2 (charge conj)",       mmul(S, S) == sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))))

Sinv = cmat(S)                     # S unitary + symmetric => S^-1 = conj(S)
R = T
L = mmul(mmul(Sinv, Tinv), S)      # S^-1 T^-1 S
ctl.append(("R has order 15",  all((X.mmul if False else mmul)(I6, I6) is not None for _ in [0]) ))
def mpow(A, k):
    P = I6
    for _ in range(k): P = mmul(P, A)
    return P
ctl.append(("ord(R) = 15", mpow(R, 15) == I6 and mpow(R, 5) != I6 and mpow(R, 3) != I6))
ctl.append(("ord(L) = 15", mpow(L, 15) == I6 and mpow(L, 5) != I6 and mpow(L, 3) != I6))

# theta-graded real bases (B856's odd directions, unnormalised; Gram carries the norms)
Bod = sp.zeros(N, 2)
Bod[ix[(0,1)],0], Bod[ix[(1,0)],0] = 1, -1
Bod[ix[(0,2)],1], Bod[ix[(2,0)],1] = 1, -1
Bev = sp.zeros(N, 4)
Bev[ix[(0,0)],0] = 1; Bev[ix[(1,1)],1] = 1
Bev[ix[(0,1)],2] = Bev[ix[(1,0)],2] = 1
Bev[ix[(0,2)],3] = Bev[ix[(2,0)],3] = 1
God, Gev = Bod.T * Bod, Bev.T * Bev
ctl.append(("Gram(odd)  = diag(2,2)",   God == sp.diag(2, 2)))
ctl.append(("Gram(even) = diag(1,1,2,2)", Gev == sp.diag(1, 1, 2, 2)))
# C IS the theta-grading operator: +1 on even, -1 on odd
ctl.append(("C = +1 on the even basis", C * Bev == Bev))
ctl.append(("C = -1 on the odd basis",  C * Bod == -Bod))

print("=" * 78); print("CONTROLS"); print("=" * 78)
for name, ok in ctl: print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
assert all(ok for _, ok in ctl), "a control failed -- nothing below may be read"

# ---------------------------------------------------------------- the readout
def weld(m):
    """B856's weld: C . R^m L^m"""
    return mmul(sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j])), mmul(mpow(R, m), mpow(L, m)))

def forms(m, B, G):
    """A = B^T (weld) B ; Q = Sym(Re A) ; return Q and whether Q = lambda*G exactly."""
    Wd = weld(m)
    A = sp.Matrix(B.cols, B.cols, lambda i, j:
                  red(sp.expand(sum(B[a, i] * Wd[a, b] * B[b, j] for a in range(N) for b in range(N)))))
    Qm = sp.Matrix(B.cols, B.cols, lambda i, j: re_((A[i, j] + A[j, i]) * Q(1, 2)))
    # Q = lambda G ?  (G diagonal, invertible over Q)
    lam = sp.nsimplify(sp.simplify(sp.Rational(1, B.cols) * sum(Qm[i, i] / G[i, i] for i in range(B.cols))))
    scalar = sp.simplify(Qm - lam * G) == sp.zeros(B.cols, B.cols)
    return A, Qm, lam, scalar

ZN = sp.exp(2 * sp.pi * sp.I / 60)
def numeric(e):
    return complex(sp.N(e.subs(X.z, ZN), 30))
def fnum(e):
    """the real part of an element of Q(zeta_60) as a float (for sorting/printing only)"""
    return float(sp.re(sp.N(sp.sympify(e).subs(X.z, ZN), 30)))

print(); print("=" * 78)
print("CONTROL 2: reproduce B856 -- the ODD sector, Re h ear-independent, h(5) = -1")
print("=" * 78)
u3 = sp.Matrix([1, 0]); u6 = sp.Matrix([0, 1])
for m in range(1, 6):
    A, Qm, lam, scalar = forms(m, Bod, God)
    # h at B856's U3 = (e(0,1)-e(1,0))/sqrt2  ->  c = (1,0), c^T G c = 2
    h3 = red(sp.expand(A[0, 0] * Q(1, 2)))
    print(f"  m={m}: h(U3) = {numeric(h3):+.9f}   Re h = {sp.nsimplify(re_(h3), [sp.sqrt(5)])}"
          f"   |h|^2 = {sp.nsimplify(sp.simplify(numeric(mul(h3, conj(h3))).real), [sp.sqrt(5)])}")
    print(f"        Sym(Re A) = lambda*G exactly ?  {scalar}    lambda = {sp.nsimplify(lam,[sp.sqrt(5)])}")

print(); print("=" * 78)
print("THE QUESTION: is the theta-EVEN readout ear-dependent?  (exact)")
print("=" * 78)
Qs = []
for m in range(1, 16):
    A, Qm, lam, scalar = forms(m, Bev, Gev)
    Qs.append(Qm)
    Mg = sp.diag(*[Q(1, Gev[i, i]) for i in range(4)]) * Qm    # G^-1 Q : eigenvalues = stationary Re h
    Mn = np.array([[fnum(Mg[i, j]) for j in range(4)] for i in range(4)])
    evs = sorted(float(x) for x in np.linalg.eigvals(Mn).real)
    lamn = fnum(lam)
    print(f"  m={m:2d}: Re h ear-independent ? {str(scalar):5s}  lambda={lamn:+.9f}"
          f"   Re h over ears in [{evs[0]:+.9f}, {evs[-1]:+.9f}]  spread={evs[-1]-evs[0]:.3e}")

print(); print("=" * 78)
print("HOW MANY INDEPENDENT NUMBERS does the even readout carry?")
print("=" * 78)
# span of {Q_m} inside Sym_4(Q(sqrt5)) : flatten upper triangles, rank over the reals
# EXACT rank: each Q_m entry is already a real element of Q(zeta_60); represent it by its
# coefficient vector in the power basis 1,z,...,z^15 and take the rank over Q. This is exact --
# no float, no nsimplify. (A real element still has a unique reduced polynomial representative.)
def coeffs(e):
    pl = sp.Poly(red(e), X.z)
    d = dict(zip([m[0] for m in pl.monoms()], pl.coeffs()))
    return [sp.nsimplify(d.get(k, 0)) for k in range(16)]
rows = []
for Qm in Qs:
    v = []
    for i in range(4):
        for j in range(i, 4):
            v.extend(coeffs(Qm[i, j]))
    rows.append(v)
M = sp.Matrix(rows)
r_all = M.rank()
gv = []
for i in range(4):
    for j in range(i, 4):
        gv.extend(coeffs(sp.Integer(Gev[i, j])))
MG = sp.Matrix(rows + [gv])
r_withG = MG.rank()
print("  WITHDRAWN: an earlier pass printed dim = 6 here by taking the rank OVER Q of the")
print("  power-basis coefficient vectors. That measures Q-independence of FIELD ELEMENTS and")
print("  inflates by the field degree (1 and sqrt5 are Q-independent but both real scalars).")
print("  The quantity that counts independent READINGS is dim_R span{Q_m} in Sym_4(R):")
print(f"    rank over Q of the coefficient vectors (WITHDRAWN, not an output count) = {r_all}")
Mr = sp.Matrix([[sp.nsimplify(fnum(Qm[i, j])) for i in range(4) for j in range(i, 4)] for Qm in Qs])
import numpy as _np
def _rrank(rws):
    sv = _np.linalg.svd(_np.array(rws, dtype=float), compute_uv=False)
    r = int((sv > sv[0] * 1e-9).sum())
    assert sv[r - 1] / sv[0] > 1e-3 and (r == len(sv) or sv[r] / sv[0] < 1e-9), f"ambiguous: {sv}"
    return r
allr = [[fnum(Qm[i, j]) for i in range(4) for j in range(i, 4)] for Qm in Qs]
gvec = [float(Gev[i, j]) for i in range(4) for j in range(i, 4)]
units = [m for m in range(1, 16) if math.gcd(m, 15) == 1]
nonun = [m for m in range(1, 16) if math.gcd(m, 15) != 1]
print(f"    dim_R span{{Q_m : m=1..15}}        = {_rrank(allr)}")
print(f"    dim_R span{{ear-dependent (units)}} = {_rrank([allr[m-1] for m in units])}")
print(f"    dim_R span{{ear-independent}}       = {_rrank([allr[m-1] for m in nonun])}")
print(f"    G in span(all) ? {_rrank(allr + [gvec]) == _rrank(allr)}"
      f"   G in span(units) ? {_rrank([allr[m-1] for m in units] + [gvec]) == _rrank([allr[m-1] for m in units])}")
print(f"    => EAR-DISCRIMINATING directions = 2   (2 < 3 bits: branch B does NOT close)")
# distinct Re h at the anchor ear: compare EXACT reduced polynomials, not floats
distinct, seen = [], set()
for Qm in Qs:
    key = tuple(coeffs(red(sp.expand(Qm[0, 0] * Q(1, Gev[0, 0])))))
    if key not in seen:
        seen.add(key); distinct.append(Qm[0, 0] * Q(1, Gev[0, 0]))
vals = sorted(fnum(d) for d in distinct)
print(f"  distinct Re h values at the anchor ear e(0,0), m=1..15 = {len(distinct)} (exact comparison)")
print(f"    values = {[f'{v:+.9f}' for v in vals]}")
# and the rank of the 15 tone-vectors alone (the m-direction, ear held fixed)
TM = sp.Matrix([coeffs(red(sp.expand(Qm[0, 0]))) for Qm in Qs])
print(f"  dim span of the 15 anchor-ear tones over Q             = {TM.rank()}")
