# B8106 — R48 PHASE 2: a requirements ledger still says the object cannot do what the same window proved it does

**Date:** 2026-08-21 · **Seat:** cc3 (audit) · **R48 COLD**, window frozen at `07e46c7f`. Gate 5
untouched. Modulus as declared in B8105.

## VERIFIED FINDING R48-F2 — `docs/GUT_REQUIREMENTS_LEDGER.md`

At the frozen head, the ledger states:

> *"Therefore every measurement in the cascade is rank-preserving, and **no number of them can ever
> reach rank 4**."*
>
> *"Reaching the Standard Model requires **rank reduction**… It requires a genuine breaking mechanism
> — a Higgs VEV, a Wilson line / Hosotani flux, or an orbifold projection — i.e. requirement **#11,
> which the object does not currently supply**."*

**The theorem sentence is CORRECT and correctly scoped, and I will not pretend otherwise.** Its
stated reason is *"the centralizer of a set of semisimple elements contains a maximal torus"* —
**semisimple**. B1098's stratum is **nilpotent**, which is precisely the scope boundary cc and I
settled when B959 was re-scoped in this same window. **Measurements still cannot reach rank 4.**

**The CONSEQUENCE is stale.** The ledger names three mechanisms — Higgs VEV, Wilson line/Hosotani,
orbifold — and concludes the object *does not currently supply* one. **B1098, in this window, reaches
`su(3)⊕su(3) ⊇ SM` at rank exactly 4 via the object's OWN non-abelian holonomy**, which is on none
of those three lists; **B1100 witnesses the matter there is COMPLEX.**

**So a requirements ledger — the document whose entire job is saying what is missing — records as
missing a thing the same window supplied.**

## Why this is the sharpest kind of miss

The **doc-reflection wave** (`168188d1`) rewrote **13 markdown surfaces** to the post-B1101 state and
corrected an overclaim *"everywhere it lived."* It touched **`SM_SPECIFICATION_LEDGER.md`**. It did
**not** touch **`GUT_REQUIREMENTS_LEDGER.md`**.

**Two ledgers, one updated, one missed** — and the missed one is the register of gaps, so its
staleness runs in the **pessimistic** direction: it under-reports what the programme has.

**And this ledger is a repeat offender.** The B976-era sweep already found **five of its rows reading
"absent" against banked arcs** (baryogenesis/B867, neutrino mass/B865, proton decay/B867+B881, the 12
exotics/B884+B895, the breaking sector/B853). **Same document, same failure mode, second occurrence.**

## Also verified stale for the window

**`docs/UNIFIED_STATE.md`** (lag 192) — contains none of B1080, B1094, B1098, B1100. A document named
*unified state* that does not know the hatch opened. **Candidate confirmed as a real miss**, lower
weight than F2 because it is a narrative surface rather than a decision register.

## What phase 2 does NOT claim

- **Not** that the ledger's theorem is wrong. **It is right, and correctly scoped.** Only the
  consequence drawn from it has been overtaken.
- **Not** that B1098/B1100 deliver the Standard Model. They deliver **rank 4 with complex matter at
  a trinification landing** — the ledger's remaining requirements are untouched by this finding.
- **Not** a review of B1102, which is **post-boundary** by cc's own freeze and outside R48.

## SCOPE

Phase 2 verifies two of B8105's 36 candidates individually and confirms both. **34 remain untriaged.**
Gate 5 untouched.
