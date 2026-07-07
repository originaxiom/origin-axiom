# B447 — D2: the m-scan harness (Thermodynamic Campaign, decisive probe 2)

**Status: banked (frontier). Firewalled; nothing to `CLAIMS.md`. Prereg: `PREREGISTRATION.md`
(committed before computation, PR #590). Verdict: LAUNDERS across all observables — including one
flag that survived SIX artifact tests and was then laundered the earned way, by an exhibited
parameter-free F (the 8-moment class-arithmetic surrogate) that reproduces the flag itself,
out-of-sample at all three couplings. No H1. The prereg's stated prediction, confirmed.**

## What was computed

Five warm observables across the metallic family `m = 1..6` (substitution `a→aᵐb, b→a`, diagonal
model, onsite ±V), with periodic/random simpler-system controls and the m=4 same-field
(`ℚ(√5)`) partner: specific heat C(T); transport exponent β(V); spectral dimensions D_q;
gap-label realization on `ℤ+ℤθ_m` (θ_m = 1/(1+λ_m), the module trap guarded); Lyapunov γ(E).
Classifier: self-calibrated leave-one-out (quadratic in log λ_m), flag iff golden's LOO error
> 3× the median of the others AND > 5% of the spread.

## Gates (reproduce-known-numbers first)

| gate | target | measured |
|---|---|---|
| three-regime transport | periodic β=1, random β≈0, metallic strictly between | 0.998 / 0.186 / 0.58–0.64 ✓ |
| gap-label module | labels on ℤ+ℤθ_m | residuals ≤ 6.5e-4, all m ✓ |
| permanent criticality (B181, class-wide) | γ≈0 on-spectrum, all m | 0.0008–0.0018 (noise floor, scales down with N) ✓ |
| **prereg correction (documented):** the "B163 D₀ anchors 0.91/0.77" were **B186's trace-map** box dims — a different object; the anchor as pre-registered was inapplicable and was replaced by a two-size consistency gate. |

**In-session bugs caught before any reading** (the honest record): the D_q estimator returned −D_q
(sign; fixed); classifier v1 (error/fit-RMS) exploded on near-perfect interior fits (replaced by
the self-calibrated LOO); the T-grid argmax had 2.9% quantization (replaced by fine grid +
parabolic interpolation).

## The three flags, and how each resolved

1. **γ_on — DISSOLVED (noise floor).** Scales down with N (0.00096 → 0.00032 from N=1000→10000);
   all m consistent with 0. Permanent criticality is **class-wide**; golden not special.
2. **D₀ — NOT SUPPORTED (estimator non-convergence).** The box value for golden drifted **−0.072**
   between N=1500→2500 (10× every other member) and the m-ordering flipped with size — the box
   estimator cannot support an exceptionality claim. The exact transfer-matrix **band method** at
   the well-resolved members (m=1: 350/377 bands, m=2: 237/239, V=1) gives **golden 0.7380 ≈
   silver 0.7363**. At V=2 the band method itself fails honestly (bands exponentially thin — 28
   of 377 visible at a 60000-point grid); a converged m-scan of D₀ needs an adaptive recursive
   band-edge tracker — **named follow-up, not built here**. No golden D₀ exceptionality survives
   at achievable resolution.
3. **C_peak_T — the real one: SURVIVED SIX TESTS, then LAUNDERED BY AN EXHIBITED F.**
   The flag: golden's high-T specific-heat peak sits ~2% above the family's smooth extrapolation.
   It survived: three fit variables (log λ, θ, 1/λ: 5.0–9.2×), fine-grid + parabolic
   interpolation (5.53×), exact σ-normalization (σ matches the θ_m second-moment formula to 5
   digits, flag persists at 5.79×), branch-tracking (the argmax follows one peak branch
   consistently), **N-doubling (values stable to 4 decimals)**, and the V-scan (relative offset
   5–6× at V = 0.5, 1, 2). A formal H1-candidate under the prereg protocol → the
   **burden-inversion session**:
   - **Declared bounded F (cap K≤4):** the peak_T of the C(T) of the **K-point Gauss quadrature
     of the DOS** (Lanczos/Golub–Welsch) — equivalent to the first 2K spectral moments, which are
     **exact class arithmetic** (tr(Hᵏ)/N = substitution letter/pair statistics). Parameter-free.
   - **Result at K=4 (8 moments):** the surrogate reproduces the peak values to 0.3–2% AND
     **reproduces the flag statistic itself** — classifier on the *surrogate*:
     e1/med = **5.53 / 5.72 / 5.43** at V = 0.5 / 1.0 / 2.0, vs measured 5.09 / 5.53 / 5.36.
     Nothing fitted; all three couplings out-of-sample.
   - **Verdict: LAUNDERS.** The golden offset is fully contained in the first 8 spectral moments —
     the letter-frequency arithmetic of the class (θ₁ closest to ½ = the m=1 face of the
     whitelisted CF-extremality mechanism). The "exceptionality" was the failure of polynomial-in-λ
     fit families to track exact moment arithmetic, not new structure.

## The positive by-products (banked with the harness)

- **The m-scan harness itself** — the campaign's new standard control (m=1..6, m²+4-stratified,
  m=4 field-partner, LOO classifier) — reusable for every subsequent probe (`harness.py`).
- C(T) peak-branch coarsening across the family: 3, 3, 2, 2, 1, 1 peaks (hierarchical-spectrum
  Schottky structure, class-generic, consistent with the log-periodic literature).
- The high-T peak law: peak_T is 8-moment-determined across the family at all tested V — a small,
  clean class-level fact (not claimed novel; the moment method is standard).
- β(V) decreases with V for all m (anomalous, sub-ballistic — the Damanik–Tcheremchantsev regime
  structure), no m=1 exceptionality (LOO smooth at both V).

## Verdict (campaign bins)

**LAUNDERS — every flag either dissolved under the right estimator or was demonstrated (not
asserted) to be whitelist arithmetic via a parameter-free, out-of-sample F.** No NEW-MATH claim
(the moment-surrogate method is standard). **No H1.** Consistent with D1: the object's
condensed-matter warm layer reads back class arithmetic (θ_m, λ_m, moments) — the frozen
whitelist, warm.

## Reproduce

```
python3 harness.py            # gates + m-scan + classifier (~10 min)
python3 flagtests.py          # flag round 1 (N/fit-form/noise-floor)
python3 flagtests2.py         # fine-grid peak + band-method D0 (V=2 fails honestly)
python3 flagtests3.py         # N-doubling + V-scan of the C_peak_T flag
python3 burden_inversion.py   # the exhibited F (K-point moment surrogate)
pytest ../../tests/test_b447.py
```
