# The thread frame: integrating over the vacuum thread's closed geodesic gives a parameter-free hierarchy whose depth is the thread's height; the golden root is the least hierarchical (1 : 0.37 : 0.0096)

> **Corrected the same evening (see the last section).** An independent referee upheld every sealed cell. Five readings
> are withdrawn or narrowed: the hierarchy is carried by the normalisation K, not by Y; the location is not integrated;
> "B990's law, sharpened" conflated two meanings of "no hierarchy"; TF4 tested nothing at these lengths; and the Markov
> heights are main's (B1629, B482, B1379).
>
> **2026-10-15: the mass formula corrected** to its basis-invariant form (last section). On these 12 threads K is real,
> so the two forms give the same matrix and no number here changes.

chat1, 2026-10-14, evening. One candidate for the owner's selection-principle task, tested.
- **Sealed** at `0cf01ff11` (sha256 71aa2bcd…). **The script** `thread_frame.py` was committed at `0516039e8` before
  its one run (371 s).
- **Output** `thread_frame_run.txt` and `thread_frame.json` (`19417427e`), committed before the read-out.
- **One labelled post hoc check** (`post_hoc_convergence.*`, `6e552ed7e`): quadrature convergence and mirror pairs at
  N = 192, 384 and 768.
- **The instrument** is the SM seat's own forms (W72), built by its modules at `87cf7f551` and read through `git archive`.
- **0 of 19. No arc number claimed. Nothing to CLAIMS.md, GENESIS or the ledgers.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q0 (controls) | h's coefficients equal W72's; the integrands are invariant; the trapezoid at N = 96 and 192 agrees to 1e-9 | 95% | **FAILS as worded, on the quadrature tolerance.** h is exact (deviation 0.0). Invariance holds to 3.9e-14 over 20 points. N = 96 against 192 differs by 2.1e-6 in the raw integrals of the two highest threads. Post hoc: every mass ratio is stable to 7 digits at N = 192, 384 and 768. The residual comes from the near-singular K of LLLLR (condition number ~10¹¹) |
| TF1 | the root's rank is 3 and K is positive definite | 90% | **HOLDS.** m₁/m₃ = 0.0096; K's eigenvalues are 60, 2.5·10⁴ and 3.6·10⁵ |
| TF2 | the root is hierarchical: m₂/m₃ < 0.2 and m₁/m₂ < 0.2 | 45% | **FAILS.** m₂/m₃ = **0.369**, m₁/m₂ = 0.026 (m₁/m₃ = 0.0096) |
| TF3 | the root's lightest state is mostly F₊ | 55% | **FAILS.** Its weight on F₊ is 9·10⁻⁶. In the thread frame **F₊ is the heaviest state, in every thread** (weight ≥ 0.9996). The two light states are mixtures of F_i and F₋ |
| TF4 | mirror pairs give equal ratios to 1e-8 | 90% | **FAILS as worded, on precision.** They agree to 2.2·10⁻⁷ (7·10⁻⁷ at N = 768), all from the LLLLR/LRRRR pair's ill-conditioned K. The other four pairs agree to 10⁻¹² or better |
| TF5 | m₁/m₃ falls as the geodesic's highest point rises (Spearman < −0.5) | 60% | **HOLDS: ρ = −0.986** |

## The read-out: hierarchy is height

| thread | Vol | CS | highest point y_max | m₂/m₃ | m₁/m₃ |
|---|---|---|---|---|---|
| **LR (root)** | 2.030 | 0 | **1.118 = √5/2** | **0.369** | **9.6·10⁻³** |
| LLRR | 3.664 | 0 | 1.414 = √8/2 | 0.0357 | 5.9·10⁻³ |
| LLRLR, LRLRR | 4.752 | ∓0.43 | 1.633 | 0.0118 | 7.7·10⁻⁴ |
| LLR, LRR | 2.667 | ∓0.41 | 1.732 = √12/2 | 3.39·10⁻³ | 3.3·10⁻⁴ |
| LLLRR, LLRRR | 4.178 | ∓0.39 | 1.937 = √15/2 | 7.8·10⁻⁴ | 1.2·10⁻⁴ |
| LLLR, LRRR | 2.989 | ∓0.73 | 2.291 = √21/2 | 5.6·10⁻⁵ | 3.0·10⁻⁶ |
| LLLLR, LRRRR | 3.177 | ∓0.97 | 2.828 = √32/2 | 1.6·10⁻⁶ | 2.5·10⁻⁸ |

- **The data** (HZ2021 at M_Z): m₂/m₃ = 0.0037, 0.0187 and 0.0589; m₁/m₃ = 7.3·10⁻⁶, 9.4·10⁻⁴ and 2.8·10⁻⁴ (up, down,
  lepton).
