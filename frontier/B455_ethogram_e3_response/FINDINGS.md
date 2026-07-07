# B455 — Ethogram E3: stimulus-response — the engine boundary (quantified) + the homeostasis retirement

**Status: banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md` (PR #598, before
computation). Verdict: ENGINE-BOUNDARY, quantified — the prereg's gates did exactly their job
(they blocked two unsound runs and priced the sound one out of budget); the banked infinitesimal
answer (B352/B370: flat to 3rd order) stands as the response card's content. Plus one clean
retirement: the homeostasis card dies by computation, as predicted. No H1.**

## What happened (the honest chronicle)

1. **Engine build:** ρ₀ = Ad(principal(ρ_geo)) as 78×78 from B351's exact brackets + the chain
   basis; H¹ directions per Sym-block; Newton continuation on the relator residual (`integrate.py`).
2. **GATES FIRED — first run refused:** relator residual 1.4e39; offblock 5e4. Diagnosis #1:
   the raw chain vectors are factorially skewed — **cond(S) = 3.5e52**; Sinv was garbage. Fixed
   (normalized columns; cond < 1e6 asserted). The sl2 triple itself is EXACT
   (‖[H,E]−2E‖ = ‖[E,F]−H‖ = 0 to machine zero).
3. **GATES FIRED AGAIN — second run refused:** block structure now clean (offblock 1.3e-9 ✓) but
   the relator residual stayed 1.4e39 (relative 2e16). Diagnosis #2 (definitive, block-wise):
   the engine is **structurally correct** — per-block expm reproduces tr Sym^{2m}(ρ_geo(a))
   exactly through m = 8 (10+ digits) — and the failure is pure **dynamic range**:
   ad(ξ) eigenvalue real parts span ±18.3 per generator; the m=11 block alone has norm 7e22
   (float64 already loses its trace at 2e-5 relative); relator prefixes reach ~e⁶⁹, so the
   telescoping cancellation floors at ~1e14 absolute error. **No float64 representation runs this
   continuation** (the minuscule 27 improves the exponent 22→16 — still e⁵⁰-scale prefixes).
4. **The priced-out sound route:** arbitrary-precision (dps ≥ 50) Newton with finite-difference
   Jacobians costs ~3 h per iteration (156 residual evaluations × ~70 s each) — orders of
   magnitude over the prereg's 60-min ceiling. Chord-Newton (frozen approximate Jacobian) reduces
   this to ~15 min per t-step — still ≥3 h per direction × 6 directions. An order-4 jet extension
   of the B352/B370 engine is the symbolic alternative (~12–24 h). **Both named, both priced,
   neither run: the pre-committed ceiling binds.**

## The verdict per the prereg taxonomy

The taxonomy assumed Newton would run; it did not get the chance — the honest bin is the one the
campaign's F3 precedent established: a **named, quantified boundary**. What stands as the
response card's content: the deformation space is **flat to third order in all six directions**
(banked, B352 dps-100 + B370) — the infinitesimal response is zero curvature, the exact opposite
of a mass hierarchy, consistent with every scale-free result. The finite continuation is the
named follow-up with concrete requirements (above). This also closes the handoffs' "Test 2"
adjudication: even the infinitesimal Hessian is banked zero; the finite version is genuinely
expensive and cannot be run casually by anyone.

## The homeostasis card: RETIRED (by computation, as predicted)

`homeostasis.py`, exact rationals: perturb the Markov point (3,3,3) off κ=−2 by ε ∈ {1/10, 1/100};
iterate the trace map 12 steps; **κ is conserved EXACTLY along the perturbed orbit** — the
dynamics never returns to the surface. No restoring response exists (conservative dynamics, no
transverse attractor). The S055 card's built-in falsifier fired; the card retires with its
dignity intact — this is precisely how the full ethological frame was designed to work: the
mapping failed honestly and taught us the disanalogy (the organism has no homeostasis because it
has no dissipation).

## Reproduce
```
python3 integrate.py      # the gates fire and refuse (the chronicle above)
python3 homeostasis.py    # the exact retirement
pytest ../../tests/test_b455.py
```
