# ADDENDUM to B1330 — the same question asked exactly, on the geometric holonomy

The body of B1330 computes over `F_p` with **brute-forced** `SL(2,F_p)` representations that have a
parabolic meridian. Those are not certified reductions of the geometric holonomy, and that was a real
scope limit on every index scan this bench has run. **This addendum removes it for `s958`.**

## The method

For a manifold tiled by regular ideal tetrahedra the holonomy is conjugate into `SL(2, Q(omega))`
(cusped arithmetic ⇒ the quaternion algebra is `M_2(k)`). SnapPy's basis is not that conjugate, so:
normalise the meridian to standard parabolic form, rescale its translation to 1, then recognise every
entry as `a + b·omega` with `a, b` rational of bounded height.

| manifold | recognised over `Q(omega)` |
|---|---|
| **m004** | **yes** — `rho(a) = [[omega, 1], [-1-omega, -1]]` |
| **s958** | **yes** (denominators of 7) |
| t12833, t12835, v2873 | no, at this precision/height |

**Validated, not assumed:** both of `s958`'s relators `abcaaBBC` and `aacBacbbc` evaluate to exactly
`I` on the recognised matrices. Exact `Q(omega)` arithmetic checked independently
(`omega^3 = 1`, `omega^2 = -1-omega`, `1 + omega + omega^2 = 0`).

## The result

`s958` is chiral, one-cusped, in the `Q(sqrt-3)` class, and carries two order-3 cusp-trivial
characters — Galois-**unprotected**. On its **geometric holonomy**, exactly, no prime:

| `t_0` | sectors | non-zero `I` |
|---|---|---|
| 0 | 6 | 0 |
| 1 | 6 | 0 |
| 2 | 4 | 0 |
| 3 | 4 | 0 |

**20 exact in-domain sectors, 8 of them at `t_0 >= 2`. Every index zero.**

## Two things this settles and one it does not

- **It removes the mod-`p` caveat** for the best-case object. The vanishing is now observed on the
  geometric germ itself, in characteristic zero.
- **It shows mod-`p` under-reaches.** `s958` has **zero** irreducible `SL(2,F_p)` representations with
  parabolic meridian at `p = 7` and `p = 13` (13 776 and 111 384 homomorphisms respectively, none
  qualifying) — the question was *unaskable* there, not answered. Any future scan should use the exact
  route where the manifold admits it.
- **It does not finish the four.** `t12833`, `t12835` and `v2873` are recognised over `Q(omega)` by
  neither route; they remain **named, not computed**.

Reproduce: `verification/qw.py` (exact `Q(omega)`), `verification/exact2.py` (the normalisation and
recognition), `verification/exact_index.py` (the index), `verification/fastreps.py` (the table-driven
`SL(2,p)` enumerator, validated against brute force at 2 688 / 16 464 / 3 696 homomorphisms).
