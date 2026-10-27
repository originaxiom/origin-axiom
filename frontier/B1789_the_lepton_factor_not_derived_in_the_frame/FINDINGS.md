# B1789 — THE LEPTON FACTOR c = 3 IS NOT DERIVED IN B1656'S FRAME (MAIN'S PLAN, STEP 2; DATA-FREE): ON THE SIX'S SLOPE FAMILY THE FRAME'S LEPTONS EQUAL ITS DOWN QUARKS IN THE SECOND GENERATION AT LEADING ORDER (R₂ → 1), SO THAT 3 IS AN INPUT; A NET FIBRE FLUX IS EXCLUDED; LOCAL HYPERCHARGE CURVATURE WITH ZERO NET DEGREE IS NOT EXCLUDED AND IS THE ROUTE LEFT

**Verdict: NEGATIVE for "c is forced by the frame as built"** — data-free; one post hoc read-out labelled in § 3. cc
(main), 2026-10-28, step 2 of main's plan (docs/MAINS_PLAN.md, P-393; P-294). Corrected before landing at its hostile
referee (§ 5). **0 of 19.**

## 1. What c is, and what the record already holds

**In the instrument** (B1726/B1741 compare.py, `errs`): c = 3 multiplies the frame's lepton m₂/m₃ by 3 and divides its
m₁/m₃ by 3. In the double ratios:
- R₂ = (m₂/m₃)_e/(m₂/m₃)_d and R₁ = (m₁/m₃)_d/(m₁/m₃)_e;
- c multiplies each by 3, and D = R₂R₁ by 9;
- the data's D is 10.58 ± 0.11 (P-094).

