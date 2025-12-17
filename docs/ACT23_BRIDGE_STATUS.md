# Act II/III θ★ bridge status (microcavity → effective vacuum → FRW)

**Date:** 2025-12-17  
**Repo:** `origin-axiom`  

This note freezes the current status of the Act II/III bridge that runs from a flavor-based θ★ prior to an effective cosmological constant in a flat FRW toy universe. It is deliberately descriptive and modest: we record what has been implemented and what it is allowed to claim, and we list the missing pieces before any serious comparison to observational data.

## 1. Inputs and internal chain

1. **Flavor-side θ★ prior**  
   - Configuration file: `config/theta_star_config.json`  
   - Fiducial value: `theta_star_fid_rad ≈ 3.63`  
   - Prior band: `theta_star_band_rad ≈ [2.18, 5.54]`  
   - Provenance: PMNS+CKM fits in the separate `origin-axiom-theta-star` repo.  
   - Interpretation: this is a working “Act II θ★ prior” that we treat as an external input to the vacuum / FRW toys.

2. **1D microcavity ΔE(θ★) scan**  
   - File: `data/processed/theta_star_microcavity_scan_full_2pi.npz`  
   - Content: θ★ grid over 0–2π, baseline energy `E0_uniform`, cavity energy `E0_cavity`, and vacuum shift `delta_E = E0_cavity − E0_uniform`.  
   - Behaviour: the microcavity lowers the vacuum energy (negative ΔE) in a broad valley that includes the Act II θ★ band, with a minimum near θ★ ≈ π and ΔE(θ★_fid) ≈ −5.3×10⁻³ (dimensionless).

3. **Effective vacuum scaling ΩΛ(θ★)**  
   - Core summary: `data/processed/theta_star_microcavity_core_summary.json`  
   - Contains:
     - `theta_fid_nominal = 3.63` rad,
     - `delta_E_fid ≈ −5.33×10⁻³`,
     - `omega_lambda_target = 0.7`,
     - `k_scale ≈ −1.31×10²`.  
   - Definition:
     - `Omega_Lambda(theta_star) = clip(k_scale * delta_E(theta_star), 0, 0.999)`.  
   - By construction: `Omega_Lambda(theta_star_fid) ≈ 0.7`, `Omega_m(theta_star_fid) ≈ 0.3`.

4. **Band scan, ensemble, and random-walk**  
   - Band scan (R4): `data/processed/effective_vacuum_band_scan.npz`  
     - θ★ band `[2.18, 5.54]` rad, 41 samples.  
     - ΩΛ range in band: `[0, ≈0.775]`.  
     - “Corridor” where `|ΩΛ − 0.7| ≤ 0.05`: 9/41 points, `theta_corridor ≈ [2.516, 3.692]` rad.  
   - Patch ensemble (R5): `data/processed/effective_vacuum_patch_ensemble.npz`  
     - N = 1000 patches with θ★ uniform in the band.  
     - ΩΛ statistics: mean ≈ 0.445, median ≈ 0.573, std ≈ 0.307, range `[0, ≈0.775]`.  
     - Fractions near ΩΛ ≈ 0.7:
       - `|ΩΛ − 0.7| ≤ 0.05`: 215/1000 ≈ 21.5%  
       - `|ΩΛ − 0.7| ≤ 0.02`: 80/1000 ≈ 8.0%  
       - `|ΩΛ − 0.7| ≤ 0.01`: 39/1000 ≈ 3.9%  
   - Random-walk residence (R6): `data/processed/theta_star_random_walk_residence.npz`  
     - 200 trajectories × 2000 steps in θ★ band with reflecting boundaries.  
     - Residence-time fractions in ΩΛ windows:
       - `|ΩΛ − 0.7| ≤ 0.05`: ≈ 20.5%  
       - `|ΩΛ − 0.7| ≤ 0.02`: ≈ 7.4%  
       - `|ΩΛ − 0.7| ≤ 0.01`: ≈ 3.7%  
     - Qualitative conclusion: the dynamical toy spends O(10%) of its “time” in a ΛCDM-like ΩΛ band without being tuned to a single θ★ value.

5. **FRW histories and observables (R2/R3/R10)**  
   - Scripts:
     - `src/run_frw_from_effective_vacuum.py`
     - `scripts/compare_frw_observables.py`
     - `scripts/compare_hubble_diagram.py`
     - `scripts/summarize_effective_vacuum_observables.py`  
   - Outputs:
     - Matter-only: (Ω_m, ΩΛ) = (1.0, 0.0).  
       - Age: `t0 ≈ 9.3 Gyr` for H₀ ≈ 70 km/s/Mpc.  
       - Deceleration: `q0 ≈ +0.5` (always decelerating).  
     - Effective vacuum (θ★-backed): (Ω_m, ΩΛ) ≈ (0.3, 0.7).  
       - Age: `t0 ≈ 13.5 Gyr`.  
       - Deceleration: `q0 ≈ −0.55` (accelerating).  
       - Luminosity distances d_L(z)/(c/H₀) at z = {0.3, 0.5, 1.0} are all larger than in the matter-only case, matching the qualitative “fainter SNe in an accelerating universe” expectation.

## 2. What this bridge is allowed to claim

Within this repo and at the current level of approximation, we are allowed to claim the following:

