# PREREGISTRATION — CELL 7: the parity classifier

*Outside bench, 2026-09-14. Sealed before the certificate runs. Gate 5 untouched.*

## The gap

`docs/THEOREM_LEDGER.md` row **T-MIRROR-ODD-VANISHES** (B1227, PROVED), verbatim:

> **For an amphichiral object, every mirror-odd invariant is 2-torsion in its value group — so the
> group's torsion decides the conclusion.** … the σ wall (ℝ/½ℤ: B1012, B1064), the selector wall (ℝ:
> B1225) and the chirality wall (ℤ: B1294, B1297) **are ONE theorem in three value groups — the corpus
> had tracked them as three.**

A fourth group was added at B1305 (formal q-series, the colored-Jones ends' ratio).

**The theorem is stated about INVARIANTS. Phase 1's table is about REQUIREMENTS. Nobody has asked which
requirements are mirror-odd.** That is this cell, and it is one question.

## THE CLASSIFICATION, derived before it is tested

| predicate | claimed parity | the derivation |
|---|---|---|
| **P_chir** | **ODD** | it *is* the mirror bit |
| **P_2T** | **EVEN** | π₁(M̄) ≅ π₁(M) as abstract groups — orientation is not part of the group — so the set of surjections onto SL(2,𝔽₃) is literally the same set |
| **P_atom** | **EVEN** | the mirror's tetrahedron shapes are the complex conjugates of M's; an imaginary quadratic field is closed under conjugation, so the shape field is unchanged |
| **P_3** | **EVEN** | an isometry of M̄ is an isometry of M with cusp map conjugated by an orientation-reversing J; det is conjugation-invariant, so \|det(A − I)\| is unchanged, and orientation-preserving classes map to orientation-preserving classes |
| **values** (CS, the real selector, net chirality, the Jones ends' ratio) | **ODD** | B1227's own four value groups, cited not re-derived |

## THE TEST

**Mirror-odd ⟹ m004 LACKS it.** Checked against Phase 1's banked table.

- **OUTCOME A** — every mirror-odd requirement is one m004 lacks, and the mirror-even ones are **not**
  determined either way (m004 has two, lacks one). Then **rows 1 and 4 of the table are one theorem, not
  two facts**, and **the count of three is the only row m004 fails for no theorem-reason** — the
  contingent row, and therefore the one worth chasing.
- **OUTCOME B** — some mirror-odd requirement m004 **has**, or a parity cannot be settled by computation.
  Then the law does not organise the table and the rows stay five independent facts.

## THE CONTROL THAT MATTERS

**An assignment that cannot be wrong is not an assignment** (#164, MB12). So each parity is **measured,
not asserted**: every predicate is computed on **m004 and on its mirror**, and

- the predicates claimed EVEN must return **the same value** on both;
- the predicate claimed ODD must return **different values** on both.

A claimed-even predicate that differs, or a claimed-odd one that agrees, **fails the cell**.

**Control C-DISC — the test must be able to discriminate.** The same even/odd check is run on a
**chiral** manifold (m412, from Phase 1 Cell 5), where P_chir must still separate M from M̄ in the sense
the certificate defines, and the even predicates must still agree. If every predicate agrees on
everything, the instrument is not measuring parity at all and the cell says so.

**Control C-POP** — the number of predicates checked is printed and asserted > 0 (the `B1197` trap).

## WHAT THIS CELL MAY NOT CONCLUDE

That mirror-even requirements are satisfiable — the law says nothing about them, which is the point.
That the four value groups are exhaustive — B1227's list is cited, not extended. That any requirement
outside §A has been classified. No value.
