# Phase 4: FRW-facing data probe design

## Role in the Phase 3 → Phase 4 pipeline

This note documents a data-facing FRW diagnostic that sits on top of
the Phase 4 FRW viability layer. Its purpose is to show how the F1
mapping and FRW viability infrastructure can be extended to make
contact with actual cosmological distance data, without turning Phase 4
into a full-blown parameter-fitting exercise.

The goals are:

- to demonstrate that the FRW-viable subset of the theta-grid can be
  tested against simple, public distance–redshift data;
- to keep the interface to external data explicit and auditable; and
- to preserve the non-binding, diagnostic-only philosophy of Phase 4.

## Inputs and outputs

### FRW viability mask (internal)

The data probe consumes the existing FRW viability mask:

- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`

with columns including:

- `theta` (float, radians),
- `E_vac` (float, Phase 3 scalar),
- `omega_lambda` (float),
- `age_Gyr` (float),
- Boolean flags (`has_matter_era`, `has_late_accel`, `smooth_H2`), and
- `frw_viable` (Boolean indicator).

Only rows with `frw_viable == 1` are candidates for data-level checks.

### External distance–redshift data (not bundled)

The data probe expects, but does not require, an external CSV file:

- `phase4/data/external/frw_distance_binned.csv`

This file is not version-controlled in the repository by default, to
avoid bundling third-party datasets. Instead, users can place a binned
distance–redshift dataset here, for example:

- supernova distance moduli binned in redshift, or
- BAO-derived luminosity or angular-diameter distances.

The expected minimal schema is:

- `z`        (float, redshift),
- `mu`       (float, distance modulus, mag),
- `sigma_mu` (float, uncertainty on `mu`, mag).

Rows with non-positive `sigma_mu` are ignored.

### FRW model assumptions

The data probe reuses the same background assumptions as the FRW
viability layer:

- flat FRW with:
  - `Omega_m = 0.3`,
  - `Omega_r = 0.0`,
  - `Omega_lambda(theta)` taken from the viability mask;
- `H0 = 70 km s^-1 Mpc^-1` (fixed).

For each theta in the FRW-viable subset, the code computes:

- the dimensionless expansion factor
  `E(z; theta) = H(z; theta) / H0` with
  `E^2(z; theta) = Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_lambda(theta)`,
- the comoving distance
  `chi(z; theta) = (c / H0) ∫_0^z dz' / E(z'; theta)`, and
- the luminosity distance
  `d_L(z; theta) = (1 + z) * chi(z; theta)`.

The distance modulus is then

- `mu_model(z; theta) = 5 log10( d_L(z; theta) / Mpc ) + 25`.

The integrals are evaluated numerically with a simple trapezoidal rule
on an internal redshift grid for each data point.

### Diagnostics and mask

The data probe writes:

- a diagnostics JSON:

  - `phase4/outputs/tables/phase4_F1_frw_data_probe.json`

  summarising:

  - the number of FRW-viable grid points,
  - the number of data points,
  - the chi^2-per-dof threshold used, and
  - the fraction of FRW-viable theta values that pass the data-level
    criterion;

- a per-theta mask CSV:

  - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`

  extending the FRW viability mask with:

  - `chi2_data`    (float, chi^2 against the external dataset),
  - `chi2_per_dof` (float, chi^2 / N_data), and
  - `data_ok`      (0/1 Boolean indicator).

If no external data file is present or it is empty, the code:

- records `data_available = false` in the diagnostics JSON; and
- writes a mask CSV with `chi2_data` and `chi2_per_dof` set to NaN and
  `data_ok = 0` for all rows.

This keeps the pipeline reproducible even in the absence of external
data.

## Non-binding nature and claim discipline

The FRW data probe is explicitly non-binding:

- It does not fit parameters.
- It does not introduce a new theta-filter.
- It does not claim to outperform a standard flat ΛCDM model.

Instead, it is used as a structured, optional diagnostic that:

- demonstrates that the Phase 3 scalar and F1 mapping can be brought
  into contact with real distance data under clear assumptions; and
- logs both positive and negative outcomes (for example, empty or
  small `data_ok` sets) in a way that is ready for later, more serious
  data work.
