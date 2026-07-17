#!/usr/bin/env python3
"""B672 cell B -- THE BRANCH-TIEBREAK LEMMA (cusp quantization).

Task: stage selection is complete at PAIR level (B666/cellW32):
{SU(3)_2 <-> the ear branch 2h' (tone -1/phi), SU(5)_1 <-> the Galois
partner 2h (tone +phi)}.  The named residual: WHY does the object sit
on the SU(3)_2 stage?  Candidate discharge (recorded by W32, not
proven): CUSP QUANTIZATION -- the object's cusp field Q(sqrt-3) is the
A2 weight-lattice field, not anything available to A4.

This cell:
 (a) formalizes "couples to" from the banked functor (B644, B650) and
     shows the branch tiebreak IS a stage tiebreak;
 (b) computes BOTH sides exactly: the cusp lattice from the banked
     peripheral holonomy (figure-eight discrete faithful rep, exact
     over Q(sqrt-3)); the A2 and A4 weight lattices with their
     quadratic forms and Coxeter arithmetic;
 (c) proves the dichotomy: the canonical (Coxeter-equivariant,
     conformal) map cusp lattice -> stage weight lattice EXISTS and is
     essentially unique for A2, and CANNOT EXIST for A4 -- exact both
     ways.

Exact arithmetic (sympy) in every decisive step.  The only floats are
the corroborating BFS over the peripheral subgroup (flagged
NON-DECISIVE; the decisive longitude verification is exact).

Banked anchors used: B637/B598 (cusp modulus -2 sqrt-3; cusp field
Q(sqrt-3)); B644 (rho_hear = golden character o mod-conductor
reduction); B650 W2-G1/W2-G2 (module-linear intertwiner = 0; the
functor is GROUP-functorial); TYPES.md T_field + K020 (Galois-orbit
position is stage-chosen); B666/cellW32 (pair-level selection).
"""

import itertools
from sympy import (Matrix, symbols, solve, sqrt, I, simplify, Poly, Rational,
                   eye, expand, nsimplify, factor, gcd, minimal_polynomial,
                   rem, im, re, radsimp)

t, x, c, p, q = symbols('t x c p q')

BAR = "=" * 72


def sec(title):
    print()
    print(BAR)
    print(title)
    print(BAR)


# ---------------------------------------------------------------------------
sec("PART A -- FORMALIZATION: what 'couples to' must mean (the banked functor)")
print("""
D1 (couples-to; forced by the bank).  'The object couples to stage S
through branch chi' :=  the theta-odd hearing functor equality
    rho_hear^S = chi o red_kappa          (B644, verification-strength)
where red_kappa is reduction of the monodromy group mod the conductor
(5), and chi is one of the two Galois-conjugate 2-dim characters of
SL(2,F5).  B650 (W2-G1) proved the module-linear channel is ZERO (the
equivariance wall); W2-G2: the ONLY functorial channel is this group
functor.  In the type system (B650 TYPES.md) the coupling is
T_field/F-class data, and per K020 the branch = the stage-chosen
position within the Galois orbit.

CONSEQUENCE (pair-level bank, W32 Part 4): each surviving stage
DETERMINES its branch -- SU(3)_2 realizes 2h' (-1/phi on the cat map),
SU(5)_1 realizes 2h (+phi).  Therefore

    THE BRANCH TIEBREAK == THE STAGE TIEBREAK:

one more exact stage-level exclusion completes the selection, and the
branch follows from the banked pair assignment.  No branch-level
choice remains to be made once the stage is forced.

D2 (cusp quantization; the W32 candidate made exact).  The object's
cusp is a flat torus C/Lambda_cusp: the peripheral holonomy is
parabolic, its translation lattice Lambda_cusp = Z<mu-translation,
lambda-translation> carries the ONLY structure hyperbolic geometry
puts on the cusp beyond the bare Z^2: the conformal class, i.e.
multiplication by the cusp modulus tau (banked: tau = -2 sqrt-3,
B637/B598).  A stage S with weight lattice P(S) carries a canonical
torus arithmetic: the Coxeter element c_S (the principal rotation),
and its ring Z[c_S] in End(P(S)).

  A CUSP QUANTIZATION of the object by S := a nonzero Z-linear map
     j : Lambda_cusp -> P(S)
  together with a unital ring embedding
     iota : Q(tau) = Q(sqrt-3)  ->  End_Q(P tensor Q),
  such that (i) iota lands in the stage-structure-preserving
  endomorphisms = the commutant of c_S, and (ii) j(alpha.v) =
  iota(alpha).j(v)  (equivariance).  Conformality of j w.r.t. the two
  quadratic forms is REQUIRED only up to one overall scale (the cusp
  shape is defined up to scale).

Why the commutant of the Coxeter ring is the canonical equivariance
scale (and not something looser or tighter):
  - full-Weyl commutant: W acts irreducibly on P tensor R for every
    A_n, so the W-commutant is Q -- equivariance would be impossible
    for EVERY stage (too tight; selects nothing).
  - bare Q-linearity: any rank-2 subspace works for EVERY stage (too
    loose; selects nothing).
  - the Coxeter ring Z[c_S] is the unique intermediate canonical
    arithmetic: it is exactly what makes the A_{n-1} lattice
    cyclotomic (A_{n-1} = Z[zeta_n] as a Z[c]-module), i.e. the
    stage's own 'complex structure' -- the mirror of the cusp's CM.
This choice is PART of the principle (see the gap statement, Part F).

D3 (the lemma to decide).  Does a cusp quantization exist for
S = SU(3)_2 (A2) and fail for S = SU(5)_1 (A4)?
""")

