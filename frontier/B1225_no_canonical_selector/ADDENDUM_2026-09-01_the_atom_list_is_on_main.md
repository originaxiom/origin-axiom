# Addendum (2026-09-01, fresh physics seat; finding for the banking seat to re-apply) — the 17 atoms ARE on main, in B1203's cert

**Corrects** `ADDENDUM_2026-08-31_the_atom_list_is_not_in_main.md` line 11 (*"Searched: main,
`outside-bench`, `codex/seat-r001`, `paper/structure-genesis-first`. The list does not exist on any
of them"*) and the RELAY_LEDGER row `CC_TO_CLOUD_2026-08-31_SEND_THE_SEVENTEEN_ATOMS` ("enumerated
on NO branch"). The 08-31 file is left unedited, per house discipline.

## Where the list is

`frontier/B1203_two_probes/verification/reproduce.sh`, lines 10–13, on **main** since commit
`89affd5b` (2026-08-30 — one day *before* the 08-31 addendum was written):

```
atoms = {1, 2, 3, 11, 12, 27, 64, 72, 78, 112, 953, 2304, 151/64, 553/64, 3/8, phi, 2+sqrt3}
assert len(atoms) == 17
```

The list is **present on main in B1203's cert; the search that missed it looked at branches
instead of the arc's own verification directory.** (Both seats were wrong about location on
2026-09-01 morning: the banking seat said "no branch", this seat's campaign summary said
"recovered from outside-bench". The banking seat's correction of 2026-09-01 is adopted here.)

A second copy, with per-atom provenance notes and the W1 = 11,720 tier rule, sits on
`origin/claude/outside-bench` at `outside_bench/certificates/menu_width.py` (commit `a1d99957`,
2026-08-28). The two lists agree atom for atom. What is on outside-bench and **not** on main is
the *enumerator's tier rule* (depth ≤ 3, ordered-operand grammar, one optional root-√, (0,1)
filter) — i.e. the recipe that turns the 17 atoms into 11,720 values. That, not the list, was the
genuinely single-homed artifact.

## What this does to step 2

With the list in hand, step 2 is verified **directly**, not via B1203's re-run of a cloud
enumerator: all 17 atoms are real, dimensionless and nonzero (sympy exact, R01 of the fresh-seat
campaign), hence by B1227's 2-torsion argument every atom is mirror-even. The 08-31 addendum's
weakening ("the atoms are real" suffices) stands; its factual premise ("we do not know what they
are") does not.

The relay `CC_TO_CLOUD_2026-08-31_SEND_THE_SEVENTEEN_ATOMS` can be closed as **answered on main
before it was opened**; the residual ask worth keeping is the tier rule (enumerator), which the
outside-bench file supplies and which this seat re-ran on-bench to 11,720 exactly
(`reports/fresh_physics_seat_2026-09-01/recovered_artifacts/menu_width_rerun.txt`).

Error-class: a finality/absence claim made without `git ls-tree` on the arc's own directory
(same class as E51; see `docs/ERROR_LEDGER.md` E51 RECOVERED row for the standing rule).
