
# Phase 2 Structural Audit (P2-A1)

- Generated: 2026-01-04 12:35:50 +0100
- Git: 7ff4e0e (phase0-2-alignment)
- Repo: /Users/dri/Documents/Projects/origin-axiom

## 1) High-level inventory

```
total 152
drwxr-xr-x@ 23 dri  staff    736 Jan  4 12:18 .
drwx------@ 16 dri  staff    512 Jan  4 12:19 ..
-rw-r--r--@  1 dri  staff   6148 Jan  2 18:26 .DS_Store
-rw-r--r--   1 dri  staff    366 Jan  4 08:07 .gitignore
drwxr-xr-x  12 dri  staff    384 Jan  3 13:46 .snakemake
-rw-r--r--   1 dri  staff   5823 Dec 31 14:40 APPROXIMATION_CONTRACT.md
-rw-r--r--   1 dri  staff   3775 Dec 31 14:40 ASSUMPTIONS.md
-rw-r--r--@  1 dri  staff    191 Jan  4 12:35 AUDIT_REPORT.md
-rw-r--r--   1 dri  staff  10019 Jan  4 08:54 CLAIMS.md
-rw-r--r--   1 dri  staff   1386 Jan  4 08:16 CLAIMS_TABLE.md
-rw-r--r--   1 dri  staff   2199 Jan  4 08:59 PHASE2_LOCK_CHECKLIST.md
-rw-r--r--   1 dri  staff   2758 Dec 31 14:40 PHASE2_WORKFLOW_GUIDE.md
-rw-r--r--   1 dri  staff   6805 Jan  4 09:09 PROGRESS_LOG.md
-rw-r--r--   1 dri  staff   1032 Dec 31 14:40 README.md
-rw-r--r--   1 dri  staff   2868 Dec 31 14:40 REPRODUCIBILITY.md
-rw-r--r--   1 dri  staff   3236 Dec 31 14:40 SCOPE.md
drwxr-xr-x   5 dri  staff    160 Jan  4 06:59 _paper_backups
drwxr-xr-x   5 dri  staff    160 Jan  2 19:40 config
drwxr-xr-x   8 dri  staff    256 Jan  4 09:00 outputs
drwxr-xr-x  20 dri  staff    640 Jan  4 12:35 paper
-rw-r--r--   1 dri  staff    135 Jan  3 23:20 pyproject.toml
drwx------   5 dri  staff    160 Jan  2 20:42 src
drwxr-xr-x   3 dri  staff     96 Jan  2 19:40 workflow
```

## 2) Presence checks (non-fatal)
- OK: phase2/README.md
- OK: phase2/SCOPE.md
- OK: phase2/CLAIMS.md
- OK: phase2/ASSUMPTIONS.md
- OK: phase2/REPRODUCIBILITY.md
- OK: phase2/PROGRESS_LOG.md
- OK: phase2/pyproject.toml

## 3) Directory tree (depth 4)

