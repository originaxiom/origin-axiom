# F04 execution and scope receipt

2026-09-20. This is a transcription of command-tool outcomes, not a raw
terminal log, independent proof review, full-suite run or banking pass.
No scientific source was edited while tests were running.

## Custody

Input: clean `audit/fork-2026-09-20` at `7d277ade`. F04 DESIGN, PROOF,
verify.py, test_verify.py and SHA256 seal were committed at `9d366599`
before first scientific execution. No failed source revision, parameter
adjustment or retry occurred. The expected analytic outcome and its
countercontrols were disclosed in the preregistration.

Post-execution checks confirm all four F04, four F03, four F02 and seven
F01-v2 seal entries unchanged: 19 digests total. Prior failed F01-v1 and
R16 checks remain in their own receipts; this run does not erase them.
The R16 failure was not rerun or relabeled as passing.

## New tests

```
python3.12 -m pytest -q reports/full_flag_growth_2026_09_20/test_verify.py
```

Python 3.12.1, SymPy 1.14.0. Process 91737, final chunk `caef42`, exit 0:

```
20 passed in 13.18s
```

The tests independently assemble the normalized symmetric-cube matrices,
check marked words, peripheral periods and flag equivariance, derive the
full trace metric including complex off-diagonal entries, distinguish the
two Maurer--Cartan orderings, and check the diagonal Euler/Cartan identities.
The generic positive metric is not restricted to induced rank-two ratios.
The central-normalization identity is tested before using Delta w=0 in
the written proof. The full local matrix tension vanishes, while a wrong
radial profile and omission of inner-boundary flux fail their controls.

The local tension is computed after conjugation by N^-dagger and N^-1 for
N=exp(-zJ). All z dependence cancels algebraically in that frame. It is not
a point-sampled numerical residual or merely the three diagonal equations.

## Unchanged antecedents

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py \
  reports/nonsplit_cusp_growth_2026_09_20/test_verify.py
```

Process 22024, final chunk `08185f`, exit 0:

```
42 passed, 1 warning in 7.06s
```

Seven F01-v2, sixteen F02 and nineteen F03 controls. The warning concerns
Plink's optional tkinter GUI, not a mathematical assertion or computation.
Importlib mode distinguishes report-local test_verify.py files of the same
basename. No assertion was skipped or scientific source changed for this.
SnapPy's m010 cusp-count/orientability check is combinatorial input, not a
new interval certificate or geometric finite-energy test.

## Analytic review boundaries

The author checked the following points in the written derivation:

- The entire representation, not only its peripheral subgroup, has the
  modulus-one diagonal action needed for global flag heights.
- Determinant normalization is justified by the harmonic trace equation;
  unrestricted central harmonic data do not create a hidden finite-energy
  assumption or change the simple-root heights.
- Cholesky coordinates include every positive determinant-one metric;
  extra mixing coordinates are not truncated to a principal SL2 ansatz.
- Positive root sources follow by variation, and summing flag equations
  gives positive higher-root multiplicities. Only necessary equations
  are used, not a false claim that they solve the off-diagonal system.
- Compact Stokes uses exactly one end and no sources/inner boundary.
- Each period estimate uses the minimum of its own root height, not an
  unjustified product of mean weight and mean derivative energy.
- The positive Cartan weights and AM-GM constants are derived. Large
  angular oscillation is retained as a possibility, not assumed absent.
- The finite-time contradiction is the elementary F03 comparison with
  positive derivative. The conclusions are limsup bounds along sequences.

The general theorem is not certified by the finite matrix tests. No second
expert reviewed the proof. No global harmonic metric, numerical PDE mesh,
physical background, mode spectrum, anomaly, interaction or gravitational
calculation was produced. No broad empirical compatibility claim is made.

## Retrieval and literature

Scoped current-file searches used word-boundary Cholesky/Iwasawa/Toda and
flag-height terms. An initial unbounded Toda search also matched 'today';
it was corrected, and that noisy count was not used. The earlier
already_banked lookup had broad flag/Cartan matches, not a semantic absence
certificate. The completed all-history report-guided resweep was not rerun
in this checkpoint; this work follows its admissibility correction.

Personally reread: F03's full proof/design and tests, F01-v2's producer,
R27's exact representation/nonsplitting discussion, F02's result, and the
living audit/resweep sections. No agent supplied a substitute summary.

The first publisher fetch for Wu--Zhang returned 403. Primary publisher
content subsequently available through search included its introduction
and main compact-base theorem statement. Only that scope was used.
The arXiv abstract of Collins--Jacob--Yau was readable; its experimental
HTML fetch failed. It was not represented as a full-paper reading, and no
proof from it was imported. No PDF was used in this checkpoint.

The work remains local to this fork. No shared B identifier was taken,
no upstream bank/gates/full-suite completion is claimed, no other seat's
unsealed producer was run, and no external publication or push was made.
