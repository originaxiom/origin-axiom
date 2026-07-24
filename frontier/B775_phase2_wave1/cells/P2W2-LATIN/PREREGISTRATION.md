# PREREGISTRATION — B775 Phase-2 Wave-2 cell P2W2-LATIN (OI-024)

Prereg parent: B775 Wave-2 addendum cc7e3b48. Structural cell. pyenv python3.
Nothing to CLAIMS; program-internal modular/fusion mathematics only; Gate 5/5-Q
(structure, no SM values, no sentience). The B774 chord discipline is binding.

## The banked-but-unproven fact (OI-024 / B629)
The E6 level-2 θ-odd hearing matrix B = Uᵀ (C·T²ST) U (the twisted weld projected
to the 3-dim θ-odd subspace of the conjugate pairs {27, 351′, 351}) has every entry
B_ij = −A_{k(i,j)}·ζ₁₄^{m(i,j)} with A_k = (2/√7) sin(2πk/7). B629 found — numerically,
to 100 digits, but WITHOUT proof — that the amplitude index k(i,j) forms the Latin
square [[1,2,3],[2,3,1],[3,1,2]], i.e. k(i,j) = ((i+j) mod 3)+1. Banked status:
exact, arrangement UNEXPLAINED.

## The question
DERIVE the Latin-square arrangement END-TO-END from the Kac–Peterson S/T fusion data
of E6 level 2 — show it is FORCED by the fusion geometry (⟹ THEOREM, RESOLVED-A), OR
show the arrangement is not forced / breaks (⟹ RESOLVED-B), OR UNRESOLVED.

## Conventions / choices (declared before run)
- Modular data built from scratch: exact W(E6) (51840 elts), S via exact 126th-root
  bincount, T via exact conformal weights h_a = ⟨λ,λ+2ρ⟩/(2κ), κ = k+h∨ = 2+12 = 14,
  c = 2·78/14. Primaries ordered [1,27,27b,351′,351′b,650,78,351,351b].
- θ = charge conjugation = the E6 diagram flip; C = S² (the conjugation permutation).
- θ-odd basis U: antisymmetric combos (e_a − e_ā)/√2 of the three conjugate pairs
  (27,27b), (351′,351′b), (351,351b); pair order i = 0,1,2 = (27, 351′, 351).
- ρ = T²ST (the "twisted weld" generator, per B594/B570); B = Uᵀ (C ρ) U.
- A_k = (2/√7) sin(2πk/7), k∈{1,2,3}; A1²+A2²+A3² = 1.
- ζ₁₄ = e^{iπ/7}.

## The claimed mechanism to be tested (stated before compute)
H1. Exact reduction: B_ij = −2i·t_i²·t_j·Im S_{a_i,a_j}, with a_i the unbarred pair-rep
    and t_a = T_{aa}; hence |B_ij| = 2|Im S_{a_i,a_j}| (amplitude = twice the imaginary
    part of the E6₂ S-matrix among the three pair-reps).
H2. Simple current: J = 351′ is an order-3 simple current (qd = 1, J³ = 1); its three
    free orbits partition the 9 primaries, and 27, 351′, 351 sit one in each orbit.
H3. Current row forced: since 351′ = J, S_{J,μ} = e^{2πiQ_J(μ)} S_{0μ} ⟹ the 351′-row of
    amplitudes = √3·S₀₀·(qd(27), qd(351′), qd(351)) = a permutation of {A1,A2,A3}, FORCED
    by the current relation + the three orbit quantum dimensions being distinct.
H4. Uniform phase: arg S_{a_i,a_j} ∈ (π/3)ℤ (specifically ±π/3, ±2π/3) for all i,j, so
    |Im S| = (√3/2)|S| uniformly (the ℤ/3 current spin h_J = 4/3 ≡ 1/3).
H5. 3-valued |S|: |S_{a_i,a_j}|/S₀₀ takes only the three quantum-dimension values
    {1, qd(27), qd(351)} (ℤ/3-orbit constancy of |S|).
H6. Unique completion: symmetric + each row a permutation of {A1,A2,A3} + current
    row = (A2,A3,A1) ⟹ the Latin square [[1,2,3],[2,3,1],[3,1,2]] is the UNIQUE completion.

## MB12 — the criterion can pass AND fail
- CAN resolve-A: if H1–H6 all verify exactly and H6's completion is provably unique,
  the Latin square is forced ⟹ THEOREM.
- CAN resolve-B: if the arrangement is NOT forced (e.g. the completion is non-unique, or
  the current row is not the qd-vector, or |S| is not 3-valued), the Latin structure is a
  coincidence of this particular data ⟹ RESOLVED-B.
- CAN be UNRESOLVED: if the reduction/current-row hold but the completion cannot be pinned
  from fusion data alone (a genuine residual modular input remains open).

## B774 chord discipline (binding)
The θ-odd object B must be genuinely non-abelian to be more than a relabeled character:
self-test — B has order 4 (B⁴ = I, spectrum {i,−i,−1}), so B² ≠ I; the θ-odd 3-space
carries a genuine order-4 operator, NOT a ℤ/2 reflection. The Latin square itself is an
ABELIAN (ℤ/3 simple-current) arrangement fact; the theorem correctly attributes the
ARRANGEMENT to the abelian center while the VALUES A_k remain the transcendental modular
qd-data (ℚ(ζ₇)). No non-abelian claim is made about the Latin square. Checked in-cell.

## Discriminating fact (computed in-cell, never cited)
The 351′-row of the amplitude matrix equals √3·S₀₀·(qd(27), qd(351′), qd(351)) exactly,
i.e. (A2, A3, A1) — the current relation forces one full row/column to be a permutation of
{A1,A2,A3}; unitarity + symmetry + 3-valuedness then force the unique Latin completion.

## Gate 5/5-Q
Structural only. No SM values, no consciousness vocabulary, nothing to CLAIMS, the
one-number pin untouched. Exact/symbolic preferred; positive reproduced a second way
(direct on B via H1, and via the |S|-Latin ⊗ uniform-phase decomposition).
