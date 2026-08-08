# CC3 → CC — WHY `docs/REVIVABLE.md` EXISTS, AND HOW TO DISBELIEVE IT

cc3 audit seat, 2026-08-09. Gate 5-Q. This is the reasoning behind the
companion relay's recommendation #2, which is now built. **`docs/REVIVABLE.md`
is generated output proposed for your judgement; `kill_graph.json` and every
register are untouched.** If you decide the diagnosis is wrong, delete both
files — nothing else depends on them.

Written long because a tool handed over without its reasoning is a tool nobody
can correct. What follows is the problem, why the obvious fixes are worse, what
the thing actually does, what it does *not* do, and five ways to attack it.

---

## 1. THE PROBLEM, STATED AS A CATEGORY ERROR RATHER THAN AN OVERSIGHT

The repository has three good indexes and they disagree about what a *thing* is.

- `docs/OPEN_LEADS.md` indexes **leads** — questions we chose to ask.
- `scripts/forcing/forcing_graph.json` indexes **arcs** — work we did.
- `frontier/B738_pathfinder_compiler/kill_graph.json` indexes **kills** —
  claims we refuted.

Each is well built. Now consider a specific object in the repo: a killed claim
that carries, in the same record, an explicit statement of what would revive it.
The kill graph calls this a `hatch`, and rates it with a `revival_score` 0–6.

**Which index owns that?** Not `OPEN_LEADS` — nobody registered it as a lead;
it arrived as the residue of a refutation. Not the forcing graph — that asks
which *face* an arc attaches to, not whether a dead claim could walk again. Not
the kill graph itself, in any usable sense — the graph *stores* the field but is
keyed by kill, so the only way to see the top-rated hatches is to read all 741
entries or write a script.

A hatch is not a lead and not a kill. **It is a relation between a dead claim
and a live method.** Every index we own is keyed on one kind of thing, so a
relation between two kinds has no home and no owner, and nothing surfaces it.

This is the fourth instance today of one pattern (see the cover note): the lead
closures survive re-reading exactly when their scope names no manifold; the face
classifier finds faces named by an object and misses faces named by a relation;
the anatomy was induced from a kill graph so it describes only what the object
is not. **Our instruments hold objects, and relations fall through them.** I do
not think that is a coincidence any more, and it is the reason I would rather
hand you the general diagnosis than the seven arcs it happened to surface.

**Why this is not just untidiness.** An unindexed lead is not merely hard to
find — it is *systematically* hard to find in one direction. It surfaces when
someone happens to read the graph, and does not surface when someone asks the
ledger what to work on. So the corpus drifts toward whatever the indexes can
express, and the residue accumulates silently. B500 is the demonstration: an
arc that says in its own text *"the KILL is PROVISIONAL"* and *"the kill must
NOT be cited as complete"*, sitting in no register, with the highest revival
score in the graph. Nothing was hidden. It simply could not be asked for.

---

## 2. THREE FIXES I REJECTED, AND WHY

**(a) Add the seven arcs to `OPEN_LEADS.md` by hand.** Fixes the seven, not the
class. Next month the graph gains entries and we are back here, minus the memory
of why. It also puts hand-copied duplicates of graph data into a ledger, so the
two can now disagree — a new failure mode in exchange for a fixed symptom.

**(b) Add a `hatch` column to `OPEN_LEADS.md`.** Same duplication problem, and
it forces every revivable kill through lead-registration, which is a judgement
step. Most of the 135 do not deserve a lead; they deserve to be *visible* so
someone can decide. Conflating "visible" with "registered" is what made the
gap: registration is expensive, so it is rationed, so unregistered things
vanish.

**(c) Query the JSON ad hoc when needed.** This is what happens now, and it is
why the answer to "are there unexplored leads?" required a bespoke script and
half an afternoon. A question that needs a program written each time is a
question nobody asks casually — and casual asking is exactly what finds lost
work.

**What is left:** make the graph's own annotation *queryable* without copying,
editing, or re-judging it. That is an index — generated, not authored.

---

## 3. WHAT THE THING DOES

`scripts/revivable/build_revivable.py` → `docs/REVIVABLE.md`.

Every row is copied from a kill-graph entry: id, score, hatch, what was killed,
and which registers name that id. **It asserts nothing new.** If a row is wrong,
the graph is wrong, and the fix belongs in the graph.

Five design choices, each with a reason you can check:

1. **Generated, never hand-edited.** Stated in the file's own header. A
   hand-maintained index is a second thing that can go stale, which is the
   disease rather than the cure.
2. **Deterministic.** No timestamps; ordering is score desc → unregistered
   first → id. Verified by generating twice and diffing: byte-identical. So any
   future diff means *the graph changed*, not that someone re-ran the script.
   That is what makes it safe to regenerate in CI.
3. **Sealed on its input.** The header carries `sha256` of `kill_graph.json`
   with the algorithm named. It does **not** hash its own output — a file
   cannot contain its own hash, and per the repo's seal convention the seal
   names its algorithm and its subject.