# ---------------------------------------------------------------------------
sec("PART B -- THE CUSP SIDE, EXACT: the peripheral lattice of the object")

print("\nB1. The discrete faithful rep over Q(sqrt-3) (exact).")
A2x2 = Matrix([[1, 1], [0, 1]])
Ai = A2x2.inv()
Bm = Matrix([[1, 0], [c, 1]])
Bi_ = Bm.inv()

# two-bridge S(5,3) presentation of the figure-eight: a w = w b,
# w = b a^-1 b^-1 a  (e_i = (-1)^floor(3i/5) = +,-,-,+)
W = Bm * Ai * Bi_ * A2x2
eqs = list(expand(A2x2 * W - W * Bm))
sols = solve(eqs, c)
print("  presentation: <a, b | a w = w b>, w = b a^-1 b^-1 a  (S(5,3))")
print("  rho(a) = [[1,1],[0,1]], rho(b) = [[1,0],[c,1]]; solve the relation:")
print("  solutions c =", sols)
csol = None
for s in sols:
    sv = s[0] if isinstance(s, (tuple, list)) else s
    if im(sv) != 0:
        csol = sv
        break
assert csol is not None, "no nonabelian solution found"
mp = minimal_polynomial(csol, x)
print("  chosen nonabelian root c =", csol, "; minimal polynomial:", mp)
print("  => the rep is defined over Q(sqrt-3) -- the cusp field (banked).")

print("\nB2. The longitude, found by bounded search (floats, NON-DECISIVE),")
print("    then verified EXACTLY (decisive).")

cnum = complex(csol.evalf())
mats = {
    'a': ((1, 1), (0, 1)),
    'A': ((1, -1), (0, 1)),
    'b': ((1, 0), (cnum, 1)),
    'B': ((1, 0), (-cnum, 1)),
}
inv_of = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}


def mul(m, n):
    return ((m[0][0] * n[0][0] + m[0][1] * n[1][0],
             m[0][0] * n[0][1] + m[0][1] * n[1][1]),
            (m[1][0] * n[0][0] + m[1][1] * n[1][0],
             m[1][0] * n[0][1] + m[1][1] * n[1][1]))


MAXLEN = 11
frontier = [(ltr, mats[ltr], 1 if ltr in 'ab' else -1) for ltr in 'aAbB']
hits = []
for L in range(1, MAXLEN + 1):
    for word, m, es in frontier:
        if abs(m[1][0]) < 1e-8 and abs(abs(m[0][0]) - 1) < 1e-8 \
                and abs(m[0][0].imag) < 1e-8:
            hits.append((word, m[0][1] / m[0][0], es))
    if L == MAXLEN:
        break
    new = []
    for word, m, es in frontier:
        last = word[-1]
        for ltr in 'aAbB':
            if ltr == inv_of[last]:
                continue
            new.append((word + ltr, mul(m, mats[ltr]),
                        es + (1 if ltr in 'ab' else -1)))
    frontier = new

