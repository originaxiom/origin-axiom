# Referee report, round 2 — the revision

**Manuscript:** revised `main.tex` + `anc/`, dated 2026-09-17, against my report of the same date
(`REFEREE_REPORT_2026-09-17.md`). Repository state reviewed: `origin/main` at `21c47a51` (S19).
**Recommendation: minor revision.** The substantive fix — the one that mattered — is done and
verified. Three defects survive, two of them recurrences of items I raised, and all three are in the
verification machinery rather than in the mathematics. None is more than a few lines' work.

I re-checked the fixes rather than taking the changelog's word for them, and I checked the revision
for anything newly broken. The paper's mathematics is untouched by this round: the only claim-bearing
edits are the census-drift paragraph, two percentages, and one added hypothesis, all verified below.

---

## 1. Status of the six changes I asked for

| # | request | status |
|---|---|---|
| 1 | fix `.gitignore` so the B1419 census ships; runner names failing tests | **done** |
| 2 | regenerate or drop `anc/REPORT.md` | **not done** — regenerated but still certifies PASS without running the locks (§2.1) |
| 3 | rebuild the manifest so `git_head` matches its contents | **not done** — the recorded commit still does not resolve (§2.2) |
| 4 | fix the census-drift population | **done, well** |
| 5 | Figure 1 caption; sin²θ_W; MFP hypothesis; manifest wording | **3 of 4** — one of three sin²θ_W sites survives (§2.3); manifest wording unchanged |
| 6 | framing: title, abstract, the 53/57 ratio, the index wording | **not adopted** (§4) |

### What is properly fixed

- **`.gitignore`.** Negation rules now exist for both
  `frontier/B1419_the_arithmetic_fillings_corrected/verification/*.jsonl` and
  `frontier/B1137_regulator_probe/results/*.jsonl`, the census file is tracked, and
  **`tests/test_b1419_arithmetic_fillings.py` now passes — 5 tests, 10 s**, on a fresh worktree of
  `origin/main`. This was the worst defect and it is gone. The sweep for other locks reading
  untracked data, which I did not ask for, is the right generalisation — **and it holds**: I scanned
  all 147 manifest locks for literal data filenames, resolved them under `frontier/`, and found
  **zero** files that a lock reads, that exist on disk, and that are untracked. (Method's limit: a
  lock building a path dynamically would escape this scan.)
- **The new regression lock checks trackedness directly.** `test_b1424_referee_defects.py` carries a
  `_tracked()` helper that shells out to `git ls-files --error-unmatch`, so the class of defect — not
  just the instance — is guarded on the data-file front. That is the right shape, and it makes the
  gap in its percentage test (§2.4) the more conspicuous.
- **`run_package.py`** now passes `-rf --durations=5 --color=no` and strips ANSI before parsing, so a
  failing run names its failures. Exactly the fix needed.
- **The census-drift paragraph** is rewritten to carry both triples, name which population each is
  taken over, and say that an earlier version had it wrong. The numbers are right: I had measured
  33.00 → 33.88 → 31.38 on the one-cusped census and 34.25 → 29.38 → 21.12 on the full one, and both
  are quoted correctly. The new conclusion — that the door is *not* an artefact of the census's small
  end, so the genericity argument is stronger — follows from the corrected figures.
- **Figure 1** now reads "Fifty-three links are forced" and its tick loop draws 57 ticks under a
  57-link axis. The chain table is intact: 57 rows, tally 36/8/6/4/2/1, axioms at 3, 4, 5, 18, none
  in 6–17. The appendix still has 67 rows.
- **The Menal-Ferrer–Porti hypothesis** is now carried, and **the translation is correct** — I
  checked it at the source rather than against the paraphrase. MFP §1 states: *"for every positive
  integer n there exists only one complex irreducible representation Vₙ of SL(2,ℂ) **of dimension
  n**. Moreover, Vₙ is **(n−1)-th symmetric power** of the standard representation."* So the source's
  n ≥ 2 is exactly m ≥ 1, and the paper's "m ≥ 1 (the source's n ≥ 2)" is right, as is its added
  remark that the theorem says nothing about the untwisted case.

