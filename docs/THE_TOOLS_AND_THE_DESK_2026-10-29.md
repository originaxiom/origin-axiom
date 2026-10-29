# THE TOOLS AND THE DESK — what we adopt, and what the desk is for (main, 2026-10-29; at the owner's ask)

*The owner (2026-10-29): "lets adopt all the tools that would sophisticate our framework and actually contribute. lets
analyze it objectively? we should clarify what we actually want from the dashboard/workdesk so we build it on those
principles". Part I judges each candidate tool by the open problem it serves; Part II states the desk's purpose and
principles. Data-free.*

## Part I — The tools

**The test applied to every candidate.**
1. Does it compute something an open row needs that the record cannot compute now? Convenience alone does not count.
2. Can it be calibrated against a published or record result before it is trusted?
3. Can it run inside the record's discipline: scripted, pinned, free to run, no external service holding our data?
4. Does it add risk: licence, maintenance, a second source of truth?

**Adoption means:**
- a pinned install in its own environment, so the canonical test environment the suite runs in is not changed;
- one calibration reproducing a known result, kept as a lock;
- only then, use.

### Adopt now

| tool | what it adds | the rows it serves | calibration before use | licence |
|---|---|---|---|---|
| **PyR@TE 3** | two- and three-loop running equations for any gauge group and matter content | P-363, P-365 (the six moved from M_Z to the frame's scale: the comparison scale is a choice today); P-415 (the towers' gauge-coupling unification with the object's matter); P-502 | the SM's one-loop gauge coefficients (41/10, −19/6, −7) and a published two-loop running | GPL-3 (used as a tool, not combined into the record's code) |
| **wilson, flavio** | SMEFT running; quark masses and CKM elements run between scales with stated schemes; flavour observables | Step B of THE FINAL ATTACK (the nine at the KIND_TABLE's precision, schemes per the input-completeness ledger); P-363 | the package's own published SM predictions for two observables | MIT |
| **RunDec (its Python port)** | quark-mass running and decoupling at four loops | the six's scheme and scale (input-completeness rows 1 and 2) | a published m_b(m_b) → m_b(M_Z) running | GPL (a tool) |
| **LiE** | branchings and tensor-product invariants of Lie groups | P-415 (SU(5) ⊂ SO(10) ⊂ E₆), P-397 (the B − L channels 45, 126, 351′ and their content), P-503 | E₆ → SO(10) × U(1): 27 = 16 + 10 + 1, and the record's own branchings | LGPL |
| **dynesty** (nested sampling) | the Bayesian evidence of a frame against the data, that is, its description length with priors | THE FINAL ATTACK's compression statistic (§ 1: explanation as compression; the evidence is its standard form, with the frame-native measure as the prior on τ); P-418's generator | a Gaussian test problem with known evidence, and a published model-comparison example | MIT |
| **the PDG's Python API** | measured values with the release, scheme and date recorded | input-completeness row 11 (source freshness); every seal's data packet | the API's value against the PDG's printed table for one release | the PDG's terms (read only) |
| **a local embedding model with a small vector index** (fastembed with a bge-small-class model, ONNX, CPU; sqlite or FAISS) | search by meaning across arcs, register and ledgers | P-500: the seen-first sweep's recall; the regex sweeps miss paraphrases (P-123) | recall on the alias sweeps' known misses (a planted control both ways) | Apache/MIT |
| **a token map** (a short script) | tokens per folder and file | P-501: delegation briefs and budgets | counts against a hand count on three files | the record's own |
| **the panel's web stack** (TypeScript, a component kit, a table and a graph library, a bundler) | the desk's standard (P-497) | P-420 | the desk's locks (the numbers on the page recounted from the files) | MIT |

### Adopt later, when a row needs it

| tool | when |
|---|---|
| **Sage** (modular forms, CM points, class groups, Hilbert modular surfaces) | P-425's finite CM set: class numbers and CM points of ℚ(√5, √−3) exactly. PARI/GP (already used) covers most of it; Sage only if PARI's coverage ends. |
| **Lean 4 + mathlib** (formal proof), with a blueprint | A pilot: one load-bearing short theorem machine-checked (the cusp parity theorem, T-CUSP-PARITY-EXCLUDES-THREE, or B1815's exit law). The blueprint's dependency graph is the desk's arc graph's formal twin. Large learning cost, so one pilot first. |
| **Regina** (normal surfaces, triangulations) | if L250's non-abelian bundle (P-401, P-403) needs surfaces in m004 beyond SnapPy |
| **SARAH and SPheno** (model to spectrum) | only if the programme builds a full field theory of the towers (Mathematica needed) |

### Not adopted

| tool | why not |
|---|---|
| **FeynArts, FormCalc** | Diagram generation for amplitudes. The programme's couplings come from geometry and its loops are closed formulas (W150's supertrace). Mathematica is needed. Revisit if a process is ever computed. |
| **FeynGame, TikZ-Feynman** | Drawing only; for the paper's figures if any. |
| **Arc676's The-Standard-Model** | A simulation of particles moving, not of the SM's parameters; archived; GPLv3. Its one lesson — computing kept apart from drawing — is already the desk's. |
| **GAMBIT, MasterCode** | Global fits of beyond-SM models at scale. The programme's sealed tests are smaller and need their own nulls; the evidence comes from dynesty directly. |
| **CYTools, Kreuzer–Skarke** | The Calabi–Yau landscape: not the programme's object class. Revisit if the towers move to a CY compactification. |
| **DataLad, DVC** | The record's hash-pinning rules (sha-256 in ARTIFACT_HASHES, gzip above 100 MB) already cover large outputs. A second system is a second source of truth. |
| **LLM-written repository wikis** (DeepWiki-style) | Summaries drift and overclaim, the failure the record keeps catching. The record's maps are generated by code. An outside index of the public repository is unverified data. |
| **Repomix, Gitingest** | The token map plus the record's own slicing do the same. |

## Part II — What the desk is for

### The questions it must answer at a glance (each view answers one)
1. **Where do we stand?** 0 of 19; the inputs scoreboard (P-418); the compression ledger; the latest landing.
2. **What is open, in what order, and what waits for the owner?** The register by disposition and queue slot; the OWNER
   rows.
3. **What does a claim rest on?** An arc's dependency cone, scope, verification route, seat provenance and supersession.
4. **What has been tried and failed, and what would reopen it?** The kill graph with its hatches. A verified negative is
   shown with the same weight as a positive.
5. **What did the seats do, and what has main verified?** Harvest and relay state by seat: pins, debt, statuses.
6. **Is the record healthy?** Gates, locks, the review counter, the debts (points, relays, harvest), the latest suite.
7. **What does the mathematics look like?** Reproducible plates of the construction — the rule, the threads, the object,
   the fibre, the clocks, the CM points — each regenerated by a repository script and labelled weave or thread.
8. **Where is the final attack?** Its steps, seals, looks and outcomes.

### Principles (each one a lock or a gate where it can be checked)
1. **Generated, never hand-kept:** every element is computed from the record at a named commit.
2. **Provenance on every value:** one click opens the file and line at that commit.
3. **The grade travels with the claim:** verdict, scope, FORCED / ADMITTED / CHOSEN / FITTED, weave or thread. No claim is
   shown without its grade.
4. **No overclaiming through pictures:**
   - counts are shown against stated end conditions (0 of 19 always visible);
   - layout does not imply importance;
   - dependency cones, not whole-graph hairballs; matrices where they read better;
   - negatives are not hidden or greyed.
5. **Read-only:** inspection, filters, search, drill-down. The repository is the only place anything is written.
6. **Answers, not decoration:** a view without a question is removed.
7. **High-end craft** (the owner's standard, P-497): a design system, light and dark, typography, accessibility,
   keyboard, performance.
8. **Private by login, public by code** (P-496): the site sits behind Cloudflare Access. The code is public, and no secret
   lives in the repository. The data is public in the repository either way.
9. **Reproducible:** a rebuild at a commit gives the same bytes.
10. **Locked:** the desk's numbers are recounted from the files by tests.

### Two readers, one source (the owner's ruling, 2026-10-29)
*"the dashboard should serve us both, me for better visualising the universe we're trying to construct, and the
frameworks structure, analyze, and you to be able to easier get back to the complete context after compactification, and
make sure you skip no arc/node/calculation/math/tool"*

- **One data layer.** The desk's SQLite index and JSON are generated at every landing. They hold:
  - every arc and dependency edge;
  - every computation (script, output and sha-256, and its arc);
  - every tool (version and calibration lock);
  - every register and ledger row, every seat's pin and debt;
  - the final attack's state.
- **The owner's reader: the visual panel.**
  - The universe under construction: the object, the weave, the frames, the towers, the clocks.
  - The framework's structure.
  - Analysis.
- **Main's reader: the context-recovery card** (`docs/views/CONTEXT_RECOVERY.md`, generated, never hand-kept), with a
  query tool over the index. It is the first read after a compaction, beside the memory files and the in-flight log.
  - What is open, by priority; what waits for the owner.
  - What is running or computed but unlanded.
  - The last landings; each seat's debt; the attack's step.
- **Skip nothing: the completeness locks.** A gap fails the gates, so nothing is skipped silently.
  - Every arc folder is in the index.
  - Every verification script has its output and an arc.
  - Every point in the register has a disposition.
  - Every adopted tool has a calibration lock.
  - Every seat commit past its pin is harvested or counted as debt.

### Non-goals
- Not an editor and not a chat.
- Not an LLM summary layer.
- Not a public relations face: that is the owner's later decision about the site.
- Not entertainment.
