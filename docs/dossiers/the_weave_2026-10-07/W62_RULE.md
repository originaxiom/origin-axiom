# W62 — the rule, recorded before the code

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. What the seat worked by hand while
drafting, and one correction it found, are listed under "Seen before the rule". The priors were set after that. Nothing
here is a result.

## Why this arc

- **The owner chose "W62, as recommended"** (2026-10-13), after the dossier's "Reading A1–W61 together".
- **That reading's question.** Every closed-form sector's τ-dependence is one Eisenstein function, so τ cannot rest at
  a generic point. The one sector not known to be universal is the matter's six-dimensional term, through the
  puncture's diffraction. Does that term hold τ at a generic point?
- **This arc computes the matter's six-dimensional τ-dependence** along the imaginary axis and the boundary arc, against
  E(τ, 3). It also computes, in closed form, what the line W60 selected does to the other sectors' τ-dependence (see
  the correction below). Then it reads which contents hold τ, and where.

## Weave or thread?

- **Weave-type.** The sectors are the weave's local systems on the shared fibre: ρ_Q and the parity characters, all at
  once.
- **The content is a dictionary datum** (GENESIS FK11): which fields, how many, bosons or fermions. So the cells are
  per sector. Contents enter only the read-outs, each stated.
- **The tags.** On the ruled branch; given Λ; at the line W60 selected (a half-period).

## Seen before the rule (disclosed)

- **A correction to the reading of A1–W61, points 3 and 4 (worked by hand).**
  - Point 3 listed "the abelian lines" among the sectors whose τ-dependence is a multiple of E(τ, 3). That holds for
    the trivial sector and for the three parities jointly (W59's K3c). It does not hold for one parity, or one line,
    alone.
  - At the line W60 selected, w = (½, ½), the Higgs's three copies sit at p + 3w: 0, (½, 0) and (0, ½). They no longer
    treat the parities alike. Their sum is (1/16) E(τ, 3) − S_{(½,½)}(τ), where S_c(τ) = Σ′ c(m, n) y³/\|m + nτ\|⁶ and
    c is the character.
  - S_{(½,½)} is invariant under S and T², not under T: the theta group Γ_θ, of index 3. Its only elliptic point is i.
    So at the selected line τ = ω is no longer forced to be stationary.
  - A leading-shell estimate: the Higgs's boson term falls from ω toward i along the arc, and from i toward the cusp
    along the axis. So the state W60 selected, (ω, a half-period), is not stationary in τ.
  - Point 4 said a generic τ is the one door for flavour. In W61's overlap reading the couplings at a half-period line
    come from the quaternion units alone, and F = (f(z), f(z + τ)) dz exists at every τ (W21). So the overlaps are zero
    (T ⊗ T) or degenerate (T̄ ⊗ T) at every τ there. A generic τ matters only in the reading where couplings are
    functions of τ alone (W50).
- **The periodic part of the matter's heat trace as abelian sectors (exact, by hand).**
  - The straight closed geodesics of class ℓ fill the whole torus. In ρ_Q their trace is 0 if ℓ ∉ 2Λ, −2 if
    ℓ ∈ 2Λ \ 4Λ, and +2 if ℓ ∈ 4Λ.
  - Since Σ over the characters of Λ/2Λ is 4·1_{2Λ}, and over Λ/4Λ is 16·1_{4Λ}, the periodic part equals the
    "comb": −½ Σ_{χ ∈ Λ̂[2]} K_χ + ¼ Σ_{χ ∈ Λ̂[4]} K_χ. Its rank is 2.
  - So its six-dimensional boson value is +(31/1024) E(τ, 3) in W59's units. The matter's term is that plus a
    diffractive part D(τ), from paths that pass near the puncture.
- **A paraxial estimate of D (crude).**
  - For odd windings, the forward diffraction along a line through the puncture integrates to zero across the line.
  - For a double winding (trace −2) the correction has the opposite sign. Its size relative to the periodic term is
    about √(2/π)·√(2t)·L/A, which is 0.6 to 0.7 for the shortest lines at the t that dominates.
  - An isolated line's correction depends on t/L² alone, so its lattice sum goes as Σ\|ℓ\|⁻⁴, an E(τ, 2) shape. But at
    those t the spread reaches the neighbouring lines, and non-forward diffraction adds other shapes. The estimate gives
    the sign, not the form.
- **The cusp coefficients (exact, by hand).** As y → ∞, S_c(iy)/y³ → κ_c = Σ_{m≠0} c(m, 0)/m⁶:
  - 2ζ(6) untwisted along the shrinking cycle;
  - −(31/16) ζ(6) for a half twist along it;
  - −(31/512) ζ(6) for ρ_Q's periodic part.
  - A sector of signed weight W (bosons +, fermions −2 per state, in units of a complex scalar) contributes
    −W κ_c y³. So a content is stable at the cusp only if Σ W κ_c < 0.
  - By hand, every content below has Σ W κ_c > 0 at the cusp, for each of the three line choices.
- **The design was enumerated before the rule; no cell quantity was computed.**
  - The sublattices of index 8400 of the triangular lattice give the hexagonal shape, 11 shapes on the imaginary axis
    (y from 1.031 to 2.021) and 6 on the arc between i and ω.
  - One sparse eigensolve was timed on W60's recorded torus (N = 96 and 192, φ = 0, 400 eigenvalues): 56 s and 274 s.

## The method

- **One lattice for every shape.** The triangular lattice of W60 has unit spacing, sites at Z² + (⅓, ⅔) in the basis
  (1, ω), the six-point Laplacian (2/3)Σ(u_x − U_xy u_y), and the puncture at the centroid 0.
  - A torus is the quotient by a sublattice Λ ⊂ Z² of index n. Its shape is v₂/v₁, reduced mod SL(2, ℤ) and the mirror.
    The matter's spectrum is the same for a shape and its mirror (the mirror twists ρ_Q by a parity, and
    ρ_Q ⊗ χ ≅ ρ_Q).
  - The flat ρ_Q connection: a link crossing the cut through v₂ carries ρ_Q(a) = i; crossing the cut through v₁ it
    carries ρ_Q(b) = j; crossing both, their product in the order crossed. The cuts are shifted by 10⁻⁷ so that no
    site lies on one.
