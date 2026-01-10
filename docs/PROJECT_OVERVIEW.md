# Origin Axiom – Project Overview (Stage I: Phases 0–5)

This document gives a **narrative overview** of the origin-axiom program as it
exists in this repository:

- what the program is trying to do,
- how the phased structure (0–5) is meant to work,
- how to read the phase papers,
- how this “Stage I” scaffold will feed future work.

It is deliberately higher-level and more discursive than the top-level
`README.md`, which stays focused on “what is here” and “how to build it”.

---

## 1. Intent of the origin-axiom program

The origin-axiom program is a **phased, reproducible exploration** of a simple
idea:

> If the “perfect cancellation” encoded in identities like
> \( e^{i \theta} + 1 = 0 \) is too ideal for a universe that actually exists,
> can we treat the failure of exact cancellation — a **non-zero residue** —
> as a primitive organizing principle for toy models of fields, ensembles,
> and cosmological backgrounds?

The program:

- chooses a **particular irrational “twist”** (\( \theta_\star \sim \phi^\phi\))
  as a mathematically interesting, self-referential, transcendental candidate;
- builds **toy mechanisms** where a non-cancelling residue is made explicit and
  can be probed numerically;
- gradually translates this into **FRW-style background toy models**, while
  aggressively separating what is *tested* inside the code and tables from
  any speculative narrative.

The key is not the specific number, but the **discipline**:

- Every claim must be tied to a **phase, rung, artifact, and script**.
- Every phase publishes a **paper** plus a **claims table** plus a
  **reproducibility appendix**.
- Future phases are required to consume the prior outputs through **narrow,
  well-specified interfaces** (rather than rummaging around in the repo).

---

## 2. Stage I scaffold: Phases 0–5

Stage I is everything currently implemented in this repo:

- **Phase 0–2**: governance, toy ensembles, and corridor/filter language.
- **Phase 3**: baseline mechanism and ensemble-level diagnostics.
- **Phase 4**: FRW toy mappings and viability masks.
- **Phase 5**: interface and cross-phase sanity layer.

Stage 2 is a **diagnostic belt** that is already in progress and lives under
`stage2/`. It stays strictly downstream of Phase 3/4 outputs and remains
non-canonical until explicitly promoted. Active axes include:
- `stage2/frw_corridor_analysis`
- `stage2/mech_measure_analysis`
- `stage2/joint_mech_frw_analysis`
- `stage2/frw_data_probe_analysis`

You can think of Stage I as building a **rigid spine**:

1. **Phase 0 – Governance and filters**

   - Defines how the program is allowed to operate.
   - Sets out constraints on claims, permissible operations, and evidence.
   - Introduces the idea of **filters and corridors** as a way to talk about
     “admissible” regions without over-claiming.
   - No physics claims; only statements about the **rules of the game**.

2. **Phase 1 – Toy ensembles and residues**

   - Introduces simple **lattice / oscillator-like** ensembles where a
     residue-like quantity can be computed as a function of \(\theta\).
   - Plays with robustness: how sensitive is the residue to obvious knobs
     (cutoffs, truncations, minor model variants).
   - The products are tables and figures which justify the move to Phase 2.

3. **Phase 2 – Corridors and theta filters**

   - Encodes “regions of interest” in \(\theta\)-space into **machine-readable
     corridor/filter objects**.
   - These are not yet “physical constraints”, but **internal language**:
     essentially, “if we use this mechanism, these regions behave better
     according to our diagnostics”.
   - Phase 2 is about **organizing the search space** for later phases.

4. **Phase 3 – Baseline mechanism and diagnostics**

   - Commits to a **single baseline mechanism**.
   - Produces:
     - an amplitude table over a filtered set of \(\theta\),
     - diagnostics for stability / binding behaviour,
     - a more mature claims ledger and reproducibility appendix.
   - Phase 3 is where the mechanism **stops changing every five minutes** and
     becomes something future phases are allowed to depend on.

5. **Phase 4 – FRW-like toy backgrounds**

   - Translates the Phase 3 mechanism output into FRW-style background
     parameters in a **toy** setting (e.g. vacuum energy proxy, \(\Omega_\Lambda\),
     age, simple viability flags).
   - Generates masks and diagnostics for which \(\theta\)-points satisfy simple
     FRW-like viability criteria.
   - Provides a **data-probe hook** (binned FRW distance data) which is kept
     empty in the baseline configuration: there is infrastructure for
     future data contact, but no claims about real data yet.

