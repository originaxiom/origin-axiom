# B1791 — Im τ IS NOT FOUND FORCED IN B1656'S FRAME (MAIN'S PLAN, STEP 4; DATA-FREE): EVERY CANDIDATE EXAMINED EITHER CLOSES OR TRADES THE INPUT FOR A FREE RATIO OR A DISCRETE CONVENTION — THE ONE LINE-INDEPENDENT HEIGHT FOUND, THE ρ′ HIGGS'S PETERSSON PEAK AT Im τ = 2.8406, IS SET BY THE η-POWER CONVENTION AND LIES OUTSIDE THE SIX'S STRIP; Im τ STAYS A COUNTED CONTINUOUS INPUT

**Verdict: NEGATIVE ("Im τ is forced by the frame" — not found).** Data-free; one post hoc sentence, labelled, in § 3. cc
(main), 2026-10-28, step 4 of main's plan (docs/MAINS_PLAN.md, P-393; P-373). Corrected before landing at its hostile
referee (§ 5). **0 of 19.**

## 1. What the record closes

- **The special points:**
  - **ω and i:** no 2–3 hierarchy at ω (where the exponents follow the residual ℤ₃ charge), nor at i (B1691).
  - **The state's cusp shape 2√3 i:** sealed, NEGATIVE (P-244, B1696).
  - **Other cusp shapes:** NEGATIVE (B1702).
  - **The strength's saddle 0.2754 + 0.9613i:** no hierarchy (B1699).
- **The thread's apexes:** the six at the thread's own point, NEGATIVE (B1720); which thread, NEGATIVE (B1722); the apex
  rule withdrawn (P-350, B1749).
