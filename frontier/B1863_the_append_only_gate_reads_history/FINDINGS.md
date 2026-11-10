# B1863 — The append-only gate reads history: the first of the audit's two critical findings, closed with its planted tests

*Main, 2026-11-10 (S306o). The advisor seat's finding G1 (harvest row 1629; P-757; the closure programme's WP-0.7):
the gate that guards the progress log could not see a committed change. Reproduced on main by main's own reading of
the gate and by main's reader's planted run (PV1, PV2). This arc is the fix and its tests. No physical value is
computed. 0 of 19.*

## 1. The answer first

- **What was wrong.** The gate compared the working file with the same file at HEAD. It saw an uncommitted change
  only. At the push hook's clean checkout the working file is HEAD's, so there the gate could not fail at all.
  Deleting two hundred lines of the log and committing passed; so did replacing the log with one line.
- **What it does now.** It reads history. Every commit on main's first-parent line after the rule's first commit that
  touches the log must keep its parent's log as a prefix. The one exception stands as before: a roll-up, whose removed
  prefix must be found verbatim in that same commit's archives.
- **It fails closed.** With no repository, in a clone that does not hold the rule's first commit, or on a history that
  does not descend from it, the gate reports that it cannot verify. It does not pass with nothing checked.
- **A violation stays visible.** Restoring the text in a later commit does not clear it. It is cleared only by a
  waiver that names the commit, with the owner's reason, in the gate's own source. The waiver list is empty.
- **The runner no longer prints a bare "ok" for a gate that checked nothing.** Such a gate is printed SKIP with its
  own words, and the review tool's fresh clone counts a SKIP against the clone.

## 2. The tests (`tests/test_append_only_history.py`)

Each builds a small repository of its own, commits the violation, and runs the check on the clean tree at that commit.
That is the audit's standard for a fix to enforcement.

| test | what is planted | result required |
|---|---|---|
| PV1 | two lines deleted from the middle of the log, committed; the tree clean | refused, naming the commit |
| PV2 | the log replaced by one line, committed | refused |
| a restored deletion | the text put back in a later commit | still refused, until each commit is waived by name |
| a roll-up | a prefix of dated entries moved into an archive in the same commit | passes; without the archive, refused |
| unreadable history | a clone of depth one; a plain directory; an unrelated history | "cannot verify", each time |
| the gate itself | the gate function pointed at a repository whose history holds the violation | fails: this is the registered control |
| the runner | the gates run on an export with no repository | the append-only gate FAILS; three gates print SKIP; none prints "ok" |

The registered control for this gate was a test that replaced the gate's own inputs and exercised the working-file
comparison only. It is kept, and the register now names the test that plants a committed violation.

## 3. What is not done here

- **History before the rule's first commit is not read.** The rule's first commit is `f31729801` (2026-11-10). The
  1,512 earlier commits that touched the log are not checked by this gate.
- **The gate's own source can be edited in the commit that violates it.** That is true of every gate that runs from
  the pushed tree. The audit's finding G12 holds it; it is open.
- **The other gates that skip without a repository still skip** (attribution, tracked-forbidden, log-changelog-paired,
  and the review counter). They are now printed as skipped. Making each fail closed is the rest of finding G5.
- **The second critical finding, G2,** an edit of a sealed file after its seal, is next. It needs the same turn: a
  sealed file read against its own history.

## Seen first

- **The repo sweep:** `grep` for the gate's name and for "git unavailable" across `tests/` and `scripts/`: one
  registered control (`tests/test_gate_failing_paths.py`), which exercises the working-file comparison only; no test
  that commits a violation. ERROR_LEDGER's E84 is the class: a check that is cited and cannot fire.
- **The literature:** none needed.

## Disclosed

- **The audit found this; main did not.** The gate has guarded the log, by its own description, since July.
- **Main's first try at the rule's first commit was a guessed hash,** and the gate failed closed on it. The constant is
  now the full hash, and a test asserts its length.

## Reproduce

```
python3 -m pytest -q tests/test_append_only_history.py tests/test_gate_failing_paths.py
python3 scripts/gates/gates.py | grep append-only
```
