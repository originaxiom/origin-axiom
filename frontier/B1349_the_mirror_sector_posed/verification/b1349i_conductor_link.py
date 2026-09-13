"""Are the three arithmetic cuts of the metallic family RELATED?  Addendum 2 left this OPEN.

B996/B997 cut the family R^m L^m by the METALLIC CONDUCTOR m^2+4 (B997: |SL(2,Z/N)| is a McKay
order for exactly N in {3,4,5}, and m^2+4 = 5 only at m = 1, so THE GOLDEN IS UNIQUE -- its
conductor 5 being PRIME makes its shadow the McKay group SL(2,Z/5) = 2I).
B1349 cuts it by gcd(m,15), 15 = ord(R) = ord(L) in the SU(3)_2 modular data.

TESTED HERE: on the ear-independent branch, does the forced value lambda leave Q exactly when the
conductor carries B997's golden prime 5?  Both sides depend only on m mod 15 (divisibility of
m^2+4 by 5 depends on m mod 5, which m mod 15 determines), so m = 1..15 is again complete.
"""
import importlib.util, os, math
import sympy as sp
from sympy import Rational as Q

HERE = os.path.dirname(os.path.abspath(__file__))
sp2 = importlib.util.spec_from_file_location("exact60", os.path.join(HERE, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(X)
S, T, W, red, conj, mmul, z = X.S, X.T, X.W, X.red, X.conj, X.mmul, X.z
N6 = 6; ix = {w: i for i, w in enumerate(W)}; I6 = sp.eye(N6)
def cmat(A): return sp.Matrix(A.rows, A.cols, lambda i, j: conj(A[i, j]))
def re_(e):  return red(sp.expand((e + conj(e)) * Q(1, 2)))
C = sp.zeros(N6, N6)
for i, w in enumerate(W): C[ix[(w[1], w[0])], i] = 1
Cm = sp.Matrix(N6, N6, lambda i, j: sp.Integer(C[i, j]))
R, L = T, mmul(mmul(cmat(S), cmat(T)), S)
def mpow(A, k):
    P = I6
    for _ in range(k): P = mmul(P, A)
    return P
Bev = sp.zeros(N6, 4)
Bev[ix[(0,0)],0] = 1; Bev[ix[(1,1)],1] = 1
Bev[ix[(0,1)],2] = Bev[ix[(1,0)],2] = 1
Bev[ix[(0,2)],3] = Bev[ix[(2,0)],3] = 1
Gev = Bev.T * Bev
ZN = sp.exp(2 * sp.pi * sp.I / 60)
t = sp.symbols('t')

def lam_of(m):
    Wd = mmul(Cm, mmul(mpow(R, m), mpow(L, m)))
    A = sp.Matrix(4, 4, lambda i, j:
                  red(sp.expand(sum(Bev[a, i] * Wd[a, b] * Bev[b, j] for a in range(N6) for b in range(N6)))))
    Qm = sp.Matrix(4, 4, lambda i, j: re_((A[i, j] + A[j, i]) * Q(1, 2)))
    lam = red(sp.expand(sp.Rational(1, 4) * sum(Qm[i, i] * Q(1, Gev[i, i]) for i in range(4))))
    scalar = sp.simplify(sp.expand(Qm - sp.Matrix(4, 4, lambda i, j: red(sp.expand(lam * Gev[i, j]))))) == sp.zeros(4, 4)
    return lam, scalar

print("=" * 78)
print("THE CORRESPONDENCE, on the ear-independent branch (gcd(m,15) > 1)")
print("=" * 78)
print(f"  {'m':>3} {'cond=m^2+4':>11} {'5|cond':>7} {'m mod 5':>8} {'lambda':>14} {'deg over Q':>11} {'irrational':>11}")
rows, ok = [], True
for m in range(1, 16):
    lam, scalar = lam_of(m)
    if not scalar:                      # branch B: no forced value
        continue
    cond = m * m + 4
    val = sp.N(sp.re(sp.N(lam.subs(X.z, ZN), 30)), 25)
    mp = sp.minimal_polynomial(sp.nsimplify(val, [sp.sqrt(5)], rational=False), t)
    deg = int(sp.degree(mp, t))
    irr = deg > 1
    div5 = (cond % 5 == 0)
    rows.append((m, cond, div5, irr))
    if irr != div5: ok = False
    print(f"  {m:3d} {cond:11d} {str(div5):>7} {m % 5:8d} {float(val):+14.9f} {deg:11d} {str(irr):>11}"
          f"  {'<-- MISMATCH' if irr != div5 else ''}")
print()
print("  LAW: on the ear-independent branch,  lambda is IRRATIONAL  <=>  5 | (m^2 + 4)")
print(f"  mismatches over the complete period: {0 if ok else 'SOME'}  ->  {'HOLDS' if ok else 'FAILS'}")
assert ok, "the correspondence fails -- do not bank it"

print()
print("=" * 78)
print("AND WHY: 5 | m^2+4  <=>  m = +-1 mod 5   (m^2 = 1 mod 5)")
print("=" * 78)
for r in range(5):
    ms = [m for m in range(1, 16) if m % 5 == r]
    div = sorted({(m * m + 4) % 5 for m in ms})
    print(f"  m = {r} mod 5: m in {ms}   (m^2+4) mod 5 in {div}")
assert all((m * m + 4) % 5 == 0 for m in range(1, 200) if m % 5 in (1, 4))
assert all((m * m + 4) % 5 != 0 for m in range(1, 200) if m % 5 not in (1, 4))
print("  verified for m = 1..199: 5 | m^2+4  iff  m = +-1 mod 5. Both sides of the law depend")
print("  only on m mod 5, hence on m mod 15, so the period-15 check above is COMPLETE.")

print()
print("=" * 78)
print("WHERE THE GOLDEN SITS -- the two roles of the same prime")
print("=" * 78)
print("  m=1: conductor 5, PRIME -> B997's condition: shadow IS SL(2,Z/5) = 2I = E8's McKay group,")
print("       and the golden is the UNIQUE metallic grammar with that property.")
print("  m=1 is also 1 mod 5, so 5 | its conductor -- but m=1 is a UNIT of Z/15, so it is on the")
print("       EAR-DEPENDENT branch and carries NO forced value at all.")
print("  The forced golden value -1/(2phi) appears only at m = 6, 9: conductors 40 and 85 --")
print("       divisible by 5 but NOT prime, so B997's uniqueness is untouched.")
print()
print("  => THE SAME PRIME 5 PLAYS TWO ROLES: PRIMALITY of m^2+4 singles out the golden grammar")
print("     (B997); DIVISIBILITY of m^2+4 by 5 decides whether the theta-even forced value is")
print("     golden or rational (here). The cuts are RELATED, and they are NOT the same cut.")
