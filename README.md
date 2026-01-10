# Origin Axiom – Phased Vacuum Mechanics Program

> “Twist Euler’s perfect cancellation just enough that reality cannot vanish,  
> then follow the residue wherever it leads.”

This repository hosts the **phased Origin-Axiom program**: a long-horizon, self-audited research workflow that tries to make one very narrow, very provocative claim:

> There may exist a **single, axiom-level deformation of perfect cancellation in the accounting of existence**—currently instantiated as a vacuum-mechanics test-bed—that:
> - is simple enough to write on a T-shirt,
> - is rich enough to imply a vast family of constraints on emergent physics,
> - is testable enough to be wrong in multiple, clear ways,
> - and is philosophically disciplined enough to resist being turned into a buzzword.

Everything in this repo is *scaffolding* around that attempt.

At this stage, the program is formulated as a **vacuum mechanics** test-bed: we treat "vacuum" as the cleanest arena where cancellation, phase twists, and residues can be defined and computed.

The long-term ambition is that the same axiom could, in principle, map into quantum fields, Standard Model structures, and cosmology; but no such map is assumed or claimed here. The work in this repo is about building the discipline that would make any such map, if it exists, legible and falsifiable.


---

## High-Level: What Is Origin-Axiom?

In the most compact form:

- We take **vacuum** (the “empty” ground state) seriously as the fundamental “object”.
- We imagine it as **perfect destructive interference** of some underlying structure – a kind of **global cancellation**.
- We ask:  
  > What if we introduce the *minimal possible twist* to this perfect cancellation, such that:
  > - it *cannot* be fully undone,
  > - it is *globally consistent*,
  > - and it produces a **structured residue** that behaves like the universe?

This “minimal twist” is encoded as a **non-cancelling phase** with a specific, axiomatically chosen angle (θ\* or related constructions explored across phases). The program is not “phi-worship” or numerology; it is a **self-critical, multi-phase attempt to see whether any such twist survives sustained mathematical, physical, and conceptual pressure**.

The repository is organized into **phases** (0–5), each with its own contracts, gates, and artifacts.

---

## Phase Overview (0–5)

The Origin-Axiom program is deliberately staged:

- **Phase 0 – Contract & Grounding**  
  - Define what counts as evidence, rigor, and non-drift.
  - Explicitly state non-claims and failure modes.
  - Specify toolchains, logging, and reproducibility requirements.
  - Lock in a **Phase 0 Contract** PDF that later work must honor.

- **Phase 1 – Toy Ensembles (Locked)**  
  - Build controlled toy ensembles where a residue can be computed.
  - Quantify existence, robustness, and scaling in toy settings only.
  - Produce the Phase 1 paper and canonical figures.

- **Phase 2 – Mode-Sum + Bounded FRW Viability (Under Audit)**  
  - Implement the residue in a stricter mode-sum model.
  - Encode corridor/filter language and bounded FRW-style diagnostics.
  - Keep claims explicitly toy/diagnostic.

- **Phase 3 – Mechanism Module (Active)**  
  - Lock a baseline non-cancellation floor on a global amplitude.
  - Provide binding-style diagnostics and mechanism-level tables.
  - No flavor calibration or corridor narrowing in the canonical Phase 3.

- **Phase 4 – FRW Toy Diagnostics (Diagnostic Stub)**  
  - Map Phase 3 outputs into FRW-style toy backgrounds and viability masks.
  - Provide a data-probe hook without claiming real-data contact.

- **Phase 5 – Interface & Sanity Layer (Rung 0–1)**  
  - Read locked Phase 3/4 outputs and emit interface summaries/sanity tables.
  - No new mechanism or cosmology claims.

- **Stage 2 – Diagnostic Belts (In Progress)**  
  - Downstream analyses over Phase 3/4 outputs: FRW corridor analysis,
    mechanism/measure analysis, joint mech–FRW analysis, and FRW data-probe audit.
  - Non-canonical until promoted.

Each phase is gated. We do not “declare success and move on”; we **audit and repair** earlier phases as new insight arrives.

---

## Repository Structure (Conceptual)

> Note: Exact paths may evolve, but this is the conceptual layout.

- `phase0/` – Contracts & Grounding
  - `paper/` – Phase 0 Contract & rationale (LaTeX, PDFs).
  - `grounding/` – Criteria for rigor, logging, and anti-drift.
  - `logs/` – Decisions, audits, and corrections.

