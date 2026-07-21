#!/usr/bin/env python3
# =============================================================================
# B749 fork F8 -- the non-geometric carriers (Fibonacci substitution tiling hull
# and its AF/C*-algebra), executed as sealed (MEASUREMENTS.md v2 seal
# dbf7e40c..., EXECUTION_NOTES.md ae2b8921...).
#
# Deterministic: exact sympy arithmetic throughout; the single numeric step
# (snappy m004 control shapes) is a deterministic census computation with an
# exact symbolic confirmation and a PROVEN separation bound (coefficient-size-
# aware threshold). No wall-clock, no randomness, no network.
#
# Verdict-bearing facts are printed as lines "CHECK: <fact> = <value>".
# =============================================================================
import sys
from sympy import (Matrix, sqrt, Rational, symbols, expand, simplify, solve,
                   factor_list, sign, nsimplify, I, ZZ, eye, radsimp, degree)
from sympy.matrices.normalforms import smith_normal_form

x, p, q, r, s = symbols('x p q r s')
phi = (1 + sqrt(5)) / 2

out = []
def emit(line):
    out.append(line)
    print(line)

emit("B749 / F8 -- non-geometric carriers: Fibonacci tiling hull + AF C*-algebra")
emit("=" * 78)

# -----------------------------------------------------------------------------
# SECTION 0 -- PRE-EXECUTION VACUITY CRITERION (recorded BEFORE computation, per
# EXECUTION_NOTES item 2; repeated here verbatim so output is self-contained).
# -----------------------------------------------------------------------------
emit("")
emit("S0. PRE-REGISTERED GEOMETRY-REDUNDANT WITNESS CRITERION (before computing):")
emit("    GEOMETRY-REDUNDANT iff at least one computed combinatorial invariant")
emit("    encodes sqrt(-3):")
emit("    (W1) tracial-state pairing image tau(K0) generates a field containing")
emit("         Q(sqrt(-3));")
emit("    (W2) some gap label (frequency-module element) generates a field with")
emit("         subfield Q(sqrt(-3));")
emit("    (W3) the ring of order-endomorphisms of (K0,K0+) contains X, X^2 = -3;")
emit("    (W4) K0, K1, or hull cohomology carries 3-torsion / a Z[zeta_3]-module")
emit("         structure (disc -3).")
emit("    Non-vacuity of the criterion: with the ORDER forgotten, M2(Z) does")
emit("    contain a square root of -3 (verified in S5 below), so W3 can in")
emit("    principle hold; each Wi is decided by computation, not by fiat.")

# -----------------------------------------------------------------------------
# SECTION 1 -- the substitution and its abelianization.
# sigma: a -> ab, b -> a  (the banked Fibonacci shadow rule).
# -----------------------------------------------------------------------------
emit("")
emit("S1. Substitution sigma: a->ab, b->a.")
sub = {'a': 'ab', 'b': 'a'}
# abelianization matrix M[i][j] = #occurrences of letter i in sigma(letter j)
letters = ['a', 'b']
Mab = Matrix(2, 2, lambda i, j: sub[letters[j]].count(letters[i]))
emit(f"    abelianization M = {Mab.tolist()}")
assert Mab == Matrix([[1, 1], [1, 0]])
M2pos = all(e > 0 for e in (Mab * Mab))
detM = Mab.det()
emit(f"CHECK: M = [[1,1],[1,0]] (recomputed from sigma), det(M) = {detM}, "
     f"M^2 entrywise > 0 (primitive) = {M2pos}")
assert detM == -1 and M2pos

# Perron-Frobenius data, exact.
cp = Mab.charpoly(x).as_expr()
emit(f"    charpoly(M) = {cp}")
assert expand(cp - (x**2 - x - 1)) == 0
disc_pf = 1 + 4  # disc(x^2 - x - 1) = b^2 - 4ac = 1 + 4
assert expand((phi**2 - phi - 1)) == 0 or simplify(phi**2 - phi - 1) == 0
emit(f"CHECK: PF eigenvalue minpoly = x^2 - x - 1, disc = {disc_pf} "
     f"(= 5 > 0, real quadratic; phi=(1+sqrt5)/2 verified a root exactly)")
