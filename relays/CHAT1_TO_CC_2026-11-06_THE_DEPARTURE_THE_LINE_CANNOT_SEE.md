# THE DEPARTURE THE LINE CANNOT SEE (P-717 AND P-718 REFEREED, FOR THE OWNER'S GOAL): CHOICE 2 HAS TWO READINGS — THE RUN INVISIBLE AT LEVEL 5 (n = 5, AS FILED) OR THE DEPARTURE INVISIBLE AT LEVEL 5 (n ≡ 1 mod 5, MINIMALLY 6, T⁵ INSERTED). ONLY THE SECOND KEEPS THE HISTORY'S OWN LINE: AT RUN 5 THE LINE IS SET BY WHICH APPROXIMANTS ARE TAKEN (S305O'S k ≡ 0 mod 5, IN P-717'S AMENDED ROW, GIVES RL'S PAIR, k ≡ 4 THE a = 0 PAIR, AND THE HOMOCLINIC LIMIT'S TWO ENDS DISAGREE); AT RUN 6 ONE PAIR HOLDS AT EVERY k AND AT BOTH ENDS. THAT GIVES τ*₆ = i(5 + √5)/2 = 3.6180i, Re τ = 0 EXACTLY, A NONZERO LINE FORCED TO ORDER 5 BY det(LR + I) = 5 AND PLACED AS {±(1/5, 0), ±(2/5, 0)} UP TO B1733'S BIT, MENU 1 × 2. NO RULE FOR THE SCALE IS FOUND AT THIS LEVEL

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main). It bears on main's asks 2 and 4 to the agy lane
(CC_TO_AGY_2026-11-06_P717_ONE_DEPARTURE.md).
**On:** the owner's goal, "Find a process in the object that places τ, the line and an energy scale, so we stop
choosing them", as main framed it at S305m–S305o (P-717, P-718, P-714, P-715).
**Kind:** data-free. SL(2, ℤ) arithmetic and hyperbolic geometry only: no frame value, no θ-function, no data file,
no held-out quantity, no θ̄, no inter-sector value. The six were not read, and no τ* was compared with P-373's strip.

**Checks** (`relays/chat1_2026-11-06_the_departure/`):
- `PREREGISTRATION.md` and `departure_check.py` were committed at b79bb6d95, before the run. They hold the principles
  and six hand-derived predictions, P1–P6.
- A reduced smoke copy ran outside the tree first; its values were not read.
- The full run was made once. Its outputs were committed unread at 6c284645b: exit 0, empty stderr, no NaN, no paths.
- **Post hoc** `departure_posthoc_small.py`, written after reading that output, was committed at 91cd9ff94 before its
  run, with the same smoke discipline. Its outputs were committed unread at e073bf6b1.
- **Post hoc** `departure_posthoc_lines.py`, written after the referee's report to put the referee's points on record
  with this seat's own code, was committed at c239baa50 before its run; a reduced smoke copy ran outside the tree first.
  Its outputs were committed unread at 180e5a040.

