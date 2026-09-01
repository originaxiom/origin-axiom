# R037 — A6 does not preserve the 2T quotient menu: one of two classes extends

Source state: `origin/main@a5138424` (B1234). Verdict: **exact finite-group and
covering-group theorem**. It replaces B1234's equality-of-counts reading with
the map-level result.

## The result

Let

```text
G = pi_1(m000),
H = ker(w_1) = pi_1(m004),
Q = SL(2,3) = 2T.
```

B1234 computed `48` surjections from each of `G` and `H` to `Q`. Equality of
those totals does not mean the quotient data pass unchanged through the
orientation cover. R037 constructs the index-two subgroup explicitly and
restricts every map:

```text
Surj(G,Q):                 48 maps = 2 Aut(Q)-orbits,
Surj(H,Q):                 48 maps = 2 Aut(Q)-orbits,
distinct restricted maps: 24 maps = 1 Aut(Q)-orbit,
restriction fibres:        24 fibres, each of size 2.
```

Thus **exactly one of m004's two `2T` quotient classes extends over the
Gieseking parent**. Both quotient classes of `m000` restrict to that same one;
the other m004 class is the unique nonzero central `H^1(m004;C2)` twist and
does not extend.

## Why restriction stays surjective

For a surjection `phi:G -> Q`, `phi(H)` is normal in `Q`, and
`Q/phi(H)` is a quotient of `G/H = C2`. The certificate independently computes

```text
Q_ab = C3,
```

so `Q` has no quotient of order two. Therefore `phi(H)=Q`: every restricted
map remains surjective.

## Why every fibre has size two

Let `z=-I` generate `Z(Q)=C2`, and let `w:G->C2` be the orientation
character. The central twist

```text
phi^w(g) = z^{w(g)} phi(g)
```

is a distinct extension with the same restriction to `H`. Conversely, if two
extensions agree on `H`, compare their values on an odd coset representative
`t`. Compatibility with conjugation by `t` says their ratio centralizes
`phi(H)=Q`; hence the ratio is in `Z(Q)={1,z}`. These are the only two
extensions.

Since `|Aut(Q)|=24` and postcomposition acts freely on surjections, every
quotient-class orbit has size 24. The 24-map restriction image is invariant
under `Aut(Q)`, hence it is exactly one of m004's two orbits. The exhaustive
matrix computation also shows that the nonzero central character of the m004
presentation exchanges the extendable and nonextendable orbits.

## Explicit cover map

Use the B1234/SnapPy presentations

```text
G = <a,b | a^2 b^2 a^-1 b^-1>,
M = <c,d | c^3 d c^-1 d^-2 c^-1 d>.
```

The unique nonzero mod-two character of `G` has `w(a)=w(b)=1`.
Reidemeister--Schreier with transversal `{1,a}` gives

```text
u=b a^-1,  v=a^2,  w=a b,
H=<u,v,w | v u w v^-1 u^-1, v w u w^-1>.
```

The Tietze conversion to `M` is

```text
c=w^-1, d=w u^-1,
u=d^-1 c^-1, v=d c, w=c^-1.
```

R037 exhausts all matrices in `SL(2,3)`, verifies all three presentations have
the stated target maps, checks the mutually inverse conversion on every map,
and then computes restriction and automorphism orbits. Stable SHA-256 digests
lock all three finite sets.

## What changes in the chain

B1234's `48=48` hid a selector. If the nonorientable parent is treated as the
pre-A6 object, it selects one of the two abstract `2T` quotient classes seen by
the oriented observer. This is a genuine discrete inheritance theorem—not an
identification made from matching counts.

There is a striking parallel with B1208/R021: exactly one of m004's two spin
structures extends over the Gieseking parent. **R037 does not identify the two
two-element menus or their selected elements.** Such an equality would itself
require an exhibited acting map under the identification discipline.

Nor does this pay I-6. McKay maps an abstract `2T` representation graph to the
affine E6 diagram; R037 does not identify the manifold quotient with a physical
transverse ALE group, create a physical `E6` gauge sector, or derive spin,
chirality, generations, dynamics, or values.

## Reproduce

```text
python3 certificates/r037_a6_2t_restriction/a6_2t_restriction.py
```

The certificate uses only the Python standard library and runs from any cwd.