tau_im = None
best = None
for word, tr, es in hits:
    if abs(tr.imag) > 0.1:
        if tau_im is None or abs(tr.imag) < tau_im - 1e-6:
            tau_im = abs(tr.imag)
            best = (word, tr, es)
print(f"  BFS over reduced words, length <= {MAXLEN}: "
      f"{len(hits)} peripheral elements found")
print(f"  minimal nonzero imaginary translation: {tau_im:.9f} "
      f"(2*sqrt(3) = {2*3**0.5:.9f})")
print("  witness word:", best[0], " translation ~", best[1],
      " exponent sum", best[2])

# lattice corroboration: every found translation lies in Z + Z*tau
worst = 0.0
for word, tr, es in hits:
    n = tr.imag / best[1].imag
    mres = tr.real - round(tr.real - round(n) * best[1].real
                           ) if False else None
    # coordinates in basis (1, tau_found):
    nn = round(tr.imag / best[1].imag)
    mm = round(tr.real - nn * best[1].real)
    res = abs(tr - (mm + nn * best[1]))
    worst = max(worst, res)
print(f"  lattice corroboration: all {len(hits)} translations lie in "
      f"Z + Z*tau, worst residual {worst:.2e}  [NON-DECISIVE]")

print("\n  EXACT verification of the witness longitude word (decisive):")
exact = {'a': A2x2, 'A': Ai, 'b': Bm.subs(c, csol), 'B': Bi_.subs(c, csol)}
Lmat = eye(2)
for ltr in best[0]:
    Lmat = Lmat * exact[ltr]
Lmat = Lmat.applyfunc(lambda e: radsimp(simplify(e)))
print("  rho(word) =", Lmat.tolist())
assert simplify(Lmat[1, 0]) == 0, "not upper triangular"
assert simplify(Lmat[0, 0] ** 2) == 1, "diagonal not +-1"
tau_exact = simplify(Lmat[0, 1] / Lmat[0, 0])
print("  exact translation:", tau_exact)
tau_red = simplify(tau_exact - re(tau_exact))
print("  modulo the meridian (translation 1):  tau =", tau_red,
      " = +-2*sqrt(-3)  [matches the banked cusp modulus, B637/B598]")
assert simplify(tau_red ** 2 + 12) == 0, "tau^2 != -12"

print("""
  (classical anchor: the peripheral subgroup of a knot group is
   exactly Z^2 = <meridian, longitude>, and the parabolic-fixed-point
   stabilizer realizes it as the translation lattice.  With the exact
   meridian translation 1 and exact longitude translation +-2 sqrt-3
   above:)""")

print("\nB3. THE CUSP LATTICE, exact:")
tau_s = 2 * sqrt(-3)
print("  Lambda_cusp = Z.1 + Z.(2 sqrt-3)   (sign/Z-shift do not change it)")
G_cusp = Matrix([[1, 0], [0, 12]])
print("  Gram (form Re(z w-bar)):", G_cusp.tolist(), "; disc =", G_cusp.det())
print("  Note |tau|^2 = N(2 sqrt-3) = 12 = |disc|.")
# multiplier ring: alpha = p + q sqrt-3 with alpha*Lambda in Lambda:
#   alpha*1 = p + (q/2)(2 sqrt-3)      -> p in Z, q in 2Z
#   alpha*(2 sqrt-3) = -6q + p(2 sqrt-3) -> automatic
al1 = (p + q * sqrt(-3)) * 1
al2 = expand((p + q * sqrt(-3)) * tau_s)
print("  multiplier check: alpha.1 =", al1, " -> coords (p, q/2) in basis",
      "(1, 2sqrt-3): need p in Z, q in 2Z")
