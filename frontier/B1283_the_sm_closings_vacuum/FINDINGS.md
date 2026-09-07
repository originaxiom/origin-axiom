# B1283 — THE SM CLOSING'S TREE-LEVEL VACUUM: on the closing whose gauge group is the Standard Model's, every SM-preserving flat direction leaves one extra U(1) unbroken — a definite Z′ with computed charges — and carries exactly one light Higgs pair, one light colour-triplet pair and a ν^c VEV

**Date:** 2026-09-07 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (exact: the F-flat rule for squarefree cubics on coordinate subspaces, D-flatness by linear programming over the four abelian charges, the unbroken directions by exact linear algebra; every monomial checked U(1)⁴-invariant) · **Price: unchanged** · **Numbering:** B1283, the last number of this branch's reserved range.

## Why this arc — D2's space, on the closing that has the group

B1277 computed the tree-level vacuum manifold of the E₈ theory on Y₃ and found nine branches, none with the Standard-Model
group: the neutral VEVs run E₆ → SO(10) → SU(5) → SU(4). B1278 then found the closing that has the group and the count:
on Y₉ a Wilson line W valued in the order-19/38 characters breaks E₆ to su(3) ⊕ su(2) ⊕ u(1)_Y ⊕ u(1)_β ⊕ u(1)′ (the
centralizer of a generic element of the SM's commutant SU(2)_β·A, B1277 (d)) with three complete 27s and 27̄s and the six
flavons. The destination ledger's item 2 asked for the vacuum manifold on which the instanton superpotential acts; here it
is computed **on the SM closing**, where the broken E₆ generators' D-terms are gone (their gauge bosons are heavy at the
closing's scale) and only the four abelian D-terms — β, ′ and the two family charges — and the SM's own remain.

## 1. The SM-singlet sector ((a), exact)

The components of the 27 that are colour singlets with T₃ = Y = 0 are **N** (the SO(10) singlet) and **ν^c**; with their
conjugates in the three 27̄s and the six flavons S_ij these are the **18 fields** whose VEVs preserve the Standard Model.
Their charges under the two extra E₆ Cartan directions (β = the su(2)_β Cartan, γ = the direction orthogonal to the SM
Cartan and to β), identified on every SM field as **β = (ψ + χ)/4** and **γ = −(5/12)ψ + (1/4)χ** (ψ: 16 → 1, 10 → −2,
1 → 4; χ: the 10 of the 16 → −1, its 5̄ → 3, its 1 → −5, the 5 of the 10 → 2, its 5̄ → −2):

| field | (q_β, q_γ) | field | (q_β, q_γ) |
|---|---|---|---|
| Q, u^c, e^c (the 10 of SU(5)) | (0, −2/3) | H_u, D (the 5 of the 10) | (0, 4/3) |
| d^c, L (the 5̄ of the 16) | (1, 1/3) | H_d, D̄ (the 5̄ of the 10) | (−1, 1/3) |
| ν^c | (−1, −5/3) | N | (1, −5/3) |

(N, ν^c) is an su(2)_β doublet: opposite β, equal γ. The one-coupling cubic (B1276) has **14 monomials among the 18
singlets** — the twelve flavon couplings S_ij N_j N̄_i, S_ij ν^c_j ν̄^c_i and the two flavon cubics — and no purely-singlet
27³ term (the zero-sum triples of the 27 are N h_u h_d and ν h_u ν^c, B1277). Every monomial is U(1)⁴-invariant (checked).

## 2. The flat directions ((b), exact)

F-flatness on a coordinate subspace (exact for squarefree cubics: no monomial may contain two switched-on fields) gives 85
maximal F-flat sets; D-flatness under the four U(1)s (a strictly positive combination of the switched-on charge vectors
vanishing — an LP on every subset) cuts them to **nine maximal SM-preserving branches, all conjugate-paired** — no
unpaired direction exists even under the reduced gauge group (the LP finds none; the paired ones are D-flat for all of E₆,
so the list is independent of how much of SU(2)_β the Wilson line leaves):

| branch | fields | surviving extra U(1)s | complex moduli |
|---|---|---|---|
| **three maximal:** generation g's N and ν^c with the other pair's flavons: {N_g, N̄_g, ν^c_g, ν̄^c_g, S_hk, S_kh} | 6 | **1** | 3 (⟨NN̄⟩, ⟨ν^cν̄^c⟩, ⟨SS⟩) |
| six: {N_g, N̄_g, ν^c_h, ν̄^c_h}, g ≠ h | 4 | 2 | 2 |

> **No tree-level branch breaks all four extra U(1)s: the minimal surviving abelian rank is 1. The gauge group of the SM
> closing at tree level is SU(3) × SU(2) × U(1)_Y × U(1)_{Z′}.**

On each maximal branch the surviving direction is Z′ = −6γ + (a family part depending on g): its E₆ part is
**(5ψ − 3χ)/2**, with charges **4 on Q, u^c, e^c; −2 on d^c, L; 10 on ν^c and N; −8 on H_u and D; −2 on H_d and D̄** (up
to the family charges ±5, ±10 that distinguish the generations). β is broken on every branch (N_g and ν^c_g both have
VEVs), and N and ν^c carry the same Z′ charge.

## 3. The electroweak sector on each branch ((c), exact)

The μ-terms come from d_abc 27₁27₂27₃: μ_jk = λ|ε_ijk|⟨N_i⟩ (B1273's zero diagonal). Every maximal branch has exactly one
generation's N, so the doublet mass matrix has rank 2: **exactly one light Higgs pair — generation g's own h_u, h_d — and,
from the same matrix on the 10 of SO(10), exactly one light colour-triplet pair D_g, D̄_g** (the doublet–triplet problem in
its E₆ form, B1276's row 4). Three N VEVs would make every doublet heavy (det = 2N₁N₂N₃) and no branch has them. **Every
branch has a ν^c VEV**, and ν h_u ν^c then mixes the heavy generations' lepton doublets with their down-Higgs doublets at
the VEV scale (the light generation-g doublets are untouched at tree level).

## 4. What this settles

- **D2's space on the SM closing:** three maximal branches, each a three-complex-dimensional flat manifold of the scales
  ⟨N_g⟩, ⟨ν^c_g⟩, ⟨S_hk⟩ with one extra U(1) unbroken; the instanton superpotential (L201, item 3) acts on these three
  moduli and must also break, or leave as a Z′, the last U(1). At tree level the object's SM closing predicts a Z′ with
  the charges of §2 and one light Higgs pair per branch.
- B1277's "no SM point" on Y₃ becomes, on Y₉, "the SM plus one Z′": the closing supplies the group, the count and the
  flat directions; the rank reduction 8 → 4 is not completed at tree level (8 → 5).
- The tree-level light spectrum of a maximal branch: three generations of the SM, one Higgs pair, one D/D̄ pair, the
  moduli — everything else at the scales ⟨N⟩, ⟨ν^c⟩, ⟨S⟩.
- Values: 0 of 19 (the scales are moduli); no identification moves; price unchanged.

## Controls (MB12)

- Every cubic monomial is checked invariant under the four U(1)s, and the absence of a purely-singlet 27³ term is checked
  against the zero-sum triples of the 27, not assumed.
- The E₆ identification of β and γ is verified on all eleven SM field types against the (ψ, χ) tables.
- The LP is run on every subset of every F-flat set (exhaustive), so "no unpaired branch" is a search over the whole
  configuration space of the 18 singlets, and the paired branches are exactly B1277's restricted to singlets — the
  reduced gauge group added nothing, which is the honest and checkable statement.
- The μ-matrix ranks are computed symbolically for every branch; the three-N case (rank 3, no light pair) is exhibited as
  the control that the rule discriminates.

## Verification

`verification/sm_closing_vacuum.py` (~3 min; `SELFTEST: PASS`; run record `verification/sm_closing_vacuum_run.txt`).
Lock: `tests/test_b1283_the_sm_closings_vacuum.py` (slow-marked; the charge tables fast). Feeds on: B1277 (the machinery:
descent data, the F-flat rule, the pairing criterion, su(2)_β), B1278 (the SM lines of Y₉), B1276 (the one-coupling
cubic), B1273 (the zero diagonal), B1279 (the 19 624 vacua; the branch list is the same for every line). Literature: the
exact F-flat rule for squarefree cubics; the Luty–Taylor / Buccella–Derendinger–Ferrara–Savoy pairing criterion for
D-flatness; the E₆SSM Z′ literature for comparison (the U(1)_N of the E₆SSM is the direction under which ν^c is neutral;
the object's Z′ = (5ψ − 3χ)/2 is not it — ν^c and N both carry charge 10). Registers no identification change.
