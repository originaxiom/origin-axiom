# B370 (W2.5) — third-order integrability + the depth-2 boundary Gram: PRE-REGISTRATION

**Campaign W2.5. Two legs, two-outcome each. Committed BEFORE any computation runs. The execution rule
learned in B366 applies: the third-order relator expansion is DERIVED SYMBOLICALLY FIRST and validated on
the integrable control before any verdict is read.**

## Leg A — the third-order Maurer–Cartan obstruction (the Massey leg)

**Object.** For each exponent direction `z₁ = z₁(m)`, `m ∈ {1, 4, 5, 7, 8, 11}` (the B347/B352 tangent
classes of the figure-eight's E₆ character variety at the geometric representation): B352 proved the
second-order class `[z₁ ∪ z₁] = 0` (exactness — a `z₂` with `d z₂ = −q₂` exists). The third-order
deformation equation adds `d z₃ + Q₃(z₁, z₂) = 0`; its obstruction class `[Q₃] ∈ H²` (the Massey-type
class `⟨z₁, z₁, z₁⟩`) decides integrability at order 3.

**Construction (declared).**
1. **Derive the order-3 expansion symbolically first**: expand `X(rel)` for
   `ρ_t = exp(t·c₁ + t²·c₂ + t³·c₃)·ρ` through `t³` on the length-9 relator `abbbaBAAB` via Fox
   calculus + BCH, obtaining `Q₃` as an explicit bilinear-plus-trilinear cochain in `(z₁, z₂)`.
   The derivation is validated on two exact identities before use: the coboundary control (must give a
   coboundary at every order) and d-square-zero consistency of the expansion.
2. `z₂ := −d⁺ q₂` (minimal-norm solve in the B352 block coordinates; dps 100). **Gauge caveat named:**
   `z₂` is defined modulo `Z¹`; the Massey class is well-defined modulo the indeterminacy
   `z₁ ∪ H¹ + H¹ ∪ z₁`. We compute the indeterminacy subspace inside `H²` explicitly and pair `Q₃`
   against functionals **transverse to it** (MB12 control: the transverse pairing must be non-vacuous on
   random vectors).
3. Machinery: B352's two-basis architecture unchanged (exact root-basis brackets; block-diagonal group
   action; vectors cross at dps 100); B352's integrity gates re-run (relator identity, bracket
   preservation, cocycle residuals) and must pass at their banked thresholds.

**Gates (all must pass before verdicts are read):** the m=1 control — the real A-polynomial curve is a
genuine curve through the representation, so its direction is integrable to all orders: **its third-order
class must vanish**; the coboundary control; the MB12 transverse-pairing control; `rep_checks`.

**Outcomes (both bank):** (i) all six directions unobstructed at order 3 ⇒ the smoothness evidence for
the 6-dim moduli strengthens one order (tier: computer-assisted, conditional — an obstruction may appear
at any higher order; no "smooth, period" claim); (ii) any direction obstructed ⇒ a sharp structural
finding (a formal tangent direction dies at order 3 — Gate-B-relevant news), reported with the class
components and the transversality control.

## Leg B — the depth-2 boundary Gram (the NZ correction)

**Object.** B357 certified: `rank(r) = 6`, the image `r(H¹(M)) ⊂ H¹(T², 𝔢₆)` is Lagrangian, and the
boundary shape is universal (`τ = −2√3·i` at every exponent). Leg B computes the **second-order boundary
data**: restrict the solved `z₂(m)` to the peripheral torus and form the depth-2 Gram
`G₂[m, m′] = ⟨r(z₂(m)) ∪ r(z₁(m′))⟩` against the B357 conventions (same complementary Lagrangian, same
normalizations — declared identical, no re-tuning).

**Pre-registered nulls (written before computing):** `G₂` is NOT assumed symmetric, universal, or
τ-aligned. Three declared readouts: (i) is `G₂` symmetric? (ii) does the universal-τ persist at depth 2
(the depth-2 shape per exponent equals the depth-1 shape) or split? (iii) block structure vs the θ-grading
(E₆/F₄ vs F₄ blocks). Whatever pattern appears is reported as data; a null pattern (unstructured `G₂`)
banks as the honest answer.

**Deliverable.** The Gate-B specialist package completes: first-order Lagrangian + universal-τ (B357) +
second-order smoothness (B352) + third-order verdict (Leg A) + the depth-2 Gram (Leg B) — the full
classical germ of the would-be `T[4₁;E₆]` integration cycle, whatever it turns out to be.

## Guards

MB12 (transverse pairing non-vacuity; the m=1 all-orders control), the B352 numerical-floor discipline
(report class components against per-direction floors, θ-parity signature check), no re-tuning of any
B352/B357 convention, atlas/FAILURE_ATLAS consulted (no prior Massey probe exists; B352's two recorded
architecture failures — double precision, Euclidean normalization — are not re-walked). Exact where
possible; dps 100 where not; every verdict with its controls in the same table.
