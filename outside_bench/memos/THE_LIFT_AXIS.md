# THE LIFT AXIS — every route from a 3-manifold to 4d physics, with its obstruction verbatim, and the one door this bench can walk

*Outside bench, memo 232, 2026-09-14. **No new claim is made here.** This is the map the owner asked for
before any further door is walked: one table, the lift axis only, each route with what was tried, the
obstruction in the record's own words, current status, and whether this bench can walk it alone.*

*It exists because this bench recommended a door that was already walked. The map is the fix.*

---

## 0. THE FINDING THAT OCCASIONED THE MAP — **185 arcs, not 35**

Phase 3 filed **BENCH ERROR #34** (this bench reasoning on a stale tree) and minted the rule

> **#34 — Diff the frontier against EVERY head before calling anything unrun.**

**The rule was minted and never built into the tool.** `certificates/the_branch_gap.py` diffs **one**
sibling head. Built today as `certificates/the_frontier_gap_all_heads.py`
(`outputs/the_frontier_gap_all_heads_out.txt`):

| | |
|---|---|
| union of frontier arcs over **all** heads | **1428** |
| present on this branch | **1243** |
| **absent here** | **185** |

Two of the 185 are `B1353` and `B1355`, and they had already answered the question this bench sealed and
ran as open on 2026-09-14. **Run with that cell's own terms (`acharya`, `isolated`, `enhancement`,
`E6 locus`, `cone`), the new instrument scores B1353 at 5/5 and prints it first — it would have stopped the
cell before it was sealed.**

> **A rule that lives in a memo and not in an instrument is not a rule.**

---

## 1. THE MAP

**Read the columns carefully.** *"Obstruction"* is quoted from the arc, not paraphrased (#26: a theorem's
hypotheses are load-bearing and a paraphrase is where they go missing). *"This bench alone?"* asks only
whether the next step is a computation this container can run — not whether it is worth running.

### 1a. The word "lift" carries two meanings on this axis, and they are not the same problem

| sense | question | state |
|---|---|---|
| **GAUGE lift** | does a flat structure on m004 lift to the group? | **SOLVED, affirmatively** |
| **DIMENSION lift** | does the 3-manifold determine a 4d/6d/7d geometry? | **the wall** |

**The gauge sense is finished and green.** `B870` (PROVED): the central-extension obstruction is
`H²(π₁; A) = A/gcd(e_a, e_b)A`; m004's relator `aaabABBAb` has exponent sums `(1, 0)`, **gcd 1**, so
**`H² = 0` for EVERY coefficient group** — *"every flat E₆/ℤ₃ structure lifts to E₆ and B862's ℤ₆ global
form meets no obstruction on the object."* `B1298` (PROVED) then resolves **which** lift: of the inner and
outer E₆ lifts, *"THE FLAT GERM SELECTS THE OUTER LIFT, EXACTLY."* **Neither is a route to 4d**, and an
argument that cites B870 as progress on dimension is a change of subject.

### 1b. The dimension axis, route by route

