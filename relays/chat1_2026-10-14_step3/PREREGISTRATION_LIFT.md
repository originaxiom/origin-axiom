# LIFT: does main's boundary-class lift (B1654) survive in the thread frame's rank-two cells, and how large is it? (chat1, 2026-10-15.) Sealed before the script is committed

**Why.**
- **The owner said "goforit"** (08:51) to step 1c of chat1's route (`../chat1_2026-10-15_route/THE_ROUTE_FROM_HERE.md`).
- **Main's B1654** (PROVED) lifts B1649's zero at a fixed τ, on one fibre.
  - Under the canonical end condition P4, the residue triplet of B1644's coupling becomes u_r = √(2πL + c_r(τ))·R_r,
    with L = log(1/ε) and c_r the finite part of the channel-r boundary class's norm.
  - Under C0's P4′ (equal framed data), u = R and the zero stays.
- **The open question.** The thread frame's rank-two cells have R, or E4·R, among their matter modes, so the τ-integral
  alone cannot lift their zero (S1; B1653's dated note). Whether B1654's u lifts it along a thread, and by how much, has
  not been computed.

**The added premise, P5 (named here, not derived): P4 holds fibre by fibre.**
- Along a thread the canonical normalisation is imposed at each τ, so u(τ) = √(2πL + c̃_r(τ))·R_r(τ) pointwise.
- A global per-channel normalisation of the Higgs along the thread would weight the channels differently. It is not
  computed here.
- Every conclusion below is conditional on P5.

**The construction** (`lift_cells.py`, committed after this seal and before its one run).
- **The coupling.** B1644's G(X, Y; v) = (v·Y)X + (v·X)Y − (X·Y)v, evaluated pointwise along each thread's closed
  geodesic. Contracted with h̄, this is B1654's Y(a; u) with a = h̄(τ).
  - The integrands, weights, cycle integrals, completions, admission and mass formula K_L^{−½} Y (K_R^{−½})ᵀ are those
    of `theta2_completion.py`.
  - The pointwise route replaces the q-series route for G.
- **The basis.** W72's R is −2π times B1654's (R_i, R_j, R_k), with i, j, k ↔ θ₂, θ₄, θ₃ (plumbing, at five τ). So the
  channel weights act componentwise.
- **The channel norms.**
  - c_r comes from the route-A prefix of main's own instrument, read from main at `1d2dac43d` and executed unchanged.
  - c̃_r = c_r − π·log Im τ puts the cutoff in the unit-area coordinate. Then S and T only permute the channels.
  - c̃ is tabulated on a 20 × 32 Chebyshev grid over x ∈ [−½, ½], y ∈ [0.86, 4.5].
  - **A closed form, found by the pre-seal reviewer:** c_r(τ) = −4π·log|θ_r(0|τ)| − 2π·ln(π/2).
    - So c̃_r = −2π·log(√(Im τ)·|θ_r(0|τ)|²) − 2π·ln(π/2). Its covariance is exact by the theta transformation laws.
    - B1654's D = −4π·Σ_r R_r²·log|θ_r(0|τ)|, with the constant dropping because R·R = 0.
    - It is used here only as a second route for c̃, in Q(a′). It is evaluated by mpmath's `jtheta`, independently of
      main's thetas.
- **The expansion.** u/√(2πL) = R + ε·δ + O(ε²), with δ = c̃∘R and ε = 1/(4πL).
  - For a rank-two cell, the first-order lift is κ = |u₀ᴴ (A Y_δ Bᵀ) v₀| / σ_max(A Y_R Bᵀ), where u₀ and v₀ are the
    cell's null pair. Then m₁/m₃ → ε·κ wherever 4πL·m₂/m₃ ≫ |Δc̃|.
  - Each null pair is fixed by an exact pointwise zero of G(·, ·; R): the R row in C3, and the E4·R column in C2/E4.
    So any common shift k(τ)·R added to δ leaves κ unchanged, even when k varies along the thread. κ is therefore the
    same for c and c̃. The convention affects only the exact-L values and the rank-three read-outs.
  - δ·R = Σ c̃_r R_r² is 4π² times B1654's D(τ), so D enters every δ-integrand.
  - Exact P4 couplings are computed at L = 10, 100, 1000 and 10⁷.
  - P4″ (unnormalised amplitudes) gives the same first-order direction with ε doubled. It is not computed separately.
- **The cells and completions.**
  - C1 = (3/2, 3/2) with h at 5/2;
  - C2 = (3/2, 7/2) with h at 9/2, under E4·F, ϑ² and H-ORTH;
  - C3 = (−½, 7/2) with h at 5/2, under the same three.
  - The rank-two cells are C2/E4, C3/E4, C3/ϑ² and C3/H-ORTH. κ is computed for these only.
- **The threads:** every Lyndon word of length 2–8, at N = 256 and 384.
- **Admission:** y_max ≤ 3, and N = 256 against N = 384 to 10⁻⁵ on m₂/m₃ and on κ (in the rank-two cells, whatever
  the rank flag says) or on m₁/m₃ (in the others).

**Controls (Q)**, holding if all hold:
- (a) the interpolated c̃ matches main's code at 20 random points of the fundamental domain, to 10⁻⁸ absolute;
- (a′) at the same points, the grid and main's route A each match the closed form, to 10⁻⁸ absolute;
- (b) every integrand is invariant under 20 random moves. The integrands are K, and Y for v = R, δ, δ + R, δ + c̃²∘R
  and the four exact L.
  - Each entry's deviation is measured relative to its family's largest entry at that point, and must be below 10⁻⁸.
  - c̃ is computed directly at both points.
  - Every v here is covariant. c̃²∘R is covariant because the squares permute with the channels.
  - A fixed channel shift such as δ + e₃∘R is not covariant, because T moves channel θ₃. So it is not used, either here
    or in (f).
- (c) the unlifted cells reproduce `weights_cells.json` (C1) and `theta2_completion.json` (C2, C3) on admitted threads.
  - Each ratio must agree to 10⁻⁵ relative or 10⁻¹⁰ absolute (in units of m₃), whichever is looser.
  - A cell that is not positive definite here, but was admitted there, fails (c).
- (d) β = (−224, −4, −112), compared in mpmath, to 10⁻²⁰;
- (e) the pointwise G matches the series G for four non-degenerate pairs at five points, to 10⁻¹² of |X||Y||R|. The
  zero pair G(R, E4·F_i; R) is reported, not counted.
- **(f), reported at the root and not counted:**
  - a common shift (δ → δ + R) leaves κ unchanged, which is an identity;
  - a covariant channel shift (δ → δ + c̃²∘R) changes it, which shows κ is sensitive to the channels.

| | prediction | prior |
|---|---|---|
| Q | the controls hold | 85% |
| L1 | an instrument check: under P4′ (u = R) each rank-two cell has m₁/m₃ < 10⁻¹⁰ on every admitted thread. It is an identity, G(R, ·; R) = (R·R)(·) = 0, so only numerics can fail it. The largest P4′ m₁/m₃ is reported | 97% |
| **L2** | under P4 and P5 the lift survives: κ > 10⁻⁶ on every admitted thread in all four rank-two cells | 88% |
| L3 | the expansion holds: at L = 10⁷, 4πL·m₁/m₃ agrees with κ to 1% on every admitted thread in all four rank-two cells. Two read-outs: the same comparison at L = 1000, where the second order can dominate on threads with small m₂/m₃; and the margin, the largest P4′ m₁/m₃ divided by ε·κ at L = 10⁷ | 85% |
| L4 | at the root, κ lies in [0.01, 10] in all four rank-two cells. The anchor: B1654's L·m₁/m₃ ≈ 0.11–0.17 at i and t1 corresponds to κ ≈ 1.4–2.1 on one fibre | 55% |

**Read-outs (no prior):**
- κ per thread and cell, its range, and Spearman(y_max, ln κ);
- the root's κ and its exact-L values;
- the root's ratios of κ between cells, which do not depend on L;
- the rank-three cells' m₁/m₃ at the root at L = 10 and 100;
- for the record only: the L at which the root would reach each sector's m₁/m₂ (HZ2021 at M_Z). That is not a value
  contact. The root cannot host all three sectors' 2–3 ratios (the route's read-out 1b). The first-order form needs
  4πL·m₂/m₃ ≫ |Δc̃|. L, the end condition and the cell assignment are free.