print("                    alpha.tau =", al2, " -> coords (-6q, p): automatic")
print("  => End(Lambda_cusp) = Z + Z.(2 sqrt-3) = Z[2 sqrt-3] = Lambda_cusp")
print("     (the cusp lattice IS an order in the cusp field Q(sqrt-3):")
print("      closed under multiplication -- tau^2 =", simplify(tau_s**2), ")")
d_order = Poly(x ** 2 + 12, x).discriminant()
print("  disc Z[2 sqrt-3] =", d_order, "= 4^2 . (-3)  -> CONDUCTOR 4 in the")
print("  maximal order Z[omega] (Eisenstein), disc -3.")
# saturation
print("  saturation by the maximal order: Z[omega].Lambda_cusp contains")
print("  Z[omega].1 = Z[omega]; and (2 sqrt-3)Z[omega] subset Z[omega];")
print("  => saturation = Z[omega] exactly (index 1).")
omega_basis = Matrix([[1, 0], [2, 4]])   # 1, 2+4w in basis (1, w); sqrt-3=1+2w
print("  index [Z[omega] : Lambda_cusp]: 2 sqrt-3 = 2 + 4 omega, basis matrix",
      omega_basis.tolist(), "-> index =", abs(omega_basis.det()), "(= conductor... see below)")
chk = expand((1 + 2 * Rational(-1, 2) + 2 * sqrt(-3) * Rational(1, 2)))
sq = expand((Rational(-1, 2) + sqrt(-3) / 2) ** 2 + (Rational(-1, 2) + sqrt(-3) / 2) + 1)
print("  (check: omega = (-1+sqrt-3)/2 satisfies omega^2+omega+1 =",
      simplify(sq), "; sqrt-3 = 1 + 2 omega )")

print("""
  SUMMARY (cusp side, exact):
   Lambda_cusp = the order Z[2 sqrt-3], conductor 4, in Q(sqrt-3);
   Gram [[1,0],[0,12]], disc 12; CM field = Q(sqrt-3) = Q(omega);
   its maximal-order saturation = Z[omega] = the Eisenstein lattice.""")

# ---------------------------------------------------------------------------
sec("PART C -- THE A2 STAGE (SU(3)_2): the canonical map EXISTS (exact)")


def simple_reflections(cartan):
    n = cartan.shape[0]
    out = []
    for i in range(n):
        S = eye(n)
        for j in range(n):
            S[j, i] = (1 if i == j else 0) - cartan[j, i]
        out.append(S)
    return out


C_A2 = Matrix([[2, -1], [-1, 2]])
GP2 = C_A2.inv()
print("\nC1. weight-lattice Gram (fundamental-weight basis) = C^-1 =",
      GP2.tolist(), "; disc =", GP2.det(), "; P/Q = Z/3 (det C = 3)")
S1, S2 = simple_reflections(C_A2)
cox2 = S1 * S2
print("C2. Coxeter element c = s1 s2 =", cox2.tolist())
cp2 = cox2.charpoly(x).as_expr()
print("    char poly:", cp2, " (= Phi_3; h = 3)")
assert cp2 == x ** 2 + x + 1
assert simplify(cox2.T * GP2 * cox2 - GP2) == Matrix([[0, 0], [0, 0]])
print("    c is orthogonal for the Gram form; det c =", cox2.det())
Z3 = 2 * cox2 + eye(2)
print("    (2c + 1)^2 =", (Z3 * Z3).tolist(), " = -3.I  -- sqrt(-3) LIVES IN Z[c]")
assert Z3 * Z3 == -3 * eye(2)
# commutant
M11, M12, M21, M22 = symbols('M11 M12 M21 M22')
Mm = Matrix([[M11, M12], [M21, M22]])
comm_sols = solve(list(Mm * cox2 - cox2 * Mm), [M11, M12, M21, M22])
print("    commutant of c: solve Mc = cM ->", comm_sols,
      " -> 2 free parameters -> commutant = Q[c] = Q(sqrt-3).  EXACT.")

print("\nC3. THE CANONICAL MAP j : Lambda_cusp -> P(A2).")
v = Matrix([1, 0])            # omega_1
cv = cox2 * v
genmat = Matrix.hstack(v, cv)
print("    generator: v = omega_1; det[v | c v] =", genmat.det(),
      " -> P is FREE of rank 1 over Z[c] (P = Z[c].v = Z[zeta_3])")
