# B8071 — the reality gate: the compact rank-4 algebra exists in e₆(2), on the orbit the object does not reach

**Date:** 2026-08-17. **Status:** positive, controlled, firewalled. Criteria sealed in
`PREREG_reality_gate.md` before the compute. Reproducer `reality_gate.py`, exact over ℚ, all
controls pass. **Nothing promotes to `CLAIMS.md`.** No physical identification (Gate 5).

## What was blocking

Two panels closed this week and both stopped on the same wall: **mod-`p` Killing rank is identical
for every real form of a given complex algebra.** `su(5)`, `su(4,1)`, `su(3,2)` and `sl(5,ℝ)` all
read `(24, 24)`. The su(5) panel named this as its own falsifier 5. The nilpotent panel named it as
"the live gate".

## The method

A real form is named by `dim k`, the dimension of its maximal compact subalgebra — an exact
integer, no floating-point signature. For a `θ`-stable complex subalgebra `c`, the induced real
form has maximal compact `c ∩ k`, so `dim(c ∩ k_ℂ)` names it. Inner involutions are the 64 sign
characters on the root lattice, `dim k = 6 + #{r : ε(r) = +1}`.

## Controls — every one aimed at the reported number

- **C1** the 64-character census gives `dim k ∈ {78, 46, 38}` and nothing else — **compact,
  e₆(−14), e₆(2)** — with counts **78×1, 46×27, 38×36**, independently reproducing B907's sealed
  inner sweep without being given it.
- **C2** `θ[x,y] = [θx, θy]` verified on 300 random basis pairs, 0 failures.
- **C3** orbits identified by **centraliser dimension against Bala–Carter**, not by name:
  `2A1 → dim z = 46`, `A2 → dim z = 36`; reductive parts `z(e,h,f)` = **22** and **16**.
- **C4** `ad(e)` verified nilpotent (`ad³ = 0` and `ad⁵ = 0` respectively).
- **C5** `dim(z_red ∩ k)` **varies** across characters — the instrument is not constant.

## The result

**Orbit A2, reductive centraliser `su(3)⊕su(3)` (dim 16, rank 4):**

| ambient real form | `dim(z_red ∩ k)` | centraliser real form | characters |
|---|---|---|---|
| **e₆(2)** | **16** | **`su(3)⊕su(3)` COMPACT** | **3** |
| e₆(2) | 12 | `su(3)⊕su(2,1)` | 6 |
| e₆(2) | 8 | `su(2,1)⊕su(2,1)` | 27 |
| e₆(−14) | 12 | `su(3)⊕su(2,1)` | 18 |
| e₆(−14) | 8 | `su(2,1)⊕su(2,1)` | 9 |

**Orbit 2A1, reductive centraliser `so(7)⊕u(1)` (dim 22, rank 4):**

| ambient real form | `dim(z_red ∩ k)` | centraliser real form | characters |
|---|---|---|---|
| e₆(2) | 16 / 12 / 10 | `so(6,1)` / `so(5,2)` / `so(4,3)` `⊕u(1)` | 2 / 6 / 28 |
| e₆(−14) | **22** | **`so(7)⊕u(1)` COMPACT** | 3 |
| e₆(−14) | 16 / 12 / 10 | `so(6,1)` / `so(5,2)` / `so(4,3)` `⊕u(1)` | 2 / 6 / 16 |

## The reading, stated exactly

**In e₆(2) — the form B907 sealed as the object's, and only there among the inner forms — a
compact rank-4 reductive centraliser exists: `su(3)⊕su(3)`, at 3 of 64 characters.** That is a
gaugeable algebra of the right rank, in the object's own real form.

**It sits on orbit `A2`. The nilpotent panel establishes that the object reaches `2A1`, not `A2`.**
And in `e₆(2)` the `2A1` centraliser is **never** compact — `so(6,1)`, `so(5,2)`, `so(4,3)` only.
The two facts compose into one sentence:

> The compact, gaugeable, rank-4 algebra is present in the object's real form, and it is on the
> one orbit no tested route reaches.

**The gap is now a single named step: `2A1 → A2`.** That is a sharper statement than the
programme has had, and it is falsifiable — exhibit a route from the object to `A2`, or prove none
exists.

Independently worth recording: **compact `su(3)⊕su(3)`, dim 16, is exactly Baez–Schwahn's
`Stab(B)₀ ≅ (SU(3)×SU(3))/ℤ₃`**, and B8068's `cell30` already found `(16,16)` inside `f₄` at 9 of
9555 charge directions. Three routes now point at the same 16-dimensional object.

## ADDENDUM — the conditional is DISCHARGED (`orbit_meets.py`, same day)

By Kostant–Sekiguchi, real nilpotent `G_ℝ`-orbits in `g_ℝ` correspond to `K_ℂ`-orbits on
nilpotents of `p_ℂ`, with corresponding orbits lying in the **same complex orbit**. So the complex
orbit `O` meets `g_ℝ` iff some nilpotent of `p_ℂ` lies in `O`. With `θ = θ_ε` diagonal,
`p_ℂ = span{e_r : ε(r) = −1}` — and since `ε(−r) = ε(r)`, `p_ℂ` is spanned by full root *pairs*
and **does** contain semisimple elements, so nilpotency is checked, never assumed.

| ambient form | `A2` meets `p_ℂ` | `2A1` meets `p_ℂ` | characters |
|---|---|---|---|
| compact `e₆(−78)` | **False** | **False** | 1 |
| `e₆(−14)` | True | True | 27 |
| **`e₆(2)`** | **True** | **True** | **36 of 36** |

**The compact row is the method validating itself:** a compact real form contains no nonzero
nilpotent, and the computation returns `False`/`False` there without being told to. Had it
returned `True`, the method would have been broken.

**`A2` has real points in `e₆(2)` at every one of its 36 characters.** The 3 characters carrying a
compact `su(3)⊕su(3)` are therefore among them, and B8071's headline is no longer conditional:

> **In `e₆(2)` — the object's sealed real form — there is a real nilpotent in orbit `A2` whose
> reductive centraliser is compact `su(3)⊕su(3)`: rank 4, dimension 16, gaugeable.**

What remains is the single step already named: **the object reaches `2A1`, not `A2`.** And in
`e₆(2)` the `2A1` centraliser is never compact.

## The scope limit, and the row that proves it bites

This cell computes **which real forms of the centraliser are compatible with each involution**. It
does **not** verify that the nilpotent `e` itself has real points in that form. **The compact-e₆
row is the proof that this matters: a compact real form contains no nonzero nilpotent at all**
(every element of a compact algebra is semisimple), so that row is vacuous by construction. It is
left in the table as a visible marker of the gate rather than deleted.

Whether the `A2` orbit has real points in `e₆(2)` specifically is therefore the **next**
computation, not something established here. Until it is run, the headline is conditional:
*if* `A2` meets `e₆(2)`, its compact centraliser is available at 3 characters.

**Also not established:** the object's own `B = A ∩ τ(A)` is still only known mod `p`. Rebuilding
it over `ℚ(√−3)` in characteristic zero — and reading `dim(B ∩ k)` against the table
`su(5)/su(4,1)/su(3,2)/sl(5,ℝ) = 24/16/12/10` — is a separate cell and is **not** claimed here.
No scale, no value; the scale-torsor theorem stands.
