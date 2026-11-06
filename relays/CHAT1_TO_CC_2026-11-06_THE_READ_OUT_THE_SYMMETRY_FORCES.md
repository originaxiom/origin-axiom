# THE READ-OUT THE HISTORY'S SYMMETRY FORCES (THE OWNER: "KEEP ME ON THE CHOICES", STARTING WITH THE READ-OUT AFTER P-723): THE ONE-DEPARTURE HISTORY HAS ONE NONTRIVIAL SYMMETRY IN PGL(2, ℤ), THE REFLECTION τ ↦ n − τ̄, WHICH FIXES ONE POINT OF IT, THE APEX, FOR EVERY RUN n ≥ 2. A NATURAL POINT READ-OUT OF THE TEICHMÜLLER HISTORY THAT USES NO ARROW (B716) IS THEREFORE THE APEX, WITH NO KINETIC STRUCTURE. ON A CLOSED THREAD, B1845'S CIRCLE, THE SAME PREMISES LEAVE THE APEX AND AN ANTI-APEX. A PERIOD AVERAGE IS BLIND TO THE DEPARTURE IN THE ONE-DEPARTURE LIMIT. THE SAME SYMMETRY FIXES P-723'S LAYER BUT NOT ITS SHAPE'S POSITION. CHOICE 6 NARROWS TO STATED PREMISES: A POINT, THE TEICHMÜLLER HISTORY, THE ONE-DEPARTURE LIMIT

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On** the owner's answer to this seat, "Keep me on the choices": keep reducing the named choices, starting with the
read-out point after P-723. The read-out is choice 6 in 21cfbc3c2 § 4 ("the apex read-out: a symmetry criterion").

**Kind:** data-free. PGL(2, ℤ) geometry, plus SnapPy 3.3.2's shapes. No coupling, no ratio of the six, no θ̄ and no
held-out quantity is computed, and nothing is compared with data. The six are not a criterion (P-708).

**Check:**
- `relays/chat1_2026-11-06_the_departure/PREREGISTRATION_READ_OUT.md` and `read_out_check.py` were committed at
  49bb0e985, before the run.
- A reduced smoke copy ran outside the tree first; its values were not read.
- The full run was made once. Its outputs were committed unread at a34f5cdd1, after checking for no NaN and no paths.
  Its stderr was captured outside the tree (0 bytes) and its exit code printed (0). Both were copied in at c6e3801c4,
  as for the seat's earlier checks.
- **Post hoc, labelled:** `read_out_posthoc.py`, written after reading a34f5cdd1 and committed before its run at
  55abf5538. Its outputs were committed unread at 70cdc8555, its stderr and exit code at c6e3801c4.

**Swept first** (main at 4baffa949; main-only form):
- `VERDICT topic-sweep /apex rule|apex read.?out|read.?out (point|rule)|which point|the point read/ (full text): 8 of 1591 arcs on main match (PROVED 8); 7 register rows match (DONE 5, QUEUED 2)`
- `VERDICT topic-sweep /time.?revers|stabili[sz]er of the (excursion|geodesic|history)|unique(ly)? (symmetric|fixed) point|fixed by the (reflection|mirror)/ (full text): 11 of 1591 arcs on main match (NEGATIVE 4, PROVED 7); 0 register rows match (none)`
- `VERDICT topic-sweep /pleated|Cannon.?Thurston|Gu[ée]ritaud|layered triangulation|shear coordinate/ (full text): 8 of 1591 arcs on main match (PROVED 8); 2 register rows match (DONE 1, QUEUED 1)`
- `VERDICT topic-sweep /period average/ (full text): 1 of 1591 arcs on main match (PROVED 1); 3 register rows match (DONE 1, QUEUED 2)`
- `VERDICT topic-sweep /half.?turn|anti.?apex|symmetric point/ (full text): 25 of 1591 arcs on main match (NEGATIVE 3, PROVED 22); 12 register rows match (DECLINED 1, DONE 6, QUEUED 5)`

Bearing on it:
- **B1845:** P-455's period average along the k = 5 thread "washes the hierarchy out", and "the apex read-out is
  load-bearing and its derivation needs a kinetic structure along the circle (FL-05)".
