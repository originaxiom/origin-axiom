# Stage 2 – Obstruction θ★ alignment diagnostic (v1)

Status: Stage 2 diagnostic helper (obstruction overlay, non-claim).

## 1. Scope

This note records how the distinguished angle θ★ ≈ φ^φ (here treated as a
fixed target value θ★ ≈ 2.178458) sits inside the current FRW-facing stack:

- the static pre-data FRW kernel,
- the LCDM-like island and toy FRW corridor,
- the toy and external-style late-time corridors, and
- the age/expansion/structure-style external helpers.

The goal is not to *promote* θ★, but to check whether any of the existing
corridors “snap” to it in a nontrivial way on the current 2048-point θ-grid.

This is an obstruction-style diagnostic overlay on the locked Phase 3/4 stack.
It does not change any Phase contracts, Stage 2 belts, or promotion gates.

## 2. Inputs and output

Inputs (all on the current 2048-point θ-grid):

- Static FRW kernel:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`
    - columns: `theta`, `E_vac`, `omega_lambda`, `age_Gyr`,
      `has_matter_era`, `has_late_accel`, `smooth_H2`,
      `frw_viable`, `lcdm_like`, `in_toy_corridor`, `in_pre_data_kernel`.
- Toy and external late-time helpers:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv`
    - adds `lt_corridor_box_from_lcdm`.
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv`
    - adds `external_lt_corridor_v1`.
- External-style age helper:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv`
    - adds `external_age_corridor_v2`.
- External-style age/expansion/structure helpers:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv`
    - adds `age_broad_v1`, `age_tight_v1`,
      `expansion_broad_v1`, `expansion_tight_v1`,
      `struct_proxy_basic_v1`, `struct_proxy_tight_v1`.

Output of this rung:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_theta_star_alignment_v1.csv`
  - single-row summary of θ★ alignment on the current grid:
    - `grid_index`, `theta_star_target`, `theta_nearest`, `delta_theta`,
      `E_vac`, `omega_lambda`, `age_Gyr`,
      `in_pre_data_kernel`, `lcdm_like`, `in_toy_corridor`,
      `lt_corridor_box_from_lcdm`,
      `external_age_corridor_v2`, `external_lt_corridor_v1`,
      `age_broad_v1`, `age_tight_v1`,
      `expansion_broad_v1`, `expansion_tight_v1`,
      `struct_proxy_basic_v1`, `struct_proxy_tight_v1`.

## 3. θ★ location on the current static kernel

On the current snapshot:

- Target value:  
  - θ★\_target ≈ **2.178458**
- Nearest grid point on the 2048-point θ-grid:
  - θ\_nearest ≈ **2.1782527**
  - Δθ ≡ θ\_nearest − θ★\_target ≈ **−2.05 × 10⁻⁴**
- FRW scalars at θ\_nearest:
  - E\_vac ≈ **1.00 × 10⁻⁵** (in current code units),
  - ω\_Λ ≈ **1.53**,
  - age ≈ **11.70 Gyr**.

So θ★ is well-resolved on the current grid: the nearest θ bin is within
|Δθ| ≪ 1 of the target value, and the corresponding FRW snapshot sits inside
the static pre-data kernel.

## 4. Corridor membership at θ★

Using the one-row alignment table, the current corridor flags at θ\_nearest are:

- Static kernel and internal FRW corridors:
  - `in_pre_data_kernel = 1`
  - `lcdm_like = 0`
  - `in_toy_corridor = 0`
  - `lt_corridor_box_from_lcdm = 0`
- External-style helpers:
  - `external_age_corridor_v2 = 0`
  - `external_lt_corridor_v1 = 0`
- Age / expansion / structure proxies:
  - `age_broad_v1 = 1`
  - `age_tight_v1 = 0`
  - `expansion_broad_v1 = 0`
  - `expansion_tight_v1 = 0`
  - `struct_proxy_basic_v1 = 1`
  - `struct_proxy_tight_v1 = 0`

In words:

- θ★ lies *inside* the static pre-data kernel.
- θ★ passes the **broad** age and basic structure proxies.
- θ★ is *not* in:
  - the LCDM-like island,
  - the toy FRW corridor,
  - the LCDM-box late-time corridor,
  - the non-trivial age v2 corridor,
  - the external LT corridor, or
  - any of the tighter expansion/structure proxies.

Separate Stage 2 summaries (e.g. `stage2_obstruction_external_age_corridor_summary_v2.csv`)
show that there are 40 points in the sweet intersection

- `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`

but the θ★ grid point is not part of this 40-point set.

## 5. Interpretation in the obstruction program

On the current snapshot:

- θ★ is **compatible** with the static kernel and broad sanity proxies, in the
  sense that it lies in the pre-data kernel and passes broad age/structure cuts.
- The more selective FRW and external-style corridors (LCDM-like island, toy
  corridor, external age and LT bands, tight expansion/structure proxies)
  **do not** currently single out θ★:
  - they carve out a non-empty sweet subset, but θ★ is not inside it.

From an obstruction perspective this reads as a **clean negative result**:

- nothing in the current FRW-facing stack “locks onto” θ★ in an interesting
  way yet;
- θ★ behaves like a generic point inside the pre-data kernel under the present
  (toy) external corridors.

This is the expected outcome at this stage: the external-style corridors are
deliberately simple and are not yet tied to concrete host metrics or data.

## 6. Non-claims and future work

Non-claims.

- No claim is made that θ★ is preferred or disfavoured by the present FRW
  machinery; this is a diagnostic overlay only.
- No Phase 0–5 contracts, FRW masks, or Stage 2 promotion gates are modified
  by this rung.
- The existence of a 40-point sweet subset is not interpreted as a discovery;
  it is a structural feature of the current toy corridors.

Future work.

- As more realistic external-style corridors are introduced (tighter age bands,
  expansion constraints, simple structure-friendly proxies, and host metrics),
  this helper can be re-run to check whether θ★:
  - remains in the surviving kernel,
  - enters or leaves the sweet subset, or
  - continues to behave like a generic pre-data point.
- Any promotion of θ★-related statements into phase papers would require
  separate, tightly scoped rungs and explicit Phase 0–style gates.

