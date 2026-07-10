# Gate D — a non-Hermitian Damanik–Gorodetski question at `κ = √3·e^{±iπ/6}`

**For:** a non-self-adjoint spectral theorist (Damanik / Gorodetski school; or a non-self-adjoint /
pseudospectra specialist). **Status:** honest — the numerics below are a conjecture-shaped data
package, never a claim; the rigorous statement is what is being asked for.

## Setup (self-contained)

The Fibonacci trace map `T(x,y,z) = (2xy − z, x, y)` conserves the Sütő invariant
`I = x² + y² + z² − 2xyz − 1`. For a Schrödinger operator `H = Δ + λ·χ_Fib` (discrete Laplacian
plus the Fibonacci potential `χ_Fib` with coupling `λ`), the transfer-matrix traces follow this
map, and the seed `((E−λ)/2, E/2, 1)` lies on `I = (λ/2)²` for every energy `E`. At **real**
coupling `λ` (equivalently real `κ > 2`, with `κ − 2 = λ²`) this is the Fibonacci Hamiltonian: the
spectrum is a zero-measure Cantor set with dimension theory (Sütő; Damanik–Gorodetski, via a
uniformly hyperbolic horseshoe for `T`).

The object here forces the **complex** parameter `κ = √3·e^{±iπ/6}`. Then
`κ − 2 = e^{±2iπ/3} = ζ₃` (a primitive cube root of unity), so `λ = e^{±iπ/3}` is a primitive 6th
root of unity, `|λ| = 1`, and `H` is **non-self-adjoint**. Two exact structural facts hold:
`H^T = H` (the operator is **complex symmetric**, not self-adjoint), and `H(λ̄) = conj H(λ)`
entrywise, so the `±` pair `κ ↔ κ̄` is a single antiunitary (Galois) `ℤ/2` orbit acting *across*
the pair, not within one member.

## The data package (finite grids / finite depth / approximant sizes ≤ 1597; controls locked)

Every item is bracketed by Hermitian controls that reproduce the DG-proven picture (the `V=1`
Fibonacci Hamiltonian gives escape rate `γ ≈ 0.14 > 0` and persistent max-gap/diameter; the `κ=2`
periodic limit gives `γ = 0` and the band `[−2,2]`, measured as `4/7` of the test line).

- **Exponential escape, zero-area spectrum.** The complexified trace map on the object's level
  surface shows clean exponential escape (rate ≈ 0.51 over ≥ 3 decades — the same signature
  validated against the DG-proven control), and the non-escaping set has **zero Lebesgue area** in
  ℂ. The real section is empty; the eigenvalue cloud sits in `0.200 ≤ Im E ≤ 0.803`.
- **Totally-disconnected signature.** The minimum-spanning-tree max-gap/diameter is persistent —
  `0.1304 / 0.1307 / 0.1305` across approximant sizes 610/987/1597 — versus `0.002 → 0` for the
  band control; escape-based and eigenvalue-cloud box-dimension estimates put the dimension at
  **≈ 1 within ±0.2** (they rule out positive area and dimension → 2, but cannot distinguish a
  Cantor subset of a curve from a genuinely 1-dimensional cloud at accessible resolution).
- **Tame non-normality.** Eigenvector condition numbers grow only **polynomially** in volume
  (`cond(V) ≈ 6.8 → 17.4` over sizes 89 → 610, `~ n^{1/2}`); pseudospectral amplification stays
  `O(10)` and under the Bauer–Fike bound (max `dist(z,Λ)/σ_min ≈ 3.16 ≤ cond(V) ≈ 10.8`); and the
  open-vs-periodic boundary-condition movement (`0.0385`) **matches the Hermitian control**
  (`0.0305`) — no Hatano–Nelson-type spectral pooling under boundary change.

## The two data-supported conjectures (never claims)

- **D1 (complex-horseshoe uniform hyperbolicity).** For `κ = √3·e^{±iπ/6}`, `T` restricted to the
  complex level surface `{I = (κ−2)/4}` is uniformly hyperbolic on its non-escaping set — a complex
  horseshoe in the Bedford–Smillie sense; the Schrödinger line `((E−λ)/2, E/2, 1)` meets its stable
  lamination in a compact, totally disconnected set `Σ ⊂ ℂ` of zero Lebesgue area with box dimension
  ≈ 1; and `Σ` is the spectrum of `H = Δ + λ·χ_Fib` (the boundary-condition-independent Hausdorff
  limit of the approximant spectra).
- **D2 (pseudospectral correspondence).** Because the cocycle is complex symmetric with only
  polynomially growing eigenvector condition numbers, the ε-pseudospectra of the approximants
  converge to the ε-neighborhood of `Σ` with polynomially bounded amplification — no spectral
  pooling, no exponential boundary sensitivity — so DG-type spectral data survive
  non-self-adjointness at this `κ`, with **pseudospectra** (not self-adjoint spectral measures) as
  the correct regularity language.

## The single question

> Is there a Damanik–Gorodetski-type structure theorem for this non-self-adjoint, complex-symmetric
> Fibonacci-type operator at the complex coupling `λ = e^{±iπ/3}` — i.e. can uniform hyperbolicity
> of the complexified trace map on the non-escaping set of a *complex* level surface be established
> (conjecture D1), identifying the spectrum with a dynamically-defined totally-disconnected set —
> or is this regime known to be genuinely open?

## Honest scope

None of the above is a proof: finite grids, finite iteration depth, approximant sizes ≤ 1597, and
about 1.5 usable decades for the condition-number fit. The rigorous statements — uniform
hyperbolicity on a complex level surface and the operator-theoretic spectral identification — stay
specialist. We claim no physical meaning for the spectrum; the question is purely spectral-theoretic.

**Provenance.** Rests on B499 (the CL-3D data package: escape structure, pseudospectra, dimension,
symmetry, and conjectures D1/D2); Hermitian dictionary K007/K010; the object's transcendentality
context B317; `docs/OPEN_PROBLEMS.md` Gate D. Literature: Damanik–Gorodetski (the Hermitian
horseshoe), Sütő (the invariant), Bedford–Smillie (complex horseshoes), Trefethen–Embree
(pseudospectra of nonnormal operators), Bowen–Ruelle (escape rate = pressure). Nothing promotes to
`CLAIMS.md`.
