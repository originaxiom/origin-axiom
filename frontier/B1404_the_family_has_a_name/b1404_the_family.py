"""
B1404 -- THE FAMILY HAS A NAME: verification on receipt of the Minsky relay.

Five independent checks, all exact where exactness is claimed:

  PART 1  the end invariants of m004's fibre group are phi and phi' EXACTLY
          (fixed points of the monodromy RL on the circle at infinity),
          with attracting/repelling settled by the derivative -- not asserted.
  PART 2  those two NUMBERS are marking-dependent; what is invariant is their
          SL(2,Z)-orbit.  Exhibited: a change of marking that moves the pair
          while fixing the manifold, and the exact continued-fraction
          certificate that every member of the orbit is NOBLE (tail all 1s).
  PART 3  the two kappas, exactly.  Fibre side kappa = -2 (Minsky's DEFINING
          condition for the family) from the corpus's OWN banked trace triple;
          meridian side kappa - 2 = omega^2 from SnapPy at high precision.
          And the decisive negative: m004's KNOT group is not in the family.
  PART 4  the banked triple sits on the MARKOV surface x^2+y^2+z^2 = xyz and
          is a fixed point of a length-2 Vieta composite -- i.e. the corpus
          had the family's defining equation under another name.
  PART 5  the absence audit of the corpus, with the homonym filter that a
          bare grep does not apply.

No float stands where an exact answer is claimed (E75, widened to inputs).
"""
import sympy as sp

OK = []
def check(name, cond, detail=""):
    OK.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))

# ---------------------------------------------------------------- PART 1
print("\n=== PART 1: the end invariants, exactly ===")

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
M = R * L                                  # [[2,1],[1,1]], the m004 monodromy
check("RL = [[2,1],[1,1]]", M == sp.Matrix([[2, 1], [1, 1]]), f"trace {sp.trace(M)}")
check("RL in SL(2,Z)", M.det() == 1)
check("RL is hyperbolic (|tr| > 2)", abs(sp.trace(M)) > 2)

z = sp.symbols('z')
a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
fixed_eq = sp.expand((a * z + b) - z * (c * z + d))          # = -(z^2 - z - 1)
roots = sorted(sp.solve(sp.Eq(fixed_eq, 0), z), key=lambda r: -sp.re(r))

phi     = (1 + sp.sqrt(5)) / 2
phi_bar = (1 - sp.sqrt(5)) / 2                                # the Galois conjugate
check("fixed-point equation is z^2 - z - 1 = 0",
      sp.simplify(fixed_eq + (z**2 - z - 1)) == 0)
check("the two fixed points are phi and phi'",
      sp.simplify(roots[0] - phi) == 0 and sp.simplify(roots[1] - phi_bar) == 0,
      f"{sp.nsimplify(roots[0])}, {sp.nsimplify(roots[1])}")
check("phi' is the GALOIS CONJUGATE of phi (sqrt5 -> -sqrt5)",
      sp.simplify(phi_bar - phi.subs(sp.sqrt(5), -sp.sqrt(5))) == 0)
check("phi' = -1/phi", sp.simplify(phi_bar + 1 / phi) == 0)

# attracting vs repelling is a DERIVATIVE fact, not a naming convention
def deriv(z0):
    return sp.simplify(1 / (c * z0 + d)**2)
dphi, dbar = deriv(phi), deriv(phi_bar)
check("phi is ATTRACTING  (|M'| < 1)", sp.simplify(dphi - 1 / phi**4) == 0 and dphi < 1,
      f"M'(phi) = 1/phi^4 = {sp.nsimplify(dphi)}")
check("phi' is REPELLING  (|M'| > 1)", sp.simplify(dbar - phi**4) == 0 and dbar > 1,
      f"M'(phi') = phi^4 = {sp.nsimplify(dbar)}")

lam = max(M.eigenvals().keys(), key=lambda e: sp.re(e))
check("dilatation of the monodromy = phi^2 = (3+sqrt5)/2",
      sp.simplify(lam - phi**2) == 0, f"{sp.nsimplify(lam)} = {float(lam):.12f}")
