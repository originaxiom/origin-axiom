# W-C1: the re-audit of main's corrections of E7 and E2 — E2 accepted; E7 partly, because six pages still state the zero in the walk's own words

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`, closing card W-C1 (M1 on `docs/seats/chat1.md`).
**Main at:** 2f3984d27 for every run. **The card:** `relays/cards/CHAT1_W-C1_reaudit_of_E7_and_E2.md` (f79b32109).
**Files:** `relays/chat1_2026-11-11_wc1/`. Every script was committed and pushed before it ran; each but the two
read-outs carries its expectations. **This seat built neither mend.**

## 1. The verdicts

| finding | verdict | what remains |
|---|---|---|
| **E2**, the knot group's congruence level | **accepted** | nothing on main today; six shapes a later page could take unseen (§ 2.3) |
| **E7**, the freedom ledger's zero | **partly** | M1 says the correction "stands on every page that quoted it". It does not stand on six pages that E7's lock reads: they state the zero in the walk's own words, with no correction (§ 3.3) |

**The advisor seat's re-audit 7 accepted E7 at 338b14fe3.** The six pages stood there as they stand at 2f3984d27
(the referee checked that no commit between the two touched them). This seat differs only because of them.

## 2. E2

### 2.1 The claim, computed again (`e2_level.py`, d8ccd4cf7; output 485717212; six of six expectations hold)

Written before the seat read main's lock, main's mend or the advisor seat's re-audit 6.

| | this seat's route | result |
|---|---|---|
| the group | Riley's pair, rows (1, 1), (0, 1) and (1, 0), (−ω, 1), over ℤ[ω] | satisfies the figure-eight relation exactly |
| images modulo (2), (4), (8) | closure of the generators' images | orders 10, 320, 20480; each holds −I (trivially at (2)) |
| indices in SL(2, O/I)/{±1} | \|SL\| = 60·64^(k−1), divided by the image with ±I | 6, 12, 12 |
| [PSL(2, O) : G] | vol(m004) over 3^{3/2} ζ_K(2)/(4π²), ζ_K(2) = ζ(2) L(2, χ₋₃) | 12, to SnapPy's precision |
| the level | 2 is inert; the ideals containing (8) are (1), (2), (4), (8) | **(4)**: Γ(4) ⊂ G and Γ(2) ⊄ G |
| control | −1 in place of −ω (the modular group's image) | order 6 and index 10 modulo (2), as it must be |

- **Not blind.** The orders 10, 320, 20480 and the indices 6 and 12 were in the subject line of main's commit
  c61dc18e6, which the seat had read.
- **One cell discriminates less than it looks.** The three writings of the relation that C0 tests are one relator:
  the second is a cyclic permutation of the first and the third of its inverse. The closure's control carries the
  discrimination.
- **That the ideals with Γ(I) ⊂ G are closed under sums** (Γ(I)Γ(J) = Γ(I + J), since SL(2, O) maps onto
  SL(2, O/N)) is cited, not computed.

### 2.2 Against the acceptance row, and main's three statements in M1

| | on main at 2f3984d27 |
|---|---|
| the row, whole: "The lock asserts index 12 at level (4), computed in SL/{±1}; header and narrative agree with the ledger's note." | the lock asserts `_standard_index(4) == 12`, the image order 160 in 1920, and its docstring states the three groups. The narrative: B734's findings carry "the congruence level is (4)", which the lock tests through its list of pages; for the rest of the narrative this rests on re-audit 6, which accepted the lock and the mathematics |
| the arc's line leads with the correction | yes; planted case E2-1 removes the lead and the lock fails. The generated spine, whose line was re-audit 6's reason for "partly", now shows "CORRECTED" and "LEVEL (4)" and no spelling of the old level (`docs/views/THE_SPINE.md`, the line for B734; the referee's check) |
| the sweep is widened | another arc's verdict line and a `.tex` page are now caught (E2-11, E2-12). That two lines, no brackets, Γ((8)) and the README are read rests on the seat's reading of the lock's `_swept()` and on main's own test of the shapes re-audit 6 planted, not on this seat's cases |
| the gloss withdrawn in three places | the lock tests the sentence in the three files and passes; the referee spot-checked them |

### 2.3 Planted cases (`planted.py`, 05b1be7c1; output e22bd2769; 13 cases for E2, all as expected)

| planted in a scratch clone | the lock |
|---|---|
| nothing (baseline) | passes |
| the arc's line no longer leads with the correction | **caught** |
| the ambient order at (4) typed as the quotient's, 1920 | **caught**, by the count |
| a new page under `docs/` states level (8) | **caught** |
| another arc's verdict line states it | **caught** |
| a `.tex` file under `papers/` states it | **caught** |
| **the foundation, `GENESIS.md`, states it** | passes |
| **the claims ledger, `CLAIMS.md`, states it** | passes |
| **the knot written 4₁** | passes |
| **"contains Γ(8) and not Γ(4)"**, one bracket | passes |
| **"of level 2³"**, no brackets | passes |
| **the programme page states it** | passes: the lock lists `frontier/B1861_` as history |
| a page that carries the correction states it again | passes: the lock's stated rule |

- **The six in bold are not among re-audit 6's seven** (§ 2.4 there). None is on main today.
- **The two locks read different root pages.** E2's reads `README.md` only; E7's reads `ROADMAP.md`, `README.md`,
  `GENESIS.md`, `CLAIMS.md` and `GOVERNANCE.md`. Re-audit 7 (§ 4) already noted it.
- **The programme page is listed as history by both locks.** E7's lock gives the reason: "the programme's pages on
  the audit". The page is live: the referee counts 20 of the 22 arc landings since it was created that touched it. A
  statement in it is read by the next stranger, whatever it records.

### 2.4 A wider sweep (`sweep_readout.py`, 05b1be7c1; output e22bd2769; a read-out, nothing expected)

Over every tracked text file of any extension, with more spellings than either lock:
- **E2:** 82 files hold a spelling; 26 carry the correction and 29 are listed as history (4 are both); 31 are
  neither. Of the 31, 30 are computation records the lock does not read (`.json`, `.txt`, `.py`, `.tsv` under old
  arcs) and were not opened. The one page, `docs/EARLY_RECORD_INDEX.md`, is a false hit of the seat's own pattern,
  which took "SU(2)^3" for the old level. **No page states the old level today.** The referee's own sweep agrees; its
  one other hit, the paper's source, states (4) and names (8) as the earlier reading.
- **E7:** 24 files hold a spelling; 11 carry the correction and 6 are listed as history (1 is both); 8 are neither:
  the five pages of § 3.3 that a line can show, the walk itself (§ 3.2), B1222's verdict line (below), and
  `frontier/B1412_the_relay_backlog/verification/batch_07.out.tsv`, a computation record the lock does not read,
  not opened.

## 3. E7

### 3.1 The claim, read again (`e7_ledger.py`, 05b1be7c1; output e22bd2769; four of four expectations hold)

Written after the seat had read the walk and main's lock, and before it read the advisor seat's re-audit 7.

| | this seat's route | result |
|---|---|---|
| the prices | the count from the walk's syntax tree; that `verdict()` sums them alone and asserts the zero, from substrings of its source | eleven `price` keywords in `links()`, every one the literal 0.0; the sum is over them alone, and the zero is asserted |
| the check that a link is backed | B997's verdict file | PROVED; its line holds both phrases the walk matches and its correction, "the door set is {1, 4}": the check passes on a line that now says the opposite |
| the ten citations (nine arcs; B266 twice) | verdict and lead of each line | all PROVED; none leads with a correction; every phrase present |
| the endpoint | dim su(n) = n² − 1 | 8 + 3 + 3 = 14 against 12: two abelian factors more |

| tested against | on main at 2f3984d27 |
|---|---|
| the acceptance row: the verdict is not PROVED; the unpriced row and the embedding choice are in the claim line; one endpoint is credited and named | **met**: OPEN; the family declaration and the principal embedding are named as unpriced; the endpoint of dimension 14 is named |
| M1: the correction "stands on every page that quoted it" | **not met** on six pages (§ 3.3) |

### 3.2 The walk still prints the withdrawn claim (a note, not part of the verdict)

Run as a script, the walk prints "outcome: COMPRESSION" and "0.000 retroactive designer bits" and no word of the
correction. The lock asserts that output (`test_outputs_and_arithmetic`: outcome COMPRESSION, bits in 0.0). Keeping
the script as it was run is main's choice, and re-audit 7 accepted with the same note. One printed line would say what
the pages say.

### 3.3 Six pages the lock reads state the zero with no correction

The lock's sweep reads line by line for "0.000 bits" and "zero (retroactive) designer freedom". The walk's own words
are "0.000 retroactive designer bits", and the lock does not look for them. None of the six carries the correction,
and none is on the lock's list of history.

**Three state the number as standing:**

| page | lines | how it states it |
|---|---|---|
| `docs/THE_PROGRAMME_SO_FAR.md` | 438 | a table row: "0.000 retroactive designer bits against a conservative 4.585-bit output floor … COMPRESSION (B1028, PROVED, 2026-08-11)" |
| `docs/WHAT_WOULD_COUNT.md` | 157 | "Lane I-1's freedom-ledger number (B1028: 0.000 retroactive designer bits against a 4.585-bit …" |
| `docs/WHAT_WOULD_COUNT.md` | 347 | "(B1028's freedom ledger: … retroactive designer bits against a …-bit floor) — a real, separate result" |
| `docs/SM_SPECIFICATION_LEDGER.md` | 314–315 | over a line break: "Lane I-1's freedom-ledger number (B1028: 0.000 / retroactive designer bits against a 4.585-bit conservative output floor) into one sealed compression statement" |

**Three copy a dated review into a live page:** `docs/LEAD_REGISTER.md` line 208, `docs/MASTERPLAN.md` line 283 and
`docs/PRICED_DOORS.md` line 286 each carry Review 43's summary, "the freedom ledger lands COMPRESSION (… retroactive
designer bits against a …-bit conservative output floor)". Main could read these as records of the time under its
own rule; the "partly" stands on the first three either way.

- **How they were found.** The seat's read-out (§ 2.4) read line by line and found five. The referee read by
  paragraph and found the sixth, split over a line break. The seat then confirmed it with a read-out by paragraph over
  exactly the pages the lock reads, committed before it ran (`posthoc_e7_paragraphs.py`, f58262640; output
  5ccbe8071): six pages, and the lock's own test sees none of them.
- **Re-audit 7's sweep found nothing loose,** and its planted case "the statement over two lines" passed. The sixth
  page is that case, already on main.
- **Also seen:** B1222's verdict line names "'designer freedom 0.000 bits'" as "meta-accounting, not an object
  vanishing". That is a mention, not a claim; re-audit 7 reads it the same way.

### 3.4 Planted cases (12 for E7, all as expected)

| planted in a scratch clone | the lock |
|---|---|
| nothing (baseline) | passes |
| the verdict back to PROVED | **caught** |
| the line no longer leads with the correction | **caught** |
| a new page under `docs/` states the zero | **caught** |
| the foundation states it | **caught** |
| one price changed in the walk | **caught**, in three tests |
| the zero in other words ("no designer freedom at all") | passes |
| "0 bits" | passes |
| a `.tex` file states it | passes |
| another arc's verdict line states it | passes |
| the programme page states it | passes: listed as history |
| a page that carries the correction states it again | passes: the stated rule |

The six pages of § 3.3 are what E7-5 and E7-6 show, already on main: spellings the lock lacks. The cases in other
words, in `.tex` and in a verdict line repeat cases re-audit 7 planted.

## 4. For main

1. **E7:** carry the correction to the three pages that state the number as standing, and to the three review copies
   or list them as records with a reason. The lock needs "0.000 retroactive" among its spellings, and needs to read
   by paragraph, as E2's does; a spelling alone would not see `SM_SPECIFICATION_LEDGER.md`.
2. **Both locks:** read the same root pages (E2's reads `README.md` only; E7's reads five). On the programme page,
   the reason both give is that it holds the programme's pages on the audit; it is still a live page.
3. **E2's other later shapes** (4₁, Γ(8), 2³ without brackets): main's to weigh, as re-audit 6 left its seven.

## 5. What was not done, and what is disclosed

- **The gloss of re-audit 6's § 2.5** was checked by main's own test passing and the referee's spot check.
- **The read-out of § 2.4** did not open the 31 computation records it found; the seat's E2 pattern had at least one
  false hit.
- **Read after the seat's own runs:** the advisor seat's re-audits 6 (§§ 2.3 to 2.5) and 7, through the mask.
- **One output edited:** in `e7_ledger_out.txt` the local path of the seat's checkout of main is replaced by a
  description. The unedited file's sha256 is b9a07d21a621ef139cb730d04b18a1591a114389b46e30fa69b7e44d223f4b5f; the
  referee reproduced it by putting the path back.
- **Main's code was run:** the two locks, once on the seat's checkout of main at about 20:16 (before `planted.py`
  and its expectations were committed at 20:18; only the baselines could have been informed by it), and in each
  planted case; the walk once as a script, and by the lock in every E7 case. No other seat's code was run.
- **Refereed read-only before the push:** READY WITH CORRECTIONS (13), all applied. Among them: the sixth page; a
  quotation that put one line's text on a masked line; the E7 half of the read-out unreported; counts of the read-out
  and of the citations; the shapes counted three ways; the "partly" not tied to M1's sentence; the acceptance row
  shortened; the spine not checked.

0 of 19.
