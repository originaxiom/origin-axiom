# T1: the consistency census. Which established results presuppose which clock? (2026-10-29)

**Status.** A reader's report for T1 of `docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md` § 8. It is not an arc, and
nothing in it is banked. Five data-free checks were run once each in the scratchpad. They re-use the arcs' own code
unchanged, by read-only import (appendix). Their numbers are exploratory until a seat re-runs them. Quotes are at most 15
words. Reader A's table "The nearest things, side by side" and its § 5 are taken as read and not repeated. This report
adds the dependence column: for each result, whether its conclusion changes under the other clock, checked where the
code allowed.

**Swept** (`scripts/checks/topic_sweep.py --full`, every VERDICT line as printed):
- `thread sum|sum over threads|over all threads|democratic|uniform measure|weave.s (uniform )?measure|equidistribut|Duke`:
  37 of 1561 arcs on main (NEGATIVE 10, OPEN 3, PROVED 24); 18 register rows.
- `by trace|by word length|word length|Hagedorn|pressure|partition function|Minkowski|Gauss.Kuzmin|apex rule|class number`:
  83 of 1561 arcs (NEGATIVE 18, OPEN 5, PROVED 60); 18 register rows.
- `entropy.{0,40}(thread|word|walk|move|letter|per)|by discriminant|discriminant.{0,30}(order|sum|up to|≤|<=)|trace ≤|trace <=|tr ≤|up to trace|length ≤|all words of length|every word of length|random walk|the walk`:
  44 of 1561 arcs (NEGATIVE 10, OPEN 1, PROVED 33); 7 register rows.
- `apex|strip|threads? (to|up to) (trace|length)|every thread (with|of)|all threads|thread census|threads of length|random hierarch|typical`:
  103 of 1561 arcs (NEGATIVE 29, OPEN 7, PROVED 67); 56 register rows.

**Also read:**
- `docs/HARVEST_LEDGER.md`: every VERIFIED or REPRODUCED row that names threads, the weave, a mean, a measure or a share;
  and the rows for § 320, W57, W95, W98, W42, W107, W34 and the arena.
- On the SM seat's branch (its branch @ 3889806ad): § 320, read at source.
- GENESIS: GM1–GM5d, § 3, GAP5, FK10, v1.44, v1.48 and v1.55.
- `docs/THE_WEAVE.md`.
- `speculations/S_THE_PUSH_BACK.md` §§ 9.2 and 10.
- Most of the hits are noise: arithmetic class numbers, Petersson norms at a point, Minkowski bounds. The candidates
  below are every hit whose computation sums, averages, orders, weights or samples over threads, τ or words.

---

## 0. The answer, first

1. **The record's established results are consistent with BOTH clocks.**
   - Every established result whose conclusion changes with the clock states its ordering in its own claim:
     - B1666, "averaged trace by trace";
     - B1629, scoped to "the weave's uniform measure" by its addendum, B1648 and GENESIS v1.44;
     - B1722, "the record's own measures";
     - B1663, "the walk";
     - B1813 and B1814 name both clocks.
   - The conclusions other results build on are clock-neutral. Checked here:
     - B1633's scalar;
     - B1676's mod-8 law and its scalar mean;
     - the "no atom" form of B1629.
2. **One established result needs the geometric clock: B1666's L1**, "the threads reach the constant mode 0.315".
   - Ordered by moves, B1666's own per-thread function gives **0.508 ± 0.003** at word length 14 (0.5176 with the
     length weight). That is the walk's 0.517 (B1663), not 0.315: computed here, check (e).
   - Its "quarter of threads" with #L ≡ #R (mod 4) is also a trace-ordering number: 0.250 by trace, 0.324 by word length
     2–16 (check (d)).
3. **The move clock is needed only by numbers:**
   - B1629's (k+1)/2^k: by trace, the share of letters in deep runs is 0.81–0.96 and rising (check (a));
   - B1722's measure-weighted misfits;
   - the root shares 0.27 / 0.50 / 0.66 of chat1's check, verified in B1650's addendum.

   Each is stated under its weights.
