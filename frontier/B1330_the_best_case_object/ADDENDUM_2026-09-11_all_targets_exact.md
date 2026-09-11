# ADDENDUM 2 to B1330 — the targets computed exactly over Q(zeta_12), and a false positive caught by T5

## The near-miss, first, because it is the useful part

The first exact run reported **NON-ZERO INDEX: 10** on `t12833` and again on `t12835`. Values of
`I = -2, -4, -6`. Taken at face value that is falsifier 6 firing and the chirality bit moving from
withheld to supplied.

**It was wrong, and the record's own banked theorem caught it.**

T5 says `t_0 = 0 ⇒ I = 0` — trivially, since `t_1 = t_0 + t_0* = 0` bounds `r_1 = 0`. The run reported
`t_0 = 0` with `r_1 = 2`. **Impossible.** So the computation was wrong, not the theorem.

**The cause:** these manifolds' geometric holonomy is a **projective (PSL_2) lift** — their relators
evaluate to **`-I`**, not `I`:

```
s958     'abcaaBBC' -> I        'aacBacbbc' -> I            genuine SL(2) representation
t12833   'aaCCbbbacAcb' -> I    'aacAcBBcb' -> -I           projective
t12835   'aaBcbac' -> -I        'aCAbcaCAbcaaaBB' -> -I     projective
```

Fox calculus assumes a genuine homomorphism. On `Sym^m` with `m` **odd**, `-I` acts as `-1`, so the
relator does not act trivially and the cocycle space is meaningless. The tell is exact: **every one of
the ten non-zero sectors carries an odd `Sym` power** — four each at `(1,)`, `(1,1)`, `(1,2)` — and
every even-only germ returned zero.

## The corrected result

Restricting the projective lifts to **even** `Sym` powers, which is the valid computation there:

| manifold | lift | exact sectors | `t_0` reached | `t_0 >= 2` | non-zero `I` |
|---|---|---|---|---|---|
| **s958** | genuine `I` | 18 | 3 | 6 | **0** |
| **t12833** | projective | 16 | 4 | 12 | **0** |
| **t12835** | projective | (even-power run) | — | — | (pending at write time; its odd-power non-zeros are the same artifact) |

All on the **geometric holonomy**, exactly over `Q(zeta_12) = Q(sqrt3, i)`, characteristic zero, on
manifolds that are chiral, one-cusped, in the `Q(sqrt-3)` class, and carrying Galois-unprotected
order-3 twists.

## Method notes worth keeping

- The holonomy is **not** in `SL(2, Q(omega))` in SnapPy's basis. Normalise the meridian to standard
  parabolic form, rescale its translation to 1, then recognise entries by **PSLQ** over `Q(sqrt3)`
  applied separately to real and imaginary parts (`Q(sqrt3,i) = Q(sqrt3) (+) i Q(sqrt3)`).
  `m004`, `s958`, `t12833`, `t12835` all recognise; **`v2873` does not**, at 50 digits.
- `ManifoldHP` supplies the precision; `snap.polished_holonomy` is broken in this build. `SnapPyHP`
  prints exponents as `" E-64"` with a space, which mpmath will not parse.
- **Always print the relator images before trusting a twisted computation.** A `-I` lift silently
  invalidates every odd-weight germ.

## What this costs and what it buys

It does not produce a non-zero index. It **removes the mod-`p` caveat** from three of the four target
manifolds and leaves the vanishing standing on the geometric germ in characteristic zero — now on
`s958` and `t12833` with `t_0` up to 4.

And it is a worked instance of the session's recurring lesson: **an instrument blind to the notation of
its target returns a clean, wrong answer.** Here the notation was the sign of a lift.
