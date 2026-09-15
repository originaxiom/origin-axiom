# PREREGISTRATION — the reopened G₂ hatch: is the enhancement isolated, in the sense Acharya–Witten needs?

*Outside bench, 2026-09-14. Sealed before computation. Gate 5 untouched.*

## Why this, and why it is the lift axis

The record's own answer to "what dimension does the chirality index live in" is **6 or 7**, never 3.
`docs/IDENTIFICATION_LEDGER.md` **I-26**: *"the index-theorem argument that licenses 'massless
multiplets = dim H¹' lives on a **Calabi–Yau 3-fold (real 6d) or a G₂ 7-manifold**; its transport to a
real 3-manifold's H¹ is never exhibited."* And the sibling branch's index campaign converged on the same
thing from below — B1334/B1339: *"the vanishing is dimension-counting, not the object"*, mechanism
Poincaré–Lefschetz / half-lives-half-dies / **image Lagrangian**.

**And 6d and 7d are the same door here.** B1259's own consequence, verbatim:

> The route to chiral matter therefore requires genuine **CURVATURE** — a conical G₂ singularity, **whose
> local model is a cone over a 6-manifold** rather than a linear action on ℝ⁷.

## The state of the hatch

**B1084 (PROVED, on this branch, reproduced here before sealing):** the flat G₂ orbifold
`(ℂ² × ℝ³)/Ĝ`, **|Ĝ| = 96** — **ONE E₆ locus with pointwise stabilizer exactly 2T** (the object's own
McKay group), **three A₁ families** (orbits 6/12/12, stabilizers exactly ℤ/2), the **Acharya–Witten
COLLISION criterion MET at the apex**, and **ISOLATION FAILING**: census {3: 53, 1: 42}, no
0-dimensional fixed set.

**B1259 (NEGATIVE):** that failure is a theorem, not a census — G₂ < SO(7), and every element of
SO(2k+1) has eigenvalue +1, so **every nontrivial element of any flat G₂ orbifold group fixes at least a
line**. No Ĝ escapes.

**B1304 (sibling branch, absent here until this session) SCOPED it:**

> The SO(odd) lemma does rule out an isolated point of the total orbifold singular set … **It does not by
> itself rule out an isolated enhancement stratum within that set. Its quantifiers may not be
> interchanged.**

verified on (ℤ/2)³ ⊂ G₂ with subgroup-order → fixed-dimension **{1: 7, 2: 3, 4: 1, 8: 0}**: *"**The
origin is an isolated maximal-isotropy stratum although no element has an isolated fixed point.**"*
So *"the hatch 'an isolated enhancement stratum' is **reopened as a question**"*. **No arc has walked it.**

## THE QUESTION, and it separates two readings that have been run together

Acharya–Witten chirality needs an **A-type locus meeting an E-type locus at an isolated point**. Two
different things are called "isolated" in the above:

- **(R1) an isolated maximal-isotropy STRATUM** — the apex, where *everything* meets. B1304 shows this
  survives the SO(odd) lemma.
- **(R2) an isolated A₁–E₆ INTERSECTION** — one A₁ locus meeting the E₆ locus in dimension 0.

**These are not the same, and the reopening establishes (R1), not (R2).** This cell computes (R2)
exactly, on B1084's own Ĝ, with B1084's own exact ℚ(√2) machinery.

**Computed:** for each of the 30 A₁ planes, the exact dimension of its intersection with the E₆ locus,
and the pointwise stabilizer of each intersection.

## THE TWO OUTCOMES

- **A — some A₁ locus meets the E₆ locus in dimension 0.** Then (R2) holds on this Ĝ, AW isolation is
  available in the sense the construction needs, and the hatch is genuinely open — the strongest
  possible result on this axis.
- **B — every A₁–E₆ intersection has dimension ≥ 1.** Then (R2) fails, and B1304's reopening
  establishes (R1) only. **The hatch is open as stated and shut as needed**, and the cell says exactly
  that, with the intersection dimensions as the evidence.

## CONTROLS