- **The coupling's strength:** the Petersson-normalised y s₁² has no maximum; it rises to the cusp (P-247, B1699).
- **One-loop dynamics:** every forced content runs to the cusp, and holding the band needs a free content ratio in a 13%
  window (B1784; the SM seat's W154 as read, row 1388, not verified in an arc). P-380's Stage B is still owed.
- **Channel thresholds:** no threshold or crossing marks the band (audit/verify_tau_threshold).
- **The literature:** no published mechanism derives Im τ ≈ 3 without a chosen continuous ratio (P-382).
- **B1667's horocycle:** L is of order one and smooth.

## 2. Computed (`verification/functionals.py`; the referee's `verification/referee/`)

**The draft's scan** (`functionals.json`): B1726's compute() internals with the Higgs DR and L_max, on three slope-2/5
lines × Re τ ∈ {0.1, 0.3, 0.7} × Im τ 1.5–8 (243 points).
- ‖Y‖_F, Σσ and σ_max rise monotonically, toward the cusp.
- |det M| falls.
- Σ c_s converges at height. Its limit is 8.270 on most lines, but **3.796 for the up sector on (2/5, 1/10)**, the strip's
  own line, where the up i-channel is off.

**The evidence is weaker than the draft's count suggests** (the referee):
- The 108 Petersson-weighted series cannot fail: a rising σ_max times y^p always rises.
- ‖Y‖_F, Σσ and σ_max share one line-blind growth (d ln σ/dy ≈ 1.44), which is B1699's S₀ again.
- Down equals leptons for two of the functionals.
- Three of the draft's four "interior extrema" are one event.
- The scale-free ratios do have extrema, scattered by line, Re τ and sector over Im τ 1.05–3.5 (σ₃/σ₂ in 279 of 336
  series, σ₂/σ₁ in 93), none line-independent. Below 1.5 the seat's strength has minima at 1.05–1.25 (10 series).
- L is frozen above Im τ 4 at 16 of the 27 heights, an extrapolation B1726's instrument never made (it stops at 3.45). L₂
  was not scanned.

## 3. The one line-independent height: the ρ′ Higgs's Petersson peak (the referee; `referee/fine_eta.py`)

B1691: the ρ′ sections are η⁶ times ρ_R's ("changes no ratio"). But in ρ′ the Higgs η⁶∂R (weight 9/2) decays at the
cusp, and its Petersson norm y^(9/4)|η|⁶|∂R| **peaks at Im τ = 2.8406 for every Re τ** (leading order 9/π = 2.8648). It is
line-independent, since the Higgs is line-free.
- **The family y^((3+m)/4)|η|^m|∂R| moves the peak with m:**
  - its leading order is 3(3+m)/(π(m − 3));
  - m = 5 gives 3.82, m = 6 gives 2.84, m = 7 gives 2.31;
  - η⁶R peaks near 1.0–1.1 and η⁶∂²R at 4.138.
- **So the height is set by a discrete convention,** the η power, i.e. which ρ′ representative is normalised. A height
  appears, but the input is traded for a convention, not removed. The same holds for (b) below.
- **Post hoc, labelled:** no integer m lands in the six's strip, Im τ 2.96–3.11 (P-373). B1691's m = 6 sits at 2.84, about
  4–9% below it.

## 4. The candidates

| candidate | verdict |
|---|---|
| (a) an extremum of a natural frame functional | the strength-type functionals rise to the cusp; the scale-free ratios' extrema are line-dependent; the ρ′ Higgs's Petersson peak is line-independent but set by the η-power convention (§ 3) — **trades the input for a convention** |
| (b) a normalisation (e.g. σ_max = 1) | trades Im τ for a scale input |
| (c) special points, cusp shapes, thread apexes | closed (§ 1) |
| (d) the horocycle L(Im τ) | smooth and monotone; marks no height |
| one-loop potential | trades Im τ for a free content ratio (W154 as read; B1784) |
| (e) the audit lane's relative gauge thresholds (P-396) | **does not involve τ as written.** Its H_R(q) belongs to a compact-core flat Wilson connection exp(iθQ), zero on the tail, with θ supplied, and with the metric, regulator and light-mode split as priced duties. Neither its map nor its relay mentions τ, a fibre or the lines w = ατ + b. Linking it to Im τ would be main's identification, and the lane already brings θ and h (row 1422) |

**Not examined:** non-perturbative and flux potentials; P-380's Stage B; P-327 and P-343 (both queued, the same question).

## 5. The referee (hostile, read-only, before landing; `audit/referee_s227_imtau/`, kept in `verification/referee/`)

1. **BLOCKING, applied:** the draft's "nothing singles out a height" and "(a) closed" were false. The ρ′ Petersson peak at
   2.8406 is line-independent, but it is set by a convention (§ 3).
2. **BLOCKING, applied:** the draft's route (e) claimed the audit lane's H_R(q) would depend on τ. As written it does not
   (§ 4).
3. **CORRECTION, applied:** the missed closures B1702, B1720/B1722 and P-350/B1749 are cited; P-343 and P-327 are named;
   the one-loop closure is scoped to W154 as read.
4. **CORRECTION, applied:** Σ c_s for up on (2/5, 1/10) is 3.796.
5. **CORRECTION, applied:** the evidence is weaker than the draft's count (§ 2).
6. **NOTE, applied:** the minima below 1.5, L frozen above Im τ 4, L₂ unscanned, and the strip 2.96–3.11.
7. **Checked and sound:**
   - the citations match their sources;
   - the sweep reproduces;
   - the referee's scan reproduces functionals.json to 4 × 10⁻¹⁶;
   - cA matches the mpmath cB to 10⁻⁶ at Im τ 3, 6 and 8.

## What it means

- **Im τ stays a counted continuous input** in main's ledger of the six's inputs.
- **A test the ρ′ peak would allow,** if a principle fixed m and named "the Higgs at its Petersson maximum" as the
  vacuum: the six at Im τ = 2.8406. But it sits outside the strip, where the six's specificity was found, and the SM
  seat's W162 already saw the class's least rise steeply below Im τ 3 (33 at 2.6–2.7). So it is registered (P-398),
  not sealed.
- **No input removed. 0 of 19.**

## Seen first

`VERDICT topic-sweep /Im tau|modulus|what fixes tau|tau selection|potential for tau|stabiliz|cusp shape|extremum|P-373|P-169/ (full text): 206 of 1537 arcs on main match (NEGATIVE 49, OPEN 14, PROVED 143)` (the draft's sweep, reproduced by the referee).
- **Bearing on it:** B1667, B1691, B1696, B1699, B1702, B1720, B1722, B1726, B1749, B1784, B1788; the register's P-169,
  P-244, P-247, P-327, P-343, P-350, P-373, P-380, P-382, P-396; the SM seat's W154 and W162.
- **Literature:** P-382's check (modular flavour near the cusp; flux vacua statistics).

## Files

- `verification/functionals.py` → `functionals.json`, `functionals_summary.json`, `functionals_run.txt`.
- `verification/referee/`:
  - `fine_eta.py` → `fine_eta_run.txt`;
  - `scan.py` → `scan_run.txt` (its scan.jsonl is regenerable);
  - `analyse.py` → `analyse_run.txt`;
  - `cbcheck.py` → `cbcheck_run.txt`.

The lock: `tests/test_b1791_im_tau_not_forced_in_the_frame.py`.
