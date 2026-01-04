
# Phase 2 Structural Audit (P2-A1)

- Generated: 2026-01-04 09:01:45 +0100
- Git: 6611be9 (phase0-2-alignment)
- Repo: /Users/dri/Documents/Projects/origin-axiom

## 1) High-level inventory

```
total 152
drwxr-xr-x@ 23 dri  staff    736 Jan  4 08:59 .
drwx------@ 16 dri  staff    512 Jan  4 09:01 ..
-rw-r--r--@  1 dri  staff   6148 Jan  2 18:26 .DS_Store
-rw-r--r--   1 dri  staff    366 Jan  4 08:07 .gitignore
drwxr-xr-x  12 dri  staff    384 Jan  3 13:46 .snakemake
-rw-r--r--   1 dri  staff   5823 Dec 31 14:40 APPROXIMATION_CONTRACT.md
-rw-r--r--   1 dri  staff   3775 Dec 31 14:40 ASSUMPTIONS.md
-rw-r--r--@  1 dri  staff    191 Jan  4 09:01 AUDIT_REPORT.md
-rw-r--r--   1 dri  staff  10019 Jan  4 08:54 CLAIMS.md
-rw-r--r--   1 dri  staff   1386 Jan  4 08:16 CLAIMS_TABLE.md
-rw-r--r--   1 dri  staff   2199 Jan  4 08:59 PHASE2_LOCK_CHECKLIST.md
-rw-r--r--   1 dri  staff   2758 Dec 31 14:40 PHASE2_WORKFLOW_GUIDE.md
-rw-r--r--   1 dri  staff   6456 Jan  4 08:59 PROGRESS_LOG.md
-rw-r--r--   1 dri  staff   1032 Dec 31 14:40 README.md
-rw-r--r--   1 dri  staff   2868 Dec 31 14:40 REPRODUCIBILITY.md
-rw-r--r--   1 dri  staff   3236 Dec 31 14:40 SCOPE.md
drwxr-xr-x   5 dri  staff    160 Jan  4 06:59 _paper_backups
drwxr-xr-x   5 dri  staff    160 Jan  2 19:40 config
drwxr-xr-x   8 dri  staff    256 Jan  4 09:00 outputs
drwxr-xr-x  19 dri  staff    608 Jan  4 08:57 paper
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
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_frw_implications.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/01_introduction.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_framework_and_axiom.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/07_limitations_and_scope.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_numerical_experiments.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/00_abstract.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_results_scaling.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_mode_sum_model.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.bbl
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/.DS_Store
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
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:393:## 4) TODO / FIXME / XXX / TBD sweep
/Users/dri/Documents/Projects/origin-axiom/phase2/PROGRESS_LOG.md:80:- Added `scripts/phase2_paper_lint.sh` to enforce: no TODO/FIXME/XXX/TBD in Phase 2 paper, and clean build log scan.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/main.tex:68:% TODO (150--250 words):
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/macros.tex:117:\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex:2:% TODO:
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/06_frw_implications.tex:4:% TODO: define mapping residual -> \OLeff via explicit parameter in config.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/08_conclusion.tex:2:% TODO
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/07_limitations_and_scope.tex:2:% TODO
```

## 5) Paper build + structure

### 5.1 Paper directory listing

```
total 232
drwxr-xr-x  19 dri  staff    608 Jan  4 08:57 .
drwxr-xr-x@ 23 dri  staff    736 Jan  4 08:59 ..
-rw-r--r--@  1 dri  staff   6148 Dec 31 14:10 .DS_Store
-rw-r--r--   1 dri  staff    128 Jan  4 08:13 .gitignore
-rw-r--r--   1 dri  staff   1537 Jan  4 08:14 PAPER_CONTRACT.md
drwxr-xr-x   3 dri  staff     96 Jan  4 08:19 appendix
drwxr-xr-x   7 dri  staff    224 Jan  2 19:40 figures
-rw-r--r--@  1 dri  staff   3456 Jan  4 08:52 macros.tex
-rw-r--r--   1 dri  staff   7703 Jan  4 08:57 main.aux
-rw-r--r--   1 dri  staff     49 Jan  4 08:25 main.bbl
-rw-r--r--   1 dri  staff    940 Jan  4 08:25 main.blg
-rw-r--r--   1 dri  staff  15605 Jan  4 08:57 main.fdb_latexmk
-rw-r--r--   1 dri  staff  17483 Jan  4 08:57 main.fls
-rw-r--r--   1 dri  staff  25687 Jan  4 08:57 main.log
-rw-r--r--   1 dri  staff   4800 Jan  4 08:57 main.out
-rw-r--r--@  1 dri  staff   3118 Jan  4 08:23 main.tex
-rw-r--r--   1 dri  staff      0 Jan  4 08:57 main.toc
-rw-r--r--@  1 dri  staff    102 Dec 31 14:40 references.bib
drwxr-xr-x  17 dri  staff    544 Jan  4 08:57 sections
```

