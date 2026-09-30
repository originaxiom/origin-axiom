# B1504 — THE END'S CHOICE: what the architecture itself fixes at a cusp point. The order bit cannot fix it: an orientation-preserving change of marking swaps LR and RL. The genesis's own data pick the two non-chiral completions of its marked point, the fibre's boundary (filling it gives the closed torus bundle, P019's "no puncture" sibling) and one other slope. And no symmetry ever forces a chiral end: where a rotation would force a charged sector's end to be chiral, it leaves the gauge sector's end no symmetric completion at all.

**Date:** 2026-09-30 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's question of 2026-09-30 (can we read the pattern
of the negatives, and did we part from genesis properly?) and the approved second step: *does the swap P act on the choice at a cusp
point the way it acts on the order bit, and does anything in the architecture fix that choice?* · **Status:**
- PROVED: T1–T3 (§2), decided at design time.
- COMPUTED: the puncture (§3) and the census (§4), own code.
- Not sealed. The question closed at design time as a theorem, so there was no open outcome to seal. This follows the record's rule
  for such arcs (B1396, B1500, B1502); the seal the owner approved was for an open outcome.

**Fence:** B1500's completion (the one-point compactification with Cheeger's ideal boundary conditions), in the seat's frame, spin-0
sectors; the orientation's action is stated in two readings (§1), and which one physics uses is not decided here. · **Price:**
unchanged, 0 of 19 · **Numbering:** B1504.

## 0. Seen from above

B1500 put the chain's remaining datum at the cusp points. On the one-point completion each cusp point is not Witt, and every sector
whose local system is trivial there needs one choice: lower perversity, upper perversity, or a Lagrangian line in H₁ of the cusp torus
(the datum of a Dehn filling). A charged sector's net chirality is the sum of the choices' signs. Charge conjugation gives the conjugate
sector the dual choice, so a self-conjugate sector, such as the gauge sector, must take a line.

The genesis gives the architecture three things that could act on that choice: the order bit (A7), the record swap P that exchanges
its two values, and the symmetries of the generated states. This arc asks what each of them does to the choice.

