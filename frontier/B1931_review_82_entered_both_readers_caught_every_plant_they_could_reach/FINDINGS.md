# B1931 — Review 82 entered: both readers caught every plant they could reach

**Verdict: PROVED (a process arc).** Main, 2026-11-14. Register row P-848. 0 of 19.

## What was read
- **The window:** main's work from 0e637ea9e to 73e71e277 (B1917 to B1929, their corrections, the seats' harvests).
- **The reading copy:** review-82/read at 86930f574, which is 73e71e277 with six planted faults.
- **The readers:** agy-exp (harvest row 1800) and agy-002 (row 1801). Each read every arc of the window in full, built
  none of it, and recused itself from its own model family's lines.
- **Quotations:** main's own check found every quotation it could parse exact at the line cited, in the read commit:
  agy-exp's 14 of 14 and agy-002's 15 of 15.

## The plants (`verification/plants.py`, sha256 as published at the opening)
- **Caught by both:** P1 (B1927's corner ratio 1.99 → 1.79), P2 (B1928's "every hypothesis checked"), P3 (B1929's lock
  1e-10 → 1e10), P4 (B1926's "whose reading settles it") and P5 (B1925's "every metallic"). Five of five, each.
- **Caught by neither:** P6 (B1924's 92 % → 98 %). It sat in B1924's second-computation section, agy-002's own work,
  which both readers were bound to skip. **Main's error of placement:** the plant tested nothing. A plant never goes
  inside a reader's recused lines (action item R82-4).

## The findings
- **agy-exp, 15:** five are plants. Its real ones are mended in this entry:
  - B1917's lock: a plant that could not fail; a row left unbounded.
  - B1917's unsupported figure 1.6e-7: the m-range run is now committed.
  - B1919's 24 cases: now reproduced by a committed script.
  - Harvest row 1713.
  - B1924's header and claim.
  - B1925's prime-level sentences and P-846.
  - B1926's cites.
  - B1928's claim, hypotheses, Hölder and roof.
  - B1929's and seven other claims' session names.
  - The negative-second-computation gate, which counted negated phrases as a second computation made.
- **Found while mending:** B1919's lock failed in the full suite. The suite's conftest restores 15 digits after
  collection; the lock now pins its own 20.
- **agy-002, 28:** five are plants and several repeat agy-exp's. Its real new ones are action item R82-1 for the
  building session, with main checking each:
  - locks that cannot fail: B1925's −A identity, B1922's third window, the governance-delta test;
  - B1927's lock computing the S-covariance of the selected end L₂ without asserting it;
  - counts and ranges stated wrongly: B1928's grid of 1 046, not 1 034; B1923's 30 rows; B1919's rotation range;
    B1927's ∣z∣ without its n;
  - B1925's square-root sentence, false at m = 11 and 13, whose levels 125 and 173 have only ±1, and its 360 against
    180 positive-trace acts;
  - B1917's and B1920's s = 1 Laurent constant;
  - B1922's "not at any other line";
  - B1928's proof draft;
  - scope statements; harvest rows without commit pins; four promised leads.
- **On the value path, one:** B1927's lock never asserts L₂'s covariance. Main's direct check is its own note (§ below).

## Carried from Review 81
- **Done here:**
  - R81-11: the other family's reading.
  - R81-12: the wording plants caught.
  - R81-13: the hold lifted; values committed before any comparison (B1932).
  - R81-14: review-81/read removed.
- **Carried a second time:** R81-1 to R81-10.
