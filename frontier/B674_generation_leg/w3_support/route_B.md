# ROUTE B — the Nahm / state-integral support pre-test at zeta_5
# (INDEPENDENT of the block-eigenvalue phi^{4k} route; sealed base 83c50a35)
# All arithmetic exact (sympy) / high-precision (mpmath); see route_B_compute.py
# (26/26 PASS). Base-rate discipline: a near-miss would be reported NO-HIT.

## MANDATE
Using ONLY the GZ 1.7 t-deformed Nahm ring
  S = Z[t^{+-1}, z^{+-1}(t), delta(t)^{-1/2}] / (1 - z - (-1)^A t z^A),
compute the q-power support of the state-integral series at zeta_5, and the
effect of the block decomposition + tau-pairing. DECISIVE: after the fixed
delta(t)^{-1/2} (the sqrt(-delta) freedom) and eta bookkeeping, which classes
mod 1 survive at zeta_5 -- {2/5,3/5}, all four, or {1/5,4/5}?

## B0 — THE 4_1 GOLDEN NAHM DATUM FROM THE RING (derived, not imported)
The ring relation with A = 2 (rank-1) is  1 - z - t z^2 = 0.
  - discriminant in z:  delta(t) = 1 + 4t.
  - delta(1) = 5  -> sqrt(-delta) = i*sqrt5; the SQRT5 / golden structure is
    intrinsic to the Nahm datum, NOT put in by hand.
  - two saddles (two flat connections): z_+- = (-1 +- sqrt5)/2  = {1/phi, -phi}.
This is the golden/Rogers-Ramanujan Nahm system: the A=2 rank-1 sum is the
(2,5) (Lee-Yang / Fibonacci) object. Independent of any phi^{4k} eigenvalue.

## B1 — c_eff = 2/5 FROM THE ROGERS DILOGARITHM (independent of phi^{4k})
Saddle of sum_n q^{n^2}/(q)_n :  1 - X = X^2  =>  X = 1/phi.
Correct saddle bookkeeping: with Psi(X) = (ln X)^2 + Li_2(X) - pi^2/6 and the
identity L(X*) = Li_2(X*) + (ln X*)^2 (uses 1-X* = X*^2), the growth is
exp(-Psi/t) with -Psi(X*) = pi^2/6 - L(X*) = pi^2 c_eff/6, hence
  c_eff = 1 - (6/pi^2) L(1/phi) = 1 - (6/pi^2)(pi^2/10) = 2/5.
L(1/phi) = pi^2/10 verified to 50 digits. This 2/5 is computed from the Nahm
saddle + dilogarithm ALONE (no block eigenvalues).

## B2 — ETA BOOKKEEPING
eta^{48/5} carries q^{48/(5*24)} = q^{2/5}, and 48/5 = 24*c_eff exactly: the
universal eta-dressing = eta^{24 c_eff} places the base component at class 2/5.
(This ties the banked eta^{48/5} to the INDEPENDENTLY computed c_eff = 2/5.)

## B3 — THE TWO RR NAHM SUMS (the orbit datum) 
G = sum q^{n^2}/(q)_n = prod 1/((1-q^{5n+1})(1-q^{5n+4}))       (denom {1,4})
H = sum q^{n^2+n}/(q)_n = prod 1/((1-q^{5n+2})(1-q^{5n+3}))     (denom {2,3})
Both verified to q^60. CRUCIAL: both products are INTEGER-power series, so
their class mod 1 = {0}. The {1,4} vs {2,3} distinction lives in the
denominator progressions, and is INVISIBLE to a class-mod-1 test. Therefore
the fractional class support cannot come from the RR products themselves; it
comes entirely from the DRESSING (c_eff + the per-component exponent nu).

## B4/B5 — THE DOUBLET GAP = 1/5 (two independent derivations)
(a) The banked pairing gives comp2/comp1 = R(q) = q^{1/5}*(unit series) (RR
    continued fraction; H/G verified a unit power series). Leading power q^{1/5}
    => the two dressed components differ by class 1/5.
(b) (2,5) minimal-model Kac weights h_{1,1}=0, h_{1,2}=-1/5 (Lee-Yang): gap =
    1/5; and c - 24 h_min = -22/5 + 24/5 = 2/5 reproduces B1's c_eff.
The gap is 1/5, NOT 3/5. (Gap 3/5 is what would produce {1/5,4/5}.)

## B6 — WHICH CONJUGATION-ORBIT: the golden monodromy is a class-{2,3} quantity
phi = -2 cos(4 pi/5) = 2 cos(pi/5). The angle 4 pi/5 is that of zeta5^2 (class 2,
and its conjugate class 3). The CONJUGATE embedding 1/phi = 2 cos(2 pi/5) sits at
class 1 (and 4). Hence the golden monodromy lambda = phi^2 belongs to the {2,3}
sector; the {1,4} sector is the arithmetic conjugate 1/phi^2. This is why the
golden block decomposition selects {2,3} and not {1,4} -- read off which root of
unity phi actually is, independent of the phi^{4k} eigenvalue arithmetic.

