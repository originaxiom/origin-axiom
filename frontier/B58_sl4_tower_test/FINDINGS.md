# ⚠️ HEADLINE CORRECTED BY B742 + B745 (2026-07-21)

**THE HEADLINE CLAIM OF THIS FILE — "the prediction cannot be tested numerically" — IS
NEGATED.** The negatives hunt (B742, audit seat) built the ε-extrapolated pinv-ratio route
(the B59 method) and computed the ambient SL(4) 15×15 fixed-line Jacobian numerically,
validated against the exact SL(3) anchor and B65's exact symbolic J(1); the banking seat
cross-verified independently (B745: re-execution identical + five independent exact checks,
ALL PASS). The SL(4) 7-factor tower prediction IS numerically testable — and the computed
spectrum reproduces B59's banked factorization. What SURVIVES from this file (the necessary
component, reconfirmed both seats): the fixed-line point is the identity representation,
where the representation-to-trace map is first-order degenerate — so the NAIVE
at-the-point route below is genuinely dead. What flips: only the impossibility headline.
The text below is kept for the record with this correction on top.

---

# B58 Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Verdict

```text
NEEDS-EXPERTISE
```

The SL(4) 7-factor tower prediction is **untested** -- neither confirmed nor
refuted. Testing it requires the ambient SL(4,C) trace-map construction, which is
not built here.

## What Is Established

**Mechanism (rigorous).** The SL(4) forward-chain Cayley-Hamilton recursion at
the identity representation,
`tau_k = 4 tau_{k-1} - 6 tau_{k-2} + 4 tau_{k-3} - tau_{k-4}`, has characteristic
polynomial `(r-1)^4`. So the fixed-line derivative sequences are **cubic in k** --
the natural step up from SL(3)'s `(r-1)^3` (quadratic, B55). The
derivative-polynomial degree is `n-1`. This is the part of the SL(n) story that
clearly does generalize.

**Obstruction (rigorous).** The fixed-line point (all traces `= n`) is the
identity representation. There the representation-to-trace map is first-order
degenerate: `d tr(W) = 0` for every word `W` (the linear term is `tr` of an
`sl(n)` tangent vector, which vanishes), and traces are second-order. Verified
numerically (`d/de tr(W) ~ 1e-10`, `d^2/de^2 tr(W) ~ 50`).

## Why The Prediction Cannot Be Tested Numerically (the key point)

The object that factors into `char(M^k)` for SL(3) (B54/B55) is the **ambient
trace-map Jacobian** -- the Jacobian of the polynomial self-map of the trace
coordinates, evaluated at the fixed-line point. It is **not** a linearization of
matrix representations. Since every representation realizing the fixed-line point
is the degenerate identity (first-order-stationary traces), the user-suggested
"pick random SL(4,C) representations near the identity and extract the Jacobian"
route **does not compute this object**; it would capture only the second-order
(representation-Hessian) data, a different and prediction-irrelevant linearization.

Therefore the rigorous test requires the ambient construction:

```text
- 15 trace coordinates: a minimal generating set for the SL(4,C) character
  variety of F_2 (Procesi second fundamental theorem; cf. SL(3) = Lawton's C^9
  hypersurface, 8 of whose coordinates B54 used).
- the substitution action: tr(word(AB, A)) reduced to polynomials in the 15
  coordinates via the SL(4) trace identities.
- then the ambient 15x15 Jacobian at (n,...,n) = (4,...,4), factored over Z.
```

This is a substantial, error-prone trace-identity build -- research-level, not
completed in this pass. Faking either a "7 factors confirmed" or a refutation
without it would violate the governance.

## Status Of The Prediction

Unchanged: recorded as an **untested prediction** in PC12's
`DRAFT_NOTE_SKELETON.md`, confirmed only at `n = 2, 3`. B58 sharpens *what is
required* to test `n = 4` (the ambient SL(4,C) trace map) and rules out the
naive numerical route. Building that map is the genuine next probe.
