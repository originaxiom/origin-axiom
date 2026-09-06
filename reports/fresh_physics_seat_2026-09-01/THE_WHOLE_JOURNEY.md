# The Whole Journey

**From "what's not nothing" to the Standard Model, computed step by step.**

All derived numerical quantities below are recomputed by the accompanying script from
explicitly stated inputs. Structural facts — topological identifications, representation
data, beta coefficients, Chern-Simons data, and census results — are external inputs
unless separately derived or cited.
Script: `computations/the_whole_journey.py`.

**Reading note (record state 2026-09-06, main @ 0ecd9557).** The record's own accounting
(B1261/B1266) is that this chain derives *structure* and *no numbers*: its free inputs are 4
framework axioms plus 7 irreducible unearned identifications — 11 in all — and they buy 0 of the
Standard Model's 19 free parameters. Every "derived" below is a structural statement; every
number (3/8, M_I) is reproduced or model-dependent, never predicted. Two frame results the record
landed after this document's previous revision are folded in where they bite: E65 (the chain's own
SL(2) holonomy cannot carry chirality) and B1265 (the object's twist derives the real form E₆(−14),
and the spacetime branch E₆(−26) sits across a rank obstruction). See "The Price" at the end.

---

## Step 1: The Simplest Interesting Pattern

Two letters. One rule.

```
a → ab
b → a
```

Watch what happens:

```
step 0: a                                         (1 a, 0 b)
step 1: ab                                        (1 a, 1 b)
step 2: aba                                       (2 a, 1 b)
step 3: abaab                                     (3 a, 2 b)
step 4: abaababa                                  (5 a, 3 b)
step 5: abaababaabaab                             (8 a, 5 b)
step 6: abaababaabaababaababa                     (13 a, 8 b)
step 7: abaababaabaababaababaabaababaabaab         (21 a, 13 b)
step 8: abaababaabaababaababaabaababaabaab...      (34 a, 21 b)
```

The counts are Fibonacci numbers. The ratio of a's to b's → the golden ratio φ = 1.618034...

The rule's recipe is a 2×2 matrix:

```
M = [[1, 1],
     [1, 0]]
```

Each 'a' makes one new 'a' and one new 'b'. Each 'b' makes one new 'a' and zero new 'b'.

- eigenvalues: φ = 1.618034 and −1/φ = −0.618034
- **determinant: −1**

That minus sign will matter a lot.

---

## Step 2: The Rule Makes a Shape

Think of a flat rubber sheet — a torus (donut shape) with a tiny hole poked in it.
A "punctured torus."

The rule acts on this surface: it stretches and folds it.
That's what the matrix M does — it maps the torus to itself.

But det(M) = −1 means the rule **flips the surface inside out**.
It reverses orientation, like looking in a mirror.

To get something that doesn't flip, apply the rule **twice**:

```
M² = [[2, 1],
      [1, 1]]

det(M²) = +1    (preserves orientation ✓)
trace(M²) = 3   (|trace| > 2 → hyperbolic: genuinely stretches, not just rotates)
```

Now imagine gluing the top and bottom of this stretching into a loop — like connecting
a video of the stretch back to its start. This makes a 3D shape called a "mapping torus."

> **The mapping torus of M² is m004: the figure-eight knot complement.**
>
> Take 3D space, remove a figure-eight knot, what's left is this shape.
> The simplest hyperbolic knot complement.
> Built from exactly 2 ideal tetrahedra.
> Volume = 2.0298832128...

---

## Step 3: The Shape's Coordinates

The shape m004 has a "fundamental group" — loops you can draw inside it. Two basic
loops, A and B, generate the fiber fundamental group F₂.

Instead of tracking the loops themselves, track three numbers — the **traces** of the
matrices representing them:

```
x = tr(A),   y = tr(B),   z = tr(AB)
```

These are Fricke coordinates. The rule acts on them. One application does:

```
F(x, y, z) = (z,  x,  xz − y)
```

The shape is the mapping torus of M², so we need the fixed points of F² (rule applied
twice).

**Computing F²:**

```
F(x, y, z)  = (z, x, xz − y)
F²(x, y, z) = F(z, x, xz−y) = (xz−y, z, xz²−yz−x)
```

**Fixed curve** — set (x, y, z) = F²(x, y, z):

```
x = xz − y    →   y = x(z − 1)
y = z          →   z = x(z − 1)
               →   x = z/(z − 1)

Fixed curve:   y = z,   x = z/(z−1)
```

Verify the third equation z = xz² − yz − x:

```
= [z/(z−1)]z² − z·z − z/(z−1)
= z³/(z−1) − z² − z/(z−1)
= [z³ − z]/(z−1) − z²
= z(z+1) − z²
= z   ✓
```

Now add the **puncture condition**. The shape has a hole (the removed knot). The boundary
loop is parabolic — its trace is −2. This gives the **Markoff condition**:

```
κ = x² + y² + z² − xyz = 0
```

Substituting y = z, x = z/(z−1):

```
[z/(z−1)]² + z² + z² − [z/(z−1)]·z² = 0

Multiply by (z−1)²:
z² + 2z²(z−1)² − z³(z−1) = 0
z²[1 + 2(z−1)² − z(z−1)] = 0

Expanding the bracket:
1 + 2z² − 4z + 2 − z² + z = z² − 3z + 3
```

