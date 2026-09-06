# LITERATURE SWEEP — 2026-09-06: the M-theory Higgs-bundle frame, and what it says about the destination

*Done at the owner's question "do you need more repo retrieval/sweep and literature search before you go for it?"
before any construction is attempted. The frame below is the modern form of the transport the corpus has used
since B277/B1269 (7d super-Yang–Mills on the 3-manifold of ADE singularities); it was absent from the corpus
(no Pantev–Wijnholt, no Higgs bundle, no T-brane in 1276 arcs). Firewall: nothing here is a value; the
statements are the literature's, cited, and the corpus's own results are placed against them.*

## 1. The frame (Pantev–Wijnholt 2009; Braun–Cizel–Hübner–Schäfer-Nameki 2018; Barbosa et al. 2019)

M-theory on a G₂ manifold with an ADE singularity along a 3-manifold Q₃ is, locally, 7d SYM on Q₃, partially
twisted: the fields are a gauge connection A and an **adjoint-valued 1-form Higgs field φ** with the BPS
(Hitchin-type) equations F_A = [φ,φ], D_Aφ = 0, D_A†φ = 0 (PW eq. 3.16–3.17; BCHS eq. 2.18). The corpus's
"flat connection on Q" is the A; the corpus's deformation classes H¹(Q; ad ρ) are the φ.

- **Abelian φ:** φ = df with f harmonic — a Morse function; charged zero modes are the Witten-deformed complex
  of q·f, and *"the massless matter content is simply given by the ranks of the relative cohomology groups:
  N_χ(R) = h¹(M, ∂⁺M), N_χ̄(R) = h²(M, ∂⁺M), where ∂⁺M is the boundary of M where the Morse function is
  increasing"* — hence **net chiral(R) = χ(M, ∂⁺M)** (PW 3.39–3.40), *"purely combinatorial"*.
- **Closed Q₃:** *"the chiral index is then given by the usual Euler characteristic, which vanishes for odd
  dimensional closed manifolds"* (BCHS §2.4, eq. 2.50). M-theory on twisted-connected-sum G₂ manifolds is
  non-chiral; chirality needs a *singular transition* that *"can no longer be a TCS"*; **no compact G₂ example
  with chiral matter is constructed** (BCHS restrict to diagonalizable φ).
- **Non-abelian φ (T-branes):** with non-commuting/nilpotent Higgs components, localized chiral modes can sit
  at loci that are geometrically codimension six, *"invisible in the geometry"*; the zero modes are the
  cohomology of the complexified connection 𝒜 = A + iφ on 𝒪 ⊗ 𝔤_ℂ (Barbosa et al. §4–5); the analysis is
  local, no compact statement.
- **Instantons:** gradient-flow lines (M2-instantons) lift paired modes; the true zero modes are the Morse
  cohomology (PW §3.3).

## 2. The corpus placed in the frame

| corpus result | its place in the frame |
|---|---|
| the holonomy ρ and h¹(Q; V_ρ) (B1263, B1268, B1270, B1273–B1274) | the flat A; the *naive* spectrum, which PW's instantons correct to the Morse cohomology of the Higgs field — on the object the Higgs field's abelian part is the b₁ = 1 class and the non-abelian part is H¹(m004; e₆) (B575/B576) |
| the abelian sector twisted by C_t, walled by Alexander reciprocity (B1260 (2)) | the Morse–Novikov complex of the b₁ class: zero modes only at the Alexander roots t = φ^{±2} (the golden face), net 0 by Δ(t) = Δ(1/t) |
| the cusp lemma N(V) = rank(res_V) − h⁰(∂M; V) and −h⁰ ≤ N ≤ h⁰ (B1268) | PW's net chiral = χ(M, ∂⁺M) on the cusped object: with ∂M a torus, χ(M, ∂⁺M) = −χ(∂⁺M), so **net chirality on the object is minus the Euler characteristic of the part of the cusp torus where the Higgs field's charge points outward** — a disc (χ = 1) gives one chiral 27, an annulus or the whole torus gives none |
| the θ-odd deformations with full E₆(ℂ) closure (B576) and the θ-odd point with N = 0 (B1268) | T-brane data (non-commuting φ); the zero modes = h¹ of the complexified connection = exactly what B1268 computed; N = 0 at the point reached, |N(27)| ≤ 1 near the geometric point |
| the flat orbifold cannot isolate (B1259) | BCHS's closed-manifold vanishing; the enhancement points are the singular transitions BCHS prescribe and do not construct |
| B1276's one coupling, μ = m_D, both D couplings | the E₆SSM's superpotential (King–Moretti–Nevzorov 2020) with its **imposed** ℤ₂ symmetries removed: the review imposes ℤ₂^H (approximate), ℤ₂^L or ℤ₂^B (exact: diquark vs leptoquark), takes ⟨S⟩ ≫ 1 TeV with μ = λs/√2, and Majorana masses from dimension-5 operators (27̄_H 27)(27̄_H 27)/M_Pl at the GUT scale; the light doublets are *assumed*. Every imposition is a D2/D3 entry of the destination ledger |

