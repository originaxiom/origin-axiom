# The suite's five cases for the grade: what is expected, written before any run

*cld-advisor, 2026-11-11. Card C4 (WP-0.9, series 1). Committed with the plants, before the suite is run with them.*

The field does not exist on main: no gate reads a grade. So each case is expected **not caught** on main's head, and
each twin is expected to pass there for the same reason. On the series each case is expected caught by `arc-data`,
and each twin to pass.

| case | the plant | the twin, which must pass |
|---|---|---|
| PV33 | an arc the candidate runs on (B1612) is graded a theorem, and the evidence it names is its findings page | the same arc graded a theorem, naming its own lock |
| PV34 | a new arc with a grade that is not one of the five words | the same arc graded a process |
| PV35 | a new arc graded an exact computation, naming a script and a lock that are not in the commit | the same, with the script and a lock that can fail committed |
| PV36 | a new arc graded a numerical estimate, naming a script and no output | the same, naming the script and its committed output |
| PV37 | a new arc graded sealed cells held, with fourteen cells held of thirteen sealed | the same, with seven of thirteen |

How it could come out wrong: a twin may fail on the series because a new arc trips another class of the same gate
(a number with no folder, a duplicated id), which would mean the plant is wrong and not the mend. A twin may fail on
main's head for that reason too, and then the case could not be read on either commit.
