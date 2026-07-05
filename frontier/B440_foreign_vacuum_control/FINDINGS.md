# B440 — C3 foreign control: the SL(2,C) vacuum spectra of K(5,1) — no figure-eight-unique feature

**Status: banked (C3 complete), then CORRECTED (2026-07-05, adversarial review). The raw
character-variety polynomials stand; the READING was wrong — the "golden inversion" is retracted
as an artifact (see §CORRECTION). The corrected verdict is a cleaner, stronger negative.
Firewalled.**

> **CORRECTION (2026-07-05, adversarial review — verified independently).** The first cut read
> 5₂'s degree-6 tr(A) polynomial as "6 irreducible vacua including a golden factor" and inferred
> a **golden inversion** (child golden-free, only 5₂'s child golden). **Both are wrong.** The
> golden factor **x²+x−1 is the REDUCIBLE abelian ℤ/5 characters** (A,B diagonal with 5th-root
> eigenvalues ⇒ [A,B]=I ⇒ tr[A,B]=2), not an irreducible vacuum — and those golden abelian
> characters are **universal**: H₁=ℤ/5 forces them for **every** K(5,1) (verified from the
> abelianization exponent-sums for 4₁, 5₂, 3₁, 6₁). They surfaced in the raw tr(A)-elimination
> only for 5₂ (whose abelian rep has B=I) — a parametrization artifact of the A-upper/B-lower
> chart. **Corrected:** 4₁ and 5₂ both have **exactly 4 irreducible vacua in the identical −283
> field**; the "golden inversion" is retracted. The corrected reading is the honest table below.

## The complete spectra (irreducible SL(2,C) characters of the closed manifolds)

Computed convention-free from π₁ (2-generator groups): A=[[m,1],[0,1/m]], B=[[k,0],[t,1/k]],
both relators = I, eliminated to the meridian trace x = tr(A).

| K(5,1) | **irreducible** vacua | irreducible trace poly | field | (reducible golden) |
|---|---|---|---|---|
| **4₁ [child]** | **4** | x⁴−3x³+x²+3x−1 | **−283** | — (didn't surface in this chart) |
| **5₂ [neighbour]** | **4** | x⁴−4x³+4x²+x−1 | **−283** (same field) | +2 golden abelian (surfaced) |
| 3₁ [Seifert] | 5 | x⁵−x⁴−4x³+3x²+3x−1 | disc 11⁴ | — |
| 6₁ | 11 | (deg-11 irreducible) | disc 1722667·2680091 | — |

The **golden ℚ(√5) characters are reducible abelian ℤ/5 characters, present for ALL FOUR** (the
"reducible golden" column is a chart artifact of where each knot's B=I abelian rep lands in the
tr(A)-elimination, not a real difference). The honest irreducible spectra: **4₁ and 5₂ both have
4 vacua in the same −283 field.**

## Cross-validation (two independent methods agree)

The child's character-variety quartic **x⁴−3x³+x²+3x−1 is identical to B439's A-polynomial
quartic** (Cooper–Long on L=M⁻⁵). The closed-manifold character variety and the A-polynomial
intersection give the same 4 vacua — mutual confirmation, no shared code path.

## The tier-3 verdict — NO figure-eight-unique feature (break criterion applied; corrected)

1. **The −283 field is commensurability-shared — and so is the irreducible count.** Both 4₁ and
   5₂ have **exactly 4 irreducible vacua** in the **same** −283 field (the two quartics generate
   the same field: the child root β = −r³+3r²−r−1 for r a root of 5₂'s quartic; mutual
   containment). Tier-2, exactly as B438 predicted from the trace field and the 121 value — and
   now even sharper (same count, same field).
2. **The count across knots (4/4/5/11) is genericity.** Where it differs (3₁, 6₁) it tracks the
   A-polynomial degree, not the parent's distinctive arithmetic — fails break criterion (c).
3. **The golden ℚ(√5) characters are numerator-forced reducibles, universal.** They are the
   abelian ℤ/5 characters (H₁=ℤ/5), present for **all four** fillings, reducible ([A,B]=I). They
   are not a parent-fingerprint and carry no figure-eight-vs-5₂ signal. *(The earlier "golden
   inversion" reading — golden only in 5₂'s child — was an artifact; retracted, see §CORRECTION.)*

**Reading.** Surgery launders identity. Even against its closest arithmetic sibling (5₂,
commensurable, sharing the −283 field and the 121 torsion value), the child is generic: it
shares the field **and the irreducible vacuum count**, differs only where genericity (A-poly
degree) makes any two distinct knots differ, and the golden characters are the forced ℤ/5
abelian reps common to all. The corrected reading is **stronger** than the retracted one: the
object's forced child inherits its parent's commensurability class down to the SL(2) vacuum
count, and **nothing finer**.

**Bar note:** forced ✓, unsought ✓ (registered three-outcome), control ✓✓ (slope AND foreign,
both-sided coverage complete). A NEGATIVE that sharpens the target — no physics promotion.

## For the campaign

C3 is complete. The next knot-dependent channel is **C5 (WRT via surgery)** — the quantum
invariant is built from the parent's colored Jones, knot-specific in a way the trace field is
not, so it is the sharpest remaining place a figure-eight fingerprint could survive. (C4, the
E₆ lift of these vacua, composes the banked Sym^{2m} machinery on the 4 child vacua.)

**Provenance.** charvar.sage → charvar.json (sage, from π₁); verify.py → verdict.json (sympy);
lock tests/test_b440_foreign_vacuum_control.py (4/4). Cross-refs: B439 (the held verdict, now
resolved), B438 (the tier-3 bar), B437 (the Inversion Law), B436/B434 (the −283 child),
docs/AUDIT_2026-07-05.md.
