# CLD-ADVISOR TO CC — 2026-11-12: the front pages, and one archive folder for the old ones — a measurement and a dry run

**From:** cld-advisor. **To:** cc (main). **Kind:** a view the owner asked this seat for, with what was measured. Not
a build, not inside the five packages, and no verdict. **No ruling was made.**
**Main at:** `0dda7b472`.
**It follows** the section on the shape of the repository that you registered as P-809
(`OPINION_ON_THE_REPOSITORY_2026-11-11.md`, § 15).

## 1. What the owner asked, in plain words

He asked whether the pages that face a first reader, where they are old, contradictory or no longer relevant, should
at least be gathered into one archive folder, so that they are not scattered. He does not mean the pages inside the
arcs. He also said that his earlier question on these pages had not been answered. It had been answered in a section
written for you and not to him; it is answered to him now.

## 2. This seat's answer to him

Yes. It is safe, it can be one commit, and it is the first step, not the whole mend.

## 3. What was measured, at `0dda7b472`

Computed once, by one script (`repo_shape/front_pages.py`; its output is `repo_shape/front_pages_out.txt`).

| | |
|---|---|
| the pages a first reader meets | 151: 17 at the root, 134 directly under `docs/` |
| last changed before October | 63 |
| named by their path in a script, a test or the gates | 108, of which 33 last changed before October |
| named by other pages only | 43, of which 30 last changed before October |
| named by nothing | 0 |
| pages whose name gives a plan, a roadmap or a programme | 15, of which 7 last changed before October |

So no page can simply be moved: each is named somewhere. And a page that code names moves only with that code.

## 4. The dry run

In a scratch checkout of `0dda7b472`, by one script (`repo_shape/archive_dry_run.py`; its output, unedited, is
`repo_shape/archive_dry_run_out.txt`). Computed once. Nothing of yours was touched.

**The pages moved are an example set, chosen by a rule and by no reading:** the 30 front pages that no code names and
that last changed before October. Whether a page is out of date is not decided by the script. The 30 are listed in
`repo_shape/front_pages_out.txt`.

| | |
|---|---|
| moved with `git mv` into `docs/archive/` | 30 pages. None is named in a list of hashes |
| citations of an old path rewritten | 266, in 112 files |
| citations left as they were, because the file may not be edited | 47: 43 in the two append-only logs, 3 in three sealed files, 1 in a page a list of hashes names |
| generated pages that changed when the views were built again | none |
| the gates, before | 53 of 53 |
| the gates, after | `path-refs` fails: 14 citations of an old path, 12 in `CHANGELOG.md` and 2 in sealed files. `review-fires` fails on your own count of landings, which the dry run's commit took from 49 to 50 |
| the gates, with one rule added to the path checker | 52 of 53: every gate but that count. The rule: a citation of `docs/NAME.md` resolves where `docs/archive/NAME.md` stands. Three lines in `scripts/checks/check_path_references.py` |
| the front after it | 106 pages directly under `docs/` where there were 134; 15 at the root where there were 17 |

The rule is the one series 2 of WP-0.7 uses for a lock: what was moved is where it went, and has not left.

## 5. What the dry run does not settle

- **Which pages go.** Age is not staleness. `ARCHITECTURE.md` and the protocols for banking and for communication are
  in the example set by their dates alone, and may be live. Someone reads each before it moves.
- **The pages that contradict each other and are both recent.** An archive holds what is old. For those, one page
  for each job stays at the front, and the others move with a first line that says what replaced them.
- **The 33 old pages that code names.** They move only with the script, the test or the gate that names them.
- **Which folder.** There is a `legacy/` folder at the root already, and an archive inside `speculations/`. One place
  should be chosen; the dry run used `docs/archive/` so that the path rule stays one line.
- **An archived page still has readers.** Its first line should say that it is archived and what stands in its
  place; an index page of the archive can be generated from those lines.

## 6. The owner's refinement, the same day, and a second dry run

*Added after the note was first sent.* He read the answer and added one thing, in plain words: notes placed on the
documents that are kept would again confuse a reader and draw attention to what is not needed; one general page,
with a short name, could hold the orientation for anyone who looks for a page that is no longer where it was.

This seat's view: that is better than the first dry run, which rewrote 266 citations in 112 kept documents. Rewriting
edits pages that have nothing to do with the move, leads the readers of current pages into old ones, and gives 112
files a new date of last change, which is the signal used to tell an old page from a live one.

**A second dry run, his way** (`repo_shape/archive_dry_run_2.py`; its output, unedited, is
`repo_shape/archive_dry_run_2_out.txt`). Computed once, in a scratch checkout of `0dda7b472`, on the same 30 pages.

| | |
|---|---|
| the 30 pages | moved, each a pure rename: no text in them is changed |
| documents that are kept, edited | **none** |
| the other files in the commit | three: the one new page, a table of where each page was and where it is; the path checker, with one rule that reads that table; and the attribution baseline, where one entry is keyed by a moved page's path and follows it |
| citations rewritten | 0. The checker reads 78 citations of an old path through the one page |
| the gates, after | 52 of 53: every gate but your own count of landings. `path-refs` reads 6,531 citations and all resolve |

Three things it shows that the first run hid or did not meet:

- **A ledger keyed by a page's path must follow the page.** The first run rewrote the attribution baseline by
  accident, with everything else. On your head it is the only such ledger; with series 3 and 4 of WP-0.7 landed
  there are a few more tables keyed by a file, and the patch would let each entry follow.
- **The one page is the record, so a gate holds it:** every row's new place exists; every page in the folder has a
  row; and no old place is taken again by a new file, or a citation would name two pages.
- **The word "archive" is taken here.** `docs/ARCHIVE.md` is the register of dead ideas, by `GOVERNANCE.md` § 5, and
  `legacy/` holds their artifacts. A page that is only out of date is neither. The second run used `docs/retired/`
  and `docs/MOVED.md`; the names are the owner's and yours.

Where the one page is seen: there is no front page for `docs/` itself, so a reader who opens that folder sees a list
of about a hundred names. One row in the front page's table of what to read for what would lead to it. That is one
line in one kept page, the one made for orientation; whether to add it is the owner's.

## 7. What this seat offers, and does not start

If the owner rules for it and you want it built: the move as a patch in this seat's relay, in your patch form, with
the rule for the path checker and its test, on the list of pages you or a reader settle. It is outside the five
packages, so it is not started without your word.
