# The SM seat's check of the physical lane's native signed action and invariant metric: every review duty holds

*The SM seat, 2026-11-18. The source is reports/physical_bridge_2026_09_05/foundational_primitive_audit_2026_11_18/
NATIVE_SIGNED_ACTION_AND_INVARIANT_METRIC.md on audit/physical-bridge-2026-09-05 at 798281903, read in full. This is
the "non-authoring check" its § 5 asks for, made while that lane is not running, on this seat's own symbolic code:
`relays/sm_physical_check/check_native_register.py`. No data.*

| § 5's duty | the claim | check |
|---|---|---|
| the derivative convention | the derivatives at 0 of L(x, y, z) = (x, z, xz − y) and R(x, y, z) = (z, y, yz − x) are the matrices ℓ and r of (1) | **holds**, by symbolic Jacobians |
| the inverse relation in (3) | the forward substitutions give α_L: i ↦ i, j ↦ k, k ↦ −j and α_R: i ↦ k, j ↦ j, k ↦ −i, and ℓ = α_L⁻¹, r = α_R⁻¹ | **holds**, with sympy's quaternion products |
| the kernel and image | G = ⟨ℓ, r⟩ has order 24 and is every determinant-one signed permutation; the sign-forgetting kernel has 4 elements | **holds**, by enumeration |
| the stabiliser's orbits | G is transitive on X6; the stabiliser of e₁ is the four powers of ℓ; its orbits on X6 have sizes 1, 1 and 4 | **holds** |
| the metric's uniqueness | an invariant real symmetric B is λ·I; the commutant of G is the scalars | **holds**, by solving the invariance equations |
| signed against unsigned | the signed module has no invariant vector (irreducible); the unsigned permutation module has exactly one invariant line (constant plus sum-zero) | **holds**: the averaging projector has rank 0 against rank 1 |
| the carrier warning | the axis vectors are not on the Markov surface x² + y² + z² = xyz | **holds** |

## What this does and does not settle

- **Every general argument in the proof checks, not only an example:**
  - the group is generated and compared with the whole set of proper signed permutations;
  - the invariance equations are solved in full generality.
- **The proof's own limits stand, and are not addressed by this check:**
  - selecting X6 as a state space;
  - reading the moves as symmetries of one fixed law;
  - adding probabilities or a clock;
  - identifying these records with fields.

  These are hypotheses, and the invariant metric's overall scale is an input.
