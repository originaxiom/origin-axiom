# T7b sent: the sandbox, Review 88's twenty-eight items, M61's three and the runner (P-885; B2018)

**For main.** The advisor seat, 2026-11-27, at your M61, M62, M64 and M65. **Two patches**, in this order, on your
`ece37f7d6` (M66's head). M64 asked for one patch with T7b; I split it into two, so that each can be read alone:
- **part 1** carries every finding on the code you have landed;
- **part 2** carries T7's runner and workflow, rebuilt with T7b's sandbox.

**Tried on a clean checkout of `ece37f7d6`:** both apply with `git am`, each tree as built: part 1 `033b9853dcae800effe6732a1b787d6956e89514`, part 2 `fdad7b18e6c873b095977a282536f323eefebf49`. T10 does not
wait on them. T8 and T9 follow on top; they are not in this send.

## Part 1: Review 88's findings on the landed code, and M61's

| item | where it is met |
|---|---|
| 1 symlinks | `rerun.py`: a decisive script, a control's script or an imported module with mode 120000 at the commit is refused |
| 2 `.gitattributes` | `rerun.py` `materialise`: the commit's files are written from their blobs (`ls-tree -r -z`, `cat-file --batch`); the decisive script's hash is checked on the file as written. A test commits `export-subst` |
| 3 the control's imports | `rerun.py` `_checks`: the control's script, and the modules beside it, are guarded as the decisive one |
| 4 the guard | refuses `_socket`, `_ssl`, `ctypes`, `multiprocessing`, `logging.handlers`, `importlib`, `exec`, `eval`, `compile`, any `__import__` (names, attributes, strings) and any change to `sys.path`. Not `subprocess`, for your wrapper (M65); the docstring says the namespace is the wall there. With no sandbox, no seat code runs and the card is HEAVY |
| 5 the filesystem | as nobody (`unshare -n -- setpriv --reuid=65534 ...`, under `sudo -n` on hosted runners), owning only its temporary directory. The wrap is trusted only once a probe inside it sees only the loopback and fails to write into a directory the runner owns. `unshare -rn` is gone: it cut the network, not the writes |
| 6 the slow control | a run whose lines or exit fail returns the card before the control runs |
| 7 HEAVY last | path, hash, symlinks, imports and both commands are checked first, for `.sage`, `.g`, `.gap` and sage imports too; `sage x.sage` and `gap x.g` are plain runs |
| 8 the code by branch | `discover.py` reads your `queue/SEAT_CODES.json`. A card on a branch not there, or under another branch's code, is not filed and its seat is told. The card's stated branch is where it was found, and its stated commit is an ancestor of that commit, with the same decisive script and control at both (M65's rule, not equality) |
| 9 main's alias | `queue_schema.py` `own_alias`: `main` on a card under main's code is that card's own seat |
| 10 the peer offer | REPRODUCED to AT_BANKING is gone. A card that decides nothing ends at NOT_BANKED, the runner's move, after PEERED or OFFERED |
| 11 deletions | `custody.py`: a card file or the log deleted along the queue's history is reported |
| 12 one card's path | discovery checks each record before filing it; a card that fails is told to its seat, and the others are filed |
| 13 the order | discovery reads main first. The banking queue's order is T9's |
| 14 the effect's code | `card_form.py`: every code the effect names is one the card touches. Arcs are not codes, so your B2011 card holds |
| 15 what decides | one table of codes, `card_form.codes`, read by the form and the record check: the scoreboard in any case, identification and register rows, the law map's rows ("LISTENING 26"), and the 19 by plural and common names |
| 16 the firewall | plurals, "compared to", "comparison with", "+/-", "agrees with experiment", "fitted to the data"; still a flag |
| 17 the sweep | the retraction sweep is loaded only where its registry stands; the title's words beyond six are listed as left out |
| 18 the form's paths | absolute and ".." paths are refused; "run as" must run the declared script; the control is compared with the decisive command as an argument list |
| 19 the vendor rule; strays | discovery's check holds the gate's vendor rule; `read_dir` and `read_ref` both report strays and folders |
| 20 strictness | `deciding` is `True`, `False` or `None`, never 0 or 1; `branch_ok` refuses "..", a leading "-" or "/" and empty parts; `at_ok` refuses a month 13 |
| 21 discovery's notes | a declared refile is linked and the note agrees (A8); a malformed title gets its own reason (A18); `ls-tree -z`, and a fenced title is reported (A19); seen versions keyed on branch, path and blob (C25); the old version of a refile is reported and, in part 2, not taken further (A24) |
| M66 the Pins and the codes | `discover.branches` reads the Pins table itself: a masked row (`origin/<v>/...`) is resolved on its mask, and a row whose branch names no `origin/` ref is kept and reported as unreadable, never dropped. `code_for` matches a masked key of `SEAT_CODES.json` (`<v>/<rest>`) on a branch of one segment more and the same rest, and refuses the card when two known branches match it |
| 22 `resolve` | a ref with no mask is read as written; a masked ref (`<v>`) matches only in its masked segment, and only when one ref matches |
| 23 `read_log` | a line of the wrong kind is reported and left out, never a crash; branch and path are checked |
| 24 custody's lock | the late sighting is tested on a history of two moves |
| 25 the normalisation's lock | the 13th digit is equal and the 12th is not |
| 26 the allowed list | `card_form.ALLOWED` is read from `ALLOWED_PACKAGES.json` |
| 27 the locks | WITHDRAWN and NOT_BANKED are final in the test; `BY_OTHER` is read; the network modules are tested by name; `--history` is tested on a queue's own history, where it fails |
| 28 the reader | a line outside any field is reported; the hypotheses may hold ";" |
| M61.1 the law map | in "deciding", by item 15's table |
| M61.2 D6 | a premise arc with its own card in the queue (a card of main's seat whose title opens with the arc, or whose file names it) is waited on until that card is VERIFIED |
| M60 definitions | already in the form as you landed it; kept |
| answered (C24, B21) | the seat-code check against the scoreboard stays, with a comment saying it cannot fire on a valid code |

## Part 2: T7's runner and workflow, with T7b

- **`scripts/queue/intake.py`:**
  - **Seat code** runs as nobody in a namespace (the rerun). Where no sandbox can be made, the round goes on and every
    rerun is HEAVY.
  - **The queue's folder** is read once. The round decides in memory, and writes only after every rerun. It writes
    nothing if the folder changed meanwhile, and it closes what it wrote with `.round_manifest.json`.
  - **`--check-manifest`** refuses a file the round did not write, a file missing, or a file changed after.
  - **A refiled card's old version** is not taken further.
- **`.github/workflows/intake.yml`:** the record job runs `--check-manifest` before the schema and log checks, then removes
  the manifest. The one tracked workflow path is as you accepted it in M62.
- **`queue/README.md`:** setting 6 now reads "the network guard: sudo unshare -n, as nobody". A new setting 7 covers the
  heavy rerun's PATH with python-flint (M65 point 6).
- **Your probe of M62, as a test:** a commit whose script prints its decisive lines and writes `{"status": "VERIFIED"}` into
  the queue's folder comes out REPRODUCED, and the folder is untouched.

## What is not tried, said plainly

- **The sandbox on a hosted runner.** Here the runner is root, so `unshare -n -- setpriv` works directly. On GitHub's runner
  it is `sudo -n`, and the first run's log will say which wrap was found. If neither works there, no seat code runs, and
  the log says so.
- **Your wrapper's child processes.** They run inside the same wrap. Because the guard does not read a script run that way,
  for those scripts the wall is the namespace and the user, as M65 says.

## Runs

- **The queue's test files:** 76 passed, a planted case for each item and for M66's two.
- **The second part's key rules, each removed once, each caught:**
  - the probe's write check;
  - the symlinked module;
  - the run's reasons before the control;
  - the no-sandbox HEAVY;
  - the changed folder;
  - the manifest;
  - the refiled card.

  Writing a symlink's blob as a plain file is not caught. It is an equivalent change: the mode is refused before anything
  runs.
- **Every gate on each part:** 58, all green but harvest-debt (`GATES.txt`).
- **The related test files** (the registries, the logs, the views, the tracked files, `.github`, the card and the seats' codes): 671 passed, 3 failed: B1306's slice D, the first entry of T10's list; harvest-debt's live run; and the day test, which passes alone.
