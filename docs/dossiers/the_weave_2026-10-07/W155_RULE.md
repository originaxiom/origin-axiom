# W155 — the census over contents, Stage B: the Higgs direction at the forced line. No copy has a zero mode; masses never change a cusp's coefficient; masses that treat the parities alike keep Stage A's one curve; a condensate selects the copy that becomes massless at a cusp and pushes τ toward it, holding neither Im τ nor Re τ (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's word:** "lets do themall" (2026-10-24), after W154 (Stage A) and its relay §270, which left Stage B,
  the Higgs direction, as the census's second stage. The effective action's ledger names the joint variables
  (τ, w, h) with h ∈ ℂ³ and leaves the fork open: (A) a covariant form, (B) a vev minimized with τ
  (`docs/dossiers/the_weave_2026-10-07/THE_EFFECTIVE_ACTION_LEDGER_2026-10-24.md`, row "the Higgs direction"). Stage
  B is fork (B) in Stage A's frame.
- **What Stage A left.** At the forced line every content that treats the three parities alike has
  V = −(A E(τ, 3) + B E(τ, 2)) at one loop. It runs to the cusp (A > 0), sits at ω or i, or holds τ on the imaginary
  axis at y*(t), t = B/|A|. Every content on record and E₈'s 248 run to the cusp. Re τ is barely held even in the band.
  The question for Stage B, as relay §270 left it: can the Higgs direction break that one-curve structure, hold τ for
  a content that runs, or lower the band's price?
- **What the hand work found while writing this rule.**
  - At the forced line the Higgs's three copies sit on the three parity characteristics (W154), so none has a zero
    mode. A constant vev h ∈ ℂ³ is not available. The copies' lowest modes are twisted, with mass² proportional to
    q_c(τ) = min over (a, b) ∈ ℤ² + c of |aτ − b|²/y.
  - A constant bulk mass enters each lattice term through f(x) = x³K₃(x)/8 = 1 − x²/8 + O(x⁴ log x), with
    x = μ|m + nτ|/√y. At a cusp the shrinking cycle's windings dominate, and their physical length goes to 0, so
    masses drop out of the leading y³ term.
  - The parity characters sum to 4·[m, n even] − 1 term by term, so for any s, Σ_c S_c(τ, s) = (2^{2−2s} − 1) E(τ, s):
    −15/16 at s = 3 (W154) and −3/4 at s = 2.
  - On the standard domain the lightest copy is c = (0, ½), with q = 1/(4y), which does not depend on Re τ.

## The objects (W154's frame and units)

