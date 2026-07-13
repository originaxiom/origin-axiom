# B569 — the "Complete Chain" handoff, adjudicated (the sixteenth chain)

**Date:** 2026-07-14. **Source:** an incoming cross-seat handoff claiming the full
σ → SM chain in seven links, with the compactness gap (B565-H1) resolved by E₆
Chern–Simons quantization at level 1 (Link 4) and a uniqueness theorem — G_SM the
only chiral theory on F₄ (Link 7). Five verification tasks were requested.
**Verdict: the two load-bearing new links fail.** Link 4's modular data is
inconsistent (its headline Z = −1 is a word artifact; the consistent value is +1,
and even corrected, the computation lives on the measurement face, not the algebra
face). Link 7 is refuted by a one-line Lie-theory fact that simultaneously
re-derives the banked chirality wall. Locks: `tests/test_b569_complete_chain.py`
(6). Reproducer: `e6_level1_modular.py`.

---

## The seven links

| # | Claim | Verdict |
|---|-------|---------|
| 1 | σ → M₄ → monodromy A₁ = F² | **STANDS** (banked long ago) |
| 2 | the charge tower ℤ/11 | **STANDS** (B552/B556/B566-S5) |
| 3 | E₆ from the cusp | **STANDS** (B347/B353; structural, firewalled) |
| 4 | compactness from E₆ CS quantization at level 1 | **CORRECTED + RE-PLACED** (below) |
| 5 | TDV: F₄ ⊃ G_SM = H₁∩H₂ | **STANDS** (literature; verified in-sandbox, B565 Krasnov) |
| 6 | triality → three generations (Boyle) | **STANDS as structural match** (B565-T, firewalled) |
| 7 | G_SM the unique chiral theory on F₄ | **REFUTED** (below) |

## Link 4: three findings

**(a) The handoff's modular data is inconsistent — its Z = −1 is a word artifact.**
The data used was S = ω^{ab}/√3, T = diag(−i, e^{iπ/6}, e^{iπ/6}), i.e. conformal
weight h(27) = 1/3 with central charge c = 6. But h = 1/3 is the **SU(3)₁** weight
(c = 2); the true E₆ level-1 weight is **h(27) = 2/3**, proved here from the E₆ root
system (Weyl dim formula at both minuscule nodes: dim 27, (ω,ω) = 4/3,
h = (Λ,Λ+2ρ)/(2·13) = 2/3 exactly). The hybrid (h = 1/3, c = 6) violates
(ST)³ = S², so "ρ(A₁)" depends on the SL(2,ℤ) word chosen for A₁:

