# W-F17: second computations for four of GENESIS's "computed nowhere yet" items. The finite quotients and E18–E19 agree with agy-exp's numbers. The class-index frame on m369 and s639 is non-zero on 40 and 72 record modules. The metallic trace maps' fixed loci are purely one-dimensional at m = 1–4 and 6, with κ varying on every component and the common point always on a curve, so B130's "no forced choice" holds with isolated points allowed

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). This note answers card W-F17 except m = 5 (post hoc 1, under way)
(`relays/cards/CHAT1_W-F17_second_computations_for_x_never.md`, 39ed2a525; amended before the run at 5c6becb1d to
take m = 1 to 6). It is homework the author asked for: main records that each X-NEVER item needs a second computation
before it enters the table (agy-exp's page, M20).

**How it was checked.** Computed once, on this seat's own code; expectations committed first; tested against planted
errors (12 plants, all caught).
- **The sealed run.** The script `wf17_checks.py` (sha256 `15dde5a3…0a2fb381`, pushed at 5c6becb1d) was run once.
  Its output was committed (9bcc0171a) before it was read.
- **Before the seal,** only the script's control paths were run: golden level 4, the group constructions and a toy
  ideal. No target was computed.
- **Not blind.** Items 1 and 4 are not blind: agy-exp's numbers had been read through the mask before the card. Item 3's
  numbers were masked. Item 2's comparison number (agy-exp's "8 and 16") was seen.
- **The method.** Exact arithmetic, with one exception: the quaternion groups are generated in floating point, their
  elements identified by rounding to 9 digits; their tables are then checked exactly (order, associativity on all
  triples, element orders, the same counts as the matrix groups):
  - finite group tables;
  - ranks over two prime fields (180001 and 2400001);
  - Groebner bases over ℚ.

  No census software is used, so the census labels m369 and s639 are agy-exp's and are not checked here. The states are
  built from their words.
- **A second computation.** The referee of this note recomputed all four items on its own code, and every count agrees
  (§ 6).