- **The law.** log(m₂/m₃) falls by about 7.3 per unit of height between every pair of threads. log(m₁/m₃) falls by
  about 7.5.
- **The heights are Lagrange values.** Each thread's highest point is half the Lagrange (Markov) value of its continued
  fraction:
  - √5/2 for the golden root;
  - √8/2 for silver;
  - √12/2 for [2, 1];
  - √21/2 for [3, 1];
  - √32/2 for [4, 1].
- **Controls.**
  - **H-end.** W72's banked Y with K = diag(1, 2, 2) reproduces W73 exactly: 0.019375 and 3.866·10⁻⁴.
  - **The hybrid.** W72's surface Y normalised by the root's thread K gives 0.364 and 0.071. The surface frame's
    hierarchy does not survive a finite normalisation.
- **Weights (post hoc read-out, from the root-share check's volumes).** At c = 6, the weave's weight splits as follows:

  | weight | root (0.37) | threads in the observed band (3·10⁻³ < m₂/m₃ < 0.06) | steeper | length > 5, not computed |
  |---|---|---|---|---|
  | (A) | 27% | 29% | 18% | 25% |
  | (B) | 50% | 32% | 13% | 5% |
  | (C) | 66% | 21% | 8% | 5% |

## What it shows

1. **Nothing need be selected inside a vacuum.** **[MATH, given H-thread]**
   - τ, the Higgs's direction and its location are integrated over the vacuum thread's closed geodesic.
   - Every coupling and every norm is a finite cycle integral: canonical, with no free number.
   - B990's law is kept by route A: the thread breaks the modular group, and no point is singled out.
   - So the four "which?" questions reduce to one: **which thread**.
2. **Hierarchy is geometry: the depth of the thread's excursion toward the end.** **[MATH, given H-thread; 12
   threads]**
   - The light-to-heavy ratios fall like e^{−7.3·y_max}, where y_max is the highest point of the thread's closed geodesic
     on the modular surface: half its Lagrange value.
   - So a vacuum's hierarchy is fixed by how close its thread comes to the modular cusp.
3. **B990's law, sharpened.** **[READING]**
   - **The most symmetric thread is the least hierarchical.** The golden root has the smallest possible Lagrange value,
     √5 (Hurwitz), the "most irrational" axis, and gives 1 : 0.37 : 0.0096.
   - Hierarchy measures an asymmetric excursion toward the end, so symmetric points have none.
4. **The first chiral threads give the observed orders of magnitude, with no free number.**
   - LLR gives 1 : 0.0034 : 0.00033. LLRLR gives 1 : 0.012 : 0.00077, which is the down sector's pair (0.0187,
     0.00094) within a factor 1.6.
   - **Base rates.** The threads trace a one-parameter curve in the plane of the two ratios. One sector of three landing
     near it is not significant.
5. **Where it fails.**
   - **One thread gives every sector the same ratios.** Three sectors need sector structure: the weights of the matter
     modes, or P-128's R.
   - **The light pair is split too little.** The threads give m₁/m₂ between 0.016 and 0.16. Up and leptons have 0.002
     and 0.005.
   - **The root alone is not hierarchical enough** (TF2).
6. **The frames disagree on which mode is light.**
   - In the thread frame F₊ (unit at −1/8) is the heaviest; in the surface frame under H-end it is the lightest (W73).
   - So the mode ordering is a statement about the normalisation, as W72 warned.

## Fence

- **Hypothesis H-thread** (named here; not derived): the couplings in thread W are the cycle integrals of the surface
  frame's invariant integrands along W's closed geodesic.
- **Object.** W72's forms (matter at weight 3/2 in ρ_R, Higgs mode h at 5/2), B1644's coupling with R, and 12 threads.
  Reach: *members*.
- **Not tested.** Any other weight or representation; sectors; mixing; c and the thread selection; the physical
  derivation of H-thread.
- No value. **0 of 19.**

## Corrections (2026-10-14, late evening, after the independent referee)

An agent of chat1's, read-only, refereed both sealed tests and the draft report. It re-ran the construction and
confirmed the seal order, the hashes and every scored cell. Withdrawn or narrowed:

1. **"The surface frame's hierarchy does not survive a finite normalisation" (the controls) is withdrawn.**
   - W72's surface Y, normalised by *each thread's own* K, reproduces that thread's m₂/m₃ within about 10%. Examples:
     LLRR 0.0355 against 0.0357, LLR 0.0031 against 0.0034, LLLLR 1.52·10⁻⁶ against 1.55·10⁻⁶.
   - **Filed later** (labelled post hoc, `post_hoc_hybrid.*`, after the second referee noted that no script held it). On
     all 12 threads the hybrid's m₂/m₃ is ×0.90 to ×1.02 of the thread's own. **m₁/m₃ agrees only within a factor
     7.4:** the root's hybrid gives 0.071 against its own 0.0096.
   - **So the 2–3 hierarchy is carried by K, the normalisation, not by Y.** The root's K compresses it; a high thread's K
     deepens it. The first generation's ratio depends on Y as well.
   - **What the thread frame supplies is a canonical normalisation:** the modes' norms along the vacuum thread's
     geodesic. That is the post hoc choice W73 had to make by hand (H-end).
2. **"τ, the Higgs's direction and its location are integrated" is wrong on the location.** G is B1644's residue
   coupling at the puncture, B1649's premise (P-129). τ and the Higgs's direction (the unique surface mode h) are
   integrated; the location stays the puncture.
3. **"B990's law, sharpened … symmetric points have none" is withdrawn.**
   - It conflated two meanings of "no hierarchy". At the record's symmetric points the masses are rank one or
     degenerate (W67: at ω on the cone m₂/m₃ < 10⁻¹⁵). The golden thread's mild 0.37 is something else.
   - The cusp is also a symmetric point, and there the hierarchies are deepest.
   - What stands is narrower: **the root has the largest m₂/m₃ of every thread computed.**
4. **"Falls by about 7.3 per unit of height between every pair of threads" is wrong.**
   - Slopes between adjacent threads run from 5.1 to 12.6. 7.3 is the least-squares slope.
   - The law itself fails beyond length 8 (`FINDINGS_LAGRANGE_LAW.md`, corrections).
5. **TF4 tested nothing here.**
   - Every word of length ≤ 5 is reverse-symmetric, so a word and its mirror trace the same geodesic with opposite
     orientation.
   - K and Y are real for all 12 threads. **The sealed CP read-out was dropped from the script without notice**;
     disclosed now. On this construction a chiral thread gives no CP phase.
6. **"The first chiral threads give the observed orders of magnitude" explains nothing by itself.** The threads cover
   m₂/m₃ from 0.37 down to below 10⁻¹⁰, so some thread always sits at any observed order.
7. **Credit.** That a thread's highest point is half its Markov (Lagrange) value, and LR the unique lowest thread, is on
   main: B1629 ("√5/2, then √2: B482's Markov values"), B482 (T-TWOTEETH) and B1379 (golden = Hurwitz). New here are the
   link to flavour hierarchies and the cycle integrals.

## Correction (2026-10-15: the mass formula, found by step 3a's pre-seal review)

- **The formula.** The masses here are the singular values of (K^{−½})ᵀ Y K^{−½}, as sealed.
  - With K_ab = ∮⟨F_a, F_b⟩ (linear in the first slot), a change of sections F → UF sends K → UKU^H and Y → UYUᵀ.
  - The singular values of K^{−½} Y (K^{−½})ᵀ are invariant under that change. The sealed form's are not, in general.
- **When the two differ.** Write A = K^{−½}. It is Hermitian, so Aᵀ is its complex conjugate Ā, and the two forms are
  Ā Y A and A Y Ā.
  - If K is real, A is real and the two matrices are equal.
  - If Y is real, each matrix is the other's complex conjugate, so the singular values agree.
  - Only when both K and Y are complex can the masses differ. On random complex 3×3 matrices they differ at order one.
- **Nothing in this file changes.** On the 12 threads K is real to 3·10⁻¹⁸ relative, so both forms give the same
  matrix.
  - Every number here stands, including the root's lightest-state weights (TF3).
  - `post_hoc_hybrid` also stands, since it uses each thread's real K.
- **Correction 5's "K and Y are real", made precise.**
  - K is real to 3·10⁻¹⁸ on the 12.
  - |Im Y|/|Y| is at most 1.2·10⁻⁶, on LRRRR, the deepest thread. Whether that residue is quadrature error is not shown.
  - No conclusion depends on it, since K is real.
- **The labelled post hoc** `post_hoc_invariant_masses.*` recomputes every thread to length 8 in both forms. Its script
  (`d5cf9f3a9`) was committed before its one run, and its output is at `ea0647ffc`.
  - On the 51 reflection-symmetric words the two forms agree to 1.05·10⁻¹⁵.
  - The other 18 are covered in `FINDINGS_LAGRANGE_LAW.md` (same date).
- **From step 3a on** (`../chat1_2026-10-14_step3/`), chat1 uses the invariant form.