```
/Users/dri/Documents/Projects/origin-axiom/phase2
/Users/dri/Documents/Projects/origin-axiom/phase2/paper
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/appendix
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/appendix/A_run_manifest.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/08_conclusion.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/01_introduction.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/00_abstract.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.bbl
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/.DS_Store
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/macros.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/references.bib
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.toc
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.out
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/.gitignore
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/figures/figB_scaling_epsilon.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/figures/figC_scaling_cutoff.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/figures/figE_frw_comparison.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/figures/figD_scaling_modes.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/figures/figA_mode_sum_residual.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.fdb_latexmk
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.aux
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.log
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.fls
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.blg
/Users/dri/Documents/Projects/origin-axiom/phase2/.DS_Store
/Users/dri/Documents/Projects/origin-axiom/phase2/config
/Users/dri/Documents/Projects/origin-axiom/phase2/config/phase2.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/config/phase2_binding_off.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/config/phase2_binding_on.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/SCOPE.md
/Users/dri/Documents/Projects/origin-axiom/phase2/pyproject.toml
/Users/dri/Documents/Projects/origin-axiom/phase2/ASSUMPTIONS.md
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS_TABLE.md
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/locks
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/conda
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/incomplete
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/shadow
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/iocache
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/conda-archive
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/singularity
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/log
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/log/2026-01-03T134601.941872.snakemake.log
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQl9zY2FsaW5nX2Vwc2lsb24ucnVuX2lkLnR4dA==
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnRV9mcndfY29tcGFyaXNvbi5ydW5faWQudHh0
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQl9zY2FsaW5nX2Vwc2lsb24ucGRm
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQ19zY2FsaW5nX2N1dG9mZi5wZGY=
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQ19zY2FsaW5nX2N1dG9mZi5zaWcudHh0
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQV9tb2RlX3N1bV9yZXNpZHVhbC5ydW5faWQudHh0
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQ19zY2FsaW5nX2N1dG9mZi5ydW5faWQudHh0
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnRV9mcndfY29tcGFyaXNvbi5wZGY=
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnRF9zY2FsaW5nX21vZGVzLnNpZy50eHQ=
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQV9tb2RlX3N1bV9yZXNpZHVhbC5zaWcudHh0
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnRF9zY2FsaW5nX21vZGVzLnBkZg==
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnRF9zY2FsaW5nX21vZGVzLnJ1bl9pZC50eHQ=
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQV9tb2RlX3N1bV9yZXNpZHVhbC5wZGY=
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnRV9mcndfY29tcGFyaXNvbi5zaWcudHh0
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/metadata/L1VzZXJzL2RyaS9Eb2N1bWVudHMvUHJvamVjdHMvb3JpZ2luLWF4aW9tL3BoYXNlMi9vdXRwdXRzL2ZpZ3VyZXMvZmlnQl9zY2FsaW5nX2Vwc2lsb24uc2lnLnR4dA==
/Users/dri/Documents/Projects/origin-axiom/phase2/.snakemake/auxiliary
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md
/Users/dri/Documents/Projects/origin-axiom/phase2/.gitignore
/Users/dri/Documents/Projects/origin-axiom/phase2/workflow
/Users/dri/Documents/Projects/origin-axiom/phase2/workflow/Snakefile
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md
/Users/dri/Documents/Projects/origin-axiom/phase2/APPROXIMATION_CONTRACT.md
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/appendix
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/appendix/A_run_manifest.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/08_conclusion.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/01_introduction.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/00_abstract.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/07_limitations_and_nonclaims.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/04_claim_C22_robustness.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/02_model_definition.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/03_claim_C21_existence.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/05_claim_C23_frw_viability.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/macros.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/references.bib
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/main.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/08_conclusion.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/06_frw_implications.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/01_introduction.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/02_framework_and_axiom.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/07_limitations_and_scope.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/04_numerical_experiments.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/05_results_scaling.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/03_mode_sum_model.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/macros.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/references.bib
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/main.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/.DS_Store
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/config
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/config/phase2.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/figures/figB_scaling_epsilon.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/figures/figC_scaling_cutoff.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/figures/figE_frw_comparison.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/figures/figD_scaling_modes.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/figures/figA_mode_sum_residual.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/run_index.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/runs
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/runs/figE_frw_comparison_20251228T012841Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/runs/figA_mode_sum_residual_20251228T012847Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/runs/figB_scaling_epsilon_20251228T012843Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/runs/figD_scaling_modes_20251228T012845Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/runs/figC_scaling_cutoff_20251228T012839Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/phase2_binding_certificate.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/binding_off.run_id.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/phase2_binding_certificate 2.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z 2
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_08.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_04.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_05.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_09.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_02.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_03.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_00.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_01.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_06.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251231T124831Z/eps_07.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/binding_on.run_id.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/outputs
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/outputs/runs
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251229T151140Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/_tmp_cfg_20251229T151140Z/eps_00.yaml
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/release
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/release/phase2_release_20260104T080055Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figB_scaling_epsilon.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figC_scaling_cutoff.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figB_scaling_epsilon.sig.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figE_frw_comparison.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figF_binding_certificate.sig 2.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figF_binding_certificate.meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figF_binding_certificate.meta 2.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figA_mode_sum_residual.sig.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figD_scaling_modes.sig.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figD_scaling_modes.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figC_scaling_cutoff.run_id.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figA_mode_sum_residual.run_id.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figC_scaling_cutoff.sig.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figD_scaling_modes.run_id.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figE_frw_comparison.sig.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figE_frw_comparison.run_id.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figB_scaling_epsilon.run_id.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figF_binding_certificate.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figF_binding_certificate.sig.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figA_mode_sum_residual.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/figures/figF_binding_certificate 2.pdf
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_on_20251229T151136Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_on_20251229T151136Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_on_20251229T151136Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_on_20251229T151136Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_on_20251229T151136Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_on_20251229T151136Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_on_20251229T151136Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20260103T124604Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20260103T124604Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20260103T124604Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20260103T124604Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20260103T124604Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20260103T124604Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20260103T124604Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124452Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124452Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124452Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124452Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124452Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124452Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124452Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20251228T012841Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20251228T012841Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20251228T012841Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20251228T012841Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20251228T012841Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20251228T012841Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20251228T012841Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20260103T124609Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20260103T124609Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20260103T124609Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20260103T124609Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20260103T124609Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20260103T124609Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20260103T124609Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20251228T012847Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20251228T012847Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20251228T012847Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20251228T012847Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20251228T012847Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20251228T012847Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figA_mode_sum_residual_20251228T012847Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20251228T012843Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20251228T012843Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20251228T012843Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20251228T012843Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20251228T012843Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20251228T012843Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figB_scaling_epsilon_20251228T012843Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20260103T124606Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20260103T124606Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20260103T124606Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20260103T124606Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20260103T124606Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20260103T124606Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20260103T124606Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T094505Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T094505Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T094505Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T094505Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T094505Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T094505Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T094505Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20251228T012845Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20251228T012845Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20251228T012845Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20251228T012845Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20251228T012845Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20251228T012845Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20251228T012845Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T094505Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T094505Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T094505Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T094505Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T094505Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T094505Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T094505Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20251228T012839Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20251228T012839Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20251228T012839Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20251228T012839Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20251228T012839Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20251228T012839Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figC_scaling_cutoff_20251228T012839Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_off_20251229T151136Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_off_20251229T151136Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_off_20251229T151136Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_off_20251229T151136Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_off_20251229T151136Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_off_20251229T151136Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/phase2_cert_off_20251229T151136Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20260103T124607Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20260103T124607Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20260103T124607Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20260103T124607Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20260103T124607Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20260103T124607Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figE_frw_comparison_20260103T124607Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124505Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124505Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124505Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124505Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124505Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124505Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/residual_test_20251231T124505Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T103250Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T103250Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T103250Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T103250Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T103250Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T103250Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_off_20251229T103250Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20260103T124602Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20260103T124602Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20260103T124602Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20260103T124602Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20260103T124602Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20260103T124602Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/figD_scaling_modes_20260103T124602Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T103250Z
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T103250Z/summary.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T103250Z/pip_freeze.txt
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T103250Z/params_resolved.json
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T103250Z/figures
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T103250Z/raw
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/runs/test_binding_on_20251229T103250Z/meta.json
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md
/Users/dri/Documents/Projects/origin-axiom/phase2/src
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/run_sweep.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/mode_model.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/__init__.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/run_mode_sum.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/__pycache__
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/test_constraints.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/constraints.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/observables.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/__init__.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/__pycache__
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/__pycache__/observables.cpython-312.pyc
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/__pycache__/utils_meta.cpython-312.pyc
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/__pycache__/__init__.cpython-312.pyc
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/utils_meta.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/__init__.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/__pycache__
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/binding_sweep_eps.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/make_fig_binding_certificate.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/make_fig_binding_certificate 2.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/certify_binding.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/cosmology
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/cosmology/__init__.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/cosmology/__pycache__
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/cosmology/run_frw.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/observables.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/__init__.py
/Users/dri/Documents/Projects/origin-axiom/phase2/src/__pycache__
/Users/dri/Documents/Projects/origin-axiom/phase2/src/__pycache__/__init__.cpython-312.pyc
```

## 4) TODO / FIXME / XXX / TBD sweep

```
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:389:## 4) TODO / FIXME / XXX / TBD sweep
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/main.tex:68:% TODO (150--250 words):
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:80:- Added `scripts/phase2_paper_lint.sh` to enforce: no TODO/FIXME/XXX/TBD in Phase 2 paper, and clean build log scan.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/macros.tex:117:\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex:2:% TODO:
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/07_limitations_and_scope.tex:2:% TODO
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/06_frw_implications.tex:4:% TODO: define mapping residual -> \OLeff via explicit parameter in config.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/08_conclusion.tex:2:% TODO
```

## 5) Paper build + structure

### 5.1 Paper directory listing

```
total 1336
drwxr-xr-x  20 dri  staff     640 Jan  4 12:35 .
drwxr-xr-x@ 23 dri  staff     736 Jan  4 12:18 ..
-rw-r--r--@  1 dri  staff    6148 Dec 31 14:10 .DS_Store
-rw-r--r--   1 dri  staff     128 Jan  4 08:13 .gitignore
-rw-r--r--   1 dri  staff    1537 Jan  4 08:14 PAPER_CONTRACT.md
drwxr-xr-x   3 dri  staff      96 Jan  4 08:19 appendix
drwxr-xr-x   7 dri  staff     224 Jan  2 19:40 figures
-rw-r--r--@  1 dri  staff    3763 Jan  4 11:36 macros.tex
-rw-r--r--@  1 dri  staff   14216 Jan  4 12:35 main.aux
-rw-r--r--   1 dri  staff     609 Jan  4 12:35 main.bbl
-rw-r--r--   1 dri  staff     950 Jan  4 12:35 main.blg
-rw-r--r--@  1 dri  staff   20802 Jan  4 12:35 main.fdb_latexmk
-rw-r--r--   1 dri  staff   21869 Jan  4 12:35 main.fls
-rw-r--r--@  1 dri  staff   30655 Jan  4 12:35 main.log
-rw-r--r--@  1 dri  staff   11777 Jan  4 12:35 main.out
-rw-r--r--@  1 dri  staff  506236 Jan  4 12:35 main.pdf
-rw-r--r--@  1 dri  staff    3410 Jan  4 11:40 main.tex
-rw-r--r--@  1 dri  staff    5473 Jan  4 12:35 main.toc
-rw-r--r--@  1 dri  staff    3013 Jan  4 11:26 references.bib
drwxr-xr-x  12 dri  staff     384 Jan  4 12:10 sections
```

### 5.2 main.tex spine (inputs/includes)

```
No inputs/includes found (or different structure).
```

### 5.3 Labels / refs / cites quick stats

