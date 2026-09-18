# B1426 — A SEAT ASKED TO BE REGISTERED AND NOTHING WAS WATCHING: two lanes outside the gate, one of them holding the results an outside review says the paper drops

cc, 2026-09-18. Owner-raised, in anger, and correctly: *"i warned you about this days ago you said its all right."*
**Verdict: PROVED. Two lanes carried work that no gate on main watched. One of them sent a relay on 2026-09-16
proposing its own seat-register row, and that relay was never rowed. The other holds the outside review the paper
is currently being revised against. Both are registered here, and the survey that finds them is now a script.**

## 1. WHAT THE OWNER WAS TOLD, AND WHY IT WAS WRONG

On 2026-09-17 a completeness sweep reported that the paper reflected the state of the programme. It was run over
**main**. Two lanes were never in its field of view, because nothing enumerates lanes: `harvest_debt.py` walks a
hard-coded list of nine seats, and a branch absent from that list is not unread, it is **invisible**. No amount of
attention finds it. That is the difference this arc is about.

## 2. THE SEAT THAT ASKED TO BE REGISTERED

`origin/sep16-branch`, **60 commits unique to it**, arcs **xB001–xB024**, each with a preregistration sealed and
pushed *before* its `verification/` directory existed. On **2026-09-16** it sent
`XB_TO_CC_2026-09-16_SEAT_OPENED_AND_TWO_DEBTS_PAID.md`, which contains a filled-in table headed *"Seat registration
(proposed row for `docs/SEAT_REGISTER.md`)"* and says, of the numbering problem it was solving:

> the fix must be checkable by a gate, not by attention.

**It was not rowed, not registered, and not watched, for two days** — by attention, exactly as its own sentence
predicted. Among its arcs is xB021, verdict PROVED, which computes that the three bits act on `CS ∈ ℝ/½ℤ`, that
the group they generate has order 4, that the **stabiliser of the object's value is exactly the two bits the paper
calls withheld and relational**, and that orbit × stabiliser closes as 4 = 2 × 2 — with a binding kill condition
declared in the seal, which did not fire, and its three misses named.

## 3. THE REFEREE'S OWN LANE WAS ALSO UNWATCHED

`<remote>/paper-review-verification-kaz3f5`, **13 commits unique**, holding the round-1, round-2 and round-3
referee reports — including the round-3 report dated today, which is the one arguing that the paper is a lossy
projection of its project. The lane the paper is being revised against was itself outside the gate. Its two mirrors
also disagree: origin is **7 commits ahead** of codeberg, and for `sep16-branch` origin is **16 ahead**.

## 4. THE LANES THAT *WERE* WATCHED WERE NOT BURIED — THEY WERE REPORTED AND UNREAD

This distinction is the actionable half. Run with `--fetch`, the harvest gate says plainly:

| seat | head vs pin | unrowed items |
|---|---|---|
| sm | +17 commits | 11, including `THE_VERDICT_OF_THE_OBJECT_2026-09-16` and sm:B1366–B1375 |
| audit | +5 commits | 4, plus one relay with no ledger row |

Those items are **two days old**, and the gate passes because its failure threshold is 21 days. So the sm lane's
B1374/B1375 — the tower's generation count — were never hidden: they were listed, dated, and unread, and the gate
that listed them printed PASS above the list. **A gate that reports a debt and passes is read as a gate that found
nothing.** That is the same defect as B1425 §8, where a receipt recorded a failure nobody opened.

## 5. AND THE OUTSIDE READER'S STRUCTURAL CLAIM IS FALSE, MEASURED

An outside report described main as a **101-commit** curated line with four lanes of ~3000 commits each, *"two of
which share no history with main at all."* Measured by `verification/lane_survey.py`:

- main is **3 457** commits, identical on both mirrors, no shallow marker, no grafts;
- **all ten same-repository lanes share main's root commit and have a merge base with it** — none is a separate
  programme;
- their "~3000" figures are each lane's **total including main's own history**; the unique work is 110, 92, 165,
  60 and 13 commits;
- exactly one lane genuinely shares no history, and it is not one of the four named: the hostile-review seat, which
  lives in a **different repository** (`github.com/originaxiom/golden_gate`), where unrelated history is expected.

101 commits back on main reaches 2026-09-14. The reader was looking at four days through a depth-limited clone.
B1425 §6 fixes what let that go unnoticed on our side.

## 6. WHAT IS FIXED HERE

Both lanes added to `harvest_debt.py`'s seat list with their item grammars, pinned in `docs/HARVEST_LEDGER.md`
(sep16 at its **merge base**, so the entire lane reads as debt; review at main's head), rowed in
`docs/SEAT_REGISTER.md`, and the seat-opening relay rowed in `docs/RELAY_LEDGER.md`. The gate now enumerates all
24 xB arcs as backlog. And the survey is a **script**, not a habit: `lane_survey.py` walks every remote-tracking
ref and reports any lane with unique work that the gate does not list. It printed two; it now prints none.

**What is NOT fixed, and is the real work:** reading them. Registration makes debt visible; it does not pay it.
The sm lane's B1374/B1375 and the sep16 lane's xB021 are verified-by-their-own-seat and unverified here.

## Locks
`tests/test_b1426_every_lane_is_watched.py`: the survey reports no unwatched lane; both new seats are in the gate's
list, in the pin table and in the seat register; the seat-opening relay has a ledger row.
