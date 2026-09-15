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

---

# ADDENDUM 1 (2026-09-14) — THE OBSERVABLE CARRIED MORE THAN THE PREDICATE

**Control C-EVEN failed on `5_2 : P_atom` in the first run.** The instrument was right; **the seal's
observable was wrong.**

**P_atom is the predicate `all_in_Q(sqrt-3)`** — a boolean. The certificate's observable bundled the
**list of tetrahedron-shape minimal polynomials** alongside it, and compared *that*. The boolean agreed
on every manifold (m004 True/True, m412 True/True, **5₂ False/False**). Only the polynomial list
differed, and it differed for a stated reason:

| | 5₂ | its mirror |
|---|---|---|
| shape min polys | `[1,−2,3,−1]`, `[1,−2,1,−1]` | `[1,−3,2,−1]`, `[1,−1,2,−1]` |

**These are exact reciprocals.** Reversing `[1,−2,3,−1]` gives `[−1,3,−2,1]`; negating gives
`[1,−3,2,−1]`. Same for the second. A polynomial and its reciprocal have roots z and 1/z, which
**generate the same field** — so the *field* is unchanged and P_atom is mirror-even, exactly as the seal
derived. What changed is SnapPy's normalisation of the shape under `reverse_orientation`, a **convention
of the triangulation, not a fact about the manifold.**

**CORRECTED CONTROL C-EVEN, and it is strengthened rather than weakened:** the claimed-even predicates
must agree as **predicates**, **and** wherever the shape-polynomial lists differ, the certificate must
**verify that the two lists are related by polynomial reciprocal** — the explanation is computed, not
asserted. A difference that is *not* reciprocal still fails the cell.

**This is the third mis-specified control in this programme** (Cell 3's L1 imported a number from the
wrong frame; Cell 4's M2 chose a probe that could not pass; this one bundled convention-dependent data
into a predicate). All three were caught by controls rather than by re-reading, and all three were this
bench's own seals being looser than the thing they were testing. **The pattern is now named: an
observable must be exactly the predicate, and no more.**

**Not changed:** the parity claims, the test, the two outcomes, or C-DISC.