```
labels:
26
refs:
44
cites:
4
```

### 5.4 Build attempt (latexmk) + hygiene checks

```
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
No existing .aux file, so I'll make a simple one, and require run of *latex.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Category 'other':
  Rerun of 'pdflatex' forced or previously required:
    Reason or flag: 'Initial setup'

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -halt-on-error -recorder  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/article.cls
Document Class: article 2024/06/29 v1.4n Standard LaTeX document class
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/size11.clo))
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amscls/amsthm.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/mathtools/mathtools.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/calc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/mathtools/mhsetup.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/caption.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
ty (/usr/local/texlive/2025/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/local/texlive/2025/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/local/texlive/2025/texmf-dist/tex/latex/url/url.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/atbegshi-ltx.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/atveryend-ltx.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty

(/usr/local/texlive/2025/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
))) (./macros.tex)
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./main.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/local/texlive/2025/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msb.cfg)
(./sections/00_abstract.tex

LaTeX Warning: Reference `fig:mode_sum_residual' on page 1 undefined on input l
ine 13.


LaTeX Warning: Reference `fig:scaling_epsilon' on page 1 undefined on input lin
e 14.


LaTeX Warning: Reference `fig:scaling_modes' on page 1 undefined on input line 
14.


LaTeX Warning: Reference `fig:frw_comparison' on page 1 undefined on input line
 15.

)
No file main.toc.
(./sections/01_introduction.tex
[1{/usr/local/texlive/2025/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/l
ocal/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t1.enc}]

LaTeX Warning: Citation `weinberg1989cc' on page 2 undefined on input line 16.


LaTeX Warning: Citation `carroll2001cc' on page 2 undefined on input line 16.


LaTeX Warning: Citation `planck2018params' on page 2 undefined on input line 18
.


LaTeX Warning: Citation `weinberg1989cc' on page 2 undefined on input line 19.


LaTeX Warning: Citation `carroll2001cc' on page 2 undefined on input line 19.


LaTeX Warning: Citation `dodelson2003modern' on page 2 undefined on input line 
44.


LaTeX Warning: Citation `ryden2017intro' on page 2 undefined on input line 44.


LaTeX Warning: Reference `sec:discussion' on page 2 undefined on input line 46.



[2]

LaTeX Warning: Reference `sec:framework' on page 3 undefined on input line 52.


LaTeX Warning: Reference `sec:claim_c21' on page 3 undefined on input line 53.


LaTeX Warning: Reference `sec:claim_c23' on page 3 undefined on input line 53.