| # | control | catches |
|---|---|---|
| **G1** | **B1084's own script is re-run first** and must reproduce its banked items: \|Ĝ\| = 96, census {3: 53, 1: 42}, stabiliser of ℝ³⊕0 = 24 = the 2T copy, 30 planes with stabiliser order 2 in orbits [6, 12, 12] | a drifted or mis-built group; nothing after it counts otherwise |
| **G2** | the intersection dimension is computed by **exact rank over ℚ(√2)**, never numerically, and each intersection's pointwise stabiliser order is printed beside it | a float rank collapsing a transverse intersection |
| **G3** | **the computation must be able to return 0** — run it on a constructed pair of subspaces meeting only at the origin and require dimension 0 | a routine that can only ever report ≥ 1 (#164: an instrument that cannot fire) |
| **G4** | the population is printed before any conclusion: 30 planes, 1 E₆ locus, 30 intersections | the `B1197` vacuity trap |

## WHAT THIS CELL MAY NOT CONCLUDE

**Nothing about what Acharya–Witten's theorem formally requires** — that is literature, and the record's
own fence on B1304's example is *"the example is not an Acharya–Witten construction."* This cell
computes **geometry**, and states the two readings so a specialist can say which one AW needs. **No
chiral matter is derived.** **No generation count** — I-26 is UNEARNED and this does not touch it. No
value. Gate 5 untouched.

---

## ADDENDUM 1 (2026-09-14, POST-COMPUTE) — OUTCOME B WAS ALREADY BANKED AS A SENTENCE; WHAT THIS CELL ADDS IS THE DERIVATION. **BENCH ERROR #35.**

**The error, stated first.** This seal quoted B1084's census and the words *"ISOLATION FAILING"*, and then
presented outcome B as an open alternative. It is not open. **B1084's `claim_one_line` and its FINDINGS §3
state outcome B verbatim:**

> **"ISOLATION: FAILS, by the census. No 0-dim fixed set ⟹ every A₁ locus meets the E₆ locus along a LINE,
> never transversally at a point ⟹ every localized state extends along a flat direction ⟹ vector-like
> in 4d."**

So the cell's numeric result — 30 intersections, all of dimension 1 — **REPRODUCES a banked conclusion and
is not news.** Reading an arc's summary line instead of its own stated conclusion is the same failure as
**BENCH ERROR #34** (reading a branch listing instead of the record). Filed as **#35**. Terms searched
before this addendum: `"meets the E6 locus"`, `"along a LINE"`, `"isolat"`, `"vector-like"` inside
`frontier/B1084_g2_cone/` — all present, all missed at seal time because only `arc_verdict.json`'s census
clause was read.

**What survives, and it is not nothing: B1084's ⟹ IS THE QUANTIFIER INTERCHANGE B1304 NAMED.**

B1084's own script says what the census ranges over:

> `# ITEM 2: fixed-subspace dimension census over the 95 nonidentity elements`
> `print(f"ITEM 2: fixed-space dimension census over 95 nonidentity elements: {census}")`

and its FINDINGS repeats it: *"The fixed-dimension census **over the 95 nontrivial elements**: {3d: 53, 1d:
42} — NO **element** has a 0-dimensional fixed set."*

But an A₁–E₆ intersection is `Fix(H₁) ∩ Fix(H₂) = Fix(⟨H₁, H₂⟩)` — **the fixed set of a SUBGROUP, which is
not in that census.** "No element has a 0-dimensional fixed set" therefore does **not** entail "no
intersection of loci is 0-dimensional". This is precisely E70, and **B1304 supplies the counterexample that
shows the step is invalid in general**: on (ℤ/2)³ ⊂ G₂ the subgroup-order → fixed-dimension map is
**{1: 7, 2: 3, 4: 1, 8: 0}** — no element reaches dimension 0, a subgroup does.

**So the conclusion was banked on an invalid derivation, and this cell's direct exact computation of all 30
intersections is the first valid derivation of it.** The cell computes the linear meet
`dim(U ∩ V) = dim U + dim V − dim(U + V)` over ℚ(√2) exactly, per locus pair — the object B1084 asserted
about and did not compute.

**The corrected reading of the cell, replacing the pre-compute framing above:**

| | |
|---|---|
| **the number** | reproduction of B1084 §3 — **not news** |
| **the derivation** | new: B1084's element-census ⟹ locus-intersection step is E70-class and is not repaired by adding data; it is replaced here |
| **R1 vs R2** | stands as written: B1304's reopening establishes R1 (the apex is an isolated maximal-isotropy stratum), and R2 (an isolated A₁–E₆ intersection) is now **computed** false on this Ĝ rather than inferred false |
| **the hatch** | open as stated, shut as needed — unchanged |

