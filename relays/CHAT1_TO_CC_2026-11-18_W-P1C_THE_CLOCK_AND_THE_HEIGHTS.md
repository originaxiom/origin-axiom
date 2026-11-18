# W-P1c: the clock and the heights. Under the move count the weave spends 0.74, 0.17, 0.008 and 0.0004 of its time above modular heights 1.118, 2, 4 and 6; under length, 0.85, 0.47, 0.23 and 0.15, approaching the area's 3/(πy). The two agree with B1813's tails. Above height 2 the move count's time is carried by words whose longest run is 4 to 9 letters; length's, by words with runs of 10 or more

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. It is step 3 of card W-P1
(`relays/CHAT1_TO_CC_2026-11-18_W-P1_THE_PROCESS_READING.md`, § 5), at the author's word of 2026-11-18.

**Order of work.**
- The condition was written first: `relays/cards/CHAT1_W-P1_STEPS_conditions.md`, step 3 (522248fe8).
- The script `relays/chat1_2026-11-18_wp1/wp1c_heights.py` was committed (98bf1b6d1) before its one run.
- Before that commit, its functions were smoke-tested on control inputs only: LR, L³R, and the count of primitive
  classes at trace 30. No share was computed.
- Its output is `wp1c_heights_out.txt` (637ed8d19).

**Typing.** [E] marks what the run or the record establishes; [J] marks this seat's judgement. Nothing here is
compared with a measured value, and no frame is read.

---

## 0. In short

1. **[E] The controls hold.** LR spends no time above √5/2. LⁿR reaches √((n + 2)² − 4)/2. Every word's pieces sum to
   its translation length. No thread rises above a/2 + 1, where a is its longest run of one letter.
2. **[E] The two clocks' shares of time above modular heights 1.118, 2, 4 and 6:**
   - (a), the move count: 0.737, 0.170, 0.0079 and 0.0004, the same at 20, 40 and 80 letters;
   - (b), length: 0.853, 0.474, 0.235 and 0.155 at trace 400 (14,690 primitive classes), rising towards the area's
     0.854, 0.477, 0.239 and 0.159.
3. **[E] They agree with the record.** B1813's law for the move count, 3.9·4^(−Y)/√Y, gives 0.172, 0.0076 and 0.0004
   at heights 2, 4 and 6. W-F24's X4 gives 0.168 above 2 and 0.007 above 4.
4. **[E] Which words carry the time above height 2:**
   - under (a), words whose longest run is 4 or 5 (0.40) or 6 to 9 (0.55);
   - under (b), words with a run of 10 or more (0.74).
5. **[J] What it means.** The clocks differ by which threads they let count, not only by how much time they spend
   high. Under length, the long-run words that reach the cusp are many and short (LⁿR has trace n + 2), so they
   dominate. Under the move count, a long run is exponentially rare in its length.

---

## 1. The run

**Definitions** (as the condition fixed them).
- A word is a positive word in L = [[1, 1], [0, 1]] and R = [[1, 0], [1, 1]] with both letters. Its thread is the
  closed geodesic of its matrix.
- Height is Im τ after reduction to SL(2, ℤ)'s standard fundamental domain: a modular height. Time is hyperbolic arc
  length along one period.
- **(a)** W-F24's measure: uniform random words of n letters, 2,000 for each of n = 20, 40 and 80 (seeds 1, 2, 3).
  Each thread is weighted by its length, and the time shares are pooled.
- **(b)** Every primitive cyclic word (a Lyndon word, L < R) with both letters and trace at most X, for X = 100, 200
  and 400, each counted once, with the time shares pooled.

**Method.** One period is cut into one piece per letter. For the word A₀ ⋯ Aₙ₋₁ and its rotations Mₖ, each axis
crosses the imaginary axis at a point qₖ. On Mₖ's axis, qₖ, Aₖqₖ₊₁, …, Mₖqₖ follow in order and span one period. Each
piece is sampled uniformly in arc length, at least 120 points per unit length, and each sample is reduced. Endpoints
are computed to 60 digits.

## 2. The controls (H0)

| control | result |
|---|---|
| LR's top, against √5/2 = 1.118034 | 1.118024 (the sample nearest the top); time above 1.118: 0 |
| L²R, L³R, L⁵R, L⁸R's tops, against √((n + 2)² − 4)/2 | 1.732036, 2.291269, 3.354102, 4.898937, each within 5e-5 of 1.732051, 2.291288, 3.354102, 4.898979 |
| pieces summed, against the translation length 2 arccosh(tr/2) | equal to the printed digits for every word of (a) and (b) |
| the highest sample, against a/2 + 1 | never above, for every word of (a) and (b) |
| (b)'s shares as X grows | 0.467, 0.472, 0.474 above 2 at X = 100, 200, 400, rising towards 0.477 |

## 3. The shares of time above each height

