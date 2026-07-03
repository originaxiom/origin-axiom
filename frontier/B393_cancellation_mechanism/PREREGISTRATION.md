# B393 (Closure II / M1) — PRE-REGISTRATION: the convolution-cancellation mechanism

**Committed before computation. Target: WHY the three dark pairs {(1,3),(1,4),(3,5)}
cancel — both local spectra are pairing-visible (P67/attribution), yet the convolution's
√−15 channel is identically zero. Time-box: 2 sessions.**

## The objects (all exact, from banked machinery)

Per pair: the local spectral vectors x₃(a,b) ∈ ℚ(ζ₁₂)⁴ and x₅(a,b) ∈ ℚ(ζ₂₀)⁸ (DFTs of the
local tables, field coordinates as in attribution_pairing.py), and the rank-2 pairing B.
The s-channel of the global cell: s(t(A,B)) = Σ over the convolution lattice
{(a,b)+(a′,b′) = (A,B)} of B(x₃(a,b), x₅(a′,b′)).

## Registered candidate mechanisms (tested in order)

- **K1 (character orthogonality):** for the cancelling pairs, x₃'s B-image and x₅ live in
  DISJOINT character sectors of the convolution group — i.e. the ζ-characters carried by
  the 3-side B-row-space never meet the 5-side support at matched frequencies (an exact
  support-disjointness statement in the (a,b)-frequency lattice).
- **K2 (Galois-isotropy):** the 3-side spectrum lies in a Galois eigenline L with
  B(L, x₅-span) forced to a τ-odd subspace whose H-average kills s specifically (an exact
  one-line Galois argument; distinguishable from K1 because it would kill s but not
  necessarily z).
- **K3 (sign pairing):** the convolution sum cancels by an explicit involution on the
  lattice pairing terms t ↔ ι(t) with B-values opposite — exhibit ι (translation/mirror
  type; must be stated arithmetically, not per-cell).

KILL: none of K1–K3 — bank the exact per-frequency cancellation table and STAGE with the
ledger (the mechanism then likely needs the all-pairs formula view, M4 — noted as the
re-entry).

## Acceptance

The mechanism must (i) verify on all three cancelling pairs, (ii) FAIL on the seven bright
pairs (it must not over-kill), and (iii) explain why {(1,5),(4,5)} instead die by the
kernel (the two dark classes must be distinguished by the mechanism's own terms).
Machinery: attribution_pairing.py field-coordinate code; exact throughout. Firewalled.
