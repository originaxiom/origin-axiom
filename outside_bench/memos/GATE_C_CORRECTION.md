# MEMO 158 — BENCH ERROR #17: THE LIVE ROUTE IS NOT UNRUN. IT IS RUN, AND SECTOR-COMPLETE.

**Banked 2026-08-30.** A correction to memo 157, filed one memo later, and it is the **same failure
memo 157 was charging.**

---

## 1. WHAT I SAID, AND WHY IT WAS WRONG

Memo 157 closed on:

> *"`B632`'s **cell 2** … is **queued and unrun**, and is **the actual live generation computation on
> the record**."*

**False.** Cell 2 was run on 2026-07-15. Sitting in `frontier/B632_cubic_route/` the whole time:

`CELL2_PREREGISTRATION.md` · `cell2_texture.py` · `cell2_output.txt` · `verify_cell2_exhaustive.py`
· `FAILED_RUN_1.txt` · `FAILED_RUN_2.txt` · `REPAIR_ADJUDICATION.md`

It was not merely run. It was **audited by an external read-only seat**, survived **162/162
coboundary-descent checks**, and carries a repair adjudication restoring two failed runs
byte-faithfully — including one whose **sealed gates fired exactly as designed** (nonzero diagonal
self-cups, antisymmetry `[True, True, False]`, coboundary-invariance FAILED) and forced a real
mathematical repair.

**How I got it wrong: I read `B632`'s own forward-looking prose — *"Cell 2 (queued, own prereg)"* —
as a statement of current state.** That sentence was true in July and describes the future from
July's vantage. **I read the register, not the corpus.**

**That is precisely the failure `B1202` named**, and precisely what memo 157 charged Gate C with. I
wrote a memo whose finding was *"the gate does not cite the material that answers it"* and, in its
final section, asserted an unrun cell **from a directory listing I never opened**, with
`already_banked.py` available and its rule adopted by me two memos earlier. **Bench error #17, and
the least excusable of the seventeen.**

---

## 2. WHAT CELL 2 ACTUALLY FOUND

The block-diagonality prediction registered **before** the run — that cross-block cup pairings
vanish — **held**:

- `[z₄ ∪ z₄] = (0,0)` — **O2 predicted zero, and it is zero**;
- `[z₈ ∪ z₈]` zero: **True**;
- class-level antisymmetry on all three pairs: **`[True, True, True]`**;
- coboundary control: class invariant **True**, raw cochain changed **True** (a non-vacuous control:
  it moves what should move and fixes what should not);
- `h²(27*) = 2`, matching expectation.

And the map `Ω : Λ²H¹(27) → H²(M; 27*)` is **NONZERO on all three pairs**.

---

## 3. AND IT DID NOT STOP THERE — THE WALL IS SECTOR-COMPLETE

Two later arcs extended it, and both are negative for a symmetric generation reading:

- **`B1036`** — *"THE SYMMETRIC TEXTURE'S OBSTRUCTION EXTENDS … the record route computes the
  seam-sector pairing (direct T² restrictions, holonomy-invariant form, gauge control PASS) and
  finds the **symmetric support EMPTY in every cell of every block**, including the seam-born
  classes."*
- **`B1039`** — *"**EXISTENCE NO, PRIOR HELD** — all **fifteen** symmetric pairs of the double's five
  classes, on both sides and in the MV difference, are **EXACTLY ZERO** … **THE WALL IS NOW
  SECTOR-COMPLETE ON THE DOUBLE**: solo all-sectors (`B632`), scalar/seam (`B1036`), V-valued
  (`B1039`)."*

---

## 4. WHAT THIS DOES TO MEMO 157'S CONCLUSION — it strengthens it

Memo 157's adjudication stands: **Gate C closes.** What changes is the sentence under it, and the
change runs in the closing direction:

| memo 157 said | corrected |
|---|---|
| the commensurator route is dead, the cohomological route is **alive and unrun** | the commensurator route is dead, **and the cohomological route has been run to sector-completeness with the symmetric texture EXACTLY ZERO** |
| "the live generation computation on the record" is queued | **there is no queued live generation computation of that kind.** Both mechanisms have been worked, and both fail the symmetric-generation reading |

**So the generation question is in a substantially more closed state than I reported.** Not "one
route dead and another open" — **two routes worked, and the symmetric reading failing in both, by
exact computation, across every sector of the double.**

What survives is what `B632` and `B1036` say survives, stated at their own banking: a **graded**
multiplicity (1 abelian + 2 chiral) solo, **5 = 2+2+1** on the double, `Ω` nonzero — *structure*,
and **not three symmetric generations.**

---

## 5. WHAT IT COSTS, AND THE RULE THAT WOULD HAVE CAUGHT IT

**Q9 stays withdrawn** — more firmly than before. Memo 157's relay to cc stands and gains a line:
Gate C's *Settled* list omits `B323`/`B324`, **and the gate's framing also predates `B632` cell 2,
`B1036` and `B1039`**, which is why it still reads as the live generation question when it is not.

**The rule I adopted in memo 153 and then failed to apply:**

> *No MISSING / OPEN / "never run" claim leaves this bench until `already_banked.py` has been run on
> its terms, and the searched terms are stated with the claim.*

Memo 157 asserted **"queued and unrun"** and stated no terms. Run now — `cup product texture H1 27
block diagonal cubic invariant` — it returns `B632`'s own FINDINGS at **7 of 7 terms**, top rank.
**The instrument would have caught this in one command.**

**Tightened, and this is the part worth carrying:** the rule as written covers claims that something
is *missing*. It did not cover **reading an arc's own forward-looking prose as present state** —
"queued", "next", "will be" — which is how this one got through. Added:

> **A future-tense sentence inside an arc is evidence about the day it was written and nothing
> else. Before repeating one, list the arc's directory.**

## 6. FENCES

- Memo 157's **G-1, G-2 and G-3 outcomes are unaffected**; only its §3 forward look was wrong.
- I have read cell 2's output and repair adjudication, not re-run its mathematics. Its 162/162
  external verification is cited, not reproduced.
