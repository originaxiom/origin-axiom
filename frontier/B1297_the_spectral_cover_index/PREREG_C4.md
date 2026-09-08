# B1297 Part II — PRE-REGISTRATION (before evaluation): the first Galois-unprotected sector, the 4-fold cyclic cover

*Written after Part I's table (16 zeros on the 3-fold cover) and after T-GALOIS-SELF-DUALITY was found and checked:
if the coefficient field of `V = Sym²ρ_geo ⊗ χ` admits an automorphism τ fixing the trace field k and inverting χ,
then `V^τ = V*`, every rank is τ-invariant, and `I(V) = −I(V) = 0`. For the object k = ℚ(√−3) = ℚ(ζ₃), so the
argument covers every χ of order prime to 3 and is UNAVAILABLE exactly for 3 | ord(χ). The 3-fold cover has no
3-torsion (H₁ = ℤ⊕(ℤ/4)²): Part I's test could not have passed. This part registers the first sector where it can.*

**Object.** `C₄` = the 4-fold cyclic cover of m004 (`a↦0, b↦1 mod 4`), one cusp, `H₁(C₄) = ℤ ⊕ ℤ/3 ⊕ ℤ/15`
(|Tors| = |Δ(i)|²·|Δ(−1)| = 9·5 = 45, Δ = t²−3t+1; SnapPy agrees). Lifted meridian `m_{C₄} = (ab)⁴` is the free
generator, lifted longitude null-homologous, so ALL 45 torsion characters are cusp-trivial (t₀ = 1 on Sym²⊗χ).

**Formula, domain, conventions.** Unchanged from PREREG.md §2: `I = t₀ − r₁` in domain D, `F = −I`, `Cc = I`;
identities (d) checked on every sector; exact arithmetic over ℚ(ζ₁₂) ∋ ω (order-3 values), plus ζ₅ for the
order-5/15 characters — those are computed numerically (SVD, second method for all) because ζ₅ ∉ ℚ(ζ₁₂); they are
Galois-protected controls (τ₅ fixes k and inverts ζ₅) and are predicted 0 (order 5) or pairwise related (order 15).

**The configuration.** As in PREREG.md §3 with the (ℤ/3)-part of H₁(C₄) supplying κ: ρ₁ = (ρ_geo|_{C₄} ⊗ κ) ⊕ κ⁻²
has det 1 for κ of order 3 as well (κ²·κ⁻² = 1), is non-extending when κ^τ ≠ κ, and the bifundamental's only
index-carrying summand is `Sym²ρ_geo ⊗ ψ`, ψ = κ/κ^τ. On the 3-torsion the deck action has t² = −1 (Δ(±i)), so
`1 − t` is invertible there (det = Φ₄(1) = 2, a unit mod 3): ψ ranges over ALL 8 order-3 characters as κ does.
NOTE the E₆ constraint of §3 (scalar twists must be cubic) now READS THE OTHER WAY: an order-3 κ is itself a
legitimate SL(3)-scalar twist, so the abelian sector `diag(κ, κ^t, κ^{t²})`-type configurations also exist here;
they are characters (T4 ⇒ 0) and are computed as controls (k = 0 rows).

**PASS / FAIL.** PASS: some order-3 ψ has `I(C₄; Sym²ρ_geo ⊗ ψ) ≠ 0` — the descent carries the bit through
3-torsion, the object's own prime. FAIL: all 8 give 0. Then the fail theorem of PREREG.md §4 extends to the
4-fold cover; the remaining Galois-unprotected sectors are the 3-torsion of higher cyclic and non-cyclic covers of
m004 (to be enumerated, not chased, in FINDINGS).

**Predictions recorded before computing (checks):** `J(ψ⁻¹) = −J(ψ)`; `J(ψ∘τ_deck) = J(ψ)`; the symmetry census of
the 32 isometries of C₄ (lifts of D₄) on the order-3 characters is computed FIRST, and its forced zeros recorded
BEFORE the table. If the census forces all 8 to zero (e.g. the period-2 lift acting as −1 on the 3-torsion, as it
did on the 4-torsion of C₃), the result is again a forced zero and is REPORTED AS SUCH — not as a passed test.
The non-vacuous case is: some order-3 ψ NOT forced to zero by the census; only then is the table a real test.
