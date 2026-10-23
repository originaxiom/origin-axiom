# The zero-free Higgs in main's frame: its a ≥ 6 lines fit about as well as ∂R, each sign class in one reading, and at their fitting rows they do not split d from e

chat1, 2026-10-23. **EXPLORATORY, labelled.** No cell, no seal and no data in the design; the read-outs compare with
the record's targets, so nothing here can earn a positive. It is the exploration that the sealed rule
`ZERO_FREE_HOLOMORPHIC_RULE.md` (38e2b8062) discloses. It was written up after that test's controls (C1, C2; C2′ post
hoc; no target) were read, and before its cells' outputs existed. The sealed rule TICK_LINE_HIGGS (e0c16e1cd) also
discloses it (F_6's best rows on (2/5, 4/5)); that test is running, and its controls were read and hold
(`relays/chat1_2026-10-23_tick_line/DISCLOSURES_BEFORE_READING.md`, item 3). Refereed read-only three times before it
left; the referee's corrections are applied, and every number the referee found in scratch runs and this note cites
was recomputed in a committed post hoc script (§1, §3, §4; `zero_free_de_mechanism.py`, `zero_free_de_checks.py`).
0 of 19.

## 1. What was done

- **The Higgs directions.** chat1's W133 check (`relays/CHAT1_TO_SM_AND_CC_2026-10-23_W133_CHECKED.md`; proof sketch,
  its §4) shows that every zero-free weight-3/2 Higgs of ρ_T ⊗ χ_η^r is a multiple of one theta power,
  F_a = η^{3−a}(εθ₂^a, εθ₄^a, iθ₃^a), with a ≡ 2 (mod 4), ε = i^{(a+2)/2} and r ≡ 2a (mod 24).
  - With one unit of end data the members are a = −10, 2, 14, 26 (r = 4); −6, 6, 18 (r = 12); and −2, 10, 22
    (r = 20). W127 counts three generations at r = 12 and 20.
  - ε = +1 for a ≡ 6 (mod 8): a = −10, 14, 6, −2, 22. ε = −1 for a ≡ 2 (mod 8): a = 2, 26, −6, 18, 10.
  - In main's frame only the direction at τ matters: (εθ₂^a, εθ₄^a, iθ₃^a), normalised. The scalar η^{3−a} drops out
    of every ratio, and a twist multiplies the coupling by a phase, which no ratio, |V| or J sees.
  - Main's ∂R is the reference. It is not zero-free (W133's P1).
- **The two classes, by hand** (the numbers checked in `zero_free_de_checks.py`, part (d)).
  - Project on the isotropic lines with the bilinear form: v₊ = v·(0, 1, i) and v₋ = v·(0, 1, −i), in the parity
    basis (i, j, k). These are the record's line components: R's line orders are (1, −1, 3) in (i, +, −), in units of
    q^{1/8}, and ∂R's are the same (B1700).
  - For F_a, v₊ = εθ₄^a − θ₃^a and v₋ = εθ₄^a + θ₃^a, while θ₃^a − θ₄^a ≈ 4a·e^{iπτ} near the cusp: to 6 × 10⁻⁵ at
    0.4 + 2.5i for all ten a, but only to 12% at 0.1 + 1.3i for a = 26.
  - So for ε = −1 (R's class) v₊ leads and v₋ is of order e^{iπτ}; for ε = +1 the reverse. The i-component, εθ₂^a,
    is about 2^a·|e^{iπaτ/4}|: small for a > 0, large for a < 0.
  - Conjugation swaps the two: (v̄)₊ = conj(v₋) and (v̄)₋ = conj(v₊). Main's second reading, S̃ = S(v̄) (proved exact
    in `relays/chat1_2026-10-23_route_b/readings_identity.py`), therefore turns one class's leading line into the
    other's.
- **The frame.** Main's B1720 instrument at 3412bf09d, unchanged, through `route_b_scan.py`'s channels.
  - Readings S and S̃ in each sector, combined four ways: S̃ for every sector; main's split (up S̃, down S, leptons S);
    S for every sector; and the flipped split (up S, down S̃, leptons S̃).
  - The lepton factor c = 1 or 3, by hand on the stored ratios (m_μ/m_τ × c, m_e/m_τ ÷ c), as the sealed census did.
