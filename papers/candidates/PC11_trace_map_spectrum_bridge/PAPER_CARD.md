# PC11 -- Half-Step Trace Lift and Fibonacci Spectrum Anchor

Status: paper candidate. No claims beyond governed repository artifacts.

## Classification

```text
Type: COMPUTATIONAL_REPORT / LITERATURE_BRIDGE
Readiness: EVIDENCE_EXISTS
Priority: companion to PC02, not first ship target
Main risk: lambda=1 depends on a projective self-similarity selector not yet derived
```

## One-Sentence Thesis

The half-step trace-map campaign B13-B26 isolates a canonical character-variety
trace lift containing the `A` sector and identifies the Fibonacci Hamiltonian at
`lambda=1` as a finite-approximant spectral anchor, while keeping the coupling
and physical dictionary unpromoted.

## What Is Genuinely New

The repository-level contribution is the governed bridge package:

```text
conditional uniqueness core
  -> exchange/half-step condition
  -> F=LP, F^2=A
  -> functorial trace lift of F
  -> A quadratic sector inside the lift
  -> lambda=1 spectral anchor on I=1/4
  -> B26 projective half-return selector for I=1/4
  -> Lucas hierarchy lambda^2 = L_n - 2 under the same projective criterion
```

The novelty, if any, is the controlled packaging of these known mathematical
objects around the Origin Axiom core, not the Fibonacci Hamiltonian facts
themselves.

## What Is Not Claimed

```text
not a proof that the projective half-return criterion is forced
not a new gap-labeling theorem
not an exact Hausdorff-dimension computation
not a physical prediction
not a derivation of matter, gauge, spacetime, or awareness
```

## Evidence Files

```text
frontier/B13_trace_map_character_variety/
frontier/B18_trace_lift_functoriality/
frontier/B22_spectrum_genericity_controls/
frontier/B25_fibonacci_spectrum_anchor/
frontier/B26_lambda1_derivation_attempt/
PROGRESS_LOG.md
docs/atlas/RESEARCH_TREE.md
```

## Reproduction Commands

```bash
python frontier/B18_trace_lift_functoriality/probe.py
python frontier/B22_spectrum_genericity_controls/probe.py
python frontier/B25_fibonacci_spectrum_anchor/probe.py
python frontier/B26_lambda1_derivation_attempt/probe.py
```

## Required Controls

```text
state B18 as trace-lift functoriality, not physics
state B22 parity genericity clearly
state B25 as finite-approximant numerics
cite known Fibonacci Hamiltonian literature
label lambda=1 as MOTIVATED unless the projective selector is itself derived
state B26 as a projective selector, not an unconditional derivation
state the literal full-return control separately from the projective half-return
```

## Required Citations

```text
Damanik, Gorodetski, Yessen -- The Fibonacci Hamiltonian, arXiv:1403.7823
standard Fricke-Vogt / character-variety trace-map references
standard Fibonacci Hamiltonian gap-labeling references
```

## Decision

```text
Keep as a companion bridge card. B26 strengthens the bridge, but external review
must decide whether the projective half-return selector is a natural theorem or
an inserted criterion.
```
