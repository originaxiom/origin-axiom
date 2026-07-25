# B784: THE TRACE-MAP INTERTWINING — FINDINGS

cc3 audit seat, 2026-07-25. Gate 5-Q. Negatives first.

## Campaign: 5 agents, 3 phases, ~1700s runtime

Two intertwining theorems tested: θ (reversal) and γ₅ (complement/
golden Galois). The θ bridge lifts. The γ₅ bridge collapses.

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

---

## THE POSITIVE

### 6. θ intertwining lifts to the character variety

**Theorem:** T_{σ_mirror} = θ ∘ T_σ ∘ θ

at every SL(n,C) character variety, by functoriality of the trace map.

At SL(2): trivially true (θ = id on traces). T_σ = T_{σ_mirror} =
(z, x, xz-y). The four substitutions collapse to two trace maps.

At SL(3): non-trivially true. θ is OUTER at SL(3) (proved by Schur's
lemma + irreducibility of the Sym² representation: no inner matrix
can conjugate Sym²(AB) to Sym²(BA)). The intertwining is a genuine
constraint, not a tautology.

Consequence: B783's word-level result (tracking = θ) lifts to the
character variety. The tracking choice is the SL(3) θ-bit, seen
through the trace-map functor.

### 7. The C intertwining holds but is vacuous

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

### 8. The inner/outer classification of involutions

| involution | inner/outer at SL(3) | flip-vector (c,θ,γ₅) | rank-onset |
|---|---|---|---|
| identity | inner | (0,0,0) | — |
| c | outer | (1,0,0) | SL(2) |
| θ | outer | (0,1,0) | SL(3) |
| γ₅ | outer (arithmetic) | (0,0,1) | eigenvalues |
| **C (swap)** | **inner** | **(0,0,0)** | **never** |

C = identity on the character variety. The complement is gauge.

---

## SCORE CARD

| prediction | statement | result |
|---|---|---|
| P784.1 | T_{σ_mirror} = θ∘T_σ∘θ at SL(3) | **PASS** |
| P784.2 | T_{CσC} = C∘T_σ∘C at SL(2) | **PASS** |
| P784.3 | C = γ₅ at incidence-matrix level | FAIL |
| P784.4 | C = γ₅ at SL(3) character variety | FAIL |
| P784.5 | coupling norm √3 in C decomposition | FAIL |

Score: 2/5. Cumulative: 3 for 25 (B783: 1/5, B784: 2/5).

---

## CONSEQUENCE FOR THE OBSERVER PROGRAMME

### The revised picture (after B783 + B784)

| operation | torsor element | level | status |
|---|---|---|---|
| tracking (parent/child) | θ | combinatorial | **CLOSED** (lifts to SL(3)) |
| complement (a↔b swap) | gauge (identity) | — | DEAD (inner automorphism) |
| γ₅ (golden Galois) | γ₅ | arithmetic | OPEN (no combinatorial avatar) |
| c (complex conjugation) | c | geometric | OPEN (requires Q(√-3)) |

The pointer closes 1 bit (θ). The complement slot is DEAD — not open,
DEAD. It cannot close anything because it is gauge.

Residual = ⟨γ₅, c⟩ = Z/2 × Z/2 = 2 bits open.

### Why γ₅ has no combinatorial avatar

γ₅ acts on Q(√5) — the field of the incidence-matrix eigenvalues.
But Q(√5) does not appear in the representation matrices (which live
in Q(√-3) at the geometric point). The two fields are linearly
disjoint over Q.

No operation on the WORD (reversal, complement, or any combination)
can reach γ₅ because:
- Reversal R maps to θ (outer at SL(3), but θ ≠ γ₅)
- Complement C maps to the identity (inner, gauge)
- R·C maps to θ (since C = id on the character variety)

The combinatorial landscape {id, R, C, R·C} maps to {id, θ, id, θ}
in the character-variety group — a rank-1 image, not rank-2. The
golden Galois γ₅ is arithmetically inaccessible from word operations.

### The stratification

1. Combinatorial level (word, substitution): θ closable, C = gauge,
   γ₅ invisible → 1 bit closed
2. Arithmetic level (number fields): γ₅ lives here (Q(√5) eigenvalues).
   Closable by an arithmetic observer? Unknown.
3. Geometric level (hyperbolization): c lives here (Q(√-3)).
   Closable by chirality choice? Unknown.

The three bits of the torsor live at three different levels.
No single mechanism closes all three.

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
