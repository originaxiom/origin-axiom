# F03 execution and review boundaries

2026-09-20. These are transcribed command-tool results, not byte-for-byte raw
terminal logs. No scientific file was modified during a running check.
This is not an independent proof review, full-suite run or banking pass.

## Pre-execution custody

Input worktree was clean at `50fa3771`, on `audit/fork-2026-09-20`.
The previous turn was progress: it changed the reports, restored B739 credit,
and recorded F02 with preserved contrary test evidence.

F03 design, proof, verifier, tests and SHA256 manifest were committed at
`eb9fee27` before first execution. Four digests matched before and after.
The expectations, countercontrols and rank-two/growth restrictions are
pre-execution, not inferred only after the tests passed.

## New exact controls

```
python3.12 -m pytest -q reports/nonsplit_cusp_growth_2026_09_20/test_verify.py
```

Python 3.12.1, SymPy 1.14.0, SnapPy 3.3.2. Process 40926, final chunk
`996cae`, exit 0:

```
19 passed, 1 warning in 3.16s
```

The warning reports that Plink could not import tkinter and its GUI is
unavailable. No GUI operation or GUI-derived scientific result is used.
No failed assertion, numerical tolerance adjustment or source retry occurred.

The marked m010 check confirms the integer cusp count and orientability;
it is not a new interval certificate of hyperbolicity. The general analytic
claim explicitly assumes the complete hyperbolic metric. The exact holonomy
and translation checks are independent small-matrix calculations.

## Unchanged antecedent checks

```
python3.12 -m pytest -q \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py
```

Process 71728, final chunk `cf7e49`, exit 0:

```
23 passed in 4.16s
```

These are seven F01-v2 controls and sixteen F02 controls. F01's originally
failed v1 implementation and F02's failed antecedent R16 recheck are still
preserved; selecting the already-corrected F01-v2 file does not erase them.
The R16 test was not rerun or changed in this turn. All seven F01-v2 seal
entries and four F02 seal entries were checked unchanged.

## Authored argument review

The decisive inequalities are stated in PROOF.md. Their nontrivial scope
checks were examined before the run:

- b must be invariant under the entire image, not invariant up to a shift.
  Unit-modulus diagonal entries give this; the dilation control fails it.
- All Stokes integrations use compact truncations. No total-energy or
  integrability assumption has entered the global flux identity.
- A single cusp and no source/boundary exclude an unaccounted compensating
  flux. Additional ends or currents require a different balance.
- Torus averaging is performed in the fixed h0 measure. The minimum of b,
  not its mean, bounds the weighted translation energy from below.
- Positive Bbar' justifies multiplication of the differential inequality;
  a finite-time bound then contradicts a globally smooth solution.
- The limsup conclusions are along a sequence, not uniform lower bounds
  for all large radii. They are necessary conditions, not existence results.
- A rank-two harmonic-map obstruction is not silently applied to every
  rank-four Hermitian metric.

Finite symbolic tests check formulas and falsifiers, not the infinite-domain
quantifier. No numerical shooting, triangulated PDE solution, physical mode
spectrum, anomaly or gravitational calculation was performed.

## Retrieval and literature

`already_banked.py 'nonsplit harmonic cusp infinite energy'` returned 113
lexical hits and zero settled matches under its threshold. Scoped searches
also examined Busemann/horospherical/infinite-energy and literature aliases.
No inference of corpus-wide absence or novelty follows from those outputs.
The report-guided all-history discovery receipt was not rerun this turn.

Personally read: F01's full proof and relevant tests, F02 findings, selected
OPEN_LEADS rows, and Sagman arXiv:1911.06937v3 HTML main theorem/definitions,
sections 3.2--3.3 and 6.1. Section 6.1 changes to a reductive representation
for a length-spectrum problem; that change does not certify the original
nonsplit physical coefficient bundle. The whole paper was not read this
turn and its surface-source statements were not promoted to a 3D theorem.

The finite-time exponential-ODE comparison is derived explicitly; no
unread Keller-Osserman theorem supplies its hypotheses. No empirical data
or externally measured constant was used or newly verified.

The full TOE goal remains active. This checkpoint narrows a realization
class while retaining the exact algebraic positive and the untested routes.