- **The basis sums,** for a characteristic c = (p₁, p₂) and a bulk mass μ (in units of the inverse square root of the
  fibre's area): S_c^{(μ)}(τ) = Σ′ cos 2π(m p₁ + n p₂) · y³/|m + nτ|⁶ · f(μ|m + nτ|/√y), with f(x) = x³K₃(x)/8, so
  f(0) = 1 and S_c^{(0)} is main's `S_c`. The massless sums at s = 2, S_c(τ, 2) = Σ′ cos 2π(m p₁ + n p₂) y²/|m + nτ|⁴,
  are used for the small-mass expansion; S_{(0,0)}(τ, s) is E(τ, s).
- **A content** is Stage A's (w₀, w_p, w_ρ), so A and B are as in W154. A **mass pattern** gives a mass μ_c to the
  fields on characteristic c ∈ {(0, 0), and the three parities}. The ρ_Q matter stays massless here (below).
- **The copies' lowest twisted modes:** q_c(τ) as above, for c ∈ {(½, 0), (0, ½), (½, ½)}.
- **The condensate (tree level, the lowest twisted mode's effective theory):** with a tachyonic bulk mass² for the
  copies, written −ν in the units where a copy's lowest twisted mass² is q_c, and a positive quartic, the
  condensation energy is E_cond(τ) = −ε (ν − q_min(τ))₊², where q_min = min_c q_c and ε > 0 carries the quartic and
  the ratio of the condensate's scale to the loop's. ν and ε are free numbers, counted against the 19.
- **The domain:** SL(2, ℤ)'s fundamental domain, |Re τ| ≤ ½, |τ| ≥ 1, to Im τ = 14, as in W154. The joint state
  (τ, c) is moved by SL(2, ℤ) acting on both, so a condensate on one copy is an orbit of three; that is not a hand-pick
  under the WEAVE rule's clause on spontaneous breaking.

## Weave or thread

**H0 to H3 are weave-type.** They take every admissible content (Stage A's set) and every mass pattern or condensate in
the stated class, search the whole domain, and claim about all of them at once. The direction h is selected by
minimization, not by hand. The free numbers it needs (the masses, ν, ε) are named and counted. Nothing in it uses data:
the band is W154's stated window, used as a read-out.

## The cells, with predictions, priors and pre-mortems

| cell | prediction | prior |
| --- | --- | --- |
| H0 | **The copies at the forced line (exact, checked).** q_c(τ) > 0 for every c and τ, so no copy has a zero mode. q_{(0,½)} = 1/(4y); q_{(½,0)} = min_n \|τ − 2n\|²/(4y); q_{(½,½)} = min over odd n of \|τ − n\|²/(4y). At ω all three equal 1/(2√3); at i they are (¼, ¼, ½). SL(2, ℤ) permutes the three as it permutes the characteristics: for S and T, at ten random τ, the multiset {q_c(γτ)} equals {q_c(τ)} to 10⁻¹² | 97% |
| H1 | **No mass rescues a running content (the cusp lemma).** For every characteristic and μ ∈ {0.5, 1, 3}, on the axis τ = iy: \|S_c^{(μ)}(iy)/y³ − κ_c\| decreases in y over y ∈ {20, 40, 80, 160, 400}, and at y = 400 the product (S_c^{(μ)}(iy)/y³ − κ_c)·y is within 10% of the limit ℓ_c(μ) = −(μ²/4) Σ_{m ≥ 1} cos(2π m p₁)/m⁴. Here κ_c = 2 Σ_{m ≥ 1} cos(2π m p₁)/m⁶ is the massless cusp coefficient. So the leading cusp term of every content is mass-independent at each of the three cusps, and every content with A > 0 runs to a cusp for every mass pattern and every Higgs direction: every record content and E₈'s 248 (W154, C3) | 92% |
| H2 | **Masses that treat the parities alike keep the one curve.** (a) The small-mass expansion: (S_c^{(μ)}(τ) − S_c(τ, 3)) / (−(μ²/8) S_c(τ, 2)) = 1 to 1% at μ = 0.01, at ten random τ and all four characteristics, on one cut \|m\|, \|n\| ≤ 200. (b) On the cut \|m\|, \|n\| ≤ M (M even), Σ_c S_c(τ, 2) = ¼ E^{(M/2)}(τ, 2) − E^{(M)}(τ, 2) term by term, to 10⁻¹² relative at the ten τ, M = 200; so Σ_c S_c(τ, 2) = −(3/4) E(τ, 2) in the limit, and at M = 200 it matches −(3/4) E_cs(τ, 2) to 10⁻³. (c) So to order μ² an S₃-invariant mass pattern keeps V in the span of E(τ, 3) and E(τ, 2), and only moves t. (d) At finite masses the global minimum is at ω, at i or on the imaginary axis, never elsewhere. The grid: B = 1 (w_ρ = 1024/31), t ∈ {1.5, 3.5, 6}, each (A, B) realized twice, by bosons on the trivial characteristic (w_p = 0) and by fermions on the parities (w₀ = 0); one mass μ ∈ {1, 3} on every field on a characteristic, the ρ_Q matter massless; twelve cases. The domain is searched on a grid of step 0.05 to Im τ = 6 and along the axis to 14 | 85% (d: 75%) |
| H3 | **The condensate selects a direction and holds nothing.** (a) On the domain, q_min = q_{(0,½)} = 1/(4y), alone except on the arc \|τ\| = 1 (tied with (½, 0)) and at ω (all three). So the condensing copy is (0, ½), up to the orbit, and E_cond depends on Im τ only. (b) E_cond is non-increasing in y for every ν, ε: it pushes τ toward the cusp where the copy becomes massless and never holds τ. (c) Added to any Stage A content: A > 0 still runs; A < 0, B > 0 still holds (E_cond is bounded below by −εν², while V grows like 2\|A\|ζ(6)y³), and the global minimum's Im τ is at least Stage A's y* (it moves up or stays); the curvature across the axis at the minimum is Stage A's V's at that height, so Re τ is no better held | 93% |
| R | **Read-outs (no prediction):** y* and V(y*) at t ∈ {3.5, 4.0} with B = 1, for (ν, ε) on the grid ν ∈ {0.1, 0.25, 0.5}, ε ∈ {0.1, 1, 10} (E_cond in W154's units of V); the band's t-window under each (ν, ε), against W154's [3.205, 4.624]; the small-mass shift of B for a uniform S₃-invariant mass, B → B − (μ²/8)(w₀ − (3/4) w_p), against the twelve cases' minima | — |

**Pre-mortems** (how each cell could fail for a reason that is not the finding):
- **H0.** The minimum over the shifted lattice is taken over |a|, |b| ≤ 6; that is enough on the domain to Im τ = 14,
  since the minimizer has |a| = ½ and |b| ≤ 1.
- **H1.** The approach is slow: the correction is of order μ²/y, so at μ = 3 and y = 12 the coefficient is still 9%
  off (seen by hand). The cell tests the scaling, not equality at finite y. The massive sums use a lattice cut of
  |m|, |n| ≤ 80; the n ≠ 0 terms are of relative size about y⁻⁵ (3 × 10⁻¹⁰ at y = 80), and the omitted m > 80 about
  10⁻¹¹. For p₁ = ½ the terms alternate, so the decrease in y is checked, not assumed.
- **H2.**
  - (a) The next term is not analytic: its lattice sum behaves like μ⁴ log²(1/μ), about 2 × 10⁻³ of the μ² term at
    μ = 0.01, so the tolerance is 1%. The same cut is used on both sides, so the tail at s = 2 (about π/M²) cancels.
  - (b) On a cut the identity is exact in the stated form, since the even terms of the cut are the cut at M/2 scaled by
    1/16. The comparison with E_cs is the cut's tail, about π/M², hence 10⁻³.
  - (d) The massive sums use the cut \|m\|, \|n\| ≤ 30 on the 2-D grid. Since f ≤ 1, the omitted terms total at most
    π y³/(2 · 30⁴), about 4 × 10⁻⁴ at y = 6, against V of order 10²; the ρ_Q part uses E_cs. The axis beyond y = 6 uses
    the cut 80. The grid includes ω and i, and its lowest point is compared with V there.
  - (d) is the cell most likely to fail. A massive sum need not keep its minimum on the symmetric lines. A failure
    there would mean S₃-invariant masses do break the one curve at finite μ, a finding. The two realizations of one
    (A, B) differ at finite μ, so they may hold τ at different y.
- **H3.** E_cond is the tree-level energy of the lowest twisted mode, valid near threshold (ν − q small against the
  next twisted level). The condensate's profile is not constant on the fibre, so the masses it gives other fields, and
  its own loop, are left out.

## What the outcomes mean (fixed now)

- **H0 to H3 hold.** At the forced line the Higgs direction cannot hold τ where Stage A does not.
  - No mass, and no Higgs direction, rescues a content that runs: the cusp lemma.
  - Directions that treat the parities alike only move Stage A's t.
  - A condensate selects one copy by minimization, the one that becomes massless at the cusp being approached, and it
    pushes τ toward that cusp. It holds neither Im τ nor Re τ.
  - So the census over contents is complete at this order. The band's price stays in the content (Stage A), and a
    condensate adds two free ratios (ν, ε) and moves y*. Option 1 of the ledger is closed. What is left is to earn the
    content (option 3, GENESIS FK11), or a frame beyond one loop.
- **H2(d) fails.** S₃-invariant masses break the one curve at finite μ. The minima found are read out, with their
  free numbers (the masses) counted.
- **H3(c) fails.** The condensate holds something Stage A does not. It is diagnosed before anything else is said.
- **Any other cell fails:** the failure is the finding, and it is diagnosed before anything else is said.
- **This is data-free.** The band is W154's stated window, used as a read-out, so this is not a trial.

## What stays out

- The matter's masses (Yukawa couplings in ρ_Q): they need the matter's spectrum, not a lattice sum.
- The condensate's own loop and the masses it gives other fields (its profile is not constant on the fibre).
- Fork (A), the Higgs as a covariant form (W146 to W152's frame).
- The area of the fibre, the line's dynamics, and every content that is not S₃-invariant (as in W154).
- Any comparison with data beyond the stated window.

## Seen before the rule (disclosed)

- **Read:** W154's rule, script and output; main's main_w62.py (E_cs, S_c, copies) by git show from 22b7d5739; the
  ledger's row on h.
- **By hand, in the scratchpad (two short scripts, not committed):**
  - x³K₃(x) at x = 10⁻³, 10⁻², 0.1 (7.999999, 7.9999, 7.99001), which fixed the expansion's coefficient at −x²/8
    (a first guess of −x²/4 was wrong);
  - S_c^{(0.05)} against S_c(τ, 3) − (μ²/4)S_c(τ, 2) at τ = 0.13 + 1.4i, with that wrong coefficient;
  - the cusp ratio at y = 12 for μ = 0, 1, 3 (2.0347, 2.0125, 1.8512 against κ = 2.0347 on the trivial
    characteristic), which showed the slow approach;
  - Σ_c S_c(τ, 2)/E(τ, 2) = −0.75005 at a cut of 80;
  - q_c at ω, at i and at x = 0.3 for y = 1.5, 2.1, 3.2, 8 (the (0, ½) copy lightest, at 1/(4y)), and the multiset
    law under S and T at one τ.
- **Not run:** no script exists; no minimum of any Stage B potential has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
