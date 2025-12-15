# SCALING_NOTES for `origin-axiom`

Status: Act II / bridge between flavor, microstructure, and cosmology.  
Scope: **bookkeeping of units and scales** used in our toy models, so that later we can make honest contact with the observable universe (Ω_Λ, H₀, etc.).

This note is *not* a claim that we already match the observed cosmological constant.  
It is a **map of assumptions** and a place to plug in future refinements.

---

## 1. General philosophy

All our simulations in `origin-axiom` are currently written in **dimensionless lattice / code units**. We typically set
- c = 1,
- lattice spacing a = 1,
- and an effective “mass scale” m₀ ~ O(0.1–1).

Energies, times, and lengths appearing in the code are therefore in **arbitrary units**. To compare with the real universe, we must choose a dictionary

(code units) → (SI / physical units)

This requires us to introduce at least:
- a **length scale** L₀ (meters per lattice unit),
- an **energy scale** E₀ (eV or J per “code energy” unit),
- and, if needed, a characteristic **volume** V₀ per effective cell (e.g. V₀ ~ L₀³).

This note does **not** fix these once and for all; instead it:
1. Makes the existing choices explicit where we already made simplifications.
2. Outlines how to introduce a flexible “vacuum bridge” from lattice ΔE(θ★) to a physical vacuum energy density ρ_Λ.

---

## 2. Toy universes with non‑cancelling constraint

Relevant scripts:
- `src/run_toy_universe_demo.py`
- `src/run_toy_universe_compare_constraint.py`
- `src/run_toy_universe_compare_constraint_nonlinear.py`
- `src/run_toy_universe_constraint_scan.py`

### 2.1 Variables and units in code

These runs simulate a finite number of complex or real degrees of freedom (a “toy universe”) with:
- internal potential terms,
- a small “epsilon” scale controlling the **target amplitude** enforced by the Origin Axiom non‑cancelling rule,
- and time evolution with time step `dt` and total number of steps `n_steps`.

In the current implementation:
- The **field amplitudes** are dimensionless.
- The **energies** printed (e.g. E ≈ 2.45e-02) are in arbitrary energy units.
- Time t is in **code units** with dt chosen for numerical stability; we have not tied this directly to any physical timescale.

Interpretation: these runs are primarily **qualitative**:
- They show how the non‑cancelling rule stabilizes the global amplitude |A| around a finite nonzero value across different nonlinearities.
- They are not yet assigned a physical mass scale or length scale; all of that is deferred to a later matching layer.

### 2.2 What we will eventually need

To turn these into a quantitative statement about vacuum energy, we would need to:
1. Identify a physical **mass scale** m_eff for the effective DOFs (e.g. something tied to neutrinos or some scalar sector).
2. Identify a typical **volume** per DOF, or equivalently, how many DOFs live in a given physical volume.
3. Convert the dimensionless energy per DOF into a physical **energy density** ρ_vac (J/m³).

For now, we treat these toy universes as **proof‑of‑concept dynamics** for the non‑cancelling mechanism, without fixed physical units.

---

## 3. 1D twisted and defected vacuum chains

Relevant scripts:
- `src/run_1d_twisted_vacuum_scan.py`
- `src/run_1d_defected_vacuum_scan.py`

These scripts simulate a 1D chain (normal modes of a discretized scalar field) with:
- N sites (e.g. 256),
- a baseline mass parameter m₀,
- and either
  - a uniform twist θ★ across the chain, or
  - a localized defect / modification.

### 3.1 Code units

In these scripts:
- The **lattice spacing** is implicitly 1: sites are indexed i = 0, …, N-1 and we do not explicitly multiply by a.
- The **mass parameter** m₀ is dimensionless.
- The computed **ground state energy** E₀(θ★) is a dimensionless number in arbitrary units.

So a printout like
- E₀(θ★) ≈ 1.639690e+02

is **not yet** in Joules or eV; it is in whatever units are convenient for the discrete Hamiltonian.

### 3.2 Potential physical matching

To turn this into a physical vacuum energy density, we could:
1. Introduce a physical lattice spacing a_phys = L₀ (meters per site).
2. Interpret the chain as a 1D cross‑section of a 3D system with some transverse area A₀.
3. Then identify the *energy difference* between two configurations,

ΔE₀(θ★) = E₀^cavity(θ★) − E₀^uniform(θ★),

as a total vacuum energy shift for a cell of volume V₀ ~ L₀ × A₀.

The physical vacuum energy density ρ_Λ would then schematically be

ρ_Λ ~ (ΔE₀ × E₀) / V₀,

where E₀ here is the **energy scale per unit code energy** (e.g. 1 code unit = 1 eV, or 1 code unit = some fraction of Planck energy).

In practice, we will implement this logic via a small “vacuum bridge” module.

---

## 4. 1D microcavity with θ★ prior

Relevant scripts:
- `src/run_1d_theta_star_microcavity_scan.py`
- `src/scan_1d_theta_star_microcavity_full_band.py`

Outputs:
- `data/processed/theta_star_prior_1d_microcavity_samples.npz` (few θ★ samples within the Act II band),
- `data/processed/theta_star_microcavity_scan_full_2pi.npz` (dense ΔE(θ★) over [0, 2π)).

Model parameters (as of current implementation):
- N = 256 (number of sites),
- c = 1.0,
- m₀ = 0.1,
- cavity_frac = 0.2,
- alpha_mass = 0.5,
- theta0 = 0.0.

### 4.1 Code‑level interpretation

