# Roadmap: Acts VI–VIII (Origin Axiom / θ★ programme)

Last updated: 2025-12-17

This roadmap records where we are after **Act V** and how we intend to climb from
the current “vacuum ↔ FRW” bridge to **particles, atoms and real observables**.

It is deliberately concrete and rung-based: each rung corresponds to one or more
scripts, figures and paper sections, following the `R#` convention used in
`PROGRESS_LOG.md` and the Act V LaTeX.

---

## 0. Where we stand after Act V

By the end of Act V we have:

- A **flavour-informed master phase**  
  \[
    \theta_\star \in [2.18, 5.54]\ \text{rad},\quad
    \theta_{\star,\mathrm{fid}} \simeq 3.63\ \text{rad},
  \]
  coming from Act II fits to PMNS + CKM (see Act II).

- A **microcavity toy** that converts θ★ into a vacuum-energy shift  
  \[
    \Delta E(\theta_\star)
  \]
  via a non-cancelling rule on a 1D lattice.

- A **calibrated effective vacuum mapping**  
  \[
    \Omega_\Lambda(\theta_\star)
    = \mathrm{clip}\!\left(k_{\rm scale}\,\Delta E(\theta_\star),\,0,\,0.999\right),
  \]
  with \(k_{\rm scale}\) fixed so that
  \(\Omega_\Lambda(\theta_{\star,\mathrm{fid}}) \simeq 0.7\).

- A family of **flat FRW models** labelled by θ★, with:
  - ages \(t_0(\theta_\star)\),
  - deceleration parameters \(q_0(\theta_\star)\),
  - toy distances \(d_L(z;\theta_\star)\),
  - linear growth factors \(D(a;\theta_\star)\).

- An **observable corridor** in θ★,
  \[
    \theta_{\star,\mathrm{corridor}} \simeq [2.43, 3.86]\ \mathrm{rad},
  \]
  for which:
  - \(\Omega_\Lambda \in [0.61, 0.78]\),
  - \(t_0 \in [12.5, 14.6]\ \mathrm{Gyr}\),
  - \(q_0 < 0\),
  - late-time growth suppression \(D_{\rm rel}(a=1) \sim 0.73\text{–}0.83\).

This is **not yet a prediction of Λ**, but it is a working chain:
\[
  \theta_\star
  \to \Delta E(\theta_\star)
  \to \Omega_\Lambda(\theta_\star)
  \to \{t_0, q_0, D(a)\},
\]
with a non-trivial θ★ corridor compatible with a ΛCDM-like universe.

Acts VI–VIII now ask: *can the same θ★ and non-cancelling logic live all the way
from this FRW picture down to neutrinos, baryons, and eventually atoms, without
contradicting basic observables?*

---

## 1. Act VI – Flavour and structure bridge

**Goal:**  
Connect the **cosmic θ★ corridor** to the **flavour sector** and a
σ₈-like growth amplitude, and define a **jointly allowed region** for θ★ that
is consistent with both flavour data and late-time structure growth.

### Act VI high-level questions

1. How does the **θ★ corridor** from Act V compare to the **Act II posterior**?
2. For θ★ values inside the corridor, do we still have acceptable PMNS + CKM
   fits (within the tolerances defined in Act II)?
3. Given the linear-growth scan \(D(a;\theta_\star)\), what does a **σ₈-like**
   amplitude look like along the corridor, and how does it compare to a rough
   ΛCDM target?
4. Can we define a **“cosmo+flavour compatible”** region in θ★ space, with
   clear numerical bounds?

### Planned rungs (Act VI)

These are **planned** R# labels; they may be refined but the intent should stay
stable.

- **R20 – Roadmap for Acts VI–VIII (this file)**  
  - Status: *completed planning rung.*  
  - Artefacts:
    - `docs/ROADMAP_ACT_VI_VIII.md` (this roadmap).
    - `PROGRESS_LOG.md` entry R20.

- **R21 – Flavour posterior export for Act VI**
  - Re-extract the Act II θ★ posterior used to define the prior band:
    - summary JSON, e.g. `data/processed/theta_star_flavour_posterior_summary.json`,
      containing at least:
      - mean / median / mode for θ★,
      - 68% and 95% credible intervals,
      - a small grid or sample of representative θ★ values.
  - Lock file format so Act VI scripts can import it without touching Act II code.

- **R22 – θ★ corridor vs. flavour posterior**
  - Script: `scripts/compare_theta_star_corridor_vs_flavour.py`
  - Inputs:
    - FRW/corridor summary (`theta_star_observable_corridor*.json`),
    - flavour posterior summary from R21.
  - Outputs:
    - Numerical comparison of:
      - overlap between flavour 68% / 95% intervals and the FRW corridor,
      - distance between flavour fiducial θ★ and corridor centre.
    - Small JSON summary + one figure (θ★ axis with bands and overlap).

- **R23 – σ₈-like amplitude along the corridor**
  - Re-interpret existing linear-growth scan
    `effective_vacuum_theta_growth_scan.npz` as a σ₈-like observable:
    - define \(\sigma_8^{\rm toy}(\theta_\star) \propto D_{\rm rel}(a=1;\theta_\star)\).
  - Script: `scripts/summarize_theta_star_sigma8_like.py`
  - Outputs:
    - stats for \(\sigma_8^{\rm toy}\) over:
      - full Act II band,
      - FRW observable corridor,
      - neighbourhood of flavour fiducial θ★.
    - One figure: \(\sigma_8^{\rm toy}(\theta_\star)\) with corridor and flavour
      bands marked.

