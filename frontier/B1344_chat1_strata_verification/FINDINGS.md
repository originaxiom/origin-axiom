# B1344 — VERIFYING chat1's STRATA REPORT: one real result, one refutation, and a collision in our own record

**Date:** 2026-09-12 · **Seat:** cc · **Lane:** MATHEMATICS.
**Depends on:** B309/B518 (the κ-unification), B416/B448 (the trace map, the orbit tower), B497
(the strata), B1248 (the object's κ), B1342 (the multipliers).
**P0:** this verifies a forwarded report by recomputation. Everything below is exact over `ℚ(ω)`.

---

## Verdict table

| claim | verdict |
|---|---|
| **C1** stratum 1 is the `χ = 0` stratum; F6's wall and B497's stratification are the same boundary | **CONFIRMED — and it is a real result** |
| **C2** multipliers `x²y²` (2), `x²+y²−xyz` (3), `0` (4) | **CONFIRMED** (reproduces B1342) |
| **C3** *"the object's geometric point is `x = ω−1, y = −2ω, z = −2`. Exactly"* | **REFUTED**, three independent ways |
| **C4** *"κ − 2 = ω"* for the object | **TRUE of one κ in the record, FALSE of the other** — see §3 |
| **C5** the ℤ/3 table (`ω → ω²` under decoherence) | **holds at chat1's point only**; fails at both legitimate points |
| **C6** F-theory already gets E₆ from IV\* fibres | **CONFIRMED** (standard) |
| **C7** leaving stratum 1 gives a solenoid, not a manifold; χ may be undefined | **CONFIRMED** |

## 1. C1 is right, and it is the best thing in the report

χ is multiplicative in fibrations, so for **any** surface bundle over the circle
`χ(M) = χ(F)·χ(S¹) = χ(F)·0 = 0`. A mapping torus requires a self-**homeomorphism**, which induces an
**automorphism** of `π₁` — stratum 1 by definition (Dehn–Nielsen–Baer: `Out(F₂) ≅ MCG ≅ GL₂(ℤ)`).
Strata 2, 2′, 3, 4 are injective-not-surjective or non-injective, so **no mapping torus exists for
them at all**.

> **F6's `χ = 0` wall and B497's "stratum 1 of 4" are the same boundary.** B497 said it in July as an
> algebraic statement and nobody read it as a geometric one. It is one.

C7's caveat is also correct and belongs next to it: the natural object for a non-invertible map is an
**inverse limit / solenoid**, which is not a manifold, so `χ` need not be defined there. Leaving the
wall does not hand you `χ ≠ 0`.

## 2. C3 is refuted — the object's geometric point is something else

**Derived here, not assumed.** The fibre holonomy is the character fixed by the monodromy `T₁²`
(B448: the figure-eight monodromy **is** `T₁²`) on the parabolic leaf `κ = −2` (B1248). Solving:

> **(x, y, z) = (2+ω, 1−ω, 1−ω)**, with **κ = −2**, and `x` satisfies **`x² − 3x + 3 = 0`** —
> *exactly* B448 Part C's banked period-2 field ℚ(√−3), *"the discrete-faithful pair"*, re-derived
> here independently.

chat1's point `(ω−1, −2ω, −2)` fails **three independent tests**:

1. its **κ = 2+ω**, not `−2` — it is on the wrong leaf;
2. it is fixed by **neither** the monodromy `T₁²` **nor** the half step `T₁`;
3. it is **not** in the `Aut(F₂)` orbit of either meridian point (186 points searched to depth 4 from
   each; and κ is `Aut(F₂)`-invariant, so orbits cannot mix κ values anyway).

It is a legitimate point of the character variety. It is **not the object's geometric point.**

## 3. Where C4 comes from — and it is our defect, not chat1's

chat1's `κ − 2 = ω` is not invented. **The record contains two different numbers both called
"κ = tr[a,b]":**

| source | generating pair | κ | κ − 2 | \|κ − 2\| |
|---|---|---|---|---|
| **B309 / B518 / B1010** | the **knot group's meridian** pair | `2 + ω²` | **`ω²`** | **1** — *"the UNIT obstruction"* |
| **B416 / B448 / B1248** | the **fibre's** pair (once-punctured torus) | **`−2`** | `−4` | 4 |

Both are `tr[a,b]`. They are traces of commutators of **different generating pairs of different
groups**, and they are not equal. The record uses **one symbol for two quantities** and has never
said so.

**C4 is true of the first and false of the second, and the report attaches it to the second.** So
*"the object's κ minus the classical floor IS the primitive cube root of unity"* is a true statement
about the meridian invariant (that is B309's banked `κ−2 = ω²`, |κ−2| = 1) and a false one about the
κ that B497's strata act on, which is `−2`.

**Recorded as `ERROR_LEDGER` E72.** This is the trap, and it caught a careful seat.

## 4. C5 does not survive at either legitimate point

Pending item 9's first step, done at the points that are actually the object's:

| point | κ−2 | evolution | renormalize | per-doubling | decoherence | erasure |
|---|---|---|---|---|---|---|
| **fibre geometric point** | `−4` | `−4` | `−36` | `−6−6√3i` | `6−6√3i` | `0` |
| **meridian point** | `ω²` | `ω²` | `−8−8√3i` | `−2−2√3i` | **`−4`** | `0` |
| *chat1's point* | `ω` | `ω` | `−12ω` | — | **`ω²`** | `0` |

The stratum-3 multiplier equals `ω` **at chat1's point only** — not at the fibre point (there it is
`3ω`, on `κ−2 = −4`) and not at the meridian point (there it is `−4ω`, sending `ω² ↦ −4`).

> **The "decoherence rotates the ℤ/3" reading does not survive at either legitimate point.** chat1's
> own two gates — the base rate, and whether this ℤ/3 is the generation ℤ/3 — are therefore not the
> binding constraint: the observation does not reach the object in the first place.

## 5. What survives, and it is not nothing

* **C1 is a genuine result** and is worth an arc of its own: *the invertibility of stratum 1 and the
  vanishing of χ on surface bundles are the same fact*, which converts B497's July line into a
  geometric statement about the programme's own wall.
* **Pending item 9 is now actually done at the object** (§4) — the multipliers evaluate to exact
  algebraic integers in `ℤ[ω]`: **`1, 9, −3ω², 3ω, 0`** at the fibre point. Those are new numbers on
  the record, unbanked before today. **No reading is attached to them**, and the honest note is that
  the clean story chat1 reported is an artefact of the wrong point.
* **The κ-collision (§3) is the most consequential finding**, because it is upstream of both reports
  and of anything else that computes with κ.

**Nothing here licenses a physics reading, and no claim is promoted.**
