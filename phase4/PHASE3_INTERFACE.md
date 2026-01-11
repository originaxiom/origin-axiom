# Phase 3–Phase 4 interface (baseline mechanism and artifacts)

Status: **DRAFT / non-binding**

This note records how Phase 4 depends on the Phase 3 vacuum mechanism
and its artifacts at the current rung. It is intended to make the
hand-off between phases explicit and auditable.

## 1. Upstream Phase 3 mechanism and artifacts

Phase 3 defines a toy global-amplitude vacuum mechanism whose core
implementation lives in the Phase 3 source tree, in particular:

- `phase3/src/phase3_mech/`:
  - the vacuum configuration and amplitude sampler;
  - the quantile-based non-cancellation floor used to enforce a
    binding regime.

The following Phase 3 artifacts are relevant for Phase 4:

1. **Baseline scan diagnostics**  
   Produced by running
   `phase3/src/phase3_mech/run_baseline_scan.py`, which writes:
   - `phase3/outputs/tables/mech_baseline_scan.csv`
   - `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`

   The diagnostics JSON records:
   - the chosen floor \(\varepsilon_{\mathrm{floor}}\);
   - the grid size \(N_\theta\);
   - the \(\theta\)-range \([0, 2\pi)\);
   - basic quantiles and extrema of the unconstrained amplitude.

2. **Binding-certificate diagnostics (Phase 3)**  
   Produced by `phase3/src/phase3_mech/run_binding_certificate.py`,
   which writes:
   - `phase3/outputs/tables/mech_binding_certificate.csv`
   - `phase3/outputs/tables/mech_binding_certificate_diagnostics.json`

   These artifacts establish that the Phase 3 floor produces a
   non-trivial, globally binding regime for the toy mechanism, in the
   sense of Phase 0.

At the present rung, Phase 4 uses only the **baseline scan diagnostics**
explicitly, but is conceptually downstream of both the baseline and
binding-certificate work.

## 2. Phase 4 F1 mapping and diagnostics

Phase 4 introduces the F1 mapping family, implemented in
`phase4/src/phase4/mappings_f1.py`, which:

- reuses the Phase 3 vacuum and floor to compute amplitudes
  \(A(\theta)\) on a grid;
- defines a scalar
  \[
    E_{\mathrm{vac}}(\theta) = \alpha A(\theta)^{\beta} > 0,
  \]
  for configurable \((\alpha, \beta)\);
- records metadata about the Phase 3 baseline diagnostics it was built
  from.

Downstream diagnostics currently include:

1. **F1 sanity curve**  
   `phase4/src/phase4/run_f1_sanity.py` writes:
   - `phase4/outputs/tables/phase4_F1_sanity_curve.csv`

   and logs:

   - the mapping parameters \((\alpha, \beta)\);
   - the Phase 3 baseline diagnostics loaded from
     `mech_baseline_scan_diagnostics.json`.

2. **F1 shape diagnostics and toy corridor**  
   `phase4/src/phase4/run_f1_shape_diagnostics.py` writes:
   - `phase4/outputs/tables/phase4_F1_shape_diagnostics.json`
   - `phase4/outputs/tables/phase4_F1_shape_mask.csv`

   The JSON file records:
   - global extrema and moments of \(E_{\mathrm{vac}}(\theta)\);
   - the definition of a toy, non-binding corridor
     \[
       E_{\mathrm{vac}}(\theta) \le
       E_{\mathrm{vac},\min} + k_\sigma \sigma
       \quad (k_\sigma = 1),
     \]
   - the fraction of the grid inside this corridor and its induced
     \(\theta\)-range.

   The mask CSV provides a per-grid indicator that can be reused by
   later rungs and by any toy FRW-like modules.

## 3. Rebuild chain (conceptual)

Putting the above together, the current conceptual pipeline is:

1. **Phase 3 vacuum + floor**  
   \(\Rightarrow\) baseline amplitude diagnostics  
   (`mech_baseline_scan_diagnostics.json`)

2. **Baseline diagnostics + mechanism**  
   \(\Rightarrow\) F1 scalar
   \(E_{\mathrm{vac}}(\theta)\)  
   (`phase4_F1_sanity_curve.csv`)

3. **F1 scalar**  
   \(\Rightarrow\) shape diagnostics and toy, non-binding corridor  
   (`phase4_F1_shape_diagnostics.json`,
    `phase4_F1_shape_mask.csv`)

4. **F1 scalar + corridor (design)**  
   \(\Rightarrow\) FRW-like toy diagnostics (planned)  
   (see `phase4/FRW_TOY_DESIGN.md`)

Only steps (1)–(3) are implemented at this rung. Step (4) is a design
target and may evolve or be retired if it proves unhelpful.

## 4. Non-claims

This interface note does **not** promote any Phase 4 output to a
binding \(\theta\)-filter, nor does it claim that the F1 mapping or the
Phase 3 mechanism are realised in nature. It records technical
dependencies so that future refactors, Phase 3 variants, or additional
mapping families can be audited against a clear upstream/downstream
contract.

---

Doc status: Phase 3–Phase 4 interface design note (draft); explains how Phase 3 mechanism outputs feed Phase 4 FRW constructions; descriptive and non-binding; interpretation is governed by `phase4/PHASE4_ALIGNMENT_v1.md` and does not override Phase 3 or Phase 4 claims registers.
