# The four-qubit compilation — the level-15 algebra as a measurable circuit

**(PD1.3. The κ-letter deliverable: the algebra physically realizable, its invariants measurable
as interference amplitudes. This document + the exact simulation constitute the in-sandbox half;
running it on hardware is an owner decision outside this campaign's scope. FIREWALL: realizing
the algebra on a device crosses the LETTER of the κ question — a real system whose algebra is
this algebra — not its SPIRIT, which asks whether nature uses it unprompted.)**

## Register and embedding

Four qubits = 16 dimensions; the theta space ℂ[ℤ/15] occupies computational basis states
|0⟩…|14⟩; |15⟩ is held fixed by every gate (all word unitaries U satisfy U|15⟩ = |15⟩, giving
the exact embedding correction tr₁₆ = tr₁₅ + 1 used below).

## The two primitives (exact; everything else is words in them)

- **D̂** — a 16-dim diagonal phase gate: phases ζ₁₅^{j(j−1)/2} on |j⟩ (j = 0…14), 1 on |15⟩.
  Exponents j(j−1)/2 mod 15: 0,0,1,3,6,10,0,6,13,6,0,10,6,3,1.
- **ÛF** — the unitary 15-point DFT ⊕ [1]: entries ζ₁₅^{jk}/√15 on the theta block.
  Verified exactly: ÛF·ÛF† = I (an identity in ℚ(ζ₆₀)); synthesis to native gates is a
  standard unitary-synthesis step (engineering, not mathematics).
- Then WR̂ = ÛF·D̂⁻¹·ÛF† **equals the banked generator exactly** (verified), the seeds are
  Ŵ_m = WR̂^m·D̂^m, and Par is the classical bit-permutation j ↦ −j mod 15.

*The CRT alternative (5 qubits):* the banked factorization W₁₅ = perm·(W₃ ⊗ W₅^tw)·perm
compiles the same algebra as QFT₃ ⊗ QFT₅ conjugations on a 2+3 qubit split with the twist
permutation; documented as the layout that scales to composite levels.

## The measurement protocol (all constants declared)

For each of the 240 words U(j,l) = Par·Ŵ₁^j·Ŵ₂^l (j < 20, l < 12): a controlled-U Hadamard
test on the maximally mixed register returns amp(j,l) = tr₁₆(U)/16 (Re from ⟨X⟩, Im from
−⟨Y⟩ on the ancilla). Post-processing:

    t(a,b) = (1/240) · Σ_{j,l} ζ₂₀^{−ja} ζ₁₂^{−lb} · (16·amp(j,l) − 1)

**Exact simulation verdict (`circuit_simulation.py`): the reconstruction reproduces the banked
seam cells exactly** — the flagship t(0,4) = −1/48 − (1/80)√5 − (1/48)√−3 + (1/48)√−15 and
(0,8), and the minimal-sector cells (6,2), (14,10) at ±1/48. The ±1/48 as a reading on an
instrument, in exact arithmetic.

**The κ-word:** U_κ = D̂·WR̂·D̂⁻¹·WR̂⁻¹ (the Weil image of the classical commutator [R,L]) is one
more word in the primitives; its trace is exactly **1** (measured the same way).

## Feasibility honestly

240 words × one Hadamard test each; the target values are rationals with denominators ≤ 480,
so resolving ±1/48 against 0 needs amplitude precision ≲ 10⁻³ ⇒ order 10⁶ shots per word
(before error mitigation) and controlled-word depths set by the synthesis of ÛF — nontrivial
but within the regime of current cloud devices for a dedicated effort. No claim is made here
about noise robustness; that is the hardware study's first question.
