# PC11 External Review Brief

Status: review brief. This is a compact handoff for a mathematical reviewer.
It does not add claims.

## What To Review

PC11 is a computational/literature bridge around the trace-map branch:

```text
conditional uniqueness core
  -> exchange / half-step F=LP, F^2=A
  -> functorial trace lift of F
  -> A-sector inside the trace-map linearization
  -> projective quotient and tangent return
  -> T1 -> S1 -> I=1/4 -> lambda/h=1
```

The review target is not a physics theory and not a new Fibonacci Hamiltonian
theorem. It is a bounded question: whether **T1** is mathematically natural or
inserted.

## Minimal Reading Set

Read in this order:

```text
papers/candidates/PC11_trace_map_spectrum_bridge/PAPER_CARD.md
docs/TRACE_SELECTOR_THEOREM.md
frontier/B18_trace_lift_functoriality/FINDINGS.md
frontier/B25_fibonacci_spectrum_anchor/FINDINGS.md
frontier/B26_lambda1_derivation_attempt/FINDINGS.md
frontier/B38_tangent_return_arithmetic_filter/FINDINGS.md
frontier/B40_filter_reuse_audit/FINDINGS.md
frontier/B47_s1_verdict_ledger/FINDINGS.md
papers/candidates/PC11_trace_map_spectrum_bridge/REVIEW_PACKET.md
```

## Main Checks Requested

Please check:

```text
Is the Fibonacci trace map correctly framed as the half-step trace lift?
Is the A-sector inside the trace-lift Jacobian stated with the right caveats?
Is the central-sign / PSL projective quotient legitimate here?
Is the tangent return quadratic q(t)=t^2-(4I+2)t+1 derived correctly?
Is T1 a standard naturality/filter-inheritance principle, or an added axiom?
Is lambda/h=1 correctly labeled conditional on T1 rather than proven?
Are the Fibonacci Hamiltonian facts presented as known mathematics?
```

## Core Conditional Step To Audit

The selector calculation is:

```text
primitive projective tangent return:
q(t)=t^2-mu t+1
mu=4c^2-2=4I+2
```

If T1 applies, the tangent return inherits the original arithmetic persistence
filters. Minimal positive integer hyperbolic trace gives:

```text
mu=3
I=1/4
(lambda/h)^2=1
lambda/h=1
```

The algebra after T1 is exact. The open question is T1 itself.

## Non-Claims

Reject wording that implies:

```text
T1 is derived from A1-A7 plus exchange
lambda/h=1 is proven unconditionally
lambda/h=1 is a physical prediction
the finite spectrum numerics prove an exact Hausdorff dimension
gap labeling is new to this project
the SL(3) trace lift derives particle/antiparticle physics
feedback language proves awareness or consciousness
```

Correct status:

```text
conditional bridge: T1 -> S1 -> I=1/4 -> lambda/h=1
```

## Suggested Outcome Labels

```text
T1_NATURAL = T1 is a standard or defensible naturality principle
T1_INSERTED = T1 is an extra axiom/filter choice
NEEDS_REVISION = algebra or presentation needs repair
KILLED = a central implication fails
```
