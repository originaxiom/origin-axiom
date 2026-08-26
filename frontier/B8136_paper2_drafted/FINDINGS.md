# B8136 — Paper II is drafted — a finite spectrum on an infinite lattice, and C is forced

**Date:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical identification; no Standard-Model quantity appears.

## What was done

Drafted **Paper II**: `papers/series/paper2_rung_spectrum/` — 8pp, clean build. **B8078's reproducer
was re-run to completion (exit 0, ALL CHECKS PASS) before any drafting.**

## The result

`dim z(S)` on the infinite subspace lattice of `C ⊂ e₆` is the **flat-function of an arrangement of
30 hyperplanes in a 4-space**:

    dim z(S) = 12 + Σ { m_λ : λ|_S = 0 }

so an infinite lattice has a **finite** image — **109 flats, eleven values, every one attained**,
where a prior sample (16 coordinate subspaces + 440 random rational directions) had returned only
`{12, 30, 78}`. The eight missing values sit on proper subvarieties. The extreme case is **46**,
which on its plane occurs exactly at the roots of an **irreducible** rational cubic and is therefore
**arithmetically inaccessible over ℚ**, not merely rare.

## New over B8078: the subalgebra is forced

`D(2T) ∩ E = {8, 14, 16, 22}` exactly, where `D(2T)` are the degrees of `2T`-invariant binary forms
and `E` the principal-`sl₂` summand degrees of `e₆`. Each surviving degree is realised by a
**unique** monomial (`Φ`, `tΦ`, `Φ²`, `tΦ²`); the degree-12 generator never appears. **The McKay
partner is load-bearing:** `D(2O) ∩ E = {8,16}` and `D(2I) ∩ E = ∅`.

## Correction recorded

**I drafted the entire paper calling `t` and `Φ` binary OCTAHEDRAL invariants.** `2O`'s generator
degrees are 8, 12, 18; the degrees actually in use — 6, 8, 12 — are **`2T`**, the binary tetrahedral
group, **which is exactly `E₆`'s McKay partner**. Caught while testing whether the exponent choice
was forced; the degree arithmetic only closes for the 6,8,12 generator set. **The correction made
the paper stronger, not weaker.** Verified afterwards by explicit invariance of `t` and `Φ` under
both `2T` generators, with a control that a non-invariant degree-8 form is rejected.

## SCOPE

- **Exact over ℚ:** `dim z(C) = 12`; the decomposition and that `C` acts as *literally zero* on
  `z(C)`; the three weight orbits; the master formula; the plane cubic and that it generates `K`;
  the forcing proposition.
- **Three faithful primes only** (409, 421, 487): the 109 flats and the eleven values. Mod-`p`
  reduction can only *add* dependencies, so a flat could be coarser than its `ℚ̄` counterpart. **The
  `ℚ̄` flat lattice is REGISTERED AS OPEN, not claimed.**
- **Assumed, not established:** the principal `sl₂` placement — `OA-C0006`, **CONDITIONAL**, and the
  paper says so.

**Gate 5 untouched.** Every dimension is a dimension of a centraliser and nothing else.