- `phase1/` – Toy ensembles (locked)
  - `paper/` – Phase 1 toy-domain paper.
  - `outputs/figures/` – Canonical toy figures.

- `phase2/` – Mode-sum model + bounded FRW diagnostics (under audit)
  - `paper/` – Phase 2 paper.
  - `src/` – Mode-sum + FRW-style diagnostic code.

- `phase3/` – Mechanism module (active)
  - `paper/` – Phase 3 mechanism document.
  - `src/phase3/` – Mechanism diagnostics and scans.
  - `workflow/` – Snakemake workflows:
    - reproducible runs,
    - logged outputs,
    - artifact generation (plots, tables, PDFs).
  - `outputs/` – Logged and timestamped artifacts.

- `phase4/` – FRW toy diagnostics (stub)
- `phase5/` – Interface + sanity layer (rung 0–1)
- `stage2/` – Diagnostic belts (downstream, non-canonical)
- `experiments/phase3_flavor_v1/` – Archived flavor-sector add-on (non-canonical)

- `docs/` – Cross-phase documentation
  - High-level overviews, diagrams, and auxiliary notes.
  - Potential “Master Index” tying together phases.

- `PROGRESS_LOG.md` – Human-readable log
  - Describes what was done, when, and why.
  - Includes **corrections and demotions** (e.g., “claim X in Phase 2 was too strong; downgraded in YYYY-MM-DD audit”).

---

## Methodology & Ethos

This project is deliberately **slow and self-suspicious**.

### 1. Anti-Numerology Contract

We explicitly **reject**:

- “Golden ratio explains everything” style narratives.
- Pattern-hunting without falsifiability.
- Post-hoc curve fitting dressed as “fundamental insight”.

We allow:

- Using **specific numbers or structures** (e.g., φ, φ^φ, or other candidates) **only when**:
  - they emerge from a structurally motivated mechanism,
  - they survive basic sanity checks,
  - and their use is clearly labeled as **hypothetical**, not established.

Every candidate mechanism must answer:

1. **Why this object?**  
   What structural role does it play in the cancellation/twist picture?

2. **What does it forbid?**  
   A good theory constrains; it makes some worlds impossible.

3. **Where does it obviously fail?**  
   We prefer mechanisms that are *clearly wrong in specific ways* over unfalsifiable narratives.

### 2. Reproducibility & Workflow

- All serious numerical or symbolic work must:
  - live in version-controlled code,
  - be runnable from minimal instructions,
  - produce outputs into `outputs/` with timestamps.

- Snakefiles / workflows:
  - define **full pipelines** from raw parameters → derived quantities → plots / tables → PDF artifacts.
  - act as **gates**: if a result cannot be reproduced, it does not “exist” as a claim.

### 3. Logging & Honesty

- **PROGRESS_LOG.md** is not a marketing document.
- It records:
  - partial wins,
  - dead ends,
  - over-claims,
  - conceptual mistakes,
  - and “we thought X in March, but it was wrong; here’s the fix.”

The goal is to make it possible for a skeptical outsider to:

1. Reconstruct what was done.
2. See how the claims shrank or sharpened over time.
3. Trust that nothing is smuggled in “between the lines”.

---

## Scientific Ambition (and Its Limits)

What this program *hopes* to eventually touch:

- **Vacuum energy & cosmological constant**  
  - Is there a principled route from the axiom-level twist to something like Λ?
  - Can we get:
    - the *order of magnitude* right,
    - or at least a **structural dependence** that’s non-trivial?

- **Field Content & Symmetries**  
  - Could the twist constrain:
    - the number / types of fields,
    - the structure of interactions,
    - symmetry-breaking patterns?

- **Flavor, Hierarchies & Scales**  
  - Is there any admissible route from the axiom to:
    - mass hierarchies,
    - mixing patterns,
    - or other “weird coincidences” in the Standard Model?

- **Emergent Spacetime & Gravity**  
  - Does the twist naturally live:
    - in field space,
    - in configuration space,
    - or in something deeper that “unfolds” into spacetime?
  - Can we say anything coherent about:
    - GR-like behavior,
    - curvature,
    - or FRW-like cosmology?

We are **not** currently claiming:

- A full new theory of everything,
- A derivation of all constants,
- Or a proven deep reason for the Standard Model.

We are building a **ladder of increasingly constrained, increasingly honest hypotheses**, starting from a single axiom-level intuition.

---

## Status Snapshot

