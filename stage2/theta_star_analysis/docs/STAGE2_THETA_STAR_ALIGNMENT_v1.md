# Stage 2 — θ★ alignment with FRW corridor families (Rung θ★–FRW–v1)

**Rung ID:** stage2_theta_star_frw_alignment_v1  
**Scope:** purely diagnostic, no claims promoted into Phase 4  
**Inputs:**  
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`  
- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`  
- θ★ = φ^φ ≈ 2.178458 (non-cancelling axiom candidate)

---

## 1. What this rung does

This rung asks a very narrow question:

> Given the FRW families we already defined on the θ grid in Stage 2,  
> does the special parameter θ★ ≈ φ^φ land in any “distinguished” place?

We **do not** introduce new FRW runs or new criteria here.  
We only:

1. Take the existing FRW families:
   - F1: FRW_VIABLE  
   - F2: LCDM_LIKE  
   - F3: TOY_CORRIDOR  
   - F4: CORRIDOR_AND_VIABLE  
   - F5: CORRIDOR_AND_LCDM  
   - (F6: DATA_OK is empty in this FRW run)
2. For each family, look at:
   - how many θ points it contains, and
   - which θ in that family is **closest to θ★** in absolute difference.

The actual nearest-neighbor search and segment bookkeeping is already done in:

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`

This rung is just the **interpretation + gating** for that table.

---

## 2. Numerical picture (from Rung 9)

From the Stage2 FRW corridor alignment run we have, schematically:

- Grid size: **2048 θ-points**
- Families (n_true, frac_of_grid):
  - F1_FRW_VIABLE: n ≈ 1016, frac ≈ 0.496
  - F2_LCDM_LIKE: n ≈ 63,   frac ≈ 0.031
  - F3_TOY_CORRIDOR: n ≈ 1186, frac ≈ 0.579
  - F4_CORRIDOR_AND_VIABLE: n ≈ 154, frac ≈ 0.075
  - F5_CORRIDOR_AND_LCDM: n ≈ 40, frac ≈ 0.020
  - F6_DATA_OK: n = 0 (empty in this FRW run)

The θ★-alignment results we logged:

- **F1_FRW_VIABLE**  
  - closest θ in the viable family: θ ≈ 2.178253  
  - |θ − θ★| ≈ 2.0×10⁻⁴  
  - So θ★ is **inside** the viable region and fairly close to one of the sampled grid points, but not sitting on an obviously special boundary.

- **F2_LCDM_LIKE**  
  - closest θ in LCDM-like family: θ ≈ 3.267379  
  - |θ − θ★| ≈ 1.09  
  - So the LCDM-like patch is **far away** from θ★ in this scan.

- **F3_TOY_CORRIDOR**  
  - closest θ: θ ≈ 3.304195  
  - |θ − θ★| ≈ 1.13  
  - The toy corridor as implemented is **not centered** on θ★; it sits in a different portion of the grid.

- **F4_CORRIDOR_AND_VIABLE**  
  - closest θ: again ≈ 3.304195  
  - |θ − θ★| ≈ 1.13  
  - The “corridor ∩ viable” family is also far from θ★ in this run.

- **F5_CORRIDOR_AND_LCDM**  
  - closest θ: again ≈ 3.304195  
  - |θ − θ★| ≈ 1.13  
  - So the “corridor ∩ LCDM-like” region is also away from θ★.

- **F6_DATA_OK**  
  - empty; there is no nontrivial θ set satisfying the current placeholder data mask,  
    so no statement is possible here.

---

## 3. Interpretation (what this means and what it **does not** mean)

### 3.1. Positive information

1. **θ★ lies in the FRW-viable band**  
   - The viable region (F1) is a broad, contiguous band containing ≈ 50% of the θ grid.  
   - θ★ sits *inside* this band, and is not near an obvious “edge catastrophe”.  
   - This is exactly what we’d hope for a “physically tolerable” θ candidate:  
     it is not immediately kicked out by our basic FRW viability checks.

2. **The FRW toy corridor is *not* tuned around θ★**  
   - In this specific run, the toy corridor and its intersections with viability/LCDM  
     live far from θ★ in θ-space.  
   - This is good from a discipline perspective: the corridor was not designed  
     by reverse-engineering θ★.

3. **Nothing in this scan “mysteriously snaps” to θ★**  
   - There is no special spike, pinch, or unique feature exactly at θ★  
     in the current FRW families we defined.

### 3.2. Negative information (what we **cannot** claim)

This rung **does not** provide evidence *for* θ★ as a physically distinguished value.

- The viable band is broad; having θ★ inside it is not surprising.
- The fact that the toy corridor sits elsewhere means:
  - we have **not** yet made the corridor definition “about” θ★;
  - but it also means the corridor as currently defined does **not** pick θ★.

We must **not** claim:

- “FRW dynamics single out θ★”, or
- “θ★ is preferred by the corridor or by LCDM-likeness”.

Current status is more modest:

> θ★ behaves like a conventional point in the **FRW-viable** half of the grid  
> under the specific F1 scan we ran here.

---

## 4. Role in the broader roadmap

This rung is a **discipline / hygiene rung**:

- It checks that our FRW constructions have **not secretly tuned themselves** to θ★.
- It records, explicitly, that:
  - θ★ is **allowed** by the F1 FRW viability band, but
  - θ★ is **not singled out** by the toy corridor or LCDM-like patches.

In the staged roadmap:

- **Stage 2**: this rung belongs to the FRW / Stage2 belt and remains **internal**.
- **Phase 3–4**: no text or figure is promoted into those phases from this rung.
- **Future Stage 3 / Phase 5**: if we later find richer structure (e.g.  
  data-informed corridors, or joint mech–FRW constraints that concentrate near θ★),  
  we can compare them directly to this rung as a **baseline**.

---

## 5. Gating decision for this rung

- **Promotion to Phase 4 / 5:** **NO** (for now).
  - Reason: This is a “nothing special yet” diagnostic; it would only clutter the main narrative.
- **Status in Stage 2:** **LOCKED as a negative-result snapshot.**
  - We keep the CSV and this document as part of the Stage2 archive.
  - Any future FRW runs that appear to pick θ★ must be compared against this baseline  
    to check for tuning artefacts or implementation changes.

