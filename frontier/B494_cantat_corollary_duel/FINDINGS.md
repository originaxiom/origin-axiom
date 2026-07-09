# B494 — CL-1b duel verdict: **COROLLARY** — the held-breath field law falls to Cantat's fixed-locus pipeline

**Pre-registered duel (docs/CLOSURE_CAMPAIGN_2026-07.md CL-1b; committed enum COROLLARY /
NOT-BY-THAT-ROUTE / PARTIAL). Protocol: adversarial derive-or-obstruct, every step recomputed from
scratch and machine-checked (`probe.py`, 54 exact checks, control-gated — the run aborts INVALID if the
control fails). The mandatory control passed; the derivation went through; the completeness direction
did NOT resist (it now has an unconditional elementary proof, all m); and the check on the banked
m = 7 row found the SAME norm-vs-field conflation as the corrected d = 5 row — the erratum extends.
Nothing to CLAIMS.md; firewall untouched.**

## Control (invalid without it) — Cantat's ℚ(√17), reproduced exactly
Pipeline built from scratch for the pseudo-Anosov Ψ = [[2,1],[1,1]]: automorphism representatives
ψ_n: A↦ABA, B↦BA (abelianization exactly [[2,1],[1,1]]) and ψ_c: A↦BA, B↦BAB ([[1,1],[1,2]],
SL(2,ℤ)-conjugate via P = [[−2,−3],[−1,−2]]); trace actions verified against honest symbolic SL₂
products; both preserve κ = x²+y²+z²−xyz−2. Result: Fix(ψ_c) is exactly the rational curve
**(x, x/(x−1), x)** (Gröbner: {z−x, xy−x−y}, nothing else); κ restricted to it is
**(x⁴−3x³+x²+4x−2)/(x−1)²**, so the four nontrivial fixed characters sit at κ = 0 (order-4 commutator)
and solve the quartic verbatim — irreducible over ℚ, **splitting into two quadratics over ℚ(√17)**
(Galois D₄, pari). Anchors: the control map equals T₁² — Cantat's Ψ *is* the m = 1 metallic
(figure-eight) monodromy σ₁²; the same pipeline at κ = −2 instead of κ = 0 returns x²−3x+3, disc −3 =
the figure-eight trace field ℚ(√−3); and Fix(σ₁) ∩ cusp is trivial, B479's breathless m = 1 row.

## The derivation (steps 1–3): the corrected law is an easy corollary
1. **B479's mechanism re-proven.** T_m(x,y,z) = (t_m, x, t_{m+1}) with t₀ = y, t₁ = z,
   t_{k+1} = x·t_k − t_{k−1} (verified on SL₂ words). Any SL₂ element of trace τ_d (d ≥ 3) is
   diagonalizable of order d — M(τ_d)^d = I identically mod Ψ_d — so aᵐ = I on the locus, and
   **T_m = the swap (x,y,z)↦(y,x,z) on {x = τ_d} exactly when d | m** (16 positive pairs, 6 negative
   controls, exact remainder arithmetic mod Ψ_d).
2. **Swap-fixed + cusp = the field law.** Fixed points force x = y (the second coordinate of T_m is
   literally x). On κ = −2 with x = y = t: **z² − t²z + 2t² = 0**, discriminant **t²(t²−8)**; at
   t = τ_d this is the corrected law **z ∈ ℚ(τ_d, √(τ_d²(τ_d²−8)))**. τ₄ = 0 collapses it to z² = 0
   (the d ≠ 4 condition = the trivial point). Sharpening: Δ_d is **totally negative** for every
   d ≥ 3, d ≠ 4 (τ² < 4 < 8 in every real embedding), so the extension is degree 2 over ℚ(τ_d)
   *exactly* — it never collapses.
3. **The banked table, re-derived per divisor** (z-eliminant E_d = Res_τ(Ψ_d, z²−τ²z+2τ²)):
   d=3: z²−z+2, ℚ(√−7). d=5: **exactly** z⁴−3z³+7z²−4z+4, irreducible, splits over ℚ(√5) into two
   quadratics, stays irreducible over ℚ(√41); poly disc 2⁴·5²·41, field disc 5²·41 (pari), Galois D₄
   with unique quadratic subfield ℚ(√5); Norm_{ℚ(√5)/ℚ}(Δ₅) = 41 and 41·Δ₅ totally negative ⟹
   √41 ∉ field — the 2026-07-09 erratum re-proven independently. d=6: same quadratic as d=3 (τ²=1;
   in full coordinates the order-3 and order-6 lines are distinct characters with the same
   z-eliminant). d=8: τ₈² = 2 rational, E₈ = (z²−2z+4)², disc −12 ⟹ **ℚ(√−3) — the banked m = 8, 16
   row explained**. d=12: (z²−3z+6)², ℚ(√−15). d=11, 13: irreducible of degree 10, 12 = φ(d) — the
   banked growing-degree rows explained.

