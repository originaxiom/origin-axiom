# Probe B15 -- Trace-map invariant controls

> **Speculative frontier work.** Everything here is a logged observation, not a
> claim (`../../GOVERNANCE.md` section 5). Nothing in this directory is promoted
> to `CLAIMS.md`.

## The Question

After B13-B14, the trace-map route suggested several stronger readings:

- the Eisenstein and golden quadratics appear as two endpoints of a diagonal
  linearization family;
- the discrete trace map may be more natural than a naive continuum flow because
  it preserves the Fricke-Vogt invariant exactly;
- the point `(1,1,3/2)` may define a Fibonacci coupling related to `sqrt(5)`;
- different `I`-surfaces may represent different interpretive phases.

This probe separates exact algebra from over-reading.

## Exact Results

For the naive vector-field proxy `V=T-id`, the Jacobian on the diagonal
`(c,c,c)` has characteristic polynomial

```text
(mu+2)(mu^2 + (1-2c)mu + (1-2c)).
```

Its quadratic discriminant is

```text
(2c-1)(2c+3),
```

so the endpoint `c=0` gives the Eisenstein quadratic, `c=1` gives the golden
quadratic, and `c=1/2` gives a double-zero transition. But only `c=0` and `c=1`
are fixed points of the trace map; `c=1/2` is not.

The discrete trace map preserves

```text
I=x^2+y^2+z^2-2xyz-1
```

exactly. The naive continuum proxy `V=T-id` is not tangent to `I=0` at
`(3/2,1,3/2)`, where `dI/dt=-5/4`. This is evidence against the naive continuum
proxy, not a proof that no continuous interpolation can preserve `I`.

## Correction

With the usual Fibonacci trace-map initial line

```text
x=(E-lambda)/2, y=E/2, z=1,
```

the same invariant evaluates to

```text
I=lambda^2/4.
```

Therefore `I=1/4` gives `lambda=1`, not `sqrt(5)`. The `sqrt(5)` result comes
from using the shifted convention `I=lambda^2/4-1`, which is not the invariant
normalization used in this probe. The `sqrt(5)` coupling is not accepted here.

## Verdict

`STALLED` at the dictionary. The number-field endpoint algebra and invariant
preservation are exact. The claims that this proves awareness phases, physical
couplings, or a mandatory discrete ontology do not follow.
