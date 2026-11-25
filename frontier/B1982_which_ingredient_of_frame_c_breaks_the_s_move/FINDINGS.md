# B1982 — Frame C is SL(2, ℤ)-covariant at order 30 with its own end law: nothing breaks the S move; B1980's failure was main's end-law error; the norm is needed for the covariance, the a₀ term is not

**Verdict: PROVED (the corrected run: S to 6e-16 at three height pairs; T exact in B1980).** Main, 2026-11-25. Data-free.
Register rows P-882 (restated) and P-845. **0 of 19.**

## The answer first

- **The question was which ingredient of frame C breaks the S move** (P-882 Q1, after B1980). The answer is none.
- **With its canonical end transformed by the record's own law,** frame C at order 30 is exactly S-covariant. The law is
  L(−1/τ) = L(τ) + log|τ| (B1667's law, tested in B1724, derived in B1921, whose invariant is
  L̃ = L + ½ log Im τ − (γ + log π)).
  - The test matched B1976's 96 points against all 899 nonzero points of E[30] at 1.25 against 0.8, 1.5 against 2/3, and
    2.5 against 0.4.
  - The largest distances were 5.6e-16, 5.9e-16 and 4.4e-16.
  - **T is exact (B1980's C1).** So frame C is SL(2, ℤ)-covariant, as B1724 found for B1656's frame.
- **B1980's "frame C fails S, so it reads the curve through one cusp" was main's error.** The first run read the end's
  table outside its domain. The correction read L(τ_FD) with no log shift. Neither used the record's law.
  - The sweep for this page found B1921 and B1724 before this arc landed.
  - B1980 carries a dated correction, and the claim is entered in the retractions.
- **The instrument is whole.** At the author's word (2026-11-25), what reads through one hole is the record's read-out,
  not the frame: one cusp, one height, one point, one level (P-882, restated).

## Seen first

- **B1980:** S failed with the end read outside its table, and again with the end read at τ_FD with no shift.
- **B1921:** the end's shift under S is the channel norm's τ-term; L̃ is invariant; the frame's S-covariance is derived
  for the channel weights' norm.
- **B1724:** S and S̃ are SL(2, ℤ)-covariant in B1656's frame, with the end passed as L + log|τ|, to 1.5e-9.
- **B1927:** the canonical end is covariant, and its invariant form is a modular function.
- **The construction read:** `determinant_law.parts`.
- **Swept:** `VERDICT topic-sweep /S-covarian|S move|covariant under S|tau -> -1/tau|modular covarian|channel phase|kappa phase/: 23 of 1723 arcs on main match (NEGATIVE 5, OPEN 2, PROVED 16); 27 register rows match (DECLINED 1, DONE 15, QUEUED 11)`.
  - B1921 and B1724 among the matches were read in full, and they decided this arc.
  - B1822, P-525 and P-594 (the T-norm, the generations' kinetic metric) were noted and not needed: the covariance holds
    without the T-norm.
  - The rest concern older frames or other senses of the words.
- **The literature:** θ[α, β](−1/τ) = (−iτ)^{1/2} e^{2πiαβ} θ[β, −α](τ), the standard law.

## Custody

- **The card** (`CARD.md`) and `ablate.py` were hashed before their run.
- **The correction card** (`CORRECTION_CARD.md`) and `s_endlaw.py` were hashed before theirs.
- **`fricke_endlaw.py`** was written after `s_endlaw_run.txt` was read, and hashed before its run (labelled).
- There was no separate seal commit.

## The sealed run, as run (`verification/ablate.py`, `ablate_run.txt`), under main's wrong end law

The largest distances, at 1.5 against 2/3 and at 2.5 against 0.4:
- **V0,** frame C: 0.18 and 0.32 (E0 held);
- **V1,** without the norm: 0.090 and 0.15;
- **V2,** without the norm and κ's phase: 0.68 and 1.9;
- **V3,** without a₀: 0.19 and 0.35;
- **V4,** without κ's phase: 0.63 and 1.6;
- **V5,** V2 with the Higgs held at (1, 1, 1): 0.94 and 2.3;
- **V6,** the Higgs held at (1, 1, 1): 0.39 and 0.31.

No variant passed (E1 to E6 failed). The variants keeping the norm (V0, V3, V4, V6) used the wrong end law at the
partner heights, so their failure is that error.

## The corrected run (`verification/s_endlaw.py`, `s_endlaw_run.txt`), with the record's end law

| variant | 1.25 / 0.8 | 1.5 / (2/3) | 2.5 / 0.4 |
|---|---|---|---|
| V0, frame C (L1) | **5.6e-16** | **5.9e-16** | **4.4e-16** |
| V3, without the a₀ term | 5.6e-16 | 6.0e-16 | 5.6e-16 |
| V1, without the norm (L2) | 0.077 | 0.090 | 0.15 |

- **L1 holds:** frame C is S-covariant.
- **L2 holds.** The norm is needed for the covariance: the theta residues' S-law is completed by the norm's. This is
  B1921's derivation seen from the other side.
- **The a₀ term plays no part.**
- **The duality family τ ↦ −K/τ, K ≠ 1,** rerun with the end evaluated covariantly at every τ
  (`fricke_endlaw.py`, `fricke_endlaw_run.txt`): none passes (K in 2, 3, 5, 6, 10, 15, 30, 60, 900; largest distances 0.59 to 0.96, nearest K = 900 at 0.59). The end law itself checks: L(0.4i) − L(2.5i) = log 2.5 to 12 digits. **Frame C has no duality τ ↦ −K/τ beyond SL(2, ℤ) in this family.**.

## What the wall teaches

- **The wall was main's, not the frame's.** A symmetry test failed because one input, the end, was not transformed by
  its own law on record (B1921). The record's top-ranked debt, P-864, had already named the table's edge. A sweep and a
  register read before computing would have prevented both errors.
- **For the read-out:** the frame is whole. What has been one-hole is choosing one thread's act, one point, one level
  and one height (P-882, restated; P-883).

## What it means

- **The record already had a whole instrument.** Frame C is a modular-covariant object, read so far at one cusp, one
  height and one point at a time.
- **B1980 part A's fact can now be read through the covariance.**
  - The 96 points are the cusps of X(30) the act fixes, and the frame is covariant. So reading B1976's 96 points at i∞
    should be the same as reading one point at those cusps.
  - On that reading, the 12 classes are the frame's cusp expansions at the act's cusps, and B1978's orbits are the act
    moving between them.
  - This is a consequence to be checked directly, not yet a result: it is P-882's next computation.
- **P-882 is restated:** read the order-30 structure over the whole curve. P-845's class and the height become one
  question there: where the object sits.
- **Nothing here is compared with data.**
