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

## Step 3's follow-up: F0's per-word bound failed (W-P1c-D)

**What happened.** The follow-up's run (`wp1c_followup_out.txt`) met F0's pooled bound (worst 5.0e-5 against 2e-4)
and failed its per-word bound (worst 6.3e-2 against 5e-3). By the condition above, F3 and the page's § 4 do not stand
until the cause is found. Written before the diagnosis's script.

**The suspect [J].** Height 1.118 is LR's top exactly (√5/2). A stretch of alternating letters gives runs whose axes
reach within a hair of it, so their time above it is short: 2 arccosh(ρ/y) grows like the square root of ρ − y. The
sampling's step is about 1/120. An excursion shorter than a step is caught by one sample or none, so a word with many
such excursions can be off by several steps, while the errors cancel in the pool.

**What, fixed now.** The same words and the same two methods.
- **D1.** For each setting and each height (1.118, 2, 3, 4, 6), the worst per-word difference between the sampling and
  the closed form.
- **D2.** For the worst word overall: its height, its runs whose ρ exceeds that height by less than 1e-3 (their number
  and their closed-form time), and the difference again with the sampling ten times as dense (1,200 per unit length).

**Expected [J].** The worst differences are at height 1.118. At heights 2 to 6 they are below 5e-3. D2: the worst
word's height is 1.118, it has grazing runs, and the denser sampling shrinks its difference.

**Failure.** A per-word difference above 5e-3 at height 2 or above, or a difference that does not shrink with the
denser sampling. Then the closed form is wrong for some words, and F3 is withdrawn.

## Step 2, the two Gramians (W-P1b-G)

**Why.** Reading B1953's code for the sweep: its operator O = Σ ζ^(−ab) Y(w) ⊗ D(w) has two family Gramians, W traced
over the 3 and over the 2, printed as the frame's outputs (B1953, § 4). They are built from products of the lines, the
place card W-P1, § 3.2 named where a read-out might see the class. B1953, lines 74 and 75, says that scaling the labels,
D(cw) for c = 2, 3, 4, gives the same Gramians, "so the two Weil classes are not told apart by these read-outs". No code
on record computes that scaling. A scalar c has determinant c², a square, so the scaling stays in one class; the step's
labels run found that the other class needs a relabelling of non-square determinant. Written before the script.

**What, fixed now.** D(a, b) = ψ(3ab) X^a Z^b (B1953). The frame's transport is class 2's label action with the
identity labelling, A(T): (a, b) → (a, b − a), A(S): (a, b) → (−b, a) (B1953's exact facts; W-P1b-F's G5).
- **J1.** For each class and each K in GL(2, 𝔽₅): whether ρ_a(g) D(Kv) ρ_a(g)⁻¹ = D(K A(g) v), with no phase, for
  g = T and S and all 24 labels v. The number of such K, and the square classes of their determinants.
- **J2.** On W: t(v, w) = tr(D(v) P D(w)†) against ζ^(±3ω(v, w)), with ω(v, w) = v₁w₂ − v₂w₁.
- **J3.** Synthetic couplings, no frame: 24 random complex 3 × 3 matrices A(w) with A(−w) = A(w), seed 11. For each K
  of J1, in both classes, O_K = Σ A(w) ⊗ D(Kw) and its Gramians G₃ = tr_W[O_K (1 ⊗ E₃) O_K†] and G₂, with
  E₃ = (1 + P)/2 and E₂ = (1 − P)/2.
  - Within a class: the largest difference between its K's.
  - Between the classes: the difference of the G₃'s, against the closed form from J2. Here S_j is the sum of
    A(v)A(w)† over the pairs with ω(v, w) = ±j.
  - In both classes: G₃ + G₂ against 5 Σ A(w)A(w)†.
  - The control: A replaced by its average over w, 2w, 3w, 4w, so that A(2w) = A(w). The classes must then agree.
- **J4.** The iteration over one period, in both classes, on synthetic covariant data. Define A(γτ, w) := U A(τ, A(γ)⁻¹w) V†,
  with random unitaries U and V and A(γ) the transport composed for γ = T S T⁻¹ S⁻¹. Do this for ten steps (A(γ) has
  order 10 on the labels). At each step, report the residual of O_K(γᵏτ) against
  (Uᵏ ⊗ ρ_a(γ)ᵏ) O_K(τ) (Vᵏ ⊗ ρ_a(γ)ᵏ)†, and G₃'s eigenvalue ratios against step 0. Report whether ten steps return the
  labels and ρ_a(γ).

**Expected [J].**
- J1: four K for each class, all with no phase. For class 2 they are the scalars (square determinants); for class 1
  their determinants are non-squares.
- J2: t = ζ^(±3ω).
- J3: the Gramians agree within a class to 1e-12. Between the classes G₃ differs, as the closed form says. The sum
  agrees. The control agrees.
- J4: covariant at every step in both classes, and the ratios unchanged.

**Failure.** Either of these means the comparison does not stand:
- J1 finds that class 1 needs phases. Then the phase table changes, and J3 does not compare the class-1 operator.
- J3's control differs between the classes. Then the closed form is wrong.

**What it would mean, set now [J].** If J3 holds, B1953's two Gramians on frame C differ between the classes unless
the frame's couplings satisfy S₁ = S₂. Their sum and the phased sum do not depend on the class. Whether frame C
satisfies S₁ = S₂ is one computation on main's frame, which this seat does not run.

## Step 3's follow-up: the diagnosis's result, and the bound (W-P1c-E)

**What happened.** The diagnosis (`wp1c_diag_out.txt`) did not find the suspect. The worst word has no grazing run.
The per-word differences are 0.6e-2 to 6e-2 at every height, including heights 2 to 6. By the clause written above,
that is a failure: F3 is withdrawn until the cause is settled. Its D2 points at the sampling: at ten times the density
the worst word's difference falls from 6.3e-2 to 4.3e-3. Written before the next script.

**The bound, derived now from the sampling's own scheme.** Each piece of length ℓ is cut into m ≥ ℓ·DENS equal parts,
each sampled at its midpoint and weighted ℓ/m ≤ 1/DENS. The height along a thread is continuous. A part without a
crossing of the level y is counted exactly. A part with a crossing is off by at most its weight. So for every word and
height, |sampled − exact| ≤ (number of crossings)/DENS. If the closed form is exact, its excursions are one arc per
run with ρ > y, so the crossings number 2·N, with N the number of such runs. The 5e-3 set in F0 ignored this. With
DENS = 120 a word with N = 5 may be off by 0.083.

**What, fixed now.** The same words, the same two methods.
- **E1.** For every word of every setting and every height: whether |sampled − closed| ≤ 2·N/DENS. Report the number
  of violations, and the largest ratio of the difference to the bound.
- **E2.** The ten words with the largest difference at each height (over all settings): the difference at DENS = 120,
  1,200 and 12,000.

**Expected [J].** No violation; the ratio below 1. E2's differences fall roughly tenfold per step.

**Failure.** A violation, or a difference that does not fall with the density. Then the closed form is wrong for that
word; F3 stays withdrawn, and so does any use of it.

0 of 19.
