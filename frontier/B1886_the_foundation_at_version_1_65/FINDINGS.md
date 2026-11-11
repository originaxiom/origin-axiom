# B1886 — The foundation at version 1.65: the owner's statements of two days, entered under the rule that a ruling is not a fact

*Main, 2026-11-11 (S306p). This is the second landing of P-767: the owner's statements of 2026-11-10 and 2026-11-11
carried into `GENESIS.md`. It was held until two things were in hand: the computation the owner asked for before
deciding on the tick (B1879), and the working rule of 2026-11-11, by which a ruling sets a goal, a standard, an order
of work or a meaning, and never a fact (P-780). It changes wording and adds three items. It computes nothing.
0 of 19.*

## 1. The answer first

- **No status cell of an existing item changes.** Every older row of the foundation has the status it had at v1.64;
  the lock compares them all with the committed v1.64.
- **Three items are new:** the claim (PF5, OPEN), the ground (SE3, POSTULATED as main's entry), and a fork on the
  observer's place (FK16, OPEN).
- **One sentence is re-typed:** "even ticks observed" is no longer recorded as the owner's ruling. It is a condition
  that the weight has to deliver.
- **The input budget grows by one:** the ground is counted as an axiom. Nothing leaves the budget.

## 2. What changed, item by item

| where | at v1.64 | at v1.65 |
|---|---|---|
| the header, on which document holds | "this file holds" | scoped: this file holds on the status of every item; the goal, the ceiling and the rules are the governing document's (closes the audit's finding X2) |
| § 0, statuses | five statuses | the same five, and who sets one: no status is set by a ruling on a fact. What the mathematics could decide is OPEN with both branches carried; what nothing can decide is main's entry, tagged and counted |
| § 1, the principle | three faces | the same three, and the owner's statements of what he means, as wording: nothing is picked next; nothing is ranked; the account is the whole ledger; the law says what takes part and does not weigh; closing means the whole agrees with itself |
| § 1, **PF5, the claim** | not an item | **OPEN.** The whole has one self-consistent outcome, one orbit of the whole. It is what the programme sets out to establish; nothing is derived from it. What would refute it is in the falsifier register |
| § 2, GM5c, the swap | OPEN; "even ticks observed" recorded as the owner's ruling | OPEN. The tick is carried as an act, and both branches are still carried. "Even ticks observed" is a condition the weight has to deliver, with a criterion for delivering it that is necessary and not shown sufficient |
| § 4, SE2, the orientation | CHOSEN | CHOSEN, and named as a condition to derive. Not derived, and not counted as derived |
| § 4, **SE3, the ground** | not an item | **POSTULATED, main's entry.** The ground is the act itself, the tick; its level is the prime its discriminant is, 5; which reading gives the level is part of the postulate |
| § 8, FK2, FK3, FK9 | as they were | each takes a pointer |
| § 8, **FK16** | not an item | **OPEN.** If the outcome is a pair that the mirror exchanges, what puts an observer at one member |
| § 7 | — | none of this brings a value |

## 3. Why three things are typed as they are

- **The claim is OPEN and not POSTULATED.** It is not an assumption that anything rests on. Whether the whole has one
  self-consistent outcome is for the mathematics to decide, and the rule of 2026-11-11 then asks that both branches be
  carried. An earlier plan of main's had it as a postulate; that would have let later work lean on it.
- **The ground is POSTULATED, and as main's entry.** The owner chose it from a menu that main had put to him. The rule
  no longer admits that as a ruling. Nothing computed can decide it: it is a definition. So main enters it, tags it,
  and counts it.
- **"Even ticks observed" is not struck.** It stands in the text as the sentence of v1.33, with its new type beside
  it. Whether it is true is what the weight is asked.

## 4. What moved with it

| | before | after |
|---|---|---|
| the closure map | — | three nodes: the ground, the claim, the observer's place; the swap's and the orientation's nodes re-worded, with two more checked quotes each |
| the programme's packages | — | the ground under the root and selection; the claim under the law and the weight; the observer's place under the swap and the hand |
| the input budget | 38 inputs, 46 items | 39 inputs, 47 items: one more axiom, the ground |
| the falsifier register | eight physics-facing predictions | the programme's own claim added, with what would refute it and how sharp that is |

The numbers above are of this landing. The live ones are on the status page (`frontier/B1883_where_we_stand/`).

## 5. What it does not do

- **It derives nothing and earns no value.**
- **It does not adopt the first instance of a read-out on the whole,** which exists on a seat's branch. That is
  judged against the eight acceptance conditions, under P-776 and P-781.
- **It does not tag the five untagged suppositions** that the advisor seat's sort names (flat counts only; positivity;
  the pull-back on the records; the ladder's rungs; the line's order as the unification pattern). Each needs its own
  read of what was built on it. That stays owed under P-780.
- **It does not finish P-767.** Left: the typed graph and the count computed from each value's ancestry (the owner's
  statements on the count, the headline and the map on the desk), which is package WP-0.12.

## Seen first

- **The repo sweep:** GENESIS itself is the record here. Its v1.33 holds the sentence on even ticks; its FK12 (iv)
  already types the law as "a hypothesis to test, not a premise", so the law is not entered again as an item; its
  FK15 already uses the number PF4 for a candidate fourth face, so the claim is PF5. The falsifier register held no
  entry for the programme's own claim (the audit's finding M10 names that kind of gap).
- **The literature:** none applies.

## Disclosed

- **Main's first draft of this version, made before the rule of 2026-11-11, had the claim as a postulate and two new
  items for the law.** Both were wrong for the reasons in § 3 and in "Seen first", and neither was committed.
- **Main first gave the claim the number PF4,** which the foundation already uses. Found before the commit, by
  counting the identifier's occurrences.
- **Four of the statements entered here came from menus main put to the owner with a recommendation.** The rule forbids
  that now. They are typed here by what they are, and not as his rulings on fact.
- **The advisor seat offered to check the foundation's next version when it lands.** This is that version, and it has
  not been read by any other seat.

## Reproduce

```
python3 -m pytest -q frontier/B1886_the_foundation_at_version_1_65/verification/
python3 scripts/gates/gates.py genesis-cited closure-generated
```
