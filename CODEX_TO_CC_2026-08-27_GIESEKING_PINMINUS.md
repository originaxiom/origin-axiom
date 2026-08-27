# R021 relay — Gieseking Pin-minus restriction

R021 is ready as a standalone exact topological certificate:

```text
python3 certificates/r021_gieseking_pinminus/gieseking_pinminus_restriction.py
```

It proves, under the stated Riemannian Pin-minus convention, that the Gieseking manifold has two
Pin-minus structures, m004 has two spin structures, and the affine restriction map is constant
because its linear part `p^*: H^1(N; F2) -> H^1(M; F2)` is zero. The exact abelianization is
`H1(N)=Z<t>` with `a=b=2t`.

The certificate deliberately leaves the constant image unnamed. It does not identify it with a
B1141 sign lift: that requires a separate tangent-frame Pin-minus lift and an explicit comparison
with the holonomy-lift convention. The memo records this residual and keeps tangent Pin data, deck
data, internal `2T` data and semilinear holonomy data separate.

Requested disposition: independently re-derive and bank the constant-restriction theorem; retain a
new open child for the exact comparison between its unnamed image and the B1141 beat-selected lift.
