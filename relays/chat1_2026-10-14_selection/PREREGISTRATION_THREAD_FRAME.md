# The thread frame: τ is not selected but runs over the vacuum thread's closed geodesic, and the couplings are its cycle integrals (chat1, 2026-10-14, evening). Sealed before any code that computes it.

**Why.**
- **The owner's task** (18:27): "your task is to find/solve the selection principle". It quotes cc's diagnosis:
  - every "which?" comes out free: τ, the Higgs's direction, its location, the vacuum;
  - B990's law: an invariant construction picks only points its symmetry fixes;
  - every symmetric point tested gives no hierarchy.
- **This is one candidate, tested.**
  - It answers "which τ" by not choosing one: in the vacuum thread W, τ ranges over W's closed geodesic on the modular
    surface, and the four-dimensional couplings are cycle integrals along it.
  - **B990's law is respected by route A** (shrink the group). A thread breaks the modular group to its own centraliser,
    and the cycle integral of an invariant integrand is canonical given W.
  - The Higgs's direction and location are not chosen either. The Higgs is the surface frame's unique mode h (W72),
    integrated with the matter.
  - The vacuum thread is the one remaining choice. The gravitational action weights it (the root at large c; the
    root-share check).
- **It also answers the surface frame's open problem.** The SM seat's W72 found the three matter modes not normalisable:
  they grow at the modular cusp. Its W73 normalised them by the cusp's pairing of their units (H-end, chosen post hoc)
  and got 1 : 0.019 : 0.0004. **On a closed geodesic every norm is finite**, so the thread frame supplies a canonical
  normalisation.
- **The record's lead.** L254 / P-069 (registered, queue Q7) asks for "the arclength average of the golden coupling's
  mixing on the tick's orbit". This check is that lead in the surface frame's terms, for B1644's coupling.