LaTeX Warning: Reference `sec:reproducibility' on page 3 undefined on input lin
e 54.


LaTeX Warning: Reference `sec:discussion' on page 3 undefined on input line 54.


) (./sections/02_model_definition.tex

LaTeX Warning: Reference `eq:uniform_shift' on page 3 undefined on input line 5
0.


[3]

LaTeX Warning: Reference `eq:floor_constraint' on page 4 undefined on input lin
e 73.


LaTeX Warning: Reference `eq:uniform_shift' on page 4 undefined on input line 8
1.


LaTeX Warning: Reference `eq:floor_constraint' on page 4 undefined on input lin
e 97.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 99.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 99.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 99.


[4{/usr/local/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-ts1.enc
}]

LaTeX Warning: Reference `eq:floor_constraint' on page 5 undefined on input lin
e 124.


LaTeX Warning: Reference `sec:reproducibility' on page 5 undefined on input lin
e 134.


LaTeX Warning: Reference `app:run_manifest' on page 5 undefined on input line 1
34.

) (./sections/03_claim_C2_1_existence.tex

LaTeX Warning: Reference `fig:mode_sum_residual' on page 5 undefined on input l
ine 17.


LaTeX Warning: Reference `app:run_manifest' on page 5 undefined on input line 1
7.


[5]

LaTeX Warning: Reference `eq:uniform_shift' on page 6 undefined on input line 2
3.


LaTeX Warning: Reference `app:run_manifest' on page 6 undefined on input line 2
6.


LaTeX Warning: Reference `fig:mode_sum_residual' on page 6 undefined on input l
ine 29.


LaTeX Warning: Reference `eq:uniform_shift' on page 6 undefined on input line 4
5.


LaTeX Warning: Reference `eq:floor_constraint' on page 6 undefined on input lin
e 46.


[6 <./figures/figA_mode_sum_residual.pdf>])
(./sections/04_claim_C2_2_robustness.tex

LaTeX Warning: Reference `fig:scaling_epsilon' on page 7 undefined on input lin
e 17.


LaTeX Warning: Reference `fig:scaling_modes' on page 7 undefined on input line 
17.


LaTeX Warning: Reference `app:run_manifest' on page 7 undefined on input line 1
7.


LaTeX Warning: Reference `sec:claim_c21' on page 7 undefined on input line 20.


LaTeX Warning: Reference `fig:scaling_epsilon' on page 7 undefined on input lin
e 24.


LaTeX Warning: Reference `fig:scaling_cutoff' on page 7 undefined on input line
 25.


Overfull \hbox (3.43513pt too wide) in paragraph at lines 25--26
[]\T1/cmr/bx/n/10.95 (-20) UV/discretization con-trol sweep: \T1/cmr/m/n/10.95 
(-20) vary the implementation-defined ul-tra-vi-o-let/discretization

LaTeX Warning: Reference `fig:scaling_modes' on page 7 undefined on input line 
26.


LaTeX Warning: Reference `eq:deltaE_def' on page 7 undefined on input line 28.


LaTeX Warning: Reference `app:run_manifest' on page 7 undefined on input line 2
8.


Overfull \hbox (2.07161pt too wide) in paragraph at lines 28--29
\T1/cmr/m/n/10.95 (-20) For each fam-ily, the re-ported quan-tity is the resid-
ual en-ergy proxy $\OT1/cmr/m/n/10.95 (-20) ^^A\OML/cmm/m/it/10.95 E$ \T1/cmr/m
/n/10.95 (-20) (Eq. []) or its implementation-

LaTeX Warning: Reference `fig:scaling_epsilon' on page 7 undefined on input lin
e 43.


LaTeX Warning: Reference `fig:scaling_cutoff' on page 7 undefined on input line
 58.


LaTeX Warning: Reference `fig:scaling_modes' on page 7 undefined on input line 
73.


[7]

LaTeX Warning: Reference `fig:scaling_epsilon' on page 8 undefined on input lin
e 81.


LaTeX Warning: Reference `fig:scaling_cutoff' on page 8 undefined on input line
 84.


LaTeX Warning: Reference `fig:scaling_modes' on page 8 undefined on input line 
84.

) (./sections/05_claim_C2_3_frw_viability.tex

LaTeX Warning: Reference `fig:frw_comparison' on page 8 undefined on input line
 18.


LaTeX Warning: Reference `app:run_manifest' on page 8 undefined on input line 1
8.


[8 <./figures/figB_scaling_epsilon.pdf>]

LaTeX Warning: Reference `eq:deltaE_def' on page 9 undefined on input line 21.


LaTeX Warning: Reference `app:run_manifest' on page 9 undefined on input line 2
8.


[9 <./figures/figC_scaling_cutoff.pdf>]

LaTeX Warning: Reference `fig:frw_comparison' on page 10 undefined on input lin
e 40.


LaTeX Warning: Reference `app:run_manifest' on page 10 undefined on input line 
40.


LaTeX Warning: Reference `fig:frw_comparison' on page 10 undefined on input lin
e 60.


[10 <./figures/figD_scaling_modes.pdf>]

LaTeX Warning: Reference `app:run_manifest' on page 11 undefined on input line 
75.

) (./sections/06_reproducibility_and_provenance.tex

LaTeX Warning: Reference `app:run_manifest' on page 11 undefined on input line 
13.


[11]

LaTeX Warning: Reference `app:run_manifest' on page 12 undefined on input line 
31.


[12]) (./sections/07_limitations_and_scope.tex

LaTeX Warning: Reference `sec:framework' on page 13 undefined on input line 11.



[13]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\star' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 35.


LaTeX Warning: Reference `app:run_manifest' on page 14 undefined on input line 
43.


LaTeX Warning: Reference `sec:reproducibility' on page 14 undefined on input li
ne 43.


[14]) (./sections/08_conclusion.tex

LaTeX Warning: Reference `sec:discussion' on page 15 undefined on input line 8.



LaTeX Warning: Reference `fig:mode_sum_residual' on page 15 undefined on input 
line 14.


LaTeX Warning: Reference `fig:scaling_epsilon' on page 15 undefined on input li
ne 17.


LaTeX Warning: Reference `fig:scaling_modes' on page 15 undefined on input line
 17.


LaTeX Warning: Reference `fig:frw_comparison' on page 15 undefined on input lin
e 20.


LaTeX Warning: Reference `sec:framework' on page 15 undefined on input line 28.



LaTeX Warning: Reference `sec:reproducibility' on page 15 undefined on input li
ne 32.


LaTeX Warning: Reference `app:run_manifest' on page 15 undefined on input line 
32.

)
[15] (./appendix/A_run_manifest.tex
Overfull \hbox (12.46654pt too wide) in paragraph at lines 10--21
 [] 
) (./sections/A_provenance.tex

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


LaTeX Warning: Reference `app:run_manifest' on page 16 undefined on input line 
20.


[16]
Overfull \hbox (18.50665pt too wide) in paragraph at lines 59--64
\T1/cmr/m/n/10.95 (-20) (i) re-gen-er-ates nu-mer-i-cal out-puts un-der \T1/cmt
t/m/n/10.95 outputs/\T1/cmr/m/n/10.95 (-20) , (ii) re-builds canon-i-cal fig-ur
es un-der \T1/cmtt/m/n/10.95 outputs/figures/\T1/cmr/m/n/10.95 (-20) ,

Overfull \hbox (17.92433pt too wide) in paragraph at lines 59--64
\T1/cmr/m/n/10.95 (-20) (iii) stages sub-mis-sion fig-ures un-der \T1/cmtt/m/n/
10.95 phase2/paper/figures/\T1/cmr/m/n/10.95 (-20) , and (iv) com-piles \T1/cmt
t/m/n/10.95 phase2/paper/main.tex
) (./main.bbl
[17])
[18]
[19 <./figures/figE_frw_comparison.pdf>] (./main.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `main.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)</usr/local/texlive/2025/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb></usr/local/texlive/2025/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb></usr/local/texlive/2025/texmf
-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb></usr/local/texlive/2025/texmf-
dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb></usr/local/texlive/2025/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi12.pfb></usr/local/texlive/2025/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi7.pfb></usr/local/texlive/2025/texmf-dist
/fonts/type1/public/amsfonts/cm/cmmi8.pfb></usr/local/texlive/2025/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr10.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr8.pfb></usr/local/texlive/2025/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb></usr/local/texlive/2025/texmf-dist/fonts/t
ype1/public/amsfonts/symbols/msam10.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/amsfonts/symbols/msbm10.pfb></usr/local/texlive/2025/texmf-dist
/fonts/type1/public/cm-super/sfbx1000.pfb></usr/local/texlive/2025/texmf-dist/f
onts/type1/public/cm-super/sfbx1095.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/cm-super/sfbx1200.pfb></usr/local/texlive/2025/texmf-dist/fonts
/type1/public/cm-super/sfbx1440.pfb></usr/local/texlive/2025/texmf-dist/fonts/t
ype1/public/cm-super/sfcc1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/typ
e1/public/cm-super/sfrm0800.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1
/public/cm-super/sfrm1000.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/p
ublic/cm-super/sfrm1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/pub
lic/cm-super/sfrm1200.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/publi
c/cm-super/sfrm1728.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/
cm-super/sfti1000.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/cm
-super/sfti1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/cm-s
uper/sftt1095.pfb>
Output written on main.pdf (19 pages, 494727 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Missing input file 'main.toc' (or dependence on it) from following:
  No file main.toc.
Latexmk: Found input bbl file 'main.bbl'
Latexmk: References changed.
Latexmk: References changed.
Latexmk: Log file says output to 'main.pdf'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: applying rule 'bibtex main'...
Rule 'bibtex main':  Reasons for rerun
Category 'other':
  Rerun of 'bibtex main' forced or previously required:
    Reason or flag: 'Initial set up of rule'

------------
Run number 1 of rule 'bibtex main'
------------
------------
Running 'bibtex  "main.aux"'
------------
This is BibTeX, Version 0.99d (TeX Live 2025)
The top-level auxiliary file: main.aux
The style file: unsrt.bst
Database file #1: references.bib
Warning--I didn't find a database entry for "weinberg1989cc"
(There was 1 warning)
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  main.aux
  main.out
  main.toc

------------
Run number 2 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -halt-on-error -recorder  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/article.cls
Document Class: article 2024/06/29 v1.4n Standard LaTeX document class
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/size11.clo))
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amscls/amsthm.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/mathtools/mathtools.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/calc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/mathtools/mhsetup.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/caption.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
ty (/usr/local/texlive/2025/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/local/texlive/2025/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/local/texlive/2025/texmf-dist/tex/latex/url/url.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/atbegshi-ltx.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/atveryend-ltx.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty

(/usr/local/texlive/2025/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
))) (./macros.tex)
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./main.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/local/texlive/2025/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./main.out) (./main.out)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msb.cfg)
(./sections/00_abstract.tex) (./main.toc
[1{/usr/local/texlive/2025/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/l
ocal/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t1.enc}])
(./sections/01_introduction.tex
[2]

LaTeX Warning: Citation `weinberg1989cc' on page 3 undefined on input line 16.


LaTeX Warning: Citation `weinberg1989cc' on page 3 undefined on input line 19.


[3]) (./sections/02_model_definition.tex
[4]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 99.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 99.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 99.


[5{/usr/local/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-ts1.enc
}]) (./sections/03_claim_C2_1_existence.tex
[6]) (./sections/04_claim_C2_2_robustness.tex
[7]
Overfull \hbox (3.43513pt too wide) in paragraph at lines 25--26
[]\T1/cmr/bx/n/10.95 (-20) UV/discretization con-trol sweep: \T1/cmr/m/n/10.95 
(-20) vary the implementation-defined ul-tra-vi-o-let/discretization

Overfull \hbox (1.14455pt too wide) in paragraph at lines 28--29
\T1/cmr/m/n/10.95 (-20) For each fam-ily, the re-ported quan-tity is the resid-
ual en-ergy proxy $\OT1/cmr/m/n/10.95 (-20) ^^A\OML/cmm/m/it/10.95 E$ \T1/cmr/m
/n/10.95 (-20) (Eq. []) or its implementation-

[8 <./figures/figA_mode_sum_residual.pdf>]
[9 <./figures/figB_scaling_epsilon.pdf>])
(./sections/05_claim_C2_3_frw_viability.tex
[10 <./figures/figC_scaling_cutoff.pdf>]
[11 <./figures/figD_scaling_modes.pdf>])
(./sections/06_reproducibility_and_provenance.tex
[12]
[13]) (./sections/07_limitations_and_scope.tex
[14]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\star' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 35.


[15]) (./sections/08_conclusion.tex
[16]) (./appendix/A_run_manifest.tex
Overfull \hbox (12.46654pt too wide) in paragraph at lines 10--21
 [] 
) (./sections/A_provenance.tex

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


[17]
Overfull \hbox (18.50665pt too wide) in paragraph at lines 59--64
\T1/cmr/m/n/10.95 (-20) (i) re-gen-er-ates nu-mer-i-cal out-puts un-der \T1/cmt
t/m/n/10.95 outputs/\T1/cmr/m/n/10.95 (-20) , (ii) re-builds canon-i-cal fig-ur
es un-der \T1/cmtt/m/n/10.95 outputs/figures/\T1/cmr/m/n/10.95 (-20) ,

Overfull \hbox (17.92433pt too wide) in paragraph at lines 59--64
\T1/cmr/m/n/10.95 (-20) (iii) stages sub-mis-sion fig-ures un-der \T1/cmtt/m/n/
10.95 phase2/paper/figures/\T1/cmr/m/n/10.95 (-20) , and (iv) com-piles \T1/cmt
t/m/n/10.95 phase2/paper/main.tex

[18]) (./main.bbl)
[19]
[20 <./figures/figE_frw_comparison.pdf>] (./main.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)</usr/local/texlive/2025/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb></usr/local/texlive/2025/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb></usr/local/texlive/2025/texmf
-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb></usr/local/texlive/2025/texmf-
dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb></usr/local/texlive/2025/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi12.pfb></usr/local/texlive/2025/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi7.pfb></usr/local/texlive/2025/texmf-dist
/fonts/type1/public/amsfonts/cm/cmmi8.pfb></usr/local/texlive/2025/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr10.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr8.pfb></usr/local/texlive/2025/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb></usr/local/texlive/2025/texmf-dist/fonts/t
ype1/public/amsfonts/symbols/msam10.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/amsfonts/symbols/msbm10.pfb></usr/local/texlive/2025/texmf-dist
/fonts/type1/public/cm-super/sfbx1000.pfb></usr/local/texlive/2025/texmf-dist/f
onts/type1/public/cm-super/sfbx1095.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/cm-super/sfbx1200.pfb></usr/local/texlive/2025/texmf-dist/fonts
/type1/public/cm-super/sfbx1440.pfb></usr/local/texlive/2025/texmf-dist/fonts/t
ype1/public/cm-super/sfcc1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/typ
e1/public/cm-super/sfrm0800.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1
/public/cm-super/sfrm1000.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/p
ublic/cm-super/sfrm1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/pub
lic/cm-super/sfrm1200.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/publi
c/cm-super/sfrm1728.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/
cm-super/sfti1000.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/cm
-super/sfti1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/cm-s
uper/sftt1095.pfb>
Output written on main.pdf (20 pages, 506148 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: References changed.
Latexmk: Log file says output to 'main.pdf'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: applying rule 'bibtex main'...
Rule 'bibtex main':  Reasons for rerun
Changed files or newly in use/created:
  main.aux

------------
Run number 2 of rule 'bibtex main'
------------
------------
Running 'bibtex  "main.aux"'
------------
This is BibTeX, Version 0.99d (TeX Live 2025)
The top-level auxiliary file: main.aux
The style file: unsrt.bst
Database file #1: references.bib
Warning--I didn't find a database entry for "weinberg1989cc"
(There was 1 warning)
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  main.aux
  main.toc

------------
Run number 3 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -halt-on-error -recorder  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/article.cls
Document Class: article 2024/06/29 v1.4n Standard LaTeX document class
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/size11.clo))
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amscls/amsthm.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/mathtools/mathtools.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/calc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/mathtools/mhsetup.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/caption.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
ty (/usr/local/texlive/2025/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/local/texlive/2025/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/local/texlive/2025/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/local/texlive/2025/texmf-dist/tex/latex/url/url.sty)
(/usr/local/texlive/2025/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/local/texlive/2025/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/atbegshi-ltx.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/local/texlive/2025/texmf-dist/tex/latex/base/atveryend-ltx.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty

(/usr/local/texlive/2025/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty
))) (./macros.tex)
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./main.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/local/texlive/2025/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./main.out) (./main.out)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msb.cfg)
(./sections/00_abstract.tex) (./main.toc
[1{/usr/local/texlive/2025/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/l
ocal/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t1.enc}])
(./sections/01_introduction.tex
[2]

LaTeX Warning: Citation `weinberg1989cc' on page 3 undefined on input line 16.


LaTeX Warning: Citation `weinberg1989cc' on page 3 undefined on input line 19.


[3]) (./sections/02_model_definition.tex
[4]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 99.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 99.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 99.


[5{/usr/local/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-ts1.enc
}]) (./sections/03_claim_C2_1_existence.tex
[6]) (./sections/04_claim_C2_2_robustness.tex
[7]
Overfull \hbox (3.43513pt too wide) in paragraph at lines 25--26
[]\T1/cmr/bx/n/10.95 (-20) UV/discretization con-trol sweep: \T1/cmr/m/n/10.95 
(-20) vary the implementation-defined ul-tra-vi-o-let/discretization

Overfull \hbox (1.14455pt too wide) in paragraph at lines 28--29
\T1/cmr/m/n/10.95 (-20) For each fam-ily, the re-ported quan-tity is the resid-
ual en-ergy proxy $\OT1/cmr/m/n/10.95 (-20) ^^A\OML/cmm/m/it/10.95 E$ \T1/cmr/m
/n/10.95 (-20) (Eq. []) or its implementation-

[8 <./figures/figA_mode_sum_residual.pdf>]
[9 <./figures/figB_scaling_epsilon.pdf>])
(./sections/05_claim_C2_3_frw_viability.tex
[10 <./figures/figC_scaling_cutoff.pdf>]
[11 <./figures/figD_scaling_modes.pdf>])
(./sections/06_reproducibility_and_provenance.tex
[12]
[13]) (./sections/07_limitations_and_scope.tex
[14]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\star' on input line 35.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 35.


[15]) (./sections/08_conclusion.tex
[16]) (./appendix/A_run_manifest.tex
Overfull \hbox (12.46654pt too wide) in paragraph at lines 10--21
 [] 
) (./sections/A_provenance.tex

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 10.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 10.


[17]
Overfull \hbox (18.50665pt too wide) in paragraph at lines 59--64
\T1/cmr/m/n/10.95 (-20) (i) re-gen-er-ates nu-mer-i-cal out-puts un-der \T1/cmt
t/m/n/10.95 outputs/\T1/cmr/m/n/10.95 (-20) , (ii) re-builds canon-i-cal fig-ur
es un-der \T1/cmtt/m/n/10.95 outputs/figures/\T1/cmr/m/n/10.95 (-20) ,

Overfull \hbox (17.92433pt too wide) in paragraph at lines 59--64
\T1/cmr/m/n/10.95 (-20) (iii) stages sub-mis-sion fig-ures un-der \T1/cmtt/m/n/
10.95 phase2/paper/figures/\T1/cmr/m/n/10.95 (-20) , and (iv) com-piles \T1/cmt
t/m/n/10.95 phase2/paper/main.tex

[18]) (./main.bbl)
[19]
[20 <./figures/figE_frw_comparison.pdf>] (./main.aux)

