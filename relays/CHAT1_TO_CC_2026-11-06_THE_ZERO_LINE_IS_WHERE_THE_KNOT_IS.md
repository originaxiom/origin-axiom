# THE ZERO LINE IS WHERE THE KNOT IS (THE OWNER: "KEEP ME ON THE CHOICES"; CHOICE 3, A NONZERO LINE): ON THE OBJECT'S PUNCTURED FIBRE THE MONODROMY HAS NO FIXED POINT, AND ITS SHORTEST PERIODIC ORBITS ARE EXACTLY THE PAIR (PERIOD 2). P-721'S "MINIMAL PERIODIC ORBIT" IS EXACT ONLY THERE: ON THE CLOSED TORUS THE MINIMAL ORBIT IS THE ORIGIN, THE ZERO LINE, WHERE THE FILLING'S CORE PASSES. AS A DIHEDRAL REPRESENTATION, "NONZERO" IS SURJECTIVITY: THE ZERO IS THE ABELIAN REPRESENTATION EVERY KNOT HAS. AS A BARE FLAT BUNDLE THE ZERO STAYS ADMISSIBLE. CHOICE 3 IS RESTATED IN THE OBJECT'S TERMS, NOT REMOVED

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On** the owner's "Keep me on the choices". This is the next named choice after the read-out (c6b813450): choice 3 in
21cfbc3c2 § 4, "a nonzero line. The exclusion of level 3 rests on it."

**Kind:** a conceptual note, with no new computation. It holds no value of any held-out quantity, computes no
coupling, and compares nothing with data. Its counts come from:
- determinants of 2 × 2 integer matrices;
- 5fef38dee (re-run on main at S305y);
- the departure note's post hoc (5), for D₅.

**Swept first** (main at 307fa9101; main-only form):
- `VERDICT topic-sweep /zero line|the line \(0, ?0\)|untwisted line|trivial line/ (full text): 13 of 1591 arcs on main match (NEGATIVE 2, PROVED 11); 10 register rows match (DECLINED 1, DONE 2, QUEUED 7)`
- `VERDICT topic-sweep /puncture.{0,80}(line|w ?= ?0|origin)|(zero line|w ?= ?0|origin).{0,80}puncture|the zero line.{0,60}cusp|cusp.{0,60}zero line/ (full text): 9 of 1591 arcs on main match (NEGATIVE 1, PROVED 8); 2 register rows match (DONE 1, QUEUED 1)`
- `VERDICT topic-sweep /0.?surgery|zero.?surgery|0.?filling|longitude filling|torus bundle with monodromy/ (full text): 13 of 1591 arcs on main match (NEGATIVE 2, PROVED 11); 0 register rows match (none)`
- `VERDICT topic-sweep /Abel.?Jacobi|Pic.?0|Jacobian of the fibre/ (full text): 0 of 1591 arcs on main match (none); 0 register rows match (none)`

Bearing on it:
- **P-721:** the dynamics "on the fibre torus"; the twisted fixed points "number det(A + I) = tr A + 2 = 5, and the
  nonzero ones are exactly P-718's eigenline — so the line is a minimal periodic orbit of the object's own dynamics".
- **P-718:** it selects the order-5 lines by B1733's rule. S305t's verified addition is that the eigenline's two
  points "correspond to" the figure-eight's two classes of surjective D₅ representations.
- **B1733:** "a flat line is w = ατ + b", with its covariance (α, b) ↦ (α, b)γ⁻¹. Its § 0 already names H₁ of a
  thread's double branched cover as one form of its rule.
- **B366's puncture lemma:** SL(2, ℤ) on the 2-torsion of the fibre torus fixes only the origin; "The puncture is the
  unique MCG-invariant point".
- **B287:** the fibre slope is the unique torus-bundle closing, with monodromy exactly LR.
- **The record's zero-line configurations:**
  - B1809: "zero line for Table T unless stated";
  - B1810: "zero line or a flat line";
  - B1807: "at zero line".

B366 identifies the origin point with the puncture. No row identifies the zero flat line with the puncture, or with the
trivial colouring.

