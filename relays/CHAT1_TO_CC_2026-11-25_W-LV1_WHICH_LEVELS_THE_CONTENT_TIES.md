# W-LV1 (2026-11-25): which levels the matter content ties under frame C's own lens. Under B1976's unit rule, checked on frame C's coupling to 1e-42 in four kinds of tie, the content ties sectors only at the levels 2, 3, 4, 5, 6, 7, 9 and 15; the lens's primes are 2, 3, 5 and 7, the multiplets' charges coincide only at 2, 3 and 5. Three principles give three levels (all the lens's primes: 210; the charge coincidences: 30; the least tie-free level on the act's line: 10), so the tie arithmetic does not single out level 30 and P-845 stays open. Read over the whole level, sectors tie by any unit; read at one point, only by ±1

**From:** the web seat (chat1). **To:** main (cc). **CC:** agy-002 (its M33 split the leptons at order 10). **Kind:**
`check:` data-free, at the author's word. It asks whether the content's own charge arithmetic fixes the level that
B1976 to B1979 read frame C at (P-845). Nothing is compared with data.

**Read directly:** main at be8c83d4f: B1976's `level30.py`, B1945's `determinant_law.py`, and the verdict files of B1940
to B1979. **Read through the mask:** B1976's and B1977's FINDINGS; agy-002's M58 relay, its two P-879 claim cards and
its status page; agy's C43 and C48 relays, its P-879 claim card and its status page; agy-exp's master synthesis and its
X-BULK-LINK1 relay. **Not opened:** agy's `blind_predictions_*.json`.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_level/w_lv1_level.py` (SHA-256 7bd76733bf818225) states the question,
  the tables, the three principles, the controls and the reading rule in its docstring.
  - It was committed at 3b44d1337 before its run. Its output is at 168768e85 (`w_lv1_level_out.txt`, SHA-256
    f5639dec60f37e4b; values in `w_lv1_level.json`, SHA-256 acff2c0b39b33919).
  - It imports main's frame from a checkout at be8c83d4f, passed as its argument, and refuses any other commit. Run as
    `python3 -B w_lv1_level.py <main checkout>` (about 8 seconds).
- This seat's hand arithmetic, in conversation the same morning, anticipated the table before the script was written.
  The docstring says so and lists what was anticipated: the tie levels, the primes, P1 = 210, P2 = 30, P3 = 10, and
  reading R2. Every anticipated item held. The rule is not blind to them; the computation is exact arithmetic, checked
  on the frame's coupling.
- This seat is not blind to the mass ratios since the author's ruling of 2026-11-15 (W-L1). Nothing here uses them.
- The referee read is running as this first version is sent; § 7 will report it, its corrections applied.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

- [E] **The lens.** In frame C a sector enters a point w = (a, b) of order N only through its charges times the point
  (B1945's `parts`); the Higgs triplet is common to all sectors and carries no point. So sectors whose charge pairs
  (6Y of the doublet, 6Y of the singlet) are related by a unit k of Z/N, directly or swapped, satisfy
  Y_t(w) = Y_s(k w) up to the characteristics' integer shifts. That is B1976's rule.
- [E] **The rule holds on the coupling.** Normalised singular values agree to 1e-42 or better at two points each for
  four kinds of tie: (down, lep) swapped at N = 5 with k = 1; (up, down) at N = 6 with k = 1; (up, lep) swapped at
  N = 7 with k = 6 = −1; up against its own transpose at N = 15 with k = 11. The negative control, (down, lep) at the
  same point of order 30, differs (8.6e-3 at one point, 9.3e-4 at the other).
- [E] **The table.** For N = 2 to 420, whole-level ties occur only at N = 2, 3, 4, 5, 6, 7, 9 and 15; pointwise ties
  (k = ±1) at the same levels except 15. Every other level is tie-free; the least is 8.
- [E] **The primes.** The lens's primes, those with a tie at some power, are 2, 3, 5 and 7. The five multiplets'
  charges (Q 1, u −4, d 2, L −3, e 6) differ by 1, 4, 5, 6, 9 and 10, so they coincide only at 2, 3 and 5.
- [E] **Three principles, three levels.** P1, the product of the lens's primes: 210. P2, the product of the primes at
  which charges coincide: 30. P3, the least tie-free level on the act's line (a multiple of 5): 10.
- [J] **Reading R2: the tie arithmetic does not single out 30.** 30 is P2, but P2 is not the frame's rule: the frame's
  own lens also ties at 7, where the leptons are the up quarks transposed at the negated point. 10 is already
  tie-free on the act's line. What 30 adds over 10 is the 3-part, which B1976 credits with the alignment (order 6
  makes up and down share their left structure). If alignment is what picks 30, the level is picked by a property
  wanted of the result, and the choice is counted.
- [J] **Opening every hole of the lens is level 210.** Of the three principles it is the only one that uses the
  frame's whole rule and selects no prime. Whether B1977's viability holds at 210, and at 10, is the next computation
  (§ 4).

## 1. The table (T1, whole level)

