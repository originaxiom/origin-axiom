# Stage 2 – Discrete obstruction kernel lemma (v1)

## 1. Scope and setup

This memo records the discrete obstruction patterns visible in the current Stage 2 FRW and obstruction pipeline, at the level of the fixed 2048 point \`θ\` grid and the masks produced by Phase 4 and Stage 2. It does not introduce new computations or change any Phase 0–5 contracts or Stage 2 promotion gates; it summarises existing CSV artifacts in set language.

We work on a fixed discrete grid
\[
\Theta_{\mathrm{grid}} = \{\theta_0, \theta_1, \dots, \theta_{N-1}\}, \quad N = 2048
\]
corresponding to the \`theta\` column in the Phase 4 FRW mask tables and the Stage 2 obstruction tables.

For each \(\theta_i \in \Theta_{\mathrm{grid}}\) we have:
- a Phase 4 FRW tuple \(F(\theta_i) = (E_{\mathrm{vac}}(\theta_i), \omega_\Lambda(\theta_i), \text{age}_{\mathrm{Gyr}}(\theta_i), \dots)\),
- Phase 4 Boolean masks:
  - \`frw_viable(\theta_i)\`,
  - \`lcdm_like(\theta_i)\`,
  - the toy FRW corridor flag \`in_toy_corridor(\theta_i)\),
- Stage 2 obstruction helper flags derived from the static kernel and external–style corridors:
  - \`in_pre_data_kernel(\theta_i)\) from \`stage2_obstruction_static_frw_kernel_v1.csv\`,
  - \`external_age_corridor_v2(\theta_i)\) from \`stage2_obstruction_external_age_corridor_v2.csv\`,
  - age and expansion proxies from \`stage2_obstruction_external_age_expansion_corridors_v1.csv\`.

All statements below are read off from the current snapshot of these CSVs.

## 2. Sets and masks

We define the following subsets of $begin:math:text$\\Theta\_\{\\mathrm\{grid\}\}$end:math:text$:

- Full grid:
  $begin:math:display$
  \\Theta\_\{\\mathrm\{grid\}\} \= \\\{\\theta\_i \\mid 0 \\le i \< 2048\\\}\.
  $end:math:display$

- Pre-data kernel $begin:math:text$K$end:math:text$:
  $begin:math:display$
  K \= \\\{\\theta \\in \\Theta\_\{\\mathrm\{grid\}\} \\mid \\texttt\{in\_pre\_data\_kernel\}\(\\theta\) \= 1\\\}\.
  $end:math:display$

- LCDM-like band $begin:math:text$L$end:math:text$:
  $begin:math:display$
  L \= \\\{\\theta \\in \\Theta\_\{\\mathrm\{grid\}\} \\mid \\texttt\{lcdm\_like\}\(\\theta\) \= 1\\\}\.
  $end:math:display$

- Internal toy FRW corridor $begin:math:text$C\_\{\\mathrm\{toy\}\}$end:math:text$:
  $begin:math:display$
  C\_\{\\mathrm\{toy\}\} \= \\\{\\theta \\in \\Theta\_\{\\mathrm\{grid\}\} \\mid \\texttt\{in\_toy\_corridor\}\(\\theta\) \= 1\\\}\.
  $end:math:display$

- External-style age corridor (v2) $begin:math:text$A\_\{\\mathrm\{ext\}\}$end:math:text$:
  $begin:math:display$
  A\_\{\\mathrm\{ext\}\} \= \\\{\\theta \\in \\Theta\_\{\\mathrm\{grid\}\} \\mid \\texttt\{external\\\_age\\\_corridor\\\_v2\}\(\\theta\) \= 1\\\}\.
  $end:math:display$
  In the current snapshot this corresponds to an age band of the form $begin:math:text$\[12\, 15\]$end:math:text$ Gyr applied to the FRW age column.

- External-style age and expansion proxies (v1):
  from \`stage2_obstruction_external_age_expansion_corridors_v1.csv\) we use:
  - a broad age band \(A_{\mathrm{broad}}\) (\`AGE_BROAD_V1\)),
  - a tight age band $begin:math:text$A\_\{\\mathrm\{tight\}\}$end:math:text$ (\`AGE_TIGHT_V1\)),
  - broad and tight expansion bands \(X_{\mathrm{broad}}\), \(X_{\mathrm{tight}}\) (\`EXPANSION_BROAD_V1\`, \`EXPANSION_TIGHT_V1\)),
  - basic and tight structure proxies $begin:math:text$S\_\{\\mathrm\{basic\}\}$end:math:text$, $begin:math:text$S\_\{\\mathrm\{tight\}\}$end:math:text$ (\`STRUCT_PROXY_BASIC_V1\`, \`STRUCT_PROXY_TIGHT_V1\)).

We denote intersections such as
\[
K \cap L,\quad K \cap L \cap C_{\mathrm{toy}},\quad K \cap A_{\mathrm{ext}},\quad K \cap S_{\mathrm{tight}}
\]
by the obvious set notation and by the corresponding family names in the summary CSVs.

## 3. Numerical facts from the current snapshot

All counts and fractions in this section are taken directly from the Stage 2 summary tables at the time of this memo.

### 3.1 Grid and pre-data kernel

From \`stage2_obstruction_static_frw_kernel_v1.csv\) and its family summary:

- Total grid size:
  - $begin:math:text$\|\\Theta\_\{\\mathrm\{grid\}\}\| \= 2048$end:math:text$.
- Pre-data kernel:
  - $begin:math:text$\|K\| \= 1016$end:math:text$,
  - so $begin:math:text$\|K\| \/ \|\\Theta\_\{\\mathrm\{grid\}\}\| \\approx 0\.496$end:math:text$.

Interpretation: about half of the $begin:math:text$\\theta$end:math:text$ grid passes the Phase 4 FRW sanity and viability checks and forms the static pre-data kernel used throughout the obstruction program.

### 3.2 External age corridor (v2)

From \`stage2_obstruction_external_age_corridor_summary_v2.csv\):

- External age band \(A_{\mathrm{ext}}\):
  - \(|A_{\mathrm{ext}}| = 358\),
  - \(|A_{\mathrm{ext}}| / |\Theta_{\mathrm{grid}}| \approx 0.175\),
  - \(|K \cap A_{\mathrm{ext}}| = 356\),
  - \(|K \cap A_{\mathrm{ext}}| / |K| \approx 0.350\).

In other words, a nontrivial age band retains roughly 35% of the pre-data kernel; the age corridor does not come close to annihilating the kernel.

The same summary records a 40-point sweet subset
\[
K_{\mathrm{sweet,age}} = K \cap L \cap C_{\mathrm{toy}} \cap A_{\mathrm{ext}}
\]
via the family \`KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2\) with
- $begin:math:text$\|K\_\{\\mathrm\{sweet\,age\}\}\| \= 40$end:math:text$,
- $begin:math:text$\|K\_\{\\mathrm\{sweet\,age\}\}\| \/ \|\\Theta\_\{\\mathrm\{grid\}\}\| \\approx 0\.0195$end:math:text$,
- $begin:math:text$\|K\_\{\\mathrm\{sweet\,age\}\}\| \/ \|K\| \\approx 0\.0394$end:math:text$.

Thus a small but non-empty fraction of the pre-data kernel survives the combination of:
- FRW viability,
- LCDM-likeness,
- the toy FRW corridor,
- and the nontrivial age band.

### 3.3 External age, expansion, and structure proxies (v1)

From \`stage2_obstruction_external_age_expansion_summary_v1.csv\):

- Broad age band \(A_{\mathrm{broad}}\) (\`AGE_BROAD_V1\)):
  - $begin:math:text$\|A\_\{\\mathrm\{broad\}\}\| \= 933$end:math:text$,
  - $begin:math:text$\|A\_\{\\mathrm\{broad\}\}\| \/ \|\\Theta\_\{\\mathrm\{grid\}\}\| \\approx 0\.456$end:math:text$,
  - $begin:math:text$\|K \\cap A\_\{\\mathrm\{broad\}\}\| \= 931$end:math:text$,
  - $begin:math:text$\|K \\cap A\_\{\\mathrm\{broad\}\}\| \/ \|K\| \\approx 0\.916$end:math:text$.

- Tight age band $begin:math:text$A\_\{\\mathrm\{tight\}\}$end:math:text$ (\`AGE_TIGHT_V1\)):
  - \(|A_{\mathrm{tight}}| = 126\),
  - \(|A_{\mathrm{tight}}| / |\Theta_{\mathrm{grid}}| \approx 0.062\),
  - \(|K \cap A_{\mathrm{tight}}| = 126\),
  - \(|K \cap A_{\mathrm{tight}}| / |K| \approx 0.124\).

- Broad expansion band \(X_{\mathrm{broad}}\) (\`EXPANSION_BROAD_V1\)):
  - $begin:math:text$\|X\_\{\\mathrm\{broad\}\}\| \= 94$end:math:text$,
  - $begin:math:text$\|X\_\{\\mathrm\{broad\}\}\| \/ \|\\Theta\_\{\\mathrm\{grid\}\}\| \\approx 0\.046$end:math:text$,
  - $begin:math:text$\|K \\cap X\_\{\\mathrm\{broad\}\}\| \= 94$end:math:text$,
  - $begin:math:text$\|K \\cap X\_\{\\mathrm\{broad\}\}\| \/ \|K\| \\approx 0\.093$end:math:text$.

- Tight expansion band $begin:math:text$X\_\{\\mathrm\{tight\}\}$end:math:text$ (\`EXPANSION_TIGHT_V1\)):
  - \(|X_{\mathrm{tight}}| = 51\),
  - \(|X_{\mathrm{tight}}| / |\Theta_{\mathrm{grid}}| \approx 0.025\),
  - \(|K \cap X_{\mathrm{tight}}| = 51\),
  - \(|K \cap X_{\mathrm{tight}}| / |K| \approx 0.050\).

- Basic structure proxy \(S_{\mathrm{basic}}\) (\`STRUCT_PROXY_BASIC_V1\)):
  - $begin:math:text$\|S\_\{\\mathrm\{basic\}\}\| \= 931$end:math:text$,
  - $begin:math:text$\|S\_\{\\mathrm\{basic\}\}\| \/ \|\\Theta\_\{\\mathrm\{grid\}\}\| \\approx 0\.455$end:math:text$,
  - $begin:math:text$\|K \\cap S\_\{\\mathrm\{basic\}\}\| \= 931$end:math:text$,
  - $begin:math:text$\|K \\cap S\_\{\\mathrm\{basic\}\}\| \/ \|K\| \\approx 0\.916$end:math:text$.

- Tight structure proxy $begin:math:text$S\_\{\\mathrm\{tight\}\}$end:math:text$ (\`STRUCT_PROXY_TIGHT_V1\)):
  - \(|S_{\mathrm{tight}}| = 51\),
  - \(|S_{\mathrm{tight}}| / |\Theta_{\mathrm{grid}}| \approx 0.025\),
  - \(|K \cap S_{\mathrm{tight}}| = 51\),
  - \(|K \cap S_{\mathrm{tight}}| / |K| \approx 0.050\).

These numbers show that even fairly tight expansion and structure-proxy bands select small but non-empty subsets of the kernel. The combined intersections of these bands with \(K\), \(L\), and \(C_{\mathrm{toy}}\) are small but not empty in the present snapshot; they will be used as targets in later obstruction rungs.

## 4. Discrete obstruction lemma (v1)

We can summarise the current discrete situation as follows.

Let \(\Theta_{\mathrm{grid}}\), \(K\), \(L\), \(C_{\mathrm{toy}}\), \(A_{\mathrm{ext}}\), \(A_{\mathrm{tight}}\), \(X_{\mathrm{tight}}\), and \(S_{\mathrm{tight}}\) be defined as above. Then, in the current Stage 2 snapshot:

1. The pre-data kernel \(K\) is non-empty and occupies roughly half of the \(\theta\) grid:
   \[
   0 < |K| \approx 0.50 \times |\Theta_{\mathrm{grid}}|.
   \]

2. The external-style age corridor \(A_{\mathrm{ext}}\) is non-trivial and removes a substantial fraction of the grid, but it does not annihilate the kernel:
   \[
   |K \cap A_{\mathrm{ext}}| \approx 0.35 \times |K| > 0.
   \]

3. The intersection of kernel, LCDM-like band, toy corridor, and external age corridor is still non-empty:
   \[
   K_{\mathrm{sweet,age}} = K \cap L \cap C_{\mathrm{toy}} \cap A_{\mathrm{ext}}, \quad |K_{\mathrm{sweet,age}}| = 40 > 0.
   \]

4. The combined external age and expansion proxies select small but non-empty subsets of the kernel, including a tight expansion and structure-proxy region with
   \[
   |K \cap X_{\mathrm{tight}}| = |K \cap S_{\mathrm{tight}}| = 51 > 0.
   \]

In words: with the current FRW pipeline and obstruction helpers, there is no choice of the present external-style age and expansion bands that collapses the static pre-data kernel to the empty set. A small but non-zero fraction of \(\Theta_{\mathrm{grid}}\) always survives the combination of FRW viability, internal toy corridors, LCDM-likeness, and the simple external-style bands in use.

This is not yet a continuum theorem; it is a fully reproducible discrete obstruction lemma for the 2048 point grid and the masks in the current repo snapshot. Later rungs will:
- attach the Phase 3 mechanism amplitudes \(A(\theta)\) to these surviving sets and study their floors,
- test robustness under grid refinement and parameter perturbations,
- and formulate a continuum obstruction conjecture that abstracts this pattern beyond the discrete grid.
