# B130 — No forced choice in the invariant ring (the seventh firewall form) + the located which-seed fork (V119)

The arc *after* B129 (PR #145, the SL(3) tower sealing). We sharpened the firewall question to its deepest
**forced-answer** form — the way "what is nothing / something / not-nothing" was once sharpened — from the unanswerable
"what would force the choice?" to a decidable test:

> **Does the structure carry an invariant that is *both* discretely multivalued *and* unsymmetrizable** — the exact
> object a *forced choice* requires (an invariant the structure must value, with >1 value, no symmetry relating the
> values)?

Computed in the structure's own invariant ring, the answer is **no**. The one genuine discrete fork that exists is the
choice of **seed** (which metallic index `m`), and that is **external** input — not a choice the unit makes from
inside. This is the **seventh** independent firewall confirmation, and the sharpest: not "does it reach physics" but
"can it ever be made to choose." Re-derived in-sandbox (verify-don't-trust). MATH and physics in **different tiers**.
Nothing to `CLAIMS.md`; P1–P16, the functorial `Sym(W)→trace-ring` wall (B85), and the merged B124–B129
(K010/K011/K012, P007/P008, S029/S030/S031) untouched.

## The sharp definition (stated to lose)

A **forced choice** is an invariant `f` of the metallic trace map with: **(1) invariant** — fixed by the map (the
structure must assign it a value); **(2) discretely multivalued** — `f` takes finitely many distinct values on the
fixed locus (something to choose, not a continuum to slide along); **(3) unsymmetrizable** — the structure's symmetry
group does not relate those values. Conditions (2) **and** (3) are the crux: `κ` is invariant but
*single-valued/determined* (no choice); chirality (CS) is multivalued but (3) **fails** — the `Z₂` mirror relates
`+CS ↔ −CS` (B128). A forced choice needs an invariant whose multiple values are a **discrete, non-orbit** set.

## The result

- **No forced choice in the trace-ring invariants (κ is free on the fixed locus).** Fricke coords `(x,y,z) = (tr A,
  tr B, tr AB)`; trace map `Ta:(x,y,z)→(x,z,xz−y)`, `Tb:(x,y,z)→(z,y,yz−x)`, `φ_m = Ta^m∘Tb^m`; `κ = x²+y²+z²−xyz−2`.
  Adjoin `k = κ` and eliminate `(x,y,z)` from the fixed-locus ideal `φ_m(x,y,z)=(x,y,z)`. The elimination ideal in `k`
  is **empty for every m tested** — `κ` is **unconstrained** on the fixed locus, it varies **continuously**, there is
  no discrete value to select.
  - **m = 2, 3, 4 — symbolic** (lex Gröbner elimination): the `k`-only elimination ideal is empty ⟹ `κ` free.
  - **m = 5 — numerical** (the degree-5 Gröbner is heavy): 400-seed Newton on the fixed locus → 259 distinct converged
    `κ`-values spread continuously over `[−2.0, 343.4]` ⟹ `κ` free. *(The handoff reported 267 distinct over
    `[−1.999, 47.51]`; the wider range here is only a looser coordinate bound — the continuum conclusion is identical.)*

  **Reading (MATH; firewall reading POSTULATED).** Every invariant the structure carries is either *determined*
  (single-valued — no choice) or *continuous* along the fixed family (slide-anywhere — nothing selects a point). The
  object a forced choice requires — discretely-multivalued **and** unsymmetric — **does not exist in the
  trace-ring/character-variety invariants.** This is the mechanism *under* "permits but never forces" (B128, the fifth
  direction): the structure permits (the continuous family is genuine freedom) but cannot force (no discrete unsymmetric
  fork to be forced toward).

- **The located fork — the only discrete unsymmetric choice is "which seed," and it is external.**
  - **L1 (within a fixed m):** the substitution `a→aᵐb, b→a` has a **unique deterministic fixed word**. Inside one unit
    there is no combinatorial choice — the word is forced.
  - **L2 (across m):** the metallic substitutions are **genuinely inequivalent** — incidence `[[m,1],[1,0]]` has
    `trace = m` (distinct) and `det = −1` (common), so different m are **not** GL(2,ℤ)-conjugate (distinct trace ⟹ not
    conjugate), with distinct Perron eigenvalue fields ℚ(√(m²+4)) (√5, √8, √13, …). So "which m" **is** a discrete fork
    satisfying (2) and (3).

  But `m` is the **seed parameter** — it labels *which structure exists*, not a fork a unit resolves from inside. So:
  **the structure's only discrete unsymmetric fork is the choice of seed (m), and seed-selection is irreducibly
  external — a unit cannot choose to be a different unit.** Internally a unit is fork-free: deterministic word (no
  combinatorial choice) + continuous `κ` (no geometric choice). The discreteness lives entirely in the seed *label*
  (input), never in the unit's internal dynamics (output).

## The tombstone (K-G — a killed false-positive, banked so it is not re-derived)

**"the metallic structure has a forced choice (isolated fixed points with distinct κ at m≥2)" — FALSE, two kills.** An
intermediate run *declared* a forced choice: `sp.solve` on the fixed-locus equations returned "isolated points" with
distinct κ-values (−6, −158/21 at m=2; −1/4 at m=3; …). Both legs were wrong: **(1)** the "isolated points" are
**degenerate points of the continuous fixed curve**, not 0-dimensional components — the empty κ-elimination ideal shows
κ is *free* (tell: some branches still carried a free symbol, e.g. `κ = z²−2` — an under-resolved curve); **(2)** the
symmetry argument was **circular** — it checked only the 4 κ-preserving *sign* symmetries (a subgroup), then concluded
"no symmetry relates them." This is **method-bug-#2's sibling** — the *revival* failure mode (a too-eager "yes") vs the
*kill* failure mode (B129). *Revival kill condition:* exhibit a **0-dimensional** fixed-locus component (Jacobian rank
3 / empty κ-elimination contradicted) with κ≠2 and no full-group symmetry to another such — none exists (§1).

> **Method note (`REPRODUCIBILITY.md`):** to test discrete-vs-continuous fixed-locus value, use the **κ-elimination
> ideal** (adjoin `k=κ`, eliminate the coordinates; empty ⟹ continuous ⟹ no choice), and confirm 0-dimensionality by
> **Jacobian rank** — **not** `sp.solve` branch-counting (which mislabels curve degeneracies as isolated points).

## Honest scope (verify-don't-trust)

- **Tested:** the **trace-ring / Fricke (κ) invariants** — the structure's *primary* invariants — m = 2..5. No forced
  choice there.
- **NOT proven:** that **no** invariant *whatsoever* (a higher cohomology class, a torsion refinement, a quantum/CS
  invariant) is discretely-multivalued-and-unsymmetric. The rigorous claim is **"no forced choice in the
  trace-ring/character-variety invariants,"** not "no forced choice, period." The theorem-version is the open MATH
  target `speculations/S032`, analogous to the S031 sealing capstone — pen-and-paper, not a computation.
- **m=5 leg is numerical** (259-point continuum); m=2,3,4 symbolic. A symbolic m=5 / uniform-m argument would upgrade
  it.

## Open frontier + co-researcher notes (scoped; NOT claims, tier-tagged)

The result *locates* the question precisely (a single seed is internally fork-free; the only fork is external
seed-selection), which suggests several genuinely new directions — recorded so the next session inherits them:

- **A sharper framing than "internal vs external fork":** the no-forced-choice result says the structure is a **moduli
  space** — continuous `κ` × discrete seed-label — and *a moduli space parametrizes, it does not choose*. This dissolves
  the "is m internal or external?" worry: even viewing "the structure" as the whole metallic family, it *contains* all
  m (a parameter space), it does not *select* one. The deepest statement: **single-seed self-reference produces a moduli
  space, and moduli spaces do not force points.**
- **A unifying synthesis with S031/K012:** a single seed is rigid **vertically** (the SL(n) tower fixes only the
  `Sym^{n−1}` image — no new arithmetic up the ranks, B129/S031) **and internally** (no discrete fork — B130). Candidate
  unifying claim (open): *single-seed self-reference is rigid in every tested direction — determined or continuous,
  never forced-discrete.*
- **The next forced-answer question:** "Is choice an **emergent property of multiplicity** — is the minimal multiplicity
  for an *internal* forced choice exactly **two**, or does fork-freeness close under all finite gluings?" (The precise
  form of the standing "minimal multiplicity to become more" intuition.)
- **Proposed two-seed construction + detector (named before computing):** glue `M_{m₁}, M_{m₂}` **along their cusp tori**
  (the JSJ/amalgam where the 3d-3d `T[M]` composition and the `S029` one-form-polarization choice actually live).
  **Detector:** the **0-dimensional part of the gluing character variety** (the fiber product of the two relative
  character varieties over the shared boundary-torus character), tested by κ-elimination on the combined fixed ideal
  **+ Jacobian rank** (the robust §1 method, avoiding the K-G `solve` trap), then checked against the full
  mapping-class-group action for unsymmetrizability. NB: simple **word concatenation** (B128's `R^{m₁}L^{m₁}R^{m₂}L^{m₂}`)
  is the *wrong* construction — its only discrete invariant is chirality, which the `Z₂` mirror symmetrizes (B128) → no
  internal fork; the **boundary gluing** is where a genuine non-orbit discrete set could appear. *(This is the §6 open
  question — **unrun**, recorded only; tracked in `S032`.)*
- **Connections (questions, not claims):** internal-fork-freeness says the trace ring has **no discrete moduli** — so
  the **B85** functorial-`Sym(W)→trace-ring` obstruction is purely about the continuous/grading structure, not hidden
  discrete components (worth checking); and B130 is the "internal" companion to S031's "vertical" rigidity.

## Reproduce

```
python frontier/B130_no_forced_choice/probe.py
python -m pytest tests/test_b130_no_forced_choice.py -q
```

The symbolic κ-elimination (m=2; m=3,4 verified in-sandbox and recorded — `kappa_elimination(3)` takes ~80s, m=4 ~8s)
and the located-fork facts (L1/L2) run unconditionally; the m=5 numerical continuum is numpy-guarded (skips when
absent; record stands).

**Tier.** MATH (low-dim topology / character-variety invariants) + a firewalled reading (POSTULATED). The naming is
`knowledge/K013`; `P007` gains the **seventh** direction; `P008` gains the *root* of permits-but-never-forces; `K-G`
is tombstoned (`speculations/TOMBSTONES.md`); the forward program is `speculations/S032` (open MATH). Nothing to
`CLAIMS.md`; P1–P16, B85, B124–B129 untouched. Ledger **V119**.

**Anchors:** B129 (S031/K012 — the rigidity sibling; the fork this answers), B128 (the chirality `Z₂` that fails
condition 3; the wrong construction for §6), `K010` (the Fricke–Vogt naming; `κ` is the Fricke–Vogt invariant), `K011`
(the deterministic word). External: Fricke trace coordinates; Markov/character-variety trace maps.
