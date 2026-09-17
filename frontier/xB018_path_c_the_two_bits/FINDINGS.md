# xB018 — PATH C: the two bits are NOT the same ℤ/2 — and each is invisible to the layer the other lives on

**Seat `xb`, `sep16-branch`, 2026-09-17. PREREGISTRATION sealed `0c9b1086…` and PUSHED at `3e63250`
before `verification/` existed, **with its CONFIGURATION AXES declared** under the rule xB017
Addendum 4 earned. Verdict: PROVED.**

Gate 5 absolute: no value, no generation count, no physics reading, nothing to `CLAIMS.md`.

---

## 0. The question, and the hazard sitting in front of it

**Path C:** *are the A5 bit (m003 vs m004) and the A7 bit (LR vs RL) the same ℤ/2?*

**The record uses "A5" for three different things**, and the question presupposes the third — so C1
names all three rather than silently picking one:

| reading | statement | is it a ℤ/2? |
|---|---|---|
| **(a)** | `THE_FRAMEWORK`'s own table row: *"the first mixed closure is torsion-free — forces the word to be **mixed**, aAbB not aA"* | **no** — a constraint on the word |
| **(b)** | xB012's: *"the manifold restriction"* — the group is torsion-free | **no** — **both sisters are manifolds**, so it cannot distinguish them |
| **(c)** | H₁ torsion-free = **knot-ness** = the m003/m004 bit | **YES** — `H₁(m004) = ℤ` vs `H₁(m003) = ℤ/5 ⊕ ℤ` |

**A terminology hazard, named and not silently resolved: this arc means A5(c) throughout.**

## 1. C2/C3 — the two bits do opposite things to the object

| | compare | result |
|---|---|---|
| **A7** | `b++LR` vs `b++RL` | **isometric** — same volume, same `H₁`, same `CS`; and `P·LR·P⁻¹ = RL` with `P = [[0,1],[1,0]]`, B979's statement re-derived |
| **A5(c)** | `b++LR` vs `b+-LR` | **same volume, NOT isometric** — `ℤ` vs `ℤ/5 ⊕ ℤ` |

> **A7 fixes the object. A5(c) changes it.**

## 2. C4 — not the same ℤ/2, under all four criteria the seal declared

**Equal as maps:** one fixes the homeomorphism type, the other does not. **Same subgroup:** they act
on different slots — A7 on the **word**, A5(c) on the **sign prefix**. **Same action on a named
invariant:** they disagree on every invariant tested (§3). **Conjugate:** conjugate involutions have
conjugate fixed sets, and **A7 fixes every bundle up to isometry while A5(c) fixes none.**

## 3. C5 — the sharp form: negation versus translation

Over **240** mixed words of length 2–7, at 40-digit precision:

| bit | action on `CS` | hits |
|---|---|---|
| **A7** (letter swap) | `CS ↦ −CS` | **240 of 240** (B128's M-C, re-derived) |
| **A5(c)** (sign prefix) | `CS ↦ CS + ¼` | **240 of 240** (xB015's K6, re-derived) |

> **On m004 itself, where `CS = 0`: negation is the IDENTITY and translation is not. The A7 bit dies
> on m004's own zero; the A5 bit does not.**

And on B979's **based** invariant, the Möbius fixed-point polynomial: `LR → t²+t−1`, `RL → t²−t−1`,
roots `φ`-family either way. **A7 moves it; A5(c) never touches the word, so it leaves it fixed.**

*The convention, which is the content:* this bench's polynomials are **transposed** relative to
B979's document — exactly the transposition B979 flagged, and B979's own reading is that **the
dependence on naming IS the inserted bit**. Reproduced here, not disputed.

## 4. C6 — the blind cell, and it found the reason A7 is "one bit"

B1083 types the founding torsor as **`K₄ = ⟨C (letter swap), P (reversal)⟩` — two spendable bits.**
On the minimal word, `C(LR) = RL` **and** `P(LR) = RL`.

| | agree | differ |
|---|---|---|
| mixed words, length 2–8 | **30** | **464** |

**First word where they separate: `RRL` — `C → LLR`, `P → LRR`.**

> **The two torsor bits coincide on the minimal word and separate immediately above it. The K₄
> collapses to a single ℤ/2 exactly at the object A6 selects — which is WHY A7 reads as "one bit"
> rather than two. A6's minimality is doing that work.**

*Honest scope:* a statement about the **word**, the axis this arc varies. It does **not** say the two
torsor bits are the same in general — they are not, above length 2 — and it is **not** a selection
principle.

## 5. C7 — the group the two bits generate

A5(c) is `(s, W) ↦ (−s, W)`; A7 is `(s, W) ↦ (s, C(W))`. **Disjoint coordinates**, so they commute,
each is an involution, neither is trivial: **`⟨A5(c), A7⟩ = ℤ/2 × ℤ/2`**, exhibited on `W = RRL` with
a 4-element orbit. **Independent — and this K₄ is a different K₄ from B1083's torsor, which lives
entirely inside the word coordinate.**

---

## 6. C8 — the verdict

> **NO. The A5 bit and the A7 bit are not the same ℤ/2.** And **the interesting part is not that they
> differ, but where each one is visible:**
>
> * **A7** is invisible to every **class** invariant (it fixes the manifold) and visible only to a
>   **based** one — B979's fixed-point polynomial. On `CS` it acts by **negation**, so it **dies on
>   m004's zero**.
> * **A5(c)** is invisible to the **character variety** (xB007) and visible in the **k-coupling**
>   (xB015 K6). On `CS` it acts by **translation by ¼**, so it **survives** there.
>
> **Two bits, each invisible to the layer the other lives on.**

**AXES HELD FIXED, named as the rule requires:** the monodromy's ambient group is **`SL(2,ℤ)`** —
**`GL(2,ℤ)` (det = −1, B1083's Breath pulse `M` with `M² = RL`) is NOT varied here** · bundles
**`b++` and `b+-` only**; `b-+`/`b--` do not parse in SnapPy for these words and were **not tested** ·
**word length ≤ 8** · **only reading (c) of A5** is carried through, with (a) and (b) named in C1 and
set aside with the reason.

**The `GL(2,ℤ)` axis is the one a next arc should vary**, because B1083 puts the Breath pulse there
(`det M = −1`, `M² = RL`) and this arc could not reach it.

## 7. What this arc does NOT claim

Not that either bit is a physical chirality or parity · not that the K₄ collapse is a selection
principle · no identification (E82/I-10) · no physics reading · nothing to `CLAIMS.md`.

**Locks / artifacts:** `verification/two_bits.py` (C1–C8), `verification/two_bits.json`,
`verification/two_bits.out`.
