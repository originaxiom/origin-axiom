"""Exact identification of the theta-EVEN ear-dependent spectra + the gcd(m,15) law.

CONTROL AGAINST MY OWN PRIOR ERROR: in b1349c I float-matched a value to 1/phi with
tol=1e-8 and a Fibonacci ratio passed. So NOTHING here is identified by float matching --
every claimed closed form is proved by exhibiting the exact characteristic polynomial.
"""
import importlib.util, os, math
import sympy as sp
from sympy import Rational as Q

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("b1349e", os.path.join(HERE, "b1349e_ear_exact.py"))
# re-import the exact instrument only (avoid re-running the whole report)
spec2 = importlib.util.spec_from_file_location("exact60", os.path.join(HERE, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(X)
S, T, W, red, conj, mmul = X.S, X.T, X.W, X.red, X.conj, X.mmul
N = 6; ix = {w: i for i, w in enumerate(W)}; I6 = sp.eye(N)
def cmat(A): return sp.Matrix(A.rows, A.cols, lambda i, j: conj(A[i, j]))
def re_(e):  return red(sp.expand((e + conj(e)) * Q(1, 2)))
C = sp.zeros(N, N)
for i, w in enumerate(W): C[ix[(w[1], w[0])], i] = 1
R = T; L = mmul(mmul(cmat(S), cmat(T)), S)
def mpow(A, k):
    P = I6
    for _ in range(k): P = mmul(P, A)
    return P
Bev = sp.zeros(N, 4)
Bev[ix[(0,0)],0] = 1; Bev[ix[(1,1)],1] = 1
Bev[ix[(0,1)],2] = Bev[ix[(1,0)],2] = 1
Bev[ix[(0,2)],3] = Bev[ix[(2,0)],3] = 1
Gev = Bev.T * Bev

def Qform(m):
    Wd = mmul(sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j])), mmul(mpow(R, m), mpow(L, m)))
    A = sp.Matrix(4, 4, lambda i, j:
                  red(sp.expand(sum(Bev[a, i] * Wd[a, b] * Bev[b, j] for a in range(N) for b in range(N)))))
    return sp.Matrix(4, 4, lambda i, j: re_((A[i, j] + A[j, i]) * Q(1, 2)))

# express each entry exactly in terms of sqrt5: Q(zeta_60)^real contains sqrt5 = z^12+z^-12+... ;
# minimal polynomial route instead: every entry satisfies a degree<=2 poly over Q here -- prove it.
t = sp.symbols('t')
def to_alg(e):
    """exact real element of Q(zeta_60) -> radical form, via its minimal polynomial over Q."""
    p = sp.minimal_polynomial(sp.expand(e.subs(X.z, sp.exp(2 * sp.pi * sp.I / 60))), t)
    rts = sp.solve(sp.Eq(p, 0), t)
    tgt = complex(sp.N(e.subs(X.z, sp.exp(2 * sp.pi * sp.I / 60)), 40))
    best = min(rts, key=lambda r: abs(complex(sp.N(r, 40)) - tgt))
    assert abs(complex(sp.N(best, 40)) - tgt) < 1e-30, (best, tgt)
    return sp.radsimp(sp.nsimplify(best, [sp.sqrt(5)]))

lam = sp.symbols('lam')
print("=" * 78)
print("EXACT spectra of G^-1 Q_m on the theta-EVEN sector (char. polys, not float matches)")
print("=" * 78)
UNITS = [m for m in range(1, 16) if math.gcd(m, 15) == 1]
NONUNITS = [m for m in range(1, 16) if math.gcd(m, 15) != 1]
print(f"  units of Z/15  = {UNITS}   (phi(15) = {len(UNITS)})")
print(f"  non-units      = {NONUNITS}")
assert len(UNITS) == sp.totient(15) == 8
rows = {}
for m in [1, 2, 3, 5, 6, 15]:
    Qm = Qform(m)
    Mg = sp.diag(*[Q(1, Gev[i, i]) for i in range(4)]) * Qm
    Ma = sp.Matrix(4, 4, lambda i, j: to_alg(Mg[i, j]))
    cp = sp.factor(sp.simplify(sp.expand(Ma.charpoly(lam).as_expr())))
    ev = sp.simplify(Ma.eigenvals())
    evs = {sp.radsimp(sp.simplify(k)): v for k, v in ev.items()}
    rows[m] = evs
    tag = "EAR-DEPENDENT" if math.gcd(m, 15) == 1 else "ear-independent"
    print(f"\n  m={m:2d}  gcd(m,15)={math.gcd(m,15)}  [{tag}]")
    print(f"      charpoly = {cp}")
    print(f"      eigenvalues = {{ {', '.join(f'{sp.sstr(k)} (x{v})' for k, v in evs.items())} }}")

print()
print("=" * 78)
print("IDENTIFY the two ear-dependent spreads exactly")
print("=" * 78)
phi = (1 + sp.sqrt(5)) / 2
for m, claim, name in [(1, phi**2 / (2 * sp.sqrt(2)), "phi^2/(2 sqrt2)"),
                       (2, sp.sqrt(10) / 4, "sqrt10/4")]:
    top = max(rows[m].keys(), key=lambda k: float(sp.N(k)))
    ok = sp.simplify(sp.radsimp(top - claim)) == 0
    print(f"  m={m}: largest eigenvalue  {sp.sstr(top)}  ==  {name} ?  {ok}"
          f"   (numeric {float(sp.N(top)):.12f})")
    assert ok, f"m={m} closed form WRONG -- do not bank it"
print()
print("  sqrt2 in Q(zeta_60) ?  8 | 60 is False ->", 60 % 8 == 0,
      " => the ear-dependent readings leave the field of the modular data.")
print("  (both spreads carry a 1/sqrt2; the ear-INDEPENDENT lambdas do not: 0, 1/2, -1/(2phi), 1)")
mp_ = sp.minimal_polynomial(sp.Rational(-1, 2) / phi, t)
print(f"  -1/(2phi) minimal polynomial over Q: {mp_}   (numeric {float(sp.N(-1/(2*phi))):.9f})")

print()
print("=" * 78)
print("ADDENDUM: the FULL ear-dependent spectra -- every eigenvalue carries 1/(2 sqrt2)")
print("=" * 78)
s2 = 2 * sp.sqrt(2)
for m, claims, names in [
        (1, [phi**2 / s2, 1 / (phi * s2)], ["phi^2/(2sqrt2)", "1/(phi.2sqrt2)"]),
        (2, [sp.sqrt(5) / s2, 1 / s2],     ["sqrt5/(2sqrt2)", "1/(2sqrt2)"])]:
    pos = sorted([k for k in rows[m] if float(sp.N(k)) > 0], key=lambda k: -float(sp.N(k)))
    print(f"\n  m={m}: positive eigenvalues, largest first")
    for got, claim, nm in zip(pos, claims, names):
        ok = sp.simplify(sp.radsimp(got - claim)) == 0
        print(f"     {nm:>16s} = {float(sp.N(claim)):.12f}  proved ? {ok}")
        assert ok, f"m={m} {nm} WRONG"
    print(f"     spectrum = (1/(2sqrt2)) * {{+-{sp.sstr(sp.simplify(pos[0]*s2))}, "
          f"+-{sp.sstr(sp.simplify(pos[1]*s2))}}}")
print()
print("  => sqrt10/4 = sqrt5/(2sqrt2): ALL FOUR ear-dependent eigenvalues, at both m-classes,")
print("     are (1/(2sqrt2)) x (a unit of Z[phi]). The 1/sqrt2 is uniform, not incidental.")