- **P-723:** the deepest layer's shape is "a second object-native candidate for τ, with the same kind of read-out
  choice (which layer)". S305x is building the pleated surfaces' τ (stages A and B validated, C and D owed).
- **P-717 and S305o:** "the limit m → ∞ (or a stated m)" is already named among P-717's choices.
- **P-720** (DONE NEGATIVE): minimal Kähler cannot localise the read-out.
- **904f19136 § 4:** "a symmetry criterion, not a derivation". § 3 there, and B1733, already hold the golden axis's
  half-turn at i.
- **B716** (NEGATIVE): no canonical arrow.
- **B1749's withdrawal** concerned the thread rule as a selector of τ across many threads, not this question.

No row states the uniqueness of § 1 or the two-point census of § 2.

**Refereed read-only:** READY WITH CORRECTIONS (9 findings and 13 suggestions), all applied in this text. The first
draft's errors are listed under Disclosures.

## 1. The result

**The history.** The one-departure history of a run n is the non-periodic geodesic from a = −1/φ to b = n + 1/φ: the
golden thread departing once and returning (P-717; 904f19136). It is the m → ∞ limit of the closed threads
L^n R (LR)^m.

**Its stabiliser in PGL(2, ℤ) is {1, ρ_n}, with ρ_n: τ ↦ n − τ̄, for every n ≥ 2.**
- **No element other than the identity fixes both ends.** Such an element would make a and b the roots of one integer
  quadratic, so they would be Galois conjugates. They are not, for n ≠ 1.
- **Only ρ_n swaps them.** For g = [[p, q], [r, s]]:
  - g(a) = b and g(b) = a give s = −p and pn + q − r·ab = 0, with ab = (n − 3)/2 + ((1 − n)/2)√5;
  - the √5 part forces r = 0, then q = −pn and det = −p².
- **Half-turns are excluded** by the same equation, since p² = −1 has no integer solution.
- **The check.** Part A confirms this exactly over ℚ(√5) for n = 2…12:
  - the swap solutions have rank 1, spanned by ±(1, −n, 0, −1) with det −1;
  - the fix solutions have rank 1, spanned by the identity.
  - At n = 1, the golden loop's own conjugate ends, both have rank 2; the stabiliser is the infinite group of § 2.
  - The referee's independent brute force (det ±1, entries up to 13–14) agrees.

**Its fixed point.** ρ_n's mirror Re τ = n/2 meets the history once, at its top: the apex n/2 + i(n − 1 + √5)/2.
- At reading (ii)'s run of 6 this is τ*₆ = 3 + i√5φ ≡ i√5φ.

**On the 3-manifold.** ρ_n reverses both the history's direction and the fibre's orientation. On the 3-manifold M it is
therefore an orientation-preserving involution, not a chirality: e·det = (−1)(−1) = +1, B1733's classification. The
referee's SnapPy run supports this: b++L⁵R(LR)^k and b++L⁶R(LR)^k (k = 3, 8) have symmetry group ℤ/2 × ℤ/2 and are
not amphicheiral.

**So, on the one-departure history, three premises force the apex:**
- **(N1)** the read-out is one point;
- **(N2)** it is a point of the Teichmüller history, the fibre's conformal modulus along its Teichmüller geodesic;
- **(N3)** the rule is natural and uses neither an arrow nor a fibre orientation beyond M's.
  - On an oriented M these two are one datum, so B716's "no canonical arrow" is its ground.
  - A rule that kept a fibre orientation would be natural only under PSL(2, ℤ). The history's stabiliser there is
    trivial, and nothing would be selected.

No kinetic structure enters where the point sits. The premises, not the apex, are what stays chosen (§ 4).

## 2. On periodic histories there are two points

**The golden loop LR** (part B, and post hoc (a), which counts both determinants):
- There are two classes of symmetric points, log φ = 0.481212 apart, half the glide G = [[0, 1], [1, 1]]'s
  translation:
  - the mirrors' class, which reduces to the golden apex ½ + (√5/2)i;
  - the half-turns' class, which reduces to i. S·LR·S⁻¹ = (LR)⁻¹, and i lies on LR's axis.
- **The count depends on (N3).** The half-turns have e·det = −1, so they reverse M's orientation; they are chiralities
  (m004 is amphicheiral). Under (N3) as stated, which keeps M's orientation, only the mirrors count. Their points all
  reduce to one τ, the golden apex.
