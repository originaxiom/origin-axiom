    # Origin Axiom – Phased Vacuum Mechanics Program

    > “Twist Euler’s perfect cancellation just enough that reality cannot vanish,  
    > then follow the residue wherever it leads.”

    This repository hosts the **phased Origin‑Axiom program**: a step‑by‑step, fully logged attempt to turn a simple *non‑cancelling phase twist* on Euler’s identity into a concrete, testable framework for vacuum mechanics, cosmology, and (eventually) a candidate path toward a unified description of fundamental structure.

    The repo is structured as a **ladder of phases (0–5)**. Each phase is designed to be:

    - **Scoped** – clear aims, hard boundaries, and explicit non‑claims  
    - **Reproducible** – Snakemake workflows, logged runs, and pinned outputs  
    - **Readable** – LaTeX papers summarizing the phase in human language  
    - **Composable** – later phases *only* lean on artifacts explicitly exported by earlier ones

    If you want to *understand the story* first, skim the phase PDFs (see below).  
    If you want to *run the machinery*, see **`INTERACTING_WITH_REPO.md`**.

    ---

    ## Current status (high‑level)

    - **Phase 0 – Motivation & framing**  
      Conceptual groundwork: why “non‑cancelling vacuum twist” at all, what problem it is trying to address, and how it relates to Euler’s identity, fine‑tuning, and “impossibility of perfect nothingness” arguments.

    - **Phase 1 – Formalization of the axiom candidate**  
      Starts turning the philosophical intuition into a precise mathematical ansatz: what we actually mean by a non‑cancelling phase, how \( e^{i	heta} + 1 
eq 0 \) is enforced, and what constraints we impose on candidate \(	heta\)-values (irregularity, transcendence, self‑reference, etc.).

    - **Phase 2 – Early dynamics & scanning attempts**  
      More exploratory and “legacy‑heavy”: various initial scanning and toy dynamics attempts to see how the axiom might generate structure. Some of this has since been locked or superseded by cleaner, later phases, but the rigorous parts remain as a historical rung.

    - **Phase 3 – Mechanism baseline**  
      A **clean baseline mechanism**: a concrete amplitude table over \(	heta\), derived from a well‑specified construction, together with diagnostic tables describing stability, cancellation behavior, and “instability penalty” summaries. This is the first phase that exports a truly *usable* computational object into later rungs.

    - **Phase 4 – F1 mapping & FRW viability probes**  
      Consumes the Phase 3 amplitude table and constructs a simple **F1 mapping** into cosmological parameters. We scan a grid of \(	heta\) values, derive toy FRW histories, and flag which configurations pass basic viability tests (matter era, late acceleration, age constraints, etc.). No claim of “true cosmology” is made – this is **a viability‑mapping layer**, not a fit to real data (yet).

    - **Phase 5 – Interface, sanity table & integration**  
      A thin **interface layer** that reads Phase 3 + Phase 4 diagnostics, checks consistency, and emits a single **sanity summary table** for rungs up to F1. This phase is about *integration and bookkeeping* rather than new physics: it proves that the pipeline is mechanically coherent and ready for future extensions (F2, real data, higher‑level structure, etc.).

    All five phases currently **build cleanly**, export canonical PDFs, and pass the Phase 5 sanity checks at the present rung.

    ---

    ## Repository structure (essentials)

    At top level:

    - `phase0/` … `phase5/` – per‑phase source trees  
      - `paper/` – LaTeX sources for the phase paper (`main.tex` + sections + appendices)  
      - `src/` – phase‑specific Python code, simulation scripts, and interfaces  
      - `outputs/` – generated tables, figures, and diagnostics (tracked where stable)  
      - `artifacts/` – canonical phase PDFs (`origin-axiom-phaseN.pdf`)
    - `artifacts/` – **aggregated copies** of all phase PDFs at repo root:  
      - `origin-axiom-phase0.pdf` … `origin-axiom-phase5.pdf`
    - `scripts/` – top‑level entry points and orchestration helpers, including:  
      - `build_all_papers.sh` – rebuilds all phase papers and aggregates PDFs into `artifacts/`  
      - `phase3_gate.sh`, `phase4_gate.sh`, `phase5_gate.sh` – gated, rung‑aware entry points for each phase
    - `docs/` – conceptual and technical documentation beyond the phase papers  
      (e.g. repo interaction guides, legacy migration notes, etc.)
    - `PROGRESS_LOG.md` – chronological, human‑readable history of major steps and rung changes  
    - `INTERACTING_WITH_REPO.md` – **how to run things reproducibly** (CLI, Snakemake, expectations)
    - `LEGACY_MIGRATIONS.md` (if present) – inventory of useful ideas from the pre‑phased legacy repo and notes on what might be re‑imported in future rungs.

    The intent is that **new work never silently bypasses this structure**. If it matters, it should either:

    - live in a new, clearly scoped phase, or  
    - be added as a documented rung extension within an existing phase.

    ---

    ## How to interact with the repo

    For detailed, command‑level interaction instructions, see:

    - **`INTERACTING_WITH_REPO.md`**

    That document covers:

    - Environment expectations (Python, LaTeX, Snakemake)  
    - How to run per‑phase gates safely (and what “Level A” vs other levels mean)  
    - How to rebuild papers and canonical artifacts  
    - What *not* to edit (e.g. generated outputs vs sources)

    At a very high level, the pattern is:

    ```bash
    # From repo root
    ./scripts/phase3_gate.sh   # run Phase 3 checks, rebuild its paper & artifacts
    ./scripts/phase4_gate.sh   # same for Phase 4
    ./scripts/phase5_gate.sh   # integration sanity + Phase 5 paper/artifacts

    ./scripts/build_all_papers.sh   # rebuild and aggregate all phase PDFs
    ```

    Each gate script is designed to be **idempotent and self‑checking**: it refuses to silently gloss over missing or inconsistent inputs, and it writes diagnostics into `phase*/outputs/` so you can inspect what happened.

    ---

    ## Reproducibility & philosophy

    This project tries to be **as transparent as possible** about what is real, what is conjecture, and what is outright speculative.

    - Every phase paper has an **appendix on reproducibility**, listing:  
      - which scripts to run,  
      - which tables/figures they generate, and  
      - how those map into claims made in the main text.
    - The **Phase 5 sanity table** provides a single CSV view of key artifacts from Phase 3–4, so reviewers can see what the pipeline actually used without spelunking through the tree.
    - **Speculative layers are clearly labeled**. For example, F1 mappings in Phase 4 are explicitly described as exploratory “toy FRW viability probes”, not predictions.

    Long‑term, the goal is to **earn the right** to attempt a genuine unification story by:

    1. Keeping each rung modest and falsifiable.  
    2. Logging failures and dead ends instead of erasing them.  
    3. Building structures that other researchers can *actually run* on their own machines.

    ---

    ## Where future work fits

    The phased program is designed to be **extendable in both depth and breadth**:

    - **Within existing phases** (new rungs):  
      - Tighten diagnostics, add more robust statistics, refine instability measures, etc.  
      - Connect Phase 4 FRW probes to actual cosmological datasets once we are satisfied with the toy layer.  
      - Enrich Phase 5 with additional cross‑phase sanity checks as new artifacts appear.

    - **New phases beyond Phase 5** (Stage 2+):  
      These would likely cover:
      - **F2+ mappings** – richer structures built on top of the F1 layer (e.g. field content, particle‑like excitations, or higher‑dimensional parameter spaces).  
      - **Real‑data confrontation** – bringing in observational datasets under well‑stated assumptions.  
      - **Downward propagation** – asking which features of earlier phases are actually *forced* by success at later ones (closing the loop from cosmology back to the axiom).  

    New phases should follow the same pattern:

    1. A clearly scoped directory (`phase6/`, `phase7/`, …)  
    2. A LaTeX paper with a locked scope and explicit non‑claims  
    3. A small set of exported artifacts that later phases may rely on  
    4. Gate scripts and sanity checks registered in `scripts/` and, where relevant, Phase 5+ integration tables

    In other words: we want a **staircase**, not a tangle.

    ---

    ## Citing or referencing this work

    This project is a **living research program**. If you need to reference it, a simple pattern is:

    > D. M. (Origin Axiom project). *Origin‑Axiom Phased Vacuum Mechanics Program*.  
    > Public git repository: https://github.com/originaxiom/origin-axiom (accessed YYYY‑MM‑DD).

    As the work matures and formal preprints/papers appear (e.g. on arXiv or journal venues), those will be listed in this section and in the phase papers themselves.

    ---

    ## Further documentation

    For deeper dives, see:

    - **Phase papers (canonical narrative for each rung)**  
      - `artifacts/origin-axiom-phase0.pdf` – motivation & conceptual foundation  
      - `artifacts/origin-axiom-phase1.pdf` – formal axiom candidate  
      - `artifacts/origin-axiom-phase2.pdf` – early scanning & legacy bridge  
      - `artifacts/origin-axiom-phase3.pdf` – baseline mechanism & diagnostics  
      - `artifacts/origin-axiom-phase4.pdf` – F1 mapping & FRW viability probes  
      - `artifacts/origin-axiom-phase5.pdf` – integration layer & sanity table

    - **Repo & interaction docs**  
      - `INTERACTING_WITH_REPO.md` – how to run gates, rebuild papers, and avoid common pitfalls  
      - `PROGRESS_LOG.md` – narrative history and rung‑by‑rung evolution  
      - `docs/` – additional conceptual notes, design documents, and migration analyses

    - **Legacy & migration notes**  
      - `docs/LEGACY_MIGRATIONS.md` (if present) – what was salvaged or earmarked from the pre‑phased legacy repo, and how it might be integrated into future phases.

    If you are new to the project and want a reading order:

    1. Skim **Phase 0** and **Phase 1** PDFs to understand the axiom’s motivation and formal shape.  
    2. Read **Phase 3** to see the concrete mechanism baseline.  
    3. Read **Phase 4** to understand how that baseline talks to FRW toy cosmology.  
    4. Glance at **Phase 5** and the sanity table to understand how the pieces are wired together.  
    5. Only then dive into code and diagnostics, using `INTERACTING_WITH_REPO.md` as your map.

    ---

    ## License

    See `LICENSE` in the repository root (or accompanying documentation) for licensing terms.  
    If in doubt about permitted use, open an issue in the repo or contact the maintainer.
