# B27 -- Findings

> Logged observation, not a claim.

## Result

The `SL(3)` Fibonacci trace lift is an exact eight-dimensional polynomial map:

```text
(x1,x2,x3,x4,x5,x6,x7,x8)
  -> (x5, x6, x1, x2,
      x1*x5 - x2*x3 + x8,
      x2*x6 - x1*x4 + x7,
      x3, x4)
```

The formula was verified against direct random `SL(3,R)` matrix substitution.

At the trivial representation `(3,3,3,3,3,3,3,3)`, the Jacobian characteristic
polynomial factors as:

```text
(t - 1)(t + 1)(t^2 - 4t - 1)(t^2 - 3t + 1)(t^2 + t - 1)
```

The eigenvalues are:

```text
phi^3, phi^2, -phi, 1, -1, 1/phi, 1/phi^2, -1/phi^3
```

The `A` quadratic sector `t^2-3t+1` survives inside the `SL(3)` lift. The
half-step sector `t^2+t-1` and a cubic-power sector `t^2-4t-1` also appear.

## Commutator Control

Under one half-step, the two `SL(3)` commutator traces swap:

```text
tr([sigma(a),sigma(b)])      = tr([a,b]^-1)
tr([sigma(a),sigma(b)]^-1)   = tr([a,b])
```

Therefore the unordered pair, and especially the sum
`tr([a,b])+tr([a,b]^-1)`, is preserved; the signed difference is parity-odd.

## Corrected Interpretation

The eight coordinates distinguish traces of elements from traces of inverses,
which collapse in `SL(2)` but not in `SL(3)`. This is a structural
direct/inverse distinction only. The fixed-point linearization decomposes more
cleanly into symmetric and antisymmetric sectors under inverse-trace pairing:

```text
symmetric:      (t - 1)(t + 1)(t^2 - 3t + 1)
antisymmetric:  (t^2 - 4t - 1)(t^2 + t - 1)
```

## Verdict

**`STALLED`**

The `SL(3)` lift enriches the exact golden tower and preserves the `A` sector,
but it does not derive a physical dictionary. Particle/antiparticle language is
not promoted.
