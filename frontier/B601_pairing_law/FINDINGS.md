# B601 — the pairing law across levels + the trace law (the V2 defect refined)

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities.
Structure-scan tier; the MB12 triple-check registered in the script
docstring before running. Lock `tests/test_b601_pairing_law.py` (ungated,
~15 s). Run: `python3 pairing_law_scan.py`.**

## 1. The pairing is a spectral fact at every level; the basis is golden-only

The full odd hearing form B_odd = −Uᵀ·W_RL·U (U = the pair-direction
basis; the identity uᵀ(CW)u = −uᵀWu for θ-odd u makes this the hearing
form) computed at k = 2..7, 12 (κ = 5..10, 15):

- **The SPECTRUM is conjugation-closed at EVERY level** (char poly real;
  eigenvalue multiset conjugate-symmetric) — the conjugate-paired hearing
  structure persists at all levels as a basis-independent fact.
- **The naive DIAGONAL multiset is conjugation-closed ONLY at κ = 5**
  (where dim_odd = 2 and the weight-label basis IS the spectral basis).

**What this does to outcome B:** the verdict stands as sealed (V2's cell
was defined in the naive basis and genuinely failed), but the defect is
now located: it is a BASIS defect, not a structure defect. Level transport
of the pairing exists spectrally; it does not pass through naive weight
labels — the same shape as B596's null (the clock is not the naive
cat-map period). Any future level-transported comparison must use the
spectral basis.

## 2. THE TRACE LAW (two indicators; two registered discriminating confirmations)

trace(B_odd) is REAL at every level and obeys, on the full grid
κ ∈ {5,...,12, 15, 16, 18, 20, 24, 25} (14 points, all exact to 1e-8):

> **trace(B_odd)(κ) = [5|κ]/φ − [4|κ]**

(values: +1/φ at κ = 5, 10, 15, 25 (and 30, 35 in the exploratory
extension); 0 at κ = 6, 7, 9, 11, 18; −1 at κ = 8, 12, 16, 24;
−1/φ² = 1/φ − 1 at κ = 20 and 40). The mod-4 clause was REGISTERED as a
conjecture after seeing κ ≤ 15 + 20 and CONFIRMED on the discriminating
predictions κ = 16 → −1 and κ = 40 → −1/φ² before the final form was
written — predictive, not post-hoc.

## 3. The cross-model identity: LAW-O is stage-universal

tr_odd(RL) = [4|κ] − [5|κ]/φ (the hearing minus of the above) is
**EXACTLY B587/B585's LAW-O**, there derived in the finite Weil model via
the ±-symmetrized Weyl assembly. The same two-indicator law now holds in
the SU(3)ₖ modular stage: the odd RL-trace law is STAGE-UNIVERSAL across
the two quantum models. This is the second cross-model bridge after
B595's det(I − B_odd) = φ² and strengthens the reading that the object's
golden channel (the 5-divisibility indicator) and the framing channel
(the 4-divisibility indicator) are properties of the OBJECT-stage
coupling, not of any one stage.

## Anchors

P3-V2 (#961, the defect on record), B587/B585 (LAW-O), B595 (the spectral
bridge), B596 (non-naive level transport), B593 (the hearing law).
