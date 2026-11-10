# B1875 — A single state is not kept when histories are composed: the web seat's sealed card verified on main

*Main, 2026-11-11 (S306p). The web seat pushed a sealed card with a post hoc amendment (`8718d4677`): in the record's
own instrument for "the state", is the property "the lightest state sits in one place" kept when two histories are
done one after the other? The relay was read in full. None of the seat's code was run. Main computed with its own
code, deciding every tie in integers. Data-free: no value of τ is read, there is no coupling and no frame output, and
nothing is compared with a measurement. 0 of 19.*

## 1. The answer first

- **The seat's card holds in every cell.** So do its post hoc amendment and the further facts its referee reported.
  Main's numbers agree with the seat's to every digit given.
- **What it says.** Two histories that each have a single state can compose to a history that does not. Of the 36
  composites tested, 18 are single and 18 are not.
- **The rule over the family tested.** A composite of two histories with the same departure is never single. A
  composite of two with different departures always is.
- **Why.** In each of the 18, a symmetry of the composite's own cyclic word exchanges the two departures. What sits
  at one then sits equally at the other.
- **So "single" is a property of one history's own cycle of heights.** It is a thread's property. It cannot be a rule
  about which histories are allowed, because what is allowed has to be kept under composition (B1872).
- **What this decides, and what it leaves.** Under the joint action, the condition the advisor seat's design of the
  first back-edge calls (A-adm) is not an admission rule. Whether "single" is kept as a labelled selection on one
  thread, or replaced by a read-out on the whole, is not decided here. A read-out on the whole needs a state of the
  whole, and the record holds none.
- **The instrument is a thread instrument on a clock the record counts as chosen** (B1857, B1815). Nothing is
  computed on the hyperbolic metric.

## 2. The instrument, and why a tie is exact

A history is a closed word, written by its runs: the lengths of its blocks of one letter. The height of a run is how
far the history's axis rises above that run's own class. In B1857's model the lightest state sits at the greatest
height, the apex. The history is **single** when one run attains the apex.

- **The height of run i is √(tr² − 4) / (2 cᵢ),** with cᵢ an entry of the word's integer matrix started at that run.
  So two heights are equal exactly when two integers are equal. No tolerance decides anything here.
- **Control 1.** That formula agrees with the continued-fraction form of B1857 to 60 digits, on the six histories and
  all 36 composites.
- **Control 2.** B1857's four apexes come out as the record has them: 3.618034 once, 1.723607 once, 1.625437 twice,
  1.617974 twice.
- **Control 3, main's.** The seat argues that one height per run is enough. Main checked it by brute force over every
  primitive class above height ½, on eight histories: each run's own class is there once per period, and every other
  class is below 1 (the greatest found is 0.597). Every apex is at least √5/2.

## 3. The card, cell by cell

The six histories are the run of 6 and (2,1,2,1,2), each closed by 1, 2 or 3 golden periods. Both are the record's
departures with a unique apex.

| cell | the seat's rule, as sealed | main |
|---|---|---|
| C0 | the instrument reproduces B1857's four apexes | **holds** (control 2) |
| C1 | each of the six has a unique apex and keeps the line modulo 5 | **holds**: the lead is 2.28 to 2.37 for (6) and 0.042 to 0.049 for (2,1,2,1,2) |
| C2 | all 18 composites with the same departure have the apex exactly twice | **holds**, as an equality of integers in all 18: heights 3.6187 to 3.6515, and 1.7236 to 1.7248 |
| C3 | all 18 with different departures have a unique apex, at the run of 6, more than 1 above the next | **holds**: the lead is 1.89 to 1.91 |
| C4 | each of the 18 of C2 has a symmetry of its cyclic word that exchanges the two departures and keeps the line | **holds**, with the symmetry built as an integer matrix (§ 4) |
| C5 | the four generators of the allowed subweave each have a unique apex | **holds** |

**Why every word of the family keeps the line:** modulo 5, (L²R)³ = 1 and L⁵ = 1, so each is a power of LR.

## 4. The symmetry behind each tie

For each of the 18, main built the symmetry as a matrix g with whole-number entries and checked the relation it
satisfies exactly.

| | how many | the symmetry | det g | the relation | the line |
|---|---|---|---|---|---|
| a history done twice | 6 | the rotation by half the word (the deck move of the double cover) | +1 | g W g⁻¹ = W | kept |
| two copies of one departure with different golden gaps | 12 | one reversal, and no other symmetry | −1 | g W⁻¹ g⁻¹ = W | kept |

- **Every symmetry that exchanges the two departures keeps the line** (g v = ±v modulo 5), in all 18.
- **A square has two reversals as well.** One exchanges the two departures and one fixes each. The seat's relay
  names only the rotation for the squares; this is an addition and changes nothing.
- **No symmetry of the family exchanges the letters.**
- 4 of the 12 words are −1 modulo 5, and 10 of the 36 composites, as the seat says.
- **SnapPy, on the bundles themselves.** Each of the 18 has twice as many isometries as its word has symmetries: 8
  for the squares, 4 for the others. None is its own mirror image. That is the law of B1867 § 2, here on words of up
  to 30 letters.
- **A control on the other 18.** The same law holds: 12 have 2 isometries and 6 have 4. Those 6 are the composites
  whose two golden gaps are equal. Their one reversal fixes the apex, so they stay single.

## 5. Three factors (post hoc at the seat)

| factors with the departure (6) | triples | single | apex twice | apex three times |
|---|---|---|---|---|
| one | 81 | 81 | 0 | 0 |
| two | 81 | 54 | 27 | 0 |
| three | 27 | 15 | 9 | 3 |
| none | 27 | 15 | 9 | 3 |
| **all** | **216** | **165** | **45** | **6** |

