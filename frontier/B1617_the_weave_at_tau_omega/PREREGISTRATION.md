# B1617 — PREREGISTRATION: THE WEAVE AT τ = ω — given the owner's tagged postulate τ = ω, the residual symmetry the choice leaves, the matter triplet's charges under it, and the mass terms it allows at ω and near it

cc (main), 2026-10-08, after S94. **The owner ruled on 2026-10-08 (in this session): the fibre's modulus τ = ω is a tagged
working postulate**, results "given τ = ω", the choice formally open. Choosing τ breaks the weave's symmetry to the
automorphisms fixing τ: the order-3 elliptic class with −I, and every inner automorphism. This arc computes that residual
group on W10's V, the triplet T under it, and the mass terms it allows. **Sealed before `weave_at_omega.py` runs.** No
data is read. A READING throughout ("given τ = ω", "given Λ"). 0 of 19.

## Seen first

`VERDICT topic-sweep /modulus|orbifold point|elliptic point|fixed point of|residual symmetr|near the fixed|stabili[sz]er of/: 35 of 1388 arcs on main match (NEGATIVE 6, OPEN 5, PROVED 23, RETRACTED 1)` — B1611–B1616 (the weave's group fixes no flavour value), B1612 (the residual subgroups RL, RRL), W19–W21
(the weave's object M₁,₂; the holomorphic triplet T), B1601 and the seat's note (LR ≡ ST mod 2, the rotation fixing ω;
the common point is the geometry mod √−3). **Literature:** the stabilisers of PSL(2, ℤ) at i and ω; the residual-symmetry
mechanism near fixed points (Novichkov, Penedo, Petcov, "fermion mass hierarchies from modular symmetry near fixed
points") — cited from the reviewer's knowledge; Z4 imports only its statement that entry powers of ε = τ − ω are set by
residual-charge differences, tagged.

## Disclosed

- The predictions are reasoned: inner automorphisms act trivially on τ and, at the common point, should act on V by the
  parity signs; if they do, the residual group contains the parity grading and T splits into its three parity lines.
- The instrument was cleaned before the seal (a dead stub removed; an order function made dimension-general).
- The convention linking an automorphism's H₁ matrix to its action on τ is checked in Z0 (all three candidate actions are
  reported); all order-3 elliptic elements are conjugate in PSL(2, ℤ), so the charges do not depend on which one is used.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **Z0** | an automorphism with H₁ matrix U = [[0, −1], [1, 1]] exists as a short word in L, R and their inverses, and U fixes ω under at least one of the three actions; the move matrices compose in one consistent order | 95% |
| **Z1** | the residual group (U, ι, conjugation by a, by b) is finite and preserves T; the inner automorphisms act on V as diagonal parity signs | 70% |
| **Z2** | T splits under the residual group into three one-dimensional pieces with distinct characters | 60% |
| **Z3** | at exactly ω the Dirac mass term allows three free couplings (diagonal in T's lines) and no fixed relation among the masses; the Majorana term allows at most one coupling | 55% |
| **Z4** | U's lift has three distinct eigenvalues on T; the charge differences are non-zero — the near-ω mechanism would give every off-diagonal entry a positive power of ε | 60% |

**The reading, written before the run (the cells can only lower it).** If Z1–Z3 hold: τ = ω fixes the mass *basis* (the
three parity lines) and no mass value — masses are three free couplings per sector at ω, like the residual vacua of B1615.
What τ = ω adds is the charge pattern (Z4) that a near-ω deformation would turn into hierarchies; the depth ε = τ − ω would
be one more parameter. So given τ = ω the flavour values are still not derived; the next question would be what fixes ε.

## Instruments

`verification/weave_at_omega.py`; hashes in `ARTIFACT_HASHES.txt`.