4. **No established result needs the move clock as the weave's dynamics.**
   - The walk's link to the move clock is B1663's computation. Its scope says "That the walk is the physical motion.
     This is the picture's reading, firewalled."
   - GM5b is "a reading of PF1's cancelling chosen by the math, not a derivation."
5. **So GM5b's walk can be the programme's whole dynamics without contradicting any established result.**
   - T1 neither excludes it nor forces it. The clock stays CHOSEN after T1, as GENESIS § 3 and GAP5 have it.
   - The price of the walk-as-dynamics reading is in § 4.
   - **The one sentence on record that contradicts it** is a ruling's reason, not a result: P-180's "Primitive threads of
     one length are equal time in the motion."

---

## 1. The census

**Columns.**
- "depends?": does the conclusion change under the other clock? YES, NO, or NOT DECIDED, with the evidence.
- Class:
  - NG: NEEDS-GEOMETRIC;
  - NM: NEEDS-MOVES;
  - N: NEUTRAL;
  - U: UNESTABLISHED.
- "(scoped)": the result's own claim names its ordering, so it stands as a conditional statement under either clock.

### 1a. Main's arcs that weight, order or average threads

| result | status | ordering used (quote) | depends? | argued / ruled / taken | class |
|---|---|---|---|---|---|
| **B1629** (FK10 v1.38, scoped v1.44) | NEGATIVE as sealed; sharpened by addendum | word length, uniform per word, time in letters: "over all primitive cyclic positive words with both letters of length n" | **The number: YES.** (k+1)/2^k = 0.75 … 0.035 for k = 2 … 8 by moves. By trace (T ≤ 1200, letter time): 0.957 … 0.814, rising with T (0.728 → 0.764 → 0.792 → 0.814 at k = 8 for T = 150 … 1200), check (a). **The scoped conclusion** ("no expectation … of a bounded observable in ever-deeper horoballs gives the cusp weight"): **NO.** Hyperbolic area gives P(Im τ > Y) = 3/(πY) → 0, and B1813's by-trace table approaches it. It fails only under a mixed clock: threads ordered by trace, time counted in letters. **The thread parts** (LR the lowest closed geodesic, the clock's word below 2.29): NO, per word | taken ("the weave's uniform measure"); flagged by the audit lane, "letter time is not arclength" | number **NM (scoped)**; conclusion and thread parts **N** |
| **B1633** | PROVED | every word of length n, uniform: "averaged over ALL threads of length n with the weave's uniform measure" | **NO**, check (b). By trace, one weight per thread, the distance of Π from a scalar is 2.6 × 10⁻⁴, 1.5 × 10⁻⁴ and 9.4 × 10⁻⁵ at T ≤ 300, 600 and 1200; by length 2–16 it is 8.2 × 10⁻⁴. The per-coset numbers carry over exactly. By trace half the threads have even length, and tr Π = 0.2080 against ½ · 5/12 = 0.2083; the zero-mode fraction is 0.1569 against ½ · 5/16 = 0.1563. Only the even/odd mixture is clock-dependent | taken | **N** |
| **B1676** (= the SM seat's W107; row 1271 VERIFIED) | PROVED | "every primitive positive word in L, R of length 2-16 up to rotation", one weight each | **The law** (rank one iff #L ≡ #R mod 8): **NO.** It holds on all 10 222 odd-trace threads to T = 600 and all 36 610 to T = 1200. **The scalar mean of means: NO in the limit (strongly indicated; the limit is not proved here).** The diagonal is equal in both orderings. Off-diagonal over diagonal: 3.1% by length ≤ 16; 18.9%, 11.1% and 6.5% at T ≤ 300, 600 and 1200, falling about as T^(−0.75), check (c). The finite-cut numbers differ: the rank-one share is 24.0% by length and 25.1% by trace | taken (W107's rule) | **N** |
| **B1666** L1 | PROVED as sealed | trace layers: "the layer averages A_t = mean <f> over the threads of trace t" | **YES**, check (e). B1666's own `_thread`, unchanged, averaged over the threads of exactly word length n gives 0.502, 0.504, 0.507 and 0.508 ± 0.003 at n = 8, 10, 12 and 14 (length-weighted 0.518, 0.517, 0.518, 0.518). By trace it gives 0.3144 → 0.315. The control reproduces B1666's stored A_t at t = 5, 7 and 10 exactly | **ruled**: P-180 indexed W95 and W-trace by trace, for the reason in row 1e. The alternative weighed was the discriminant, not word length | **NG (scoped "trace by trace")** |
| B1666 L0 and the "quarter" | PROVED as sealed | every thread with trace ≤ 600 | **L0** (period phase i^(#L−#R) on every thread): NO, it is per thread. **"The quarter of threads with #L ≡ #R mod 4": YES.** It is 0.250 by trace and 0.324 by word length 2–16, because odd lengths never qualify (check (d)). **L2** (the coherence regression on the trace-cut sample): NOT DECIDED | ruled (as above) | L0 **N**; the quarter **NG** (stated in THE_WEAVE without its ordering) |
| **B1662** (GM5b, v1.48) | PROVED | the walk, per step: "A reading of PF1's cancelling chosen by the math, not a derivation." | **NO** for every conclusion. The legality of the pull-back, −I generated, transience ("never settles"; a reparametrisation of time cannot change recurrence) and positive escape all hold. Only the rate 0.0992 *per step* is move time | **ruled** (the owner, P-179) | **N** (but it generates the move clock: next row) |
| **B1663** | NEGATIVE as sealed (T4(b)) | the walk's step law, equal within each pair; τ averaged in arclength "along the geodesic ray to the walk's limit" | **NO** as a fact about the walk. Its content is that the walk's limit has fair-coin digits (Minkowski), whatever p; that is the bridge from GM5b to the move clock. Its own scope: "That the walk is the physical motion … firewalled." Its placement is by arclength, so its 0.517 belongs to a mixed clock (reader A, T9) | step law **ruled** ("no preference"); placement taken | **N** (the bridge GM5b-walk ⇒ moves; the general theorem cited, not read: P-473) |
| **B1722** | NEGATIVE as sealed | μ_U: "a primitive class of length n carries its n rotations, each 2^-n"; μ_A = e^(−Vol/π) | **The numbers: YES** (they are weights). **The NEGATIVE: NOT DECIDED on its census** under a geometric weight. The same outcome holds by another instrument: B1814 found the geometric clock's worlds consistent but not specific, with 73% of random hierarchies passing. The post-read "the walk selects at most a length, never a thread" presupposes walk = moves | taken: μ_U from B1629; μ_A from L154, UNDECIDED at B1034 | numbers **NM (scoped)**; outcome **N** (by B1814) |
| **B1813** | PROVED | both: "the counting rule is CHOSEN"; A0 by words of length n, A1 by trace ≤ T, and the s-family between them | NO, by construction | argued (the family) | **N** |
| **B1814** | NEGATIVE as sealed (D2) | both: A0 "word length ≤ 16"; A1 "trace ≤ 400" | NO, by construction. The clock is not decided by the six (power about 19%) | sealed | **N** |
| **B852** | PROVED (not preregistered; exact control) | the Farey family's pressure: "inducing the parabolic point away … destroys the transition" | NO. It is the mathematics that makes the two clocks the ends of one family (s = 0 and s = 1) | none to make | **N** |
| **B1720, B1741, B1748, B1749** | NEGATIVE; PROVED as sealed (B1741 a READING, not PASSED; B1749 scoped to the strip) | one point per thread (the apex); censuses cut by word length: "every primitive positive class w of length 2-9" (B1720, B1741), lengths 10–11 (B1748), "length 12 with apex height in [2.0, 3.6]" (B1749) | **NO** for the conclusions as scoped. B1720's NEGATIVE is a best over its census. B1749's result is a property of the frame's strip: random 125-point sets in the band find it 99.7% of the time. **NOT DECIDED** which thread would be best under a trace-cut census of equal size. No measure enters | taken (convenience) | **N** |
| **L244 (c)**: β_c = 2 log φ (OPEN_LEADS, verified on main 2026-10-03) | verified identity; the lead is OPEN | per tick: "verified on main … as the topological entropy of the monodromy LR" | NO for the identity, which is ℓ(LR)/2 = the golden path's length per move (reader A, C2). The "Hagedorn point" reading is not established. P-441: B1813's s = 1 is not β_c | — | identity **N**; reading **U** |
| **B156** | PROVED | per letter: "Wall-avoiding history entropy = log 2" (the Ω cone, 12 shears) | NO. It is a counting fact, and it is the move clock's rate by definition | definition | **N** |
| **B189** | NEGATIVE | the Ω cone graded by depth, i.e. move count | **NOT DECIDED** under a grading by length. Its mechanism (a graded-DAG truncation artifact) would be expected to persist | taken | **N** (likely) |

### 1b. Results with no thread weight (the dial does not reach them)

| result | status | ordering | depends? | class |
|---|---|---|---|---|
| Universal statements over a thread family: B1600 (W1–W4; row 911), B1601, B1602, B1605, B1675 (W34; rows 1264, 1267), B1690 (W76, row 1149: "all 248 mirror-symmetric threads of 8798 to length 16"), B1733 ("0 mismatches in 6 989 … checks over 241 classes"), B1666 L0, B1676's mod-8 law; row 1123's existence claim (690 of 745 threads have CS ≠ 0) | PROVED / NEGATIVE / VERIFIED | a finite family, mostly cut by word length (B1666's by trace) | **NO**: a universal statement carries no weight. Note that a word-length cut samples deep-run threads (Lᵃ R, trace a + 2) late. Check (c) carries B1676's law to a family cut by trace, 10 times larger | **N** |
| Single-word time averages: B1620 (the letter walks along the rule's word), B1621 (the clock's and tick's means, "averaged over the rule's time"), B1630, B1636 | PROVED (thread results, v1.49) | the rule's own word, letter by letter (reader A's T7: fibre time) | **NO**: one word, no measure over threads | **N** |
| Thread-level internal time: B716 (the suspension flow), B721 (tracial II₁), B850 (m004's own length spectrum), B413/B415 (the tower measure over levels n, proportional to length on one thread) | PROVED / NEGATIVE | one thread | **NO**: outside the weave's dial | **N** |
| GENESIS v1.55 (B1750): "the arrow is forced (the walk's escape, B1083, B1662)" | adopted | the walk | **NO**: escape belongs to any one-sided history from the identity on the group, walk or followed geodesic. Only the rate per step is move time | **N** |
| The arena (row 1232): three facts VERIFIED (the axes of LLR and LRR through ω; the root's closest approach to ω; the 26 reciprocal threads through i) | VERIFIED | geometry of axes | **NO**: no measure | **N** |

### 1c. Seat results that weight threads

| result | status | ordering (quote) | depends? | argued / ruled / taken | class |
|---|---|---|---|---|---|
| **chat1's root-share check** (row 1139; B1650's addendum) | **VERIFIED** | word weights × action: "the word weights 2⁻ⁿ, 3⁻ⁿ and 1/(n(n − 1)L(n))", times e^(−Vol/π) | **The number: YES.** The share moves with the word weight: 0.27, 0.50 and 0.66 under three move-type weights. **The "plurality" (LR the largest class): NOT DECIDED** under a geometric weight; not computed | taken (three weights) | number **NM (scoped)**; plurality not decided |
| **SM § 320** (row 1450) | **READ** ("a design reading, no rule") | length-weighted, Duke/ELMV: "the length-weighted sum of any point-pair kernel unfolds to a constant" | **YES.** By word length the democratic sum's limit is Minkowski's lift, not flat (B1813's A0 table; reader A, T4) | taken | **U** (needs geometric) |
| **W57** (row 1099) | **REGISTERED** at headline; its premise scoped by the audit lane (row 1112, P-107) | "τ hyperbolic, the invariant Gaussian on the allowed couplings" | **YES.** Under Minkowski's measure the deep hierarchies it found in 25% of draws are power-suppressed (B1813 § 3) | argued by a uniqueness premise that P-107 shows false | **U** (needs geometric) |
| **W95, W98** (rows 1246, 1247, 1252) | **READ** at headline; not re-run on main | by discriminant, then "every primitive thread with 3 ≤ t ≤ 40 (245 classes)" | **NOT DECIDED.** By-trace and by-discriminant agree exactly (W98); no word-length run | **ruled** (P-180) | **U** |
| chat1's trace layers (row 1250 (A)) | **READ**; not re-run on main | "f's trace layers settle toward 0.31500491 (agrees with B1666; independent code)" | **YES** (as B1666 L1) | the W-trace design | **U** (B1666 carries it) |
| W42's thread-H¹ census (row 1058) | READ in full; the census registered | per thread to length 12 | as B1633 | taken | **U** (B1633 carries it) |

### 1d. Rulings and readings (not results; listed because they carry a clock)

| item | what it says | clock | status |
|---|---|---|---|
| **P-180's reason** (`S_THE_PUSH_BACK.md` § 9.2; ruled 2026-10-16) | "Primitive threads of one length are equal time in the motion." | **geometric** | the ruling's operative content ("W95 by trace" against "by discriminant") is geometric on both sides and clock-neutral between them; the reason sentence is a definition of time |
| `S_THE_PUSH_BACK.md` § 10, P-183 | "The feedback is the walk"; "Its long-run averages are set by equidistribution" | mixes both | the second sentence is false of the walk (0.517, B1663; P-469); a reading (LEAP) |
| P-183's pairing | the trace formula sums "over closed geodesics (the threads, by length)" | geometric | a reading; check (e) shows the move clock's threads do not reach the constant mode |
| "The weave's uniform measure" (B1629, B1633, B1676, B1722) | the move clock named as the weave's | moves | a name, never argued (P-471, T5 of reader A) |
| GM5b's walk as the dynamics | the walk with fair steps | moves | a reading. B1663 firewalls "that the walk is the physical motion" |
| P-413, P-441 | the forced weight; the critical line | — | QUEUED |

---

## 2. The two lists

**NEEDS-GEOMETRIC, established:**
1. **B1666 L1** (PROVED as sealed): the trace layers of f reach 0.315, "the weave side meeting the wave side's constant"
   (THE_WEAVE). Ordered by moves the same per-thread function gives 0.508, i.e. 0.518 length-weighted (check (e)). The
   claim says "trace by trace"; THE_WEAVE's gloss ("the weave side meeting the wave side's constant") does not.
2. **B1666's "quarter of threads"** with #L ≡ #R (mod 4): 0.250 by trace, 0.324 by moves. THE_WEAVE states it without
   the ordering.

Nothing else established needs it. Each item that does is unestablished: § 320's flatness, W57, W95 and W98, chat1's
trace layers, P-183's pairing, and P-180's reason.

**NEEDS-MOVES, established** (each a number stated under its own weights, none a conclusion another result builds on):
1. **B1629's (k+1)/2^k** (GENESIS FK10 v1.38, scoped v1.44). By trace the deep-letter share is 0.81–0.96 and rising. Its
   scoped conclusion, no atom at the cusp, is NEUTRAL.
2. **B1722's measure-weighted misfits** (3.85 against 4.62; 3.04 against 3.77). Its NEGATIVE is matched under the
   geometric clock by B1814.
3. **chat1's root shares** 0.27 / 0.50 / 0.66 (row 1139, VERIFIED). Its plurality is not decided.

**Bridges** (neutral facts that connect a clock to a dynamics):
- B1663: walk ⇒ Minkowski's measure.
- B1813: length ⇒ area, numerically, as equidistribution.

## 3. The verdict

> **The record's established results are consistent with: BOTH.**

## 4. What this implies for GM5b's walk as the programme's whole dynamics

1. **It is admissible.** No established result contradicts it.
   - The one established geometric result, B1666 L1, is a statement about an ordering, not about the dynamics, and it
     stays true as such.
   - T1 therefore does not give the inconsistency § 8 of the briefing asked about. The decision must come from T2 (does
     the frame's own structure need hyperbolic volume?) or T3/T4.
2. **It is not forced by the established record.**
   - GM5b adopts the pull-back's legality. The walk's step law ("no preference", equal weights, finitely supported) is
     a ruling and a choice.
   - B1663 firewalls the walk as the physical motion. The theorem that every finitely supported walk is singular is
     cited, not read (P-473).
3. **Adopting it would cost these, all readings and none results:**
   - (a) P-180's reason sentence becomes false of the motion. In the walk, equal steps are equal time; equal length is
     not. It is the single place where a ruled sentence and the adopted dynamics disagree, and it is already inside one
     document (`S_THE_PUSH_BACK.md` §§ 1, 9.2, 10).
   - (b) B1666's "weave meets wave" gloss and P-183's identification of weave and wave through the trace formula "by
     length" describe an ordering the dynamics would not generate. They would be relabelled CHOSEN orderings.
   - (c) So would § 320's "democratic = flat" and W57's "seed's own measure".
4. **The walk alone still does not give a τ-law.**
   - It gives a boundary point. B1663's 0.517 and B1813's A0 place τ by arclength along the ray, which is geometric
     placement (reader A, T9). A placement by steps puts τ on Re τ = 0 (the briefing's § 2, G).
   - Even the walk-as-whole-dynamics reading leaves the placement CHOSEN. The "move clock" of B1813 and B1814 is a mixed
     clock.

## 5. Where dependence was not decided

- **B1676's scalar.** Its limit by trace is indicated (6.5% at T = 1200, falling) and not proved. Equidistribution of
  closed geodesics in the finite image would give it; that was not read at source.
- **The root-share check's plurality** under a geometric weight: not computed.
- **B1722's NEGATIVE** recomputed on its own census under a geometric weight: not computed. B1814 covers the outcome by
  another instrument.
- **B1720 and B1741's best thread** under a census cut by trace: not computed.
- **B1666 L2's regression** on a census cut by moves: not computed.
- **B189** under a grading by length: not computed.
- **W95 and W98** by word length: not run anywhere.

## 6. Incidental findings (for the register, if main agrees)

- **THE_WEAVE's B1666 entry gives no ordering for one statement.** "So coherent averages live on the quarter of threads"
  is a by-trace number, 0.324 by moves. "By trace, the threads reach the constant mode" does name its ordering, but its
  gloss does not say that the move ordering gives 0.517.
- **B1637 § 2 over-reads B1629 even in the move clock.** It says "Under the weave's uniform measure the principle's
  dynamics puts no weight there" (Im τ 2.6–7). B1813's A0 puts 3.5% above Im τ = 3, and B1648's scope is the limit
  Y → ∞.
- **B1633's W4 comparison, not decided.** B1633 compares its word fraction at even n (0.3125) with "the seat's primitive
  census … 237/745 ≈ 0.32 to length 12". With B1633's own projectors, one count per thread over lengths 2–12 gives
  157/745 (0.211), because odd lengths carry no zero modes. Either the seat's census counts something else (V = T ⊕ T̄?
  signed threads?) or the comparison mixes two quantities. Not decided here.
- **Already registered:** S_THE_PUSH_BACK § 10's 0.315 for the walk (P-469); B1813's Seen first missing B1666 (P-470);
  "democratic" in two senses (P-471).

---

## Appendix: the checks (scratchpad; one run each; not banked)

**Controls.** Every one reproduced a recorded value before the new cells were read:
- the trace enumerator gives 30 674 threads to T = 600 with layers 1, 2, 2, 3 at t = 3–6 (B1666's L0);
- the length enumerator gives 8 798 Lyndon words of length 2–16, 3 822 of odd trace, 916 rank-one, off-diagonal 3.1%
  (B1676);
- the deep share at n = 16 equals (k+1)/2^k (B1629);
- B1666's stored A_t at t = 5, 7 and 10 is reproduced exactly by its own `_thread`.

**Outputs.**

```
(a) letters in runs >= k      k=2    k=3    k=4    k=5    k=6    k=7    k=8
    by length n = 16          0.750  0.500  0.313  0.188  0.109  0.063  0.035   (= (k+1)/2^k)
    by trace T <= 300         0.946  0.901  0.865  0.835  0.808  0.785  0.764
    by trace T <= 600         0.952  0.913  0.881  0.854  0.831  0.810  0.792
    by trace T <= 1200        0.957  0.922  0.893  0.869  0.848  0.830  0.814   (109 880 threads)
(b) B1633's Pi, one weight per thread: distance from scalar / tr Pi / zero-mode fraction
    length 2-16  8.2e-4 / 0.287 / 0.210     length 16  1.6e-3 / 0.457 / 0.327
    T <= 600     1.5e-4 / 0.210 / 0.158     T <= 1200  9.4e-5 / 0.208 / 0.157   (1/2 * 5/12 = 0.2083; 1/2 * 5/16 = 0.1563)
(c) B1676: odd threads / rank-one share / rank1-iff-mod-8 holds on / diag / offdiag:diag
    length 2-16  3 822 / 0.240 / 3 822 / 0.0799 / 0.031
    T <= 300     2 904 / 0.251 / 2 904 / 0.0838 / 0.189
    T <= 600    10 222 / 0.252 / 10 222 / 0.0841 / 0.111
    T <= 1200   36 610 / 0.251 / 36 610 / 0.0838 / 0.065
(d) #L - #R mod 8, shares 0..7
    length 2-16  .164 .089 .163 .086 .160 .086 .163 .089     (= 0 mod 4: 0.324)
    T <= 1200    .126 .125 .124 .125 .125 .125 .124 .125     (= 0 mod 4: 0.250)
(e) B1666's <f> per thread, threads of exactly word length n (its _thread unchanged)
    n = 6: 0.490 (9)  8: 0.502 (30)  10: 0.504 (99)  12: 0.507 (335)  14: 0.508 +- 0.003 (1 161)
    length-weighted:  0.509, 0.518, 0.517, 0.518, 0.518      [B1663's walk: 0.5157-0.5185; by trace: 0.3144 -> 0.31500]
```

**Code** (the parts that are new; the averaging bodies are copied verbatim from B1633's `main()` and B1676's
`tick_on_the_weave_main.py`, which import B1611's and B1617's modules read-only):

```python
Lm = ((1, 1), (0, 1)); Rm = ((1, 0), (1, 1))                       # GENESIS core convention
def threads_by_trace(T):                  # every Lyndon word over L < R (both letters) with trace <= T
    out, stack = [], [("L", Lm)]
    while stack:
        q, M = stack.pop(); tq = M[0][0] + M[1][1]
        if q[-1] == "R" and tq <= T and all(q < q[i:] + q[:i] for i in range(1, len(q))): out.append((q, tq))
        for ch, X in (("L", Lm), ("R", Rm)):
            N = mm(M, X)                  # positive words: completions only grow entrywise, and end in R
            bound = (N[0][0] + N[1][1]) if ch == "R" else (N[0][0] + N[0][1] + N[1][1])   # = tr(N R)
            if bound <= T: stack.append((q + ch, N))
    return out
def deep_share(ws, k):                    # B1629 P4: letters in a cyclic run of length >= k, pooled
    return sum(r for w, _ in ws for r in cyclic_runs(w) if r >= k) / sum(len(w) for w, _ in ws)
def word_lifts_all_rotations(w):          # lift of rotation i = h_i^-1 g h_i in B1633's group G (order 96)
    hs = [e]
    for ch in w: hs.append(G.mult[hs[-1]][iL if ch == "L" else iR])
    return [G.mult[G.mult[INV[h]][hs[-1]]][h] for h in hs[:-1]]
def b1633_avg(ws):                        # one weight per thread: mean over its rotations of P_g, then over threads
    acc = np.zeros((3, 3), complex)
    for w, _ in ws:
        gs = word_lifts_all_rotations(w); acc += sum(P[g] for g in gs) / len(gs)
    return acc / len(ws)                  # then: norm(Pi - tr(Pi)/3 I), tr Pi, share with tr P_g > 1/2
# (e): lr = B1666's the_layers_robust.py loaded by importlib (no __main__); for each Lyndon word w of exactly
#      length n: lr._thread((w, trace(w)))["f"]; mean over threads, and weighted by 2 arccosh(t/2).
```

Run on 2026-10-29 with single-threaded BLAS, at most 7 cores. The scratchpad files (`by_trace_checks.py`,
`b1666_by_length.py` and their outputs) are not preserved in the repo.
