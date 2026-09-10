# 195 — WHAT EACH FACE LACKS, THE OTHER PROVIDES: one theorem, found five times, never joined

**Date** 2026-09-10 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/face_complementarity.py` · **Output**
`outputs/face_complementarity_out.txt` · **Gate 5 untouched**

**Occasion — the owner, in full:** *"what Q sqrroot 5 lacks Q qsrroot 3 provides and viceversa /
maybe reading the results of each failed crossing would help as we expected smthe wlse"*

---

## 1. The question has an exact answer, and it is Dirichlet's unit theorem

B1276/B730: the arithmetic forces **exactly three** quadratic faces — **being** ℚ(√−3),
**hearing** ℚ(√5), **meeting** ℚ(√−15) — the three involutions of `V₄`, with
**being · hearing = meeting**. Unit rank is `r₁ + r₂ − 1`:

| face | field | signature | **unit rank** | units | c = conjugation | what it *provides* | what it *lacks* |
|---|---|---|---|---|---|---|---|
| **being** | ℚ(√−3) | r₁=0, r₂=1 | **0** | μ₆ — **the trit** | **nontrivial** | torsion, orientation, a bit | **growth** — no unit of infinite order |
| **hearing** | ℚ(√5) | r₁=2, r₂=0 | **1** | ±φⁿ, `φ=(1+√5)/2` | **trivial** | growth, a rate, a ratio | **orientation** — mirror-even by arithmetic |
| **meeting** | ℚ(√−15) | r₁=0, r₂=1 | **0** | ±1 | **nontrivial** | torsion, orientation | **growth** |

`N(φ) = −1`, regulator `log φ = 0.481211825…`. Being's regulator is **1 exactly** — rank 0 leaves
nothing of infinite order to measure.

**And the exclusivity is a theorem, not a sample.** For a quadratic field `r₁ + 2r₂ = 2`, so
`(r₁,r₂)` is `(2,0)` or `(0,1)`: unit rank is **1 or 0, never both**, and `c` is nontrivial exactly
in the second case. **Growth and orientation cannot co-occur on one quadratic face.** That is the
owner's sentence, proved: what hearing lacks, being provides; what being lacks, hearing provides;
and no single face can be asked for both.

## 2. The corpus states this at four levels, in five arcs, and joins none of them

| arc | level | what it says |
|---|---|---|
| **B318** | the ℤ/2 | *"the Eisenstein ℤ/2 **is** the geometric amphichiral involution (complex conjugation), the golden ℤ/2 is **arithmetic-only with no geometric τ**"* |
| **B1069** | the Hecke palette | 1,1,2 against 1,2,8 — *"the discriminator is **Dirichlet unit rank** (1 vs 0; the free unit outraces the residue tower)"* |
| **B1216** | the regulator | *"ℚ(√−3) has **UNIT RANK 0** so its regulator is **IDENTICALLY 1**"* |
| **B1222** | the vanishings | the regulator vanishing is *"a **SIGNATURE** fact about the field, **not a symmetry**"* |
| **B1276** | the parity law | *"c acts nontrivially on a quadratic field **IFF the field is IMAGINARY**"* — so hearing is **mirror-even by arithmetic** |

**Measured, by B1276's own method — cross-citation by grep over each arc's whole directory:**

    20 ordered pairs.  0 citations.

Not one of the five names another. **The same theorem, found five times from four directions,
never once joined.** This is precisely the shape B1276 itself reported (*"the same V₄, discovered
twice, never joined"*) — at five.

**Non-vacuity control:** the same grep finds B1276's citations of B1174 and B730, so a zero means
absence and not a broken instrument.

## 3. B1222's surviving residue is the same statement from the other side

B1222 proposed *"the selection is the obstruction"* — one law for ~65 vanishings — with three kill
conditions named in advance, and **was killed by them** (r = +0.50 where it predicted negative).
What it left standing is the sentence this memo needs:

> *"what the data says instead is that symmetry **REDISTRIBUTES** content — removing Chern–Simons,
> modular flow and invariant pairings while **ADDING** homological torsion."*

Redistribution, not removal. And its decisive test was **m003 versus m004** — the same pair memo 194
found split by the bit — noting that m003 *"carries ℤ/5 torsion m004 lacks"*, while B781 records that
*"the golden 5 is field √5 in m004, torsion ℤ/5 in the sister."* **The same 5, relocated between the
archimedean and the finite shadow.** B1222 saw the redistribution and left it as an observation. The
unit theorem says *why* the two locations are the only two.

## 4. The reading of the failed crossings — A HYPOTHESIS, WITH KILL CONDITIONS, NOT A CLAIM

The record holds **seven sealed value crossings, seven misses** (`CROSSING_REQUIREMENTS` §1, §4),
with root causes already extracted: *assumed interpolation* (B915), *wrong hemisphere* (B925),
*missing normalisation* (B929), and four that *died at power* (B1027+B1063, B1066 R-A, B1066 R-B,
B1075). The old success criterion is formally **retired** — *"closed by theorem (B666/B936/B1096)
plus the seven-for-seven exhaustion."*

**The hypothesis.** A measured dimensionless CP-odd value is a **magnitude with an orientation**. By
§1 the magnitude can only come from hearing and the orientation only from being or meeting, and no
one face carries both. So every crossing that asked a single face for a value asked it for a
commodity it provably lacks — and the seven-for-seven is **structural, not statistical**.

**This is NOT banked as a law, and B1222 is exactly why.** B1222 proposed a unification of the
programme's negatives, named its kill conditions in advance, and died on them. A second unification
of the same negatives, proposed the same afternoon it is thought of, gets the same treatment.

**Kill conditions, fixed here, before any sorting:**

* **K1** — exhibit a banked result deriving an **orientation or chirality** datum from the
  **hearing** side. *One found kills it.* (B318 and B1276 both say the opposite, independently.)
* **K2** — exhibit a banked result deriving a **growth rate or running** from **being**.
  *One found kills it.* (B1216 says the regulator is identically 1.)
* **K3, the decisive one** — sort the seven crossings by which commodity each asked of which face,
  **from the sealed text, not from memory**. If any crossing can be classified either way, the
  hypothesis is **vacuous** and dies there. If any crossing asked a face for its **own** commodity
  and still missed, the hypothesis is **false**.
* **K4** — exhibit a banked **positive** structural result that required both commodities from one
  face. *One found kills it.*

**K1 and K2 return nothing on a first corpus pass. K3 IS NOT RUN.** It is the next cell, it requires
reading seven sealed prereg documents in full, and it is the one that decides. Until it runs, §4 is a
hypothesis with a name and a way to die, which is the only honest thing to call it.

## 5. What is banked here, and what is not

**Banked:** the complementarity is exactly Dirichlet's unit theorem; it is **exclusive** by the
signature identity, not by sampling; five arcs state it at four levels with **zero** cross-citations
between them; and B1222's surviving residue is the same statement from the other direction.

**Not banked:** any reading of why the seven crossings missed. That is §4, it is fenced, and it has
four ways to die.

*Nothing here promotes to `CLAIMS.md`. Gate 5 untouched — no measured value is named or used.*
