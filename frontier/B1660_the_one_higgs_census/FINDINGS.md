# B1660 — THE ONE-HIGGS CENSUS UNDER THE CANONICAL END CONDITION: one Higgs reproduces the data's five non-electron mass ratios on none of W59's lines, in any reading of the up sector (a scoreboard)

**Verdict: NEGATIVE, as sealed.** Every cell's pass criterion held as sealed. Two expectations stated beside the cells missed: C1's start rates were exceeded for S̃ and S̄ (the search more reliable than predicted), and S̄ came to 34.40 on two lines, not "several hundred". cc (main), 2026-10-16.
- Sealed `f798b2368` (sha256 f0f9518c) before the run. The output was committed unread at `aff4233ea`: one run of
  6 h 43 min, exit 0, the instrument unchanged since the seal (sha256 d5d4d905).
- No interruption, so no resume.
- **A scoreboard, not a blind test:** the data were seen.
- **0 of 19.**
- POINT_REGISTER P-168 and P-175, after B1659.

## 0. Seen first

As sealed: `VERDICT topic-sweep /one.higgs census|inverse map|census under P4|conjugate higgs|H~|tilde higgs|second higgs|type II/: 6 of 1431 arcs on main match (NEGATIVE 2, PROVED 4)`
— none on this question. The precedents are B1658's census, the SM seat's W88, W90 and W93, and B1659.
**Literature:** the two-Higgs-doublet ("type II") pattern and the Standard Model's H̃ for the up quarks; modular-flavour
fits near fixed points (Novichkov, Penedo, Petcov, Titov; Feruglio). For the read-out of §2: the Georgi–Jarlskog
relation between the down quarks' and the leptons' middle masses, as context, not as a claim.

## 0b. Disclosed

- In full in the preregistration's §0b and §5: main's explorations, the instrument's smoke test and its
  interrupted-and-resumed test, and one reviewing pass.
- **After the run, two post-seal explorations** (labelled, not cells). First run from the draft room, they are kept in
  `verification/after_the_seal/` with their outputs and hashed below the seal's lines (Review 64):
  - the ceiling of (m_μ/m_τ)/(m_s/m_b) over every Higgs and L on four lines;
  - a fit of the down and lepton targets alone.

  Both are reported in §2.

## 1. The sealed run (`verification/the_one_higgs_census.py`, unchanged; `.json`, `_run.txt`)

| cell | prediction | kind | result |
|---|---|---|---|
| **C0**, plumbing | the fast coupling equals B1656's, and B1659's J1 holds on the sector matter, to 10⁻¹² | gate | **HOLDS:** 2.6 × 10⁻¹⁶ |
| **C1**, the search's reliability | per reading, five planted worlds each recovered to χ² < 0.1; 15–35% of starts below 0.1 at the census-best plants | test of the instrument | **HOLDS** for all 15 plants (best 10⁻²⁶ to 1.5 × 10⁻³). The rate prediction held for the same S (31%, 18%, 16%) and was exceeded for S̃ (49%, 25%, 22.5%) and S̄ (46%, 79%, 78%). Two random data-like plants were recovered by few starts: 4 of 160 (same S, line 0) and 2 of 160 (S̄, line 9) |
| **C2**, the census | no fit below 11.07 on any of 18 lines in any of three readings; every cell reliable (> 2 starts at its best) | scoreboard | **HOLDS:** all 54 cells excluded and reliable (8 to 160 of 160 starts within 5% of the best), with no failed fit |
| **C3**, read-outs | ratios, ∣det S∣/∣∣S∣∣², L, boundary margin, residuals | read-out | §2 |

**χ²_min by class of lines** (lines named by 9 × (x, y)):

| reading | χ²_min (lines) |
|---|---|
| the same S | 85.35 (1,1), (1,7), (7,1), (2,8), (8,2), (8,8) · 87.33–87.41 (1,4), (4,1), (4,4), (5,5), (5,8), (8,5) · 291.14 (4,7), (7,4), (7,7), (2,2), (2,5), (5,2) |
| S̃ = εS̄εᵀ | 542.81 (the third class above) · 545.41 (the second) · 591.80 (the first) |
| S̄ | **34.40 (1,7), (8,2)** · 412.12 (7,4), (2,5) · 468.28 (1,1), (7,1), (2,8), (8,8) · 478.67 (4,7), (7,7), (2,2), (5,2) · 486.63 (4,1), (5,8) · 731.45 (1,4), (4,4), (5,5), (8,5) |

