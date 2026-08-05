# B915 PREREGISTRATION — R4: THE CROSSING (sealed before any data contact)

**Date sealed:** 2026-08-05 · **Seat:** cc (banking) · **Register:** ROADMAP
REGISTER v1, rung R4, protocol locked (one input, sealed prereg, two outcomes,
no fitting — the non-weakening clause applies to this document itself) ·
**Owner authorization:** "moment has come" (2026-08-05).

## What is being tested (the physics identification, named exactly)

**The identification under test:** the object's gauge boundary — E₆ unification
(one coupling g_U at one scale M_U, with the banked exact boundary value
sin²θ_W(M_U) = 3/8 implied by the trace identities Tr(T₃²) = 3, Tr(Y²) = 5,
Tr(T₃Y) = 0) — matched to the measured low-energy gauge couplings through
**standard-model running across an assumed desert** (no intermediate
thresholds). The desert assumption is PART of the identification under test:
a MISS kills "object boundary + SM desert," not the object's structure.

## The one input (the observer-coupling normalization)

**α_em(M_Z)** (MS̄), the electromagnetic coupling — the observer's own probe.
No other measured number enters the construction; the two remaining gauge
observables are the TEST PAIR, contacted only at verdict time:
sin²θ_W(M_Z) (MS̄) and α_s(M_Z).

## The declared imports (textbook, verifiable, fixed now)

Two-loop SM gauge β-functions (three families, one Higgs doublet — the SM
field content the structure itself selected in B892/B897); one-loop matching
at M_U (no threshold corrections — the desert); GUT-normalized hypercharge
g₁² = (5/3)g′² (the normalization under which 3/8 is the banked boundary
value). Data source: the current PDG world averages, fetched AFTER this seal;
their central values and quoted uncertainties are used as published, with no
reinterpretation.

## The construction (no fitting anywhere)

Given the single input α_em(M_Z): impose g₁(M_U) = g₂(M_U) = g₃(M_U) = g_U.
With three unknowns (sin²θ_W(M_Z), α_s(M_Z), M_U) and two matching conditions,
the solution is a ONE-PARAMETER CURVE 𝒞 in the (sin²θ_W(M_Z), α_s(M_Z)) plane,
parametrized by M_U ∈ [10³ GeV, M_Pl]. 𝒞 is the object's prediction under the
identification. Computed at one loop and at two loops.

## The two-outcome criterion (sealed band, truncation-dominated)

Let d = the minimal distance from the measured point P = (sin²θ_W, α_s)(M_Z)
to the two-loop curve 𝒞₂, measured componentwise in units of
σ_tot,i = sqrt(σ_exp,i² + σ_th,i²), where σ_th,i = |𝒞₂ − 𝒞₁|_i at the
nearest-approach parameter (the 1↔2-loop shift as the truncation proxy),
componentwise for i ∈ {sin²θ_W, α_s}.

- **OUTCOME HIT:** d ≤ 3.
- **OUTCOME MISS:** d > 3. The banked deliverable is then the QUANTIFIED
  failure mode: the three pairwise meeting scales M_{ij} (g_i = g_j), their
  spreads, the sin²θ_W gap along 𝒞, and the sign/direction of the deviation —
  the data the registered follow-up needs.
- **UNSTABLE:** the curve construction fails numerically (a computation
  error — recompute; not an outcome).

## The disclosed prior (stated with its reasons, then the cell decides)

**MISS, high confidence.** The non-meeting of the SM gauge couplings under
desert running is classic (the three pairwise meeting scales differ by orders
of magnitude). The last four sealed priors lost; this one is stated anyway,
with its literature-standard reason. THE INFORMATIVE CONTENT OF A MISS is the
quantified failure geometry, which becomes the input to the registered
follow-up **R4b (NOT this cell, requires its own seal): does the object's own
compact-measurement chain — the banked D-chain E₆ ⊃ D₅ ⊃ D₄ ⊃ D₃ ⊃ A₂-floor
(§LVIII, B909 lane) — supply the intermediate thresholds that move the curves,
with NO new free parameters beyond the chain's own banked scales?** If the
object's ladder is the desert's replacement, the failure geometry of THIS cell
must match the chain's correction pattern — a sharper, second crossing.

## What a MISS does NOT kill (pre-stated, per the register)

Every structural theorem (the FMT/SMT, the tiling isomorphism, the classes,
the atoms, T, I = −1, e₆(2), the signature split); the 3/8 boundary value AS
STRUCTURE; the flavor skeleton. It kills exactly: "the object's boundary +
pure SM desert" as a physics identification.

## Files (after sealing)

`crossing.py` → `results.json`; `FINDINGS.md` verbatim against these
criteria; locks in `tests/test_b915_crossing.py` (seal-integrity first).
