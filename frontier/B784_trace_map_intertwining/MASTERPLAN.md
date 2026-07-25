# B784: THE TRACE-MAP INTERTWINING — cc3 campaign masterplan

cc3 audit seat, 2026-07-25. Gate 5-Q.

## The question (revised scope — chat1's elevation)

Two intertwining theorems, not one:

1. **θ intertwining:** Does the KKT trace map carry word-level σ_mirror
   to character-variety θ? If yes: tracking = θ lifts from a word-level
   lemma (B783) to a character-variety theorem.

2. **γ₅ intertwining:** Does the trace map carry word-level complement
   (C·σ·C) to character-variety γ₅? If yes: the combinatorial operation
   that is "object-side" at the word level (it changes the word) becomes
   "observer-side" at the geometric level (it changes the representation,
   not the knot). This would settle γ₅'s observer/object status.

Chat1's insight: "object-side at the combinatorial level" is not the same
as "object-side at the geometric level." Complement changes the WORD
(object-side combinatorially). But γ₅ at the character variety changes
the REPRESENTATION (observer-side geometrically — same knot, different
rep). The trace-map intertwining determines whether these are the same
operation seen through different lenses.

## The substitution landscape

Four substitutions related by reversal R and complement C:

| substitution | rule | incidence matrix |
|---|---|---|
| σ | a→ab, b→a | [[1,1],[1,0]] |
| σ_mirror = R·σ·R | a→ba, b→a | [[1,1],[1,0]] |
| C·σ·C | a→b, b→ba | [[0,1],[1,1]] |
| R·C·σ·C·R | a→b, b→ab | [[0,1],[1,1]] |

Note: R is invisible at the incidence-matrix level (same letter counts).
C swaps the incidence matrix's eigenspaces (φ ↔ φ̄).

## The θ intertwining

**Claim:** T_{σ_mirror} = θ ∘ T_σ ∘ θ

**Proof sketch:** σ_mirror = R·σ·R. The trace map is functorial:
T_{f∘g} = T_f ∘ T_g and T_R = θ. Therefore
T_{σ_mirror} = T_R ∘ T_σ ∘ T_R = θ ∘ T_σ ∘ θ. QED.

Levels of triviality:
- At SL(2): trivially true (θ = id, tr(AB)=tr(BA))
- At SL(3) on V0: trivially true (V0 is θ-fixed)
- At SL(3) tangent space: NON-TRIVIALLY TRUE (coupling norm √3)

## The γ₅ intertwining

**Claim:** T_{CσC} = C ∘ T_σ ∘ C where C acts on trace coordinates
by swapping generators: (x,y,z) = (tr(a), tr(b), tr(ab)) → (y,x,z).

**Proof sketch:** same functoriality. T_C = C (the swap). So
T_{CσC} = T_C ∘ T_σ ∘ T_C = C ∘ T_σ ∘ C.

**The critical question:** Is C (swap of generators) the same as γ₅
(golden Galois conjugation) on the character variety?

At the incidence-matrix level: YES. C swaps the φ and φ̄ eigenspaces
of M = [[1,1],[1,0]]. The Perron-Frobenius eigenvector carries the
letter frequencies d(a) = 1/φ, d(b) = 1/φ². C sends these to
d(a) = 1/φ², d(b) = 1/φ, implementing φ → φ̄.

At the character variety: OPEN. The question is whether the swap
C: (x,y,z) → (y,x,z) acts as γ₅ on the specific trace axes (T3, T7)
that γ₅ is known to flip (from B766). The B766 flip-table:
- γ₅ flips T3 (basepoint) and T7 (time's direction)
- θ flips T6 (chord sign)
- c flips T4 (chirality) and T6 (chord sign)

## The computation

### Phase 1: ALGEBRAIC (3 agents, parallel)

**Agent A1: SL(2) four trace maps.**
Compute T_σ, T_{σ_mirror}, T_{CσC}, T_{RCσCR} at SL(2) using SymPy.
Verify: T_σ = T_{σ_mirror} (θ trivial), T_{CσC} = C∘T_σ∘C.
Evaluate at the geometric point A=[[1,1],[0,1]], B=[[1,0],[-ω,1]].
Verify the Sütō invariant is preserved by all four.

**Agent A2: Incidence-matrix eigenspace analysis.**
Compute M_σ = [[1,1],[1,0]], M_{CσC} = [[0,1],[1,1]].
Show both have eigenvalues φ, -1/φ but different eigenvectors.
Verify: C swaps the Perron-Frobenius eigenspace with the φ̄ eigenspace.
This is "γ₅ at the linear level."

**Agent A3: SL(3) = Sym² trace computation.**
At the geometric point, compute all Sym² matrices and trace coordinates.
Apply the swap C (A↔B) and check which trace coordinates change.
Compare with B766's γ₅ action (flips T3, T7) and θ action (flips T6).
Does C at SL(3) match γ₅? Or θ? Or neither?
Read B766 compute.py and audit_compute.py for exact T-axis definitions.

### Phase 2: TANGENT SPACE (1 agent, sequential)

**Agent A4: Derivative of the trace map.**
Compute Jacobians dT_σ and dT_{CσC} at the geometric point on V0.
Decompose into θ-even and θ-odd sectors.
Check: do the Jacobian eigenvalues involve φ? Does C swap φ ↔ φ̄
eigenspaces at the tangent level?
Connect to B759's coupling norm √3.

### Phase 3: SYNTHESIS (1 agent, sequential)

**Agent C1: Grade both intertwining theorems.**
θ intertwining: confirmed/refuted at each level.
γ₅ intertwining: does C = γ₅ at the character variety?
Consequence for the observer programme:
- If C = γ₅: complement is observer-side geometrically, γ₅ closable,
  pointer closes 2 bits (θ + γ₅), residual = ⟨c⟩
- If C ≠ γ₅: the two levels disagree, the bridge is broken or partial
Updated score card for the observer programme.

## Preregistered predictions

P784.1: T_{σ_mirror} = θ ∘ T_σ ∘ θ at SL(3) — PASS (by functoriality)
P784.2: T_{CσC} = C ∘ T_σ ∘ C at SL(2) — PASS (by functoriality)
P784.3: C = γ₅ at the incidence-matrix level — PASS (eigenspace swap)
P784.4: C = γ₅ at the SL(3) character variety — OPEN (the hard test)
P784.5: The tangent-space coupling norm √3 appears in the C decomposition — OPEN