- If the rule also uses no orientation of M, treating the hand as a bit, i counts too, and the loop has two τ's.

**Every closed thread L^n R (LR)^k** (n = 5, 6; k = 0…6):
- There is no root, and there are exactly two classes, half a period apart. That is a theorem for D∞; the outputs
  agree to all digits printed.
- With no root, both classes have the same determinant. Here they are mirrors, so they count under either reading of
  (N3). Post hoc (a) lists every direction-reversing element for k ≤ 2 and finds mirrors only.
- **The departure's class** is the apex. Its heights continue the record's table:
  - n = 6: 3.87298, 3.65148, 3.62284, 3.61873, 3.61814, 3.61805, 3.61804, at Re 0;
  - n = 5: 3.35410, 3.14907, 3.12250, 3.11868, 3.11813, 3.11805, 3.11804, at Re ½.
  - The record held n = 6 to k = 4, n = 5 to k = 3, and B1845's k = 5 height 3.118047822312, which matches. The other
    entries are new.
- **The anti-apex** is the second class:
  - k ≥ 2: reduced Im 1.04 to 1.15, oscillating towards √5/2;
  - k = 1: 1.350 (n = 5) and 1.369 (n = 6);
  - k = 0: 0.958 and 0.968, on |τ| = 1.
  - It sits in the alternating block: in the golden stretch for k ≥ 1, at the single R for k = 0. The check did not
    locate it in the word; the location comes from the palindrome's two axes.
- **So on B1845's circle the premises leave two candidates, the apex and the anti-apex.** B1845's call for more
  structure stands there.
- **In the one-departure limit** the anti-apex lies half a period away, a distance that grows without bound, and only
  the apex remains. Uniqueness therefore needs the non-periodic history: S305o's limit m → ∞, already one of P-717's
  named choices.

**A period average is blind to the departure in the one-departure limit** (part D):
- l(L^n R (LR)^k) − k·l(LR) converges to 3.976109 (n = 5) and 4.273565 (n = 6).
  - By definition this is l(LR) plus the least-action excess: 2.051262 and 2.348718, from the closed form
    2 log((n − 1 + √5)/√5).
  - 0772952e3 named 2.3487. The agreement is a consistency check, not new information.
- The departure's arc above Im 2 has fixed length A_n = 2 acosh(r_n/2): 2.0269 and 2.3978.
- So its share of the period falls like 1/k. Sampled at 4000 points in arclength over one period, the fraction above
  Im 2 equals A_n/l to within the sampling resolution (2.5 × 10⁻⁴):

  | thread | k = 5: sampled, A_n/l | k = 20: sampled, A_n/l |
  |---|---|---|
  | L⁵R(LR)^k | 0.1490, 0.14903 | 0.04775, 0.04772 |
  | L⁶R(LR)^k | 0.1725, 0.17253 | 0.0560, 0.05606 |

- **The consequence** (standard shadowing): a period-averaged read-out of any bounded continuous function tends to the
  golden loop's average for every n. In that limit it cannot place τ by the departure; that is (N1)'s ground.
- At finite k the departure is not negligible (15% of the period at k = 5), and P-720's weighted proxy at finite k is
  not blind.
- **B1845's "17% of the period above Im 2"** is 7 of its 41 arclength samples on L⁵R(LR)⁵ (its FINDINGS § 4;
  translation length 13.600). That agrees with this seat's 14.9% at its resolution of 1/41.

## 3. The 3D candidate (P-723), and main's pleated build

**Where the symmetric object sits** (part C).
- The apex lies on the Farey edge (n/2, ∞) for even n, so the 3D symmetric object is a flip (a tetrahedron).
- For odd n it lies inside the triangle ((n − 1)/2, (n + 1)/2, ∞), so the 3D symmetric object is a surface.

**What SnapPy shows** (part E, b++ L^n R (LR)^k, n = 5, 6, k = 8, 12):
- **The structure.** There is one tetrahedron per letter, and all are positively oriented.
- **One reflection.** Exactly one reflection of the cyclic sequence, i ↦ n − i, preserves the shapes as Z/3 orbits, to
  10⁻²⁰. The next best fails by 1.8 (n = 5) and 2.4 (n = 6).
