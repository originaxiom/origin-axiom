# B1394 PREREGISTRATION — THE REGULAR THREE: can a symmetric source placement in m004's class give a three that is not three times one?

**Sealed 2026-09-28, before any member of the census is computed. Seat: cc (the SM-derivation branch). Occasion: sL-7 and sL-8
after B1393. The one computed completion that keeps a count is sourced: the physical-bridge lane's R24, flux sign(q)·k. On m202
the lane's R32 found that three sources on the fixed arcs of an order-3 isometry give the regular representation of C₃, so only one
mode is invariant.**

## The question

B1390 proved that in m004's arithmetic class every order-3 or order-6 isometry fixes only arcs from cusp to cusp. Those arcs are the
canonical, symmetric places to put the lane's sources. The question is whether, anywhere in the class, sources on the fixed arcs of an
order-3 isometry give a mode module that is *not* a sum of regular representations, i.e. a three that is not three times one.

## The theorem (proved now, before any census number)

This generalises the lane's R32 argument (its "fixed-fibre Hopf trace identity"); the credit is the lane's.

**Setting.**
- Q is the compact core of a member, and g an orientation-preserving isometry of order 3 with fixed set F.
- By B1390, F is a union of k arcs from cusp to cusp. g rotates each rotated cusp torus with |det(R − I)| = 3 fixed points, and the
  arcs pair them (B1371), so k = 3m.
- L is a rank-one flat bundle with g*L ≅ L, and ĝ a lift. ĝ³ = 1 automatically, because g has fixed points.
- λ_i ∈ μ₃ is the scalar by which ĝ acts on the fibre over arc i. It is constant along the arc by flatness.

**Theorem.** Σ_i λ_i = L(ĝ; Q) := Σ_j (−1)^j tr(ĝ | H^j(Q; L)). If H*(Q; L) = 0, then:
- the weights are balanced: exactly m of each cube root of unity;
- the source-mode module H¹(Q, N; L) ≅ H⁰(N; L) = ⊕_i L_{arc_i} is m copies of the regular representation of ℤ/3 (N the source
  tubes; the identification is the lane's R32);
- each lift's invariant part has dimension m.

*Proof.*
- Take an equivariant cell structure. Cells outside F are permuted freely by ℤ/3 and contribute 0 to every trace. The cells of F
  contribute Σ_i λ_i χ(arc_i) = Σ_i λ_i (the Hopf trace formula).
- If H* = 0, then Σ λ_i = 0. For weights a·1 + b·ω + c·ω² with ω² = −1 − ω, this reads (a − c) + (b − c)ω = 0, so a = b = c.
- The pair sequence with H*(Q; L) = 0 gives H¹(Q, N; L) ≅ H⁰(N; L). ∎

## The census (fixed now)

**Members.**
- The 99 arithmetic census members of B1390: B1186's 112 less its 13 non-arithmetic ones.
- cube~3.24 (B1386).
- **Control:** m202, the lane's R32 case, whose outcome is already published. It is the replication control and is part of the 99.

**Isometries.** Every cyclic subgroup of order 3 whose generator is orientation-preserving and has non-empty fixed arcs (a rotation).
These are the automorphisms of SnapPy's canonical retriangulation (B1369's and B1390's instruments).

**Characters.** Every g-invariant character χ: H₁(M) → μ₃, torsion included. These are the classes of H¹(spine; F₃) fixed by g*,
enumerated in full.
- The trivial character is included and reported separately. It is never acyclic, since H⁰ = 1.

**Per (member, ⟨g⟩, χ):**
- the twisted Betti numbers h⁰, h¹, h² of M over F₇ (ω = 2) and F₁₃ (ω = 3), which must agree;
- h²(M) = h²(spine) − (number of finite vertices of the retriangulation);
- the lift φ (solving δφ = z − g*z mod 3) and the weight λ_i on each arc. For an arc through an invariant tetrahedron t this is
  ω^{φ(t)}. For an arc along an invariant edge it is ω^{φ(t) + S(t → g t)}, S the cocycle summed along the walk around the edge;
- Σλ_i and the balance (counts of 1, ω, ω²).

**Self-tests, run first; a failure stops the run.**
- δ¹δ⁰ = 0 for every twisted complex, and h⁰ − h¹ + h²(spine) = χ(spine).
- The arc count per rotation equals B1390's instrument's count.
- The weight is constant along every arc with several invariant tetrahedra.
- The two primes agree.

## BANKED IDENTITY:

Before any census number is read, the pipeline must reproduce inside itself the lane's R32 case, m202. If any part fails, the run stops
and nothing below is read.
- One order-3 rotation subgroup with k = 3 fixed arcs.
- g-invariant order-3 characters: the trivial one and exactly two non-trivial ones.
- The trivial character: h = (1, 2, 1), weights (3, 0, 0).
- The two non-trivial characters: acyclic, with weights (1, 1, 1).
- The arc count per rotation agrees with B1390's instrument on m202.

## Predictions, sealed

- **P1 (the theorem; must hold).** In every acyclic (g, χ) the weights are balanced. A failure is an instrument error to be
  reported and repaired, not a finding.
- **P2 (open).** The fraction of non-trivial invariant characters that are acyclic. No prior worth stating; it is read, not tested.
- **P3 (open; the kill test).** Does any non-acyclic, non-trivial (g, χ) have unbalanced weights?
  - **NONE.** Every symmetric source three in the class is regular at order-3 characters. With B1390 (Higgs-twist threes are
    pullbacks) and B1384/B1378 (the deck triplet is induced), every three the record makes in m004's class is three times one, and
    the level question (sL-5) alone decides one versus three.
  - **SOME.** Those (member, g, χ) are the only places in the class where a source three is not regular. They are registered with
    their weights as a lead for the lane and for sL-7. This is not a derivation: the source and its completion remain unpaid.
  - **Prior: NONE, about 60%.** Non-acyclic cases exist (the trivial character, and characters on classes that survive), but I
    expect their extra classes to come in g-orbits that keep the weights balanced. That expectation is weak.

## Fences

- The seat's frame. The flat-twist mode module in the lane's identification (R32), not the lane's analytic domain (R18/R19), which
  is cited, not re-derived.
- Order-3 characters only. Characters of other finite orders, and the continuous invariant families, are outside this seal.
- A regular three is a statement about symmetry, not about physics. The physical sources and their completion remain unpaid (B1393,
  sL-8).

## PRIOR ART:

- The design-time sweep: `scripts/checks/already_banked.py "regular representation fixed arcs source C3"` and `git grep` on both
  branches for "regular representation" with "fixed arc".
- **Main.** No arc on sources at fixed arcs.
- **The lane.** R32 on m202 (this arc's control) and R19's Fox complex.
- **This branch.**
  - B1390 (the fixed sets are arcs);
  - B1391 (the pullback three is ℤ/3's regular representation);
  - B1384 (the deck triplet is induced);
  - B1371 (the arcs pair the fixed points).
