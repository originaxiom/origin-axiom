# The Ledger Desk (P-420, phase 1): a read-only desk over the record

A generated, static page over main's own files. It is ported from the SM seat's prototype (HARVEST_LEDGER rows 1471 and
1474), not merged from it: the scripts are adapted to read main, the page is a template with no data in it, and every
number on the page is computed by a script in this directory from the record at a named commit, except view E's
hand-copied table, which says so. The page is **not a result of the program**; it is a view of the record, and its data
change only when the record does.

## Rebuild

Everything below is read-only on the repository except `--land`, which writes `docs/workdesk/the_ledger_desk.html`.
Main does not commit that page (the ruling of 2026-10-29, D1): it is built on demand, and by the site's build at deploy
(DEPLOY.md). It is listed in .gitignore.

    python3 -B docs/workdesk/build_page.py --out DIR            # main's HEAD only (the default); writes DIR/index.html
    python3 -B docs/workdesk/build_page.py --out DIR --check    # the same, with the index built twice and compared
    python3 -B docs/workdesk/build_page.py --land               # writes the page into the checkout (not committed; D1)
    python3 -B docs/workdesk/build_page.py --seat-ref auto --out DIR   # also read the SM seat's branch, found by its name
    python3 -B docs/workdesk/build_index.py --out DIR --check   # the index alone: index.sqlite, index.json, manifest.json
    python3 -m pytest -q tests/test_workdesk_builds.py          # the locks on all of the above

`--out` must lie outside the repository or in a path git ignores. `--main-ref REF` reads another commit of main.
`--repo DIR` reads another checkout. The page opens from the file system; it needs no server and no network. The scripts
use the standard library only; `--seat-ref` needs Python 3.11.4 or later.

## Files

| file | what it is |
| --- | --- |
| `docs/workdesk/build_page.py` | builds the page: takes the template, embeds the data and the commits read |
| `docs/workdesk/build_index.py` | reads `frontier/*/arc_verdict.json` and `docs/RELAY_LEDGER.md` through git, resolves edges, writes the index and its manifest |
| `docs/workdesk/extract_desk_data.py` | reads the SM seat's weave dossier when it is given (the W views); empty on main, which holds none |
| `docs/workdesk/the_ledger_desk.template.html` | the page's markup and script, with no data; edited by hand |
| `docs/workdesk/the_ledger_desk.html` (not committed) | the generated page, built on demand; never edited by hand |
| `tests/test_workdesk_builds.py` | rebuilds the page into a temporary directory and locks the properties below |

## What each view is

Each view states what it reads. A label is copied from the record where the record states one and is shown as absent
where it does not; the desk assigns none. (Where the SM seat's branch is read, a label the seat assigned under its own
rule is marked as assigned.)

| view | question | reads | label and scope | cannot show |
| --- | --- | --- | --- | --- |
| A, the weave stage | which closed geodesics do the threads give, all at once? | nothing in the record: computed in the page from L and R (`GENESIS.md`, the core convention) | WEAVE (every primitive cyclic word in L, R with both letters, length at most n, none picked); a clicked thread is labelled THREAD | the sign of a thread; not a result |
| D, the tick walk | how does each thread act on the three parities at ticks 1 to 9? | computed in the page: the thread's matrix mod 2, raised to the tick | WEAVE; the counts beside the table are recomputed from the rows shown | |
| E, P-415's gauge chain | what has each frame said of each rung? | a **hand-copied** table, from the verdicts of B727, B1805 and B1812 | the table is not generated; above and below it, computed: P-415's disposition in the register, each cited arc's verdict now, its last commit, and whether it changed since the copy | frames nobody has tested (shown open) |
| F, the index | how many arcs, with what verdicts and labels, and which edges resolve? | verdict files, through git | counts by (seat, kind, verdict); labels by era; the manifest names the commit, the schema, each script's sha-256 and each table's rows and sha-256; targets not found are listed, never guessed | arcs without a verdict file |
| H, the board | what is open, and which relays wait? | verdict files (verdict OPEN) and `docs/RELAY_LEDGER.md` (rows whose first word is OPEN) | the weave-or-thread word; a relay is aged to the commit read; "the gate sees it" is the relay-debt gate's own row pattern, read from `scripts/checks/relay_debt.py` | a relay with no ledger row |
| I, the atlas | what rests on what, and what would be re-read if this fell? | `depends_on` and `rests_on_seat` of the verdict files | the verdict is the colour, the weave-or-thread word is the frame; a cone counts dependency, not truth | |
| B, C, G, and D's field list, E's plates | the SM seat's calibration, W-arc ledger, lifecycle strip and tower plates | the SM seat's weave dossier and commit subjects; only with `--seat-ref` | the seat's results, keyed `sm:`, never main's verdicts | |

## Keys, eras and labels

- An arc is keyed (seat, id): `main:B1816`. A number carried by several folders (B58) keys the later ones `main:B58#2`,
  `main:B58#3`; an edge that cites the bare number goes to the first. The SM seat's arcs, when read, are keyed `sm:`.
- The label is the first word of the verdict file's `weave_or_thread`. Main states it on every verdict file from B1491
  on ("after the rule"); earlier arcs carry none and are shown as before the rule, not as unlabelled.
- A first word that is none of weave, thread or neither is counted under "other label"; one missing after the rule under
  "none, after the rule".
- An edge target is resolved in the citing arc's own seat, then at main. A target that is a folder without a verdict file,
  or that is on no branch read, is listed in view F. `scripts/checks/arc_data.py` (gate `arc-data`) classes the
  `depends_on` cases among these as resolved, not defects; it reads `depends_on` only, so a `supersedes` target with no
  folder shows here and nowhere else. A seat id whose branch is not read is counted apart, as "seat branch not read".

## Provenance, determinism and what the page loads

- The page is a function of the commits read and of these scripts: everything is read through git, so uncommitted changes
  in the working tree are not seen.
- The manifest in view F names the commit read for each seat, the schema, the sha-256 of the scripts and of the template
  that built the page, and each table's rows and sha-256. `--check` builds the index twice and stops unless they agree.
- Every link goes to the file at the commit read. The links are navigation: the page loads nothing. It carries a
  content-security policy that refuses every external script, style, font, image and request, and its data is embedded
  with `<` escaped so that no record text can close the script.
- The page is public if it is published, as the repository is.

## Limits

- The generated page is a snapshot of the commit it names. It is not committed (D1); the site rebuilds it from each push.
- Views B, C and G, D's field list and E's plates need the SM seat's weave dossier, which main does not hold. They are
  absent from the default page, not empty.
- View E's table is typed by hand. Its freshness is checked; its content is not computed.
- Not built: a register board over `docs/POINT_REGISTER.md`, an identification matrix, the scoreboard of P-418, the
  scope fields (frame, object, reach) of the verdict files, and any figure plate beyond views A and D.