## B7 — DECISIVE UNIQUENESS (the tau-pairing closes the argument)
The tau-pairing (q -> 1/q) forces the support to be closed under class -> -class
(mod 1), i.e. conjugation-symmetric. Enumerate 2-element fifth-class doublets
{a, a+gap} that are conjugation-symmetric:
  - gap 1/5  ->  {2/5, 3/5}  (UNIQUE)
  - gap 2/5  ->  {1/5, 4/5}
  - gap 3/5  ->  {1/5, 4/5}
Since the gap is 1/5 (B4/B5), the ONLY conjugation-symmetric fifth-doublet is
{2/5, 3/5}. The base component sits at c_eff = 2/5 (B1/B2), the second at
2/5 + 1/5 = 3/5. Both land inside the single conjugation-orbit {2,3}.

## B8 — VERDICT (two-outcome, as in Route A)
Support classes mod 1, assembled from INDEPENDENT Nahm inputs
  { c_eff + nu_a : nu = (0, 1/5) } = { 2/5, 3/5 }.

  LANDS {2/5, 3/5}.  (Not all four; not {1/5,4/5}.)

Mechanism (Galois/field, computed): the A=2 Nahm datum forces delta(1)=5 and the
golden/(2,5) system; the Rogers dilog forces c_eff = 2/5 (= the eta^{48/5} shift);
the (2,5) Kac gap / RR continued fraction forces the doublet gap = 1/5; the
tau-pairing forces conjugation-symmetry. The unique conjugation-symmetric
fifth-doublet with gap 1/5 is {2/5,3/5}. All four is excluded because the golden
block reduces the four-class orbit to the rank-2 (2,5) sector (phi^2 is a class-
{2,3} quantity, B6); {1/5,4/5} is excluded because that requires gap 3/5, whereas
the RR/(2,5) gap is 1/5.

## HONEST CAVEAT (what rests on structure vs. from-scratch computation)
The class-DETERMINING numbers -- c_eff = 2/5 and gap = 1/5 -- are each computed
from scratch on the Nahm side (dilogarithm; Kac table / RR continued fraction),
independent of the phi^{4k} route, and both point to {2/5,3/5}. Two structural
links are argued rather than computed as a from-scratch 4x4 object: (i) that the
tau-paired reduced series has integer base support (the fractional data is purely
c_eff + nu) -- consistent with 4_1 amphichirality (tau-invariance) and with
Route A's integer-support Molien product; (ii) the four->two reduction to the
{2,3} sector via B6. Neither link, if made fully explicit, can move the landing
off {2/5,3/5} without contradicting the computed gap=1/5 and c_eff=2/5. This is a
genuine LANDS, not a forced near-miss.

## TWO-SEAT STATUS — DISAGREEMENT (checked AFTER Route B was computed)
Route A (the independent phi^{4k}/Galois seat, route_A.md, same base 83c50a35)
returns ALL FOUR, not {2/5,3/5}: it finds every block eigenvalue phi^{4k} (in
Q(sqrt5), H-fixed) has zeta5-content on all four classes, so the Galois-covariant
support of Phi.tauPhi is the full orbit {1,2,3,4}; only phi^{+-1} would give a
clean 2-class support, and the blocks do not supply that.

=> The two seats DISAGREE. Per the sealed gate ("Disagreement => STOP + diagnose;
the shot is NOT fired on a disagreement") this is NOT a passed support pre-test.

THE EXACT CRUX (the diagnosis): the two routes use different notions of "q-power
class mod 1".
  - Route B: the fractional class is the LEADING q-exponent of each holomorphic
    block, = the modular prefactor c_eff + conformal weight (2/5, then +1/5). The
    block eigenvalues phi^{4k} are COEFFICIENTS, they do not move the q-exponent's
    fractional part. On this reading the class is set by the (2,5)/RR modular data
    and lands {2/5,3/5}.
  - Route A: the fractional class is carried by the zeta5-content of the block
    eigenvalues phi^{4k}, which fills all four classes => all four.
These cannot both be the operative definition. Which one is the genuine "q-power
support class of Phi.tauPhi" must be resolved (is the twisted character expanded
as a modular form with a q^{c_eff} prefactor, or as a zeta5-graded eigenvalue
sum?) BEFORE the support pre-test can be called PASS or FAIL. Route B's own
computation is internally sound and lands {2/5,3/5}; it does not, by itself,
license firing the shot while Route A stands.