- **The grid.** Re τ ∈ {0.1, 0.4}; Im τ = 1.0, 1.1, …, 4.0 (the range of main's horocycle table, B1667); the sealed
  census's 266 lines of order 1–12 (B1713's list); both horocycles, L_max (the first) and L_2 (the second). That is
  16 492 points and 32 984 rows per direction and reading.
- **The measure.** Main's: the worst factor over the six ratios ("six") and over the six plus |V_us|, |V_cb|, |V_ub|
  ("nine"), against Huang–Zhou 2021 at M_Z and PDG 2025, the record's pinned files.
  - Random as good: the fraction of random targets that the same rows fit at least as well. Main's distributions and
    seed, one draw: `random.Random(1720)` gives 4 000 six-targets, then 4 000 nine-targets. The nine-target stream
    differs from main's (`relays/chat1_2026-10-22_selection_map/THREADS_C2_AMENDMENT.md`, disclosure 1).
  - Bold in §3 marks, for ∂R and each line with a ≥ 6, the reading with the lower nine. The sealed census's bars
    (TWO_INGREDIENTS_RULE, F1–F4:
    six ≤ 2.0, nine ≤ 2.5, each with at most 1% of random targets as good) are applied separately below.

## 2. The order of events, and the controls

- `zero_free_census.py` and `zero_free_readout.py` were committed before the scan ran (d6c6021d2).
  `zero_free_route_b.py` was committed while the census ran, before its output was read (0b2dca3a8; 16 of 83 chunks
  written), with its base points fixed by rule.
- Every read-out was committed as written before it was read: the census (ab05339eb), its read-out (b10b6936f), the
  post hoc (4400b40c3 before its run, 9e92a5ca6), route (b) (dc6beae7f), route (b) in S (3fa276afa before its run,
  9a64bb286).
- The controls (no target) were read when written and committed with C1′'s output in ad21818bc. C1′'s first-run output
  was overwritten by the amended run, which reports the same 0.104.
- **C1 failed as written, on rounding.** It compared the mixing on the trivial line (0, 0), where up and down read
  alike give Y_up = Y_down, so V = 1 and the off-diagonal |V| are rounding noise (1.05 in log10).
  - C1′ (post hoc, labelled; f32559c92, amended in 119588862 after its first run) repeats it on three non-trivial
    census rows. Every |V| agrees with the sealed census to 3.1 × 10⁻¹³ in log10, J to 1.3 × 10⁻¹⁶, and every ratio
    above 10⁻¹² to 1.2 × 10⁻¹¹.
  - The amendment: the first run's 0.104 sat at four rounding-level entries (m₁/m₃ near 10⁻¹⁴–10⁻¹⁶ on an order-12
    line, both values listed in `zero_free_census_c1prime.json`), so ratios above 10⁻¹² are reported apart.
- **C2:** F_2's direction is R's, to 2 × 10⁻¹⁶. **C3:** T-covariance (τ → τ + 1, (α, β) → (α, β − α)) for F_6, F_−2
  and ∂R, at most 8 × 10⁻¹² in log10.
- **Sanity:** the read-out reproduces the sealed census's values for ∂R with S̃ in every sector, 1.513 / 2.087 at c = 3
  and 2.553 / 3.274 at c = 1.
- **Route (b)'s covariance control failed (0.59 in ln), and was diagnosed.** `zero_free_route_b.py` compared a fixed κ
  between two unit theta-vectors at τ and τ + 1. The unit vectors drop η^{a−b}, whose T-phase e^{iπ(a−b)/12} is −1
  when |a − b| = 12 or 36.
  - Only the fixed-κ control was affected. Both route (b) runs scan κ at each point (24 phases, |κ| from 10⁻⁴ to 10),
    which samples the same family as full sections.
  - `zero_free_route_b_holo.py` (post hoc, labelled; 3fa276afa) builds its control from full sections: 5 × 10⁻¹³ in ln
    for the pair (6, 18) at one point, and 1.42 across twists (6 with 2), as it should. Its scan combines unit
    directions, as the first run's does.

