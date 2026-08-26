# B8122 — constructive items

**Arc dated:** 2026-08-21 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

THREE OF THE FIVE CONSTRUCTIVE ITEMS VERIFIED AND ADOPTED, ONE DECLINED, ONE LEFT OPEN AND NAMED
-- AND THE TRIAGE CAUGHT A FALSE NEGATIVE OF MY OWN. E1: for any A in GL(2,Z) with det -1 and
trace m, det(A^2 - I) = chi_A(1) chi_A(-1) = -m^2 exactly, so the mapping torus of A^2 has
torsion m^2 and is a knot complement only at m=1, where h(5)=1 makes the class unique;
Selections I-III therefore select the golden across the WHOLE period-one locus and only
Selection IV needs the conjugacy class -- removing a concession the paper itself said a referee
would raise first. E2: the threshold the body declined to name is m=6, from PRIMITIVE class
counts 1,1,1,1,1,2,1,1,2,2,1 at discriminant m^2+4 -- and my first count was WRONG because it
included imprimitive forms, an error the scrutiny's own E4 observation (content is a
GL(2,Z)-invariant) identified; restricted to primitives the two counts agree exactly on m=1..11,
with a flagged residual disagreement at m=12 that is not load-bearing. E3: A_2+A_1's largest
mutually-orthogonal root set has size 2, verified in E6's actual 72-root system, so it contains
no 3A_1 and z(C) = sl_3 + t^4 -- closing the dimension-12 ambiguity exactly where it is used. E4
declined as cosmetic, though its observation repaired my own miscount. E5 NOT adopted and NOT
dismissed: it needs the stratification internals checked against B8078, which was not done. AND
THE PROCESS CATCH: my first triage grep reported E2 absent when it is present but HARD-WRAPPED
-- the same instrument failure this seat banked in R48/B8109, repeated by the seat that recorded
it; the second pass ran wrap-insensitively WITH A POSITIVE CONTROL. Verifies three constructive
claims independently and adopts them into the paper. The class-count table is computed for m <=
12 only, and the m=12 entry disagrees with the source and is flagged. E5 is untriaged. Gate 5
untouched.

## What the arc recorded

### `verdict`

THREE OF THE FIVE CONSTRUCTIVE ITEMS VERIFIED AND ADOPTED, ONE DECLINED, ONE LEFT OPEN AND NAMED
-- AND THE TRIAGE CAUGHT A FALSE NEGATIVE OF MY OWN. E1: for any A in GL(2,Z) with det -1 and
trace m, det(A^2 - I) = chi_A(1) chi_A(-1) = -m^2 exactly, so the mapping torus of A^2 has
torsion m^2 and is a knot complement only at m=1, where h(5)=1 makes the class unique;
Selections I-III therefore select the golden across the WHOLE period-one locus and only
Selection IV needs the conjugacy class -- removing a concession the paper itself said a referee
would raise first. E2: the threshold the body declined to name is m=6, from PRIMITIVE class
counts 1,1,1,1,1,2,1,1,2,2,1 at discriminant m^2+4 -- and my first count was WRONG because it
included imprimitive forms, an error the scrutiny's own E4 observation (content is a
GL(2,Z)-invariant) identified; restricted to primitives the two counts agree exactly on m=1..11,
with a flagged residual disagreement at m=12 that is not load-bearing. E3: A_2+A_1's largest
mutually-orthogonal root set has size 2, verified in E6's actual 72-root system, so it contains
no 3A_1 and z(C) = sl_3 + t^4 -- closing the dimension-12 ambiguity exactly where it is used. E4
declined as cosmetic, though its observation repaired my own miscount. E5 NOT adopted and NOT
dismissed: it needs the stratification internals checked against B8078, which was not done. AND
THE PROCESS CATCH: my first triage grep reported E2 absent when it is present but HARD-WRAPPED
-- the same instrument failure this seat banked in R48/B8109, repeated by the seat that recorded
it; the second pass ran wrap-insensitively WITH A POSITIVE CONTROL.

### `scope`

Verifies three constructive claims independently and adopts them into the paper. The class-count
table is computed for m <= 12 only, and the m=12 entry disagrees with the source and is flagged.
E5 is untriaged. Gate 5 untouched.

### `false_negative_self_caught`

My first triage grep reported E2 ABSENT. It is present, HARD-WRAPPED ('we do not' / newline /
'assert a threshold here'). That is the SAME instrument failure this seat banked in R48/B8109 --
a regex that cannot cross a hard wrap -- repeated by the seat that recorded it. Re-run wrap-
insensitively WITH A POSITIVE CONTROL, which is what made the second pass trustworthy.

## Depends on

`B8120`, `B8121`, `B8078`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
