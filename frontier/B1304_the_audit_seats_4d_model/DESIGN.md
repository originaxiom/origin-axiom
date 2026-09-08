# B1304 — THE AUDIT SEAT'S 4d MODEL, PRICED (rounds R0–R20 and the strategy documents): DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 (early) · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 row B1304 (the audit seat's R1–R18, now R0–R20) · **Seat
pinned:** `origin/audit/physical-bridge-2026-09-05` @ `6f862099` (worktree `oa-audit-seat/audit-seat-6f862099`); the seat takes no B number, its
rounds are path-local labels under `reports/physical_bridge_2026_09_05/` (its own BANKING_RECEIPT) · **Read in full before this seal:**
`AUDIT.md` (§ executive finding, § history, § 4 the crossing solver), `PHYSICS_BOTTLENECKS.md` (§1–§3), `GOAL_VERDICT.md`, `README.md` (the
round index R4–R20 and the reproduce block), `FAILURES.md` (head), `BANKING_RECEIPT.md`, `PARTIAL_FILLING.md`, `UPSTREAM_THIRD_AUDIT.md`, the
heads of R4 `VACUUM_MODEL`, R5 `QUANTUM_VACUUM`, R11 `FAMILY_ACTION`, R18 `WEIGHTED_COHOMOLOGY`, R19 `HOLONOMY_SPECTRUM`, R20
`HOLONOMY_EQUIVARIANCE`; main's B915 `crossing.py` (lines 48–59) and B1259's FINDINGS (§ The theorem, § Consequence). **Seat suite re-run in the
pinned worktree before the seal (receipt `verification/audit_focused_suite_rerun.txt`):** the 33 `tests/test_physical_bridge_*.py` files —
**235 passed, 13 failed, 8 errors, 235 s**; the 13 failures are exactly the seat's own preserved set (4 `charged_domain`, 1 `g2_isolation`'s
serialisation test, 2 `higgs_sector` small-step controls, 6 `holonomy_equivariance` transfer failures) and the 8 errors are its R11 fixture
errors — the seat's state reproduces; nothing new fails. Nothing below was computed with main's own code before the seal.

## 0. The rules' lines and the view from above

- `already_banked.py "one-loop" "zero modes" "family action" "weighted cohomology" "adjoint character" "three-source" "partial filling"
  "compact real form"`: no settled arc ≥ 6 of 8 (nearest B1225). `absence_sweep.py`: "weighted cohomology" and "three-source" PRESENT only
  on the seat's heads and the intake; **"TOE_REQUIREMENTS_LEDGER" and "ToE requirements" ABSENT on every head** — the ledger the plan's
  Phase 4 (4) names does not exist; this arc creates it because the seat's input list is exactly its §E.
- **The view from above.** The audit seat did what the plan calls JOIN 3 without waiting: it chose a 4d theory (compact E₆, two 27s, an
  adjoint, N_f Weyl 27s, Lorentzian spin spacetime) and computed in it — a classical SM-algebra minimum (R4), positive one-loop masses for
  its eleven flat directions (R5), leading quantum shifts and a broken-vacuum EFT (R6–R10), a family action from the founding ratio (R11) —
  and then walked the singular chirality route on m202 (R12–R20): a global singular Higgs field with three source arcs, a uniform cusp-tail
  bound, complete weighted cohomology four/one, a flat-holonomy three/zero at generic unitary transport, and a source-symmetric pair-free
  character orbit in E₆/ℤ₃ with an obstructed simply-connected lift. Every one of these is fenced by the seat itself as CONDITIONAL on
  declared inputs. **What main takes:** (i) the inputs, priced — the ToE ledger's §E, where "say which endpoint" becomes a table; (ii) the
  results, VERIFIED as the seat's by re-run and REGISTERED against main's leads (L205 for m202, JOIN 3 for the action); (iii) two claims
  AGAINST main, adjudicated by computation: B915's crossing solver (a leak of a comparison coupling into the first solve) and B1259's
  isolation theorem (a quantifier interchange between elements and strata); (iv) one convergence: the partial filling — the cloud found it
  (memo 170), main re-derived it (B1305 A), the audit seat interval-CERTIFIED it at 160 bits — three seats, one witness. **Nothing here
  moves the chirality bit:** the seat's three/zero lives in a declared strong-source maximal complex on the sibling under chosen
  transport, and the seat says so in every paragraph.