### 5.2 main.tex spine (inputs/includes)

```
No inputs/includes found (or different structure).
```

### 5.3 Labels / refs / cites quick stats

```
labels:
35
refs:
24
cites:
0
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
No file main.toc.
(./sections/01_introduction.tex
[1{/usr/local/texlive/2025/texmf-var/fonts/map/pdftex/updmap/pdftex.map}{/usr/l
ocal/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-t1.enc}]

LaTeX Warning: Reference `sec:framework' on page 2 undefined on input line 50.


LaTeX Warning: Reference `sec:modesum' on page 2 undefined on input line 51.


LaTeX Warning: Reference `sec:cosmology' on page 2 undefined on input line 52.


LaTeX Warning: Reference `sec:discussion' on page 2 undefined on input line 53.


) (./sections/02_model_definition.tex
[2]

LaTeX Warning: Reference `eq:uniform_shift' on page 3 undefined on input line 5
8.


LaTeX Warning: Reference `eq:uniform_shift' on page 3 undefined on input line 6
9.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 87.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 87.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 87.


[3{/usr/local/texlive/2025/texmf-dist/fonts/enc/dvips/cm-super/cm-super-ts1.enc
}]

LaTeX Warning: Reference `eq:floor_constraint' on page 4 undefined on input lin
e 110.


