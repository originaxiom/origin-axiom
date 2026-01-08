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

## Rung F1.D0 – External FRW distance data contract (stub)

This rung introduces an explicit contract for an external FRW
distance–redshift dataset that Phase 4 (family F1) and Phase 5 may use
for comparison with the toy and viability constructions.

The dataset is represented by a single CSV file:

- **Path (relative to repo root)**:
  `phase4/data/external/frw_distance_binned.csv`
- **Semantics**:
  - One row per redshift bin.
  - No particular survey is assumed at this rung; any real survey or
    synthetic data must be re-binned into this common format before
    being placed here.
  - The file is allowed to be header-only in the baseline repository;
    Phase 4 and Phase 5 code must treat the absence of real rows as a
    valid, non-fatal state.

### Schema

At Rung F1.D0 the CSV is defined to have at least the following
columns:

- `z` (dimensionless):
  - The central redshift of the bin.
- `mu` (mag):
  - Distance modulus for the bin.
- `sigma_mu` (mag):
  - 1-sigma uncertainty on the distance modulus in that bin.

Additional columns are permitted but not required, for example:

- `sample_id`: a short string identifying the underlying survey or
  sample (e.g. `SNLS`, `Pantheon`, `mock_v1`).
- `systematics_flag`: an integer or string flag for systematics
  categories.

Any additional columns must be documented in this design file in a
future rung if they become relied upon by Phase 4 or Phase 5 code.

### Units and conventions

- `z` is a pure number (redshift).
- `mu` and `sigma_mu` are in magnitudes, defined in the usual way:
  \[
    \mu = 5 \log_{10}\!\left(\frac{D_L}{10\,\mathrm{pc}}\right) ,
  \]
  where \(D_L\) is the luminosity distance.
- The mapping from \(\theta\) to cosmological parameters (e.g.
  \(H_0\), \(\Omega_m\), \(\Omega_\Lambda\), and any additional
  parameters used in F1) is *not* specified here; it is handled in
  `FRW_SYNTHESIS.md` and the associated Phase 4 code.

### Error model at this rung

At Rung F1.D0 we assume:

- The uncertainties encoded in `sigma_mu` are treated as independent
  Gaussian errors.
- No off-diagonal covariance or shared systematics structure is used
  in computations that consume this file at this rung.

Future rungs may replace this with a more realistic covariance
treatment, possibly by introducing an explicit covariance matrix and a
separate design contract.

### Repository state requirements

- The baseline repository may ship with a header-only
  `frw_distance_binned.csv` (no data rows).
- Phase 4 and Phase 5 scripts that touch this file must:
  - succeed if the file exists and matches the schema, even if it
    contains zero data rows;
  - fail clearly (with a helpful error) only if:
    - the file is missing entirely, or
    - the required columns (`z`, `mu`, `sigma_mu`) are absent.

The Phase 5 interface currently treats this dataset as optional. Once
real data are added in a later rung, this section provides the
reference contract against which the code and diagnostics should be
checked.

## Rung F1.D1 – External FRW distance diagnostics script

This rung wires the external FRW distance–redshift dataset into a small
diagnostics script, without yet introducing any likelihood or
θ-dependent modeling. The goal is to:

- verify that the CSV file
  `phase4/data/external/frw_distance_binned.csv` exists and matches the
  schema defined in Rung F1.D0;
- compute simple, model-independent diagnostics (row counts, redshift
  range, basic checks on the uncertainties); and
- emit a compact JSON summary that can be consumed by later rungs
  (including Phase 5 interface layers) as part of a program-level
  viability dashboard.

### Script and output locations

At this rung, the diagnostics are implemented by:

- Python script (relative to repo root):
  `phase4/src/phase4/f1_frw_external_diagnostics_v1.py`
- JSON output:
  `phase4/outputs/tables/phase4_F1_frw_external_diagnostics.json`

The script is expected to:

1. Resolve the repository root and Phase 4 root from its own location.
2. Read `phase4/data/external/frw_distance_binned.csv`, ignoring
   comment lines starting with `#`.
3. Require at least the columns `z`, `mu`, and `sigma_mu`:
   - If the file is missing, it should report `file_exists: false` and
     set an informative status.
   - If the required columns are absent, it should report a schema
     mismatch (including the observed field names).
4. Parse rows into floats and:
   - count the number of valid data rows;
   - compute `z_min`, `z_max`, `mu_min`, `mu_max`,
     `sigma_mu_min`, `sigma_mu_max` when there is at least one row;
   - check whether the sequence of `z` values is non-decreasing.
5. Treat the zero-row case as a valid, non-fatal state:
   - this corresponds to the baseline repository shipping with a
     header-only file at Rung F1.D0.

### Contract at this rung

- The script must not:
  - construct or evaluate any cosmological model,
  - interpret the data in terms of θ, F1 mappings, or FRW dynamics, or
  - introduce any notion of likelihood or fit quality.
- The script may be extended in future rungs, but any additional fields
  or checks in the JSON output must be documented here.

The JSON output is intended to serve as a small, stable contract between
the external data file and higher-level viability dashboards. It records
what data are present (or absent) without making physical claims.
