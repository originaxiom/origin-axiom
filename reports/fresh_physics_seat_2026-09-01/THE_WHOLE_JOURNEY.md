# The Whole Journey

**From "what's not nothing" to the Standard Model, computed step by step.**

Every derived numerical quantity below is recomputed from explicitly stated inputs;
structural facts (volumes, Lie-algebra data, topological invariants) are cited inputs.
Script: `computations/the_whole_journey.py`. Every derived number reproduced.

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
loops, A and B, generate everything.

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

## Step 4: The Number Field Picks a Symmetry

The field Q(√−3) has:
- discriminant: −3
- **conductor: N = 3** (the "complexity" of the field)

Now we use the **McKay correspondence** — a bridge between number theory and symmetry.

**Step 1:** Build the group SL(2, ℤ/3ℤ) — all 2×2 matrices with entries mod 3 and
determinant 1.

```
Counting by brute enumeration: 24 matrices with entries in {0,1,2} and det ≡ 1 (mod 3)

|SL(2, ℤ/3ℤ)| = 3³ × (1 − 1/3²) = 27 × 8/9 = 24
```

**Step 2:** This 24-element group, lifted into SU(2), is the **binary tetrahedral group
(2T)**. The tetrahedron has 12 rotational symmetries; the "binary" version doubles it to
24 by including the −I element of SU(2).

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

> **This is the affine Ê₆ diagram** (7 nodes, including the trivial representation).
> Removing the trivial-rep node recovers the finite E₆ Dynkin diagram (6 nodes).
> The Lie algebra obtained is **E₆** either way.
>
> conductor 3 → group of order 24 → McKay graph = affine Ê₆ → Lie algebra **E₆**

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
E₆  ⊃  SO(10)  ⊃  SU(5)  ⊃  SU(3) × SU(2) × U(1)
78      45         24         8  +  3  +  1  = 12
```

The 27 decomposes at each step:

```
Under SO(10):   27 = 16 + 10 + 1
The 16 under SU(5):   16 = 10 + 5̄ + 1
```

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

---

## Step 6: The Charges Are Forced

The numbers in the third column (Y = +1/6, −2/3, +1/3, ...) are the **hypercharges**.
Are we free to choose them?

No. **The SU(5) group theory determines them uniquely.**

### The mechanism: the maximal-subgroup chain

The canonical decomposition from Step 5 goes through maximal subgroups:

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

### What about anomaly cancellation?

Anomaly cancellation is a **consistency check**, not the derivation mechanism.
Applied alone (without the SU(5) structure), it leaves a one-parameter family:

```
(Y_Q, Y_u, Y_d, Y_L, Y_e, Y_ν) = (1, t, −2−t, −3, 2−t, 4+t)
```

The free parameter t corresponds to the B−L direction, which lives in
SO(10)/(SU(5) × U(1)_χ) — **outside** SU(5). The canonical maximal-subgroup
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

> **Hypercharge is unique.** The SU(5) group theory within the canonical maximal-subgroup
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

The GUT normalization factor:

```
k = Tr(T₃²) / Tr(Y²) = 3/5
```

At the unification scale, g₁(GUT) = √(5/3) × g'. When g₁(GUT) = g₂:

```
sin²θ_W = g'² / (g² + g'²)
        = k·g₁² / (k·g₁² + g₂²)
        = k / (k + 1)
        = (3/5) / (3/5 + 1)
        = 3/8
```

> **sin²θ_W = 3/8 = 0.375 exactly**
>
> Measured at low energy: 0.231.
> The difference is the running of the couplings from high energy to low energy —
> and that running tells us WHERE the matching happens.

---

## Step 8: The Scale

E₆ has a maximal subgroup SU(3) × SU(3) × SU(3) — **trinification**. Under trinification,
sin²θ_W = 3/8 is not a boundary condition at the top — it's a **matching condition** at
the intermediate scale M_I where trinification breaks to the Standard Model.

The condition: α₁(GUT normalization) = α₂ at M_I.

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

The object's boundary condition (3/8) **determines** this scale.

Above M_I, the three SU(3)s of trinification run with β = (−4, −4, −5):

```
gap  = α₂⁻¹ − α₃⁻¹ = 5.58   (in α⁻¹ units)
Δb   = b_L − b_C = 1          (barely differ)

