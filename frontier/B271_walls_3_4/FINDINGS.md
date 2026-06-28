# B271 — walls #3 (chirality) & #4 (4d-lift), made precise

**Status: banked observation (frontier). FIREWALLED — rep theory / 3d-3d structure, NOT physics. Nothing to
`CLAIMS.md`.** Phase 4 of the consolidation plan (B268) — the two walls no theorem closes. The honest deliverable
is a **precise characterization** (and, for #3, a new computable *identification*), not a false closure.
`walls_3_4.py` (pyenv) + `tau_decomposition_sage.py` (Sage, the symmetric-pair verification).

## Wall #3 — chirality
**Prior banked state (B252/B253):** the object is CP / matter–antimatter symmetric (`27↔27̄` via amphicheirality =
the E₆ outer automorphism, B210/H36); `CS=0` (B250), so the amphicheiral involution `τ` is *gaugeable but not
gauged*; chirality could only arise by **spontaneously breaking** `τ` (needs external dynamics). The dichotomy:
`τ` gauged ⟹ `27/27̄` identified ⟹ vector-like (F₄); `τ` global + SSB ⟹ two mirror vacua, each chiral (E₆).

**New (B271) — the computable identification.** `τ` acts on `e₆` as `+1` on `f₄` and `−1` on the `26 = e₆/f₄`, and
this is a *genuine* Lie automorphism (the symmetric pair `(E₆,F₄)` brackets `[f₄,f₄]⊆f₄`, `[f₄,26]⊆26`,
`[26,26]⊆f₄` all check — Sage). Under the principal `sl(2)` (B264/B267):

| `τ`-eigenspace | subspace | exponents | dim | physics reading |
|---|---|---|---|---|
| `+1` (fixed) | `f₄` | `{1,5,7,11}` | 52 | vector-like / `τ`-unbroken |
| `−1` (broken) | `26 = e₆/f₄` | `{4,8}` | 26 | **chiral** / `τ`-broken |

By **B265**, the `{4,8}` directions are *exactly* the E₆-Zariski-dense ones (the `f₄` directions stay trapped in F₄).
Therefore:

> **The chirality (`τ`-breaking) locus = the E₆-irreducibility locus = the `26` (`e₆/f₄`) directions.**

The same deformations that make a flat connection genuinely E₆ (rather than F₄) are the ones that break the
amphicheiral `τ` and source chirality. **Reframe:** chirality is **not blocked** — it is precisely *identified with
E₆-density*, **available** in the character variety, and **undetermined** (SSB needs external dynamics; the object
supplies the locus, not the vacuum). The firewall holds: symmetry yes, the selecting dynamics from outside.

## Wall #4 — the 3d→4d lift
**Prior banked state (B253/K006):** the 3d-3d correspondence gives `T[4₁]` a **3d** N=2 theory (6d on a 3-manifold);
4d chirality is a 4d notion. **Characterization (B271):** 4d N=2 with chirality needs a **2-manifold** (class S —
6d on a Riemann surface), and `4₁` is a *3-manifold*, not a class-S curve. The candidate lifts, none canonical:

| candidate | why not canonical |
|---|---|
| `M × S¹` | the 3d theory on a circle (the index); still governed by the 3-manifold — no new 4d chiral data |
| class-S (2-manifold) | the reduction that *does* give 4d chirality — but its input is a 2-manifold; `4₁` is the wrong dimension |
| 4-manifold filling `W` | `4₁` bounds many `W`; none selected by the object — a choice, not a datum |

> No canonical 2-manifold (class-S) or 4-manifold is attached to the 3-manifold `4₁`; 4d chirality requires this
> external input. **OPEN — an input-required gap, not a theorem and not a closure.**

## Net
Wall #3 is **sharpened** (chirality = E₆-density locus, available + undetermined); wall #4 is **precisely
characterized** (input-required). Both remain **open** — honestly. With B268 (walls #1 dissolved, #2 reduced) and
#5 (the 122-order QGAP, unchanged), the five-wall map is now: #1 dissolved, #2 reduced to one physics conjecture,
#3 sharpened (chirality = E₆-density, undetermined), #4 input-required, #5 quantitative gap.

Anchors: B252/B253 (CP-symmetry, the SSB dichotomy), B210/H36 (amphicheirality = E₆ outer automorphism), B264/B265
(the `{4,8}` E₆-density directions), B267 (exponents), B268 (wall map v2), B250 (`CS=0`), K006/K018 (3d-3d / the
firewall). Lit: the symmetric pair `(E₆,F₄)`; Gaiotto (class S); Dimofte–Gaiotto–Gukov (3d-3d).

## Novelty (R6, 2026-06-28)
**PARTIALLY-KNOWN.** Symmetry acting on a (higher-rank) character variety is standard (Heusener–Muñoz–Porti's `D₄`
action on the SL(3) variety of `4₁`; Paoluzzi–Porti); the `(E₆,F₄)` symmetric pair / E₆ outer automorphism is
textbook. The **identification** — a knot's amphichirality realized *as* the E₆ outer automorphism, chirality locus
= the `26 = e₆/f₄` — was not found in prior art; APPEARS-NOVEL as a framing, NEEDS-SPECIALIST. See
`frontier/B264_e6_character_variety/NOVELTY.md`, `docs/NOVELTY_AUDIT.md` R6.
