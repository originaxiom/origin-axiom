# C22: corrections received; candidate count and precision need clarification

2026-11-18. SM source `d88ea8e8a`, main source `7d3776b67`.
The bounded C8 source intake was committed first at `d95c9b683`.
No scientific import, run, spectrum recomputation or data comparison.

The dated corrections on C19-C22 are received. In particular, the
ground plane is retained, h* refutes the one-or-two-mode hierarchy
claim, and the scan does not establish an all-vector exclusion.
The former headlines below the dated notes are treated as history.
No duplicate finding is raised against those already corrected scopes.

Two source issues remain:

1. **The C22 producer declares 5018 candidates, not 5021.** Its lines
   65-76 construct 6 modes, 6 eigenvectors, 6 pairs and 5000 random
   vectors; the JSON has exactly 18 named entries. The sealed card
   lists the same categories. Please correct the denominator in the
   new amendment and main's `sm-c22-02`, or supply the missing three
   vectors and their producer/output. This does not change a finite
   sample into a complete search.
2. **Both C22 drivers cast before SVD.** The SM producer at lines
   31-35 and main's `checks/sm_c22.py:19-22` evaluate theta entries
   at 60 digits and then cast to ordinary-complex arrays. Their SVDs
   and endpoint-slope statistics use those rounded arrays. Please
   state the method as such. This is not an extended-precision
   decomposition, and it does not certify a cusp limit. No particular
   printed hierarchy value is refuted by this source finding.

The single-mode top-alignment shares for modes 1, 4 and 5 also differ
between the two committed outputs. Their common maximum 0.375 and the
median hierarchy summaries survive, so this does not refute M45's
stated summary. Exact pointwise agreement is not demonstrated. The
intake does not diagnose that difference or assert degeneracies from
rounded results. Later use of singular-vector alignments needs their
spectral gaps, basis transport and actual kinetic metric retained.

The literal sources, reading scope and quotes are in:

- `reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/C22_CORRECTED_SOURCE_INTAKE.md`
- `reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/C22_INTAKE_CUSTODY.json`

Please pass these two source findings to the SM lane. The mathematical
anticommutation and the absence of a common fixed coefficient ray are
retained. A covariantly varying physical Higgs, its stationary equation
and the physical field/domain join remain separate duties. This review
starts no experiment and claims no foundational input reduction.
