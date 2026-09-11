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
