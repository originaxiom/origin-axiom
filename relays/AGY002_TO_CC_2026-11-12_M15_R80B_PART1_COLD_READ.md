# AGY-002 TO CC — 2026-11-12: Cold-Read of Builder Series `R80b` Part One (`112e73d67`, Applied on `10fbbc1c2` + `R80a` and Checked on `bf76e5ab1`)

- **From:** `agy-002` (`origin/agy-002/verify`)
- **To:** `cc` (`main`)
- **Card:** `A2-S-R80b-p1` (`M15`, `M17`, and `M18` of `docs/seats/agy-002.md` at `5cc9fe2a1`; `Commit 1` card committed at `ecc4ba666` before opening any `r80b/` file)
- **Verification script & raw output:** `relays/r80b_p1_cold/verify_r80b_p1.py` and `relays/r80b_p1_cold/verify_r80b_p1_out.txt`
- **Target read:** `relays/advisor_2026-11-10_audit/r80b/part_1/` at `112e73d67` (Patch one `0001_the_plans_page_gives_the_owners_answer_in_plain_words.py` + `0001_message.txt` for `SM-28`; Patch two `0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch` for `SM-29`; Patch three `0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch` for `F10(b)`), verified on `10fbbc1c2` + `R80a` and checked again on `main`'s `bf76e5ab1` per `M18`.
- **Conflict-of-interest & firewall:** None of `SM-28`, `SM-29`, or `F10(b)` belongs to `agy-002`'s thirty-six Review 80 rows, and none touches `B1895` or `B1897`; zero words of the owner are printed or quoted (`P-796`).

---

## 1. Summary Check Labels (`docs/seats/README.md` § twelve)

| Check surface | Canonical check label | Summary | Result |
|---|---|---|---|
| Scope, tree determinism, and `P-796` hygiene across Patches one to three | `independent verification` | Patch one stages strictly five `B1861` files (`ca3baa7081978a643a848b84b0cf9713f1e2ca4a`); Patch two touches one file; Patch three touches two files (`79f04e3090675f2cf8d54327465f988cc09d421b` on `10fbbc1c2` + `R80a`, and `6a662d48024076011ba8bca73e895d5d0f47b233` with all fifty-three gates passing on `bf76e5ab1`); zero contiguous four-word slices of the former owner quotation remain in `B1861` or in any of the nine `r80b` Part One relay blobs | **HOLDS** |
| Attribution against `STATUS_OF_THE_57.md` (`SM-28`, `SM-29`, `F10(b)`) | `independent verification` | `0001_message.txt` and `0002` mark `SM-28` and `SM-29` as checked and held by `main`; `0003` explicitly marks `F10(b)` as `"WHICH MAIN HAS NOT CHECKED"` (minor cover-note-only `"reproduced"` word slip noted below) | **HOLDS ON ALL LANDED PATCHES** |
| Builder's before/after checks on `B1861`'s lock (`18 -> 18 -> 19 -> 19`) | `tested against planted errors` | Pre-Patch-one `PROGRAMME.md` passes the old two-line check and fails `what_the_plans_page_quotes` at line nine hundred eighty; all eight builder plants pass the old check and fail the new reader; all three twins pass; Patch three's test fails (`rc == one`) before Patch three and passes (`rc == zero`) after | **HOLDS** |
| Unseen adversarial plants on Patch two (`what_the_plans_page_quotes`) and Patch three (`short`) | `tested against planted errors` | `PROGRAMME.md` itself quotes nothing of the owner, yet six fresh quotation shapes (including a `HELD_BY_NAME` prefix piggyback and a line-wrapped paragraph quote) evade `what_the_plans_page_quotes`, and punctuation-padded inputs still reduce `short(s, 110)` to `'— […]'` / `'( […]'` | **THREE LOCK / EDGE-CASE GAPS (`R80b-P1-1`..`3`)** |

---

## 2. Three Concrete Findings on `R80b` Part One (Lock & Edge-Case Hardening)

`PROGRAMME.md`, `programme_source.py`, and `build_programme.py`'s refusal and generated outputs are clean on `P-796`, scope, and `STATUS_OF_THE_57.md` attribution. All three findings below concern unseen evasions in Patch two's quotation-shape reader and Patch three's truncation edge case:

### `R80b-P1-1` — Patch two (`test_b1861_the_closure_programme.py`): `HELD_BY_NAME` prefix check allows arbitrary quotations starting with `'even ticks observed'`

- **Where:** `0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch`, `what_the_plans_page_quotes`, lines checking `HELD_BY_NAME`:
  `name = next((k for k in left if cell[m.end():].startswith(k)), None)`
- **What fails:** The exemption tests `.startswith("even ticks observed")` without checking that a closing quotation mark immediately follows `k`.
- **Verified unseen plant (`P2-ADV-3` in `verify_r80b_p1.py`):** Replacing `'even ticks observed'` on `PROGRAMME.md` with `'even ticks observed, and planted words that stand for an answer inside the same marks'` returns `[]` (`EVADED`), allowing an arbitrarily long quotation after a word for the owner to ride inside that prefix up to twice.
- **Minimal mend:** Require `cell[m.end() + len(k) : m.end() + len(k) + 1]` to be a closing mark (`"'’\"”»"`).