## The m = 7 row: REFUTED as a field label, explained as a norm — **the erratum extends**
- E₇ = z⁶−5z⁵+16z⁴−25z³+30z²−12z+8, **irreducible over ℚ of degree 6 = φ(7)**; the brute Gröbner
  z-eliminants at m = 7 and m = 14 equal it verbatim, so this IS the banked row's object.
- **Norm_{ℚ(τ₇)/ℚ}(τ₇²(τ₇²−8)) = −239 exactly.** Poly disc(E₇) = −2¹²·7⁴·239, squarefree part −239 —
  the verbatim output of B479's degree-2-only "disc → ℚ(√sf)" labelling heuristic
  (`held_breath_tower.py`) applied outside its validity range; field disc −7⁴·239 (pari).
- ℚ(√−239) is not the field and **not even a subfield**: E₇ stays irreducible over ℚ(√−239), and the
  subfield degrees of the true field are [1, 3, 6] (pari) — no quadratic subfield exists. The Galois
  closure is C₂≀C₃ (order 24); √−239 = √(Norm Δ₇) lives in the closure, not in the field.
- **Correction (extends the 2026-07-09 B479/B491 erratum, same mechanism as d = 5):** everywhere the
  banked table says the m = 7, 14 held-breath field is ℚ(√−239), read: a **degree-6 field
  ℚ(τ₇, √(τ₇²(τ₇²−8))) containing the cyclic cubic ℚ(τ₇)**; −239 is the norm of the discriminant, not
  a field generator. Hygiene: the B479 erratum banner currently covers only d = 5 and should be
  extended to the m = 7, 14 row when that node is next touched (flagged here, not edited — single-node
  discipline).

## Completeness (the pre-named hard direction): did NOT resist — PROVEN for all m
**Lemma (fixed locus of T_m, every m ≥ 1).** Fix(T_m) = {(0,0,0)} ∪ {(2,2,2)} ∪ {(−2,−2,2) iff 2|m}
∪ ⋃_{d|m, d≥3} {(τ_{d,k}, τ_{d,k}, z) : z ∈ ℂ}. *Proof.* Fixedness forces y = x and
(t_m, t_{m+1}) = (t₀, t₁), i.e. (Mᵐ−I)(z,x)ᵀ = 0 for the transfer matrix M = [[x,−1],[1,0]]
(t_k = z·F_k − x·F_{k−1}, Chebyshev; Mᵐ = [[F_{m+1},−F_m],[F_m,−F_{m−1}]]). det(Mᵐ−I) = 2 − tr Mᵐ =
−λ^{−m}(λᵐ−1)² with λ+λ⁻¹ = x, zero iff λᵐ = 1. Either (z,x) = 0 (the trivial point), or λ is a
primitive d-th root, d|m: d ≥ 3 makes M diagonalizable of order d, Mᵐ = I, the whole line fixed;
λ = 1 (x=2) gives kernel span(1,1), the single point (2,2,2); λ = −1 (x=−2) gives (−2,−2,2) for even
m and nothing for odd m. ∎ Intersecting with κ = −2: the isolated points sit at κ = 2 (off), the
d-lines give the cusp quadratic, d = 4 collapses to the trivial point — **B479's "held breath =
torsion" theorem, previously Gröbner-verified m ≤ 16, is now unconditional for all m.** Every
ingredient is a one-line induction; machine-checked to m = 24 as belt-and-braces (identities I1–I4,
the eigenvalue-locus factorization 2 − tr Mᵐ = −(x−2)(x+2)^[2|m]·∏_{d|m,d≥3}Ψ_d², line and boundary
checks), plus full Gröbner agreement at m = 1..16 (the entire banked table) and **out-of-sample
m = 17..20**. The prereg's contemplated obstruction ("the fixed curve degenerates at the elliptic
points; the method sees only the ℚ(τ_d)-rational part") does not occur: the fixed locus is a union of
τ_d-lines plus isolated points, all of it visible to the pipeline.

## Verdict: **COROLLARY** (per the committed enum) — residue named honestly
Cantat's fixed-locus pipeline (trace action → fixed locus → restrict κ → minimal polynomial → field)
transfers verbatim to the finite-order-at-torsion σ_m at κ = −2 and yields the full corrected law —
divisor indexing, d ≠ 4 condition, closed-form field — with ONE supplement not in Cantat: the
elementary Chebyshev transfer-matrix classification of Fix(T_m) above, at or below the difficulty of
the control computation itself. No mathematically hard residue survives. Consequences: **R1's novelty
(B491) closes to a remark** — what remains is the observation (the divisor-indexed torsion fixed
locus, its closed-form field, and the norm-vs-field distinction), now carried by a complete
elementary proof rather than a Gröbner sweep; the P3 paper rescopes to the divisor-indexing
observation with Cantat cited for the method. Two banked corrections ride along: the m = 7, 14 field
label (above) and the all-m completeness upgrade. **Nothing to CLAIMS.md; firewall untouched.**

Reproducers: `probe.py` (control + steps 1–5, 54 exact checks, exits INVALID on control failure;
sympy exact, cypari ground truth where present). Locks: `tests/test_b494_cantat_corollary_duel.py`.