- **Phase 0**:  
  - Conceptually solid, under ongoing refinement in wording and structure.
  - Contract-like documents exist (PDFs via LaTeX).
  - Grounding criteria are defined; may get sharpened.

- **Phase 1**:  
  - **Locked** for conceptual continuity.
  - Serves as a stable narrative skeleton.
  - New insights should not casually alter Phase 1, but may be captured in Phase 2+ with cross-references.

- **Phase 2**:  
  - Mixed quality: contains:
    - genuinely interesting structural ideas,
    - alongside earlier over-extensions (especially around φ^φ).
  - Currently in an **audit/repair** mode:
    - demote or retire weak arguments,
    - preserve only those parts that can be defended under Phase 0 standards.

- **Phase 3**:  
  - Actively developed.
  - Focus on:
    - building a **ledger of constraints**,
    - testing mechanisms against simple models,
    - and preparing a path to Phase 4 without hype.

- **Phase 4 & 5**:  
  - No serious “results” yet, by design.
  - Will only be activated once Phase 2–3 withstand an internal skeptical review.

---

## How to Engage with This Repo

### If You’re a Physicist / Mathematician

- Treat this as:
  - a **living lab notebook** around a speculative, axiom-level idea.
- Where to look first:
  - Phase 0 Contract – to understand the standards and ethos.
  - Phase 1 – for the conceptual framing.
  - Phase 2 / 3 – for mechanisms and constraints.
- What feedback is most valuable:
  - “This mechanism cannot work because ___.”
  - “Here’s a no-go argument you should check.”
  - “This part overlaps with [known result]; you should either integrate it or constrain against it.”

### If You’re a Philosopher of Science / Foundations Person

- Examine:
  - How the axiom is framed in relation to:
    - explanation,
    - unification,
    - and meaning.
  - Whether the methodology respects:
    - underdetermination,
    - model pluralism,
    - and the limits of inference.

- We welcome:
  - critiques of the **ambition** itself:
    - Is “one twist to rule them all” even a coherent desideratum?
  - suggestions for:
    - better ways to phrase claims,
    - clearer epistemic boundaries.

### If You’re a Curious Reader

- Start with:
  - The Phase 1 conceptual document (once linked clearly).
  - High-level diagrams in `docs/`.
- Read this as:
  - a long-term research story,
  - not a finished theory.
- It’s okay to just enjoy the narrative and the diagrams without buying into any of the speculative parts.

---

## Roadmap (Conceptual)

Near-term goals:

1. **Complete a rigorous Phase 2 audit**
   - Identify and clearly mark:
     - over-claimed sections,
     - numerological temptations,
     - and places where “structure” is actually just pattern-finding.

2. **Stabilize a small set of candidate mechanisms**
   - Keep only:
     - those with structural motivation,
     - clear testability,
     - and non-trivial constraints.

3. **Build and document Phase 3 constraint ledger**
   - Implement a reproducible code path:
     - from axiom-level parameters → derived quantities → tests.
   - Document both:
     - successes,
     - and “this obviously fails; here is why”.

4. **Clarify gateways into Phase 4**
   - Define:
     - what counts as “enough” in Phase 3 to justify serious confrontation with data.
   - This includes:
     - internal peer review,
     - checklists for self-consistency,
     - and “no-go” test suites.

Longer-term aspirations:

- If, after all this, any part of the axiom-level twist remains:
  - Prepare:
    - one or more honest papers,
    - with a strong distinction between:
      - established consequences,
      - conjectural extensions,
      - and outright speculative visions.
  - Engage:
    - with institutional partners,
    - with a clear ethical frame around:
      - interpretation,
      - potential technological spinoffs (if any),
      - and societal discourse.

---

## Contributing / Contact

At this stage, the project is mostly **closed-development but publicly readable**. Contributions are welcome in the form of:

- Issues pointing out:
  - mathematical mistakes,
  - conceptual confusions,
  - redundant or misleading sections.
- References to:
  - relevant no-go theorems,
  - related work in foundations, cosmology, QFT, or philosophy of physics.

If you’re seriously interested in engaging:

- Please open an issue summarizing:
  - your background,
  - what aspect of the program you’d like to probe,
  - and any initial critique or pointer.

The safest way to interact with this repository is as a **speculative, rigorous playground** around a single, stubborn question:

> Can we write down a minimal, axiom-level deformation of vacuum cancellation that:
> - forces a structured universe,
> - stands up to hostile scrutiny,
> - and stays honest about what it does *not* explain?

Everything here is in service of that question.