u = (4 * cox2 + 2 * eye(2)) * v      # iota(2 sqrt-3) v
jm = Matrix.hstack(v, u)
print("    j: 1 |-> v,  2 sqrt-3 |-> iota(2 sqrt-3).v = (4c+2)v =",
      u.T.tolist()[0])
print("    image basis matrix [j(1) | j(tau)] =", jm.tolist(),
      "; index in P =", abs(jm.det()), " (= the conductor 4 of the cusp order)")
g11 = (v.T * GP2 * v)[0]
g12 = (v.T * GP2 * u)[0]
g22 = (u.T * GP2 * u)[0]
print("    Gram of the image: [[", g11, ",", g12, "],[", g12, ",", g22, "]]",
      "= (2/3) . [[1,0],[0,12]]  -- CONFORMAL, one scale 2/3")
assert (g11, g12, g22) == (Rational(2, 3), 0, 8)
print("""    equivariance: by construction j(alpha.z) = iota(alpha).j(z) with
    iota(sqrt-3) = 2c+1  (the other embedding -(2c+1) = the complex-
    conjugate/orientation choice -- exactly the banked zeta_6-unit
    ambiguity of B637's omega').
    saturation: Z[c].j(Lambda_cusp) = Z[c].v = P  (det +-1 above)
    -- the maximal-order saturation of the cusp lattice IS the full
    weight lattice.  The map is canonical: unique up to the stage's
    lattice units Z[c]^* = {+-c^k} (the hexagon), the Galois pair, and
    the one conformal scale.

    => CUSP QUANTIZATION BY THE A2 STAGE EXISTS -- explicitly.""")

print("C4. level-2 conductor compatibility (kappa = 5 = the conductor):")
p5 = Poly(t ** 2 + t + 1, t, modulus=5)
print("    Phi_3 mod 5 irreducible?", p5.is_irreducible,
      " -> 5 is INERT in Z[omega]: P/5P = F_25, an irreducible F_5[c]-plane")
print("    gcd(index 4, kappa 5) =", gcd(4, 5),
      " -> j mod 5 : Lambda_cusp/5 -> P/5P is an ISOMORPHISM of F_5-planes")
print("    -- the canonical map is invertible exactly at the conductor:")
print("    the cusp torus's mod-5 points ARE the stage's mod-5 plane,")
print("    the home of B644's SL(2,F5) shadow.  [exact remark]")

# ---------------------------------------------------------------------------
sec("PART D -- THE A4 STAGE (SU(5)_1): the canonical map CANNOT EXIST (exact)")

