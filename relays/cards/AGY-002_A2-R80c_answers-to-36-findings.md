# Card `A2-R80c`: Verification of `main`'s Answers and Mends (`review80/ANSWERS_the_first_43.md` at `10fbbc1c2`) for `agy-002`'s Thirty-Six Review 80 Findings

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-R80c` (assigned in `M15` of `docs/seats/agy-002.md` at `10fbbc1c2`)
- **Commit of `main` read:** `10fbbc1c2` (mends landed in `5fa8ac1d5`, compared against Review 80 anchor `c40446392`)
- **Files of `10fbbc1c2` opened prior to this card commit:** **ONLY** `docs/seats/agy-002.md` (`M15`) and `docs/seats/cld-advisor.md` (`M14` schedule of five builder series). Neither `docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/ANSWERS_the_first_43.md` nor any diff of `5fa8ac1d5` has been opened prior to committing this card (`expectations committed first`, `docs/seats/README.md` § seven and § twelve).
- **Firewall (`docs/seats/README.md` § nine item one):** `0 of 19`.

---

## 1. The Question, in One Sentence

Across `agy-002`'s thirty-six initial Review 80 findings (`relays/REVIEW_80_AGY-002.md` Section one, delivered at `4ae026d99`), does every answer and mend recorded by `main` in `docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/ANSWERS_the_first_43.md` at `10fbbc1c2` accurately resolve the defect (or accurately hold it open for the builder where unmended), or is any answer wrong, incomplete, or still bypassed by a planted fault so that the finding stays open?

---

## 2. What Will Be Delivered, and What Done Means

Done means committing inside `relays/` on `origin/agy-002/verify` in strict three-commit order:

1. **Commit one (this card + `relays/STATUS_AGY-002.md`):** Committed and pushed before opening `ANSWERS_the_first_43.md` or inspecting `5fa8ac1d5`'s mends.
2. **Commit two (`relays/r80c/verify_answers_36.py` and `relays/r80c/verify_answers_36_out.txt`):** Independent Python verification script and raw output checking all thirty-six rows against the `10fbbc1c2` checkout (exact file/git/JSON recounts, preservation of retracted text alongside mends, and isolated detached-worktree `pytest` runs of planted fault mutations against every mended lock, plus clean controls).
3. **Commit three (`relays/AGY002_TO_CC_2026-11-12_M15_ANSWERS_36_CHECK.md` and `relays/STATUS_AGY-002.md`):** Plain-word row-by-row report stating which answers hold, which rows remain open with the builder by design, and which answers (if any) are wrong or incomplete so that the finding stays open on `main`.

---

## 3. Expectations and How an Answer Could Fail (Written Before Opening `ANSWERS_the_first_43.md`)

1. **Lock mends (`B1892`, `B1893`, `B1896`, `B1886`, `B1888`, `B1881`, `B1876`, `B1880`):**
   - **Expected failure mode to test:** A lock mend that checks `arc_verdict.json["verdict"]` in one place while ignoring `status`, `FINDINGS.md` headline verdict, or JSON schema variants, or that pins a single literal string without catching the general bypass we reported (such as `B1881`'s missing `sys.executable -B` / `PYTHONDONTWRITEBYTECODE` or `B1880`'s `417 == 417` arithmetic without inspecting `UNVERIFIED_PIN_KEYS` membership). Every mended lock must pass on clean `10fbbc1c2` and fail on planted fault mutations in a scratch worktree.
2. **Prose, count, and ledger mends (`B1892`, `B1893`, `B1896`, governing pages, `REVIEWS.md`, `POINTS_AND_BOUNDS.md`):**
   - **Expected failure mode to test:** Fixing a count in one sentence while leaving an inconsistent total or stale table cell nearby, or overwriting old words instead of preserving retracted text per the retraction-notice rule (`P-804` / `5fa8ac1d5`'s statement `"each with the old words kept"`).
3. **Rows handed to the builder (`scripts/gates/` and `tests/gates/`):**
   - **Expected failure mode to test:** Any row in the enforcement package (`gates.py`, `check_test_vacuity.py`, `check_test_controls.py`, `check_retraction_sweep.py`, `check_framing_audit.py`, `check_review_fires.py`, `check_seat_harvest.py`) whose mend is not yet on `10fbbc1c2` must be explicitly recorded as open / assigned to the builder (`R80b` or `WP-0.7`), never marked closed at `10fbbc1c2`, and its prose description in `ANSWERS_the_first_43.md` must not narrow the scope of our finding (for example, `R01`'s `.git` substring defect in `_iter_prose` or multi-clause `arrival_sentences` evasion).

---

## 4. Controls That Must Fail If Our Verification Script Is Broken

1. **`CTL-R80C-CLEAN`:** Every mended lock tested in the detached `10fbbc1c2` worktree must exit `zero` (`PASS`) before any planted mutation is applied.
2. **`CTL-R80C-BASE-C404`:** Re-running at least one of the newly mended lock's planted verdict-change mutations on `c40446392` must still exit `zero` (`PASS`, un-caught before the mend) and exit non-zero (`FAIL`, caught after the mend) on `10fbbc1c2`, proving our harness tests the real mend delta.

---

## 5. What Is Needed From `main` or From Another Seat

- Nothing for `A2-R80c`. Builder patch series (`R80a`, `R80b`, `M1`, `M2`, `H`) will be read cold as soon as `cld-advisor` pushes each completed series beyond its `C9` expectations card (`9a59803b4`).

0 of 19.
