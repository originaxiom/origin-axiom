# B455 — PREREGISTRATION: Ethogram E3 — stimulus-response: integrate the curve

**Committed before computation. Firewalled. Campaign: OPEN_LEADS §Ethogram; dictionary cards:
"response", "homeostasis" (S055).**

## The question (blind)

What does the object DO away from equilibrium? Finite deformations along the FIVE non-geometric
E₆ moduli directions (exponents m ∈ {4,5,7,8,11}) at the principal point — never integrated
(B352/B370 banked orders 1–3 as unobstructed/zero; the curve itself unrun).

## Design

Engine: the adjoint realization. ρ₀ = Ad∘(principal∘ρ_geo) as 78×78 (block-diag Sym^{2m} in the
chain basis — the B445 formulation), built from B351's exact brackets + B352's chain vectors +
SnapPy holonomy. Deformation: ρ(a) = expm(ad_u)·ρ₀(a), ρ(b) = expm(ad_v)·ρ₀(b); Newton
continuation in t along each H¹ direction (least-squares on the relator residual; float64,
landed points verified at mpmath dps≥30). ENGINE GATES (must pass before any run): (i) the
built Ad(ρ₀) is block-diagonal and matches the B445 Sym-blocks; (ii) the relator residual at
ρ₀ is machine-zero; (iii) the H¹ dimensions reproduce B445 (=1 per block).

**The run gate (must pass FIRST):** direction m=1 (geometric) — the continuation must stay
block-diagonal (sl2-factored) and track the known A-polynomial curve. FAIL ⇒ fix the engine,
no non-geometric runs.

**The probe:** the five non-geometric directions, each continued t: 0 → t_max (step 0.05–0.1,
adaptive halving). **Landing-verdict taxonomy (every run must end in exactly one):**
- COMPONENT-FOUND: converged at t_max with residual < 1e-9 (float) verified < 1e-25 (mpmath),
  invariants stable → identify (traces via PSLQ; block structure; H¹-projection).
- WALL: Newton fails beyond t* despite ≥4 step-halvings → certify the radius t*.
- OBSTRUCTED-AT-ORDER-k: divergence as t→0 scaling like a jet obstruction (would contradict
  banked B352/B370 — escalate as an anomaly if seen).
- DIVERGENT: unbounded invariants along the continuation.
"Nothing happened" is inadmissible.

## Bins
All five land COMPONENT/WALL with whitelist-expressible invariants → LAUNDERS. A landing with
non-whitelist exact invariants (PSLQ-identified, out of the frozen list) → escalate (B398). A
genuine OBSTRUCTED signature → NEW-MATH (contradicts banked smoothness — adversarial recompute
first).

## Controls
5₂ at ITS principal point (B444/B445 data; its own holonomy + H¹): the gate direction + ≥2
non-geometric directions through the identical engine. (Silver is out of scope: no banked
geometric holonomy for the RRLL bundle in the sandbox; stated, not hidden.)

## Ceiling & tier
Wall-clock ceiling 60 min total continuation compute; float64 with mpmath verification of
LANDED points only. Conditional tier note: the direction vectors inherit B352's dps-100
numerics (the W2.10 self-bar) — landings bank at the same conditional tier, stated.
