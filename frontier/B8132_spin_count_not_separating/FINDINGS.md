# B8132 — spin count not separating

**Arc dated:** 2026-08-25 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

THE SPIN-STRUCTURE COUNT IS NOT A SEPARATING PROPERTY OF m004 -- FOUR OF FOURTEEN FAMILY MEMBERS
SHARE IT. B1141 assigns the last free discrete bit and states the spin lift's two-ness as
following from H_1 = Z. Computing H^1(M;Z/2) = Hom(H_1,Z/2) across B8128's shape-field family:
m004 gives 2, and so do m003 (Z/5+Z), m206 (Z/5+Z) and m207 (Z/3+Z/3+Z) -- because Hom(-,Z/2)
kills ODD torsion. The general condition is RANK 1 WITH ODD TORSION; m004 meets it by having no
torsion, which is SUFFICIENT BUT NOT NECESSARY. This is NOT a refutation: B1141's selection
rests on the beat, an exact 1-dimensional intertwiner space and norm-form positivity, none of
which this touches and all of which were re-derived two-bench with three engines. It corrects
the FRAMING -- 'since H_1 = Z' invites reading the two-ness as m004's own, and the count is a
family fact shared with three siblings. The selection may still be object-level; it does not
inherit that from the count. THE PAPER IS UNAFFECTED: it mentions spin structures zero times.
One elementary computation over B8128's 14-manifold family. Does not examine B1141's selection
mechanism, which is cc's and was hostile-verified two-bench. Gate 5 untouched.

## What the arc recorded

### `verdict`

THE SPIN-STRUCTURE COUNT IS NOT A SEPARATING PROPERTY OF m004 -- FOUR OF FOURTEEN FAMILY MEMBERS
SHARE IT. B1141 assigns the last free discrete bit and states the spin lift's two-ness as
following from H_1 = Z. Computing H^1(M;Z/2) = Hom(H_1,Z/2) across B8128's shape-field family:
m004 gives 2, and so do m003 (Z/5+Z), m206 (Z/5+Z) and m207 (Z/3+Z/3+Z) -- because Hom(-,Z/2)
kills ODD torsion. The general condition is RANK 1 WITH ODD TORSION; m004 meets it by having no
torsion, which is SUFFICIENT BUT NOT NECESSARY. This is NOT a refutation: B1141's selection
rests on the beat, an exact 1-dimensional intertwiner space and norm-form positivity, none of
which this touches and all of which were re-derived two-bench with three engines. It corrects
the FRAMING -- 'since H_1 = Z' invites reading the two-ness as m004's own, and the count is a
family fact shared with three siblings. The selection may still be object-level; it does not
inherit that from the count. THE PAPER IS UNAFFECTED: it mentions spin structures zero times.

### `scope`

One elementary computation over B8128's 14-manifold family. Does not examine B1141's selection
mechanism, which is cc's and was hostile-verified two-bench. Gate 5 untouched.

### `computation`

H^1(M;Z/2) = Hom(H_1,Z/2) by universal coefficients (H_0 = Z is free, so the Ext term vanishes),
and spin structures form a torsor over it, so the COUNT is |Hom(H_1,Z/2)|. A Z summand
contributes a factor 2; a Z/n summand contributes 2 iff n is EVEN.

### `context`

B1141 (memo 28) assigns the last free discrete bit -- the spin lift -- resting on
'H^1(M;Z/2)=Z/2 since H1=Z'. B8128's instrument applies directly.

### `finding`

THE SPIN-STRUCTURE COUNT DOES NOT SEPARATE m004. Four of the fourteen family members have
exactly two: m004 (H_1 = Z, no torsion), and m003, m206, m207 (rank 1 with ODD torsion, which
Hom(-,Z/2) kills). The general condition for exactly two spin structures is RANK 1 WITH ODD
TORSION -- m004 satisfies it by having no torsion at all, which is sufficient but not necessary.

### `what_this_is_and_is_not`

NOT a refutation of B1141. Its selection uses the beat, the exact 1-dimensional intertwiner
space and the norm-form positivity -- none of which this touches, and all of which cc re-derived
on their own bench with three engines. What this corrects is the FRAMING: 'since H_1 = Z' reads
as though the two-ness were m004's own, and it is not. The count is a family-level fact shared
with three siblings; the SELECTION may still be object-level, but it does not inherit that from
the count.

## Depends on

`B8128`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