- **Its centres.**
  - n = 6: tetrahedron 3, which is fixed;
  - n = 5: between tetrahedra 2 and 3, a surface;
  - on each closed bundle the second centre lies in the alternating block.
  - SnapPy's tetrahedron i is the flip entering letter i. This is inferred from the centre's position (P6's either/or),
    not checked directly.
- **The pairing of layers.**
  - Tetrahedra j and n − j have equal shapes.
  - The surfaces (letters) pair as j ↔ n − 1 − j: at n = 6, letters 2 and 3 flank tetrahedron 3; at n = 5, letter 2 is
    the fixed surface.
- **The run's pairs are equal, not conjugate.** Their conjugate-orbit distances are 3.30, 1.86 and 0.36 (n = 5), and
  4.04, 2.04 and 0.32 (n = 6). So the symmetry acts as an orientation-preserving involution, as § 1 derives.
- **The highest tetrahedra:**
  - n = 5: the central pair, 2 and 3, equal, at height 2.146219 (shape −2.865326 + 2.146219i);
  - n = 6: tetrahedra 2, 3 and 4, tied to working precision at 2.458778.
  - The tie comes from an observed identity, z₃ = z₂ − 1 = z₄ − 1. Post hoc (b) finds an integer translation between
    the orbits, residual 10⁻⁶⁰, and the referee finds it at every k = 0…12. It is not derived.
- **Comparison with P-723.**
  - Its 2.459 and run-6 shape −3.494 + 2.459i are tetrahedra 2 and 4 here.
  - Its run-5 shape −2.866 + 2.146i is a finite-k value (the referee: −2.86557 + 2.14641i at k = 5). The limit is
    −2.865326 + 2.146219i.
  - Between k = 8 and k = 12 the central shapes move at most 3.3 × 10⁻⁶.

**So, in the one-departure limit, the same premises fix P-723's "which layer":** the central tetrahedron at run 6, the
central pair at run 5.

**But the symmetry does not pin the 3D shape to a mirror.** An orientation-preserving involution leaves a tetrahedron's
shape free. Run 6's central shape reduces to −0.494242 + 2.458778i, which is 0.0058 off the mirror Re = −½. The apex is
pinned to Re 0.

**For main's pleated build (S305x, stages C and D), the symmetry predicts, for the intrinsic modulus:**
- **Odd runs.** The central surface is mapped to itself with its orientation reversed. Its τ is fixed by an
  orientation-reversing element of PGL(2, ℤ), so it lies on a mirror.
  - Frame-free: the reduced τ lies on the fundamental domain's boundary, |Re| = ½ or |τ| = 1.
  - With the run's fan at ∞, it lies on Re ½ mod 1.
- **Even runs.** There is no central surface. The two surfaces flanking the central tetrahedron (letters n/2 − 1 and
  n/2) have τ's exchanged by ρ_n.
  - Frame-free: they reduce to τ_F and −τ̄_F.
  - So a pleated read-out at run 6 carries a two-layer choice, unless it reads the tetrahedron or a symmetric
    construction from the pair.
- **In general,** surfaces j and n − 1 − j have τ's related by ρ_n.
- "On a mirror" is invariant under any mapping-class-equivariant identification of Teichmüller space with H. Stage D's
  output can be checked against these.

## 4. What this does to choice 6

**The apex is the unique output of the symmetry criterion on the one-departure history.**
- 904f19136 § 4 called it "a symmetry criterion, not a derivation". What is new: the criterion is well posed, since the
  stabiliser is exactly {1, ρ_n} for every n ≥ 2, and its no-arrow ground is B716.
- Under reading (ii) it gives τ*₆ = i√5φ.

**B1845's "needs a kinetic structure" narrows.**
- On the one-departure history, the point's position follows from the symmetry; a kinetic structure would only explain
  why the read-out is a point (N1).
- On a closed thread, the circle B1845 speaks of, the symmetry leaves the apex and the anti-apex, and the need stands.

**What stays chosen for the read-out:**
- **(N1), a point rather than an average.**
  - This is the frame's form as a commitment: its couplings are modular forms evaluated at one τ.
  - An average returns no τ, and in the one-departure limit it is blind to the departure (§ 2).
- **(N2), the Teichmüller geodesic.**
  - The pleated surfaces' moduli are also a path of the fibre's modulus, which S305x is building.
  - The tetrahedron shapes would need a dictionary from shapes to the fibre's modulus; the figure-eight's shapes
    e^{iπ/3} are "the retired τ = ω" (P-723).
- **(N3), no arrow and no fibre orientation beyond M's**, grounded in B716. Whether M's own orientation may also be
  dropped changes only the golden loop's count (§ 2).
- **The one-departure limit**, apex rather than anti-apex: S305o's m → ∞, already one of P-717's named choices.

**The line.** At τ*₆ the mirror fixes both lines of the pair (904f19136 § 4). So the symmetry does not decide the bit
(B1733), and choice 7 stands.

**The goal's other choices are unchanged by this note:**
- (K);
- reading (ii);
- a nonzero line;
- minimality or the ladder (S305w derives R1 given minimality);
- one departure, or least action;
- the bit.

## Disclosures

- **By the pre-registration's own list, the claim was refuted as measured on two counts.**
  - A closed axis had a number of classes other than two: the golden loop showed one.
  - P8 failed.
  - It is kept on post hoc grounds. P2's failure is an instrument limit, repaired by post hoc (a). P8's is a tie.
- **P2 failed as measured.**
  - The check built only mirrors, the palindromic P·J₀ elements. It found one class on the golden loop, the golden
    apex.
  - The predicted second class (i) is a half-turn class. The golden loop's glide makes the two classes alternate in
    determinant, which the pre-registration did not foresee.
  - Post hoc (a) enumerated both determinants (free entries to 300) and confirmed two classes, log φ apart, at
    ½ + (√5/2)i and i.
  - Whether the half-turn class counts depends on (N3) (§ 2).
- **P3:**
  - its hand-set bound on the anti-apex ("below 1.3") failed at k = 1, at 1.350 and 1.369;
  - its location clause ("in the golden stretch") was not measured, and at k = 0 there is no golden stretch: the
    anti-apex sits at the R;
  - its class count, separations and departure heights held.
- **P8:**
  - "the highest is the central tetrahedron" failed at n = 6, by a three-way tie to working precision;
  - its convergence tolerance was loosened from 10⁻⁶ to 10⁻³ before the commit. The measured movement, up to
    3.3 × 10⁻⁶, would have failed 10⁻⁶;
  - its heights and off-mirror clauses held.
- **The derivation in § 1 is algebraic and holds for every n ≥ 2.** Part A checks it for n ≤ 12.
- **The first draft overstated,** and the referee's corrections are applied:
  - It said "the departure makes the read-out unique". Every closed thread carries the departure and still gives two
    points; only the non-periodic limit gives one.
  - It gave the golden loop two τ's without noting that the half-turns reverse M's orientation.
  - It said (N2) excluded the pleated layers, which are also fibre moduli.
  - It said "the apex is no longer a rule".
  - It misread B1845's 17%. That figure is 7 of 41 samples on L⁵R(LR)⁵ and agrees with this seat's figure.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE READ-OUT THE HISTORY'S SYMMETRY FORCES (the owner: "Keep me on the choices"; data-free; prereg 49bb0e985, outputs a34f5cdd1, post hoc 55abf5538 / 70cdc8555, stderr and exit c6e3801c4) | "the one-departure history has one nontrivial symmetry in PGL(2, ℤ), the reflection τ ↦ n − τ̄, which fixes one point of it, the apex, for every run n ≥ 2. A natural point read-out of the Teichmüller history that uses no arrow (B716) is therefore the apex, with no kinetic structure. On a closed thread, B1845's circle, the same premises leave the apex and an anti-apex. A period average is blind to the departure in the one-departure limit. The same symmetry fixes P-723's layer but not its shape's position. Choice 6 narrows to stated premises: a point, the Teichmüller history, the one-departure limit" | `relays/CHAT1_TO_CC_2026-11-06_THE_READ_OUT_THE_SYMMETRY_FORCES.md` @ the commit adding it | — | P-723, P-455, P-717, P-720, B1845, B716, FL-05 | 2026-11-06 |

0 of 19.
