# B1266 — THE SOURCE OF INPUT: the 14 overcounts; the irreducible number is 11

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (a structural reading of the ledger, gated by three MB12 controls) · **Corrects B1261's headline**

## The question

**Owner: *"should we find the source of input"*.** Yes — and doing it **corrects B1261**.

B1261 measured the trade as **4 axioms + 10 UNEARNED identifications = 14** unpriced inputs against
the SM's 19 free parameters. But that counts **rows**, and the rows are **not independent**: several
state, *in their own earning conditions*, that they reduce to another.

## Read from the ledger's own text

| row | its own words |
|---|---|
| **I-18** | *"earning it means … i.e. **paying I-13**, the listener map u"* |
| **I-23** | *"… i.e. **paying I-13** on this instance"* (its claim reads *"an I-13 instance"*) |
| **I-11** | *"**the same map as I-10**, restricted to the boundary"* |

**Two parser traps had to be avoided**, and the controls now assert both:

- **I-25's** earning text references **I-1** — but **I-1 is EARNED** (McKay), and *an earned row is
  not a debt*. Counting it would invent a dependency.
- **I-10 ↔ I-11 reference each other** — a **2-cycle** that a naive transitive closure splits into
  **two** roots instead of one, giving 8 sources instead of 7.

Union-find over the dependency relation, restricted to edges into still-UNEARNED rows:

```
10 unearned rows  ->  7 IRREDUCIBLE SOURCES
   [3] I-13, I-18, I-23    THE LISTENER MAP u
   [2] I-10, I-11          THE FORK (internal A1 / theta-polarisation = spacetime spin)
   [1] I-6                 the 2T quotient = the transverse ALE Gamma
   [1] I-7                 the object's Z/3 = the boundary CFT module group
   [1] I-14                L3 grading = L4 commensurator unit
   [1] I-25                which sl2 embedding the object supplies
   [1] I-26                h^1 = the number of 4d chiral generations
```

## The price, restated — and both numbers kept

> **rows outstanding** (what the ratchet tracks, each individually dischargeable): **4 + 10 = 14**
> **IRREDUCIBLE INPUTS** (the theory's actual free inputs): **4 + 7 = 11**

**They measure different things and this arc keeps both.** Earning **I-13** discharges **I-18 and
I-23 with it**; earning **I-10** discharges **I-11**. So against the SM's **19** free parameters,
**the comparison that means something is 11, not 14.**

**B1261 is corrected, not withdrawn.** Its accounting method was right and its row count was right;
what it did not do was **quotient by the rows' own stated reductions**. The trade remains **net
negative by parameter count** — 11 irreducible inputs bought **0** of 19 — and the two currencies
still do not convert.

## And the sources classify by type — which says what work each needs

| type | sources | what it means |
|---|---|---|
| **H5-type** — the object supplies a **family**, the observer picks a point | **I-6** (2 quotients), **I-14** (85 gradings), **I-25** (4 embeddings) | multiplicities **measured** at B1263/B1264/B1256 |
| **missing bridge** | **I-10/I-11** (the fork — **B1265** shows the real form is *derived* and the obstruction is **rank**, inner vs outer), **I-26** (an index theorem across a dimension gap) | a construction, not a choice |
| **the master** | **I-13** | three rows reduce to it |
| **unclassified** | **I-7** | — |

**So "the source of input" has a concrete answer: seven sources, of three kinds, one of which
accounts for three rows by itself.**

## Controls (MB12, both directions)

- **Edges into EARNED or REFUTED rows are excluded**, so a reference to a discharged row cannot
  masquerade as a dependency — asserted on **I-25**, whose text cites the earned I-1.
- **The I-10/I-11 mutual cycle is resolved by union-find, not closure**, and the arc asserts they
  land in **one** group — a naive closure reports **8** and is wrong.
- **The reduction must be accounted:** source count strictly below row count, with the difference
  equal to the number of rows stating a reduction (**3**), or the reduction is miscounted.

## Verification

`verification/sources.py` — standalone, reads the live ledger.

- **Feeds on:** B1261 (the price, corrected here), B1231 (the unpriced-input rule), B1263/B1264/B1256
  (the measured multiplicities), B1265 (the fork as a rank obstruction), B950 (the SM's 19).
- **Registers:** no status change; **restates the price** and classifies its sources.


---

## ADDENDUM 2026-09-07 (B1296) — an eighth source

B1296 registered **I-27** (the singular-frame chiral vacuum: locus, sign pair and θ-odd direction are three closer's choices) UNEARNED at creation. Its earning text names no other unearned row, so under this arc's own union-find it is a NEW irreducible source, H5-type (the object supplies the family, the closer picks the point — like I-14 and I-25). Live count: **11 rows → 8 sources; the irreducible price is 4 + 8 = 12** (was 11). The script's selftest pin and `tests/test_b1266_sources.py` are moved 10/7 → 11/8 with this note; the 2026-09-06 numbers above are the arc's original measurement and stand as written.

*2026-09-08 (B1298): I-28 (the lift of an isometry to E₆) registered UNEARNED; its earning text names I-27, so it joins I-27's source — 12 rows, 8 sources, price 12 unchanged.*