| # | route | what was tried | **the obstruction, verbatim** | status | this bench alone? |
|---|---|---|---|---|---|
| **1** | **class-S of the fibre** — `B277` (PROVED) | m004 is a once-punctured-torus bundle, so it carries a canonical surface **Σ₁,₁** and monodromy **φ = RL**, pseudo-Anosov; `class-S(A₁, Σ₁,₁)` = 4d **N=2\* SU(2)**, `MCG = SL(2,ℤ)` = its S-duality group, and `T[4₁]` is φ's duality wall | *"The canonical lift is **N=2 (8 supercharges) → non-chiral** … The SM is **chiral = N=1** … needs an **external datum** (superpotential / flux / twist) that the geometry of `4₁` does **not** supply."* and *"the 6d type `G` is **still a free input** … the 4d lift does **not** resolve `input-E₆ = output-E₆`"* | **a lift EXISTS; it is the wrong one.** Two named missing inputs | **no** — both are inputs, not computations |
| **2** | **the multiplicity supplier** — `B292` (PROVED) | three candidates for the "2-manifold/family": the fibre Σ₁,₁, the metallic tower RᵐLᵐ, the filling family (1,n) | *"Only the FIBER is a 2-manifold … **NONE supplies the N=2→N=1 chiral datum** ⇒ wall #4 stays blocked"* | closed | **no** |
| **3** | **6d (1,0) twist / flux** | never an arc — a *residual-hint* in B277 and B292 | *"a chiral lift would need 6d (1,0) / a half-BPS twist / flux on the fiber — **none canonical to `4₁`**"*; `B292`: a **STOP-GATE (NEEDS-SPECIALIST)**, *"**consolidated, not attempted**"* | **never attempted, and correctly so** | **no** — a specifier at most |
| **4** | **the 4d suspension** — `B1104` (PROVED) | the complete finite menu `MCG(m004) = Isom = D₄`, 8 elements, table-exact | **NO-SECTION**: the θ-filter selects the central involution, the tick-filter the two reflections, **"JOINT SURVIVOR SET EMPTY"** — *"no canonical fourth dimension"*; and C1: *"no infinite-order element exists, the genesis act (Anosov suspension) **CANNOT repeat at 4d** via mapping tori"* | **closed by exhaustion of a complete menu** | — (done) |
| **5** | **the 4d filling** — `B716` (NEGATIVE) | oriented 3-bordism; the literature's near-misses | *"Ω₃^SO = 0, so a 4d filling **EXISTS but is infinitely non-unique** (W, W#ℂP², W#2ℂP²,…) with **nothing to select one**"*; Slavich's ℍ⁴ filling is *"one non-canonical Riemannian (4,0) filling"*; and *"no canonical Wick rotation"* | **closed: the problem is selection, not existence** | — (done) |
| **6** | **the flat G₂ orbifold** — `B1084` → `B1259` → **`B1353`** | B1084 built `(ℂ² × ℝ³)/Ĝ`, \|Ĝ\| = 96; B1259 made the census a theorem; **B1353 enumerated all fourteen local models by Goursat** | `B1259`: *"every nontrivial element of **ANY** flat G₂ orbifold group fixes at least a LINE … AW isolation is unavailable across the **ENTIRE class**"*. `B1353` corrects the mechanism: *"not 'no element isolates' but '**no stratum collides**'"* — the apex **is** an isolated fixed point of the group in all fourteen, but *"every A-type plane through the apex meets the E₆ plane P in a line"* | **CLOSED, with the mechanism repaired.** Also: A₁/A₁ *do* collide at a point (216 of B1084's 435 pairs) — the failure is specific to **A₁/E₆** | — (done; **this bench reproduced one of the fourteen and claimed nothing further**) |
| **7** | **the curved G₂ cone** — **`B1355`** (PROVED geometry / CITED physics) | B1259's own consequence — *"chiral matter requires genuine **CURVATURE**, a conical G₂ singularity whose local model is a **cone over a 6-manifold**"* — walked | **the model is NAMED: the G₂ cone over CP³/2T**, the Bryant–Salamon cone over nearly-Kähler CP³ quotiented by the object's own McKay group. E₆ and A₁ loci meet **only at a curved non-orbifold apex**; link **b₂ = 1**, `∫_U w ≠ 0`; by Witten's inflow the apex *"must carry chiral E₆-charged matter with U(1) charge"*. Its own limit: *"a **compact** G₂ manifold containing three such apexes on one E₆ locus is **not constructed here or anywhere I know**"* | **OPEN AT THE GLOBAL STEP** — the local model is done | **partly — see §2** |
| **8** | **Piergallini's branched covers** — `FRESH_EYES` **Q13** | registered as a question; the corpus archived | *"does the selector problem survive an explicit branched-cover 4-fold whose branching set is a knot complement?"* — status: *"his corpus (16 papers) archived under `audit/`"* | **OPEN — and unreachable from here.** `audit/` is **gitignored** (`.gitignore:11`), absent from **every** head, and absent from this container's filesystem | **NO** — its critical path runs through documents this bench does not have (**R90**) |
| **9** | **`T[4₁;E₆]`** — the CRUX | the state integral at exceptional type | a **specialist gate**; the type G is the free input of route 1 | OPEN, held | **no** |
| **10** | **the audit seat's 4d model** — `B1304` (PROVED) | a conditional compact-E₆ 4d action, R4–R11 | exists, at the price of the whole of `TOE_REQUIREMENTS_LEDGER` **§E row 1**: 4d Lorentzian spin spacetime, the compact real form, the field content, `N_f`, the potential's coefficients, the scales | **a DECLARED-INPUT construction**, not a lift | — |

### 1c. The two chirality routes that are *not* lifts, both closed, listed so they are not re-proposed

| | |
|---|---|
| `B1260` → **`B1267`** (NEGATIVE) | B1260 named the deciding computation on the non-self-dual rank-3 components W1/W2 and did not run it; **B1267 ran it: "THE ANSWER IS AGREE"** — the index is zero and the components are rigid. Its control caught a real bug (a Sym^n routine returning the transpose, making Sym an anti-homomorphism) |
| `B1351` (PROVED) | main's Q9 answered: *"On a closed closing χ = 0 and every Wilson-line vacuum is vector-like"* |

---

## 2. THE ONE LIVE DOOR, AND IT IS NOT A LIFT — IT IS **B1355'S OWN SUM RULE**

Everything in §1b is closed, input-priced, specialist-gated, or unreachable — **except route 7's global
step**, and B1355 registers the live question itself, with a tension already visible in its own words:

> *"∑_α ∫_{U_α} wᵢ = 0 for every harmonic two-form of the compact closing, so with b₂ = 1 the three 27s
> carry U(1) charges summing to zero (a 2 + 1 structure, e.g. (1, 1, −2)), and **a ℤ/3 that permutes the
> apexes and fixes w gives equal charges 3q = 0 and no inflow** — a ℤ/3-symmetric triple needs b₂ ≥ 2 with
> the ℤ/3 moving the harmonic forms."*

**Read against the record's own source of the "three", that is a candidate wall.** The record's three comes
from the **ℤ/3 descent** — `B1273`, *"the 3-fold cyclic branched cover Y₃ … **three copies permuted by
ℤ/3**"*. So: **the symmetry that supplies the count is the symmetry that kills the inflow that would supply
the chirality**, unless the closing's `b₂ ≥ 2` **and** the ℤ/3 acts non-trivially on `H²`.

That is the shape of **T-MIRROR-ODD-VANISHES** in a new value group, and it is **decidable by computation
on objects the record already has**: `H²(Y₃)` and the ℤ/3 action on it. `B1273` built Y₃ by
Reidemeister–Schreier from `π₁(m004)`.

**Checked before naming it a gap, per memo 153 and #34 — terms stated with the claim:**

| instrument | terms | result |
|---|---|---|
| `the_frontier_gap_all_heads.py` (all 11 heads, 185-arc gap) | `sum rule`, `charge sum`, `b_2`, `inflow`, `Z/3 symmetric`, `permutes the apexes` | **B1355 alone at 5/6** — and it *registers* the question rather than computing it. **No arc on any head has walked it.** |
| `already_banked.py` | `charge sum rule three apexes`, `b2 of the closing Z/3 harmonic two-form`, `inflow forces chiral 27` | no settled arc on the question; the ≥7-term hits are method arcs (B1009, B1231, B1295, B994), none on this content |

**What it can and cannot yield.** It can yield a **new wall** (ℤ/3-symmetry ⟹ no inflow ⟹ the count and the
chirality are not simultaneously available) or a **specification** (exactly what `b₂` and what ℤ/3-action a
closing must have). **It cannot yield a generation count**: `I-26` is **UNEARNED**, and B1355's *"one 27 per
point"* is, in its own words, *"the literature's rule … not re-derived here."*

---

## 3. WHAT THIS BENCH SHOULD NOT DO, STATED SO IT IS NOT PROPOSED AGAIN

1. **Route 3 (6d (1,0)) as a construction.** `B292` marks it NEEDS-SPECIALIST; the record's judgement that it
   was *"consolidated, not attempted"* is correct and this bench cannot improve on it.
2. **Route 8 (Piergallini).** Not adjudicable here: the sources are gitignored and absent. Naming it a gap
   would violate **R90** and **#24**.
3. **Re-deriving route 6.** Done fourteen ways by B1353.
4. **Any generation-count sentence.** `I-26` UNEARNED; the ledger's own rule is that until it is earned
   *"every generation-count statement in the corpus … is conditional on it."*

---

## 4. CELLS 11–15, FOLDED IN

| cell | result | disposition |
|---|---|---|
| **11** consistency-campaign finish | **C-4 FINITE-PLACE CONFIRMED**, ord(T) = 12; the S-matrix sign is **fixed by the relations** at `S_jk = ω^(−jk)/√3` (residuals < 1e-30), not fitted; C-2/C-3 BLOCKED | banked |
| **12** the branch gap | **BENCH ERROR #34** filed; 35 arcs named | **superseded today** by §0's 185-arc all-heads instrument |
| **13** the last target (t12835) | **OUTCOME A**; B1330's *"NOT DONE"* line discharged; V1 reproduced v2873 field-for-field; V5 resolved on two independent runs | banked |
| **14** rank(H₁/⟨peripheral⟩) | **0 on all four best-case objects** ⟹ B1334's S⁰ is a point ⟹ every order-3 sector lies **outside** its proof | banked — a rating this bench revised **upward** before results were known |
| **15** the reopened G₂ hatch | OUTCOME B, all four controls PASS — and **SUPERSEDED IN FULL by B1353** (**#35**: the outcome was already banked in B1084 §3; **#34 third instance**: B1353 did fourteen models, five days earlier, on a head never diffed) | **superseded; no priority claimed.** Its one contribution is §0's instrument |

---

## 5. THE ERRORS THIS MEMO FILES

- **#34, third instance** — the rule was minted and not instrumented. **Fixed in code**, not in prose.
- **#35** — reading an arc's summary clause (`arc_verdict.json`'s census phrase) instead of its own stated
  conclusion (`FINDINGS.md` §3). The new instrument's closing section states the residual limit in its own
  output: *per-arc presence is not per-question coverage.*

**Gate 5 untouched. Nothing promotes to `CLAIMS.md`. No value, no generation count, no physics claim.**
