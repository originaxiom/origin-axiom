# B1304 — THE AUDIT SEAT'S 4d MODEL, PRICED: its twenty-one rounds are verified as its own (235 pass, its 13 preserved failures and 8 fixture errors reproduced exactly), its declared inputs open the ToE requirements ledger's §E, its two claims against main both hold by computation — B915's crossing solver never re-solved its first equation (verdict unchanged), B1259's isolation theorem interchanged quantifiers (scoped, E70 minted) — R20's three-character locus is forced by B1302's own order-3 matrix, and the partial filling is one witness on three benches, now interval-certified

**Date:** 2026-09-09 · **Seat:** cc (main) · **MASTERPLAN v3.1 Phase 1, sixth harvest arc** · **DESIGN sealed** `866bd71e…` · **Seat pinned:**
`origin/audit/physical-bridge-2026-09-05` @ `6f862099` (worktree `oa-audit-seat/audit-seat-6f862099`); it takes no B number, its rounds are
path-local · **Status:** **VERIFIED** (the seat's suite state; R20's locus by main's data; the B915 defect by B915's own definitions; the B1259
counterexample by own exact code; the partial-filling witness by three benches) + **REGISTERED** (R4–R19 as the seat's conditional results with
their fences; the inputs into `docs/TOE_REQUIREMENTS_LEDGER.md` §E) + **two corrections to main's record** (B915 addendum, E52 instance; B1259 scope
addendum, E70 minted; kill-graph note) · **Price:** unchanged (no identification row; §E is the price table) · **Credit:** the audit seat (R0–R20,
`PARTIAL_FILLING.md`, three upstream audits @ 6f862099).

## 0. What the seat said, first