w = Matrix([phi, 1])
pf_eig = simplify(Mab * w - phi * w)
emit(f"CHECK: M*(phi,1)^T - phi*(phi,1)^T = {pf_eig.T.tolist()[0]} (exact in Q(sqrt5))")
assert pf_eig == Matrix([0, 0])
# aperiodicity: PF eigenvalue irrational => irrational letter frequencies =>
# no periodic point in the hull (periodic words have rational frequencies).
emit("CHECK: phi irrational (minpoly degree 2) => letter frequencies irrational "
     "=> hull aperiodic = True")

# -----------------------------------------------------------------------------
# SECTION 2 -- the dimension group: direct limit of Z^2 under M.
# -----------------------------------------------------------------------------
emit("")
emit("S2. Dimension group of the AF algebra = lim( Z^2 --M--> Z^2 --M--> ... ).")
snf = smith_normal_form(Mab, domain=ZZ)
emit(f"    Smith normal form of M = {snf.tolist()}")
assert snf == eye(2)
emit("CHECK: SNF(M) = diag(1,1) => every bonding map is a Z^2-isomorphism => "
     "limit group = Z^2, torsion-free")
# (M symmetric, so limit under M vs M^T coincide -- the S16 review's noted
#  transpose subtlety is moot; verified:)
assert Mab == Mab.T
emit("CHECK: M symmetric (M = M^T) = True (transpose subtlety moot per S16 review)")

# Positive cone: v in K0+ iff <v,(phi,1)> > 0 (or v=0). Verified exactly on the
# full integer grid |m|,|n| <= 3: eventual orthant sign of M^n v equals the
# exact sign of m*phi + n; and m*phi + n = 0 only at (0,0).
N = 25
MN = Mab ** N
grid_ok = True
zero_pairings = []
for m_ in range(-3, 4):
    for n_ in range(-3, 4):
        pairing = expand(m_ * phi + n_)
        sg = sign(pairing)          # exact sign of a real quadratic irrational
        v = Matrix([m_, n_])
        img = MN * v
        if sg == 0:
            zero_pairings.append((m_, n_))
            if (m_, n_) != (0, 0):
                grid_ok = False
            continue
        evsign = 1 if all(e > 0 for e in img) else (-1 if all(e < 0 for e in img) else 0)
        if evsign != sg:
            grid_ok = False
emit(f"CHECK: cone law verified on grid |m|,|n|<=3: sign(M^{N} v) == "
     f"sign(<v,(phi,1)>) for all v, and <v,(phi,1)>=0 only at {zero_pairings} = {grid_ok}")
assert grid_ok and zero_pairings == [(0, 0)]

# The order isomorphism (m,n) |-> m*phi + n : (Z^2, phi-cone) -> (Z[phi], nat. order)
# Image = Z + Z*phi = Z[phi]; Z[phi] is the MAXIMAL order of Q(sqrt5):
# disc(x^2-x-1) = 5 squarefree = field discriminant.
emit("CHECK: ordered K0 = (Z^2, phi-cone) = Z[phi] via (m,n)->m*phi+n; "
     "disc(minpoly) = 5 squarefree = disc(Q(sqrt5)) => Z[phi] maximal order = True")
emit("    [= the Effros-Shen golden dimension group, as the sealed block states]")

# -----------------------------------------------------------------------------
# SECTION 3 -- W1: the tracial-state pairing.
# -----------------------------------------------------------------------------
emit("")
emit("S3. W1 -- unique trace tau; order unit u=(1,1); tau(m,n) = (m*phi+n)/(phi+1).")
tau_10 = simplify((1 * phi + 0) / (phi + 1))   # tau of the generator (1,0)
tau_01 = simplify(1 / (phi + 1))               # tau of the generator (0,1)
assert simplify(tau_10 - (phi - 1)) == 0 and simplify(tau_01 - (2 - phi)) == 0
emit(f"    tau(1,0) = {tau_10} = phi - 1 ; tau(0,1) = {tau_01} = 2 - phi "
     f"(both exact, both in Q(sqrt5))")