- **Why one lattice and one index.** On the same lattice with the same n, every local term of the heat trace (the bulk
  and the puncture's own constant) is identical across shapes. So differences between shapes see only the global
  parts: closed orbits and diffraction.
- **The family.** n = 8400.
  - It contains every index-n sublattice whose reduced shape lies on the imaginary axis with 1 < y ≤ 2.1, or on the
    unit arc with 0 < x < ½. Each shape takes the first sublattice in Hermite order.
  - The reference is the hexagonal shape (ω), first in Hermite order. The other hexagonal sublattice is a read-out.
- **The resolution check.** The same shapes with 2Λ, index 4n = 33600, are the same tori at half the spacing.
- **The six-dimensional term.**
  - In heat-trace units, V = −∫_{t₀}^∞ t⁻³ K(t) dt, with the closed form per eigenvalue of W60.
  - t₀ is set per family: t₀ = ℓ²_min/25, with ℓ_min the shortest torus vector among the family's shapes. Every
    member's τ-dependent orbits with nonzero trace have length at least 2ℓ_min, so the neglected t < t₀ part is below
    e⁻²⁵ of them.
  - ρ_Q: the lowest K = 400 eigenvalues by shift-invert Lanczos, with λ_K t₀ ≥ 30 checked.
  - The comb: every eigenvalue in closed form, (4/3)[3 − cos 2πκ₁ − cos 2πκ₂ − cos 2π(κ₁ + κ₂)] at κ = M⁻¹(m + φ).
- **The differences.**
  - ΔV_ρ(T) = V_ρ(T) − V_ρ(T₀), and the same for the comb. ΔD = ΔV_ρ − ΔV_comb.
  - They are converted to W59's units at fixed area by πA²/32, with A = n√3/2.
  - The exact periodic part is ΔV_per = (31/1024)[E(τ, 3) − E(ω, 3)], from Chowla–Selberg.
- **The closed forms.** S_c(τ) is computed by the direct sum over \|m\|, \|n\| ≤ 60. E(τ, s) for s = 2 and 3 is
  computed by Chowla–Selberg, against the direct sum as a control.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **M0, the construction** | (a) On every member at both sizes, exactly one triangle has holonomy −1 and every other +1, to 10⁻¹². (b) The spectra come in Kramers pairs, to 10⁻⁹ relative. (c) Built by the same code, W60's N = 96 torus gives W60's lowest ten eigenvalues at φ = 0 (times 96⁻²), to 10⁻⁹ relative. (d) The rank-1 operator from the same gauge code, with phases (¼, ½), matches the closed-form spectrum (the lowest 50) to 10⁻¹⁰ on the reference and two members. (e) λ_K t₀ ≥ 30 on every member at both sizes. | 95% |
| **M1, the periodic part on the lattice (the control)** | For every member, \|ΔV_comb − ΔV_per\| is at most 0.5% of max \|ΔV_per\| at n. The largest error at 4n is smaller than at n. | 85% |
| **M2, the diffraction is there** | At 4n, max \|ΔD\| over the members exceeds 10 times the largest M1 error at 4n. | 80% |
| **M3, its sign and size** | At 4n, for every member with \|ΔV_per\| above 10% of its maximum, ΔD has the sign opposite to ΔV_per, and \|ΔD\| < \|ΔV_per\|. The diffraction partly cancels the even windings. | 55% |
| **M4, not a multiple of E(τ, 3)** | Fit ΔV_ρ = β ΔE₃ over the members at 4n. The largest residual exceeds 3 times its member's uncertainty, taken as the larger of \|ΔV_ρ(4n) − ΔV_ρ(n)\| and the largest M1 error at 4n. | 55% |
| **M5, the matter's own critical points stay at i and ω** | At 4n, V_ρ increases along the axis members ordered by y, and along the arc members from ω toward i. So it is lowest at ω, a saddle at i, with no new stationary point between members. | 65% |
| **M6, convergence** | For every member with \|ΔD(4n)\| above 20% of its maximum, \|ΔD(4n) − ΔD(n)\| < 25% of \|ΔD(4n)\|. | 60% |
| **A1, the Higgs's copies at the selected line** | At five sample τ: the three copies' S sum to (1/16) E(τ, 3) − S_{(½,½)}(τ), to 10⁻¹⁰ of E. S_{(½,½)} is unchanged by τ → −1/τ and τ → τ + 2 (to 10⁻¹⁰), and changed by τ → τ + 1 (by more than 10⁻³). | 97% |
| **A2, the selected state is not stationary in τ** | In the frame w = (½, ½), the copies' boson term V_H = −Σ S has a τ-gradient at ω above 1% of \|V_H(ω)\| per unit τ. V_H decreases along the arc from ω to i (at the arc members' points) and is lower at i than at ω. | 85% |
| **A3, the cusps** | At τ = 8i, S_c/y³ equals κ_c to 10⁻⁴ of 2ζ(6), for the trivial sector, the three parities and the comb: 2ζ(6), −(31/16) ζ(6) for (½, 0) and (½, ½), 2ζ(6) for (0, ½), and −(31/512) ζ(6). | 95% |