LaTeX Warning: Reference `sec:reproducibility' on page 4 undefined on input lin
e 120.


LaTeX Warning: Reference `app:run_manifest' on page 4 undefined on input line 1
20.

) (./sections/03_claim_C2_1_existence.tex

LaTeX Warning: Reference `fig:mode_sum_residual' on page 4 undefined on input l
ine 18.


[4]

LaTeX Warning: Reference `eq:uniform_shift' on page 5 undefined on input line 2
4.


LaTeX Warning: Reference `fig:mode_sum_residual' on page 5 undefined on input l
ine 29.


LaTeX Warning: Reference `eq:uniform_shift' on page 5 undefined on input line 4
5.


LaTeX Warning: Reference `eq:floor_constraint' on page 5 undefined on input lin
e 46.

) (./sections/04_claim_C2_2_robustness.tex

LaTeX Warning: Reference `fig:scaling_epsilon' on page 5 undefined on input lin
e 18.


LaTeX Warning: Reference `fig:scaling_modes' on page 5 undefined on input line 
18.


LaTeX Warning: Reference `sec:claim_c21' on page 5 undefined on input line 21.


[5]

LaTeX Warning: Reference `fig:scaling_epsilon' on page 6 undefined on input lin
e 23.


LaTeX Warning: Reference `fig:scaling_cutoff' on page 6 undefined on input line
 24.


LaTeX Warning: Reference `fig:scaling_cutoff' on page 6 undefined on input line
 25.


LaTeX Warning: Reference `fig:scaling_modes' on page 6 undefined on input line 
25.


LaTeX Warning: Reference `eq:deltaE_def' on page 6 undefined on input line 27.


LaTeX Warning: Reference `fig:scaling_epsilon' on page 6 undefined on input lin
e 42.


LaTeX Warning: Reference `fig:scaling_cutoff' on page 6 undefined on input line
 57.


[6 <../outputs/figures/figA_mode_sum_residual.pdf>]

LaTeX Warning: Reference `fig:scaling_modes' on page 7 undefined on input line 
72.


LaTeX Warning: Reference `fig:scaling_epsilon' on page 7 undefined on input lin
e 80.


LaTeX Warning: Reference `fig:scaling_cutoff' on page 7 undefined on input line
 83.


LaTeX Warning: Reference `fig:scaling_modes' on page 7 undefined on input line 
83.


Overfull \hbox (21.48515pt too wide) in paragraph at lines 83--85
 []\T1/cmr/bx/n/10.95 (-20) (ii) The ob-served resid-ual is not a single-cutoff
 ar-ti-fact.[] \T1/cmr/m/n/10.95 (-20) Changes in the en-gine's UV/discretizati
on
) (./sections/05_claim_C2_3_frw_viability.tex

LaTeX Warning: Reference `fig:frw_comparison' on page 7 undefined on input line
 18.


[7 <../outputs/figures/figB_scaling_epsilon.pdf>]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 20.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\Omega' on input line 20.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 20.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\Lambda' on input line 20.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\theta' on input line 20.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 20.


LaTeX Warning: Reference `eq:deltaE_def' on page 8 undefined on input line 21.


[8 <../outputs/figures/figC_scaling_cutoff.pdf>]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 46.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 46.


LaTeX Warning: Reference `fig:frw_comparison' on page 9 undefined on input line
 58.


[9 <../outputs/figures/figD_scaling_modes.pdf>])
(./sections/06_reproducibility_and_provenance.tex
! Missing $ inserted.
<inserted text> 
                $
l.6 ...xttt{phase2/CLAIMS.md} (``Claim \rightarrow
                                                   Artifact mapping''). The ...

!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Missing input file 'main.toc' (or dependence on it) from following:
  No file main.toc.
Latexmk: Summary of warnings from last run of *latex:
  Latex failed to resolve 32 reference(s)
Latexmk: ====Undefined refs and citations with line #s in .tex file:
  Reference `sec:framework' on page 2 undefined on input line 50
  Reference `sec:modesum' on page 2 undefined on input line 51
  Reference `sec:cosmology' on page 2 undefined on input line 52
  Reference `sec:discussion' on page 2 undefined on input line 53
  Reference `sec:discussion' on page 2 undefined on input line 53
  Reference `eq:uniform_shift' on page 3 undefined on input line 58
  Reference `eq:uniform_shift' on page 3 undefined on input line 69
 And 25 more --- see log file 'main.log'
Latexmk: Errors, so I did not complete making targets
Collected error summary (may duplicate other messages):
  pdflatex: Command for 'pdflatex' gave return code 1
      Refer to 'main.log' and/or above output for details

Latexmk: Sometimes, the -f option can be used to get latexmk
  to try to force complete processing.
  But normally, you will need to correct the file(s) that caused the
  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.
```

Result: OK (no hygiene-pattern hits)

## 6) Claims discipline scan (generic)

```
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/observables.py:15:# Observables + plotting helpers (per-run artifacts)
/Users/dri/Documents/Projects/origin-axiom/phase2/APPROXIMATION_CONTRACT.md:69:Phase 2 implements a deterministic, auditable rule to enforce the constraint. The exact enforcement mechanism is part of the model definition and is recorded by provenance metadata (constraint applied flag + details).
/Users/dri/Documents/Projects/origin-axiom/phase2/APPROXIMATION_CONTRACT.md:104:- absence of numerical pathologies or “wild artifacts” in these sweeps.
/Users/dri/Documents/Projects/origin-axiom/phase2/APPROXIMATION_CONTRACT.md:110:## Provenance & Reproducibility Contract
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:26:-rw-r--r--   1 dri  staff   2868 Dec 31 14:40 REPRODUCIBILITY.md
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:42:- OK: phase2/REPRODUCIBILITY.md
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:64:/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:66:/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:144:/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:161:/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:167:/Users/dri/Documents/Projects/origin-axiom/phase2/REPRODUCIBILITY.md
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:400:/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex:2:% TODO:
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:596:LaTeX Warning: Reference `sec:reproducibility' on page 4 undefined on input lin
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:740:(./sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/AUDIT_REPORT.md:745:                                                   Artifact mapping''). The ...
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:5:It is intentionally narrow, reproducible, and claim-disciplined.
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:10:- `CLAIMS.md` — the only claims Phase 2 makes (and their artifact backing)
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:12:- `REPRODUCIBILITY.md` — provenance rules and what “locked” means
/Users/dri/Documents/Projects/origin-axiom/phase2/README.md:30:which points to a provenance-complete run directory:
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
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:4:artifact-first, drift-resistant process.
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:12:1. **Artifacts are the source of truth.**
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:18:3. **Provenance is mandatory.**
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:67:- a `*.run_id.txt` file pointing to the provenance-complete run.
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:94:- explicitly state non-claims and limitations,
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:103:1. Lock MD documents (scope/claims/assumptions/provenance rules).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_WORKFLOW_GUIDE.md:115:- A–E are reproducible and pinned,
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
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:10:  - sections: 01..08 + 06_reproducibility_and_provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:11:  - appendix: `appendix/A_run_manifest` and `sections/A_provenance`
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:13:## B) Provenance integrity (Claim → Figure → run_id → run folder)
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:14:- [ ] `bash scripts/phase2_verify_provenance.sh` passes.
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:30:  - explicit non-claims boundary sentence
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:31:- [ ] `phase2/CLAIMS.md` is the canonical claim→artifact map (paper points to it).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:35:- [ ] Paper build artifacts ignored (except policy choice for main.pdf).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:40:  2) A script/checker added that enforces reproducibility (lint, provenance, build).
/Users/dri/Documents/Projects/origin-axiom/phase2/PHASE2_LOCK_CHECKLIST.md:41:  3) A lock/release artifact added (checklist, bundle index, tag instructions).
/Users/dri/Documents/Projects/origin-axiom/phase2/SCOPE.md:19:Phase 2 is a *discipline phase*: it tightens definitions, provenance, and robustness
/Users/dri/Documents/Projects/origin-axiom/phase2/SCOPE.md:37:- Strict reproducibility: a single YAML config, Snakemake as the canonical runner, and
/Users/dri/Documents/Projects/origin-axiom/phase2/SCOPE.md:38:  complete run provenance.
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS_TABLE.md:1:# Phase 2 Claims → Artifacts Map (P2-S2)
/Users/dri/Documents/Projects/origin-axiom/phase2/CLAIMS_TABLE.md:11:| Claim | Paper section | Figures (paper/figures) | Run-id sidecars (outputs/figures) | Run meta (outputs/runs) | Notes / Non-claims |
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/utils_meta.py:39:# Git provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/workflow/Snakefile:4:# Canonical rule: one rule -> one canonical artifact (figure PDF).
/Users/dri/Documents/Projects/origin-axiom/phase2/workflow/Snakefile:420:        runs/<run_id>/... (full provenance for each canonical figure)
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/observables.py:15:# Observables + plotting helpers (per-run artifacts)
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/scripts/certify_binding.py:103:        "provenance_present": True,
/Users/dri/Documents/Projects/origin-axiom/phase2/config/phase2.yaml:163:# Paper artifact mapping (for sanity checks)
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:3:\section{Limitations and non-claims}
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:7:Its purpose is to lock a reproducible toy pipeline and to establish three auditable claims (C2.1--C2.3), not to assert a completed fundamental theory.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:8:To keep the work intellectually honest and arXiv-appropriate, we enumerate limitations and explicit non-claims.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/structural_dupes_20260104T055918Z/07_limitations_and_nonclaims.tex:16:The lattice vacuum sector and the FRW mapping are toy realizations with a fixed code-unit normalization used for internal consistency and reproducibility.
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/mode_model.py:304:    Keep this stable: it is part of the reproducibility contract.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/main.tex:70:% - Mention numerical sweeps (epsilon / cutoff / modes) + reproducibility (Snakemake, per-run provenance).
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/main.tex:92:\input{sections/A_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/main.tex:18:\input{sections/06_reproducibility_and_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/run_mode_sum.py:26:# Direct invocation is allowed for debugging, but canonical artifacts
/Users/dri/Documents/Projects/origin-axiom/phase2/src/phase2/modes/run_sweep.py:83:    # Setup run + provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:4:Phase 2 is a *claims-first* paper whose only goal is to establish three auditable claims (C2.1–C2.3) with strict provenance. No new “Phase 3+” claims may enter Phase 2.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:13:7. 06_reproducibility_and_provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:18:- sections/A_provenance
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:29:  - A bounded list of evidence artifacts (figures + run_ids)
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:30:  - A “Non-claims / limits” note (what is *not* asserted)
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/PAPER_CONTRACT.md:32:## Provenance rule
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/phase2_binding_certificate 2.json:24:    "provenance_present": true
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.tex:81:\input{sections/06_reproducibility_and_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.tex:85:% Appendix (computational provenance)
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/main.tex:91:\input{sections/A_provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/05_claim_C2_3_frw_viability.tex:6:% (iv) explicit non-claims boundary sentence.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/A_provenance.tex:1:\section{Computational Provenance (Appendix)}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex:6:% (iv) explicit non-claims boundary sentence.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/03_claim_C2_1_existence.tex:46:This confirms that the observed nonzero residual is causally attributable to enforcing~\eqref{eq:floor_constraint} rather than to a numerical artifact of the unconstrained dynamics.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex:7:% (v) a single sentence pointing to provenance: outputs/figures + Appendix run manifest.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex:18:The intent is reproducibility: every quantity referenced by Claims~C2.1--C2.3 is defined here, with implementation details fixed by the Phase~II reference code and configuration.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/02_model_definition.tex:120:Precise artifact provenance (scripts, configs, run IDs, and figure build rules) is documented in Sec.~\ref{sec:reproducibility} and Appendix~\ref{app:run_manifest}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:1:% paper/sections/06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:3:\section{Reproducibility and provenance}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:4:\label{sec:reproducibility}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:6:\noindent\textbf{Canonical mapping.} A compact claim-to-artifact map (Claim C2.1--C2.3 $\rightarrow$ figures, run\_id sidecars, and run folders) is maintained in \texttt{phase2/CLAIMS.md} (``Claim \rightarrow Artifact mapping''). The Appendix run manifest (Appendix~\ref{app:run_manifest}) provides the per-figure run\_id pointers.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:8:Phase~II is designed to be reproducible from a clean checkout: every figure in this paper is generated from version-controlled code, explicit configuration, and logged run artifacts.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:9:This section specifies (i) where the authoritative artifacts live, (ii) how figures are built, and (iii) how a third party can reproduce the full PDF.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:11:\subsection{Repository layout and authoritative artifacts}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:17:  \item \texttt{outputs/}: generated data and figures (treated as build artifacts).
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:20:Figures included in the manuscript are copied or symlinked into \texttt{paper/figures/} for arXiv packaging, with provenance pointers to the original build products in \texttt{outputs/figures/}.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:23:Each figure in the main text corresponds to a tagged run or sweep whose provenance is recorded in a run manifest:
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:32:\subsection{Build system and exact reproduction}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:47:All data products necessary to reproduce the plots are generated by the build graph and are either:
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/06_reproducibility_and_provenance.tex:49:  \item stored under \texttt{outputs/} as build artifacts, or
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/01_introduction.tex:26:The goal of Phase~2 is to demonstrate that this mechanism can reproduce a vacuum energy scale compatible with cosmological observations in a setting that approximates realistic quantum field behavior.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011723Z/sections/06_reproducibility_and_provenance.tex:1:% 06_reproducibility_and_provenance.tex
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:6:% (iv) explicit non-claims boundary sentence.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:52:  The residual remains well-behaved and changes in a structured manner, indicating that the observed remainder is not a fragile artifact of a single cutoff choice.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:82:\paragraph{(ii) The observed residual is not a single-cutoff artifact.}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_claim_C2_2_robustness.tex:84:In the explored regime, the induced effect remains small (percent-level modulation in the relevant scan summaries), supporting the claim that the pipeline is stable and reproducible rather than parameter-explosive.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_numerical_experiments.tex:10:All figures presented here are generated automatically via the Phase~2 workflow and are reproducible from the accompanying configuration and run logs.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/04_numerical_experiments.tex:59:This saturation confirms that the residual is not a finite-size artifact and persists in the large-$N$ limit of the finite ensemble.
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/tests/phase2_binding_certificate.json:24:    "provenance_present": true
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/A_provenance.tex:1:\section{Computational Provenance (Appendix)}
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/01_introduction.tex:26:The goal of Phase~2 is to demonstrate that this mechanism can reproduce a vacuum energy scale compatible with cosmological observations in a setting that approximates realistic quantum field behavior.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/04_numerical_experiments.tex:10:All figures presented here are generated automatically via the Phase~2 workflow and are reproducible from the accompanying configuration and run logs.
/Users/dri/Documents/Projects/origin-axiom/phase2/_paper_backups/paper_20251228T011539Z/sections/04_numerical_experiments.tex:59:This saturation confirms that the residual is not a finite-size artifact and persists in the large-$N$ limit of the finite ensemble.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/00_abstract.tex:4:We report Phase~II of the \emph{Origin Axiom} program: a reproducible, claim-audited demonstration that a strict global \emph{non-cancellation floor} can be threaded through a minimal chain linking (i) a flavor-inspired phase anchor, (ii) a toy vacuum sector, and (iii) a toy cosmological background, without inducing numerical instability or uncontrolled dynamics.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/sections/00_abstract.tex:15:We emphasize scope and falsifiability: Phase~II does not derive the axiom from a local action, does not claim a quantitative prediction for the observed cosmological constant, and treats the models as minimal testbeds. All figures are generated from tagged runs with explicit scripts, configurations, and run manifests, enabling full third-party reproduction.
/Users/dri/Documents/Projects/origin-axiom/phase2/paper/appendix/A_run_manifest.tex:12:Figure & Artifact stem & run\_id & git \\
/Users/dri/Documents/Projects/origin-axiom/phase2/outputs/paper_bundle/config/phase2.yaml:160:# Paper artifact mapping (for sanity checks)
```

## 7) Git status snapshot (informational)

```
 M phase2/AUDIT_REPORT.md
?? scripts/phase2_gate.sh
```

## 8) Next recommended Phase 2 rungs (after audit)

- P2-S1: Define Phase 2 paper spine + section contract (order, naming, invariants)
- P2-S2: Claims map hardening (CLAIMS.md -> paper table -> artifact paths)
- P2-S3: Provenance enforcement (git hash, params, seed, environment) in every run artifact
- P2-S4: Rewrite passes (structure first, then math/rigor), zero new claims until audits pass
