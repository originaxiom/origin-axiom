# B1329 — the index vanishing is not formal; the naive route is closed, and the evidence survives its own bias

**Verdict: OPEN.** The theorem is *not* proved. What is established is where it cannot come from, and
a considerably stronger statement of what is being observed.

## 1. Every identity is formal, and they leave `I` free

All four of B1297's identities follow from the long exact sequence of `(M, dM)`, Poincaré–Lefschetz
duality and `chi(M) = 0`. Writing `rho_k` for the rank of `H^k(M;V) -> H^k(T;V)`:

```
h^k(M,dM;V) = (t_{k-1} - rho_{k-1}) + (a_k - rho_k)      (exactness)
h^k(M,dM;V) = a_{3-k}*                                    (Poincare-Lefschetz + UCT)
a_0 - a_1 + a_2 = 0                                       (chi(M) = 0, a_3 = 0)
```

which give `rho_0 = a_0`, `a_0* = t_2 - rho_2`, and

> `a_1 - a_1* = (a_0 - a_0*) + r_1 - t_0`   — B1297's `F`.

**`r_1 + r_1* = t_1` is also a consequence**, not an extra input: run the same computation for `V*`
and subtract. So the identities are complete and **they do not constrain `I`**. No rearrangement of
them proves the vanishing.

## 2. The classical argument provably does not extend

Half-lives-half-dies for **self-dual** `W` works because the cup product of two restricted classes is
evaluated through

```
H^2(M;C) -> H^2(T;C) = C ,
```

and that map is **zero**, since it factors through `H^3(M,dM;C) = H_0(M;C)* = C`.

For `V = W (x) chi` with `chi` of order 3 the product lands in `H^2(M;chi^2)`, and there

```
H^3(M,dM;chi^2) = H_0(M;chi^2)* = 0      (coinvariants of a non-trivial rank-1 system vanish)
```

so `H^2(M;chi^2) -> H^2(T;C)` is **surjective**, not zero. **The isotropy argument fails exactly where
the twist is non-trivial** — which is the only place the index can be non-zero at all.

## 3. A bias in this bench's own scan, found and removed

The earlier scan used a **single** `Sym^m` germ. That has `t_0 = 1`, `t_1 = 2`, so `L_V` is a **line in
a 2-dimensional space** and `I != 0` would need `r_1 = 0` or `2` — the restriction zero or onto, both
extremes. **The scan was structurally disposed toward the answer it found.**

The realistic object is a **sum**: `27` restricted to an `sl2` germ is `(+) Sym^{n_i}`, with
`t_0 = #summands`. Re-run on sums `(1,1), (1,2), (2,2), (1,1,1), (1,2,3)`:

| `t_0` | sectors | non-zero `I` |
|---|---|---|
| 2 | 488 | **0** |
| 3 | 208 | **0** |

At `t_0 = 3` a 3-plane sits in a 6-dimensional space and half-dimensionality is a real condition, not
an accident of rank. The result survives the harder test. The earlier 9 108 are also **63% non-vacuous**
(`t_0 = 1`, not `0`), so T5 does not account for them either.

## 4. The sharp statement

> **`r_1 = t_0`** — the restriction image is exactly half-dimensional, even for non-self-dual `V`.
> Equivalently (in D) `a_1 = a_1*`.

And it is **not** the weaker "`a_1 = t_0` with the restriction injective": **32 sectors carry
`a_1 = 2 > t_0 = 1`** with a one-dimensional kernel, and `r_1 = 1` regardless.

| `t_0` | `a_1` | `r_1` | `I` | count |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 264 |
| 1 | 1 | 1 | 0 | 198 |
| **1** | **2** | **1** | **0** | **32** |
| 2 | 2 | 2 | 0 | 108 |
| 3 | 3 | 3 | 0 | 108 |

## 5. A caution for whoever proves it

`Sym^m` carries a **symmetric** invariant form for `m` even and an **alternating** one for `m` odd.
Against the alternating cup product on `H^1` of a torus, the induced pairing on `H^1(T;W)` therefore
**changes parity with `m`** — so "Lagrangian" is the correct word for only one parity, and a proof
phrased as "the image is Lagrangian" must say which.

`V` is genuinely non-self-dual throughout: `V = W (x) chi ≅ W (x) chi^{-1}` would force `chi` trivial
for irreducible `W`. No accidental self-duality is doing the work.

Reproduce: `verification/sums.py` (the summed-germ scan), `verification/structprobe.py` (the
`(t_0, a_1, r_1)` table), `verification/t0check.py` (the non-vacuity check).