## 3. The read-outs (`zero_free_readout_run.txt`)

Best six / best nine at c = 3, with random as good (six, nine) for ∂R's and each a ≥ 6 line's better reading (bold):

| direction | ε | S for every sector | S̃ for every sector |
| --- | --- | --- | --- |
| ∂R (reference) | | 2.04 / 4.01 | **1.51 / 2.09** (0.90%, 0.55%) |
| F_6 (r = 12) | +1 | **1.50 / 2.30** (0.83%, 1.03%) | 1.70 / 4.24 |
| F_14 (r = 4) | +1 | **1.50 / 2.35** (0.65%, 1.20%) | 1.98 / 4.08 |
| F_22 (r = 20) | +1 | **1.59 / 2.53** (1.03%, 1.90%) | 2.09 / 3.84 |
| F_10 (r = 20) | −1 | 1.70 / 4.10 | **1.47 / 2.15** (0.35%, 0.55%) |
| F_18 (r = 12) | −1 | 2.12 / 4.03 | **1.68 / 2.42** (2.03%, 1.32%) |
| F_26 (r = 4) | −1 | 1.98 / 3.93 | **1.73 / 2.31** (2.55%, 0.95%) |
| F_−2 (r = 20) | +1 | 55 / 55 | 66 / 67 |
| F_−10 (r = 4) | +1 | 80 / 80 | 44 / 44 |
| F_−6 (r = 12) | −1 | 125 / 125 | 83 / 83 |
| F_2 (R's direction) | −1 | degenerate | degenerate |

- **For a ≥ 6, each class has one reading with nines of 2.15–2.53 and one with 3.84–4.24.** At c = 3 the ε = +1
  lines with a ≥ 6 reach nines of 2.30–2.53 with S and 3.84–4.24 with S̃. The ε = −1 lines with a ≥ 10 reach
  2.15–2.42 with S̃ and 3.93–4.10 with S. On the six the two readings overlap (1.47–2.12).
  - By the projection of §1, in every bold combination the vector the coupling sees has its leading isotropic
    component on the − line, as ∂R does in S̃.
- **Against the sealed census's four bars (one seed), only F_10 with S̃ meets all four**, as ∂R with S̃ does here. With
  S, F_6's nine is at 1.03% and F_14's at 1.20%, and F_22's nine is 2.53 (1.90%).
- **The best rows of the bold combinations lie on α = 2/5 lines at Im τ 2.3–2.8, mostly at Re τ = 0.4 in L_2.**
  - F_6: six at 0.4 + 2.4i and nine at 0.4 + 2.3i, both on (2/5, 4/5). F_14: both on (2/5, 1/10), at 0.4 + 2.6i and
    2.5i. F_10: (2/5, 3/10).
  - The exceptions are F_22's best nine (0.1 + 2.6i on (2/5, 7/10)) and F_26's (0.1 + 2.8i on (2/5, 3/10)), both in
    L_max.
  - This matches the target that THE_SELECTION_MAP §7 reads (a reading, not a sealed result) in α, Re τ and horocycle
    only. Of the zero-free best rows, just F_14's best six- and nine-rows and F_22's best six-row lie on one of its
    lines, (2/5, 1/10); the others are on (2/5, 4/5), (2/5, 3/10), (2/5, 7/10) and (2/5, 0).
- **The lines with a < 0 fail on this grid.** Their i-component dominates over most of the grid (6 to 1.6 × 10⁵ times
  the leading line component at 0.4 + 2.5i). Their best rows sit at the grid's lowest Im τ (1.0–1.3), where it is
  comparable to it (0.6–0.9 times at their best six-rows with S, all at Im τ = 1.0; `zero_free_de_checks.py` (d)).
- **F_2 is degenerate:** R·R = 0 (Jacobi), the record's untwisted first-generation zero. Its median per-row smallest
  m₁/m₃ is 1.4 × 10⁻¹⁷, against 5.9 × 10⁻⁵ for ∂R.
- **The split readings** reach sixes of 1.17–1.37 at c = 3 for every line with a ≥ 6 (the better of the two
  splits), but their nines are 21–24, as for ∂R.
- **c = 1 gives a worse six for ∂R and every line with a ≥ 6** (2.0–2.7 in their bold reading). On
  the nine it ties for F_26 with S̃ (2.31), and it is better for the ε = +1 lines with S̃ (F_22 3.01 against 3.84;
  F_14 3.81 against 4.08; F_6 4.00 against 4.24).
- **J is too small.** At the best nine-rows of the bold combinations |J| is 5.8 × 10⁻⁷ to 4.0 × 10⁻⁶, 7.7 to 53 times
  below 3.08 × 10⁻⁵.

## 4. Where d = e, and why at the fits [POST HOC, labelled]

- **d = e on every line whose order divides 4 or 5, for every direction except F_2**, as main's coincidence law states
  (B1698, B1703). `zero_free_de_lines.py` (b57f141ac before its run, 3b573703e; amended after its first run in
  f2d000035, 5e694f49a):
  - on the 16 lines of order 1, 2 and 5, exactly (|ln R2| and |ln R1| below 10⁻⁶ at every point);
  - on the six lines of order 4, up to a massless first generation (R2 exact, m₁/m₃ below 10⁻¹² in both sectors). The
    first run read them as failures through the 0/0 of the massless generation.
  - Five cases miss the 10⁻⁶ test, each on one line: (0, 1/2) for F_−10 with S and with S̃, F_−6 with S and F_−2
    with S̃; (0, 1/5) for F_6 with S̃. They fail at 29 rows in all (`zero_free_de_checks.py` (a)). R2 is exact there
    (to 6 × 10⁻¹⁶). R1 departs only at rows where m₁/m₃ is below 10⁻⁸·⁷ in both sectors: by 2.2 × 10⁻⁶ (one float32
    step of the stored log10 ratios) up to 1.55, growing as m₁/m₃ falls toward 10⁻¹⁷. That is rounding, not a split.
  - B1698's reading: 6Y mod 5 is constant on SU(5)'s 10 and 5̄, so on an order-5 line the lepton coupling is the down
    coupling transposed, minimal SU(5)'s Y_e = Y_dᵀ. 6Y mod 4 is constant on Pati–Salam's SU(4) multiplets.
- **Only F_6's best six-row lies on such a line** ((2/5, 4/5), order 5). The other best six-rows lie on order-10 lines,
  (2/5, 1/10) and (2/5, 3/10), where the law does not force d = e.
- **On those order-10 lines the down–lepton split is carried by the Higgs's i-component alone**
  (`zero_free_de_mechanism.py`, 569ecbfdb before its run, f6b64196f).
  - With v_i set to zero, D_frame − 1 (D at c = 1, minus 1) stays below 2 × 10⁻¹¹ at every sampled point of
    (2/5, 1/10), (2/5, 3/10) and (2/5, 7/10): Re τ ∈ {0.1, 0.4}, Im τ ∈ {1.5, 2.0, 2.5, 3.0, 3.5}, both readings and
    horocycles, for F_6, F_14, F_10 and ∂R.
  - With v_i as it is, the same samples split d from e by up to 0.50 (F_6), 0.041 (F_10), 7.2 × 10⁻³ (F_14) and 6.1
    (∂R). At the fitting rows D_frame − 1 is linear in v_i over the scaling tested (F_14 and F_10, from 0.01 to 100
    times v_i).
  - On the order-5 line (2/5, 4/5) it stays below 2 × 10⁻¹¹ with v_i or without, as the law says.
- **Which order-10 lines behave so** (`zero_free_de_checks.py` (c): all 36 order-10 lines of the census at 0.4 + 2.5i,
  F_14 and ∂R, both readings and horocycles).
  - On the 12 lines with 5α ∈ ℤ and 5β ≡ ½ (mod 1), that is (0, 1/10), (0, 3/10), (1/5, β) and (2/5, β) with 10β
    odd, setting v_i = 0 gives d = e to 7 × 10⁻¹².
  - On the other 24 (α ∈ {1/10, 3/10, 1/2}), |D_frame − 1| is 0.98–151 with v_i or without it.
  - This refines B1703 ("every order from 8 on splits all three") for d and e: on the 12 order-10 lines that are
    order-5 lines shifted by (0, ½), the d–e split needs the Higgs's i-component (at 0.4 + 2.5i for F_14 and ∂R, and
    at the 10 sampled τ for the three α = 2/5 lines above).
