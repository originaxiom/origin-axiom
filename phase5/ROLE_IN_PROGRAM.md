# Phase 5 – Role in the Program

Phase 5 sits at the boundary between:

- The **internal technical pipeline** (Phases 0–4), and
- The **external-facing synthesis and data confrontation** work.

This document explains that role.

---

## 1. Position relative to other phases

- **Phase 0**: Conceptual foundation, ledger, and high-level architecture.
- **Phase 1**: Toy universes and narrative scaffolding.
- **Phase 2**: Baseline θ-ensemble and binding toy mechanisms.
- **Phase 3**: Concrete vacuum mechanism A, baseline scans, and diagnostics.
- **Phase 4**: FRW-style cosmological mappings built on the mechanism.

**Phase 5**:

- Does **not** add a new “physics engine”.
- Instead, it:
  - Bundles and inspects the Phase 3/4 artifacts,
  - Prepares them for external confrontation,
  - Guards against internal inconsistency and over-claiming.

---

## 2. Interface and gatekeeper

Phase 5 is both:

1. A **programmatic interface**:
   - `phase5/src/phase5/phase5_interface_v1.py` gathers all required
     upstream tables and diagnostics into a structured view.
   - `phase5/outputs/tables/phase5_interface_v1_summary.json` is a
     machine-readable snapshot of what Phase 3 and Phase 4 provide.

2. A **gatekeeper** for later narrative:
   - Future Phase 5 rungs must draw from this interface, not from
     arbitrary ad-hoc filesystem reads.
   - Any Phase 5 paper, figure, or claim must trace back to:
     - A specific interface version (v1, v2, ...),
     - A specific bundle of upstream artifacts.

---

## 3. Relationship to external data

Phase 5 is the **first phase that is allowed to look outward** to data,
but even that is carefully constrained:

- External files (e.g. `phase4/data/external/frw_distance_binned.csv`)
  are treated as **optional overlays**.
- Phase 5 must:
  - Handle their absence gracefully,
  - Document clearly when such data is used,
  - Avoid silently mixing “toy” and “real” data.

The pipeline remains valid and reproducible even if external datasets
are missing; their presence enables additional *layers* of analysis, not
a different core theory.

---

## 4. Narrative responsibility

Phase 5 will eventually:

- Translate the multi-phase pipeline into:
  - A coherent cosmology-facing narrative,
  - A set of falsifiable questions and proposed tests.

Its responsibilities include:

- Making clear which claims belong to which phase,
- Avoiding the temptation to smuggle Phase 0–4 *aspirations* into
  Phase 5 as if they were already validated facts,
- Being explicit about uncertainties, approximations, and failure modes.

---

## 5. Non-destructive design principle

A core design rule for Phase 5 is:

> “Phase 5 may add layers of interpretation and confrontation, but it
> must not silently rewrite or break upstream phases.”

Practically, this means:

- Upstream artifacts in `phase3/` and `phase4/` are read-only for Phase 5.
- Any new transforms or re-packagings happen in `phase5/` or clearly
  marked sandbox locations.
- Changes to upstream phases must go through their own rungs and gates,
  not be hidden inside Phase 5 scripts.

