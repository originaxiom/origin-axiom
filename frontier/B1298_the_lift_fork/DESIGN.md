# B1298 — THE LIFT FORK: DESIGN (pre-registered before any computation; sealed by sha256)

*MASTERPLAN v3.1 Phase 1, first arc. Inform-before-execute: sources read in full before this file was written — fc R72
(`reports/fresh_physics_seat_2026-09-01/R72_THREE_FROM_THE_THIRD_ROOT.md` @ 659487bb, §1–§8) and its relay
`FC_TO_CC_2026-09-06_THE_LIFT_AND_THE_THIRD_ROOT`; the SM-derivation seat's sm:B1280 §3 (Theorem 2, the six signs) and
sm:B1281 refinement C/3 (@ 87a9004a); main's own B353 items (A)–(C); B1296's `e6_theta_spectra.py`. Date 2026-09-08.*

## 1. The question, in the seats' words and the record's

fc R72 §1: the manifold's involution σ acts on the SL(2) local system by Ad(N); on the E₆ local system (principal ι)
**two** automorphisms realise σ — the inner `Ad(ι(N))` and the outer `Ad(ι(N))∘θ_D` — because θ_D commutes with the
principal image (main's B353 item (B): "θ commutes with the full holonomy Ad-image", residual 1.8e−88). R70/R71 and
main's B1296 assumed the outer lift. Under the inner lift `ι(N) = exp(πiρ^∨)` acts on the root α by (−1)^{ht α}: fc
reports 32 fixed roots, fixed algebra A₅ ⊕ A₁ (dim 38), fixed Cartan = all of 𝔥 — every U(1) direction is even, and R69's
±2 on Fix(θ) with u = ω₁^∨ becomes 2 × (16 ⊕ 10 ⊕ 1), anomaly-free, WITHOUT dropping equivariance. fc asks main for a
new identification row: *"the lift of an isometry of Q to the E₆ gauge algebra (inner or outer)"*, and fences: *"which
lift the physics uses is G₂-data the record does not have."*

sm:B1280 Theorem 2: on the germ of the E₆ character variety at the geometric point the inversion acts as the OUTER
automorphism — the proof is six signs: `ε_n(ι) = (−1)^{n/2+1}` on `H¹(M; Sym^n ρ₀)` for the six exponents' n = 2, 8, 10,
14, 16, 22, which equals θ_D's (+ on 𝔣₄ = V₂⊕V₁₀⊕V₁₄⊕V₂₂, − on the 26 = V₈⊕V₁₆); the period-2 swap acts trivially.
sm:B1281 refinement 3: *"on the germ of the geometric E₆ holonomy the lift is outer, so the inner-lift count does not
live there."* **Main's B353 item (C) (2026-07) already holds the same six signs** — "the hyperelliptic cocycle action
satisfies J(z₀) = (−1)^{m+1} z₀ + d⁰(v)" for m ∈ {1,4,5,7,8,11} with explicit coboundary certificates — under the name
"hyperelliptic", without naming which of the two order-2 isometries it is. So the germ statement is a REDISCOVERY across
seats (B353 → sm:B1280), and part of this arc is to say so with both credits and to pin the name.

## 2. What is computed here (exact, this bench, THE IDENTIFICATION RULE: exhibit the intertwiner, then show it acts)

(a) **The twelve signs, exactly over ℚ(ζ₁₂), in SnapPy's presentation** ⟨a, b | aaabABBAb⟩ with the B1297 engine:
for k = 0, 2, …, 22 (h¹(M; Sym^k ρ_geo) = 1 for even k, 0 for odd — B1256/B1267/B1297 control), the intertwiners
`N_S`, `N_P` with `N ρ(g) N⁻¹ = ρ(σ(g))` solved as exact nullspaces (det normalised to 1; for even k the sign of N is
irrelevant), the induced map `f ↦ Sym^k(N)⁻¹ f∘σ` on Z¹, and the eigenvalue ε on H¹ read off by exhibiting `z' − εz ∈ B¹`.
σ ranges over the STRONG INVERSION `S: a ↦ a⁻¹, b ↦ b⁻¹` (f = −1 on H₁) and the PERIOD-2 `P: a ↦ a⁻¹, b ↦ a³b` (f = +1),
both exact automorphisms (B1297 §4.2).
(b) **The inner lift on B1296's E₆** (rational, ℝ⁸, Bourbaki simple roots): `ρ^∨` = the Weyl coweight, `⟨ρ^∨, α⟩ = ht α`;
the involution `α ↦ (−1)^{ht α}`: fixed-root count, fixed subalgebra type from the Cartan matrix of its simple system,
fixed Cartan dimension; the order-3 inner lift `e^{2πi ht/3}`: fixed roots and type. And B1296's T3 configuration
(u = ω₁^∨, equal signs) re-read under the inner lift: is it θ_G-equivariant? (θ_G u = u for every u.)
(c) **The price**: I-28 registered UNEARNED; its earning text names I-27 (the two are one debt: the closer's frame),
so B1266's union-find keeps eight sources; the ratchet is raised by hand 11 → 12 with the reason.

## 3. Pre-registered predictions (PASS/FAIL, each can fail)

- **P1 (the germ's lift):** `ε_S(k) = (−1)^{k/2+1}` for all even k ≤ 22 (k = 0: −1, the meridian-reversing control) and
  `ε_P(k) = +1` for all even k. PASS = both patterns hold: sm:B1280 Thm 2 and B353 (C) are reproduced exactly, the
  germ's lift IS the outer θ_D, and "hyperelliptic" in B353 names the strong inversion S. FAIL = any sign differs:
  then the inversion is not θ_D on the germ, the fork is open on the flat germ too, and B1296's scope clause widens.
  (A third outcome is possible and would be the finding: ε_P ≠ +1 somewhere — then the period-2 acts non-trivially
  on the germ and B1297's −1-on-torsion result has a flat-sector shadow.)
- **P2 (fc's inner lift):** 32 fixed roots, A₅ ⊕ A₁ (dim 38), fixed Cartan = 𝔥; order-3 lift: 18 fixed roots, A₂³
  (dim 24). PASS = reproduced; FAIL = a different type (then R72 §1 is wrong on the algebra, and §5's table with it).
- **P3 (the physics reading, stated before the numbers):** under the inner lift the T3 configuration is equivariant
  and anomaly-free (two 16's) — so the honest wall is NOT equivariance but the LIFT: on the flat germ it is outer
  (P1), in the singular charge-locus frame it is a choice (I-28); count 2 on both roads. If P1 FAILS, this reading is
  withdrawn and the fork is registered as open on both roads.

## 4. What this arc does not do
No new count; no m202 (B1302); no verification of R72 §2's refined boundary formula beyond citing it; the seat
scripts `r72_inner_lift.py` (fc, ~5 min) and `theta_odd_pairing.py` (sm, ~7 s) are RE-RUN in pinned worktrees
(`oa-audit-seat/fc-seat-659487bb`, `oa-audit-seat/sm-seat-87a9004a`) as rule 4 requires, and their
selftests recorded alongside this bench's exact numbers.