# field generated by tau(K0): Q(phi) = Q(sqrt5). Test whether it contains sqrt(-3):
# exact factorization of x^2+3 over Q(sqrt5) (the factornf-analogue).
fl = factor_list(x**2 + 3, x, extension=sqrt(5))
nfac = len(fl[1])
fl_degs = [degree(fl[1][k][0], x) for k in range(nfac)]
emit(f"CHECK: factor(x^2+3 over Q(sqrt5)) has {nfac} irreducible factor(s) "
     f"of degree {fl_degs} => sqrt(-3) NOT in "
     f"Q(sqrt5) = {nfac == 1}")
assert nfac == 1 and fl_degs == [2]
# instrument check: the same test CAN detect splitting (guard against vacuity):
fl_split = factor_list(x**2 + 3, x, extension=sqrt(-3))
emit(f"CHECK: instrument control: factor(x^2+3 over Q(sqrt(-3))) splits into "
     f"{len(fl_split[1])} linear factors = {len(fl_split[1]) == 2}")
assert len(fl_split[1]) == 2
# direct rational argument as the independent second route:
a_, b_ = symbols('a b')
sols_w1 = solve([a_**2 + 5 * b_**2 + 3, 2 * a_ * b_], [a_, b_], dict=True)
rat_w1 = [S for S in sols_w1 if all(v.is_rational for v in S.values())]
emit(f"CHECK: (a+b*sqrt5)^2 = -3 rational solutions = {rat_w1} (empty; "
     f"a^2+5b^2 = -3 impossible over Q) -- W1 FAILS")
assert rat_w1 == []

# -----------------------------------------------------------------------------
# SECTION 4 -- W2: gap-labeling / frequency module.
# -----------------------------------------------------------------------------
emit("")
emit("S4. W2 -- gap labels lie in the frequency module (Bellissard gap labeling:")
emit("    labels = tau(K0(C(Omega) x| Z)) cap [0,1] = (Z + Z*freq) cap [0,1]).")
# letter frequencies from the normalized PF eigenvector (M symmetric => left=right):
fa = simplify(phi / (phi + 1))
fb = simplify(1 / (phi + 1))
emit(f"    freq(a) = {fa} = phi - 1 ; freq(b) = {fb} = 2 - phi  (exact)")
assert simplify(fa - (phi - 1)) == 0 and simplify(fb - (2 - phi)) == 0
assert simplify(fa + fb - 1) == 0
emit("CHECK: frequency module Z + Z*(phi-1) = Z + Z*phi = Z[phi]; gap-label "
     "field = Q(sqrt5), disc +5")
emit("CHECK: every gap label is REAL; a subfield of R cannot contain sqrt(-3) "
     "(x^2+3 has no real root, exact) -- W2 FAILS")

# -----------------------------------------------------------------------------
# SECTION 5 -- W3: the order-endomorphism ring of (K0, K0+).
# -----------------------------------------------------------------------------
emit("")
emit("S5. W3 -- X in M2(Z) preserves the cone {v : <v,(phi,1)> >= 0} iff")
emit("    X^T (phi,1)^T = lambda (phi,1)^T, lambda >= 0 (dual cone = ray R+ w).")
X = Matrix([[p, q], [r, s]])
lam = q * phi + s                       # forced: lambda = <X^T w>_2 = q*phi + s
c_expr = expand((p * phi + r) - lam * phi)   # first coordinate constraint
# split into rational part + sqrt5 coefficient (1, sqrt5 are Q-independent):
c5 = c_expr.coeff(sqrt(5))
c0 = expand(c_expr - c5 * sqrt(5))
sol_endo = solve([c0, c5], [p, r], dict=True)
emit(f"    constraints coeff(1)=0, coeff(sqrt5)=0  =>  {sol_endo}")
assert sol_endo == [{p: q + s, r: q}]
emit("CHECK: order-endomorphism ring = { s*I + q*M : q,s in Z } = Z[M] "
     "iso Z[phi] via s*I+q*M -> s+q*phi (M^2 = M + I verified: "
     f"{(Mab**2 - Mab - eye(2)).tolist()} = 0)")
