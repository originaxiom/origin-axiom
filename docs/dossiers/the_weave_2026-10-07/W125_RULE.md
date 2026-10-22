# W125 — the quantum weave of closed universes: the sum over every closed universe the record's threads fill diverges, and is its divergence, thread by thread, the thread's own weight with one universal coefficient? (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's call** (2026-10-22): "continue bravely". This arc takes the gravity line's open question about the
  ground state.
- **Where the gravity line left it.**
  - Every thread is the space of an exact vacuum universe (W120).
  - W122 filled every thread at every slope in a box. The least closed universe is the Weeks manifold, a filling of
    −LR, and W122 read it as the ground state.
  - But a filling is a choice of slope, and the principle chooses none.
- **What quantum gravity does instead.** The path integral sums every saddle. Each filling σ of thread b is a closed
  hyperbolic universe, weighted at tree level by e^{−s·V_b(σ)}. Here s > 0 is the coupling, with s = 1/(4πG) in
  curvature units; the record's dictionary writes it as σ in S = −CS·k − Vol·σ.
  - Over every slope the sum is the weave's own operation: every thread, every slope, none chosen.
  - **It diverges.** The volumes of the fillings accumulate at the thread's own volume from below (Thurston; Jørgensen).
  - **Stanford and Yan** (arXiv 2510.19920, 2025) propose to renormalize such accumulation points by including the
    limiting cusped manifold itself as a counterterm. They check it at one loop, for the family of SL(2, ℤ) black holes.
    Their argument for the general case is locality (their §4, after Collier, Eberhardt and Zhang).
- **This arc** checks the tree-level form of that structure on the record's own threads. Is every thread's divergence
  exactly that thread's weight, with coefficients that do not depend on the thread?

## The object (by hand, to be checked)

- **The normalized slope length.** Take thread b and its cusp's Euclidean torus at the complete structure, with SnapPy's
  basis (μ, λ) and shape τ_b = λ/μ.
  - A primitive slope σ = (p, q) has Q_b(σ) = |p + qτ_b|²/Im τ_b. This is a positive binary quadratic form of
    determinant 1, independent of the horotorus's size. Slopes are taken up to sign.
  - Q_b(σ) = 1/Im(γτ_b), where γ is any matrix in SL(2, ℤ) with bottom row (q, p). So sums over slopes are values of
    the real-analytic Eisenstein series E(τ_b, w) = Σ_γ (Im γτ_b)^w.
- **Neumann and Zagier (1985).** As Q → ∞:
  - V_b − V_b(σ) = π²/Q + O(Q⁻²);
  - the core geodesic's length is ℓ(σ) = 2π/Q + O(Q⁻²).
  - The leading coefficients π² and 2π do not depend on the thread. The O(Q⁻²) term does, and on the slope's direction.
- **The count.** The number of slopes with Q ≤ X is (3/π)X + o(X): the ellipse Q ≤ X has area πX, a fraction 6/π² of
  lattice points are primitive, and slopes are taken up to sign.
- **The smoothed tower.** Z_b(s, ε) = Σ_σ e^{−s·V_b(σ)} e^{−εQ_b(σ)}, over the certified fillings. The factor e^{−εQ} is
  the cut on the core, e^{−2πε/ℓ} to leading order, as in Stanford and Yan's §3.
- **The divergence, by Mellin transform.** Write e^{s(V_b − V_b(σ))} = e^{sπ²/Q}(1 + O(Q⁻²)) and expand.
  - Σ_σ e^{−εQ} = (1/2πi)∫Γ(w)ε^{−w}E(τ_b, w)dw. The pole of E at w = 1 has residue 3/π, and E(τ, 0) = 1. So the sum is
    3/(πε) + 1 + O(ε), up to terms of size ε^{−1/4} whose residues are of order 10⁻⁵, from the zeros of ζ(2w).
  - Σ_σ e^{−εQ}/Q = (3/π) log(1/ε) + a constant + O(ε). The constant carries log(√(Im τ_b)·|η(τ_b)|²), by Kronecker's
    limit formula. That is the same modular invariant that Stanford and Yan's (3.30) finds in the cusp's one-loop
    determinant.
  - The O(Q⁻²) remainder converges absolutely.
  - So e^{s·V_b} Z_b(s, ε) = 3/(πε) + 3πs·log(1/ε) + fin_b(s) + o(1). **Both divergent coefficients, 3/π and 3πs, are
    the same for every thread.** That is the claim this arc checks.
