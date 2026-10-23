# W137 — the joint frame's Yukawas: which weight the record allows, the minimal mass relation, the free numbers against the quark data, and θ̄ with J (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **W136** counted the coupling forms of the joint frame. The family group is Γ₄, and the least coupling is weight 2
  in ρ′.
- **The owner approved the next step (2026-10-23):** build the frame's mass matrices at the least weight, count its
  free numbers exactly, and compute θ̄. This decides whether the joint frame can predict the thirteen flavour numbers
  at all.
- **Two things have to be fixed first,** and the record has not fixed them:
  - which picture of the generations the coupling belongs to;
  - which weight the coupling carries. The web seat's relay on the count (CHAT1_TO_SM_2026-10-23_THE_CUBE_COUNT)
    suggests the 27s' weight (3 + m)/2 from W134.

  This rule states both pictures and computes in each.

## The objects

- **Reading I (modular flavour).**
  - τ is a four-dimensional modulus.
  - The three generations are the three components of one triplet of chiral fields Φ (each a 27 of E₆). They
    transform by ρ′_k (k ∈ {5, 13, 21}) with modular weight −k_Φ.
  - The superpotential has weight −h: h = 0 for global supersymmetry, h = 1 for supergravity with K = −log(−i(τ − τ̄)).
  - A coupling Y(τ)·Φ³ is invariant iff Y ∈ M_w(Sym³ρ′) with w = 3k_Φ − h. That space has dimension C(w) (W136).
  - **The 27s' weight as k_Φ** (the web seat's suggestion; a READING). The field carries the inverse of its section's
    factor, so k_Φ = (3 + m)/2 at W134's datum m.
- **Reading II (the weave's surface).** The generations are three sections ψ_a of the family bundle. Their coupling is
  E₈'s ε contracted with them, det(ψ_a, ψ_b, ψ_c) (W134, W135).
- **The minimal Higgs and Clebsch.**
  - The Higgs doublets sit in the families' 10s (W135's reading), with constant vevs v_u·h_u and v_d·h_d, h ∈ ℂ³.
  - The Yukawas come from SO(10)'s 16·16·10, the standard decomposition (Slansky), not computed here:
    M_u = v_u λ(h_u) and M_d = M_e = v_d λ(h_d), with λ(h)_{jk} = Σ_i h_i λ_{ijk}.
- **The quark observables:** six masses, three angles and J; the invariants of the pair (H_u, H_d) = (M_uM_u†, M_dM_d†).
- **CP.** τ → −τ̄ with v(−τ̄) = X·conj v(τ), where X = diag(1, 1, −1) in the parity basis (by hand from the thetas'
  real coefficients). Xρ′(S)X = ρ′(S) and Xρ′(T)X = ρ′(T)⁻¹, so CP acts on M_w(Sym³ρ′) as an antilinear involution.

## Weave or thread

**WEAVE-type.**
- The joint frame: E₆ from the moves, the families' Γ₄, every det-1 twist, every admissible datum m.
- Claims about every coupling, constant and vev at once.
- No line is chosen.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| Y0 | **Reading II has no tree-level coupling** (exact, symbolic). For any three vectors, the full symmetrisation of det(ψ_a, ψ_b, ψ_c) over (a, b, c) is 0. Identical 27s see only the symmetric part, so the tree-level superpotential among the generations vanishes at every point of the surface (as W134 and W135 stated) | 99% |
| Y1 | **The weight in reading I** (exact). ρ′_k(−I) = 1 for k = 5, 13, 21, so k_Φ is even. With h = 0, w ∈ 6ℤ: the least coupling is at w = 6 (k_Φ = 2), with C(6) = 6 constants. W136's weight 2 is not reachable. k_Φ = 0 gives no coupling (C(0) = 0). With h = 1, w is odd and carries no form: **no coupling at all**. With k_Φ = (3 + m)/2: k_Φ is even at every admissible (r, m). At W134's least data, m = 1 gives w = 6 and m = −3 gives none. At the twelve three-generation data, m ∈ {−23, −19} (five data) give w < 0 and no coupling; m = 17 gives w = 30 with C = 26; m = 21 gives w = 36 with C = 30 | 92% |
| Y2 | **The minimal relation** (exact; numerical check at five random points). λ is totally symmetric, so λ(h) is symmetric and M_e = M_dᵀ = M_d. Hence m_e = m_d, m_μ = m_s, m_τ = m_b at the matching scale, and D = (m_μ/m_e)/(m_s/m_d) ≡ 1 at every τ, weight, constant and vev. Against P-094's D = 10.58 ± 0.11 (W58's A2), **the minimal joint frame is excluded**, with no fit | 97% |
| Y3 | **The instrument** (exact). Projection of the degree-w polynomials in v = 2η³R through the 48-element image gives dim M₂(Sym³ρ′) = 2 and dim M₆(Sym³ρ′) = 6, matching W136's C(2) and C(6). v(−τ̄) = X·conj v(τ) to 10⁻⁴⁰ at five random τ. The CP-fixed forms span each space over ℂ, with real dimension 2 and 6 | 95% |
| Y4 | **θ̄ and J** (60 digits). Real constants on the CP-fixed basis at w = 6, and CP-invariant vevs (h = X·conj h). **On the CP line τ = iy** (y = 0.9, 1.3, 2.1): J = 0 and θ̄ ∈ {0, π}, to 10⁻³⁰. **At five random τ off it:** J ≠ 0 and θ̄ ∉ {0, π} at every point (both above 10⁻⁶). So CP violation in the mixing comes with θ̄ ≠ 0, and the frame does not fix θ̄ apart from τ | 85% |
| Y5 | **The free numbers against the quark data** (the rank of the Jacobian of the quark invariants, at five random points each). The invariants are the traces of H_u, H_d and their products, ten independent plus J. **w = 6 with CP: rank 10. w = 6 without CP: rank 10.** So the minimal frame predicts nothing in the quark sector at its least weight. For contrast, at the unreachable w = 2: rank 9 with CP (ten real parameters less one scale redundancy, so one quark relation) and rank 10 without | 80% |
| Y6 | the read-out. The parameter counts. The tensors of the least coupling. What the thirteen flavour numbers would need. A READING by hand | — |

