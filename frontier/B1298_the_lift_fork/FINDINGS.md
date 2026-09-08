# B1298 — THE LIFT FORK: the involution has two lifts to E₆; the flat germ selects the outer one (twelve signs, exact), the singular frame does not — the wall on the count-2 road is the lift, not θ-equivariance, and it is priced as I-28

*MASTERPLAN v3.1 Phase 1, first harvest arc. DESIGN sealed before computation (`DESIGN.sha256`, `d81fba42…`). Sources read in
full: fc R72 + its relay (@ 659487bb), sm:B1280 §3 and sm:B1281 C/3 (@ 87a9004a), main's B353 items (A)–(C). Every seat
number re-run in a pinned worktree (`/Users/dri/oa-audit-seat/fc-seat-659487bb`, `…/sm-seat-87a9004a`) AND re-derived
here in exact arithmetic. Seats credited by branch + pin; the HARVEST_LEDGER opens with this arc (rows 1–7). Date 2026-09-08.*

## The sentence

**fc R72 is right that B1296 assumed one of two lifts.** The involution of m004 acts on the SL(2) local system by an
intertwiner N; on the E₆ local system (principal embedding) both `Ad(ι(N))` (inner) and `Ad(ι(N))∘θ_D` (outer) realise it,
because θ_D commutes with the principal image (main's B353 (B)). Under the inner lift every Cartan direction is even, so
B1296's count-2 SO(10) configuration on `ω₁^∨` is θ-equivariant AND anomaly-free — the singular road's wall was never
equivariance. **But the flat germ selects the outer lift, exactly:** the strong inversion acts on the twelve one-dimensional
`H¹(m004; Sym^k ρ_geo)`, k = 0…22 even, by `(−1)^{k/2+1}`, which on the six deformation classes of `e₆` is (+,−,+,+,−,+)
= θ_D; the period-2 acts trivially. That is sm:B1280 Theorem 2 (proved mod two primes), and it is main's own B353 (C)
(2026-07, "the hyperelliptic cocycle action"), reproduced here over ℚ(ζ₁₂) in SnapPy's presentation. So: the lock stands on
the flat germ; in the singular charge-locus frame the lift is a choice — registered as **I-28**, joining I-27's source
(price unchanged at 12). **Count 2 on both lifts; the wall's name changes from "equivariance" to "the lift".**

## 0. Pre-registration and outcome (DESIGN §3)

| prediction | outcome |
|---|---|
| P1 `ε_S(k) = (−1)^{k/2+1}`, `ε_P(k) = +1`, all even k ≤ 22 | **PASS**, exact (`b1298_signs.py`, 73 s): S = (−,+,−,+,−,+,−,+,−,+,−,+), P = (+)¹² |
| P2 inner lift: 32 fixed roots, A₅⊕A₁ (dim 38), all of 𝔥; order-3: 18, A₂³ | **PASS** on B1296's rational E₆ (`b1298_inner_lift.py`); outer θ_D: 24 fixed roots, F₄ |
| P3 the reading | stands: the flat germ's lift is outer (P1); the singular frame's lift is I-28; count 2 on both |

## 1. The twelve signs (THE IDENTIFICATION RULE: the intertwiner exhibited, then shown to act)

Presentation ⟨a, b | aaabABBAb⟩, ρ_geo in Fricke form over ℤ[ω] (B1297). The strong inversion S: a ↦ a⁻¹, b ↦ b⁻¹ has the
exact intertwiner `N_S = [[0,1],[1,0]]` (det −1; normalised to det 1 by λ = i, which multiplies the eigenvalue on Sym^k by
`(−1)^{k/2}` — the source of the alternation); the period-2 P: a ↦ a⁻¹, b ↦ a³b has `N_P = [[−1, −2+2ζ²],[ζ², 1]]` (det 1),
ζ = ζ₁₂. On each `H¹(m004; Sym^k)` (dim 1 for even k, 0 for odd — the B1256/B1267 control again) the induced map
`f ↦ Sym^k(N)⁻¹ f∘σ` has eigenvalue exhibited by `z′ − εz ∈ B¹`:

| k | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ε_S | − | + | − | + | − | + | − | + | − | + | − | + |
| ε_P | + | + | + | + | + | + | + | + | + | + | + | + |
| θ_D on `e₆ = V₂⊕V₈⊕V₁₀⊕V₁₄⊕V₁₆⊕V₂₂` | | + | | | − | + | | + | − | | | + |

k = 0 is the control (S inverts the meridian: −1 on H¹(M;ℂ); P preserves it). The six e₆ classes give (+,−,+,+,−,+) = θ_D
(+ on 𝔣₄ = V₂⊕V₁₀⊕V₁₄⊕V₂₂, − on the 26 = V₈⊕V₁₆): **the inversion IS the outer automorphism on the Zariski tangent
space at the geometric point**, hence on the germ (linearisation: a finite-order automorphism of a germ trivial on the
tangent space is the identity — sm:B1280's argument, which this arc adopts as cited).

## 2. The inner lift, on main's E₆

`ρ^∨` = the Weyl coweight, `⟨ρ^∨, α⟩ = ht α`. `Ad(exp πiρ^∨)` acts on α by `(−1)^{ht α}`: 32 of 72 roots fixed, simple
system of the even-height subsystem of type **A₅ ⊕ A₁** (dim 38), fixed Cartan = all of 𝔥 (a torus element). The order-3
lift `e^{2πi·ht/3}`: 18 roots, **A₂³** (dim 24). θ_D for comparison: 24 roots + a 4-dim Cartan = F₄. On `u = ω₁^∨` the 27
splits 16₍₁/₃₎ ⊕ 10₍₋₂/₃₎ ⊕ 1₍₄/₃₎ and B1296's T3 content (equal signs) is 2×(16⊕10⊕1) — under the inner lift this
configuration satisfies the lock's condition `θ_G u = u` trivially. fc's `r72_inner_lift.py` re-run: SELFTEST PASS.

## 3. What changes on main

- **T-CHARGE-LOCUS-PARITY-LOCK** carries its scope: the spectral half is the OUTER-lift statement; on the flat germ the
  lift is outer (§1), so the lock stands there; in the singular frame the lift is I-28.
- **I-27's price restated:** locus (T2) and sign pair (T4b) unchanged; its third item "the direction must be θ-odd, hence
  non-equivariant" becomes "the direction is a Cartan choice and the LIFT is a choice" — one debt, I-27 ∪ I-28 (B1266's
  union-find keeps eight sources; the ratchet is raised by hand 11 → 12).
- **The head sentence stands:** count 2 on every road, now including the inner-lift road.
- **A theorem rediscovered across three benches** (B353 (C) → sm:B1280 → here): recorded as H-B1298-GERM, an E53 at the
  level of theorems; the corpus's "hyperelliptic" involution is named: the strong inversion (H-B1298-NAME).

## 4. Seat credits (the seat speaks first — §1a rule 2)
- **fc R72** (2026-09-06): *"the lift of θ to E₆ is not unique (B353's own item (B)), the inner lift makes every direction
  even"* — VERIFIED (§2); its identification ask is REGISTERED (I-28); its m202 count is SCHEDULED (B1302). Its
  fence *"which lift the physics uses is G₂-data the record does not have"* is adopted as I-28's earning condition.
- **fc R71** (2026-09-06): *"on the θ-even directions the ±2 is vector-like or anomalous, never a spectrum"* — the
  scripts re-run here (SELFTEST PASS ×2); the dichotomy is B1296's spectral half, credited there at landing.
- **sm:B1280 Theorem 2** (2026-09-06): *"the θ-odd E₆ frame is vector-like on its whole germ … the question is six
  signs"* — VERIFIED exactly (§1); `theta_odd_pairing.py` re-run, two primes agree, SELFTEST PASS.
- **sm:B1281 refinement C/3** (2026-09-07): *"on the germ of the geometric E₆ holonomy the lift is outer, so the
  inner-lift count does not live there"* — AGREES (P1 + P3).
- **main B353 (C)** (2026-07): the six signs with explicit coboundary certificates, under the name "hyperelliptic" —
  the corpus anchor both seats and this arc converge on.

## 5. Fences
The linearisation step (tangent action trivial ⇒ germ action trivial) is cited from sm:B1280, not re-proved. Nothing here
is a count of generations: I-26 still conditions every "16 = a generation". The singular-frame configuration (a Higgs
field with log sources on Fix(θ)) is PW's mechanism and is not constructed on m004 here (fc R72 §8's fence adopted).
The inner lift's "every direction even" is a statement about Aut(E₆), not about which Cartan direction the object picks
(I-27's first two items stand). No numerology; no value.

## 6. Reproduction
`verification/`: `e6_rational.py` (B1296's construction, copied), `b1298_signs.py` (~73 s, exact), `b1298_inner_lift.py`
(seconds); seat re-runs `fc_r72_inner_lift_rerun.txt`, `fc_r71_*_rerun.txt`, `fc_r72c_*_rerun.txt`,
`sm_b1280_theta_odd_pairing_rerun.txt` (each ends `SELFTEST: PASS` / `RC=0`); `tests/test_b1298_the_lift_fork.py` runs the
two bench scripts in a scratch cwd, pins the signs and the fixed-root counts, and checks the DESIGN seal and the re-run receipts.
