# SM-R614 — what discrete symmetry survives 27 → SM, on main's own 27 weights and in GENESIS's U1-η

*Card of the SM seat, 2026-11-25, for register row P-614 (main's page M53). Written with its script
(`relays/sm_r614/run.py`, SHA-256 3c0d41bdb158ef68) before the script is run on E6. Until then the script has only been
import-tested and smoke-tested on toy inputs: SU(3) on its 3, SU(5) on its 5, and U(1) lattices. Data-free: no
measured value is read. Main's checkout was read at be8c83d4f.*

## 0. The question and what the record already says

- **The ask (M53):** the discrete symmetry that survives 27 → SM, computed on main's own 27 weights in GENESIS's U1-η
  normalisation. If it holds, the GENESIS line is owed a dated note.
- **GENESIS v1.69, §8 "Computed nowhere yet"** (lines 518 to 531 at be8c83d4f; the register row cites the older lines
  483 and 484):
  - U1-η is "left by the flat closing Y₃". It is the η direction of the rank-five E₆ breaking and is
    family-universal.
  - Both E₆-charged singlets of the 27 carry the same η charge, "so that no field of the 27 or the 78 gives ν^c a
    Majorana mass".
  - "Dirac against Majorana: decided by the discrete symmetry left when the extra abelian factor is broken, which no
    arc computes (A5)."
- **The charges on record.** Main's B1303 re-derived sm:B1283's table of the 27: for each of its eleven multiplets,
  the states, colour, weak dimension, Y, ψ and χ. It also gives γ = −5ψ/12 + χ/4.
  - B1365, harvested and checked on main's own code in B1415, identifies γ with the η model: γ = (2√15/3)·Q_η, the U(1)′
    of the Y₃ line. That line is a Q₈ line into SU(2)_β times an order-4 character. β is the Standard-Model-singlet
    root.
  - B1418 cell 4 (iv) found that the 27's two charged singlets share η and that no field has −2 times that charge. So
    no η-neutral term ν^cν^cX exists in 27³ or in the 78.
  - B1418 cell 4 (v) found that (27·27̄)² contains an η-neutral ν^cν^cν̄^cν̄^c.
- **The cloud seat's memos**, read by Review 74's reader (B1831, rows 450, 461, 465, 466 and 474). Their certificates
  reproduce. They were computed in a trinification frame whose ψ is a different SO(10) (memo 72's filed frame error).
  - Memo 72: the 27 has exactly two SM-safe vev directions, ν^c-like and S-like. With both, the Cartan annihilator is
    4-dimensional and holds the SM torus.
  - Memo 76: 15 nontrivial ℤ/2 gradings h ∈ ℤ⁶ mod 2 are even on both doors. One is the ℤ/6 shadow and 14 are called
    "extra". None is odd on all 15 matter states, and each is odd on exactly 8 of them.
  - Memo 77: the torus is exactly the SM's, and the u(1)_ψ remnant is trivial because gcd(1, 2) = 1.
  - Memo 61: a singlet-only vev keeps the matter parity but stops at rank five.
  - Memo 85: 27³ has no Majorana-shaped entry.
- **Related arcs:**
  - B1805: Spin(10)'s central z₂ is exactly matter parity. If C(H) contains the SM, then the rank is at least five.
  - B1208 LEG 4: main's 27-weight generator is B299's _weights_27.
  - B1652: main rules the E₆ frame refuted for the Standard Model. Everything here is a statement about the root's E₆
    bookkeeping, not about the world.

## 1. What will be computed, all exactly

The script uses Fractions, integer column reduction and sympy's Smith form. It imports main's B299 module
(the 27 weights and E6_CARTAN) from the checkout given on the command line.

- **A. The SM on main's weights.**
  - ψ is 3 times the fundamental coweight of the 27's top node.
  - Four embeddings are tried: SU(5) ⊂ D₅ has two spinor nodes to remove, and SU(3) × SU(2) ⊂ SU(5) has two splits.
  - For each, χ and Y are solved as Cartan directions, normalised, and every weight is labelled.
  - An embedding is kept only if it reproduces B1303's table on all 27 weights.
- **B. U1-η.**
  - η = 3γ = (3χ − 5ψ)/4 is the integer form of B1303's γ.
  - Checks:
    - η is constant on each multiplet and matches γ.
    - η is equal on ν^c and N, as GENESIS says.
    - η is orthogonal to the SM roots, Killing-orthogonal to Y, and annihilated by β = μ(N) − μ(ν^c).
    - β is a root.
    - Σq = Σq³ = 0.
    - η lies in the coroot lattice.
  - V₅ = V_SM + ℝη is checked to be ker β, the torus of SM × U1-η.
  - −1 ∈ SU(2)_β is shown to lie in that torus. This is a consistency fact for any root and cannot fail.
- **E. E₆-level vevs, the memos' setting.** The vevs are N only, ν^c only, ν^c + N in one 27 (two directions), and ν^c
  and N in two different 27s. For each:
  - the compact stabiliser: its dimension in the 78; its rank, from the centraliser of a random element, minimum over
    two seeds; and whether the SM algebra lies inside it;
  - the torus stabiliser's identity dimension and component group;
  - an exact matter-parity search over GF(2). It asks for a torus element that commutes with SU(3) × SU(2), fixes the
    vevs, is −1 on Q, u^c, d^c, L and e^c, and is +1 on H_u and H_d. A variant also makes ν^c odd.
  - E5 redoes memo 72/76's census on main's weights and tests each grading for three things: odd on all 15; central in
    the SM, that is constant on SM multiplets; and inside the SM torus, exp(iπh) ∈ exp(V_SM).
- **G. GENESIS's setting.** The flat closing leaves SM × U1-η, with torus V₅. A 27 singlet vev (ν^c, N, or both) breaks
  U1-η. For each:
  - the component group of the stabiliser modulo the SM's identity component, which is the residual discrete symmetry;
  - its generators' phases on the multiplets;
  - the matter-parity search;
  - whether every residual element allows ν^cν^c.
  - G4 asks directly whether exp(2πi η/5), the naive ℤ/5 a charge-5 vev leaves, is already an SM element.
- **M. 27³.** The zero-sum weight triples, those containing two SM singlets, whether −2 times a singlet is a weight, and
  whether every triple is η-neutral.
- **Plants that must fail:**
  - P1: a vev on H_u. Then the SM must not lie in the stabiliser, and V_SM must not be in its kernel.
  - P2: ψ and χ in place of η. Neither may be equal on ν^c and N.
  - P3: the naive rule "a charge-q vev leaves ℤ/|q|" applied to η, 2η and γ. It gives ℤ/5, ℤ/10 and a non-integer,
    while the lattice answer does not depend on the normalisation.
  - P4: an impossible parity that is odd on Q, u^c and H_u, which the cubic Q u^c H_u forbids. It must not be found.
- **Positive controls that must fire:**
  - C1 is E1 itself. With N only, the parity must be found: it is B1805's z₂, and memo 61's row.
  - C2: a vev with charge 2μ(ν^c), outside the 27 (351′-like). It should leave a nontrivial residual.

## 2. Expectations, written before the run

Disclosure: the priors for E3, E4 and G rest on hand reasoning done while designing the card, not on any run.

- **E3 and E4.** ν^c and N form a doublet of SU(2)_β, and SU(2)_β commutes with the SM. So a single 27's vev in their
  plane can be rotated onto N, and its stabiliser should be Spin(10), not the SM. Two independent 27s should leave
  SU(5).
- **G.** By hand, η/5 plus a hypercharge rotation of 2/5 and the colour centre is integral on all 27 states. So the
  naive ℤ/5 would already be an SM element.

| | expectation | prior |
|---|---|---|
| A1 | at least one of the four embeddings reproduces B1303's table on all 27 weights | 90% |
| B1 | η matches γ, is constant on multiplets, equal on ν^c and N (−5), ⊥ SM roots, ⊥ Y, β·η = 0, traces 0 | 90% |
| B2 | η is in the coroot lattice (a primitive integer cocharacter) | 85% |
| E1 | N only: stabiliser dim 45, rank 5, SM inside; matter parity found, with ν^c odd as well (C1) | 85% |
| E2 | ν^c only: dim 45, rank 5; no matter parity | 60% |
| E3 | ν^c + N in one 27: dim 45, rank 5, SM inside (Spin(10), not the SM: memo 77 holds for tori only) | 80% |
| E4 | ν^c and N in two 27s: dim 24, rank 4 (SU(5) ⊋ SM); torus identity = V_SM, no components; no matter parity | 75% |
| E5a | 15 nontrivial gradings even on both doors (memo 72's dim 4) | 80% |
| E5b | none is odd on all 15 (memo 76) | 85% |
| E5c | every grading is odd on exactly 8 of the 15 (memo 76) | 60% |
| E5d | all 15 lie in the SM torus, so none is a symmetry beyond the SM's group | 80% |
| E5e | exactly one of them is SM-central (the shadow) | 50% |
| G1 | for each singlet vev: identity dimension 4 (= SM) | 90% |
| G2 | the residual modulo the SM is trivial, and G4 holds (exp(2πi η/5) is an SM element) | 75% |
| G3 | no matter parity in SM × U1-η after a singlet vev | 90% |
| G4 | every residual element allows ν^cν^c (vacuous if G2 holds) | 90% |
| M1 | 45 zero-sum triples; none contains two SM singlets; −2 × singlet is not a weight; all η-neutral | 90% |
| P | P1, P2 and P4 fail as planted; P3's naive values differ (5, 10, 5/3) while the lattice answer is fixed | 95% |
| C2 | the 2μ(ν^c) vev leaves a nontrivial residual (ℤ/2), and a matter parity | 55% |

## 3. What it means

- **G2 and G3 hold.** GENESIS's line gets a dated note. On the root, when U1-η is broken by any 27 or 27̄ singlet vev,
  nothing beyond the SM's own group survives. The naive ℤ/5 lies in the SM's centre times hypercharge.
  - No residual symmetry then forbids a Majorana mass, and none is a matter parity.
  - Dirac holds only while U1-η is unbroken, which is B1365's statement.
  - A Majorana mass still needs a source that 27³ and the 78 do not have (B1418 iv). The record offers (27·27̄)²
    (B1418 v).
- **G2 fails** (a nontrivial residual). The note names the group and its phases, and says whether it forbids ν^cν^c.
- **E3 and E4 hold.** The memos' "only the SM torus survives" is right for the torus. The surviving group, however, is
  Spin(10) for one 27 and SU(5) for two 27s. A 27-only breaking at the E₆ level never reaches the SM. This is the
  E₆ analogue of B1805(e). The row's "only the SM torus survives" is then corrected in that scope.
- **E5d holds.** Memo 76's "14 extra E₆ remnants" are elements of the surviving SM torus, gauge transformations rather
  than extra symmetries. Its "no matter parity" stands.
- No outcome gives a value of any of the 19. Everything concerns the root's E₆ bookkeeping (GENESIS: root only;
  B1652).

## 4. What this does not check

- **The centraliser of the Q₈ line is taken to be connected, SM × U1-η.** This is an inference, not computed: the
  centraliser of SU(2)_β is SU(6) up to centre, SU(6) is simply connected, and −1 ∈ SU(2)_β lies in its torus (block
  B). Discrete elements outside the torus, such as Weyl-type components of a disconnected centraliser, are not
  searched.
- Not covered:
  - the components of the non-abelian E₆-level stabilisers;
  - 27̄, 351 or 351′ Higgs content (only C2 touches it, as a control);
  - any potential, vacuum selection or holomorphy (SUSY) argument for which operators are generated.

## 5. Files

relays/sm_r614/: the script, and in phase 2 its output r614_run.txt and r614_results.json. The page will be
relays/SM_R614_THE_DISCRETE_REMNANT.md, and the claim card relays/claims/CLAIM_2026-11-26_discrete_remnant_27.md.
Run as: python3 relays/sm_r614/run.py <main checkout>, with stdout saved to r614_run.txt.
