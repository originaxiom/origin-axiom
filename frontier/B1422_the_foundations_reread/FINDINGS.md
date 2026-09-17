# B1422 — THE FOUNDATIONS RE-READ: the verification package shipped two green tests asserting a retracted claim, the repository held a no-re-litigation gate against its own paper, the genesis theorem was uncited where it is strongest, and the one inserted bit was written both ways

cc, 2026-09-17. **Owner-directed:** *"are u sure sure sure? verify verify first please? read the foundations of project,
first 300 arcs, B's, progresslog and changelog entries, and first 300 commit notes."* Five readers over the first three
hundred arcs, the founding documents, the earliest logs and the first three hundred commits; every finding re-verified
here before action. **Verdict: PROVED (the audit), and it found worse than the recent sweep did.**

## 1. THE WORST ONE — the verification package contradicted the paper it verifies
`tests/test_b291_scale_extremal.py` asserted `min_volume_is_arithmetic() is False` and
`tests/test_b296_seam_arc_verification.py` asserted `EXTENDED_CHECKS["B288_arithmetic_up_to_12"] == 0`. **Both passed.**
Both are listed in `papers/P3_THE_PAPER/verification_package/MANIFEST.json` as locks for the claim row that now reads
*"six are arithmetic by the closed criterion (m004(±5,1) Meyerhoff, (±6,1), (±8,1))"*. **A reviewer running the shipped
package would have obtained green tests asserting the negation of the sentence they were meant to verify.**

- **Root cause, same as E82.** B291's predicate is `(degree == 2) and has_sqrt_neg3` — the *cusped* criterion conjoined
  with √−3-containment, which on a closed manifold cannot be satisfied. It asks "is this the object's own field", not
  "is this arithmetic", and it was named `min_volume_is_arithmetic`.
- **B296 is worse in kind.** It is the seam family's *adversarial* pass. It extended the unfailable test to
  `|p|,|q| ≤ 12` (174 closings), got the guaranteed zero, and reported *"every probe SURVIVES; 0 refutations"*.
  A red team that re-runs a criterion which cannot fail launders the defect it exists to catch.
- **Why no gate fired.** B1419's retraction was never registered in `docs/RETRACTED_PHRASES.md`, and
  `retraction_sweep.py` reads only that file. Registered now — and on the first run it immediately caught a fourth
  live instance in B296's own FINDINGS.
- **Repaired:** both predicates renamed to what they compute, both tests corrected to the verified reading, addenda in
  both arcs, `B294`'s display table and `docs/HINT_LEDGER.md` corrected, three phrases registered.
- **What it costs the arcs' finding, stated:** B291/B294's *"no single closing is distinguished on all axes"* is
  **weakened** — under the correct criterion the scale axis and the arithmetic axis **coincide** at `m004(±5,1)`,
  which is simultaneously the minimum-volume closing and an arithmetic one. What survives is that it keeps none of the
  object's own field and is not the dynamical closing.

## 2. THE REPOSITORY HELD A CLOSED-CHAPTER GATE AGAINST ITS OWN PAPER
B82/V65 (2026-06-05) banked *"there is no physics here … the physics-probing chapter is **closed**; future runs should
not re-litigate these kills without genuinely new evidence."* `arc_verdict.json` carries `superseded_by: null`,
`docs/RETRACTIONS.md` had no row, and the sentence is live on about ten surfaces including `ROADMAP.md` (touched three
days ago) and `ARCHITECTURE.md` as a standing governance gate. Meanwhile `GOVERNANCE.md` §2 was amended with the
owner's approval on 2026-08-25 to *"derives the form of Standard-Model structure"*, and a 51-page paper now rests on a
route B82 never tested. **For fifteen months the repository asserted a no-re-litigation gate and litigated past it.**
Resolved by scoping, not by retraction: B82's kills stand on B82's routes (the SL(n)-tower bridges), the gate is scoped
in place at both top-level surfaces, and a dated row is in the retraction registry. The lesson filed: *a verdict that
closes a chapter must name the routes it closes; an unscoped closure cannot be superseded, only ignored.*

