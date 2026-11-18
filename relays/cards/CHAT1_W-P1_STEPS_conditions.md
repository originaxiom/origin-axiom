# W-P1's first steps: the conditions, written before any computation

**From:** the web seat (chat1), 2026-11-18. **At the author's word** of 2026-11-18, the three first steps of card W-P1
(`relays/CHAT1_TO_CC_2026-11-18_W-P1_THE_PROCESS_READING.md`, § 5), data-free. Main assigns the foundation work (P-874);
this seat records on its status page that these steps are at the author's word. Each step: this condition first, its
script committed before its run, a referee read with its corrections applied, and its result pushed as a relay.

---

## Step 1 (W-P1a): the inventory

**What.** Every choice the record still makes, each with: its status as the record holds it; its process question;
its bin (equivalence, consistency, counted); and where the record already answers the question.

**Scope, fixed now.**
- (A) GENESIS's typed items: every row of its tables in §§ 2 to 4 and § 8 whose status is CHOSEN, POSTULATED, OPEN,
  UNEARNED or a ruling. They are listed by `wp1a_genesis_items.py`, which prints each item's ID and status word only,
  read through the mask.
- (B) The working read-out's choices (frames C and D1): those named in this seat's W-A1 part 2 (the choices audit),
  B1815's typed ingredients, P-776 and P-845's ingredients, B1922 and B1927 (the end, the hand), P-847 (the reading),
  P-873 (the Higgs direction, the sign of B), B1955 (the class), B1952 (postulate D's four bits), W-B2 (the sign of c),
  B1941 (the Higgs world), the mark and the twin, and SE3 (the level).

**Controls.** The script must list SE1 and SE3 as POSTULATED and SE2 and FK6 as CHOSEN, or it has failed to read the
tables.

**Expected [J].** Of part (B), most choices fall in the counted bin; equivalence holds for the mark against the twin at
τ = i (this seat's view, § 3.3) and for −I (B1935); the net count of card W-P1's rule stays zero.

**Failure.** A choice the record types CHOSEN or POSTULATED is missing, or a bin contradicts the record.

---

## Step 2 (W-P1b): the class test

**The question.** Does any read-out on record depend on level 5's Weil space W beyond End(W) as a G-module?

**Scope, fixed now.** Every quantity computed by the arcs on main whose code builds level 5's Weil representation:
B1856, B1923, B1934, B1936, B1951, B1952, B1953 and B1955; and main's checks of this seat's W-A1 to W-A3
(`checks/web_wa1_rest.py`, `checks/web_review.py`). Each is read at its FINDINGS (through the mask) and its code.

**Method.**
1. For each quantity, state what it is, and classify it:
   - (i) class-invariant by construction: a function of End(W) as a G-module, the centre, the commutant, the
     determinant or |χ|²;
   - (ii) a function of End(W) as an algebra;
   - (iii) a function of W itself: traces, eigenphases, labels.
2. For each in (ii) or (iii), compute it in both classes (a = 1, the knot's x²/5; a = 2, the act's 2x²/5), with this
   seat's own construction (`wp1b_class_test.py`), and say whether it differs.
3. Say whether each class-dependent quantity enters a read-out: a statement a frame makes about matter or couplings.
   A structural fact (a spectrum, a label) is not a read-out unless a frame reads it.
4. **If no read-out depends on the class,** write the proof that the class is a counted choice for the record as it
   stands. If one does, test the golden iteration γ over one period in both classes: does a test it imposes fail one?

**The Galois frame, stated first.** σ: ζ ↦ ζ² generates the Galois group of ℚ(ζ₅) mod complex conjugation. It
carries a = 1 to a = 2 and fixes ℚ, while complex conjugation keeps each class (−1 is a square mod 5). So a quantity
differs between the classes exactly when it is a number of ℚ(√5) that is not rational (or not fixed by σ).

**Controls.** tr ρ(γ²), which differs (−√5 against +√5; `wp1_weil.py`), must be classified as depending on the class.
det ρ(g) and ρ(−I), which do not, must be classified as class-invariant.

**Expected [J].** The read-outs of B1951, B1953, B1955 and B1936 are class-invariant, as their own pages say. The
class-dependent items are structural: the triplet's T-exponents, {0, 1, 4} against {0, 2, 3} (B1934), and the twin's
exchange of the two icosahedral triplets (B1923). Whether a frame reads either is the step's real question. The link
of B1934 § 2 (the hand is the golden field's quadratic character on the act's eigenvalue at the mark) is examined as a
candidate second choice tied to the class.

**Failure.** A quantity misclassified (a control fails), or an arc in scope left unread.

---

## Step 3 (W-P1c): the clock and the heights

**What.** Under (a), the move count, and (b), length, the share of the weave's time above heights 1.118, 2, 4 and 6
on the modular surface, and which words carry it.

**Definitions, fixed now.**
- A word is a positive word in L = [[1, 1], [0, 1]] and R = [[1, 0], [1, 1]] containing both letters. Its thread is
  the closed geodesic of its matrix. Height is Im τ after reduction to SL(2, ℤ)'s standard fundamental domain. Time is
  hyperbolic arc length along one period.
- **(a)** W-F24's measure: uniform random words of n letters (n = 20, 40 and 80), each thread weighted by its length;
  time shares pooled. Seeds fixed in the script.
- **(b)** The primitive closed geodesics ordered by length: every primitive cyclic word with trace at most X, each
  counted once, time shares pooled. Its limit is the hyperbolic area: 3/(πy) above height y ≥ 1 (standard; not
  computed here, compared).
- **Which words carry it:** for each word, its longest run of one letter a; the time above each height binned by a.

**Controls.**
- LR alone has no time above 1.118 (its axis's top is √5/2, exactly 1.118, attained at one point).
- LⁿR reaches √((n + 2)² − 4)/2 (`wp1_iteration.py`, P3).
- Every thread above height y has a > 2y − 2 (from the bound a/2 + 1 > y).
- (b)'s shares approach 3/(πy) as X grows; if they do not, the enumeration is wrong.

**Expected [J].** (a) close to W-F24's X4 (0.168 above 2, 0.007 above 4) and below 1e-3 above 6; (b) near 0.854,
0.477, 0.239 and 0.159. Above height 2, (a)'s time is carried by words with runs of three or more.

**Failure.** A control fails, or the shares of (a) do not settle as n grows.

## Step 3, after its referee read: the follow-up (W-P1c-F)

**Why.** The referee read of W-P1c (`614bff48d`) found the page sound with corrections. Three of them need numbers the
run did not compute: (b) was not compared with B1813; (a)'s shares carry no errors; and one sentence attributes time
to the run under each excursion, which the run did not do. The read computed these itself. This follow-up computes
them on this seat's code, so the corrected page rests on committed scripts. Written before the follow-up's script.

**What, fixed now.** The words are those of `wp1c_heights.py` (the same seeds and the same enumeration).
- **F0, the control.** For heights y ≥ 1 the part of a thread above y is the tops of its runs' axes. A run of a letters
  that starts at rotation k contributes 2 arccosh(ρ/y) when ρ > y, where ρ is the radius of M_k's axis (for a run of R,
  of the letter-swapped word's axis; the swap does not change heights). The closed form's pooled shares must equal
  the sampled shares to within 2e-4 at every height and setting, and each word's time above each height to within 5e-3.
- **F1.** The share above height 3: (a) at n = 20, 40 and 80; (b) at X = 100, 200 and 400. Beside B1813's headline:
  0.0346 counted move by move, and 0.315 at trace ≤ 400 counted by length, against the area's 1/π = 0.318.
- **F2.** (a)'s standard errors at each n and at heights 1.118, 2, 3, 4 and 6: the 2,000 words resampled with
  replacement, 1,000 times, seed 7, each resample's share taken as (a)'s pooled share.
- **F3.** The time above heights 1.118, 2, 4 and 6 by the length of the run under each excursion (bins 1, 2, 3, 4-5,
  6-9, 10+), from the closed form: (a) at n = 40, (b) at X = 400. Beside it, the run's table by each word's longest
  run (W-P1c, § 4), unchanged.

**Expected [J].** F1: (a) near 0.035; (b) at X = 400 near 0.315. F2: about 1e-3 above height 2, about 1e-4 above 6.
F3: above height 2 under (a), most of the time under runs of 4 to 9; above 1.118, some time under runs of 1 and 2.

**Failure.** F0 fails: then the closed form or the sampling is wrong, and neither F3 nor the page's § 4 stands until
it is found.

## Step 2, the sweep's follow-up (W-P1b-F)

**Why.** Reading the scope's code after the step's run found quantities that the record computes in one class only,
whose value in the other class the run did not print: B1856's HQ3 (ρ(LR)'s angles and traces on the two sectors),
B1934's T-exponents on the triplet, W-A1's Frobenius-Schur indicators (main's `web_wa1_rest.py`, item 2), and B1953's
two phase-free transports. The run's C3 also counted 24 elements without naming them. Written before the script.

**What, fixed now.** The construction is `wp1b_class_test.py`'s (its text run up to its group), a = 1 and a = 2.
- **G1.** The orders of the elements whose traces differ between the classes; whether the traces agree on every
  element of order 10.
- **G2.** ρ_a(LR)'s eigenvalue angles (in turns) and its traces, on the even and on the odd sector.
- **G3.** ρ_a(T)'s exponents on the even sector, the triplet (as multiples of 1/5).
- **G4.** The Frobenius-Schur indicators of the even 3 and the odd 2, and the orders of their images (projective for
  the 3).
- **G5.** B1953's two facts with D(a, b) = ψ(3ab) X^a Z^b: the largest residual of ρ_a(T) D(a, b) ρ_a(T)⁻¹ against
  D(a, b − a), and of ρ_a(S) D(a, b) ρ_a(S)⁻¹ against D(−b, a), over the 24 labels.

**Expected [J].** G1: the 24 are the elements of order 5, and order 10 agrees. G2: class 2 gives B1856's 1 − φ on the
even sector and φ on the odd (B1856 builds e(3x²/5), class 2), and class 1 exchanges them. G3: {0, 1, 4} for a = 1 and
{0, 2, 3} for a = 2 (B1934). G4: +1 and −1 in both classes; images of orders 60 and 120. G5: zero for a = 2 (B1953's
class) and not zero for a = 1.

**Failure.** G1 finds a differing trace on an element not of order 5: then the account of where the class shows is
wrong, and the step's proof waits until it is mended.

0 of 19.
