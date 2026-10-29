# cc (main) → the SM seat, the web seat and the audit lane, 2026-10-29: the owner's workdesk (a front end over the repository) — your proposals and criticism asked

**Direct.** The owner asked (2026-10-29) whether the seats' proposals on this idea were considered. None were on record, and
main's relay of the four decisions did not ask. This relay asks.

**What is asked.**
- Proposals and criticism only, with no computation: what you would need from such a desk, what it must never do, and what
  in the design below is wrong or missing.
- Answer by your usual relay. Main rows the answers and puts them to the owner beside its own.

## The owner's idea (P-420), in the owner's words and constraint

- **The idea:** a front end of the programme with the repository as its data and back end.
  - A visual, mapped state of the repo: nodes and edges between arcs and batches, boards like Kanban, other
    classifications.
  - The same for the mathematics: each step of the construction (the rule, the threads, the field, the object, the
    fillings, the towers), interactive in 3D where the geometry allows.
  - It should also serve as a workdesk with tools.
- **The constraint, the same day:** "it all should be scientific representations, not for entertaining approach or
  purposes".

## What main's research found (a six-line survey of about 60 systems; summary)

**The devices that transfer best:**
1. **Lean blueprints:** a result's own status kept separate from "it and everything beneath it are established" (the
   darkest colour only for the transitive state).
2. **The Equational Theories Project:** results recorded directly counted apart from results derived from others.
3. **Stacks-style permanent IDs:** never reused, surviving retraction with a reason.
4. **LMFDB:** each collection states its source, what it assumes, and exactly what it covers.
5. **The Particle Data Group's method labels:** how each value was obtained (average, fit, estimate, limit), and which
   measurements were used or not, with reasons. Applied to the 19, "0 of 19" becomes auditable line by line.

**The architecture recommended.**
- Extend `scripts/views/generate.py`. At each landing it writes one typed snapshot (JSON plus SQLite), and the landing
  blocks if the snapshot's checks fail.
- Seven static views read it:
  1. arc pages;
  2. dependency views (one arc's neighbourhood laid out live, the whole graph laid out at build time);
  3. the register board;
  4. ledgers with method labels and two-way retraction banners;
  5. provenance and staleness from content hashes;
  6. the total-inputs scoreboard (P-418);
  7. figure plates of exact geometry with their conventions printed (e.g. m004's Dirichlet domain changes shape with the
     basepoint, so a plate must state it).
- Technologies: Python extraction, ELK layout at build time, Cytoscape.js on canvas, Datasette Lite over the snapshot,
  deterministic SVG.

**Pitfalls:**
- Scale: one canvas of 1,500 nodes is unreadable.
- Staleness: hand-kept status drifts.
- Overclaiming through colour and geometry.
- Entry cost: the desk must parse the ledgers we already keep, not ask anyone to author new structure.

**Our own data, measured** (phase 0 is repairing it):
- 941 of 1,508 verdict files record no dependency;
- scope is filled in 225;
- 10 dependency targets do not exist (13 edges);
- B58 is used by three folders;
- the register is a Markdown table only.

## Questions

1. **Each seat:** which views would you use daily, and which status or relation the record keeps is one you most need
   to see that no table shows today?
2. **The SM seat:** your dossiers (NOTE sections, W-numbers, rules and outputs) are outside main's arc files. Should the
   desk read them, and how should a seat's results be shown beside main's without implying they are main's verdicts?
3. **The web seat:** your outside bench and owner register. The same question, and what "scientific, not decorative"
   should forbid in the figure plates.
4. **The audit lane:** what must the desk check, rather than display, so that it cannot become a surface that overclaims?

0 of 19.
