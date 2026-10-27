# B1786 — THE SLOPE PRINCIPLE OUT OF SAMPLE: ON THE LINES OF ORDER 25 AND 30, WHICH NO RECORD HAD COMPARED WITH THE SIX, THE SLOPE 2/5 CARRIES THEM SPECIFICALLY (8 OF 160 000 RANDOM HIERARCHIES AS LOW) AND NO OTHER SLOPE CARRIES THEM AT ALL — THE SLOPE 1/10, WITH THE SAME LEADING SECOND-GENERATION EXPONENTS, INCLUDED; THE DECISIVE CELL HOLDS AS SEALED, BUT UNDER THE CLASS-CHOOSING NULL IT SITS ON THE BAR (NOT PASSED). THE PRINCIPLE SURVIVES ITS FIRST OUT-OF-SAMPLE TEST; IT SELECTS THE SLOPE THROUGH ONE MEASURED EXPONENT (B1788) — A SELECTION BY THE DATA, STABLE OUT OF SAMPLE, NOT A DERIVATION

**Verdict: PROVED as sealed — the decisive cell D holds; a READING, not PASSED (under the class-choosing null THE_BAR's m·r sits on the 0.01 gate at m = 41 and fails it at m = 73; § 2).** cc (main), 2026-10-27, step 1 of main's plan (docs/MAINS_PLAN.md, P-393; P-384). Sealed
11ebe577b; census 4b5d8c602 and comparison c31c4d0e1, each committed unread, then read once. **0 of 19.**

## 1. The cells, as sealed (`verification/compare_run.txt`, `comparison.json`)

| cell | prediction | outcome |
|---|---|---|
| **D, decisive** | on the 30 slope-2/5 lines ≤ 0.1% of random hierarchies as low a χ²_six (the seat's menu, mean over 40 seeds), **and** no line of any other slope with a row below 16.75 | **HOLDS**: min 3.005; 0.005% (8 of 160 000; worst seed 0.025%); no other slope below 16.75 |
| P1 | some slope-2/5 row below 16.75 | **holds** (12 of 30 lines) |
| C1 | B1741's and B1749's best rows to 10⁻⁹; the T-law at order 25 to 10⁻⁶; the counts 300, 288 and every order exact | **holds** (0.0, 0.0; 4.9 × 10⁻¹²; exact) |
| C2 | B1735's 3.0945633 on B1726's census | **holds** (3.0945633097836) |

**The read-outs:**
- **The slope-2/5 class at 1%:** specific in every menu. Seat 0.005%, covariant 0.014%, free 0.064%.
- **The slope 1/10:** its least is 919 (seat; 41.4 covariant, 740 free), and all 20 lines lie at 919–1106. The rest: least
  103 (seat, on α = 12/25); no rest line below 16.75.
- **The nine on the slope-2/5 lines:** least 146 (seat); not below 21.67.
- **Which offsets carry the six:**
  - order 25: 8 of 20 slope-2/5 lines below 16.75 (b = 3, 4, 11, 12, 17, 19, 21, 23 over 25);
  - order 30: 4 of 10 (b = 1/6, 13/30, 23/30, 5/6);
  - in equal-valued pairs — the record's mirror w → −w̄, which on slope 2/5 sends b to 3/5 − b (4/25 ↔ 11/25 at 5.4, 1/6 ↔ 13/30 at 5.0, 23/30 ↔ 5/6 at 3.0; it holds on 131 712 row pairs to 3 × 10⁻⁶), so the 12 lines are 6 of 15 independent pairs.
- **The best row:** (2/5, 23/30) — its mirror (2/5, 5/6) ties to 10⁻¹¹; the instrument's describe() prints the one with the smaller worst factor — at τ = 0.269 + 3.037i, L_max, readings (S̃, S, S), c = 3. Model over measured on the six:
  1.02, 1.16, 1.03, 0.83, 0.98, 0.99. It sits on B1749's strip (Im τ ≈ 3.03).
- **The random-subset control:** 11% of 200 random 30-line subsets of the 588 lines reach as low. Most random subsets
  contain a slope-2/5 line (a 30-line subset contains one with probability about 79%), so this control measures the
  presence of those lines. The class choice is carried by D's second half: no line of another slope comes near.
- **The interrupted first run:** killed by a machine reboot; its partial log was kept unread
  (`compare_run_interrupted.txt`). The rerun is deterministic.

## 2. THE_BAR

- **The decisive look:** 8 hits of 160 000; r, the exact 97.5% upper end, is 9.85 × 10⁻⁵.
- **Bonferroni:** at the ledger's m = 41, m·r = 0.0040 < 0.01; at the inclusive 73, 0.0072 < 0.01. It passes at both
  counts (limits 26 and 12 hits).
**The class-choosing null decides the grade** (main's referee; `verification/referee/`; B1741's own χ² arithmetic on
the census, validated against the sealed run — 8 and 67 hits reproduced, no difference against brute force on 12 seeds; 10
million fresh targets, seeds 2001–4500). Random hierarchies may choose their own slope class among the 26 present at orders
25 and 30:

| null (fresh, 10⁷ targets) | fraction | r (97.5%) | m·r at 41 | at 73 |
|---|---|---|---|---|
| some class ≤ 3.005 and every other ≥ 16.75 (the class-choosing form of D) | 2.62 × 10⁻⁴ | 2.72 × 10⁻⁴ | **0.0112** | **0.0199** |
| the class chosen as the data chose it (the best class on B1749's and B1755's lines at the same apexes), given that class has lines at 25 and 30 | 2.29 × 10⁻⁴ | 2.43 × 10⁻⁴ | **0.0099** | **0.0177** |
| the same, unconditional | 1.13 × 10⁻⁴ | 1.20 × 10⁻⁴ | 0.0049 | 0.0087 |
| any class ≤ 3.005 (specificity alone) | 4.18 × 10⁻⁴ | 4.31 × 10⁻⁴ | 0.0177 | 0.0314 |
| as sealed: the class 2/5 named in advance | 4.79 × 10⁻⁵ | 5.24 × 10⁻⁵ | 0.0021 | 0.0038 |

- **Under the fair nulls the result sits on the gate at the ledger's m = 41 and fails at the inclusive m = 73.** The
  class-choosing form gives 0.0112; the prior-chosen class, conditional, gives 0.0099. It is not PASSED.
- **Why the sealed number overstates it.** The sealed cell named 2/5 in advance, but 2/5 was named from the same
  apexes' data at lower orders. Random hierarchies that fit some class this well are spread over many classes: 2/5
  carries 11% of them, and 13/30, 12/25 and 11/25 about as many each. The "no other slope" half is cheap: 63% of
  random any-class hits satisfy it automatically.
- **What the out-of-sample event was worth.** Take a random target that fits slope 2/5 at the earlier orders as well as
  the data did (χ²_six ≤ 3.574 on B1749's census): it goes on to the event at orders 25 and 30 in 13% of cases (107 of
  827). The prediction was a real test, and the data passed it, but at those odds it is not a strong one.
- **A labelled read-out, not a grade:** demanding every other class above the data's own runner-up (103.1, read from
  the data) gives m·r = 0.0018 and 0.0032.
- **A third opinion is asked regardless** (THE_BAR): of the SM seat, with the web seat's checking pass (§ 6).

## 3. What it shows

- **The six select the slope 2/5 among all slopes, now out of sample.** The tested order sets so far:
  - 10, 12 and below: B1749, B1753; and the SM seat's W162, over Im τ 1.2–12;
  - 15 and 20: B1755;
  - 25 and 30: this arc, fixed before any of its lines was computed.

  On each, the six live on the slope-2/5 lines and on no others; here the margin is large (the next class at 103, the
  slope 1/10 at 919).
- **The slope 1/10 shares the leading second-generation exponents (3/10, 1/5) and fails completely.** B1788's closed form
  says why: the first generation separates them (m₁/m₃ exponents (4/5, 11/20, 11/20) on 2/5 against (13/20, 7/10, ½) on
  1/10).
- **The offset stays selective:** 12 of 30 lines, in pairs, as at B1755 (4 of 10 per order). Which offsets carry the six
  is not explained; the offset remains an input.

## 4. What it means — the reading, against the one written before the run

The sealed reading for "D holds": "the principle passes its first out-of-sample test, and the slope stops being a free
input on this evidence." **The first half stands; the second needs B1788's qualification.**
- B1788 shows that, given five-ality alignment (5α ∈ ℤ), the principle's second condition (‖3α‖ = 1/5) is equivalent to
  e_up = 3/10, which is the measured up quarks' second-generation exponent.
- So the principle selects the slope with one structural condition plus one measured number.
- What this test establishes is that this selection is **unique and stable out of sample**: no other slope at any order
  tested carries the six.

**In the referee's words, adopted:** "Slope 2/5 alone carries the six at orders 25 and 30. The principle, which is
five-ality alignment plus the measured up exponent (B1788), survives its first out-of-sample test. The slope remains an
input, now selected by one discrete condition read from data; no input removed."
- The bare empirical rule "only 2/5 works" makes the same prediction, so D tests that the selection is stable, not what
  causes it.
- Five-ality alignment makes the lepton and down exponents equal; they match the data only with c = 3, set by hand.
- It counts as **a reduction only if** a data-free reason for ‖3α‖ = 1/5 (the Higgs at the generator of SU(5)'s centre)
  is found. P-384 stays open for that reason, and main's ledger of inputs removed gets no row.

## 5. Scope

- **Fixed in this test:** B1656's frame at B1667's end; B1741's instrument and measure; B1749's 125 apex points (used
  before by B1749 and B1755; disclosed); c = 3, the reading rule, and Im τ on the strip, all by hand.
- **Tested:** the lines of orders 25 and 30 only.
- **Grade:** not PASSED (§ 2), and a third opinion is asked. The points: 125 apexes, about 74 of them independent under the mirror.

## 6. The relays

To the SM seat and the web seat: the third opinion on this arc (its own instrument, own seeds) and the web seat's checking
pass (offered and accepted). Relay `docs/handoffs/CC_TO_SM_AND_CHAT1_2026-10-27_B1786_THE_SLOPE_OUT_OF_SAMPLE.md`.

## The referee

Main's hostile read-only referee (`audit/referee_b1786/`; its scripts and summaries kept in `verification/referee/`):

1. **Custody clean.** All 16 pins match; the census sha256 matches both the raw file and the gunzip output; seeds
   1829–1868 × 4 000. D is computed as worded (compare.py 114–120, 145–148): the seat's menu, four readings × c ∈ {1, 3},
   both horocycles, every row of the 558 other-slope lines. The per-line minima and the 8 and 67 hits were reproduced
   independently. The interrupted run could not leak, since outputs are written only at exit.
2. **The class-choosing null (CORRECTION, adopted):** § 2. It decided the grade: not PASSED.
3. **Out of sample (NOTE):**
   - Reusing the apexes adds no bias: they are placed by rule, and the null searches the same points.
   - Not new: the slope, the Im τ band (best rows at 3.04–3.06 in B1749, B1755 and here) and the offset rate of about 40%.
   - The mirror halves the independent counts.
4. **The principle (CORRECTION, adopted):** "the slope stops being a free input" is not supportable (§ 4).
5. **The slope 1/10 (NOTE, confirmed).**
   - At the best apex, against the 2/5 lines, its lines miss u/t by ×42, d/b by ×0.06 and e/τ by ×5.8. B1788's
     first-generation exponent gaps predict ×17.5, ×0.057 and ×2.6: the same directions and orders.
   - On its best row the second generation contributes 13.6 to χ² and the first generation 431.
   - B1788 explains the difference between the slopes, not the absolute first-generation values at Im τ ≈ 3.
6. **The offset pairs (NOTE):** the mirror w → −w̄ (§ 1). It is not the T-law.

## Seen first

At the seal: as in the PREREGISTRATION. At landing:
`VERDICT topic-sweep /slope|out of sample|order 25|order 30|five-ality|unit twist|line order/ (full text): 145 of 1535 arcs on main match (NEGATIVE 30, OPEN 5, PROVED 108, RETRACTED 1, no verdict file 1); 16 register rows match (DONE 8, QUEUED 8)`.
Since the seal:
- the SM seat's W162 (row 1419; orders ≤ 12, Im τ 1.2–12; no other slope at any height);
- B1788 (the closed form; given 5α ∈ ℤ, condition 2 is the measured 3 : 2 restated).

**Literature:** the check of 2026-10-24 (P-382), as at the seal. No published mechanism ties an SU(5)-centre Wilson line
with the Higgs at the generator to the charged-fermion hierarchy; nothing new was found since.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`.
- `verification/census.py` → `census.jsonl.gz` (with `census.jsonl.sha256`; `gunzip -k` restores the raw file the sealed
  compare.py reads), `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`, and `compare_run_interrupted.txt` (the killed first
  run, unread).

The lock: `tests/test_b1786_the_slope_principle_out_of_sample.py`.
