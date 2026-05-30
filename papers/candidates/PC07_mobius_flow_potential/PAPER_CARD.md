# PC07 -- Mobius-Flow Potential and Kink Toy Model

Status: paper candidate. Exact algebra plus quarantined field-theory lift.

## Classification

```text
Type: THEOREM_NOTE / SPECULATIVE_MODEL
Readiness: NEEDS_VALIDATION
Priority: companion note after PC02
Main risk: field-theory, units, and observable language are inserted unless a carrier is derived
```

## One-Sentence Thesis

The Mobius action of `A` derives an exact vector field and cubic potential with
minimum at `phi`, while any field-theory or particle interpretation remains a
separate frontier lift.

## What Is Genuinely New

The exact, governed part is:

```text
A acts on H by tau -> (2 tau + 1)/(tau + 1)
the log(A) flow gives v(tau) = -kappa(tau^2 - tau - 1)
integrating the gradient gives V(tau)=kappa(tau^3/3 - tau^2/2 - tau)
V has minimum at phi and tau=0 is not a critical point
```

This narrows the earlier field-theory work: the potential is no longer guessed.

## What Is Not Claimed

```text
not a derivation of a physical field theory
not a derivation of kinetic term, dimension, units, or carrier space
not a derivation of particles or observed masses
not a cosmological prediction
not evidence for the m/g near-miss as exact
```

## Evidence Files

```text
CLAIMS.md
docs/SESSION3_SYNTHESIS.md
tests/test_mobius_vector_field.py
tests/test_derived_potential.py
frontier/B6_field_equation/
frontier/B7_fisher_kpp_creation/
frontier/B8_particle_spectrum/
frontier/B9_fusion_scattering/
```

## Reproduction Commands

```bash
python -m pytest -q tests/test_mobius_vector_field.py tests/test_derived_potential.py
python frontier/B6_field_equation/probe.py
python frontier/B7_fisher_kpp_creation/probe.py
python frontier/B8_particle_spectrum/probe.py
python frontier/B9_fusion_scattering/probe.py
```

## Required Controls

```text
separate P15/P16 exact algebra from B6-B9 frontier interpretation
state that the kinetic term is inserted
state that dimensionality and carrier space are inserted
state that m/g is a non-exact near-miss
avoid particle, gauge, gravity, or cosmology claims
```

## Status-Change Gate

PC07 can become `DRAFTABLE` only if the draft is framed as a theorem note about
P15/P16 with a clearly quarantined toy-model appendix.

It must be rescaled or killed as a physics candidate if no canonical kinetic
term, carrier, unit convention, and observable dictionary can be derived.

## Best Publication Form

```text
short theorem note about the derived potential
appendix or companion note for the toy field-theory lift
not a physics preprint
```

## Decision

```text
Keep as exact algebra plus quarantined frontier model. Do not promote the lift.
```
