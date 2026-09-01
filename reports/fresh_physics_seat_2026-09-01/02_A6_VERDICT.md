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

## Second pass: the verdict stress-tested against the record's newest arcs (B1224–B1232, R021)

Run after the full corpus read, deliberately hunting the counter-case.

**(1) "Every wall traces to amphichirality" — the seed's framing — is OVERBROAD, and I
reject it explicitly.** My own wall-tracing over the full record:
- Walls with genuine A6/mirror ancestry: the chirality/orientation underdetermination
  (B713/B1163/B1183 — the one-class theorem), CS ∈ 2-torsion (B1224), the CP-sector
  bit-structure (B303/L192), the c-as-swap motif.
- Walls **without** mirror ancestry: the **scale wall** (Mostow rigidity + the scale-torsor
  theorem Hom(G,ℝ⁺)=0 — no mirror anywhere in either proof); the **value walls** (the type
  law B1032, the exhaustive disjointness B1126/B1129/B1137, and now B1225's selector
  theorem, which is about invariance in general, not the mirror); the **generation
  obstruction** (trace-field degree, B298/B307); the **rank wall** (semisimple centralizers
  preserve rank, B952 — pure Lie theory).
So A6 organizes the *chirality/CP corner* of the boundary, not the boundary. My verdict
(A6 = the first closing, mislabeled) stands, but its blast radius is that corner.

**(2) The record's own B1224–B1227 sharpen, and partly discipline, my amphichirality
theorem.** Amphichirality forces a mirror-odd invariant to 2-torsion in its value group —
{0, ¼} for CS in ℝ/½ℤ (m003, m135, m207 genuinely sit at ¼), exactly 0 in torsion-free ℝ
(B1227). So my "CS = 0 is what the deck involution pins" needs the honest refinement:
amphichirality alone pins CS only to {0, ¼}; that m004 sits at 0 rather than ¼ is a
further fact (B1226 re-types the k-blindness wall onto "the complex volume is real" — a
contingent datum of m004, and a second separator of the sister pair: m004 at 0, m003 at ¼).
The a-priori theorem (orientation double covers are amphichiral) is untouched; what it
buys downstream is 2-torsion, not vanishing. My falsifier-paragraph claim stands corrected
in this one respect.

**(3) What genuinely requires orientation — checked, and the record already works the
Gieseking side.** CS, complex volume, spin-lift data need an orientation *as inputs of the
oriented description* — consistent with the relabeling. Better: the record's spin payment
already runs *through the non-orientable partner*: codex R021 (verified B1175) computes
the **Gieseking Pin⁻ restriction** — exactly one of m004's two spin structures extends to
m000 — and B1141's beat-selection plus the paper's own §ledger note ("the object discarded
at the most fragile fork is what later pays the last discrete bit") make the discarded
sibling load-bearing. This is my verdict's strongest corroboration from inside the record:
the Gieseking manifold is not a rejected alternative but an active computational site, and
treating m000/the class as the object with orientation as closing #1 matches how the
mathematics is actually being used.

**(4) Convergence note.** The P3 paper (2026-08-31 draft) now names the Gieseking sibling
in its axiom pricing and grades orientation the most expensive fork; B1003 prices F5
FRAGILE with "M² = RL" stated; P020's comparator discipline names Gieseking as the
mandatory comparator. The record has moved to within one step of this verdict. The step it
has not taken — and my residual recommendation — is the **relabeling itself** (axiom →
first closing, object → class/Gieseking, amphichirality → theorem-of-the-construction),
which shortens the axiom count at the entrance from three to two plus one closing, and
converts the 83/112-member amphichirality census from evidence into an instance of a
one-line theorem.

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
