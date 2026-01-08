# Phase 5 Roadmap: From FRW Toy Corridors to Data-Contact

_Last updated: 2026-01-08 (local), branch: phase3-polish-local_

## 1. Position in the Phase 0–4 Ladder

- **Phase 0 – Conceptual foundation**  
  - Defines the origin-axiom motivation and the “non-cancelling twist” idea at a narrative level.  
  - No binding numerical claims; sets language, constraints, and story.

- **Phase 1 – Formal axiom + vacuum bookkeeping**  
  - Encodes the non-cancellation principle into a precise axiom structure.  
  - Introduces the bookkeeping language for amplitudes, residuals, and admissible θ-structure.  
  - Still pre-physical: toy objects, no FRW yet.

- **Phase 2 – Static mechanism and lattice-level toy**  
  - Implements a concrete mechanism on a discrete structure (toy lattice / ensemble).  
  - Explores cancellation patterns and residual structure at a static level.  
  - Output: a Phase 2 paper + artifact PDF, but no dynamical cosmology.

- **Phase 3 – Dynamical mechanism and amplitude measure**  
  - Promotes the mechanism to a dynamical amplitude story with θ ↦ A₀(θ) behavior.  
  - Defines “binding” rungs and what it means for the mechanism to be numerically under control.  
  - Adds:
    - An ensemble-level **A₀ distribution probe** (`phase3_measure_v1.py`)  
    - A derived **instability penalty** (`instability_penalty_v1.py`) as a toy diagnostic  
  - Still no physical Λ, no FRW, no data; everything is clearly labeled as toy.

- **Phase 4 – FRW F₁ surface and toy viability corridors**  
  - Maps θ to an effective vacuum energy and FRW expansion history via a toy F₁ surface.  
  - Builds:
    - FRW viability masks (matter era, late acceleration, age bounds, etc.)  
    - Toy “corridors” of acceptable θ in FRW space  
    - An **ΛCDM-like probe**: checks whether any θ sits in a loose ΛCDM-shaped patch  
  - All of this is **exploratory** and clearly marked as “toy FRW probes”, not a physical fit.

**Phase 5 must not retroactively change these roles.**  
Instead, it should sit *on top* of the existing stack and ask:

> _“Given the toy mechanism and FRW corridors, what is the right, modest way to contact real data or more realistic theory without over-claiming?”_

---

## 2. Phase 5: Core Purpose and Non-Negotiable Boundaries

### 2.1. Purpose

Phase 5 exists to:

1. **Define a disciplined interface between the origin-axiom toy tower (Phases 0–4) and the external world**:
   - Observational cosmology (H₀, Ωₘ, Ω_Λ, distance–redshift curves, etc.)
   - Possibly other sectors (particle-physics-inspired priors), but only if grounded.

2. **Test whether the existing tower can survive “first contact” with simple, robust data summaries** without:
   - Introducing hidden fine-tuning,
   - Retrofitting hand-chosen parameters,
   - Or smuggling in the result we want.

3. **Clarify failure modes**:
   - Phase 5 should be equally successful if it *falsifies* naive identifications (e.g. simplistic Ω_Λ formulae) and records that cleanly.

### 2.2. Hard Boundaries (What Phase 5 Must Not Do)

- **No “miracle fits.”**  
  Phase 5 must not:
  - Introduce adjustable knobs just to match Ω_Λ, H₀, or any dataset.  
  - Declare success based on single-number numerology (e.g. generation counts, exponents) unless derived within a reproducible, clearly logged model.

- **No unverified claims imported from the sandbox.**  
  - Speculative structures (e.g. Ω_Λ ≈ (n-1)/n or ε-exponent relations) may be **mentioned** as hypotheses, but:
    - They must be clearly marked as *external ideas* not yet part of the runged tower.
    - They must not appear in claims tables until they have a full derivation + code + diagnostics.

- **No data massaging.**  
  - If external data are used (e.g. FRW distance moduli, chronometers, BAO-ish toy points):
    - The dataset must be logged in a reproducible way (source, preprocessing, format).  
    - Any cuts, binning, or transformations must be explicit and scripted.

---

## 3. Inputs: What Phase 5 Is Allowed to Consume

Phase 5 may use, as **read-only inputs**:

1. **Phase 3 diagnostics outputs**, e.g.:
   - `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`
   - `phase3/outputs/tables/phase3_measure_v1_stats.json`
   - `phase3/outputs/tables/phase3_measure_v1_hist.csv`
   - `phase3/outputs/tables/phase3_instability_penalty_v1.json`
   These encode how the mechanism distributes A₀ and how “dangerous” low-amplitude regions are in the toy ensemble.

