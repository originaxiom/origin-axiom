# Path 1-SL(n): SL(n) multichannel realization — real classical chain, but NO quantum crossing (n≥3)

**Date:** 2026-06-04. **Status:** exploratory probe, committed for honest history (labels below).
Proven core P1–P16 untouched. Script: `frontier/physics_probes/sln_multichannel_probe.py`.
Standalone math-physics; **no Origin-core / no thesis claim**.

**Question (the one genuinely-novel computable Tier-1 target).** The Fibonacci quasicrystal *is* the
SL(2) trace map (Path 1, confirmed) because a single-channel tight-binding transfer matrix lives in
`SL(2,R)`. Does an n-channel / n-th-order 1D chain realize the **SL(n)** trace map for `n≥3`, and do
the tower's `a_d` multiplicities control its spectrum? **Negative-result control baked in:** if no
such *physical* (Hermitian) chain exists, that is the informative NEGATIVE.

**Verdict.** Mixed, mostly negative — and precisely localized:
- **Realization as a real 1D system: YES**, but only as a **classical / non-Hermitian** linear-
  recurrence (transfer) system.
- **Realization as a quantum (Hermitian) spectrum: NO for `n≥3`** — a clean *symmetry-class*
  obstruction. The golden/SL(2)=Fibonacci quasicrystal is **special to `n=2`**.
- **`a_d` controls the gaps: unsupported** — `a_d` is band-center data, not the gap label.

## What was computed

**(a) Realization (constructive, POSITIVE).** Explicit `SL(3,R)` transfer matrices arise as companion
matrices of a 3rd-order linear recurrence `ψ_{j+1}=a ψ_j + b ψ_{j-1} + ψ_{j-2}` (`T=[[a,b,1],[1,0,0],
[0,1,0]]`, `det=1` for all `a,b`). Two energy-dependent letters `A(E), B(E)` + the metallic
substitution give a genuine real 1D linear-recurrence system whose trace dynamics is the project's
SL(3) trace map (B33/B60). So **the SL(n) metallic quasicrystal exists as an abstract/classical wave
system.**

**(b) The obstruction (the real test, NEGATIVE).** A *self-adjoint* (quantum) 1D operator has transfer
matrices preserving the Wronskian **symplectic (antisymmetric) form** → `Sp(2p,R)`. The decisive
computation — does a nondegenerate constant antisymmetric `S` with `MᵀSM=S` exist for both letters?

| n | system | invariant antisym. forms | nondegenerate? | self-adjoint? |
|---|---|---|---|---|
| 2 | SL(2)=Sp(2) (Fibonacci) | dim 1 | **yes** | **HERMITIAN** ✓ |
| 3 | SL(3) metallic transfer | dim 0 | **no** | **NOT self-adjoint** |

`SL(n,R)=Sp` only for `n=2`. For `n=3` (odd dimension) **no nondegenerate antisymmetric form exists at
all**, so `SL(3)` cannot be the transfer group of a self-adjoint 1D operator — the SL(3) metallic
chain is intrinsically **non-Hermitian**. The Fibonacci↔SL(2)↔quantum-spectrum link is an `n=2`
coincidence (`SL(2)=Sp(2)`), not a feature of the tower.

**(c) Spectrum (illustrative).** The SL(3) metallic transfer system still has a structured,
Cantor-like bounded-Lyapunov set distinct from a random arrangement (allowed-energy fraction
`metallic 0.17` vs `random 0.03`) — a genuine multifractal/quasiperiodic spectrum, but of a
**non-self-adjoint** operator (so "spectrum" here is the classical transfer-stability set, not a
quantum DOS; the periodic comparison is muddied by non-Hermiticity and is not over-read).

**(d) Does `a_d` control the gaps? — structural note (NEGATIVE).** The tower / `a_d` multiplicities are
the fixed-line Jacobian spectrum at the **trivial rep** (all traces `=n`) — the *band-center*
linearization of the trace map. The spectral **gaps** are labeled by the substitution's abelianization
(gap-labeling theorem; IDOS in `Z+Z/φ` for SL(2), Path 1b) — a **different** invariant. There is no
evidence `a_d` = gap labels; `a_d` is band-center data, not a gap label.

## Honest reading

- The SL(n) metallic quasicrystal is a **real classical 1D linear-recurrence system** with genuine
  quasiperiodic spectral structure — modest, real, and constructible.
- But it is **not a standard quantum (Hermitian) spectrum for `n≥3`**: the symmetry class
  (`SL(n≥3)` ∉ symplectic) forbids it. The clean Fibonacci↔quantum story does **not** generalize.
- The tower's `a_d` does **not** control the gap structure (it is band-center, not gap-label data).
- **NET:** Path 1-SL(n) lands in the *same* 1D condensed-matter neighborhood as SL(2), no deeper, and
  with a sharper-than-SL(2) caveat (non-Hermitian). **No new quantum-physics crossing.** Consistent
  with the project's standing finding that the framework does not cross into thesis-supporting
  dynamical physics.

**Disposition:** the realization exists (classical/non-Hermitian); the quantum crossing is CLOSED for
`n≥3` (controlled, symmetry-class reason). Together with the metallic-anyon negative (V28), the two
live real-physics targets are exhausted: both land in known, modest, non-fundamental territory.
Proven core untouched.