## 1. Pre-registered questions

**Q1 — R20's C₃-compatible character locus, from main's own data** (`b1304_c3_locus.py`). B1302's census gives the order-3 H₁ action of
m202's isometry, M = [[0, 1], [−1, −1]] on ℤ² (char. poly t² + t + 1, det(M − I) = 3). The characters χ: H₁ → U(1) fixed by the C₃ action are
the kernel of (Mᵀ − I) on (ℝ/ℤ)²: predicted **exactly three — the trivial character and a conjugate pair of order 3** (R20's "trivial transport
and a conjugate pair"). PASS/FAIL. Then, with B1302's Fox machinery (`b1302_faces.py`'s Δ), Δ_{m202} evaluated at the pair: predicted **non-zero**
(the pair is off the Alexander zero locus, so R19's "four/one on the zero locus" does not apply to it — 70 %), and the ALGEBRAIC twisted
h¹(m202; χ) from the Fox Jacobian's rank at χ: predicted **1** at each of the pair (one relator, two generators, χ ≠ 1) and **2** at the trivial
character (b₁). These algebraic counts are recorded NEXT TO the seat's analytic "three/zero" and "four/one" as different quantities (the
seat's complex carries the source arcs, the spinor pair's charges and a weighted L² structure); no grade follows from the difference.

**Q2 — B915's crossing solver, adjudicated** (`b1304_b915_residual.py`, importing B915's own `run`/`alphas_from` without executing its
output-overwriting scan). B915's `solve` finds sin²θ_W from g₁(M_U) = g₂(M_U) with α_s held at 0.118, then finds α_s from g₂(M_U) = g₃(M_U)
without re-solving the first equation; at two loops the first equation depends on g₃ through the off-diagonal beta matrix. Predictions: at
B915's archived two-loop curve points, the maximum residual of the FIRST UV equation, |x₁ − x₂|(M_U), is **≈ 0.0268 in inverse-coupling units**
(the seat's 0.02683971597) and not below 10⁻⁶; a re-solve with α_s ∈ {0.09, 0.15} in the first stage moves the final (sin²θ_W, α_s) by more than
the truncation tolerance. If PASS: B915's INSTRUMENT is defective (the seat is right), B915's VERDICT (MISS by the d ≤ 3 criterion) is unchanged
because the seat's corrected solver moves the minimal distance from 15.97 to 16.116 — retract-keeping-the-computation on the instrument, a
dated addendum on B915, an ERROR_LEDGER instance (E39-adjacent: a solver whose second stage silently invalidates its first; recorded under
the existing class that fits or minted). FAIL = the residual is < 10⁻⁶ (then the seat misread the code and the addendum says so).

**Q3 — B1259's isolation theorem, adjudicated** (`b1304_g2_strata.py`, own exact code). The seat's counterexample: G = (ℤ/2)³ acting on ℝ⁷ by
diagonal sign matrices (−1)^{a·v} on the seven non-trivial characters of 𝔽₂³, preserving the standard G₂ 3-form φ = e₁₂₃ + e₁₄₅ + e₁₆₇ + e₂₄₆
− e₂₅₇ − e₃₄₇ − e₃₅₆. Predictions: all eight matrices preserve φ exactly and have det +1; every non-identity element fixes a 3-plane (B1259's
lemma, confirmed); the common fixed dimension by subgroup order is **{1: 7, 2: 3, 4: 1, 8: 0}** over all 16 subgroups; so the origin is an
isolated maximal-isotropy (order-8) stratum while the total singular set is not isolated. If PASS: B1259's theorem ("every element of SO(7)
has eigenvalue +1 ⇒ no 0-dimensional fixed set") is correct as a statement about ELEMENTS and its consequence sentence "Acharya–Witten
isolation is unavailable in the entire class of flat G₂ orbifolds" interchanges quantifiers (an isolated STRATUM of a group's common fixed
set is not excluded) — B1259's verdict is SCOPED by a dated addendum (not retracted: the census fact about B1084's 95 elements stands, and
the seat itself says the example is not an AW construction), MAIN_GOAL's JOIN 1 wording checked, and an ERROR_LEDGER class recorded (the
quantifier interchange between a lemma about elements and a claim about strata; minted as E70 unless an existing class fits). FAIL = the
sign matrices do not preserve φ or some proper subgroup already has fixed dimension 0 (then the counterexample is wrong and B1259 stands).