**The read-outs (no prior).**
- **The contents.** In signed weights (bosons +, fermions −2 per state; a complex scalar is 1):
  - (a) W60's: quarks and leptons, 45 states in ρ_Q, plus the Higgs doublet's three copies at the line (+2 each);
  - (b) (a) with the 12 gauge bosons in the trivial sector (+2 each: four real on-shell degrees of freedom in six
    dimensions);
  - (c) (b) with the six-dimensional graviton in the trivial sector (+4.5);
  - (d) the matter alone.
  - For each, and for each of the three half-period lines: the weighted cusp coefficient Σ W κ (stable only if
    negative), the totals at every member, and the lowest.
- **The shape of D.** Fits of ΔD to ΔE₃, to ΔE₂, and to both, with their residuals. The correlation of ΔD with the
  paraxial estimate's double-winding term.
- **The content window.** For contents built only from the trivial sector and ρ_Q, the τ-potential is
  c_E E(τ, 3) + c_ρ V_ρ(τ). The ratio r = ΔV_ρ/ΔE₃ at each axis member, and the range of c_E/c_ρ that would put a
  stationary point on the axis between members.
- **The reference's orientation.** The other hexagonal sublattice's ΔV_ρ and ΔD against the reference, at both sizes.
- **Extrapolations.** ΔD extrapolated as O(h) and as O(h²) from n and 4n.

## The reading, written before the run (predicted)

- **The matter's six-dimensional τ-dependence is not a multiple of E(τ, 3).**
  - It is the periodic part, (31/1024) E(τ, 3), partly cancelled by diffraction at the puncture, which has its own
    shape.
  - But it keeps E's critical points: lowest at ω, a saddle at i. So on its own it sends τ to ω or the cusp, as E does.
- **At the selected line the Higgs's copies break the modular group to the theta group.** The state W60 selected is not
  stationary in τ: the Higgs's term pushes τ from ω toward i, and from i toward the cusp.
- **Every content on record runs to a cusp.** Its six-dimensional term is unbounded below as one cycle of the fibre
  shrinks. Holding τ at an interior point needs fields of the other statistics in the trivial sector, or bosons twisted
  along the shrinking cycle. That is a dictionary datum (GENESIS FK11), not something the weave selects.
- **So the owner's first question, what fixes τ, gets this answer: nothing computed does, for the contents on record.**
  A generic τ is possible only for contents chosen to make it so.
- **For flavour.** At a half-period line the overlaps are zero or degenerate at every τ (W61's algebra does not depend
  on τ). So even a held generic τ would not split the generations in the overlap reading.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count. A smoke test of the gauge construction alone (plaquettes on a tiny torus,
  no spectrum used) may precede the run, and is disclosed.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
- **The method is fixed here before any run:** the lattice, n = 8400 and 4n, the shapes' rule, K = 400, t₀, and the
  contents.