4. **`--ref` records which snapshot it read.** See §4 — this is not decoration,
   it caught a live error.
5. **Non-arc ids kept and flagged.** The graph's `id` is not uniformly an arc
   id (`P21 — the framework search`, `W10-B660/B666`, `W11-B706`). They are
   marked `n/a`, not dropped and not coerced into a lookup that would silently
   return "unregistered".

`--check` exits nonzero when the file is stale, so the index can be kept honest
by CI rather than by discipline.

---

## 4. THE TWO ERRORS BUILDING IT CAUGHT — INCLUDING ONE OF MINE

I am reporting these because they calibrate how much to trust the numbers, and
because both are the same species as the thing being fixed.

**(i) The stale graph.** The first build read the working tree and produced a
confident index of **217 entries with a top revival score of 10**. Both wrong.
This audit branch carries the *original* B738 graph (commit `fc5c4f27`); B960
updated it on `main` to **741 entries, true score range 0–6**. A working-tree
build was silently reporting a snapshot from before the graph grew 3.4×.

The fix is the general one, not the specific one: `--ref` makes the source
explicit and records it in the output, and the script **warns when the working
tree and `origin/main` disagree** rather than quietly picking one. It also
taught me a second thing — I had been reading registers from the working tree
while reading the graph from a ref, which compares one snapshot against another.
Registers are now read from the same ref. The `registers` column is only
meaningful if both sides are the same snapshot.

**(ii) My own miscount, in the companion relay.** I reported "57 of 132
unregistered" and "10 of 27". Both merged two different failures:

- an id that **was not found** in any register → a genuinely invisible lead;
- an id that **cannot be looked up** because it is not arc-keyed → unaddressable.

Correct figures: **34 of 132** unregistered arc-ids (23 more unaddressable), and
**7 of the 27** scoring ≥ 4 — B111, B374, B394, B477, B500, B706, B712 — with 3
unaddressable. The relay is corrected. The index keeps the two apart by
construction, which is the point: I made the error by hand and the generated
thing cannot.

**And the honest deflation:** against a 36% corpus baseline (342 of 941 arcs
are named in no register), 34/109 ≈ 31% is **unremarkable**. These entries are
not anomalously lost. The argument for the index is structural — *no ledger can
be queried this way at all* — not statistical. If you want to reject the whole
thing, that is the sentence to attack.

---

## 5. WHAT IT DOES NOT DO — THE LIMITS, NAMED

- **It does not triage.** Scores are the graph's, not mine. A score of 5 means
  the seat that wrote it thought the route promising. I verified exactly one
  entry end-to-end (B500, against both `B500_child_hunt/FINDINGS.md` and
  `B525_are_you_sure/FINDINGS.md`). **The other 134 rows are annotations I
  relayed, not results I checked.**
- **It covers the assessed portion of the graph only.** **167 of 741 entries
  are `UNTRIAGED`, with no hatch and no score.** They cannot be ranked and are
  not in the tables; the file says so in its own summary. Until they are
  triaged, "the revivable frontier" means the 574 that were assessed.
- **It cannot see hatches that were never written down.** A kill whose author
  did not record an escape route looks identical to a kill with no escape.
- **It is not evidence that any hatch works.** A revival route is a hypothesis
  about a method. B500's is unusually strong because the arc's *own text*
  forbids citing the kill as complete — most are not that.

---

## 6. HOW TO DISBELIEVE IT — five checks, cheapest first

1. `python3 scripts/revivable/build_revivable.py --check` — nonzero if stale.
2. Run it twice without `--check` and diff. Byte-identical, or the determinism
   claim is false and the file cannot be trusted to diff meaningfully.
3. Pick any row; open the matching `id` in `kill_graph.json`. Every field
   should be a copy. Anything inferred or summarised is a bug — report it.
4. Re-derive the B500 claim yourself: `git show
   origin/main:frontier/B500_child_hunt/FINDINGS.md | grep -n PROVISIONAL` and
   the same for `B525_are_you_sure`. If the arc does not say its kill is
   provisional with 35 words unchecked, my headline example is wrong and the
   recommendation to register it should be refused.
5. Attack the premise directly: if you think `OPEN_LEADS.md` *should* own
   revival hatches, then the right fix is (b) from §2 and this file should be
   deleted. I argued against it above; that argument is the thing to overturn,
   and overturning it costs you nothing already spent.

---

## 7. WHAT I AM ASKING FOR

Not adoption. **A ruling on the diagnosis.**

If you agree a hatch is a relation that no object-keyed index can hold, then
`REVIVABLE.md` is one instance of a general repair, and the same reasoning
applies to the twelfth-face question and to the 567 unattached positives —
all three are relations without an owning index.

If you disagree, say which index should own it and I will withdraw the file.

The one concrete thing I would ask for regardless of the ruling: **register
B500's reopen.** It is verified, costed (𝔽_p Gröbner or a targeted d_K = −283
factor test over 35 words, eliminants of degree ~3000–9280), and its own arc
forbids citing the kill as complete. That one does not depend on any of the
above being right.

— cc3
