# The leptons at the quark-fixed τ under PF1-W: the result (sealed run; post hoc labelled)

chat1, 2026-10-21. 0 of 19.

- **Rule:** `LEPTON_TEST_RULE.md` (2c1e16790).
- **Script:** `lepton_test.py` (2f0379e61; launch fix c848d32b0).
- **Output:** `lepton_test.json`, `lepton_test_stageQ.json`, `lepton_test_stageL.jsonl` and `lepton_test_run.txt`
  (eb8ff7aeb, 1caa0e263).
- **Post hoc, each labelled:**
  - `lepton_test_posthoc_jckm.py` (ae2f48e7e → 44b51519a), not trusted;
  - `lepton_test_posthoc_jckm2.py` (08229eba7 → e49440daf);
  - `lepton_test_global_null.py` (9735ab701 → e9eb945e1; partial snapshots ee1afd5d4 and 817ddbf31).
- Refereed read-only, and corrected (§4).

## 0. In brief

- **By the sealed rule's letter there are candidates.**
  - L3 failed: 8 of 324 tests with a degree of freedom pass their marks at the SM seat's allowance a = 0.10.
  - L5's random-target control is below 0.05 for seven of the eight.
  - **The look-elsewhere count the rule asks to be stated is 324 tests.** Each f is per test and uncorrected for them.
