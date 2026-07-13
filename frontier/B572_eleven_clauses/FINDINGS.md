# B572 — the eleven-clause chain, adjudicated (the seventeenth chain, asking the right question)

**Date:** 2026-07-14. **Source:** the cross-seat "SM from σ: a→ab, end-to-end" handoff
(eleven clauses, cost accounting "zero", five verification tasks). **Locks:**
`tests/test_b572_eleven_clauses.py` (3). **Context:** unlike the sixteen value-chains,
this chain asks the selection-rules question — and most of it is the program's own
banked results, correctly cited. The adjudication therefore separates three things:
what stands (nine clauses), what is wrong (one detail, refuted against an existing
lock), and what is silently welded (one unpaid selector switch — the actual open
question of the program, smuggled in as free).

## Clause-by-clause

| # | Claim | Verdict |
|---|-------|---------|
| 1 | σ: a→ab → A₁ = F² → M₃ | STANDS (banked, textbook) |
| 2 | trace field ℚ(√−3), Galois ℤ/2 | STANDS (banked) |
| 3 | ρ̄ ≁ ρ (their commutant proof) | STANDS — their unipotent-commutant argument is correct and equivalent to the banked Galois-pair lock ((5±√−3)/2, t²−5t+7); their trace 3/2+(√3/2)i is the SnapPy-generator convention of the same fact |
| 4 | H¹ = 6 | STANDS (banked; V2's independent Fox-calculus route is a genuine strengthening task, queued) |
| 5 | θ-grading, ω-connection | STANDS (banked B353 + B570 spine) |
| 6 | the Klein four ⟨θ, σ⟩ | STANDS (= B570 Q-A) — one wording nit: "dφ = θ" is the pre-correction registry phrasing; the corrected statement is dφ = conj∘θ (antilinear) and d(σ∘φ⁻¹) = θ |
| 7 | F₄ ⊃ G_SM (TDV/Krasnov) | STANDS (banked B565-H1 verification) |
| 8 | "σ distinguishes 27 from 27̄"; 27\|_princ = V₃⊕V₇⊕V₁₇ | **REFUTED in detail, CONFLATED in substance** (below) |
| 9 | 27 = 16⊕10⊕1 under Spin(10)×U(1) → SM fermions | TEXTBOOK-TRUE, **OBJECT-UNCONNECTED** (below) |
| 10 | three generations (B299 ≡ Boyle triality) | STANDS as banked structural match (V3 — orbits ↔ three 16s — is a genuine open task, on the Spin(10) side) |
| 11 | SM anomaly cancellation | TEXTBOOK-TRUE; zero object content (and distinct from the object's own mod-11 cast arithmetic, where the SM remains unevaluable — AP1/AP6) |

## The refuted detail (their V1)

**27|_{principal SL(2)} = V₃ ⊕ V₇ ⊕ V₁₇ is FALSE.** The exact height multiset of the
27 under (μ, ρ∨) has multiplicity **2 at height ±1** (their partition predicts 3) and
**2 at height ±4** (theirs predicts 1). The correct branching is
**V₁₇ ⊕ V₉ ⊕ V₁** (tops 8, 4, 0) — already banked and locked
(`test_b570_qa_trichotomy.py::test_f4_principal_is_e6_regular`), and the basis of the
fifth wall. Consequently their tr₂₇(ρ(xy)) = 3339.5 + 4258.2i is wrong; the corrected
value at the banked Galois point (tr₂ = (5+√−3)/2) is
**tr₂₇ = 647707.5 + 876344.0965…·i** (exact in ℚ(√−3); locked).

## The weld (the load-bearing gap)

Clause 8's title — "σ distinguishes 27 from 27̄" — is the c/θ conflation made
load-bearing. Exactly:

> **χ₂₇(z) = χ₂₇(1/z) (palindromic, locked): the 27 and the 27̄ have the SAME
> character on any SL(2)-factored representation.** The holonomy cannot
> distinguish 27 from 27̄ — that is the fifth wall (AP4, banked). What their
> computation shows is tr₂₇(ρ) ≠ tr₂₇(ρ̄) — **σ moving the point** — which is
> Clause 3 restated, a c-fact, not a 27-vs-27̄ selection (a θ-fact).

Then Clause 9 switches routes: gauge comes from the θ-fold (→ F₄, whose matter is
vector-like — B569), while the chiral fermion content comes from **Spin(10)×U(1) ⊂
E₆ — a different subgroup, not θ-fixed, which nothing in the object selects.** The
chain pays for this switch nowhere. The missing bridge — carrying the object's
c-chirality into the θ/rep-theoretic slot — is precisely the program's open question
(Q-C transport, quarantined in B570; AP6 open item 10), not a solved step.

**The cost accounting is therefore wrong at one line: "Chirality — σ — cost 0
(forced)."** σ is real and free (it is the B469 orientation residue), but it buys
c-chirality; the chain spends it as θ-chirality. The unpaid items: (i) the selector
switch F₄ → Spin(10)×U(1); (ii) the c→θ transport. These are THE open items, and
they are exactly where all sixteen predecessors died, one level up.

Also regressed: the "five sources" table repeats **"B470: covers are chiral"** —
refuted by C4 (banked, 35 locks: every cyclic cover n = 2..12, branched and
unbranched, is amphichiral). B470's chiral limbs are the LETTER tower.

## The upgrade (their V4, run here): the ℤ/7 sine kernel

The M(2,7) observation is now an **exact identity** (residual 2e-14, identity
ordering of the pairs 27↔1, 351′↔2, 351↔3):

> **S_odd = −i · (2/√7)·[sin(2πst/7)]_{s,t=1..3}** — the θ-odd S-block of E₆ level 2
> IS the ℤ/7 sine kernel; S_odd² = −I (= conjugation on the odd sector), and the
> kernel matches the M(2,7)-family S-matrix up to a primary rephasing gauge
> (D = diag(1,−1,1) vs the standard Cardy formula; Review-16 R2 check). **S-block only:** the T-phases
> {13/84, 73/84, 61/84} are E₆-specific and do not match M(2,7)'s. Locked.

## Verification tasks: status

- **V1** (branching): answered — refuted, corrected, locked (above).
- **V2** (H¹ = 6 by Fox calculus, independent of deformation theory): genuine;
  queued as the PC25 strengthening task.
- **V3** (B299 orbits ↔ three 16s of Spin(10)): genuine and open — but note it lives
  on the Spin(10) side of the unpaid weld.
- **V4** (M(2,7) pattern): answered — upgraded to the exact sine-kernel identity
  (above). The level-2 θ-odd nontriviality was already banked (C3, order 4).
- **V5** (global gap⟺chirality with Galois descent): genuine; C2 banked the SL(2)
  biconditional; the global/descent version is queued.

## Papers

PC25 unaffected and strengthened (the ω-connection + the sine kernel belong in it).
**PC26 is premature:** its central theorem contains the refuted branching and the
unpaid weld. PC23/24/P4 unaffected. If the weld is ever paid (a computed c→θ
transport, or a forced non-principal selector), PC26 becomes the program's flagship —
that is exactly what makes the two open items the priority.

## The honest summary

Nine clauses stand — because they were already ours. The chain's genuinely new
content was one branching rule (wrong, now corrected and locked) and one weld
(unpaid, now named precisely). The seat's own error ledger (8 errors, all caught) is
appreciated and extended by two: the V₃⊕V₇⊕V₁₇ branching and the covers regression.
The right question was asked; the answer remains: **structure yes — five walls, one
live channel, one unpaid bridge; and the bridge, not the chain, is the work.**

Firewalled. Nothing to CLAIMS.md.
