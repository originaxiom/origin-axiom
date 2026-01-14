# Phase 4 FRW-like toy: equations, masks, and external host alignment (v1)

Status: **Alignment memo – non-binding**

This note records, in one place, how the Phase 4 FRW-like *toy* module
is wired:

- what scalar quantities we actually use,
- how the FRW-inspired masks are defined,
- how we introduce a **flat-FRW background host** in Stage 2, and
- how the current empirical anchor box \((\Omega_\Lambda, t_0)\) sits
  inside that structure.

It is an **alignment document**, not a claims register. All physics
claims continue to live in:

- `phase4/SCOPE.md`
- `phase4/CLAIMS.md`
- `phase4/NON_CLAIMS.md`
- `phase4/PHASE4_ALIGNMENT_v1.md`
- Stage 2 belts (`stage2/frw_corridor_analysis/`,
  `stage2/joint_mech_frw_analysis/`,
  `stage2/frw_data_probe_analysis/`,
  `stage2/external_frw_host/`).

---

## 1. FRW-like toy quantities in Phase 4

The “FRW toy” that Phase 4 actually uses is deliberately minimal. It
is driven by a scalar

\[
  E_{\mathrm{vac}}(\theta) = \alpha\,A(\theta)^\beta
\]

constructed in the F1 mapping family (see
`phase4/FRW_TOY_DESIGN.md` and `phase4/FRW_SYNTHESIS.md` for the
design discussion). No physical units are assigned to
\(E_{\mathrm{vac}}\); it is a positive, rescalable scalar.

From this scalar and a fixed 1D \(\theta\)-grid we build tables such as:

- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`

These tables carry, among others, the columns:

- `theta` – the Phase 3/4 \(\theta\)-grid (shared across Stage 2).
- `E_vac` – the F1 scalar \(E_{\mathrm{vac}}(\theta)\).
- `omega_lambda` – an *effective* Λ–like fraction, treated as a
  dimensionless parameter that roughly plays the role of
  \(\Omega_\Lambda\).
- `age_Gyr` – a toy “age of the universe” in Gyr, derived from
  `omega_lambda` via an internal mapping fixed within the Phase 4 toy.
  This mapping is **monotone** in `omega_lambda` but is **not** treated
  as a precise implementation of the standard FRW age integral.
- FRW-background flags (from `phase4_F1_frw_viability_mask.csv`):
  - `has_big_bang` (or equivalent): did the toy FRW history start at a
    finite past singularity?
  - `has_matter_era`: did the history exhibit a matter-dominated phase?
  - `has_late_accel`: did the late-time expansion accelerate?
  - `smooth_H2`: did the discrete Hubble-like profile avoid spikes?
  - `frw_viable`: a Boolean combining these background checks into a
    coarse “FRW-like, not pathological” mask.
- Toy “data probe” flags (from `phase4_F1_frw_data_probe_mask.csv`):
  - `data_ok` plus its components (`has_matter_era`, `has_late_accel`,
    `smooth_H2`, etc.), used as a **pseudo-data** filter in Stage 2.

At the toy level, Phase 4 interprets these quantities narrowly:

> Does a given \(\theta\) produce a scalar \(E_{\mathrm{vac}}(\theta)\)
> that can be embedded in a qualitatively FRW-like background (via
> `omega_lambda`, `age_Gyr`, and the FRW flags), and does it pass our
> coarse pseudo-data checks?

No direct contact with real cosmological data is made at this layer.

---

## 2. Flat-FRW background host introduced in Stage 2

To decouple **“equations of FRW”** from the **toy mapping** used in
Phase 4, Stage 2 introduces an explicit **flat-FRW background host**
in `stage2/external_frw_host/`.

The idea is:

- treat the Phase 4 `omega_lambda` column as an effective
  \(\Omega_\Lambda\) parameter,
- assume a spatially flat FRW universe with matter + Λ and no
  radiation,
- compute a standard FRW background age for each \(\Omega_\Lambda\),
- compare that “host age” to the toy `age_Gyr` that lives in Phase 4.

### 2.1. Host equations (background only)

On the host side we assume:

- Spatially flat FRW with matter + Λ:

\[
  \Omega_m + \Omega_\Lambda = 1, \quad
  \Omega_\Lambda \equiv \texttt{omega\_lambda}, \quad
  \Omega_m = 1 - \Omega_\Lambda.
\]

- Neglect radiation, curvature, and any extra components.
- Use a dimensionless scale factor \(a \in (0, 1]\) with \(a=1\) today.

Define the dimensionless Hubble function

\[
  E(a; \Omega_\Lambda)
  \;=\; \sqrt{ \Omega_m a^{-3} + \Omega_\Lambda }
  \;=\; \sqrt{ (1 - \Omega_\Lambda) a^{-3} + \Omega_\Lambda }.
\]

Then the **dimensionless age** of the universe in this host model is

\[
  t_0^{\text{(host)}}(\Omega_\Lambda)
  \;=\; \int_{0}^{1} \frac{da}{a\,E(a;\Omega_\Lambda)}.
\]

Stage 2 evaluates this integral numerically for each
\(\Omega_\Lambda = \texttt{omega\_lambda}\) using a simple trapezoid
rule on a dense grid in \(a\).

To convert to Gyr we introduce a single calibration factor

\[
  \mathcal{C}_{\text{age}} \;[\mathrm{Gyr}]
  \quad\text{so that}\quad
  t_{0,\mathrm{host}}^{\mathrm{Gyr}}
  = \mathcal{C}_{\text{age}} \,
    t_0^{\text{(host)}}(\Omega_\Lambda).
\]

In the current Stage 2 implementation:

- \(\mathcal{C}_{\text{age}}\) is chosen empirically from the Phase 4
  grid so that the host ages match the toy ages as closely as possible
  on the FRW-viable subset; numerically this comes out to

  \[
    \mathcal{C}_{\text{age}} \approx 2.75~\mathrm{Gyr}
  \]

  (see `stage2/external_frw_host/outputs/tables/`
  `stage2_external_frw_rung1_age_crosscheck_v1.csv` for the precise
  value and diagnostics).

This host is **not** a new “Phase 4 model”; it is a diagnostic:
a standard FRW background attached downstream of the Phase 4 toy.

---

## 3. Empirical anchor box in \((\Omega_\Lambda, t_0)\)

Stage 2 introduces a small **empirical anchor box** in the space of
background observables \((\Omega_\Lambda, t_0)\), encoded in

- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

and applied to the Phase 4 toy table via

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
- output:
  `stage2/frw_data_probe_analysis/outputs/tables/`
  `stage2_frw_empirical_anchor_mask_v1.csv`.

At the time of this memo:

- The anchor box is centred near
  \[
    \Omega_\Lambda \simeq 0.69, \qquad
    t_0 \simeq 13.5~\mathrm{Gyr},
  \]
  with small half-widths in both directions (specified precisely in the
  JSON config file).
- Applying this box to the Phase 4 FRW table yields:
  - total grid size: \(N_{\theta} = 2048\);
  - anchor set size: \(N_{\text{anchor}} = 18\);
  - fraction of grid in the anchor:
    \[
      \frac{N_{\text{anchor}}}{N_{\theta}}
      \approx 0.0088.
    \]

The Stage 2 joint mech–FRW belt combines this anchor mask with the
FRW viability and toy corridor masks to study intersections such as

- `FRW_VIABLE_AND_ANCHOR`
- `CORRIDOR_AND_ANCHOR`
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`

(see
`stage2/joint_mech_frw_analysis/outputs/tables/`
`stage2_joint_mech_frw_anchor_intersections_v1.csv`,
`stage2_joint_mech_frw_anchor_kernel_v1.csv`,
`stage2_joint_mech_frw_anchor_profiles_v1.csv`,
`stage2_joint_mech_frw_anchor_sensitivity_v1.csv`).

These tables show, in particular, that:

- there **are** \(\theta\)-points that lie in the intersection

  \[
    \text{FRW-viable} \;\wedge\;
    \text{toy corridor} \;\wedge\;
    \text{anchor box},
  \]

  but the resulting “kernel” consists of only 18 grid points, split into
  two short contiguous segments in \(\theta\);
- within this kernel, both the Phase 4 toy `age_Gyr` and the host FRW
  age are tightly clustered around \(\sim 13.5~\mathrm{Gyr}\), but they
  differ by \(\mathcal{O}(10~\mathrm{Gyr})\) in absolute terms when we
  compare them across the broader FRW-viable corridor (see below).