- **The zero-free lines with a ≥ 6 carry an exponentially small i-component where they fit.** At their best six-rows
  |v_i| of the unit direction is 5.5 × 10⁻⁴ (F_6), 2.1 × 10⁻⁶ (F_10), 4.4 × 10⁻⁹ (F_14), 4.9 × 10⁻¹² (F_18),
  1.6 × 10⁻¹⁴ (F_22) and 5.4 × 10⁻¹⁷ (F_26), against 0.081 for ∂R.
  - So at those rows D_frame − 1 is 2.5 × 10⁻⁵ (F_10), −7.9 × 10⁻⁸ (F_14) and below 10⁻¹¹ for the others, against
    −3.9 × 10⁻³ for ∂R. With c = 3, D = 9 to that accuracy; P-094 is 10.58 ± 0.11, which needs D_frame − 1 ≈ 0.18.
  - Near the fits it stays small (`zero_free_de_checks.py` (b): Re τ ∈ {0.1, 0.4}, Im τ 2.3–2.7, the five α = 2/5
    order-10 lines, both horocycles, each line's bold reading). The largest |D_frame − 1| there is 1.9 × 10⁻² (F_6),
    1.9 × 10⁻⁴ (F_10), 2.5 × 10⁻⁶ (F_14), and zero at the stored precision (about 10⁻⁶) for F_18, F_22 and F_26,
    against 6.6 for ∂R.
- **So at their fitting rows the a ≥ 6 lines do not split d from e** (|D_frame − 1| ≤ 2.5 × 10⁻⁵). On the order-5
  lines the law forbids a split. On the α = 2/5 order-10 lines, only v_i makes one, and at those rows v_i is
  5.5 × 10⁻⁴ (F_6) down to 5 × 10⁻¹⁷ (F_26). Away from the fits they do split: over the sampled Im τ 1.5–3.5 on the
  same lines, by up to 0.50 (F_6), 0.04 (F_10) and 7 × 10⁻³ (F_14), against at most 1.9 × 10⁻² (F_6) at Im τ 2.3–2.7.
  This holds at the points sampled; it is not a theorem over the strip.

## 5. Route (b) on the zero-free lines (`zero_free_route_b_run.txt`, `zero_free_route_b_holo_run.txt`)

- **The model.** Two directions from one twisted space (a ≡ b mod 12; 24 ordered pairs), the second with Clebsch −3
  for the leptons or 1 (the control). κ is complex and scanned at each point (24 phases, |κ| 10⁻⁴–10); there is no
  by-hand factor.
- **The base points.** `zero_free_route_b.py` (S̃ for every sector, and the split): each first line's ten best census
  points with S̃ for every sector and c = 3, by a rule fixed before the census was read.
  `zero_free_route_b_holo.py` (S for every sector; post hoc): the same rule in S, applied after the census was read.
- **With S̃ for every sector.** Clebsch −3 gives six 1.63 (D 3.58) and nine 1.92; Clebsch 1 gives 1.85 and 1.90.
  Random as good: 2.6% / 0.55% with −3, 4.3% / 0.40% with 1 (one seed, at data-chosen base points).
  - With −3, where D is within 3σ of P-094 (446 rows), the best six is 2.14 (R2 2.82, R1 3.80), and the nine at that
    row is 23.8. With Clebsch 1: 124 such rows, best six = nine = 3.10 (R2 0.95, R1 11.29).
- **With S for every sector.** Clebsch −3 gives six 1.95 (D 4.49) and nine 2.18; Clebsch 1 gives 1.91 and 1.93.
  Random as good: 9.2% / 0.90% with −3, 5.5% / 0.35% with 1.
  - With −3, 689 rows meet P-094's D, the best six is 2.04 (R2 2.56, R1 4.13), and the nine at that row is 16.7. With
    Clebsch 1: 381 such rows, best six = nine = 3.41 (R2 1.03, R1 10.46).
- **The split readings** (first run): six 1.84 with −3 and 1.86 with 1; nines 22.4.
- **What the D-matched rows show.**
  - At the best D-matched six-rows with −3 the split is Georgi–Jarlskog-like (R2 2.6–2.8, R1 3.8–4.1), and the mixing
    fails there: |V_cb| about 10.6 times its value, |V_us| 0.04–0.06 times.
  - D-matched rows with working mixing exist, but there D comes from R1 alone (R2 0.87–0.96, R1 11–12). In S: F_6 with
    F_18 at 0.4 + 2.3i on (2/5, 4/5), L_2, six = nine = 2.77, |V| 0.46, 0.85 and 1.22 times the data. In S̃: F_10 with
    F_22, six = nine = 4.02.
  - The best D-matched nine was not computed.
- In S̃ the −3 lowers the best six (1.63 against 1.85), at D = 3.6. In S it does not (1.95 against 1.91). In neither
  does it improve the nine.

## 6. What it means [READING]

- **The zero-free lines with a ≥ 6 fit about as well as ∂R** in main's frame, at main's coarse measure, on this grid.
  F_6 and F_14 with S, and F_10 with S̃, reach sixes of 1.47–1.50 against ∂R's 1.51, and nines of 2.15–2.35 against
  2.09. On specificity (one seed) only F_10 with S̃ meets all four of the sealed census's bars.
- **The reading is tied to the sign class, on the nine.** If the Higgs's components must enter holomorphically (W135,
  applied to the Higgs factor; the frame's channels are not holomorphic in τ), only the ε = +1 lines with a ≥ 6 reach
  nines near 2.5 on this grid (2.30–2.53; none meets the 1% bar on the nine at seed 1720). With three generations and
  one unit (r = 12 or 20) that leaves F_6, F_−2 and F_22, and F_−2 fails.
  This is the menu the sealed rule tests on unseen points, with its predictions written before its outputs.
- **The reading the sealed census put in by hand** (I2: main's ∂R through S̃ in every sector) **and a zero-free Higgs
  read holomorphically put the same isotropic line first on this grid,** the latter without conjugation, with fits
  about as good at main's coarse measure. That is a match of the leading line, not a derivation of I2.
- **It derives neither the Clebsch nor P-094.** At the best six-rows of the zero-free bold combinations d = e to
  3 × 10⁻⁵ (∂R's: 4 × 10⁻³, D = 8.96), so D = c², and for the a ≥ 6 lines that is structural at the fitting rows
  (§4).
  - Route (b) reaches P-094's D with a Georgi–Jarlskog-like split only at rows where the mixing fails, among the rows
    reported (the best D-matched six-row overall and for each first line); D-matched rows with working mixing get D
    from R1 alone.
  - The B − L Wilson line (BL_LINE_EXPLORATION, 25ccfdf4c) reached P-094's D only with sixes of 7.3–11.7, at three
    points (one window).
- **Nor the CKM phase:** at the best nine-rows of the bold combinations |J| is 7.7 to 53 times too small.

## 7. Scope

- Two values of Re τ, one random-target draw (seed 1720) and the census's 266 lines.
  - Random as good is per combination: the choice among 11 directions, four readings and two values of c is not
    counted.
  - The seed matters: the sealed census's six was 0.73% at seed 1720 and 1.17% ± 0.04% over 20 seeds.
  - ∂R's 0.90% / 0.55% here come from 32 984 rows, against 17 024 in the sealed census (0.73% / 0.48%).
- The fits are at main's coarse measure (a factor 1.5–2.5), with τ, the line and the horocycle chosen by the data.
- Main's frame is outside PF1-W as written (the W133 check, §5–6). This tests the lines as Higgs directions, not PF1-W.
  Where χ_η^r is absorbed (the fermions' twists or a counterterm) is not tested.
- Route (b) sampled same-twist pairs only, and the best D-matched nine was not computed.
- What the sealed test can add is whether the menu's fits survive on points nobody has computed, and how specific they
  are there.

0 of 19.
