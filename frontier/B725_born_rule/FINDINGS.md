# FINDINGS — B725: THE BORN RULE — the observer construction gives Born FORM (+ why quadratic), not Born CONTENT

cc banking seat, 2026-07-20. Prereg sealed `fecb337a` (frontier/B725_born_rule/PREREGISTRATION.md).
Ran as a multiagent loop campaign (wf_739739fb-1df: 3 probes × compute → 3-skeptic adversarial
verify → refine, web-enabled). **Cross-verified against cc2's independent axiomatic run**
(wf_73cde374, relay CC2_TO_CC_2026-07-20_born_rule.md) — the two seats ran the same door from
opposite angles (cc = SSB-dynamics; cc2 = axiomatic/forced) and **converged**. Gate 5 holds:
operator-algebra/modular structure only, no SM value, the observer's choice stays free (B701).

## VERDICT — OUTCOME A, honestly bounded: FORM forced (+ the quadratic explained), CONTENT open

The observer construction (B723: observer = a state on the object's algebra, born at the β=1 SSB;
S070/B723: the observer's c-swap = the modular conjugation J) gives a **genuine structural account
of the Born rule's FORM**, and adds a mechanism for **why the form is quadratic** — but does **not**
deliver the Born rule's quantum **CONTENT** (interference between outcomes; the specific non-uniform
pure-state weights |⟨e|ψ⟩|²). Precisely: **form yes, content open.** Not "we derived the Born rule."

