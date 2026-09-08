# B1261 — THE PRICE, COMPUTED: fifteen unpriced inputs bought zero of nineteen numbers, and the exchange rate is the thing to work on

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (a reading of the banked ledgers, gated against their own ratchet; two MB12 controls, one enforcing the incommensurability)

## Why this arc exists

JOIN 2's lead — *is n in κ = 2 + n² object-determined?* — closed **NEGATIVE**: n = 1…7 all occur
with hundreds of partners, reconfirming **B1248**'s *"infinite family, not a point."* That made a
different question the live one, and the corpus has never answered it **in one place**:

> **How many unpriced inputs does the programme spend, and what does it buy?**

**B1231** made the question askable: an unearned identification is an **unpriced observer input**,
so the input ledger's parameter count is a **lower bound** until every identification is earned.

## The two sides, read from the ledgers

| | |
|---|---|
| **SPENDS** | **4 axioms** (census unchanged — B1248 closed checklist I1 *without* reducing it; A7 stays an axiom) **+ 11 UNEARNED identifications** = **15 unpriced inputs** |
| **The SM's side** | **19 free parameters** (26 with Dirac neutrinos), plus the un-derived structure: why the gauge group, why three generations, why m_H ≪ M_Pl, why θ_QCD ≈ 0, ν-mass mechanism, flavour origin, DM, DE, baryon asymmetry, gravity |
| **BUYS** | **0 of the 19 numbers** — *"none. Seven sealed crossings, seven negatives"* |

**What it does buy, counted separately and never converted:**

- the **global ℤ₆ form** — DERIVED (B862), and **the SM itself cannot fix it**: a fact physics cannot
  even state, let alone measure;
- **hypercharge direction** — DERIVED (B864): the unique gaugeable U(1). *The normalisation is not
  derivable*;
- **anomaly cancellation** — all six, with hypercharge conserved on 45/45 cubic triples;
- **termination at the SM** — the SM is the terminal registerable algebra (B863);
- **partial**: the gauge algebra is su(3)⊕su(2)⊕u(1)³, **dim 14 against the SM's 12** — the chain is
  **two steps from the SM, not zero**;
- **not a prediction**: sin²θ_W = 3/8 reproduces a **known GUT relation** and is **non-discriminating**
  (identical for 5, 5̄, 10, 16, 27 — B1250);
- **closing-supplied**: chirality is **not self-supplied** (B713/B760) and enters through a **closing**
  (B582/B576/B432) — which E65 and B1260 now explain: the object is **self-paired**, and handedness
  is exactly the mirror-odd content a self-paired thing cannot hold.

## The verdict, in two currencies that do not convert

> **BY PARAMETER COUNT the trade is NET NEGATIVE: 15 unpriced inputs bought 0 of 19 numbers.**
>
> **BY STRUCTURAL CONTENT the programme derives what the SM assumes or cannot state** — which is
> real, and is the honest reason to continue — **but it is not a parameter reduction and must never
> be reported as one.**

The arc's control enforces exactly this: structural deliveries are counted in a separate list and
the selftest asserts they are **not** subtracted from the parameter tally.

## The constructive consequence — and it changes what to work on

The exchange rate is **15 : 0**, and there are exactly **two** ways to move it:

1. **EARN an identification** — price −1;
2. **DERIVE a parameter** — purchase +1.

**Earning is cheaper, is already instrumented (the B1231 ratchet), and 8 rows are EARNED already.**
So `docs/IDENTIFICATION_LEDGER.md` is **not bookkeeping around the physics — it IS the scoreboard**,
exactly as B1231 argued and this arc now measures. Every earned row is worth as much to the trade as
a derived parameter, and the corpus knows how to earn rows.

## Controls (MB12, both directions)

- **The counts are read, not asserted:** the arc **fails** if the ratchet's `unearned` disagrees with
  the ledger's own row census, or if `total_rows` drifts from the row count.
- **The incommensurability is enforced, not merely stated:** the selftest asserts that the structural
  tally is never subtracted from the parameter tally.
- **The zero is pinned deliberately:** if `bought` ever becomes nonzero the selftest fails, so the
  headline can only change by an explicit edit.

## Verification

`verification/the_price.py` — standalone, reads the live ledgers.

- **Feeds on:** B1231 (unpriced-input rule), B950/`SM_SPECIFICATION_LEDGER` (the 19 and section C),
  B862, B864, B863, B1250, B713/B760, B582/B576/B432, B1248 (the closed lead), E65/B1260.
- **Registers:** no identification change; measures the ledger rather than adding to it.


---

## ADDENDUM 2026-09-07 (B1296) — the ratchet raised by hand

I-27 registered UNEARNED (B1296, the singular-frame road to count 2). The ratchet baseline is raised 10 → 11 with its reason in `docs/IDENTIFICATION_BASELINE.json`; the price this arc measures becomes 4 axioms + 11 unearned rows = 15 rows outstanding (B1266's irreducible count: 4 + 8 = 12). The arc's tests read the live ledger and baseline and need no change.
