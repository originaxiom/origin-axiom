# W60 — the rule, recorded before the code

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. Nothing here is a result.

## Why this arc

- **The owner ruled "W60: quark sector (Recommended)"** (2026-10-13; `docs/THE_OWNERS_RULINGS_2026-10-08.md`), after
  W59.
- **What W59 left open.** At τ = ω a charged boson in the parity sectors sends the hypercharge Wilson line to the
  colour centre's 3-torsion lines. Only the quarks see that line (W59's K5). The quarks live in the matter's local
  system ρ_Q, whose spectrum with a line was not computed.
- **This arc computes it directly.** It takes the spectrum of the ρ_Q ⊗ L_φ Laplacian on the punctured fibre at τ = ω,
  with the puncture's −1 as a half flux. From the spectrum it gets the line's potential, in two dimensions and in six.
- **The question.** Does the quark sector prefer or resist the colour-centre line?

## Weave or thread?

- **Weave-type.** The object is the weave's own local system on the shared fibre.
- **The content is a dictionary datum** (GENESIS FK11): which fields, how many, bosons or fermions. The cells are
  stated per sign. The one content-weighted number is a read-out, with its content stated.
- **The tags.** On the ruled branch; given Λ; at τ = ω (W59's τ).

## The objects (derived by hand, stated before the code)

- **The sector.** Sections of ρ_Q ⊗ L_φ on E_ω minus the puncture.
  - ρ_Q is the common point's quaternion representation, with ρ_Q(a) and ρ_Q(b) the units i and j, so the puncture's
    holonomy is −1.
  - L_φ is the flat U(1) line with holonomies e^{2πiφ₁} along 1 and e^{2πiφ₂} along ω.
  - A field of hypercharge charge q (in units of 6Y) sees φ = q w.
- **Its Laplacian is taken with the Friedrichs extension at the puncture** (eigenfunctions ~ r^{1/2}).
- **Fermions see the same nonzero spectrum.** D†D and DD† share their nonzero spectra. With the weave's end condition
  (W22) one chirality is regular at the puncture, so that chirality's Laplacian is the Friedrichs one. The other
  chirality carries the zero mode ℓ (W21).
  - The index is −1 per block for every φ, since the line does not change the degree. So ℓ persists: the line gives
    the generations no mass.
- **Exact symmetries of the sector's potential U(φ).**
  - **Period ½ℤ²**, since ρ_Q ⊗ χ_p ≅ ρ_Q (W49).
  - **U(−φ) = U(φ).**
  - **At ω, invariance under the order-3 rotation of the line torus.** The rotation permutes the units and keeps ρ_Q's
    class.
- **The colour-centre line w₀ = (⅓, ⅓).** There Q sees (⅓, ⅓), u^c sees (⅔, ⅔) and d^c sees (⅔, ⅔), and each of these
  is equivalent to (⅙, ⅙) under the symmetries. The leptons and the Higgs see 0 (W59's K5).

## The method

- **The lattice.** A triangular grid on E_ω: N × N points z_ij = ((i + ⅓) e₁ + (j + ⅔) e₂)/N, with e₁ = 1 and e₂ = ω.
  - The puncture z = 0 sits at the centroid of one triangle.
  - Each point has six neighbours: ±e₁/N, ±e₂/N and ±(e₁ + e₂)/N.
  - The Laplacian is the standard isotropic six-point one: (H u)(x) = (2/(3h²)) Σ_y (u(x) − U_xy u(y)), with h = 1/N.
- **The link variables are lattice gauge fields.**
  - A link crossing the cut s ≡ 0 in the +e₁ direction carries G₁ = ρ_Q(a) e^{2πiφ₁}.
  - A link crossing t ≡ 0 in the +e₂ direction carries G₂ = ρ_Q(b) e^{2πiφ₂}.
  - A diagonal link crossing both carries their product in the order crossed. Reversed links carry the inverses.
  - Every other link carries 1.
  - So the only plaquette with holonomy other than 1 is the triangle around the puncture, which carries −1: the half
    flux.
- **The spectrum.** The lowest K = 300 eigenvalues of H, computed by shift-invert Lanczos.
  - Matter: rank 2, at N = 96 and N = 192.
  - Abelian control: rank 1, with G = e^{2πiφ}.
- **The potential, from heat-trace differences against φ = 0**, with t₀ = 30/λ_K:
  - **two dimensions:** Δ log det(φ) = −∫_{t₀}^∞ ΔK(t) dt/t;
  - **six dimensions:** ΔV₆(φ) = −∫_{t₀}^∞ ΔK(t) t^{−3} dt.
  - Here ΔK(t) = Σ_n (e^{−tλ_n(φ)} − e^{−tλ_n(0)}). Both integrals are done in closed form per eigenvalue.
  - For a boson the potential is +½ Δ log det in two dimensions and ΔV₆ in six. For a fermion both signs are reversed.
  - Larger ΔK means a lower spectrum, so a boson prefers larger ΔK.
- **The units are the heat-trace units throughout.** The abelian exact values are computed in the same units:
  - ΔV₆ = −(A/4π) · 128 · Σ_{ℓ≠0} (cos 2πφ·ℓ − 1)/|ℓ|⁶ (Poisson), with A = √3/2;
  - Δ log det by W59's Kronecker form.
- **Where the potential is sampled.**
  - A 12 × 12 grid of φ on [0, ½)², step 1/24, at N = 96.
  - The special points 0, (¼, 0), (0, ¼), (¼, ¼), (⅙, ⅙) and (⅓, ⅓) at both N.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **P1, the abelian control** | At N = 192, for φ ∈ {(¼, 0), (½, 0), (⅓, ⅓), (0.1, 0.37), (0.4, 0.15)}: Δ log det matches Kronecker's exact value to 2 × 10⁻³ absolute. ΔV₆ matches the exact lattice sum to 3% relative. The N = 96 errors are larger than the N = 192 ones. | 75% |
| **P2, the symmetries on the lattice** | For the matter at N = 96, at six generic φ: the spectra at φ and φ + (½, 0), and at φ and −φ, agree to 10⁻⁹ relative. The order-3 image of φ gives the same Δ log det and ΔV₆ to 10⁻⁶. | 85% |
| **P3, the matter's two-dimensional term** | At N = 192 the fermion's two-dimensional potential (−½ Δ log det) is lowest at φ ≡ 0 among the special points, and highest at (⅙, ⅙) ≡ (⅓, ⅓). | 60% |
| **P4, the matter's six-dimensional term** | At N = 192 the fermion's six-dimensional potential (−ΔV₆) is lowest at φ ≡ 0 among the special points, and highest at (⅙, ⅙) ≡ (⅓, ⅓). So the quarks, as fermions, resist the colour-centre line, and as bosons they would prefer it. The grid at N = 96 shows no lower fermion value than at 0. | 65% |

**The read-outs (no prior).**
- **Convergence.** The matter's lowest ten eigenvalues at N = 96 and 192, and their apparent order of convergence.
- **The hand estimate's form.** The geodesic estimate gives ΔK ∝ −2 Σ_{k₀} (cos 2π(2φ)·k₀ − 1) e^{−1/t}, since odd
  windings have trace 0 in ρ_Q. Its shape is compared with the computed ΔV₆ on the grid.
- **A stated content's net term at the colour-centre line.** In the same units, with 6d Casimir weights per real
  on-shell degree of freedom (bosons +, fermions −):
  - the quarks as 3 generations × (Q: 6, u^c: 3, d^c: 3) colour-isospin states, each a complex fermion field in
    ρ_Q ⊗ L (rank 2, already in the sector), with charges 1, −4 and 2;
  - the Higgs as a complex doublet in the three parity sectors jointly (W59's joint boson), with charge 3.
  - The sign of the net ΔV₆ at w₀ against w = 0 is reported. It is a read-out, not a cell: the content is a dictionary
    datum.

## The reading, written before the run (predicted)

- **The quark sector resists the colour-centre line if its fields are fermions.**
  - In ρ_Q every odd winding has trace 0, so the line enters only through doubled windings, where the holonomy is −1.
  - Turning on the line then lowers the bosons' spectrum and raises the fermions' energy.
- **So with the Standard Model's content, where the quarks are fermions and many,** the line most likely sits at
  w ≡ 0 mod ½ for the quarks.
  - At w = 0 nothing splits d from e.
  - At a half-period the quarks see what they see at 0.
- **So D1's route to a d–e split at a symmetric state most likely closes.**
- **What would reopen it.** A content with enough charged bosons in ρ_Q, or the Higgs's term dominating, which the
  counts make unlikely.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
- **The method is fixed here before any run:** N, K, t₀, the grid and the special points.