- **The order bit cannot fix it (T1).** Conjugation by L, an orientation-preserving change of marking, carries LR to RL. The two
  words present m004 with orientation-preserving isometries between them. So the order bit is not a property of the oriented
  manifold (B979's finding, with the orientation made explicit), and no datum at a cusp point can depend on it. At the level of
  isometries the swap induces the fibre's reflection, whose sign is s_l in main's B1324 dictionary. The characters that can act on a
  choice that exists are the Higgs class's sign (in the frame) and the mirror s_m·s_l (with a G₂ orientation), never the swap's sign
  alone.
- **The genesis's own data pick non-chiral completions (T2).** At m004's cusp point, the lines every isometry fixes are exactly the
  meridian and the longitude, and the longitude is the fibre's boundary: the puncture's own loop. Filling along it gives the closed
  torus bundle of LR (Sol), which is P019's F6 sibling, "no puncture". Filling along the meridian gives S³. m003, the sign partner,
  has the same structure, with its fibre boundary (1, −2) among its two fixed lines. The chiral choices, lower or upper, are the
  other symmetric completions. They are exchanged by nothing in the frame (a charge-conjugation torsor, a relabelling) and by the
  mirror isometries with a G₂ orientation.
- **No symmetry forces a chiral end (T3).** A finite group of lattice automorphisms fixes a line iff it contains no rotation of order
  3, 4 or 6.
  - At a cusp point that a rotation fixes, every symmetric completion of a charged pair is chiral.
  - But the gauge sector, which is self-conjugate, has no symmetric completion there at all: it needs a line, and none is fixed.
  - So a completion of the whole theory that every isometry preserves exists iff no cusp point is rotated, and then a non-chiral
    one exists.
  - The architecture's symmetries either permit a non-chiral completion or permit none; they never force chirality.
  - At a rotated hexagonal point the completion must pick one of the three root lines, which the rotation permutes. These are
    B1502's three smooth phases.

The answer to the owner's question: the swap does not act on the end's choice the way it acts on the order bit, and nothing in the
architecture fixes a chiral choice. The end's chirality is an input, which is sL-3's second closing condition, now at the ends.

## 1. The frame, and the two readings of orientation

- **The choice** (B1500 §2).
  - At a cusp point p_c, the choices for a sector with trivial local system near p_c are: lower (ε = −1), upper (ε = +1), or a
    Lagrangian line L ⊂ H₁(T_c; ℝ) (ε = 0).
  - The sector's net chirality is −Σ_c ε_c.
  - Under charge conjugation the conjugate sector gets the dual choice: lower ↔ upper, and L ↔ L.
- **Which sectors need a choice.**
  - With a cuspidal Higgs class (zero on every cusp torus), every charged sector needs one. With the trivial vacuum (no Higgs field),
    every sector does.
  - With a class alive on a cusp, the charged sectors are acyclic there (Witt) and need none. That is B1392's sealed end.
  - The neutral sector (the unbroken group's Cartan and adjoint, a real representation) always needs one, and it must be a line:
    its conjugate is itself, so its choice must equal its dual.
- **Symmetric completions.**
  - An isometry g permutes the cusp points. It carries sector μ to sector c(g)μ, where g*v = c(g)v for the Higgs class (for v = 0
    nothing is carried).
  - It maps lines by its linear part on the cusp tori.
  - A completion is symmetric when every isometry carries it to itself: when nothing outside the geometry chooses.
  - This is the genesis's own criterion. "Forced means natural" (B1384 §1): data force what is invariant under their automorphisms.
- **Two readings of orientation.**
  - *The frame.* An isometry fixes lower and upper whatever its orientation. B1500's count is intersection homology, which uses no
    orientation. Pantev–Wijnholt's superpotential ∫_M CS(𝒜) changes sign under orientation reversal, and a U(1)_R phase absorbs
    that.
  - *With a G₂ orientation.* If the completion lives in a G₂ ambient, the associative calibration orients M. An orientation-reversing
    isometry can then be a symmetry only together with M-theory's parity, which acts on the four-dimensional theory as parity, so it
    exchanges lower and upper.
  - The record's frame is the first reading. The second is what a G₂ completion would add. Every statement below is made in both
    where they differ.

## 2. The statements

**T1 (the order bit).**
- (a) L⁻¹(LR)L = RL with det L = +1: a change of marking that keeps the fibre's orientation carries one order to the other. b++LR and
  b++RL are both m004, and four of the eight isometries between them preserve orientation. So the order bit is not an invariant of
  the oriented manifold, and no choice at a cusp point (a datum of the manifold) is a function of it.
- (b) On m004 the eight isometries have diagonal cusp maps diag(s_m, s_l) with orientation o = s_m·s_l, each pattern twice (main's
  B1324, reproduced in §3). The swap P induces the fibre's reflection, pattern (−, +, −).
  - With the trivial vacuum, nothing exchanges a chiral choice at m004's cusp point in the frame. With a G₂ orientation, the mirror
    character o = s_m·s_l exchanges it.
  - With the flow-class vacuum, the class sign is s_m and the frame's exchanging character is s_m. With a G₂ orientation it is
    o·s_m = s_l, the swap's own sign. But there the charged sectors are acyclic at the cusp and carry no choice.
  - So the swap's character governs a choice only in the one case where no choice exists.

**T2 (the puncture).**
- The lines fixed by every isometry of m004 are exactly the meridian (1, 0) and the longitude (0, 1). The longitude is the
  homological longitude, the fibre's boundary.
- The symmetric self-dual completions of m004's cusp point are exactly these two. The fillings are S³ (meridian) and the closed torus
  bundle of LR (longitude; Sol, H₁ = ℤ).
- For m003 the fixed lines are (1, 0) and (1, −2), and (1, −2) is its fibre boundary. The fillings are the closed torus bundle of −LR
  (H₁ = ℤ/5 ⊕ ℤ, Sol) and a closed manifold with H₁ = ℤ/10.
- With the trivial vacuum the frame also admits the two chiral completions at each root's point, exchanged only by charge
  conjugation. With a G₂ orientation, four of the eight isometries reverse orientation and exchange them, so only the two self-dual
  completions are symmetric.

**Lemma (the lattice).** A finite group G ⊂ GL(2, ℤ) fixes a real line iff it has no element of order 3, 4 or 6.
- The elements of finite order are ±I, reflections (det −1, with two rational eigenlines) and rotations of order 3, 4 and 6 (no real
  eigenline).
- Without rotations, the product of two reflections is ±I, so all reflections share their eigenlines.
- Checked on all subgroups of D₄ and D₆ (26 of them), which up to conjugacy are all the finite subgroups of GL(2, ℤ).

**T3 (the rotation).**
- Let a cusp point p_c have in its stabiliser an isometry rotating T_c by order 3, 4 or 6. Then:
  - (i) no symmetric completion of a self-conjugate sector exists at p_c. Its choice must be a line; the rotation fixes none and
    permutes the lines in free orbits, of three (order 3 or 6) or two (order 4).
  - (ii) every symmetric completion of a charged pair at p_c is chiral, in the frame. With a G₂ orientation, if the stabiliser also
    reverses orientation, the charged pair has no symmetric completion either.
- **Corollary.** A completion of the whole theory (neutral sector included) that every isometry preserves exists iff no cusp point is
  rotated. When none is, fixed lines exist at every point (the lemma), and completing every sector along them, transported between
  cusp points by the isometries, is symmetric and non-chiral.
- So on no cusped hyperbolic 3-manifold does symmetry force a chiral cone-point completion. It permits a non-chiral one or permits
  none.
- In m004's class, rotations at cusps have order 3 or 6 (B1390: order 4 fixes only closed geodesics), so the rotated points are
  hexagonal. The three root lines of the lattice form one rotation orbit, and filling one of them is one of B1502's three smooth
  phases.

## 3. The puncture, computed

`verification/end_choice.py puncture`; recorded in `end_choice.json`.

**m004.**
- SnapPy's eight isometries have cusp maps ±diag(1, ±1): the patterns (o, s_m, s_l) = (+, +, +), (+, −, −), (−, +, −), (−, −, +),
  each twice, with o = s_m·s_l. This is main's B1324 C1, reproduced.
- The flow class's sign under each isometry, from B1369's instrument (its exact action on H₁(M)), equals s_m as a multiset over the
  eight.
- The lines they all fix are (1, 0) and (0, 1). The homological longitude, computed from the abelianised presentation, is (0, 1): the
  fibre's boundary.
- Filling (1, 0) gives π₁ = 1 (S³). Filling (0, 1) gives H₁ = ℤ with flat tetrahedra: the Sol torus bundle, as in B1380 S7.

**m003.**
- Eight isometries, four orientation-reversing. The cusp is hexagonal (shape ω), and no isometry rotates it: the maps are ±I and two
  reflections.
- The fixed lines are (1, 0) and (1, −2). The homological longitude is (−1, 2), the same line: the fibre's boundary.
- Filling (1, −2) gives H₁ = ℤ/5 ⊕ ℤ with flat tetrahedra (the closed torus bundle of −LR). Filling (1, 0) gives H₁ = ℤ/10.

**The order bit.** L⁻¹(LR)L = RL with det L = 1, and P(LR)P = RL with det P = −1. b++LR is m004. Of the eight isometries between
b++LR and b++RL, four preserve orientation.

**The lemma.** All 26 subgroups of D₄ and D₆ were checked. The 7 that contain a rotation of order 3, 4 or 6 fix no line; the other 19
fix one.

## 4. The census, computed

`verification/end_choice.py census`; recorded in `end_choice.json` and `end_choice_run.txt`.
- **The members (209).**
  - m004, m003 and the rest of B1186's 99 arithmetic members.
  - cube~3.24 (B1386).
  - B1399's 109 covers.
- **The data.** 398 cusp points and 2 034 isometries (SnapPy), every cusp's stabiliser and the linear parts of its elements.
- **Two independent checks.**
  - Every cusp map of every cusp-fixing isometry (3 024 stabiliser elements) is a similarity of that cusp's flat lattice, computed
    from the cusp shape (§1 of the script): 3 024 of 3 024.
  - On the 99 family members, B1369's instrument (the canonical retriangulation's automorphisms and their exact torus action) agrees
    with SnapPy on the number of isometries and on every cusp's stabiliser types: 99 of 99.
  - On cube~3.24 and the covers it was not completed. Run on cube~3.24's own triangulation (90 tetrahedra), its exact homology
    ran out of memory: the process was killed at about 14 GB. It was not attempted on the covers. There the check rests on the
    geometric similarity check and on SnapPy's symmetry-group order.
- **The lemma on real stabilisers.** At every one of the 398 points, "no fixed line" coincides with "a rotation of order 3, 4 or 6 in
  the stabiliser".

**The rotated points.**
- 25 points on 10 members: m202, s959, v3551, o9_40999, o10_150704, o10_150725, o10_150726, o10_150729, cube~3.24, and one cover of
  o10_150725 (B1399's no. 101).
- Their rotation orders are 3 and 6, never 4 (B1390). Every rotated point is hexagonal, and at every one the rotation permutes the
  three root lines in a 3-cycle.
- On seven members every cusp point is rotated: m202, s959, v3551, o9_40999 and o10_150726 (all chiral), and o10_150704 and
  o10_150729 (amphichiral).
  - On the five chiral ones, symmetry alone would force every charged sector's end to be chiral: every point is rotated, and nothing
    reverses orientation.
  - But the same rotations leave the gauge sector's ends no symmetric completion. So the completion breaks the symmetry, and the
    forcing goes with it (T3).

**The unrotated members (199).**
- A symmetric self-dual completion exists on each, as T3 says.
- Its lines at m004 are the meridian and the fibre's boundary. At cube~3.24's two unrotated cusps every line is fixed, because the
  stabilisers there act by ±I.
- In the frame, a symmetric chiral completion (trivial vacuum) is also allowed on all 199.
- With a G₂ orientation it is allowed on exactly the 123 chiral ones. On the 76 amphichiral ones, m004 and m003 among them, the
  orientation-reversing isometries forbid it, because they exchange lower and upper:
  - on 72 of them every cusp point's stabiliser reverses orientation, so no end can be chiral at all;
  - on the other 4 (o10_150685 and three of B1399's covers) chiral ends can be symmetric, but they come in lower–upper pairs and
    their net is zero.
- So, read with a G₂ orientation, the census says:
  - amphichirality forbids a net chirality at the ends, and nothing forces one;
  - the genesis's own root is on the forbidden side.

## 5. What it means

**Q1: does P act on the end's choice as it acts on the order bit?** No.
- The order bit is invisible to the oriented manifold (T1a).
- The swap's isometry leaves m004's end choices alone in the frame. With a G₂ orientation it acts through the mirror character,
  which is the swap times the arrow (B1324), not through the swap's own sign (T1b).
- P022's "one question asked three times" splits in two:
  - the orientation fork and matter's chirality meet only where a G₂ orientation acts;
  - the order bit is a based datum that chirality cannot see.

**Q2: does anything in the architecture fix the choice?** Not a chiral one.
- The genesis's own data, the fibration and its flow, pick the two non-chiral completions of the marked point (T2). The natural way
  to complete the puncture is to fill it, which returns the carrier without its puncture.
- The architecture's symmetries force the *type* of choice at special points, and they never force it to be chiral (T3).
- Rotated points are the only places where a charged sector's end is forced chiral, and there the gauge sector's end has no
  symmetric completion at all. The completion must choose one of three root lines. The Eisenstein face therefore forces a selection
  at the ends, not a supply.

**For sL-3.** The end's chirality is an input, not supplied by the architecture. That is the lead's second closing condition, now at
the ends: every datum that fixes it comes from outside.
- In the frame, orientation does not act on the end at all; charge conjugation does.
- With a G₂ orientation, orientation acts, and at the genesis's own puncture it forbids a chiral end rather than supplying one.
- So the one question this arc leaves is physical: whether the completion carries a G₂ orientation. That belongs to sL-8, the end law.

## 6. Prior art and fences

- **Main's B1324 (2026-09-09)**, harvested by citation and reproduced here on m004: the dictionary det = s_m·s_l, the four patterns
  twice each, "the fibre's reflection is the A7 swap", mirror = swap × arrow. It also states the pattern this arc turns on: "every
  no-go on chirality used a symmetry the object has".
- **T1 (a) is not new.** B979 found that LR and RL are conjugate, so A7 is based-level data (B1379's correction of record). This
  arc adds only that the conjugation keeps orientation: four of the eight isometries between b++LR and b++RL do.
- **B1083 (2026-08-19)** typed the origin torsor: reversal is a parity bit, the swap a charge-conjugation-type bit, and the arrow is
  not on the torsor. §1's two readings match that typing. In the frame, what exchanges a chiral end choice is charge conjugation, a
  relabelling. With a G₂ orientation, the mirror, a parity, exchanges it too. The order bit, the swap's torsor, is invisible to the
  oriented manifold either way.
- **B1385 L1** used "the rotation has no fixed line on H₁(T²)" for the far-up partition. T3 uses the same fact for the completion's
  lines.
- **This branch.** B1500 (the choice), B1502 (the three smooth phases fill the three roots), B1390 (order-3 and order-6 axes end at
  cusps; order 4 fixes only closed geodesics), B1380 S7 (m004(0,1) is Sol), B1384 §1 (naturality), P019 (F6), P022 (the addendum).
- **The literature, cited.** Cheeger, and Albin–Leichtnam–Mazzeo–Piazza (ideal boundary conditions, self-dual iff Lagrangian);
  Pantev–Wijnholt (the superpotential ∫ CS(𝒜)); Acharya–Witten (a G₂ manifold's orientation fixes the four-dimensional chirality).
- **The sweep.** This branch, main (`987c0c8f`) and the audit lane (`b72c6ae1`, and again at `e94abeb1` before banking) were searched
  for symmetric or natural completions, invariant Lagrangian lines, equivariant ideal boundary conditions, anti-G₂ maps and M-theory
  parity. Found: B1324's dictionary and statement, B1279's orientation-reversing symmetry "up to charge conjugation", and old cells on
  rotations with no invariant line (B760, B775) in other contexts. No prior statement was found of T2's identification (the puncture's
  natural completions are the fibre's boundary and one other slope), of T3's consequence for the self-conjugate sector, or of its
  corollary. The lattice lemma is standard.
- **The audit lane's control (ROOT_SCOPE_AUDIT, `9d75f7cb`, 2026-09-30),** harvested by citation. A symmetric problem can have
  asymmetric solutions: "no unique invariant choice does not mean no asymmetric solution". This arc respects that. T3 says symmetry
  never *forces* a chiral end; it does not say a chiral end is impossible, which is why the end's chirality is called an input. The
  same report reads the negatives note as organization, not a universal impossibility theorem, which is how the note describes itself.
  The lane's open item PB-BOUNDARY (its OPEN_LEADS, 2026-09-30) asks for the latest genesis-side marking and order proposal to be
  compared with an actual end action. T1 answers the marking half: the order bit cannot select an end condition, because it is not a
  datum of the oriented manifold. The end action itself stays open (sL-8).
- **Fences.**
  - The completion is B1500's. Caps and walls (B1395–B1397) are different completions: a cap's torus boundary condition does not pick
    a line, and B1396 built ℤ/3-symmetric caps.
  - The census uses the trivial vacuum wherever a vacuum enters. T3 holds for every vacuum.
  - The G₂ reading is stated, not derived.
  - The P-as-move root (the Gieseking manifold) is non-orientable, and the frame's superpotential needs an orientation, so the frame
    gives it no count.
  - No physics crossed. 0 of 19.

## 7. Files

- `verification/end_choice.py`: parts A–D (the puncture, the lattice lemma, the census with B1369's cross-check, the per-member
  statements).
- `verification/end_choice_run.txt`, `verification/end_choice.json`: the recorded run.
- `tests/test_b1504_the_ends_choice.py`: the lock.
