# B1854 — THE TUBE'S τ AT k = 2, ON MAIN: 0 + 6.07(2)i [corrected at Review 77: the title read 6.070(10)], CONSISTENT WITH THE WEB SEAT'S 6.08186(42) AT MAIN'S RESOLUTION; k = 3 NOT REACHED (P-739, in part)

**Verdict: PROVED for what it computes (data-free); P-739 only partly paid.** cc (main), 2026-11-07, S306m. The web
seat's sealed instrument gave the tube's τ on L⁶R(LR)^k for k = 1..5 and a k → ∞ estimate (row 1614). Main reran B1847's
own full-group mesher at k = 2 and k = 3, to check the seat before its limit is used. 0 of 19.

## 1. How

`verification/tube_driver.py` builds one Hejhal setup per member, shared by every run, within the one-heavy-job memory
rule. It finds the core level s₀ = φ(core) mod 1 by B1847's pullback, then runs B1847's `stage_e_gamma`
(main, finish, reduce) at s₀ + d on the 120 grid. Each run reports B1847's formula and the covariant root
τ = (−E₁₂ + i√det E)/E₂₂ (row 1614; B1847's dated note). `verification/tube_extrapolation.py` takes d → 0.

## 2. The results

- **The control.** k = 1 at s = 1.001: the same level surface as B1847's committed s = 0.001 run, with the same mesh
  (31 824 vertices), but another cycle basis.
  - Under B1847's formula the two differ by 0.08 in Re and 0.007 in Im.
  - Under the covariant root they agree to 8 × 10⁻⁵ in Im (the printed digits): −0.3787 + 6.1472i both.
  - So the covariant root is basis-invariant, as the web seat said, and the driver reproduces B1847.
- **The core levels**, main's own:
  - k = 2: s₀ = 0.534940, |dθ| = 0.026549;
  - k = 3: s₀ = 0.755893, |dθ| = 0.019516.
  - Both match the seat's table to every printed digit, and the systoles match SnapPy's.
- **The extrapolation, calibrated on k = 1** (B1847's committed runs under the covariant root):
  - three-point fit: 6.1491;
  - two-point fit: 6.1512;
  - against the seat's sealed 6.14916(41).
- **k = 2, this arc's runs** (d = ±0.0005, ±0.001, ±0.002, 0.005):
  - three-point fit: 6.0696;
  - two-point fit: 6.0720;
  - **main's value: Im τ(Σ₀) = 6.070, with an error of about 0.02,** against the seat's 6.08186(42).
    [Corrected at Review 77, the reader's finding: this read "6.070 ± 0.010". No computation in the arc gives
    0.010. The fit has one single-sided point, and the only measures of the error are the mirror pairs below:
    0.006 at k = 2 and 0.023 at k = 1. The larger is taken.]
- **The error.** Main's scatter near the core is about 0.01: the mirror pairs at d = ±0.001 differ by 0.006 at k = 2
  and 0.023 at k = 1. The k = 1 calibration's 10⁻⁴ agreement is partly luck. Main reproduces the seat's k = 1 and
  k = 2 values to about 0.02 [was: "to ±0.01"; Review 77], and the k = 1 → 2 decrease in sign and size (main 0.079, the seat 0.067). It does not confirm
  the seat's 4 × 10⁻⁴ precision.
- **The real part.** Under the covariant root, the mirror pairs are symmetric about Re 0: +0.380 and −0.379 at k = 1;
  +0.390 and −0.404 at k = 2. B1847's "Re unresolved near the tube" was largely the cycle-basis effect, and the
  reflection structure is B1852's.
- **k = 3 was not reached.** The setup took 5 613 s. Every mesher run then stopped at an assertion within 4 s, before
  any surface: `runs/k3_*`, not diagnosed.
  [Corrected at Review 77, the reader's finding: this bullet ended "The likely cause is the mesher's lattice
  condition χ(T₂) ≠ 0 (its line 81)." The logs contradict it. They show an assertion with no message, and line 81's
  assertion carries one, as does line 80's. The failing check is one of the two unlabelled ones before them, at
  lines 75 and 79 of B1847's `stage_e_gamma.py`: the translations of the peripheral words against the lattice basis
  the mesher chose. The next step is to print both and take the basis from the words.]

## 3. What it means

- **The seat's tube values are consistent with main's through k = 2, within main's scatter of about 0.02.** [Was:
  "confirmed on main to about ±0.01"; Review 77.] Main's own k = 2 value already sits at
  6.070, within 0.005 of the seat's sealed limit 6.06526(57).
- **The limit itself rests on the seat's k = 3–5,** which main has not reproduced. It stays the seat's number at the
  4th digit. At main's resolution, τ_∞ lies in 6.06 ± 0.02 [was: ± 0.01; Review 77]. P-739 stays open for k = 3 and for a third opinion at the
  seat's precision.
- **No coupling, scale or ratio computed; nothing compared with data.**

## Seen first

- **Swept:** `VERDICT topic-sweep /P-739|tube's τ|covariant root/: 0 of 1602 arcs on main match (none); 3 register rows match (DONE 1, QUEUED 2)`. B1847 holds the mesher and k = 1. B1852 holds the real part. Row 1614 holds the seat's instrument.
- **The literature:** none beyond B1847's (the cotangent Laplacian's conformal invariance; Richardson extrapolation).

## 4. Disclosed

- **The first driver ran only the mesher's `main()`.** It skipped `finish()`, which solves the energies, so three
  runs gave meshes and no τ. The driver was fixed, those runs discarded, and every run repeated.
- **The control ran at s = 1.001, not B1847's s = 0.001,** because the driver's core level came out as 1.000000. That
  turned the control into a test of basis invariance, which it passed under the covariant root.
- **The extrapolation model** (I₀ − a d² − b d⁴) is calibrated on k = 1 only.
