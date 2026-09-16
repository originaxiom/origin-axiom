# B1372 — THE DOUBLET HALVES (door 2): the third reading of a generation — the 10 from the 78's SL(2)_β-doublets and the 5̄ from the 27's, both halves carried by the non-abelian part of the connection rather than by a character — is closed by charge arithmetic at the cusp: with a non-unitary peripheral eigenvalue the two halves are never cusp-fixed together (γ(10 ⊂ 78) = 1 against γ(5̄ ⊂ 27) = ⅓), with a unitary one only at fourth roots of unity and then always on opposite eigenvectors, so wherever the abelian Higgs field vanishes their chiralities are opposite; parabolic and central cusp holonomy make every doublet sector vector-like outright; on m004 the order-4 points are the four SU(2) dihedral representations, unitary — door 2 is closed on m004 and on the 77 members without a free cusp, and survives on the 35 free-cusp members only at order-4 points with non-unitary global holonomy, if any exist

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the weight table; Theorems B, C, C′ exact over ℚ; m004's order-4 points and their unitarity exact) + NEGATIVE (the mixed frame on m004 and on every member without a free cusp, under the abelianised reading at the cusp) + OPEN (the mixed frame on the 35 free-cusp members at order-4 points, contingent on such points existing with non-unitary holonomy) · **Price: unchanged** · **Numbering:** B1372 (door 2 of the owner's question; opened by the reply of 2026-09-16).

## 0. Seen from above

The record's exclusions of chirality on the cusped object and its family all pass through the same hinge: the connection leaving the
Standard Model unbroken lives in SL(2)_β × ℂ*², so every bulk sector is an SL(2)_β-spin times a character, and in each of the two
matter frames one half of a generation is spin 0 — a character alone, abelian Higgs data — where B1369's free-cusp theorem and parity
decide. Door 2 asked what the non-abelian part can do that a character cannot. The only place it can act on a full generation is
the third reading, unexamined until now: the 10 taken from the 78's (2,20) and the 5̄ from the 27's (2,6̄), both halves doublets,
both halves seeing the SL(2)_β connection ρ and its Higgs field Φ = Im 𝒜. This arc closes that reading wherever the abelian Higgs
field vanishes, by arithmetic on the cusp. A doublet sector is cusp-fixed when a joint eigenvector of the peripheral holonomy has
total holonomy 1, so its character must equal an eigenvalue of ρ(p)^{∓1} on the peripheral elements. If that eigenvalue is
non-unitary, the imaginary parts of the character data are pinned by the weights' (Y, γ): the 10 of the 78 (γ = 1, three Y-types)
forces Im s = 0 and Im t = ±L, the 5̄ of the 27 (γ = ⅓) forces Im t = ±3L — never both (Theorem B). If it is unitary, e^{2πiθ}, the
fifteen congruences Y(w)a + γ(w)b + ε_wθ ∈ ℤ have solutions only for θ ∈ ¼ℤ (Theorem C), and at θ = ±¼ the eigenvector signs ε_w are
never uniform: either the 10 and the 5̄ sit on opposite eigenvectors, or Q and d^c on one and u^c, e^c, L on the other (Theorem C′).
The fixed weight's partition of the torus is by ε_w times the σ₃-component of Φ's leading cusp mode, the same function for every
doublet, so where no abelian Higgs field exists the chiralities of the pieces are opposite and no generation is assembled. Parabolic
peripheral holonomy (the hyperbolic structure itself and its conjugates, on every member) and central holonomy make every doublet
sector vector-like outright (Lemmas A and D). On m004 the order-4 points of the character variety are the four SU(2) dihedral
representations, unitary, with no Higgs field: door 2 is closed on the object. On the 77 members without a free cusp the abelian
Higgs field vanishes at every order-4 point and C′ closes the door. What survives is narrow and double-conditional: an order-4
point with non-unitary global holonomy on one of the 35 free-cusp members, where the abelian Higgs field could reorder the
partitions — nobody has computed those character varieties.

## 1. The frame, and two lemmas on non-abelian cusp holonomy

1. **Sectors** (B1368, B1369 §1). ρ: π₁(M) → SL(2)_β and a character χ on (Y, γ); a doublet sector is V₂ ⊗ χ_w. On cusp c the
   peripheral holonomy ρ(μ), ρ(λ) commutes and is parabolic (eigenvalues ±1, non-scalar), central (±I) or diagonalisable with
   eigenvalues m_p^{±1}, m_p ≠ ±1. The sector is cusp-fixed iff a joint eigenvector has total holonomy 1: χ_w(p) = m_p^{−1} on e₁
   or χ_w(p) = m_p on e₂, for p = μ, λ. A non-fixed weight contributes nothing (B1351 (ii)).