| clock | 1.118 | 2 | 4 | 6 |
|---|---|---|---|---|
| (a) n = 20 | 0.73768 | 0.17179 | 0.00781 | 0.00043 |
| (a) n = 40 | 0.73754 | 0.16982 | 0.00792 | 0.00039 |
| (a) n = 80 | 0.73600 | 0.16889 | 0.00771 | 0.00034 |
| (b) X = 100, 1,214 classes | 0.85005 | 0.46691 | 0.22459 | 0.14347 |
| (b) X = 200, 4,186 classes | 0.85251 | 0.47174 | 0.23138 | 0.15094 |
| (b) X = 400, 14,690 classes | 0.85334 | 0.47427 | 0.23470 | 0.15485 |
| the area, 3/(πy) | 0.85412 | 0.47746 | 0.23873 | 0.15915 |
| B1813's move-count law, 3.9·4^(−Y)/√Y | (0.78, asymptotic) | 0.172 | 0.0076 | 0.00039 |

- [E] (a) settles: its shares move by less than 0.003 from n = 20 to n = 80.
- [E] (b)'s shares rise with X towards the area at every height, as the equidistribution of closed geodesics ordered
  by length requires (Bowen, Margulis; standard). At X = 400 they are within 0.005 of it.
- [E] (a) agrees with B1813's law at heights 2 to 6, and with W-F24's X4 (0.168 and 0.007). The law is asymptotic
  and is not meant at 1.118.

## 4. Which words carry it (H3)

Each word's time above a height is binned by the word's longest cyclic run of one letter, a. The table gives each bin's
share of all the time above that height.

| clock, height | a = 1 | 2 | 3 | 4–5 | 6–9 | 10+ |
|---|---|---|---|---|---|---|
| (a) n = 40, above 1.118 | 0 | 0 | 0.029 | 0.477 | 0.460 | 0.034 |
| (a) n = 40, above 2 | 0 | 0 | 0.007 | 0.399 | 0.546 | 0.048 |
| (a) n = 40, above 4 | 0 | 0 | 0 | 0 | 0.707 | 0.293 |
| (a) n = 40, above 6 | 0 | 0 | 0 | 0 | 0 | 1.000 |
| (b) X = 400, above 1.118 | 0 | 0.005 | 0.029 | 0.117 | 0.227 | 0.622 |
| (b) X = 400, above 2 | 0 | 0 | 0.004 | 0.063 | 0.189 | 0.744 |
| (b) X = 400, above 4 | 0 | 0 | 0 | 0 | 0.057 | 0.943 |
| (b) X = 400, above 6 | 0 | 0 | 0 | 0 | 0 | 1.000 |

- [E] Each row respects the bound: a word rises above y only with a run of more than 2y − 2. Above 4 every word has a
  run of 7 or more, and above 6 a run of 11 or more.
- [E] **This bins by the word's longest run, not by the run at each excursion.** At n = 40 a typical word's longest
  run is 4 to 6, so a word's time high may come from a shorter run than its longest. The finer attribution, by the run
  under each excursion, is not done here.

## 5. What it means

- [J] **The two clocks differ in which threads they count.** Under length, each primitive class counts once. The
  long-run words that reach the cusp are many and have small trace: LⁿR has trace n + 2. So above height 2, 74% of
  length's time is in words with a run of 10 or more. Under the move count, a run of n equal letters is rare
  (probability about 2^(−n) at each place). The time above 2 comes from the commoner runs of 4 to 9, which rise only
  to between 2 and 5.5.
- [J] **For card W-P1's § 3.1:** the weight over threads (C01) is not only a weight on heights. It is a choice of
  which words matter at each height. Under the record's principle, (a), the cusp above height 4 is reached by runs of 7
  or more letters and holds under 1% of the time. Frame C's hierarchy is a height effect (W-F24). So under (a), most of
  the read-out comes from heights 1.118 to 2, where the hierarchy is weakest. This is the record's W-F24 reading, now
  attributed to words.
- [J] **What is new here** is only § 4. § 3 reproduces B1813 and W-F24, and confirms the area at modular heights by a
  direct enumeration.

## 6. Typed

- **[E] by the run:** §§ 2, 3 and 4.
- **[E] by the record:** B1813's law; W-F24's X4.
- **[E] standard:** the equidistribution of closed geodesics; the bound a/2 < height < a/2 + 1 (card W-P1, § 2.1).
- **[J]:** § 0 item 5, and § 5.
- **Expectations, set in the condition before the run:** (a) close to W-F24's X4 and below 1e-3 above 6; (b) near
  the area; above 2, (a)'s time carried by runs of three or more. Each is met.

## Files

- `relays/chat1_2026-11-18_wp1/wp1c_heights.py` (98bf1b6d1, before its run), `wp1c_heights_out.txt` and
  `wp1c_heights_err.txt` (637ed8d19), `SCRIPT_SHA256.txt`.
- The condition: `relays/cards/CHAT1_W-P1_STEPS_conditions.md` (522248fe8).
- Cited: B1813, W-F24, P-845, card W-P1.

0 of 19.
