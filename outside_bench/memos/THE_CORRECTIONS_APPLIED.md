# Memo 216 — THE CORRECTIONS APPLIED: fourteen status lines superseded in place, three artifacts regenerated

**Authorization:** the owner, this session — *"do as u recomend"*, against memo 215's
recommendation and the standing ones in memos 208 and 212.
**Where:** branch `claude/outside-bench`, as a **proposal**. **Main is not touched by this
bench.**
**Certificates re-run green after the edits:** `the_seal_already_happened.py`,
`the_triage_was_already_done.py`, `the_artifact_pair_sweep.py`.

---

## 0. The discipline, before the list

**Nothing was deleted.** Every stale sentence is **struck in place** (`~~…~~`) and followed
by a dated supersession that **quotes its decider**. No verdict, no number, no arc, and no
piece of mathematics was changed. Only status text, and only where a cited decider or the
file's **own header** contradicted it.

## 1. `docs/WHAT_WOULD_COUNT.md` §4A.2

| | |
|---|---|
| struck | *"**STATUS: SPEC ONLY, OWNER-PENDING** … what has not happened is the seal."* |
| new | **STATUS: SEALED 2026-08-21 — AWAITING AN EXPERIMENTALIST, NOT A DECISION**, with the ledger line, B1106, the owner's executed D-2/D-3, the spec's own *"Status at landing: SEALED"*, and R6′ the commissioned observable |
| added | the **price of passing**, stated inside the tier so it cannot be read as stronger than it is: memo 197's *one phase in five*, and the slope-specific-not-phase-specific reduction |

## 2. `docs/OPEN_LEADS.md` — 15 supersessions across 13 leads and one campaign cell

| lead | what it said | the decider now quoted beside it |
|---|---|---|
| **L26** | `OPEN — SUSPECTED near-known` | B644 derived the structural content in-repo; residual is a literature check (**partly stale**, written as such) |
| **L53** | `OPEN — first in the queue` | this file's **own primary L53 row** reads `L53 CLOSED.` (B578-D1) |
| **L54** | *"extend to the full torsion-polynomial Galois orbit"* | **executed by B581**; the E₆-principal product is memo 210 |
| **L64** | `OPEN (B572/B573)` | *"the G4 gates **ARE** an exact Fox-calculus recomputation"*; B771/W2-020 CLOSED |
| **L65** | `OPEN (B572)` | B562/P13 — a 9-weight orbit is dimensionally incompatible with a 16 |
| **L68** | `OPEN (queue)` | B578-D3/D4/D5/D6; the single live remainder is L63's Q-C |
| **L72** | `OPEN (B579)` | phases 2–3 **have run**; phase 1 is memo 210; phase 3 walled |
| **L73** | *"find where it first fails"* | **ANSWERED**: level 4, Z₄ = 0 exact |
| **L74** | *"predict and compute … dyadic?"* | the level-4 dyadic prediction **realized** (B600) |
| **L78** | `OPEN — Round 2 first` ★★★★ | *"L78 resolves negative-and-final"*; reproduced and extended in memo 206 |
| **L112** | `OPEN, ready` | this file's **own later L112 row** reads `CLOSED` — 148 lines apart |
| **L173** | `SPEC ONLY … owner-pending` **and** `GATED on the owner` | contradicts **its own header**; sealed 2026-08-21 |
| **L174** | `OPEN — C1 first` ★★★★★ | C1–C4 all `DONE`, **eight lines above** |
| **C5** | `NEEDS-SPECIALIST, honestly fenced` | an arc **titled** *"C5 CLOSED NEGATIVE, harvested"* |

**Structural verification, because a table is easy to break:** line count unchanged
(**2433 → 2433**), **14 changed lines**, and **zero rows with an altered unescaped pipe
count**. A first attempt *did* break it — the strike-through wrapped whole table rows and
doubled their cells — and was caught by that same check and fully reverted before any
commit.

## 3. Three artifact pairs regenerated, from their own committed `compute.py`

| cell | before | after |
|---|---|---|
| `P2W5-L72` | `results.json`: `UNRESOLVED`, `h¹ = {0,0,0,0,0,0}` | **`RESOLVED-A`, `h¹ = {1,1,1,1,1,1}`**, gates consistent |
| `W4-017r` | `results.json`: `PENDING_PART_B`, only key `part_A` | **`RESOLVED-A`**, keys `cell/verdict/reason/part_A/part_B/runtime_s` (474.8 s) |
| `W2-270` | `output.txt`: `UNRESOLVED (=> EXTERNAL)` on *"depth 9-11 … did not complete"* | **`FINAL VERDICT: RESOLVED-B`**, depths 7–11 all completed (860.0 s) |

**W2-270 is the one that settles memo 212's direction question by running rather than
reading:** its JSON was right and its text was stale, and the regenerated text now agrees
with the JSON it contradicted.

> **The corpus-wide census is now `0` of 75** (it was 3). The defect class memo 212
> measured is eliminated on this branch.

## 4. The two certificates that had to change, and why

A certificate that asserts a defect **must fail once the defect is repaired** — and both
did, immediately, which is the behaviour to want. They are converted to **before/after**
form: the pre-fix values are printed as quoted history, the post-fix values are asserted.

- `the_triage_was_already_done.py` — anchors re-pointed at the **struck** forms
  (`~~OPEN (B579)~~`), so the historical text is still verified to be present.
- `the_artifact_pair_sweep.py` — the three cells now assert their corrected state.

## 5. What was NOT done, and why

- **Main is untouched.** All of this is on `claude/outside-bench` for main's seat to take
  or refuse.
- **No lead was closed.** Every annotation supersedes a **status**, never a verdict. L26 is
  written as *partly* stale because that is what its decider supports.
- **No mathematics was revisited.** B581's torsions, B656's clock law, B583's rank, L174's
  C1–C4, B1108's C5 and the three regenerated cells' results all stand exactly as banked.
- **The gate memo 212 recommended is not installed.** Writing `results.json` and
  `output.txt` in one process exit path, and asserting their verdicts match, is a change to
  the cells' own harness — main's call, not this bench's. The check itself already exists
  and runs in under a second.
