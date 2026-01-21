# Stage 2 – Frustrated floor projection (toy v1)

**Status:** Stage 2 obstruction-program helper, *diagnostic only*, non-binding.  
**File:** `stage2/docs/STAGE2_OBSTRUCTION_FRUSTRATED_FLOOR_PROJECTION_V1.md`  
**Implements:** `stage2/obstruction_tests/src/apply_frustrated_floor_projection_v1.py`

---

## 1. Purpose and context

This memo documents a **toy, internal-only helper** that projects the current obstruction stack onto a *frustrated-floor* subset of the pre-data FRW kernel.

The goal is to have **one concrete object** that reflects the intuition:

> “Reality is what remains when cancellation is *tried* but cannot fully succeed.”

In this Stage 2 implementation, that intuition is realized in the *mildest possible way*:

- we **do not** claim a fundamental non-cancellation law,
- we **do not** tie anything to real data or to a preferred \(\theta\),
- we **do not** promote any new phase-level claims.

Instead, we:

1. Start from the **pre-data FRW kernel** in Phase 4 (vacuum → FRW diagnostic),
2. Overlay a set of **external-style corridors** (age, expansion, structure proxies),
3. Attach the **Phase 3 mechanism amplitudes** (baseline and binding),
4. Define a **“frustrated-floor core”** as a small, constrained intersection where:
   - FRW background is viable at toy level,
   - age / expansion / structure proxies all pass tight cuts,
   - and the binding amplitude satisfies a simple *floor* condition.

This core is then used as a **diagnostic sandbox** for the obstruction program, not as evidence for any physical floor in Nature.

---

## 2. Inputs and outputs

### 2.1 Upstream tables

The helper assumes the following Stage 2 tables already exist:

1. **FRW kernel with mechanism amplitudes**

   - Path:  
     `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv`
   - Built by:  
     `stage2/obstruction_tests/src/attach_mech_amplitudes_to_kernel_v1.py`
   - Key columns (subset):
     - `theta`
     - FRW / mask columns:  
       `E_vac`, `omega_lambda`, `age_Gyr`, `has_matter_era`, `has_late_accel`,  
       `smooth_H2`, `frw_viable`, `lcdm_like`, `in_toy_corridor`,  
       `shape_and_viable`, `shape_and_lcdm`, `data_ok`, `in_pre_data_kernel`
     - Mechanism amplitudes (Phase 3):
       - `mech_baseline_A0`
       - `mech_baseline_A_floor`
       - `mech_baseline_bound`
       - `mech_binding_A0`
       - `mech_binding_A`
       - `mech_binding_bound`

2. **External-style age / expansion / structure corridors**

   - Path:  
     `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv`
   - Built by:  
     `stage2/obstruction_tests/src/apply_external_age_expansion_corridors_v1.py`
   - Key columns (subset):
     - `theta`
     - Boolean flags:
       - `age_broad_v1`, `age_tight_v1`
       - `expansion_broad_v1`, `expansion_tight_v1`
       - `struct_proxy_basic_v1`, `struct_proxy_tight_v1`

3. **Non-cancellation floor summary (for context)**

   - Path:  
     `stage2/obstruction_tests/outputs/tables/stage2_obstruction_non_cancel_floor_vs_corridors_v1.csv`
   - Built by:  
     `stage2/obstruction_tests/src/analyze_non_cancellation_floor_vs_corridors_v1.py`
   - Used to define a **toy floor threshold** for `mech_binding_A0`:
     - In the current snapshot, we adopt  
       \[
       A_{\text{floor}}^{(\text{toy})} = 0.045
       \]
       as a simple, quasi-minimal floor that still leaves a non-trivial subset of the kernel.

### 2.2 Output table

The frustrated-floor projection helper writes:

- Path:  
  `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_frustrated_floor_v1.csv`

This table is essentially:

- the **kernel+mech** table,
- joined with **tight external corridor flags**, and
- augmented by a single Boolean flag:

- `in_frustrated_floor_core_v1` — whether a given grid point is in the toy frustrated-floor core.

The header (at the time of this memo) is of the form:

- FRW + mask columns (as in the kernel table),
- Phase 3 amplitudes,
- corridor flags:
  - `age_tight_v1`
  - `expansion_tight_v1`
  - `struct_proxy_tight_v1`
- and:
  - `in_frustrated_floor_core_v1`

The helper also reports on stdout:

- the total kernel size, and
- the size of the frustrated-floor core.

In the current snapshot:  
**core size = 49** out of **1016** kernel points.

---

## 3. Definition of the toy frustrated floor

### 3.1 Ingredients

We define the frustrated-floor core using the following Boolean ingredients on each grid point:

1. **Kernel membership**

   - `in_pre_data_kernel == True`  
     → passes all Phase 4 *pre-data* FRW viability filters.

2. **Tight external-style corridors**

   - `age_tight_v1 == True`  
     → age in a toy external-style band (v1) compatible with a late-time universe of order \(\sim 14\) Gyr.
   - `expansion_tight_v1 == True`  
     → satisfies a tight expansion proxy corridor in \((E_\text{vac}, \Omega_\Lambda)\) space.
   - `struct_proxy_tight_v1 == True`  
     → passes a simple structure-friendliness proxy (v1), built out of the background sector only.

3. **Toy non-cancellation floor**

   We use the **Phase 3 binding amplitude** `mech_binding_A0` as a *candidate* non-cancellation proxy and impose:

   \[
   \texttt{mech\_binding\_A0} \geq A_{\text{floor}}^{(\text{toy})}
   \]

   with

   \[
   A_{\text{floor}}^{(\text{toy})} = 0.045.
   \]

   This threshold is:

   - **internal and ad hoc**,
   - **chosen within** the range explored in `stage2_obstruction_non_cancel_floor_vs_corridors_v1.csv`,
   - **not tuned** to the 40-point “sweet” subset, and
   - **not physically motivated** beyond “large enough to count as non-trivial” but still leaving a useful subset.

