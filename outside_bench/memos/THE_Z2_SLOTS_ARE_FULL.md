# 200 — THE ℤ/2 CENSUS HAS ONE KIND IN IT, AND THAT KIND'S SLOTS ARE FULL

**Date** 2026-09-11 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/the_z2_slots_are_full.py` · **Output**
`outputs/the_z2_slots_are_full_out.txt` · CELL 1/2/3 = **B/B/B**, four controls, all passing
**Gate 5 untouched**

**Occasion.** Memo 199 adjudicated B1327's handoff — §8's chirality bit is *not* the manifold's
mirror sign. That answer raises the structural question the record has never put in one place:
**what kind of object is each of the programme's ℤ/2's, and how many kinds are there?**

**Exhausted first** (`already_banked.py`, terms: *"Z/2 census every two-element invariant
identified"*, *"genus bit same as c mirror involution"*, *"how many distinct Z2 bits does the object
carry"*, *"Z/2 bits are different KINDS not all Galois legs square class torsion subgroup"*). The
census **exists and is sound**:

* **B1174 — NEGATIVE.** The ℤ/2-identification cell. Four candidates (B942 chirality/Gal(K/ℚ),
  B957 value torsors, B1168 mirror bit, S068's genus-ℤ/2 of ℚ(√−15)). *"Not one torsor — one shared
  involution"*: two V₄'s sharing exactly the **c**-leg.
* **B1276 — PROVED.** B1174's legs **are** B730's faces, and the parity law: *c acts nontrivially on
  a quadratic field iff the field is imaginary.*
* **B1041 — PROVED.** The Galois / operations / closings (ℤ/2)³ cubes are **one** cube at direction
  level.

**Nothing was rebuilt.** What follows is the increment those three do not contain.

---

## 1. Everything in the existing census is the SAME kind of object

Every candidate B1174, B1276 and B1041 weigh is *the sign of a named surd under a field
automorphism*. That is one kind, and for the V₄ the object's arithmetic forces, **its slots are
full — by counting, not by inspection**:

`Hom(V₄, ℤ/2)` enumerated by brute force over the group: **4 elements, 3 non-trivial** (control C1).
And B730/B1174 already name all three, exhibited here as those three homomorphisms:

| leg | field | flips | who names it |
|---|---|---|---|
| **being** = c | ℚ(√−3) | the √−3 sign | B942 / B1168 / B1174 |
| **hearing** | ℚ(√5) | the √5 sign | B957 / B1067 |
| **meeting** | ℚ(√−15) | the composite, `c · hearing` | B1174 / B1276 / B698 |

The parity law is reproduced before the machinery is used (control C2), on all three faces **plus
B1276's off-face control ℚ(√−7)**: `c` acts iff imaginary, 4/4.

**Scope, stated plainly.** *Full* is a statement about the **meeting V₄** = `Gal(ℚ(√−3,√5)/ℚ)`, the
group B730 proves the object's arithmetic forces. B1041's `(ℤ/2)³` cube is a **larger** group with
seven non-trivial characters and this memo says nothing about how many of those are spoken for.

## 2. Two bits the record books are NOT of that kind — and neither was in the census

### §8's relational bit is not even two-valued on its own domain

With the object relatum held fixed at B1248's `A_OBJ` and only the partner moving, B1248's
`D = (2 − κ)/g²` runs over

    -181, -29, -19, -1, +1, 5, 11

**It is a bit only on the sub-locus `|D| = 1`.** Off that locus the class is a **torsor** with no
distinguished pair of elements — B1248's own TORSOR branch. Control C3 confirms the classifier *can*
return a genuine ℤ/2 (both signs of `|D| = 1` occur), so this is not a broken instrument.

**Calling it "a bit" is exact where `|D| = 1` and a contraction everywhere else.** The paper does
not overclaim here — §8 speaks of *the pairs that carry the bit* — but a ledger row that books "one
bit" carries none of that structure.

### The Chern–Simons bit is the torsion of an archimedean value group, and it is independent of c

`A[2] = {0, ¼} ⊂ ℝ/½ℤ`. Genuinely two-valued — and **not the c-leg**:

| | amphichiral | volume | CS | `A[2]` class |
|---|---|---|---|---|
| **m003** | yes | 2.029883213 | +0.250000000000 | **¼** |
| **m004** | yes | 2.029883213 | +0.000000000000 | **0** |

**Both amphichiral** — so `c` is present and non-trivial on both — and **of equal volume**, so no
archimedean invariant separates them either. Yet they sit at **different** elements. Across this
bench's own banked L192 census (203,122 manifolds, control C4): **181 amphichiral, 106 at 0 and 75
at ¼.**

> **Amphichirality forces membership in `A[2]`. It does not force which element.**

## 3. So the record carries at least three KINDS of ℤ/2, not one family

| kind | what it is | slots |
|---|---|---|
| **(a) Galois leg** | the sign of a surd under an automorphism | exactly 3 on the meeting V₄ — **full** |
| **(b) square class of a pair** | §8's relational bit | two-valued only on a sub-locus |
| **(c) torsion of a value group** | the Chern–Simons bit | two-valued, independent of (a) |

## 4. Why this matters, and it is why B1327 could raise its question at all

**A ledger that books bits without typing them by kind invites exactly the over-count worry B1327
raised.** Two bits of different kinds cannot be the same input, and that is settleable **by typing,
before any pair of them is compared**. Memo 199 settled one such pair by computation. This settles
the general shape: the comparison B1327 worried about is between a **(b)** and an **(a)**, and those
cannot coincide.

This is the same move B1327 itself made for "observer" — replacing one overloaded word with four
types, because *an identity can be searched for and an observer cannot*. The same is true one level
down: **a bit whose kind is named can be compared; a bit booked as "one bit" cannot.**

## 5. What this does not do

It does not move a freedom-ledger row — the ledger owner's call. It does not claim the list of kinds
is complete; it claims **at least three, exhibited**. And it does not weaken B1174, B1276 or B1041:
each is reproduced here as far as it is used, and the finding is that **their census was sound and
scoped** — it answered the question it asked, about legs, and two later bits are not legs.

*Gate 5 untouched — no measured value is used or named. Nothing promotes to `CLAIMS.md`. No arc is
retracted.*