**What a result means, fenced.**
- **If L2 holds,** then under P4 and P5 B1654's lift carries into the thread frame. To first order, where
  4πL·m₂/m₃ ≫ |Δc̃|, a rank-two cell's first generation gets m₁ = ε·κ·m₃, with κ independent of L. The rank-two zero
  then belongs to P4′, not to integration.
- **If L2 fails,** the lift cancels on some threads: by a symmetry, by numerics, or because the transcription is wrong.
  That is to be found.
- **Not tested:**
  - which end condition is physical (the parent's clauses 4 and 6);
  - P5 against a global normalisation;
  - L;
  - sectors (main's twisted channels);
  - CP;
  - the (7/2, 7/2) cell;
  - any value.
- **0 of 19.**

**Disclosed: seen before the seal.** Every script named here is filed in
`../chat1_2026-10-15_audit/auditors/lift_review/`, with sandbox paths scrubbed.

**chat1's plumbing:**
- c_r at τ = i and 0.13 + 1.07i, at −1/τ and at τ + 1;
- W72's R against B1654's at five τ;
- a 14 × 22 interpolation test of c̃ alone (8.8·10⁻⁹);
- route A against the closed form by mpmath's `jtheta` at four τ (≤ 8.7·10⁻¹³).

**chat1's glue run of the first draft**, on the threads LR and LLR, with c̃ replaced by fake, non-covariant numbers.
- It computed real values of:
  - Q(b) for the K and R families;
  - Q(c) on LR and LLR;
  - Q(d) and Q(e);
  - the P4′ masses on LR and LLR.
- Q failed in it: Q(e) through a degenerate pair, and Q(b) through the R family's normalisation. Both are fixed here.
- It printed lift coefficients computed with the fake c̃, on LR and LLR in all seven cells (the rank-three cells
  included, where κ was later removed). They range from 4.9·10⁻⁴ to 418. They are not κ, and L4's prior was set before
  they were seen.

**The pre-seal review, read-only, in two passes.**
- **The first pass found:**
  - three controls failing by construction: Q(e), Q(b), and Q(c)'s threshold;
  - L3 failing at L = 1000 on threads with small m₂/m₃;
  - the unstated premise P5;
  - L1 as an identity that could mask its own failures;
  - the false sentence "D is not computed";
  - the saving order;
  - κ at rank three;
  - Q(d)'s precision;
  - wording.
- **The second pass found:**
  - that the then-control δ + e₃∘R is not covariant, so Q(b) would have failed by design. It is replaced by δ + c̃²∘R;
  - the closed form above;
  - Q(f)'s division by the root's κ before a save;
  - L3's margin at L = 10⁷, now reported. The reviewer said that in random-matrix draws at m₂/m₃ = 8·10⁻⁵ the second
    order exceeds 1% in 0.3–1.3% of draws. That figure is as the reviewer reported it; no filed script reproduces it;
  - wording, including this ledger's account of the fake coefficients.
- **Its own runs:**
  - main's route A at 18 skewed τ pairs (covariance to 6.7·10⁻¹¹) and at nine τ against the closed form;
  - random matrices;
  - **glue3:** chat1's glue procedure on the second draft, with chat1's non-covariant fake c̃, on LR and LLR. Its
    controls read Q(e) 1.9·10⁻¹⁵, Q(e′) 2.3·10⁻¹⁶, Q(b) for the K and R families ≤ 1.2·10⁻¹⁴, Q(c) 9.1·10⁻⁸ and
    Q(d) 1.7·10⁻³⁹. Its lift coefficients are the fake ones above.
  - **An incident, glue2:** the reviewer started a glue copy with a covariant fake, −log(√y·|θ_r(0)|²). It then found
    that 2π times that fake, minus 2π·ln(π/2), is exactly the real c̃, so the run's κ would have been the real κ
    divided by 2π. It killed the run at "modules loaded", before the forms were built. The run wrote nothing beyond its
    log header and computed no κ, and the reviewer deleted the script.
- All findings of both passes are taken above.

**After the second pass, chat1:**
- added Q(a′);
- guarded Q(c) and the read-outs against cells that are not positive definite;
- moved Q(f) after the cells' save, and guarded it;
- ran the post-processing on synthetic random rows (no forms, no c̃, no κ) to exercise the admitted branches and the
  guards.

**A third read-only pass** read the diff and this text, and found no blocker. Its own checks, all on c̃ alone:
- the closed form against route A at six τ (≤ 9.1·10⁻¹³);
- a 20 × 32 grid built from the closed form, tested at 203 points (6.1·10⁻¹¹);
- the permutation of c̃ and of B1654's R under S and T (the same swaps, to 4·10⁻¹⁶);
- the smoke test.

It also asked for:
- the code-level conditions listed below to be stated;
- this ledger's figures to be traceable. The outputs of `cov.py`, `closed_form_c.py` and `plumb4.py` are now filed
  beside them. Each was re-run on c̃ alone and reproduces the quoted figures.

**Code-level conditions,** stated so that the text matches the script:
- L1, L2 and L3 hold only if each rank-two cell has at least one admitted thread.
- L3 skips a thread whose κ is exactly 0. Such a thread already fails L2.
- L4 needs LR to be admitted in each rank-two cell.
- Admission also needs K_L and K_R to be positive definite at both N.
- Q(d) is relative.
- Q(c) compares only m₂/m₃ where the earlier run flagged rank two.

**Also seen:** main's B1654 values at its sealed τ, as its FINDINGS print them.

**No real κ** has been computed on any thread.

chat1, 2026-10-15.
