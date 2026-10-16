# B1663 — THE PULL-BACK'S STRENGTH: it sets which end and how fast, not the shape of the motion that survives

**Verdict: NEGATIVE, as sealed.** The central prediction, T4(b) ("the pull-back's strength is not idle"), failed;
every other cell held. **The finding is the failure's content:** the motion's averaged defect is the same for every
pull-back strength. cc (main), 2026-10-16.
- Sealed `9c3f74238` (sha256 1ce96661) before the run. The output was committed unread at `4d9eb2001`: one run of
  187 s, exit 0, the instrument unchanged since the seal (sha256 ce1cf289).
- **0 of 19.** POINT_REGISTER P-183, step 3 of `speculations/S_THE_PUSH_BACK.md` §10.1, after B1662.

> *Sharpened 2026-10-17 (S142, after an outside referee's report on the paper). The escape rate of T3 is the instrument's (1/n) log‖X_n‖_F at the first n at which an entry passes 10⁶⁰ (or n = 40 000). This is a first-passage estimate of the top Lyapunov exponent, half the hyperbolic drift of d(i, X_n i), and it runs high at the per-cent level. A fixed-length estimate (`papers/P9_what_a_grammar_fixes/checks/lyapunov_fixed.py`, 60 walks of 40 000 steps) gives 0.3964 ± 0.0001 at p = 0 and 0.0987 ± 0.0002 at p = ½, against 0.3959 and 0.1007 here. T3's cell (a difference of more than 10 SE between p = 0 and ½) is unaffected. No verdict changes.*

## 0. Seen first

As sealed: `VERDICT topic-sweep /pull.back.s strength|random walk|harmonic measure|escape rate|exit law|Guivarc|Furstenberg|Kesten/: 3 of 1434 arcs on main match`
— B1083, B186 and B451, none on this question. **Literature:** Kesten (1959); Furstenberg (1963); Guivarc'h and Le Jan
(1990, 1993, with its 1996 erratum), for the singularity of the exit law in the modular and Γ(2) case, and Gadre, Maher
and Tiozzo (2015) for nonuniform lattices (the preregistration's "Guivarc'h–Le Jan for a non-cocompact lattice" was
wider than their papers; corrected at banking by the paper's attribution check); Series (1985); the Minkowski
question-mark measure.

## 0b. Disclosed

- In full in the preregistration's §0b and §5: the ray instrument's design (a truncation bias found and removed),
  the p = 0 value seen (0.517), a smoke test, and one reviewing pass (no blockers, ten points taken).
- **After the run:** one labelled exploration, `verification/after_the_seal/digit_law.py` with its output (§2).

## 1. The sealed run (`verification/the_pull_backs_strength.py`, unchanged; `.json`, `_run.txt`)

| cell | prediction | result |
|---|---|---|
| **T0**, plumbing | f mirror-, T- and S-invariant; the Lebesgue control recovers 0.31500491 within 3 SE | **HOLDS:** mirror 0, T and S 1.0 × 10⁻¹³; control 0.3155 ± 0.0018 |
| **T1**, the character | each step multiplies χ by i with probability ½ at every p (exact); the count | **HOLDS:** 0.4997–0.5017, every p within 4 SE |
| **T2**, the side | P(ξ > 0) is 1 at p = 0, ½ at p = ½, non-increasing | **HOLDS:** 1.000, 0.900, 0.753, 0.713, 0.622, 0.531 ± 0.028 |
| **T3**, the escape rate | differs between p = 0 and ½ by more than 10 SE | **HOLDS:** 0.3959 ± 0.0004 at p = 0; 0.1007 ± 0.0005 at p = ½ |
| **T4**, the motion's averaged defect | (a) at p = 0 not the typical 0.315; **(b) different between p = 0 and ½ by more than 5 SE;** (c) at p = ½ not the typical 0.315; failures at most 10% | **(a) HOLDS** (0.5157 ± 0.0012); **(b) FAILS:** 0.5157 against 0.5178 ± 0.0013, and the spread over all six p is 0.0028; **(c) HOLDS** (0.5178); no failures. T4 as a whole fails |

E_p⟨f⟩ at p = 0, 0.1, …, 0.5: 0.5157, 0.5179, 0.5185, 0.5162, 0.5173, 0.5178, each ± 0.0013.

## 2. What it shows

- **The pull-back's strength p sets two things and not a third.**
  - It sets **which end** the motion reaches: P(ξ > 0) falls from 1 to ½.
  - It sets **how fast**: the escape rate falls from 0.396 to 0.101 per step.
  - It does **not** set the motion's averaged defect, which is 0.517 at every p to within about 0.003.
  - The push-back adds no number to the sizes. Within this test's resolution (5 SE ≈ 0.009), the sizes are idle in
    p.
- **Why, by a post-seal exploration (labelled).**
  - The limit's continued-fraction digits follow the geometric law 2⁻ᵏ at p = 0 and at p = ½ alike: frequencies of
    1, 2, 3, 4 and ≥ 5 are 0.502, 0.248, 0.123, 0.064, 0.064 and 0.504, 0.253, 0.121, 0.060, 0.062 (24 000 digits
    each). The Gauss–Kuzmin law of a typical point is 0.415, 0.170, 0.093, 0.059, 0.263.
  - **The motion that survives the cancellations is the forward-only motion, letter by letter, whatever the
    pull-back's strength.** Cancelling changes only the sign and the clock.
  - That is a reading of 2 × 24 000 digits, not a proof.
- **The motion's averaged defect is a definite number:** 0.517, with no parameter. It is the forward motion's (the
  uniform word measure's), not the typical motion's 0.315. A number without a dictionary.
- **For the push-back picture** (`S_THE_PUSH_BACK.md` §10): the opposing force fixes when and which side, and leaves
  the shape of what exists to the step alone. Main's prediction that its strength would matter was wrong.

## 3. What it does not show

- Any value of the Standard Model.
- That the walk is the physical motion. This is the picture's reading, firewalled.
- Other generator sets or weights within a pair. The statement is for L, R and their inverses, with equal weights
  within each pair.
- A difference smaller than about 0.009. A mild p-dependence of that size is not excluded.

## 4. Credit

The reviewing agent before the seal: the power statement, the failure accounting in T4, T4(c) as a contrast, and
DROP 20.
