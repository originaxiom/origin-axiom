# B442 — C4: the E₆ lift of the child's vacua — composite data is −283-forced (Bin 3)

**Status: banked (C4, composite level rigorous; intrinsic-E₆ residue NAMED as the specialist
boundary, per the plan). Firewalled.**

## The lift

The child's E₆ content comes from the composites **principal-sl2 ∘ ρ** over the C3 vacua. The
E₆ adjoint **78 = ⊕ᵢ Sym^{2mᵢ}**, mᵢ = the E₆ exponents **{1,4,5,7,8,11}**. So the composite E₆
adjoint torsion factors as **∏ᵢ τ(Sym^{2mᵢ}∘ρ)** — a *function of the SL(2) vacuum ρ*.

## Result — the composite E₆ data is −283-forced (verified at the character level)

The C3 vacua (B439/B440, corrected) are the roots of the child quartic `x⁴−3x³+x²+3x−1`
(disc −283), **commensurability-shared** with 5₂'s quartic `x⁴−4x³+4x²+x−1` (same −283 field).
The E₆ adjoint meridian character `χ_adj(x) = Σᵢ S_{2mᵢ}(x)` (degree 22) reduces at each vacuum
to an element of the −283 field:

- child vacua: **−1116x³ + 1844x² + 1767x − 741**
- 5₂ vacua: **−23777x³ + 25467x² + 5928x − 6016** — a *different* element of the *same* field.

The Galois-invariant sum over the 4 child vacua is **rational (5201)**, as it must be.

**Structural:** the full E₆ adjoint Reidemeister torsion of the closed child at each vacuum is a
function of the (−283-field) rep data (Sym^{2mᵢ} twisted by ρ on the 2-generator group), hence
algebraic over the −283 field and commensurability-shared with 5₂. **Bin 3, inheriting C3** — the
E₆ lift adds no figure-eight-specific structure; it is determined by the (shared) vacua.

## The named boundary (honest, per the plan)

The **intrinsically-E₆ vacua** — Hom(π₁(child), E₆)/conj *beyond* the principal composites (the
26 abelian + any non-composite irreducibles) — are the child's **L50-analog**. Their exact E₆
Reidemeister torsions are the specialist residue: **NAMED here, not computed** in-sandbox (the
closed-manifold E₆ torsion engine is the standing specialist gate). The composite floor is
in-sandbox and forced; the intrinsic floor is the honest boundary.

**Bar note:** forced ✓, unsought ✓, control ✓ (5₂). A NEGATIVE (Bin 3) — the E₆ composite data
is commensurability-shared, no bar cleared. Character-level rigorous; the full closed-manifold
torsion is structural (a function of the −283 vacua) + the named intrinsic boundary.

**Review note (2026-07-05).** Independently confirmed: the 78-decomposition (dims [3,9,11,15,17,23],
sum 78), the degree-22 character, both reductions, the same −283 field (5₂'s quartic has a linear
factor over ℚ(child-root)), and the Galois sums (child 5201, 5₂ −105717). The `galois_invariant_sum`
was **hardened** from a fragile `nsimplify(re(N(...)))` to the exact companion-matrix trace of χ
(same value, airtight method).

**Provenance.** e6_lift.py → e6_lift.json; lock tests/test_b442_child_e6_lift.py (3/3). Reuses the
E₆ exponents + Sym machinery (B425/B428/B306). Cross-refs: B439/B440 (the vacua), B435 (26 abelian
vacua), the Inversion Law (B437/B438), C5 (B441, WRT also forced).
