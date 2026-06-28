# B255 — the dimensional filter (verified, firewalled)

**Status: banked observation (frontier). FIREWALLED — simplices / finite groups / McKay / rep theory, NOT physics.
Nothing to `CLAIMS.md`.** From the Chat-1 handoff (2026-06-28, Addendum 2). `dimensional_filter.py` (pyenv).
Connects **B253** (E₆ is the unique exceptional with a complex fundamental).

## The fact
The `d`-simplex has `d+1` vertices and rotation group `A_{d+1}`. The finite subgroups of `SO(3)` are exactly the
cyclic, dihedral, `A₄(=T)`, `S₄(=O)`, `A₅(=I)` groups — so `A_{d+1}` is an `SO(3)` subgroup only for `d∈{2,3,4}`:

| d | simplex rotation group | binary cover | McKay image | complex fundamental? |
|---|---|---|---|---|
| 2 | `A₃ = ℤ₃` (cyclic) | `ℤ₆` | A-type `SU(n)` (classical) | — |
| 3 | `A₄ = T` (tetrahedral) | `2T` | **E₆** | **yes** (the 27) |
| 4 | `A₅ = I` (icosahedral) | `2I` | E₈ | no (248 real) |
| ≥5 | `A_{d+1}` simple | — | none (not in `SO(3)`) | — |

Among the exceptional groups only **E₆** has a complex (non-self-dual) fundamental (**B253**: G₂ 7 real, F₄ 26 real,
E₆ 27 complex, E₇ 56 pseudoreal, E₈ 248 real). Therefore:

> The **tetrahedron (`d=3`)** is the **unique** regular simplex whose rotation group's binary cover
> McKay-corresponds to an **exceptional Lie group with a complex fundamental** — the (firewalled) "chirality-capable"
> end. `d=4` gives E₈ (real); `d≥5` gives no exceptional at all.

This is the same `d=3` that hosts the figure-eight: the tetrahedral shape `e^{iπ/3}` (the regular ideal tetrahedron,
trace field `ℚ(√−3)`) is the hyperbolic-end geometry (B250), and `A₄/V₄ = ℤ₃` is the E₆ center.

## Correction caught
The handoff's `d=2` line ("`ℤ₃ →` double cover `ℤ₆ → A₂ = SU(3)`") is inconsistent — `ℤ₆` McKay is affine `A₅ →
SU(6)`, not `SU(3)`; it skipped the binary cover it used at `d=3,4`. Either reading gives a **classical type-A**
group at `d=2`, never an exceptional, so the **filter core is unaffected** (only `d=3` → exceptional-with-complex-
fundamental). Stated cleanly above without endorsing the `SU(3)` detail.

## Firewall
McKay/ADE are *labels*, not gauge groups. The leap "`d=3` spatial dimensions ⟹ chiral matter is possible" is the
firewalled physics reading (and for any gauge-theory meaning rests on the dead bridge B247). What is **banked** is
the math: *the tetrahedron is the unique simplex selecting an exceptional group with a complex fundamental.* It is a
clean structural companion to B253 and the geometric transition (B248–B250): the same `d=3` arithmetic that puts
`ℚ(√−3)→2T→E₆` at the hyperbolic end also makes E₆ the unique complex-fundamental exceptional.

Anchors: B253 (complex-rep capability of the exceptionals), B248/B249/B250 (the E₆↔E₈ transition; the ideal
tetrahedron `e^{iπ/3}`), B210/B249 (McKay E₆+E₈), B247 (dead bridge — physics reading firewalled). Lit: McKay
correspondence; finite subgroups of `SO(3)`/`SU(2)`; Arnold's trinity.
