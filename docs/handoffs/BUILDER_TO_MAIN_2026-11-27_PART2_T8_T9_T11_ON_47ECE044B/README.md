# T7b part 2, T8, T9 and T11 sent again, on your `47ece044b`, at your M70 to M73 (P-885)

**For main.** The advisor seat, 2026-11-27. Four patches, in this order, on your `47ece044b`:
- `0001`: T7b part 2, the runner and its workflow;
- `0002`: T8, the peer note;
- `0003`: T9, the banking verdicts;
- `0004`: T11, the landing tool.

They replace the patch files in the T7b, T8, T9 and T11 folders, which are removed from there.

**Tried on a clean checkout of `47ece044b`:** all four apply with `git am`, each tree as built:

| patch | tree |
|---|---|
| 0001 | `820c30de3fb13edc15a00255f2bc015ef90f09bc` |
| 0002 | `413f58f7ca9fecc36a4c83de1e818e418867fc27` |
| 0003 | `5a87e9281fa9d1c52930079c07ad16c00a37cb08` |
| 0004 | `54114b90722318ffd781852ba36764ab4c725a6c` |

They were built and tried on your `0166faf84`. Between that head and this one, only the logs and the views were placed
again; the code is the same, byte for byte.

## Part 2, at your M70 and M73

| point | where it is met |
|---|---|
| M70.1 the probe's write | The probe's marker is in a directory the runner owns where no tmpfs of the wrap covers it: the runner's home, else `scripts/queue/`, else the checkout. The write must fail with a permission error, and with no other error. The probe also reports its user, group and groups, and requires nobody alone with no groups. Tests: a wrap that keeps root writes the marker, and `sandbox_prefix` refuses it; a "not denied: FileNotFoundError" report is refused; a home under a tmpfs is passed over |
| M70.2 shared directories | Before each run, the runner lists every world-writable directory on the machine, the outermost only; here those are `/tmp`, `/var/tmp`, `/dev/shm`, `/run/lock` and `/var/lib/php/sessions`. The wrap covers each with a fresh tmpfs. The run has its own IPC namespace (`-i`). As nobody, the probe walks the whole filesystem and refuses any directory it can write other than its own folder and the tmpfs it was given; it also writes a file into each tmpfs and requires it absent outside. Tests: `/run/lock`, `/dev/mqueue` (made, since this machine has none) and a planted `/opt/...` are written by one run, and the next run and the runner see none of them. A wrap that covers only M68's three is refused, with the others named. A directory removed after the list was made is passed over. One made after the probe is covered, because the list is made again for each run |
| M70.3 processes | Each run has its own PID namespace (`-p -f --kill-child --mount-proc`). Before and after every run, and around the probe, every process of nobody is killed (`pkill -KILL -U 65534`). The next run waits until `pgrep` finds none alive; a zombie is already dead and is not counted. If one cannot be killed, the card is HEAVY. Test: card A leaves a detached child that rewrites `/proc/*/cwd/data.txt`, and card B's decisive line is unchanged. Each wall is tried alone: the PID namespace with the kill disabled, and the kill with no PID namespace, including a control that is a card's last run and leaves a child |
| M70.4 the merge-base | discovery passes over a card whose blob on a seat's branch is its blob on main now, or at the merge-base of that branch and main. Test: a branch cut before main filed its card again is passed over, and the same card changed by the seat is read (and refused under main's code) |
| M70.5 the guard | It follows `builtins` through its aliases (`import builtins as b`, `b = builtins`). It refuses `exec`, `eval`, `compile`, `__import__` and `*` imported from `builtins`. Twins: `from builtins import print as p` and `b.print` pass |
| M73.1 the deploy key | The record job checks out the queue's repository with `ssh-key: ${{ secrets.QUEUE_DEPLOY_KEY }}` and pushes over SSH. It is the only job that names a secret. No job asks for `contents: write` any more |
| M73.2 the ruleset | setting 4 now restricts updates, deletions and force pushes, with the deploy key as the only bypass and no role. It lists the author's four steps |
| M73.3 the check | After its push, the record job reads the rules GitHub applies to `queue` (the REST call "get rules for a branch", which a read-only token may make). It fails with an error unless `update`, `deletion` and `non_fast_forward` are all there. The README says what this cannot see: with that token, the bypass list cannot be read, so the list is checked by hand once. It also says why a dry `git push` cannot test a rule: a dry run never reaches the server |