**Q4 — the partial filling, three seats:** the seat's certified witness is the same isosig, slope and CS (+0.157590040879…) as the cloud's
and B1305 A's (+0.157590041): **VERIFIED by agreement of three benches**; the interval certificate (Sage/SnapPy `verify_hyperbolicity` at 100
and 160 bits; complex volume verified modulo 2-torsion; the quarter lattice excluded by > 0.0924099) is the seat's — main has no Sage —
REGISTERED, and L202(b)'s note is upgraded from "unverified numerics on both benches" to "interval-certified by the audit seat".

**Q5 — R4–R11 (the chosen 4d model): VERIFIED as the seat's by the suite re-run; the inputs REGISTERED.** `docs/TOE_REQUIREMENTS_LEDGER.md` is
created in GUT_REQUIREMENTS_LEDGER's shape: §A what any ToE must supply; §B this object's three faces; §C what the record delivers row by row
(banked arcs only); §D the walls (B1227's four regimes; V-3; B1265's rank obstruction); **§E the declared inputs of every conditional physical
theory in the record** — the audit seat's list verbatim (Lorentzian 4d spacetime, compact real form, field content, family number N_f,
coefficients, scales; R14–R19's sourced twisted-reduction background, parent adjoint, maximal domain, flat connection; the partial filling's
cover/cusp/slope) beside main's own priced choices (I-26, I-27, I-28; the vacuum among the nine branches; the closing among Y₉/Y₁₂; the fork
of B1303). Every "absent" row carries its absence line. No verdict changes.

**Q6 — R12–R19 registered against main:** R12 AGREES with B1291 (already row 25); R13/R14 (the harmonic and singular cusp fields), R15/R18
(four/one), R16/R17 (domain, tail bound), R19 (three/zero at generic holonomy; "the Alexander polynomial is already present in the SM seat's
B1282" — i.e. Δ_{m202}, = B1302's) REGISTERED as the seat's conditional analytic results on m202 under L205 (the owner's D3 arc), each with the
seat's own fence quoted; R11 (the family action's factorisation, exact) REGISTERED against B1275/B1138 with its fence. The three upstream
audits: the first (B915 → Q2), the second (bounded corrections, read and listed), the third (B1259 → Q3).

**Q7 — HARVEST_LEDGER rows for R0–R20, the seven strategy/audit documents and PARTIAL_FILLING (one row each, the seat's headline verbatim);
the harvest pins for the seat set at `6f862099`; hints; the E53 check that B1259's scope reaches MAIN_GOAL/JOIN 1 and the kill graph.**

## 2. Priors

Q1: 90 % (the locus is forced by det(M − I) = 3); Δ(pair) ≠ 0: 70 %. Q2 PASS (the leak is real): 90 % — the code shows it. Q3 PASS (the
counterexample is exact): 85 %. Expected verdict: **VERIFIED (the seat's suite state; the C₃ locus; the witness) + two corrections to
main's own record (B915's instrument, B1259's scope) + REGISTERED (the 4d model's inputs into the new ToE ledger; the m202 analytic chain
under L205).**

## 3. Method, controls, discipline

Own code for Q1–Q3 (exact where the objects are exact); the seat's suite re-run in its pinned worktree with the receipt; PASS and FAIL
branches in every script; pytest's own rc; the seat credited by round and pin; no grade lowered without a computation; corrections to main
made where the claim lives (B915, B1259 addenda) with the log entries; loose relay files never at root. Out of scope: re-deriving the seat's
4d action or its one-loop sums (they are its chosen theory: priced, not verified); the analytic weighted-cohomology counts (registered);
the σ bridge; any generation count.
