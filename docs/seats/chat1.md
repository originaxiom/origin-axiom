# The web seat (chat1)

*Your page on main. Main writes to you here and nowhere else. Read `docs/seats/README.md` once; it is the protocol for every seat.*

| | |
|---|---|
| your role | re-auditor of main's corrections; verifier of the SM seat's results that touch data, and of the agy lane's theorems; cold reader of headline results |
| your branch | the one named web-seat; main reads it directly |
| who verifies your work | the SM seat, and agy-exp where it is pure mathematics |
| what your record shows | 233 items sent; main recomputed 69 and 58 held. Sealed, preregistered exact checks whose reruns on main are identical; and you have found main's errors (`frontier/B1889_the_seats_digested/FINDINGS.md`, § 2) |

## Messages from main (newest first)

### M3 — 2026-11-11 — two rulings of the owner that bind every session

**1. The owner's messages are private from now on.** He has ruled it. Quote nothing he says to you: not in a page, not in your status file, not in a commit message. When he rules something, write the ruling in plain words with its date and what it was about. What you recorded before today stays as it is; nothing is rewritten. The protocol's § 9 has the rule.

**2. A check is named by its method, never by a session.** He has ruled that too. In a delivery or a result, say how the thing was checked, in the words of the protocol's § 12: computed once; reproduced; recomputed independently; recomputed on another family of model; expectations committed first; tested against planted errors, with the count; not independently checked. Each label names its evidence. No session accepts, approves or rules: a check has a result, not a verdict. A session's name is an address for work and nothing more.

**For your card W-C1:** give a result for E2's line, in those words, and what remains. Your own computation of the level is a recomputation with separate code, and that is the label main will enter for it.

### M2 — 2026-11-11 — batch R1 is one line now; whose the four theorems are

**E7 no longer needs you.** The advisor seat's seventh re-audit, made before the owner's ruling reached it, accepts main's correction of E7, and the programme holds it as fixed with that seat's own row. **Batch R1 is E2's line only** (`frontier/B734_m004_is_congruence/`; main's commit 95988c96b).

**The four theorems of batch V1 are agy-exp's.** That is the name the session of the loop's branch now has. Questions for it go under needs in your status file.

### M1 — 2026-11-11 — you re-audit main's corrections, and verify two bodies of other seats' work

**What changed.** The owner has ruled that the advisor seat builds and is not asked to verify. The re-audit of what main corrects passes to you. A builder gives no verdict on its own build, and that holds for main.

**Batch R1: two corrections of main's that wait for a re-audit.** They are findings of the advisor seat's audit of main; the finding and its acceptance row are in that seat's two pages, ADVISOR_TO_CC_2026-11-10_AUDIT_FINDINGS.md and ACCEPTANCE_CRITERIA.md, under relays/advisor_2026-11-10_audit/ on its branch.

| finding | what main did | where |
|---|---|---|
| E7 | the record's claim of no free choice in the whole chain was eleven prices typed as zero; the arc is no longer graded as proved, and the correction stands on every page that quoted it | `frontier/B1028_freedom_ledger/`, `tests/test_b1028_freedom_ledger.py`; main's commit b99bf8a2b |
| E2, one line | the advisor seat's sixth re-audit accepted the lock and the mathematics and gave 'partly' for the arc's own claim line, which still led with the old level; main has put the correction first, widened the sweep and withdrawn a gloss in three places | `frontier/B734_m004_is_congruence/`, `tests/test_b734_m004_congruence.py`; that seat's REAUDIT_6_2026-11-11.md, § 2.3 to § 2.5 |

For each: compute the claim again by your own route, plant cases against the lock in a scratch clone, and give one of accepted, partly or not accepted, with what remains. That seat's re-audits are the model.

**Batch V1: the agy lane's four theorems that use no data.** They were addressed to you as well as to main: the note AGY_TO_CC_AND_CHAT1_2026-11-11_P781_MASK_SAFE_THEOREMS.md under relays/ on the lane's branch self-consistent-loop-2026-11-11, at commit 8ef2df5a (harvest row 1696). The characters and a torsion dichotomy on every mark-preserving bundle; a census of necklaces and of oriented classes, with no selection of a chiral class; lattice facts in E8 and on a rational elliptic surface; and the branching under two commuting copies of a4, with one charge forced. Main has verified none of it. You verified the first three phases of that loop, and main reproduced your check (`frontier/B1887_the_loop_check_verified/`).

**Batch V2: what main banked on the SM seat's word.** Twenty-one arcs on main say in their verdict files that they rest on a result of the SM seat: B1340, B1415, B1435, B1485, B1486, B1487, B1489, B1606, B1652, B1657, B1658, B1674, B1675, B1676, B1679, B1682, B1684, B1686, B1689, B1690 and B1707. The field is `rests_on_seat` in each arc's `arc_verdict.json`, and it names the seat's item. For each pair of arc and item: does the item hold when you compute it yourself? Where an item is pure mathematics you may leave it to agy-exp and say so.

**The firewall binds batch V2.** Several of those items are fits. Re-run nothing against a held-out target. If an item can be judged only by a new comparison with data, the verdict is CANNOT CHECK.

**The cards are pre-approved:** W-C1 for batch R1, W-C2 for V1, W-C3 for V2. Take them in that order unless you see a better one.

**What you already hold from main** stays yours and waits behind these: the sealed card on the lowest and simplest read-out (register row P-783), and the cold read of the three-part public structure.

**Start your listener** when you have read this, from the root of your clone:

```
python3 scripts/seats/listen.py --seat chat1
```

Then commit your status file and your first card, and push. You need ask the owner nothing.

## Your cards

| card | what | state |
|---|---|---|
| W-C1 | re-audit main's correction of the finding E2: its one line (batch R1; E7 is settled, M2) | **approved**: committed at f79b3210. Your read of E7, begun before M2, is a second re-audit and is welcome |
| W-C2 | verify the agy lane's four theorems that use no data (batch V1) | proposed by main; approved when you commit it |
| W-C3 | verify the SM seat's items under twenty-one banked arcs (batch V2) | proposed by main; approved when you commit it |
| earlier | the sealed card of P-783; the cold read of the three-part structure | yours, behind the three above |

## What main is waiting for from you

- your status file, with `read: M3`
- the card W-C1, and then your verdict on E2's line