6. **Phase 5 – Interface and sanity layer**

   - Reads the current repository state and produces a **cross-phase summary**
     (`phase5_interface_v1_summary.json`) and a **sanity table**
     (`phase5_rung4_sanity_table_v1.csv`).
   - Acts as the **contract boundary** between Stage I and any future work:
     future code should talk to the program primarily via the Phase 5 interface
     and the per-phase artifacts, not via ad-hoc paths into `phase3/` or `phase4/`.

---

## 3. How to read the phase papers

A suggested reading order:

1. **Phase 0 paper** – to understand the governance and constraints.
2. **Phase 1 and 2 papers** – to see how the toy mechanism and corridor language
   emerged.
3. **Phase 3 paper** – to understand the baseline mechanism and why it is
   considered “locked” at this rung.
4. **Phase 4 paper** – to see how the mechanism is mapped into FRW-style
   backgrounds and what the simple viability probes actually test.
5. **Phase 5 paper** – finally, to see the interface layer and how all the
   pieces are summarized for future consumption.

At any point, the paper’s **claims table** and **reproducibility appendix**
should be treated as the canonical source on:

- what the phase asserts,
- which scripts and outputs support those assertions,
- what is explicitly *not* being claimed.

---

## 4. Interacting with the repository

For **usage details**, see `docs/INTERACTING_WITH_REPO.md`. At a high level:

- Always go through the **phase gates** and the global
  `scripts/build_all_papers.sh` when you want a clean rebuild.
- Treat `phaseN/artifacts/origin-axiom-phaseN.pdf` as the canonical paper
  for Phase N.
- Treat `phase5_interface_v1_summary.json` and
  `phase5_rung4_sanity_table_v1.csv` as the preferred machine-readable entry
  points for tooling that wants to consume the Stage I program.

---

## 5. Where future work fits

Stage I (Phases 0–5) is designed so that **future work has a clear place to
plug in** without rewriting the entire stack.

Examples of natural directions:

- **Stage II – Data-aware FRW probes**

  - Populate the `phase4/data/external/frw_distance_binned.csv` hook with
    real or mock data.
  - Introduce new phases (e.g. Phase 6) that sit “above” Phase 4 and Phase 5,
    consuming the existing viability masks and probe summaries and making
    strictly scoped additional claims (e.g. “within this toy, certain regions
    of \(\theta\)-space are consistent with this particular toy dataset”).

- **Stage II – Deeper mechanism analysis**

  - Add new diagnostics to the Phase 3 mechanism (e.g. stability under
    more complex perturbations, spectral properties).
  - Introduce sub-phases or new rungs that enrich the **mechanism side** while
    maintaining the existing contracts (tables, paths, and masks stay
    compatible, or provide clear migration notes if they change).

- **Stage II – Microphysics and fields**

  - Construct toy field-theory or many-body embeddings that take the Phase 3
    mechanism as input and output more detailed observables.
  - These would likely live in new directories (`phase6/`, `phase7/`, or
    dedicated `field/` submodules) but they should still respect the Phase 0
    governance and the Phase 5 interface contract.

In all cases, the intent is to **extend the scaffold**, not to silently mutate
the meaning of existing artifacts. When big changes happen, they should be
accompanied by:

- updated phase papers,
- updated claims tables,
- migration notes (see e.g. legacy migration docs in `docs/`).

---

## 6. Legacy material

Earlier explorations – scattered notebooks, older repos, prior scans – live
outside this phased program. When a legacy idea is worth salvaging, it should:

1. Be summarized and evaluated in a **migration note** under `docs/` (e.g.
   `LEGACY_MIGRATIONS.md`).
2. Be reintroduced as a **cleaned-up** script, module, or phase extension that
   passes through the same gate / artifact / claims discipline as Stage I.

Flavor-sector Phase 3 work is archived under `experiments/phase3_flavor_v1/`
and is non-canonical.

This ensures that the Stage I program remains a **coherent, auditable
experiment**, even as it evolves.

---

For a compact table of phase status, canonical artifacts, and promotion gates, see `docs/GATES_AND_STATUS.md`.
