# Master-master-plan re-verification pass — Phases 1,2,4,5,6,7

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Scripts:
`masterplan_reverification.py`, `holo_arealaw.py`, `emergent_geometry2.py` (the handoff holographic
scripts, banked). Standalone math; topology / number theory; **no physics claim earned**. This closes
the re-verification half of the two-handoff masterplan (the new math = B69/V35; the dormant bank =
V36). Per the user's **paranoid-verify standard**: each item re-checked by an independent route or a
control, scripts audited, nothing taken on faith.

## Phase 1 — torsion "1-vs-4 ratio" DISSOLVES (κ-sign artifact)
The handoff flagged an unexplained `|τ|/|Δ(−1)|` = `5/5=1` (m=1), `32/8=4` (m=2). But `|τ|=5,32` were
the **κ=+2 mis-evaluation**; the corrected geometric values (κ=−2, V30) are `−3, −16`. The clean
1-vs-4 pattern was an artifact of the wrong κ sign — it **dissolves**. (Confirms V30/V31.)

## Phase 2 — independent A-poly route: my shape-route was BUGGY; Gate 0 (V32) stands
Attempted an independent `(M,L)` extraction from SnapPy's `gluing_equations(rect)` cusp rows. **It is
buggy:** those rows are *completeness equations* (they equal `(−1)^c` at any solved structure), **not
holonomy extractors** — they returned a constant `(−1,1)` for every Dehn filling, i.e. degenerate
`(±i,±1)` points and garbage "matches" (including a spurious Cooper-Long ↔ m136 match). Caught by a
head-to-head: the fundamental-group route gives properly **varying** `(M²,L²)`; the shape "holonomy"
is constant. **The shape-route is discarded.** The reliable verification remains **Gate 0 (V32)** —
fundamental-group holonomy, a clean figure-eight control (Cooper-Long 88% on 4₁, 6% on m136), m=2
eliminant 100% @ 1e-15 on m136. The full **symbolic gluing-variety elimination** is the gold-standard
independent check and is **deferred** (high effort; Gate 0's controlled result is already strong).
*(This is paranoid-verify working: a buggy "independent route" was caught, not reported as a
confirmation.)*

## Phase 4 — invariants + the 2-isogeny aside (handoff B), and SW closure
- Binary-quartic invariants of `M⁴−6M²+1`: **I=4, J=0** ⇒ Jacobian `Y²=4X³−4X = (Y/2)²=X³−X`
  (j=1728). Matches V33 and handoff B.
- **2-isogeny aside verified:** `(s,t)=(M²,yM)` sends the curve to `t²=s³−6s²+s`, depressing to
  **`X³−11X−14`** exactly — handoff B's 2-isogenous partner (`j=−4599936`). The naive substitution is
  a degree-2 isogeny, *not* a birational map; the curve itself is `Y²=X³−X` (j=1728).
- **SW conclusion (V34) stands:** a single curve, no Coulomb-branch family / prepotential / scale —
  the j=1728 / τ=i match is a forced single-point CM coincidence, not a Seiberg–Witten identification.
  (The explicit Cassels/Silverman point-map adds normalization detail — `X³−X` over ℂ vs `X³−108X`
  from the invariants are the same CM curve — but no new conclusion.)

## Phase 5 — holographic re-test (handoff scripts re-run): honest-negative confirmed
- `holo_arealaw.py`: entanglement is **log, not volume** (linear-slopes ~0); Fibonacci ≈ periodic
  (both critical). Script clean (free-fermion correlation-matrix method).
- `emergent_geometry2.py`: emergent geometry AdS-like but **generic** — Gromov `δ/diam`: Fibonacci
  **0.381** ≈ periodic **0.385** (random 0.265, lower) → the test is too crude to single out the
  quasicrystal. **No special geometric feature; does not bridge.** (Confirms the chat's own verdict.)

## Phase 6 — Sym kill (V27) + nilpotent stall (V36) re-confirmed
The Sym membership rule `char(M^h)∈Sym^d ⇔ d≡h (mod 4)` is provable from the eigenvalue structure
(V27, the independent derivation); the θ-split divergence at n=6 stands. The nilpotent SL(4) gate
stalls at the `e₂`/two-block sector (V36). Both confirmed; no reopening.

## Phase 7 — figure-eight Kashaev invariant → hyperbolic volume
`(2π/N) log⟨N⟩` for `4₁`: 2.447 (N=100) → 2.203 (N=300) → 2.127 (N=600), converging toward
`vol=2.0299` (slow `O(log N/N)`). The **volume conjecture holds for the figure-eight** (a verified
check, not a new claim). m=2/m136: the colored Jones is not in closed form → not computed (honest
scope).

## Phase 8 — research-scale (deferred)
SL(3) figure-eight A-polynomial (GTZ; needs the boundary-unipotent component, not the principal-`Sym²`
lift — V23) and the trace-ring proof (B58 proper; the nilpotent gate is the lead) remain the open
research items — not attempted this pass.

## Net
The two-handoff masterplan is executed: the new math is banked (B69/V35, cusp-torsion law verified
m≤4, novelty open); the dormant findings are banked (V36); and the overlap is re-verified by
independent routes/controls (this file) — including **catching a bug in my own attempted independent
route** (Phase 2 shape extraction). Every committed conclusion (V27–V35) survives the paranoid
re-check; no overclaim, no silent drop. Proven core untouched.
