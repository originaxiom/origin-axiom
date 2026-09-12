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

---

# ADDENDUM 2 (2026-09-12) — **ℚ(√77) BUYS OFF BOTH OBSTRUCTIONS, AND IS CHARGED EXACTLY ONCE**

**Certificate** `certificates/the_price_is_charged_once.py` · **Output**
`outputs/the_price_is_charged_once_out.txt` · **CELL 1/2/3 = B/B/B**, controls pass

Completes the computation §7 named as owed: whether the Allen invariant **E** is split, and over
which field the object's triality becomes available. Inputs are the sextic and cubic **reproduced
from memo 204's own banked output** — the e₆ build is not needed for this cell.

## 1. The sextic is irreducible, so the 48 does not split over K

`ad(x₈)` commutes with the 28 (memo 204, 0/28 failures) and `ad(x₈)² = u ∈ K`, so a splitting of
the 48 over K along `ad(x₈)` needs `√u ∈ K`.

    sextic: t^6 - 15095808t^4 + 56970854793216t^2 - 23922095638236364800
       irreducible over Q: True,  degree 6      (and its square IS the cubic, checked symbolically)

**So `F₆ = ℚ[ad(x₈)|₄₈]` is a degree-6 FIELD containing K, `√u ∉ K`, and the 48 is an
EIGHT-DIMENSIONAL `F₆`-vector space on which the 28 acts `F₆`-linearly.** The 8-dimensional
representation — and with it the splitting of **E** — lives over `F₆`.

## 2. And a negative result of this bench's own is confirmed as an artifact

A mod-p meataxe found a proper submodule of ℚ-dimension 24 at two primes. At **exactly those
primes**:

    sextic mod 10007  : factor degrees [2, 2, 2]
    sextic mod 100003 : factor degrees [2, 2, 2]

so `√u` exists mod p and the module splits there while **nothing splits over ℚ**. **The result was
not read at the time** — the cyclic-vector test's branches had already been found incomplete, and
the meataxe was run precisely because mod-p data cannot settle a ℚ-question. **CELL 2 is why.**

## 3. And `F₆` is the same field as the L-obstruction's

    sqrt(77) lies in F6 : True
    sqrt(-77), sqrt(3), sqrt(7), sqrt(11), sqrt(33), sqrt(21), sqrt(-3), sqrt(5), sqrt(13) : all False

**`F₆ = K(√77)` — the Galois closure of K.** Nine of ten candidates come back False, so the
containment test can say no.

## 4. The result

> **The object's triality is defined over the Galois closure of its own charge field, and that
> closure is `K(√77)`.**
>
> **77 is not one price among several. It appears independently in the L-obstruction and in the
> E-obstruction, and resolves both at the same extension. The price is charged exactly once.**

* **The L-obstruction:** over ℚ, `L` is non-cyclic with `Aut = 1` (type ⁶D₄, no triality). Over
  `ℚ(√77)` the discriminant becomes a square, `L` becomes cyclic, the type drops to ³D₄.
* **The E-obstruction:** the 8-dimensional representation appears over `F₆`.
* **Same field.**

## 5. What this does not do

It does **not** decide whether `E` is split over **K itself**. What is shown is that `E` is split
**by** `K(√77)`, and that the 8-dimensional representation does not appear over K **along
`ad(x₈)`**. Settling `E` over K needs the algebra type of the commutant — `M₂(K)` versus a
quaternion division algebra — **the one computation that has twice been killed by resource limits**,
and it is recorded as outstanding. It does not change the headline either way.

*Gate 5 untouched — no measured value is used or named. Nothing promotes to `CLAIMS.md`.*

---

# ADDENDUM 3 (2026-09-12) — **B1077 REPRODUCES. THE FLAGGED CONFLICT IS NOT A CONFLICT — AND IT RESOLVES IN B1077'S FAVOUR.**

**Certificate** `certificates/b1077_reproduces.py` · **Output** `outputs/b1077_reproduces_out.txt` ·
**CELL 1/2/3 = B/B/B**, controls pass

§6 flagged a conflict and declined to adjudicate, with its own rule: *"to be settled by
**reproducing B1077's**, not by preferring the newer one."* **This is that reproduction.**

## Reproduced

B1077's norm form, from its own banked claim — `N(x) = x₀x₇ − x₁x₄ − x₂x₅ − x₃x₆`, with the Gram
built here **by differentiation** rather than transcribed, so a typo could not silently reproduce
B1077's answer:

    Gram symmetric, rank 8, det 1/256; matches B1077's stated entries G[0,7]=1/2, G[i,i+3]=-1/2
    signature (exact congruence): (4, 4, 0)   -- B1077 claims (+1,+1,+1,+1,-1,-1,-1,-1)
    signed discriminant = 1/256, a square in Q*: True
    Witt index 4 EXHIBITED: span(e0,e1,e2,e3) is totally isotropic

