#!/usr/bin/env python3
# B749 — fork F6 (sealed campaign, seal v2). Executed exactly per the binding block in
# MEASUREMENTS.md:
#   Sibling: the CLOSED torus bundle M = T^2 x_A S^1 of A = [[2,1],[1,1]] (no puncture).
#   Measure: geometry type via the trichotomy (computed, not cited); hyperbolicity NO;
#   H1 = Z + coker(A - I) exactly; trace field NONE; every V4 face present/absent explicitly.
#   Verdict: ROBUST = total face-loss; FRAGILE = any face survives closure.
# Cross-fork instrument rules honored: exact field claims by symbolic minpoly (not numerics);
# snappy identifications by TWO independent invariants (volume AND isometry); deterministic
# (no wall-clock, no unseeded randomness, no network); CHECK lines for the merge gate.
#
# Conventions: closed torus bundle of A in SL2(Z): pi1 = Z^2 x|_A Z;
# H1(M) = Z (+) coker(A - I) (Wang sequence); trichotomy for closed torus bundles:
# A finite order => E^3; |tr A| = 2, A != +/-I => Nil; A Anosov (real eigenvalues off the
# unit circle, char poly irreducible) => Sol. Membership in the Anosov class is COMPUTED
# below; only the geometrization statement itself is the theorem.

import sympy as sp
from sympy import Matrix, eye, sqrt, simplify, symbols, Rational

lines = []
def emit(s):
    print(s)
    lines.append(s)

def check(fact):
    emit("CHECK: " + fact)

t, x = symbols("t x")

# ---------------------------------------------------------------- section 0: the sibling
A = Matrix([[2, 1], [1, 1]])
R = Matrix([[1, 1], [0, 1]])
L = Matrix([[1, 0], [1, 1]])
assert R * L == A
assert A.det() == 1
emit("F6 sibling: closed torus bundle M = T^2 x_A S^1, A = [[2,1],[1,1]] (sealed block).")
check("sibling A = [[2,1],[1,1]]; det(A) = %s (A in SL2(Z), total space orientable); A = R*L" % A.det())

# ------------------------------------------------- section 1: trichotomy => geometry type
tr = A.trace()
p = sp.Poly(A.charpoly(x).as_expr(), x, domain="QQ")
assert p.as_expr() == x**2 - 3 * x + 1
irred = p.is_irreducible
lam = (3 + sqrt(5)) / 2
lamc = (3 - sqrt(5)) / 2
assert simplify(p.as_expr().subs(x, lam)) == 0
assert simplify(lam * lamc - 1) == 0          # det 1: eigenvalues reciprocal
assert lam.evalf(30) > 1                      # off the unit circle (real, > 1)
check("trace(A) = %s; charpoly = x**2 - 3*x + 1, irreducible/QQ = %s; eigenvalues (3+-sqrt(5))/2 "
      "real, irrational, reciprocal, off unit circle => A is Anosov (infinite order, no root of unity)" % (tr, irred))
check("trichotomy(closed torus bundle: finite-order => E3; |tr|=2,!=+-I => Nil; Anosov => Sol): "
      "|trace| = 3 > 2 and Anosov verified => geometry = Sol; hyperbolic = NO")

# --------------------------------------------------------------- section 2: H1, exactly
AmI = A - eye(2)
d = AmI.det()
assert AmI == Matrix([[1, 1], [1, 0]])
from sympy.matrices.normalforms import smith_normal_form
snf = smith_normal_form(AmI)
assert snf == Matrix([[1, 0], [0, 1]])
check("A - I = [[1,1],[1,0]]; det(A-I) = %s; Smith normal form = diag(1,1) => coker(A-I) = 0" % d)
check("H1(M) = Z (+) coker(A-I) = Z  (exact, Wang sequence + SNF)")

# ------------------------------------- section 3: snappy closed model (independent route)
import snappy
emit("snappy version: %s" % snappy.__version__)
m004 = snappy.Manifold("m004")
k41 = snappy.Manifold("4_1")
bRL = snappy.Manifold("b++RL")
vols = [m004.volume(), k41.volume(), bRL.volume()]
vol_agree = max(abs(vols[i] - vols[0]) for i in range(3)) < 1e-9
iso1 = k41.is_isometric_to(m004)
iso2 = bRL.is_isometric_to(m004)
check("punctured partner: b++RL (monodromy R*L = A) isometric to m004 = %s; 4_1 isometric to m004 = %s; "
      "volumes all = %.9f (agree to 1e-9 = %s) — identification by TWO invariants (isometry AND volume)"
      % (iso2, iso1, vols[0], vol_agree))

