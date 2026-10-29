# The labels rule: main's weave-or-thread field on every W arc (2026-10-29)

This rule is committed before any label is set. It is a record-hygiene step for the Ledger Desk, not an arc. It changes
no result, no status and no prior, and it does not edit `docs/dossiers/the_weave_2026-10-07/NOTE.md`.

## The occasion

The proposal asked the owner two questions (`docs/workdesk/THE_LEDGER_DESK.md`, Decisions). The owner answered "if u
recomend ao" on 2026-10-29, ruling for this seat's recommendation. Reading main's schema showed that the first question
was half settled before it was asked. Main has carried `weave_or_thread` on every verdict file from B1491 on, under its
test for B1600, and all 198 of those files carry it. This seat's two B arcs from after the rule (B1548, B1552) carry it
too. B1549 and B1550 were sealed hours before the rule was adopted. The gap on the two branches the index reads is this
seat's 171 W arcs. They state their label in prose, when they state it, and the index found a machine-readable tag in
only 54 status rows.

## The field

Main's convention, unchanged: `weave_or_thread` is a string whose first word is `weave`, `thread` or `neither`,
optionally followed by a short parenthetical. `neither` always carries its reason, for example "neither (a reading)".

## The arcs

Every W id in NOTE's status table, each once: 171 arcs, none skipped. Arcs that predate the rule do not arise here,
since W1 opened the weave dossier on the day the rule was adopted.

## Where a label comes from, in this order

1. **The status row.** The row's status cell contains exactly one of "weave result" and "thread result".
2. **The arc's own paragraph in NOTE.** The paragraph in the arc's section that opens with a bold "Weave or thread".
3. **The arc's rule file.** The "Weave or thread" section of its `W###_RULE.md`.
4. **Assigned by this seat.** Only when none of 1 to 3 gives a label.

Sources 1 to 3 are copied, never inferred. A source gives a label when its answer opens with "Weave", "Weave-type" or
"A weave result" (weave), with "Thread" or "A thread result" (thread), or with "Neither" (neither). A qualifier the
record attaches in the same sentence, such as "on a chosen structure", is kept in the parenthetical. An answer that
opens any other way gives no label, and the next source is read.

Assignment (step 4) applies THE WEAVE's test (`docs/THE_WEAVE.md`) to the arc's section and rule:
- **weave:** all three conditions hold, or the state is selected by the joint action's own effective action under the
  2026-10-24 clause;
- **thread:** the claim is about one thread or covers of one thread;
- **neither:** anything else, with the reason. This covers a reading with no computation on threads, a check of another
  seat's arc (as main labels its own verification arcs, "neither (a verification of main's B…)"), a process arc, and a
  fit or comparison to data that defines no quantity by the joint action. An arc that checks another seat's arc and
  also extends it is labelled by its extension.

## What is never done

- A label is never taken from a keyword met in passing: a sentence that mentions "weave result" while discussing another
  arc gives nothing.
- The desk never assigns a label. Step 4 is this seat's reading, recorded as assigned, with its reason.
- When two sources disagree, the earlier source in the order wins and the arc is listed under `conflicts` with both
  quotes, for the owner and the other seats to see. Nothing is silently reconciled.

## The register

W_VERDICTS.json in the weave dossier, one entry per arc, holds:
- `id`;
- `verdict`, the status keyword copied from the row (W arcs use their own words, such as COMPUTED or READING, which
  are not main's verdict enum and are not mapped onto it);
- `weave_or_thread`;
- `source`: "status row", "NOTE.md:line", "W###_RULE.md:line", or "assigned";
- `quote`: the record's sentence, up to 200 characters, or for an assigned label the reason.

The script w_labels.py in docs/workdesk builds it and checks it. Copied labels are re-derived from their quoted
lines on every check; assigned ones are listed in the script itself, with their reasons. A test locks the register to
NOTE's table.

## What this seat expects

These are stated before the script exists:
- copied labels about 120, assigned about 50;
- conflicts: none, at 70%;
- among assigned labels, `neither` the most common, since the early verification and reading arcs are the ones without a
  stated label.

From now on every new W arc's record step sets its entry, and the test fails when an arc in NOTE's table has none.