1. There exists a **flavor-informed θ★ band and fiducial point** (imported from `origin-axiom-theta-star`) that we treat as an external prior for the vacuum sector.  
2. A simple 1D **microcavity toy** with θ★-dependent mass profile produces a non-trivial vacuum shift ΔE(θ★) whose valley lies inside the flavor-based θ★ band.  
3. A **single scaling parameter** `k_scale` can map ΔE(θ★) to an effective ΩΛ(θ★) such that at θ★_fid we reproduce an illustrative ΩΛ ≈ 0.7, Ω_m ≈ 0.3.  
4. Within the microcavity-selected θ★ band, the resulting ΩΛ(θ★) is not sharply peaked at 0.7:  
   - O(10–20%) of static patches or random-walk time-samples fall into ΩΛ = 0.70 ± 0.05.  
   - Our own patch (ΩΛ ≈ 0.7) is therefore “typical” in this toy θ★ ensemble, not exponentially fine-tuned to one isolated angle.  
5. When plugged into a **flat FRW toy model**, the θ★-backed effective vacuum produces:  
   - An age and deceleration parameter in the **qualitative** regime of standard ΛCDM,  
   - A distance–redshift relation where standard candles appear fainter than in a matter-only universe, as expected in an accelerating cosmology.

All of these claims are explicitly **model-dependent** (1D cavity, linear scaling, no realistic field content) and are understood as scaffold-level checks, not a final theory.

## 3. Limitations and open gaps

The current bridge has several deliberate limitations:

1. **Toy microphysics**  
   - The cavity is one-dimensional, with a hand-chosen mass modulation and parameters tuned for numerical convenience, not derived from a full Origin-Axiom microstructure.  
   - There is no direct link yet between this cavity and the 4D lattice Δα(θ) constructions used elsewhere in the project.

2. **Linear, single-parameter scaling**  
   - ΩΛ(θ★) = k_scale × ΔE(θ★) with a single k_scale fixed at θ★_fid.  
   - No attempt is made to derive k_scale from first principles (e.g. physical units, volume factors, or renormalisation arguments).  
   - Alternative non-linear mappings (e.g. thresholds, saturation, multi-scale effects) are not explored.

3. **Toy FRW and limited components**  
   - Only matter + vacuum in a flat FRW background with H₀ ≈ 70 km/s/Mpc.  
   - No radiation, no curvature, no massive neutrinos, no detailed baryon or dark-matter modelling.  
   - H₀ is chosen “by hand” rather than being derived from the microcavity or θ★ sector.

4. **No actual fit to real data (yet)**  
   - We compare only **qualitative** behaviours (age scale, sign of q0, relative luminosity distances).  
   - There is no χ² or likelihood analysis against real SN Ia, BAO, CMB, or H(z) datasets in this repo.  
   - The pipeline is not wired to any real catalogue; all distances and ages are internal toy predictions.

5. **Scaling to physical ρΛ is only exploratory**  
   - Scripts like `scripts/estimate_lambda_scaling.py` treat ΔE(θ★) as a dimensionless proxy and estimate what physical energy-density scale per unit ΔE would be required to match ρΛ,obs.  
   - This is explicitly a **back-of-the-envelope scaling exercise**, not a rigorous derivation of Λ from microphysics.

## 4. Next steps before touching real data

Before we use this bridge in any serious observational test, we should:

1. **Separate “toy branch” vs “physics branch”**  
   - Clearly label the current microcavity + FRW path as a toy / scaffold branch in the paper and repo.  
   - Decide which subset of its results (if any) will enter the main Origin-Axiom narrative versus a methods appendix.

2. **Design a proper data interface (likely another repo or module)**  
   - Define which observables we want to confront first: SN Ia Hubble diagram, H(z) measurements, BAO distance scale, or simplified CMB distance priors.  
   - Build a clean interface where the only inputs are (Ω_m, ΩΛ, H₀) or a small extended parameter set, without exposing internal microcavity details.  
   - Keep this interface modular so different vacuum models (microcavity, lattice, cancellation system) can plug into the same cosmology layer.

3. **Upgrade the FRW engine**  
   - Add radiation and optionally curvature and massive neutrinos.  
   - Allow for arbitrary (Ω_m, ΩΛ, H₀) coming from a microphysics layer, with consistent unit handling.  
   - Implement robust numerical integrators and error control for a(z), H(z), and distance measures.

4. **Clarify the physical meaning of k_scale**  
   - Decide whether k_scale is purely phenomenological (fit to data) or whether it can be tied to a more fundamental quantity (e.g. lattice spacing, Planck-scale cutoff, or field-theory parameters).  
   - Explore whether the sign and magnitude of ΔE(θ★) in more realistic microstructures are compatible with the required ρΛ scale.

5. **Connect to 4D Δα(θ) and cancellation-system results**  
   - Investigate whether the θ★-dependence in the 4D lattice Δα(θ) and in the cancellation-system toys can be related to the cavity ΔE(θ★) pattern.  
   - The long-term goal is a coherent story: θ★ selected by flavor physics, echoed in Δα(θ★), and feeding a microstructure that sets the effective vacuum.

## 5. Status summary

As of 2025-12-17, the θ★-backed microcavity → effective vacuum → FRW pipeline in `origin-axiom` is:

- **Operational** as a toy model: the code runs end-to-end, produces sensible numbers, and illustrates how a single θ★ dial can back an effective ΛCDM-like expansion.  
- **Internally self-consistent**: the θ★ prior, microcavity ΔE(θ★), scaling k_scale, ensemble / random-walk statistics, and FRW observables all point to a non-fine-tuned, Λ-like corridor in θ★-space.  
- **Not yet a predictive theory of dark energy**: it does not derive Λ from microphysics, does not fit real data, and relies on simplified, phenomenological mappings.

This note is the reference snapshot for the Act II/III θ★ bridge in this repo. Any future changes to the microcavity model, the scaling, or the FRW layer should be recorded against this baseline.


