# K002 — The metallic family and continued fractions

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## The family

The **metallic means** are the family of numbers
```
   λ_m = (m + √(m²+4)) / 2,      m = 1, 2, 3, …
```
— `m=1` is the **golden** mean `φ`, `m=2` the **silver** mean, `m=3` the **bronze**, and so on. Each is the positive
root of `λ² = mλ + 1`. The whole family is cut out by one matrix:
```
   M_m = [[m, 1], [1, 0]],     det M_m = −1,     tr M_m = m,
```
whose eigenvalues are `λ_m` and `−1/λ_m`. So a metallic mean is the spectral radius of the integer matrix `M_m`, and
`M_m ∈ GL(2,ℤ)` is a mapping class of the once-punctured torus (`K001`, `K004`).

## Why continued fractions

The continued-fraction expansion of `λ_m` is **periodic with period 1**:
```
   λ_m = [m; m, m, m, …] = m + 1/(m + 1/(m + ⋯)).
```
This is the arithmetic signature of "self-similar at one scale": the tail of the expansion is identical to the whole,
which is exactly the statement that `M_m` is a *single* hyperbolic generator whose powers reproduce the metallic
Fibonacci/Pell recurrences (`m=1` → Fibonacci, `m=2` → Pell). The golden mean is, by the **Hurwitz theorem**, the
*most badly approximable* irrational (the `[1;1,1,…]` tail is the slowest-converging), which is one precise sense in
which `m=1` is extremal within the family.

## The two structural facts the project leans on

1. **`det M_m = −1` (orientation-reversing).** The metallic generator lies in `GL(2,ℤ) ∖ SL(2,ℤ)`. This single sign
   is load-bearing throughout: it is the parity that splits the tower's catalog into `char(+M^k)` and `char(−M^k)`
   sectors (`K003`, B93/B94), gives the inversion identity `char(M⁻¹) = char(−M)` (B118), and is the obstruction
   distinguishing the external monodromy `sl(2)` from the internal principal one (B121, `K008`).
2. **Period-1 / "not-nothing" cuts out the family, not a member.** The condition "is a metallic unit" (a hyperbolic
   `GL(2,ℤ)` element with period-1 continued fraction) selects the whole family `{M_m}`; choosing a *member* requires
   importing extra structure. `K009` collects these imports — the **systole** (a metric: `m=1` is the shortest closed
   geodesic on the modular surface, B92) and the **expansion threshold** (a dynamical onset, P004/B120) each uniquely
   select `m=1`; **arithmeticity** (a number field) is a **two-element selector** picking `{m=1 golden ℚ(√−3),
   m=2 silver ℚ(i)}` — the two arithmetic punctured-torus bundles (B125, correcting B123). The motivation for aiming
   the theorem at the *family* rather than the seed is in `../philosophy/METALLIC_FOUNDATIONS.md` and
   `../philosophy/P000`.

## How the project uses it

- `B92` (V76) computes the **systole** length `2 log λ_m` and confirms `m=1` is the systole — the load-bearing
  one-liner of `S001` ("the systole, not amphichirality, selects `m=1`").
- `B93/B94` establish the `det = −1` ⟺ parity theorem (the catalog's sign structure follows the orientation sign).
- The `det = −1` slice is shown to be *structurally distinguished* (Paper 0): it is exactly what gives the tower its
  parity (`K003`, `K008`).

## What this is and is not

The metallic family is a family of **arithmetic / dynamical objects** (units, geodesics, mapping classes). The means
`λ_m` are not physical constants; the family-in-`m` is **dead as a moduli/physics family** (genus locked, forced
`j = 1728`; the volume-conjecture and CS-crossover readings are tombstoned). The live content is the **arithmetic
distinctness** of the members (e.g. the distinct trace fields `ℚ(√(m²+4))`, `S023`) and the catalog the family shares.

**Anchors:** B92/V76 (systole), B93/B94 (det=−1 parity), B103 (the catalog as a class function); `../philosophy/
METALLIC_FOUNDATIONS.md`, `../philosophy/P000`, `K009` (the `m=1` selections). External: continued fractions
and the Hurwitz theorem (Hardy–Wright); the metallic means (de Spinadel); `M_m` as a once-punctured-torus mapping
class (`K004`).
