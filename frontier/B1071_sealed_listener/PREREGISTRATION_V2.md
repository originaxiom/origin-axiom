# PREREGISTRATION v2 — B1071: THE SEALED LISTENER CELL (promotion of B1070's derivation)
# (v2 2026-08-19: supersedes v1 — hash f0b7726d…, preserved byte-identical as PREREGISTRATION_V1_SUPERSEDED.md in this directory — by adding the
#  seal-provenance gate's two required marker sections, which v1 carried as prose without
#  the literal markers. THE THREE CLAIMS ARE VERBATIM-UNCHANGED from v1; the computation
#  reported in FINDINGS ran against v1's sealed text, and v1's timestamp governs the
#  claims' pre-compute status. Candor over cosmetics: this file exists because the gate
#  is right that markers must be greppable.)
# (scratchpad draft; seals only after W6's checks + the owner-standing GO already given;
#  seal protocol: shasum → docs/SEAL_LEDGER.md → commit → push BOTH → then compute)

## SCOPE (binding, per the W6 adversarial reader's ruling)

This cell certifies **THE DERIVATION** — Λ's definition, its output, and the two
closed-form channel theorems — and NOTHING more. It does NOT certify a completed
listener map under `docs/LISTENER_MAP_SPEC.md`: AC3 (the sister transplant) gates on
the silver instrument's build, and AC6 (type conformance of the u-dependent
functionals) is a separate, unattempted run — both are OUT OF SCOPE here and are the
named next gates. Any text citing this seal says "the derived listener pair," never
"the listener map, constructed."

## The claim, sealed verbatim

Λ := the map assigning to the instrument (B593/B1011: ⟨R,L⟩ on ℂ⁶, the θ-grading,
ρ_odd = χ⊗V₂(2I) on ℂ²_odd) the set of directions u ∈ ℂP¹_odd such that
  (i) u lies in an exceptional orbit of MINIMAL size under the projective action of the
      instrument's full symmetry (Inn via ρ_odd's image; Out(2T×2I); no other input), and
  (ii) the ray of u is fixed INDIVIDUALLY by every element of Gal(ℚ(ζ₆₀)/ℚ).

CLAIM (three parts, each independently checkable, each able to FAIL):
  C1: the projective image of ⟨R,L⟩ on ℂP¹_odd is the 60-element icosahedral group, with
      exceptional orbits exactly 12/20/30 (+ generic 60). FAIL-witness: any fourth
      exceptional orbit, any other order profile.
  C2: Λ's output = EXACTLY {u3, u6} (hearing_family.py's banked pair): they lie on the
      size-12 orbit (R|_odd's own eigen-axis, projective order 5) and are the UNIQUE
      Galois-individually-fixed pair there. FAIL-witness: any third fixed direction, or
      u3/u6 landing off the 12-orbit, or a Galois element moving either ray.
  C3: the derived pair reproduces the banked instrument exactly: M_odd(g) = χ(g)W(g),
      W(g) ∈ SU(2), for all 2880 elements (B641's law as theorem), with
      Re(ζ⁻¹u†M_odd u) = ½tr W for every unit u (sanity, non-discriminating; THE
      CREDIT LINE, inherited from B1070's amendment: B641 named the mechanism first —
      "the strict law was SU(2) membership, not a hearing theorem" — this claim is the
      CLOSURE and POINTWISE FORM of B641's law, not a fresh discovery) and
      Im(ζ⁻¹u†M_odd u) = ⟨n(g), Bloch(u)⟩ separating points (the AC4′ witness).
      FAIL-witness: any element with W ∉ SU(2); any u-dependence of Re; Im failing to
      separate two named directions.

## BANKED IDENTITY: the pipeline reproduces Σ·Σ† = 75·I (exact) and the θ-grading's
##   exact invariance (B1011 C2) inside itself, from its own fresh build, BEFORE any new
##   number is read — the re-derivations' stated first checks.
## PRIOR ART: the design-time record — Klein's icosahedral orbit structure on ℂP¹ is
##   classical (typed; the claim's content is the IDENTIFICATION, not the orbit census);
##   the corpus anticipation sweep of 2026-08-18 (owner-prompted): B641 is the
##   mechanism's origin ("the strict law was SU(2) membership"), credited inside C3;
##   B593/B856 supply the pair as convention without uniqueness; B700/B713's
##   Galois-fixed vocabulary belongs to the disjoint observer battery (zero
##   cross-citations, grepped both ways).
## Inputs (banked, cited, not recomputed): B1011 C1–C6; B593/B856's instrument; B641.
## Method (sealed): independent re-implementation (no code reuse from wf_e25251a5-72a's
##   agents), exact ℚ(ζ₆₀)/cross-multiplication arithmetic, no float in any verdict line.
## MB12: each Cᵢ's fail-witness named above; the OPERATION is non-trivial (the generic
##   direction [1:1] has trivial stabilizer — computed, the not-bite case).
## Prior art (typed): the icosahedral orbit structure of ℂP¹ is classical (Klein). The
##   claim's content is the IDENTIFICATION: this instrument's banked listener pair = the
##   unique Galois-rigid vertex axis, plus both hearing channels in closed form.
## Outcome grammar: C1∧C2∧C3 → PROMOTED (the crossing prereg may cite Λ); any Cᵢ fails →
##   B1070 RETRACTED-or-narrowed per which link broke; partial = PARTIAL, stated.
## Gate 5: no measured number appears in this cell, its scripts, or its verdict.
