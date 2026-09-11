# 204 — THE OBJECT'S D₄ IS OF TYPE ⁶D₄, AND IT CARRIES NO TRIALITY OVER ℚ

**Date** 2026-09-11 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/the_object_is_6d4.py` · **Output** `outputs/the_object_is_6d4_out.txt`
**Primary sources** supplied by the owner: Knus–Tignol arXiv:1409.1718; Knus–Tignol arXiv:0912.3405;
Barry–Tignol arXiv:2301.10130
**Gate 5 untouched**

**Occasion — the owner, governing this cell:** *"verify load bearing math, dont lean on old work
which might have been misinformed, or later superseded."*

**Every computational step below is redone in the certificate from the e₆ structure constants.**
The only outside inputs are two verbatim statements from a primary source, quoted with page
numbers, whose proofs were read.

---

## 1. The source, quoted

**Knus–Tignol, *Triality and Algebraic Groups of Type ³D₄*, p. 12 — the type table:**

> *"(i) type ¹D₄: `L ≅ F×F×F` and `Aut_F(L)(F) ≅ S₃`; (ii) type ²D₄: `L ≅ F×Δ` …;
> (iii) type ³D₄: `L` a **cyclic** cubic field extension and `Aut_F(L)(F) ≅ ℤ/3ℤ`;
> **(iv) type ⁶D₄: `L` a NON-CYCLIC cubic field extension of `F` and `Aut_F(L)(F) = 1`.**"*

**Theorem 4.1** (proof read, not just the statement):

> *"Let `G` be an adjoint simple group of type `D₄` over `F`. If `Aut(G)(F)` contains an outer
> automorphism `φ` such that `φ³` is inner, then **`G` is of type ¹D₄ or ³D₄**, and in the
> trialitarian algebra `T = (E,L,σ,α)` such that `G ≅ Aut_L(T)`, the central simple `L`-algebra
> `E` is split."*

**p. 3**, the definition of a cyclic composition, requires *"an `F`-automorphism `ρ` of `L` of
**order 3**."*

## 2. What was computed here

**CELL 1 — K is non-cyclic, from two independent models of the field.**
`μ` (the branch-locus model) and `x³ − 12x − 5` (the monic model) both: irreducible over ℚ,
discriminant **not a square**, squarefree part **77**, and each factors over K as `[1,2]` — so

> **`|Aut(K/ℚ)| = 1`. K has no automorphism of order 3.**

**CELL 2 — the real form of the 28, by exact congruence.**
The Killing Gram matrix `K(x,y) = tr(ad x · ad y)` on the 28, rebuilt here:

    KILLING SIGNATURE: (+16, −12, 0:0)   ->   so(4,4) = THE SPLIT REAL FORM

against `so(8)` compact `(0,28)`, `so(7,1) (7,21)`, `so(6,2) (12,16)`, `so(5,3) (15,13)`. The
routine is validated on four forms whose signature is known independently.

**CELL 3 — the cubic that indexes the three 16s.** For **both** dual-pair charges, independently:

    ad(x8)^2 |48 : charpoly = (irreducible cubic)^16;  the cubic ANNIHILATES it
                   disc not a square, squarefree 77;  commutes with all 28 of the 28;  GENERATES K
    ad(x16)^2|48 : the same, independently

with both bite controls firing — a member of the 28 itself and a random 48×48 matrix are both
reported as **not** commuting, so the test can say no.

## 3. The argument

1. **A degree-3 FIELD lies in the commutant of the 28 acting on the 48.** The annihilation check
   is what makes it a field rather than merely a factor of a characteristic polynomial.
2. **If `L` were split**, the three 16s would be individually ℚ-rational and the commutant would be
   `Mat₂(ℚ) × Mat₂(ℚ) × Mat₂(ℚ)`. **A cubic field cannot embed there:** K is simple, so each
   projection is 0 or injective, and an injective one would make K a subfield of `Mat₂(ℚ)`, whose
   subfields have degree at most 2. **3 ∤ 2.** ⇒ **`L` is not split; the object is not ¹D₄.**
3. `L` is a cubic field with **non-square** discriminant ⇒ **non-cyclic** ⇒ by the type table,
   **the object is of type ⁶D₄**.
4. By **Theorem 4.1**, a group with an outer `φ`, `φ³` inner, is ¹D₄ or ³D₄. **The object is
   neither.** Independently: a cyclic composition needs `ρ` of order 3, and `Aut(K/ℚ) = 1`, so
   **K admits no cyclic composition at all.**

> **The object's D₄ carries no trialitarian automorphism over ℚ.**

## 4. What this does to B882

B882's conjecture is **"the arithmetic S₃ IS the geometric S₃."**

The **arithmetic** cubic **is** K — obtained here from the object's own **forced** charges (memo 202
CELL 1), with **no enhancement triple anywhere**, so the circularity B1077 named does not apply to
this route. But the **geometric** S₃ is **triality**, and the theorem says a non-cyclic cubic is
exactly what makes triality fail to exist over the base field.

> **The two S₃'s are not the same object. They are incompatible.**
> **B882's conjecture is refuted — in the direction nobody was checking.**

B1077 called B882 *"the UNIQUE non-circular route to a 77-mechanism."* The route is non-circular.
It also does not lead where the programme hoped.

## 5. And it resolves a tension rather than creating one

The 28 is **split over ℝ** — Killing signature `(16,12) = so(4,4)` — while its **cubic is a field
over ℚ**. **Real-split, arithmetically twisted.** Both hold, and neither implies the other. The
earlier worry that the real form and the arithmetic disagreed was a worry about two different
questions.

## 6. A CONFLICT with a banked claim — flagged, NOT resolved here

B1077 / W4 state: *"the **UNDRESSED** algebra attaches the split cubic ℚ³ — trivial discriminant,
no 77."* This certificate computes the cubic from **the object's D₄ as it sits in e₆ with its
forced charges** and gets **K**.

The two may be consistent (bare versus dressed) or may not. **This bench does not adjudicate by
assertion.** It is recorded as a **conflict between two computations**, to be settled by
**reproducing B1077's**, not by preferring the newer one.

## 7. What this does NOT do

* It does not compute the full commutant (expected `dim 12`, centre `dim 3`); the §3 argument
  deliberately avoids needing it, and the running computation is corroboration, not load-bearing.
* The **positive** claim I made earlier in this session — *"the object has triality over ℚ in its
  bare form"* — was **withdrawn before this** and is now **refuted**, not merely unproved. It came
  from reading Theorem 4.1's **necessary** condition as sufficient.
* No value, ratio or prediction; no measured quantity. Gate 5 untouched.

## 8. A bug worth recording, because it was caught by luck

An earlier draft of the certificate reused the **78×78** `ad` matrices where the **48-restrictions**
were required. It crashed on a shape mismatch. **Had the shapes matched, it would have silently
compared the wrong operators and the commutant test would have been meaningless.** The separation is
now explicit in the code with that note attached. **Loud failure here was luck, not design.**

*Gate 5 untouched — no measured value is used or named. Nothing promotes to `CLAIMS.md`. One
conjecture of the programme (B882) is refuted; one banked claim (B1077's split cubic) is flagged as
in conflict and left for reproduction.*

---

# ADDENDUM 1 (2026-09-11, same session) — **WHERE THE TRIALITY LIVES: 77 IS THE PRICE, NOT THE MECHANISM**

The constructive counterpart to §3's refutation. Verified on **three** cubics independently — `μ`,
the monic model `x³−12x−5`, and **the 48-commutant cubic from `ad(x₈)²`**:

    disc = 77 x (a perfect square)   in all three cases
      -> sqrt(disc) lies in Q(sqrt 77)
      -> over Q(sqrt 77) the cubic has SQUARE discriminant  ->  Galois group A3 = Z/3
      -> Aut over Q(sqrt 77) has an element of ORDER 3

and the cubic stays irreducible over `ℚ(√77)` because `deg 3` and `[ℚ(√77):ℚ] = 2` are coprime.

| | `L` | type | the `L`-obstruction |
|---|---|---|---|
| over **ℚ** | non-cyclic cubic field, `Aut = 1` | **⁶D₄** | **present** |
| over **ℚ(√77)** | cyclic cubic, `Aut` of order 3 | **³D₄** | **gone** |

**And `ℚ(√77)` is minimal** — it is the fixed field of `A₃` inside the `S₃` Galois closure, so no
smaller field makes `L` cyclic. Knus–Tignol p. 5 adds that *"cyclic compositions over finite fields,
p-adic fields or algebraic number fields are reduced"*, so Theorem 4.2(i)'s **reduced** hypothesis is
automatic over any number field.

> **77 is not what makes triality work. It is the exact price of buying triality at all.**

This inverts the programme's reading of the resolvent. Months were spent asking what mechanism
*produces* 77. **It is not a product. It is the measure of what the object cannot do over its own
base field** — the size of the obstruction, not a clue to a mechanism.

## The fence on the positive half, stated plainly

Over `ℚ(√77)` the obstruction **from `L`** vanishes, giving type ³D₄. **Triality there additionally
requires `E` split over that base** — Theorem 4.1 gives that as necessary, and **this bench has not
verified it.** So the correct statement is:

> **`ℚ(√77)` is where the `L`-obstruction dies. It is not yet where triality is proved to live.**

**Whether `E` — the Allen invariant — is split is the named next computation**, and it is what
completes the verdict in either direction: if `E` is not split, the object has no triality even over
`ℚ(√77)`, and the obstruction is doubled.

## Recorded, not dropped: a computation that died

The full commutant of the 28 on the 48 (expected `dim 12`, centre `dim 3`) was attempted and **killed
by a resource limit (exit 143)**. It was corroboration only — §3's `Mat₂(ℚ)³` argument deliberately
avoids needing it — but it was attempted and did not finish, and that belongs in the record rather
than quietly vanishing.
