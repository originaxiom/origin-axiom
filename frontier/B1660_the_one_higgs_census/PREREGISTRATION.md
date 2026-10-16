# B1660 — THE ONE-HIGGS CENSUS UNDER THE CANONICAL END CONDITION: with B1659's joint law, can one Higgs reproduce the data's five non-electron mass ratios on any of W59's lines? (a scoreboard): preregistration

cc (main), 2026-10-16. POINT_REGISTER P-168 and P-175, after B1659.
- **The setting.** B1656's twisted frame at τ = ω on W59's 18 lines, given Λ, the dictionary and B1654's premises with
  B1656's four channels. Under the canonical end condition P4 each sector's matter carries its own defect
  (u_s = √(2πL + c_s)R_s, det M_s ∝ D_s). With B1659 the masses are closed-form in the Higgs's defect, the matter's and
  their pairing.
- **The question.** Can **one** Higgs S ∈ M₂(ℂ) (scale-free) and the end radius L reproduce the five non-electron mass
  ratios of HZ2021 at M_Z? Those are the up quarks' m₂/m₃ and m₁/m₃, the down quarks' m₂/m₃ and m₁/m₃, and the
  leptons' m₂/m₃.
- **Three readings of the up sector** (the owner's binary of 2026-10-15, H and H̃): the same S; S̃ = εS̄εᵀ; S̄.
- **The electron** is massless on these lines for every S and L (B1656) and is not a target.
- **The data were seen.** Main's explorations computed these fits on three lines (§0b), so this is **a scoreboard, not
  a blind test**. Its value is a census over all 18 lines and three readings with a search shown reliable in the data's
  own hierarchy regime.

0 of 19.

## 0. Seen first

`VERDICT topic-sweep /one.higgs census|inverse map|census under P4|conjugate higgs|H~|tilde higgs|second higgs|type II/: 6 of 1431 arcs on main match (NEGATIVE 2, PROVED 4)`
— none on this question; the six use the words in other senses (B178, B721, B850, B1188, B1199, B1219). The precedents
on record are:
- B1658's census (one Higgs under equal framed data: a factor 15.9 needed, against a bound of 4);
- the SM seat's W88 (verified on main), W90 (verified on main) and W93 (B1658 on its own code), and its read-out that
  a separate up-quark Higgs puts down/leptons inside B1658's bound (P-175);
- B1659, the joint law, whose closed form this census evaluates.

**Literature:** the two-Higgs-doublet ("type II") pattern and the Standard Model's use of H̃ for the up quarks (context:
the reason for the three readings); modular-flavour fits near fixed points (Novichkov, Penedo, Petcov, Titov; Feruglio)
as the class of comparison this is.

## 0b. Disclosed

- **Main's explorations of 2026-10-15/16**, kept beside the seal (`verification/before_the_seal/`). The same frame, P4,
  W59's lines, the same five targets and the 5% floor:
  - Early optimisers disagreed: Nelder–Mead 86–89, trust region 131–154 and differential evolution 88–596 on one line.
  - A reliable protocol was then built: trust region plus Nelder–Mead polish per start, half the starts near-null,
    in parallel; planted worlds recovered. It gave, on lines (1/9, 1/9), (4/9, 1/9) and (7/9, 1/9), with 120 starts:

    | the up quarks see | best χ² |
    |---|---|
    | the same S | 85.4, 87.3, 85.4 |
    | S̃ | 592, 545, 592 |
    | S̄ | 468, 487, 468 |

    Planted worlds at those points were recovered to between 10⁻¹⁴ and 2.4 × 10⁻³.
  - A smoke test of this instrument (3 starts, 2 lines) gave 91 and 596 (same), 704 and 901 (S̃), 468 and 886 (S̄). On
    line (2/9, 2/9) an earlier trust-region run had found 296 < 596, so per-line reliability with few starts is not
    assured. C1 tests it.
  - The reviewing agent's reduced runs found the landscape multi-basin. On line 9 (same) 6 of 48 starts reached 291.1
    and the rest 596.4. With the right metric (starts below χ² 0.1), the recovery rates of census-best plants were 40 of
    120 (line 0) and 7 of 48 (line 9). The explorations' "1 of 120" counted starts within 5% of a tiny best value, an
    artefact of that metric.
  - The explorations caught failed fits and returned them as missing. The first draft of this instrument raised
    instead, which the review caught (§5).
