# 201 — THE MEASURED PLANE IS NOT A CHOICE: the object partitions its own four charges, and both blocks carry K

**Date** 2026-09-11 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/six_planes_77.py` · **Output** `outputs/six_planes_77_out.txt` +
`outputs/six_planes_77_branch.json`
**Seal** `seals/SIX_PLANES_77_PREREG.md`, sha256
`be58d6ce51c3b2a636d2bbacd462146de63cfcd1158b3657689860c405bb8016` — **sealed before the
certificate was written**
**CELL 1/2/3 = B/B/B · six controls, all passing · Gate 5 untouched**

**Occasion — the owner: "go after physics."**

`docs/WHAT_WOULD_COUNT.md` §4A.3 leaves exactly three licensed targets for the value layer after
B1076 closed everything else. B1077 says of one of them: **B882's conjecture is "the UNIQUE
non-circular route to a 77-mechanism."** That is the door this memo works.

---

## 0. The state of the door before this run

* **B1077 (PROVED).** The object's **bare** D₄ geometry carries **nothing 77-shaped** — even
  Clifford algebra `M₈(ℚ)×M₈(ℚ)`, centre `ℚ×ℚ`; at the trialitarian level the split cubic `ℚ³`,
  trivial discriminant. *"Every 77-bearing structure in the corpus is therefore DRESSING."*
* **The floor-lift** (Dolphin–Quéguiner-Mathieu, Def. 4.2 / Rem. 4.8): a trialitarian triple has
  trivial discriminant **by definition**; `ℚ(√77)` can enter only through the twisted **³D₄** form.
  B882 in KMRT's language: *the dressed datum is the ³D₄ twist of the split triple by K.*
* **The blocker, in B1077's words:** *"the only dressing source in the bank is the pencil triple —
  forbidden as a twist-source by the circularity theorem-let."* The pencil's branch locus **is** μ
  by construction.

**That argument has one load-bearing premise: that the measured plane is a free choice.** This
memo tests the premise.

## 1. The gap nobody had run

B886's matter pencil `P(x,λ) = det(xI − ρ(x₈) − λ·ρ(x₁₆))` is built on **one chosen pair** of the
object's **four** superselection charges — `INV[8], INV[14], INV[16], INV[22]`, at invariant degrees
`2×(4,7,8,11)`. There are **six** pairs. **The pencil had only ever been built at one of them.**

All six pairs commute exactly (control C2), so the pencil is defined at every plane. B886 reproduces
at its own plane — shape `F₁¹·F₂⁸`, branch locus the banked μ **coefficient for coefficient**
(control C1). Everything exact: rational 27×27 matrices, exact charpolys, 28-point exact
interpolation, exact factorization over ℚ.

## 2. What the six planes give

| plane (exponents) | factorization shape (deg in x, mult) | branch locus | resolvent |
|---|---|---|---|
| (4,7) | (3,1) (6,1) (6,3) | sextics | **−3, −231** |
| **(4,8)** | **(3,1) (3,8)** — all cubic | **the cubic μ** | **77** |
| (4,11) | (3,1) (6,1) (6,3) | sextics | **−3, −231** |
| (7,8) | (3,1) (6,1) (6,3) | sextics | **−3, −231** |
| **(7,11)** | **(1,3) (6,1) (6,3)** — a LINEAR factor | **two cubics** | **77** |
| (8,11) | (3,1) (6,1) (6,3) | sextics | **−3, −231** |

**CELL 3 = B.** Four planes share one generic shape. The **(4,8)** plane — the one the entire 77
story rests on — is the **only** one factoring into cubics alone. The **(7,11)** plane is the only
one carrying a **linear** factor: a joint weight **rational over ℚ**. The two exceptional planes are
exactly the two B888 named, and they are exceptional in **opposite directions**.

## 3. The resolvents close into a Klein four-group, and one leg is the being face

**CELL 1 = B** — the resolvent is not plane-invariant. **The way it varies is the result:**

    -231 = -3 x 77

so `{−3, 77, −231}` is **closed under squarefree product**. The charge system's resolvent data is a
**Klein four-group `{ ℚ(√−3), ℚ(√77), ℚ(√−231) }`** — and **ℚ(√−3) is the being face.**

**And the partition is computed, not chosen.** Resolvent **77** at exactly `{4,8}` and `{7,11}`;
`{−3, −231}` at all four planes that **mix** the two blocks.

> **The object's four superselection charges split into two blocks of two. A pencil within a block
> gives 77; every pencil across the blocks gives {−3, −231}. Nothing selected that partition.**

## 4. B888's echo is a coincidence of one plane — withdrawn, and replaced by something better

**CELL 2 = B.** *"The resolvent remembers exactly the complementary exponent pair"* — B888's own
*"observation, unweighted, no mechanism claimed"* — holds at `(4,8) → 7·11 = 77` and **fails at the
other five**, including at `(7,11)`, whose complement product is `4·8 = 32` and whose resolvent is
**77 again**. The echo is withdrawn as a mechanism. What replaces it is §3, which is stronger: the
77 is not about exponent arithmetic, it is the **within-block** resolvent of a partition the object
computes for itself.

## 5. And the unmeasured plane produces **K itself**

The `(7,11)` pencil — built from the **two charges the measured construction never used** — has
branch cubics that are **not** μ (no shared root over ℚ; discriminants carrying `19¹²` where μ
carries `13¹²`) and that nevertheless **generate a field isomorphic to K**.

    (7,11) branch cubic  2771822592000*L^3 + 3033676800*L^2 - 56402640*L - 6859
       resolvent 77 · disc 2^28·3^10·5^6·7^3·11·19^12 · shares a root with mu: False · GENERATES K: True
    (7,11) branch cubic  1686085632000*L^3 - 94043980800*L^2 - 34309440*L + 212629
       resolvent 77 · disc 2^32·3^12·5^6·7·11^3·19^12 · shares a root with mu: False · GENERATES K: True

**Control C5 — the test can say no.** Positive control: μ itself is found isomorphic to K. Bite
control: unrelated resolvent-77 cubics are found **not** K.

**Control C6 — the base rate, stated with the claim.** In the window `|a| ≤ 6, |b|,|c| ≤ 30` there
are **3** distinct cubic fields of resolvent `ℚ(√77)`, and **K is one of them** — the one of
smallest discriminant, `6237 = 3⁴·7·11`. **So the field landing, conditional on resolvent 77, is not
rare, and this memo does not claim it is.** The strength is in the **partition**, not in one field
coincidence, and the base rate is printed so it cannot be read the other way.

## 6. Why this moves the door

B1077's circularity argument needs the measured plane to be a free choice. **It is not.** The
object's own factorization singles out `{4,8}` (all-cubic) and `{7,11}` (a rational joint weight)
out of four mixed planes that demonstrably give **different** arithmetic — and **both distinguished
planes carry K**. A datum reached from **two disjoint pairs** of charges, with the four cross-pencils
returning `{−3, −231}` instead, is not an artifact of which pair was picked.

**The blocker's premise is refuted. The door is not closed by circularity.**

## 7. What this does NOT do, stated plainly

* **It does not prove B882's conjecture.** The remaining half is the ³D₄ twisting classification —
  a literature proposition, and this bench does not close it here.
* **No value, no ratio, no prediction, no measured quantity anywhere.** Gate 5 untouched.
* **It does not decide the other two §4A.3 doors** (the gauge-datum question; L154's σ).
* **It does not claim the V₄ of resolvents means anything yet.** That `{ℚ(√−3), ℚ(√77), ℚ(√−231)}`
  is a Klein four-group containing the being face is **computed and recorded**. Whether it is the
  same V₄ as B730's faces is exactly the kind of identification B1223 killed once already, on the
  **action**, and memo 200 typed by **kind**. It is **not** asserted here.

## 8. BENCH ERROR #21 — a preregistered outcome text that carried a rider

The seal's **CELL 1 outcome B** reads, in full: *"the resolvent **varies** with the plane. Then 77
is a property of which two charges were measured, **the (4,8)-plane has no privileged status**, and
B882's door closes on its own circularity."*

**The measurement is B. The rider is false, and it is refuted by CELL 3 of the same seal.** The
(4,8) plane *does* have privileged status. I wrote a consequence into an outcome slot instead of
writing only the observable, and another cell in the same preregistration then contradicted it.

**The rule this buys: a preregistered outcome states only what will be OBSERVED. Consequences go in
the interpretation section, where a later cell can overturn them without corrupting the seal.**
The seal is unedited; this is the correction, filed at the point of occurrence.

*Gate 5 untouched — no measured value is used or named. Nothing promotes to `CLAIMS.md`. No arc is
retracted; one "observation, unweighted" of B888's is withdrawn as a mechanism, and one rider of my
own seal is withdrawn.*

---

# ADDENDUM 1 (2026-09-11, same session) — **THE GENERICITY CONTROL TRIMS THIS MEMO'S READING — and what survives is better than what was banked**

**Certificate** `certificates/six_planes_genericity.py` · **Output**
`outputs/six_planes_genericity_out.txt` · **CELL 1/2/3 = B/B/B**, four controls, all passing.

Run on this bench's own result the same session it was banked, under B1223's rule: *"the value of
a small-group coincidence is not zero, but it is not evidence, and the difference is one
computation."* The analogue for this memo is **randomisation**.

## Trimmed

This memo's §3 and §6 read as though **77 is tied to measuring WITHIN a block**. **It is not.**
Five random 2-planes in the same four-dimensional charge space, all commuting, all exact:

    random plane 1..5:  shape [(3,1),(6,1),(6,3)]   resolvents [-231, -3, 77]   (all five)

**Every generic plane sees all three resolvents.** 77 is not confined to the coordinate planes; it
is everywhere in the space. The measurement in §2 is correct and reproduces (control C1) — the
**six coordinate planes** really do split `{77}` / `{−3,−231}` — but the sentence *"the 77 is the
within-block resolvent of a partition the object computes for itself"* over-reads it.

## What survives, and it is a cleaner statement than the one banked

1. **The Klein four-group is an INVARIANT OF THE CHARGE SPACE**, not an artifact of a chosen pair.
   `{ℚ(√−3), ℚ(√77), ℚ(√−231)}` is what a generic plane sees, 5 of 5. `−231 = −3·77`. One leg is
   the **being face**.
2. **The six coordinate planes are DEGENERATE LOCI.** Each sees a **proper subset** of the generic
   picture — `{77}` within a block, `{−3,−231}` across. A generic plane sees the whole group; the
   coordinate planes go **partially blind**.
3. **Which half goes blind is COXETER DUALITY.** `{4,8}` is the unique complete dual pair among the
   charges (`4+8 = 12 = h`); 7 and 11 are orphans, their duals 5 and 1 carrying no charge.
4. **The orphan kernel is NOT generic** (CELL 1 = B):

       dim ker rho(x8)  (exp 4)  = 0        dim ker rho(x16) (exp 8)  = 0
       dim ker rho(x14) (exp 7)  = 3        dim ker rho(x22) (exp 11) = 3
       six random elements of the same space: 0, 0, 0, 0, 0, 0

   `ker x₁₄ = ker x₂₂` **as subspaces** — one canonical rational 3-space in the 27, annihilated by
   both orphans, invariant under both dual-pair charges, and **no other pair of the four
   annihilates anything at all**.

## And a fourth and fifth route to K, with no pencil in them

Restricting the dual-pair charges to that orphan kernel — **no λ, no branch locus, no pencil**:

    rho(x8)  | orphan-kernel :  x^3 - 10063872x - 9710862336            resolvent 77, GENERATES K
    rho(x16) | orphan-kernel :  2197x^3 - 6963104474726400x + ...       resolvent 77, GENERATES K

## Why §6's conclusion is STRENGTHENED rather than weakened

B1077's blocker: *"the only dressing source in the bank is the pencil triple"* — so any 77 it
yields is circular, the branch locus being μ by construction. **This control shows 77 is not a
property of that pencil at all.** It is visible from almost every plane of the charge space, and K
is reachable with **no pencil whatsoever**. **A datum that shows up from almost anywhere is not an
artifact of where one looked.** The premise of the circularity argument is refuted more firmly by
the control than by the partition story the memo told.

## Three more V₄'s note, recorded and not claimed

`{−3, 5, −15}` (B730's faces), `{−3, 3, −1}` (B1174's branch V₄) and `{−3, 77, −231}` (this run)
each close under squarefree product and **pairwise share exactly the leg −3**. B1174's theorem for
two of them was *"not one torsor — one shared involution."* This is a **third** on the same hub,
found from the charge system rather than from Galois theory. **Recorded. Not claimed to be the same
V₄, not claimed to act** — that identification is precisely what B1223 killed once on the **action**
and what memo 200 typed by **kind**.

*Gate 5 untouched. Nothing promotes. No arc retracted; one reading of my own is.*