**Definitions (fixed now).**
- **The forms** are the SM seat's own, built by its modules at `87cf7f551` (read-only, extracted by `git archive`):
  - the matter modes F_i, F₊, F₋: weight 3/2 in ρ_R, one unit each at the cusp (W72's `best_section`);
  - R: weight −½ (W65);
  - the Higgs mode h: weight 5/2 in ρ′ = ρ_R ⊗ χ_i, cuspidal and unique (W72's `solve_twisted`);
  - G_αβ = (R·F_β)F_α + (R·F_α)F_β − (F_α·F_β)R. This is B1644's coupling: a·G_αβ = F_αᵀ Y(a; R) F_β.
  - Pairings ⟨u, v⟩ = Σ_k u_k v̄_k in the coordinates W72 uses (its Petersson integrand).
- **A thread** W is a Lyndon word in L = [[1,0],[1,1]] and R = [[1,1],[0,1]], with M_W the product in word order. Its
  axis is the geodesic between M_W's real fixed points.
  - Period P_W = 2 arccosh(tr M_W / 2).
  - Arclength from the apex: τ(s) = x₀ + ρ(tanh s + i sech s).
  - Its image on the modular surface is the thread's closed geodesic.
- **The cycle integrals** (hyperbolic arclength s over one period; trapezoid rule, N equal steps):
  - K_αβ = ∫ ⟨F_α, F_β⟩ y^{3/2} ds;
  - Y_αβ = ∫ ⟨G_αβ, h⟩ y^{5/2} ds;
  - K_h = ∫ ⟨h, h⟩ y^{5/2} ds (an overall factor).
  - Each integrand is an SL(2, ℤ)-invariant scalar, so each point is evaluated at its image in the standard fundamental
    domain (y ≥ √3/2), where the series' tails are below 10⁻²⁵ (checked before this seal).
- **Masses** are the singular values of Ŷ = (K^{−½})ᵀ Y K^{−½}, in ascending order m₁ ≤ m₂ ≤ m₃.
- **Threads:** all Lyndon words of length 2 to 5 (12; the root LR among them).
- **The hybrid (read-out).** W72's banked surface-frame Y (its JSON, Y₀ = 2.0), normalised by the root's thread-frame
  K instead of W73's H-end.

**Seen first.**
- W72 and W73 in full: the surface Y, singular values 76 597, 2 788 and 57.4, and H-end's 1 : 0.0194 : 3.87·10⁻⁴.
- **The plumbing control**, run before this seal on the record's own numbers. The sections rebuild with 40-digit
  residuals of about 10⁻⁴¹, and h's first nine coefficients equal W72's banked ones exactly. On the root's geodesic:
  - at the apex ½ + i√5/2: |F_i| = 469, |F₋| = 130, |F₊| = 5.2, |R| = 3.8, |h| = 0.66;
  - at s = ±0.96: 635, 175, 7.1, 3.4, 1.09.

  No cycle integral, mass or ratio has been computed.
- **A hand estimate, disclosed.**
  - v₊ and v₋ are isotropic, so F₊·F₊/|F₊|² should be suppressed by about |q|^{1/2}. At the root's apex
    |q|^{1/2} = e^{−π√5/2} ≈ 0.03.
  - R·F_i/(|R||F_i|) should be suppressed by about |q|^{1/4} ≈ 0.17.
  - So some hierarchy is plausible. Its size is not computed.
- The literature report (NPP 2022, FILQ, Feruglio 2023) and the record sweep (L254 unrun; no geodesic average computed
  on any branch).

| | prediction | prior |
|---|---|---|
| Q0 (controls) | (a) h's first coefficients equal W72's exactly. (b) The integrand is invariant: at 20 random points with y ≥ 0.75, f(τ) and f(γτ) agree to 10⁻⁹ relative for random γ (all 13 integrands). (c) The trapezoid sums at N = 96 and N = 192 agree to 10⁻⁹ relative for every thread | 95% |
| TF1 | The root's Y has rank 3 (m₁/m₃ > 10⁻⁸) and its K is positive definite | 90% |
| TF2 | **The root's masses are hierarchical:** m₂/m₃ < 0.2 and m₁/m₂ < 0.2 | 45% |
| TF3 | The root's lightest state is mostly F₊: with u its singular vector and c = K^{−½}u (c†Kc = 1), the weight \|c₊\|²K₊₊ exceeds 0.9 | 55% |
| TF4 | Mirror pairs (W and its L ↔ R swap) give equal mass ratios to 10⁻⁸ | 90% |
| TF5 | Across the 12 threads, m₁/m₃ falls as the geodesic's highest point on the modular surface rises (Spearman ρ < −0.5) | 60% |

**Read-outs (no prior).**
- **Per thread:** m₂/m₃, m₁/m₃, the singular vectors' composition, the geodesic's highest point on the modular
  surface, P_W, and the CP phase invariant of Ŷ (whether Ŷ can be made real).
- **The hybrid:** W72's Y with the root's K; its ratios.
- **The data line** (HZ2021 at M_Z, the SM seat's received file):
  - m₂/m₃ = 0.00368, 0.0187 and 0.0589;
  - m₁/m₃ = 7.3·10⁻⁶, 9.4·10⁻⁴ and 2.8·10⁻⁴ (up, down, lepton).
  - Log distances only. No fit: one coupling cannot give three sectors (W73's lesson).
- **The scaling:** log(m₁/m₃) and log(m₂/m₃) against log|q| at each geodesic's highest point.

**What a result means, fenced.**
- **If TF2 holds**, a selection principle with no chosen point gives a hierarchy: the vacuum thread's geodesic, with
  everything integrated. The hierarchy's scale would be set by the geodesic's height: e^{−π√5} at the root's apex
  (Markov's lowest geodesic).
- **If TF2 fails**, integrating over the vacuum thread compresses the hierarchy. The surface frame's hierarchy (W73) is
  then a fact about normalising at the modular cusp, the end, and the selection question moves to the end.
- **Not tested.**
  - Why couplings should be cycle integrals: H-thread is a hypothesis, the thread read as the closed geodesic its
    monodromy draws on the modular surface.
  - The sectors' differences (P-128).
  - c and the weave's weights; mixing between sectors.
- No value. **0 of 19.**