2. **Phase 4 FRW & F₁ outputs**, e.g.:
   - Sanity + shape diagnostics over the F₁ surface  
   - FRW toy diagnostic tables (age, matter-era flags, acceleration flags, Ω_Λ-like quantities)  
   - Viability masks and ΛCDM-like probe masks  
   - Any shape-probe plots already produced for the paper artifacts  

3. **Simple external summaries**, if and only if:
   - They are stable, widely agreed-upon constants (e.g. Ω_Λ ≈ 0.685, Ωₘ ≈ 0.315 from Planck/ΛCDM-like fits).
   - They are treated as **targets for comparison**, not as inputs to tune against.

---

## 4. Outputs: What Phase 5 Should Produce

Phase 5 should aim to produce:

1. **A small set of clearly defined scalar diagnostics**, for example:
   - A measure of how often the toy tower lands near Ω_Λ-like values under the Phase 4 FRW mapping, given the Phase 3 A₀ ensemble.  
   - Simple mismatch metrics between toy FRW histories and ΛCDM-like benchmark curves (e.g. max deviation in E(z), age, or Ω_Λ fraction).

2. **A disciplined claim table**, explicitly labelled as **Phase 5**:
   - Claims about what we *do* and *do not* see when trying to align toy FRW with real-world summary numbers.  
   - Clear separation between:
     - “Internal consistency” claims (tower-only),
     - “External contact” claims (tower vs. data).

3. **A reproducible script pipeline**, in the style of Phases 3–4:
   - A `phase5/src/phase5/` family of scripts that:
     - Read Phase 3 and Phase 4 tables,
     - Optionally ingest one or two simple external CSVs,
     - Emit Phase 5 diagnostics JSON/CSVs and, if needed, a small number of figures.

4. **A Phase 5 paper** (later):
   - Initially, Phase 5 can exist as code + diagnostics + notes.  
   - At a later rung, we can mirror Phase 3–4 and build:
     - `phase5/paper/main.tex`
     - `phase5/artifacts/origin-axiom-phase5.pdf`
   - That should only happen once the scope is crisp and the diagnostics feel stable.

---

## 5. Initial Phase 5 Rungs (Concrete To-Dos)

Here is a proposed sequence of early Phase 5 rungs:

1. **Rung P5.1 – Inventory and interface definition**
   - Enumerate exactly which Phase 3 & 4 outputs are “Phase 5 inputs.”
   - Fix their paths and columns in a small YAML or JSON interface spec.
   - No new physics, just a clean contract.

2. **Rung P5.2 – Toy comparison metrics**
   - Implement a small Python module (e.g. `phase5_metrics.py`) that:
     - Takes a toy FRW history from Phase 4,
     - Compares it to a canonical ΛCDM summary (Ω_Λ, Ωₘ, age),
     - Produces scalar mismatch numbers.
   - Still purely internal; no external data files yet.

3. **Rung P5.3 – External data stub**
   - Decide on one simple, robust observational proxy to include:
     - e.g. binned E(z) or distance–redshift points from a standard compilation.
   - Do *not* ship real data yet; instead:
     - Add a reproducibility note about where such a CSV would live,
     - Add placeholder hooks in the code.

4. **Rung P5.4 – Claims table + limitations section**
   - Draft Phase 5 claims in the same style as Phases 2–4:
     - What Phase 5 actually shows,
     - What is explicitly *not* claimed,
     - How it could be falsified or extended.

5. **Rung P5.5 – Paper and gate (later)**
   - Once the above is stable, scaffold `phase5/paper` and a `phase5_gate.sh`,
   - Add Phase 5 to the unified `scripts/build_paper.sh` / gate pattern,
   - Promote the Phase 5 diagnostics into a proper artifact PDF.

---

## 6. Relationship to Sandbox Ideas

Explorations carried out in separate “sandbox” scripts or with other models (e.g. alternative Ω_Λ formulae, generation-count numerology, exponent tricks) are:

- **Valuable for intuition**, but
- **Not part of the Phase 0–4 tower** unless:
  - They appear as explicit definitions,
  - Have code and diagnostics under `phase3/`–`phase5/`,
  - And are referenced in the paper claims tables.

Phase 5 may include a short “sandbox appendix” that:

- Summarises which sandbox ideas were tested,
- Records why they are **not yet promoted** to formal claims, and
- Outlines what would be required for promotion (derivation, reproducible scripts, diagnostics).