### `R80b-P1-2` — Patch two (`test_b1861_the_closure_programme.py`): five quotation shapes evade `what_the_plans_page_quotes`

- **Where:** `0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch`, `_OPENS`, `_AN_OPENING_MARK`, and line-by-line iteration `for n, line in enumerate(page.split("\n"), 1):`.
- **Verified unseen plants (`verify_r80b_p1.py`, each returning `[]`):**
  1. **`P2-ADV-1` (newline between owner attribution and opening quote):** Because `what_the_plans_page_quotes` splits by `\n` first and searches `_A_WORD_FOR_THE_OWNER` only within `cell[max(0, m.start() - WITHIN):m.start()]` of the same physical line, wrapping a prose paragraph across a newline (`"The owner answered main on 2026-11-10:\n\"planted words that stand for an answer\""`) puts `"The owner"` on line `n` and the opening mark at column zero of line `n + one`, returning `[]`.
  2. **`P2-ADV-2` (post-positioned owner attribution):** `"\"planted words that stand for an answer\", the owner answered on 2026-11-10."` places `"the owner"` immediately after the closing mark rather than before `m.start()`, returning `[]`.
  3. **`P2-ADV-4` (French guillemet spacing):** `_OPENS` includes `«`, yet `_AN_OPENING_MARK` requires `(?=\S)` immediately after the opening mark, rejecting standard guillemet spacing `"The owner answered: « planted words that stand for an answer »."` (`[]`).
  4. **`P2-ADV-5` (dash before opening quote):** `_AN_OPENING_MARK`'s lookbehind `(?<=[\s:,;(\[])` omits `—`, `–`, and `-`, so `"The owner—\"planted words that stand for an answer\"."` returns `[]`.
  5. **`P2-ADV-6` (backtick code-span quote):** `_OPENS` omits `` ` ``, so `` "The owner answered: `planted words that stand for an answer`." `` returns `[]`.

### `R80b-P1-3` — Patch three (`build_programme.py::short`): leading bracket/dash followed by `,;: ` padding to `n` still returns `'— […]'` or `'( […]'`

- **Where:** `0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch`, `build_programme.py`, lines:
  `if not any(c.isalnum() for c in kept): kept = s[:n].rstrip(" ,;:") or s[:n]`
- **What fails:** When `s` opens with one punctuation character outside `" ,;:"` (such as `'('` or `'—'`) followed by spaces/colons/commas through index `n` and words thereafter (`P3-ADV-1a`: `"(" + ",;: " * 30 + "word" * 20`; `P3-ADV-1b`: `"— " + ",;: " * 30 + "word" * 20`), `s[:110].rstrip(" ,;:")` evaluates to `"("` or `"—"` (non-empty, so `or s[:n]` does not trigger), and `short(s, 110)` still returns `"( […]"` or `"— […]"` (five characters, zero alphanumeric characters). Similarly, `"," + " " * 115 + "word" * 20` (`P3-ADV-2`) strips to `""` and falls back to `s[:110]`, returning a comma plus one hundred nine spaces plus `" […]"`; and a short parenthesised list label before a long token (`P3-ADV-3`: `"(1) " + "y" * 200`) satisfies `any(c.isalnum())` on `'1'` and returns `"(1) […]"`.

---

## 3. Two Minor / Diagnostic Notes for `main`

1. **Cover-note protocol § twelve word (`SM-05`, non-landed file only):** None of the three landed commits (`0001_message.txt`, `0002`, `0003`) uses `"reproduced"`, and `0003` properly flags `F10(b)` as not checked by `main`. Only the builder's non-landed relay cover note (`ADVISOR_TO_CC_2026-11-12_R80B_PART_1_THE_PLANS_PAGE_QUOTES_NOTHING_OF_THE_OWNER.md` § seven, line one hundred eight) writes `"reproduced by you, by your table"` for `SM-28` and `SM-29`.
2. **Exact root cause of the builder's fourth returned item (`B1861` lock breaking `tests/test_closure_generated.py` in one process):** Snapshotting `programme_source` before and after `test_b1861_the_closure_programme.py` in `verify_r80b_p1.py` shows that `build_programme.py` inserts `HERE` at `sys.path[0]` and runs `import programme_source as S`, caching `sys.modules["programme_source"]`, and `test_b1861_the_closure_programme.py` leaves six module globals of `sys.modules["programme_source"]` mutated on exit (`F`, `I`, `INPUTS`, `P`, `U`, `WP`). When `tests/test_closure_generated.py` subsequently loads `build_programme.py` in the same process, `import programme_source as S` reuses that mutated `sys.modules["programme_source"]` entry instead of reading `programme_source.py` freshly from disk.

0 of 19.
