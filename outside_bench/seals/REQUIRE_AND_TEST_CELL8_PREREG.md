# PREREGISTRATION — CELL 8: the latent witness — assemble, verify, then price

*Outside bench, 2026-09-14. Sealed before any artifact is loaded or any manifold scored. Gate 5 untouched.*

## What this cell is, and why assembly comes first

Cell 7 split the table: **chirality is a FORCED failure** for m004 — the only solve is a chiral object.
The standing rule is to **exhaust the repository before building**. Three banked artifacts, never
cross-referenced by any arc, appear to already contain the answer:

| predicate | artifact | what it holds |
|---|---|---|
| **P_atom** | `frontier/B1186_family_is_112/verification/family_census.json` | the 112 manifolds of 212 641 whose shape field is ℚ(√−3) (`members_B`) |
| **P_chir** | `frontier/B1235_two_seat_harvest/verification/chirality_112.json` | per-member `is_amphicheiral` — B1186's own field was **orientation-blind** and is retracted by its `ADDENDUM_2026-09-02_chirality_B1235.md` |
| **P_3** | `frontier/B1321_l205_the_siblings_localized_count/verification/b1321_class_search.json` | the census members with \|det(A − I)\| = 3 |

and a fourth number is banked separately: `frontier/B1292_.../verification/m202.py` computes
**96 surjections π₁(m202) ↠ SL(2,𝔽₃)**, with m004's 48 as its in-run control.

## THE ASSEMBLY (read the record first, state what it implies)

Intersect the three artifacts as committed and report the result **before computing anything**. The
claim under test, stated now so the cell cannot be re-aimed:

> **PREDICTED FROM THE RECORD: m202, s959, v3551 and o9_40999 satisfy P_chir ∧ P_atom ∧ P_3, and m202
> additionally satisfies P_2T — so m202 scores 4 of 4 where m004 scores 2 of 4.**

**No arc states this.** The nearest is B1292, which checked m202 against a four-clause hatch and called
it *"a witness meeting every clause"* — but **chirality was not one of its clauses**, and B1292 predates
B1235's chirality correction.

## THE VERIFICATION (one code path, this cell's own)

Re-score **m004, m412, m202, s959, v3551, o9_40999, v3461, o9_43931** with
`outside_bench/certificates/require_and_test_cell6.py::score` — the same function Phase 1 used — so
every number in the memo comes from this certificate (#20) rather than from four arcs' conventions.

**The genuinely new measurements**, which no arc has run:
- **P_2T for s959, v3551, o9_40999, v3461, o9_43931** — the only 2T counts banked anywhere are m004 = 48
  and m202 = 96.
- **P_atom for v3461 and o9_43931** — predicted **False**, since B1186's enumeration is census-complete
  and neither is in `members_B`.

## THE TWO OUTCOMES

- **OUTCOME A — the assembly is CONFIRMED by the verification.** The record already contained a
  four-predicate witness and never said so. m202 is named, and the cell proceeds to price it.
- **OUTCOME B — the verification CONTRADICTS the assembly.** Some manifold scores differently on one
  code path than the three artifacts imply. Then **the latent witness is an artifact of mixed
  conventions — three banked JSONs that do not compose** — and that is the result, reported as such.

## THE PRICING (owner's instruction: score and price, do not adopt)

If OUTCOME A: price what adopting m202 would cost, **link by link against `docs/THEOREM_LEDGER.md`
C1–C54**, and state plainly the thing that is expected to hurt:

> **The genesis chain C1–C5 DERIVES m004** — two records, one cusp, H₁ = ℤ. **m202 has two cusps and
> H₁ = ℤ ⊕ ℤ.** So m202 cannot be *derived* by the existing genesis; it can only be **selected**. Which
> links survive, which break, and what would have to be re-derived — named, not waved at.

**This cell does NOT recommend adoption.** That is the owner's call.

## FENCES TO CARRY, from the arcs' own words

- B1292: m202's commensurability is *"argued, not certified"* (the invariant trace field needs Sage,
  absent here). **B1186's census certifies the shape field exactly** — stronger than B1292 knew.
- B1292: *"'Keeps E₆' is inferred from 2T via the McKay door, not recomputed here."* And Phase 1 Cell 2
  measured the 2T door at **33.92 %** of the census, so that inference is weaker than it reads.
- B1292 on itself: *"nothing here claims m202 is the object — m004 is the object by the programme's own
  axioms and its genesis theorem."*
- B1321's *"none of which keeps the golden face"* means the **golden ℚ(√5) Alexander face** `t² − 3t + 1`,
  **not** the ℚ(√−3) atom. `frontier/B1302_the_sibling_m202` §3: *"'leave the knot, keep the field'
  keeps ℚ(√−3) and 2T only."* **The cell must quote this before scoring and must not infer it.**

## TWO LIVE INCONSISTENCIES — recorded, not silently resolved

1. B1321 says m202 has *"6 isometries, none swaps the cusps"*; B1302/B1292 report order 12 with 6
   swapping (B1302 §0 Q3 attributes it to `isomorphisms_to` vs `symmetry_group()`). The cell prints
   **both** numbers from its own run and says which it used.
2. A seat's *"7 of 72 tetrahedral manifolds to 12 tetrahedra"* against B1321's six to nine tetrahedra —
   **the 10–12 tetrahedra band is absent from the record.** Named as a gap, not filled here.

## CONTROLS

| # | control | catches |
|---|---|---|
| Q1 | **m004 and m412 re-score exactly as Phase 1 banked them** (m004: ¬chir, atom, 2T raw 48, det {0:2,4:2}; m412: chir, atom, 2T raw 0, det {0:4,4:4}) | a changed code path silently rescoring the baseline |
| Q2 | **m202's 2T count must reproduce B1292's 96**, and m004's 48 alongside it | a 2T counter that disagrees with the one banked arc that ran it |
| Q3 | the three artifacts are loaded and their **sizes asserted** (112 members, 112 chirality rows, 6 three-line members) before any intersection | intersecting a truncated or wrong file |
| Q4 | every manifold scored is reported even when it fails — **no silent drops** | a witness list that looks clean because failures vanished |
| Q5 | the observable is exactly the predicate and no more (Cell 7's ADDENDUM 1 lesson) | the third mis-specification of this programme |

## WHAT THIS CELL MAY NOT CONCLUDE

That m202 should replace m004. That m202 supplies physics — nothing here touches the SM, and I-26
remains UNEARNED (B1292 says so itself). That the four predicates are the right four: they are the four
this programme has base rates for. That "keeps E₆" follows from the 2T door. No value.