The full equation is z²(z² − 3z + 3) = 0. The solution z = 0 is the **non-geometric**
character: at (x,y,z) = (0,0,0) the peripheral commutator is −I (central element),
not a nontrivial parabolic. Requiring nontrivial parabolic peripheral holonomy selects
the geometric branch:

> ### z² − 3z + 3 = 0
>
> discriminant = 9 − 12 = **−3**
>
> roots: z = (3 ± √−3) / 2

The roots are complex conjugates — a **mirror pair**.
The number field is **Q(√−3)** (its ring of integers is the Eisenstein integers ℤ[ω]).

**The rule + the puncture + nondegeneracy → discriminant −3.** Just algebra.

---

## Step 4: The Number Field Picks a Symmetry (Axiom A3)

The field Q(√−3) has:
- discriminant: −3
- **conductor: N = 3** (the "complexity" of the field)

Now we use the **McKay correspondence** — a bridge between number theory and symmetry.
(The McKay route itself is axiom A3: the declared choice to pass from the geometric
conductor N = 3 to the finite linear group SL(2, F₃) and apply McKay's correspondence.
A3 as used in this document is specifically the map N = 3 → SL(2, F₃) ≅ 2T → Ê₆;
no universal conductor → SL(2, ℤ/Nℤ) → McKay rule is asserted. The conductor entering
this route is N = 3, from the **geometric trace field** Q(√−3). The object
also carries a second number field: the eigenvalue field Q(√5) (conductor 5),
from the Perron–Frobenius eigenvalue φ of the substitution matrix. These are
not a confusion but a theorem: the two-ended theorem (LAW_MAP §141) establishes
that the object has an E₆/Q(√−3) end (hyperbolic geometry / 2T) and an
E₈/Q(√5) end (monodromy / 2I). The McKay route uses the E₆ end; the E₈ end
is a separate structure. Among the metallic family σ_m, only m = 1 produces
a mapping torus whose invariant trace field has conductor 3 (T13): m = 2
gives invariant trace field Q(i) (conductor 4; the ordinary trace field
properly contains Q(ζ₈) and has degree 8 over Q), m ≥ 3 gives
higher-degree fields.
B997's pre-selection via the eigenvalue discriminant Λ(m) = m² + 4 concerns
the Perron–Frobenius eigenvalue field (a polynomial discriminant, not
necessarily the field conductor) — the E₈ end, not the E₆ end.)

(The E₈ end is read off the same monodromy: the Alexander polynomial of the figure-eight is
det(tI − M²) = t² − 3t + 1, roots φ^{±2}, discriminant 5. It is reciprocal — invariant under
t → 1/t — which is what walls the abelian sector against net chirality in B1260, below.)

By A3, we pass from the conductor to the finite linear group and apply McKay's correspondence:

**Step 1:** Build the group SL(2, ℤ/3ℤ) — all 2×2 matrices with entries mod 3 and
determinant 1.

```
Counting by brute enumeration: 24 matrices with entries in {0,1,2} and det ≡ 1 (mod 3)

|SL(2, ℤ/3ℤ)| = 3³ × (1 − 1/3²) = 27 × 8/9 = 24
```

**Step 2:** This 24-element group is isomorphic to the **binary tetrahedral group (2T)**,
which has a faithful embedding in SU(2). The tetrahedron has 12 rotational symmetries;
the "binary" version doubles it to 24 by including the −I element of SU(2).

**Step 3:** The McKay correspondence says: draw a graph where each node is an irreducible
representation of 2T, and connect nodes by how they appear when you tensor with the
fundamental 2D representation.

```
2T irrep dimensions: [1, 1, 1, 2, 2, 2, 3]
Sum of squares: 1+1+1+4+4+4+9 = 24 = |2T|   ✓
Number of irreps: 7

The McKay graph:

         1
         │
         2
         │
  1 ─ 2 ─ 3 ─ 2 ─ 1
```

> **This is the affine Ê₆ diagram** (7 nodes, including the trivial representation),
> corresponding to the affine Kac–Moody type E₆⁽¹⁾. The trivial representation is
> the affine node; removing it gives the finite E₆ Dynkin diagram (6 nodes) and hence
> the finite-dimensional Lie algebra **E₆** used below.
>
> conductor 3 → group of order 24 → McKay graph = affine Ê₆ → finite Lie algebra **E₆**

**The 2T quotient is not unique (B1263; reproduced here).** π₁(m004) admits 72 homomorphisms to
2T = SL(2, F₃), 48 of them surjective, and the 48 fall into exactly two orbits under
Aut(2T) ≅ S₄ (24 each): the object supplies *two* genuinely distinct 2T quotients, and no
relator-preserving automorphism of π₁ exchanges them, so the choice between them is not the
orientation bit. This document's seat computed which is which, and the two routes to 2T named
in this document's Round-11 exchange turn out to be the two orbits:

- **Geometric:** reduce the holonomy SL(2, ℤ[ω]) → SL(2, F₃) modulo the prime (1 − ω). The
  meridian, unipotent in the holonomy, maps to an element of order 3.
- **Non-geometric:** the (0, 0, 0) character of Step 3, realised on the Hurwitz units as
  ρ(a) = i, ρ(b) = j, ρ(t) = (1 + i + j + k)/2. The meridian maps to an element of order 6.