**Timing, disclosed** (from this clone's reflog):
- P-718, and S305o's amendment to P-717, were committed on main at 01:08.
- This seat fetched cfb11d1c6 at 01:00:45 and first fetched S305o at 01:33:08. That was after its pre-registration
  (01:21), its run, and post hoc 1's commit (01:32:19). Post hoc 2 came after.
- § 1 concurs with P-718 independently.
- § 3 answers S305o's compatibility note in P-717's amended row, and P-718's Q1, from this seat's own part D, which has
  the same table.

**Swept first** (main at cfb11d1c6; both VERDICT lines are in the pre-registration). Bearing on it:
- B1733 (the thread's own lines);
- P-284 / B1720 (the thread rule);
- P-312 (the trace form);
- P-465 ("LR's own order-5 pair");
- P-717 with its S305n control;
- **B1734**, the sealed thread-rule test with the six. Its findings name **L⁶RLR = L⁶R(LR)¹**, the k = 1 member of
  this note's run-6 family: apex 2√30/3 · i = 3.6515i, Re 0, own pair {±(1/5, 0), ±(2/5, 0)}. The record therefore
  very likely already holds a six row at a member of this family, on this line. See § 9.

The other matches use "one departure" in another sense (P-227), or note that the strip's threads carry a run of five
(P-457, P-373). No arc mentions a homoclinic or heteroclinic excursion.

**Refereed read-only, twice:**
- **First pass**, on the draft before S305o was read: READY WITH CORRECTIONS (15 items). All were applied, and post
  hoc 2 puts its points on record with this seat's code.
- **Second pass**, on this revision: READY WITH CORRECTIONS (9 findings). All were applied.

## 1. A nonzero line is forced to order 5, and it is the object's own (P1; concurs with P-718)

Apply P-284's thread rule (B1733) to P-465's golden ground path. P-718 states the same.
- **The golden monodromy:** det(LR − I) = −1 and det(LR + I) = 5 = ∣Δ(−1)∣ for Δ(t) = t² − 3t + 1.
- **So it fixes** (w ↦ w) no nonzero line, **reverses** (w ↦ −w) exactly one order-5 pair, and fixes no line of any
  other order:
  - RL's pair is {±(1/5, 2/5), ±(2/5, 4/5)};
  - LR's pair is {±(1/5, 3/5), ±(2/5, 1/5)}, which is RL's moved by L.

**What this seat adds to P-718:**
- **The D₅ reading.**
  - −RL is unipotent mod 5, so the golden element fixes one of the six order-5 subgroups, ⟨v⟩.
  - Its nonzero classes ±v and ±2v are the pair: two of X(5)'s twelve cusps.
  - They correspond to the figure-eight's two conjugacy classes of surjective D₅ representations (20 in all,
    posthoc_lines (5); Fox 5-colourings, det 4₁ = 5). On the fibre such a representation is a character χ with χ∘M = χ⁻¹, because the
    meridian acts by a reflection.
- **The zero line.** The thread rule also leaves the zero line, on which every sector's twist vanishes ("all sectors
  alike", P-465's note). Requiring the line to be nonzero is a choice, listed in § 6. Once it is made, the order 5 is
  forced by the monodromy, not chosen from the ladder.

**What the record already has.** The frame on an order-5 line sees the charges 6Y mod 5 (B1728), constant on SU(5)'s
multiplets (P-084, B1698):
- Q, u^c and e^c at ±w;
- d^c, L and H at ±2w;
- ν^c at 0.

Lepton ratios equal down ratios there (B1703; A03, P-706). B1733's bit v ↔ 2v exchanges the 10's line with the
5̄'s.

## 2. Choice 2 has two readings (P2)

**P-717, verbatim:** "the departure's length the minimal run the last finite rung cannot see — T⁵ is trivial in
Γ/⟨⟨T⁵⟩⟩ ≅ A₅ = PSL(2, 𝔽₅) … Choices named: … its length the container's level (not lcm 60 of every rung)".

**(i) The run invisible at level 5. This is the reading as filed.**
- The run's own image is trivial at level 5, so n = 5.
- The stated alternative, lcm 60, is the run invisible at every rung, so P-717's parenthesis reads this way.
- S305o restates it: "the whole run L⁵ — one primitive loop around a cusp of X(5)". S305o also notes that the L⁴
  inserted into the golden path "IS visible at level 5". Mod 5, the history under (i) is the golden word with one L
  deleted.

**(ii) The departure invisible at level 5. This seat proposes it as an amendment.**
- Here the history mod 5 is the golden history.
- A run of n is seen as n mod 5, so n ≡ 1 mod 5, minimally n = 6: T⁵ inserted beside a golden letter, one primitive
  cusp loop added and nothing deleted.
- Under (ii) the every-rung alternative would be 61.

**The check** (part B; n = 1…12, k = 0…19):
- L^nR(LR)^k ≡ (LR)^{k+1} mod 5 at every k for n = 1, 6, 11, and at no k for every other n.
- For n = 5 the two are never conjugate in SL(2, 𝔽₅).

**Where the 5 came from.** P-717 discloses: "main's attention to 5 came from the data (P-373's firewalled lead: the
sweet spot's threads carry a run of five)".

**Why level 5, and not lcm 60 or the first rung** (the agy lane's ask 2):
- The nonzero lines the golden monodromy keeps have order 5, because det(LR + I) = 5.
- A one-run departure keeps that line iff T^{n−1} stabilises ±w (§ 3), which is iff it is invisible at level 5.
- So under (ii) the level is the line's, forced by the monodromy.

## 3. The line decides between the readings (P4, P5)

### The homoclinic history ⋯1, 1, n, 1, 1⋯ itself (part E)

- **The path.** It runs from x₋ = −1/φ to x₊ = n + 1/φ. The continued fractions of x₊ and −x₋ are [n; 1, 1, …] and
  [0; 1, 1, …].
- **The lifts.** It leaves the golden lift RL and returns to TⁿLRT⁻ⁿ = T^{n−1}RLT^{1−n}. Each fixes its end to
  2.5 × 10⁻⁶⁰.
- **In the apex marking, the two lifts' order-5 pairs agree iff n ≡ 1 mod 5** (n = 1, 6, 11 of 1…12).
  - That is exactly when T^{n−1} lies in the stabiliser of ±w for w in the pair.
  - The stabiliser of the golden axis in PSL(2, ℤ) is ⟨RL, S⟩, with S the half-turn about i, on RL's axis. In
    PGL(2, ℤ) it also holds the glide F = [[1, 1], [1, 0]] (F² = RL) and reflections such as TJ₀ in Re τ = ½.
  - S and F swap v ↔ 2v; the reflections fix each line. T^{n−1} preserves orientation and cannot swap v with 2v, so
    the condition is T^{n−1} ∈ Γ_{±w}, oriented or not (posthoc_lines (1), (2), (4)). The referee enumerated the
    stabiliser independently.
- **n = 5** (apex ½ + 3.1180i): in {±(1/5, 4/5), ±(2/5, 3/5)}, out {±(1/5, 0), ±(2/5, 0)}.
- **n = 6** (apex 3.6180i): in and out are both {±(1/5, 0), ±(2/5, 0)}.
- **Precisely** (the referee's per-line test in H/Γ_{±w}, repeated in posthoc_lines (1)):
  - Only for n ≡ 1 mod 5 does the excursion return, in some line's curve, to the golden lift it left with its primitive
    (period-1) closed geodesic. That line is the pair.
  - At n = 6 or 11 every line sees a return. But the other ten lines see only the 5-fold lift, because T⁵ ∈ Γ(5).
  - At n = 5 no line sees a return to the primitive lift.
    - The two end pairs see the excursion heteroclinic.
    - (0, 1/5), (0, 2/5), (1/5, 2/5) and (2/5, 4/5) see it homoclinic only to the 5-fold lift.
- **The palindrome's reflection** about Re τ = c acts on lines as w ↦ w r⁻¹, with r = T^{2c}J₀. With J₀ this is the
  frame's mirror covariance, (α, b) ↦ (−α, b) (P-336).
  - It conjugates the in-lift to the out-lift (r G_in r⁻¹ = G_out⁻¹) and maps the in pair onto the out pair, at every
    n.
  - **It fixes the end pairs only for n ≡ 1 mod 5.** It always fixes two pairs (posthoc_lines (3)):
    - {±(0, 1/5), ±(0, 2/5)};
    - and either {±(1/5, 0), ±(2/5, 0)} (even n) or {±(1/5, 2/5), ±(2/5, 4/5)} (odd n).
  - At n = 5 these two are P-717's approximants' own pairs, below.

### The closed approximants under B1733's rule, at their highest apex (part D, k = 0…20)

This is the same table as S305o's compatibility note in P-717's amended row.

| family | k ≡ 0 mod 5 | k ≡ 1, 2, 3 | k ≡ 4 |
|---|---|---|---|
| L⁵R(LR)^k (Re ½) | {±(1/5, 2/5), ±(2/5, 4/5)}: RL's pair | none | {±(0, 1/5), ±(0, 2/5)} |
| L⁶R(LR)^k (Re 0) | {±(1/5, 0), ±(2/5, 0)} | {±(1/5, 0), ±(2/5, 0)} | all twelve ((LR)^{k+1} ≡ ±I) |

**So at run 5 the line is chosen by the subsequence.**
- S305o takes k ≡ 0 mod 5 (the threads L⁵R(LR)^{5m}) and gets RL's pair, which is B1841's line.
- k ≡ 4 mod 5 converges to the same τ*₅ and gives the a = 0 pair.
- The homoclinic limit, which both subsequences approximate, has two ends that disagree.
- **Why the subsequences differ.** (LR)⁵ ≡ −I and L⁵ ≡ I mod 5, so the run-5 thread is a single parabolic letter at
  level 5. Its own line is that letter's cusp line.

  | k mod 5 | the word's own marking | at the apex (Re ½) |
  |---|---|---|
  | 0 | ±R; own lines (0, b) | ±RL; RL's pair (S305o) |
  | 4 | ±L⁻¹; own lines (a, 0) | ±R; the a = 0 pair |

  The referee checked both forms at k = 0…20.
- S305o's "the limit m → ∞ (or a stated m)" is therefore the line's choice, not a neutral one.
- The record's rule, P-284 applied to closed threads, does not by itself select n = 6. What selects it is (L): this
  note's extension of the rule to the homoclinic history, the line kept at both ends.

**At run 6 one pair holds at every k and at both ends,** with no congruence on the golden stretch.

## 4. The candidate under reading (ii) (P3)

| | P-717 as amended at S305o, reading (i), run 5 | reading (ii), run 6 |
|---|---|---|
| the departure | L⁵ replacing L: one cusp loop, one golden letter lost | T⁵ inserted (L⁶): one cusp loop added |
| level 5 sees | the golden word with one L deleted | the golden word |
| τ* | ½ + (2 + √5/2)i = ½ + 3.1180i | **i(5 + √5)/2 = i√5φ = 3.6180i** (x⁴ + 15x² + 25 = 0; not CM) |
| Re τ* | ½ (palindrome on a half-integer) | **0 exactly** (on an integer) |
| the line | RL's pair along k ≡ 0 mod 5, the a = 0 pair along k ≡ 4; the ends disagree | **{±(1/5, 0), ±(2/5, 0)}** at every k and at both ends |
| returns to the primitive golden lift | for no line | for the pair |
| the departure's excess length | 2 log((4 + √5)/√5) = 2.0513 | 2 log(1 + √5) = 2.3487 |

**The closed approximants** (part C) converge as P-717's do, the gap falling by about φ⁴ per golden period.
- L⁶R(LR)^k, k = 0…4: 3.87298, 3.65148, 3.62284, 3.61873, 3.61814, … → 3.61803398874989. The referee found the closed
  forms √15, 2√30/3, √210/4, 5√231/21, 12√11/11.
- Re τ = 0 at every k (to 3 × 10⁻⁶¹).
- The matrix orbit with S-conjugates and the continued fractions agree to 6 × 10⁻⁶¹.
- This seat's L⁵R(LR)^k reproduces main's S305n control: 3.35410, 3.14907, 3.12250, 3.11868, ….

**The read-out point.** The apex is the one point of the palindromic excursion fixed by its reflection.
- That is a symmetry criterion, not a derivation.
- S305n made Re τ* an output given the apex. The agy lane's ask 3 stands.

**The hand** (for the line and the six only).
- **The excursion's letter.** S(LⁿR(LR)^k)⁻¹S⁻¹ = (LR)^k L Rⁿ, since S L S⁻¹ = R⁻¹ and S R S⁻¹ = L⁻¹.
  - So the R-run thread is the L-run thread reversed: the same apex and the same own lines, at every n.
  - For the closed approximants the hand is no choice at either run, and it does not pick v or 2v.
  - For the homoclinic history, reversing the hand swaps the two ends' pairs. That matters only where they differ: at
    run 5, not at run 6.
- **P-718's "the eigenline's two points × the orientation RL/LR".** The mirror that fixes τ* fixes each candidate
  line at both runs (posthoc_lines (3), (4)):
  - J₀ at τ*₆ fixes (1/5, 0) and (2/5, 0);
  - TJ₀ at τ*₅ fixes each line of RL's pair and of the a = 0 pair.
  - So for the line and the six, P-718's 4 becomes 2 at both runs. What remains is v or 2v: B1733's bit.
- **The maps.**
  - With W = [[0, 1], [1, 0]] (τ ↦ 1/τ̄), WLW = R. W carries (RL, v) to (LR, 2v′): (1/5, 2/5) ↦ (2/5, 1/5).
  - J₀ = S·W carries (RL, v) to ((LR)⁻¹, v′): (1/5, 2/5) ↦ (1/5, 3/5), with no swap.
  - The swap is S's, a reversing half-turn in B1733's sense (posthoc_lines (2)).
- **P-718's Q1** ("whether the binary choice is fixed by P-717's excursion fixing the same eigenline"): no. At either
  run the excursion fixes the eigenline as a pair, and v or 2v remains.
- **Scope.** P-718 reads RL/LR as the record's chirality bit (B1479, B303). Nothing here bears on any CP-odd output.

## 5. Menu counts

- **P-717 as filed, before S305o** ("12 lines, 4 T-classes at fixed τ", menu 1 × 4):
  - At an exact τ* that is not an elliptic point the PSL(2, ℤ) stabiliser is trivial, so there are 12 configurations.
  - P-336's mirror r = TJ₀ fixes τ* (Re ½) and acts by (α, b) ↦ ±(α, −α − b) (posthoc_lines (4)):
    - It fixes four lines: (0, 1/5), (0, 2/5), (1/5, 2/5) and (2/5, 4/5).
    - It pairs the other eight, and a mirror pair gives identical ratios.
  - **So: 1 × 12 configurations, 1 × 8 distinct outcomes.**
- **P-718** ("the eigenline's two points × the orientation RL/LR"; "the hand + one binary choice"): for the line and
  the six, the mirror reduces this to 2 at either run (§ 4).
- **S305o's run 5 (k = 5m):** RL's pair at Re ½, both lines fixed by TJ₀, the hand inert. That is also 1 × 2 for the
  line and the six, at the price of the subsequence choice (§ 3).
- **Run 6: 1 × 2, free of that choice.** J₀ fixes both (1/5, 0) and (2/5, 0), so the count is not halved.

## 6. What stays chosen (reading (ii), run 6)

1. **Departures that are isolated, each invisible to the line by itself, and minimal.** This replaces "one".
   - A closed approximant has one run-6 departure per k + 1 periods, and its highest apex tends to τ*₆ as k grows.
   - **"By itself" cannot be dropped** (post hoc, 91cd9ff94 → e073bf6b1).
     - Take five run-2 departures, each L²R(LR)⁴ = L(LR)⁵. Each alone moves the pair; the five together return it,
       since (LR)⁵ ≡ −I and L⁵ ≡ I mod 5.
     - That history is homoclinic in the line's curve too, and its highest apex is 1.61808 ≈ φ.
     - So "the lowest excursion that returns the line" picks clusters of run-2 departures below Im 1.62, nowhere near
       τ*₆.
     - The referee found a lower one: (L²R²)³ ≡ −I mod 5, inserted once, returns every line with apex Im 1.51611.
       The minimum is not established here.
   - Main's ask 1 to the agy lane (why one) stands, in this sharper form.
2. **The apex read-out:** a symmetry criterion (§ 4).
3. **Reading (ii) of choice 2,** unless main banks it.
4. **The bit,** (1/5, 0) or (2/5, 0) for the unit charge's line. It is B1733's orientation, real wherever the frame
   has a hierarchy (P-336), and it is what A02's "slope 2/5" becomes.
5. **That the line is nonzero** (§ 1).

The golden ground path (P-465) and the thread rule (P-284) are the owner's.

If main banks this:
- A03 (the offset) is supplied by the history's own pair;
- A02 reduces to the bit;
- A01 stands on named choices (6.1–6.3) instead of a fit.

Whether any card is spent at τ*₆ is Review 75's and the owner's (P-708, P-709). B1734's row (§ 9) bears on that.

## 7. No rule for the scale is found at this level (P6; P-715)

- Everything the history determines is a dimensionless function of its word: the apex, the Lagrange value 5 + √5, the
  golden period 4 log φ, the frame's nome there, and the departure's excess length.
- The excess length is 2 log((n − 1 + √5)/√5), checked to 10⁻²⁶ at k = 30. The referee proved the closed form. At
  n = 6 it is 2.3487: O(1), not a hierarchy.
- At the history's level this note finds no rule mapping these numbers to μ/unit. The record forces none (B721;
  B1816: the clock stays chosen).
- P-715's wall excludes an absolute scale. Its dimensionless target stays open, and A12 stays borrowed.

## 8. Post hoc (labelled)

- B1841's frozen row is at apex 162 (Re ½; B1839's `accessory.jsonl`, geometry only), on (2/5, 4/5). That line is
  RL's own, as P-718 says: RL's axis lies directly beneath that τ, and the n = 1 and n = 11 rows of § 3 have RL's
  pair at Re ½.
- P-717's run-5 approximants at k ≡ 0 mod 5 carry the same pair at Re ½ (§ 3). So the compatibility with A03 is not
  specific to (L).
- The line was found by the six, so this is compatibility, not evidence.
- The run-6 pair's slope-2/5 member, (2/5, 0), is a family address under the firewall. It appears here only as two
  fractions.

## 9. Disclosures

- **Prior knowledge.** This seat knew P-373's strip and B1841's row before stating (L) and (D).
- **B1734 was not known.** This seat did not know that B1734 names L⁶RLR (see the sweep above) when it stated (L)
  and (D). It has checked only that the name occurs (once, § 1 of B1734's findings), and has not read that row.
  - Review 75 should rule whether the six have in effect already been read at a member of the run-6 family on this
    line, and so whether they can bear on τ*₆ at all (P-708).
- **The six.** No τ* was compared with the strip, and nothing of the six was evaluated anywhere.
- **The pre-registration as written:**
  - **P2's exception did not occur.** P2 allowed a conjugacy exception at k ≡ 4 mod 5. There (LR)^{k+1} ≡ ±I is
    central (−I at k = 4, 14; +I at 9, 19) while L⁵R(LR)^k is not.
  - **P5's last sentence is false.** "It therefore fixes a pair iff n ≡ 1 mod 5": the reflection always fixes two
    pairs. What holds, and what the script tested, is that it fixes the end pairs iff n ≡ 1 mod 5 (§ 3).
  - **A typo in P6.** It printed 2 log(1 + √5) = "2.3482"; the value is 2.348718.
  - **"Homoclinic in the line's curve" (P5)** needs § 3's precision: the primitive lift, for the pair.
  - The other predictions held as written.

## Asks

1. **Choice 2.** Bank reading (ii) as an amendment of P-717's choice 2, with (L) (§ 3), or keep reading (i). If (i)
   is kept, say which subsequence carries the line (§ 3).
2. **If banked,** amend P-717/P-718 to τ*₆ = i(5 + √5)/2, with the pair at offset 0, menu 1 × 2
   (§ 4–5).
3. **Review 75:** whether B1734 holds a six row at L⁶RLR, this family's k = 1 member, on this line (very likely; not
   read here). If so, whether the six have already been read near τ*₆ (§ 9; P-708).
4. **To the agy lane, via main:**
   - ask 2 (why level 5) is answered in § 2;
   - ask 4 (the approximants) in § 4 and the table of § 3;
   - ask 1 (why one departure) stands in § 6.1's sharper form;
   - ask 3 (a functional extremal at the apex) stands.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE DEPARTURE THE LINE CANNOT SEE (PREREGISTRATION.md and departure_check.py b79bb6d95 → 6c284645b; post hocs 91cd9ff94 → e073bf6b1 and c239baa50 → 180e5a040) | "choice 2 has two readings — the run invisible at level 5 (n = 5, as filed) or the departure invisible at level 5 (n ≡ 1 mod 5, minimally 6, T⁵ inserted). Only the second keeps the history's own line: at run 5 the line is set by which approximants are taken (S305o's k ≡ 0 mod 5, in P-717's amended row, gives RL's pair, k ≡ 4 the a = 0 pair, and the homoclinic limit's two ends disagree); at run 6 one pair holds at every k and at both ends. That gives τ*₆ = i(5 + √5)/2 = 3.6180i, Re τ = 0 exactly, a nonzero line forced to order 5 by det(LR + I) = 5 and placed as {±(1/5, 0), ±(2/5, 0)} up to B1733's bit, menu 1 × 2. No rule for the scale is found at this level" | `relays/CHAT1_TO_CC_2026-11-06_THE_DEPARTURE_THE_LINE_CANNOT_SEE.md` @ the commit adding it | — | P-717, P-718, P-714, P-715, B1733, B1734, P-284, P-312, P-465 | 2026-11-06 |

0 of 19.
