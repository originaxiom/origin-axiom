# B912 DRAFT — the sealed cell decides: OUTCOME B — OBSTRUCTION: the norm is indefinite on every COLORED atom, (1,2) each; all nine colorless atoms are positive lines; the wall's norm splits the 27 as (15,12)

**Date:** 2026-08-05 · **Seat:** multiagent computation seat (R1), for cc banking ·
**Prereg:** `PREREGISTRATION.md`, SEALED BEFORE COMPUTE · **Run:** `norm_cell.py` →
`results.json` (36/36 checks PASS, end-to-end ~300 s).

## The verdict, VERBATIM against the sealed criteria

The seal: *"OUTCOME B — OBSTRUCTION: some atom-Gram is indefinite or degenerate —
the scale assignment fails as posed; the signature data and WHERE it fails become
the banked finding (R2/R3 then need a different construction, and the register
requires a dated amendment)."*

> **OUTCOME B fires. Six of the fifteen atom-Grams are INDEFINITE — exactly the
> six colored (3-dimensional, quark-type) atoms, every one with signature
> (1,2,0). None is degenerate (all Gram eigenvalues ≥ 0.489 in absolute value
> against residuals < 10⁻⁴⁰). All nine colorless (1-dimensional) atoms are
> definite — positive, after the declared normalization. The scale assignment
> fails as posed, and it fails precisely on the colored sector.**

OUTCOME A required *"H restricted to every atom is DEFINITE (all 15 atom-Grams
definite)"* — false at six atoms. UNSTABLE required *"J fails to exist or the σ±
cross-check fails"* — J exists (solved exactly, uniqueness proven), and the σ±
cross-check agrees on the entire declared readout to < 10⁻⁴⁰ relative (§5).

## 1. The construction (sealed step 1 — J)

- φ± = τ∘σ_χ rebuilt from B907 (τ's cocycle d by the same F₂ elimination, rank
  66); verified EXACTLY: involutions on all 78 basis vectors, automorphisms on
  all 3003 bracket pairs, charge pattern (ε₈,ε₁₄,ε₁₆,ε₂₂) = (−1,+1,−1,+1) on
  the four B854 charges — the banked wall pattern.
- The sealed premise "φ maps the 27 to its dual" is COMPUTED, not assumed: the
  linear intertwiner space Hom(27, 27∘φ) is 0 (verified at the full-tower prime
  40123). J is therefore antilinear-through-the-dual: J(u) = H ū, and the sealed
  equation transcribes through the frame's pairing into the rational system
  **(S): ρ(x)ᵀH + Hρ(φ(x)) = 0 for all 78 generators** — exactly the statement
  that H(u,v) = ⟨Jū, v⟩ is invariant under the real form g₀ = Fix(φ∘σ_split).
- (S) solved EXACTLY over ℚ. The Cartan equations force the support onto the
  weight pairing a = π(b), wt_a = −flip(wt_b) (π a 27-permutation with 12
  2-cycles and 3 fixed slots); the root equations connect all 27 remaining
  unknowns with zero conflicts ⟹ **existence AND uniqueness up to one real
  scale, proven by the elimination itself**. H± are integer ±1 signed-permutation
  symmetric matrices; (S) verified exactly on all 78 generators for both.

## 2. The Hermitian form (sealed step 2)

- H is real symmetric (Hermitian); |det H| = 1; nondegenerate.
- Exact raw signature by cycle count: 12 two-cycles contribute (+1,−1) each; the
  3 fixed slots (9,13,15) all carry −1 ⟹ raw (12,15).
- **Declared normalization:** H = +1 on the first canonical vacuum line = B889's
  block 0 = the vacuum line owned by frame 2 (B889's computed map {0:2, 1:0,
  2:1} reproduced from scratch here). The raw value on that unit line is
  −3.6281186…×10⁻¹¹ < 0, so normalization flips the global sign:
  **signature of H on the 27, normalized: (15,12)** — indefinite, as the e₆(2)
  noncompactness demands, and equal to the per-atom sum (atoms are mutually
  H-orthogonal to < 10⁻⁴⁸).

## 3. The atoms (sealed step 3 — the banked tri-partition basis)

