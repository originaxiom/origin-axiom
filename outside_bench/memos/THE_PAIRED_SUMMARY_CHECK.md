# THE PAIRED-SUMMARY CHECK — NOT ADOPTED, AND THE CONTROL THAT PASSED WAS EMPTY

**Bench memo 166 · 2026-08-31 · outside bench (lane 1B)**
Seal: `outside_bench/seals/PAIRED_SUMMARY_PREREG.md` (pushed **before** the instrument was written).
Certificate: `outside_bench/certificates/paired_summary_check.py` — **BUILT, NOT ADOPTED.**
Output vendored: `outside_bench/outputs/paired_summary_check_out.txt`.
Gate 5 untouched: this cell reads text and computes document frequencies. No measured value enters.

---

## 0. The verdict, first

**Both arms return `P1-USELESS`. The seal makes P-1 binding and says `P1-USELESS` voids the
instrument. It is voided. NOT ADOPTED.**

| | arm A — the **sealed** substrate | arm B — the **repaired** substrate |
|---|---|---|
| summary half | `arc_verdict.json:claim_one_line` | `claim_one_line` + `FINDINGS.md` |
| cell half | `FINDINGS.md` | the arc's own machine-readable **cell records** |
| positive `B1196` | 3 flags | 74 flags |
| **caught B1220's actual pair?** | **NO** | **NO** |
| negative `B990` | **FIRES (5)** | silent |
| negative `B1202` | **FIRES (12)** | silent |
| negatives *able* to fire? | yes | **NO — zero cell records** |
| selectivity on its own domain | **434 of 1121 arcs (39%)** | **9 of 9 arcs (100%)** |
| verdict | `P1-USELESS` | `P1-USELESS` |

This is the **second** mirror-class detector this bench has built and not adopted. Memo 164 was the
first. The seal anticipated the possibility in as many words — *"taking it twice is cheaper than
shipping a detector that cries wolf"* — and it is being taken.

---

## 1. BENCH ERROR #18 — the seal named the wrong second half, and the way it went wrong is the class

**The error.** Memo 165 recorded the mechanizable form of B1220's finding as:

> *"for every arc compare `frontier/<arc>/arc_verdict.json:claim_one_line` against
> `frontier/<arc>/FINDINGS.md`"*

and the seal carried that forward as the substrate. **B1220 did not compare those two texts.**
Its own words, quoted in memo 165 one paragraph earlier, are:

> *"while its own **cell record GC-27** says …"*

GC-27 lives in `frontier/B1196_close_loop_batch5b/verification/batch5b_cells.json`.

**Why this is not a clerical slip.** `B1196`'s `FINDINGS.md` **repeats the overstatement verbatim** —
*"the sigma and lambda continuous legs sit on the non-normalizable side of the sharp boundary, which
is WHY they are anchors"* — and carries **no** limitation about λ anywhere. So the sealed pairing
could not have caught the instance it was sealed to catch, at any parameter setting, for a reason
present before the first line of code was written.

**And the shape of the error is the class under audit.** I summarised a finding, and my summary
dropped precisely the detail the finding turned on. *That is a paired-summary defect, committed by
this bench, in the memo that proposed the paired-summary detector.* Filed here rather than argued
away, per the standing rule that errors are filed at the point of occurrence.

**The repair is arm B**, and it is not a post-hoc loosening: the direction of the repair was fixed by
B1220's original instance, chosen before this instrument existed and by another seat.

---

## 2. Why arm B's `P1-DISCRIMINATES` was a false pass — a **third** way a control can lie

Run as first written, arm B reported **`P1-DISCRIMINATES`**: the positive flagged, both negatives
stayed silent. That looked like the sealed outcome. It was empty:

> **`B990` and `B1202` have ZERO machine-readable cell records.** They carry no text at all on arm
> B's cell side. **They cannot fire at any setting of any parameter.** Their silence is a property of
> the substrate, not of the detector.

A negative control drawn from outside the instrument's domain is not a control. The certificate now
computes this and refuses the pass (`*** VACUITY:` in the output). Two further guards were added for
the same reason and are reported rather than tuned:

- **pair granularity.** The sealed positive is not "arc `B1196` flags" — it is *the pair B1220 found
  by hand.* Flagging that arc on some other sentence pair is not catching the instance. Arm B's
  top-scoring flag on `B1196` is about `selector-free` / `bit`, **not about λ**.
- **negative capacity.** An instrument that flags **9 of the 9 arcs in its own domain** carries zero
  information, whatever its controls say. No arbitrary "known-faithful" arc had to be picked to
  establish this, which matters: any such pick, made *after* seeing the sweep, would have been fitted.

**This joins two failure modes already on this bench's record, and it is genuinely distinct from
both:**

1. **synthetic positive** (memo 164) — the control passes because the same hand wrote the positive
   and the detector;
2. **vacuous pass** (memo 156, Gate D) — the control passes because the instrument finds *nothing*,
   and "monotone and small" is satisfied by zeros;
3. **substrate-mismatched negative** (here) — the control passes because the *negative* was drawn
   from outside the domain the instrument actually runs on.

All three are the same sentence at different angles: **control passing is not instrument working.**

---

## 3. Why it misses the real pair — computed, not asserted

Both halves of B1220's instance are present in arm B's substrate, and each **passes its own marker
test**:

- summary: *"the sigma and lambda continuous legs sit on the non-normalizable side of the sharp
  boundary, **which is WHY** they are anchors"* → closure marker `which is why`, **no** limitation
  marker (it does not fence itself).
- cell (`batch5b_cells.json:GC-27`): *"**λ fails** even the theorem's first hypothesis (**no (T,G)
  pair has been read off D** for it)"* → two limitation markers.

