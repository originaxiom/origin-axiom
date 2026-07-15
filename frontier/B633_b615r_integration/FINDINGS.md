# B633 — B615-R integrated: the last SM residual DISSOLVES (verdict A); the closure hardened

**Date: 2026-07-15. Status: BANKED (verified on receipt, integrate-don't-
merge). Source: seat 4's sealed re-analysis packet (design + runner
hashed pre-run, SEAL.txt reproduced here; outputs banked verbatim).
This seat's verification: the seal hashes CHECK against the delivered
files, and an independent rerun of the self-contained runner reproduces
the headline exactly (p = 0.1450, verdict A; sensitivities c2 = 0.3152,
c3 = 0.1450).**

## What B615-R fixes (the Level-1 defect, real and now-corrected)

B615's targets mixed schemes and scales (pole m_t over MS-bar m_b(m_b);
m_b(m_b) over m_s(2 GeV) — the same physical ratio spans 36–61 across
conventions) and carried no uncertainties. Since the object supplies no
scale (banked), "object number = SM value" is not well-posed until a
scheme and μ are stated — the firewall theorem showing up inside our own
methodology. B615-R re-runs the identical sealed grids with:
uncertainty-aware windows, NuFIT 6.1 / PDG-2026 centrals, the
other-octant θ₂₃ sensitivity, and three stated scheme columns for G3.

## The verdict (all variants, Šidák-corrected best-grid p; B615 recorded 0.0775)

- a (uncertainties alone): **0.62**
- b (new centrals alone): **0.35**
- c (both — HEADLINE): **0.145 → VERDICT A: the AMBIGUOUS dissolves;
  Branch 3's SM-silent closure is HARDENED on scheme-stated,
  scale-stated, uncertainty-correct inputs.**
- c2 (other-octant θ₂₃): 0.315; c3 (scheme-consistent G3): 0.145.

Notable inside the null: NuFIT 6.1 flipped the θ₂₃ octant (0.470), so
B615's best coarse match (0.5431 vs 0.546) dies as a central-value
match; and sin²θ₁₂ = 0.3088 ± 0.0067 sits 0.03σ from 1/(2φ) — priced
honestly: the same ±1σ window contains 4/13, 8/25, 3/10, 225/692 from
our own inventory, so the tightness carries no extra evidence. **The
zero-cost forward row: JUNO-class precision (~0.5% on sin²θ₁₂) will
separate 1/(2φ) = 0.30902 from 4/13 = 0.30769 from 0.3088 — nature
adjudicates the golden question within a few years; no seat does
anything.**

## Adopted governance artifact

Seat 4's **Input-Completeness Ledger** (the mandatory 12-item per-cell
checklist for any SM-facing design: scheme per quantity, scale + μ
rationale or scan, full posteriors, convention flags, look-elsewhere
across variants, MB13 grep, the firewall question) is adopted as
`docs/INPUT_COMPLETENESS_LEDGER.md` and joins the sealing checklist
(MB12 + MB13-in-doc + pipeline controls + this ledger).

## The consolidated Branch-3 final state (superseding B628's)

Across B614/B615 (sealed grids), B616 (control object), B627/B628
(held-out exterior families), B629–B631 (the matrix layer), and now
B615-R (corrected inputs): **every SM-facing comparison is null or
dissolved; the single residual (p = 0.078) is gone at p = 0.145–0.62
under every correction separately and combined. The SM-values question
is closed at every tested level, on hardened inputs.** The mathematics
publishes as mathematics; the JUNO row waits; any future comparison
needs the owner's directive + the full sealing checklist.

## Lock

tests/test_b633_b615r.py: the seal hashes of the banked copies; the
runner reruns (self-contained, ~seconds) and the headline line asserts.