- **A related negative, not part of this arc:** a Higgs confined to the two isotropic vacua, S₀ + βS̄₀, fits no line
  (χ² ≥ 689; `speculations/S_THE_PUSH_BACK.md` §6).
- **The owner's reading behind the variants** (P-177): binaries both happen; H and H̃.
- **Reviewing agents before the seal:** §5.

## 1. The setting

- **The coupling.** Y(S, M) is B1656's `coupling`, evaluated as KM·(vec S ⊗ vec M), which C0 checks equal to B1656's
  function. The sector matter is M_s(L) = Σ_r √(2πL + c_r)·R_r·E_r, with B1656's residues R, channel norms c and dual
  basis E, on each line and sector.
- **The fit.** For each line and reading, minimise
  χ² = Σ_targets [(ln m_k/m₃ − ln data)/σ]² over S (8 real parameters; the ratios are scale-free) and log L, with
  σ = max(the data's relative error, 0.05).
  - The 5% floor reflects that the frame is leading order.
  - The data's errors: m_u, m_d and m_s carry 5–17%, the rest less.
- **The search.** NST = 160 starts per line and reading. Half are near-null (S = uvᵀ + 0.05X, where the hierarchy
  lives) and half generic, with log₁₀ L uniform in [0.4, 3]. Each start runs a trust-region least squares (600
  evaluations), polished by Nelder–Mead (6000 iterations). Eight parallel workers, deterministic seeds.
- **The statistic and the exclusion (corrected by the review, §5).** χ²_min is the squared distance, in σ units, from
  the five log-ratio targets to the model's image, minimised over S and L.
  - S has 8 reals, 6 effective, since a complex scale cancels in ratios.
  - No degrees of freedom are subtracted (7 effective parameters against 5 targets), and **χ²_min is not
    χ²₅-distributed.**
  - If the frame were true with Gaussian log-errors at the stated σ, χ²_min would be at most the χ² at the true point,
    which is distributed as χ²₅. So P(χ²_min > 11.07 ∣ frame true) ≤ 5%: a conservative one-sided bound, made more
    conservative by the floor. The charm and lepton targets sit at the floor (their own errors are 2.8% and 0.02%).
    Gaussian-in-log is rough for m_u's 17%.
  - **A multistart search gives only an upper bound on χ²_min.** "No fit below 11.07" therefore means none was found in
    160 starts.
  - **A cell counts as excluded** only if its best value is also reached by more than 2 starts (within 5%). Otherwise it
    is flagged unreliable, not excluded: for a basin with hit rate r, the miss probability is (1 − r)¹⁶⁰.
  - No p-value is claimed.
- **The domain.** Fits are restricted to 2πL + c_s > 0.5 for every channel, so the radicands stay real. The minimum c_s
  is about −3.58, which cuts L off below about 0.5. The start values have log₁₀ L in [0.4, 3], and the fit itself is
  unbounded above. C3 records each best point's margin from the boundary.
- **Robustness.** Failed fits are caught and counted per cell, and a cell with more than 5% failures stops the run. If
  the run is interrupted (the owner restarts often), a rerun resumes from the JSON, keeping completed cells. The resume
  is logged and will be disclosed in the findings. Eight workers (half of 16 cores, the owner's rule for a shared
  machine), single-threaded BLAS, deterministic and distinct seeds.

## 2. The cells (the instrument `verification/the_one_higgs_census.py`; one run; JSON after every line)

| cell | prediction | kind |
|---|---|---|
| **C0**, plumbing | the fast coupling equals B1656's, and B1659's J1 holds on the sector matter, both to 10⁻¹² (two lines, three sectors). The run stops if it fails | gate |
| **C1**, the search's reliability in the data's regime | per reading, five planted worlds are each recovered by the same search to χ² < 0.1. Three sit at the census's own best point on lines 0, 9 and 12 (two classes, and line 9 the known multi-basin line). Two are random data-like worlds (near-null S, up m₁/m₃ < 10⁻⁴) on lines 0 and 9. **Predicted to hold for all 15 plants**, with 15–35% of starts below 0.1 at the census-best plants (the review's reduced runs). C1 holds per reading | a test of the instrument |
| **C2**, the census | for each of the 18 lines and each reading, χ²_min over 160 starts, with the count of starts within 5% of it and the failures. **Predicted: no fit below 11.07 on any line in any reading, every cell reliable (more than 2 starts at its best), so every cell excluded.** Expected from the explorations: the same S from 85 to about 600 across lines, and S̃ and S̄ at several hundred | scoreboard |
| **C3**, read-outs | the best point's ratios, ∣det S∣/∣∣S∣∣², L, the boundary margin, the residual pattern, and the largest single-target miss of the same S's best line | read-out, no test |

