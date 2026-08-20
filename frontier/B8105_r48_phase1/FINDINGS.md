# B8105 — R48 PHASE 1 (mechanical): the theorem registry has been violating its own standing rule for 179 arcs

**Date:** 2026-08-20 · **Seat:** cc3 (audit) · **R48, run COLD at the owner's word.** Phase 1 of the
full-corpus decadal review. Gate 5 untouched.

## THE MODULUS — declared up front, as cc declared theirs

**I am cold on cc's arcs B1074–B1099: I had no hand in them.** I am **NOT** cold on the last two
days — **I flagged B1085, I flagged B1098-vs-B959, I proposed the `seal-digests` gate, and my arcs
were harvested into B1092–B1094.** A review of this window is **partly me reviewing changes I
caused**. That ceiling is smaller than a self-review's and it is real. **Declared, not discovered.**

## TWO METHOD CORRECTIONS, both of which would have invalidated the review

1. **My working tree is not the corpus.** This branch's main-band tip is **B1067**; `origin/main` is
   at **B1099**. cc3 does not merge, so 32 of cc's arcs are absent here. **R48 runs against
   `origin/main`**, and a review run against the working tree would have silently missed them.
2. **The directive needs scoping or it manufactures thousands of false positives.** *"No single md
   document is outdated"* cannot mean the 1985 arc `FINDINGS.md` files — **those are historical
   records and should be frozen.** The directive targets **synthesis surfaces**: `docs/` (112) +
   root (14) = **126 documents.**

## The currency spine

Of **126 synthesis surfaces**, **57** have their highest main-band reference below **B1000**.
Splitting by whether the document is a **dated snapshot** (legitimately frozen) or an **undated live
surface**:

- **21 dated snapshots** — `AUDIT_2026-07-05`, `CLOSURE_2026-07-11`, `PROGRESS_2026-Q2`, … **not
  defects.**
- **36 undated live surfaces** lagging ≥100 arcs. Worst: `ARCHITECTURE.md` and the four
  `docs/atlas/*` documents at **lag 975** (highest reference **B124**); `AUDIT_REPORT.md` 946;
  `METHOD.md` 874; `STRATEGIC_SYNTHESIS.md` 866.

**CAVEAT, and it bounds every row above: lag is a CANDIDATE-GENERATOR, not a verdict.** A glossary
need not cite B1099. **Only verified rows below are findings.**

## VERIFIED FINDING 1 — the theorem registry violates its own standing rule

`docs/THEOREM_REGISTRY.md`, line 7, **its own text**:

> *"Standing rule: **every future bank that creates a theorem or law adds its line here IN THE SAME
> PR.**"*

**It has 56 entries and tops out at B920. The corpus is at B1099.** Checked individually and
**absent**: **B1012** (the forced action and `c = 6σ` — *used in the paper*), **B1076**, **B1080**,
**B1085**, **B1088**, **B1094**, **B1098**.

**So the registry created for "every theorem and law, mapped for the novelty relaunch" is missing
the entire recent window, including the hatch, the global form, the two-route wall, and the action
the paper cites.** This is not lag: it is **179 arcs of a stated same-PR rule going unenforced**,
because **no gate reads that rule** — `representation-sweep` polices synthesis surfaces generally,
but nothing checks the registry against new laws.

## What phase 2 owes

The remaining 35 live surfaces triaged one by one (function-requires-currency vs legitimately
static); the `GUT_REQUIREMENTS_LEDGER` (lag 147), `UNIFIED_STATE` (192) and `BANKING_PROTOCOL` (115)
verified individually; B8097's nineteen carried in as named items; and the counter reset.

## SCOPE

Phase 1 is **mechanical**: an inventory, a currency spine, and **one verified finding**. The 36-row
list is **candidates**, explicitly not verdicts. No measured value; Gate 5 untouched.
