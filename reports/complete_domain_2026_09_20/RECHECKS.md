# F02 execution and source receipt

2026-09-20. These are transcriptions of tool outputs, not byte-for-byte raw
logs. No scientific source was modified during a running check. F02's four
sealed files remained unchanged. Other seats' files were neither patched
nor imported as new work. No independent banking or full-suite run occurred.

## First F02 execution

Input commit `09f41662`, Python 3.12.1, SymPy 1.14.0.
All four SHA256 digests were checked before the first run and again after it.

```
python3.12 -m pytest -q reports/complete_domain_2026_09_20/test_verify.py
```

Process 13307, final chunk `6bd988`, exit 0:

```
16 passed in 1.86s
```

These are finite controls. The complete-space proof uses local elliptic
regularity, compactly supported graph approximation and a complete-metric
cutoff exhaustion. Those analytic facts are not certified by pytest.

## Unchanged antecedent checks: retain the failure

```
python3.12 -m pytest -q \
  tests/test_physical_bridge_source_action.py \
  tests/test_physical_bridge_global_singular.py::test_cutoff_flux_is_nonzero_and_constant_cutoff_is_zero \
  tests/test_physical_bridge_global_singular.py::test_scalar_gap_and_geodesic_source_normalization_identities \
  tests/test_physical_bridge_global_singular.py::test_mean_repair_uses_actual_area_and_leaves_flow_freedom \
  tests/test_physical_bridge_charged_domain.py::test_nonzero_green_form_and_distinct_complex_domains
```

Process 93029, final chunk `e77e2d`, **exit 1**:

```
FAILED tests/test_physical_bridge_charged_domain.py::test_nonzero_green_form_and_distinct_complex_domains
1 failed, 23 passed in 24.74s
```

Failure at line 94: `assert out['capacity_energy_identity'] == 0`.
The returned expression still contained unevaluated `Integral` and `Piecewise`
terms. This is not numerical evidence of a nonzero residual. The Green-pair
and domain-cutoff assertions earlier in the same test completed successfully;
the later normalization assertion was not reached. No rerun was relabeled
as an original pass and the old test remains unchanged.

The [post-failure diagnostic](R16_DIAGNOSTIC.md) and its independent primitive
check were committed at `d7490ab9` before execution. Command:

```
python3.12 reports/complete_domain_2026_09_20/r16_capacity_diagnostic.py
```

Tool chunk `8049ab`, exit 0, SymPy 1.14.0: all four derivative/endpoint
residuals exactly zero, half-primitive mutant rejected, rational capacity
control `3/25`. This establishes the elementary integral identity without
asking the definite integrator to find it. It does not turn the original
red test green. The evidence supports a symbolic-evaluation failure in that
recheck, not a refutation of R16's capacity formula or the complete-space
domain theorem. No dependency upgrade/downgrade was attempted.

## Personal readings and boundaries

- R15 global construction and homogeneous freedom; its `parametrix_identities`
  producer and the whole global-singular test file.
- R28 action/norm material already read in the resweep; no new energy
  functional was substituted here.
- R30 proof section 1 for the quadratic fermion dictionary and explicit
  compact-regulator domain. This is not a rerun of all R30 results.
- R16 normal-domain discussion, Green-form/capacity producer and selected
  test. The old indefinite/definite integration failure is recorded above.
- B739 findings, convention and function-level proof blocks; its full three-
  test file. Three tests passed, recorded in the separate
  [scattering recovery](../report_guided_resweep_2026_09_20/SCATTERING_RECOVERY.md).
- Braun et al. 1812.06072v2, HTML equations (2.9)--(2.18) and
  (2.34)--(2.44), personally reread; not a new full-paper reading.
- Wolf's scanned PDF: printed pp. 611 and 621--625 rendered and visually
  read, including the whole Theorem 5.1 proof. Theorem 6.1's proof continues
  beyond this reading and is not claimed as fully reviewed here.
- Sarnak's scanned PDF: printed pp. 258--260 and 264 rendered and visually
  read; page-257 unit restriction checked in text. These are source pages
  for the separate scalar scattering recovery, not a spin-2 computation.
- Chernoff publisher abstract and Thaller's author abstract inspected;
  Thaller's TeX request failed. Neither full paper was read or used as an
  uninspected theorem whose precise hypotheses substitute for F02's proof.

The PDF skill determined the render-and-inspect workflow. Browser screenshots
failed; public PDFs downloaded to temporary storage and local Poppler rendering
succeeded. Initial sandbox DNS failures were followed by approved public
downloads. No private data were uploaded. Download checksums:

```
sarnak.pdf  c2d8b30d045f75e0ba0242151993c21809db5c46de8912057bfa13af901e38ab
wolf.pdf    c9c70f8e70358559ba87e9c2d4d66237c845c4173df9ad45f1c9674d731cde0f
```

## Scientific status

The standard domain theorem is recorded as an authored argument with exact
controls, not an independent expert review. Its smoothness, completeness,
positive metric and operator-identification hypotheses are explicit. A
fixed external background is not a dynamical choice of vacuum. Nothing
here certifies a globally admissible nonsplit background or the complete
physical theory.