---

## 4. Summary of current toy vs host age contrast

The Stage 2 host-analysis belt collects summary statistics in

- `stage2/external_frw_host/outputs/tables/`
  `stage2_external_frw_rung1_age_crosscheck_v1.csv`
- `stage2/external_frw_host/outputs/tables/`
  `stage2_external_frw_rung2_age_contrast_v1.csv`.

At the time of this memo, the key numbers (using the host age defined
in §2 and the anchor box from §3) are:

- **ALL_GRID** (all 2048 \(\theta\)-points):
  - \(\langle \Delta t_0 \rangle \approx -8.41~\mathrm{Gyr}\),
  - \(\langle |\Delta t_0| / t_{0,\mathrm{toy}} \rangle \approx 0.53\),
  - i.e. large, sign-consistent differences between the toy and host
    ages across the full grid.

- **FRW_VIABLE** (Phase 4 FRW background mask applied):
  - \(N \approx 1016\),
  - \(\langle \Delta t_0 \rangle \approx -2.49~\mathrm{Gyr}\),
  - \(\langle |\Delta t_0| / t_{0,\mathrm{toy}} \rangle \approx 0.18\),
  - i.e. the toy `age_Gyr` and the host FRW age are closer, but still
    differ at the \(\sim 20\%\) level on average.

- **CORRIDOR_AND_VIABLE** (toy corridor ∧ FRW viable):
  - \(N \approx 154\),
  - \(\langle \Delta t_0 \rangle \approx -11.86~\mathrm{Gyr}\),
  - \(\langle |\Delta t_0| / t_{0,\mathrm{toy}} \rangle \approx 0.84\),
  - i.e. within the corridor that Phase 4 currently treats as “toy-good”
    and FRW-viable, the toy ages differ dramatically from the host
    ages.

- **CORRIDOR_AND_VIABLE_AND_ANCHOR** (our current “anchor kernel”):
  - \(N = 18\),
  - \(\langle \Delta t_0 \rangle \approx -10.87~\mathrm{Gyr}\),
  - \(\langle |\Delta t_0| / t_{0,\mathrm{toy}} \rangle \approx 0.81\).

Taken together, these numbers say:

> The *shapes* and qualitative masks used by the Phase 4 FRW toy behave
> roughly FRW-like, but the **absolute age calibration** of
> `age_Gyr` in the toy differs significantly from a standard flat-FRW
> background once we attach a realistic \((\Omega_\Lambda, t_0)\) box.

This is not a bug in the Phase 4 toy; it reflects that:

- the original FRW toy was built as a **diagnostic scaffold**, not a
  precision FRW age calculator;
- we are now explicitly separating:
  - **toy-level diagnostics** (Phase 4 tables and masks),
  - **host-level background equations** (Stage 2 external FRW host),
  - **empirical anchors** (narrow \((\Omega_\Lambda, t_0)\) box),
  - and **mechanism correlation structure** (Stage 2 joint mech–FRW
    belts).

---

## 5. How this memo should be used

1. **For Phase 4**  
   This file documents what “FRW-like” means at the toy level and how
   the quantities in `phase4_F1_frw_*` tables relate to a standard
   FRW background. Any future changes to:

   - the definition of `omega_lambda`,
   - the internal mapping used to compute `age_Gyr`, or
   - the FRW viability masks

   should be recorded here and cross-referenced in
   `phase4/PHASE4_ALIGNMENT_v1.md`.

2. **For Stage 2 belts**  
   This memo serves as the equation-level anchor for:

   - `stage2/frw_corridor_analysis` (how FRW masks are interpreted),
   - `stage2/frw_data_probe_analysis` (how the empirical anchor box is
     defined and applied),
   - `stage2/external_frw_host` (what equations the host solves),
   - `stage2/joint_mech_frw_analysis` (how mech/FRW/anchor intersections
     are interpreted).

3. **For future “real data” contact**  
   Before any promotion to *real* data contact (Planck, BAO, SN, etc.),
   this memo should be revisited and extended with:

   - explicit Hubble-constant and unit choices,
   - any additional background components,
   - links to whatever external pipelines (CLASS/CCL/Cobaya/…) are used
     as hosts.

Until then, the statements in this file remain **diagnostic and
structural**, not physics claims.

