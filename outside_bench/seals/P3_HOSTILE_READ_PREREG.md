# SEAL — THE HOSTILE READ OF P3 (THE PAPER)

**Sealed 2026-08-29, committed and pushed BEFORE any computation in this cell.**

Subject: `papers/P3_THE_PAPER/main.tex` at **`89affd5b`** (`THE PAPER currency pass`), the
paper's newest state on `main`. Spec at the same commit.

Why this cell exists: the paper's own SPEC lists, under **§11 build plan item 6** and under
**"what remains before submission"**, *a hostile read*. This bench is the seat for it. The read is
adversarial by assignment: the object is to find what a referee would find, and to find it by
exact computation rather than by opinion.

---

## 0. The honesty clause this seal exists to enforce

Memo 147's transferable lesson was that a criterion written loosely enough licenses whatever the
data shows. A hostile read has the mirror hazard: **an adversarial reader can always produce
findings**, so a seal that does not fix in advance what counts as a finding is worthless.

Two clauses, both binding:

1. **Every finding must be a defect provable by exact computation or by exhibited internal
   contradiction between two passages of the paper.** Matters of taste, emphasis, framing,
   or "a referee might not like it" are NOT findings and are reported, if at all, in a separately
   labelled advisory section that claims nothing.
2. **Blind vs confirmatory is declared per cell, now.** I have already read the draft once. Cells
   whose answer I scoped by that reading are marked **CONFIRMATORY** and their agreement with my
   expectation is worth strictly less than a blind cell's. Cells I have not scoped are marked
   **BLIND**. Declaring this is the only way the distinction survives contact with a favourable
   result.

## 1. The cells

### H1 — the displayed forcing of §4 · **CONFIRMATORY** (hand-scoped on first reading)
Recompute symbolically, exactly, over ℚ: the three linear anomaly conditions on an SM-shaped
15-plet, the claimed reduction to a line, the claimed cubic `-18(t-3)(t+3)`, and the full solution
variety.
- **H1-SOUND** — all three linear relations, the cubic as an exact polynomial identity, and the
  solution set reproduce as displayed, with no branch of the variety unaccounted for.
- **H1-DEFECT** — any relation, the cubic, or the completeness of the displayed solution set fails.

### H2 — the two survivors' description · **CONFIRMATORY**
§4 describes the same pair twice: once as *"the Standard Model 15-plet up to overall scale, and its
conjugate"*, once as *"(1,-4,2,-3,6) and (1,2,-4,-3,6): the Standard Model, and the Standard Model
with u^c <-> d^c relabelled"*. Decide by exact computation whether both descriptions denote the
same two-element set.
- **H2-CONSISTENT** — they do.
- **H2-CONTRADICTION** — they do not, and one of the two sentences is false as written.

### H3 — Theorem 2.1's proof · **BLIND**
The paper's only formally stated theorem. Check every arithmetic step exactly, and check the
proof's completeness against the standard meanings of its undefined term **"conductor"**.
- **H3-COMPLETE** — the arithmetic is exact AND every standard reading of "conductor of the
  metallic grammar R^m L^m" leaves m = 1 the unique solution.
- **H3-GAP** — some standard reading admits an m > 1 whose modulus is McKay-type, so the theorem
  as stated depends on a definition the paper does not give.

### H4 — the abstract's ledger summary against the §7 table · **CONFIRMATORY**
Count row types in the §7 table exactly and compare with the abstract's enumeration.
- **H4-MATCH** — the abstract's enumeration is the table.
- **H4-MISMATCH** — it is not, and the direction of the error (for or against the paper) is stated.

### H5 — §9's falsifiers against the body · **CONFIRMATORY**
Mechanically: every technical referent used in a falsifier must be defined or introduced somewhere
in §§1-8. A falsifier for a claim the paper never makes is a defect, because a falsifier matrix is
the paper's contract with a referee.
- **H5-GROUNDED** — every referent resolves in the body.
- **H5-DANGLING** — one or more do not; each is named with the term and the falsifier.

### H6 — the 252 / 222 / 2 census · **BLIND**
§4's flagship number. Recompute the candidate count, the colour-condition kill count, and the
survivor count independently, from the paper's own stated alphabet and conditions, without reading
the corpus's implementation first. If the paper's statement does not determine the enumeration,
**that under-specification is itself the finding**.
- **H6-REPRODUCED** — 252 / 222 / 2 reproduce from the paper's stated setup.
- **H6-DIVERGENT** — they do not, or the paper's text does not determine the enumeration.

### H7 — Gate 5 on the draft · **BLIND**
Scan the full source for measured physical values. The programme's Gate 5 permits a measured value
ONLY as a comparison target for a computed negative.
- **H7-CLEAN** — every measured value present is a comparison target for a computed negative.
- **H7-BREACH** — some measured value enters a derivation.

## 2. What this cell may NOT conclude

It may not conclude that the paper is right. A hostile read that finds nothing has found that
*these cells* found nothing, on a draft with no bibliography and no per-claim citations — and the
absence of those two is a fact about the draft's stage, not a finding of this read.

It may not conclude that any defect it finds is fatal. Defect severity is the owner's and cc's
call. This bench reports the defect, the exact computation establishing it, and the smallest repair
that removes it.

## 3. Gate 5

No measured SM value enters any computation in this cell. H7 *reads* the draft for measured values;
reading a paper's text is not a derivation.

## 4. Standing

Nothing here is transmitted anywhere. This is a bench memo on `claude/outside-bench`, addressed to
the owner and to the seats. `golden_gate` receives nothing.