## 3. THE GENESIS THEOREM WAS UNCITED WHERE IT IS STRONGEST — now in the paper, with its limits
`docs/UNIQUENESS_THEOREM.md` (banked day nine; lock green, nine tests) proves **A1–A6 ⟹ A = LR**, machine-checked
144 → 1. The paper cited it zero times; the chain document cited it zero times. Now in both, with everything that
qualifies it: the forcing is **over-determined rather than tight** (the primitive-update axiom already fixes the
increments; the last two axioms each suffice alone; positivity is imported, and over ℤ alone `ab = 1` also admits
`a = b = −1`), so 144 → 1 is a consistency demonstration and not a search; the residual bit is the **order**, and
trace, determinant, characteristic polynomial and spectrum are all blind to it while the **based** Möbius polynomial
is not (φ against −φ); the theorem does **not** derive its axioms from anything weaker; and the two routes are **not
independent** because A1's ℤ² is the punctured torus's H₁. Also added: **the object preceded the axioms** — the
knot-theory turn is dated to the third week of May 2026 and the first probe naming the figure-eight to the 22nd, while
the axioms were committed on the 28th.

## 4. THE ONE INSERTED BIT WAS WRITTEN BOTH WAYS (`verification/lr_vs_rl.py`)
B1083 wrote *"M² = [[2,1],[1,1]] = RL exactly"*. The matrix is right; the name is wrong. Under the project's own
convention (A4: L = [[1,1],[0,1]], R = [[1,0],[1,1]]) that product is **LR**; RL is [[1,1],[1,2]]. The mislabel
propagated to `docs/THE_LADDER.md` (X23) and `docs/THE_FORCED_AND_THE_FREE.md`. It survived because the two are
conjugate and therefore invisible to every invariant the corpus checks — which is precisely why it matters: the order
is the project's **single irreducible inserted bit**. Corrected at both sites, with an addendum in B1083.

## 5. THE AXIOMS ARE NOT WHAT SURVIVED A SEARCH, and the paper now says so
`paths/PATHS.md` — the registry of twenty-five routes from "nothing is unstable" to a world — stands at one dead, four
stalled, three narrow, **eighteen never touched**, with no route ever reaching its own `PRODUCES-OBSERVABLE` label and
no update since 2026-06-07. The paper now states this as the evidence for its own scope note rather than leaving the
axioms to read as survivors of an elimination.

## 6. FOUR MORE, VERIFIED AND ACTED ON
- **Arithmeticity does not force amphichirality** — four arithmetic once-punctured-torus bundles to word length seven,
  and the mirror pair over ℚ(√−7) is **chiral** (B147, both Maclachlan–Reid conditions plus a Humbert volume
  cross-check). The paper reached the same conclusion three months later from the object's covers; the earlier, cleaner
  witness is now in it. The capstone `speculations/S032` still closed the chirality axis on the refuted form and is
  corrected; B145 and B123 carried refuted claims with no in-body signal and now have addenda.
- **The record swap is an added axiom**, not a consequence of the substrate axioms (B16: *"plausible, but it is still
  an axiom"*), so the presentation through the substitution rule spends it in addition to the order. Now stated.
- **The A6 self-criticism at full strength**: *every* wall downstream of the mirror-as-self-isometry is a property of
  the orientation axiom rather than of the object, with a 40/40 control on orientation double covers. Now in the paper.
- **`ARCHITECTURE.md` called three open things "proven mathematics"** — degree=rank (refuted at SL(5)), the plethysm
  (open for non-metallic N at n ≥ 3) and the all-n tower (a conjecture, the Procesi problem). Corrected in place;
  P1–P16 stands.

## 7. WHAT THE READERS FOUND THAT IS NOT REPAIRED HERE (named, for the owner)
The McKay door's own arc (B266: ℚ(√−3) → 3 → 𝔽₃ → 2T → affine E₆) is cited in no spine document and has **no chain
link** — the chain runs from the invariant trace field at link 6 to a presumed e₆ at link 24, and the step between is
prose. The paper's treatment is *stronger* than that arc (it rests the exclusion on direct enumeration of
homomorphisms rather than the trace-field argument, which is about subgroups and not quotients), so this is a chain
gap rather than a paper defect — but it is the door the whole construction walks through. Also unrepaired: the era's
four exact reproductions of published invariants (an A-polynomial matching Cooper–Long literally, two SL(3) matches,
a Ptolemy cross-check) and two *geometric* selections of the object (systole, volume) that the paper's
all-arithmetic criterion census does not mention.

## Locks
`tests/test_b1422_foundations_reread.py` (the LR/RL computation with its conjugacy control; that the two corrected
tests now assert the verified reading; that the retracted phrases are registered).