They fail to pair on **subject binding**. Computed over all 1122 arcs:

> **The two sentences share exactly one content token: `lambda`.**
> **df(`lambda`) = 290 / 1122 arcs = 25.8%.** The declared distinctiveness cutoff was **25%**
> (df_max = 280.5). **The instrument missed its own sealed instance by 9.5 arcs of document
> frequency.**

For contrast, computed in the same pass: df(`sigma`) 26.9%, df(`theorem`) 40.2%, df(`boundary`)
20.9%, df(`anchors`) 15.2%, df(`regime`) 2.6%, df(`non-normalizable`) 0.3%. The rare terms are all on
one side or the other; **the only term the two sentences share is the corpus's most-discussed
object.**

**And loosening does not rescue it — it is measured, both ways:**

| cutoff | real pair caught | flags on `B1196` alone | sweep pairs over 9 arcs |
|---|---|---|---|
| 0.25 (declared) | **NO** | 74 | 746 |
| 0.50 | yes | 144 | 1262 |
| 0.75 | yes | 155 | 1478 |
| 1.00 | yes | 163 | 1587 |

The declared prior in the seal was: *"a handful, not dozens. **If it returns dozens I will suspect
the detector.**"* The setting that catches the instance returns **~140 flags per arc**. The instance
is one of them. That is a highlighter, not a detector, and the prior it was sealed against is the
reason to say so out loud rather than report the catch.

---

## 4. The finding that outlasts the instrument: **the substrate does not exist at scale**

Computed over the frontier:

| | count | share |
|---|---|---|
| arcs with `arc_verdict.json` | **1122** | — |
| arcs with `FINDINGS.md` | **1121** | 99.9% |
| arcs with machine-readable **cell records** | **9** | **0.8%** |

The nine: `B1189 B1190 B1191 B1192 B1194 B1195 B1196 B1199 B1201`. All of them are close-loop batch
arcs from one window. **The corpus stores a per-cell record with its own verdict and its own caveats
for nine arcs out of eleven hundred.**

So even a *working* paired-summary instrument would cover **0.8% of the corpus**, and the 99.2%
remainder is exactly the part where arm A shows the pairing is meaningless — because for those arcs
`FINDINGS.md` **is a second summary, not a source**, written by the same hand at the same sitting.
Arm A flagging **39% of arcs** is not noise to be tuned away; it is what happens when you compare two
summaries of the same thing and call one of them the evidence.

**This is the constructive half, and it is a different statement from memo 164's.** Memo 164
concluded the mirror class needs *route-level records* and named `docs/OPEN_LEADS.md` /
`docs/OPEN_PROBLEMS.md` as the nearest existing thing. This cell adds: the *other* substrate that
would work — a cell-level record carrying its own verdict and its own caveats, which B1220 used and
which is genuinely load-bearing — **exists for nine arcs.** Mechanising the paired-summary check is
therefore not an instrument problem. It is a **records** problem: it becomes possible exactly when
arcs bank per-cell verdicts as data rather than as prose.

That is offered, **not pressed**, and it is not this seat's call: this bench does not edit main, and
telling another seat to change its banking format on the strength of a detector that did not work
would be exactly the overreach the record keeps catching.

---

## 5. What stands, unchanged

- **B1220's finding stands**, on its own evidence. It was found **by reading**, by a seat that read
  both texts. The failure of two successive detectors to mechanise it says nothing against it — and
  it is worth saying that plainly, because a memo reporting a failed detector can be misread as
  doubting the instance.
- **B1196's addendum stands.** The overstating verdict line and the note sit together, per the house
  rule for corrected inputs that keep counting; nothing here edits either.
- **Memo 164's verdict stands** and its instrument remains NOT ADOPTED.
- **The mirror class remains named and uninstrumented**, now after two designs on two substrates.
  Memo 163's coverage statement is unchanged: three instruments hunt *something settled, asserted
  open*; **nothing hunts the mirror.**

---

## 6. Fences

- **No flags are reported as findings.** P-2 was not run on either arm, because the seal makes P-1
  binding and P-1 failed on both. The 434 arcs arm A would have flagged and the 746 pairs arm B would
  have flagged are **not claims about any arc** and must not be quoted as such by a later seat.
- This memo does **not** claim the mirror class is rare, or common. It claims two named designs did
  not detect it.
- The parameter table in §3 is **diagnosis, not tuning**: no threshold in the committed certificate
  was changed on the strength of it, and the certificate still runs at the declared 0.25.
- **Pre-bank checks run** (memo 154's rule — the corpus's own instruments before a bespoke one, and
  memo 159's — the linter before banking): `outside_bench/certificates/state_claim_linter.py` →
  **L2-CLEAN, 0 flagged**; `scripts/checks/check_path_references.py` → **2695 citations, all
  resolve**; `scripts/checks/check_test_vacuity.py` → **0 NO-ASSERT, 0 TAUTOLOGY**.
- **The one state claim here is memo 163's, restated, not new** (*nothing hunts the mirror*), and per
  memo 153 the terms are stated with it: `already_banked.py "paired summary overstates cell record
  detector mirror class"` returns no settled arc above 4 of 7 terms, and no arc claiming a
  paired-summary or mirror-class detector.
- Gate 5 untouched. No measured Standard-Model value entered any computation here.

---

## 7. What this means for the Standard Model

**Nothing.** No value moves, no structure moves, no ledger row moves. This is a records-hygiene cell
about how this programme's own summaries relate to its own evidence. It is filed because a document
meant for outsiders is read through its summaries, and because the one instance the corpus has of a
summary overstating its cell was found by hand and remains, after two attempts, findable only by
hand.
