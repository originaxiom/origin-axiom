# PREREGISTRATION — B1076: the paper-closure campaign, twelve items, none abandoned

**Sealed before the first item is worked.** Ledger: `CAMPAIGN.md`. Lock:
`tests/test_b1076_paper_closure.py`. Gate 5: no physical identification enters the paper body;
this campaign closes *mathematical* debts only.

## Why this exists, stated plainly

Two external referees and one self-audit produced a list of everything the paper cannot
confidently claim. **The failure mode this campaign exists to prevent is not error — it is
drift**: an item is named, agreed to be real, and then quietly not done while attention moves.
The corpus has this defect on record — the standing law-harvest has run **twice in forty-six
reviews**, and R32-9b's 105 candidates have been carried through **six** reviews unopened.

So the list is a **tracked artifact with a lock**, not a message in a transcript.

## BANKED IDENTITY: what is reproduced before any item is read as closed

Every item's closure must reproduce, in its own script, the banked fact it depends on before
reading anything new — the pattern used in B1073/B1074/B1075. An item may not be marked GREEN on
a claim about a computation; only on a computation, with the evidence path recorded in the ledger.

## PRIOR ART: the greps run at design time

`docs/BANKING_PROTOCOL.md` (the 19-row checklist), `WORKING_RULES.md` §0/§2/§10/§12,
`docs/COMPUTE_THE_PROGRAM.md` (the full-relations quantifier instruction and its standing
inventory), Appendix B of `papers/structure_paper/arxiv/main.tex` (blocks (a) and (b)), and the
two referee reports. Established before designing: **block (b) is undeposited**; the terminus
depends on it; and `docs/OPEN_LEADS.md:766` already carries the THEOREM_REGISTRY/LEDGER debt as
**B921-9, OPEN**.

## The twelve items

Listed in `CAMPAIGN.md` with a status column. **Statuses are exactly:** `GREEN` (closed, with an
evidence path), `OPEN` (not yet worked), `BLOCKED` (worked, cannot close, with the reason and what
would unblock it), `WITHDRAWN` (the item was wrong, with why).

**`BLOCKED` and `WITHDRAWN` are legitimate outcomes and are not failures** — an item that cannot
be closed is closed *as a finding*. What is forbidden is an item silently leaving the list.

## Declared outcomes — per item, before any is worked

| result | reading |
|---|---|
| an item computes and the paper's claim strengthens | mark `GREEN`, record the evidence path, and state in the ledger what the paper may now say that it could not before |
| an item computes and **contradicts** the paper | the contradiction is the finding. Correct the paper, mark `GREEN`, and record the correction — as with the rung spectrum, where the referee was right |
| an item cannot be computed with available means | `BLOCKED`, with the obstruction named and what would remove it. **Not** left ambiguous |
| an item turns out to be a non-issue on inspection | `WITHDRAWN`, with the reason — and the reason must be a computation or a citation, never a judgement call |

## Controls against my own known failure modes

1. **No headline may be a printed constant.** Every reported number is bound to a computed
   variable. (E42 — minted as E41 and re-keyed when main took that number the same window; after B1070 printed `{2+1+3} -> {2+1+1}` as its result.)
2. **Every control targets the claim, not its neighbourhood.** Before marking GREEN, state what
   would have to be true *in the world* for the check to fail. If the answer is "nothing outside
   this file", it is documentation, not a check.
3. **Quantifier stated first.** Per `COMPUTE_THE_PROGRAM.md`, each item names which layer of the
   full-relations inventory it covers — member / ends / class / sisters / rows / child / faces /
   axioms / algebra / observer — and its conclusion states no more. Today's A2 result was
   under-quantified twice in ten minutes; that is the error this control exists for.
4. **No absence without search.** "We lack X" is a hypothesis requiring a grep of the code and the
   FINDINGS bodies, not of claim lines.

## The anti-drift mechanism

`tests/test_b1076_paper_closure.py` asserts that the ledger contains **exactly twelve** items,
that every item carries one of the four statuses, and that **every `GREEN` item names an evidence
path that exists on disk**. An item cannot be deleted, renamed away, or marked closed on prose
without the suite noticing.

## Scope

This campaign closes the paper's *verification and definition* debts. It does **not** decide
whether the paper's framing changes, does not touch Gate 5, and does not license any physical
identification in the body. Items 1–3 are the terminus; 4–8 are unverified statements the paper
currently makes; 9–12 are hygiene.
