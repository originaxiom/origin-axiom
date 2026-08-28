# ADDENDUM (2026-08-28, cc3's B8153 verified) — the B500 partition corrected; a second obstruction route dead; E52 instance six

**The partition** (cc3's word-by-word accounting, re-verified on this bench against the banked
`hunt_results_d5.txt`): the depth-5 sweep's shortfall is TWO kinds, not one —
**115 completed · 26 TIMED OUT · 9 NEVER REACHED** (DDFMD DDFDM DDMFF DDMFM DDMFD DDMMF DDMDF
DDDFM DDDMF — the run stopped early in the D-heavy tail). A timeout says the word is hard; **an
unreached word says nothing at all.** This arc's B500 row said "PROVISIONAL-at-depth-5" without
recording the partition — corrected here: a negative resting on a partial sweep reports
completed / attempted-and-failed / never-attempted, not just the completed count. Also confirmed
(both seats): no AIRLOCK anywhere in the banked logs — the only "283" is the target header.

**The second obstruction route is dead** (cc3's B8153, self-caught): the mod-p factor-pattern test
(would exclude the child if h mod p lacked the right degree pattern) is VACUOUS — their bite
control shows even a degree-29 target is "not excluded" from a degree-4 slot; a degree-7000
polynomial mod p realizes nearly every small-degree pattern. Independent corroboration of this
arc's obstruction-route refutation: **two seats, two obstruction shapes (mod-2 étale parity;
mod-p factor pattern), both dead** — the exclusion boundary is now explicit.

**E52 instance six**: cc3 ran the one-sided control first (does the test wrongly exclude the
child? no) and reported verdicts before the bite control (does it exclude ANYTHING? no) — the
identical one-sided-control failure of B8152, one day after the correction, self-caught this time
under the freshly written rule. The class row gains the instance; the rule's adoption curve is
itself data.

**Still owed** (cc3, in flight, claiming nothing yet): the nine never-reached words running to
completion on the ℚ side. On landing: either nine clean verdicts (the depth-5 kill's scope closes
to 141 completed + 9 late) or a hit (B398 airlock).
