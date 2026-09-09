# B1275 — THE E₈ FAMILY MECHANISM, VERIFIED ON MAIN — and the one step that is not

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (E₈ rebuilt from scratch; five MB12 controls) · **Integrates the SM-derivation seat's B1269, harvest-not-merge**

## The task

Owner: *"lets integrate three generations derivation in main, verify whats remains unverified."*
E₈ is **rebuilt from its own definition** here — nothing imported, nothing taken on the seat's word.

## Verified

| claim | result |
|---|---|
| E₈ has 240 roots (±e_i±e_j; (±½)⁸, even # of minus signs) | **240** ✔ |
| an A₂ subsystem exists, **found by search** (dot = −1, sum a root) | **6 roots** ✔ |
| its centraliser in E₈ is E₆ | **72 roots** ✔ |
| the remainder is 6 × 27 | **162** ✔ |
| they fall into six classes of exactly 27, by A₂ weight | **6 × 27** ✔ |
| **SUM RULE 1**: two roots of the **same** class never sum to a root | **0** ✔ |
| **SUM RULE 2**: different classes sum to a root **270×** per ordered pair | **270 for exactly the 12 within-orbit ordered pairs** ✔ (full census: 27×12, 270×12, 432×6) |
| **THE FAMILY STRUCTURE**: an order-3 element cycles the six classes in **two orbits of three** | the A₂ Weyl rotation s_a s_b, **order verified = 3**, gives orbits **[3, 3]** ✔ |

**So 248 = 78 + 8 + (27,3) + (27̄,3̄) and the family structure are REAL and STANDARD**, and the seat's
arithmetic reproduces exactly. This is the classic **E₈ ⊃ E₆ × SU(3)** family mechanism — and the
corpus now has it **verified rather than cited**.

## What remains unverified — the whole object-specific step

> **THAT THE OBJECT'S OWN ORDER-3 ELEMENT IS THIS A₂ ROTATION.**

**Everything above is a fact about E₈. Nothing in it mentions m004.** The seat's claim is that *"the
founding ratio g"* (B1268's icosian construction) supplies the order-3 element — **not checked here**,
and checking it would require rebuilding that construction on main.

## And the chain this exposes — the sharp question

The corpus now has **three order-3 structures**:

| | what | where |
|---|---|---|
| **L3** | the trinification ℤ/3 grading of the 27 | B305 — **85 distinct gradings** (B1264) |
| **L4** | the commensurator's Eisenstein-unit ℤ/3 | B302/B323 |
| **A₂** | the family rotation | **verified here** |

**B1264** established that **L3 and L4 act by the SAME ω of ℚ(√−3)** — not merely both of order 3 —
though L3 → L4 is still not a map that **acts** (85 candidate gradings). **If the A₂ family rotation
is that same ω, three generations become object-supplied.**

**That is the sharp open question, and it is far more concrete than "derive three generations."**

## Two fences carried from the source seat, not relaxed

- Its own arc says **THE BIT** — choosing the matter triplet, **ω vs ω̄** — is *"supplied by a
  **closing**, not by the object"*: the same mirror-odd ℤ/2 the corpus has carried since **B582**.
- It reports **N = 0** and **the Yukawa forced to ZERO on the triplet.**

**So even if the object-specific step lands, the mechanism buys the COUNT and not the VALUES.**

## Controls (MB12, both directions)

- E₈ built **from its own definition**, its 240 roots counted — not imported.
- The A₂ is **found by search**, not hard-coded.
- The centraliser is **computed** and checked to be 72 — "E₆" is verified, not assumed.
- The Weyl rotation's **order is computed to be 3** before its orbits are read.
- **SUM RULE 2's full value census is reported** (27/270/432), so the branch's single number 270 is
  **placed in context** rather than confirmed selectively.

## Verification

`verification/e8_family.py` — standalone, from scratch.

- **Feeds on:** the SM-derivation seat's B1269 (harvested), B1273 (the harvest register), B1264 (L3/L4),
  B302/B305/B323, B582.
- **Registers:** no status change. **Isolates** the object-specific step as the live question.