### Probe 1 — WHY QUADRATIC = the c-swap order (A, high; the piece cc2's run did not have)
The Born rule is quadratic because the observer's fundamental operation is the **c-swap**, and the
probability pairs ψ with its swap-image:
```
|ψ|² = ψ·c(ψ) = N_{ℂ/ℝ}(ψ) = ∏_{g∈Gal(ℂ/ℝ)} g(ψ)    (verified: = x²+y², total degree 2)
```
The **degree of the invariant norm = the order of the swap group** (computed both directions
in-sandbox): the c-swap `Gal(ℂ/ℝ)` has order 2 (complex conjugation is the unique nontrivial
involution of ℂ/ℝ) → degree-2 form → **quadratic**. Live falsifier confirmed: an order-3 swap
(cyclic cubic field ℚ(2cos2π/7), min poly t³+t²−2t−1) gives a degree-**3** norm — had the c-swap
been order 3 the probability would be cubic. The modular conjugation **J** was built explicitly on
the GNS/HS space (J(a)=a*, antiunitary ⟨Ja,Jb⟩=conj⟨a,b⟩, J²=1, JMJ=M', S(xΩ)=x*Ω, all to ~1e-15);
the Born pairing's **conjugate-linear bra slot IS this antilinearity of J**.

**Skeptic refinement (adopted):** order-2 alone forces the degree's **parity (even)** — killing
linear and cubic; it does *not* by itself rule out quartic (ψ²c(ψ)² is equally phase-invariant).
**Gleason (probe 3) closes it to exactly 2.** So the honest statement is: *the c-swap fixes the
degree's parity (even, so not cubic/linear); Gleason selects the quadratic representative Tr(ρP).*
The genuine new content over "a state is defined to give |ψ|²" is the **degree = swap-order
mechanism** (falsifiable) and the identification **conjugate-linear-slot = J**. Rung 3.

*Input, not derived (flagged):* that amplitudes live in ℂ at all — so the c-swap = Gal(ℂ/ℝ) is
order 2 — is itself the observer's complex-structure closing (B715/B716), an input here.

### Probe 2 — the SSB weights are Tr(ρP) = the FORM, i.e. Gibbs, not the CONTENT (A, high — reconciled)
In the finite-dim model, the β=1 SSB selects the **orthogonal pointer MASA**, and its decomposition
weights are `p_i = e^{-βE_i}/Z = Tr(ρ P_i)` exactly (~1e-16, n=2,3,5, β∈{0,…,16}). Non-vacuous:
a *non-orthogonal* ensemble for the same ρ (overlap 0.4) gives weights that **differ** from Tr(ρP)
(0.58≠0.50, Σ=1.16≠1) — so "SSB → orthogonal pointer decomposition → weights = Tr(ρP)" is a real
discriminator, not the trivial spectral identity applied blindly.

**But this is the Born FORM, not the CONTENT (reconcile with cc2, verified in-sandbox):** ρ here is
**thermal**, so Tr(ρP_i) are **Gibbs** weights (classical, already-decohered). Two facts, both
recomputed in-sandbox this pass, pin the gap:
- **Gleason does NOT fix the weights on the broken/abelian outcome algebra.** Once the SSB breaks to
  the classical pointer algebra (⊕ℂ, all minimal projections type-I₁), the frame-function
  constraint is vacuous: a pure state's Born weights |⟨e_i|ψ⟩|²=(0.369,0.138,0.493) and a Gibbs
  vector (0.631,0.284,0.085) are **both valid states** — Gleason singles out neither. cc2's
  "**Gleason's exclusion zone IS the frame's outcome zone**" (the torsor points = the type-I₁ blocks
  Gleason excludes) is **CONFIRMED**: Gleason forces the form on the ambient factor but says nothing
  about the weights *across* outcomes. Those come from a separate thermal/KMS input.
- **The CMR extremal-KMS formula is diagonal** (cc2, cited from CMR math/0501424):
  `φ_{β,L}(f)=ζ_K(β)⁻¹ Σ_J f(J⁻¹L,J⁻¹L) N(J)⁻ᵝ` — same J both slots, a classical Gibbs measure over
  ideals, **no interference** term. Consistent with an extremal KMS = an already-decohered pointer.

So probe 2 delivers the **form** and honestly stops there; genuine SSB/non-trivial central-measure
content needs the thermodynamic limit (M_n is a factor, trivial center) — modeled, not reproduced.

### Probe 3 — the honest floor: Gleason forces the form once observer = state (A, high)
A state ω on the object's vN algebra is a positive normalized functional; on projections ω(P) is a
noncontextual frame function; **Gleason** forces `ω(P)=Tr(ρP)` on dim≥3 / factors without
type-I₁,I₂ summands — which the II₁ object algebra (B721) and III₁ observer algebra (B723) are.
The harmonic core was reproduced in-sandbox: the SO(3)-equivariant frame-sum vanishes-in-variance
**only** at Legendre degrees {0,2} (l=0 dim 1 + l=2 dim 5 = 6 = dim of symmetric 3×3 forms), and is
non-constant (uncancellable) at l=1,3,4,5,6 — so smooth frame functions are exactly quadratic forms
= Tr(ρP). Non-vacuity shown by the explicit dim-2 counterexample (h(n)=n_z³ is a valid non-Born
frame function — Gleason genuinely needs dim≥3). **Honest bound:** Gleason is the CITED
load-bearing theorem; the computation demonstrates its algebraic/harmonic core but does not reprove
its hard analytic continuity lemma. The framework's three additions are structural
**identifications**, not independent derivations: (state-supplier = B723) · (c-swap = quadratic =
probe 1) · (SSB = orthogonal pointer weights = probe 2).

## THE TWO-SEAT JOINT RESULT (cross-verified, no seam)
| part | status | who |
|---|---|---|
| **probabilism is native** (a state / a thermal KMS state IS a probability) | ✓ delivered | both |
| **Born FORM forced** (ω(P)=Tr(ρP), Gleason, on the frame's own II₁/III₁ factors) | ✓ delivered | both |
| **why the form is QUADRATIC** (degree = c-swap order 2; parity even, Gleason closes) | ✓ **cc adds** | cc (probe 1) |
| **SSB selects the orthogonal pointer decomposition** (weights = Tr(ρP), non-vacuous) | ✓ delivered | cc (probe 2) |
| **Born CONTENT: interference + non-uniform pure-state \|amp\|² weights** | ✗ **OPEN** | both (cc2 sharpest) |

**The honest bottom line:** the frame gives *classical Gibbs probabilism wearing the Gleason-forced
Born form, with the quadratic degree explained by the observer's c-swap* — and the genuinely quantum
part (interference among outcomes, the specific state-dependent weights) is an **open gap**.

## The deepest caveat (both seats foreground it)
The entire row **inherits "measurement = the β=1 SSB" (B723)** as an axiom — no probe re-derived it.
The form/content split is a structural fact *given* the frame's factors and that identification;
whether "measurement = the SSB" is physically right is the deeper unproved premise.

## Placement
LAW_MAP: the Born-rule row = FORM forced (+ quadratic from the c-swap), CONTENT open. **Nothing to
CLAIMS.** No SM value. Credit cc2 (flagged the door; the axiomatic cross-check; the content-gap
framing). Choice free (B701). Next doors (to close/kill the content gap): Busch POVM/unsharp-Gleason
on the III₁ layer; Zurek envariance (non-uniform weights from symmetry, vs the torsor's Haar
uniformity); read the full CMR/Hecke algebra (off-diagonal interference the diagonal φ_{β,L}
suppresses?); Ojima/Ozawa (KMS↔Born direct); and interrogate "measurement = the SSB" itself.
