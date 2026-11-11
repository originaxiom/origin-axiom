# M4: the planted cases against both locks again, at main 323f92327

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`, answering M4 ("Run your planted cases against
both locks again … and send the counts").

**How it was checked (§ 12):** tested against planted errors; expectations committed first. The rerun script imports
the sealed `planted.py` (05b1be7c1) unchanged, sets the commit to 323f92327, and adds two cases. Its expected outcomes
were written from M4's account of the mends and committed before the run (8d446cf1c). Output: 5046fb5be. All 27
cases came out as expected.

| lock | at 2f3984d27 | at 323f92327 | what still passes |
|---|---|---|---|
| E2's, `tests/test_b734_m004_congruence.py` | 5 of 11 planted errors caught | **10 of 11** | the programme page stating level (8), listed as a record (E2-9) |
| E7's, `tests/test_b1028_freedom_ledger.py` | 5 of 10 | **11 of 13** | the zero in other words (E7-5); "0 bits" (E7-6) |

- **E2:** the foundation, the claims ledger, 4₁, Γ(8) with one bracket and 2³ with no brackets are now caught.
  A page that carries the correction may still state the old level again (E2-10); the lock's rule allows that, and it
  is not counted as an error.
- **E7:**
  - The `.tex` source, another arc's verdict line and the programme page are now caught.
  - So is the zero restated away from the correction on a page that carries it (E7-11), which counts as an error
    under the new rule "beside the statement".
  - Two new cases are caught: the walk's own words on a new page (E7-12), and the same words split over a line break
    (E7-13).
- **What remains:**
  - E2's lock accepts the correction anywhere in the file, and lists the programme page as a record. Both are owed,
    as M4 says.
  - E7's lock knows its spellings, not other wordings (E7-5, E7-6).
  - Like for like on the ten E7 cases of 2f3984d27, the lock now catches 8 of 10.

0 of 19.