---

## 2. What is still wrong

### 2.1 `anc/REPORT.md` still certifies PASS without having run the locks

The report was regenerated — fresh timestamp, and the counts now match the manifest (67 claims,
95 pairs, 21 seals, 147 locks) instead of the stale 54/75/111/18. But it is **29 lines long**: a
header, the manifest line, a `## Seals — PASS (21/21 match)` section, and

> **Overall: PASS.**

There is **no `## Test locks` section at all.** It was produced by `run_package.py --seals`, not
`--seals --locks`. So the shipped certificate is green on a run that never executed the thing the
package exists to execute.

This is the same defect as my §4.2 in a new form, and it is now sharper rather than softer, because
the changelog for this very revision says in its own words that locks still fail:

> *The package's remaining failures are named rather than mysterious: the harvest lock fires
> correctly on six genuinely unrowed audit-seat pre-execution documents … and one subprocess lock
> whose timeout was tuned to an idle machine.*

A reader opening `anc/` sees "Overall: PASS" beside a manifest of 147 locks, with nothing indicating
that the locks were not run and that some of them fail.

The mechanism is visible in `run_package.py`: `all_ok` is initialised to `True` and is only `&=`-ed
against steps that actually ran, so any subset of steps that passes yields `Overall: PASS`. A run
with `--seals` alone therefore cannot fail. Either run the locks before shipping the report, or have
the runner qualify its verdict by what it ran — "Overall: PASS (seals only; locks not run)" — which
is three lines and cannot be forgotten at submission time the way running the right command can.

### 2.2 The manifest's `git_head` still does not resolve

`MANIFEST.json` records `environment.git_head = ddff9c63`, in both the shipped bundle and the
repository's own copy at `origin/main`. **That object does not exist in the repository** —
`git cat-file -t ddff9c63` and `git rev-parse ddff9c63` both fail after fetching every ref. The
manifest was again built before the commit that contains it existed; S19 landed as `21c47a51`.

The changelog says "the rule is now in the submission recipe", which is a procedure, not a check.
The shipped artefact still violates it, so the recipe did not hold on the first run after being
written. `build_manifest.py` should refuse to record a `git_head` that is dirty or that does not
contain the files it just catalogued — again a few lines, and unlike a recipe it cannot be forgotten.

### 2.3 The chain table ships one stale row, and its drift gate samples 9 of 57

This is the most interesting of the three, because it explains the near-miss in §1's item 5 and
because it touches a guarantee the paper makes in its own text.

The changelog says the 0.9 % figure was "stated in three places" and corrected. Two were: the
summary and the non-claim both now read 0.8 %. The third was not. **Link 43 of the chain table still
reads `$\sin^2\theta_W$ by 0.9\%`** — in the repository's `main.tex`, in the shipped bundle, and in
the submitted PDF, where it renders as *"(α_s by 35%, sin²θ_W by 0.9%); the desert is dead as a
mechanism"*.

That row is *generated*. Running `scripts/checks/paper_chain_table.py --tex` on the current tree
emits link 43 with **0.8 %**. So the shipped paper disagrees with its own generator:

```
link 43  generator: ... known to ($\alpha_s$ by 35\%, $\sin^2\theta_W$ by 0.8\%); the desert is dead ...
         paper    : ... known to ($\alpha_s$ by 35\%, $\sin^2\theta_W$ by 0.9\%); the desert is dead ...
```

Comparing every generated row against both files: **exactly 1 of 57 rows is stale**, and it is
link 43. (`referee_2026-09-17/scripts/r2_chain_table_drift.py` does this comparison and prints the
pair above.)

The paper says of this table (§3):