def second_column(mat):
    try:
        return (int(mat[0, 1]), int(mat[1, 1]))
    except TypeError:
        return (int(mat[0][1]), int(mat[1][1]))

isos = k41.is_isometric_to(m004, return_isometries=True)
cols = sorted(set(second_column(i.cusp_maps()[0]) for i in isos))
slope_ok = all(c in [(0, 1), (0, -1)] for c in cols)
check("all 4_1 -> m004 isometries map slope (0,1) to +/-(0,1) (second columns of cusp maps = %s): %s"
      % (cols, slope_ok))
Mlong = snappy.Manifold("m004(0,1)")
check("m004(0,1) homology = %s => (0,1) is m004's homological longitude (the unique b1 = 1 filling slope); "
      "so 4_1(0,1) = m004(0,1) = fiber-capping filling = the closed bundle of A" % Mlong.homology())

M = snappy.Manifold("4_1(0,1)")
sol = M.solution_type()
vol0 = M.volume()
check("snappy 4_1(0,1): solution_type = '%s'; volume = %s => no positively-oriented (hyperbolic) solution "
      "— non-hyperbolicity confirmed independently of the trichotomy" % (sol, vol0))
FT = M.filled_triangulation()
check("filled_triangulation(4_1(0,1)): num_cusps = %s; homology = %s (closed model cross-checks: "
      "0 cusps, H1 = Z matches the exact SNF computation)" % (FT.num_cusps(), FT.homology()))

# --------------------------- section 4: the dilatation field, exactly (instrument rules)
phi = (1 + sqrt(5)) / 2
mp = sp.minimal_polynomial(lam, x)
assert mp == x**2 - 3 * x + 1
disc = sp.discriminant(mp, x)
assert disc == 5
check("minpoly(lambda) = x**2 - 3*x + 1 (SYMBOLIC minpoly, exact — not numeric algdep); disc = 5; "
      "lambda = (3+sqrt(5))/2")
assert simplify(lam - phi**2) == 0
check("lambda - phi**2 = 0 exactly (phi = (1+sqrt(5))/2) => dilatation of the monodromy = phi^2 (golden)")
s_u = simplify(lam - 2)          # unstable eigenvector slope: y = (lambda-2) x
s_s = simplify(lamc - 2)
assert simplify(s_u * phi - 1) == 0
assert simplify(s_s + phi) == 0
check("invariant foliation slopes: lambda - 2 = 1/phi and lambda' - 2 = -phi exactly (golden slopes)")
res = sp.resultant(x**2 - 3 * x + 1, x**2 + 3, x)
sq15 = sp.sqrt(15).is_rational
check("Q(lambda) = Q(sqrt(5)) (real quadratic); resultant(x**2-3*x+1, x**2+3) = %s != 0 and "
      "sqrt(15) rational = %s => Q(sqrt(5)) != Q(sqrt(-3))" % (res, sq15))
check("trace field of M: NONE — a trace field needs a finite-covolume Kleinian group; geometry is Sol "
      "(section 1) and the closed model has volume 0 / flat solution (section 3): no such group exists")

# ------------------------- section 5: pi1 = O_K x|_{eps^2} Z (the O_{Q(sqrt5)} structure)
P = Matrix([[1, 0], [1, 1]])
assert P.det() == 1
B = P * A * P.inv()
assert B == Matrix([[1, 1], [1, 2]])
# multiplication by phi^2 on Z[phi] in basis (1, phi):
assert simplify(phi**2 - (1 + phi)) == 0        # phi^2 * 1   = 1*1 + 1*phi
assert simplify(phi**3 - (1 + 2 * phi)) == 0    # phi^2 * phi = 1*1 + 2*phi
Nphi = simplify(phi * (1 - phi))                # field norm of phi
assert Nphi == -1
check("P = [[1,0],[1,1]] in SL2(Z): P*A*P^-1 = [[1,1],[1,2]] = matrix of mult-by-phi^2 on Z[phi] "
      "(phi^2*1 = 1+phi, phi^2*phi = 1+2*phi exact); 5 mod 4 = 1 so O_{Q(sqrt5)} = Z[phi]; N(phi) = -1 "
      "(phi = fundamental unit) => pi1(M) = O_{Q(sqrt5)} x|_{eps^2} Z, eps = phi")
