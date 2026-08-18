# B8083 — the positivity bridge: why a cyclic-word invariant settles a conjugacy question

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** untouched.
**Verdict: PROVED** (exhaustive to length 10, with a complete invariant). Reproducer
`positivity_bridge.py`. **Not preregistered**; the falsifier is sharp and stated in advance.

## The gap

The arithmeticity theorem's proof argues on **block sequences**. But the classification it cites
delivers the arithmetic monodromies as those **conjugate** to a power of one of three words, and
conjugacy in `SL(2,ℤ)` is *a priori* coarser than cyclic rotation of a positive `R,L` word:
nothing preserves positivity under `GL(2,ℤ)`, and the paper itself warns that equal trace does not
imply conjugacy (`φ₁³` and `φ₄` both have trace 18 and are not conjugate).

So the step from *"conjugate to a power"* to *"compare block sequences"* needs a bridge, and the
paper states none. Without it, the comparison answers a **coarser question than the one asked**.

## The bridge

> **On positive words, the two relations coincide:** two positive words in `R, L` are conjugate in
> `SL(2,ℤ)` **iff** they are cyclic rotations of one another.

One direction is free — `w = uv` gives `vu = u⁻¹wu`. The other is the content, and it is classical:
the positive `R,L` word of a hyperbolic matrix is its continued-fraction reduction cycle,
equivalently the cutting sequence of its axis on the Farey tessellation, and conjugation only moves
the starting point.

## The check, and why it is a check and not a search

Conjugacy is decided by a **complete invariant**, never by a bounded search for a conjugator: to
`M = [[a,b],[c,d]]` attach the indefinite binary quadratic form `(c, d−a, −b)`, whose proper
`SL(2,ℤ)`-equivalence class is a complete conjugacy invariant (**Latimer–MacDuffee**, which the
paper already invokes elsewhere), and compute its **cycle of reduced forms**.

| | |
|---|---|
| positive words of length 2–10 containing both letters | **2026** |
| cyclic-rotation classes | **241** |
| distinct `(trace, form-cycle)` conjugacy invariants | **241** |
| cyclic classes sharing an invariant | **0** |

**A perfect bijection.** Had any two cyclic classes shared an invariant, the block-sequence
argument would have been unsound as written.

## Controls

- `R^mL^m = φ_m = [[m²+1, m],[m, 1]]` for `m = 1..6`, so the words in play are the paper's
- **`φ₁³` and `φ₄` share trace 18 and have different form-cycles** — reproducing, independently and
  by a different instrument, the non-conjugacy the paper asserts at its own §4

## SCOPE

`SL(2,ℤ)`-conjugacy on **positive words only**, exhaustive to length 10. It says nothing about
non-positive words, and nothing about `GL(2,ℤ)` — whose orientation-reversing elements do not
preserve positivity. The theorem needs no more than this, since every word in play is positive,
but the scope is stated rather than assumed.