- **A third factor can make a composite single again.** (6)₁(6)₂ is not single. Followed by (2,1,2,1,2)₁ or
  (2,1,2,1,2)₃ it is. Followed by (2,1,2,1,2)₂ it is not.
- **The margins are thin.** Where two or three runs of 6 compete, a single triple's apex leads by 0.00098 to 0.016.
  With no run of 6 it leads by 7.5·10⁻⁵ to 5.9·10⁻⁴.
- **Over the 258 words** (6 + 36 + 216) the runs at the apex are exactly one orbit of the symmetries of the cyclic
  word. Of the 165 single triples 120 have no symmetry and 45 have one reversal, which fixes the apex.

## 6. Beyond the family (the referee's reports, recomputed)

| | main |
|---|---|
| ties with no symmetry behind them exist | runs (1,3,1,3,4,3): a run of 3 and a run of 4 tie (c = 72 for both), and the word's one reversal fixes each. Runs (2,2,1,3,3,1,1,3): two runs of 3 tie (c = 196), the word has no symmetry, and it keeps the line |
| how common | 16 of the 15 641 cyclic run sequences to 18 letters |
| in the family's four-factor words | none of 1 296 |
| two non-single composites can compose to a single one | 180 of 324 are single; (6)₁(6)₁(6)₃(6)₃ leads by 0.016 |
| a departure that is not a palindrome | two copies of (2,1,3) with different gaps are single, by 0.0009 to 0.007 |
| (2,1,1,1,2) closed by one golden period | it is LLRLR twice over and is −1 modulo 5. The deck move moves the line. The reversal that exchanges the two runs of 2 keeps it; the reversal that fixes each run moves it |
| (2,1⁸,2) closed by an even number of golden runs | its two runs of 2 are L² and R². One symmetry: a reversal that exchanges the letters, det g = +1. It carries the line to its twin |

**So the "exactly when" of § 5 is a statement about the 258 words.** The direction that always holds is: a symmetry
that moves a deepest run forces a tie.

## 7. What it means for the programme

- **The closed loop (P-761; the rulings R9 and R10 confirmed to main, P-767).** The first back-edge's design asked
  that a history be allowed only if its state is single. That condition is not kept under composition, so it does not
  define a set of allowed histories. This is the test the advisor seat itself put before any run of that design.
- **The single histories do not form a smaller weave.** The four generators of the allowed subweave are single (C5).
  With inverses they generate all of it (B1872: index 12). So as a condition on the subweave "single" removes
  nothing; as a condition on histories it is not kept. LR itself keeps the line and is not single.
- **What is left is the fork the seat states, and it is the owner's.**
  - A selection on one thread, labelled as that. The owner's ruling confirmed to main (R10) puts the claim on all
    allowed histories together, and the design already labels its one-history form a thread result.
  - A read-out on the whole. It needs a state of the whole: an operator, a clock and a statement of what its
    symmetries force, written before anything is computed. None is on record (B1872 § 3).
- **The weave's own rule already treats a tie differently.** THE_WEAVE keeps the whole set of minima. A tie is kept
  as a set there. It does not make a history disallowed.
- **The word's symmetries (P-766).** Over this family they decide a second thing besides the bundle's isometries:
  how many places the apex has. The two ties of § 6 show they do not decide it in general.
- **The record's two "mirror" departures (B1857, P-742)** are now described exactly (§ 6, last two rows).

## 8. What is not shown

- **Nothing on the hyperbolic metric.** The seat's § 5 argues what the same symmetries give there, given that a
  lowest state exists. Main checked only that the symmetries are isometries of the bundles. Where a state sits on
  that metric is open (P-744).
- **The family is small:** two departures, both palindromes, one to three golden periods, two to four factors.
- **The area of the fibre is unearned** (P-743). The criterion is exact at every area; the state's reading at the
  apex is exact only in the limit of small area.
- **The owner's choice "Test closure first" was made with the seat.** Main records it as relayed (P-768) and acts on
  no ruling here. Verifying a seat's data-free result is main's standing task.

## Seen first

- **The repo sweep:** the seat's seven sweeps were read with its relay. The record holds the instrument and the four
  apexes (B1857), the law of a bundle's symmetries (B1867 § 2), the definition of "together" and the allowed subweave
  (B1872), and the line's census (B1733). It holds no statement on whether a composite of single histories is single.
  B1872 says so itself.
- **The literature:** that a symmetry of the word is an isometry of the bundle is rigidity (Mostow, Prasad); main
  tested it with SnapPy and proves nothing.

## Disclosed

- **Main read the seat's numbers before computing.** The method is independent; the reading was not blind.
- **Main's first brute-force control was wrong twice before it was right.** It first compared against every run's
  height with a threshold that excluded some runs, and it then counted one class twice at the edge of a period because
  the edge was decided in floating point. The edge is now decided in integers. Both slips were in the control, not in
  the result.
- **Main's first check of C4 assumed one symmetry per word.** The squares have three. The check now asks what the
  cell asks: that a symmetry exchanging the departures exists and keeps the line.
- **The seat discloses a flaw in its own control C0** (one control closed with an odd number of golden runs). Main's
  control 2 uses an even number for that departure and gets the record's value.

## Reproduce

```
python3 -B frontier/B1875_a_single_state_is_not_closed_under_composition_verified/verification/closure_on_main.py
python3 -m pytest -q frontier/B1875_a_single_state_is_not_closed_under_composition_verified/verification/
```
