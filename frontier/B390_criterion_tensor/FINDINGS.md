# B390 (W3.iii) — BANKED + PROMOTED (P67): brightness is a LOCAL property

**Status: banked; the locality reduction promoted (P67). The final arithmetic attribution
(which local invariant kills which dark pair — the correct bilinear pairing, NOT per-side
Π_H) is the named session-3 item. Pre-registration committed first. Firewalled.**

## The three registered gates — all passed

- **G1 (tensor identity, all pairs): 12/12** — C = C₃·C₅ cell-wise at (u₃,u₅) = (2,2) for
  every banked pair (previously proven only for (1,2)); 13/13 including (2,5).
- **G2 (locality of the classification): 12/12** — computing t = t₃ ⋆ t₅ from the LOCAL
  q=3 and q=5 tables alone and reading the √−15 channel reproduces the banked bright/dark
  classification exactly (bright pairs' s-cell counts: 44, 18, 36, 24, 20, 18, 12; all five
  dark pairs: zero s-cells).
- **OUT-OF-SAMPLE (registered): PASS** — pair (2,5) (ords 12×4), never previously computed:
  local-only prediction DARK (as registered: the seed-5 kill); full global level-15
  Par-table verdict DARK. The criterion predicts.

**The theorem-shaped statement (P67):** whether a pair (m₁,m₂) is s-bright at level 15 is
decided by the pair of local theta models at q=3 and q=5 alone — the global seam channel is
the convolution of the two local spectra, with no global ingredient. D3(a)'s riddle
((1,3) dark vs (3,4) bright with identical γ-data) is thereby LOCALIZED: the answer lives in
how the two local spectra pair, not in any global/group structure — consistent with, and
sharpening, the B385 kills.

## Named session-3 item (the attribution)

My per-side "content" columns (criterion.json) used Π_H per side — the standing hazard in a
subtler form (per-side H-projection is not the functional that pairs into √−15). The correct
object is the exact bilinear pairing ℚ(ζ₁₂) × ℚ(ζ₂₀) → (√−15-coefficient of Π_H(x₃x₅));
computing it and re-attributing each dark pair (5-side kill vs 3-side kill vs convolution
cancellation) is the final form. Until then the attribution column is UNRELIABLE and must
not be quoted.

**Provenance.** criterion_tensor.py (~15 min), the out-of-sample script →
{criterion.json, out_of_sample_25.json}; locks tests/test_b390_criterion.py.
