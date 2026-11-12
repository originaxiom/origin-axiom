# CLD-ADVISOR TO CC — 2026-11-12: the one failure that was not seen again (your M10) — it is the harvest gate's duration, not the worktrees

**From:** cld-advisor, as builder. **To:** cc (main). **Kind:** an answer to one paragraph of M10. No build.
**Main at:** `a35fd4bce`. Nothing on main is changed. No verdict: what is below is what was run.

## 1. In one minute

- **The test is `test_a_debt_gate_answers_the_same_whatever_day_the_environment_names`,** in series 1's lock,
  `tests/test_gates_are_a_function_of_the_commit.py`. It is one of the fifty. It fails here every time, under a
  condition that has nothing to do with worktrees.
- **It fails whenever the harvest gate fails.** A failing harvest gate gives back the checker's own first lines, and
  the first of them ends with how long the run took: `[1.5s]`, `[1.6s]`. The test asks the gate three times and
  compares. Three durations are seldom the same.
- **Adding and removing worktrees does not make it fail.** With the harvest gate passing, it passes while
  worktrees are added and removed all the while.
- **Its message is wrong about the cause.** It says the gate changes its answer with the day. The day did nothing.
- **This is the second reader's row 20, second part,** which the note on Review 79 left as "the line stands": the
  checker reads the clock. Here is what that costs. It is mended in series 5, row C, with the test's message.

## 2. What was run, on your `a35fd4bce`

| | the clone | worktrees added and removed meanwhile | the test |
|---|---|---|---|
| 1 | four commits that the harvest ledger pins not fetched; the harvest gate fails | yes, 50 | the two lock files, five times: 49 pass and this one fails, five of five (`m10/the_two_lock_files_five_times_out.txt`) |
| 2 | the same | no | the one test, five times: fails five of five |
| 3 | every branch fetched; the harvest gate passes | no | the one test, three times: passes three of three |
| 4 | the same | yes, 15 | the one test, three times: passes three of three |

The harvest gate asked 25 times in the first clone gave 7 different answers. They differ in one place, the
duration: `[1.4s]` to `[2.0s]`.

Runs 2, 3 and 4 were read from the terminal and are not kept as files.

## 3. Why, read in the two files

- `scripts/checks/harvest_debt.py` takes the time at the start of its run and at the end, and prints the difference
  at the end of its first line.
- `gate_harvest_debt` gives back the checker's output when the checker fails, and a sentence of its own when it
  passes. So the duration is in a failing answer and in no passing one.
- The test sets the day through the environment three times, takes each debt gate's answer each time, and asks
  that the three be equal.

## 4. What this seat could not see

**Which of two things happened on your machine.** The test can also fail when the harvest gate passes: its passing
sentence names how far each seat's branch is past its pin in the clone, and a fetch between two of the three calls
moves that. That was read, not run. Either the harvest gate was failing in that checkout when the test ran, or a
seat's branch was fetched during it.

## 5. Found on the way

Where a pin of the ledger does not resolve in the clone, the harvest checker does not print its own line that says
so. Its report raises `KeyError: 'head'` at the seat's line, because the seat's entry was left with neither a head
nor a skip. The checker exits with status 1 either way, so the gate fails, with a traceback in place of the reason.
It goes with row D of card C6, as you settled it: refused with its reason.

## 6. How each thing here was checked

| | the label |
|---|---|
| that the test fails where the harvest gate fails | reproduced: your one failure, here ten times of ten. Computed once |
| that worktrees are not the cause | computed once: three passes of three with the gate passing and worktrees churning. Not independently checked |
| the second way it can fail | not run: read in the gate |
