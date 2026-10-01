# B1507 — THE RECORD REREAD: the three on the root's 3-fold cover is the record's oldest generation idea (July, B326–B350), its fence was already Gate C, one element carries both the family rotation and the trinification (R64), I-14's 85 candidate gradings narrow to one (R68), s961 carries a deck-inverting isometry, and five statements are scoped or corrected

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (banked and relayed claims re-verified on this bench
with own code; corrections of record; no prediction sealed or run) · **Price: unchanged** · **Numbering:** B1507 (the owner's
"should we swipe the repo once more for forgoten work that enriches the picture substantially?", 2026-10-01).

## 0. Seen from above

The sweep read the record's work on the three generations, flavour, chirality and vacuum selection against B1506. It covered this
branch, main, the audit lane, the physics seat, the codex seat and outside-bench. Six findings change how the picture reads:

- **The idea is from July.** B335 (July) says "the three generations are related by the deck transformation of the 3-fold cyclic
  cover of 4₁". B326 has the deck acting irreducibly on (ℤ/4)². B343 and B345 drew its flavour consequences, and B350 (iv) proved the
  deck fixes no non-zero class on any level. None of B1270–B1506 cites B335, B343, B345 or B350.
- **The fence is from July too.** B521's Gate C ("INDEPENDENTLY CONFIRMED") says the deck acts as the scalar ω within one Eisenstein
  module, "never a generation-3". That is B1506's fence: a single E₆ vacuum carries one generation. Both rest on one fact, recomputed
  here: det(φ − 1) = −1 makes the deck fixed-point-free on every level, so every non-trivial character lies in a free orbit of three.
- **One element, two faces.** For an order-3 unit g of the golden E₈ (B1270), left multiplication is the family rotation of the plane
  ℤ[g] times an order-3 element of E₆ fixing no vector. Its lift is the trinification. B1271's family triplet and Gate C's "within
  one 27" are the two factors of one element: the physics seat's R64, verified here.
- **I-14's 85 candidates narrow to one.** Of E₆'s 40 trinification subsystems, exactly one is stable under g from both sides, and it
  is mirror-invariant (the physics seat's R68, verified here). I-14 stays UNEARNED.
- **s961 carries a deck-inverting isometry.** It has 12 of them, 6 orientation-preserving. That is the second half of B1391's named
  target, on the root's own cover. Whether such an isometry preserves B1506's orbits, giving S₃'s "2 + 1", is not computed here; it
  is registered as a lead to seal.
- **Corrections of record.**
  - B335's "the masses … are exactly degenerate" is overstated. A deck-invariant mass matrix forces a degenerate pair only when it is
    symmetric (B1362), and three equal masses only without inter-generation coupling.
  - The chirality map's C3 headline ("zero on every representation computed") is out of date by its own definition: B1378's orbit
    sum has N = +3 per sector. Its provenance line also claims citations it never makes.
  - B1504's two broad sentences hold for real lines and root lines only (the audit lane's R60/R61, verified here).
  - B1374 carries the lifted-scope "s961 = 0" that B1506 §6 corrected for main's B1427.
  - The short form of B1366 drops the Standard-Model-shaping condition that main's B1430 found necessary.

The price is unchanged: 4 axioms and 7 irreducible identifications. 0 of 19.

## 1. How the sweep was done

- **Instruments.** `scripts/checks/reverse_sweep.py` (44 settled arcs off every surface),
  `coverage_candidates.py --unrepresented` (156 arcs on no synthesis surface, 10 depended on) and `open_claim_sweep.py` (59 open
  claims with a matching settled arc).
- **Five reading lanes:**
  - the three and flavour;
  - chirality;
  - dynamics and vacuum selection;
  - the other seats;
  - the instruments' candidates.

  Each was given the B1506 picture and asked for quotations with file and line. The seat read LAW_MAP's generation rows, the
  philosophy notes and the July clusters itself.
