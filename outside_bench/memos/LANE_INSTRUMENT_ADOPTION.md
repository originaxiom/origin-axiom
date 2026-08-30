# MEMO 154 — THE CORPUS'S OWN INSTRUMENTS, TURNED ON THIS LANE

**Banked 2026-08-30.** Seal `seals/LANE_INSTRUMENT_ADOPTION_PREREG.md`, pushed before any run.
Output vendored: `outputs/lane_instrument_adoption_out.txt`. Run at lane HEAD `e7d9562a`, clean tree.

Memo 153 found the corpus had built the instrument this bench needed and that this bench had never
run it. **That was one instrument. `scripts/checks/` carries twelve.**

---

## 0. OUTCOMES

| cell | outcome |
|---|---|
| **F1** — path references | **F1-BROKEN → REPAIRED.** 12 unresolved, **all 12 in this lane**; now 0 |
| **F2** — document currency | **the instrument cannot see this lane at all** |
| **F3** — retraction sweep | **F3-CLEAN.** 2649 files, 9 retracted phrases, **0 violations** |
| **F4** — adoption | **F4-GAPS.** 11 of 12 have been on this branch the whole time; the lane used **none** |

---

## 1. F1 — TWELVE DEAD CITATIONS, ALL OURS, AND THE REASON IS STRUCTURAL

`check_path_references.py` checked **2491** backticked repo-paths across the tree. **12 did not
resolve. Every one was in `outside_bench/`.** The rest of the repo was clean.

The cause is not typos. **This branch is 94 commits behind `main`**, and all five distinct dead
targets are main-side artifacts that exist at the pin and simply are not on this branch:

| target | on branch | at pin `89affd5b` |
|---|---|---|
| `89affd5b:scripts/checks/already_banked.py` | no | yes |
| `89affd5b:docs/SPECIALIST_SEND_QUEUE.md` | no | yes |
| `89affd5b:docs/GRAND_COMPUTATION_v0.md` | no | yes |
| `89affd5b:frontier/B1184_quine_synthesis/FINDINGS.md` | no | yes |
| `89affd5b:docs/COSMOLOGY_LEDGER.md` | no | yes |

**Why this is a real defect and not a nit.** A reader who checks out `claude/outside-bench` — which
is what "go read the bench's work" means — and follows a citation hits nothing. Memo 153 is the
sharpest case: it tells a reader to run `already_banked.py`, **and that file does not exist on the
branch the memo lives on.** It ran here only because the certificate materialized it from the pin.
That is the same evidence-contract family as the floating refs and the uncommitted probe: *the
claim is true, and the reader cannot get to it.*

**REPAIRED, and by the lane's own convention.** `_oa_source.py` reads main as `git show REF:path` at
a pinned SHA. The citations now do the same — `89affd5b:docs/…` — which is both resolvable in
principle and *honest*, because it says out loud that the file is on main and not here. Eleven
citations across seven documents rewritten; re-run: **2479 checked, all resolve.**

> **Scope of the edit, stated because the lane is addendum-only.** This changed *citation form*, not
> a single claim. No sentence's meaning moved. Addendum-only governs claims; a citation that names
> the wrong location is simply wrong and is corrected in place.

---

## 2. F2 — THE CURRENCY INSTRUMENT STRUCTURALLY CANNOT SEE THIS LANE

`doc_currency.py` exists precisely to catch *"a document that was true when written and was never
updated as the corpus moved past it"* — the failure memo 153 spent a whole cell finding **by hand**.

It runs clean here, and the reason is the finding:

> **Its `LIVING` registry holds 18 documents. Zero are in `outside_bench/`.**
> **This lane has 40 standing documents and 118 memos — 158 files, none registered.**

Its four flagged debts (`CLAIMS.md`, `docs/GUT_REQUIREMENTS_LEDGER.md`, `docs/THEOREM_LEDGER.md`,
`docs/TOOLBOX.md`) are all main-side. **This lane's documents were never in scope, so the checker
could never have caught `THE_TOE_GAP.md` contradicting its own addendum, or `THE_FULL_ACCOUNTING.md`
carrying two items closed before it was written.** Memo 153 did by hand what an existing instrument
would have done automatically, had anyone registered the lane.

**This is not a defect in the instrument.** Registering documents is the citing lane's job, and this
lane never did it. **Relayed to cc** (§5), because `scripts/checks/doc_currency.py` is a main-side
file and this seat does not edit main.

---

## 3. F3 — CLEAN, AND REPORTED AS A RESULT

`retraction_sweep.py`: **9 registered retracted phrases, 2649 tracked `.md` files swept, 0
live-claim violations.**

The seal bound this in advance: *a clean result is a result, and manufacturing a finding to justify
the cell is the failure it exists to avoid.* **This lane quotes no retracted claim as live.** Given
how heavily these memos quote arcs — memo 149 alone traced 50 claims across 1119 records — that is
worth having measured rather than assumed. It is the one cell of the four that came back with
nothing wrong, and it is the one whose failure would have mattered most: a retracted result quoted
as live is how a wrong answer re-enters a record that had already removed it.

---

## 4. F4 — ELEVEN OF TWELVE WERE HERE ALL ALONG

| available on this branch | used by this lane before today |
|---|---|
| `audit_sample` · `check_path_references` · `check_test_vacuity` · `derive_lexicon` · `doc_currency` · `fleiss_kappa` · `forcedness_census` · `instrument_freshness` · `relay_debt` · `representation_sweep` · `retraction_sweep` — **11** | **0** |
| `already_banked` — **absent** (it postdates the branch point) | n/a |

**So the gap is unadopted, not unrunnable** — F4-GAPS, exactly the outcome the seal said would be
unacceptable. Only `already_banked` has a structural excuse.

**And the sting:** memo 142 built a bespoke lane self-audit — 112 certificate/output pairs re-run by
hand — while `instrument_freshness.py`, written for precisely that failure (*"re-run every arc
instrument and report the ones whose committed `results.json` is a LIE"*), sat unused on the same
branch. The lane has repeatedly built by hand what it already had.

---

## 5. WHAT THIS CHANGES, AND WHAT IS RELAYED

**Adopted here, added to the lane's practice alongside memo 153's rule:**

> **Before banking any cell, run the corpus's own applicable checks — path references, retraction
> sweep, and `already_banked` on every MISSING claim with the terms stated. Build a bespoke
> instrument only after establishing that no `scripts/checks/` instrument covers the case.**

**Relayed to cc (main-side, not this seat's to edit):**
1. **Register this lane's standing documents in `89affd5b:scripts/checks/doc_currency.py`'s `LIVING`
   registry**, with a declared tolerance. Without it the lane is permanently invisible to the
   programme's currency gate, and memo 153's findings will recur.
2. **Consider whether the 94-commit branch lag should be closed.** This seat did not merge `main`
   — that is a change to the lane's shape and belongs to the owner — but the lag is what made the
   twelve citations dead, and it will keep producing them.

## 6. FENCES

- F1's repair changed citation form only; no claim moved.
- F2 is a statement about **coverage**, not about the instrument's correctness.
- F3's clean result covers the **registered** retracted phrases (9). A claim retracted without being
  registered would not be caught, and that limit belongs to the instrument, not to this run.
- The run is a snapshot at lane HEAD `e7d9562a` with a clean tree, stated so it is reproducible.