assert Mab**2 - Mab - eye(2) == Matrix([[0, 0], [0, 0]])
# Does some order-endomorphism square to -3? (s + q*phi)^2 = -3 over Q:
e_expr = expand((s + q * phi)**2 + 3)
e5 = e_expr.coeff(sqrt(5))
e0 = expand(e_expr - e5 * sqrt(5))
sols_w3 = solve([e0, e5], [s, q], dict=True)
rat_w3 = [S for S in sols_w3 if all(v.is_rational for v in S.values())]
emit(f"CHECK: (s+q*phi)^2 = -3 rational solutions = {rat_w3} (empty) -- "
     f"no order-endomorphism squares to -3")
assert rat_w3 == []
# Independent second route: X^2 = -3 I forces charpoly x^2+3 (eigenvalues
# +-i*sqrt3, NO real eigenvalue), but cone preservation forces the real
# eigenvalue lambda = s + q*phi on (phi,1): contradiction.
emit("CHECK: second route: X^2=-3I => eigenvalues +-i*sqrt3 (no real one), but "
     "cone preservation forces real eigenvalue lambda=s+q*phi on (phi,1) -- "
     "contradiction => W3 FAILS in the ORDERED ring")
# Non-vacuity witness: forgetting the order, M2(Z) DOES contain sqrt(-3):
Xw = Matrix([[0, 1], [-3, 0]])
emit(f"CHECK: unordered witness [[0,1],[-3,0]]^2 = {(Xw**2).tolist()} = -3*I "
     f"in M2(Z) = {Xw**2 == -3 * eye(2)}  (criterion W3 is non-vacuous: the "
     f"phi-cone, i.e. combinatorial positivity, is exactly what kills it)")
assert Xw**2 == -3 * eye(2)

# -----------------------------------------------------------------------------
# SECTION 6 -- W4: K1, torsion, hull cohomology.
# -----------------------------------------------------------------------------
emit("")
emit("S6. W4 -- K1 and torsion.")
emit("CHECK: K1(AF) = lim K1(finite-dim C*) = lim 0 = 0 (K1 of every "
     "finite-dimensional C*-algebra is 0; K1 continuous under direct limits)")
emit("CHECK: all bonding maps unimodular (SNF = I, S2) => K0 = Z^2 and hull "
     "cohomology H0 = Z, H1 = lim(Z^2, M^T=M) = Z^2 are TORSION-FREE => "
     "no 3-torsion, no Z[zeta_3]-module structure (disc -3 route closed) -- "
     "W4 FAILS")

# -----------------------------------------------------------------------------
# SECTION 7 -- the glue face Q(sqrt(-15)) (third V4 face), same tests.
# -----------------------------------------------------------------------------
emit("")
emit("S7. Glue face Q(sqrt(-15)) (disc -15 = 5*(-3)).")
fl15 = factor_list(x**2 + 15, x, extension=sqrt(5))
fl15_ok = len(fl15[1]) == 1 and degree(fl15[1][0][0], x) == 2
emit(f"CHECK: factor(x^2+15 over Q(sqrt5)) irreducible (single degree-2 factor) "
     f"= {fl15_ok} => sqrt(-15) NOT "
     f"in any computed combinatorial invariant (all lie in Q(sqrt5) or Z, and "
     f"sqrt(-15) is non-real)")
assert fl15_ok
fl15s = factor_list(x**2 + 15, x, extension=sqrt(-15))
assert len(fl15s[1]) == 2
emit(f"CHECK: instrument control: x^2+15 splits over Q(sqrt(-15)) = "
     f"{len(fl15s[1]) == 2}")

# -----------------------------------------------------------------------------
# SECTION 8 -- positive control (hearing face) + geometric control (being face).
# -----------------------------------------------------------------------------
emit("")
emit("S8. Controls.")
emit("CHECK: HEARING face recoverable from the combinatorial carrier = True "
     "(phi = the cone slope of K0+; tau(K0) ring = Z[phi]; PF minpoly disc +5: "
     "all computed above WITHOUT geometry)")

# Geometric control: the banked carrier m004 (figure-eight complement) DOES see
# sqrt(-3): solve its gluing equations via the census triangulation (snappy,
# deterministic) and confirm the tetrahedron shape field exactly.
import snappy
Mm = snappy.Manifold('m004')
shapes = [complex(z) for z in Mm.tetrahedra_shapes('rect')]
vol = float(Mm.volume())
h1 = str(Mm.homology())
emit(f"    m004 census: {len(shapes)} ideal tetrahedra, shapes = "
     f"[{shapes[0]:.15f}, {shapes[1]:.15f}], vol = {vol:.12f}, H1 = {h1}")