- **Heads read:**

  | branch | head | date |
  |---|---|---|
  | this branch | ad64b558 | |
  | main | 987c0c8f | its last commit is 2026-09-18 |
  | the audit lane | 24356ebd | 2026-09-30 |
  | the physics seat | 659487bb | R72, 2026-09-06 |
  | codex | f7a49536 | |
  | outside-bench | 13d2c5b6 | for B1291 and B1321 |

- **Grades.** Every load-bearing statement below was either recomputed here (`verification/`, six scripts) or is quoted with its file
  and line and labelled as read.

## 2. The three on the root's 3-fold cover: July first, then September

**July.**
- **B326** (verified 2026-07-01). H₁ of the 3-fold cyclic cover is ℤ ⊕ (ℤ/4)². The deck acts as the companion of Φ₃, irreducible
  mod 4 and mod 2: "the three generations are bound into one irreducible ω-module".
- **B335:9.** "The three generations are related by the **deck transformation** of the 3-fold cyclic cover of 4₁." It records the
  cover's isometry group: order 24, abelianization (ℤ/2)², centre ℤ/2 (B335:28–30; its "dihedral-type" is loose: SnapPy's
  `is_dihedral()` is False, §6).
- **B343:10–19.** The Klein 2-torsion of (ℤ/4)² is 3-cycled with no fixed element, which forces exact tribimaximal mixing (θ₁₃ = 0,
  experimentally excluded). See §4.
- **B345.** The anti-diagonal texture. See §4.
- **B350 (iv).** "The deck action is fixed-point-free for every n, uniformly": det(A − I) = Δ(1) = −1 is a unit. Its own tier note
  adds that Δ(1) = ±1 for every knot, so this is generic to knots.
- **B502/B521 Gate C.** "The deck ℤ/3 acts as scalar ω-multiplication *within one* Eisenstein module." Fix = {0}, det(T − I) = 3,
  and 16 is not a cube, so the deck is "the trinification-3 acting within one 27, never a generation-3" (B521:63–74).
- **B715's coda** (2026-07-19). It kills chat-1's "ℤ/3 = A₄/V₄ location", which is exactly B1506's deck, through B685, but in a
  different role: cycling three quadratic fields, which no ℤ/3 can do, since Gal(ℚ(√−3, √5)/ℚ) = V₄. It also kills the cycling of
  the three H¹ classes on m004 by the block obstruction (§3).

**September.** B1273/B1274, B1356, B1361/B1362, B1364, B1378 and B1506 all use the same deck: m004 has one index-3 subgroup
(B1506 §9).

**Citations.** None of B1270–B1506, THE_SM_VERDICT, OPEN_LEADS or the chirality map cites B335, B343, B345, B350, Gate C or B715's
coda (grep). B326 is cited by B1273 and B1278, for the torsion only.

**Recomputed** (`deck_on_the_tower.py`; H₁(Yₙ) = coker(φⁿ − 1), the deck acting as φ):

| n | H₁(Yₙ) | order | deck-fixed elements | orbit sizes |
|---|---|---|---|---|
| 2 | ℤ/5 | 5 | 1 | 1 + 2·2 |
| 3 | (ℤ/4)² | 16 | 1 | 1 + 5·3 |
| 4 | ℤ/3 ⊕ ℤ/15 | 45 | 1 | 1 + 2·2 + 10·4 |
| 5 | (ℤ/11)² | 121 | 1 | 1 + 24·5 |
| 6 | ℤ/8 ⊕ ℤ/40 | 320 | 1 | 1 + 2·2 + 5·3 + 50·6 |

