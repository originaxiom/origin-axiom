# Memo 209 — MOST OF THE SWEEP'S HITS ARE HEALTH, NOT DEBT — and memo 208's diagnosis was too broad

**Certificate:** `outside_bench/certificates/the_sweeps_false_positives.py` ·
**Output:** `outside_bench/outputs/the_sweeps_false_positives.txt`
**No seal.** Every claim is a substring test on a tracked file at HEAD.

---

## 0. The question memo 208 left open, and its answer

Memo 208 ended: *"28 of those lie outside `OPEN_LEADS` and were not examined here"* —
framed as a backlog. **They are mostly not a backlog.**

| | of the 28 |
|---|---|
| **genuinely stale** | **2** — `THE_SPINE`'s `B171` and `B1130` |
| correct as written | 1 — `THE_SPINE`'s `B1156`: the arc's own verdict really is OPEN |
| exemplary | 1 — `OPEN_PROBLEMS` gate D |
| tracked-pending | 1 — `GRAND_COMPUTATION_LEDGER` I3 |
| **benign self-citation** | **23**, by classification, fenced below |

## 1. The sweep has a structural false-positive class, and naming it makes it usable

`open_claim_sweep.py` ranks by shared-term IDF: a surface and an arc that share rare terms
score high. **A verdict document scores high against the arc that produced its verdict by
construction.** `LAW_MAP` (7 hits), `THE_SM_VERDICT` (3), `main.tex` (3),
`THE_FRAMEWORK` (2), `PRICED_DOORS` (2), `CROSSING_REQUIREMENTS` (2) — these rows name
their deciders **inside the row**:

> `| **THE MEETING IS A PRODUCT, NOT A FUSION (B698 Leg A, analytic side)** | …`
> `| **MULTIPLICITY/SCALE IS THE OBSERVER'S (B719)** | …`

**A high score there is the healthy state, not the sick one.**

> **The triage rule this yields.** A sweep hit is a true positive only when the surface's
> claim carries an **OPEN / never-run / unresolved** status **and** the arc settles that
> same question. A hit on a document whose job is to *record* the arc's verdict is
> expected. Without this rule the sweep's 52 read as 52 debts; with it, the debts are few
> and findable.

## 2. The two that are genuinely stale

Both on `docs/views/THE_SPINE.md`, which lists arcs with a status token — the same shape
as `OPEN_LEADS`, and the same failure.

| | |
|---|---|
| **B171** `OPEN` (`:211`) | `frontier/B172_combination_gap_resolution/FINDINGS.md:1` — *"the combination gap, resolved (Phase 1)"*, and at `:4` *"**Answers the question B171** opened … affirmatively, hedged"* |
| **B1130** `OPEN` (`:1240`) | `frontier/B1133_c4_single_end/FINDINGS.md:1` — *"the tower is **SINGLE-END**"* … *"the two-ended question **RESOLVED single-end**"* |

B171's decider is hedged and Phase-1, so its row is stale in status, not necessarily
finished as a programme. B1130's is not hedged: the question it states is answered.

## 3. The one that is right, and why it matters

`THE_SPINE` lists **B1156** `OPEN` — and `frontier/B1156_seam_a_gate2/FINDINGS.md` reads
*"Verdict OPEN (seam INDETERMINATE/FLOOR …)"*. **The spine agrees with its arc.** Three
status rows checked on one surface, two wrong and one right: the surface is not uniformly
rotten, which is why the rule in §1 matters more than the count does.

## 4. The write-back loop exists — memo 208 said otherwise, and was wrong

Memo 208 concluded: *"the write-back step has no owner."* **Too broad.**

`docs/OPEN_PROBLEMS.md` gate D states its own scope — *"the non-Hermitian case is open
(L19/L20)"* — and then carries a **dated currency note**:

> *"Currency note, Review 47 (2026-08-20): … a future session **tempted to reuse
> B1085/B1095's code** for this gate must re-derive the non-self-adjoint case fresh — the
> verified numbers do not transfer."*

That is the write-back done right: not just a status, but a warning aimed at the next
reader.

And `docs/HARVEST_LEDGER.md` is a **working write-back loop**. The one stale row this
bench found on `GRAND_COMPUTATION_LEDGER` is **I3**, still reading
*"THE DESIGNED CROSSING, never run"* and *"SPEC'D-READY, off-queue"* — stale against
**this bench's own memo 136**, which found the shot *"NOT FIREABLE, THE LAST LICENSED ROW
LEFT UNSPENT."* The harvest ledger already has it, at `:417`, marked **SCHEDULED**, with a
reason and a deadline: *"no main text names it — the slice D backlog, read before Review
57."*

> **Corrected diagnosis:** the programme **has** a write-back loop, it works, and it tracks
> its own backlog with reasons. **`docs/OPEN_LEADS.md` is outside it.** That is a far more
> actionable statement than "no owner," and it is the one supported by the files.

**Memo 208 is corrected by addendum, not rewritten.** Its count of eleven stale leads
stands; its sentence about ownership does not.

## 5. The fence

**23 of the 28 were classified, not individually verified.** They are placed in the benign
class because their surfaces are verdict/law/paper documents citing their own deciders —
a classification, not a verdict on each row. Any one of them could be a true positive that
the class hid. **Stated here so the number is not later quoted as twenty-three checked
rows.**

Nothing here touches any mathematics. B172's gap label, B1133's single-end arithmetic,
B1156's floor, memo 136's non-fireability — all stand exactly as banked.
