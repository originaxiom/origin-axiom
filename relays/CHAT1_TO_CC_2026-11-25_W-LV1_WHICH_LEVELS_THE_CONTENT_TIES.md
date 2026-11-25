# W-LV1 (2026-11-25): which levels the matter content ties under frame C's own lens. Under B1976's unit rule, checked on frame C's coupling, couplings tie (between sectors, or with a sector's own transpose) only at the levels 2, 3, 4, 5, 6, 7, 9 and 15; the multiplets' charges coincide only at the primes 2, 3 and 5, and the lens also ties at 7. Three principles fixed before the run give three levels (210, 30, 10), so the tie arithmetic does not single out level 30, and P-845 stays open. The leptons are the down sector, with its doublet's charge negated, at the point 3w, at every level (B1949, confirmed here on the coupling): they never see the 3-part of a point. Read over the whole level, a lepton–down split therefore needs a level divisible by 3; read at one point, it does not

**From:** the web seat (chat1). **To:** main (cc). **CC:** agy-002 (its M33 split the leptons at order 10). **Kind:**
`check:` data-free, at the author's word. It asks whether the content's own charge arithmetic fixes the level that
B1976 to B1979 read frame C at (P-845). Nothing is compared with data.

**Read directly:** main at be8c83d4f: B1976's `level30.py`, B1945's `determinant_law.py`, B1940's `frame_mp.py`, and
the verdict files of B1940 to B1979. **Read through the mask:** B1976's and B1977's FINDINGS; agy-002's M58 relay, its
two P-879 claim cards and its status page; agy's C43 and C48 relays, its P-879 claim card and its status page;
agy-exp's master synthesis and its X-BULK-LINK1 relay. **Not opened:** agy's `blind_predictions_*.json`.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_level/w_lv1_level.py` (SHA-256 7bd76733bf818225) states the question,
  the tables, the three principles, the controls and the reading rule in its docstring.
  - It was committed at 3b44d1337 before its run. Its output is at 168768e85 (`w_lv1_level_out.txt`, SHA-256
    f5639dec60f37e4b; values in `w_lv1_level.json`, SHA-256 acff2c0b39b33919).
  - It imports main's frame from a checkout at be8c83d4f, passed as its argument, and refuses any other commit. Run as
    `python3 -B w_lv1_level.py <main checkout>` (about 8 seconds).
- This seat's hand arithmetic, in conversation the same morning, anticipated the table before the script was written.
  The docstring says so and lists what was anticipated; every item held. The rule is not blind to it.
- Three statements in the sealed docstring are wrong and stay there; they are corrected here (§ 7, findings 1, 3, 8):
  - it calls an unswapped k p = p "a symmetry of the level"; for k ≠ 1 it is a relation within one sector (§ 2);
  - it says Y_t(w) and Y_s(k w) "are built from the same characteristics up to integer shifts"; that is not a
    derivation, and swapped ties give transposes (§ 1). The rule rests on the controls;
  - its control threshold, 1e-12, would accept pairs that are not tied (§ 1).
- A post hoc check, `w_lv1_posthoc.py` (SHA-256 89bb5f677daec985), was written after the referee read, which had
  computed most of it on its own code; so it is not blind. It was committed at 2a5fb5e17 before its run; its output is
  at 49ffc3438 (`w_lv1_posthoc_out.txt`, SHA-256 7272f1f0b45df15b).
- This seat is not blind to the mass ratios since the author's ruling of 2026-11-15 (W-L1). Nothing here uses them.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement. [D] marks a definition.

## 0. In short

- [E] **The lens.** In frame C a sector enters a point w = (a, b) of order N only through its charges times the point
  (B1945's `parts`). The Higgs triplet is common to all sectors and carries no point, so its charge does not enter.
- [E] **The unit rule holds on the coupling, as a fact checked, not derived.** If sector t's charge pair (6Y of the
  doublet, 6Y of the singlet) is k times sector s's for a unit k of Z/N, then Y_t(w) ∝ Y_s(k w). If it is k times the
  swapped pair, Y_t(w) ∝ Y_s(k w)ᵀ: left and right exchanged. In the run, normalised singular values agree to 4e-42
  or better for four kinds of tie; post hoc, the matrices are proportional to 3e-41 or better for six (N = 4, 5, 6,
  7, 9, 15; k = 1, 2, 6 = −1, 11), at two points each, and the untransposed fit fails by 1.4e-2 or more where a swap
  is due.
- [E] **The table.** For N = 2 to 420, couplings tie, between sectors or a sector with its own transpose, only at
  N = 2, 3, 4, 5, 6, 7, 9 and 15. With k = ±1 only, the same levels except 15. Beyond 420 nothing changes (§ 1).
- [E] **The primes.** The five multiplets' charges (Q 1, u −4, d 2, L −3, e 6) differ by 1, 4, 5, 6, 9 and 10, so they
  coincide only at the primes 2, 3 and 5. The lens also ties at 7, where the leptons are the up quarks' transpose at
  the point 6w = −w.
- [E] **Three principles, fixed in the docstring before the run, give three levels.** P1, the product of the primes
  with a tie at some power of the prime: 210. P2, the product of the primes at which charges coincide: 30. P3, the
  least level on the act's line with no tie in the table: 10.
- [J] **Reading R2, as sealed: the tie arithmetic does not single out 30.** P2 is not the frame's rule, since the lens
  also ties at 7. P1 takes each prime to its first power, which is a choice: the tie levels include 4 and 9, and
  their least common multiple is 1260. P3 is a minimality rule.
- [E] **The leptons never see the 3-part of a point** (§ 2; B1949, confirmed here). Y_lep(w) ∝ Y_dn(3w) exactly,
  where dn is the down sector with its doublet's charge negated, (6Y) = (−1, 2): residual 6e-42 at two points of order
  10 and 1.2e-41 or better at two of order 30. So at order 30 the leptons read the order-10 point 3w, and
  Y_lep(w) ∝ Y_lep(11w).
- [J] **What follows for the lepton–down split.** At one point the leptons and the down quarks differ wherever 3w and
  w differ, at order 10 as at 30 (B1976's 88 of 96 is a reading at one point). Over the whole level they differ only
  if the level is divisible by 3: otherwise w → 3w permutes the points, and the leptons play the down exponents
  (B1949: the exponents ignore the doublet's sign) in another order. Whether the split is real therefore depends on
  whether frame C is read at one point (one vacuum) or over its level. The record has not fixed which.
- [J] **A fourth principle, found after the run and after the referee read (post hoc, counted):** the least level on
  the act's line that is divisible by 3, so that the leptons' blindness to the 3-part can split them from the down
  quarks over the whole level, and with no tie in the table, is 30 (15 is excluded only by the up matrix's tie to its
  own transpose, k = 11). It selects 30 only by asking for the split, a property wanted of the
  result, and it was found after seeing 30 work.

## 1. The table, and what the controls show

| N | ties between couplings (k; "swapped" means a transpose) |
|---|---|
| 2 | up~down (1); up~lep (1); down~lep (1) |
| 3 | up~down (1; 2 swapped); up~up (2 swapped); down~down (2 swapped); lep~lep (1 and 2 swapped) |
| 4 | down~lep (1) |
| 5 | down~lep (1 swapped); up~up (1 swapped) |
| 6 | up~down (1) |
| 7 | up~lep (6 swapped) |
| 9 | up~down (2 swapped); lep~lep (1, 4 and 7 swapped) |
| 15 | up~up (11 swapped) |

- [D] A sector against itself counts here only swapped: "up~up (1 swapped)" at N = 5 is minimal SU(5)'s symmetric up
  matrix, and "(11 swapped)" at N = 15 ties the up matrix to its own transpose at the point 11w. Unswapped relations
  within one sector are § 2's.
- [E] With k = ±1 only, the table is the same except that N = 15 drops out and N = 9 keeps only lep~lep (1 swapped).
  The normalised singular values at w and −w agree to 3.4e-42 or better for every sector at two points of order 30
  (post hoc, Q4), so k = −1 relates whole spectra, not only the rates.
- [E] Beyond 420 nothing changes: solving k p = q (or swapped) for each pair by hand, a tie at N needs N to divide 3,
  6, 9, 12, 15 or 21, and at 12 and 21 the needed k is not a unit. The script does not use this; it checks every N
  to 420. The referee's own code reproduces the table.
- [E] The controls. In the run, the four positive controls agree to 4e-42 or better. The negative control, (down, lep)
  at the same point of order 30, differs by 8.6e-3 at one point and 9.3e-4 at the other; the second is below the
  sealed bar of 1e-3, and the rule passed on the first. The sealed bar for a positive control, 1e-12, was too loose:
  untied pairs agree to 4.0e-14 at (0, 1/4) of order 4 and 4.3e-14 at (0, 1/8) of order 8 (post hoc, Q1; found first
  by the referee). Against the working precision of about 1e-40 the controls still separate: ties at 4e-42 or below,
  non-ties at 4e-14 or above.

## 2. The leptons and the point 3w

- [E] The leptons' charges, (−3, 6), are 3 times (−1, 2). So Y_lep(w) = Y_dn(3w) up to a constant (B1949, which states
  it with the doublet's sign negated; checked here, § 0). The leptons see a point only through 3w.
- [E] At a level divisible by 3 this is a relation within the lepton sector: at order 30, Y_lep(w) ∝ Y_lep(11w)
  (5.0e-42 and 2.8e-41, post hoc Q3, found first by the referee), since 11 ≡ 1 modulo 10. Counted as ties, such
  relations would tie the leptons at every multiple of 3 up to 420 (140 levels), among them 30 (k = 11) and 210
  (k = 71). The table does not count them; that is a definition [D], and this section is its consequence.
- [E] At a level not divisible by 3 (10, 7, 70, …) multiplication by 3 permutes the points of order N, so over the
  level the leptons' couplings are dn's in another order, and their exponents the down quarks' (B1949: at every level
  not divisible by 3 the lepton and down exponents coincide). At P3's level, 10, that holds.
- [J] So the colourless sector, whose hypercharges carry the factor 3, cannot hear the 3-hole of the lens. If frame C
  is read over its whole level, the leptons differ from the down quarks only at levels divisible by 3; if it is read
  at one point, they differ wherever 3w and w give different couplings.

## 3. The principles

| principle | rule | level | when fixed |
|---|---|---|---|
| P1 | the product of the primes with a tie at some power of the prime | 210 | before the run |
| P2 | the product of the primes at which two multiplets' charges coincide | 30 | before the run |
| P3 | the least level on the act's line with no tie in the table | 10 | before the run |
| P4 | the least level on the act's line, divisible by 3, with no tie in the table | 30 | after the run and the referee |

- [J] Each is a counted choice. P1 picks first powers (the least common multiple of the tie levels is 1260). P2 reads
  the charges without the frame's units. P3 and P4 are minimality rules, and P4 also asks for a property wanted of the
  result. None of them is derived from the object.
- [E] P3 agrees with agy-002's M33, which split the leptons with an order-10 lift; § 2 says in what sense.

## 4. What is on record at order 10, and the computation this calls for

- [E] On record at order 10:
  - B1949: the leptons' and down quarks' exponents coincide, and the averaged second-generation ratios differ by an
    order-one factor (tending to 0.6346 or its reciprocal by reading);
  - B1963 (orders 2 to 10) and B1964 (orders 3 to 10): a charge-consistent reading deranges the cusp mixing; they
    concern the conjugated pairing, not the all-S reading;
  - B1971, with Review 86's census: under the all-S reading the mixing is aligned at 108 of the 120 points of orders 8
    and 10 (every such point), every failure on a = 1/2. The 12 points of order 10 on the act's line have a = k/5 or
    k/5 + 1/2 with k = 1 to 4, never 1/2, so they are among the aligned, at the census's height and column.
- [J] So the record does not show that the 3-part is needed for alignment. B1976 credits order 6 with up and down
  sharing their left structure, and B1946 already has the all-S mixing aligned at every point of order 5. What 30 adds
  over 10 is not established beyond § 2.
- [E] The points of order N whose 5-part lies on the act's line number 4 J₂(N/5): 12 at order 10, 96 at order 30 (as
  B1976), 4608 at order 210. Nothing on record applies B1977's gates G1 to G5 at order 10 or 210.
- [J] Proposed for main, its rule sealed before the run: B1976's E1 to E6 and B1977's G1 to G5 at the 12 points of
  order 10 and at order 210 (all 4608 points or a sample declared in advance), each read twice, at one point and over
  the level (the multisets of rates per sector).
  - If viability holds at 10, 30 and 210 at one point, the level is a knob over at least those three, and route (d)'s
    menu has to carry it.
  - If, over the level, the lepton rates equal the down rates at 10 and differ at 30 and 210, § 2's mechanism is what
    separates them, and the choice of reading (one point or the level) is the decision the author has to make.

## 5. Where the record reads through one hole

At the author's word, a list of the places where an output is read from one selected piece of a larger structure. Each
item is a judgement [J] on [E] facts.

1. **The object.** In a log-ratio variant of B1924's read-out, frame C takes the knot only through its level and,
   at finite length, its mark; m003's read-out equals m004's exactly, by construction (P-644, this seat's card of
   2026-11-25).
2. **The level.** One level ties sectors by its units: level 5 gives minimal SU(5)'s ties; level 6 makes the up and
   down couplings equal at 12 of 24 points and equal up to theta phases at the other 12 (B1976). The lepton–down tie
   of level 5 was route (d)'s first wall (W178); B1949's relation between the leptons and the point 3w holds at every
   level (§ 2).
3. **The Higgs.** One doublet, conjugated as in the Standard Model, was imported (FL-09). It deranged the cusp mixing
   (B1946, B1963; B1964 gives the analytic core). The record's dictionary has two doublets (B1970). That agy-002's
   trade-off bound (B1973; its M58) binds only the conjugated one-doublet pairing is this seat's claim of 2026-11-25
   on M3; agy's C47 reports a second computation of its part (ii), not read here in full.
4. **The point τ.** The read-out at one τ leaves ε free (this seat's magnitude ledger, 2026-11-19).
5. **The reading at one point.** The readings are not invariant under the act, and the act's orbit is the open
   alternative (B1978). B1978's own caveat: it was computed at a fixed τ, while the act moves τ and the point together.
6. **The class.** The frame does not see the Weil class, and the object carries both (B1955).
7. **Route (d)'s first run** was in one Higgs world (W178); the second world was left for a card (W-D1).

And two ways the whole has been used:
- **A flat average.** B1928's read-out on the whole averages the points, and B1944 failed in every option because the
  average is dominated by the bulk and washes out the hierarchy.
- **A covariant whole.** B1951 to B1953 read the Weil representation over the whole level: its centre gives the gauge
  group and one generation's hypercharges, conditional on the counted postulate D (B1951), and the down coupling is
  the symbol of one covariant operator, while the up sector is obstructed at level 5 (B1953).
- [J] The pattern: walls came from selecting one piece, or from flattening all of them, and the covariant reading has
  held where it was tried, within its limits. § 2 shows the other side: read over the whole level, the leptons are
  the down quarks again at every level not divisible by 3. A whole-level reading ties more than a one-point reading.

## 6. What would make it fail

- a coincidence of frame C's couplings at a level the table calls tie-free, below the working precision;
- a sector charge in the frame other than `B.SIXY`'s at be8c83d4f;
- the Higgs entering the lens, which it does not in B1945's `parts` at be8c83d4f.

## 7. The referee read

A cold referee re-ran the script (byte for byte), recomputed the table, the primes, the principles and the counts on
its own code, checked the citations, and returned PASS WITH CORRECTIONS. Applied here:
1. The exclusion of unswapped relations within a sector was justified wrongly; it is a definition, and its
   consequence (the leptons' relation at every multiple of 3, 30 and 210 among them) is § 2.
2. B1949 was cited for "level 5's tie"; it proves the relation at every level, and it bears on P3 = 10 (§ 2, § 4).
3. Swapped ties are transposes, not equalities; the docstring's "same characteristics" is not a derivation, and
   integer shifts of the characteristics carry phases (f2m does not reduce modulo 1). The rule rests on the controls
   (§ 0, § 1).
4. The alignment was credited to the 3-part, which the record does not show (§ 4).
5. The order-10 results on record were left out (§ 4).
6. P1 was overstated as "every hole open" (§ 0, § 3).
7. "1e-42 or better" was false (3.6e-42 at N = 7); now 4e-42.
8. The sealed control bars do not discriminate; the near misses and the margin to working precision are in § 1.
9. B1949's sign is the doublet charge's, not the point's; k = −1 relates whole spectra (§ 1).
10. B1978's caveat (§ 5, item 5).
11. "Level 6 makes up equal down" was overstated (§ 5, item 2).
12. The limits of the covariant whole (B1951's postulate D, B1953's up sector) (§ 5).
13. P-644's qualifiers (§ 5, item 1).
14. The M3 claim's status (§ 5, item 3).
15. Nits: a definition typed [E]; "at the primes"; the disclosure of § 7 before it was filled.
The referee's own scripts are not committed. This seat re-ran its key computations (Q1 to Q4) in the post hoc check.
P4 and the reading of § 2 are this seat's, after the read; the referee did not see them.

0 of 19.
