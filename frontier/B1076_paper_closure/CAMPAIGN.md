# B1076 — THE PAPER-CLOSURE CAMPAIGN: twelve items, tracked until every one is accounted for

**Sealed** in `PREREGISTRATION.md` before the first item was worked. **Locked** by
`tests/test_b1076_paper_closure.py`, which fails if an item is deleted, given a status outside the
four, or marked `GREEN` without an evidence path that exists on disk.

**Statuses:** `GREEN` (closed, evidence path recorded) · `OPEN` (not yet worked) · `BLOCKED`
(worked, cannot close — obstruction named) · `WITHDRAWN` (item was wrong — reason recorded).
**`BLOCKED` and `WITHDRAWN` are legitimate closures. Silently leaving the list is not.**

---

## THE LEDGER

| # | item | what closes it | quantifier | status | evidence |
|---|---|---|---|---|---|
| 1 | **The 14-locus existence.** Appendix B block (b): *"the 78 weights; seven hyperplanes; certified gap."* The `A₂⊕A₁` terminus is currently *"if a 14-dim locus occurs, its type is forced"* — the **occurrence** is a floating-point census | certify the weight census exactly, and establish that a 14-dimensional locus **occurs** | algebra (member) | **GREEN** | **occurrence established, by two independent routes.** (i) `frontier/B1078_rung_spectrum_attained/` — `dim z(S) = 14` is attained, at 3-dimensional `S`, in the flat enumeration; (ii) **B892** banked a 14 independently (`su(3)⊕su(2)⊕u(1)³` at the wall point `y*`), recorded in B874's amendment. So `thm:smt`'s antecedent is discharged. The weight census is replaced by something stronger than the floating-point version: `frontier/B1076_paper_closure/item01_weight_field.py` — the weight field **IS** K (exact factorisation), and `frontier/B1076_paper_closure/item01b_stratification_output.txt` gives the rational stratification `{0} ⊂ (8,16)-plane ⊂ C` as a **biconditional** over 624 exact directions. **Residue:** the 14 is certified at three faithful primes plus B892, not yet over ℚ̄; B892's `y*` has `a² < 0`, so the locus is not real |
| 2 | **The realized rung spectrum.** The bound is proved (11 values); the realized set `{12,30,78}` is a **sample**, not an enumeration | exhaustive computation over the subspace lattice of `C`, plus citation of **B874**'s independently banked ladder `{78,46,30,12}` | algebra (member) | **GREEN** | `frontier/B1078_rung_spectrum_attained/rung_attained.py` — the lattice is infinite, so the sample was replaced by **structure**: exactly over ℚ, `e6 = z(C) ⊕ V'` with `C` acting as **literally zero** on `z(C)`, giving `dim z(S) = 12 + Σ{m_λ : λ(S) = 0}` for **every** `S` — the rung function is the flat-function of 30 hyperplanes in a 4-space. **109 flats; the realized spectrum is all eleven values `{12,14,16,18,20,26,28,30,36,46,78}` — the paper's bound is TIGHT.** B874's ladder is cited and all four of its values land. The eight the sample missed lie on proper subvarieties, which a random rational direction misses with probability 1. **Residue CLOSED same day** by `frontier/B1079_arrangement_exact/` — reaching the same arrangement as the **E₆ roots restricted to `C`** makes every weight rational, so the ℚ-enumeration **is** the ℚ̄-enumeration. Two routes, no shared code path, one answer |
| 3 | **All 64 Levi subsystems** — block (b), undeposited | ship the enumeration | algebra | **GREEN** | `frontier/B1079_arrangement_exact/arrangement_exact.py` and, shipped inside the submitted source, `papers/structure_paper/verify/check_levi_arrangement.py` — **the row moved from block (b) into block (a)**. Root counts `0,2,4,6,8,10,12,14,20,22,24,30,40,72`; the fourteen ambient dimensions; **24 is not a Levi dimension**; **26 realized by exactly four `A₄` node-subsets**; and **exactly three dimensions carry two types — 12, 18, 20** — which is `rem:leviscope`'s claim, with the four counts the paper leans on each unambiguous |
| 4 | **Theorem "assembly" (thm:classify).** The term is now defined; the six-group enumeration behind it is **not deposited**, so the classification is unverified | enumerate multiset decompositions of 27 into non-trivial irreducible degrees for each of `{A₄,S₄,2T,2O,A₅,2I}`, with a non-degeneracy test on the cubic | algebra | OPEN | — |
| 5 | **Prop 2880 / the coupling law — ρ, T, Σ, θ.** A theorem about a representation whose matrices are not printed; `check_coupling_law.py` verifies trace sets, not ρ | print the six Kac–Peterson SU(3)₂ entries; make the script **build ρ** and verify the decomposition | algebra / faces | OPEN | — |
| 6 | **π₁(4₁) ↠ neither 2I nor A₅**, and **"exactly two quotients" onto 2T** — both currently labelled conjecture | quotient enumeration on the 2-generator 1-relator presentation | member | **GREEN** | `frontier/B1076_paper_closure/item06_quotients.py` — exhaustive: **2I 600 reps / 0 surjective** (14,400 pairs), **A₅ 300 reps / 0 surjective** (3,600 pairs), so the conjecture is a **theorem**; and **2T: 48 surjections, 4 classes up to Inn, 2 up to Aut** — the paper's *"exactly two"* is correct **up to Aut(2T)** and the paper must say so. Control: relator exponent sums (1,0) match B870's independent Fox-calculus route |
| 7 | **Prop geodir** — 6-dimensional unobstructed moduli, `1+5` split. No proof, no citation, and load-bearing for C6's retyping | a genuine `H¹` / obstruction-theory computation — **or** accept `BLOCKED` and leave C6 a fully priced choice | algebra | OPEN | — |
| 8 | **Order 2880 / 63-of-63 characters** — block (b), undeposited | deposit the character comparison | faces | OPEN | — |
| 9 | **Theorem 4.7's positivity step.** GL(2,ℤ)-conjugacy does **not** preserve word positivity; the block-sequence argument needs its bridging sentence | one lemma: why cyclic rotations of positive words suffice | axioms | OPEN | — |
| 10 | **Lemma toral** — likely folklore (cf. Vinberg θ-group theory, fixed points of finite automorphisms). A literature pass is owed before any implicit priority | search; then cite, or record `APPEARS-NOVEL` in `docs/THEOREM_REGISTRY.md` | — (literature) | OPEN | — |
| 11 | **Census 5.1 (43 links, 4 axioms)** — counts an external ledger that is not deposited. An unverifiable census in a paper about verifiability | deposit the ledger, or replace the count with what is checkable | axioms | OPEN | — |
| 12 | **`refs.bib` — five `STANDARD` entries** flagged *"verify before submission"* (Hurwitz 1891, Slansky 1981, Georgi–Glashow 1974, McKay 1980, Conway–Smith 2003). `PRIOR_ART.md` calls this blocking | verify each against the actual source | — (bibliography) | OPEN | — |

---

## STANDING RULES FOR THIS CAMPAIGN

**No item closes on prose.** `GREEN` requires an evidence path — a script, a deposited artifact, a
citation — that exists on disk and that the lock can see.

**Every item states its quantifier before it is worked** (`docs/COMPUTE_THE_PROGRAM.md`): which
layer of the full-relations inventory it covers, and its conclusion claims no more. *Today's A2
question was under-quantified twice in ten minutes — first by grading on a mark-2 node, then by
searching a single 16 when the programme has both gradings, both faces, the class and the rows.
Both were caught, and both were the same error.*

**No headline may be a printed constant** (error class E42). Every reported number is bound to a
computed variable, and the arc states which computed invariant **changes** between the before and
after states. If none does, there is no result.

**Contradiction is a legitimate outcome.** If an item computes and refutes the paper, that is the
finding — the rung-spectrum correction is the worked precedent, where an external referee was
right and the repair made the paper stronger.

---

## PROGRESS

*(updated as items close; the lock reads the status column above, so this section is narrative
only and carries no authority)*

- **2026-08-18** — campaign sealed, twelve items registered, none worked.
- **2026-08-18** — **item 6 GREEN.** π₁(4₁) surjects onto neither 2I nor A₅ (exhaustive); the 2T
  count is 2 **up to Aut**, 4 up to conjugacy — an unstated equivalence the paper must fix.
- **2026-08-18** — **item 1 stays OPEN, with two sub-results certified.** *(A first edit marked it
  `PARTIAL`; the lock rejected that — `PARTIAL` is not one of the four statuses, and a half-status
  is precisely the limbo this campaign exists to prevent. The mechanism worked on its own author
  within the hour.)* The item asks for the **14-locus existence** and that is **not established**.
  What *is* certified, and replaces two thirds of block (b)'s floating-point census:
  **(i)** the weight field **IS** K — the weight cubic acquires a root in K, so the ad-spectrum is
  K-valued rather than merely 77-resolvent-sharing (`item01_weight_field.py`);
  **(ii)** the rational stratification is `{0} ⊂ (8,16)-plane ⊂ C` with `dim z = 78, 30, 12`, a
  **biconditional** over 624 exact directions (`frontier/B1076_paper_closure/item01b_stratification_output.txt`).
  **The 14 itself is real-inaccessible** (B892: `a² < 0`) and certifying it needs arithmetic **in
  K**, not over ℚ — a specified computation now, not a vague gap.
- **2026-08-18** — **item 2 GREEN, and it is the largest single correction of the campaign.**
  The paper's Theorem `thm:rungspec` bounds `dim z(S)` by eleven values and Remark
  `rem:spectrumscope` withdraws attainment, concluding the realized set *"appears on present
  evidence to be far smaller."* **It is not smaller — it is exactly the eleven.** The bound is
  TIGHT. The withdrawal was correct on the evidence then available; the evidence was a sample of
  an infinite lattice, and the eight missing values sit on proper subvarieties that a random
  rational direction misses with probability 1. **The sample was not unlucky, it was the wrong
  instrument.** Three paper edits are now owed: `thm:rungspec` → equality; `rem:spectrumscope`'s
  *"far smaller"* sentence → deleted and replaced; `thm:smt`'s 14-locus occurrence → no longer an
  assumption. B866 is upgraded as a by-product: its 46, previously a 55-digit numeric spectral
  gap with an open type check, is now exact with its multiplicity 16 **derived**.
- **2026-08-18** — **item 1 GREEN.** The 14-locus **occurs** — B1078's enumeration and B892's
  independently banked wall point agree. Both halves of the original item are now closed: the
  weight field is K, and the occurrence is established. Residue recorded in the ledger cell.
- **2026-08-18** — **the three owed paper edits are APPLIED**, and they are the first edits of
  this campaign that make the paper claim *more* rather than less. `thm:rungspec` retitled and
  restated as an **equality**, its proof gaining an *Attainment* half (the decomposition, the
  master identity, the 109 flats); `rem:spectrumscope` **rewritten** to record that the statement
  has been wrong in *both* directions — first an invalid converse, then an over-correction from a
  sample — and to say what is exact over ℚ versus certified at three primes; the figure caption,
  the abstract, the falsifier table and the downstream `thm:smt` paragraph all follow.
  `papers/structure_paper/verify/check_rung_attained.py` added, and its companion
  `check_rung_spectrum.py` re-pointed so it can no longer be read as the whole story.
  **`verify_all.py` is now 12/12.** Build: **45 pp, 0 overfull, 0 undefined refs**; main.tex
  re-grepped by hand against all ten registered retracted phrases — **0 live uses**.
- **2026-08-18** — **item 3 GREEN, and item 2's residue closed, both from one idea the owner
  prompted by asking me to fetch.** cc's banked no-moduli theorem — *`dim C = 4` with
  `dim z(C) = 12` forces `|Φ ∩ C^⊥| = 6`, the only rank-≤2 system with six roots is `A₂`, and all
  such lie in one `W`-orbit* — was **reproduced in-sandbox** (`WORKING_RULES` §2/§12 forbid banking
  it by citation) and turns the arrangement into **the 72 E₆ roots restricted to `C`**: six vanish,
  `66 = 72 − 6` remain, profile `12×1 + 18×3` — **exactly what B1078 computed from the charges by a
  route sharing no code**. Every vector is rational, so the ℚ-enumeration **is** the ℚ̄-enumeration:
  **109 flats, eleven values, exact.** The apparent tension with the 46 is not one — the
  *arrangement* is rational, the *charge basis's position relative to it* is not. Paper updated:
  the attainment proof is now stated from the root side and is exact, and the *"certified at three
  primes"* hedge is **gone**.
- **2026-08-18** — *(not a campaign item, banked alongside)* **B1077**: both sides of the
  remaining `14 → 12` step are **compact** in the object's own real form; reality is not the
  obstruction. `frontier/B1077_compact_home`.