**If C1 fails for a reading,** C2's exclusion for that reading is reported as unsupported: the search may have missed a
fit. It is not reported as a refutation. An unreliable cell (2 or fewer starts at its best) is reported as such. **If C2 finds a line not excluded,** that line's fit is a scoreboard entry and
must be sealed blind on unseen quantities (the CKM, J) before any use.

## 3. What it would mean

- **If C1 and C2 hold.** In B1656's frame at ω on W59's lines under P4, no fit of one Higgs to the data's five
  non-electron ratios below the bound was found, in any of the three readings of the up sector, with a search shown to
  recover planted worlds in the data's regime.
  - The largest single-target miss at the best fit is a C3 read-out. This statistic is not compared with B1658's
    15.9, which is a required defect-sum ratio under a bound.
  - A reading for the record, not a cell: the up sector already sees the Higgs's twist with the opposite sign
    (ū = −3w against +3w), so H̃ may be built in through the line. That would be why conjugating S again does worse.
- **What is left:** another τ, other lines, the thread frame with the per-field units (the seats' sealed comparison), a
  term between threads (P-166), or a second Higgs (P-175).

## 4. What it does not show

- Anything blind: the data were seen.
- The electron, which is zero here.
- Other τ, other lines, other end conditions, the thread frame or the interacting weave.
- That the 5% floor is right. With a 10% floor the best χ² on line 0 (the same S) is 42.3, checked by the reviewing
  agent for that line only. That is a reading, not a cell.

## 5. Reviewing agents before the seal, and files

- **One read-only reviewing pass** (its scripts kept in `verification/before_the_seal/review1/`).
  - **B1:** the χ²₅ framing was wrong. Taken: the conservative one-sided bound, with "no fit below 11.07 found".
  - **B2:** the domain and the start ranges were undisclosed. Taken.
  - **B3:** a single failed fit would have killed the run, unlike the explorations. Taken: failures caught and counted,
    a per-cell cap, resume from the JSON.
  - **S1:** C1's seeds collided with C2's. Taken: distinct bases.
  - **S2:** C1's plant lines included two equivalent lines. Taken: lines 0, 9 and 12, plus two random data-like plants
    per reading, C1 per reading, and the reliability flag in C2.
  - **S3:** the comparison with B1658 dropped.
  - **S4:** the 10% floor remark scoped.
  - **S5:** the expected range widened.
  - **S6:** this section and the files filled.
  - **One note not taken:** the review read 8 workers as over the owner's limit; 8 of 16 cores is the owner's 50/50
    rule.
- **Main's checks after the review:** a smoke test of the revised instrument (3 starts, 2 lines) ran end to end, and an
  interrupted run resumed from its JSON with the completed cells kept.
- **Files:**
  - `verification/the_one_higgs_census.py`, with `.json` and `_run.txt` after the run;
  - `verification/before_the_seal/` (the explorations of §0b and the reviewers' scripts).