## 3. What this decides about the destination (`docs/THE_DESTINATION_LEDGER_2026-09-06.md`)

1. **D3's carrier is a formula now.** Net chirality of a charged field on the object is χ(M, ∂⁺M): on any closed
   closing it is 0; on the cusped object it is −χ(∂⁺ cusp). The chirality bit the corpus has carried since
   B582 *is* the choice of the Higgs field's outward region on the cusp torus — a disc versus an annulus — which
   the complete hyperbolic Higgs fields (asymptotically translation-invariant on the cusp) do not make.
   **The bit is a boundary condition at the cusp.** This is B1268's lemma in the literature's words.
2. **The compact chiral G₂ closing does not exist in the literature either.** BCHS (2019): TCS is non-chiral,
   chirality needs a non-TCS singular transition, none constructed; Joyce–Karigiannis resolutions need a
   nowhere-vanishing harmonic 1-form on the singular locus (b₁ > 0 — not Y₃). The corpus's "named object" is the
   field's open problem, not a gap in the record.
3. **T-branes are the one loophole the corpus has not typed.** The θ-odd second-order deformation certificates of
   B575 are nilpotent-type Higgs data; Barbosa et al.'s prescription (h¹ of 𝒜 = A + iφ on 𝒪 ⊗ 𝔤_ℂ) is exactly the
   twisted cohomology the corpus computes — so the loophole is already inside |N(27)| ≤ 1 near the geometric point.
4. **Instantons in orbifolds are computable** (Acharya–Braun–Svanes–Valandro 2018: infinitely many associatives
   in compact G₂ orbifolds contribute to the superpotential); in a vector-like flat closing the hierarchy question
   (L201) can be asked as structure before chirality is solved.

## 4. Registered

- **L204 — the cusp Morse structure of the object's Higgs fields:** compute ∂⁺(cusp) for (a) the b₁ class
  (abelian: the Novikov complex at t = φ^{±2}) and (b) the θ-odd E₆ deformations (T-brane), and the boundary
  condition at the cusp that would make ∂⁺ a disc; relate to B432's fillings.
- **L205 — the tree-level vacuum manifold of the Y₃ theory** (D2's space): the F- and D-flat directions of the
  one-coupling superpotential (B1276) with 3 × 27 + 3 × 27̄ + 6 singlets under e₆ ⊕ u(1)².

Both closed the same day by B1277: L204 with N = 0 (χ(M, ∂⁺M) = 0 for every ∂⁺ ⊆ T²; abelian zero modes only at the
non-unitary golden values t = φ^{±2}); L205 with the nine-branch manifold, no SM point, the SM point through the
closing's sign character at the cost of one generation's doublets, and the theorem SM + three generations ⟹ SU(5)
on Y₃.

## Sources

Pantev, Wijnholt, *Hitchin's equations and M-theory phenomenology*, J. Geom. Phys. 61 (2011), arXiv:0905.1968 ·
Braun, Cizel, Hübner, Schäfer-Nameki, *Higgs bundles for M-theory on G₂-manifolds*, JHEP 03 (2019) 199,
arXiv:1812.06072 · Barbosa, Cvetič, Heckman, Lawrie, Torres, Zoccarato, *T-branes and G₂ backgrounds*, PRD 101
(2020) 026015, arXiv:1906.02212 · King, Moretti, Nevzorov, *A review of the exceptional supersymmetric Standard
Model*, Symmetry 12 (2020) 557, arXiv:2002.02788 · Acharya, Braun, Svanes, Valandro, *Counting associatives in
compact G₂ orbifolds*, JHEP 03 (2019) 138, arXiv:1812.04008 · Acharya, Foscolo, Najjar, Svanes, *New G₂-conifolds
in M-theory and their field theory interpretation*, JHEP 05 (2021) 250, arXiv:2011.06998 · Helling, Kim, Mennicke,
*A geometric study of Fibonacci groups*, J. Lie Theory 8 (1998) (the Fibonacci manifolds as the cyclic branched
covers of the figure-eight knot; Y₃ the Hantzsche–Wendt manifold).