**Hyperbolic, signed discriminant trivial, `Z(C₀) = ℚ×ℚ`, attached cubic SPLIT. Every part of
B1077's claim holds.**

## And the conflict dissolves

* **B1077's object:** the **bare** split-octonion norm form, on the 8-dimensional octonion space.
* **Memo 204's object:** the cubic indexing **the three 16s inside the object's e₆**, from the
  **forced** charges.

**Different objects.** And B1077 said in advance exactly where the 77 would have to come from:

> *"the 77 is NOT in the bare algebra; **any echo mechanism must come from the
> measurement-dressing**."*

Memo 204 computed the dressing and found K, resolvent 77. **Memo 204 is B1077's completion, not its
contradiction.**

## And the procedure is the point

B1077's artifact records **exhaustive** associativity on all **2,097,152** even-blade triples and
the centre checked on all **16,384** ordered even-blade pairs rather than by a generating-set
shortcut. **Had this bench adjudicated by assertion — preferring its own newer computation — it
would have been wrong about a careful arc.**

**Flagging rather than deciding was the load-bearing choice, not the cautious one.** That is the
counterexample to this session's dominant error pattern (#21–#23: claiming before the governing
check has run), and it is worth recording as such.

*Gate 5 untouched. No arc is retracted; one flagged conflict is closed, and closed in favour of the
older arc.*

---

# ADDENDUM 4 (2026-09-12) — **THE OPEN E-QUESTION, REDUCED TO ONE ARITHMETIC STATEMENT**

Addendum 2 left one item open: **is `E` split over `K` itself?** It is still open, but it is now
reduced from "compute a 48×48 commutant" — twice killed by resource limits — to a **statement about
one quaternion algebra**. Recorded as a reduction, **not** as a result.

## The reduction

1. **The commutant has ℚ-dimension 12.** Over `ℚ̄` the 48 is `2·8ᵥ ⊕ 2·8ₛ ⊕ 2·8_c` — the magic
   square's three 16s, each `8 ⊗ ℂ` and hence two copies of one 8 (consistent with memo 202 CELL 4,
   which measured six weight spaces of dimension 8). Three pairwise non-isomorphic irreducibles of
   multiplicity 2 give commutant `M₂ × M₂ × M₂`, dimension 12 — and **dimension is preserved under
   base change**, so the ℚ-commutant is 12-dimensional.
2. **It contains `F₆ = ℚ[ad(x₈)|₄₈] ≅ K(√77)`**, a degree-6 field (addendum 2).
3. **Its centre is `K`** (memo 204 CELL 3: `ℚ[ad(x₈)²]` is a degree-3 field in the commutant).
4. A 12-dimensional ℚ-algebra with centre `K` (degree 3) is **4-dimensional over `K`** — a
   **quaternion algebra over `K`**, containing `K(√77)` as a maximal subfield.

> **So: `E` is split ⟺ that quaternion algebra over `K` is split, i.e. `≅ M₂(K)`.**

## And one place-condition is already settled

`K` is **totally real** with three real places. The Killing signature of the 28 is `(+16,−12) =
so(4,4)`, the **split** real form (memo 204 CELL 2). So the quaternion algebra is **unramified at
every real place**.

> **It is therefore split iff it is unramified at every finite place too** — a statement about a
> finite ramification set of even cardinality, and nothing more.

## One further constraint, computed rather than assumed

`ad(x₈)` and `ad(x₁₆)` both lie in the commutant (both are central in the 30) and they **commute**.
A commutative subalgebra of a quaternion algebra is at most quadratic over the centre, so
`ℚ[ad(x₈), ad(x₁₆)] ⊆ F₆`: **`ad(x₁₆)` lies in `ℚ[ad(x₈)]`.** The two dual-pair charges do not give
independent handles on the commutant — which is why the remaining six dimensions need the full
computation, and why the cheap routes are exhausted.

## Stated as what it is

**This closes nothing.** It converts an intractable linear-algebra computation into a question about
the ramification of one quaternion algebra over one totally real cubic field — a question a seat with
a number-theory package (`pari`/`sage`) could answer directly, and this bench cannot with `sympy`
alone. **It does not change addendum 2's headline either way:** `ℚ(√77)` is where both obstructions
die, whether or not `E` was already split over `K`.

*Gate 5 untouched. Nothing promotes.*
