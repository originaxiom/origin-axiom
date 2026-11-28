# A88b: W-LV1 and B1977's second computation filed as cards, with main's frame copied in

*Web seat (fam1-v1-unset-03), 2026-11-28, for main, after M88 item 2. Data-free. This seat is not blind to the mass
ratios, by the author's ruling of 2026-11-15 (W-L1). Main's .py and .json were read directly; nothing else of main's.*

## 0. In short

Two of the four frame-dependent cards are filed, as M88 asks:
- relays/claims/CLAIM_2026-11-28_wlv1_the_levels_the_content_ties.md, at bd3ca8e9e;
- relays/claims/CLAIM_2026-11-28_b1977_second_computation_in_the_queue_form.md, at 876b11f1c.

Each card's folder copies main's frame from the stated commit (be8c83d4f and 88a1e9474, the same blobs at both).
- **What changed in the copy:** every file is verbatim but for its loaders, each replaced line marked and listed in
  the folder's MANIFEST.md with main's text. A build script in the folder makes the copy and checks each replaced line
  against main's text first.
- **The copy's test:**
  - Each card script reproduces its old sealed output byte for byte: W-LV1's of 2026-11-25 and CHK-1's addendum of
    2026-11-24.
  - Main's sandboxed rerun, run here, gives REPRODUCED on both: 8 and 10 seconds, each control exiting 1.
  - Main's form check holds on both. Main's record check gives deciding true, no wait and no firewall word.
- **Three replaced lines are not loaders,** each off the run's path, and the cards and manifests say so:
  - covariance.py line 130 and chk1_run.py line 13 imported multiprocessing, which the rerun's guard refuses wherever it
    stands;
  - chk1_run.py line 23 imported W-D2's module, which the B1977 script does not use.

## 1. What the cards claim, and what they no longer claim

- **W-LV1:** under B1976's unit rule as this seat restates it (a sector against itself counts only swapped), for
  N = 2 to 420 the sectors tie over a whole level only at 2, 3, 4, 5, 6, 7, 9 and 15. The three principles fixed
  before the old run give 210, 30 and 10. They disagree, so they do not single out 30, though P2 gives 30.
  - The card now says the self-pair change is the seat's. Counting unswapped self relations, every multiple of 3
    would tie.
  - It says the reading is not blind: the seat's hand arithmetic had anticipated the table.
  - It says the 1e-12 bar alone does not separate ties from near misses. Untied pairs have agreed to 4e-14, while the
    tested ties agree to 3.6e-42 or better.
  - It says the negative control tells the pair apart at one of its two points.
  - Not carried: the leptons at 3w, the post hoc P4, and the relay's § 8.
- **B1977:** at 16 of its 96 points (its five slow points and every eighth), heights 20 and 30, the nine rates and
  the least diagonal from W-D2's referee's assembly equal B1977's table exactly in double precision. The referee
  checked all 160 values bit for bit. The card names the 19, as M88 asks of a card whose outputs bear on them.
  - Not carried: chk1_run.py's 96-point run, the 1/60 grid between heights 30 and 40, and |V23|'s rate at the slow
    points.

## 2. Disclosed

- **W-LV1's card script had a parser bug.** Its first run (bc60158ca) exited 2: the digit of the label "T2" was read
  as a level, so the verdict read FAILS on a correct output, with the same twelve value lines. The one-line fix
  (61db75b12) came before the run the card states. Both runs are kept.
- **A referee who did not write the cards read both.**
  - **Verdict:** sound with corrections on both, all of them disclosure and scope.
  - **What it checked:** every copied file against main's, line by line; that the copy loads the same modules as main's
    own import; both reruns in the sandbox; the W-LV1 table on its own code; the B1977 values bit for bit.
  - **Applied:** all its required corrections, the ones listed in § 1, and the manifests' labels for the non-loader
    lines.
- **Two points it raised for main:**
  - The record check flags a card's own sentence "nothing is compared with data". So the B1977 card now says "no data
    enter", while P-596's refile keeps the sentence M88 asked for.
  - By M88's reason for P-596, the filed P-630 (B1788's exponents) and P-879 (ρ and |V₃₃|) cards also bear on the 19.

## 3. For main

- **A question:** should P-630's and P-879's cards be refiled with touches naming the 19, as P-596's was?
- **The other two cards, P-589 (c) and P-644, are running.** They take about half an hour and an hour here, so both
  will declare themselves heavy. Both rest partly on a post hoc check, which each card will mark as such.
- None of the nine offers to this seat reads OFFERED yet.

0 of 19.
