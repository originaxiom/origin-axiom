# B1447 — THE BRANCH: at the real branch point an irreducible family of rank-three flat connections leaves one member's Higgs curve; on it the three states of a family triplet carry three different eigenvalues; and it has a boundary-parabolic point

cc, 2026-10-02. B1446 located where a second member's Higgs can be switched on along the first member's curve: six
algebraic points on the root's three-fold cover, one of them on the arc of real representations. Lead L237 (a)
asked whether a family of flat connections actually leaves there, and what sits on it. This arc answers on that
level. **Verdict: PROVED** (computed at 60 digits; one level; no population, so no seal).

## 1. The block representation and the question

At a point of the first member's curve where the doubly matched sector D = ρ ⊗ a has a class, put b = a³, c = a² (so
b/c = a and b²c = 1) and R₀ = (ρ ⊗ b) ⊕ c, meridian T ⊕ 1: a representation of the level into SL(3) whose
off-diagonal blocks are D and its dual. The linearised relator equations dG at R₀ (18 equations, 27 unknowns) give

| point of the curve | rank dG | kernel | coboundaries | h¹ | h² | classes in the upper / lower block |
|---|---|---|---|---|---|---|
| generic (u = −0.7) | 17 | 10 | 7 | 3 | 1 | 0 / 0 |
| the real branch point (u = −0.62070…) | 15 | 12 | 7 | 5 | 3 | 1 / 1 |

so h¹ jumps by two there, one class in each block, as B1446 found from the torsion.

## 2. The second-order obstruction vanishes

A first-order deformation u₁ extends to second order exactly when G(εu₁)/ε² lies in the image of dG. With one
class on, the second-order term is zero (the block squares to zero). With both on it has norm 10.4 and its distance
from the image of dG is 3.6·10⁻¹⁴ (ε = 10⁻¹⁴): **in the image.** The same for the other doubly matched sector
(10.3; 6.4·10⁻¹⁴).

**And at all six branch points** (`all_branch_points.py`): at each of the six roots of B1446's sextic, for both
signs of Z and with the sector and the sign of the meridian found there, h¹ = 5, h² = 3, one class in each block,
and the second-order term (norms 10 to 320) lies in the image of dG to 8·10⁻¹⁴ or better. The obstruction
vanishes at every one of them.

## 3. The branch exists and is irreducible

Gauss–Newton on the relator equations, started at R₀(1 + s(c₊ + φc₋)) for s = 0.02 … 0.2 and φ = 1, i, converges to
exact representations (residual 10⁻⁴⁸ to 10⁻⁶⁰) with both off-diagonal blocks non-zero, whose matrices span all of
M₃(ℂ) (dimension 9, against 5 at R₀): **irreducible flat connections of rank three of the level, with the other two members' Higgs both switched on (the two new classes are the sectors of the second and of the third member; one alone gives only a reducible, non-split representation).** At them rank dG = 16, kernel 11, coboundaries 8: h¹ = 3 for gl₃, 2 for sl₃ — a two-dimensional family.

## 4. The family link is structural

In a deck orbit of three the Higgs characters η₀, η₁, η₂ have trivial product, and so have the three extension
characters. The characters of a triplet of the rank-three group through member 0's coupled pair are
α_A⁰, α_A⁰/η₀ = 1/β_B⁰ and a third, α_A⁰·η₂ (or its analogues). **The third is a sector character of another
member:** counted over the four candidate thirds per coupling,

| three-fold level | fibre torsion | characters that are sector characters of members 1, 2 | thirds among them |
|---|---|---|---|
| +LR 3 | 16 | 12 of 15 | up 2 of 4, down 4 of 4, all 16 orbits |
| +LLR 3 | 50 | 16 of 49 | 2 or 3 of 4, all 16 orbits |
| −LLLR 3 | 112 | 12 of 111 | up 2 of 4, down 4 of 4, all 16 orbits |

On −LLLR 3 chance would give about one in nine. So the Higgs characters of an orbit act as roots of a rank-three
group and the members' matter characters are weights of its triplets. (On −LR 3 the products are not trivial and
half the orbits have one Higgs character for all three members; the statement is for the levels above.)

## 5. Three different eigenvalues along the branch

For a triplet V = R ⊗ χ the monodromy acts on H¹(F; V), of dimension three. At R₀ its eigenvalues are e, 1/e, 1 —
the first member's lifted pair and a state of another member, not lifted. On the branch (χ trivial; |log| of each):

| s | lightest | the pair |
|---|---|---|
| 0 | 0 | 1.4234, 1.4234 |
| 0.02 | 0.0014 | 1.4223, 1.4236 |
| 0.05 | 0.0092 | 1.4164, 1.4250 |
| 0.1 | 0.0367 | 1.3949, 1.4298 |
| 0.2 | 0.1510 | 1.3027, 1.4490 |

The lightest grows as 3.6·s² and the pair splits by the same order. **This is the first configuration in the record
in which the states belonging to different members of a deck orbit carry different numbers**, and the small one
is small because the other two members' Higgs are only partly on.

## 6. A boundary-parabolic point on the branch