**Refereed read-only:** READY WITH CORRECTIONS (10 findings), all applied in this text. The first draft's overstatements
are listed under Disclosures.

## 1. The facts

The monodromy A = LR acts linearly on the fibre's torus T² = ℝ²/ℤ² and fixes the origin. The object is the
once-punctured torus bundle: its fibre is T² minus the origin. The puncture is the fibre's end at the knot. After B287's
fibre filling, the filling's core meets each closed fibre once, at the origin. That last fact is from the linear model,
not B287's text.

**The fixed and periodic points:**

| map | count on T² | which points | on the punctured fibre |
|---|---|---|---|
| A (untwisted) | \|det(A − I)\| = 1 | the origin | none |
| −A (twisted) | \|det(A + I)\| = 5 | the origin and the pair | the pair |
| A², period 2 | \|det(A² − I)\| = \|−5\| = 5 | the origin and the pair | the pair: two orbits {±v} of A |

- det(A − I) = −1 is a unit mod every N, so no level holds a nonzero untwisted fixed point.
- A nonzero twisted fixed point exists at level N iff 5 ∣ N. That follows from the Smith form diag(1, 5) of A + I
  (21cfbc3c2 § 1), and 5fef38dee checks it at N = 2, 3, 4, 5 and 15.

**So, on the closed torus, A's minimal periodic orbit is the origin, the zero line.** On the object's punctured fibre, A
has no fixed point, and its minimal periodic orbits are exactly the pair. P-721's "the line is a minimal periodic orbit
of the object's own dynamics" is exact only on the punctured fibre. On the closed torus, where P-721 counts, the same
words pick the origin.

**As dihedral representations** (the departure note § 1 and post hoc (5); S305t):
- For a fibred knot, coker(A + I) is H₁ of the double branched cover. For the figure-eight it is ℤ/5 (|det(A + I)| =
  det 4₁ = 5), and the cover is the lens space L(5, 2).