All fences in the pre-compute text stand unchanged: nothing is claimed about what Acharya–Witten formally
requires, no chiral matter is derived, I-26 remains UNEARNED, and everything here concerns **flat**
orbifolds, the class B1259 closed. **Nothing above is struck.** Gate 5 untouched.

---

## ADDENDUM 2 (2026-09-14) — **THIS CELL IS SUPERSEDED IN FULL BY B1353**, which did more of it, five days earlier, on a head this bench had never diffed. **BENCH ERROR #34, THIRD INSTANCE — AND THE INSTRUMENT IS NOW FIXED.**

**`frontier/B1353_the_isolated_enhancement_point` (PROVED, 2026-09-09, on
`<seat>/standard-model-derivation-…`, absent from this branch and from main)** asked this cell's exact
question — it is titled *"main's E70 scope of B1259 answered"* — and answered it across **fourteen local
models** where this cell did one. Its row for **B1084's own Ĝ**, `(D*₂, C₄; 2O)`:

| | B1353's row 8 | this cell |
|---|---|---|
| \|Γ_p\| | 96 | 96 (control G1) |
| fixed dims of non-trivial elements | 42, 53 | {3: 53, 1: 42} (control G1) |
| **apex isolated** | **yes** | R1 holds — same |
| **distinct A-planes through 0** | **30** | 30 |
| **A ∩ P** | **line, always** | **{1: 30}** — same |

**Everything this cell reported, B1353 reported first and more of**, including the structural reason: its
two-line proof gives `Fix(g) = Fix_{Im ℍ}(Ad l) ⊕ Fix_ℍ(x ↦ l x r⁻¹)`, so the A-planes are
`axis(l) ⊕ {x : l x = x r}` and *"each A-plane contains the line axis(l) ⊕ 0 ⊂ P. The intersection is
exactly that line."* — the same fact this cell found as "ℝ³⊕0 meets (line in ℝ³)⊕(plane in ℍ)", stated
uniformly in `n` rather than for one group.

**And it goes past this cell in three directions this cell explicitly declined:**
1. **The AW literature question this cell called out of scope, B1353 settles with verbatim citation** —
   Witten hep-th/0108165 (*"not just an orbifold singularity"*), Acharya–Witten hep-th/0109152
   (*"worse-than-orbifold"*), Acharya–Gukov hep-th/0409191.
2. **The detector, not just the geometry:** the flat apex's link is `S⁶/Γ_p` with **b₂ = 0**, so there is no
   C-field U(1); and **E₆ is anomaly-free** (no cubic Casimir), so nothing at the apex can carry *or detect*
   a count.
3. **A₁/A₁ collisions at a point DO occur in the flat class** — *"216 of B1084's 435 pairs"* — so the flat
   class fails specifically at **A₁/E₆**, not at isolation generally. This cell never looked at A₁/A₁ pairs
   and would have reported the wrong shape of the obstruction.

**And `B1355_the_e7_point_made_explicit` (PROVED, same head) then walked the door this bench was about to
recommend as never attempted** — the curved model is named: **the G₂ cone over CP³/2T**, the Bryant–Salamon
cone over nearly-Kähler CP³ quotiented by the object's own McKay group, with E₆ and A₁ loci meeting **only
at a curved non-orbifold apex**, link `b₂ = 1`, `∫_U w ≠ 0`.

### The error, and the instrument

**#34 was minted on this bench as "Diff the frontier against EVERY head before calling anything unrun" —
and was never built into the tool.** `the_branch_gap.py` diffs **one** sibling. The all-heads diff, built
today as `outside_bench/certificates/the_frontier_gap_all_heads.py`, reports:

- **185 arcs absent from this branch**, not the 35 filed at #34 — the union over all heads is **1428**
  against this branch's **1243**;
- run with this cell's own terms (`acharya`, `isolated`, `enhancement`, `E6 locus`, `cone`), **B1353 scores
  5/5 and prints first** — *the instrument would have stopped this cell before it was sealed.*

**A rule that lives in a memo and not in an instrument is not a rule.** That is the transferable finding
here, and it is the only thing this cell contributes that B1353 does not.

### Disposition

**This cell is SUPERSEDED BY B1353.** Its computation is correct and its controls pass; it is a
**reproduction on one of fourteen models**, and no claim of priority, novelty or first-valid-derivation
stands. ADDENDUM 1's repair claim is corrected accordingly in place below and at
`frontier/B1084_g2_cone/FINDINGS.md`. Nothing is struck. Gate 5 untouched.
