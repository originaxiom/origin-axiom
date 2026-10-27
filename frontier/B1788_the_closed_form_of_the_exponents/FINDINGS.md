# B1788 — THE CLOSED FORM OF THE EXPONENTS (MAIN'S PLAN, STEP 1; DATA-FREE): IN B1656'S FRAME EVERY SECTOR'S SECOND-GENERATION EXPONENT IS e(m₂/m₃) = ½ − (‖2q_Lα‖ + ‖2q_Rα‖)/2, THE SAME IN BOTH READINGS (LEADING ORDER, CONDITIONAL); THE SM SEAT'S W160 VERIFIED ON MAIN AND GENERALISED; GIVEN FIVE-ALITY ALIGNMENT, "THE HIGGS AT THE UNIT TWIST" IS THE MEASURED 3 : 2 RESTATED, NOT A DERIVATION

**Verdict: PROVED at leading order in Im τ, conditional on § 5's hypotheses.** It is a derivation, each step checked
numerically on main's instrument, and the convergence checked by independent 40-digit code. No measured value is used;
one post hoc read-out is labelled in § 4. cc (main), 2026-10-27, step 1 of main's plan (docs/MAINS_PLAN.md, P-393;
P-384). Corrected before landing at its hostile referee (§ 6). **0 of 19.**

## 1. What is derived

Notation:
- twists a_x = q_Lα, a_y = q_Rα, with 6Y charges up (1, −4), down (1, 2), leptons (−3, 6);
- an exponent E means a modulus ∝ exp(−E · 2π Im τ), B1785's convention;
- ‖·‖ is the distance to the nearest integer.

1. **The four pole blocks** (`blocks.py` → `blocks.json`). B1656's bilinear has four poles at u = 0: r₀₀ (through θ₁),
   r₀₁ and r₁₀ (through den), and **r₁₁**, since θ₁ also vanishes at u + τ and |θ₁′(τ)| = |q|^(−1/2)|θ₁′(0)|.
   - **Their exponents:** E_ij = ‖a_x + i/2‖² + ‖a_y + j/2‖² − 1/8 (i, j ∈ {0, 1}). The 5 724 fitted blocks agree within
     0.0097. Another 36 are flagged rather than fitted: their theta constant vanishes exactly (§ 5).
   - **The channel map**, checked against the instrument's own residues on 360 line-sectors: R₁ = r₀₁ − r₁₀,
     R_i = −i(r₀₁ + r₁₀), R_j = −(r₀₀ + r₁₁), R_k = i(r₀₀ − r₁₁), to 1.3 × 10⁻¹⁰ relative to the largest residue.
