# B1446 — THE PARABOLIC POINTS AND THE BRANCH POINTS on the root's three-fold cover: where the frame's own boundary condition leaves no parameter, the torsions are exact numbers in ℚ(√5, √−3); the index there is zero; and a second member's Higgs can be switched on along the first's curve at exactly six points

cc, 2026-10-01. B1444 and B1445 gave the extension and the Higgs value an object — positions on two curves of flat
connections — and left both positions free. The owner approved an order of work whose first item is what tells
the three members of a deck orbit apart. This arc computes, on the root's three-fold cover s961 where the formulas
are exact, the two things that question needs first: what sits at the points where the positions are *not* free,
and where one member's curve meets another member's Higgs. **Verdict: PROVED** (computed, exact where stated; one
hope refuted). One level; no population, so no seal.

## 1. The parabolic points

The frame imposes unipotent peripheral holonomy at a background. On a periodic curve only finitely many points have
parabolic or trivial peripheral holonomy in PSL(2): the reducible end, and the points with κ = −2.

- For a character of order four the curve is a rational quartic and κ = −2 at two complex-conjugate points, the
  **complete-cusp points** of B1444 §2 (w² − w + 4 = 0, coordinates in ℚ(√5, √−3)). Reached here on all twelve
  curves by continuation round the branch point of κ on either side; X satisfies B1444's minimal polynomial to
  10⁻⁵⁹ and the meridian is parabolic (trace 2) on all 24.
- For a character of order two the curve is a line and κ = −2 at one point, the quaternion point (0, 0, 0), where
  the representation has finite image.

## 2. The sectors at the complete-cusp points (`parabolic.py sectors`, record `parabolic_sectors.json`)

All 14 doublet sectors on each of the 12 curves at both points, 336 torsions; they depend only on the sector's
class:

| the sector at the reducible end (B1444) | torsion at the complete cusp | modulus |
|---|---|---|
| one match, coefficient 1/2 — **the generation's sectors** (the six sectors of all 48 backgrounds) | **−√5 ± √−3** | 2√2 |
| no match, first-order coefficient 2 | √5 ± √−3 | 2√2 |
| one match, coefficient 3/4 | −2.3117… ± 0.0818… i | 2.3132… |
| no match, first-order coefficient 4 | 6.1861… ± 2.2520… i | 6.5833… |
| two matches, order three | −0.7697… ± 5.7162… i | 5.7677… |