Identification made exact first: the four charge matrices ρ(x₈),ρ(x₁₄),ρ(x₁₆),
ρ(x₂₂) commute pairwise (exact), and at the full-tower prime 40123 the probeB
construction (B906's banked DATA triples, rebuilt on the banked B883 27)
reproduces its chain dims (46,8,1)×3, its cell structure, and its 15 atoms —
six colored 3-dim + nine colorless 1-dim — and **each probeB atom equals a joint
eigenspace of the four charges, span for span, bijectively**. The banked
tri-partition basis IS the canonical joint-eigenspace decomposition of the
charge quartet. The ℂ-side atoms are that same decomposition at dps 60 (two
seeds, projector agreement 10⁻⁵²; invariance/scalarity residuals ≤ 10⁻⁴⁴; the
Π-blocks [1,1,1,8,8,8] and the three vacuum lines with their frame bijection
reproduced en route).

## 4. The readout (normalized, orthonormal atom bases in the frame metric)

| atom | dim | kind | signature | |det Gram|^(1/dim) |
|---|---|---|---|---|
| 0 | 1 | vacuum (frame 2) | (1,0) | 1 (the normalization line) |
| 9 | 1 | vacuum (frame 1) | (1,0) | 19.142020743905498523723… |
| 14 | 1 | vacuum (frame 0) | (1,0) | 1.6803202716718931117598… |
| 3, 4 | 1 | colorless pair | (1,0) | 53.078638438636745051644… |
| 7, 8 | 1 | colorless pair | (1,0) | 0.7862600340686760227939… |
| 12, 13 | 1 | colorless pair | (1,0) | 3.0889357198937381812466… |
| **1, 2** | 3 | **colored pair** | **(1,2)** | 1867.6882465382868116767… |
| **5, 6** | 3 | **colored pair** | **(1,2)** | 702.46346123720135020146… |
| **10, 11** | 3 | **colored pair** | **(1,2)** | 451.71617857652337422145… |

(35-digit values, per-atom Gram eigenvalues, and the μ₈,μ₁₄,μ₁₆,μ₂₂ tuples are
in `results.json`. The non-vacuum atoms come in complex-conjugate pairs with
equal invariants; |det|^(1/dim) is recorded for all 15 as data — under the seal
it is a well-defined *scale* only where the Gram is definite, i.e. on the nine
colorless atoms.)

**The banked signature finding:** 27 = 9 positive colorless lines ⊕ 6 colored
triples of signature (1,2) ⟹ total (15,12). Definiteness fails EXACTLY on the
colored sector, uniformly: every colored atom carries one positive and two
negative directions. Fenced observation: (15,12) coincides with the dims of the
27's K-types under e₆(2)'s maximal compact su(6)⊕su(2) (15 + 2·6), the standard
shape for an invariant Hermitian form on an irrep of a noncompact real form —
consistency with B907's form identification, no physics claim.

## 5. The σ± cross-check (the sealed gate)

Both wall involutions computed independently end-to-end. The entire DECLARED
readout is identical between σ+ and σ−: same normalization constant c₀ (0
relative difference at dps 60), same total signature, same 15 atom signatures,
same |det|^(1/dim) to < 10⁻⁴⁰ relative. **The gate passes on the declared
readout.**

Matrix-level fact, stated for the record (a theorem, not a computation error):
H₋ = H₊·D exactly, with D the diagonal ±1 involution exhibited in
`results.json` (tr D = 3). D commutes with all four charges (exact) — it
preserves every atom, acts as +1 on all nine 1-dim atoms (hence the identical
normalization), and as a non-scalar involution inside each colored triple. This
is forced: the global negation of χ differs from χ by the inner sign character
ε′(r) = (−1)^{ht r}, implemented by a torus element g₀ with φ₋ = Ad(g₀)∘φ₊, and
uniqueness of the (S)-solution transports H₊ to H₊·ρ(g₀). Literal matrix
proportionality of H₊ and H₋ is therefore impossible by rep theory for ANY
correct computation; the seal's gate is satisfiable — and satisfied — only in
the invariant/declared-readout sense just verified. Flagged for the banking
seat's ruling; treated here as a PASS because the gate's sealed purpose ("a
computation error by rep theory; recompute") is met by a deterministic,
independently re-derived, exactly explained agreement.

## 6. The disclosed prior (sealed §prior)

The prior leaned A. It was half right (H on the full 27 indefinite, sign
pattern tied to the compact/noncompact dichotomy) and WRONG where the cell
decides: definiteness does NOT hold atom-by-atom — the colored atoms each
straddle the split as (1,2). The fourth sealed cell in a row to overrule its
disclosed prior; the discipline is working.

## 7. Honest scope

- Exact: the frame, the rep verification (all 3003 pairs), φ± (all checks), the
  (S) solve + uniqueness + 78-generator equivariance, Hermiticity, the raw
  signature, the charge commutation, D and its properties, and the mod-40123
  atom identification (span-for-span).
- 35-digit-certified (dps 60, residuals printed): the ℂ-side atom bases, the
  vacuum-line values, the Grams and their eigenvalues — margins ≥ 0.489 against
  residuals < 10⁻⁴⁰; sign determinations are certified far beyond the sealed bar.
- The atom-span identification ran at the one full-tower prime 40123 (40639 was
  verified for probeB itself in B906); the ℂ-side needs no prime.
- The solo seat's `rep27.pkl` is a 27̄ realization (weight multiset = exact
  negatives); this cell computes on the banked B883 27 — noted, no discrepancy.
- |det Gram|^(1/dim) values are relative to orthonormal atom bases in the
  frame's coordinate Hermitian metric (the same convention B889's tables use);
  the declared vacuum normalization then fixes the global scale.

## 8. What follows (per the seal)

*"R2/R3 then need a different construction, and the register requires a dated
amendment."* The signature data to carry: the colored sector is where
indefiniteness lives, (1,2) per atom, and the colorless nine give well-defined
positive scales {1, 19.142…, 1.680…, 53.079…×2, 0.786…×2, 3.089…×2}. Gate 5
untouched; no physics identification is made here.

## Files

- `PREREGISTRATION.md` (sealed) · `norm_cell.py` → `results.json` (this run) ·
  this draft. Locks (`tests/test_b912_norm.py`) are the banking seat's step.

## Depends on

B854 (frame), B883 (the 27), B886/B889 (Π-blocks, vacuum lines, frames),
B898/B901/B907 (the wall pair φ±, the form e₆(2)), B906 (the banked atoms/DATA).
