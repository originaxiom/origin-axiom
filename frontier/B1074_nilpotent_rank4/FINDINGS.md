# B1074 — the rank ceiling's hypothesis is load-bearing: nilpotent centralisers reach rank 4

**Date:** 2026-08-17 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical
identification anywhere in this arc; every statement is about `e₆`, its Levi subalgebras, its
nilpotent orbits and the `27` as a representation.

**Verdict: PROVED.** Criteria sealed in `PREREGISTRATION.md` before the first run. Reproducer
`nilpotent_rank4.py`, exact over ℚ, all controls pass.

## What was open

`docs/GUT_REQUIREMENTS_LEDGER.md` §D states the rank obstruction as **"a theorem, not an
estimate"**: *"the centralizer of a set of **semisimple** elements contains a maximal torus, hence
has full rank … therefore every measurement in the cascade is rank-preserving, and no number of
them can ever reach rank 4."* It has been cited to explain why four sealed crossings failed.

**No arc in the bank had tested the word "semisimple."**

## Part 1 — the hypothesis is load-bearing

`ad(h)` for `h` in the Cartan is diagonal in the root basis with eigenvalues `α(h)`, so it is
nilpotent iff every eigenvalue vanishes. Computed exactly over all `4⁶−1 = 4095` integer Cartan
points: **0 nonzero Cartan elements have `ad` nilpotent.**

Therefore: if a maximal torus `T` lay in `Z_G(x)` then `x ∈ z_g(T)` = the Cartan, which contains no
nonzero nilpotent. **So for every nonzero nilpotent `x`, `Z_G(x)` contains no maximal torus, and
`rank(Z_G(x)) ≤ 5`.** The nilpotent class was never inside §D's argument.

**Control — §D is true on its own class**, verified rather than assumed: every torus element's
centraliser contains the full Cartan, **400/400** sampled. The wall is real on semisimple
elements, which is what makes the nilpotent exit meaningful.

## Part 2 — which orbits reach rank 4, exhaustively

For any `x`, a maximal torus of `Z_G(x)` is `Z(L)°` for `L` the minimal Levi containing `x`, so
`rank(Z_G(x)) = 6 − rank_ss(L)`. Every Levi is conjugate to one of the **64 standard** ones — a
finite, exhaustive check, no sampling.

| `rank(Z)` | `27` self-dual? | standard Levis |
|---|---|---|
| 6 | False | 1 |
| 5 | False | 6 |
| **4** | **False** | **15** |
| 3 | False | 20 |
| 2 | True / False | 1 / 14 |
| 1 | True / False | 2 / 4 |
| 0 | True | 1 |

**Rank 4 occurs at exactly 15 standard Levis — 5 of type `A2`, 10 of type `2A1`** — and on
**every one of them the `27` is non-self-dual**, i.e. stays complex. Self-duality first appears
only at rank ≤ 2. Self-duality is computed from the weight multiset (`wt(M*) = −wt(M)`) restricted
to `Z(L)°`, not inferred from a name.

**Controls:** Bala–Carter agreement — the representatives give `dim z(e) = 36` (`A2`) and `46`
(`2A1`), matching the published tables, with `ad(e)` verified nilpotent · non-genericity — rank 4
is reached by 15 of 64, not all.

## The reading, and its limits

> §D is **true as written**. Its hypothesis names semisimple elements, and that word is
> load-bearing. Rank 4 *is* reached — by nilpotent centralisers, at exactly the Levi types `A2`
> and `2A1` — and on both the `27` remains complex.

**SCOPE. This is a scope note on §D, not a refutation.** §D's own sentence already says it is about
what *measurement alone* cannot do, and it names the remedy (a VEV, a Wilson line, an orbifold
projection). What this arc adds is that the **nilpotent-centraliser class is a fourth route its
argument does not cover**, and that the class is non-empty and chirality-preserving.

**Not established here:**
- **That the object reaches either orbit.** The ω-covariant purity reading that would place it on
  `2A1` is mod-`p` work in `frontier/B1068_j2t_charge_field/` and is **owed**, not claimed.
- **Which real forms** these orbits and centralisers admit — that is
  `frontier/B1071_reality_gate/`, a separate arc.
- Anything about generations, values, or scale.
