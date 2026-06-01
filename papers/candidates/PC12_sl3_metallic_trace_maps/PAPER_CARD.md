# PC12 -- Metallic SL(3) Trace-Map Arithmetic

Status: paper candidate. No claims beyond governed repository artifacts.

## Classification

```text
Type: THEOREM_NOTE / COMPUTATIONAL_REPORT
Readiness: NEEDS_VALIDATION
Priority: standalone companion to PC11, not an Origin-core promotion
Main risk: the fixed-line splitting classification is certificate-assisted and
must be made human-reviewable
```

## One-Sentence Thesis

The metallic substitutions `phi_m(a)=a^m b, phi_m(b)=a` induce a rigid family of
rank-two `SL(3,C)` trace maps with preserved commutator trace-pair, exact
algebraic entropy, and certificate-backed fixed-line arithmetic.

## What Is Genuinely New

The repository-level contribution is the governed extension of B27:

```text
B27 m=1 SL(3) Fibonacci trace lift
  -> B48 metallic family m>=1
  -> explicit Cayley-Hamilton trace-map recurrences
  -> unordered commutator trace-pair invariant
  -> entropy log((m + sqrt(m^2+4))/2)
  -> fixed-line Jacobian arithmetic splitting classification
  -> compact SU(3) diagonal-slice survival c=-1,0,1,3
  -> B49 certificate-to-proof hardening for the splitting classification
  -> B50 internal proof-draft skeleton
  -> B51 symbolic-m c=3 factorization proof module
  -> B52 multichannel physics-bridge negative control
```

The novelty, if any, is the metallic `SL(3)` trace-map package and its exact
arithmetic controls. Literature priority remains a validation target.

## What Is Not Claimed

```text
not an Origin-core theorem
not a proof of PC11's T1/S1 selector
not a physical prediction
not a derivation of matter, gauge, spacetime, gravity, or awareness
not a particle/antiparticle interpretation of direct/inverse traces
not a claim that certificate-backed classification has independent validation
not a public-ready manuscript release
```

## Evidence Files

```text
frontier/B27_sl3_fibonacci_trace_lift/
frontier/B48_sl3_metallic_trace_maps/
frontier/B49_sl3_certificate_proof_hardening/
frontier/B50_pc12_proof_draft_assembly/
frontier/B51_sl3_symbolic_m_factorization/
frontier/B52_multichannel_fibonacci_bridge_control/
tests/test_sl3_metallic_trace_maps.py
tests/test_sl3_certificate_proof_hardening.py
tests/test_sl3_symbolic_m_factorization.py
tests/test_multichannel_fibonacci_bridge_control.py
tests/test_pc12_draft_skeleton.py
papers/candidates/PC12_sl3_metallic_trace_maps/CERTIFICATE_APPENDIX.md
papers/candidates/PC12_sl3_metallic_trace_maps/DRAFT_NOTE_SKELETON.md
papers/candidates/PC12_sl3_metallic_trace_maps/LITERATURE_POSITIONING.md
papers/candidates/PC12_sl3_metallic_trace_maps/VALIDATION_BRIEF.md
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

## Known Controls

```text
trace-map formula checked at m=1 against explicit formula
direct exact SL(3,Z) matrix trace checks for m<=4
entropy degree recurrence checked for m<=25, n<=30
c=3 and c=1 Jacobian block factorizations checked exactly
integer splitting classification checked over default and deep rectangles
compact SU(3) slice checked by explicit representatives
B49 checks universal splitting criterion, direct split families, square-gap
propagation, finite positive strips, and negative strip / boundary exclusions
B50 organizes the note into five theorem blocks with explicit non-claims
B51 proves the c=3 fixed-line Jacobian block factorization symbolically for
formal m
B52 confirms the naive three-channel Fibonacci tight-binding model has 6x6
symplectic transfer matrices and fails the PC12 third-order trace recursion
```

## Known Failures / Limits

```text
draft skeleton exists, but polished human proof text is not yet written
literature priority is not settled for the standalone SL(3) character-variety
package
diagonal fixed-line arithmetic is not automatically a representation-locus theorem
compact SU(3) slice is compact-unitary mathematics, not physics
the simplest multichannel physics bridge fails; no verified physical dictionary
to PC12 is known in this repo
```

## Required Citations

```text
Procesi -- matrix trace invariant theory
Lawton -- SL(3,C) rank-two character varieties and trace coordinates
classical SL(2) trace-map / Fricke-Vogt literature
Bellon-Viallet and related algebraic-entropy degree-growth literature
Out(F2) / character-variety dynamics references where needed
```

## Target Audience

```text
character varieties
trace identities
algebraic dynamics
computationally assisted arithmetic classification
```

## Best Publication Form

```text
short theorem note with a certificate appendix
```

## Decision

Keep as a standalone PC12 candidate. It strengthens the trace-map ecosystem and
gives B27 a systematic metallic-family context, but it does not change the
conditional status of PC11 or any Origin-core claim.

Next governed path:

```text
B53 -- PC12 global-exclusion proof text and literature-priority tightening
```