Naive unification: M_U = 1.8 × 10²⁸ GeV   (log₁₀ = 28.2)
```

That's 10⁹ **above** the Planck scale. The gap closes too slowly. Extra matter (sextet
Higgses at mass M₆) is needed to steepen the convergence and pull unification below Planck.

- **What's determined:** M_I (from the object's 3/8)
- **What's missing:** M₆ (one mass, one named pair of representations)

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
gap 1: width 1.4967, IDS = 0.381967 ≈  0 + (−1)/φ  (mod 1), residual 1.2×10⁻⁶
gap 2: width 0.5842, IDS = 0.618033 ≈ −1 +   1 /φ  (mod 1), residual 1.2×10⁻⁶
gap 3: width 0.3964, IDS = 0.763934 ≈  0 + (−2)/φ  (mod 1), residual 2.4×10⁻⁶
gap 4: width 0.2112, IDS = 0.236066 ≈ −3 +   2 /φ  (mod 1), residual 2.4×10⁻⁶
gap 5: width 0.1680, IDS = 0.527869 ≈ −1 + (−4)/φ  (mod 1), residual 4.8×10⁻⁶
```

The transfer-matrix trace map **is** the Fricke action F, and the Fricke invariant
κ = x² + y² + z² − xyz is conserved:

```
For the chain:   κ = 4 + 4V²  ≥  4   for all V
For the shape:   κ = 0        (the puncture condition)

4 + 4V² ≥ 4 > 0 = κ(m004).
```

The chain and the shape **never share a level set**. They're on different slices of the
same invariant.

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
- The SM's E-type parameter = **θ̄_QCD** (the strong CP phase)
- 2-torsion in ℝ/2πℤ = {0, π}

Why CS = 0 selects θ = 0, not θ = π: the dictionary is a group homomorphism ℤ/2 → ℤ/2.
Every group homomorphism preserves the identity element. CS = 0 is the identity of {0, 1/4}
under addition mod 1/2; θ = 0 is the identity of {0, π} under addition mod 2π. Both group
homomorphisms ℤ/2 → ℤ/2 (trivial and identity) send 0 → 0. No value-level choice is made.

- CS = 0 → **θ̄ = 0: strong CP is conserved**

Falsifiability: 593 of 594 chiral census manifolds do NOT sit at 2-torsion Chern-Simons.
If the strong CP phase is measured to be nonzero, the prediction fails.

What the dictionary does NOT fix: the weak CP phases (CKM and PMNS), which are free bits
on the γ₅ axis.

(Note: T17's dictionary maps symmetry TYPES ℤ/2 → ℤ/2. It is NOT the refuted I-4
dictionary, which attempted a VALUE identification CS = θ. B813 kills I-4; T17 survives.
See `STATE_2026-09-02.md` addendum 2026-09-03.)

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
└──────────────────────┬──────────────────────────────────┘
                       │ fundamental representation
                       ▼
┌─ MATTER ────────────────────────────────────────────────┐
│  27 = 16 + 10 + 1                                       │
│  16 = one SM generation (quarks + leptons + ν_R)         │
│  hypercharge uniquely fixed by SU(5) group theory        │
└──────────────────────┬──────────────────────────────────┘
                       │ trace identities on the 27
                       ▼
┌─ FORCES ────────────────────────────────────────────────┐
│  SU(3) × SU(2) × U(1) with sin²θ_W = 3/8 exactly       │
│  under trinification: M_I = 10¹³ GeV (determined)       │
└──────────────────────┬──────────────────────────────────┘
                       │ Chern-Simons + dictionary
                       ▼
┌─ PREDICTION ────────────────────────────────────────────┐
│  θ̄_QCD = 0  (strong CP conserved)                       │
│  weak CP phases = free                                   │
│  bite: 1/594 chiral manifolds at 2-torsion CS            │
└─────────────────────────────────────────────────────────┘
```

## Axioms (declared inputs, not derived)

| | axiom | role |
|---|---|---|
| A1 | why this rule | minimal description |
| A3 | the McKay route | disc → conductor → 2T → E₆ |
| A4 | matter in the fundamental 27 | which representation |
| A5 | chirality | chiral 16, not vector-like |
| A7 | chain's scale = experimenter's | scale identification |
| A8 | dictionary c = P, γ₅ = T | discrete-symmetry map |

## What's Not Supplied

- **absolute mass scale** — external, by theorem (the rank theorem proves the 12-dim SM algebra is never a centralizer in E₆; two U(1)s are forced, and the overall scale requires a VEV whose direction is unsourced)
- **VEV direction** within the forced orbit — free
- **M₆** — sextet Higgs mass; one number, one named pair of representations
- **generation count** — 3 exhibited, not forced
- **coupling values at low energy** — structure, not values

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
