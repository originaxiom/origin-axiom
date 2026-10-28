# B1797 — GENESIS v1.59: THE CUSP'S UNIT REDUCED TO THE FIELD'S EXISTENCE AND THREE FURTHER LINKS, NONE DERIVED (P-288; THE COMPLETION MAP'S C8, ON B1796)

**Verdict: PROVED** (a record of a verified reduction in the foundation's wording; no status cell and no computation
changes). cc (main), 2026-10-28. Corrected before landing at its hostile referee (§ 4). **0 of 19.**

## 1. What changed (`adoption/amend.py`, from the hash-pinned v1.58 in `received/`)

**FK10 (the end law) gains a [v1.59] sentence.** Its status is unchanged: OPEN, the unit a tagged working postulate. The
sentence carries six points:
- B1796 verified on main the SM seat's W123, its exact route. Of W130 it verified the point's non-unitarity and Hitchin's
  equation; the rest of W130 stays the seat's.
- The dimension of the weight-3/2 forms of ρ_T under m units of end data is max(0, Σm) on every vector computed. It is
  proved to be 0 whenever Σm ≤ 0, and 3n for n ≥ 0 uniform units (W46's uniform twist).
- One unit on v₊ alone gives ∂R (B1700); the least uniform datum gives three. That the Higgs and the chiral three's zero
  modes share this space is B1700's reading, not a claim.
- At a Fuchsian point of the fibre the flat datum is not unitary, so its Higgs field is nowhere zero.
- So the unit follows from four links, none derived on the record, given Λ and the hand:
  1. the field's existence (FK15; W130's "forced" is the seat's reading);
  2. the type identification;
  3. uniform end data;
  4. the least remainder.
- That the three are generations is FK11's.

**FK15 (the field's genesis) gains a pointer.** FK10's unit follows from this fork's existence half, for the fibre's Higgs
field as W130 types it (End E ⊗ K), not B1654's (0, 1) typing, with three further links.

**The version log** gains the v1.59 entry, above an unrewritten v1.58 entry.

**Companion:** `docs/THE_COMPLETION_MAP.md`'s summary of gap 3 now states the four links and FK11. It had said "one open
link … FK10 reduces to FK15", which B1796 corrected.

## 2. What it does not do

- It derives none of the four links.
- It removes no input and changes no status cell.
- FK10 stays a tagged postulate. The record now states what the postulate amounts to.

## 3. Evidence

B1796 (PROVED), with its referee's two independent reproductions of W123. The arithmetic of the implication "four links ⇒
n = 1 ⇒ three" uses only the parts proved there: the Σm ≤ 0 half, and the uniform case.

## 4. The referee (hostile, read-only; `audit/referee_b1797/`)

**Mechanics clean:**
- the pin matches;
- exactly four spans change;
- the table cells are kept;
- the genesis-cited gate passes on the built file;
- earlier GENESIS locks are unaffected.

**One blocking finding, applied:** the draft's bold heading, "the unit reduces to the field", left out three of the four
links and would read as a derivation.

**Six corrections, applied** — four of them restored fixes that B1796's own referee had made:
1. W130 verified only as far as checked.
2. The reading tag and the FK11 sentence kept.
3. "A" Fuchsian point, with the rest-state reading tagged.
4. "3n" stated for n ≥ 0, in GENESIS's own terms.
5. "Now located" became "a reduction of the postulate, not a derivation".
6. The FK15 pointer moved before the settle sentence and scoped to the existence half and W130's typing.

**Notes:**
- the log entry names FK15's pointer;
- the script runs from its frontier location;
- the completion map's summary had to change in the same landing.

## Seen first

As B1796's sweep: `VERDICT topic-sweep /cusp unit|unit of end data|end data|O\(n.?δ\)|W123|W130|non-abelian Hodge|uniformi[sz]ing Higgs|least remainder|FK10|FK15/ (full text, aliases: the cusp's unit): 87 of 1543 arcs on main match (NEGATIVE 19, PROVED 67, no verdict file 1); 44 register rows match (DONE 27, LEAD 1, QUEUED 16)`.
- **Bearing on it:** GENESIS FK10's earlier sentences (v1.37–v1.54), FK15, B1700, B1754 (the amendment machinery).
- **Literature:** none beyond B1796's (non-abelian Hodge; vector-valued modular forms as a free module).

## Files

- `adoption/amend.py` (python3 amend.py writes GENESIS.md; --check exits 1 if the root file is v1.59 and differs).
- `received/GENESIS_v1_58_main.md` (sha256 95e6d2f5…).

The lock: `tests/test_b1797_genesis_v1_59.py`.
