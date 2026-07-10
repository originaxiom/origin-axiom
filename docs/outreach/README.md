# External-specialist briefs — index

This directory holds the outbound specialist package regenerated from the current corrected
sources after the Closure Campaign (2026-07). Each brief is self-contained, at most two pages,
honest about proof status, and carries **one question for one kind of expert**. There is no
physics framing and no undefined internal vocabulary; every brief ends with a provenance line
naming the internal computations (B-numbers) it rests on.

## The discipline (please keep it when using these)

- **One gate, one expert, one question per contact.** No cross-brief storytelling; lead with the
  concrete computed object, never with the wider program.
- **Honest proof-status line stays in.** A "known, see [reference]" reply is a *good* outcome — we
  want the state of the evidence, not encouragement.
- **Sending is owner-gated.** These briefs are prepared, not sent. Any contact, address, and
  covering note is decided by the project owner; regenerating the package is explicitly separate
  from sending it.

## What each brief is

| file | subject | one question | expert type |
|---|---|---|---|
| `GATE_B_brief.md` | Realization of `T[4₁; E₆]` (3d-3d correspondence at exceptional gauge type), with the character-level embedding search reduced to 28 explicit survivors | Does an exceptional-type state-integral `T[4₁; E₆]` exist, and does any of the 28 surviving 27-dim assemblies realize as an actual `2T ↪ E₆` homomorphism? | 3d-3d / character-variety specialist (Dimofte / Garoufalidis class) |
| `GATE_D_brief.md` | Spectral theory of a non-self-adjoint Fibonacci-type operator at complex coupling `κ = √3·e^{±iπ/6}` | Is there a Damanik–Gorodetski-type structure theorem in this non-Hermitian regime? | non-self-adjoint spectral theorist (Damanik / Gorodetski school) |
| `R1_held_breath_brief.md` | The divisor-indexed torsion field law on the one-holed-torus character variety, now a corollary of Cantat's fixed-curve method | Is the divisor-indexed *completeness* statement genuinely new, or a known corollary? | character-variety dynamicist (Cantat–Loray / Goldman / Markoff-dynamics) |
| `R2_seam_brief.md` | The level-15 pair invariant whose √−15 Galois channel vanishes in a subfield-lattice pattern | Why do the flagship pair's 5-side windows never mismatch under the c₃-flip? | Weil representations / modular data / arithmetic of quantum invariants (Gannon type) |
| `TOWER_carrier_selection_brief.md` | The forced Sym⊗det block form of the SL(n) trace-map tower, and the residual carrier-selection rule at n ≥ 5 | Is there a canonical, filtration-independent rule that selects the carrier copy inside the n ≥ 5 multiplicity space? | invariant theorist / geometric representation theorist |

There is no Gate A brief and no Gate C brief here on purpose: **Gate A** is an in-sandbox theorem,
now sealed at the computable horizon (below), so it carries no outbound question; **Gate C** is
closed by its own written refutation condition. Only **B** and **D** remain as genuine specialist
gates, and they are joined by the two novelty questions (R1, R2) and the tower question.

## Status of the four gates after the campaign

- **Gate A** (any invariant of the single seed that is trace-map-invariant, discretely multivalued,
  and unsymmetrizable — a genuine forced choice): **sealed across thirteen invariant classes at the
  computable horizon** — the eight sealed before the campaign by one Galois-orbit mechanism, plus
  the five Phase-2 classes: nonabelian adjoint/Reidemeister torsion of the SL(2,ℂ) character
  variety (B495), Chern–Simons / complex-volume (B496), irregular covers at index 7–8 (B500),
  SL(3,ℂ) gluing/character-variety invariants (B498), and the extended-Bloch / K₃^ind class (B497).
  Every class hands back a symmetric Galois orbit, never a distinguished member. Honest scope: this
  is "sealed at every computable horizon," not a proof of universal impossibility.
- **Gate B** (`T[4₁; E₆]` realization): **reduced** — the character-level chiral-embedding search
  collapses from 70262 candidates to **28 explicit survivors** (B501); the escape sector `{4,8}` is
  **integrable through order 4** (B501); and the manifold's involution is proven to induce the
  diagram involution θ on the E₆ tangent, **canonically** (the tangent-level θ-identification
  theorem, B501). The realization question itself stays specialist. See `GATE_B_brief.md`.
- **Gate C** (does the intrinsic commensurator ℤ/3 permute three symmetric copies of the 27):
  **closed** — computed on every available substrate, the commensurator ℤ/3 acts *within* a single
  27 (as the E₆ ⊃ SU(3)³ grading / triality, or as scalar multiplication on one indecomposable
  Eisenstein module) and never permutes three symmetric copies; the three-copies exhibit appears
  nowhere and its necessary conditions are positively refuted (B502).
- **Gate D** (a non-Hermitian Damanik–Gorodetski theorem): **data-banked with two conjectures** —
  D1 (complex-horseshoe uniform hyperbolicity) and D2 (pseudospectral correspondence with
  polynomial condition numbers), each a precisely posed, data-supported conjecture, never a claim
  (B499). See `GATE_D_brief.md`.

**Provenance.** Rests on B493–B503 (Closure Campaign Phases 1–4), `docs/OPEN_PROBLEMS.md`
(the four gates), and `docs/CLOSURE_CAMPAIGN_2026-07.md` (the pre-registrations). Nothing here
promotes to `CLAIMS.md`; the physics firewall is untouched.