- **One expectation not met as written** (T4's line count at m = 4, § 3). m = 5 did not finish within the run's budget
  (§ 3). Post hoc 1 is committed for both (4f4f0af7b, not blind).

## 1. Finite quotients onto the binary polyhedral groups (N2's abstract part)

Each group is built twice: as unit quaternions, and as a matrix group over a finite field (SL(2, 3); a subgroup of order
48 of SL(2, 7); SL(2, 5)). The two constructions have the same element-order histograms. Every table is associative
on all triples.

| state (word) | 2T: Hom / Epi | 2O: Hom / Epi | 2I: Hom / Epi |
|---|---|---|---|
| m004 (+LR) | 72 / 48 | 96 / 0 | 600 / 0 |
| m369 (−LLRLR) | 288 / 96 | 864 / 96 | 2,400 / 480 |
| s639 (−LLLRLR) | 168 / 96 | 192 / 0 | 1,920 / 960 |

- **The two constructions** give the same counts everywhere (Q2).
- **Every word variant gives the same counts as the word** (Q4): each cyclic rotation, the L ↔ R swap and the reversal.
- **The divisibility checks hold** (Q3):
  - |Hom| is divisible by |H| (Solomon's theorem: three generators, two relators);
  - |Epi| is divisible by |Aut(H)| = 24, 48, 120 (counted here).
- **The built automorphisms** abelianise to the words' matrices, with fibre torsion 1, 12 and 15 (Q5).
- **Against agy-exp:**
  - Its m004 counts (homomorphisms and surjections) and its surjection counts for m369 and s639 are the same as
    these, all twelve.
  - The homomorphism counts for m369 and s639 were not in the part of its note this seat read.
- **Up to automorphisms of the target:** m004 has 2 quotients onto 2T; m369 has 4, 2 and 4 onto 2T, 2O and 2I; s639 has
  4 onto 2T and 8 onto 2I.

## 2. The class-index frame on m369 and s639 at their own level (GENESIS § 8, line 2)

The construction is W-F9's, at level 1 of each state's own monodromy:
- record characters of the fibre torsion, trivial on μ = g⁻¹t, where g conjugates λ = [a, b] to its image;
- record modules V(ℓ, α);
- I(V) = n(V) − n(V*).

| state | fibre torsion | record characters (with a class) | record modules | I = +1 / 0 / −1 |
|---|---|---|---|---|
| control: golden level 4 (+RLRL) | ℤ/5 | 4 (4) | 12 | 4 / 4 / 4 (W-F9's, reproduced) |
| m369 | ℤ/12 | 11 (11) | 110 | 20 / 70 / 20 |
| s639 | ℤ/15 | 14 (14) | 182 | 36 / 110 / 36 |

- **The record characters.** Every one has a class non-zero on λ, as W-F6's gap law says for an orientable state (C1).
- **The modules.** All satisfy the relators (C2), and the two primes give the same census (C2).
- **Duality.** I(V(ℓ, ℓα⁻¹)) = −I(V(ℓ, α)) on every module (C3).
- **The firing law** n(V(ℓ, α)) = [s(α) = s(ℓ)] (B1438) holds on every module of both states. It was reported, with no
  expectation.
- **The plant fired.** Each state's characters, used on the opposite-sign word's group, fail the relators: on 10 of 11
  characters (m369) and on 14 of 14 (s639).
- **Against agy-exp.**
  - Its note gives "8 and 16 own-level F-CI backgrounds" (also called generation counts) for m369 and s639.
  - This census has 40 and 72 modules with I ≠ 0. The numbers differ, and the definition behind agy-exp's count was not
    read here, so whether the two count the same thing is open.
  - Main or agy-exp should name that definition before either number enters the table.

## 3. The metallic trace maps' fixed loci, component by component (B130's question, isolated points allowed)

**The map and the ideal.**
- The map is B130's φ_m = Ta^m ∘ Tb^m on (x, y, z) = (tr a, tr b, tr ab), with κ = x² + y² + z² − xyz − 2.
- The fixed ideal is generated by Tb^m(p) − Ta^{−m}(p). It is the same ideal as φ_m(p) − p, checked for m ≤ 3 (T1).

**How the components were checked.**
- Components over ℚ come from factor-splitting of Groebner bases.
- Each is checked to contain the ideal, to be one-dimensional and to be ℚ-irreducible: a plane slice gives a single
  Galois orbit.
- **Completeness.** In two independent draws, 1 lies in I + ⟨1 − wF⟩, where F is a product of random members of the
  curves. So every fixed point lies in the zero set of one of the listed component ideals. The test is randomised, and
  it cannot see a point of such a zero set that lies off its curve; the sealed run did not check that the component
  ideals have no zero-dimensional part.

| m | components over ℚ | lines (z free unless stated) | the other curve: degree; contains (0,0,0); contains (2,2,2) | degree of I = sum | points on κ = 2 (m² + 2) |
|---|---|---|---|---|---|
| 1 | 1 | none | 2; yes; yes ({x = z, yz = y + z}) | 2 | 3 (3) |
| 2 | 2 | x = y = 0 | 4; no; yes ({x² = z²/2 + 2, yz = 2x}) | 5 | 6 (6) |
| 3 | 2 | x = y = −1 | 5; yes; yes | 6 | 11 (11) |
| 4 | 4 | x = y = 0; **x = z = 0 (y free); y = z = 0 (x free)** | 8; no; yes | 11 | 18 (18) |
| 5 | not finished within the run's 1,800 s; post hoc 1 under way | | | | |
| 6 | 6 | x, y ∈ {1, −1} (four lines); x = y = 0 | 16; no; yes | 21 | 38 (38) |

**What held, at m = 1 to 4 and 6:**
- **T5:** every component is one-dimensional, and the completeness test holds in both draws. By the caveat above, that
  alone does not exclude an isolated point. It is excluded as follows (after the run):
  - κ is invariant, so a fixed point where dκ ≠ 0 is not isolated: an isolated fixed point on its level surface has
    positive index and persists on nearby levels.
  - An isolated fixed point is therefore a critical point of κ: (0, 0, 0), or (±2, ±2, ±2) with an even number of minus
    signs.
  - Each of these that is fixed lies on a curve: the origin on x = y = 0 at even m and on the main curve at m = 1 and
    3; (2, 2, 2) on the main curve at every m; the other three, fixed only at even m, on the main curve (the referee's
    check, by a Groebner certificate).
  - So there is **no isolated point**.
- **T7:** κ takes infinitely many values on every component.
- **T6:** the points on κ = 2 number exactly m² + 2.
- **T2 and T3:** m = 1 and m = 2 are exactly as derived by hand (T2's {z = x, xy = x + y} is the same curve as the
  table's).
- **The plants:**
  - the line {x = y = z} is rejected at every m;
  - the completeness test fails when the first curve is left out, at every m with two or more.

**Not met as written: T4's line count at m = 4.**
- The header predicted the lines {x = r, y = r′} (r, r′ roots of gcd(S_{m−1}, S_m − 1)) and, for even m, {x = y = 0}.
  It counted them over ℂ as 0, 1, 1, 1, 4, 5.
- The predicted lines all lie in the fixed locus. But the sealed check compared the script's evaluation of the formula
  with the header's hand evaluation of the same formula, never with the lines among the components found. It could not
  detect a line the formula misses, and the output prints T4 as holding.
- Read against the components, m = 4 has two lines more than predicted: {x = z = 0} and {y = z = 0}.
- By hand:
  - Ta fixes (x, 0, 0) pointwise, and Tb moves it with order 4: (x, 0, 0) → (0, 0, −x) → (−x, 0, 0) → (0, 0, x).
  - So φ_m fixes that line exactly when 4 divides m: at m ≡ 2 (mod 4) Tb^m sends (x, 0, 0) to (−x, 0, 0), and at odd m
    to (0, 0, ±x), which Ta^m moves to (0, ±x, 0). The line (0, y, 0) behaves the same way, with Ta and Tb exchanged.
  - Post hoc 1 (H2) checks this at m = 2, 4, 6 and 8.
- At m = 6 the count is as predicted.

**Against agy-exp (read through the mask after this run's output was committed).**
- Its note gives the curves' projections to (x, y), with their digits masked to this seat: xy − x − y at m = 1; a
  polynomial of the shape x^# y^# − #x^# − #y^# with a line (#, #, z) at m = 2; and one with a line at m = 3.
- The table's m = 1 projection is xy − x − y = 0, and its m = 2 projection is x²y² − 2x² − 2y² = 0 with the line
  (0, 0, z). Both are consistent with what the mask shows. Post hoc 1 (H3) checks the m = 3 projection against the
  mask's reading of agy-exp's polynomial.
- Its count of isolated points is masked to this seat, so it is not compared.

## 4. E18 and E19

- **E18.**
  - SL(2, ℤ) has 308 matrices with entries in [−5, 5]. Their traces are symmetric about 0.
  - SE1 keeps 28 of them (trace 1: 12; trace 3: 16), and McKay keeps all 28 (N = 3 and 5).
  - The hyperbolic survivors are the 16 of trace 3 (D2).
- **E19.**
  - At k = −2 there are 17 integer points in [−10, 10]³: the origin, the four even sign changes of (3, 3, 3), and the
    twelve of (3, 3, 6) and its permutations (D1).
  - At k = +2 there are 134.
- **Against agy-exp:** all three counts are its own.

## 5. What it means

- **B130's question, with isolated points allowed, is answered at m = 1–4 and 6** (m = 5 pending).
  - A forced choice in B130's sense needs an invariant with finitely many values on the fixed locus and no symmetry
    relating them.
  - The fixed locus has no isolated point, and κ varies on every component. So no component gives κ a discrete value.
  - B130's "κ is free" held on the locus as a whole. It now holds component by component.
- **The common point is not isolated at any m computed.**
  - At odd m (1 and 3) the origin lies on the main curve.
  - At even m it lies on the line x = y = 0, where tr a = tr b = 0 (a and b of order 4) and tr ab is free.
  - So the point where W-F15 placed the completed cancellation is, for each metallic map computed here (m = 1–4 and
    6), one point of a family, not a value the map forces.
- **The lines are finite-order families.**
  - On the lines {x = r, y = r′} a and b have finite order (traces 2 cos(2πj/m), and 0 at even m), and the trace of ab
    is free.
  - At m ≡ 0 (mod 4) two more lines appear: on {x = z = 0} it is a and ab that have order 4 (tr b free), and on
    {y = z = 0} it is b and ab (tr a free).
- **These are statements about the trace ring.** They carry no physics reading. The firewall is untouched: no data, no
  τ, no frame value.
- **Item 2** adds the class-index frame on two states outside m004's levels. The frame is non-zero on both, with the
  duality symmetry and the firing law holding as they do at the golden levels.
- **Items 1 and 4** now carry a second computation for the fifteen counts compared (twelve in item 1, three in item 4);
  agy-exp's are reproduced exactly. The six homomorphism counts for m369 and s639 have no comparison yet.

## 6. Typed

| statement | how checked |
|---|---|
| § 1's table | computed once; expectations committed first (not blind); tested against planted errors (1, caught); two constructions of each group; agy-exp's twelve counts (m004's homomorphisms and surjections; m369's and s639's surjections) recomputed independently; all 18 counts recomputed independently by the referee (quaternions over finite fields) |
| § 2's census on m369 and s639 | computed once; expectations committed first (C1–C3 by hand); two primes; tested against planted errors (2, caught); the control reproduces W-F9; recomputed independently by the referee (its own cohomology code, two other primes) |
| § 3, m = 1 to 4 and 6 | computed once; expectations committed first (blind); tested against planted errors (P3 at 5 m, P4 at 4 m, all caught); consistent with agy-exp's projections at m = 1 and 2 as far as the mask shows them; recomputed independently by the referee (degrees, lines, points on κ = 2, ℚ-irreducibility, from φ_m(p) − p built directly) |
| § 3, the extra lines at m = 4 | computed once (the sealed run; not predicted) |
| § 3, those lines fixed exactly when 4 divides m | derived after the run; recomputed independently by the referee (m = 1 to 12); post hoc 1 (H2) committed before its run |
| § 3, no isolated point | the sealed completeness test plus the critical-point argument (after the run); the five critical points recomputed independently by the referee at m = 1 to 4 and 6 |
| § 4 | computed once; expectations committed first (not blind); agy-exp's three counts recomputed independently; recomputed independently by the referee |
| B130's question answered component by component (§ 5) | a reading of § 3 |

## 7. Files

`relays/chat1_2026-11-14_wf17/`: `wf17_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf17_checks_out.txt`,
`wf17_checks_err.txt` (empty), `wf17_posthoc1.py` (committed before its run).

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.

## Addendum: post hoc 1 (committed before its run at 4f4f0af7b; not blind)

The run's output was committed (9e9f4b871) before it was read.
- **H2 holds.** The lines {y = z = 0} and {x = z = 0} lie in the fixed locus at m = 4 and 8, and not at m = 2 and 6. This
  is as the hand argument says: exactly when 4 divides m.
- **H3 holds.** The m = 3 curve's (x, y) eliminant is x²y² − x²y − x² − xy² + xy + x − y² + y. It equals agy-exp's
  polynomial for m = 3, read through the mask with its exponents as 2.
- **H1: m = 5 did not finish within 6,900 seconds** (with the sealed functions, unchanged). m = 6 took 43 seconds, so the
  slow step is specific to m = 5, possibly the lines over ℚ(√5). m = 5 stays open. The statements of § 3 and § 5 stand
  for m = 1 to 4 and 6 only.

| statement | how checked |
|---|---|
| H2 (m = 2, 4, 6, 8) | computed once (post hoc, not blind); recomputed independently by the referee (m = 1 to 12) |
| H3 | computed once (post hoc, not blind) |

0 of 19.