2. **Lemma A (parabolic).** For the holonomy of the hyperbolic structure the complexified connection on the cusp is ω + ie with e the
   coframe; its dt-component is the boost generator, Cartan in the eigenbasis of the parabolic holonomy with eigenvalues ±½ on V₂.
   The two weights of a doublet therefore see Morse functions ±t/2 along the cusp: the partition is the whole torus for one and empty
   for the other, χ(∂⁺; L) = 0 either way, N = 0. This holds at every parabolic point on every member, cusp-fixed or not, and
   sharpens B1368's "never cusp-fixed for the geometric representation" to "never chiral".
3. **Lemma D (central).** If ρ(P_c) = ±I, both weights of the doublet are fixed by the same character and the Cartan direction of Φ's
   leading cusp mode gives them complementary partitions {F > 0} and {F < 0}; the sector's index is −χ(∂⁺_F) − χ(∂⁻_F) = 0 for
   transverse zeros.
4. **Diagonalisable, m_p ≠ ±1.** Exactly one eigenvector can be fixed for a given character; its partition is by ε·½·F_Φ plus the
   abelian part Y(w)F_Y + γ(w)F_γ, with F_Φ the σ₃-leading mode of Φ in the peripheral eigenbasis (the abelianised reading at the
   cusp, §5.1) and F_Y, F_γ the abelian Higgs forms, which vanish unless the cusp is free (B1369).

## 2. Computed

`verification/doublet_halves.py` (seconds, exact over ℚ and ℚ(i, √5); record `doublet_halves_run.txt`).

| item | result |
|---|---|
| the 27 by SM type, β·w, γ | Q ×6, u^c ×3, e^c ×1 at β·w = 0, γ = −⅔ (the 10: spin 0); d^c ×3 and L ×2 at β·w = ±1, γ = ⅓ (the 5̄ and the 5̄′: doublets); ν^c/N at β·w = ±1, γ = −5/3; D ×3, H_u ×2 at β·w = 0, γ = 4/3 |
| the 78 by SM type, β·w, γ | Q ×6, u^c ×3, e^c ×1 at β·w = ±1, γ = 1 (the 10: doublets), their conjugates at β·w = ±1, γ = −1 (the 10̄); d^c-type ×3 and L-type ×2 at β·w = 0, γ = 2 (the 5̄: spin 0), D ×3 and H_u ×2 at β·w = 0, γ = −2; the SL(2)_β adjoint at β·w = ±2, γ = 0; the 24 of SU(5) at spin 0, γ = 0 |
| frame theorem (B1368) | reproduced: in the 27 the 10 is spin 0 and the 5̄ doublets; in the 78 the 10 doublets and the 5̄ spin 0 |
| the both-doublet assignment | unique: the 10 from the 78 (γ = 1, Y-types 1/6, −2/3, 1) with the 5̄ from the 27 (γ = ⅓, Y-types ⅓, −½); the 27's other 5̄ (the 5̄′) has the same charges |
| Theorem B (non-unitary m_p) | sign patterns (which eigenvector each of the five (Y, γ)-types fixes) admitting (Im s, Im t) with L ≠ 0: **0 of 32**; the 10 alone: (Im s, Im t) = (0, ±L); the 5̄ alone: (0, ±3L) or (±12L/5, ±3L/5) |
| Theorem C (unitary m_p = e^{2πiθ}) | θ mod 1 admitting a solution of the fifteen congruences, over all 32 patterns: **{0, ¼, ½, ¾}** |
| Theorem C′ (θ = ±¼) | 4 patterns with a solution; all fifteen weights on the same eigenvector: **0**; the patterns: (Q, u^c, e^c \| d^c, L) = (+, +, + \| −, −), (−, −, − \| +, +), (+, −, + \| +, −), (−, +, − \| −, +); example (a, b, θ) = (0, −15/4, ¾) |
| m004's order-4 points | Riley's form on the meridian presentation ⟨a, b \| a w b⁻¹ w⁻¹⟩; at m = ±i the representations are y = −(5 ± √5)/2 (the y = 0 factor of the two-entry gcd is not a representation there): 4 points, ρ(λ) = 1 at all, each preserving a definite Hermitian form — the four SU(2) dihedral representations of B1368 |

## 3. The theorems

**Theorem B.** On a peripheral element p with a non-unitary eigenvalue e^{L}e^{iα}, L ≠ 0, no character makes the 10 of the 78 and
the 5̄ of the 27 cusp-fixed together. *Proof.* |χ_w(p)| = e^{−2π(Y(w)Im s + γ(w)Im t)} must equal e^{∓L} for each weight. The three
Y-types of the 10 share γ = 1: the differences force Im s = 0, then Im t = ±L/2π up to the sign convention. The two Y-types of the
5̄ share γ = ⅓: with Im s = 0 they force Im t = ±3L/2π. Contradiction for L ≠ 0; the exhaustive check over the 32 sign patterns
confirms it. ∎

