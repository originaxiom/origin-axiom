# B784: THE TRACE-MAP INTERTWINING — FINDINGS

cc3 audit seat, 2026-07-25. Gate 5-Q. Negatives first.

**CORRECTED** per cc relay (2026-07-25) and chat1's trace-cyclicity
theorem. Original claimed θ closes 1 bit via trace-map lift.
Correction: θ is trivial on ALL traces at ALL ranks. 0 bits closed
at the character-variety level. Score: 1/5 (was 2/5).

## Campaign: 5 agents, 3 phases, ~1700s runtime

Two intertwining theorems tested: θ (reversal) and γ₅ (complement/
golden Galois). Both collapse on the character variety — θ because
word reversal is invisible to traces, C because it is inner/gauge.
The observer programme closes 0 bits at the trace level.

---

## NEGATIVES FIRST

### 1. C ≠ γ₅ at the character variety. C is gauge.

The complement operation C (swap generators A↔B) is an INNER
automorphism of SL(2,C): the matrix

    P(u) = [[0, 1/√u], [-√u, 0]]     det(P) = 1, P² = -I

satisfies P(u)·A·P(u)⁻¹ = B(u) and P(u)·B(u)·P(u)⁻¹ = A for the
entire Riley family B = [[1,0],[-u,1]], for all u ≠ 0. At the figure-
eight geometric point, P = [[0, ω], [ω+1, 0]] with ω = (-1+√-3)/2.

Inner automorphisms act TRIVIALLY on the GIT quotient (character
variety). C has flip-vector (0,0,0) = identity in the (c, θ, γ₅) basis.
γ₅ has flip-vector (0,0,1). They are as different as the identity and
a generator.

### 2. C ≠ γ₅ already at the incidence-matrix level

The masterplan predicted P784.3: "C = γ₅ at the incidence-matrix level
(eigenspace swap)." FAIL. C and γ₅ implement structurally different
Z/2 symmetries:

- C is "horizontal": it acts BETWEEN the two matrices M_σ = [[1,1],[1,0]]
  and M_{CσC} = [[0,1],[1,1]], conjugating one to the other while
  PRESERVING eigenvalue labels (φ stays φ).
- γ₅ is "vertical": it acts WITHIN a single matrix, swapping eigenvalue
  labels (φ ↔ φ̄ = -1/φ).

The resemblance (both "swap φ/φ̄ eigenspaces" at a coarse description)
is an artifact of the incidence matrix forgetting inner/outer structure.

### 3. The Sütō invariant formula in K007 is wrong for the full-trace map

K007 states I = x²+y²+z²-2xyz-1 (coefficient 2 on xyz) for the KKT
map T(x,y,z) = (z, x, xz-y). The correct invariant is the Fricke-Vogt:

    I_Fricke(x,y,z) = x² + y² + z² - xyz - 2     (coefficient 1)

The Sütō formula x²+y²+z²-2xyz-1 applies to the half-trace convention
T(x,y,z) = (2xy-z, x, y), used in Schrödinger operator theory where
x = tr(M)/2. Both are preserved by their respective maps. The mismatch
is a coordinate-system issue, not a mathematical error in either source.

### 4. P784.5 FAIL: no √3 in the C decomposition

The C-eigenbasis decomposition of the Jacobian at the geometric point
has coupling norms 1/√2 and √(53/4). Neither is √3. The coupling norm
√3 = √|disc Q(√-3)| belongs to the θ-even/θ-odd decomposition at
SL(3) (B759), not to the C-even/C-odd decomposition at SL(2).

### 5. The observer/object distinction is real and irreducible

Chat1's question: does complement (object-side: changes the word) =
γ₅ (observer-side: changes the representation, not the knot)?

Answer: NO. They are separated by three independent diagnostics:

1. **Inner/outer**: C is inner (gauge), γ₅ is outer (arithmetic)
2. **Number field**: C acts on representations (Q(√-3) data), γ₅ acts
   on eigenvalues (Q(√5) data)
3. **Flip-vector**: C = (0,0,0) = identity, γ₅ = (0,0,1) ≠ identity

The two number fields Q(√5) and Q(√-3) are linearly disjoint over Q.
No matrix operation at the geometric point can reach γ₅ because the
geometric-point data lives in Q(√-3), where γ₅ acts trivially.

