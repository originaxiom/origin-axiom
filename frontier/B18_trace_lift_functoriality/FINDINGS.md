# B18 -- Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` section 5).

## Result

The trace map is canonical for the half-step. Starting from the automorphism

```text
phi_F(a)=ab,  phi_F(b)=a,
```

the full-trace map is

```text
(X,Y,Z) -> (Z, X, XZ - Y).
```

The half-trace convention gives

```text
(x,y,z) -> (z, x, 2xz - y).
```

The Fricke-Vogt invariant is preserved exactly. The square of this trace map is
the `A=F^2` trace lift; at `(1,1,1)` its Jacobian has characteristic polynomial

```text
(t-1)(t^2-7t+1),
```

so the half-step parity `-1` resolves to `+1` at the `A` level.

## What This Gates

B20-B24 are allowed to run because the trace map is not an accidental matching
calculation. It is the functorial trace lift of the half-step. However, this
does not produce spacetime, matter, gravity, awareness, or anyon phases.

## Verdict

**`STALLED`**

The canonical trace-lift gate passes; the physical/semantic dictionary is still
not derived.
