# B356 — the σ-stability quick pair: the det-lemma, and the chirality window is exactly the Eisenstein ω (H104 RUN)

**Status: banked (frontier). Campaign W1.2 (the value-boundary queue). Runs H104 and the two pinned notes B327
left; sharpens H103 into a precise finite target. Firewalled; nothing to `CLAIMS.md`; no physics claim.**

## What was computed (self-verifying; no transcribed tables)

All six groups `{A₄, S₄, 2T, 2O, A₅, 2I}` built **concretely** (unit quaternions for the binaries — 2T = 24
Hurwitz units, 2O = 48, 2I = 120 icosians; permutations for A₄/S₄/A₅); conjugacy classes and power maps computed
from the group; character tables **derived** by decomposing tensor powers of a faithful seed (the SU(2) trace
`2a` for binaries; permutation characters + the concretely-computed abelianization 1-dims; for A₅ the icosahedral
`χ₃` seed, whose `φ ↔ 1−φ` assignment ambiguity is the Galois table-automorphism — verdict-invariant), then
**snapped to exact algebraic values and gated exactly**: row orthonormality over `ℚ(√5,√2,√3,i)`, `Σdim² = |G|`,
Frobenius–Schur indicators in `{1,−1,0}`. A failed gate raises (it caught two real bugs during development —
an incomplete derivation and a bad snap — MB12 working as intended).

## Results

**1. The det-lemma (exact, all binaries).** For every 2-dim irreducible: the det-character
`δ(c) = (χ(c)² − χ(c²))/2` is trivial **iff** the irrep is quaternionic (FS = −1):

| group | 2-dim irreps | FS | SL(2)-admissible |
|---|---|---|---|
| 2T | `2` | −1 | **yes** |
| 2T | `2′, 2″` (ω-twisted) | 0 | **no** |
| 2O | `2, 2̃` | −1, −1 | **yes, yes** |
| 2O | the FS=+1 2-dim (factors through S₃) | +1 | **no** |
| 2I | both 2-dims | −1, −1 | **yes, yes** |
| S₄ | the 2-dim | +1 | **no** |

So **every `SL(2,ℂ)`-factoring route (holonomy, quaternion units) forces a quaternionic, self-dual 2** — the
"complex 2′/2″ escape" from B327 is closed at the determinant level, before any branching computation.

**2. Mod-3 blindness (exact).** `2T`'s three 2-dims differ by the ω-characters, and `ω^k − 1` is divisible by
`(1−ω)` in `ℤ[ω]` — so their Brauer characters at the prime over 3 coincide: **the mod-`√−3` arithmetic route is
structurally blind to the `2` vs `2′/2″` fork.** (Together with 1., the "arithmetically-forced route" question
B327 left is pinned: SL(2)-routes can't be twisted, and mod-3 data can't see the twist.)

**3. The factor-route identities (statements, one line each).** For *every* finite `G`: an SU(2)-factoring
embedding restricts the 27 to a sum of self-dual SU(2)-irreps (self-dual); a single-SU(3)-factor trinification
route gives `27|G = 3ρ ⊕ 9·1 ⊕ 3ρ̄` (balanced); the diagonal trinification gives `27|G = 3·(ρ⊗ρ̄)`
(self-conjugate). **Every factor route is σ-stable, for every finite group** — B329's two computations are
instances of these identities.

**4. The H104 chirality scan (the headline).** Enumerating **all** faithful 27-dim assemblies with an invariant
cubic (`(Sym³V)^G ≠ 0` — character-level necessary conditions for a chiral `G ↪ E₆`):

| group | assemblies | complex (chiral candidates) |
|---|---|---|
| **A₄** | 1089 | **1028** |
| S₄ | — | **0** (all characters real — theorem) |
| **2T** | 71192 | **70262** |
| 2O | — | **0** (theorem) |
| A₅ | — | **0** (theorem) |
| 2I | — | **0** (theorem) |

**The chirality window is exactly the Eisenstein ω:** complex candidates exist *only* for the two groups with a
nontrivial `ℤ/3` abelianization — the ω-characters. `S₄, 2O, A₅, 2I` are closed by the reality theorem (every
character real ⇒ every assembly self-dual). The scan counts *character-level candidates* (necessary conditions
only): whether **any** of the ω-window assemblies is realized by a genuine `E₆`-conjugacy class of embeddings
with a *nondegenerate* invariant cubic is precisely **H103** (wave 2) — now a sharply-scoped finite question.

## Honest tiers and scope

- Exact: the tables (gated), the det-lemma, mod-3 blindness, the factor-route identities, the reality theorem.
- The enumeration itself runs in floats off the exact table with integer gates at `1e-6` (values ≤ 27³ —
  comfortably exact-as-floats); counts are reproducible by `run_group()`.
- **Not claimed:** that any complex assembly embeds in `E₆` (that is H103's question — Sym³-invariance is
  necessary, not sufficient; nondegeneracy and actual conjugacy are not tested here); no physics.

**Provenance.** Campaign W1.2 (`docs/OPEN_LEADS.md`); B327 (the self-duality reduction), B329 (canonical routes
closed — this probe's identities generalize it), H103/H104 (`docs/HINT_LEDGER.md:183-184`, S046 paths 1–2).
Reproducer: `sigma_stability.py`; test: `tests/test_b356_sigma_stability_scan.py`.
