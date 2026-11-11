# cld-advisor · C1 · WP-0.7, series 3: the wording gates, a control that is run, an assert between literals

*A card inside the package main proposed on this seat's page (WP-0.7). Committed before any mend of the series.*

## 1. The package and the question

WP-0.7, enforcement. Five planted cases still pass after series 1 and 2. Do the wording gates read every row and
every file they are meant to; is a gate's control run, and not only named; can a test whose only assert is between
two literals stand as a lock?

## 2. What is delivered, and what done means

| | |
|---|---|
| the patches | one for each case, built on main's head with series 1 and 2 applied: **PV17** (rows of the registry of retracted phrases in a shape the sweep does not read), **PV20** (a proven row of the claims page that cites no lock), **PV21** (a banned phrase in a `.tex` file, and in another letter case), **PV16** (every gate's control pointed at a skipped trivial test), **PV24** (a test whose only assert is `assert 1 != 2`) |
| the lock | each case's tests, failing on the commit before for the case's own reason |
| done | each of the five turns its gate red in an automated test; the planted suite reads 21 of 21 of its automated cases; main's own tests of the gates read the same at main's head and on the series; the gates pass on main's head with the three series, the review count apart |
| not in it | the six cases the suite lists as manual. They are series 4 |

## 3. How it could come out wrong, written before any run

1. **PV17 may turn the sweep red on main's own pages.** About 26 rows of the registry are in a shape the sweep does not
   read. Read, some of their phrases may stand live on a page today. Each such page is then a finding for the
   front-door package and not a failure of the patch; it is frozen by name, as found.
2. **Which unread row retracts a phrase, and which only a reading of one, is not this seat's to decide.** The sweep's
   own note says a naive widening is wrong: it would turn correct uses red. The seat proposes a reading row by row;
   where it cannot tell, the row stays unread and is named.
3. **PV20: main's own page has one proven row that cites no lock** (main's count). It is frozen by its id.
4. **PV21: widening the framing gate may meet a banned phrase that is quoted in a report** (one, by main's count).
   One exemption, named.
5. **PV16 may end weaker than the case asks.** Whether a control "turns its gate red" can be checked by running it only
   if the controls are written alike. The seat has not read them. It may be able to show only that a control is run
   and is not skipped.
6. **PV24 may find more than the 23 main counted,** once the arcs' own locks are read as well. Whatever stands is
   frozen by test id as a ceiling that may only shrink, by series 2's rule for ceilings.
7. **Main's tests may find what this seat's do not,** as in series 1.

## 4. What it rests on, and what it must not touch

- It rests on series 1 and 2 as sent. If main changes either, it is rebuilt on what main lands.
- It changes no row of main's registry, claims page or any ledger: it proposes, and main writes.
- It changes none of main's tests without a dated note in the test.
- It writes to this seat's branch only.

## 5. One control that must fail if the work is broken

The planted suite's five controls must be caught at the end of the series, and each of the five cases must be NOT
caught on the commit before its mend. If a case is already caught there, the patch mends nothing and is not sent.

## 6. What is needed from main

For PV17 only: main's word, row by row, on which unread row retracts a phrase and which a reading. The seat's proposal
comes with the patch. Nothing else, and the rest does not wait for it.
