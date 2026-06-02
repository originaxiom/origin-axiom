# PC12 -- Metallic SL(3) Trace-Map Arithmetic

Status: paper candidate. No claims beyond governed repository artifacts.

## Classification

```text
Type: COMPUTATIONAL_REPORT
Readiness: NEEDS_VALIDATION
Priority: standalone companion to PC11, not an Origin-core promotion
Main risk: per the 2026-06-01 literature screen (LITERATURE_POSITIONING.md),
most blocks are STANDARD_REPACKAGE (Lawton SL(3,C) coordinates x
Baake-Grimm-Roberts substitution trace maps); only the fixed-line splitting
classification (Thm 4) is APPARENTLY_NEW, and it is elementary. The result is a
computational note, not a theorem paper; specialist confirmation still needed.
```

> **Rescaled 2026-06-01** from THEOREM_NOTE to COMPUTATIONAL_REPORT after the
> B53 literature screen. The exact algebra stands and was extended (B54); the
> framing is downgraded to match what is genuinely new.

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
  -> B54 general-c exchange commutation (all c) + c=1 Eisenstein/golden twins
  -> B55 c=1 fixed-line structure for general m (symmetric mod-4; antisym char(M))
  -> B56 figure-eight I=1/4 bridge negative control (cyclotomic coincidence)
  -> B57 general-m Diophantine splitting classification ({c=1,c=3} universal)
```

Per the 2026-06-01 literature screen (`LITERATURE_POSITIONING.md`), the
trace-map formula (Thm 1), commutator invariant (Thm 2), algebraic entropy
(Thm 3), exchange decomposition, and symbolic-`m` factorization are
`STANDARD_REPACKAGE` — standard methods (Lawton; Baake-Grimm-Roberts;
Bellon-Viallet) applied to the metallic family. Only the fixed-line integer
splitting classification (Thm 4) is not located in the literature, and it is
elementary. The contribution is therefore a governed, reproducible
**computational note**, not a theorem paper; the `c=1` twin polynomials echo
the figure-eight gluing-equation discriminant pair (P12).

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
frontier/B54_general_c_exchange_structure/
frontier/B55_c1_fixed_line_structure/
frontier/B56_figure_eight_invariant_surface/
frontier/B57_general_m_splitting/
frontier/B59_sl4_factorization/
frontier/B60_sln_tower/
frontier/B61_sl5_high_precision/
tests/test_sl3_metallic_trace_maps.py
tests/test_sl3_certificate_proof_hardening.py
tests/test_sl3_symbolic_m_factorization.py
tests/test_multichannel_fibonacci_bridge_control.py
tests/test_general_c_exchange_structure.py
tests/test_c1_fixed_line_structure.py
tests/test_figure_eight_invariant_surface.py
tests/test_general_m_splitting.py
tests/test_sl4_factorization.py
tests/test_sln_tower.py
tests/test_b61_sl5.py
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
B54 proves [J(m,c),P]=0 for symbolic c (exchange block-diagonalization on the
whole fixed line, generalizing B51) and records the c=1 Eisenstein/golden twins
B55 classifies the c=1 sectors for general m (symmetric mod-4; antisym char(M)),
proved per residue class and cross-checked m=1..12
B56 records the figure-eight I=1/4 bridge as a dead negative control (diagonal
reps at I in {4,-17/2+-7sqrt5/2}, none=1/4)
B57 classifies integer splitting for m=1..6 ({c=1,c=3} universal; class-field
coincidence killed for m>=2)
B59/B60 compute the SL(4) fixed-line factorization and the cross-n tower (n=3,4)
by an extrapolated ambient Jacobian, validated on SL(3) ground truth
B61 high-precision SVD pinv (dps 60) resolves 22 of 24 SL(5) multipliers
(inverse-word coords, rank 24); SL(3)/SL(4) reproduce to ~4e-14/~3e-9
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
B53 literature screen -- DONE (LITERATURE_POSITIONING.md): rescaled to a
  computational note; heavy theorem-prose for the standard blocks is not warranted.
B54 -- DONE: general-c exchange commutation + c=1 twin polynomials integrated.
Remaining: independent specialist read (confirms Thm 4 novelty + framing),
  deferred this cycle. No physics dictionary is claimed; B52 stays the explicit
  negative control. The self-evidencing / free-energy framing is quarantined in
  paths/E21_self_evidencing_closure/ and is not part of PC12.
```
