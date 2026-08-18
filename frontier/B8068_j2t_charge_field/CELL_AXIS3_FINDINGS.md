# B8068 AXIS 3 — reality: so(10) is real in EVERY inner form; su(5) in none

**Date:** 2026-08-17 · **Seat:** cc3 · **Gate 5:** algebra only.

## THE RESULT

Conjugation for a real form is `τ_θ = θ ∘ τ_compact`. The **inner** θ are exactly the 63
nontrivial sign-gradings of the `E₆` root system (all verified in this session to fix the
full Cartan). `τ` sends `e_r → −e_{−r}` with coefficient conjugation `√−3 → −√−3`, hence
maps the **27 to the 27-bar** — gated and confirmed.

Sweeping **all 63 inner real forms × both pure spinors = 126 cases**:

| | result |
|---|---|
| `Stab(s) ∩ Stab(τ_θ s)` | **dim 45, reductive 45 = so(10)** — in **126 of 126** |

> **so(10) is real in every inner real form of `E₆`. `su(5)` is real in none of them.**

The uniformity is the content. `so(10)` is not real in some form the object happens to
prefer — it survives **every** inner conjugation. And `so(10)` is `D₅`, `n` odd, so
`−1 ∉ W(D₅)`: the **16** and **16-bar** are distinct. **Chirality is real too.**

## WHAT THIS MEANS FOR THE CHAIN

`su(5)` exists over `ℂ` and composes in one annihilator (`dim 34`, Killing rank 24,
cell 11). But the descent `SO(10) → SU(5)` is **not defined over ℝ** in any inner form:
the conjugation always pulls it back to `so(10)`.

So the object supports an **SO(10) structure with chiral matter, real** — and does not
support its real breaking to `SU(5)` by this route.

## THE CLASS THIS NEGATIVE COVERS — per THE RULE

Covered: **inner** involutions, i.e. inner real forms, exhaustively (63 of 63).

**Outside it:** the **outer** involutions — the `τ`-composite conjugations. `B907` swept
"all 128 frame-diagonal inner **and τ-composite outer** involution representatives" and
found this object's first measurement wall real in `e₆(2)` **and only there**. The outer
half is untested here.

**Caution, recorded in advance:** `B959` showed the outer route makes the 27 self-dual on
`Fix(τ)`, killing chirality. That is a statement about a *subalgebra*, not about a real
form defined by a `τ`-composite conjugation — a different object — but it is the obvious
place for the outer branch to fail, and it should be checked rather than assumed either way.

## GATES

| gate | result |
|---|---|
| su(5) control (generic `27 × 27-bar` → Killing rank 24) | **PASS**, in-process |
| Casimir multiplicities on the 27 | **{1, 10, 16}** |
| every 27-root negates into the 27-bar block | **True** |
| Φ·Ψ = W mod p | **PASS** |
| all 63 gradings enumerated | 63, none skipped |

## RUN

```
python3 cell16_reality.py 1093      # the compact form alone
python3 cell18_realforms.py 1093    # all 63 inner forms
```
