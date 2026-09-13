# B1349 — THE MIRROR SECTOR POSED: the residual freedom is 48, and R11's arithmetic says DO NOT SPEND THE ROW

**Date:** 2026-09-13 · **Seat:** cc · **Lane:** MATHEMATICS (the crossing door).
**Depends on:** B1011 (C6, the mirror set), B1040, B1348, `docs/KIND_TABLE.md`,
`docs/CROSSING_REQUIREMENTS.md` (R1–R12), `docs/LISTENER_MAP_SPEC.md`.
**P0:** this **counts a freedom**. It performs **no** value comparison — `F2` absolute — and pays
nothing. Its purpose is to make R7's look-elsewhere ledger and R11's anchor arithmetic *computable*
for the crossing's only remaining target.

---

## Why this sector and not the other

`KIND_TABLE`'s four coupling rows: **tones CONSUMED** (B1066 R-B, MISS decisive), **probability
CONSUMED** (B1066 R-A, MISS decisive), **phases CONSUMED** (B1027 + B1063, MISS both sectors), and

> **mirror set (θ-even) — UNCONSUMED — the last licensed row**, delivered by B1011 C6 and *"never
> drawn on by any sealed comparison."*

And the one-shot rule *"consumes CONTACT ROWS"* — so the row is spent whatever the outcome.
**B1348 posed the θ-ODD plane, which is not the crossing target.** This poses the right one.

## The instrument on the even sector (controls first)

| | |
|---|---|
| canonical rational basis from the weights: `e₍₀,₀₎`, `e₍₁,₁₎`, `e₍₀,₁₎+e₍₁,₀₎`, `e₍₀,₂₎+e₍₂,₀₎` | all satisfy `C v = +v` ✔ |
| `⟨R,L⟩` restricts exactly to it | ✔ |
| **projective image** | **720 = 12 × 60 = `A₄ × A₅`** ✔ (as forced: `(−1,−1)` and `(−1,1)` act as scalars on `V₂⊗V₂`) |
| `ℂ⁴_even` irreducible | ✔ no common eigenvector |
| control: a random direction | `\|Stab\| = 1`, orbit 720 ✔ |

## The stabilizer spectrum — every orbit size divides 720, as orbit–stabilizer requires

| `\|Stab\|` | 15 | 10 | 9 | 6 | 5 | 3 | 2 |
|---|---|---|---|---|---|---|---|
| **orbit size** | **48** | 72 | 80 | 120 | 144 | 240 | 360 |

> ### MAXIMAL `|Stab| = 15` ⟹ THE SMALLEST DISTINGUISHED ORBIT HAS **48** ELEMENTS.

And the structure is confirmed, not assumed: `15 = 3 × 5` = (tetrahedral vertex stabilizer) ×
(icosahedral vertex stabilizer), and the maximal-stabilizer direction is **rank 1** — singular values
`[1, 0]` — i.e. a **product state** `v ⊗ w`, a tetrahedral vertex tensored with an icosahedral vertex.

**Method correction, recorded not hidden.** A first pass orbit-decomposed by rounding projective
coordinates and produced sizes that **do not divide 720** (68, 370, 423, …) — impossible by
orbit–stabilizer. That enumeration is **withdrawn**; the table above is derived from *stabilizer
orders only* (robust integer counts over 720 matrices) with `|orbit| = 720/|Stab|`. Same float-drift
failure as B1348's withdrawn step 4, caught the same way — by an invariant the answer must satisfy.

## R11's ARITHMETIC — and it is the point of the arc

R11: *"outputs − consumed anchors > 0, else the cell is vacuous (MB12)."* R7: *"every designer
freedom priced in a look-elsewhere ledger."* Both are now computable for the mirror row:

| | |
|---|---|
| **anchor cost, branch A** (the row needs **one** direction) | a **48-fold discrete selection** — `log₂ 48 ≈ 5.58 bits` |
| **anchor cost, branch B** (the row uses the **whole orbit**) | no selection, but the prediction becomes a **48-element set** — a 48-fold look-elsewhere on the comparison side instead |
| **outputs** | the mirror row is **one** row |

> **On either branch the inequality does not close.** One output against ~5.6 bits of selection, or
> one output against a 48-element target set. **R11 declares that vacuous before the seal.**

## THE RECOMMENDATION, stated as a result

> **Do not spend the last row.** Not now, and on this arithmetic not through this row at all — unless
> the mirror set's *"value set already exact"* (B1011 C6) is shown to carry **more than one
> independent output**, in which case the outputs are recounted and R11 is re-evaluated.

Three of four rows are spent with decisive misses. The fourth is unrepeatable. **A gating
computation that says "no" is worth more than a fourth miss**, and cheaper.

## What would change it

1. **Count the mirror set's independent outputs.** If it yields `k` genuinely independent numbers
   with `k > log₂ 48 ≈ 5.6` bits' worth, R11 closes and the arc becomes worth its shot.
2. **Cut the 48.** Anything that reduces the orbit — a Galois obstruction, a further canonical
   condition — improves the ledger directly. The Galois question at the point level is **open**
   (B1348's withdrawal left it so).
3. **A new licensed row**, derived not fitted (`F1` forbids fitting), added to `KIND_TABLE` under
   `R5` in advance.

## Fences

`F2` untouched, no comparison performed, no value read. **I-13 remains UNEARNED.** `R4`, `R5`, `R10`
stay as banked (discharged / existing / answered); nothing here re-opens them. And the same
exactification debt B1348 registered applies: the verdict rests on integers computed in double
precision, robust here because orbit–stabilizer checks them, but the exact `ℚ(ζ₆₀)` re-derivation is
**owed** for both arcs.

**Numbering note:** this arc takes **B1349**, the last id before the reserved range
`B1350–B1399` (E71). The next new arc on this branch needs a range grant.