Imposing that the meridian have a single eigenvalue (two conditions on the two-dimensional branch), by homotopy
from 32 starting points of the branch (s = 0.1, 0.2, 0.3, 0.45 and eight phases; `search_parabolic.py`) and
polishing: **22 of the 32 arrive at the same point** (tr R(x) agreeing to 30 digits, the same spectra; they differ
only by the scalar on the meridian), and the other ten stall short of the target without reaching another. It is a
representation with relator residual 10⁻⁵⁹, **irreducible** (dimension 9),
**longitude a regular unipotent** (tr = 3, rank(λ − 1) = 2) and **meridian a scalar times a regular unipotent**.
Record `parabolic_point.json`. tr R(x) = 2.80915567…, tr R(y) = tr R(xy) = −1.24109544… − 2.14946232… i.

At it every one of the 16 triplets R ⊗ χ has an eigenvalue equal to 1 to 10⁻⁵⁸ — the class the cusp forces — and
a pair e, 1/e with e + 1/e real: 1.7311, 1.7442, 1.7819, 1.8674, 1.9006, 2.1978, 2.2685, 2.7481, 8.0137, 43.436
(|log e| from 0.317 to 3.771). So at the pinned point the three eigenvalues of §5 close up again into a zero and a
pair, and the pairs differ from triplet to triplet.

So on what was searched the branch has one boundary-parabolic point; that it has no other is not proved.

**The index there is zero, and these modules are not self-dual** (`triplet_index.py`). The vanishing of the class
index on irreducible modules has so far been seen only for a self-dual representation twisted by a cusp-trivial
character (the unproved theorem of B1329–B1332; B1446's bidoublets are of that kind). A triplet R ⊗ χ is not: for
each of the 16 the equation X·V(g) = V*(g)·X has only the zero solution. Their class index at the parabolic point,
by singular values at 60 digits (smallest kept 0.26, largest dropped 2·10⁻⁵⁹): **boundary invariants 1, h¹ = 1, no
interior class, for the module and for its dual — index 0, on 16 of 16.** So the one irreducible, boundary-unipotent,
non-self-dual background constructed in the record does not carry the frame's index either.
The point was refined to 229 digits (Newton converges quadratically there). tr R(x), a real number, satisfies no
integer polynomial of degree at most 24 with coefficients below 10⁶ (`identify_field.py`, run stopped after the
first invariant): the point is algebraic, being an isolated solution of polynomial equations, and its field is not
identified.

## 7. The eigenvalues behind B1446's torsions (lead L237 (d))

A torsion 2 − E hides a pair e, 1/e with e + 1/e = E. At the parabolic points of B1446:

| torsion | E | e | \|log e\| |
|---|---|---|---|
| −√5 − √−3 (the generation's sectors at the complete cusp) | 2 + √5 + √−3 | 4.0302 + 1.8253 i, modulus 4.4243 | 1.5467 |
| √5 + √−3 (the unmatched sectors there) | 2 − √5 − √−3 | −0.0406 + 0.4538 i, modulus 0.4557 | 1.8367 |
| 4 (each factor of the 16 at the quaternion point) | −2 | −1 | π |

At the complete cusp the pair is not on the unit circle (the representation is not unitary there); at the
quaternion point the eigenvalue is −1, half a turn.

## 8. What it means, and the fence

- **Where the members of an orbit differ has been found, on one level:** not at the symmetric points, where the
  deck symmetry makes them equal, but on a branch that leaves one member's Higgs curve at a specific algebraic
  point and on which the other two members' Higgs are switched on. The difference has a mechanism and a small parameter.
- **Imported expectation, stated separately:** that the pinned point would carry three distinct non-zero values.
  It carries a zero and a pair for each triplet. The three-fold difference lives along the branch; the pinned
  point of this branch that was found does not show it within one triplet.
- **The fence:** one level, one branch point of six, one parabolic point found; eigenvalues of a monodromy are not
  masses; which group of the frame contains two members' Higgs directions as non-commuting roots is still not
  established (L235 (b)) — the rank-three representations exist as representations of the level whatever the answer,
  but their reading as the frame's Higgs configurations depends on it. **0 of 19.**

## 9. Not computed (lead L237)

The branches at the other five branch points beyond second order (the obstruction vanishes there too; no
representation was constructed on them); the complete set of parabolic points of this branch; a third member's Higgs (a
further branch); the number field of the parabolic point; the same on other three-fold levels.

## Verification

`verification/branch_obstruction.py` (the linearised relators, the classes in the two blocks, the second-order
test), `branch_follow.py` (the Gauss–Newton construction, the Burnside test), `family_link.py`,
`triplet_spectrum.py`, `branch_parabolic.py` and `search_parabolic.py` (the homotopy to a single eigenvalue of the
meridian, eight records), `all_branch_points.py`, `triplet_index.py`, `identify_field.py` (its run record is partial: stopped after tr R(x));
the point itself in `parabolic_point.json` (58 digits). All on
B1444's `curve_engine.py` and B1445's `mass_term.py`. Lock: `tests/test_b1447_the_branch.py`.
