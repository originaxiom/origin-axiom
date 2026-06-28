# B280 — the 2T higher-spin content: a generation-counting negative + the SU(6)×SU(2) branching

**Status: banked (frontier). Rep theory, FIREWALLED. Nothing to `CLAIMS.md`.** From the Chat-1 handoff
(2026-06-28, section II B-candidates). Verified with GAP (`spin_content_2T_gap.py`) and Weyl-character branching.

## The verified content
2T = SL(2,𝔽₃) (binary tetrahedral, order 24); irrep dims `{1,1,1,2,2,2,3}`. spin-1/2 = the faithful **quaternionic**
2-dim irrep (Frobenius–Schur indicator −1; `2T ⊂ SU(2)=Sp(1)`). spin-j = `Sym^{2j}` of it.

- **spin-1 |₂ₜ = ρ₃** (the 3-dim irrep). Under `ℤ/3 = A₄/V₄`, `ρ₃` splits `3 → 1+1′+1″` (three ℤ/3-charged
  components) — consistent with a three-generation *singlet-sector* bookkeeping.
- **spin-3/2 |₂ₜ = 2 + 2** — two **distinct** 2-dim irreps (`ρ₂′ ⊕ ρ₂″`), each once. **NOT 3 + 1.**

### The negative (the headline)
Because spin-3/2 gives **2+2, not a triplet+singlet**, there is **no** "3 generations (triplet) + 1 Higgs
(singlet)" structure in the 2T spin-3/2. This **kills the "three generations + Higgs from A₄/2T spin-3/2"** reading.
A first-class negative — it removes a tempting but false generation-counting shortcut.

## The branching (Weyl-character verified, `branchings.py`)
`E₆ ⊃ SU(6) × SU(2)`: **`27 = (15,1) + (6̄,2)`** — i.e. as `SU(2)`: `15·(j=0) + 6·(j=½)`. (This is the Chat-2
"27 = 15(j=0)+6(j=½)" decomposition; the `SU(2)` here is the `SU(2)_R` factor of the `E₆ ⊃ SU(6)×SU(2)_R` maximal
subgroup.) Dimension-consistent companions (standard tables, dimensions checked): `27=(3,7)+(6̄,1)` and
`78=(8,1)+(1,14)+(8,7)` under `SU(3)×G₂`; `14=(3,1)+(4,2)+(1,3)` under `SU(2)×SU(2)`. The `E₆⊃F₄` split
(`78=52+26`, `27=26+1`) is already banked (B271, τ = E₆ outer automorphism).

## Scope / firewall
This is **representation theory of 2T and E₆** — no dynamics, no claim that any of these reps are realized as
physical generations or matter. The *kinematic* slot-counting is exact; whether the object selects any of it is the
firewalled physics question (walls #2/#3, the input-required stop-gates). The generation negative is the bankable
content. `spin_content_2T_gap.py` (GAP) · `spin_content_verdict.py` (pyenv) · `tests/test_b280_2T_higher_spin.py`.
