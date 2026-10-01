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

- **The slope instruments (2026-10-01, B1432–B1440)** — read these before any probe of the Standard-Model frame on
  a punctured-torus bundle; **never run a module-by-module index census there again**:
  - `frontier/B1438_the_slope_law/verification/slope_census.py` — `slope_census(eps, word, k)`: the index of every
    sector module, the generation-shaped backgrounds, lifts, signs and deck orbits of a level, from the slope
    s(χ) alone (two primes above 2·10⁹); reproduces B1434's 68 levels in twenty seconds. `slope_law.py::exact_slopes`
    gives s exactly over ℚ(ζ_N); `cot_formula.py` the letter-by-letter closed form.
  - `frontier/B1439_the_census_by_slope/verification/census_by_slope.py` — the same with the vanishing of every
    allowed coupling, and `population(maxlen, tmax)` for any range of signed word states.
  - `frontier/B1435_the_interaction_census/verification/relcup.py` — the relative triple product a ∪ b ∪ h on an
    explicit relative fundamental chain (`Bundle.fundamental()` asserts ∂C = z as integer chains); modules and
    cocycles over a prime field; `interaction_census.py` drives it; `exact_couplings.py` is the second
    implementation over ℚ(ζ_N).
  - `frontier/B1440_the_rank_bound/verification/modules.py` — `build(L, chars, coeff)`: a triangular module of
    any rank, one superdiagonal at a time (returns None when the Massey-type obstruction is non-zero);
    `two_step`, `ext2`, `dsum`; feed the result to B1427's `myindex.index`. Before searching for an index above
    ⌊rank/2⌋ on a one-cusped bundle, read B1440: it cannot exist.
  - `frontier/B1434_the_architecture_census/verification/architecture_census.py` — `monodromy`, `level`,
    `states(maxlen)`: the mapping-torus presentation of any signed word state and its cyclic levels.
- **Two gates added 2026-10-01:** `lead-debt` (`scripts/checks/lead_debt.py`: leads and OPEN arcs age at 21 days on
  a ratchet; a lead number carried by two open leads fails outright) and the doc-currency lock
  (`tests/test_doc_currency_gate.py`: the declared-debt set is pinned; another seat's arc number is not a citation).

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

## Three more (2026-10-01, B1432–B1440)

- **A script that writes next to `__file__` and is `exec`'d from the repository root writes into the root.** A banked
  frame run that way overwrote a tracked `results.json`. Run banked scripts in a scratch checkout
  (`git worktree add --detach <dir> HEAD`), never by `exec` from the working tree.
- **A reader sealed with an instrument must be run twice before the seal.** B1439's reader matched its own output
  with its input pattern and could not be re-run; it was sealed, so it could not be fixed (E52).
- **A census that parametrises backgrounds by a lift enumerates only what lifts.** Two seats and main reported "the
  three-fold cover does not fire" for that reason (B1432, E54). Ask of every enumeration what it cannot reach.
