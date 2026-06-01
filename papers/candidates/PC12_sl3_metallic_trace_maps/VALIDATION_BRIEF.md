# PC12 Validation Brief

Status: validation brief. This is a compact path for auditing PC12.

## What To Validate

PC12 asks whether the metallic `SL(3)` trace-map package is correct and
reviewable as standalone mathematics:

```text
B27 m=1 trace lift
  -> B48 metallic family
  -> trace-map formula
  -> commutator trace-pair invariant
  -> entropy
  -> fixed-line arithmetic
  -> compact SU(3) diagonal-slice controls
  -> symbolic-m proof support at c=3
```

It does not ask whether this derives physics or solves PC11's T1/S1 selector.

## Minimal Reading Set

Read in this order:

```text
papers/candidates/PC12_sl3_metallic_trace_maps/PAPER_CARD.md
frontier/B48_sl3_metallic_trace_maps/FINDINGS.md
papers/candidates/PC12_sl3_metallic_trace_maps/CERTIFICATE_APPENDIX.md
frontier/B49_sl3_certificate_proof_hardening/FINDINGS.md
frontier/B51_sl3_symbolic_m_factorization/FINDINGS.md
papers/candidates/PC12_sl3_metallic_trace_maps/DRAFT_NOTE_SKELETON.md
papers/candidates/PC12_sl3_metallic_trace_maps/LITERATURE_POSITIONING.md
frontier/B52_multichannel_fibonacci_bridge_control/FINDINGS.md
frontier/B27_sl3_fibonacci_trace_lift/FINDINGS.md
```

## Reproduction Commands

```bash
python frontier/B48_sl3_metallic_trace_maps/probe.py
python frontier/B48_sl3_metallic_trace_maps/probe.py --deep
python frontier/B49_sl3_certificate_proof_hardening/probe.py
python frontier/B51_sl3_symbolic_m_factorization/probe.py
python frontier/B52_multichannel_fibonacci_bridge_control/probe.py
python -m pytest tests/test_sl3_metallic_trace_maps.py -q
python -m pytest tests/test_sl3_certificate_proof_hardening.py -q
python -m pytest tests/test_sl3_symbolic_m_factorization.py -q
python -m pytest tests/test_multichannel_fibonacci_bridge_control.py -q
python -m pytest tests/test_pc12_draft_skeleton.py -q
```

## Main Checks

```text
Is the eight-coordinate trace convention correct?
Are the Cayley-Hamilton recurrences indexed correctly?
Is the commutator trace-pair invariant stated with the right convention?
Is the entropy proof genuinely no-cancellation, not just observed degree growth?
Can the fixed-line splitting classification be converted from certificate to proof?
Is the compact SU(3) slice stated as compact-unitary mathematics only?
Does the literature already contain any part of the metallic SL(3) package?
Does B52 correctly rule out the naive multichannel tight-binding bridge without
overstating the negative result?
```

## Core Missing Object

The missing object is:

```text
polished human proof text for the fixed-line splitting classification
a verified physical dictionary, if PC12 is ever to be connected to physics
```

B49 supplies the proof-module architecture, and B51 supplies a symbolic proof
module for the `c=3` fixed-line factorization. The certificate runners are
evidence and reproducibility support; they should not be the only proof if PC12
is drafted. B52 is a negative control for physics language, not part of the
mathematical proof.

## Non-Claims

Reject wording that implies:

```text
PC12 promotes Origin-core claims
PC12 derives PC11's T1/S1 selector
PC12 makes physical predictions
PC12 derives matter, gauge, gravity, spacetime, or awareness
compact SU(3) means particle physics
```

## Suggested Outcome Labels

```text
DRAFTABLE = proof architecture and literature positioning are coherent
NEEDS_REVISION = algebra is sound but presentation/proof needs repair
NEEDS_RESCOPING = a result survives only in a narrower form
KILLED = a central trace-map, invariant, entropy, or classification claim fails
```
