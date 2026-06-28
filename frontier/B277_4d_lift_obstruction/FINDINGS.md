# B277 — wall #4 made precise: a canonical N=2 lift exists; a chiral 4d SM is blocked by two named inputs

**Status: banked observation (frontier). FIREWALLED — geometry of the 6d (2,0) reductions, NOT a physics claim.
Nothing to `CLAIMS.md`.** The "probe-where-computable" pick for wall #4. `b277_4d_lift.py` (pyenv).

## Instead of asserting "wall #4 open" — pin down the obstruction
Two reductions of the 6d (2,0) theory of type `G`:
- **3d-3d:** `G` on a 3-manifold `M` → 3d N=2 `T[M]` (`T[4₁]` = U(1)+2 chirals, B262).
- **class-S:** `G` on a Riemann surface `C` → 4d N=2 `T[C]` (a chiral 4d SM needs the 4d side).

A 4d theory needs a **surface**, not a 3-manifold. But the figure-eight is a once-punctured-torus **bundle**, so it
carries a canonical surface (its fiber) and a canonical mapping class:

| datum | value |
|---|---|
| fiber | `Σ_{1,1}` (once-punctured torus), Euler char `χ = 2−2g−n = −1` |
| monodromy | `φ = R·L = [[2,1],[1,1]] ∈ SL(2,ℤ) = MCG(Σ_{1,1})`, trace 3, **pseudo-Anosov** |

## Class-S of the fiber (computable identification)
`class-S(A₁, Σ_{1,1}) = ` 4d **N=2\* SU(2)** (one SU(2), one adjoint hyper; the puncture = adjoint mass).
`MCG(Σ_{1,1}) = SL(2,ℤ) = ` the **S-duality** group of N=2\* SU(2); `φ` is an S-duality element. And `T[4₁]` (3d,
B262) `=` the **duality-wall** theory of `φ` (Terashima–Yamazaki / Dimofte–Gukov: the 3d-3d theory of a mapping
torus is the duality wall of its monodromy) — this **connects the 3d-3d and class-S pictures consistently**.

## The obstruction — exactly what is missing for a chiral 4d Standard Model
1. **SUSY/chirality.** The canonical lift is **N=2 (8 supercharges) → non-chiral** (vector-like matter only). The SM
   is **chiral = N=1 (4 supercharges)** or less. The N=2→N=1 reduction needs an **external datum** (superpotential /
   flux / twist) that the geometry of `4₁` does **not** supply. This is wall #3 (chirality) reappearing as the gate
   on wall #4.
2. **Type.** The 6d type `G` is **still a free input** — the fiber fixes the *surface* and *monodromy*, not the type.
   So the 4d lift does **not** resolve `input-E₆ = output-E₆` either; it inherits the same **CRUX**.

## Verdict (first-class input-required result)
Wall #4 is **not** "no lift": there is a canonical N=2 lift (the fiber class-S theory N=2\* SU(2), with `φ` as
S-duality). It fails to be a chiral 4d SM for two precise, **named** reasons — it is N=2 (needs an N=2→N=1 datum =
wall #3), and the type is free (= the CRUX). *residual-hint:* a chiral lift would need 6d (1,0) / a half-BPS twist /
flux on the fiber — none canonical to `4₁`.

Anchors: B262 (`T[4₁]`, the duality-wall side), B271 (wall #3 chirality / τ), B266 (the type CRUX). Lit: Gaiotto
(class-S; `Σ_{1,1}` = N=2\* SU(2)); Terashima–Yamazaki, Dimofte–Gukov (mapping-torus 3d-3d = duality wall).