- A₁ = T²ST (the handoff's word)  →  Z = −1
- A₁ = T·(ST⁻¹S⁻¹) (the same group element)  →  Z = +1

Gauss–Milgram seals it: Σθₐ/√3 = +i forces c ≡ 2 (mod 8) for h = 1/3, and −i forces
c ≡ 6 (mod 8) for h = 2/3. The handoff's pairing satisfies neither theory.

**(b) The consistent computation.** With genuine E₆,₁ data (S = ω^{−ab}/√3,
h = 2/3, c = 6), the rep is word-independent and:

> ρ(A₁) is unitary, order 4 (matching ord(A₁) = 4 in SL(2, ℤ/3)), commutes with
> θ = (27 ↔ 27̄) exactly (and does **not** invert — the handoff's own caveat was
> honest), θ-even eigenvalues {+i, −i}, **θ-odd eigenvalue +1**, and
> **Z = Tr ρ(A₁) = +1**.

The conjugate theory SU(3)₁ gives the same Z = +1 (the trace is real). **There is
no −1 in any consistent theory: the claimed "chirality bit" does not exist.** The
handoff's cost accounting ("the whole chain costs 1 bit") priced exactly this bit;
the corrected ledger has nothing to buy.

**(c) Placement — what the corrected fact is and is not.**
- Tr ρ(A₁) is the level-1 invariant of the **closed torus bundle** with monodromy
  A₁ (a Sol manifold — the fiber Dehn-filling of the knot complement), not of M₃
  itself. The knot complement (a *punctured*-torus bundle) needs the
  punctured-torus conformal blocks, which this 3×3 computation does not contain.
- The θ-even ℂ² carries **no F₄ action** — the smallest faithful F₄ rep is 26.
  Labeling the 2-dim block "the compact F₄ sector" is a category error.
- Unitarity of ρ(A₁) is an instance of the **two-faces theorem** (PR #884): the
  measurement face is always unitary/compact. It does not touch the algebra-face
  wall (B565-H1: the geometric holonomy's adjoint traces are non-real; no real
  form of F₄(ℂ)/E₆(ℂ) contains it). **The compactness gap stands.**

What survives as a small positive: A₁ = T²ST = T·ST⁻¹S⁻¹ in SL(2,ℤ) is a clean
word identity, and Z_{E₆,₁} = +1 with the exact θ-split {±i | +1} is a genuine,
canonical quantum invariant of the object's Sol sibling. Banked as such.

## Link 7: refuted, and the refutation is a theorem we keep

The claimed branching 27 → 16 ⊕ 10 ⊕ 1 with a complex chiral 16 is the
**Spin(10)×U(1) ⊂ E₆** branching. Spin(10) is not a subgroup of F₄. Inside F₄ the
27 restricts as 1 ⊕ 26, and:

> **The 26 of F₄ is self-dual.** Its 24 nonzero weights are exactly the short
> roots of F₄ (verified: 48 roots, 24 short, negation-closed; the unique dominant
> short root has Weyl dimension exactly 26; the remaining 2 dims are zero weights
> since any nonzero F₄ weight has W-orbit ≥ |W|/|W(B₃)| = 24 > 2). The character
> is real; 26 ≅ 26*.

A self-dual rep restricts to a self-dual rep of **every** subgroup. So 27|_{F₄} =
1 ⊕ 26 is self-conjugate under SO(9), Sp(6)×SU(2), SU(3)² — *and equally under
G_SM = H₁∩H₂*. The handoff proved the three maximal-rank cases self-conjugate and
inserted the E₆ branching for the fourth. Corrected: **zero chiral theories on the
F₄ stage, not one.** There is no uniqueness theorem because there is no existence.

This is the banked chirality wall (B565-T3: chiral index ≡ 0, the fourth wall)
re-derived from pure Lie theory, independent of the object: *the stage itself
refuses chirality.* It also re-confirms B568-SQ from a new direction — the one
ingredient the minimal play cannot buy is the one this chain priced at "1 bit."

## The five requested tasks

1. **CS computation** — done exactly; data corrected (above). Z = +1, not −1.
2. **θ commutes, not inverts** — confirmed exactly ([θ,ρ] = 0; ‖θρθ − ρ⁻¹‖ ≈ 2.83).
   The handoff flagged this honestly.
3. **Uniqueness theorem** — refuted (above).
4. **Boyle/B299 triality → three 16s** — previously banked as a structural match
   (B565-T); the three 16s live in E₆(ℂ)/complexified h₃(𝕆), outside the F₄
   stage. Unaffected by this adjudication, and not a chirality mechanism *on F₄*.
5. **H¹(E₆ character variety) = 6** — previously banked (B347/B565). Stands.

## Methodology note

The sixteenth chain dies by the two standing rules: (i) **verify the modular data
before the modular computation** — an inconsistent (S,T) makes every downstream
number word-dependent noise; the discriminating fact was two spellings of the same
group element giving Z = −1 and Z = +1; (ii) **check which group the branching
belongs to** — the chain's chirality was imported from an E₆ embedding that does
not factor through its own stage. Both kills are in-sandbox, exact, and locked.

Firewalled. Nothing to CLAIMS.md.
