# ZERO_FREE_HOLOMORPHIC — the rule, sealed before the script exists

chat1, 2026-10-23. **SEALED.** This file is committed and pushed before the script that reads it exists. Nothing here is
a result. 0 of 19.

## The claim under test

Three principles on record, taken together, select the Higgs and the reading in main's frame, leaving only the lepton
factor by hand:

1. **PF1-W on the Higgs** (chat1's reading of GENESIS PF1, registered by the owner as a reading; W133): the Higgs's
   joint coupling N(F) has no zero on the upper half plane. By chat1's W133 check every such Higgs is one theta power,
   F_a = η^{3−a}(εθ₂^a, εθ₄^a, iθ₃^a), a ≡ 2 (mod 4), ε = i^{(a+2)/2}, twist r ≡ 2a (mod 24).
2. **Holomorphy** (W135: every family mass must be a modular form of τ): the Higgs's components enter every coupling
   holomorphically, i.e. main's reading S (not S̃ = S of the conjugates) in every sector.
3. **Three generations with one unit** (W127's count, GENESIS FK10's unit): r ∈ {12, 20}, n = 1.

With one unit, the lines with ε = +1 in those spaces are **a = 6 (r = 12), a = −2 and a = 22 (r = 20)**. That menu is
fixed by the principles, not by the data. The ε = −1 lines need the conjugate reading, which holomorphy excludes.

## What was seen before this rule (disclosed)

- The zero-free census (`zero_free_census.py`, 16 492 points at Re τ ∈ {0.1, 0.4}, Im τ 1.0–4.0, the 266 lines) and
  its read-outs: with S for every sector and the by-hand factor 3, F_6 fits the six within 1.50 and the nine within 2.30
  (random as good 0.83% and 1.03%), F_22 within 1.59 and 2.53, F_−2 not at all (55); the e = +1 lines fit with S and not
  with S̃; the best rows lie on α = 2/5 lines; at them d = e holds to 10⁻⁵, so D = 9 with the factor 3.
- Route (b) on the zero-free lines (`zero_free_route_b.py`, `zero_free_route_b_holo.py`): a −3 on a second line of the
  same twist reaches Georgi–Jarlskog-like ratios at P-094 only where the mixing fails.
- Route (b) on B1700's untwisted directions, route (a), the sealed census and main's B1725. Main's B1726 is sealed, not
  run; its grid is avoided here.

## The model

- **Directions:** F_6, F_−2 and F_22 (the menu), each as its unit direction (εθ₂^a, εθ₄^a, iθ₃^a)/norm at τ; the scalar
  η^{3−a} drops out of every ratio.
- **The frame:** main's B1720 instrument at 3412bf09d, unchanged, through `route_b_scan.py`'s channels (as the zero-free
  census). Reading S in every sector. The lepton factor c = 3 by hand on the stored ratios (m_μ/m_τ × 3, m_e/m_τ ÷ 3),
  as the sealed census did.
- **Read-outs computed alongside, not cells:** the same directions with S̃ in every sector; c = 1; and main's ∂R with S̃
  in every sector and c = 3 (the sealed census's model) on the same points, as the reference.

## The grid (nobody has computed it)

- Re τ ∈ {0.15, 0.30, 0.45, 0.60, 0.75, 0.90}: none is a value of chat1's grids (0, ¼, ½, 0.1, 0.4) or of main's B1726
  (0.05, 0.2, 0.35, 0.55, 0.7, 0.85).
- Im τ ∈ {2.05, 2.15, …, 3.45} (15 values).
- B1713's 266 lines of order 1–12 (the sealed census's list); both horocycles.
- 23 940 points, 47 880 rows per direction and reading.

## Measure and calibration (main's)

- Targets: Huang–Zhou 2021 at M_Z and PDG 2025's three moduli, the record's pinned files at main's 3412bf09d (sha256 as
  in the sealed census). Worst factor over the six ratios ("six") and over the six plus three \|V\| ("nine").
- Random as good: main's generator; for each seed s in 1720–1739, `random.Random(s)` draws 4 000 six-targets, then
  4 000 nine-targets; the fraction of targets that the menu's rows fit at least as well (Chebyshev distance in log);
  the cell uses the mean over the 20 seeds. The menu is all rows of the three directions with S and c = 3.

## The cells, with predictions and priors

| cell | statement | prior |
| --- | --- | --- |
| Z1 | the six fit within 2.0 at the menu's best row | 70% |
| Z2 | the six are specific: random as good ≤ 1% (mean over 20 seeds) | 45% |
| Z3 | the nine fit within 2.5 at the menu's best row | 65% |
| Z4 | the nine are specific: ≤ 1% | 40% |
| Z5 | P-094: at the best six-row, D = (y_μy_d)/(y_sy_e) is within 3σ of 10.58 ± 0.11 (unfitted) | 5% |
| Z6 | at the best nine-row, \|J\| is within a factor 3 of PDG's 3.08 × 10⁻⁵ (unfitted) | 10% |
| Z7 | the reading: over the same menu, the best six and the best nine with S are both lower than with S̃ | 85% |
| Z8 | the location: the best six-row's line has α = 2/5 | 75% |
| C1 | the instrument: ∂R with S reproduces main's `TC.ratios_at` at ½ + 3.08i on (2/5, 1/10) to 10⁻⁹ in ln (the sealed census's control) | 95% |
| C2 | covariance: with F_6, τ → τ + 1 and b → b − a change no ratio or \|V\| by more than 10⁻⁹ in ln, at the first grid point | 95% |

## What the outcomes mean (fixed now)

- **Z1–Z4 and Z7 hold.** The three principles select a Higgs and a reading that do main's frame's work on unseen points,
  with only the lepton factor by hand. The reading rule I2 of the sealed census is then derived (PF1-W plus holomorphy),
  not chosen. Recorded as a positive at main's measure; it derives none of the nineteen.
- **Z1 and Z3 hold, Z2 or Z4 fails.** The selected Higgs fits, but not specifically at this menu.
- **Z1 or Z3 fails.** The selection does not reach main's frame's fits on unseen points; the census's 1.50 and 2.30 were
  local.
- **Z7 fails.** Holomorphy does not pick the reading the data want.
- **Z5 fails as expected.** The frame's d = e at the best rows leaves P-094's D for the lepton factor alone, which a pure
  3 cannot give (9 against 10.58). Recorded, not explained away.
- **Z6 fails as expected.** The CKM phase stays open (Lemma CP).
- **A control fails.** Nothing is read until it is resolved post hoc, labelled.

## Discipline

- One script, `zero_free_holomorphic_test.py`, and its comparison, `zero_free_holomorphic_compare.py`, are committed
  before the run. The run is resumable in chunks (the census's design); its outputs are committed before they are read.
- A failed launch is disclosed with its log kept. Any later check is labelled post hoc.

0 of 19.