LaTeX Warning: There were undefined references.

 )
(see the transcript file for additional information)</usr/local/texlive/2025/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb></usr/local/texlive/2025/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb></usr/local/texlive/2025/texmf
-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb></usr/local/texlive/2025/texmf-
dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb></usr/local/texlive/2025/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi12.pfb></usr/local/texlive/2025/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi7.pfb></usr/local/texlive/2025/texmf-dist
/fonts/type1/public/amsfonts/cm/cmmi8.pfb></usr/local/texlive/2025/texmf-dist/f
onts/type1/public/amsfonts/cm/cmr10.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr8.pfb></usr/local/texlive/2025/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy10.pfb></usr/local/texlive/2025/texmf-dist/fonts/t
ype1/public/amsfonts/symbols/msam10.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/amsfonts/symbols/msbm10.pfb></usr/local/texlive/2025/texmf-dist
/fonts/type1/public/cm-super/sfbx1000.pfb></usr/local/texlive/2025/texmf-dist/f
onts/type1/public/cm-super/sfbx1095.pfb></usr/local/texlive/2025/texmf-dist/fon
ts/type1/public/cm-super/sfbx1200.pfb></usr/local/texlive/2025/texmf-dist/fonts
/type1/public/cm-super/sfbx1440.pfb></usr/local/texlive/2025/texmf-dist/fonts/t
ype1/public/cm-super/sfcc1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/typ
e1/public/cm-super/sfrm0800.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1
/public/cm-super/sfrm1000.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/p
ublic/cm-super/sfrm1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/pub
lic/cm-super/sfrm1200.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/publi
c/cm-super/sfrm1728.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/
cm-super/sfti1000.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/cm
-super/sfti1095.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/cm-s
uper/sftt1095.pfb>
Output written on main.pdf (20 pages, 506236 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: Summary of warnings from last run of *latex:
  Latex failed to resolve 2 citation(s)
Latexmk: ====Undefined refs and citations with line #s in .tex file:
  Citation `weinberg1989cc' on page 3 undefined on input line 16
  Citation `weinberg1989cc' on page 3 undefined on input line 19
Latexmk: All targets (main.pdf) are up-to-date
```

Matches in main.log:

```
587:LaTeX Warning: Citation `weinberg1989cc' on page 3 undefined on input line 16.
590:LaTeX Warning: Citation `weinberg1989cc' on page 3 undefined on input line 19.
770:LaTeX Warning: There were undefined references.
```

Result: NOT clean (see matches above)

## 6) Claims discipline scan (generic)

```
/Users/dri/Documents/Projects/origin-axiom/phase2/SCOPE.md:19:Phase 2 is a *discipline phase*: it tightens definitions, provenance, and robustness
/Users/dri/Documents/Projects/origin-axiom/phase2/SCOPE.md:37:- Strict reproducibility: a single YAML config, Snakemake as the canonical runner, and
/Users/dri/Documents/Projects/origin-axiom/phase2/SCOPE.md:38:  complete run provenance.
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/observables.py:15:# Observables + plotting helpers (per-run artifacts)
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:10:  - sections: 01..08 + 06_reproducibility_and_provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:11:  - appendix: `appendix/A_run_manifest` and `sections/A_provenance`
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:13:## B) Provenance integrity (Claim → Figure → run_id → run folder)
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:14:- [ ] `bash scripts/phase2_verify_provenance.sh` passes.
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:30:  - explicit non-claims boundary sentence
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:31:- [ ] `phase2/CLAIMS.md` is the canonical claim→artifact map (paper points to it).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:35:- [ ] Paper build artifacts ignored (except policy choice for main.pdf).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:40:  2) A script/checker added that enforces reproducibility (lint, provenance, build).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:41:  3) A lock/release artifact added (checklist, bundle index, tag instructions).
/Users/dri/Documents/Projects/origin-axiom/phase2/APPROXIMATION_CONTRACT.md:69:Phase 2 implements a deterministic, auditable rule to enforce the constraint. The exact enforcement mechanism is part of the model definition and is recorded by provenance metadata (constraint applied flag + details).
/Users/dri/Documents/Projects/origin-axiom/phase2/APPROXIMATION_CONTRACT.md:104:- absence of numerical pathologies or “wild artifacts” in these sweeps.
/Users/dri/Documents/Projects/origin-axiom/phase2/APPROXIMATION_CONTRACT.md:110:## Provenance & Reproducibility Contract
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:1:# Phase 2 — Reproducibility and Provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:3:This document defines the **reproducibility guarantees, provenance tracking, and execution
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:6:**Rule:** No scientific claim is valid unless it is backed by a fully reproducible artifact
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:25:The only canonical way to generate Phase 2 artifacts is:
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:30:artifacts** unless the outputs are identical and the run metadata is complete.
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:34:## 3. Canonical artifacts and run pointers
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:83:2. Regenerating canonical artifacts A–E.
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:85:4. Updating `CLAIMS.md` provenance pointers if any file paths changed.
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:94:- `snakemake -c 1 all` reproduces **exactly** the canonical figures A–E,
/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md:108:- `REPRODUCIBILITY.md`
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS_TABLE.md:1:# Phase 2 Claims → Artifacts Map (P2-S2)
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS_TABLE.md:11:| Claim | Paper section | Figures (paper/figures) | Run-id sidecars (outputs/figures) | Run meta (outputs/runs) | Notes / Non-claims |
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/utils_meta.py:39:# Git provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:4:**canonical, reproducible artifacts**.
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:6:**Rule:** No claim is valid unless it is backed by at least one canonical artifact listed
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:15:## Canonical artifacts (A–E)
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:30:That file contains the `run_id` of the provenance-complete run directory:
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:34:### Locked run_ids (canonical provenance)
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:36:These run_ids are the canonical provenance for the present Phase-2 artifact set A–E:
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:62:**Primary artifact**
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:66:**Provenance pointer**
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:115:**Primary artifacts**
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:121:**Provenance pointers**
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:198:**Primary artifact**
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:202:**Provenance pointer**
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:251:## Explicit Non-Claims (binding)
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS.md:276:## Claim → Artifact mapping (Phase 2 canonical)
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:7:- Scope and claims discipline established (SCOPE/CLAIMS/ASSUMPTIONS + reproducibility contract).
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:8:- Next: implement Phase 2 computational pipeline (mode-sum + sweeps + FRW wrapper) and canonical artifacts A–E.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:15:- Established provenance per run:
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:38:- Confirmed status: Phase 2 computational artifacts + claims mapping exist; paper build currently blocked by mismatched \\input filenames in paper/main.tex (structural issue).
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:41:- Stage 3 will (1) fix paper structure (inputs/duplicates), then (2) rewrite text to be unambiguous and scope-tight, mapping every claim to figs A–E + run provenance.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:45:- Confirmed claims-first ordering is the canonical main spine (C2.1–C2.3) with reproducibility + limitations before conclusion.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:46:- Added/confirmed Phase 2 paper `.gitignore` to prevent tracking LaTeX artifacts and draft `main.pdf`.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:59:## 2026-01-04 — Phase 2 Stage 1 (P2-S2): claims map hardening (CLAIMS → paper → artifacts)
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:60:- Added `phase2/CLAIMS_TABLE.md` as the canonical claim-to-artifacts map (C2.1–C2.3).
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:64:  - meta.json exists per run_id and contains provenance hints,
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:68:## 2026-01-04 — Phase 2 Stage 1 (P2-S3): provenance enforcement for paper-referenced artifacts
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:69:- Added `scripts/phase2_verify_provenance.sh` enforcing that every paper figure (A–E) has:
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:75:- No new scientific claims; this rung hardens auditability and provenance completeness.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:84:## 2026-01-04 — P2-S5.2: Paper ↔ CLAIMS map pointer (claims-to-artifacts hard link)
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:85:- Added a single canonical pointer in `paper/sections/06_reproducibility_and_provenance.tex` directing readers to `phase2/CLAIMS.md` for the Claim C2.1–C2.3 → artifact mapping.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:90:- Added `PHASE2_LOCK_CHECKLIST.md` to define a concrete “Phase 2 locked” bar (build, lint, provenance, claims discipline, hygiene).
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:91:- Added an explicit commit policy: commit only per-rung / reproducibility enforcement / lock artifacts, not micro-edits.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:94:- Fixed LaTeX build failure in reproducibility section (text-mode arrow -> math-mode).
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:95:- Phase 2 gate now passes: structural audit + provenance verification + paper lint + clean build.
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:96:- Phase 2 paper PDF is now tracked in git for exact artifact reproducibility.
/Users/dri/Documents/Projects/origin-axiom/phase2/workflow/Snakefile:4:# Canonical rule: one rule -> one canonical artifact (figure PDF).
/Users/dri/Documents/Projects/origin-axiom/phase2/workflow/Snakefile:420:        runs/<run_id>/... (full provenance for each canonical figure)
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:26:-rw-r--r--   1 dri  staff   2868 Dec 31 14:40 REPRODUCIBILITY.md
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:42:- OK: phase2/REPRODUCIBILITY.md
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:59:/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:61:/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:140:/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:157:/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:163:/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:396:/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex:2:% TODO:
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:610:LaTeX Warning: Reference `sec:reproducibility' on page 3 undefined on input lin
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:656:LaTeX Warning: Reference `sec:reproducibility' on page 5 undefined on input lin
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:804:) (./sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:848:LaTeX Warning: Reference `sec:reproducibility' on page 14 undefined on input li
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:878:LaTeX Warning: Reference `sec:reproducibility' on page 15 undefined on input li
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:889:) (./sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:1144:(./sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:1173:) (./sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:1414:(./sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:1443:) (./sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:4:artifact-first, drift-resistant process.
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:12:1. **Artifacts are the source of truth.**
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:18:3. **Provenance is mandatory.**
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:67:- a `*.run_id.txt` file pointing to the provenance-complete run.
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:94:- explicitly state non-claims and limitations,
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:103:1. Lock MD documents (scope/claims/assumptions/provenance rules).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:115:- A–E are reproducible and pinned,
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:5:It is intentionally narrow, reproducible, and claim-disciplined.
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:10:- `CLAIMS.md` — the only claims Phase 2 makes (and their artifact backing)
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:12:- `REPRODUCIBILITY.md` — provenance rules and what “locked” means
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:30:which points to a provenance-complete run directory:
/Users/dri/Documents/Projects/origin-axiom/phase2/config/phase2.yaml:163:# Paper artifact mapping (for sanity checks)
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/observables.py:15:# Observables + plotting helpers (per-run artifacts)
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:3:\section{Limitations and non-claims}
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:7:Its purpose is to lock a reproducible toy pipeline and to establish three auditable claims (C2.1--C2.3), not to assert a completed fundamental theory.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:8:To keep the work intellectually honest and arXiv-appropriate, we enumerate limitations and explicit non-claims.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:16:The lattice vacuum sector and the FRW mapping are toy realizations with a fixed code-unit normalization used for internal consistency and reproducibility.
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/run_mode_sum.py:26:# Direct invocation is allowed for debugging, but canonical artifacts
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/main.tex:18:\input{sections/06_reproducibility_and_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/certify_binding.py:103:        "provenance_present": True,
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/mode_model.py:304:    Keep this stable: it is part of the reproducibility contract.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/main.tex:70:% - Mention numerical sweeps (epsilon / cutoff / modes) + reproducibility (Snakemake, per-run provenance).
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/main.tex:92:\input{sections/A_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/run_sweep.py:83:    # Setup run + provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:4:Phase 2 is a *claims-first* paper whose only goal is to establish three auditable claims (C2.1–C2.3) with strict provenance. No new “Phase 3+” claims may enter Phase 2.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:13:7. 06_reproducibility_and_provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:18:- sections/A_provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:29:  - A bounded list of evidence artifacts (figures + run_ids)
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:30:  - A “Non-claims / limits” note (what is *not* asserted)
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:32:## Provenance rule
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex:6:% (iv) explicit non-claims boundary sentence.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex:17:Evidence is provided by a paired constrained vs.\ free run with identical initialization, summarized in Fig.~\ref{fig:mode_sum_residual}; exact provenance (run\_id(s), configuration, and scripts) is given in Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex:26:All reported curves correspond to the tagged run artifacts referenced in Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex:46:This verifies that the observed persistence of $|A(t)|\gtrsim\varepsilon$ is produced by enforcing~\eqref{eq:floor_constraint} in the specified implementation, rather than being an incidental feature of the unconstrained baseline or a plotting artifact.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex:51:\noindent\textbf{Non-claims boundary (C2.1).}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex:6:% (iv) explicit non-claims boundary sentence.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex:18:Evidence is provided by the FRW comparison in Fig.~\ref{fig:frw_comparison}; exact run provenance is given by Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex:21:The vacuum module produces a residual proxy $\Delta E(\theta)$ (Eq.~\eqref{eq:deltaE_def}) or an implementation-defined equivalent recorded in the Phase~II run artifacts.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex:73:\noindent\textbf{Non-claims boundary (C2.3).}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex:75:It supports only the bounded statement that the Phase~II residual proxy can be embedded into the configured FRW background module as a constant contribution without inducing numerical failure in the explored regime, with full provenance given by Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/phase2_binding_certificate 2.json:24:    "provenance_present": true
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.tex:92:\input{sections/06_reproducibility_and_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.tex:101:\input{sections/A_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex:8:The purpose of this section is to state precisely what these claims do \emph{not} imply, what would falsify them, and what additional work is required before any physical interpretation can be elevated beyond the present scope.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex:40:\subsection{What would falsify the Phase~II claims}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex:43:  \item \textbf{Non-reproducibility:} inability to regenerate the figures and PDF from the recorded run identifiers and scripts (Appendix~\ref{app:run_manifest} and Sec.~\ref{sec:reproducibility}).
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex:52:  \item \textbf{Mechanism upgrade:} a candidate local formulation or symmetry principle whose constrained dynamics reproduce (or justify) the operational floor.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex:53:  \item \textbf{Universality upgrade:} controlled convergence/refinement studies and cross-implementation checks showing that the residual behavior is not an artifact of a particular discretization or integrator.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex:58:Phase~II should therefore be read as a rigorous \emph{engineering and auditing milestone}: it demonstrates a stable constrained-cancellation mechanism and a reproducible pipeline that can be independently verified.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex:1:\section{Computational Provenance (Appendix)}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex:7:% (v) a single sentence pointing to provenance: outputs/figures + Appendix run manifest.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex:17:The intent is reproducibility: every quantity referenced by Claims~C2.1--C2.3 is defined here, while the remaining microphysical and numerical choices (integrator, potential, and update schedule) are treated as fixed by the Phase~II reference implementation and configuration.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex:134:Precise artifact provenance (scripts, configs, run IDs, and figure build rules) is documented in Sec.~\ref{sec:reproducibility} and Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/01_introduction.tex:40:The focus is isolated and diagnostic: determine whether a global non-cancellation constraint yields a reproducible, well-behaved residual across nontrivial numerical variations in a minimal setting.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/01_introduction.tex:49:Reproducibility is treated as a first-class requirement: figures correspond to tagged runs with recorded configurations, run identifiers, and an explicit run manifest.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/01_introduction.tex:54:Section~\ref{sec:reproducibility} documents provenance and reproduction instructions, and Section~\ref{sec:discussion} states scope boundaries and limitations.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/08_conclusion.tex:27:The core contribution of Phase~II is therefore methodological and reproducibility-focused:
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/08_conclusion.tex:31:and documented with end-to-end provenance so each figure can be traced to tagged runs and regenerated from a clean checkout.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/08_conclusion.tex:32:Reproduction instructions and repository structure are stated in Sec.~\ref{sec:reproducibility}, and per-figure run identifiers are indexed in Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/08_conclusion.tex:36:What it provides is a concrete, checkable baseline: a fully audited toy pipeline in which ``no perfect cancellation'' is imposed as a global constraint and its consequences can be measured, reproduced, and scrutinized.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:1:% paper/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:3:\section{Reproducibility and provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:4:\label{sec:reproducibility}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:6:Phase~II is designed to be reproducible from a clean repository checkout in the following operational sense:
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:8:and each figure is traceable to recorded run artifacts (including code-state identifiers) sufficient for independent auditing and regeneration.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:9:This section specifies (i) what is treated as authoritative, (ii) how artifacts are traced from the manuscript back to runs, and (iii) how a third party rebuilds the figures and the PDF.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:11:\subsection{Canonical claim-to-artifact mapping}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:12:A compact claim-to-artifact index (Claims~C2.1--C2.3 $\rightarrow$ figure files, \texttt{run\_id} sidecars, and run folders) is maintained in \texttt{phase2/CLAIMS.md}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:14:These two files are the intended audit anchors: starting from any claim or figure, a reader can locate the corresponding run signature and reproduce (or at minimum verify) the artifact.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:16:\subsection{Repository layout and authoritative artifacts}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:22:  \item \texttt{outputs/}: generated run folders, intermediate data products, and canonical figures (treated as build artifacts).
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:28:Figures included in the manuscript are staged under \texttt{phase2/paper/figures/} for arXiv-style packaging, and each staged figure is paired with a \texttt{run\_id} pointer that links back to the authoritative run artifacts under \texttt{outputs/}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:31:Each figure in the main text corresponds to a tagged run or sweep whose provenance is recorded in Appendix~\ref{app:run_manifest}:
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:52:\subsection{Build system and exact reproduction}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:71:All data products necessary to reproduce the plots are either:
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:73:  \item stored under \texttt{outputs/} as build artifacts and run folders, or
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:6:% (iv) explicit non-claims boundary sentence.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:17:Evidence is provided by the sweep summaries in Figs.~\ref{fig:scaling_epsilon}--\ref{fig:scaling_modes}; exact run provenance is given by Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:28:For each family, the reported quantity is the residual energy proxy $\Delta E$ (Eq.~\eqref{eq:deltaE_def}) or its implementation-defined equivalent, computed from matched constrained and free runs using the Phase~II run protocol (late-time average or end-of-run value as specified in the run artifacts referenced in Appendix~\ref{app:run_manifest}).
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:87:\noindent\textbf{Non-claims boundary (C2.2).}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:89:They only support the bounded statement that the constrained implementation remains stable and produces a reproducible, smoothly varying residual proxy under the stated numerical controls.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/06_reproducibility_and_provenance.tex:1:% 06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/phase2_binding_certificate.json:24:    "provenance_present": true
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:1:% phase2/paper/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:3:\section{Computational provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:4:\label{app:provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:7:Its purpose is narrow and concrete: enable an independent reader to (i) map each figure to the exact run artifacts that produced it,
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:22:\subsection{Run identifiers and artifact structure}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:29:  \item \texttt{meta.json}: provenance metadata (code state, configuration, and execution identifiers);
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:34:\paragraph{Provenance fields recorded in \texttt{meta.json}.}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:50:It therefore provides a direct, file-level link from the staged manuscript figure to the authoritative run artifacts under \texttt{outputs/runs/}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:70:\subsection{Scope of reproducibility}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:72:They ensure that the numerical evidence presented is transparent, auditable, and reproducible.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/appendix/A_run_manifest.tex:12:Figure & Artifact stem & run\_id & git \\
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/00_abstract.tex:4:We present Phase~II of the Origin Axiom program as a bounded, reproducible test of a single operational hypothesis: imposing a strict global \emph{non-cancellation floor} on a vacuum-like numerical system induces an auditable residual, and that residual can be carried through a minimal end-to-end pipeline without numerical pathology.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/04_numerical_experiments.tex:10:All figures presented here are generated automatically via the Phase~2 workflow and are reproducible from the accompanying configuration and run logs.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/04_numerical_experiments.tex:59:This saturation confirms that the residual is not a finite-size artifact and persists in the large-$N$ limit of the finite ensemble.
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/config/phase2.yaml:160:# Paper artifact mapping (for sanity checks)
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/01_introduction.tex:26:The goal of Phase~2 is to demonstrate that this mechanism can reproduce a vacuum energy scale compatible with cosmological observations in a setting that approximates realistic quantum field behavior.
```

## 7) Git status snapshot (informational)

```
 M phase2/AUDIT_REPORT.md
 M phase2/paper/main.pdf
```

## 8) Next recommended Phase 2 rungs (after audit)

- P2-S1: Define Phase 2 paper spine + section contract (order, naming, invariants)
- P2-S2: Claims map hardening (CLAIMS.md -> paper table -> artifact paths)
- P2-S3: Provenance enforcement (git hash, params, seed, environment) in every run artifact
- P2-S4: Rewrite passes (structure first, then math/rigor), zero new claims until audits pass