2. **The residue matrix is rank one**, r₀₀r₁₁ = r₀₁r₁₀ (here to 5 × 10⁻¹¹). This is **B1716's** theorem, re-derived from
   θ₁′(τ) = −q^(−1/2)θ₁′(0) and den′(0)² = −q^(−1/2)θ₁′(0)².
   - **With equal channel weights √(2πL + c_s):** M would be rank one, Y = Aᵀ(εS)B rank ≤ 2 and m₁ = 0, and m₂/m₃ would
     have exponent ½ on every line (B1692's frame).
   - **So the frame's slope dependence comes from the inequality of the channel norms c_s** (B1716: det M = ¼ Σ c_s R_s²).
3. **S is line-free and exact** (B1691's q-series): S₀₀ = −S₁₁ at 1/8, S₀₁ at −1/8, S₁₀ at 3/8, det S at ¼. S̃ swaps the
   two off-diagonal entries.
4. **The singular values** (`tropical.py`, symbolic):
   - **σ₁σ₂:** the tropical minimum of Y's 2×2 minors gives e(m₂/m₃) = min(½, E(det M) − 2μ_min). Here
     det M = ¼[(c₁ − c_i)(r₀₁² + r₁₀²) + (c_j − c_k)(r₀₀² + r₁₁²) + 2r₀₀r₁₁(c_j + c_k − c₁ − c_i)], so E(det M) = E₀₀ + E₁₁
     under § 5's hypotheses (a) and (b).
   - **σ₁σ₂σ₃ = |det Y| = 4 · |det M| · |det S| · |P|** (**B1659's** law), with P linear in S and M; this gives e(m₁/m₃).
5. **THE CLOSED FORM.** Write D = ‖2a_x‖/2 and E′ = ‖2a_y‖/2. Then min E_ij = D² + E′² − 1/8 and
   E₀₀ + E₁₁ = D² + (½ − D)² + E′² + (½ − E′)² − ¼, so:

   **e(m₂/m₃) = ½ − (‖2q_Lα‖ + ‖2q_Rα‖)/2**, the same in both readings and a function of the slope alone. By sector:
   - e_up = ½ − (‖2α‖ + ‖8α‖)/2;
   - e_down = ½ − (‖2α‖ + ‖4α‖)/2;
   - e_lep = ½ − (‖6α‖ + ‖12α‖)/2.

   The tropical prediction equals this formula in all 3 972 (line, sector, reading) cases of B1785's census
   (`domain.py`). Predicted pairs (m₂/m₃, m₁/m₃), against B1785's medians:

   | slope | up S̃ | down S | leptons S | B1785's medians |
   |---|---|---|---|---|
   | 2/5 | (3/10, 4/5) | (1/5, 11/20) | (1/5, 11/20) | 0.301/0.806, 0.199/0.550, 0.549 |
   | 1/10 | (3/10, 13/20) | (1/5, 7/10) | (1/5, ½) | 0.652, 0.700, 0.498 |
6. **The torsion degeneracy.** When one chiral twist point is exact 4-torsion and the other 2-torsion, the four c_s
   coincide and M is rank one, so m₂/m₃ = ½ exactly and m₁ = 0. This is **B1716's** proved cancellation (the involution
   u → −u), and it is B1785's "tie at ¼".

## 2. Against B1785's window and at height

**In B1785's window** (Im τ 4–6, three-point fits; `domain.py`). The domain excludes the torsion degeneracy (66
line-sectors) and the 16 line-sectors where a theta constant vanishes exactly.
- **Agreement within 0.05:** m₂/m₃ 3 334 of 3 808 (87.6%); m₁/m₃ 3 676 of 3 808 (96.5%).
- **Failures:** 474 m₂/m₃ cases in 32 (slope, sector, reading) classes, most of them below the closed form.

**At height, in double precision** (`high.py`). This covered 24 of the 32 failing classes, each on its b = 0 line
only, at Im τ 10–14. Their residuals of −0.014 to −0.015 all have the same sign: a polynomial prefactor's bias. So this run
is consistent with the form but **does not confirm it by itself**. The four classes with closed value ½ fall below
double precision at those heights.

**At height, at 40 digits** (`highprec/`; mpmath at dps 40, the instrument's own quadrature, matching the instrument to
10⁻¹² at Im τ 4; the referee's independent code, `compare_closed.py` → `compare_closed_run.txt`). On seven lines,
including members of failing window classes ((0, 1/7) up, (0, 2/7) down, (1/3, 0) up, (1/7, 0) down, (2/11, 1/11) up):
- **m₂/m₃ converges to the closed form on every line.** The last local exponent at Im τ 14–16 sits 0.000 to −0.020 from
  it, approaching from below as a ln Im τ prefactor predicts; fits with a log term give 0.4997, 0.5011, 0.5033, 0.4993 on
  the ½ lines. (2/11, 1/11) reaches 0.0901 and 0.0907 against 1/11 at Im τ 28–32.
- **m₁/m₃ matches within 0.005 wherever precision allows:** (2/5, 0) up S̃ 0.8001 against 4/5; (1/3, 0) up S̃ 0.6667
  against 2/3; (1/7, 0) down 0.6051 and 0.5352 against 17/28 and 15/28. On (2/11, 1/11) the last pair falls below 40
  digits (σ₃/σ₁ ≈ e^(−107)); the height before gives 0.5693 against 25/44.

**So the window's disagreements are finite-height effects on every line tested at 40 digits.** Open: 8 of the 32
failing classes were never run at height, and each tested class was run on one line.

## 3. The SM seat's W160, verified on main and generalised (`w160_check.py` → `w160_check.json`)

- **W160's zero law:** 0 mismatches over the 662 lines (17 up, 5 down).
- **Its invariant:** I = 2ε/(1 + ε²) with ε = |r₁₁/r₀₀| is an exact identity on every line; the worst deviation is
  1.3 × 10⁻¹¹ (stored as `identity_worst_rel`, an absolute deviation).
- **ε's exponent** is |‖q_Lα‖ + ‖q_Rα‖ − ½|. For the up sector with 5α ∈ ℤ that is ½ − ‖3α‖, W160's branch.
- **Accuracy and reproduction:** within 4.2% at Im τ 3.03, 2.6% at 3.45 and 0.1% at 6. It reproduces W160's run
  (0.0063–0.0068 on the 2/5 lines, 0.2905–0.2910 on the 1/5 lines).
- **Verdict:** W160 is correct, and its law holds on every line, not only on 5w ≡ ½.

## 4. What it means for the slope (P-384; B1786's principle)

- **The exponents depend only on 2qα mod 1.** With 5α ∈ ℤ, 2qα mod 1 depends only on q mod 5, the SU(5) multiplet. So
  five-ality alignment (B1786's first condition) makes the exponents multiplet functions, which is why leptons equal down.
- **{x, ½ − x} is not a law.** For 5α ∈ ℤ, e_up = ½ − ‖3α‖ exactly, and e_down = e_lep = 1/5 at α = 1/5 and at 2/5.
  B1785's "down = ‖3α‖" holds on 2/5 and fails on 1/5.
- **The principle's second condition is a measured number restated.** Given 5α ∈ ℤ with α ≠ 0, "the Higgs at the unit
  twist" (‖3α‖ = 1/5) is equivalent to e_up/e_down = 3/2. That is the measured ratio of the up and down second-generation
  exponents; it is free of Im τ (the measured values themselves, 0.296 and 0.208, need the fitted Im τ = 3.03; B1785 § 3).
  No data-free condition here singles it out.
- **Post hoc, labelled:** (e_up, e_down) = (3/10, 1/5) occurs only at α = 2/5 and α = 1/10. This holds analytically and on
  every α with denominator ≤ 800 (`domain.py`); only the first generation separates the two.
- **The offset is untouched:** the exponents are offset-free except through the degeneracy and the excluded pairs.
- **No input removed.** The slope's effect is now understood asymptotically. At Im τ 4–6 several slopes are still far
  from their limits, so the strip's own exponents carry finite-height corrections.

## 5. Scope and hypotheses

- **Leading order in Im τ**, conditional on:
  - **(a)** the channel-norm differences c_j − c_k and c₁ − c_i decay at least at rate |E₀₀ − E₁₁|. This is a bound,
    from K_j − K_k = 2ε(K₀₀ − K₁₁)/(1 − ε²); it decays about three times faster on some lines (2/5, 1/7 and 4/9 down);
  - **(b)** c_j + c_k − c₁ − c_i ≠ 0;
  - **(c)** no cancellation among tied tropical terms.
- **The domain excludes** the line-sectors where a theta constant vanishes exactly: q·α ∈ {0, ½} with 2q·b ≡ ½ mod 1, for
  q_L or q_R, so that X₀(0) or X₁(0) is identically zero. These are 16 of B1785's line-sectors outside the degeneracy, for
  example (0, 1/8) down.
- **The prefactors c_s are computed, not derived in closed form.**
- **L is clamped at Im τ = 4**, as in B1785.

## 6. The referee (hostile, read-only; main's; before landing)

Main's referee found one blocking fault and five corrections, all applied:
- **Blocking: § 1.1's evidence was false as first written.** The first `blocks.py` omitted r₁₁ (it set R_j = −r₀₀ and
  R_k = i r₀₀, errors of order 1 there), had no committed output, and counted the line-free θ₁′ as 720 "blocks". The
  mathematics was sound: the referee's independent mpmath code reproduced the full map to 10⁻¹⁵. `blocks.py` now
  computes r₁₁ and checks the map on 360 line-sectors, and its run is committed.
- **Corrections, all applied:**
  - (a) and (b) added as hypotheses, and the vanishing-theta lines excluded;
  - § 2's counts corrected (32 failing classes and 474 cases, not 24; a double-precision residual just under a 0.015
    threshold is not convergence);
  - the 40-digit runs adopted as the convergence evidence (they show m₁/m₃ testable and matching);
  - the pair scan's citation fixed (`domain.py`; `selectivity.py` does not compute it);
  - the 3 : 2 stated scale-free;
  - B1659's det Y law cited with its sign (+4);
  - cites_seat sm:W160, and depends_on B1659, B1667, B1692;
  - the lock strengthened.
- **Noted as sound:** W160, and the closed form itself.

## Seen first

`VERDICT topic-sweep /closed form|exponent|rank one|rank-one|residue matrix|channel norm|tropical|W160/ (full text): 301 of 1535 arcs on main match (NEGATIVE 72, OPEN 8, PROVED 219, RETRACTED 2); 24 register rows match (DONE 14, QUEUED 10)`.

Bearing on it:
- **B1716:** rank one, det M, the torsion cancellation. Cited, not re-claimed.
- **B1659:** det Y. B1653 (rank at a point), B1691 and B1692 (the exponent ½ in B1653's frame), B1728, B1755, B1785.
- **The register:** P-373, P-384, P-393; the SM seat's W160 (row 1413).
- **Literature:** none beyond the record's (P-382).

## How it was made

Main drafted the arc in a forked session of its own and moved it here with repo-relative paths. Four scripts were
rerun here, with byte-identical outputs:
- `tropical.py`, `classify.py`, `selectivity.py` and `w160_check.py`, logs in `run_*.txt`.

`layers.py` and `high.py` were not rerun; their outputs are kept as made. Added after the referee:
- `blocks.py` (fixed), `blocks.json`, `domain.py` → `domain.json`;
- `highprec/`: the referee's 40-digit code, its outputs and `compare_closed.py`.

No B1786 output was read while B1788 was made.

## Files

`verification/` holds:
- `blocks.py` → `blocks.json`, `run_blocks.txt`;
- `tropical.py` → `tropical_fails.json`;
- `classify.py` → `classify_run.txt`, `classify_other.json`;
- `domain.py` → `domain.json`, `run_domain.txt`;
- `selectivity.py` → `selectivity.json`;
- `layers.py` → `layers_sample.json`; `analyse_layers.py`;
- `high.py` → `high_a.json`, `high_b.json`;
- `w160_check.py` → `w160_check.json`;
- `highprec/`: `mpframe.py`, `run_high.py` (→ `high_*.jsonl`, `h211.jsonl`), `analyse_high.py` → `analyse_high_run.txt`,
  `compare_closed.py` → `compare_closed.json`, `compare_closed_run.txt`.

The lock: `tests/test_b1788_the_closed_form_of_the_exponents.py`.
