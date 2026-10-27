# B1787 — P210 REVIEWED AND ACCEPTED BY MAIN (P-386): THE AUDIT LANE'S SEALED PACKAGE IS SOUND FOR ITS BOUNDED CLAIMS AND ITS WRAPPER FAIL-CLOSED; ACCEPTED FOR EXECUTION WITH NAMED CAVEATS — A PASS CONFIRMS THE LANE'S ARITHMETIC; P-210 IS SHARPENED, NOT ANSWERED

**Verdict: PROVED (a review; main's decision: accept for execution with named caveats).** cc (main), 2026-10-27, at the
owner's ruling: "no, just audit lane with its agents. youre ment to verify and review finally, everything". **0 of 19.**

## 1. Why main reviewed it

The audit lane sealed its P210 execution package (39ce620a8; 39 artifacts; ten check methods) and asked for a non-authoring
review and main's acceptance. Its "independent" review (523821858) was the lane's own agents (the owner), so main does not
accept it as independent. Main reviewed the package itself with two read-only reviewers — the code and check design
(`REVIEW_CODE.md`), the mathematics (`REVIEW_MATHEMATICS.md`) — statically; nothing in the package was imported or run.

## 2. What main found

- **Custody holds:** the specification's hash, all 39 pins and the design are unchanged from the seal to the branch head.
- **The mathematics holds for its bounded claims:** every load-bearing identity re-derived in main's reviewers' own code
  (the maximal null planes b = Ua; the Q8 commutant and U = C ⊗ I₂; graded planes with index 2r − 3; Y = −2I₃ in main's
  B1659 basis; the exterior tail and its even positive rank; the comparator's gap; the ratio 12).
- **The wrapper is fail-closed;** no bypass found.
- **Named caveats (none blocking):** a pass confirms arithmetic, not P-210 (P-210 sharpened, not answered; the package's own
  answer is conditional and negative — no domain selected at the symmetric state); several checks pass by construction or
  are definition checks (4, 6, 7, 10); missing controls (a transpose-versus-dagger control in check 1; a wrong Green sign, a
  wrong decay orientation and an omitted MINUS slot in checks 8–9 — the orientation is a convention, untested); scope (the
  Q8 stabiliser full only at generic τ; the index sheaf-level; K = 0 at the symmetric state not Fredholm); the run procedure
  (a fresh clone of the audit branch, the pinned runtime, the literal argv, the wrapper chain hashed externally).

## 3. The records

- `MAIN_REVIEW.json` — main's review in prospective.py's schema (reviewer "main", non-authoring, source complete,
  APPROVE_EXECUTION, unresolved empty, every caveat in its scope), committed separately from the acceptance.
- `ACCEPTANCE.json` — main's acceptance (receiver main, ACCEPT_INDEPENDENT_REVIEW, binding the review commit), in a later
  commit, reachable from origin/main.
- How a result will be read: a pass records "the bounded quotient-model statements confirmed by the lane's code; P-210
  sharpened, not answered"; a failure is diagnosed against these caveats. Neither is a banked positive.

## Seen first

`VERDICT topic-sweep /P210|P-210|symmetric state|Green response|exterior gap|Q8 stabili/ (full text): 4 of 1534 arcs on main match (PROVED 3, no verdict file 1)` — the record's B1678 (the
lifted register, verified on main), and the register's P-210, P-218, P-386. **Literature:** none beyond the record.

## Files

`MAIN_REVIEW.json`, `REVIEW_CODE.md`, `REVIEW_MATHEMATICS.md`, `ACCEPTANCE.json` (the later commit). The lock:
`tests/test_b1787_p210_reviewed_and_accepted_by_main.py`.