- **R24 – Joint “cosmo + flavour” compatibility region**
  - Combine the **FRW corridor** and **flavour constraints** into a simple
    joint condition:
    \[
      \theta_\star \in \mathcal{I}_{\rm flavour} \cap \mathcal{I}_{\rm FRW},
    \]
    with explicit numerical endpoints.
  - Script: `scripts/select_theta_star_joint_corridor.py`
  - Output: JSON summary + short LaTeX subsection in Act VI.

- **R25 – Act VI LaTeX section**
  - File: `docs/paper/act6_flavour_structure_bridge.tex`
  - Content:
    - narrative of the above rungs,
    - one or two figures (θ★ overlap plot, σ₈-like plot),
    - final definition of the joint θ★ interval to be carried into Act VII.

---

## 2. Act VII – From θ★ to matter and baryons (toy sector)

**Goal:**  
Build a **toy matter sector** that lives on top of the θ★-selected vacuum and
is at least qualitatively compatible with **baryon fraction** and basic
large-scale structure, without over-claiming.

This act is intentionally modest and toy-like; it is about **consistency**, not
precision cosmology.

### Act VII high-level questions

1. Given a θ★ value in the joint region from Act VI, what **matter content**
   (Ω\_b, Ω\_c, Ω\_m) do we assume in the toy universe?
2. Can we define a simple **baryon fraction** \(f_b = \Omega_b / \Omega_m\)
   that is compatible with the θ★ corridor and non-cancelling principle?
3. How does this choice impact the **growth history** and our toy σ₈-like
   amplitude?
4. Can we phrase the outcome as a **consistency statement**:
   “There exists a θ★ interval and a simple matter composition such that
   background + growth resemble a ΛCDM-like universe”?

### Planned rungs (Act VII)

- **R26 – Toy matter budget on θ★-selected vacuum**
  - Define a small set of toy matter compositions
    (e.g. Ω\_b, Ω\_c pairs) consistent with
    \(\Omega_\Lambda(\theta_\star)\) in the joint region.
  - Script: `scripts/build_theta_star_matter_budget_grid.py`
  - Output: grid of (θ★, Ω\_b, Ω\_c, Ω\_m, Ω\_Λ) in an NPZ file.

- **R27 – Growth and background with toy matter**
  - For each combination from R26, recompute simple FRW histories and linear
    growth factors (re-using existing FRW/growth machinery).
  - Output: summary of how sensitive the toy σ₈-like observable is to changes
    in Ω\_b and Ω\_c within the θ★ joint region.

- **R28 – Consistency window in (θ★, Ω\_b, Ω\_m) space**
  - Select combinations that:
    - live within the joint θ★ region from Act VI,
    - have reasonable H0 t0, q0,
    - have a σ₈-like amplitude not wildly different from a rough ΛCDM target.
  - Output: JSON summary + one figure.

- **R29 – Act VII LaTeX section**
  - File: `docs/paper/act7_matter_sector_toy.tex`
  - Content:
    - definition of the toy matter sector and its relation to θ★,
    - description of the consistency window,
    - clear statement of limitations (no detailed CMB, no full Boltzmann code).

---

## 3. Act VIII – Towards atoms and observational hooks

**Goal:**  
Sketch how a θ★-labelled vacuum and toy matter sector could, in principle,
connect to **atoms and concrete observables**, without pretending we have a full
particle-physics model. Act VIII is more of a **conceptual and structural act**
than a heavy numerical one.

### Act VIII high-level questions

1. Given the θ★ region from Acts VI–VII, what are the **natural next observables**
   to target?
   - e.g. a toy σ₈–like amplitude vs. a rough Planck/galaxy-survey target,
   - simple proxies for BAO scale or distance ladder (already partially covered).
2. How could θ★ enter **particle masses, couplings, or mixings** in a way that
   is at least qualitatively compatible with known atoms and chemistry?
3. How do we cleanly separate:
   - what the current Origin Axiom model actually does,
   - what is left as an open programme for future work?

### Planned rungs (Act VIII)

- **R30 – Observational hooks catalogue**
  - Non-numerical but precise:
    - list the key observables we eventually want to match:
      H0, Ω\_m, Ω\_Λ, σ₈, simple neutrino mass/angle targets, etc.
  - File: `docs/OBSERVABLE_HOOKS_CHECKLIST.md`.

- **R31 – Toy σ₈ and distance comparison**
  - Using the σ₈-like amplitude and distance curves from Acts V–VII, define
    a small set of **dimensionless comparison ratios** to standard ΛCDM
    (no direct data fit, just “are we in the right ballpark?”).
  - Script: `scripts/compare_toy_observables_to_LCDM_ratios.py`.
  - Output: table + figure.

- **R32 – Act VIII LaTeX section (atoms and outlook)**
  - File: `docs/paper/act8_atoms_and_outlook.tex`
  - Content:
    - clear summary of what is actually achieved:
      θ★ corridor, effective vacuum, growth, joint region with flavour,
      toy matter sector.
    - explicit list of “missing steps” from here to real atoms and chemistry.
    - roadmap for how a more complete model could promote θ★ and the
      non-cancelling rule into a realistic particle sector.

---

## 4. Usage notes

- This roadmap is a **living document** but the *structure* (Act VI–VIII goals
  and main rung labels) should not be changed lightly.
- Each rung:
  - must have a corresponding entry in `PROGRESS_LOG.md`,
  - should clearly list which files/scripts it touches,
  - should be visible in the repo history (one or more commits with R# in the
    message).
- If a rung is later superseded, we keep it in the log and mark the replacement
  instead of silently rewriting history.