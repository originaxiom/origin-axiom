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
tests/test_sl3_metallic_trace_maps.py
papers/candidates/PC12_sl3_metallic_trace_maps/CERTIFICATE_APPENDIX.md
papers/candidates/PC12_sl3_metallic_trace_maps/LITERATURE_POSITIONING.md
papers/candidates/PC12_sl3_metallic_trace_maps/VALIDATION_BRIEF.md
```

## Reproduction Commands

```bash
python frontier/B48_sl3_metallic_trace_maps/probe.py
python frontier/B48_sl3_metallic_trace_maps/probe.py --deep
python -m pytest tests/test_sl3_metallic_trace_maps.py -q
```

## Known Controls

```text
trace-map formula checked at m=1 against explicit formula
direct exact SL(3,Z) matrix trace checks for m<=4
entropy degree recurrence checked for m<=25, n<=30
c=3 and c=1 Jacobian block factorizations checked exactly
integer splitting classification checked over default and deep rectangles
compact SU(3) slice checked by explicit representatives
```

## Known Failures / Limits

```text
certificate-assisted classification is not yet a compact human proof
literature priority is not settled
diagonal fixed-line arithmetic is not automatically a representation-locus theorem
compact SU(3) slice is compact-unitary mathematics, not physics
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
B49 -- SL3 certificate-to-proof hardening
```