print(f"    phi  = {sp.N(phi, 15)}")
print(f"    phi' = {sp.N(phi_bar, 15)}")

# ---------------------------------------------------------------- PART 2
print("\n=== PART 2: the numbers are a MARKING; the orbit is the invariant ===")

def mob(P, x):
    return sp.simplify((P[0, 0] * x + P[0, 1]) / (P[1, 0] * x + P[1, 1]))

# conjugating the monodromy by P in SL(2,Z) changes the MARKING of the fibre and
# leaves the mapping torus (hence m004) alone; the fixed points move with P.
moved = []
for P in [sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]]),
          sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[0, -1], [1, 0]])]:
    Mc = P * M * P.inv()
    pair = (mob(P, phi), mob(P, phi_bar))
    same_class = sp.simplify(sp.trace(Mc) - sp.trace(M)) == 0
    fixes = sp.simplify(sp.expand((Mc[0, 0] * pair[0] + Mc[0, 1])
                                  - pair[0] * (Mc[1, 0] * pair[0] + Mc[1, 1]))) == 0
    moved.append((P.tolist(), pair, same_class and fixes))
    print(f"    P={P.tolist()}  ->  pair = ({sp.nsimplify(pair[0])}, {sp.nsimplify(pair[1])})"
          f"   = ({float(pair[0]):+.6f}, {float(pair[1]):+.6f})")
check("every conjugate monodromy has the SAME trace (same mapping class)",
      all(m[2] for m in moved))
check("but the fixed-point PAIR takes different values under different markings",
      len({(sp.nsimplify(p[0]), sp.nsimplify(p[1])) for _, p, _ in moved}) == len(moved))

# the marking-free content: the whole orbit consists of NOBLE numbers
# (continued fraction eventually all 1s) -- exact, via the periodic-CF routine.
from sympy.ntheory.continued_fraction import continued_fraction_periodic as cfp
def as_pqd(x):
    """write x in the form (p + sqrt(d))/q with p,q,d integers, exactly"""
    x = sp.nsimplify(sp.radsimp(x))
    p_, q_ = sp.fraction(sp.together(x))
    poly = sp.Poly(sp.minimal_polynomial(x, sp.Symbol('t')), sp.Symbol('t'))
    A, B, C = poly.all_coeffs()
    disc = B * B - 4 * A * C
    return (-B, 2 * A, disc)

nobles = []
for _, (p0, _), _ in moved:
    pp, qq, dd = as_pqd(p0)
    cf = cfp(int(pp), int(qq), int(dd))
    nobles.append((sp.nsimplify(p0), cf))
    print(f"    CF({sp.nsimplify(p0)}) = {cf}")
check("every marked value is NOBLE: periodic part is exactly [1]",
      all(cf[-1] == [1] for _, cf in nobles))
check("phi itself is purely periodic [1]", cfp(1, 2, 5) == [[1]], f"{cfp(1,2,5)}")

# ---------------------------------------------------------------- PART 3
print("\n=== PART 3: the two kappas, and the decisive negative ===")

w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # primitive cube root of unity
check("omega is a primitive cube root of unity",
      sp.simplify(w**2 + w + 1) == 0 and sp.simplify(w**3 - 1) == 0)

# the corpus's OWN banked fibre trace triple (B448 / B1344 / E72)
x0, y0, z0 = 2 + w, 1 - w, 1 - w
check("banked fibre trace x = 2+omega has minpoly x^2 - 3x + 3  (E72's datum)",
      sp.simplify(sp.expand(x0**2 - 3 * x0 + 3)) == 0)
check("x + conj(x) = 3 = trace(RL)",
      sp.simplify(sp.expand(x0 + (2 + sp.conjugate(w))) - sp.trace(M)) == 0)

def fricke(x, y, zz):
    return sp.expand(x**2 + y**2 + zz**2 - x * y * zz - 2)