The explorations' values on their three lines are reproduced exactly: 85.4, 87.3 and 85.4 (same S); 592, 545 and 592
(S̃); 468, 487 and 468 (S̄).

## 2. What it shows

- **One Higgs does not reproduce the data's five non-electron ratios** in B1656's frame at ω on W59's lines under P4.
  No fit was found below the conservative bound, in any reading of the up sector, with a search shown to recover
  planted worlds in the data's regime.
- **The conjugate readings are mostly worse.** S̃ is worse on every line. S̄ is worse on 16 lines, but on the conjugate
  pair (1/9, 7/9) and (8/9, 2/9) it gives 34.40, the census's best and below the same S's 85.35. It is still excluded.
- **Where the misses are (C3).** At every class's best point:
  - the up quarks' m₁/m₃ is met (∣residual∣ ≤ 0.55σ), and in the best classes so are their m₂/m₃ and the down quarks'
    m₁/m₃;
  - the misses are the two middle ratios: m_s/m_b too large (+4.7σ to +17.5σ) and m_μ/m_τ too small (−3.5σ to −19.2σ);
  - at the census's best (S̄ on (1,7)), m_s/m_b = 0.0282 against 0.0187 and m_μ/m_τ = 0.0495 against 0.0589;
  - the data's (m_μ/m_τ)/(m_s/m_b) is 3.14, against 0.63–1.75 at the best points;
  - the Higgs is near-null (∣det S∣/∣∣S∣∣² 0.014–0.057), with L between 2.5 and 272.
- **Not a ceiling (post-seal exploration).** Over every Higgs and L, with no other target, (m_μ/m_τ)/(m_s/m_b) reaches
  17.4, 33.8, 9.0 and 17.3 on lines (1,1), (1,4), (4,7) and (1,7). The misfit is therefore a joint conflict among the
  five targets, not a bound on any one ratio.
- **P-175, the up quarks on their own Higgs (post-seal exploration):** see §2b.

## 2b. The down quarks and leptons alone (post-seal exploration, P-175)

- **The test.** Drop the up quarks, as a separate Higgs for them would, and fit the three down and lepton ratios with
  one S and L. The search is the census's, with 40 starts per line.
- **The result.** It fits exactly on every line tried: χ² from 2.8 × 10⁻²⁰ to 6.9 × 10⁻¹⁸ on (1,1), (1,4), (4,7) and
  (1,7), with L from 2.9 to 17.9.
- **What it means.**
  - The conflict in §2 comes from asking one Higgs to serve the up quarks as well. Seven effective parameters
    against three targets is underdetermined, so the exact fit carries no information.
  - A separate Higgs for the up quarks (P-175, the type II pattern) therefore makes the five ratios fittable with
    room to spare. At this level it predicts nothing.
  - **So its test must be blind,** on quantities not yet used: the mixing (CKM) and J. That is the rule the
    preregistration set for any line not excluded (§2).
- **What one Higgs's failure shows.** Of the two versions computed here, one Higgs for every sector and one without the
  up quarks, only the first could fail. It had more effective parameters (seven) than targets (five), and still its
  image misses the data's point in every cell. That is structure in the frame, not a shortage of parameters.

## 3. What it does not show

- Anything blind: the data were seen.
- The electron, which is zero on these lines (B1656).
- Other τ, other lines, other end conditions, the thread frame or the interacting weave. This is one τ, a frozen piece.
  The owner's motion reading (P-177, P-179) puts ω at a rest the motion passes through but does not stop at.
- That the 5% floor is right. It is a leading-order allowance.
- That a multistart of 160 starts found every basin. "No fit below 11.07" means none was found. C1 bounds this in the
  data's regime, and two random plants were reached by few starts.

## 4. Credit

- **The reviewing agent before the seal:** the χ²₅ framing corrected (B1), and the domain, failure handling and resume
  (B2, B3).
- **The SM seat:** W93's read-out (P-175) and W94's relation, whose quantity (m_μ/m_τ)/(m_s/m_b) is the one this census
  misses most.
- **The owner:** the binary behind the three readings (H and H̃).
