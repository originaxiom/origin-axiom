# B359 — the seam form: pair-specific, parity-selective, exactly

**Status: banked (frontier), EXACT tier (Fraction arithmetic over `ℚ(ζ₆₀)`, B358's engine; the committed
readout is regenerable end-to-end). The first L57 computation — the cross-session "seam form" proposal, run the
same day it was made. Firewalled; nothing to `CLAIMS.md`; field-membership mathematics, not physics.**

## The question (pre-registered)

B358 certified that the theta-lift Par-inserted **(1,2)** pair invariants carry `√−15` (44/49 doubles, exact
rationals) while the canonical lift carries none. The declared next question: run the identical exact readout
on pairs **(1,3)** and **(2,3)** — are the seam coefficients **pair-specific** (a seam-valued pairing structure
on the metallic family) or shared/absent? Independently, the cross-session seat's own symbolic certificate for
the (1,2) flagship (integer vectors mod `Φ₆₀`, Galois-norm inversion) was run on this machine first and
**PASSES** — `s = 1/48` exactly — making three independent exact paths to B358's flagship before this probe ran.

## The result — a selection rule, not a uniform glow

| pair (theta lift) | nonzero doubles | seam-bearing | the `s`-value set |
|---|---|---|---|
| (1,2) golden×silver (B358) | 49 | **44** | `{±1/48, ±1/80, ±1/120, ±1/160, ±1/240, ±1/480, …}` |
| **(1,3) golden×bronze** | 39 | **0** | **∅ — seam-dark, exactly** |
| **(2,3) silver×bronze** | 39 | **18** | `{±1/144, ±1/288}` — **disjoint from (1,2)'s set** |
| canonical lift, all pairs | 49+39+39 | **0** | ∅ (the control dichotomy, again) |

Sample exact entries, (2,3): `t_H(P₀Q₂) = 1/144 + (1/144)√5 + (5/144)√−3 + (1/144)√−15`;
`t_H(P₁Q₀) = 1/288 + (1/288)√5 + (5/288)√−3 + (1/288)√−15`.

**The two headline structures:**
1. **Pair-specificity, strongly:** not only do bright pairs carry *different* exact `s`-sets ((1,2) vs (2,3)
   completely disjoint), but the values carry pair arithmetic — the bronze-containing pair's denominators pick
   up `9 = 3²` (144 = 16·9, 288 = 32·9) where (1,2)'s carry `3·16, 5·16, …`.
2. **A parity selection rule (observed pattern, 3 points):** both seam-bright pairs contain the **even** seed
   (silver, m=2); the odd–odd pair (1,3) is **exactly dark**. This is the repo's parity texture
   (B354's divisibility law; B356's mod-2 window) surfacing at the seam level. **Pre-registered prediction for
   the next run: (1,4) bright, (3,5) dark.** (Three points do not make a law — the prediction is the test.)

## Honest tiers and scope

- **EXACT:** all tables (both lifts, all three pairs), the (1,3) darkness, the (2,3) values, the controls.
  Committed artifact `seam_form_theta.json` regenerable by `seam_form.main()` (~8 min, pure Fractions);
  `regenerate_matches_banked()` is the OA_SLOW lock. The shared engine and theta construction carry B358's
  independent numeric guards.
- **OBSERVED PATTERN (not claimed as law):** the parity selection rule — 3 data points, one declared
  prediction. The seam-form-as-invariant question remains **L57** (is the theta-characteristic forced?); until
  L57 resolves, all of this is a statement about the explicitly-constructed lifts.
- Nothing promotes; K020 stands; these are field-membership facts about quantum invariants of two-seed
  pairings.

**Provenance.** B358 (the dichotomy + engine), the cross-session seam package + symbolic certificate
(verified here), L57 (`docs/OPEN_LEADS.md`), B354/B356 (the parity texture the selection rule echoes).
Reproducer: `seam_form.py`; test: `tests/test_b359_seam_form.py`.