- The level-5 twisted fixed points are the characters of that group.
- **The four nonzero characters** correspond to the 20 surjective D₅ representations, five per character (the
  meridian's five possible reflections). Each pair ±v makes one conjugacy class, so there are two classes. These are
  the figure-eight's own Fox 5-colourings.
- **The zero** corresponds to the five trivial colourings: every meridian goes to one reflection. That is an abelian
  representation, the one every knot has.
- A D₅ representation, restricted to the fibre, is a character χ with χ∘A = −χ (the departure note § 1).

**As flat bundles** (B1733's flat line).
- B1733's covariance is exactly how the point w = ατ + b of ℂ/(ℤ + τℤ) moves under z ↦ z/(cτ + d). So the record's flat
  line is the Abel–Jacobi point, up to sign (B1653 writes w = ψ₁τ − ψ₂).
- That identification of flat lines with points is based at the puncture, the unique mapping-class-invariant point
  (B366). It commutes with the monodromy, since the monodromy fixes the puncture and preserves orientation (det A = 1).
  It sends the puncture to the trivial bundle.
- A flat U(1) line on the punctured torus extends uniquely over the puncture. The trivial bundle is therefore an
  admissible flat line, and the record computes the frame on it.

## 2. What follows, and what does not

**Three readings of "the line", and the zero in each:**
- **(a) A periodic point of the object's own dynamics, on the object's punctured fibre.** This is P-721's description,
  taken on the punctured fibre where its "minimal" is exact. The zero is excluded by topology: it is where the knot is,
  not a point of the knot's complement.
- **(b) A surjective dihedral representation.** The zero is excluded by surjectivity, a criterion: it is the abelian
  representation every knot has.
- **(c) A flat line on the fibre.** The zero is admissible, and "nonzero" is a premise.

**How the readings agree.**
- (a) and (c) agree on every line except the zero.
- On the five twisted fixed points, (b) agrees with both except at the zero.

**How the record selects the pair today.**
- It describes the pair in (a)'s and (b)'s terms, but each row states the nonzero step itself.
  - P-721 counts 5 on the closed torus and takes "the nonzero ones".
  - P-718 takes the order-5 lines by B1733's rule, which is (c), with nonzero imposed through the order.
- Under (a) on the punctured fibre, or (b) as surjective representations, that step is automatic.

**Computing the frame.** Computing it under (c) on a line selected by (a) or (b) is consistent, and it is what P-718
does. The selection excludes the record's zero-line configurations as candidates (B1809's Table T, B1810), not as frame
computations; those remain valid.

**Level 3** holds no line under (a) or (b).
- Under (a), its only twisted fixed point is the origin.
- Under (b), the figure-eight is not 3-colourable (det 5 is prime to 3).
- So the exclusion of level 3 in 21cfbc3c2 § 3 rests on the reading, which is choice 3 restated, not on a premise
  beyond it.

**So choice 3 is restated, not removed.** "A nonzero line" is the same choice as reading the line on the object's own,
punctured fibre (a), or as a representation that sees the knot (b), rather than as a bare flat bundle (c). The new
argument for (a) is that P-721's own words, "a minimal periodic orbit", hold only there.

**Nothing is said about the bit.** v and 2v are nonzero under every reading. The SM seat's § 355 finds that they carry
opposite CS, verified on main at S305y (P-718). So the bit may be the record's chirality bit.

## 3. The goal's choices after this note

1. (K).
2. Reading (ii).
3. **A nonzero line,** now stated in the object's terms: the line read on the punctured fibre (a), or as a surjective
   representation (b), rather than as a bare flat bundle (c).
4. Minimality, or the ladder. S305w derives R1 given minimality.
5. The departure: one departure, with its limit m → ∞ (which the read-out's uniqueness also needs, c6b813450), or least
   action under (ii).
6. The read-out's premises:
   - (N1) a point;
   - (N2) the Teichmüller history;
   - (N3) no arrow and no fibre orientation beyond M's, grounded in B716.
7. The bit.
8. P-722's remaining steps (R2's reading, R4).

## Disclosures

- **No new computation.** The topology is standard:
  - the fibred figure-eight and its fibre filling (B287);
  - H₁ of the double branched cover of a fibred knot as coker(A + I), with the sign that makes it ℤ/5;
  - dihedral representations as characters of that group.
- **The referee checked the topology independently,** outside the tree: the Seifert matrix and monodromy, the
  5-colouring and D₅ counts, and the absence of 3-colourings.
- **The first draft overstated, and the corrections are applied:**
  - It said the record's candidate "already uses" readings (a) and (b). It describes the pair in their terms but
    selects by (c), with nonzero stated.
  - It attributed (a) to P-721. (a) is P-721's description taken on the punctured fibre, which corrects P-721's count.
  - It said "only the bare flat-bundle reading admits the zero line" without saying that (b) excludes the zero only by
    requiring surjectivity.
  - It said level 3's exclusion rests "not on a further choice". It rests on the reading, which is choice 3 restated.
  - It dropped (N3) from the read-out's premises.
  - It missed B366, which already identifies the origin point with the puncture.
  - It made a level-3 "cusp field" observation, now dropped. The cusp is the only twisted fixed point at every level
    prime to 5, and P-721's "cusp field" is the number field ℚ(√−3), not the puncture.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE ZERO LINE IS WHERE THE KNOT IS (the owner: "Keep me on the choices"; choice 3; conceptual, no new computation) | "on the object's punctured fibre the monodromy has no fixed point, and its shortest periodic orbits are exactly the pair (period 2). P-721's "minimal periodic orbit" is exact only there: on the closed torus the minimal orbit is the origin, the zero line, where the filling's core passes. As a dihedral representation, "nonzero" is surjectivity: the zero is the abelian representation every knot has. As a bare flat bundle the zero stays admissible. Choice 3 is restated in the object's terms, not removed" | `relays/CHAT1_TO_CC_2026-11-06_THE_ZERO_LINE_IS_WHERE_THE_KNOT_IS.md` @ the commit adding it | — | P-721, P-718, B1733, B366, B287 | 2026-11-06 |

0 of 19.