The microcavity model modifies the **mass profile** in a subregion of the chain, producing a localized “cavity” where the vacuum energy is different from the uniform chain.

We compute, for each θ★,
- E₀_uniform(θ★): vacuum energy without cavity modulation,
- E₀_cavity(θ★): vacuum energy with cavity modulation,
- ΔE(θ★) = E₀_cavity(θ★) − E₀_uniform(θ★).

All of these are **dimensionless energies** in code units.

The important structure we already see is:

- ΔE(θ★) is **negative** over a range of θ★, i.e. the cavity lowers the energy.
- The **minimum** of ΔE(θ★) over [0, 2π) occurs very close to θ★ ≈ π.
- Our Act II θ★ band [θ_lo, θ_hi] ≈ [2.18, 5.54] rad includes that minimum, and the fiducial θ★ ≈ 3.63 rad lies in a sector where ΔE is negative but slightly above the absolute minimum.

This pattern is what we will eventually try to connect to an **effective vacuum energy density** in FRW cosmology.

### 4.2 From ΔE(θ★) to a physical ρ_Λ (to be implemented)

For the microcavity, a minimal physical dictionary will look like:

- **Length scale** L₀: physical size of one “cell” or one cavity region (meters).
- **Energy scale** E₀: energy per code unit (eV or J).
- We then interpret a single microcavity configuration as an effective cell of volume V₀ ~ L₀³.

Given a dimensionless ΔE(θ★), we can then define

E_phys(θ★) = |ΔE(θ★)| × E₀,

ρ_Λ(θ★) ≈ E_phys(θ★) / V₀.

If we work in SI units (Joules and meters), we can convert this to a **mass density** via

ρ_Λ, mass = ρ_Λ / c²

and compare to the cosmological critical density

ρ_c = 3 H₀² / (8πG).

Then the implied **Ω_Λ** from our microcavity is

Ω_Λ(θ★) = ρ_Λ, mass(θ★) / ρ_c.

The key point: different choices of L₀ and E₀ correspond to different hypotheses about the underlying microphysics. Our next step is to expose these choices explicitly in code and scan over them.

---

## 5. FRW toy universe and cosmological units

Relevant scripts:
- `src/run_frw_vacuum_demo.py`
- `scripts/plot_frw_vacuum_demo.py`

In `run_frw_vacuum_demo.py` we solve the FRW equation

(ȧ / a)² = H₀² (Ω_m a⁻³ + Ω_Λ)

in **dimensionless units** with
- H₀ = 1 (code units),
- a(t) dimensionless,
- t measured in units of H₀⁻¹.

So:
- t = 1 in code corresponds to one “Hubble time” for the chosen H₀.
- We explore qualitative differences between Ω_Λ = 0, 0.3, and 0.7, keeping the same H₀ and a_init.

To relate this to the real universe, we would choose:
- a physical H₀_phys (e.g. 70 km/s/Mpc),
- compute the physical critical density ρ_c from that,
- and then match the **vacuum energy density** derived from ΔE(θ★) to a physical Ω_Λ = ρ_Λ / ρ_c.

The upcoming `run_frw_from_microcavity.py` script will be the first step in this direction.

---

## 6. Plan for the “vacuum bridge”

To keep things transparent and modular, we will introduce a small module (name provisional, e.g. `src/vacuum_bridge.py`) that will:

1. Provide a simple **data structure** for scale choices, e.g.

   ```python
   @dataclass
   class VacuumScaling:
       length_unit_m: float   # L₀
       energy_unit_eV: float  # E₀
   ```

   and assume a fiducial **cell volume** V₀ = L₀³ unless specified otherwise.

2. Implement the conversion

   ```python
   def lattice_deltaE_to_rho_lambda(deltaE_dimless: float,
                                    scaling: VacuumScaling) -> float:
       """Map a dimensionless ΔE from the microcavity model to a physical
       vacuum energy density ρ_Λ (J/m³), given a choice of L₀ and E₀."""
   ```

3. Provide utilities to convert ρ_Λ to Ω_Λ for a chosen physical H₀:

   ```python
   def rho_to_omega_lambda(rho_lambda_J_m3: float, H0_km_s_Mpc: float = 70.0) -> float:
       """Convert ρ_Λ (J/m³) to Ω_Λ using ρ_c = 3 H₀² / (8πG)."""
   ```

4. A **demo script** `src/run_frw_from_microcavity.py` will then:
   - Load the dense ΔE(θ★) scan,
   - Read the Act II θ★ config (`config/theta_star_config.json`),
   - Pick ΔE at the fiducial θ★ and at representative points in the band,
   - Apply several example scaling choices (e.g. microscopic, mesoscopic),
   - Print the implied Ω_Λ for each, and compare to Ω_Λ,obs ≈ 0.7.

This will **not** yet be a final physical model, but it will:
- expose all assumptions,
- let us see **how many orders of magnitude** we are away from the real Λ for different plausible micro scales,
- and give us a concrete place to refine the model.

---

## 7. What this note is and is not

**Is:**
- A clear statement of how units are currently used in the code.
- A roadmap for turning lattice ΔE(θ★) into a physically comparable ρ_Λ.
- A reminder that all current numbers are in **code units** until we pass them through an explicit scaling layer.

**Is not:**
- A claim that we already match the observed cosmological constant.
- A derivation of the “true” microphysical scale of the universe.

As we refine the microstructure models and introduce more realistic scales, this note should be updated to keep the bridge from **origin-axiom-theta-star → origin-axiom → cosmology** completely transparent.