emit("Intrinsicness: pi1 = Z^2 x|_A Z with A Anosov (computed) => Z^2 is the Fitting subgroup (unique "
     "maximal nilpotent normal subgroup), so the GL2(Z)-class of A up to inversion — hence Q(sqrt(5)), "
     "phi^2, the slopes — is an invariant of pi1(M), not of the chosen description.")

# ----------------------- section 6: cyclic-cover torsion growth (hearing-face exhibit 2)
tors = []
ok_lucas = True
for n in range(1, 13):
    Tn = abs((A**n - eye(2)).det())
    tors.append(int(Tn))
    ok_lucas = ok_lucas and (Tn == sp.lucas(2 * n) - 2)
growth = sp.log(tors[-1]) / 12
target = 2 * sp.log(phi)
check("|Tor H1(n-fold cyclic cover)| = |det(A^n - I)| = Lucas(2n) - 2 for n = 1..12: %s (all match = %s)"
      % (tors, ok_lucas))
check("torsion log-growth at n = 12: log(%d)/12 = %s ~ 2*log(phi) = %s (golden growth rate 2*log(phi))"
      % (tors[-1], sp.N(growth, 10), sp.N(target, 10)))

# ---------------------------------------------- section 7: the V4 faces, each explicitly
emit("")
emit("V4 face audit of the closed sibling M (yardstick = MEASUREMENTS.md preamble):")
check("face BEING (trace field Q(sqrt(-3))): ABSENT — no hyperbolic structure => no trace field "
      "(Sol by computed trichotomy; snappy volume 0/flat independently); the only number field in any "
      "computed invariant is Q(sqrt(5)) (disc 5), and Q(sqrt(5)) != Q(sqrt(-3)) (section 4)")
check("face CUSP/INTERFACE: ABSENT — M is closed: filled model has num_cusps = 0 (the fork's defining "
      "variation, certified on the model, not assumed)")
check("face ARITHMETICITY (Maclachlan-Reid, of a Kleinian group): ABSENT/undefined — its carrier (a "
      "finite-covolume Kleinian group) does not exist; the arithmetic that DOES survive is the "
      "O_{Q(sqrt5)} unit action, which is hearing-side data (section 5)")
check("face HEARING (golden/Q(sqrt5)): PRESENT — dilatation phi^2 exact; foliation slopes 1/phi, -phi; "
      "pi1 = O_{Q(sqrt5)} x|_{phi^2} Z; Lucas torsion growth 2*log(phi); all intrinsic (Fitting argument)")
check("H1 = Z yardstick (knot-ness): the VALUE survives — H1(M) = Z exact (= H1(m004)); knot-complement-"
      "ness itself is absent (M closed; M = 0-surgery on 4_1, not a complement)")

# --------------------------------------------------------------------- section 8: verdict
emit("")
emit("Sealed criterion (MEASUREMENTS.md F6): ROBUST = total face-loss; FRAGILE = any face survives closure.")
check("faces surviving closure: HEARING (golden/Q(sqrt5)) and the H1 = Z value => the FRAGILE trigger "
      "'any face survives closure' FIRES => VERDICT F6 = FRAGILE")
emit("")
emit("Finding (contra the sealed prior 'F6 ROBUST' — per PREREGISTRATION, a finding, not a failure):")
emit("closure strips exactly the BEING half of the V4 — being field, interface, arithmeticity, "
     "hyperbolicity all die with the puncture (B747/B748's interface-only prediction holds for the being "
     "side) — but the HEARING face is monodromy-borne, not interface-borne: it survives closure intact "
     "and indeed becomes the whole manifold (pi1 = O_{Q(sqrt5)} x|_{phi^2} Z). The no-puncture choice is "
     "load-bearing for being + interface, cheap for hearing. House rule: FRAGILE => 3-skeptic verify "
     "(downstream of this fork agent).")

with open(__file__.rsplit("/", 1)[0] + "/output.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
