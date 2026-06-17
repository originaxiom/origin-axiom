# K007 — The Fibonacci Hamiltonian / quasicrystal trace map

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## The Fibonacci Hamiltonian

The **Fibonacci Hamiltonian** is the one-dimensional Schrödinger operator
```
   (Hψ)_n = ψ_{n+1} + ψ_{n−1} + V·χ(n)·ψ_n ,
```
where the potential follows the **Fibonacci substitution** `a → ab, b → a` (a model 1D **quasicrystal**). It is the
canonical mathematical quasicrystal: aperiodic but long-range ordered. Its spectrum is a **Cantor set** of zero
Lebesgue measure (Sütő 1987; Damanik–Gorodetski), with purely singular-continuous spectral measures — the hallmark of
quasiperiodic order.

## The trace map and Sütő's invariant

The transfer matrices of the Hamiltonian over successive Fibonacci approximants are related by the
**Kohmoto–Kadanoff–Tang (KKT) recursion**, which on the traces `(x_k, x_{k+1}, x_{k+2})` is exactly a **trace map** of
the same shape as `K001`'s `T(x,y,z) = (z, x, xz − y)`. The dynamically invariant quantity is the **Sütő invariant**
```
   I(x,y,z) = x² + y² + z² − 2xyz − 1 ,
```
conserved under the KKT map and equal (up to normalization) to the Fricke commutator coordinate `κ` (`K001`). The
spectrum of the Hamiltonian is the set of energies whose KKT orbit stays bounded — the non-escaping set of the trace
map. So the **metallic trace map of this project IS a quasicrystal trace map**: the same `GL(2,ℤ)` dynamics, with the
metallic means (`K002`) as the substitution-frequency analogues (golden = Fibonacci, silver = Pell, …).

## Gap labeling

The gaps in the Cantor spectrum are labeled by the **gap-labeling theorem**: the integrated density of states takes
values in `ℤ + φ⁻¹ℤ` (the module of the substitution), so each gap carries an integer pair — a `K`-theoretic invariant
of the tiling. This is the studied, rigorous content the metallic-mean family inherits: each `m` gives a distinct
quasicrystal with its own gap structure and trace field `ℚ(√(m²+4))` (`S023`).

## How the project uses it

- `B107` (V94, POSTULATED/firewalled) makes the identification explicit: the metallic trace map = the KKT/Fibonacci
  trace map, `κ = tr[A,B]` = the Sütő invariant (conserved ∀m), and every `SL(3)` tower eigenvalue is `±φ^k` — **one
  golden scale**. This is precisely why the spectral physics readings are **dead**: a one-scale "spectrum" is
  re-presented moduli-space monodromy, not a mass spectrum (`S015`, killed; `K006`'s firewall).
- `S023` (TESTED-POSITIVE) banks the genuinely-live content: the metallic means are **distinct real quasicrystals**,
  separated by their exact arithmetic (the trace fields `ℚ(√5)`, `ℚ(√2)`, `ℚ(√13)`, …), not by a finite-size box
  dimension.
- `S007` records the (firewalled) "mass gaps" reading; the entanglement/holography reading is tombstoned
  (`S021`, generic 1D-CFT criticality, not a bridge).

## What this is and is not

This is **rigorous condensed-matter mathematics** (spectral theory of quasicrystals) and it is genuinely the same
object as the trace map — a real, citable connection. It is **not** a bridge to fundamental physics: the conserved
`κ` and the golden scale are quasicrystal structure, not particle data, and the "something is hiding in the quantum
data" instinct is relocated to the honest, tooling-gated question of `S027` (does the metallic structure fingerprint
the quantum invariants?), not to any spectral identification.

**Anchors:** B107/V94 (the KKT identification, POSTULATED/firewalled); **B160/V154** (a fresh cross-session worker
independently re-derived the bridge from scratch and converged on the same firewall — *corroboration, not new
physics*; pins `κ=tr[A,B]=2+λ²` to the explicit transfer matrices via `z=xy−2`, adds an independent **bronze m=3**
quasicrystal, and the **κ-sweep** lead to the figure-eight hyperbolic point `κ=−2` ⟺ `λ=2i`); `../speculations/S007` (mass gaps, firewalled),
`S023` (distinct metallic quasicrystals, TESTED-POSITIVE), `S027` (the metallic-quantum-modular question, DORMANT).
External: Kohmoto–Kadanoff–Tang (1983); Sütő (1987, the invariant + Cantor spectrum); Damanik–Gorodetski (the
Fibonacci Hamiltonian, hyperbolicity); Bellissard (gap labeling).