- **What it means, if it holds.**
  - The divergent part of the sum over every closed universe is Σ_b e^{−s·V_b}·(3/(πε) + 3πs·log(1/ε)): the cusped
    threads' own ensemble times one universal factor.
  - So the threads, with one fugacity rule, μ(ε) = −3/(πε) − 3πs·log(1/ε), are counterterms for all threads at once.
    This is Stanford and Yan's proposal at tree level, on the record's threads.
  - The finite part of each thread's bare slope count is exactly 1. Regularized this way, each thread's tower of
    closed universes counts as one universe.

## The census (fixed now)

- **The threads:** W122's 42 bundles. Those are b++w and b+-w for every primitive cyclic word w in L and R with both
  letters, of length 2 to 6.
- **The slopes:** for each bundle, every primitive (p, q) up to sign with Q_b ≤ 16 000. The bounds come from the form:
  q² ≤ X·|μ|²/A, where A is the torus's area in the same normalization.
- **The fillings:**
  - SnapPy fills each slope.
  - A filling is certified when its solution type is "all tetrahedra positively oriented" and its volume is below its
    bundle's.
  - For Q ≤ 200, the volume must also agree at high precision within 10⁻⁹.
  - The core length is the real part of SnapPy's core_length.
- **The cuts:** ε ∈ {0.016, 0.008, 0.004, 0.002}, with e^{−0.002·16 000} = e^{−32}.
- **The couplings:** s ∈ {½, 1, 2, 4}.
- **The lattice sums** in K3 use every primitive slope, certified or not, from the cusp shape alone. K3(c) uses the full
  lattice, with every (m, n) ≠ (0, 0), to Q ≤ 20 000.

## Weave or thread

**A weave result if K1–K4 hold, with one caveat.**
- Condition 1 holds: every thread of W122's stated rule and every slope to the stated bound, none hand-picked.
- Condition 2 holds: the quantity is the sum over every closed universe the threads fill.
- Condition 3 holds: the claim is that one counterterm rule, with coefficients independent of the thread, serves every
  thread at once.
- **The caveat:** the sum splits into one tower per thread, and each tower's finite part is that thread's. Those finite
  parts are read out as thread results.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | the instrument: (a) every bundle's cusped volume equals W122's JSON value to 10⁻⁹; (b) every bundle's slope count with Q ≤ 16 000 is within 1% of (3/π)·16 000; (c) no slope with Q > 60 fails certification; (d) the least certified volume is the Weeks manifold's, 0.9427073628, at b+-LR, as in W122 | 90% |