**Closed on record** (P-294's row and what it names):
- **The horocycle:** a per-sector horocycle moves the leptons the wrong way (S201).
- **The line order:** the leptons' coarser line on 3 ∣ N orders gives no factor (B1729).
- **Pati–Salam:** the split is not structural (audit/verify_lepton_factor).
- **The web seat's routes:**
  - its Clebsch −3 on a second direction worsens the fits, though its split reading reaches (R₂, R₁) = (2.28, 3.26);
  - its B − L line only perturbs;
  - its GJ_WALL test failed G2 (4 rows reached D 9.16 and Z 1.05, with weak hierarchies).
- **E₆:** E₆'s 27 vevs give D ≡ 1 (B1738).
- **A 45 or 351′:** neither is in the representation content at tree level (P-294's sweep). The 24 has a vev
  proportional to Y, which is § 2 (d)'s route, not an independent closure.

**Identities on record:**
- B1728: d = e whenever the charges agree mod the line's order up to swap and sign.
- B1742 and P-355: on (2/5, k/10) the lepton spectrum is the down spectrum, for any Higgs at even k and for a Higgs with
  no QI component at odd k.

## 2. The candidates

**(a) The frame's own charge dependence: NEGATIVE for R₂.**
- In B1656's frame hypercharge enters only through the flat twists (qα, 2qb), that is, periodically (B1653's Szegő
  profile on the fibre's zero modes).
- Computed (§ 3): on the slope-2/5 family R₂ → 1 at leading order, prefactors included. **The second-generation 3 is
  therefore an input.**
- R₁ also tends to 1, but slowly. At the band's height it ranges widely, because the record's Higgs (DR) has a QI
  component (about 7% of the largest at Im τ 3, 6 × 10⁻⁴ at Im τ 6) that breaks B1742's odd-k identity.

**(b) A net hypercharge flux on the fibre: EXCLUDED.**
- The premise: one zero mode per field and generation block (B1653: the fibre's zero modes and the Szegő profile).
- A flux n along 6Y gives |1 + q n| zero modes, and |1 + q n| = 1 for q = 1 and q = 2 forces n = 0.
- This holds for any net flux, integer or fractional, that is compatible with the charges.
- A flux on another internal factor does not enter the fibre-local coupling.

**(c) A 45-type Clebsch:** closed on record (§ 1).

**(d) An insertion that sees the integer charge — NOT EXAMINED, and the route left.** Two forms:
- **Local hypercharge curvature with zero net degree.** It keeps every zero-mode count but changes the channel norms c_s,
  which set D through det M = ¼ Σ c_s R_s² (B1716), with weights that are integer in the charges. This is the local
  analogue of arXiv:1211.6529's flux mechanism; P-397.
- **A 24-type vev ∝ Y**, or a hypercharge insertion on the doublet leg (a moment-map or D-term vertex).

The frame as built has neither. Each would bring an input unless a principle fixes it.

## 3. Computed (`verification/`)

1. **`frame_ratios.py`** → `frame_ratios.json`: the frame's own R₂, R₁, D (readings S and S, both horocycles, no c) on
   B1786's census (orders 25 and 30) and B1755's (orders 13–20).
   - On the slope-2/5 lines the per-line median R₂ is 0.92–1.04 and the per-line median R₁ is 0.67–1.42.
   - Mirror pairs (b ↔ 3/5 − b) give equal values.
2. **`r_twofifths.py`:** on six slope-2/5 lines (orders 10–30), R₂ and R₁ → 1 as Im τ grows.
   - Im τ 3: R₂ 0.97–1.02, R₁ 0.76–1.23.
   - Im τ 6: R₂ 1.000.
   - Im τ 8: R₂ 1.0000, R₁ within 0.0005 of 1.
   - In the reading S̃, R₁ converges slowly (0.45 at Im τ 3, 0.87 at 6, 0.96 at 8; the referee's recompute).
3. **`d_frame_band.py`** → `d_frame_band.json` (added after the referee): the band's spread, slope-2/5 rows.
   - **R₂ stays near 1:** 0.81–1.16 over B1786's 7 500 rows.
   - **R₁ does not:** 0.36–2.95 (161 rows above 2), from the QI breaking of the identity.
   - **D_frame:** quantiles 0.75 / 0.99 / 1.47 at 10/50/90%, so **9·D_frame spans about 6.7–13.2**. B1755's rows agree.
   - **So exact c = 3 does not imply D = 9 at the band** (the first draft's error, § 5). Examples:
     - B1741's best row gives D = 11.05 on (2/5, 9/10);
     - B1749's gives 10.94;
     - B1786's best row gives 8.46 (R₂ 0.9987, R₁ 0.9413, recomputed exactly).
   - **Post hoc, labelled** (one look at one measured number, P-094): 2.4% of the slope-2/5 rows put 9·D_frame inside
     10.58 ± 0.11 (the referee's count).
4. **`r2_tenth.py`:** on slope 1/10 the frame's R₂ passes near 3 at the band's height (3.53 and 3.69 at Im τ 2.9) and
   tends to 4 higher up (3.98 at Im τ 8), while R₁ → 0.
   - This is a coincidence of height on a slope whose first generation fails (B1786: χ²_six ≥ 919 in the seat's menu,
     41.4 in the covariant menu), so it is not a source.
   - But a leading factor of 4 from purely periodic twists shows that twists can make lepton/down factors at other
     slopes.

## 4. What it means

- **c is not derived.** On the six's slope family the second-generation lepton/down ratio is 1 at leading order, so the
  3 is put in by hand.
- **Exact c = 3 is not excluded at the band.** The frame's own first-generation spread carries 9·D_frame across the
  measured 10.58. Whether a principled c = 3 together with the band's R₁ meets P-094 is open (P-355's owed item).
- **The route left:** an insertion that sees the integer hypercharge, either local curvature of zero net degree acting on
  the channel norms, or a 24-type vev. It is **main's design task** (P-397):
  - which leg (charge −3 or +3);
  - which channel block;
  - the predicted (R₂, R₁, D) including D_frame, stated before any comparison.

  It is not a question for the SM seat: its Higgs enters every sector alike, as main's does.
- **No input removed.** c stays one discrete input in this frame, not derived.

## 5. The referee (hostile, read-only, before landing; `audit/referee_s226_lepton/`, its recompute in `verification/referee/`)

1. **BLOCKING, applied: the first draft's claim was wrong.** It said "exact c = 3 gives D = 9 on this family, which
   P-094/P-355 exclude".
   - P-355 covers (2/5, k/10) only, and at odd k only for a Higgs with no QI component.
   - The record's DR has a QI component, and its own c = 3 best rows give D = 11.05, 10.94 and 8.46.
2. **CORRECTION, applied:** "the whole Georgi–Jarlskog factor is c's" holds for R₂ only. R₁ at the band ranges 0.36–2.95.
3. **CORRECTION, applied: the flux argument.**
   - The premise is one zero mode per field (B1653), not "degree-0 bundles".
   - Zero-net-degree hypercharge curvature is not excluded.
   - The draft's pointer "B1656 § 0" was wrong.
4. **CORRECTION, applied: citations.**
   - B1738 does not mention the 248.
   - GJ_WALL had been omitted.
   - Route (b)'s (2.28, 3.26) had been omitted.
   - The 1/10's 919 is the seat's menu only.
   - P-329 is queued before P-294.
5. **CORRECTION, applied:** the next step is main's own design task, not a question to the SM seat.
6. **NOTE:** slope 1/10's R₂ → 4 is confirmed.

## Seen first

`VERDICT topic-sweep /lepton factor|Georgi|Jarlskog|Clebsch|c = 3|factor 3|flux|hypercharge flux|P-294/ (full text): 82 of 1535 arcs on main match (NEGATIVE 24, PROVED 58); 29 register rows match (DONE 15, QUEUED 14)`.
- **Bearing on it:** B1653, B1716, B1726, B1728, B1729, B1738, B1741, B1742, B1749, B1786, B1788; the register's
  P-094, P-294, P-295, P-304, P-329, P-355; the web seat's GJ_WALL and BL_LINE_EXPLORATION.
- **Literature:** Georgi–Jarlskog (1979); magnetized-torus hypercharge flux (arXiv:1211.6529); the double-ratio target
  (Antusch, Hinze and Saad, arXiv:2510.01312v2, P-094).

## Files

`verification/`:
- `frame_ratios.py` → `frame_ratios.json`, `frame_ratios_run.txt`;
- `r_twofifths.py` → `r_twofifths.json`, `r_twofifths_run.txt`;
- `r2_tenth.py` → `r2_tenth.json`, `r2_tenth_run.txt`;
- `d_frame_band.py` → `d_frame_band.json`, `d_frame_band_run.txt`;
- `referee/`: the referee's independent recompute.

B1786's raw census is restored with `gunzip -k`. The lock: `tests/test_b1789_the_lepton_factor_not_derived_in_the_frame.py`.
