# F02: complete-space domain, not a chirality verdict

2026-09-20. Fork-local research checkpoint. No shared B number or main-bank
certification. Design and exact-control sources must be committed before
their first execution. Existing analytic expectations below are not blind
predictions; the computation checks signs, identities and countercontrols.

## One-sentence question and quantifier

For EVERY complete smooth Riemannian manifold without boundary, finite-rank
positive Hermitian bundle with smooth unitary connection A, and smooth
Hermitian endomorphism-valued one-form Psi, does the formally symmetric
operator Q=d_A+d_A^*+sum(Psi_i*(epsilon_i+iota_i)) on compactly supported
smooth forms have a unique self-adjoint closure in ordinary L2, without
requiring integral |Psi|^2 finite?

This is a standard analytic result applied to the program's domain question,
not a claim of new mathematics. The analytic proof is the universal part;
finite tests cannot establish its quantifier. The adopted quadratic fermion
action and its positive Hilbert metric remain model inputs. Their microscopic
origin is not derived. No empirical values, fitted constants or SM counts.

## Pre-execution outcomes

A. The cutoff proof closes under exactly those hypotheses and all prescribed
   exact controls pass. Reuse its unique-domain conclusion for a background
   ONLY after establishing that background and the operator dictionary.
B. A hypothesis or identity fails. Retain the original source and failure;
   narrow or correct in a separately recorded version. No physical exclusion
   follows from a failed implementation.

Neither outcome constructs a harmonic metric for the nonsplit m010 witness,
proves Fredholmness, computes a 4D chiral index, or completes a TOE.

## Prior work reused

- R15 GLOBAL_SINGULAR: scalar parametrix/resolvent and homogeneous through-flux
  freedom. Its source-free specialization is a global commuting control.
- R28 SOURCE_ACTION: residual potential differs from background and variation
  norms. Its source and cusp norm formulas are not discoveries of F02.
- R16 CHARGED_DOMAIN: singular-line domains are on an incomplete complement.
- R23 and R30 RESOLVED_FERMION_PROOF section 1: quadratic form-valued fermion
  operator, ordinary L2 and explicit compact-regulator boundary choices.
- B739: completeness already supplies scalar essential self-adjointness.
  Restored separately in SCATTERING_RECOVERY; do not claim that idea absent.
- F01: finite-harmonic-energy splitting theorem remains intact. F02 neither
  removes its energy hypothesis nor interprets it as physical automatically.

`already_banked.py` was run for `harmonic finite energy source boundary` and
`self-adjoint complete cutoff`; the latter gave 90 lexical hits and no settled
match under its threshold, NOT an absence theorem. A .md/.py/.tex search of
unique head/remote/tag tips for essential-self-adjointness/Chernoff/Gaffney
found B739. It did not search all historical versions or prove novelty.
The all-history resweep receipt remains the broader discovery inventory.

## Exact controls and falsifiers

1. Creation/annihilation relations in exterior dimensions 1, 2, 3; Clifford
   symbol norm; parity; Hermitian noncommuting matrix-valued Higgs potential.
2. A polynomial product-rule check: the cutoff commutator is c(dchi), with
   no Higgs term. Adding i*identity is a deliberately nonsymmetric mutant.
3. Hyperbolic cusp F=c*exp(2r): zero harmonic residual, but growing background
   norm; zero c is the negative control. Weighted signed through-flux balance
   has nonzero two-cusp solutions, not a forced one-cusp solution.
4. Complete real line with Q=c*d/dx+hat-c*x: one even L2 Gaussian kernel and
   no odd L2 partner. This forbids deducing zero graded index just from
   self-adjointness. It is NOT a BPS background or a 4D generation.
5. Free complete real line: normalized broad Gaussians with image norm
   tending to zero, no L2 zero eigenfunction. Unique domain need not be
   Fredholm. Incomplete half-line has explicit nonzero deficiency vectors.

All tests are exact SymPy checks, not a finite-element approximation to m010
or a certificate of a global solution. No search grid will be widened after
seeing results. Independently inspect the written proof's completeness,
compact-core smoothing, positivity and smoothness assumptions before running.

## Custody and stop rule

Seal DESIGN, PROOF, verify and test_verify with SHA256 and commit before run.
Run only the focused new tests and unchanged relevant existing controls.
Write actual outcome after completion; no entire-suite or independent banking
claim. Keep the fork and other seats' scientific files separate. The immediate
next scientific task, if A holds, is background existence/asymptotics and
physical fluctuation spectrum, not another choice of cutoff boundary condition.
