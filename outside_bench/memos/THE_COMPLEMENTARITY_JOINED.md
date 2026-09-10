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

---

# ADDENDUM 1 — WHAT THIS DOES TO THE GOAL, AND TO MY OWN LAST REPORT

**2026-09-10.** Owner: *"how do we proceed towards the new goal, and how does your recent findings
reframe your last report"*. Read against `docs/WHAT_WOULD_COUNT.md` §4A, which is the new goal and
which I had not read when I gave that report.

## 1. §4A.0's fourth pillar is not a theorem, and it says so itself

The old Tier 2 was retired on four legs. Three are theorems — **B666** (the scale-torsor no-go,
`Hom(G, ℝ₊) = 0` for finite/profinite `G`), **B936** (value-invisibility), **B1096** (the anomaly
layer identically zero). The fourth is the seven sealed misses, and §4A.0 flags it in its own words:

> *"This leg is **empirical exhaustion, not theorem** — the distinction matters and is kept below."*

**§4 of this memo is a candidate theorem for exactly that leg**, and K3 is the test that decides.
That is now the sharpest single target this bench has: not new territory, but converting the one
non-theorem pillar of the programme's own retirement argument.

## 2. Three of the programme's walls may be one lemma

* **B666** — `Hom(finite G, ℝ₊) = 0`. A finite group has no nontrivial map to a torsion-free one.
* **B1227** — a mirror-odd invariant valued in a **torsion-free** abelian group satisfies `2I = 0`
  hence `I = 0`.
* **Dirichlet, rank 0** — being's unit group is **finite**, so its regulator is identically 1: no
  growth to measure.

All three are *"a finite thing cannot fill a torsion-free slot."* One lemma, three domains, three
separately-named walls. It is elementary, which is precisely why nobody joined them — each looked
like a fact about its own subject.

**Measured, extending §2's method to eight arcs (B318, B666, B1069, B1095, B1216, B1222, B1227,
B1276): 56 ordered pairs, 16 citations — all of them in ONE cell, `B1069 → B666`, one-directional.
Fifty-five of fifty-six pairs are empty.**

## 3. B1095 is a POSITIVE confirmation, not merely an absent counterexample

K1 asked for a banked result deriving orientation from hearing. What the corpus has is the
opposite, computed and banked, on the hearing platform itself. **B1095**, the lab lane:

> *"the hand is spectrally **INVISIBLE**, not merely IDS-blind"* — max difference **1.3 × 10⁻¹⁵**
> across 2584 eigenvalues — and *"**ENERGIES ARE P-INVARIANT (FORCED), LOCALIZATION IS
> P-EQUIVARIANT (FREE)**"*.

The Fibonacci chain **is** the hearing face. The hand — orientation — is invisible to its spectrum
to machine precision, and the split runs *inside one computation*: energies (magnitudes, hearing's
commodity) cannot carry the P-bit; localization (a labelling, torsion-shaped) can. B1095 is a
lab-lane result that knew nothing of this; it confirms the complementarity from outside.

*Honest limit, in B1095's own words:* at **odd** Fibonacci index the reversal fails at the two
cut-adjacent letters and isospectrality breaks (0.147). The invisibility holds at reversal-closed
index and is a theorem about those windows, not everywhere.

## 4. How the eight-row report changes

| row | what I reported | what it should say now |
|---|---|---|
| **2 chirality** | *"wall … unless Phase 2's chiral-cover test finds otherwise"* | **a theorem with a named escape.** The object cannot carry a count in ℤ — for *every* mirror-odd invariant, not the tried ones — because ℤ is torsion-free (B1227) and orientation lives only on the rank-0 faces. **The generation number must come from the carrier.** A redirection, not a gap |
| **3 values** | *"0 of 19; open"* | **three of the four closing legs are theorems and the fourth is not**, by §4A.0's own admission. §4 is a candidate theorem for it. Compression (4A.3) is untouched by all four |
| **7 predictions** | *"conditional — P9, a Z′ regime"* | **under-reported.** Tier-INTERFACE is stronger and live: a **function** `ρ ↦ edge content`, refutable on an **existing** photonic/polariton platform, theory complete (B1085/B1095), **owner-pending on the L173 unseal decision.** It waits on a signature, not a computation |

## 5. And a correction to my own ranking, one turn old

I ranked the paths as *box D's dictionary → re-grade row 2 → the 54 covers*. Having read §4A that
ranking is wrong on its own terms. The dictionary question sits inside 4A.3, whose **tested** ground
B1076 already closed at four gauges; the licensed successors are three named structural doors, none
a data contact. And **Tier-INTERFACE outranks all of it**, because it is the only tier that touches
an instrument and the only one whose blocker is a decision rather than work.

**Revised, and this one is read off the goal document rather than off my own enthusiasm:**

1. **Tier-INTERFACE** — spec-complete, owner-pending. *Not ours to advance; ours to state clearly.*
2. **K3** — convert §4A.0's fourth pillar from empirical exhaustion to theorem. Ours, and decisive
   either way; four ways to die, already fixed.
3. **Re-grade Tier-STRUCTURE's one open item** (chirality) from *open* to *closed on the object,
   open on the carrier*. Ours, cheap, and it is a re-grade with a proof behind it.
4. **Type the three 4A.3 doors by commodity** — which of the gauge-datum question, L154's σ, and
   B882's S₃-equality asks for growth and which for torsion. Nobody has sorted them, and §1 gives
   the sorting rule.

*Nothing here promotes. Gate 5 untouched.*
