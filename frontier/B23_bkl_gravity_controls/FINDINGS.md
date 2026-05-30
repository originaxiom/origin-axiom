# B23 -- Findings

> Logged observation, not a claim.

## Result

The perturbation expansion of the trace map at `(1,1,1)` is exact:

```text
(u,v,w) -> (w, u, 2u - v + 2w + 2uw).
```

The only nonlinear term is `2uw`. This is a useful structural target for any
BKL comparison, but it is not an equation-level match by itself.

No explicit dictionary from `(u,v,w)` to Misner variables `(beta_+, beta_-,Omega)`
or to Kasner/BKL variables is derived here.

## Verdict

**`STALLED`**

The nonlinear term is isolated; the gravity dictionary is missing.