# the identity is USED below, so it is PROVED here rather than recalled (E58)
_p = sp.symbols('p1:5 q1:5')
_A = sp.Matrix([[_p[0], _p[1]], [_p[2], _p[3]]])
_B = sp.Matrix([[_p[4], _p[5]], [_p[6], _p[7]]])
_A = _A.subs(_p[3], (1 + _p[1] * _p[2]) / _p[0])          # det A = 1
_B = _B.subs(_p[7], (1 + _p[5] * _p[6]) / _p[4])          # det B = 1
_C = _A * _B * _A.inv() * _B.inv()
check("FRICKE IDENTITY tr[A,B] = x^2+y^2+z^2-xyz-2 proved symbolically in SL(2)",
      sp.simplify(sp.trace(_C) - fricke(sp.trace(_A), sp.trace(_B), sp.trace(_A * _B))) == 0)

kappa_fibre = sp.simplify(fricke(x0, y0, z0))
check("FIBRE kappa = tr[A,B] = -2 EXACTLY  (Minsky's defining condition)",
      kappa_fibre == -2, f"kappa_fibre = {kappa_fibre}")
check("equivalently: the triple solves the MARKOV equation x^2+y^2+z^2 = xyz",
      sp.simplify(sp.expand(x0**2 + y0**2 + z0**2 - x0 * y0 * z0)) == 0)
check("|kappa_fibre - 2| = 4", sp.simplify(sp.Abs(kappa_fibre - 2)) == 4)

# meridian side, from the geometry rather than from the record
import mpmath as mp
import snappy
mp.mp.dps = 60                                    # set explicitly (E75)
Mhp = snappy.Manifold("m004").high_precision()
G = Mhp.fundamental_group()
def hp(x):
    """SnapPy high-precision Number -> mpmath mpc via its OWN decimal string.

    NOT via complex(): that truncates at 1e-16 and would silently make every
    exact identification below a 16-digit coincidence (E75, widened to inputs).
    """
    # SnapPy prints exponents with a space before the 'e'; strip it rather
    # than fall back to float()
    f = lambda v: mp.mpf(str(v).replace(' ', ''))
    return mp.mpc(f(x.real()), f(x.imag()))

def gen(name):
    g = G.SL2C(name)
    return mp.matrix([[hp(g[i, j]) for j in range(2)] for i in range(2)])

A, B = gen('a'), gen('b')
check("SnapPy generators arrive at high precision, not through complex()",
      mp.mp.dps >= 50 and len(str(G.SL2C('a')[0, 0].real())) > 30,
      f"dps = {mp.mp.dps}, digits carried = {len(str(G.SL2C('a')[0,0].real()))}")
check("the holonomy is a representation: det = 1 on both generators",
      max(mp.fabs(X[0,0]*X[1,1] - X[0,1]*X[1,0] - 1) for X in (A, B)) < mp.mpf(10)**(-40))
def inv2(X):
    det = X[0, 0] * X[1, 1] - X[0, 1] * X[1, 0]
    return mp.matrix([[X[1, 1] / det, -X[0, 1] / det], [-X[1, 0] / det, X[0, 0] / det]])
comm = A * B * inv2(A) * inv2(B)
kappa_mer = comm[0, 0] + comm[1, 1]
print(f"    kappa_meridian = {mp.nstr(kappa_mer, 25)}")
check("|kappa_meridian - 2| = 1 (Jorgensen's attained value for m004)",
      mp.fabs(mp.fabs(kappa_mer - 2) - 1) < mp.mpf(10)**(-40),
      f"|k-2| = {mp.nstr(mp.fabs(kappa_mer - 2), 25)}")
# identify it exactly.  The LABEL-FREE statement is the one to test: kappa - 2
# is a primitive cube root of unity.  Which of omega, omega^2 it is depends on
# an orientation convention, so testing against a named one tests the label.
u = kappa_mer - 2
TOL = mp.mpf(10)**(-40)
check("kappa_meridian - 2 is a CUBE ROOT OF UNITY", mp.fabs(u**3 - 1) < TOL,
      f"|u^3 - 1| = {mp.nstr(mp.fabs(u**3 - 1), 6)}")
