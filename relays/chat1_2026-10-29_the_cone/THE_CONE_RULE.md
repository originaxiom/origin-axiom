# THE CONE AND THE SIGN — the rule, committed before the script exists

chat1 (the web seat), 2026-10-29, at the owner's word the same evening ("yes please. deriving physical spacetime would
be progress"), after this seat's answer that the record half-holds a canonical 3+1 vacuum spacetime (B1708) and
half-denies it (B716). Data-free. 0 of 19.

## What this is, and what it is not

- **It is** an exact check of classical facts on the record's own object, so that a relay to main can propose:
  - re-scoping B716's "4-dimensionality and Lorentzian signature are the observer's";
  - re-scoping B97's "not on the geometric side";
  - an answer to P-282 ("does any structure the moves keep fix the relative sign of the time and space terms?").
- **It is not** a derivation of physical spacetime. The cone is a vacuum, without matter or scale. Calling it ours is an
  identification, and this rule does not earn it.
- **Every fact checked here is classical:**
  - PSL(2,ℂ) ≅ SO⁺(3,1) through Hermitian matrices;
  - the hyperboloid model of H³;
  - the Milne universe;
  - SL(2,ℝ) ≅ SO⁺(2,1) through binary quadratic forms and the discriminant.

  The priors are high for that reason, and an outcome below them would mean a slip in the script or in this seat's
  reading, not news.

## Seen first (main at 2a4635a15; full text; cut before the lists of other lanes)

- `VERDICT topic-sweep /spacetime|space-time|Lorentzian|Milne|physical time|arrow of time|FLRW|Friedmann|cosmolog|Einstein equation|Ricci.flat|3\+1|four.dimensional spacetime|emergent (space|time)/ (full text): 136 of 1561 arcs on main match (NEGATIVE 37, OPEN 12, PROVED 87); 12 register rows match (DONE 4, QUEUED 8)`
- `VERDICT topic-sweep /discriminant.{0,40}(signature|Lorentz|Minkowski|time)|binary quadratic form|hyperboloid|Hermitian matri|SO\(3, ?1\)|SO\(2, ?1\)|Lorentz group|velocity hyperboloid|light.?cone|spacetime sign/ (full text): 25 of 1561 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 21); 1 register rows match (QUEUED 1)`
- **Read for this rule:**
  - B716's FINDINGS. Its probe 2 searched 4d *fillings*, an H⁴ filling and a CH² structure. Its probe 3 searched Wick
    rotations of H³. It did not consider the cone.
  - B97's FINDINGS: the (2,1) Killing form of sl(2,ℝ) on the Teichmüller component, "not on the geometric side".
  - B1708's verdict line and FINDINGS: the cone is Ricci-flat iff the curvature is −1; it names the Milne universe.
  - The verdict lines of B96, B981, B1104, B1114 and B1134 (Lorentz inside E₆, a different route), and of P-282, P-289,
    P-439 and P-443.

## The object's holonomy (inputs, stated before the script)

- **Riley's representation of the figure-eight knot group,** with ω = e^(2πi/3) and entries in ℤ[ω]:
  x ↦ [[1, 1], [0, 1]], y ↦ [[1, 0], [−ω, 1]], with the relation w x = y w, where w = x⁻¹ y x y⁻¹.
  - If this relator fails exactly, the script reports it, and the cells run on SnapPy's holonomy of m004 (numerical)
    alone.
  - Disclosed: the relator's form is quoted from memory, and cell S1a checks it.
- **A second source:** SnapPy's `Manifold('m004').fundamental_group().SL2C(g)` for its generators, numerically.
- **A control of genericity:** m003 (the sister manifold, also of least volume) through SnapPy.

## The cells (the priors fixed now)

| cell | statement | prior |
|---|---|---|
| S1a | Riley's matrices satisfy w x = y w exactly in SL(2, ℤ[ω]) (or with −I) | 85% |
| S1b | for each generator A (Riley's and SnapPy's), the map X ↦ A X A† on Hermitian 2×2 matrices, written in the basis (I, σ₁, σ₂, σ₃), is a 4×4 real matrix Λ with Λᵀ η Λ = η for η = diag(1, −1, −1, −1), det Λ = +1 and Λ₀₀ ≥ 1: an element of SO⁺(3,1) (exact for Riley's, 10⁻⁹ for SnapPy's) | 97% |
| S2 | in hyperbolic-slicing coordinates X = t (cosh r, sinh r sin θ cos φ, sinh r sin θ sin φ, sinh r cos θ), the Minkowski metric is exactly −dt² + t²(dr² + sinh²r dΩ²), the cone over H³ (B1708's metric, with g of curvature −1); t² = det X | 99% |
| S3 | the arrow: X ↦ −X commutes with every Λ and swaps the two halves of the light cone. Complex conjugation of entries, an orientation-reversing isometry of H³, acts with det −1 and Λ₀₀ = 1, so it keeps each half. No isometry of space reverses the cone's time | 97% |
| S4 | the 2+1 half: L = [[1,0],[1,1]] and R = [[1,1],[0,1]] act on binary quadratic forms (a, b, c) by substitution and preserve the discriminant b² − 4ac. That form has signature (2,1). LR's invariant form is x² + xy − y² up to sign and scale, of discriminant 5 > 0 (spacelike), and the cusp forms (discriminant 0) are null | 95% |
| S5 | that 2+1 form is B97's: the map from sl(2,ℝ) to forms intertwines Ad with the action on forms and carries the Killing form to a multiple of the discriminant | 90% |
| S6 | sl(2,ℂ) as a real Lie algebra has Killing form of signature (3,3), not (3,1). So the 3+1 Minkowski form lives in the *vector* representation of S1b, not in the adjoint, which is why B96 and B97 did not see it on the geometric side | 92% |
| S7 | the control: m003's generators (SnapPy) also land in SO⁺(3,1) by S1b's test. The construction is generic, as B1708 says | 97% |

## What the outcomes mean (fixed now)

- **S1–S3 hold.** Given m004's hyperbolic structure, which Mostow fixes up to conjugation and orientation, the object
  carries a canonical flat 3+1 Lorentzian spacetime, the Milne cone over itself.
  - Its signature and its time coordinate are fixed by the group; only the arrow (one bit, S3) and the unit are not.
  - B716's clauses on 4-dimensionality and signature are then over-scoped. Its clauses on fillings, Wick rotations and
    the arrow stand.
  - The label to propose: FORCED, as mathematics, with that scope. "Physical spacetime" stays an identification,
    UNEARNED.
- **S4 and S5 hold.** The moves keep a form of signature (2,1). P-282's answer in 2+1 is then already B97's, read as
  the discriminant. Whether that is what P-282 asks is main's ruling.
- **S6 holds.** B97's "not on the geometric side" is right for Killing forms and Hessians, and over-scoped for the
  group's action.
- **S7 holds.** The cone does not single out m004. Nothing here bears on the 19.
- **Any cell fails.** It is reported bare, with what it means for the proposal, before the relay is written.

## Discipline

- `cone_checks.py` is committed before its run, its helpers checked only on synthetic inputs.
- Its outputs are committed unread, then read.
- A failed launch is kept and disclosed. Any later check is labelled post hoc.
- One read-only referee before the relay is pushed.

0 of 19.
