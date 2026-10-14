# The scale on the weave and at the cusp: a check of the premises (chat1, 2026-10-14). Sealed before any code that computes it.

**Why.**
- The owner, 2026-10-14, on chat1's sentence "The record has found repeatedly that the scale comes from outside
  (B151)": *"are u sure this is still valid? - now that we arent computing only in one thread but together with the
  weave and field? isnt the scale there? the right scale needed for us? compatible with the rest?"*
- The record's sealed position is B1015, which binds every crossing:
  - **A1 = ℓ**, the length unit;
  - **A2 = c = 6σ** (σ = ℓ/4G), "the one continuous dimensionless external coupling".
- A2 is declared external on B1012's argument:
  - S = −CS·k − Vol·σ (Gukov's split, at level t = k + iσ);
  - m004 is amphichiral, so CS = 0 and ∂S/∂k ≡ 0;
  - so the object cannot see k, and the level that survives, σ, is unquantised.
- That argument is about **one thread**. chat1's answer will say:
  1. the weave's chiral threads see k;
  2. k multiplies CS and σ multiplies Vol, so seeing k does not fix σ;
  3. the weave's natural volume-weighted sum selects no σ;
  4. under H-RES the field's size at a genuine cusp is not a free input — the residue is nilpotent, and in the harmonic
     metric its norm decays into the cusp like the horocycle length.

  This seal checks the mathematical premises of those four statements before they are asserted.

**Seen first** (read before this seal).
- B151, B167 and its B1241 addendum, B168, B169, B170, B181, B207, B290, B291, B399, B408, B413, B426, B563, B719, B899,
  B1012, B1015 (`DECLARATION.md`), B1017, B1088, B1205, B259; K018, K020; `docs/THE_LAMBDA_POSITION.md`.
- GENESIS v1.44, GAP5 and §7. P010.
- chat1's relays of today: O1–O8 and H-RES; the condensate test; the field note.
- Guéritaud, with an appendix by Futer, Geom. Topol. 10 (2006), Theorem B.1, read at its source today: for the cyclic word
  R^{a₁}L^{b₁}⋯R^{aₙ}L^{bₙ}, 2n·v₃ ≤ Vol < 2n·v₈, both bounds sharp.
- Simpson, *Harmonic bundles on noncompact curves*, JAMS 3 (1990): norm estimates near a tame puncture (cited, not
  re-read today). Grimm–Palti–Valenzuela, arXiv:1802.08264: the nilpotent orbit theorem and towers that become light
  exponentially in distance (abstract read today).
- **Plumbing only, before this seal:** `Manifold('b++LR')` identifies as m004, with volume 2.0298832128 and complex
  volume ≈ 0 (banked; B151, B1088). No other thread's volume or Chern–Simons value has been looked at.

**Objects and instrument.**
- **Threads.**
  - Every primitive positive cyclic word in L, R containing both letters, of length 2 to 12, taken as its least rotation
    (a Lyndon word): 745 threads.
  - The bundle is SnapPy 3.3.2 `Manifold('b++' + word)`, the record's own convention (GM5d: the − threads stay outside).
  - Vol = `volume()`. CS = Im `complex_volume()`, reduced mod π² to (−π²/2, π²/2].
- **Mirror.** swap(W) is W with L ↔ R: conjugation by P = [[0,1],[1,0]], which reverses the fibre's orientation, so
  M_swap(W) = −M_W. A thread is **swap-symmetric** when the least rotation of swap(W) equals W, or equals the least
  rotation of W reversed (reversal does not change the bundle).
- **n**, for Guéritaud–Futer, is the number of R-syllables of the cyclic word.
- **Local model** (sympy, exact). The punctured disc, with L = −log|z|².
  - Hitchin's equation: Θ_h + [θ, θ*_h] = 0, with Θ_h = −∂∂̄ log h and θ* = h⁻¹ θ̄ᵀ h.
  - The complete hyperbolic metric: 4|dz|²/(|z|²L²).

| | prediction | prior |
|---|---|---|
| Q0 (control) | (a) b++LR identifies as m004, with \|Vol − 2.0298832128\| < 1e-9 and \|CS\| < 1e-9. (b) Guéritaud–Futer holds on all 745 threads: 2n·v₃ − 1e-9 ≤ Vol < 2n·v₈. (c) every thread's solution is "all tetrahedra positively oriented" (the layered triangulation is geometric, Guéritaud) | 95% |
| K1 | **The weave is not k-blind.** At least 80% of the 745 threads have \|CS\| > 1e-6 mod π², so their action depends on the quantised level k | 90% |
| K1b | Every swap-symmetric thread has 2·CS ≡ 0 mod π² (to 1e-6) | 95% |
| K2 | **Mirror pairs.** For every thread, Vol(swap W) = Vol(W) to 1e-9, and CS(swap W) ≡ −CS(W) mod π² to 1e-6. The weave's Chern–Simons content comes in ± pairs | 97% |
| K3 | **No σ is selected by weighting the weave by its action.** For 1 ≤ a, b ≤ 25, every Vol(L^a R^b) < 2v₈ = 7.32772… So infinitely many threads have volume below 7.33, and Σ over threads of e^{−σ·Vol/π} = ∞ for every σ > 0. This is the theorem; the cell checks the instrument against it | 95% |
| K3b | Vol(L^a R^b) is strictly increasing in a for each fixed b, and in b for each fixed a, on 1..25 | 85% |
| K4a | **The field at a genuine cusp.** θ = E₁₂ dz/z (nilpotent residue) and h = diag(L⁻¹, L) satisfy Hitchin's equation. Within the ansatz h = diag(c₁L^{a₁}, c₂L^{a₂}) this is the only solution (a₁ = −1, a₂ = 1, c₁ = c₂) | 97% |
| K4b | The residue's operator norm in h is 1/L, which tends to 0 at the puncture | 97% |
| K4c | In the metric 4\|dz\|²/(\|z\|²L²) the circle \|z\| = r has length 4π/L. So \|Res\|_h equals the horocycle's length divided by 4π, exactly | 97% |
| K4d | **Sign control.** In the same convention the uniformising Higgs bundle (Φ = E₂₁ dz on K^{1/2} ⊕ K^{−1/2}, h = diag(g^{−1/2}, g^{1/2})) reduces to Gaussian curvature −4, i.e. hyperbolic. The opposite sign gives +4. So the convention is the one that uniformises, and the decay in K4b is not a sign artefact | 97% |
| K4e | **Semisimple control.** θ = diag(λ, −λ) dz/z with the flat metric solves the equation, and \|Res\|_h = \|λ\|: constant, no decay | 97% |

**Read-outs (no prior).**
- The distribution of CS over the threads.
- Threads with 2·CS ≡ 0 that are not swap-symmetric.
- Vol(L²⁵R²⁵) and its gap to 2v₈.
- In h, the operator norms of the sl₂ directions E₁₂, H, E₂₁ (expected L⁻¹, 1, L).

**What a result means, fenced.**
- If K1 and K2 hold, B1012's "invisible to the object in principle" is a statement about m004, not about the weave.
  The weave sees k, in mirror pairs.
- K3 says one natural route to fixing σ is closed. A weave weighted only by its gravitational action is not
  normalisable at any σ. It does not show that nothing fixes σ.
- K4 is a fact about tame harmonic bundles. Its physical reading needs H-RES, which no arc has tested. Under H-RES it
  would mean the size of the Higgs at a genuine cusp is set by where the cusp is cut, not by a free ℝ₊. It would also
  mean the masses B1644–B1646 read with the quaternion frame's Euclidean product need the harmonic one. Both are
  readings, for the note.
- **Not tested:**
  - any value of c;
  - any 4D statement;
  - whether the end's depth is forced (FK10);
  - H-RES itself;
  - the size of the electroweak condensate (W70), which is still unsourced (B1017).
- No number of the nineteen. **0 of 19.**