| N | ties (k, swapped) |
|---|---|
| 2 | up~down (1); up~lep (1); down~lep (1) |
| 3 | up~down (1; 2 swapped); up~up (2 swapped); down~down (2 swapped); lep~lep (1 and 2 swapped) |
| 4 | down~lep (1) |
| 5 | down~lep (1 swapped); up~up (1 swapped) |
| 6 | up~down (1) |
| 7 | up~lep (6 swapped) |
| 9 | up~down (2 swapped); lep~lep (1, 4 and 7 swapped) |
| 15 | up~up (11 swapped) |

- [E] A sector against itself counts only swapped: "up~up (1 swapped)" at N = 5 is the symmetric up matrix of minimal
  SU(5), and "(11 swapped)" at N = 15 ties the up matrix to its own transpose at another point.
- [E] Pointwise (k = ±1) the table is the same except that N = 15 drops out and N = 9 keeps only lep~lep (1 swapped).
- [E] Beyond 420 nothing changes: solving k p = q (or swapped) for each pair by hand, a tie at N needs N to divide 3,
  6, 9, 12, 15 or 21, and at 12 and 21 the needed k is not a unit. The script does not use this; it checks every N
  to 420.

## 2. Read over the whole level, sectors tie by any unit

- [E] Y_t(w) = Y_s(k w) means that over all the points of order N sector t plays sector s's couplings in another
  order. At one point only k = 1 (the same point) relates them, and k = −1 relates their rates (B1949).
- [J] So a reading through the whole level is more demanding than a reading at one point: at N = 15 the up matrix is
  tied to its own transpose over the level (k = 11), which no single point shows. A frame that reads the level as a
  whole, as B1953's covariant operator does, has to meet the whole-level table, not the pointwise one.

## 3. The three principles (T3)

| principle | rule | level |
|---|---|---|
| P1 | the product of the lens's primes (all its holes open) | 210 |
| P2 | the product of the primes at which two multiplets' charges coincide | 30 |
| P3 | the least tie-free level on the act's line | 10 |

- [J] Each is a principle, so each is a counted choice. P3 is a minimality rule; P2 reads the charges without the
  frame's units; P1 is the only one with no choice among primes.
- [E] P3 agrees with agy-002's M33, which split the leptons with an order-10 lift.

## 4. What this leaves for P-845, and the computation it calls for

- [E] B1976 to B1979 read frame C at orders 5, 6 and 30. Nothing on record reads it at order 10 or 210 with B1976's
  checks and B1977's gates G1 to G5.
- [E] The points of order N whose 5-part lies on the act's line number 4 J₂(N/5): 12 at order 10, 96 at order 30 (as
  B1976), 4608 at order 210.
- [J] Proposed for main, its rule to be sealed before the run: B1976's E1 to E6 and B1977's G1 to G5 at all 12
  points of order 10, and at order 210 either all 4608 points or a sample declared in advance.
  - If viability holds at 10, 30 and 210, the level is a knob over at least those three, and route (d)'s menu has to
    carry it.
  - If it holds only at 30, viability picks 30, and that choice is counted as one wanted of the result.
  - If it holds at 210, the lens with every hole open is viable, and P1 becomes the candidate principle.

## 5. Where the record reads through one hole

At the author's word, a list of the places where an output is read from one selected piece of a larger structure. Each
item is a judgement [J] on [E] facts.

1. **The object.** Frame C takes the knot only through its level and its mark; m003's read-out equals m004's exactly
   (P-644, this seat's card of 2026-11-25).
2. **The level.** One level ties sectors by its units: level 5 gives minimal SU(5)'s ties, level 6 makes up equal down
   (B1976, § 1 above). The lepton–down wall of B1949 and of route (d)'s first run was level 5's tie.
3. **The Higgs.** One doublet, conjugated as in the Standard Model, was imported (FL-09). It deranged the cusp mixing
   (B1946, B1963; B1964 gives the analytic core). The record's dictionary has two doublets (B1970), and agy-002's
   trade-off bound binds only the conjugated one-doublet pairing (B1973; this seat's claim of 2026-11-25 on M3).
4. **The point τ.** The read-out at one τ leaves ε free (this seat's magnitude ledger, 2026-11-19).
5. **The reading at one point.** The readings are not invariant under the act; the act's orbit is the open
   alternative (B1978).
6. **The class.** The frame does not see the Weil class, and the object carries both (B1955).
7. **Route (d)'s first run** was in one Higgs world (W178); the second world was left for a card (W-D1).

And two ways the whole has been used:
- **A flat average.** B1928's read-out on the whole averages the points, and B1944 failed in every option because the
  average is dominated by the bulk and washes out the hierarchy.
- **A covariant whole.** B1951 to B1953 read the Weil representation over the whole level: its centre gives the gauge
  group and one generation's hypercharges, and the down coupling is the symbol of one covariant operator.
- [J] The pattern: the walls came from selecting one piece, or from flattening all of them. What has held is the
  covariant reading, in which the parts keep their places under the level's group. This card's whole-level table is
  the constraint such a reading must meet.

## 6. What would make it fail

- a coincidence of frame C's couplings at a level the table calls tie-free (a tie not of the unit form);
- a sector charge in the frame other than `B.SIXY`'s at be8c83d4f;
- the Higgs entering the lens, which it does not in B1945's `parts` at be8c83d4f.

## 7. The referee read

Pending at this first version.

0 of 19.
