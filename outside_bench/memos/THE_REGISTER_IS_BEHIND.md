# Memo 207 — THE LEAD REGISTER IS BEHIND ITS OWN ARCS, AND THE CORPUS'S OWN INSTRUMENT ALREADY SAYS SO

**Certificate:** `outside_bench/certificates/the_register_is_behind.py` ·
**Output:** `outside_bench/outputs/the_register_is_behind.txt`
**No seal.** This memo asserts only the presence of exact strings in tracked files at
the current HEAD; every claim is a substring test that fails loudly if the string moved.

---

## 1. Four rows that read as live work and are not

Each pair below is two strings in the repository at this HEAD, verified by the certificate.

| lead | the row says | the record says |
|---|---|---|
| **L53** | `OPEN — first in the queue` (`docs/OPEN_LEADS.md:521`) | `L53 CLOSED.` — in the **primary row of the same file** (`:270`), on `THIRD ORDER NOW ALSO EXACT (B578-D1, 2026-07-14)` |
| **L72** | `OPEN (B579)`, with *"Phases 2-3 … **gated on phase 1**"* (`:531`) | `PHASE 1 is banked: B581` and `THIS CELL RUNS PHASES 2 AND 3.` — `frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py:9,11`, with its row in `FINDINGS_WAVE5.md:22` |
| **L78** | `OPEN — Round 2 first`, ★★★★ (`:552`) | `L78 resolves` — `frontier/B583_chiral_content/FINDINGS.md:45`, on `Level 2: rank exactly 6 = dim(θ-even) over 719 slopes` (`:43`) |
| **L174** | `OPEN — C1 first`, ★★★★★ (`:1922`) | `**DONE (B1088`, `(B1090`, `(B1089`, `(B1091` — C1, C2, C3, C4, all four at `:1915–1918`, **eight lines above the row that says C1 first** |

Two of these need no arc read at all: **L53 and L174 contradict themselves inside
`docs/OPEN_LEADS.md`**, four and eight lines apart.

## 2. The corpus already has the instrument, and it already fired

`scripts/checks/open_claim_sweep.py` exists for exactly this. Run here:

- `--selftest`: **positive control 5/5** (each hand-found lock ranks **first**), **negative
  control PASS** (max score on off-corpus text 0.00, floor 6.0). The instrument bites.
- The sweep: **52 open claims with a strongly-matching SETTLED arc.** Of the blocks
  printed, **18 are `docs/OPEN_LEADS.md` rows.**
- **It flags L78 → `B583_chiral_content` at score 36.4**, with `l78` itself among the
  shared terms — the highest-scoring lead row in the file.

> The instrument was not missing, was not broken, and had already named the answer. What
> is missing is anyone acting on its output.

Its reach is also bounded, and honestly: it did **not** flag L53, L72 or L174. Those three
were found by reading. **Sweep and reading are complementary, and neither has been run
against this file recently.**

## 3. What memo 206 actually added, stated against what already existed

`frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py` **already built the E₆ modular data
at k = 1, 2 from first principles** — the same Kac–Peterson sum over the same |W(E₆)| =
51840. Memo 206's stage is therefore an **independent re-derivation of an existing
instrument, not a new one**, and it must be read that way.

The two builds agree exactly. All nine level-2 conformal weights, matched as rationals:

| weight | h | | weight | h |
|---|---|---|---|---|
| 000000 | 0 | | 100000 | 13/21 |
| 000001 | 13/21 | | 100001 | 9/7 |
| 000002 | 4/3 | | 200000 | 4/3 |
| 000010 | 25/21 | | 010000 | 6/7 |
| 001000 | 25/21 | | | |

P2W5-L72 reached 3.4e−41 with high-precision arithmetic; memo 206 reached 5.7e−15 in
float64 from an independent integer Weyl sum. **Two independent builds, one answer.**

So memo 206's genuinely new content is **narrower than its own framing suggested**, and
the honest split is:

| | |
|---|---|
| the E₆ level-2 stage | **a re-derivation.** P2W5-L72 had it. Value: corroboration, not novelty |
| B583 X3's level-2 rank 6 | **a first reproduction.** The arc directory holds `FINDINGS.md`, `READING_RAW.md`, `arc_verdict.json`, `x2r_recompute.py` — none computes X3 — and the lock defines exactly `test_x1_witness_is_banked_b572_value` and `test_x3_mechanism_level1`. **Level 1 only.** Verified by the certificate |
| CELL 2, the a-priori exclusion | **new as a stated fact**, though the mechanism is B583's own |
| CELL 3, the reach law | **new.** Nothing in the corpus computes it |

## 4. What this is and is not

> **INTERPRETIVE.** This is not a discovery about the object. It is a measurement of the
> distance between what the programme's own index says is left and what its arcs have
> already done — and that distance is large enough to have sent this bench up a resolved
> lead in the previous turn.

**What it does not say:** it does not say the other 14 flagged `OPEN_LEADS` rows are
stale. A sweep hit is a **read order**, not a verdict; each needs its arc opened, exactly
as these four did. Nor does it touch any of the four rows' underlying mathematics — L53's
third-order class really does vanish, L174's C1–C4 really are banked, L78's rank really is
6. **The rows are wrong about status, not about content.**

## 5. Filed

**BENCH ERROR #25 (from memo 206) generalises.** Its fix was stated per-lead: *read the
lead's own arcs before naming it open.* That was too narrow. The certificate here shows
two of the four rows could have been caught **without opening any arc**, by reading the
lead file against itself, and a third by running a check the repository already ships.

> **The rule, restated:** before this bench ranks any lead as open, it runs
> `scripts/checks/open_claim_sweep.py` and reads the lead's own row **and** the rows
> adjacent to it. Not a substitute for reading the arcs — a cheaper first pass that
> catches the self-contradictions.
