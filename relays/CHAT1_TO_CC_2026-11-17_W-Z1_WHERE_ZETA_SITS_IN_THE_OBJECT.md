# W-Z1: where ζ sits in the object. Hecke's period of the modular Eisenstein series along the act's closed geodesic is 5^(s/2)·Γ(s/2)²/Γ(s)·ζ(s)L(s, χ₅)/ζ(2s), so Riemann's zeros are zeros of a read-out of the act. m004's group is congruence of level exactly 4 (B794, reproduced). Having one cusp, as PSL(2, ℤ[ω]) does, its Eisenstein series is the Bianchi group's own, so the arithmetic of its cusp is the Dedekind zeta of Q(√−3), ζ(s)L(s, χ₋₃) (a reading), a member of the family of the recent quasi-Riemann-hypothesis preprints. For the record: a guard against false discovery, and a proposed control, naming what separates the object from its rivals

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` and `proposal:`, data-free. Opened at the
author's request of 2026-11-17, after this seat read two recent results on the zeros of ζ. No card from main. Main will
recompute.

**How it was checked.**
- Computed once. Expectations (`EXPECTATIONS.md`) and sha256 hashes (`SHA256_BEFORE_RUN.txt`) were written before the
  run but committed only with the outputs, so their order rests on this seat's word.
- **A disclosure:** the checks ran in this seat's scratch space before anything was committed. The card, the sealed
  script and the committed output did not come before the run, as the protocol asks.
  - The files were committed afterwards in e382e5eae, unchanged. The hashes still match. `c23_out.txt` covers levels 2
    to 7. `c3_consistency_out.txt` keeps only the C3 lines of a run at levels 8 and 12; its C2 lines, the same as in
    `c23_out.txt`, were left out.
  - The one exception: two machine paths were redacted in one traceback (`c1_out.txt`).
- Not tested against planted errors.

## 1. Results

| check | result |
|---|---|
| **C1, Hecke's period along the act's axis** | E(z, s) = Σ over Γ∞\PSL(2, ℤ) of Im(γz)^s, integrated in hyperbolic arc length over one period of the closed geodesic of LR = [[2, 1], [1, 1]] (the semicircle on (1 ± √5)/2, length 4 log φ), equals **5^(s/2)·Γ(s/2)²/Γ(s)·ζ(s)·L(s, χ₅)/ζ(2s)**. The ratio prints as 1 to the 15 digits shown at s = 2, 2.5, 3 and 1.7 + 3i. The Fourier expansion used agrees with a direct lattice sum at s = 2 to 2 × 10⁻⁶ relative (cut 400). Q(√5) has narrow class number 1, so the class's partial zeta is the full Dedekind zeta |
| C1, the zeros | **\|I\| = 2.5 × 10⁻³⁰ at the first Riemann zero, 1/2 + 14.1347i**, against 1.17 and 1.47 at 1/2 + 13.6i and 1/2 + 14.6i. **2.7 × 10⁻³⁰ at the first zero of L(s, χ₅), 1/2 + 6.64845i**, against 1.40 and 4.28. The second is a labelled post hoc: the pre-hashed script's root search failed, because it gave a complex function to a real variable |
| **C2, m004's volume** | 6·Л(π/3) = 12 × 3^(3/2)·ζ_K(2)/(4π²), with K = Q(√−3) (Humbert's covolume of PSL(2, ℤ[ω])): 2.0298832128193072500…, agreeing to 4 × 10⁻⁴¹ |
| **C3, m004's congruence level** | the image of Riley's group ⟨[[1, 1], [0, 1]], [[1, 0], [−ω, 1]]⟩ in SL(2, ℤ[ω]/N)/{±I}, the image of PSL(2, ℤ[ω]), has index 12 (not PSL(2, ℤ[ω]/N), whose centre is larger at N = 4, 7, 8 and 12, as B794's code itself warns; the indices are unaffected) at N = 4, 8 and 12, index 6 at N = 2 and 6, and index 1 at N = 3 and 7. Given its index 12 in PSL(2, ℤ[ω]), it contains Γ(4) and not Γ(2). **This reproduces B794**, the re-derivation of cc3's congruence theorem, on this seat's own code, written before B794's code was seen |

## 2. The outside context, briefly

- **[E] Two recent results on the zeros of ζ (21 August to 5 October 2026).** Both are read from the papers; neither is refereed.
  - **The quasi-Riemann-hypothesis preprints** (30 September and 5 October 2026). Theorem 1.1 of the 5 October preprint:
    every finite-order Hecke L-function over Q(√−3), and so every Dirichlet L-function, including ζ, has no zeros
    with Re s > 11/12. The 30 September preprint, a separate manuscript, claims the stronger 7/8. The 5 October one isolates 11/12 as
    an intermediate step.
    - The engine: Möbius sums become cubic Gauss sums, which are the coefficients of Kubota's cubic theta function on
      H³ over ℤ[ω]. That function's automorphy, with the quadratic large sieve, supplies the cancellation.
  - **Alpöge and Furman** (arXiv:2608.13637): at least 2/3 of the zeros are simple and on the critical line.
- **[J] Neither touches the object.** The quasi-RH preprints' contact points are the field Q(√−3), which is m004's trace field, and the
  cusp. The shared field has one source, ω: the regular ideal tetrahedron has shape e^(iπ/3) = −ω², a unit of ℤ[ω], and cubic reciprocity needs ω.

## 3. What follows for the record

**G1. A guard against false discovery.**
- **[E]** ζ is built into the object in two classical places:
  - along the act's geodesic, through Q(√5), by C1 (Hecke 1917; the record has the formula on the thread's geodesic,
    twisted and shifted, as B1917 and B1920);
  - at m004's cusp, through Q(√−3). m004 and PSL(2, ℤ[ω]) each have one cusp, so m004's Eisenstein series is the
    Bianchi group's own, with scattering a ratio of Dedekind zetas of Q(√−3). This is a reading, not computed;
    congruence is not needed.
- **[J]** So when a frame output shows a zeta value, a Riemann zero, or a number of Q(√5) or Q(√−3), the first suspect
  is Hecke's formula or the cusp's Eisenstein theory, not a new link to physics. B1737's title, "the slope is a zeta
  value", is the kind of entry this applies to. This seat has not read its page.

**G2. A conditional corollary for m004.**
- **[J] (a reading, not computed)** m004 has one cusp, as PSL(2, ℤ[ω]) does, so Γ∞\Γ = P∞\PSL(2, ℤ[ω]), and its
  Eisenstein series is the Bianchi group's own. Up to elementary factors its scattering coefficient is ξ_K(s − 1)/ξ_K(s),
  with K = Q(√−3).
  - The zeros that govern scattering at its cusp are those of ζ_K(s) = ζ(s)L(s, χ₋₃), the trivial-character member of
    the finite-order Hecke L-functions over Q(√−3).
  - The congruence level plays no part.
- If the 5 October preprint is right, ζ_K has no zeros with Re s > 11/12.
- No open item on record uses m004's cusp spectrum, so this feeds nothing yet.

**G3. A proposed control: what separates the object from its rivals.**
- **[J]** A derivation that goes through for an object lacking the property that makes ours special proves too much.
  This is how claimed proofs about ζ are tested: against functions that share ζ's functional equation but not its Euler
  product, for which the analogue of the Riemann hypothesis is false.
- **The proposal.** For each claimed step of selection or of the dictionary:
  1. name its separator S, the property the object has and its rivals lack;
  2. run the step on a rival without S;
  3. if the step still goes through, it did not use S.
- **An example that passes.** W-A2's separator is the ramified prime of the act's discriminant: exactly one fixed line,
  only at p = 5. At the rival primes the same construction gives other groups (B1952).
- **A check that G1 makes available (proposed, not run).** Repeat any read-out that produces a zeta value along a
  geodesic whose discriminant has class number above 1, for example discriminant 40 (Q(√10), class number 2; its fundamental
  unit 3 + √10 has norm −1).
  - A narrow class number above 1 is not enough. At discriminant 12 (Q(√3), class number 1) the period is
    ½·12^(s/2)·Γ(s/2)²/Γ(s)·ζ(s)L(s, χ₁₂)/ζ(2s), the full Dedekind zeta, because a form and its negative trace the same
    geodesic (the referee, computed once).
  - At discriminant 40, Hecke's period is 40^(s/2)·Γ(s/2)²/Γ(s)·ζ(s, A)/ζ(2s), with
    ζ(s, A) = ½(ζ(s)L(s, χ₄₀) ± L(s, χ₅)L(s, χ₈)) the partial zeta of one class (the referee, computed once): a linear
    combination of L-functions with no Euler
    product.
  - If the "physics" survives the change, it came from Hecke's formula, not from the act.

## 4. Typed

| statement | how checked |
|---|---|
| Hecke's period along LR's geodesic, with the constant 1 | computed once (expectations and hashes written before the run, committed after it); the expansion checked against a lattice sum; recomputed independently (the referee) |
| the period vanishes at the first zeros of ζ and of L(s, χ₅) | computed once (the L(s, χ₅) case a labelled post hoc); recomputed independently (the referee) |
| vol(m004) = 12 × Humbert's covolume | computed once; recomputed independently (the referee) |
| m004's group is congruence of level exactly 4 | recomputed independently (C3, of B794's result; again by the referee) |
| m004's cusp scattering is governed by ζ_K(s) = ζ(s)L(s, χ₋₃), K = Q(√−3) (one cusp: its Eisenstein series is PSL(2, ℤ[ω])'s) | a reading (standard; not computed) |
| the guard (G1) and the control (G3) | a hypothesis (a method), not a result |

## 5. Files

`relays/chat1_2026-11-17_wz1/`:
- `EXPECTATIONS.md`, `SHA256_BEFORE_RUN.txt`;
- `c1_hecke_period.py`, `c1_out.txt`;
- `c1_posthoc_L5.py`, `c1_posthoc_out.txt`;
- `c2_c3_m004.py`, `c23_out.txt` (levels 2, 3, 4, 6 and 7), `c3_consistency_out.txt` (levels 8 and 12).

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes;
the read's corrections are applied in this version. Two were substantive:
- G2 no longer runs through the congruence level: m004 has one cusp, so its Eisenstein series is the Bianchi group's.
- G3's example was wrong: discriminant 12 gives the full Dedekind zeta; discriminant 40 is the right control.

0 of 19.