check("... and a PRIMITIVE one (u != 1), so kappa - 2 = omega^(+/-1): "
      "B309/B518/B1010's banked value, up to which root is named omega",
      mp.fabs(u - 1) > mp.mpf("0.1") and mp.fabs(u**2 + u + 1) < TOL,
      f"u = {mp.nstr(u, 20)}")
# and against the named candidates, built at mpmath precision -- NOT via
# complex(sp.N(...)), which truncates at 1e-16 and made this very check fail
# at a 5e-17 residual on the first run (E75 instance #9, in the CONTROL).
r3 = mp.sqrt(3)
cand = {"omega": mp.mpc(mp.mpf(-1) / 2, r3 / 2), "omega^2": mp.mpc(mp.mpf(-1) / 2, -r3 / 2)}
hit = min(cand, key=lambda k: mp.fabs(u - cand[k]))
check("kappa_meridian - 2 matches a named primitive cube root to full precision",
      mp.fabs(u - cand[hit]) < TOL,
      f"= {hit} in this convention, residual {mp.nstr(mp.fabs(u - cand[hit]), 6)}")
check("THE NEGATIVE: m004's KNOT group is NOT a punctured-torus group "
      "(its commutator is not parabolic: kappa != -2)",
      mp.fabs(kappa_mer + 2) > mp.mpf("0.1"),
      f"|kappa_meridian + 2| = {mp.nstr(mp.fabs(kappa_mer + 2), 12)}")
check("the two kappas differ (E72's collision, now with the family's reason)",
      mp.fabs(kappa_mer - (-2)) > mp.mpf("0.1"))

# ---------------------------------------------------------------- PART 4
print("\n=== PART 4: the triple is a FIXED POINT of the mapping-class action ===")

def V1(t): return (t[1] * t[2] - t[0], t[1], t[2])
def V2(t): return (t[0], t[0] * t[2] - t[1], t[2])
def V3(t): return (t[0], t[1], t[0] * t[1] - t[2])
import itertools
T = (x0, y0, z0)
gx, gy = sp.symbols('gx gy')                       # a GENERIC Markov point:
gz = sp.solve(sp.Eq(gx**2 + gy**2 + z**2 - gx * gy * z, 0), z)[0]
GEN = (gx, gy, gz)

def apply(seq, t):
    for f, perm in seq:
        t = f(t)
        t = (t[perm[0]], t[perm[1]], t[perm[2]])
    return tuple(sp.expand(v) for v in t)

def fixes(seq, t):
    out = apply(seq, t)
    return all(sp.simplify(out[i] - t[i]) == 0 for i in range(3))

elems = [(f, p) for f in (V1, V2, V3) for p in itertools.permutations(range(3))]
nontrivial_fixers = []
for e1 in elems:
    for e2 in elems:
        seq = [e1, e2]
        if not fixes(seq, T):
            continue
        if fixes(seq, GEN):            # acts as the identity on the whole surface
            continue
        nontrivial_fixers.append((e1[0].__name__, e1[1], e2[0].__name__, e2[1]))

check("the Markov surface is preserved by each Vieta involution",
      all(sp.simplify(sp.expand(sum(v**2 for v in f(T)) - f(T)[0] * f(T)[1] * f(T)[2])) == 0
          for f in (V1, V2, V3)))
check("a NON-TRIVIAL length-2 Vieta composite fixes the banked triple "
      "(trivial composites filtered by acting on a generic surface point)",
      len(nontrivial_fixers) > 0,
      f"{len(nontrivial_fixers)} of {len(elems)**2}, e.g. {nontrivial_fixers[:2]}")
check("being fixed is INFORMATIVE: those same composites move a generic point",
      all(not fixes([(V1 if a == 'V1' else V2 if a == 'V2' else V3, pa),
                     (V1 if b == 'V1' else V2 if b == 'V2' else V3, pb)], GEN)
          for a, pa, b, pb in nontrivial_fixers))
check("and the banked triple is NOT fixed by everything",
      any(not fixes([e], T) for e in elems))

# ---------------------------------------------------------------- PART 5
print("\n=== PART 5: the whole metallic ladder, in Minsky's coordinates ===")

