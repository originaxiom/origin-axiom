# THE LIVE TOOLBOX (the split's live half — R1-1 discharged 2026-08-13)

**The protocol's rule ("read the toolset before any important probe") points
HERE.** The historical body is frozen at `docs/TOOLBOX.md`. This page stays
small on purpose — the currency gate watches it, and a one-pager can stay
current where a 600-arc enumeration provably could not (four reviews of
escalation are the proof).

## The bench's standing instruments (2026-08-13)

- **The suite** (`python -m pytest tests -q`) — the certificate; read ITS exit
  code, never a pipe's (§G's law).
- **The gates** (`scripts/checks/` — run via any push, seconds) — including
  doc-currency (18 living docs), the freshness sweep
  (`instrument_freshness.py`, non-mutating), the representation sweep, the
  verdict-body agreement gate.
- **The atlas** (`scripts/atlas/query.py card <topic>`) — re-orientation and
  the obstacle→resolution oracle; regenerate with `scripts/atlas/atlas.py`
  whenever an arc is added.
- **The views** (`scripts/views/generate.py`) — the 4 generated read-only
  surfaces; the review refreshes all 8 (these + README + the 7 state-block
  ledgers) IN the review commit.
- **The kill graph** (`frontier/B738_pathfinder_compiler/kill_graph.json`) —
  every NEGATIVE routes here with a hatch, or the b833 gate blocks the push.
- **The seal protocol** — shasum-256 → `docs/SEAL_LEDGER.md` → commit → push
  BOTH remotes → only then compute.
- **The extraction debt, named**: the full inventory of the frozen body's
  still-live tools (scripts under `frontier/*/` with reuse value) is owed as
  a digest side-task; this page grows only from that audited extraction,
  never from memory.

## The extraction seed (B1177/R50-5 — the owed digest side-task, opened with the audited first inventory)

- **`e6_centralizer.py`** (54 consumers corpus-wide) + **`frame.py`** — the E₆ centralizer/frame engines;
  the single most-reused unindexed pair.
- **The B1103 engine** (live SEAM/SP-2 consumers) — the being-gate machinery.
- **The B878 Maass solver** — already cost one full failed rebuild (B1007) for want of indexing.
- **Path repairs owed:** three main-branch scripts point at a nonexistent `frontier/B792_maass_m004_eigenvalues`
  (the Maass material lives elsewhere) — repoint or rehome at next touch.
- Rule: this list grows only from audited extraction (per the frozen body's split), never from memory.

## Instruments audited at landing (each run on the bench the day it is listed)

- **B1238 (2026-09-02)** — `frontier/B1238_seat_harvest_40a3_bronze_octic/verification/`:
  `bronze_invariant_trace_field.py` (invariant trace field of a SnapPy census word by TWO routes —
  tr(g²) at 1000 bits and the tetrahedra shape field — cross-checked with `nfisisom`; this is the
  E55 axis instrument, and it is what caught the degree-6 error at four sites);
  `b211_phi_jacobian.py` (a plane curve's Jacobian → `ellfromeqn` → minimal model → Cremona label,
  with the isogeny-class degree matrix so a point-count match is not mistaken for a label match);
  `z1_compare.py` (rerun-vs-banked ladder comparison for a deleted cell, byte-identity included).
- **The `tracked-deps` gate** (`scripts/gates/gates.py`, E57) — a tracked test or script may not
  depend on a path that exists on the bench but not in git; the local suite is blind to this class
  by construction, so the gate runs at push.

## Four traps this bench walked into in one session (2026-09-10/11, B1325–B1329)

Recorded because each cost a wrong answer that a re-run caught, and all four are
the same species: **an instrument that cannot see the notation its target is
written in reports a clean result.**

- **A grep over TeX or PDF text must be normalised first.** Three separate wrong
  answers in one session: a prior-art PDF scan reported *zero* "figure-eight"
  mentions when the file reads `ﬁgure` with a **ligature**; a retraction gate
  missed the retracted `all $83$ members` while matching `all 83 members`; and a flattener that
  stripped `~` deleted the markdown `~~strikethrough~~` that marks a line as a
  *mention*, turning a struck-out claim into a live one. **Normalise ligatures and
  TeX wrappers before matching, and read mention-cues from the ORIGINAL line**
  (`scripts/checks/retraction_sweep.py::_flatten`, B1326).
- **`retraction_sweep` now sweeps `*.tex` as well as `*.md`** (B1326). It globbed
  `*.md` only, so `papers/P3_THE_PAPER/main.tex` — the flagship document — was
  structurally invisible to the gate meant to guard it.
- **`scripts/atlas/render.py` renders; `scripts/atlas/atlas.py` mines.** Running
  only the first refreshes the rendered map while leaving `atlas_data.json` stale,
  and `gate_atlas_fresh` then reports the new arcs as dirs-only. **Run `atlas.py`
  then `render.py`, in that order, whenever an arc is added** (B1328).
- **A single `Sym^m` germ is a biased test of the index** (B1329). It has
  `t_0 = 1`, `t_1 = 2`, so the restriction image is a line in a 2-dimensional
  space and `I != 0` would need the extreme `r_1 = 0` or `2`. The realistic object
  is a **sum** — `27` on an `sl2` germ is `(+) Sym^{n_i}`, `t_0 = #summands`. Test
  sums before concluding anything vanishes.