| item | the seat's own words (verbatim) | here |
|---|---|---|
| its verdict | "tested conditional field theory, not a source-derived physical TOE" (GOAL_VERDICT) | **AGREES**; the inputs are now a table (§E) |
| R1 on B915 | "B915's purported two-loop unification curve does not satisfy its own two simultaneous UV equations. A comparison coupling leaks into its first sequential solve." | **VERIFIED**: residual 0.0268 (theirs 0.02683971597; here 0.02683971620); the guess moves the answer by ~3·10⁻⁵ (below the DESIGN's 10⁻⁴ threshold — the threshold was mine, the leak is real); the simultaneous solve differs. **B915's MISS stands** (the seat's corrected d_min 16.116 σ) |
| UPSTREAM_THIRD_AUDIT on B1259 | "The SO(odd) lemma does rule out an isolated point of the total orbifold singular set … It does not by itself rule out an isolated enhancement stratum within that set. Its quantifiers may not be interchanged." | **VERIFIED exactly** ((ℤ/2)³ ⊂ G₂: {1:7, 2:3, 4:1, 8:0}); **B1259 SCOPED**, not retracted; E70 |
| R20 | "the source C3 symmetry permits exactly three rank-one adjoint characters" | **VERIFIED from B1302's own order-3 matrix**: {(0,0), (1/3,2/3), (2/3,1/3)} |
| PARTIAL_FILLING | "The core existence claim passes interval verification." | the same witness as the cloud's and B1305 A's; the certificate is the seat's; L202(b) upgraded |
| its suite | "broad 250 pass / 13 fail / 8 error" | **235 pass / 13 fail / 8 error** on the 33 `test_physical_bridge_*` files here — the identical failure set (4 charged_domain, 1 g2_isolation serialisation, 2 higgs_sector controls, 6 R20 transfer failures) and the identical 8 R11 fixture errors: the seat's state reproduces; nothing new fails |

## 1. Q1 — R20's locus and the algebraic twisted cohomology of m202 (`b1304_c3_locus.py`)

B1302's census holds the order-3 action of m202's isometry on H₁ = ℤ², M = [[0, 1], [−1, −1]] (t² + t + 1, det(M − I) = 3). Its fixed
characters on the dual torus are **exactly three: the trivial one and the conjugate pair (1/3, 2/3), (2/3, 1/3) of order 3** — R20's "trivial
transport and a conjugate pair", forced by det(M − I) = 3 before any Higgs field is chosen. Fox calculus on R72b's presentation
⟨a, b | aabbAbAABBaB⟩ (exponent sums zero) gives Δ_{m202} = t₁²t₂ + t₁² + t₁t₂² + t₁t₂ + t₁ + t₂² + t₂ — **seven monomials**, B1302's count by
another presentation — and **Δ = −2 at both characters of the pair**: they are off the Alexander zero locus, so R19's "four/one on the zero
locus" does not apply to them, consistent with the seat. **One mis-prediction of mine, recorded:** the DESIGN predicted the ALGEBRAIC twisted
h¹(m202; χ) = 1 at the pair; for the aspherical one-relator complex it is dim ker d¹ − rank d⁰ = (2 − 1) − 1 = **0** off the zero locus (the
DESIGN's arithmetic dropped the d⁰ term), and 2 = b₁ at the trivial character. The seat's "three/zero" and "four/one" are analytic counts in a
weighted L² complex carrying three source arcs and the spinor pair's charges — a different quantity, recorded beside the algebraic one, no
grade following from the difference.

## 2. Q2 — B915's crossing solver (`b1304_b915_residual.py`, B915's own definitions exec'd without its scan)

At the 16 archived two-loop curve points the FIRST UV equation's residual |x₁ − x₂|(M_U) is up to **0.02683971620** inverse-coupling units
while the second is satisfied to 10⁻¹¹; at the archived d_min scale (1.54·10¹³ GeV) the first-stage guess 0.118 → 0.09 / 0.15 moves the final
(sin²θ_W, α_s) by 3.5·10⁻⁵ and 2.7·10⁻⁵ (one σ of sin²θ_W; below the DESIGN's 10⁻⁴ threshold, so that sub-check is recorded as FAIL against
my number and PASS on the seat's claim); a simultaneous two-equation solve gives (0.229196, 0.076683) against the archived (0.229251,
0.076641). **The instrument was not solving the crossing** (E52 instance: a verifier defect under a standing verdict); **the verdict is
unchanged** — the seat's corrected solver moves the minimal distance from 15.97 to 16.116 σ, a MISS either way. B915 carries a dated
instrument addendum; the fix rule (a chained solver ends with every equation's residual) joins E39's family.

## 3. Q3 — B1259's isolation theorem (`b1304_g2_strata.py`, own exact code)

G = (ℤ/2)³ acting on ℝ⁷ by diagonal signs (−1)^{a·v} on the Fano coordinates preserves the standard 3-form exactly (its seven triples are the
Fano lines under the labelling used), has det +1 throughout, **every non-identity element fixes a 3-plane** (B1259's lemma, confirmed element
by element), and the common fixed dimension by subgroup order over all 16 subgroups is **{1: 7, 2: 3, 4: 1, 8: 0}**; isotropy orders 2 / 4 / 1 /
8 at a plane point, an axis point, a free point and the origin. **The origin is an isolated maximal-isotropy stratum although no element has an
isolated fixed point.** So B1259's theorem is right about elements and its consequence sentence ("Acharya–Witten isolation is unavailable in
the entire class of flat G₂ orbifolds") interchanged quantifiers: scoped by a dated addendum to "no isolated point of the total singular set
for any Ĝ"; the hatch "an isolated enhancement stratum" is reopened as a question; **no chiral matter is derived** — the example is not an
Acharya–Witten construction (the seat's own fence, with Witten and Acharya–Witten cited). **E70, the quantifier-interchange class, minted**;
the kill graph's B1259 node carries the scope note.

## 4. Q4 — the partial filling, three benches

Same isosig `kLLLPLQkcefegijjiijiieldllxtxa_aBbBabBbbacb`, same slope (2,1) on cusp 0, two complete cusps, CS +0.157590041 here and
+0.15759004087917… there; the seat's `verify_hyperbolicity` at 100 and 160 bits and its interval complex volume (the quarter lattice excluded
by > 0.0924099) are the certificate main lacks (no Sage). L202(b)'s note now says "interval-certified by the audit seat". Three seats — the
cloud (found), main (re-derived), the audit seat (certified) — hold one witness, none citing the others when they did it.

## 5. Q5–Q6 — the 4d model and the m202 chain, registered and priced

R4–R11 (the compact-E₆ action, its SM-algebra minimum, positive one-loop masses for the eleven flat directions, the quantum shifts, the
broken-vacuum EFT, the alignment logarithms, the family action's exact factorisation) are VERIFIED as the seat's by the suite re-run and
REGISTERED with the seat's fences; their inputs — Lorentzian 4d spin spacetime, the compact real form, the field content, N_f, the
coefficients, the scales — are rows of **`docs/TOE_REQUIREMENTS_LEDGER.md` §E**, created here in the GUT ledger's shape (§A the checklist any
ToE must pass; §B the three faces; §C what the record delivers row by row; §D the four walls; §E the declared inputs of every conditional
theory in the record, main's own I-rows and vacuum choices included; a reading rule: a ToE sentence must name its §E row). R12–R20 (the
singular route on m202) are REGISTERED under L205 with their fences; R12 agrees with B1291; R19's Δ is B1302's.

## 6. What this arc settles

- The record now has its **input table** (§E). "Uniquely derived from the source" is a sentence no theory in the record can say; each one
  can say which row it stands on.
- **Two instruments of main were wrong while their verdicts stood** (B915: the solver; B1259: the quantifier), both found by the audit seat,
  both confirmed here by computation, both corrected at source without a verdict change — the E52/E70 pair.
- R20's character locus is a fact of B1302's matrix; the seat's dynamics on it are the seat's.
- The harvest-debt gate's case is made a third time: the audit seat's twenty-one rounds had rows 25–26 on main before this arc.

## Receipts, verification, credit

`verification/audit_focused_suite_rerun.txt` (235 / 13 / 8, RC=1 as the seat's own state), `b1304_c3_locus.py`, `b1304_b915_residual.py`,
`b1304_g2_strata.py` (+ `.out`/`.json`). Lock: `tests/test_b1304_the_audit_seats_4d_model.py`. HARVEST_LEDGER rows 54–76. Addenda on B915
and B1259; `docs/TOE_REQUIREMENTS_LEDGER.md` opened; ERROR_LEDGER E52 instance + E70; L202(b) upgraded; the kill graph's B1259 node noted.
