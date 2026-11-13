# cld-advisor · C15 · B805's two locks, re-scoped to the panel's era, with the drift printed

*Main's card in M22, register row P-239's next action. After C13 and C14. Committed before any work of it. Main gives
the builder the choice between two mends, to be stated with its reason.*

## 1. The question

B805's forcing graph has two locks in `tests/test_b805_forcing.py` that have failed since October: "arcs on no face below
half" and "attachment outnumbers authored". The graph attaches an arc to a face only through B738's kill graph and B842's
reader panel, and neither was extended after the panel's era, so the arcs since then sit on no face while their honest
`depends_on` grow the authored edges. Main's two ways: re-attach the unattached arcs by B842's panel, or re-scope both
locks to the attached era with the drift printed.

## 2. The choice, and its reason

**Re-scope, with the drift printed.** Measured before the card was committed, on the tree of card C16's tip:

| arcs up to | arcs | on no face | half | authored edges inside | attachment edges inside |
|---|---|---|---|---|---|
| B842 (the panel) | 791 | 155 | 395 | 20 | 1,359 |
| B1000 | 941 | 288 | 470 | 662 | 1,403 |
| all (to B1905) | 1,618 | 948 | 809 | 3,506 | 1,451 |

The attachment ends with the panel: of 691 arcs on a face, 52 are after B842, and none after B1349. Up to B842, 20% of
arcs sit on no face, close to the panel's own judgement that about 15% sit on none. **The reason for re-scoping:**
re-attaching about 800 arcs is a classification that B842 made by a sealed panel of readers, sessions that did not write
the arcs; it is not record-keeping, it costs a panel, and a builder's classifier is what sank B806. Re-scoping keeps what
both locks were written to guard (the attached state, and that a citation is not counted a forcing), says plainly where
the attachment stops, and prints the drift, so that the debt stays visible until a panel is run. The re-attachment stays
main's to order, under P-239.

## 3. What is delivered, and what done means

One patch:

| | |
|---|---|
| the instrument | `scripts/forcing/build.py` gains the panel's era (its last arc, B842, read from the arc's folder) and a report of the drift: the arcs after the era, and how many of them sit on no face. Its printed report gives the drift |
| the two locks | each held to the era, under a dated note that keeps the assertion as it stood: in the era, fewer than half of the arcs sit on no face and more than 20 do; in the era, attachment outnumbers authored edges. A third test holds the drift: it is reported, its counts agree, and it is not hidden |
| done | the two locks pass; each fails on a planted case (the era's attachment taken away; a citation counted a forcing); the full test file passes; every gate passes but the count of landings |
| not in it | any attachment of an arc; any change to B842's panel or B738's kill graph |

## 4. How it could come out wrong, written before any run

1. **The era is a choice.** B842 is where the panel's attachment ends; a later cut-off would pass too, and would hide more.
   The cut-off is the panel's own arc, read from the record, not a number fitted to pass.
2. **A re-scoped lock can pass while the record drifts for ever.** So the drift is printed and held by a test that fails
   if it is not reported, and P-239 stays open.
3. **The instrument's other readers** (the gates, the views) may read `gaps()`. Its keys are kept; one is added.

## 5. What it rests on, and what it must not touch

- It rests on main's `0e637ea9e` with the series before it as sent (R80b's parts 3 to 6, C13, C14's first part, C16).
- None of main's tests changed without a dated note; no sealed file; nothing of the owner's quoted.
- It writes to this seat's branch only.

## 6. One control that must fail if the work is broken

With every attachment of the era's arcs taken away, the re-scoped lock on arcs on no face must fail.

## 7. What is needed from main

Nothing to start. Whether a panel is run for the drift is main's (P-239).
