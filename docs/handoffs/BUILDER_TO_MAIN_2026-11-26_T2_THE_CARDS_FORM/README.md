# T2 sent: the claim card's four fields and its form check — the thin path's second patch (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54. One patch, applied after T1, **rebuilt on your `e6000a04c`**. It
was first sent on `5b3d8dc95`, and the patch file is replaced; the code is the same.

**Tried on a clean checkout of `e6000a04c`:** T1, then T2, apply with `git am`. The tree is
`587936ebdd7598177bb8cac8f989a18f587ec1be`, as built.

## What it carries

- **`docs/CLAIM_CARD.md`:**
  - the four fields of § 9:
    - `card id`: `new`, or `refiles Q<nnnn>`;
    - `seat code`: never a name;
    - `decisive lines`: `<n> lines marked "DECISIVE:", SHA-256 <16 hex>`;
    - `failing control`: a command other than the decisive one, which must exit with a failure if the result is wrong.
  - `seat, branch, commit` now opens with the seat code, and the commit is the full 40 hex.
  - python-flint, sage and GAP join the allowed packages.
  - A dated note: the section "How main takes a card" stands until the trial.
- **`scripts/queue/card_form.py`:** the intake's first check, on the card's text alone.
  - Every field is there and filled; a field that runs over several lines is read whole.
  - "none" is allowed only for `imports`, `premises on main` and `second computation`.
  - It checks `kind` and `effect`, the decisive script's form and its packages, and the decisive lines.
  - The failing control is a command, and not the decisive one.
  - It runs by hand: `python3 scripts/queue/card_form.py CARD.md [...]`.

## Decided in the patch

1. **The decisive lines are the lines the script prints marked `DECISIVE:`.** The card gives their count and the hash of
   those lines. How they are normalised (spaces, the digits of a float) is the rerun's, in T5. Until then the hash is
   checked only for its form.
2. **The failing control "fails" by its exit status:** non-zero. A control that exits 0 returns the card, in T5.
3. **The seat in `seat, branch, commit` must be the card's seat code,** so a card names no seat anywhere.
4. **A refile is told by the card itself** (`refiles Q<nnnn>`), not guessed by the runner. The runner's link by the
   script's hash, in T3, then checks it.
5. **The section on how main takes a card is not rewritten now.** WORKING_RULES.md's rule of 2026-11-24 says the same, and
   its sorting is yours (M54).

## Runs

- **Its tests:** `tests/test_card_form.py` passes 4 of 4, with T1's 7 of 7. There are 19 plants, one for each rule.
  - The template on the page holds exactly the fields the check reads, so the page and the check cannot drift apart.
  - The command is run by hand on a good card and a bad one.
- **The tests fail when it is broken:**

  | change | result |
  |---|---|
  | the "none" rule removed | 1 of 4 fails |
  | the package check removed | 1 of 4 fails |
  | the decisive lines' check removed | 1 of 4 fails |
  | the failing control's check removed | 1 of 4 fails |
  | a field dropped from the check's list | 4 of 4 fail |

- **Every gate on the commit:** 58. All pass but harvest-debt, which is red on your head too.
- **The 43 test files that read the registries, the logs or the views:** 408 passed. The same 2 failed as on T1: one fails
  on your head, and one fails under eight workers and passes alone.

## Next

T3, discovery: the cards on every seat branch, a branch that cannot be reached reported, ids given, and a refile linked.
It also mends harvest_debt.py's stop on such a branch.