| K1 | Neumann–Zagier's volume: on every bundle, every certified filling with Q ≥ 400 has \|Q(V_b − V_b(σ))/π² − 1\| ≤ 0.02 | 90% |
| K2 | the core: on every bundle, every certified filling with Q ≥ 400 has \|Q·ℓ(σ)/2π − 1\| ≤ 0.02 | 90% |
| K3 | the lattice, for each bundle's cusp shape: (a) with F_b(ε) = Σ_σ e^{−εQ} − 3/(πε) over every primitive slope, 2F_b(0.002) − F_b(0.004) is within 0.01 of 1; (b) with G_b(ε) = Σ_σ e^{−εQ}/Q, G_b(0.002) − G_b(0.004) is within 1% of (3/π)·log 2; (c) with H_b(ε) = (1/2π)Σ' e^{−εQ}/Q − ½log(1/ε) over the full lattice, 2H_b(0.002) − H_b(0.004) is within 0.01 of γ/2 − log 2 − log(√(Im τ_b)·\|η(τ_b)\|²) (Stanford and Yan's (3.30)) | 85% |
| K4 | the remainder converges: for every bundle and s ∈ {½, 1, 2}, Δ_b(s, ε) = Σ_σ e^{−εQ}[e^{s(V_b − V_b(σ))} − e^{sπ²/Q}], over the certified fillings, changes by less than 0.5 between ε = 0.004 and 0.002, while the bare e^{s·V_b}Z_b changes by about 239 + 3πs·log 2 | 80% |
| K5 | read-out: per bundle, the slope count, the uncertified slopes with their Q and solution types, and the median of Q·(Q·ΔV/π² − 1) over Q ∈ [100, 1000] (the second-order coefficient); fin_b(s) at ε = 0.002 and its Richardson value 2fin_b(0.002) − fin_b(0.004), for s ∈ {½, 1, 2, 4}; Δ_b(s, 0.002); the renormalized ensemble Z^ren(s) = Σ_b e^{−s·V_b}·fin_b(s), each thread's share and the leading thread; the Weeks manifold's term's share of Z^ren(s) | — |

## What the outcomes mean (fixed now)

- **K1 to K4 hold.** Then, at tree level, five things follow (by K1–K4 with the Mellin argument above).
  1. **No bare ground state.** The sum over every closed universe the record's threads fill diverges at every
     coupling. W122's "ground state" is a statement about single closed universes, not about the quantum sum.
  2. **The threads are the counterterms.** The divergence is, thread by thread, the thread's own weight e^{−s·V_b}
     times 3/(πε) + 3πs·log(1/ε), with coefficients the same for every thread. So the cusped threads, with one
     fugacity, cancel it for every thread at once. This is Stanford and Yan's proposal, checked here at tree level on
     the record's threads.
     - It is a proposal, not a theorem: off-shell topologies might cancel the divergence instead (their footnote 4).
     - The one-loop form is theirs and is not checked here.
  3. **One universe per tower.** The finite part of each thread's slope count is exactly 1. Regularized, each tower of
     closed universes counts as one universe: the thread.
  4. **The renormalized ensemble is defined up to adding a multiple of the cusped ensemble Σ_b e^{−s·V_b}.** That
     multiple is the counterterm's finite part, a scheme choice.
     - At weak gravity (large s) the least closed universe's term, e^{−s·0.9427}, outgrows any such multiple, which
       falls like e^{−s·2.03}. So W122's Weeks manifold leads the renormalized sum there, independent of the scheme.
     - At strong gravity (small s) the leader depends on the cusp's fugacity. The read-out reports this scheme's
       ranking, labelled scheme-dependent.
  5. **A READING.** The threads, which W120 and W122 left outside the closed-universe theorems, re-enter quantum
     gravity as the counterterms that make the sum over closed universes finite.
- **K1 or K2 fails.** Then Neumann–Zagier's leading coefficient fails on that thread at the stated Q, or the instrument
  is wrong there. Either way it is recorded, and the universality claim fails with it.
- **K3 fails.** Then the slope enumeration or Q's normalization is wrong, or a recalled formula is misquoted. It is
  recorded, and nothing in K4 is read until it is resolved post hoc, labelled so.
- **K4 fails.** Then the actual towers diverge differently from the universal form at the stated cuts. It is recorded
  with the size of the drift.

## What stays out

- The one-loop determinant and higher loops (Stanford and Yan; Maloney and Witten; Giombi, Maloney and Yin; main's
  B1107).
- Off-shell topologies. Fillings that are not certified. Manifolds with more than one cusp.
- The scale: s is free. The sign and value of the cosmological constant.

## Seen before the rule (disclosed)

- **Read:** Stanford and Yan, arXiv 2510.19920 (sections 1 to 4 and 6 in full; appendices by title). Duncan and
  Frenkel, arXiv 0907.4529 (the abstract). Neither is reproduced here.
- **Recalled:**
  - Neumann–Zagier's asymptotics; Kronecker's first limit formula;
  - E(τ, 0) = 1 and the residue 3/π at w = 1;
  - Thurston's filling theorem; Jørgensen's theorem.
- **Instrument checks** (not part of any cell's evidence):
  - SnapPy's cusp_info "shape" is λ/μ in its own basis: 2√3 i for m004, and −½ + 0.2887i for b+-LR. A filling takes
    about 1 ms.
  - **Neumann–Zagier was seen** on 20 fillings: m004, b++LR, b+-LR, b++LLLRRR and b+-LLRLR, each at the slopes
    (7, 3), (11, 4), (13, 5) and (29, 10), with Q from 45 to 2942.
    - Q·ΔV/π² ran 0.986 to 1.029, and Q·ℓ/2π ran 0.972 to 1.056. So K1 and K2 are not blind.
    - The size of the O(Q⁻²) term seen there, a coefficient of about 15, set K4's tolerance.
- **By hand:** the Mellin argument, and the estimate that K4's drift is about 0.01·s·κ for a second-order coefficient κ.
- **No tower sum, lattice sum or remainder** has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
