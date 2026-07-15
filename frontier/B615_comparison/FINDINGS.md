# B615 — THE COMPARISON (Branch 3): AMBIGUOUS, corrected p = 0.078

**Status: banked (frontier). The Listening Campaign's Branch 3, run ONCE,
mechanically, under the director-approved design (B614, sha 9a189f49…,
hash verified in-run). CC reports; interpretation is chat-1's lane; SEAT 4
REVIEWS THIS RAW RECORD FIRST. Lock `tests/test_b615_comparison.py`.
Full pair table: `comparison_output.txt` (every one of the 217 pairs).**

## Disclosure for seat 4 (before anything else)

1. Two implementation bugs against the design's own §4 formulas were
   found and fixed AFTER a first statistics printout: G3's null had been
   coded linear-[0,1] instead of the design's log-uniform, and the Šidák
   combination was inverted; G4 also double-counted R1 against the SET
   clause. **The match rows never changed** (they are window comparisons,
   independent of the null); only the null arithmetic did. Both outputs
   are in the session record; the fixes brought the code INTO compliance
   with the pre-sealed design. Verdict moved from a mislabeled
   STRUCTURED-NULL to AMBIGUOUS.
2. The measured targets are PDG 2024 central values recorded from the
   assistant seat's knowledge (flagged in the script header). All are
   accurate far inside the 1e-2 tier. NOTE for review: the PMNS targets
   carry experimental uncertainties of order several percent — the
   point-value windows understate the effective null probability for
   those rows; a target-uncertainty-aware re-analysis can only WEAKEN
   the observed significance.
3. The design text's "26 fractions" estimate vs the actual 17-member SET
   (the SET clause governs; noted in-run).

## The raw result

- **G1 (amplitudes × couplings): ZERO matches at both tiers.** The
  couplings hear nothing.
- **G2 (amplitudes+fractions × angles), tier 1e-2: THREE matches**
  (expected 0.57 under the null; raw tail p = 0.020):
  (4/7)sin²(4π/7) = 0.5431 vs sin²θ₂₃ = 0.546 (dev 0.52%);
  1/(2φ) = 0.30902 vs sin²θ₁₂ = 0.307 (dev 0.66%);
  4/13 = 0.30769 vs sin²θ₁₂ = 0.307 (dev 0.23%).
  **Tier 1e-3: ZERO** — none survive the tight tier.
- **G3 (ratios × mass ratios): ZERO matches at both tiers.**
- **G4 (the hierarchy): one match** — τ₈/τ₄ = 3.86×10¹⁴ vs
  M_GUT/M_Z = 2.19×10¹⁴ within the declared half-decade (expected 0.68;
  tail 0.50 — fully null-compatible).
- **Šidák-corrected best-grid p: 0.0775 (tier 1e-2); 0.94 (tier 1e-3).**

## THE VERDICT (per the locked table)

> **AMBIGUOUS** (0.01 ≤ p < 0.1): banked as suggestive-only. NO
> escalation. Per the sealed design, any further test requires a NEW
> sealed design on held-out, not-yet-computed quantities — the designated
> held-out set is the m136 classical side (its torsions and hearing
> integers), whose computation now becomes the decisive next arc.

Structural notes for the record (description, not interpretation): two of
the three G2 matches hit the SAME target (sin²θ₁₂); all three matches are
angle-family; the amplitude family's within-[0,1] values found no
coupling; the tight tier is empty everywhere. The 1/(2φ)-vs-solar-angle
proximity is a long-noted coincidence in the wider literature; the sealed
protocol treats it identically to every other pair.

## What happens next (per the design and the campaign)

Seat 4 reviews; chat-1 interprets after. CC's decisive follow-up, per the
AMBIGUOUS clause: the m136 classical port (B616+) — the held-out set —
under a fresh sealed design. If the held-out set reproduces angle-family
matches at matched precision, that is a signal; if not, the suggestion
dies and the stopping rule closes the SM-values question at this level.

## Addendum — the robustness (algebraic-mimic) ensemble (design §4, completed)

Run mechanically as part of the same record (`b615_robustness.py`,
`robustness_output.txt`; 10⁶ draws per declared mimic family, fixed seed
in-script): the expected G2 pair-match counts under the mimic families
are 0.55 ((a+b√5)/c), 0.59 ((a+b√2)/c), 0.51 (p/q) — bracketing the
primary uniform null's 0.57 — with raw tails P(X ≥ 3) ≈ 0.019, 0.023,
0.015 versus the primary's 0.020. **The analysis is
ensemble-insensitive; the AMBIGUOUS verdict stands under both ensembles.**
Notably, ~1.1% of random matched-complexity algebraic numbers in (0,1]
land in the sin²θ₂₃ window and ~0.6% in the sin²θ₁₂ window at the coarse
tier — the angle windows are not hard to hit by chance, which is exactly
what the corrected p already said.

**The seat-4 packet is complete:** the hashed design (B614), the full
pair table, the null statistics under BOTH ensembles, the disclosures,
and this addendum. The hash was the gatekeeper; the review is
retrospective, per the director's order.
