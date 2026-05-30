# PC11 Review Packet -- Half-Step Trace Lift and Conditional Spectrum Anchor

Status: external-review packet. This is a guide for auditing the PC11 bridge.
It does not promote C5 and does not add claims.

## Review Target

The candidate statement is:

```text
half-step F=LP with F^2=A
  -> functorial trace lift of F
  -> projective trace quotient
  -> primitive projective tangent return
  -> T1 -> S1 -> I=1/4 -> lambda/h=1
```

The result is conditional. The exact algebra after T1 is reproducible; T1 is the
object needing review.

## Files To Read

Primary:

```text
docs/TRACE_SELECTOR_THEOREM.md
papers/candidates/PC11_trace_map_spectrum_bridge/PAPER_CARD.md
papers/candidates/PC11_trace_map_spectrum_bridge/VALIDATION_BRIEF.md
CLAIMS.md
frontier/B38_tangent_return_arithmetic_filter/FINDINGS.md
frontier/B40_filter_reuse_audit/FINDINGS.md
frontier/B47_s1_verdict_ledger/FINDINGS.md
```

Secondary:

```text
frontier/B18_trace_lift_functoriality/FINDINGS.md
frontier/B22_spectrum_genericity_controls/FINDINGS.md
frontier/B25_fibonacci_spectrum_anchor/FINDINGS.md
frontier/B26_lambda1_derivation_attempt/FINDINGS.md
frontier/B28_projective_quotient_legitimacy/FINDINGS.md
frontier/B29_hierarchy_normalization_controls/FINDINGS.md
frontier/B30_projective_state_space/FINDINGS.md
frontier/B31_primitive_projective_return_selector/FINDINGS.md
frontier/B32_selector_axiom_audit/FINDINGS.md
frontier/B37_operational_feedback_quarantine/FINDINGS.md
```

## Reproduction Commands

Run from the repository root:

```bash
python frontier/B18_trace_lift_functoriality/probe.py
python frontier/B25_fibonacci_spectrum_anchor/probe.py
python frontier/B26_lambda1_derivation_attempt/probe.py
python frontier/B38_tangent_return_arithmetic_filter/probe.py
python frontier/B40_filter_reuse_audit/probe.py
python frontier/B47_s1_verdict_ledger/probe.py
python -m pytest -q
```

Expected current result:

```text
full suite: 66 passed, 1 skipped
B38/B40/B47: CONDITIONAL
```

## The Algebra To Check

The primitive projective tangent return has quadratic:

```text
q(t)=t^2-mu t+1
mu=4c^2-2=4I+2
```

If T1 applies, the tangent return inherits the original arithmetic persistence
filters used in the conditional uniqueness theorem. Minimal positive integer
hyperbolic trace gives:

```text
mu=3
I=(3-2)/4=1/4
```

With the Fibonacci Hamiltonian normalization:

```text
I=(lambda/h)^2/4
```

this gives:

```text
lambda/h=1
```

The audit should check whether this is a legitimate reuse of the original
filters or an additional selector.

## Controls Already Logged

```text
B25: finite-approximant spectrum anchor only; not exact Hausdorff dimension
B26: projective half-return selector exact; criterion still added
B28: central-sign quotient legitimate locally; not by itself a selector
B29: Lucas hierarchy exact; not a physical spectrum
B30-B32: quotient/return alone leaves I free; S1 isolated
B37: feedback/invariant language only; awareness terms quarantined
B38-B47: T1 implies S1; T1 not derived
```

## Non-Claims To Enforce

The validation process should reject any draft wording that implies:

```text
T1 is already derived
lambda/h=1 is an unconditional prediction
finite spectra establish a physical observable
the Fibonacci Hamiltonian gap-labeling result is new
SL(3) direct/inverse traces are particles and antiparticles
trace-map feedback is awareness
```

The correct wording is:

```text
given T1, the trace selector conditionally selects I=1/4 and lambda/h=1
```

## Draft Readiness Checklist

Before PC11 becomes `DRAFTABLE`, it needs:

```text
independent check of T1 status
related-work scan for trace maps, Fricke-Vogt invariants, and Fibonacci Hamiltonian gap labeling
clear separation of known literature from project-specific packaging
explicit statement that lambda/h is dimensionless
explicit statement that no physical units or observables are derived
short appendix reproducing B18, B25, B26, B38, B40, and B47
```

## Validation Questions

Check:

```text
Is the trace lift of F described with standard terminology?
Is the PSL / central-sign quotient being used correctly?
Is T1 equivalent to a known naturality or arithmeticity condition?
If T1 is inserted, is it still a useful named conditional assumption?
Should the Lucas hierarchy be included in the body or only an appendix?
What existing literature should be cited before any public draft?
```

## Outcome Labels

After review, assign exactly one:

```text
T1_NATURAL = T1 is defensible as standard/natural mathematics
T1_INSERTED = T1 is an extra assumption but clearly isolated
NEEDS_REVISION = the bridge is plausible but presentation or algebra needs repair
NEEDS_RESCOPING = PC11 should be reduced to a smaller note
KILLED = a central trace-lift, quotient, or selector implication fails
```

## Current Decision

```text
Prepare PC11 for external mathematical review.
Do not merge with physics-facing claims.
```
