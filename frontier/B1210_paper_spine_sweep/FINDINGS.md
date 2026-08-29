# B1210 — THE PAPER-SPINE SWEEP: the spec was written from memory, and the corpus says so

**Verdict**: `OPEN` (instrument arc) · **2026-08-29** · **Gate 5 clean** · answers the owner's
question *"does the paper reflect the current state, to the last bit?"* — **it did not.**

## 0. The question, answered by measurement

The P3 spec (B1208) was drafted from the thesis as this seat holds it. The owner asked whether it
reflects the current state. Rather than assert, this arc **measured**:

| | |
|---|---|
| arcs banked in the spec's own last ten days | **85** |
| of those, cited in the spec | **11** |
| law-creating arcs in the corpus (`creates_law = true`, PROVED/NEGATIVE) | **48** |
| of those, cited in the spec | **1** |

**A paper spine assembled from memory reproduces the memory, not the record.** That is the same
defect class the spec itself warned about for `THE_SM_VERDICT.md` — and this arc found the spec
committing the inverse of it within a day of writing that warning.

## 1. The instrument, and its own mid-run correction

`spine_sweep.py` builds the claim pool mechanically (law-creating arcs ∪ arcs cited on the
registered synthesis surfaces = **442**) and then looks for **supersession**: later arcs whose claim
text names a pool arc with a verb of extension, correction, withdrawal or confirmation.

**The first pass was wrong and its wrongness is the useful part.** Matching verbs anywhere in an
arc's claim flagged **229** pool arcs and **15 of the spec's 24 citations** as
extended/corrected/withdrawn. Spot-checking the two most alarming killed the statistic:

- **B1159 was flagged as withdrawing B727.** It does the opposite — *"E₆ is generic (B727), inherits
  A's non-payment"* **cites** B727's genericity.
- **B978 was flagged as withdrawing B862 and B864.** It is the arc that **confirms** them — it
  records that B950 and B976 wrongly declared absent what B862/B864 had already derived.

An arc claim is **one long sentence about many things**, so claim-scope matching reads every verb as
applying to every reference. Rescoped to **clause scope** (the verb within 90 characters of the
reference), the numbers fall to **79** pool arcs and **5 of 24** citations — and those five are
real. **The reportable number is the second one**, and the first is recorded here so nobody
re-derives the alarming version.

## 2. The two findings that change the paper

**(a) The ℤ₆ derivation is cited on the weaker of two footings.** The spec cites **B862**, whose
result is *"conditional on exactly what the cascade is conditional on."* **B1080** — later,
law-creating — confirms it **independently and extends** it: ℤ/6 forced **uniformly over six Weyl
realizations**, with row 1's full algebra giving **ℤ/6 × ℤ/2**. The spec now cites both.

**(b) THE ONE THAT MATTERS — the cascade's landing is not a discovery.** The spec listed *"the
measurement cascade landing on su(3)⊕su(2)⊕u(1)³"* among the **forced** results. **B951 deflates
exactly that headline**: the landing is precisely the **A₂+A₁ Levi subalgebra** of e₆ — dimension
6+8 = 14, semisimple part 11, centre 6−3 = 3, *"WHICH ARE EXACTLY B892's THREE NUMBERS"* — and
arriving there from E₆ is **Borel–de Siebenthal (1949) / Dynkin (1952)**. Classical.

> **It moves from the forced list to the recognition table.** What survives as forced is the chain's
> **termination** and the **global form**, not the **arrival**. B953 sharpens the same point for the
> paper's benefit: skipping SU(5) is skipping the rank reduction, and the two units the cascade
> cannot shed are **U(1)_ψ and U(1)_χ**, the standard E₆ extra abelian directions — also a
> recognition-table row.

**This is precisely the correction a referee would have made**, on the paper's most exposed claim,
in the genre where that exposure is fatal. Catching it before a draft existed is the whole reason
the sweep was worth running.

## 3. What was produced

- `papers/P3_THE_PAPER/CLAIM_CANDIDATES.md` — all 48 law-creating arcs grouped by the section they
  would serve, each with its supersession flags and an empty disposition column
  (**IN** / **SUP** / **OUT**). The grouping is a keyword first pass; **the disposition is an
  editorial call and is deliberately not made here.**
- The distribution is itself a finding: **20 of 48** law-creating arcs land in **§6, the observer** —
  the programme's densest law-creating region, which is where the paper's weight genuinely sits.
- `SPEC.md` corrected in three places (the Levi deflation, the B1080 citation, and §10b recording
  that the pool is swept rather than remembered).

## 4. Fences

The pool is **complete for its criterion** (`creates_law = true` plus the registered surfaces) and
that criterion is not the same as "everything the paper might cite" — an arc can matter to P3
without creating a law. **Coverage of the remaining ~660 PROVED arcs is not claimed.** The
supersession detector reports *lexical* relations, not adjudicated ones: five flags means five pairs
**to read**, not five corrections established — two of the five (B904, B928, B1129) are
confirmations on their face. The keyword section-assignment is a convenience, not a judgement.
