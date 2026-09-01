# The A6 fork, adjudicated independently — fresh physics seat, 2026-09-01

*The question as posed to me: was A6 — replacing the det = −1 half-step with its square,
i.e. passing to the orientation double cover (Gieseking m000 → figure-eight m004) — the
right branch? I was told not to inherit the asking seat's framing. I re-ran everything.*

## What I verified (script: `computations/verify_fresh_seat.py`)

1. m000 is the Gieseking manifold (nonorientable, vol = ½·vol(m004)); its orientation
   double cover is isometric to m004. **[computed-here]**
2. The arithmetic route to E₆ runs **identically** on the pre-squaring object: shape field
   ℚ(√−3) both sides; π₁(m000) and π₁(m004) each have exactly **72 homs and 48 surjections
   onto SL(2,3) = 2T**. **[computed-here]** (The seed's claim checks out.)
3. Orientation double covers of the first 40 nonorientable census manifolds are
   amphichiral **40/40**; the orientable-census base rate is 7/300 ≈ 2.3%. **[computed-here]**
4. **The 40/40 is a theorem, not a statistic:** the nontrivial deck transformation of an
   orientation double cover is orientation-reversing by construction, and Mostow rigidity
   makes it an isometry — so *every* hyperbolic orientation double cover is amphichiral,
   with the mirror self-isometry being precisely the deck involution. **[argued]** B605
   already computed the instance (the amphichiral involutions of m004 ARE the Gieseking
   deck transformations) without drawing the general corollary.

## My verdict: A6 is not a fork. It is the observer's first closing, mislabeled as an axiom.

Three parts:

**(a) Nothing arithmetic hinges on A6.** Trace field, 2T count, hence the entire
ℚ(√−3) → 2T → E₆ chain, are commensurability-class invariants, and m000 and m004 are in
the same class (the double cover is the commensurability). Dropping A6 does not open the
chirality door: the Gieseking has no orientation *at all*, so there is still no canonical
handedness — the wall moves from "the mirror is a self-isometry" to "there is no mirror
because there is nothing to reflect," which is the same underdetermination stated more
honestly. **No door opens on the other branch.** The seed's suspicion that A6 might be
"the wrong branch" resolves as: there is no branch with different physics on it.

**(b) What A6 actually costs is a confusion the record has been paying interest on.**
Squaring *manufactures* an object with an orientation and a mirror symmetry, and the
programme then spent real effort treating amphichirality as a discovered depth ("the
object is swap-symmetric; the observer breaks the swap"; amphichirality as one of the
sieve filters pointing at 4₁ in P10). By (4) above, the mirror self-isometry is the
residue of the covering choice — the swap-symmetry is the memory of the forgotten sheet.
Every "wall" that traces to the mirror being a self-isometry traces, one step further
up, to A6 itself. The asking seat's afternoon reading was correct on this point, and I
confirm it independently.

**(c) The repair is a relabeling, and it strengthens the programme's own thesis.** The
record's observer doctrine (B717: the object supplies incompletenesses; the observer
supplies closings) *already contains the right category for A6*: on the Gieseking side,
"orientation" is literally a choice of sheet of the double cover — an observer closing in
exactly the B717 sense, and visibly the same act as the chirality bit (B713's Galois-sheet
choice) and cousin to the C/P relational bits Review 53 distilled. Concretely:

> Take the **Gieseking manifold** (equivalently: the commensurability class) as the
> object. Demote A6 from axiom to **the first closing**: the observer orients. The
> figure-eight complement is then not the object but *the object as seen by an oriented
> observer* — and its D₄ symmetry, its amphichirality, its CS = 0, and the c-as-swap
> motif all become theorems about that closing (deck-transformation residue) instead of
> mysteries about the object.

This (i) removes the FRAGILE label from the fork by dissolving the fork, (ii) shortens
the input ledger's story (orientation stops being an unexplained axiom and joins the
closings, where B1083 already put the P-bit), and (iii) makes the amphichirality
literature honest: it is *forced*, and the record should say by whom.

**Cost check (the tools).** Chern–Simons, complex volume, and SL(2,ℂ) representation
theory do need orientation — but they need it as *inputs of the oriented observer's
description*, which is exactly where the relabeling puts them. Nothing breaks; the
PGL-vs-PSL point the record already banked (B1112: the canonical holonomy is projective;
the SL(2,ℂ) lift is a spin-structure choice) is the same move one storey up. CS(m004) = 0
stops being a striking vanishing and becomes what it is: the value pinned by the deck
involution.

## Pre-registered falsifiers of this verdict (stated before I computed)

- If the 2T surjection counts had differed between m000 and m004, or the shape fields had
  differed, A6 would be arithmetically load-bearing → verdict fails. (They did not.)
- If some downstream structural result provably requires the *knot-complement* property
  in a way no closing-relabeling can absorb, the relabeling must keep A6-as-closing
  *prior* to invoking it: being a knot complement in S³ is a property of the oriented
  representative (Reid's uniqueness speaks of knots), even though H₁ = ℤ itself holds on
  BOTH sides (m000 and m004 both have H₁ = ℤ — checked **[computed-here]**, which in fact
  *strengthens* the relabeling: the one census separator B1136 found survives the descent
  to the nonorientable object). I checked the chain's use: B1136's separator is used for
  rank-preservation structurality (B955), which lives after orientation. The order of
  operations survives; flagged for any future arc that leans on S³ itself.