> *the table itself is generated from the ledger rather than typed --- which is how two mis-parses
> were caught while preparing it*

and the gate `tests/test_paper_chain_table.py` is meant to enforce that. Its last test ends:

```python
rows = [l for l in gen.splitlines() if re.match(r"^\d+ & ", l)]
assert len(rows) >= 46, len(rows)
for row in rows[:6] + rows[-3:]:
    assert row in tex, f"chain table is stale, regenerate: {row[:60]}"
```

It compares **the first six and last three rows** — 9 of 57. Rows 7 through 54 are never checked, and
the one stale row sits there. The gate passes. The fix is to drop the slice and iterate over `rows`;
I ran that comparison and it finds the stale row immediately.

So the guarantee as the paper states it — generated, not typed, gated against drift — currently holds
for 9 of 57 rows. Either widen the gate or soften the sentence; widening is one line and is clearly
what was intended.

### 2.4 Two smaller things

- **The new regression lock guards the instance, not the class.**
  `tests/test_b1424_referee_defects.py` is good practice and its five tests cover the tracked census
  file, the `.gitignore` negation, both drift triples and a second method. But its percentage test
  asserts the literal strings `"0.9\\%$, about fifty experimental" not in t` and
  `"$0.8\\%$, about fifty experimental" in t` — it pins the one prose site and says nothing about any
  other occurrence, which is why the generated row sailed past it. `"0.9\\%" not in t` would have
  caught it. This is worth fixing not for its own sake but because the project's own `ERROR_LEDGER`
  opens with the rule that entries are per error *class*, not per incident; the lock is written the
  other way round. Note also that the lock covers the three defects that were fixed and none of the
  two that recurred (§2.1, §2.2) — its shape is the shape of what got done.
- **`MANIFEST.md`'s header** still reads "95 establishing records" where 95 is the number of
  claim–record *pairs* and the number of distinct records is 80. Unchanged from round 1.

---

## 3. Nothing new is broken

I diffed the revision in full. Beyond the fixes, the only changes are typesetting: an `array`
package, the freedom ledger's three explicit ragged-right columns, and the chain figure's labels
rewritten as two-line centred nodes. The abstract is byte-identical. The chain table and the
appendix table are structurally unchanged and I re-verified both tallies. No new claim was
introduced, so nothing in this round needed fresh mathematical verification beyond the three edits
checked in §1.

---

## 4. The framing recommendation, restated once and then dropped

My §3 asked for three things that are judgement rather than defect: bring the title and abstract to
the standard the §4 scope note already meets; demote the 53-of-57 ratio; and say in the abstract, as
§7 already says in its scope note, that the index is a count of twisted classes rather than a
four-dimensional index. None was adopted, and the author is entitled to decline a referee's taste.
I record the recommendation as standing and will not press it again: it does not bear on whether the
paper's claims are true, only on how a reader will first read them.

---

## 5. Recommendation

**Minor revision.** Items §2.1, §2.2 and §2.3 are each a few lines and each is a check rather than a
prose change, which is the right kind of fix for a paper whose thesis is auditability. Once the
package refuses to print PASS for a step it did not run, the manifest refuses a `git_head` it cannot
justify, and the chain-table gate reads all 57 rows, the verification story will be as strong as the
paper says it is.

I will say plainly what this round showed: the one defect that could have invalidated a claim — the
census evidence excluded from every clone — was fixed properly, generalised to a sweep for other
instances, and locked. The three that remain are the machinery reporting on itself more favourably
than it has earned, which is exactly the failure mode a paper like this one has to be hardest on.

---

*Both rounds' reproductions are in `referee_2026-09-17/scripts/`. Round 2 additionally: a fresh
worktree at `21c47a51` with the package run end to end; `git cat-file`/`rev-parse` on the recorded
manifest commit; a row-by-row comparison of the generator's 57 rows against both `main.tex` copies;
and the Menal-Ferrer–Porti convention read from the source PDF.*
