# PRICED LEDGER — the TRUE quantum child: the E6 RT invariant of 4_1(5,1)

**Status: NEEDS-SPECIALIST.** Track (iii) of the SEALED prereg `d3_child/PREREG_D3.md` (sha 75d69af3).
This is a text-only feasibility/cost assessment — nothing here is executed as a claim, and it prices
exactly the gap that track (i) (`d3i_results.json`, `d3i_run.log`) does not reach: track (i) banked the
CLASSICAL invariants of the child manifold (volume, Chern-Simons, geodesics, homology); this ledger
states what the QUANTUM child — the E6-colored Reshetikhin-Turaev (RT) invariant of the closed
hyperbolic 3-manifold 4_1(5,1) — would additionally require, and why it is out of reach in-house.

## What "the true quantum child" means

4_1(5,1) is (5,1)-Dehn surgery on the figure-eight knot in S^3. Its E6 RT invariant Z_{E6,k}(4_1(5,1))
is computed by the standard surgery formula (Reshetikhin–Turaev 1991): present the manifold via a
framed knot (4_1, framing 5), choose the modular tensor category built from the E6 quantum group at
level k, and sum the knot's colored invariant over every admissible color, weighted by the twist
(framing) and quantum-dimension data:

    Z_k(4_1(5,1))  ~  (framing/signature normalization) x  Sum_a  J_a(4_1) * theta_a^5 * S_{0a}

— where `a` ranges over the level-k admissible E6 weights, `J_a(4_1)` is 4_1's own colored invariant
at color `a` (built from the E6 R-matrix / braiding data of the actual knot diagram), `theta_a` is the
ribbon twist eigenvalue, and `S_{0a}` the quantum dimension. **`J_a(4_1)` is the missing, load-bearing
piece** — everything else (twists, quantum dimensions) is bookkeeping once the color set is fixed.

## What computing J_a(4_1) requires

**Route A — colored R-matrix / cabling.** 4_1 is the closure of the 3-strand braid
sigma_1 sigma_2^{-1} sigma_1 sigma_2^{-1} (4 crossings). Coloring by an E6 weight `a` means: build the
finite-dimensional U_q(e6)-module V_a, construct the universal R-matrix's action on V_a (x) V_a from the
ribbon-Hopf-algebra data (Casimir/twist eigenvalues on each isotypic summand of the tensor-square,
via Freudenthal/Brauer–Klimyk weight multiplicities), represent the braid group on this space, close the
braid (quantum trace) to get J_a(4_1), then repeat for every color up to level k and assemble the sum
above. This needs full quantum-group representation theory for E6 (weight multiplicities, tensor-product
branching, the universal R-matrix, ribbon twists) — none of which reduces to a simple SL(2) cabling,
because E6 is an **exceptional** Lie algebra with no SL(N)-style skein/HOMFLY shortcut.

**Route B — E6 Kashaev-type state-integral analog.** The prereg's alternative: generalize the
Andersen–Kashaev quantum-dilogarithm state integral (the SL(2)/A1 construction whose classical limit
recovers vol(4_1), already verified in-house feasible for SL(2), `frontier/physics_probes/kashaev_feasibility.py`)
to an E6 analog. The repo's own `speculations/S026_3d3d_state_integral.md` (read for this ledger) already
flags the **next** rank up — **SL(3)**, i.e. one step past SL(2) — as HEAVY/DORMANT: *"the state-integral
needs the quantum dilogarithm machinery and a careful contour/saddle analysis — research-level, not a
bounded probe; the SL(n>=3) state-integral is at the frontier of the field."* E6 (rank 6, exceptional,
not even in the SL(N) classical series S026 was already declining to pursue) is well beyond that stated
frontier; to our knowledge no published "E6 state-integral" construction exists at all — this route may
not just be expensive, it may not yet be a *defined* object in the literature.

## Rough size estimates