**Theorem C.** On a peripheral element with unitary eigenvalue e^{2πiθ}, both halves are cusp-fixed only if θ ∈ ¼ℤ. *Proof.* The
fifteen conditions reduce to five, Y_i a + γ_i b + ε_i θ ∈ ℤ; eliminating a and b between the 10's three types and between the
5̄'s two types gives (ε₂ + ε₃ − 2ε₁)θ ∈ ℤ, (ε₅ − ε₄)θ ≡ (ε₂ − ε₁)θ and (ε₁ − 3ε₄)θ ∈ ℤ modulo the lattice, whose only solutions
for signs ±1 have 4θ ∈ ℤ; the symbolic solution over all patterns returns exactly {0, ¼, ½, ¾}. ∎ (θ ∈ {0, ½} is the parabolic or
central case of Lemmas A and D.)

**Theorem C′.** At θ = ±¼ the four admissible sign patterns are never uniform. Since ε_w decides which eigenvector is fixed and hence
the sign of the weight's Morse function along the common Cartan direction of Φ, on a cusp where the abelian Higgs field vanishes the
pieces of a would-be generation have opposite chiralities: either the whole 10 against the whole 5̄, or {Q, d^c} against {u^c, e^c,
L}. Neither is a generation. ∎

**Corollary.** In the mixed frame no generation arises (i) on m004 — its order-4 points are unitary, Φ = 0; (ii) on any member on a
cusp of full peripheral rank — the characters are of finite order there (B1369), the abelian Higgs field vanishes and C′ applies;
(iii) at any parabolic or central point of any member (Lemmas A, D). What is left: order-4 points with non-unitary global holonomy on
a free cusp, where F_Y, F_γ can reorder the partitions.

## 4. What it means

1. **Door 2 is closed where the record's frames live.** The non-abelian part of the connection cannot rescue a generation on m004 or
   on the 77 full-rank members; the two matter frames' spin-0 halves (B1369) and the mixed frame's doublet halves (this arc) are closed
   by the same charge table read at the cusp.
2. **The mixed frame is a stronger reading than the record adopted.** It requires the 27 and the 78 both as bulk matter, so that the
   10 comes from one field and the 5̄ from the other; B1368's caveat 4 did not consider it. It is closed here regardless.
3. **What remains is double-conditional.** An order-4 point (peripheral eigenvalues ±i) with non-unitary global holonomy, on one of the
   35 members with a free cusp, with the abelian Higgs field's leading cusp mode dominating Φ's on the right weights. The record has no
   character-variety data for those members; on m004 the order-4 points are the dihedral representations, unitary.
4. **The three faces.** The charge table is the root system's; the peripheral eigenvalues are the hyperbolic geometry's (parabolic for
   the structure itself); the partition is the quantum theory's.

## 5. Caveats

1. The abelianised reading at the cusp: a doublet weight's boundary behaviour is taken from the σ₃-component of Φ's leading cusp mode
   in the eigenbasis of the peripheral holonomy, the off-diagonal components being subleading for the fixed weight; this is the
   record's Pantev–Wijnholt frame applied sector by sector (B1351, B1368), and it is what makes C′'s sign argument bite.
2. Lemma A uses that the dt-component of the coframe is Cartan in the parabolic eigenbasis with eigenvalues ±½ — the standard form of
   the hyperbolic holonomy on a cusp; Lemma D needs transverse zeros as in B1281 §2D.
3. Theorems B and C assume one connection for both halves (the same s, t on each peripheral element), which is what a single
   background means; the 5̄′ of the 27 carries the same (Y, γ) as the 5̄ and changes nothing.
4. Whether order-4 non-unitary points exist on the free-cusp members is not known; B1368's resultant method (Riley's form) applies to
   two-bridge groups, and most members are not.

## 6. Registered

Door 2's residual named: order-4 points with non-unitary holonomy on the 35 free-cusp members (character-variety data the record lacks).
Nothing else new.

## Verification

`verification/doublet_halves.py`: the E₆ roots and the 27 in the record's coordinates, SM typing by colour and weak weights and Y,
β·w and γ per weight; Theorem B by solving the imaginary-part systems over all sign patterns; Theorem C by solving the congruences
symbolically (three equations for (a, b, θ), the other two as integrality constraints, integers enumerated in a box); Theorem C′ by
listing the admissible patterns at θ = ±¼; m004's order-4 points from Riley's normal form on the meridian presentation with the full
relator check, ρ(λ) from the longitude word, unitarity by an invariant Hermitian form. Lock: `tests/test_b1372_the_doublet_halves.py`.

**Sources.** B1368 (the placement in SL(2)_β × ℂ*², the sector census, the λ-parabolic points), B1369 (the free-cusp theorem, the
parity lemma), B1351 (the index), B1365/B1366 (the charge table and the unique embedding), B1281 §2D (transverse zeros). Riley's normal
form for two-bridge knot groups; the cusp form of the hyperbolic holonomy (the coframe as the Higgs field, as in BCHS 2018).