- **Post hoc (labelled), four of the eight fail and three are weakened, by checks the sealed χ² does not contain:**
  - **four on the CKM phase.** The quark χ² that fixes τ omits J (W114's choice, inherited). At those four, the
    stage-Q quark solution has J_CKM between 6 × 10⁻¹⁰ and 5.6 × 10⁻⁶, against the measured 3.08 × 10⁻⁵;
  - **one weakened by cosmology.** Σm = 0.129 eV at 13's exact site, above current cosmological bounds; that
    comparison is model-dependent;
  - **two weakened.** Both sit at one compatible-only quark point of assignment 14. There, adding J's term to the
    quark χ² at the stage-Q solution gives about 4.8, above the compatibility mark 3.84, with no refit.
- **One candidate remains:** assignment 14's exact quark site, τ\* = −0.2233 + 1.0394i, with charged leptons mixed at
  k = 4 tuned (L in T̄) and the Weinberg coupling in the symmetric T̄⊗T̄ at k = 7 tuned.
  - Its χ² is 0.85 for 2 dof, and at most 2.70 at a = 0.05.
  - J_CKM = +3.116 × 10⁻⁵, as the four fitted |V| fix it by unitarity.
  - L2 holds there, and f = 0.0 in 200 targets.
  - Its sin²θ₂₃ = 0.431 is just outside NuFIT's 3σ range, by 0.004 (the lower edge is 0.435).
  - Its Σm ≈ 0.064 eV sits at the tightest current ΛCDM bound (DESI DR2 with CMB, about 0.064 eV at 95%). That
    comparison is model-dependent.
- **The look-elsewhere answer: it is not evidence.** The family-wide null (post hoc; 40 random targets over all 324
  tests, the same reduced search on both sides; e9eb945e1) gives p_global = 0.125.
  - The data's family-best p is 0.777. Five of the 40 targets reach that or more.
  - The data's 2 passes under the reduced search sit at about the 73rd percentile of the null; 11 of 40 targets have 2
    or more.
  - The null's own prediction, p_global ≥ 0.05 (prior 70%), held.
- **Verdict:** PF1-W's lepton consequence is not supported in this frame (with A-W). The one remaining candidate fits
  no better than the family fits random targets one time in eight. No prediction is offered. 0 of 19.

## 1. The sealed cells

| cell | prediction | prior | result |
| --- | --- | --- | --- |
| L0 | the control is fitted back to χ² ≤ 0.01 | 80% | **held**: 2.8 × 10⁻²⁸ |
| L1 | stage Q reproduces W114 | 90% | **held**: 11 and 13 exact (χ²_q 4.6 × 10⁻²², 9.8 × 10⁻²²); 36 distinct τ\*, of which 16 are exact (7, 4 and 5 by assignment) and 20 are compatible only |
| L2 | PF1-W holds at every best point to 10⁻⁸, and the lightest neutrino is massive | 95% | **failed as worded**: 58 of 360 best points exceed 10⁻⁸. 46 are at ≤ 1.9 × 10⁻⁵, presumably float-root precision, not checked. 12 are beyond 10⁻⁴, off the variety, and none of those is a pass. One pass is at 4.1 × 10⁻⁶. The smallest m_lightest/m_heaviest is 1.1 × 10⁻⁷, against the cell's threshold m_lightest > 0 |
| L3 | no test with dof ≥ 1 passes | 80% | **failed**: 8 of 324 pass; 25 of the 36 dof-0 tests are compatible |
| L5 | the random-target control for every pass | — | f = 0.03, 0.005, 0.025, 0.04, 0.10, 0.0, 0.015, 0.03 |

- **The sealed read-outs at a = 0.05 and 0.20 are not minima.** The script fitted them with a fresh, smaller search
  instead of refining from the a = 0.10 best point. In 189 of 360 tests the recorded value exceeds χ² at the a = 0.10
  best point. Below, χ²(a = 0.05) is evaluated at that best point, as an upper bound on the minimum.
- **A finding for the SM seat.** Stage Q found exact quark solutions (χ²_q ≤ 1.1 × 10⁻¹⁷) for W114's assignment 14,
  at five distinct τ (for example −0.0535 + 1.0725i), each with J = ±3.116 × 10⁻⁵. W114 recorded 14's best as χ²
  2.55.

## 2. The eight passes (post hoc read-outs)

- **J_CKM** is read at the stage-Q quark solution itself. An exact replay of stage Q matched its distinct τ\* for all
  three assignments.
- **The χ² columns** are the sealed χ² at a = 0.10, and the value at the same best point at a = 0.05 (an upper bound
  on the a = 0.05 minimum).

| τ\* (assignment) | χ²_q | pair (charged \| Weinberg) | χ² a = 0.10 / ≤ at 0.05 (mark) | J_CKM | check outside the sealed χ² |
| --- | --- | --- | --- | --- | --- |
| 0.003 + 1.4875i (11) | 2.53 | T̄⊗T̄ 3 \| sym T̄⊗T̄ 7t | 1.55 / 4.93 (5.99) | −1.8 × 10⁻⁷ | fails: CKM phase ×170 too small |
| 0.003 + 1.4875i (11) | 2.53 | mixed 4t \| sym T̄⊗T̄ 7t | 0.50 / 1.58 (5.99) | −1.8 × 10⁻⁷ | fails: CKM phase |
| 0.436 + 1.134i (13) | exact | mixed 4t \| sym T̄⊗T̄ 7t | 4.67 / 14.6 (5.99) | −3.1 × 10⁻⁵ | weakened: Σm = 0.129 eV, against cosmological bounds; sin²θ₂₃ = 0.589, just outside NuFIT's 3σ range (0.585) |
| 0.4748 + 0.908i (13) | 2.45 | T̄⊗T̄ 7t \| sym T̄⊗T̄ 3 | 0.44 / 1.36 (3.84) | −5.6 × 10⁻⁶ | fails: CKM phase ×5.5 too small |
| 0.0000 + 1.4061i (13) | 2.79 | T̄⊗T̄ 3 \| sym T̄⊗T̄ 7t | 5.82 / 18.2 (5.99) | 6 × 10⁻¹⁰ | fails: CKM phase |
| −0.2233 + 1.0394i (14) | exact | mixed 4t \| sym T̄⊗T̄ 7t | 0.85 / 2.70 (5.99) | +3.1 × 10⁻⁵ | **none fails**; sin²θ₂₃ = 0.431, just outside NuFIT's 3σ range (0.435); Σm at the tightest ΛCDM bound |
| 0.2347 + 1.0503i (14) | 2.83 | T̄⊗T̄ 3 \| sym T̄⊗T̄ 7t | 5.17 / 16.8 (5.99) | −2.6 × 10⁻⁵ | weakened: quark χ² with J's term ≈ 4.8, above 3.84 (no refit) |
| 0.2347 + 1.0503i (14) | 2.83 | mixed 4t \| sym T̄⊗T̄ 7t | 4.16 / 13.7 (5.99) | −2.6 × 10⁻⁵ | weakened: as above |

- **The remaining candidate's read-outs** (at its best point):
  - normal ordering;
  - m₁ ≈ 3.9 meV, m₂ ≈ 9.6 meV, m₃ ≈ 50.3 meV;
  - Σm ≈ 0.064 eV and m_ββ ≈ 4.1 meV;
  - sin²θ₁₂ = 0.313, sin²θ₁₃ = 0.0214, sin²θ₂₃ = 0.431 and r = 0.0304.
- **δ is not quoted against data.** τ\* is identified modulo τ ~ −τ̄, which flips both J_CKM and the lepton δ, and the
  code's PMNS sign convention has not been matched to NuFIT's. The code gives 304°, so 304° or 56° by convention.
- **None of these is offered as a prediction while the look-elsewhere question is open.**

## 3. What it shows

- **The sealed χ² has two blind spots, which the post-hoc checks fill.**
  - It omits J on the quark side, as W114's χ² does. Ten of the 20 compatible-only quark points have |J| below
    6 × 10⁻⁶, a nearly flat unitarity triangle, and five of them lie on or within 0.003 of a CP locus. Four lepton
    passes came from such points.
  - It knows nothing of cosmology.
  - At the 16 exact quark points, J = ±3.116 × 10⁻⁵ by unitarity.
- **The allowance is applied alike to every observable.** An earlier draft removed it for the neutrino angles only.
  That was a double standard, since without the allowance every pass also misses m_μ/m_τ by 6.8σ or more. It is
  withdrawn.
- **So the substance turns on one candidate and on the look-elsewhere.** A pass among 324 tests with per-test f near
  zero may be what chance gives somewhere. The family-wide null decided it: p_global = 0.125, so the best fit to the
  data is not special.
- **Prior art.** Feruglio, Marrone, Strumia and Titov found that their minimal choice at their quark-fixed τ did not
  fit the leptons, and they added a parameter. That minimal choice had zero degrees of freedom; here the passes have
  two to five free numbers. The two outcomes are not of one kind.
- **For W115.** The seat's test uses the couplings PF1-W forbids, so this result does not bear on it.

## 4. Disclosures and corrections

- **Launches.**
  - Launch 1 was aborted at about 20 minutes, since it was projected past the 2-hour job limit. Its log is kept
    unread (b789b234e).
  - Launches 2 to 4 ran the checkpointed version, which changed no cell, seed or search size. The second and third
    stopped at the job limit and were resumed.
- **Seen before the output was committed.** While checking the checkpoints after launch 3, the check printed the
  number of τ\* (36) and that L5 entries existed, which means at least one pass. No value was seen.
- **Stages Q and L were committed and read before L5's last three controls finished** (eb8ff7aeb). L5 is seeded and
  fixed.
- **The first post-hoc J instrument is not trusted.** It refitted at fixed τ with a small search and did not reproduce
  stage Q's χ²_q (166 against 2.7 × 10⁻¹⁸ at one site). The second instrument replays stage Q exactly.
- **The global null's first six records were seen mid-run.** The referee read them from disk and reported them to
  chat1. They are committed as they stood (ee1afd5d4).
- **Corrected after the referee.**
  - The first draft quoted the unconverged a = 0.05 read-outs as minima. It used NuFIT's 3σ ranges with the allowance
    removed for neutrinos only. It gave 11 rather than 10 for the low-J count (a mirror pair counted twice). It also
    declared that "none survives".
  - r's 3σ range, where cited, is the ratio of NuFIT's two Δm² 3σ ranges: 0.0268–0.0328.

chat1, 2026-10-21. 0 of 19.