### 6. θ is TRIVIAL on the character variety at ALL ranks

**CORRECTION (cc relay, 2026-07-25).** The original FINDINGS claimed
P784.1 as a non-trivial PASS ("θ is OUTER at SL(3)... the intertwining
is a genuine constraint"). This is wrong. θ = word reversal acts as the
IDENTITY on ALL trace functions at ALL ranks.

**Three independent proofs, all conclusive:**

(a) **Trace cyclicity on generators.** θ fixes tr(A), tr(B) (single
    letters). θ(AB) = BA, and tr(AB) = tr(BA) by trace cyclicity.
    ALL trace functions on F₂ are polynomials in (tr A, tr B, tr AB).
    θ = id on the entire character variety at SL(2). Since Sym^n traces
    are polynomials in SL(2) traces, θ = id at ALL ranks.

(b) **Chat1's cyclic-permutation theorem.** σ_mirror(w) is a cyclic
    permutation of σ(w) for every word w. The shift follows a Fibonacci
    sub-sequence (0, 1, 0, 1, 3, 6, 11, 19, 32, 53, 87, 142...).
    Therefore tr(ρ(σ_mirror(w))) = tr(ρ(σ(w))) at every rank n, for
    any representation ρ, by trace cyclicity of the matrix product.

(c) **cc3's own A3 computation.** A3_sym2_trace_computation PART 3
    prints "theta TRIVIAL at SL(3) trace level: True". The FINDINGS
    erroneously interpreted "θ OUTER at SL(3)" (a matrix-level fact from
    Schur's lemma: no inner matrix conjugates Sym²(AB) to Sym²(BA)) as
    "non-trivial on the character variety." OUTER ≠ NON-TRIVIAL ON TRACES.
    Sym²(AB) ≠ Sym²(BA) as matrices, but tr(Sym²(AB)) = tr(Sym²(BA)).

The intertwining T_{σ_mirror} = θ∘T_σ∘θ collapses to T_σ = T_σ at
every rank: a tautology. P784.1 is vacuously true, not a structural
constraint.

### 7. B780 mislabels ι (inversion) as θ (reversal)

B780 attributes the permutation (1 4)(2 5)(3 8)(6 7) on the 8 Lawton
SL(3) trace coordinates to "θ at SL(3)". The 8 coordinates (B71/B48):

    x = (tr A, tr B, tr AB, tr A⁻¹, tr B⁻¹, tr A⁻¹B, tr AB⁻¹, tr A⁻¹B⁻¹)

The permutation swaps each direct-trace with its inverse-trace partner:
x1↔x4, x2↔x5, x3↔x8, x6↔x7. This is the INVERSION map ι: w → w⁻¹,
not the REVERSAL map θ: w → w^R. Verified at random SL(3) matrices:
θ = identity on all 8 coordinates, ι = exact permutation match.

- At SL(2): both ι and θ are trace-trivial (tr(M) = tr(M⁻¹), tr(XY) = tr(YX)).
  B780's mislabeling arises because they coincide at SL(2).
- At SL(3): ι separates (tr(M) ≠ tr(M⁻¹) for generic SL(3)), while θ
  stays trivial (trace cyclicity).
- On V0 (Sym² locus): ι also collapses back (tr(Sym²(M)) = (tr M)² - 1
  = (tr M⁻¹)² - 1 = tr(Sym²(M⁻¹))). The permutation has content only on
  the W1/W2 components (non-geometric, trace-1 components of the SL(3)
  character variety).

The "rank-onset at SL(3)" signature in B780 is real, but it belongs to ι,
not θ. The two involutions separate at SL(3): ι acts on direct/inverse
trace pairs, θ acts on nothing (trace level) or on matrix entries
(representation level).

### 8. ι (inversion) is INDEPENDENT of ⟨c, θ, γ₅⟩ but GAUGE on V0

**ADDENDUM (2026-07-25).** Chat1's follow-up: where does ι sit in the
closing group (Z/2)³ = ⟨c, θ, γ₅⟩? Three options: ι = c, ι = cθ (chord),
or ι independent (rank > 3).

**Answer: ι = θ · inner(S), where S = diag(1,−1,1) = Sym²(diag(1,−1)).**

This is the Sym² lift of the SL(2) self-duality matrix P = diag(1,−1).
For ALL words w: P·ρ₂(w⁻¹)·P⁻¹ = ρ₂(w^R) at SL(2), and
S·Sym²(w⁻¹)·S⁻¹ = Sym²(w^R) on V0. Verified symbolically at 6 words
including AB, A⁻¹B, AB⁻¹, A²B, ABA.

Consequences:
- On V0 (Sym², self-dual): S exists, ι is gauge-equivalent to θ. Both
  trivial on the character variety. B766's rank 3 stands.
- On W1/W2 (generic SL(3), NOT self-dual): no such S exists (verified:
  nullity 0 at 5 random SL(3) trials). ι is OUTER and genuinely
  independent of {c, θ, γ₅}. Full SL(3) group: (Z/2)⁴.
- Chat1's options: (1) ι = c → NO (c conjugates traces, ι permutes
  them). (2) ι = cθ → NO (cθ = c on traces, c ≠ ι). (3) ι independent
  → YES, but gauge on V0.
- ι's non-triviality IS the non-self-duality obstruction. Where the
  representation is self-dual, ι = θ (mod gauge). Where not, they
  separate and ι adds a fourth bit.

---

## THE POSITIVE

### 8. The C intertwining holds but is vacuous

**Theorem:** T_{CσC} = C ∘ T_σ ∘ C  where C: (x,y,z) → (y,x,z)

Verified algebraically at SL(2):
    T_σ(x,y,z) = (z, x, xz-y)
    T_{CσC}(x,y,z) = (y, z, yz-x)
    C ∘ T_σ ∘ C(x,y,z) = (y, z, yz-x) ✓

The Fricke-Vogt invariant x²+y²+z²-xyz-2 is preserved by both maps.
At the geometric point (2, 2, 5/2-i√3/2), the C-swap between orbits
persists through all iterates.

But: since C is inner, this intertwining says nothing about the torsor.
Two dynamical systems that are conjugate by an inner automorphism
describe the SAME physics — the C-swap is a choice of coordinates,
not a structural distinction.

### 9. The inner/outer classification of involutions (CORRECTED)

| involution | matrix level | character variety | flip-vector (c,θ,γ₅) |
|---|---|---|---|
| identity | inner | trivial | (0,0,0) |
| c | outer | NON-TRIVIAL (flips T4) | (1,0,0) |
| θ (reversal) | outer (Schur) | TRIVIAL (all traces) | (0,1,0) — rep. variety only |
| γ₅ | outer (arithmetic) | NON-TRIVIAL (flips T3,T7) | (0,0,1) |
| C (swap) | inner | TRIVIAL (gauge) | (0,0,0) |
| ι (inversion) | outer | SL(3): non-trivial on W1/W2 | not in torsor |

θ and C are both trivial on the character variety, by DIFFERENT
mechanisms: θ because reversal = cyclic permutation (trace-invisible),
C because inner automorphism (gauge). θ's flip-vector (0,1,0) applies
to T6, which is a REPRESENTATION-VARIETY (matrix-level) observable,
not a character-variety (trace-level) one.

---

## SCORE CARD (CORRECTED per cc relay)

| prediction | statement | result |
|---|---|---|
| P784.1 | T_{σ_mirror} = θ∘T_σ∘θ at SL(3) | VACUOUS (θ = id on traces) |
| P784.2 | T_{CσC} = C∘T_σ∘C at SL(2) | **PASS** |
| P784.3 | C = γ₅ at incidence-matrix level | FAIL |
| P784.4 | C = γ₅ at SL(3) character variety | FAIL |
| P784.5 | coupling norm √3 in C decomposition | FAIL |

Score: 1/5. Cumulative: 2 for 25 (B783: 1/5, B784: 1/5).

---

## CONSEQUENCE FOR THE OBSERVER PROGRAMME (CORRECTED)

### The revised picture (after B783 + B784 + trace-cyclicity correction)

| operation | torsor element | level | char. variety status |
|---|---|---|---|
| tracking (parent/child) | θ | combinatorial | INVISIBLE (trivial on traces) |
| complement (a↔b swap) | gauge (identity) | — | DEAD (inner automorphism) |
| γ₅ (golden Galois) | γ₅ | arithmetic | OPEN (non-trivial on T3, T7) |
| c (complex conjugation) | c | geometric | OPEN (non-trivial on T4) |

The pointer closes 0 bits at the character-variety level. θ is
invisible to traces at every rank. The observer's tracking choice is
REPRESENTATION-VARIETY structure — visible on matrices (Sym²(AB) ≠
Sym²(BA)), invisible on traces (tr(Sym²(AB)) = tr(Sym²(BA))). It
lives in the gap between the representation variety and the character
variety: the fibre-functor torsor (B701).

Character-variety torsor: ⟨c, γ₅⟩ ≅ Z/2 × Z/2 = 2 bits open.
Full torsor: ⟨c, θ, γ₅⟩ ≅ F₂³ = 3 bits, all open at the character
variety. θ requires representation-variety data to detect.

### Why NO combinatorial operation reaches the character variety

The combinatorial landscape {id, R, C, R·C} maps to {id, id, id, id}
on the character variety:

- R (reversal) → id (trace cyclicity, all ranks)
- C (complement) → id (inner automorphism, gauge)
- R·C → id (both factors trivial)

The character-variety image has RANK 0, not rank 1 as originally
claimed. No word-level operation produces a non-trivial action on
traces. The golden Galois γ₅ and the complex conjugation c both
require operations OUTSIDE the combinatorial landscape.

### The stratification (corrected)

1. Character variety (traces): sees c and γ₅. 2 bits open. The
   combinatorial landscape maps entirely to the identity here.
2. Representation variety (matrices): adds θ. 3 bits open. θ is
   visible through Sym²(AB) ≠ Sym²(BA) (traceless matrix difference
   with 6 nonzero entries). This is the level of T6 (chord sign).
3. Combinatorial (word): tracking = θ confirmed (B783). But this
   does NOT propagate to the character variety because θ is
   trace-invisible. The word-level structure is finer than traces.

The trace-map functor operates ON the character variety. Since θ is
invisible there, the functor cannot carry B783's word-level θ result
to the character variety. The bridge that B784 attempted to build
does not exist at the trace level.

### The mapping class is θ-insensitive and ι-insensitive

**ADDENDUM (2026-07-25, chat1 task 3).** The monodromy trace
tr(ρ(meridian)) = 2 (parabolic) is θ- and ι-insensitive at all ranks.
The trace map T_σ = T_{σ_mirror} (θ trivial on traces). Moreover,
ι commutes with ALL homomorphisms: φ(g⁻¹) = φ(g)⁻¹. So ι·σ = σ·ι
on all of F₂. No trace-map dynamics can detect either θ or ι.

### The Fox calculus IS the non-trace bridge

**ADDENDUM (2026-07-25, chat1 task 4).** The Fox Jacobian in the group
ring ZF₂ IS θ-sensitive:

    J_σ = [[1, a], [1, 0]]         det(J_σ) = -a  in ZF₂
    J_{σ_mirror} = [[b, 1], [1, 0]]  det(J_{σ_m}) = -1  in ZF₂

DIFFERENT. Under ρ at the geometric point: the 4×4 matrices have the
same eigenvalues (φ, −1/φ each double) but different entries. The
difference ρ(J_σ) − ρ(J_{σ_m}) = [[I−B, A−I], [0, 0]] lives in the
NILPOTENT (cusp) directions: I−B = ω·e₂₁, A−I = e₁₂. θ is visible
in the cusp data that traces erase.

θ-sensitivity grows with rank: rank(I − Symⁿ(A)) = n. At SL(n+1), the
Fox bridge carries n independent cusp directions where θ acts non-trivially.
This is the first θ-sensitive invariant connected to the geometry.

---

## ERRATUM ON K007

The Sütō invariant formula should specify the coordinate convention:
- Full traces: I(x,y,z) = x²+y²+z² - xyz - 2 (Fricke-Vogt, coeff 1)
- Half traces: I(x,y,z) = x²+y²+z² - 2xyz - 1 (Sütō, coeff 2)

The KKT map in full-trace form is T(x,y,z) = (z, x, xz-y). K007's
statement of the invariant uses Sütō's convention, which applies to
T(x,y,z) = (2xy-z, x, y). Both are correct in their own coordinates.

---

## SEAL

Algorithm: SHA-256 of this file's content excluding the SEAL section.