The orbit invariants (ord ρ(x), ord ρ(xy), ord ρ(xy⁻¹)) are (3, 6, 4) on one orbit and (6, 6, 4)
on the other, so the meridian's order alone separates them (reproduced in `computations/the_whole_journey.py`; the quaternionic
representation is transported to the knot group through explicit fiber words, checked in the
faithful Riley representation). So B1263's "genuine binary with no symmetry reason to prefer
either" has a name: the geometric character versus the non-geometric one — the same fork Step 3
resolved by requiring nontrivial parabolic peripheral holonomy. McKay itself, 2T ↔ Ê₆, is a
theorem (the record's I-1, EARNED); that a π₁-quotient *is* the 2T that builds E₆ is the record's
identification I-6, UNEARNED. A3 as declared here routes through the conductor, so it neither
picks a quotient nor needs to — but it inherits I-6's gap the moment the group is asked to act on
the manifold.

---

## Step 5: What's Inside E₆

E₆ is a Lie algebra — a specific symmetry structure.

```
rank: 6         (6 independent "directions" of symmetry)
dimension: 78   (78 generators total)
fundamental representation: 27-dimensional
```

The 27 is the smallest non-trivial "package" that E₆ can act on. Open it up.

E₆ contains a chain of smaller symmetries:

```
E₆  ⊃  SO(10) [Spin(10)]  ⊃  SU(5)  ⊃  SU(3) × SU(2) × U(1)
78      45                     24         8  +  3  +  1  = 12
```

(The SM algebra is the forced endpoint: imposing registerability on a maximal-subalgebra
descent from E₆ gives six possible chains through different intermediates — SO(10)×U(1),
SU(3)³, Pati-Salam — but **all six terminate at SU(3)×SU(2)×U(1)**. The endpoint is
rule-independent. See B994/B863.)

(Two steps short, precisely: the record's registerable cascade lands on
su(3) ⊕ su(2) ⊕ u(1)³ — dimension 14, two abelian factors more than the SM's 12 (B892 as
corrected 2026-09-02). The descent from 14 to 12 needs a VEV the object does not source; see
"What's Not Supplied".)

The 27 decomposes at each step:

```
Under SO(10):   27 = 16 + 10 + 1
The 16 under SU(5):   16 = 10 + 5̄ + 1
```

(Writing "SO(10)" throughout follows standard GUT convention; the 16 is a spinor representation
of the universal cover Spin(10), and the precise maximal subgroup is [Spin(10) × U(1)]/ℤ₄.)

The **16 of SO(10) = one generation of Standard Model fermions**:

| (color, weak, Y) | name | what | count |
|---|---|---|---|
| (3, 2, +1/6) | u_L, d_L | left-handed quarks | 6 |
| (3̄, 1, −2/3) | ū_R | right-handed up (anti) | 3 |
| (3̄, 1, +1/3) | d̄_R | right-handed down (anti) | 3 |
| (1, 2, −1/2) | ν_L, e_L | left-handed leptons | 2 |
| (1, 1, +1) | ē_R | right-handed electron (anti) | 1 |
| (1, 1, 0) | ν̄_R | right-handed neutrino | 1 |
| | | **TOTAL** | **16** |

That's exactly: 3 colors of up and down quarks (left-handed doublet), 3 colors of up
antiquarks, 3 colors of down antiquarks, electron and neutrino (left-handed doublet),
positron, and the right-handed neutrino (the 16th particle).

One complete chiral generation of the Standard Model, plus ν_R.

Two fences from the record (2026-09-06):