m = sp.symbols('m', positive=True, integer=True)
Rm, Lm = sp.Matrix([[1, m], [0, 1]]), sp.Matrix([[1, 0], [m, 1]])
Am = sp.expand(Rm * Lm)
check("R^m L^m = [[1+m^2, m],[m, 1]]",
      Am == sp.Matrix([[1 + m**2, m], [m, 1]]), f"trace = {sp.expand(sp.trace(Am))}")

Xm = sp.Matrix([[m, 1], [1, 0]])                 # B469/T-GIES-FAM's det -1 letter
check("A_m = X_m^2, so the two have the SAME fixed points on the circle",
      sp.expand(Xm * Xm) == Am and Xm.det() == -1)

fe = sp.expand((Am[0, 0] * z + Am[0, 1]) - z * (Am[1, 0] * z + Am[1, 1]))
check("the fixed-point equation of R^m L^m is z^2 - m z - 1 = 0",
      sp.simplify(sp.expand(fe + m * (z**2 - m * z - 1))) == 0)
check("its discriminant is m^2 + 4 -- THE SHADOW MODULUS (B666/B997)",
      sp.simplify(sp.discriminant(z**2 - m * z - 1, z) - (m**2 + 4)) == 0)

print("    m   attracting end invariant      CF        discriminant   dilatation")
rows = []
for mm in range(1, 9):
    mu = sp.nsimplify((mm + sp.sqrt(mm**2 + 4)) / 2)
    mub = (mm - sp.sqrt(mm**2 + 4)) / 2
    A = Am.subs(m, mm)
    fixes_it = sp.simplify(sp.expand((A[0,0]*mu + A[0,1]) - mu*(A[1,0]*mu + A[1,1]))) == 0
    # Galois conjugacy tested by VIETA, not by substituting into the printed
    # radical: nsimplify turns (2+sqrt(8))/2 into 1+sqrt(2), after which
    # subs(sqrt(8) -> -sqrt(8)) matches nothing and every EVEN m failed a
    # correct statement.  E75's disease in symbolic clothing -- identifying an
    # object by its representation instead of by a property.
    mp_ = sp.minimal_polynomial(mu, z)
    conj = (sp.simplify(sp.expand(mp_ - (z**2 - mm * z - 1))) == 0
            and sp.simplify(mu + mub - mm) == 0
            and sp.simplify(sp.expand(mu * mub) + 1) == 0
            and not sp.sqrt(mm**2 + 4).is_rational)
    recip = sp.simplify(mub + 1 / mu) == 0
    dil = sp.simplify(max(A.eigenvals().keys(), key=lambda e: sp.re(e)) - mu**2) == 0
    cf = cfp(mm, 2, mm**2 + 4)
    rows.append(all([fixes_it, conj, recip, dil, cf == [[mm]]]))
    print(f"    {mm}   mu_{mm} = {str(mu):22s} {str(cf):9s} {mm**2+4:6d}        mu^2"
          f"   {'ok' if rows[-1] else 'FAIL'}")

check("for m = 1..8 the attracting end invariant IS the m-th METALLIC MEAN, "
      "the repelling one is its Galois conjugate = -1/mu (Vieta: sum m, product -1), "
      "the dilatation is mu^2, and the continued fraction is purely periodic [m]",
      all(rows))
check("z^2 - m z - 1 is irreducible over Q for every m >= 1 "
      "(m^2+4 = k^2 forces (k-m)(k+m) = 4, i.e. m = 0), so the two roots really "
      "are Galois conjugates",
      all(not sp.sqrt(mm**2 + 4).is_rational for mm in range(1, 60)))
check("m = 1 recovers the golden case of PART 1",
      sp.simplify(sp.nsimplify((1 + sp.sqrt(5)) / 2) - phi) == 0 and cfp(1, 2, 5) == [[1]])

# ---------------------------------------------------------------- summary
print("\n=== SUMMARY ===")
bad = [n for n, o in OK if not o]
print(f"  {len(OK) - len(bad)}/{len(OK)} checks pass")
if bad:
    print("  FAILURES: " + "; ".join(bad))
raise SystemExit(1 if bad else 0)
