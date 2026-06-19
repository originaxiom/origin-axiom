# B180 — the two-faces dictionary (understand-completely #5): one hinge quantity, two analogous operations

**Date:** 2026-06-19. **Status:** the honest resolution of "what does *two faces of one principle* (K019) actually
mean — identity or analogy?" (#5 of the understand-completely menu). **Answer: a sharpening** — a single **hinge
quantity κ** genuinely lives on *both* faces (a real link, K010), while the two **interaction operations** are
**distinct-but-analogous** (not one map). **Firewall-side**: emergent low-dim-topology / spectral math (`K010`
boundary); no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V174. Reproducer `two_faces.py`
(`ALL CHECKS PASS`).

## The genuine link: κ is one quantity on both faces

- **C1 [κ conserved — the same number].** `κ = tr[A,B] = x²+y²+z²−xyz−2` is simultaneously (i) the **character-variety
  boundary coordinate** (`K001`/`K013`) and (ii) the **trace-map conserved invariant** (`K010`). Verified
  symbolically: the Dehn-twist trace maps **conserve κ** (`κ∘Ta = κ∘Tb = κ`, exact). So it is *literally the same
  conserved number* on the character-variety side and the spectral side — not two numbers that happen to rhyme.
- **C2 [κ sets the spectral type — live].** The invariant's *value* controls the spectrum: at its **periodic value**
  (Schrödinger coupling 0) the spectrum is a **full band** (0 prominent gaps); for **κ>2** (coupling 1.5) it is a
  **Cantor set** (13 prominent gaps). So the character-variety κ genuinely **governs** the spectral face. *This is
  the real, banked bridge (`K010`): κ is the hinge.*

## The fence: two distinct interaction operations (MB12)

- **C3.** The two **interaction operations** are **not the same map**:
  - **cusp-gluing** (`B174`/`B131`): match two *bundles'* boundary `(κ,P)` → a discrete **κ-fork** (e.g. `(1,2)→{−4,−2}`)
    — a **trace-matching** of two 3-manifolds;
  - **potential-weaving** (`B171`–`B176`): **add** two metallic Sturmian *potentials* → **gap labels** `n₁α₁+n₂α₂`
    (e.g. `(2,1)→0.6503`) — an **IDS frequency-combination** of a 1D operator.
  Different math, different *output type* (a trace-fork vs IDS-fractions). They share only the **conceptual
  signature** — *single unit = continuum* (`K013`), *distinct units = structure* (`K014`). So they are **analogues**,
  not one operation.

## The sharpening of K019

"Two faces of one principle" is honest, read precisely as: **(i) one hinge quantity κ** that genuinely lives on both
faces (character-variety boundary coordinate = spectral conserved invariant, governing band-vs-Cantor) — a real
identity (`K010`); **(ii) two distinct interaction operations** (cusp-gluing, potential-weaving) that share the
conceptual signature but are different math with different outputs — an analogy, not an identity. The naive read
("the κ-fork values *equal* the gap labels") is **false** (trace values vs IDS-fractions, distinct operations) — and
that is exactly the conflation the do-not-conflate boundary (`B179`) guards against.

## Scope / firewall
Emergent low-dim-topology / spectral mathematics; no physical-magnitude claim; **nothing to `../../CLAIMS.md`**;
P1–P16 untouched. Sharpens K019 (no retraction — "two faces" stands, read as hinge+analogues).

## Anchors
`K019` (the two-faces statement this sharpens), `K010` (κ = Fricke–Vogt invariant = trace-map invariant — the hinge),
`K001`/`K013` (κ as character-variety boundary coordinate; κ free), `B162`/`B163` (κ=2 full band / κ>2 Cantor — the
spectral-type thresholds), `B174`/`B131`/`K014` (cusp-gluing κ-fork), `B171`–`B176` (potential-weaving gap labels),
`B179` (the do-not-conflate boundary this is an instance of).

## Reproduction
`python frontier/B180_two_faces_dictionary/two_faces.py` — C1 the Dehn-twist trace maps conserve κ (symbolic);
C2 the live κ→spectral-type link (band at coupling 0, Cantor at 1.5); C3 the fence (gluing trace-fork vs weaving gap
labels). Prints `ALL CHECKS PASS`.
