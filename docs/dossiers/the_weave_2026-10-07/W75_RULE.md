# W75 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **chat1 sealed and ran a check of the scale** (`chat1/web-seat` @ c1986e33d → 28bb46c83; PREREGISTRATION sha256
  78fa6de2). The owner had asked chat1: "isnt the scale there? the right scale needed for us? compatible with the
  rest?" Every cell held as sealed:
  - the weave's chiral threads see the quantised level k, in mirror pairs (690 of 745 threads have CS ≠ 0);
  - weighting the weave by its volume selects no σ (Guéritaud–Futer: infinitely many threads below 2v₈);
  - at a genuine cusp the nilpotent residue's norm in the harmonic metric is 1/L, the horocycle's length over 4π.
  - A labelled post hoc then found that the field's pointwise norm on unit vectors of the cusp metric is exactly ½.
- **The owner's rule is to verify load-bearing mathematics with the seat's own code, even when it is published.** Two
  parts carry weight here.
  - **The mirror pairs** re-scope B1012's k-blindness, a premise of the record's anchor declaration B1015, from the
    weave to the one thread m004.
  - **The local model** decides whether the field at the puncture has a free size. The seat's reading after §91 says
    the field there is the fibre's own uniformization. If so, the size of the electroweak condensate is not a new
    number.
- **The owner's order is "we look what fixes τ then we count free numbers".** This arc asks what fixes the field's
  size, and whether it adds a free number.

## Weave or thread?

- **U1 is a census of every thread under a stated rule.** The rule is chat1's: every Lyndon word in L, R of length 2 to
  12 containing both letters, with the bundle `b++` + word (the record's GM5d convention in GENESIS). Its claim, that
  the threads' Chern–Simons content comes in mirror pairs, is about all threads at once.
- **U2 to U4 are facts of the shared fibre's end, the same for every thread.** Their quantity is local at the puncture,
  not defined by the joint action. So they are not weave results in THE WEAVE's three-condition sense, and they are
  not one thread's either. They are labelled **fibre-level**.
- **The tags.** H-RES (chat1: the field is a tame Higgs field with its residue at the puncture), untested by any arc.
  §91's reading (the field at the puncture is the uniformization). No four-dimensional statement.

## Seen before the rule (disclosed)

- **chat1's whole arc was read before this rule:** the preregistration, the script, its run output (every cell held),
  and the post hoc's output (pointwise norm ½ for the nilpotent model, "1" for the uniformising field in chat1's
  normalisation).