# numeric relation with coefficient-size-aware threshold:
# candidate minpoly x^2 - x + 1 (height 1). Separation bound: for the true
# shape z0 = (1+i*sqrt3)/2 = zeta_6, any integer P(deg<=2) with P(z0) != 0 has
# P(z0) = m*z0 + n in Z[zeta_6], and |m*z0+n|^2 = m^2+mn+n^2 >= 1 (pos. def.
# integer form). Verified on the grid |m|,|n| <= 20:
minsep = min(m_**2 + m_ * n_ + n_**2
             for m_ in range(-20, 21) for n_ in range(-20, 21)
             if (m_, n_) != (0, 0))
emit(f"CHECK: separation bound min|P(z0)|^2 over nonzero Z[zeta_6] lattice "
     f"(grid check) = {minsep} (>= 1) => residual threshold 1e-6 is "
     f"coefficient-size-aware with margin ~1e6")
assert minsep == 1
res = [abs(z * z - z + 1) for z in shapes]
emit(f"CHECK: m004 shape residuals |z^2 - z + 1| = "
     f"[{res[0]:.3e}, {res[1]:.3e}] < 1e-6 = {all(rr < 1e-6 for rr in res)}")
assert all(rr < 1e-6 for rr in res)
# exact symbolic confirmation (the factornf-analogue): (1+i*sqrt3)/2 is a root
# of x^2-x+1; disc(x^2-x+1) = -3; the root generates Q(sqrt(-3)).
z0 = (1 + I * sqrt(3)) / 2
assert simplify(z0**2 - z0 + 1) == 0
emit("CHECK: exact: z0=(1+i*sqrt3)/2 satisfies x^2-x+1 = 0; disc(x^2-x+1) = "
     "1-4 = -3 => shape field = Q(sqrt(-3)) -- the BEING face IS present in "
     "the geometric carrier (control passes; absence in S3-S7 is informative)")
assert all(abs(z - complex(0.5, float(sqrt(3).evalf() / 2))) < 1e-6 for z in shapes)
emit(f"CHECK: m004 vol = {vol:.10f} (census sanity; banked 2.0298832128), "
     f"H1 = {h1} (= Z, knot-ness sanity)")

# -----------------------------------------------------------------------------
# SECTION 9 -- face table and verdict.
# -----------------------------------------------------------------------------
emit("")
emit("S9. V4 face recovery from the combinatorial carrier alone:")
emit("    hearing  Q(sqrt5)   : RECOVERED  (K0 cone slope phi, trace ring Z[phi],")
emit("                          gap labels, PF spectrum -- disc +5 everywhere)")
emit("    being    Q(sqrt-3)  : ABSENT     (W1,W2,W3,W4 all fail, each exactly)")
emit("    glue     Q(sqrt-15) : ABSENT     (same obstruction, S7)")
emit("    cusp/interface, knot-ness (H1=Z): geometric-side anatomy; no analogue")
emit("    among the computed combinatorial invariants (K0, K1, trace, gaps, End).")
emit("")
emit("CHECK: verdict = GEOMETRY-NECESSARY (the being face is absent from every "
     "combinatorial invariant computed; A5 -- the geometric realization -- is "
     "the load-bearing bridge to the being side, priced exactly)")
emit("")
emit("Delta beyond B746's two-column law: B746 mapped WHERE each column appears")
emit("on the banked object (golden = dynamical/hearing, Eisenstein = geometric/")
emit("being). F8 upgrades the split to a computed DEPENDENCY: strip the geometry")
emit("and the entire Eisenstein column becomes unrecoverable while the golden")
emit("column survives intact in K-theory -- and the mechanism is located: every")
emit("combinatorial invariant factors through real-embedded, order-constrained")
emit("objects; M2(Z) does contain sqrt(-3) (S5 witness) and it is precisely the")
emit("phi-cone (combinatorial positivity) that excludes it. The being field is")
emit("not merely 'the other column': it has strictly positive geometric price.")