On Y₃:
- φ² + φ + 1 = 0, so the deck is the scalar ω.
- Gate C's det(T − I) = Φ₃(1) = 3 and det(φ − 1) = −1 are the same unit mod 4.
- (φ − 1)v has the order of v for every v, so the blocks of an orbit differ by characters of their own order (B1506's "order 4").
- The Klein 2-torsion {(0,0), (0,2), (2,0), (2,2)} is 3-cycled with no fixed element.
- Φ₃ is irreducible mod 2, and Δ = t² − 3t + 1 ≡ Φ₃ mod 4.

**Reading.** Gate C's fixed-point-freeness is not an obstruction to B1506's three. It is its cause. A scalar ω with N(1 − ω) = 3
prime to |H₁(Y₃)| = 16 fixes no non-zero class or character. So each of the 15 non-trivial characters lies in a free orbit of three
(B1506's loci orbits [1,3,3,3,3,3]), and the three blocks of an orbit are three different vacua, never three copies of one module.

Gate C (July), B715's coda (July) and B1506's fence (September) are three arrivals at one statement: the deck never makes three
generations inside one vacuum. B350's tier note calibrates it:
- **Generic to knots:** the free orbits, since Δ(1) = ±1 for every knot.
- **The object's own:**
  - the order-16 Eisenstein module (Δ ≡ Φ₃ mod 4, B326);
  - the uniqueness of the 3-fold cover among all 3-fold covers (det 4₁ = 5, so no S₃ quotient);
  - the 48 generation-shaped backgrounds that sit on the order-4 characters (B1506).

## 3. The record's other threes

Five threes on the record are not the deck's orbit:

- **The cohomological three** (B632, B656, B657, B662).
  - h¹(m004; 27) = 3 under the principal sl₂, one class per block of 27 = V₁₇ ⊕ V₉ ⊕ V₁ (LAW_MAP's "dimension grammar").
  - Recomputed (`principal_blocks.py`, Fox calculus on m004's Riley representation, p = 601, 1201, 1801): h¹ = 1 on each block.
  - B714's item 6′ and B715's coda: no symmetry or Hecke correspondence cycles them, because the blocks have different dimensions.
    LAW_MAP:153 places this as "generations = COUNT only, never a permutable triple".
  - B1506's triple is a triple of vacua, so that law holds per vacuum. LAW_MAP's rows 151/153 get a currency note.
- **The Eisenstein triplet** (B1138 §4, B1270/B1271). The (27,3) of E₈ ⊃ E₆ × SU(3), cycled by the founding ratio g. As 4d fields on
  the object it is one 27 and one 27̄ (N = 0, B1271). §5 places it.
- **The two-cusped three** (main's B1320/B1321, B1418:38, the physics seat's R72d).
  - It comes from fixed-point counts of order-3 isometries on two-cusped members. These members are "not covers of m004" (B1418:38).
  - It "costs the golden face" (B1321's addendum) and drops to |net| = 1 when the cusps are filled (R72:79).
  - B1390: in m004's class every three is a pullback of a one.
- **The trinification 3** (B305, B308). "The ω-triality … within one 27 … **not** a structure across generations" (B308:18–20). Also
  B1255:68: "Three generations cannot live inside one 27" (I-24, REFUTED).
- **P015's three.** The contracting dimension of the golden Rauzy fractal: spatial, not generations.

## 4. Flavour: what the July cluster knew, and one overstatement

**Recomputed** (`flavour_cluster.py`):
- A matrix commuting with the cyclic permutation of the generations is a circulant circ(c₀, c₁, c₂). It is diagonal in the charge
  (Fourier) basis, with eigenvalues c₀ + c₁ωᵏ + c₂ω²ᵏ.
  - Generic: three distinct singular values (50 of 50 random draws).
  - Symmetric (c₁ = c₂, as E₆'s symmetric cubic gives): eigenvalues c₀ + 2c₁, c₀ − c₁, c₀ − c₁, a degenerate pair.
  - All three equal only when c₁ = c₂ = 0, with no coupling between generations.
- **B345's texture is B1362's circulant.** In the charge basis circ(x, y, y) is exactly [[x + 2y, 0, 0], [0, 0, x − y], [0, x − y, 0]].
  Its support is B345's allowed set {(0,0), (1,2), (2,1)}, so B345 had B1362's degenerate pair in July.
- **B335's sentence is overstated.** B335:10–13 says "every real geometric invariant … is ℤ/3-equal across the three generations — so
  the masses (… singular values of any Yukawa) are **exactly degenerate**."
  - **Right for:** the vacuum's isometry-invariant functionals (volume, Chern–Simons, length spectrum), which are equal across an
    orbit (§6).
  - **Wrong for masses.** B325 (July) had already shown that "a generic complex ℤ/3-invariant circulant has two distinct light
    singular values".
  - **The correct mass statement** is B1362's: a symmetric deck-invariant Yukawa has a degenerate pair, so a kept deck must be broken
    at order one. (Correction of record; ERROR_LEDGER.)

**Read, not recomputed:**
- **B343 (July).** On the Klein 2-torsion the unbroken deck selects no column, so the full Klein survives and mixing is exactly
  tribimaximal: θ₁₃ = 0, against the observed 8.57°. With B1361/B1362's mass-side refutations, the record has the unbroken deck
  refuted from the mixing side as well. Scope:
  - the identification of the object's Klein group with the neutrino residual symmetry is B343's own [LEAP] (S048);
  - it is stated on the order-2 orbit (B1273's three flat directions), not on the order-4 orbits that hold B1506's backgrounds.
- **B342** (would-be TM2) was corrected by B343; its `superseded_by` is now set.
- **B687:44–45.** Koide's 2/3 is "120°-TAUTOLOGICAL (holds for any three-fold structure)". Any deck orbit meets it, so it is no
  evidence.
- **B1033's addendum.** "SU(3)_F is a GLOBAL family symmetry acting on the space of generations, NOT the internal SU(3) index
  structure of the 27."

## 5. One element, two faces: R64 and R68 recomputed

Run with B1270's exact icosian E₈ (`founding_ratio_frames.py`; two different order-3 units, each from scratch).

**R64.** Left multiplication by an order-3 unit g maps the family plane ℤ[g] to itself (1 ↦ g ↦ g² = −1 − g, the 120° rotation).
It acts on E₆ = ℤ[g]^⊥ without a fixed vector (g − 1 is invertible in the definite quaternion algebra):
- on E₆'s 72 roots: no fixed root, 24 free orbits of three, B(r, gr) = −1 for every root;
- an order-3 element of W(E₆) without eigenvalue 1 is the regular class (characteristic polynomial (x² + x + 1)³), whose lift is the
  principal order-3 element;
- its centraliser's roots are those of height ≡ 0 mod 3: 9 positive roots, dimension 24, simple components of 6, 6 and 6 roots.
  That is A₂³, the trinification.

So B1271's family triplet (the A₂ factor) and Gate C's and B308's "within one 27" (the E₆ factor) are the two factors of one element
(the physics seat's R64:19, 26; main's B1306 FINDINGS_C verified its A₂ half).

**R68.** There are 120 A₂ subsystems in E₆ and 40 trinification frames A₂³. Under the founding ratio:

| condition on an A₂³ ⊂ E₆ | count |
|---|---|
| stable under left multiplication by g | 4 |
| stable under right multiplication by g | 4 |
| stable under both | 1 |

- Right multiplication permutes the four left frames as a 3-cycle and a fixed point.
- The two-sided frame is invariant under quaternion conjugation, the mirror.

So I-14's measured multiplicity falls 85 (B1264) → 40 (R65, verified by main's B1306) → 4 → 1.

**What this does not do** (R68's own §2):
- It exhibits the subsystem and the element that selects it.
- It does not show that the physical trinification is this subsystem: that is the listener-map half of I-14.
- It does not give a map from I-14's L4 (the commensurator's Eisenstein unit on the cusp) to g.
- I-14 stays **UNEARNED**, with multiplicity 1 (note on IDENTIFICATION_LEDGER).

**How it relates to the deck.** The deck is the base's ℤ/3 (A₄/V₄ of the 2T holonomy). g is the gauge side's. Gate C read the deck's
scalar ω as E₆'s ω-grading; that reading is I-14's identification, now an identification of one specified thing rather than of 85.

## 6. Two readings of the cover's three, the one bit, and what the record says about selecting

**Two readings, one object.**
- **R1 (B1506).** An orbit is three vacua with one generation each.
- **R2 (B335:21–22; B1390:106; B1391:35–41).** The orbit summed into one configuration carries the deck's regular representation:
  "one zero mode per character: a ℤ/3 family charge, not three identical copies" (B1390).
- R2 is R1's orbit taken in one configuration, which needs structure group E₆ ≀ ℤ/3 (B1506 §5).
- The invariant projection keeps the charge-0 mode, one generation: B1356's descent, Shapiro, and the audit lane's DECK gate
  (`received_r58/coupled_boundary_gate_2026_09_27_DECK_FINDINGS.txt`, cited, not re-derived): "Ordinary geometric invariant projection
  retains J0 … It therefore cannot retain an upstairs target three … This does NOT exclude charged states of a finite gauge group …
  The physical interpretation must be declared before that count is claimed as generations." B1506's sweep head contained this gate
  but did not cite it (E54).

**The deck-inverting isometry, recomputed** (`deck_inverting.py`, SnapPy 3.3.2):
- **m004.** Of its eight isometries (D₄), four negate the meridian, two of them orientation-preserving: the knot's inversions.
- **s961.** It is the only cyclic 3-fold cover. Isom(s961) has order 24 = 8 · 3, so every isometry is a lift. It is nonabelian and
  not dihedral, with centre ℤ/2 and abelianization (ℤ/2)², as B335 recorded.
- **The deck.** The multiplication table has exactly two elements of order 3. Both act trivially on the cusp homology (they are
  translations of the cusp) and they form a normal subgroup: the deck.
- **The inverting elements.** Twelve elements conjugate τ to τ². Six of them are orientation-preserving, and all twelve negate the
  meridian: the lifts of m004's four meridian-negating isometries.
- **B1391's target.** OPEN_LEADS:3255 names "A member Q with |N(Q)| = 1 whose free ℤ/3 cover carries a deck-inverting isometry".
  - Its second half holds on m004's own cover.
  - Its first half is not met by m004 in the seat's frame (B1368). In main's frame the count is that of the induced object, whose
    structure group is E₆ ≀ ℤ/3 (B1506 §5).
- **Not computed: an open outcome, registered to seal first.** Does an orientation-preserving deck-inverting isometry map a B1506
  orbit to itself? If it does, the orbit's three carry S₃'s "2 + 1" (B1391:38–41; Pakvasa–Sugawara 1978; Harari–Haut–Weyers 1978).

**The one bit, read with the record's earlier judgments:**
- **B719 (July 20), "MULTIPLICITY/SCALE IS THE OBSERVER'S"** (LAW_MAP:158): "the COUNT is the observer's", the covering degree
  imported. B1506's bit (gauge the root's deck and count one on m004, or keep it and count three on s961) is that datum, made sharp.
  An orbit of three counts gcd(n, 3) ∈ {1, 3} on every level, so the choice is between two counts and no level gives another.
- **B1225:65, 80–82.** "An invariant selector cannot pick a point of its own orbit." A selector from non-invariant data "is not
  forbidden by this argument; it is simply not the object's."
- **THE_FORCED_AND_THE_FREE §1, §3, §5.** Each orbit is a free ℤ/3-orbit: a torsor of vacua. The object fixes the counting prior,
  not the point. This is a seventh instance of the torsor pattern (a reading, tagged as such).
- **The record's vacuum convention.**
  - B1279:7–9: "lines related by a symmetry of Y₉ are the same vacuum". Likewise B1302's addendum on the 768 and B1277:140.
  - Under that convention a B1506 orbit is one vacuum up to isometry. B1506's "three distinct vacua" means distinct up to gauge.
  - Under either convention there is one generation per vacuum.
- **The audit lane.**
  - PHYSICS_MISSION:21–22: "m004 remains a conditional minimum in its specified sector, not an assumed universal physical root".
  - PHYSICS_MISSION:126–127: "Do not require a unique vacuum if a physical law legitimately admits several".
  - GOAL_VERDICT:361–367: "Invariant-selector statements alone neither supply a vacuum nor forbid spontaneous breaking".
  - ROOT_SCOPE_AUDIT:160–161: "(x²−1)² is symmetric, with two nonsymmetric minima".
  - So B1506's kill form "symmetry cannot select" is not "nothing selects". A kept deck is broken spontaneously, and the object does
    not say which vacuum.
- **The record's explicit deck breakers** (B1364:32, 58; B1365:25–27). They choose inside the same order-4 orbits that hold s961's
  backgrounds (B1506 §9). The choice is moved, not made.
- **No functional on the record weights the three** (lane 3).
  - No Chern–Simons, torsion or η value has been computed on any generation-shaped background.
  - Every isometry-invariant functional is equal across an orbit: B335's argument, applied where it holds.
  - The named weighting dynamics are uncomputed: the instanton superpotential (L201, L209(i)) and L72's CS-functional programme.

## 7. Chirality: the map's headline, the walls against the carrier, and three scopes

**The chirality map's C3 headline is out of date by its own definition.** Its rows say "ZERO on every representation computed"
(docs/CHIRALITY_MAP_2026-09-06.md:14), "No row is nonzero" (:67) and "vector-like on every representation it supplies" (:456).
- The map's N is h¹(M; V) − h¹(M; V*).
- B1378's recorded run (`deck_triplet_run.txt`, Sec. 1b) gives, in every sector: V = (a₀, a₁, t₀, r₁) = (0, 6, 3, 6) and
  V* = (0, 3, 3, 0). So N = +3 on the M₆ orbit sum: +1 per background.
- These are the non-split modules of the cusped covers (main's B1418; B1374–B1378; B1506).
- A currency note is added. The zero rows hold for the representations the map computed by 2026-09-06.
- Its provenance line (:461) lists 57 arcs as "cited above". 20 of them are not cited in the body (B127, B128, B134, B144, B193, B318,
  B612, B1036, B1064, B1098, B1145, B1183, B1222, B1226, B1227, B1239, B1255, B1257, B1264, B1278). The line is split into cited and
  retrieved (ERROR_LEDGER).

**The walls against the carrier** (the lane's reading, condensed):

| wall | B1378/B1506's carrier | why |
|---|---|---|
| \|I\| ≤ 2 (B1377, B1381) | falls under | \|count\| = 1 |
| B1297's T4 | falls under | for rank-one sectors |
| W-boundary | falls under | saturated: t₀ = 3 |
| B1506's family-frame fence | falls under | |
| W-closed | evades | the carrier is cusped; but its derivation uses irreducible V (B1260:18), and native non-split modules on the closed Yₙ were never examined (lead) |
| W-self-dual | evades | through the ℂ*² characters |
| W-Hermitian | evades | non-unitary (B1374:109) |
| W1/W2, the θ-odd germ | evade | |
| the seat's-frame walls | evade | a different index |
| B1368 | evades | a cover, main's index, non-lifted backgrounds |
| B1367 | evades | bulk matter: its own named door |

**B1504 is scoped by the audit lane's R60/R61 (2026-09-30, uncited until now).** Recomputed (`end_lines.py`):
- (a) **The root lines.** "The completion must pick one of the three root lines" (B1504:44, :210) holds for the root-line orbit, which
  is B1502's smooth phases. It does not hold for every ideal line. On ℤ[ω] the order-3 rotation 3-cycles every primitive line, and
  (1, 3)'s orbit {(1,3), (3,2), (2,−1)} is another triple.
- (b) **Complex lines.** The lattice lemma excludes real invariant lines only. In an orthonormal frame of the link torus, the
  rotation's complex eigenlines w = (1, ∓i):
  - are invariant under rotations of order 3, 4 and 6;
  - satisfy the combined Hodge-and-conjugation reality C u = u, each with its phase;
  - carry zero Hermitian current.

  The rotation chooses neither line.
- (c) **The marking.** T1's "no datum at a cusp point can depend on it" holds for laws that descend to the unmarked manifold. Marked
  equivariance is a different requirement (R60, read).

B1504's verdict, that the end's chirality is an input, stands within its real self-dual completion category. It is not shown for
complex domains. A scope note is added to B1504 (ERROR_LEDGER; caught by the audit lane).

**Main's B1430 (2026-09-18) verified B1366 from scratch.**
- It reproduced 120 A₂'s in one orbit, 720 commuting pairs in one orbit, and three hypercharges.
- It found that uniqueness holds given the Standard-Model shaping of the 27. Without it there are 8 177 branchings of the 27 over
  28 513 hypercharge directions.
- B1366's claim line carries that condition. The short form "the Standard Model embeds in E₆ once up to conjugacy" on this branch's
  surfaces does not (currency note).

**B1506's equal sign split has a mechanism on the record that B1506 did not join.** The split (P2: 24/24, 128/128, 200/200,
1 080/1 080) could follow from two facts:
- Every cyclic cover is amphichiral: main's B1324 (its table at l.21: nine cyclic covers to degree 10, none chiral) and
  B1427:24; s961 here, by SnapPy.
- B1297's T6 flips the index under orientation reversal with complex conjugation (B1297:66–68).

Joining them would make P2 a theorem. That needs a check that orientation reversal with conjugation maps the generation-shaped census
to itself (lead).

**Lifted-scope zeros.**
- B1374:145 says "s961 = Y₃ (0 at N = 12)". That holds for lifted modules only, as B1506 §6 found for B1427. It also uses the wrong
  name: s961 is M₃ and Y₃ is its filling. A note is added.
- Main's B1418:33 ("s961 … 0 of 2 511") and B1297's 2026-09-16 addendum carry the same lifted-scope zero. They are relayed in the
  letter.

**Main's uncited joins:**
- B1305:41–43: "A = ℤ torsion-free ⇒ net chirality 0 on every closing". The σ, selector and chirality walls are one theorem in three
  value groups.
- S13 (main's CHANGELOG:157): "the reducible index can fire ONLY through the twist".

Both are cited here and not re-derived.

## 8. Record hygiene

**Changed:**
- B342's `superseded_by` is set to B343. B343 "Corrects B342", and its own `supersedes` field already names B342.

**Noted, not changed:**
- B770's census grades OI-129 (Gate C) as specialist work. B521 records Gate C as CLOSED.
- B6: `arc_verdict.json` says OPEN; its FINDINGS say "STALLED".
- B625's 3 | κ boundary was later found to be "a PRESENTATION ARTIFACT" (B666 WAVE3_FINDINGS:57); its `superseded_by` is null.
- THE_SM_VERDICT credits V5 to B978. The computing arc is B974 (SYNTHESIS.md:247–249), whose anomaly caveat (:238–241) is missing
  from the verdict's L132 row.
- LAW_MAP carries no row for this seat after B1304 (B1351–B1506). That is a currency debt, registered as a lead.

## 9. What it means

1. **The three on the root's cover is the record's oldest generation idea.** B1506 completes it in the index frame. It adds the level
   law for induced objects of any orbit size, the non-lifted census and the triplet's place, and it does not originate it. B1506 §7's
   remaining novelty is narrowed accordingly (E68).
2. **The fence has one mechanism.** The deck is the scalar ω on an Eisenstein module of order prime to 3 (det(φ − 1) = −1 on every
   level), so it never yields three generations inside one vacuum. July and September agree, and the mechanism is generic to knots.
3. **An unbroken deck is refuted twice:** by masses (B1362's pair) and by mixing (B343's θ₁₃ = 0, under B343's own [LEAP]).
   - A kept deck is broken at order one, spontaneously.
   - The record's only explicit breakers move the choice rather than make it.
4. **On the gauge side the object supplies the point.** One element carries the family rotation and the trinification (R64), and it
   selects one trinification frame of 40 (R68). The base-to-gauge identification (I-14) remains unearned.
5. **The one bit is B719's datum, sharpened to {1, 3}.** The audit lane's gate asks that it be declared, not derived. No functional
   on the record distinguishes the three vacua, and none will (every isometry-invariant one is constant on an orbit).
6. **The flavour route has a concrete next step on the root's own cover.** s961 has deck-inverting isometries. If they preserve the
   orbits, the record's three carries S₃'s "2 + 1", the classic starting point of S₃ flavour models (B1391). That is a structure, not
   a value: the hierarchy would still be a breaking effect.

## 10. Leads registered (to seal before anything is computed)

- (i) **The deck-inverting isometry on B1506's orbits.**
  - Does an orientation-preserving lift of the knot's inversion map a generation-shaped orbit on s961 to itself, as a set of three
    backgrounds up to gauge?
  - If yes, the orbit is an S₃-set and its three carry "2 + 1". If no, the inversion pairs orbits.
- (ii) **P2 as a theorem.** Does orientation reversal with conjugation (amphichirality and B1297's T6) map the generation-shaped census
  to itself with signs flipped, on every level?
- (iii) **The closed covers.** Do the closed Yₙ carry native non-split modules? W-closed's derivation (B1260:18) assumes irreducible V.
- (iv) **LAW_MAP currency.** Rows for B1351–B1507.

## 11. Corrections of record

- **E68 instance.** B1506 re-derived the July cluster without citing it: "three = the deck of the 3-fold cover" (B335), the
  fixed-point-free deck on every level (B350 (iv)), the fence (Gate C, B715's coda) and the DECK gate. B1361/B1362 likewise did not
  cite B345 or B325.
- **Correction of record (another seat's July arc).** B335's "exactly degenerate" is overstated (§4).
- **This seat's chirality map:**
  - its C3 headline is out of date (§7);
  - its provenance line claims 20 citations the body does not make.
- **B1504: two scope notes**, caught by the audit lane's R60/R61 (§7).
- **B1374's lifted-scope zero** and its s961 = Y₃ name (§7).

## Verification

- `verification/deck_on_the_tower.py` (`deck_on_the_tower_run.txt`): the deck on H₁(Yₙ), n = 2–6; Y₃'s scalar ω; Gate C's unit; the
  Klein 3-cycle.
- `verification/principal_blocks.py` (`principal_blocks_run.txt`): h¹(m004; V₁₇, V₉, V₁) = 1, 1, 1 at three primes.
- `verification/flavour_cluster.py` (`flavour_cluster_run.txt`): the circulant facts and B345's texture.
- `verification/founding_ratio_frames.py` (`founding_ratio_frames_run.txt`): R64 and R68 on B1270's icosian E₈, for two order-3 units.
- `verification/deck_inverting.py` (`deck_inverting_run.txt`): Isom(m004) on the meridian; Isom(s961), its deck and the inverting
  elements.
- `verification/end_lines.py` (`end_lines_run.txt`): R60's root-line orbit and R61's complex lines.
- Lock: `tests/test_b1507_the_record_reread.py`. Every script is live: all six together take about 10 s.

**Sources.**
- **Read and quoted** (this branch): B305, B308, B324–B345, B350, B502/B521, B625/B666, B687, B714, B715, B719, B770, B974, B1033,
  B1225, B1255, B1264, B1270–B1274, B1277, B1279, B1302, B1356, B1361–B1367, B1374, B1378, B1390, B1391, B1504, B1506.
- **Main:** B1297, B1305, B1306, B1320/B1321, B1324, B1418, B1427, B1430 and CHANGELOG S13.
- **The audit lane:** the DECK gate, PHYSICS_MISSION, GOAL_VERDICT, ROOT_SCOPE_AUDIT, END_LAW (R60) and FERMION_END (R61).
- **The physics seat:** R64, R65, R68 and R72.
- **Recomputed here:** everything in the six scripts.
- **Nothing merged.**