- **The seat worked these by hand while drafting, before any code.**
  - **The ODE.** In the log frame e = ((dz/z)^{½}, (dz/z)^{−½}), take θ = E₂₁ dz/z and h = diag(e^{u}, e^{−u}) with u a
    function of L = −log|z|² alone. Then Hitchin's equation F_h + [θ, θ*_h] = 0 reduces to u″ + e^{−2u} = 0.
    - It has three branches: e^{u} = L − L₀, e^{u} = sinh(a(L − L₀))/a, and e^{u} = sin(a(L − L₀))/a.
    - The sinh branch grows like |z|^{−2a}, a parabolic weight a. The sin branch degenerates at finite L. So at weight
      zero only the linear branch is left, and its shift L₀ is the rescaling z ↦ e^{−L₀/2} z.
  - **The identification.** Write the uniformizing Higgs bundle as K^{½} ⊕ K^{−½}, with Φ = E₂₁ dz and
    h = diag(g^{−½}, g^{½}), where g|dz|² is a cusp metric. In the log frame it becomes θ = E₂₁ dz/z with
    h = diag(L/c, c/L), c = (g|z|²L²)^{½}. By the ODE it solves Hitchin's equation only at c = 1, the cusp metric of
    curvature −4 (chat1's K4d). There it is chat1's model with the basis order reversed.
  - **The monodromy.** On the circle |z| = r, the flat connection's φ-component in the log frame is iN with
    N = [[−1/L, −1/L²], [1, 1/L]]. Then N² = 0, so the monodromy exp(−2πiN) is unipotent, trace 2. The log frame
    itself turns by −1 around the puncture, so in the frame (dz)^{±½} the trace is −2: the record's κ = tr[a, b] = −2,
    which no choice of lift can change.
  - **The size.** The residue's norm in h is 1/L, and dz/z has norm L/2 on a unit vector of 4|dz|²/(|z|²L²). So the
    field's pointwise norm is ½ at every point. For a metric of curvature −1/R² it is 1/(2R): ½ at curvature −1 and 1
    at curvature −4, chat1's two numbers.
  - **The canonical coordinate.** If the cusp's parabolic generator is normalised to w ↦ w + 1, with z = e^{2πiw},
    then L = 4π Im w. The horocycle Im w = y has length 1/y, and the residue's norm is 1/L = ℓ_h/(4π) = e^{−d}/(4π),
    where d is the distance from the horocycle of length 1.
  - **The full action.** |e^{−σVol + ik CS}| = e^{−σVol}, so chat1's K3 already makes the weave weighted by its whole
    action (k and σ) diverge at every k and σ.

## The method (fixed here)

- **U1, the threads (SnapPy 3.3.2; chat1's thread list and convention).** For each thread W, take the bundle `b++` + W
  and the bundle of swap(W), the least rotation of W with L ↔ R. Then:
  - **The isometry:** `is_isometric_to` between the two bundles. An exception is recorded as a failure.
  - **Reversal:** a copy of W's bundle with `reverse_orientation()`. Its CS (Im `complex_volume()`, reduced mod π² to
    (−π²/2, π²/2]) is compared with −CS(W) and with CS(swap W).
  - **chat1's K1 count, reproduced on the same instrument:** the number of threads with |CS| > 10⁻⁶. This step
    repeats chat1's computation and is labelled a reproduction. It is not a second route.
- **U2 to U4, exact (sympy), written from the definitions on this seat.**
  - The Chern connection's curvature is F_h = ∂̄(h⁻¹∂h). For diagonal h it is −∂_z∂_z̄ log h_i dz ∧ dz̄.
  - θ*_h = h⁻¹ θ̄ᵀ h, and the bracket is [θ, θ*] = (θθ* − θ*θ) dz ∧ dz̄.
  - All derivatives are taken in x and y, with L = −log(x² + y²).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **U1, the mirror pairs on the seat's instrument path** | For all 745 threads, `is_isometric_to` finds b++swap(W) isometric to b++W, with no failures. The reversed copy's CS equals −CS(W) mod π² to 10⁻⁸ and CS(swap W) mod π² to 10⁻⁶. The reproduced count of threads with \|CS\| > 10⁻⁶ is 690. | 85% |
| **U2, the local model by the ODE** | With h = diag(e^{u(L)}, e^{−u(L)}) and θ = E₂₁ dz/z, Hitchin's equation is u″ + e^{−2u} = 0 in both diagonal entries, with zero off-diagonal. The three branches solve it exactly. Replacing z by λz moves L to L − log\|λ\|², so the linear branch's L₀ is a rescaling of z. | 95% |
| **U3, the identification and the monodromy** | The uniformizing bundle in the log frame is θ = E₂₁ dz/z with h = diag(L/c, c/L), c = (g\|z\|²L²)^{½}. It solves Hitchin's equation at c = 1 (curvature −4) and not at c = 2 (curvature −1). On \|z\| = r the flat connection's φ-component is iN with N² = 0 and N ≠ 0, for every r. So exp(−2πiN) has trace 2, and −exp(−2πiN) has trace −2. | 90% |
| **U4, the size** | The pointwise norm of θ on unit vectors of R²·4\|dz\|²/(\|z\|²L²) (curvature −1/R²) is 1/(2R) exactly, independent of the point: ½ at R = 1 and 1 at R = ½. In the canonical coordinate (z = e^{2πiw}) L = 4π Im w, and the residue's norm equals ℓ_h/(4π), with ℓ_h = 1/Im w the horocycle's length. | 97% |

**The read-outs (no prior).**
- The number of swap-symmetric threads, and of threads whose CS equals π²/2.
- U1's wall-clock time.
- U3's N at three values of L.

## The reading, written before the run (predicted)

- **B1012's k-blindness is a fact about one thread.** The weave's chiral threads see the quantised level k, and their
  Chern–Simons content comes in mirror pairs. A weave sum weighted by e^{ik CS} is real but depends on k. So B1015's
  premise "the object cannot see k" holds for m004 and must be scoped to it. A2 = c = 6σ stays external, since k
  multiplies CS and σ multiplies the volume (chat1's point 2), and the action-weighted weave diverges at every k and σ.
- **At a genuine cusp the field has no free size (fibre-level, under H-RES).**
  - At weight zero the local model is unique up to a rescaling of z. The global cusp's parabolic generator fixes that
    rescaling.
  - Its pointwise size is ½ in units of the fibre's curvature radius: the uniformization's own size. If that radius
    is A1's ℓ, the condensate's size is ℓ's, and B1015 says no dimensionless number flows from A1.
- **A hierarchy would be a depth.** The residue's norm is the horocycle's length over 4π, e^{−d} at depth d: a warp
  factor, as in Randall–Sundrum. A hierarchy as large as the electroweak one would need d ≈ 39 between where the
  observer's units are set and where the field's are. Nothing on record forces such a depth.
  - GENESIS FK10's unit sits at the modular cusp, not at the puncture (§90).
- **What this does to the count.** The Standard Model's one dimensionful number (v) would be the unit, not a new free
  number. The dimensionless Higgs number (m_H/v, the quartic) stays free. **0 of 19.**

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
- **This arc verifies another seat's sealed work.** chat1's arc keeps its own record. This seat rows it in the ledger
  and does not re-seal it.