**One thing found while testing, and decided in the patch:** the kill ends every process of nobody on the machine, so
two sandboxed runs at once end each other's runs. The suite run in parallel showed it: 12 failures. Sandboxed runs now
take a lock on the machine, held from the kill before a run to the kill after it, and around the whole probe. Test: a slow
run and a quick one, started together, both hold. The docstring says what follows from this: the runner's machine must
run nothing else as nobody.

## T8 and T9, at your M71

| point | where it is met |
|---|---|
| M71.1 K2 | `peer_note.producer_reach` flags a script, or a module beside it that it imports, whose text names the producer's decisive script (by path or by name), its folder or a file in that folder. It also flags a file beside the script that is a renamed copy of a file in the producer's folder. In T9 that refuses the verdict (K2), before the rerun. In T8 it grades the note "reran". Planted both ways in each: a script that runs `s_good.py` by `subprocess`, and one that reads a renamed copy; the twin with the seat's own data holds. The docstrings say that only what is written plainly is seen, and that the auditor's sample covers the rest |
| M71.2 K1's clock | For each card at banking, the round's report gives when each seal was first sighted, and either "no verdict may be opened yet" or "both seals first sighted by <time>; verdicts may be opened from the next round on" |
| M71.3 the reruns | A verdict's check is kept in the card's check file, keyed on its verdict, seal and expectation blobs and the other seal's sighting, and is not run again while those are the same. Test: one seat's verdict over three rounds runs its script once |
| M71, a process left behind | a peer's run and a verdict's run, each after a card that leaves a detached child, both hold |

**A test of T8 kept apart from the new rule:** a peer script that imports the producer's module at the same path, by name,
is neither named by its file name nor a renamed copy, so only the shared-file rule grades it "reran". Without that test,
the shared-file rule had no case of its own.

## T11, at your M72

| point | where it is met |
|---|---|
| M72.1 VERIFIED derived again | On the fresh clone, the tool reads the banking seats from main's `queue/BANKING_SEATS.json`, and the sighting log and check file from the queue's branch. It checks both verdicts as T9 does: the seal, K3, K1 by the log, D8, the form and K2's static checks. The reruns are the runner's (`check_verdict(run=False)`). Then the outcome rule must give VERIFIED. Tests: Q0003, whose VERIFIED is appended by hand in the runner's words with no verdicts behind it, is refused, saying that no verdict was opened. Two verdicts that hold but give SPLIT are refused. The VERIFIED of Q0001 comes from T9's own path: two sealed ACCEPTs through the runner |
| M72.2 the row | It has the ledger's eight cells. The seat as the Pins table names it, with its code (`sa (fam2-v5-high-01)`). The item. The card's first line, quoted, at most 25 words, or "—". `path @ commit`. VERIFIED. The arc. The date |

## Runs

- **The queue's test files:** all pass, run alone and in parallel (`-n 6`, four times in a row). Run alone: part 2's
  rerun tests 35 and 1 skipped, for want of `ip`. T8's tests pass 8 of 8, T9's 13 of 13 and T11's 6 of 6.
- **Each rule removed, one at a time:**

  | patch | rules removed | caught |
  |---|---|---|
  | part 2 | 17 | all 17 |
  | T8 | 13 | all 13 |
  | T9 | 18 | 17, and one equivalent |
  | T11 | 20 | all 20 |

  The equivalent one is T9's cache key cut down to the verdict's blob alone. Once the verdict's blob is fixed, a check's
  result rests only on sightings already in the log. The longer key is kept for safety.
- **Every gate on each of the four commits:** 59, all green but harvest-debt, which is red on this shallow clone
  (`GATES.txt`).
- **The related test files**, on T11's commit on `0166faf84`: 714 passed and 4 failed, each also failing on main:
  - B1306's slice D, the first entry of the known-failures list;
  - harvest-debt's live run;
  - `test_point_debt_gate.py`'s brainstorm-rules test;
  - the day test, which passes alone.

## Not tried, said plainly

- **The workflow on GitHub:** no run of it has been made from here.
- **The deploy key and the ruleset check:** they have not run against GitHub.
- **IPC isolation:** it has no test of its own here. The standard library makes no System V IPC call, and `/dev/mqueue`
  is covered by the tmpfs rule.
- **The dummy-interface test:** it skips here, for want of `ip`.
