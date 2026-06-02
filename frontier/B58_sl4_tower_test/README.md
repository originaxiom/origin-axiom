# B58 -- SL(4) Factor-Count Tower Test (attempt)

## Question

Does the SL(n) factor-count tower prediction (PC12 `DRAFT_NOTE_SKELETON.md`,
"Open Prediction") hold at `n=4`? Predicted: at the identity representation, the
rank-two `SL(4,C)` Jacobian factors into a parity block + **7** degree-2
`char(M^k)` factors (total degree 15).

## Status

```text
FRONTIER ATTEMPT
PC12 SUPPORT
NO CLAIM PROMOTION
```

## Run

```bash
python frontier/B58_sl4_tower_test/probe.py
```

## What It Establishes (rigorously)

```text
(1) SL(4) identity forward recursion tau_k = 4 tau_{k-1} - 6 tau_{k-2}
    + 4 tau_{k-3} - tau_{k-4} has characteristic polynomial (r-1)^4
    => derivative sequences are CUBIC in k (SL(3) was (r-1)^3 / quadratic;
       derivative-polynomial degree = n-1).
(2) the fixed-line point (all traces = n) is the IDENTITY representation, where
    the representation->trace map is first-order degenerate (d tr(W) = 0; traces
    are second-order). Demonstrated numerically.
```

## Why The Prediction Is Not Tested Here

The object that factors into `char(M^k)` for SL(3) (B54/B55) is the **ambient
trace-map Jacobian** at the fixed line -- a polynomial self-map of the trace
coordinates, not a linearization of matrix representations. Because every
representation realizing the fixed-line point is the degenerate identity, a
**representation-based numerical Jacobian cannot recover it** (confirmed in (2)).

The B55-style ambient construction requires:

```text
- the explicit minimal generating set of 15 trace coordinates for the SL(4,C)
  character variety of F_2 (Procesi / second fundamental theorem for SL(4));
- the substitution's action (A,B) -> (AB,A) on all 15 coordinates via the SL(4)
  trace identities (reduction of tr(word(AB,A)) to polynomials in the 15 coords).
```

That construction is **not built here** (it is a substantial trace-identity
computation). The forward-chain recursion alone gives only part of the
coordinate set and does not assemble the full `15 x 15` Jacobian.

## Verdict

`NEEDS-EXPERTISE` -- the 7-factor prediction is **untested** (neither confirmed
nor refuted). The mechanism (step (1)) and the obstruction (step (2)) are
established. The prediction remains recorded as a prediction in PC12; building
the SL(4,C) ambient trace map is the required next step (a real future probe).
