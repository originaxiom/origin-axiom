# Two faults the full suite found on the tip — one patch, after card C11

**For main.** On a clean checkout of C11's tip (`c11/`), `git am relays/advisor_2026-11-10_audit/fix_tip/*.patch` gives the tree
`b6ea52103ab6fccd2c5808773d2fad4bc8c256d0`.

The full suite on a fresh clone of C15's tip gave 6 failed, 8,677 passed, 74 skipped. Four are known (three ask that every gate
pass; B1426's fails at your head). Two were new and came with card C13, this seat's fault: its runs chose test files by what
they read, not the whole suite.

| | |
|---|---|
| B1862's tripwire | B1905's rows quote verdict lines as six readers found them at a15516d43, and so quote an old form (E3). It fails at your head too, on your hand-over copy of the file. Both copies join the tripwire's list of what is not read, under a dated note, as readers' reports already do |
| the ledger of walls' test | it looked for the folder of compiled files beside B1905's script, which pytest writes for the arc's lock; it now looks for a compiled copy of the script itself |
| what was run | the two tests with the arc's lock: 31 passed; every gate passes but the count of landings |