C_A4 = Matrix([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
GP4 = C_A4.inv()
print("\nD1. weight Gram = C^-1 (4x4), disc =", GP4.det(),
      "; det C =", C_A4.det(), " -> P/Q = Z/5")
refl = simple_reflections(C_A4)
cox4 = refl[0] * refl[1] * refl[2] * refl[3]
cp4 = cox4.charpoly(x).as_expr()
print("    Coxeter element c4 = s1 s2 s3 s4; char poly:", cp4)
assert cp4 == x ** 4 + x ** 3 + x ** 2 + x + 1, "char poly != Phi_5"
print("    = Phi_5 (h = 5): Z[c4] = Z[zeta_5]; the A4 lattice is the")
print("      zeta_5-cyclotomic lattice -- weight-lattice field Q(zeta_5).")
assert simplify(cox4.T * GP4 * cox4 - GP4).norm() == 0
print("    c4 orthogonal for the Gram form; det c4 =", cox4.det())

print("\nD2. the commutant of c4 (where iota must land):")
ms = symbols('m0:16')
Mm4 = Matrix(4, 4, ms)
csol4 = solve(list(Mm4 * cox4 - cox4 * Mm4), list(ms))
free = 16 - len(csol4)
print("    solve M c4 = c4 M: ", len(csol4), "constrained of 16 ->",
      free, "free parameters")
assert free == 4
pows = [eye(4), cox4, cox4 * cox4, cox4 ** 3]
pmat = Matrix.hstack(*[Matrix(16, 1, list(P)) for P in pows])
print("    I, c4, c4^2, c4^3 rank:", pmat.rank(),
      " -> commutant = Q[c4], a FIELD = Q(zeta_5) (Phi_5 irreducible).")

print("\nD3. is there z in Q[c4] with z^2 = tau^2 = -12 (or -3)?  EXACT NO:")
Phi5 = Poly(t ** 4 + t ** 3 + t ** 2 + t + 1, t)
print("    (i) Phi_5 irreducible over Q:",
      Poly(Phi5.as_expr(), t).factor_list()[1][0][0].degree() == 4)
for k in (2, 3, 4):
    r = rem((t ** k) ** 4 + (t ** k) ** 3 + (t ** k) ** 2 + t ** k + 1,
            Phi5.as_expr(), t)
    assert simplify(r) == 0
print("    (ii) t^k (k=2,3,4) are again roots mod Phi_5 -> the field is")
print("         GALOIS over Q; group = (Z/5)^* (t -> t^k), cyclic of")
print("         order 4 (generated by 2: 2,4,3,1 mod 5).")
print("    (iii) a cyclic C4 has EXACTLY ONE subgroup of order 2 (k=4),")
print("          hence exactly one quadratic subfield.")
eta_sq_rel = rem(expand((t + t ** 4) ** 2 + (t + t ** 4) - 1),
                 Phi5.as_expr(), t)
print("    (iv) eta = t + t^4 (fixed by k=4): eta^2 + eta - 1 =",
      simplify(eta_sq_rel), "mod Phi_5")
print("         -> the unique quadratic subfield = Q(eta) = Q(sqrt5), REAL.")
sol_m12 = solve([2 * p * q - q ** 2, p ** 2 + q ** 2 + 12], [p, q],
                dict=True)
rat_m12 = [s for s in sol_m12 if all(val.is_rational for val in s.values())]
sol_m3 = solve([2 * p * q - q ** 2, p ** 2 + q ** 2 + 3], [p, q], dict=True)
rat_m3 = [s for s in sol_m3 if all(val.is_rational for val in s.values())]
print("    (v) z = p + q.eta with z^2 = -12: (p^2+q^2) + (2pq - q^2) eta")
print("        = -12  ->  {q(2p-q) = 0, p^2 + q^2 = -12}:")
print("        q = 0 -> p^2 = -12 (no rational); q = 2p -> 5p^2 = -12 (no).")
print("        rational solutions found by sympy:", rat_m12, " (empty)")
print("        same for z^2 = -3: rational solutions:", rat_m3, " (empty)")
assert rat_m12 == [] and rat_m3 == []
print("""    (vi) CONCLUSION: any z with z^2 = -12 would generate a quadratic
         subfield isomorphic to Q(sqrt-3); the only quadratic subfield
         of Q(zeta_5) is the REAL field Q(sqrt5), which contains no
         square root of a negative rational.  NO SUCH z EXISTS.""")

try:
    from sympy import factor as _factor
    f_pos = _factor(x ** 2 + 3, extension=sqrt(-3))
    print("    positive control: x^2+3 over Q(sqrt-3):", f_pos, " (splits)")
except Exception as e:
    print("    positive control skipped:", e)

print("""
D4. THE NONEXISTENCE, assembled:
    a cusp quantization (D2) of the object by SU(5)_1 requires
    iota : Q(sqrt-3) -> commutant(c4) = Q[c4] = Q(zeta_5), unital,
    with iota(2 sqrt-3)^2 = -12.  By D3 no element of Q(zeta_5)
    squares to -12 (or -3).  Hence iota does not exist; a fortiori no
    nonzero equivariant j exists (equivariance would make ker j an
    iota-stable subspace of the 1-dimensional Q(sqrt-3)-line
    Lambda_cusp tensor Q, so j nonzero would be injective and force
    iota).  EXACT, no float content.

    (Field-door contrast, cf. the W32 SU(6)_1 exclusion: this is NOT
    the cyclotomic-field door -- SU(5)_1's full modular field Q(zeta_30)
    DOES contain sqrt-3.  The obstruction is the WEIGHT LATTICE's own
    arithmetic Z[c4] = Z[zeta_5]: the stage's torus has no room for the
    cusp's complex multiplication.  The lattice, not the ambient
    cyclotomic field, is the discriminating structure -- exactly as the
    task's candidate discharge proposed.)""")

# ---------------------------------------------------------------------------
sec("PART E -- THE TWO-LATTICE PICTURE (exact remark, unification)")
print("""
  The object carries exactly two rank-2 arithmetic lattices:
   - the FIBER lattice H_1(T^2) = Z^2 with the Anosov cat-map action:
     REAL multiplication by Z[phi], field Q(sqrt5) (eigenvalues
     phi^{+-2}; the trace field side);
   - the CUSP lattice Lambda_cusp = Z[2 sqrt-3]: COMPLEX
     multiplication, field Q(sqrt-3)  (this cell, exact).
  The two surviving stages split these two structures:
   - SU(3)_2: Coxeter/weight-lattice field Q(sqrt-3) = THE CUSP FIELD
     (exact match, Part C), and the hearing values in Q(sqrt5) enter
     through kappa = 5 = the conductor (B644/B620);  -> BOTH of the
     object's quadratic fields are realized, each in its proper slot.
   - SU(5)_1: weight-lattice field Q(zeta_5) contains Q(sqrt5) (eta =
     zeta+zeta^4, Part D3(iv)) -- the FIBER side only; the cusp field
     cannot enter the lattice (Part D).  The partner stage hears the
     object's trace arithmetic but cannot quantize its cusp.
  The tiebreak, in one sentence: the ear stage is the one whose torus
  is built on the object's OWN cusp arithmetic.""")

# ---------------------------------------------------------------------------
sec("PART F -- VERDICT AND THE PRECISE GAP")
print("""
LEMMA (PROVEN, exact, both directions -- the dichotomy):
  With cusp quantization as formalized in D2 (equivariance w.r.t. the
  cusp CM through the commutant of the stage's Coxeter ring, conformal
  up to one scale):
  (i)  A2 (in particular SU(3)_2): a cusp quantization EXISTS and is
       canonical -- j : Z[2 sqrt-3] -> P(A2), 1 |-> omega_1,
       2 sqrt-3 |-> (4c+2).omega_1; conformal with scale 2/3; image of
       index 4 = the conductor of the cusp order; maximal-order
       saturation = the FULL weight lattice; at the selected level
       (kappa = 5 = the conductor) its mod-5 reduction is an
       isomorphism onto the stage's mod-5 plane F_25 -- the home of
       the banked SL(2,F5) shadow (B644).
  (ii) A4 (SU(5)_1): NO cusp quantization exists: the commutant of the
       Coxeter ring is the field Q(zeta_5), whose unique quadratic
       subfield is the real Q(sqrt5); no element squares to
       tau^2 = -12.  Exact.

CONSEQUENCE (conditional completion): under the principle

  H-CUSP: the bearing stage must quantize the object's cusp torus
          (in the D2 sense),

stage selection completes from the pair {SU(3)_2, SU(5)_1} to the
single stage SU(3)_2; by D1 (branch == stage, banked pair assignment,
W32 Part 4) the object couples through the ear branch 2h' with tone
-1/phi.  THE BRANCH TIEBREAK IS DISCHARGED MODULO H-CUSP.

THE PRECISE GAP (named, honest):
  g1: H-CUSP itself -- WHY bearing requires quantizing the cusp -- is
      not derived from H-EAR; it is the exact analogue, one level up,
      of H-EAR's own status (W32).  The candidate unification (Part E,
      recorded): one principle, 'the stage realizes the object's two
      rank-2 arithmetic structures in the two stage slots (weight
      lattice <- cusp CM; conductor/level <- fiber RM)'.
  g2: inside D2, the identification 'stage-structure-preserving
      endomorphisms = commutant of the Coxeter ring' is the
      formalization choice (motivated in Part A: the W-commutant is
      too tight for every stage, bare Q-linearity too loose; the
      Coxeter ring is the unique intermediate canonical arithmetic and
      is what makes A_{n-1} = Z[zeta_n]).  A future derivation of g1
      should produce this ring, not posit it.

Nothing here touches physics; kappa = 5 stays a conductor statement.
""")
print("DONE")
