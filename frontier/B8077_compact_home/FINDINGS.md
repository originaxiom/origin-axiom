# B8077 — the cascade's endpoint has a COMPACT home in the object's own real form

**Date:** 2026-08-18 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical
identification; "compact" here is a statement about a Killing form and nothing else.

**Verdict: PROVED.** Reproducer `compact_home.py`, exact over ℚ, exhaustive over the 64 inner
characters. All controls pass.

## Why it matters, stated once

A gauge algebra must be **compact** — unitarity and a positive-definite kinetic term force it. So
reaching `su(3)⊕su(2)⊕u(1)` **over ℂ is not enough**; the compact real form is the requirement.
The reality question has been treated across the corpus as the thing standing between the cascade
and physics. This settles the part of it that is decidable by computation.

## The result

**(a) The object's charge algebra `C` is θ-stable in exactly 4 of 64 characters** — 1 compact
form and **3 copies of `e₆(2)`**.

**B907 sealed `e₆(2)` for the wall by a completely different route** (128 swept involutions,
τ-twisted alignments, fixed dimension 38 = `su(6)⊕su(2)`). This arrives at `e₆(2)` from the
**charge** side, over ℚ. **Two independent methods, one real form.**

**(b) The Standard Model gauge algebra is compact in `e₆(2)` — 36 of 36 characters.**
`k = su(6)⊕su(2)` has root system `A5+A1`, and `A5 ⊃ A2` by deleting nodes, so an `A2+A1`
subsystem sits inside `k`: **8 roots + 4 Cartan = 12**, exactly `su(3)⊕su(2)⊕u(1)`.

**(c) B892's second-measurement endpoint is compact too.** The *same* 8 roots with the *full*
rank-6 Cartan give **8 + 6 = 14** — precisely `su(3)⊕su(2)⊕u(1)³`, B892's `z(x₁,y*)`. Inside `k`
in **36 of 36** `e₆(2)` characters, and 27 of 27 in `e₆(−14)`.

**(d) The cascade's own chain has a compact home as well.** Two characters give
`k = so(10)⊕u(1)` (dim 46, derived 45), so `so(10) ⊃ su(5) ⊃ su(3)⊕su(2)⊕u(1)` is a chain of
**compact** subalgebras in `e₆(−14)` — the banked cascade E₆ → SO(10)×U(1) → SU(5)×U(1) → SM
(B861, B863, B994) sitting inside a maximal compact.

## The reading

> **Both sides of the remaining step are compact and real.** The 14-dimensional endpoint and the
> 12-dimensional SM algebra each sit inside the maximal compact of the object's own real form.
> What lies between them is the single step **14 → 12** — dropping two of the three `u(1)`s, the
> rank-6 → rank-4 drop — which is exactly the one row B1017's resource table marks **UNSOURCED:
> the VEV direction**.

So reality is **not** the obstruction it has been read as. The obstruction is one *direction*, and
B990 already names the only two ways past an orbit-to-point gap: shrink the group (ℚ → ℤ, a
class-number question) or add non-invariant structure.

## Controls

- the inner census reproduces **B907's sealed sweep — 78×1, 46×27, 38×36 — without being given
  it**; if a fourth value appeared the involution construction would be wrong
- `C` abelian: all six pairwise brackets vanish
- the charge degrees rebuild at 8/14/16/22 from the 2T-invariant forms
- dimensions are **counted** (roots + Cartan), never asserted

## SCOPE — what this does not establish

- **Inner forms only.** The outer real forms `e₆(6)` and `e₆(−26)` are **not swept**.
- **Existence, not occupancy.** This shows a compact home **exists** for the endpoint in the
  object's own real form. It does **not** show the object's *specific* SM-shaped subalgebra **is**
  that one — that is a matching problem between the θ-eigenstructure of `C` and the `A2+A1`
  subsystem inside `k`, and it is open.
- **Nothing about the 14-locus's own reality.** B892 computed `a² < 0`, so `y*` is not a real
  point; that stands and is untouched here. What is shown is that an algebra *of that type* is
  compact in the form, not that B892's particular point is real.
- No values, no scale, no physical identification.