1. *"The 16 is one generation"* is standard GUT nomenclature for the representation, not a
   derivation (B1250's own fence). What is verified is narrower and exact (B1253): on the derived
   hypercharge, the 16 is a complete, anomaly-free generation — all six anomalies cancel,
   hypercharge is conserved on 45/45 cubic terms, and the 40 terms of 10·16·16 contain all four SM
   Yukawa operators.
2. The *chirality* of the 16 is axiom A5 here, and E65 makes A5 a theorem-backed input rather than
   a convenience: every Sym^n of SL(2) is self-dual, so any representation factoring
   π₁(m004) → SL(2) → E₆ has 27 ≅ 27̄ as π₁-modules and net chirality identically zero — for
   every embedding of SL(2) in E₆. The chain's own holonomy cannot supply chirality. In the record,
   chirality enters through a *closing* (Dehn filling: 31/31 sampled slopes chiralize, B432; the
   slope is a free input) in the θ-odd, full-E₆(ℂ) frame (B576/B582) — a mechanism outside this
   document's chain.

### The object picks the SO(10) grading and the real form (B1250, B1265; reproduced)

The SO(10) in the chain above is not only the textbook maximal subgroup. The object's own 11-flip
twist D₂ (B916) is an affine sign character on the 27 weights whose stabiliser is so(10) ⊕ u(1)
and whose orbits on the 27 are exactly [1, 10, 16]: D₂ flips the 1 + 10 and fixes the 16 (I-22,
EARNED; control: 0 of 4000 random 11-subsets admit such a character). Reproduced here from the
bare E₆ root system, independently of B1250's basis: grade the 72 roots by their α₁-coefficient
(Bourbaki labelling) — 40 roots at 0, 16 at +1, 16 at −1 — and the 27 weights by the same
coweight, 3·charge ∈ {4, −2, 1} with multiplicities 1, 10, 16; the even-charge block is the
11 = 1 + 10.

Because D₂ is an involution of e₆ with dim 𝔨 = 6 + 40 = 46 and dim 𝔭 = 32, its Cartan signature
is 32 − 46 = −14, and E₆(−14) is *by definition* the real form of that signature (B1265). The
object's twist selects one real form out of five — a point, not a family. D₂ is inner
(conjugation by a torus element), and inner involutions reach only the equal-rank real forms;
E₆(−26), whose maximal compact subalgebra is f₄ of rank 4, is outer and unreachable by any torus
element. The record's E₆(−26) branch is where Lorentz, compact colour and the graviton live
(B1140), so spacetime sits across a rank obstruction from the charge branch this document
follows. The only candidate crossing is the diagram automorphism θ (27 ↔ 27̄), and the record's
own θ facts cut against it: θ is trivial on the character variety, and θ-odd deformations destroy
F₄-stability rather than land in it (B576).

---

## Step 6: The Charges Are Forced

The numbers in the third column (Y = +1/6, −2/3, +1/3, ...) are the **hypercharges**.
Are we free to choose them?

No. **The SU(5) group theory determines them uniquely.**

### The mechanism: the standard embedding chain

The canonical decomposition from Step 5 goes through a standard nested
embedding chain (commuting U(1) factors and finite global quotients suppressed):

```
E₆  ⊃  SO(10)  ⊃  SU(5)  ⊃  SU(3) × SU(2) × U(1)_Y
```

Within SU(5), hypercharge is a diagonal 5×5 traceless matrix that must commute with
the SU(3) block (upper-left 3×3) and the SU(2) block (lower-right 2×2). Commuting
with a block means being proportional to the identity on that block. The most general
such matrix is:

```
c₁·diag(1,1,1,0,0) + c₂·diag(0,0,0,1,1)
```

Tracelessness requires 3c₁ + 2c₂ = 0, giving c₂ = −3c₁/2:

```
Y = c₁ · diag(1, 1, 1, −3/2, −3/2)
```

**One direction, not two.** Choosing the standard normalization (c₁ = −1/3):

```
Y = diag(−1/3, −1/3, −1/3, +1/2, +1/2)
    └──── SU(3) ────┘  └── SU(2) ──┘

trace = 3(−1/3) + 2(+1/2) = 0   ✓
```

### The charges follow from group theory

The 16 of SO(10) decomposes under SU(5) as **10 ⊕ 5̄ ⊕ 1**.
Each piece decomposes under SU(3) × SU(2), and Y is fixed:

```
SU(5) origin       Y       particle
─────────────────  ──────  ────────
10 → (3,2)          +1/6   Q_L
10 → (3̄,1)          −2/3   u^c
10 → (1,1)          +1     e^c
5̄  → (3̄,1)          +1/3   d^c
5̄  → (1,2)          −1/2   L
1  → (1,1)           0     ν^c
```

Every charge is **fixed by the SU(5) embedding**. No free parameter.

What is *not* fixed by group theory is the anchoring of this abstract U(1) to the physical
hypercharge — Q = T₃ + Y, the electromagnetic identification that sets the sign and scale of c₁.
The direction is derived (B864: the unique gaugeable U(1) in the abelian sector); the
normalisation is not derivable from the object, and the anchoring is the record's identification
I-23 (UNEARNED, an instance of the listener map I-13).

### What about anomaly cancellation?

Anomaly cancellation is a **consistency check**, not the derivation mechanism.
Applied alone (without the SU(5) structure), the three linear anomaly conditions
leave a general solution (q, u, −2q−u, −3q, e, 6q−e). At q = 0 the cubic
vanishes identically, giving a two-parameter family (0, u, −u, 0, e, −e) with
uncharged quarks — excluded by the SU(5) embedding. For q ≠ 0, normalizing
Y_Q = 1 gives (1, t, −2−t, −3, e, 6−e). The cubic [U(1)]³ anomaly factorizes as
18(e − t − 4)(e + t − 2) = 0, giving two one-parameter branches related by
interchange of the two SU(3)×SU(2)-singlet assignments (e^c ↔ ν^c).
Choosing the conventional identification:

```
(Y_Q, Y_u, Y_d, Y_L, Y_e, Y_ν) = (1, t, −2−t, −3, 2−t, 4+t)
```

Before fixing normalization, the anomaly-free Abelian charge space is spanned by Y and
B−L. After fixing Y_Q = 1, the free parameter t parametrizes an affine line in the
(Y, B−L) plane; its tangent direction is (B−L) − 2Y. The canonical embedding
chain goes through SU(5), which fixes t = −4 (the SM value) by group theory.

We can verify anomaly cancellation holds for the group-theoretically
determined charges:

```
[SU(3)]²×U(1):  2·Y_Q + Y_u + Y_d                          = 0  ✓
[SU(2)]²×U(1):  3·Y_Q + Y_L                                 = 0  ✓
[grav]²×U(1):   6Y_Q + 3Y_u + 3Y_d + 2Y_L + Y_e + Y_ν      = 0  ✓
[U(1)]³:        6Y_Q³ + 3Y_u³ + 3Y_d³ + 2Y_L³ + Y_e³ + Y_ν³ = 0  ✓
```

(Computed with exact Fraction arithmetic — all four sums are identically zero.)

> **Hypercharge is unique.** The SU(5) group theory within the canonical embedding
> chain E₆ ⊃ SO(10) ⊃ SU(5) ⊃ SM determines exactly one U(1) direction. It produces
> quarks with charge 2/3 and −1/3, electrons with charge −1, neutrinos neutral. Anomaly
> cancellation is a consistency verification, not the mechanism.

---

## Step 7: The Weak Mixing Angle

The Standard Model has two forces that mix: the weak force (SU(2)) and hypercharge (U(1)).
How much they mix is set by the "weak mixing angle" θ_W.

In E₆, the mixing is determined by a trace identity. Over the full **27** representation:

```
Total states: 27
Tr(T₃²)  = 3
Tr(Y²)   = 5
Tr(T₃·Y) = 0
```

The GUT normalization factor (the ratio that relates g' to the properly normalized
GUT coupling g₁ = √(5/3) g'):

```
k = Tr(T₃²) / Tr(Y²) = 3/5
```

At a scale where the normalized couplings match, g₁(GUT) = g₂:

```
sin²θ_W = g'² / (g² + g'²)
        = k·g₁² / (k·g₁² + g₂²)
        = k / (k + 1)
        = (3/5) / (3/5 + 1)
        = 3/8
```

> **sin²θ_W = 3/8 = 0.375 (tree-level group-theoretic matching value)**
>
> Measured at low energy: 0.231.
> The difference is the running of the couplings from high energy to low energy —
> and that running tells us WHERE the matching happens.

**Non-discriminating (B1250; registered as a retracted reading 2026-09-05).**
Tr(T₃²)/Tr(Y²) = 3/5 on the SU(5) 5̄ and 10, the SO(10) 16 and 10, and the E₆ 27 alike
(verified block by block in the script), so 3/8 follows from any SU(5)-compatible embedding with
equal normalised couplings. It reproduces a known GUT relation; it does not select E₆, and it does
not select the knot. Run the other way — as a sealed top-down prediction with α_em(M_Z) as the
single input and the E₆ boundary plus a pure SM desert — the curve misses the measured
(sin²θ_W, α_s)(M_Z) pair at 16σ, α_s-dominated (B915). Step 8 is the bottom-up computation: the
M_Z values are inputs and the matching scale is the output.

---

## Step 8: The Scale

E₆ has a maximal subgroup SU(3) × SU(3) × SU(3) — **trinification**. Under trinification,
sin²θ_W = 3/8 is not a boundary condition at the top — it's a **matching condition** at
the intermediate scale M_I where trinification breaks to the Standard Model.

The canonical tree-level matching relation is α₁⁻¹ = (1/5)α₃L⁻¹ + (4/5)α₃R⁻¹.
With D-parity (g₃L = g₃R), this reduces to α₁ = α₃L = α₂ at M_I.

Running the SM couplings up from M_Z = 91.19 GeV:

```
Inputs (PDG):
  α_em⁻¹(M_Z) = 127.952
  sin²θ_W(M_Z) = 0.23122
  α_s(M_Z) = 0.1180

Derived:
  α₁⁻¹(GUT) = 59.02
  α₂⁻¹      = 29.59
  α₃⁻¹      = 8.47

SM one-loop β coefficients:
  b₁ = +41/10 = +4.1    (U(1) — grows with energy)
  b₂ = −19/6  = −3.17   (SU(2) — shrinks)
  b₃ = −7               (SU(3) — shrinks)
```

Solving α₁⁻¹(M_I) = α₂⁻¹(M_I):

> **M_I = 1.03 × 10¹³ GeV**     (log₁₀ = 13.01)

At M_I:

```
α₁⁻¹ = 42.41  ┐
α₂⁻¹ = 42.41  ┘  matched (= sin²θ_W = 3/8)
α₃⁻¹ = 36.83     (color, still different)
```

The object's boundary condition (3/8), combined with D-parity, SM one-loop running,
and the assumption of no new thresholds below M_I, **determines** this scale.

Above M_I, the three SU(3)s of trinification run with β = (−4, −4, −5) (model-spectrum
input: these depend on the assumed matter content above M_I):

```
gap  = α₂⁻¹ − α₃⁻¹ = 5.58   (in α⁻¹ units)
Δb   = b_L − b_C = 1          (barely differ)

Formal one-loop L/C crossing: M_U = 1.8 × 10²⁸ GeV   (log₁₀ = 28.2)
```

That's 10⁹ **above** the Planck scale, where this field-theory extrapolation is not
physically trustworthy. If one insists on perturbative unification below M_Pl within
this model class, additional threshold or spectrum effects are required; the proposed
sextet Higgs sector is one possible mechanism.

- **What's determined:** M_I (from the object's 3/8, assuming D-parity, SM content, and one-loop running with no intermediate thresholds)
- **What's missing:** M₆ (sextet Higgs mass; the representation content of the trinification Higgs sector must be specified to fix the high-scale running)

---

## Step 9: The Fibonacci Chain

The same rule that made the shape also makes a **crystal**.

Take the Fibonacci word from Step 1: a b a a b a b a a b ...
Put atoms at each position. Give 'a'-atoms potential +V, 'b'-atoms potential −V.
Connect neighbors with hopping t = 1.

This is a real physical system — built in photonic waveguides, polariton wires, and
cold-atom lattices.

Its electronic spectrum has **gaps**, and these gaps are labelled by the integrated
density of states (IDS):

```
IDS at each gap ∈ ℤ + ℤ/φ   (mod 1)
```

where φ is the golden ratio from Step 1.

Computed on a 610-site Fibonacci chain with V = 1:

```
gap 1: width 1.4967, IDS = 0.381967 ≈ (−1)/φ  (mod 1), residual 1.2×10⁻⁶
gap 2: width 0.5842, IDS = 0.618033 ≈ (+1)/φ  (mod 1), residual 1.2×10⁻⁶
gap 3: width 0.3964, IDS = 0.763934 ≈ (−2)/φ  (mod 1), residual 2.4×10⁻⁶
gap 4: width 0.2112, IDS = 0.236066 ≈ (+2)/φ  (mod 1), residual 2.4×10⁻⁶
gap 5: width 0.1680, IDS = 0.527869 ≈ (−4)/φ  (mod 1), residual 4.8×10⁻⁶
```

The transfer-matrix trace map **is** the Fricke action F, and the Fricke invariant
κ = x² + y² + z² − xyz is conserved:

```
For the chain:   κ = 4 + 4V²  ≥  4   for all V
For the shape:   κ = 0        (the puncture condition)

4 + 4V² ≥ 4 > 0 = κ(m004).
```

The chain and the shape are governed by the same Fricke trace-map polynomial, but occupy
different invariant level sets — they **never share a level set**.

---

## Step 10: The Prediction

The shape m004 is **amphichiral** — it admits an orientation-reversing self-symmetry
(a "mirror"). Its symmetry group has order 8, and the closing lattice
(mirror × flow-reversal) is (ℤ/2)².

Under the dictionary c = P (parity), γ₅ = T (time reversal) — **axiom A8**, a declared
choice:

The Chern-Simons invariant CS(m004) is:
- odd under mirror (c-odd)
- odd under flow reversal (γ₅-odd)
- therefore (P-odd, T-odd) = CPT-even
- and **2-torsion**: CS ∈ {0, 1/4} mod 1/2

For m004 specifically: **CS = 0**.

Under the dictionary:
- CPT-even (P-odd, T-odd) type = the E type
- The SM's E-type parameter = the topological QCD vacuum angle **θ**
- 2-torsion in ℝ/2πℤ = {0, π}

Why CS = 0 selects θ = 0, not θ = π: both torsion points are fixed by their respective
ℤ₂ involutions (−c ≡ c for c ∈ {0, 1/4} mod 1/2, and −θ ≡ θ for θ ∈ {0, π} mod 2π),
so equivariance alone does not distinguish them. What rules out 0 ↦ π is the requirement
(part of A8) that the torsion-sector correspondence is an identity-preserving group
homomorphism ℤ/2 → ℤ/2. Every group homomorphism preserves the identity element.
CS = 0 is the identity of {0, 1/4} under addition mod 1/2; θ = 0 is the identity of
{0, π} under addition mod 2π. The unique nontrivial group homomorphism ℤ/2 → ℤ/2 (the
identity isomorphism) sends 0 → 0 and 1/4 → π. (The trivial homomorphism also sends
0 → 0, but it erases the nontrivial type; A8 requires the map to preserve torsion
structure, selecting the isomorphism.)

- CS = 0 → **θ = 0** (dictionary selection)

**Open issue — θ̄ vs θ:** the physical observable is θ̄_QCD = θ + arg(det M_q), not the
topological angle θ alone (which is basis-dependent). The dictionary constrains the
topological angle θ: CS is a topological invariant of the manifold; θ is the coupling
multiplying QCD's topological density F∧F. An anomalous chiral rephasing moves phase
between θ and arg(det M_q), so θ alone is basis-dependent; the dictionary must specify
a phase convention, which A8 does not yet operationally define. (θ = 0 is a representative
in the dictionary's chosen basis.) For the full prediction θ̄ = 0, one additionally needs
arg(det M_q) = 0. E₆ admits a cubic 27³ invariant, but the reality of the group-theoretic
invariant tensor does not by itself fix the phases of the physical Yukawa matrices or VEVs;
the chain does not derive arg(det M_q) = 0. θ̄ = 0 is contingent on controlling the
Yukawa sector.

(This dictionary is T17, which maps symmetry TYPES ℤ/2 → ℤ/2. It is NOT the refuted I-4
dictionary, which attempted a direct VALUE identification CS = θ. B813 kills I-4 on three
independent mismatches: kind, group, and slot. T17 survives because it has no coefficient
slot. See `STATE_2026-09-02.md` addendum 2026-09-03.)

(The record registered this dictionary as identification I-18 (B1243) with θ̄ as its target. After
this document's flag, B1246 verified the discriminating computation — under ψ → e^{iαγ₅}ψ on N_f
flavours, θ → θ − 2N_f α and arg det M → arg det M + 2N_f α, so θ̄ is invariant and θ is not — and
re-priced the row: the type map reaches θ, and earning I-18 needs the dictionary *and* the Yukawa
phase. T17 stands; I-18 stays UNEARNED and reduces to I-13.)

Falsifiability: for m004 specifically, 2-torsion is forced by amphichirality —
CS ≡ −CS (mod 1/2) in SnapPy's normalization, so 2·CS ≡ 0 (mod 1/2)
and CS ∈ {0, 1/4} (mod 1/2). This is
a theorem, not a coincidence. The genuinely sharp content is *within* the
amphichiral class: all 6 amphichiral census manifolds land exactly at
{0, 1/4}, and m004 at 0 separates from its sister m003 at 1/4 (B1224).
Among the 394 non-amphichiral census manifolds, only 1 sits at 2-torsion CS
(B1224). (Census methodology:
OrientableCuspedCensus in SnapPy, first 400 one-cusped orientable manifolds,
amphichirality tested via symmetry_group(), CS values checked for 2-torsion
within floating-point tolerance. The census script will be supplied
separately for independent verification.)
A measured nonzero θ̄ would not by itself
falsify the topological θ = 0; it would falsify θ̄ = 0 only jointly with a demonstration
that arg(det M_q) = 0.

What the dictionary does NOT fix: this argument does not constrain the numerical
weak-CP phases (CKM and PMNS matrices). These are free parameters of the chain.


---

## The Whole Chain, Compressed

```
┌─ RULE ──────────────────────────────────────────────────┐
│  a → ab,  b → a                                        │
│  (the simplest non-trivial substitution on 2 letters)   │
└──────────────────────┬──────────────────────────────────┘
                       │ incidence matrix M, det = −1
                       ▼
┌─ SHAPE ─────────────────────────────────────────────────┐
│  mapping torus of M² → m004 (figure-eight knot)         │
│  the simplest hyperbolic knot complement                │
└──────────────────────┬──────────────────────────────────┘
                       │ Fricke action + puncture condition
                       ▼
┌─ FIELD ─────────────────────────────────────────────────┐
│  z² − 3z + 3 = 0,  discriminant −3                     │
│  the number field Q(√−3)                                │
└──────────────────────┬──────────────────────────────────┘
                       │ conductor 3 → McKay correspondence
                       ▼
┌─ SYMMETRY ──────────────────────────────────────────────┐
│  binary tetrahedral group 2T → E₆                       │
│  rank-6 Lie algebra, 78-dimensional                     │
│  D₂ twist → real form E₆(−14) (derived, B1265)          │
└──────────────────────┬──────────────────────────────────┘
                       │ fundamental representation
                       ▼
┌─ MATTER ────────────────────────────────────────────────┐
│  27 = 16 + 10 + 1                                       │
│  16 = one SM generation (rep. nomenclature; chirality = A5)│
│  hypercharge direction fixed by SU(5); anchoring = I-23  │
└──────────────────────┬──────────────────────────────────┘
                       │ trace identities on the 27
                       ▼
┌─ FORCES ────────────────────────────────────────────────┐
│  SU(3) × SU(2) × U(1); sin²θ_W = 3/8 tree-level, non-discriminating │
│  under D-parity trinification: M_I = 10¹³ GeV (one-loop, no thresholds) │
└──────────────────────┬──────────────────────────────────┘
                       │ Chern-Simons + dictionary
                       ▼
┌─ PREDICTION ────────────────────────────────────────────┐
│  θ = 0 (dictionary); θ̄ = 0 contingent on Yukawa          │
│  weak CP phases = free                                   │
│  bite: amphichiral 6/6 at 2-torsion; non-amphichiral 1/394│
└─────────────────────────────────────────────────────────┘
```

## Axioms (declared inputs, not derived)

| | axiom | role |
|---|---|---|
| A1 | why this rule | minimal description |
| A3 | the McKay route | N = 3 → SL(2,F₃) ≅ 2T → Ê₆ → E₆ |
| A4 | matter in the fundamental 27 | which representation |
| A5 | chirality | chiral 16, not vector-like — not suppliable by the chain's SL(2) holonomy (E65); the record supplies it by a closing |
| A7 | chain's scale = experimenter's | scale identification |
| A8 | dictionary c = P, γ₅ = T; identity-preserving on torsion sectors | discrete-symmetry map |

## What's Not Supplied

- **absolute mass scale** — external, by theorem (the rank theorem proves the 12-dim SM algebra is never a centralizer in E₆; two U(1)s are forced, and the overall scale requires a VEV whose direction is unsourced)
- **VEV direction** within the forced orbit — free
- **exotic decoupling** — the 10+1 accompanying the chiral 16 in each 27 (vectorlike color triplets, extra electroweak doublets, and a singlet under SU(5)) must acquire acceptable masses; the chain does not derive their mass spectrum or decoupling mechanism
- **M₆** — sextet Higgs mass; the representation content of the trinification Higgs sector must be specified
- **D-parity origin** — D-parity (g₃L = g₃R) is a model assumption used in Step 8; the chain does not derive or protect it
- **generation count** — not derived; this document constructs one generation. The record's
  state (2026-09-06), in four parts. (a) B632's h¹(m004; 27_ρ) = 3 is computed under the
  *principal* sl₂ ⊂ E₆ (27 = 17 + 9 + 1) and types as 1 abelian + 2 chiral (B1253/B1256); the
  embedding was assumed, never derived (I-25, UNEARNED). Of the 30 integral sl₂-labellings, four
  give three nontrivial odd summands, and Brieskorn–Slodowy selects the subregular
  (27 = 13 + 9 + 5, three chiral) as the unique orbit whose slice returns 2T (B1257) — but that the
  object's holonomy lands there is unshown. (b) E65: any ρ through SL(2) has 27 ≅ 27̄, so no h¹ in
  this frame is a *net*-chirality count, for any embedding. B1260/B1267 extend the wall: on any
  closed oriented 3-manifold Poincaré duality forces h¹(V) = h¹(V*); on the cusped manifold the
  abelian sector is walled by reciprocity of Δ(t) = t² − 3t + 1; and the corpus's only
  non-self-dual rank-3 systems (B102's W1/W2) are rigid, h¹ = 0, index zero. (c) Reading any h¹ of
  a real 3-manifold as a 4d generation count is itself an identification (I-26, UNEARNED): the
  index theorem lives on a CY3 or a G₂ manifold, and the surviving gauge group is never named.
  (d) Three generations cannot live inside one 27: the 16 has multiplicity one, and three copies
  need dimension ≥ 48 (B1255).
- **chirality mechanism** — A5 is an axiom here; the record's mechanism (a θ-odd closing,
  B432/B576/B582) is not part of this chain, and the slope it selects is a free input.
- **spacetime, Lorentz, gravity** — the E₆(−26) branch (B1140) is an outer real form; the object's
  D₂ is inner and reaches only E₆(−14). The fork is a rank obstruction (B1265), priced at two
  identifications (I-10/I-11), and no arc crosses it.
- **A8 phase convention** — A8 does not yet operationally define the chiral phase convention in which θ = 0 is stated
- **coupling values at low energy** — structure, not values

## The Price (record accounting, B1261/B1266, 2026-09-06)

| | |
|---|---|
| **spends** | 4 framework axioms + 7 irreducible unearned identifications = **11 free inputs** (14 ledger rows outstanding; I-18 and I-23 reduce to I-13, I-11 to I-10) |
| **buys** | **0 of the SM's 19** free parameters (26 with Dirac neutrinos) |
| **derives, structurally** | E₆ (McKay, I-1 EARNED) · the SO(10) grading (D₂, I-22 EARNED) · the real form E₆(−14) (B1265) · the descent cut by three characters of the object's own 27 (B1250/B1252) · one complete anomaly-free generation (B1253) · hypercharge direction (B864) · termination at the SM (B863) · the global ℤ₆ form (B862, conditional on the cascade's premises) |

The two currencies do not convert: by parameter count the trade is net negative; by structural
content it derives what the SM assumes or cannot state. The rate moves only by earning a source
(−1), refuting one (−1: I-9 was refuted at B1262), or deriving a parameter (+1).

Where the seven sources touch this chain:

| source | what it identifies | where it bites here |
|---|---|---|
| I-13 (the listener map; I-18 and I-23 reduce to it) | structural analogue ≡ physical quantity | every physics reading; Step 6's anchoring (I-23); Step 10's θ (I-18) |
| I-10/I-11 (the fork) | internal A₁ / θ-polarisation ≡ 4d Lorentz spin | not in this chain — spacetime is the E₆(−26) branch (Step 5) |
| I-6 | π₁(m004) ↠ 2T ≡ the transverse ALE Γ | Step 4: two 2T quotients, geometric versus non-geometric |
| I-7 | the object's ℤ/3 ≡ the boundary CFT module group | Step 8's trinification ℤ/3 |
| I-14 | trinification ℤ/3 grading ≡ the commensurator's Eisenstein-unit ℤ/3 | Step 8: the 9+9+9 grading exists in the 27 — 85 distinct colourings, nothing selects one (B1264) |
| I-25 | which sl₂ ⊂ E₆ the holonomy realises | the generation-count note above |
| I-26 | h¹ of a 3-manifold ≡ a 4d generation count | the generation-count note above |

Labelling note: this document's A1/A3/A4/A5/A7/A8 are chain-axioms named by this seat. The record's
"4 axioms" are its framework axioms in its own A-labelling (state space ℤ², invertibility,
orientation, the two shears, first mixed closure, minimality, the order). The two lists are
different objects and are not to be added together.

## Forcedness Census

| status | count |
|---|---|
| THEOREM | 26 |
| IDENTITY | 6 |
| NO-GO | 7 |
| AXIOM | 4 links (at C3, C4, C5, C18) — see note |
| COROLLARY | 1 |
| CENSUS | 1 |

Axiom-free stretch: C6–C17.

**Note on axiom counts:** The table above lists 6 declared axiom *inputs* (A1, A3, A4, A5,
A7, A8). The forcedness census counts 4 axiom-bearing *links* in the derivation chain. The
metrics differ: an axiom input is a declared choice; an axiom link is a step in the chain
where such a choice is exercised. Some axioms share a link; the two counts measure different
things.

**Model assumptions in Step 8** (not axioms, but additional inputs that affect the M_I output):
D-parity (g₃L = g₃R); standard trinification hypercharge embedding; tree-level matching
at M_I; SM field content below M_I; no intermediate thresholds; one-loop running.
These are standard trinification model choices. Without D-parity, the α₁ = α₂ matching
does not hold and M_I is not uniquely selected.