- **E6 data:** rank 6, dimension 78, 72 roots, Coxeter number h = dual Coxeter number h^v = 12, Weyl
  group order 51,840. Smallest nontrivial irreps: 27, 27bar (minuscule fundamentals), adjoint 78, then
  351, 351', 650, 1728, 2925, ... — representation dimensions climb fast with weight.
- **Level-1 fusion rank = 3** (colors {1, 27, 27bar}, c=6) — this repo already computed E6 level-1
  modular data correctly (`frontier/B569_complete_chain/e6_level1_modular.py`, read for this ledger).
  Level-2/3 fusion rank (the number of colors the surgery sum must run over) is already dozens, growing
  combinatorially with k for a rank-6 algebra (Weyl-alcove counting) — nothing like SL(2)_k's `k+1`.
- **R-matrix size:** even the smallest color (27) needs a linear map on a 27x27 = 729-dimensional space
  per crossing (4 crossings); non-minuscule colors reach representations of dimension in the hundreds to
  tens of thousands, so most of the level-k color sum is computationally heavy even *given* the R-matrix
  construction — and that construction is the hard, missing part, not an engineering afterthought.
- **Software gap:** SnapPy (used for track (i)) has zero quantum-invariant machinery — it is purely
  hyperbolic-geometry/triangulation software. We are aware of no existing package that computes colored
  RT invariants for an exceptional Lie algebra at arbitrary rank/color for a general knot; this would be
  built from scratch. By contrast, the SL(2) Kashaev sum for 4_1 is a single finite sum of N terms,
  already coded and verified in-house (`kashaev_feasibility.py`, `frontier/B384_kashaev_bridge/`).
- **Effort class:** multi-week-to-multi-month specialist research (quantum-group representation theory +
  Reshetikhin–Turaev surgery bookkeeping), not a bounded compute cell — and a clean execution would
  likely itself be a publishable result, not a routine evaluation.

## Why the banked Sol-bundle operators do NOT suffice (the prereg's correction)

Track (ii)'s banked operators (S, T diag exponents from the counts `.npz`, used in the identity
`Tr(T^n rho) = Sum_a t_a^(n+3) S_aa`, cf. `frontier/B569_complete_chain/e6_level1_modular.py`) compute
the E6_k WZW invariant of **closed torus bundles** — mapping tori of SL(2,Z) elements acting on the
*closed* torus T^2 (Sol/flat/elliptic 3-manifolds, depending on trace). This is a self-contained
2d-CFT/modular-data computation: it depends only on the mapping-class-group word (via S and T), and
carries **no information about how a knot is embedded or knotted**.

4_1(5,1) is a different kind of object entirely: a Dehn filling of the cusped, once-punctured-torus-bundle
knot complement 4_1, and its RT invariant needs `J_a(4_1)` — the colored braiding invariant of the actual
knot diagram (Route A/B above). No manipulation of the banked S/T data can produce this: S and T supply
only the twist/quantum-dimension bookkeeping in the surgery formula above, never the knot-colored term.
This is exactly the correction stated at the top of the sealed prereg: *"our banked Z is the SOL
TORUS-BUNDLE invariant (mapping torus of T^2), not the cusped 4_1 complement's colored theory."* Track
(i) and track (ii) both stand on their own; neither one's banked numbers assemble into the quantum child.

## Verdict

**NEEDS-SPECIALIST** (house convention, cf. `CLAIMS.md` P10/C8, `papers/SPECIALIST_NOTE_R1_held_breath.md`).
The true quantum child is well-defined in principle (the RT surgery formula above is standard), or lies
along an open research construction (Route B); either way it requires quantum-group / TQFT expertise this
seat does not have and cannot bound as a cheap probe. Nothing here is claimed as a result; this is a cost
estimate for the owner/cc to weigh against the project's standing "NEEDS-SPECIALIST" queue.

Anchors read for this ledger (no repo writes; read-only per seat rules): `knowledge/K006_3d3d_correspondence.md`,
`speculations/S026_3d3d_state_integral.md`, `frontier/B569_complete_chain/e6_level1_modular.py`,
`frontier/physics_probes/kashaev_feasibility.py`, `CLAIMS.md`.