### 3.2 Core definition

On each row (grid point), we define:

```text
in_frustrated_floor_core_v1 =
    in_pre_data_kernel
    AND age_tight_v1
    AND expansion_tight_v1
    AND struct_proxy_tight_v1
    AND (mech_binding_A0 >= A_floor^(toy)).
```

In the current snapshot, this yields:

- pre-data kernel size: 1016,
- frustrated-floor core size: 49.

This **49-point core** is the working “toy frustrated-floor set” in Stage 2.

---

## 4. Implementation sketch

The helper:

1. **Loads** the kernel+mech table:  

   `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv`

2. **Joins** tight corridor flags (if needed) from:  

   `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv`

   so that the resulting DataFrame has columns:
   - `in_pre_data_kernel`,
   - `age_tight_v1`,
   - `expansion_tight_v1`,
   - `struct_proxy_tight_v1`,
   - Phase 3 amplitudes (including `mech_binding_A0`).

3. **Checks** that all required columns are present; if any are missing, it prints a clear error and exits without writing an output file.

4. **Applies** the logical condition above to compute `in_frustrated_floor_core_v1`.

5. **Writes** the augmented table to:  

   `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_frustrated_floor_v1.csv`

6. **Reports** on stdout:
   - repo root,
   - output path,
   - kernel size,
   - frustrated-floor core size.

The logic is fully deterministic and purely algebraic on the existing diagnostic columns; it does **not** re-solve any FRW or mechanism equations.

---

## 5. Role in the obstruction program

Within the obstruction program, this helper is used as a **diagnostic lens**, not as a source of new claims.

Concretely, it enables tests of the form:

- Start from the **pre-data FRW kernel** (Phase 4 diagnostic).
- Apply a collection of **external-style corridors**:
  - late-time age bands,
  - late-time expansion boxes in \((E_\text{vac}, \Omega_\Lambda)\),
  - simple structure proxies built only from background quantities.
- Impose a **toy non-cancellation floor** on the Phase 3 binding amplitude.
- Ask:

  1. Does a **non-empty core** remain?
  2. How large is this core compared to:
     - the full grid,
     - the pre-data kernel?
  3. How does this core relate to:
     - the 40-point FRW “sweet” subset (kernel ∩ LCDM-like ∩ toy corridor ∩ external-age-v2),
     - the behaviour of the mechanism amplitudes more generally?

By design:

- This helper **does not**:
  - modify any Phase 0–5 contracts,
  - alter Phase 4 FRW masks,
  - change Stage 2 promotion gates,
  - declare any specific \(\theta\) (or \(\theta_\star\)) as preferred.
- It **does**:
  - make the “frustrated-floor” intuition *explicit and inspectable* on the existing grid,
  - provide a small, tightly filtered subset that can be compared against other diagnostics.

---

## 6. Non-claims

This helper comes with strong **non-claims**:

1. **No physical floor is claimed.**  
   The condition `mech_binding_A0 ≥ 0.045` is a toy internal choice, not a derived law of Nature.

2. **No preferred \(\theta\) or \(\theta_\star\) is selected.**  
   The existence of a 49-point core does not single out any particular angle; it only shows that the current stack supports a small, tightly constrained subset.

3. **No connection to real data is made.**  
   External-style corridors (age, expansion, structure) are placeholders; their thresholds are not fit to observational data and should not be used for inference.

4. **No change to the cosmological constant problem.**  
   This helper does not compute, explain, or alter the effective cosmological constant; it operates entirely inside the existing Phase 4 toy FRW sector.

5. **No mechanism measure is promoted.**  
   Using `mech_binding_A0` as a non-cancellation proxy in this context does not elevate it to a fundamental measure or to a basis for claims.

Any future use of frustrated-floor language in phase papers or external-facing documents will require:

- separate, tightly scoped rungs,
- Phase 0–style gates,
- and explicit, conservative claims clearly distinguished from this Stage 2 diagnostic helper.

---

## 7. Next steps and possible refinements

The current helper is **O2.x-level infrastructure** for the obstruction program. Potential follow-up rungs include:

1. **Threshold robustness checks**
   - Vary the floor threshold around 0.045 and study how the core size and location change.
   - Quantify whether the core is robust or highly sensitive to this choice.

2. **Corridor combination studies**
   - Compare the frustrated-floor core to:
     - the 40-point FRW “sweet” subset,
     - subsets defined by different combinations of corridors (age-only, expansion-only, structure-only).
   - Use the summary tables from:
     - `stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv`
     - `stage2_obstruction_non_cancel_floor_vs_corridors_v1.csv`.

3. **Cross-check with \(\theta_\star\) alignment**
   - Use `stage2_obstruction_theta_star_in_stack_v1.csv` to see how the nearest-grid \(\theta_\star\) point sits relative to:
     - the pre-data kernel,
     - external corridors,
     - the frustrated-floor core.

4. **Design of more realistic external corridors**
   - Replace the current toy age / expansion / structure proxies with sharper, more physically motivated corridors (still clearly marked as external-style helpers).
   - Only after that, reconsider whether any frustrated-floor language should be used outside Stage 2 diagnostics.

Until such refinements are in place, this helper should be interpreted strictly as:

> a **toy, internal, diagnostic projection** of the existing obstruction stack onto a small, non-empty subset where FRW viability, external-style corridors, and a simple non-cancellation floor all hold simultaneously.