The first two are identified exactly (integer relations at 45 digits). The other three do not lie in ℚ(√5, √−3);
their field (it contains the square root that B1444's Z needs) is not identified here.

## 3. The bidoublet at the parabolic points of the product (`parabolic.py bidoublet`, six records)

All 96 couplings of the 48 backgrounds (48 of up type through a Higgs character of order four; 48 of down, lepton
and neutrino type through one of order two), at every combination of parabolic points of the two curves, 816
evaluations.

| extension | Higgs | points | class index | cohomology | torsion |
|---|---|---|---|---|---|
| complete cusp | complete cusp | 288 | **0 on all** | h¹ = t₀ (1 for up, 2 for the others), no interior class, for the module and its dual | 0 |
| end | complete cusp, up | 96 | 0 | none | **2 ± 2√−15 = (√5 ± √−3)²**, modulus 8 |
| end | quaternion point, down / lepton / neutrino | 48 | 0 | none | **16** |
| complete cusp | end | 192 | 0 | none | modulus 8 |

- **The index at the doubly-parabolic points is zero.** There the two signs of the longitudes cancel in the tensor
  product, the cusp holonomy on the bidoublet is unipotent again and has invariants, and the module is irreducible
  and not unitary, so nothing forces its class index to vanish; it was computed (ranks by singular values at 60
  digits; smallest kept 0.074, largest dropped 8·10⁻⁶⁰) and it vanishes: the classes present are exactly those the
  boundary forces. **A hope refuted:** an irreducible background carrying the frame's index would have removed the
  fence on non-semisimple backgrounds. It does not exist among these 288 points.
- **With the extension at its end and the Higgs at its complete point the bidoublet is acyclic and its torsion is a
  fixed number,** the same for every background: (√5 ± √−3)² for the up coupling and 16 for the down, lepton and
  neutrino couplings. (The end is taken at e = 10⁻¹⁴, so these are certified to 10⁻¹³; the value is the product of
  the two sector torsions of §2.)

## 4. The branch points (`branch_points.py`, record `branch_points.json`)

The three Higgs characters of a deck orbit have trivial product and equal slopes (checked on the orbit of (2, 1):
(2, 1), (1, 3), (1, 0)). On the curve of the first, the doublet sector with characters (η₀η₁, η₁) is doubly
matched — and the doubly matched sectors on that curve are exactly the two belonging to the other two members. A
class of that sector at a point of the curve is a first-order direction in which the second member's Higgs is
switched on while the first is on.

B1444's exact record gives the product N of that sector's torsions for the two signs of the meridian:
N = 8√2·Z·P₅(u)/u² + R₆(u)/u³, and N = 0 forces

    R₆² − 128(u² + 1)P₅² = 16·(u − 1)⁴·(u + 1)²·(u⁶ − 8u⁴ + 12u³ + 4) = 0.

So the sector has a class only at the two reducible ends and at the six roots of the irreducible sextic

    u⁶ − 8u⁴ + 12u³ + 4 = 0        (discriminant 2²³·13·17²;  w = u − 1/u satisfies 4w⁶ − 8w⁴ + 36w³ − 100w² + 204w − 135 = 0),

verified numerically: at each root the torsions of the two doubly matched sectors (the other two members') vanish
to 10⁻³⁰ for one sign of the meridian, and that of no other sector does.

- Two roots are real. **u = −0.62070…, w = 0.99037…, κ = 1.99046…** lies on the real arc of the curve between the
  root's background and the sister's (B1444 §2), where the representations have real traces and κ < 2, and the
  vanishing is for the meridian normalised as the frame normalises it (tending to 1 at the end along the arc). The
  other, u = −3.3922…, has κ = 14.69 and the opposite sign of the meridian, as have the four complex roots.
- So along one member's Higgs curve a second member's Higgs cannot be switched on at a generic point, and can at
  six algebraic points, one of them on the arc of real representations just before the sister's end.

## 5. What it means, and the fence

- **The parameters of B1444 and B1445 are not free once the frame's boundary condition is imposed on the
  irreducible connections too:** each curve then has finitely many points, and at them the torsions are algebraic
  numbers. On the root's three-fold cover the generation's sectors give −√5 ± √−3 and the up coupling its square.
  The two square roots are those of the object's two fields; here they occur in one number at one point. That is
  recorded as a fact, not read.
- **Where the members of an orbit can differ now has a location.** At the symmetric points the three members carry
  the same numbers, as the deck symmetry requires. The six branch points are where a configuration with one
  member's Higgs fully on and another's switching on can leave the first's curve — an unsymmetric configuration,
  with its two images under the deck transformation. Whether a branch of flat connections actually leaves there,
  what its parabolic points are and what torsions sit on them is not computed here; it is the next computation
  (lead L237).
- **Imported expectation, stated separately:** that the Standard Model's values would appear as these numbers.
  Read naively — the up-type torsion of modulus 8 against 16 for down, lepton and neutrino, equal for the three
  members — they do not resemble the observed masses, and no rule here turns a torsion into a mass.
- **The fence:** one level; torsion is not a mass; the three members are not distinguished at any point computed;
  the index is zero off the reducible ends; which larger group contains two members' Higgs directions as
  non-commuting roots is not established (L235 (b)), and the branch points presuppose one. **0 of 19.**

## Verification

`verification/parabolic.py` (on B1444's `curve_engine.py` and B1445's `mass_term.py`), `index_num.py` (the class
index of a numerically given module by singular values), `branch_points.py`; records `parabolic_sectors.json`,
`parabolic_bidoublet_NN.json`, `branch_points.json`. Lock: `tests/test_b1446_parabolic_points.py`.
