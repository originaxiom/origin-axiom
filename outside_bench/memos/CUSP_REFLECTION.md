# THE CUSP REFLECTION — the beat acts on the cusp lattice as exactly diag(1,−1): meridian fixed, longitude reflected, both signs +; one beat, two lattices, two orders
## (outside bench, 2026-08-25; thirty-first memo; campaign cell A3; every claim exact)

### The gap
The beat's action was banked on the fiber torus's H₁ (FIRST_BEAT: the tick's square
root, H₁-matrix [[2,1],[1,1]], trace 3, infinite order), on holonomy, algebra, matter,
spin. Never computed: the beat's action on the CUSP torus's own H₁(∂M;ℤ) = ℤ⟨μ⟩⊕ℤ⟨λ⟩
as an integer matrix — the other natural lattice the object hands us.

### THE THEOREM (`certificates/cusp_beat.py`, standalone, exact over ℚ(q))
With μ = A, λ = the banked longitude word bABaaBAb (trace −2 on the χ=+1 lift;
[μ,λ]=1 verified), and β(x) = W·conj(x)·W⁻¹ the beat:
1. β(μ) = **+μ** (memo 28's fact, re-verified);
2. β(λ) = **+λ⁻¹** — exact matrix equality, tested against all four candidates
   ±λ^{±1}; the identification is closed by the peripheral structure (ℤ², trace and
   commutation pin the candidate set).

> **Ω_cusp = [[1,0],[0,−1]]: the beat is a REFLECTION of the cusp lattice — order 2,
> det −1 — while on the fiber lattice it is [[2,1],[1,1]] — trace 3, infinite order.
> One beat, two invariant lattices, two different orders.**

Both signs are + at the SL(2,ℂ) level: no sign anomaly anywhere on the cusp over the
beat-selected lift. The + on λ⁻¹ is exactly what the spin selection predicts —
χ(λ) = +1 for both lifts since the longitude dies in H₁(M) = ℤ — so this doubles as an
independent consistency check of memo 28's character bookkeeping.

### What it connects
VII.1's mirror law ("the mirror fixes the meridian and inverts the longitude") was
banked from the bare Galois twist; here the same law is re-derived from the beat
itself, signs included — two separately-banked constructions agreeing on the nose. And
the contrast Ω_cusp (order 2) vs the fiber tick (infinite order) is the cleanest
statement yet of the beat's double life: reflection on the boundary, translation in
the fiber.

### Fences
Exact throughout; standalone certificate (no machinery imports); the candidate set
{±λ^{±1}} is justified by the peripheral subgroup being ℤ² (any image of λ under an
automorphism fixing μ and preserving the peripheral ℤ² is μ^k λ^{±1}; the exact matrix
equality with k = 0 and the trace check settle it — and the certificate verifies the
equality, not just membership). Gate 5 untouched; no value claimed.

### Certificates
`certificates/cusp_beat.py`; output `outputs/cusp_beat_out.txt`.

### One sentence for the ledger
On the boundary torus the beat is a pure reflection — meridian kept, longitude
reversed, both with sign +1 on the selected lift — the mirror law re-derived from the
beat itself, and the beat's two invariant lattices now sit side by side with orders
two and infinity.