## What the outcomes mean (fixed now)

- **Y0 to Y5 hold.** Then, for the joint frame as the record now has it:
  - **Its only rigid predictions are the minimal GUT relations, and they fail.** m_e = m_d and m_μ = m_s, with
    D = 1 against 10.58.
  - **Everything else is fitted.** At the least weight reading I allows (6), the coupling's six constants, τ and the
    two vev directions saturate the ten quark observables. Supergravity with one modulus (h = 1) allows no coupling at
    all.
  - **θ̄ moves with τ.** It is fixed only on the CP line, where J vanishes too.
  - **So for the 19, the joint frame needs two things it does not have:**
    - a principle that fixes the constants and the vev directions (PF1-W, the web seat's reading of GENESIS PF1, on
      the couplings or on the Higgs; the owner's P-303 is part of this);
    - a Clebsch beyond 16·16·10 that breaks M_e = M_d. In E₆ that could be the mixing of d^c with D^c and of L with
      the 10's doublets after E₆ breaks, or a 351′.
  - B1726's factor 3 and main's D = 9 on order-5 lines are the record's current stand-ins for the second.
- **Y1 fails** (an odd or fractional weight is allowed). Recorded as found; the counts are redone at that weight.
- **Y4 fails** (θ̄ ∈ {0, π} off the CP line with J ≠ 0). That would be a structural θ̄ like W113's. It is recorded as
  found, the positive this seat does not expect.
- **Y5 finds a rank below 10 at w = 6.** The minimal frame would then predict quark relations. Recorded as found.

## What stays out

- **The values:** of the constants, τ and the vevs. No fit to data; the only data number used is P-094's D.
- **Beyond the minimal frame:** non-minimal Kähler potentials; E₆ breaking and its exotic mixings; the 351′.
- **The neutrinos' Majorana masses;** running between scales (D is close to scale-independent).
- **Reading I with generations of different weights** (impossible for one triplet).

## Seen before the rule (disclosed)

- **Read:**
  - W134, W135 and W136's records;
  - the web seat's cube-count relay (its weight suggestion and its reading of the 1′ channel);
  - B1726's FINDINGS line on D = 9 on order-5 lines (commit message);
  - B1732's and S195's commit messages;
  - W58's P-094 target;
  - B1730 and B1731 (the zero-free family; F₆).
- **By hand:**
  - k_Φ even and the weight arithmetic in Y1, with C(30) = 26 and C(36) = 30 from W136's closed forms;
  - the symmetric λ(h) and D = 1;
  - X = diag(1, 1, −1) and its action on ρ′;
  - the CP-line argument (M = X·conj(M)·X makes det M real and det[H_u, H_d] zero);
  - the parameter counts behind Y5's ranks.
- **From general knowledge, not the record:** in modular flavour models CP broken by τ generically gives θ̄ ≠ 0. The
  literature's escape ties the determinant's total weight to zero.
- **Not run:** nothing has been computed by a script.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
