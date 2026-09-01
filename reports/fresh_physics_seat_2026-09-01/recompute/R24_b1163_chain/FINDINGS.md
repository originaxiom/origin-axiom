# R24 — B1163 w0 attempt chain: audit under corrected amphichirality

**Verdict: DISCREPANCY (addendum chain) / MATCH (headline).** The B1163 headline (w0 = an object-canonical
orientation of m004, which m004 — amphichiral, CS=0 — cannot supply) SURVIVES. Every *family-wide* statement
built on the mirror-isometry census FALLS; the chain's later "83-of-83 CLOSED" step (B8147 addendum) is a
second instance of the same vacuous instrument and falls with it.

## Blind-first record

Read before computing: FINDINGS.md lines 1–30 (headline + "one obstruction three ways") and
`ADDENDUM_family_wide.md` in full (to get the four named members). Read after computing: rest of FINDINGS.md,
`ADDENDUM_2026-09-01_amphichirality_instrument.md`, `ADDENDUM_family_denominator_B8147.md`,
`ADDENDUM_orientation_theorem.md`, `arc_verdict.json`, `verification/reproduce.sh` (grep for amphich).

Own scripts/outputs in this dir: `recompute.py` -> `recompute.out`; `control.out`; `b8147_spot.out`.
Instrument: SnapPy, `M.symmetry_group().is_amphicheiral()`; CS via `float(M.chern_simons()) mod 1/2`.

## Recomputed inputs (diff table)

| member | banked (addendum) | blind instrument (reverse+is_isometric_to) | orientation-aware | CS mod 1/2 | banked row |
|---|---|---|---|---|---|
| m004 | amphichiral True | True | **True** | 0 | MATCH |
| m003 | amphichiral True | True | **True** | 1/4 | MATCH |
| m202 | amphichiral True | True | **False (chiral)** | 1/12 | DISCREPANCY |
| s118 | amphichiral True | True | **False (chiral)** | 1/12 | DISCREPANCY |
| o10_150700 | "spot-verified 5/5" (B8147 addendum) | True | **False (chiral)** | 5/12 | DISCREPANCY |
| t12840 | "spot-verified 5/5" | True | True | 0 | MATCH |
| s955 | "spot-verified 5/5" | True | True | 1/4 | MATCH |

Planted-positive control (`control.out`): known-chiral m015, m016 -> blind instrument True, aware False. The
blind instrument returns True on chiral input; the banked 4/14 and 5/5 spot-checks could not have failed ->
VACUITY of the banked checks, and DISCREPANCY on 3 of 7 named rows. Consistency: every aware-amphichiral
member has CS in {0, 1/4} (the only classes with CS = -CS mod 1/2); every chiral one does not. 12*CS integral.

## Dependent claims, one by one

| # | claim (where) | depends on | recomputed input | status |
|---|---|---|---|---|
| 1 | "all fourteen Q(sqrt-3) census manifolds are amphichiral" (family_wide) | family census | m202, s118 chiral | **FALLS** |
| 2 | "amphichirality is the most-shared invariant of the family" | 14/14 | 2 of 4 named members fall; 2026-09-01 addendum counts 6/14 | **FALLS** |
| 3 | "H1=Z shared with none; m004 unique knot complement" | homology only | m003 Z/5+Z, m202 Z+Z, s118 Z/2+Z, m004 Z | UNAFFECTED (not an amphichirality statement; 14-wide not re-verified here) |
| 4 | "Robust — no sibling escape: orientation fixed identically (amphichiral) for all fourteen" | 14/14 | m202, s118 chiral: siblings whose mirror is NOT an automorphism exist | **FALLS** as stated. A chiral sibling still does not *supply* an embedding Q(sqrt-3)->C (the Galois/analytic legs do not use amphichirality), so "no sibling self-orients" may be re-derivable from the arithmetic route alone — but the banked argument is gone. |
| 5 | "Correctly typed as family-level: any canonical datum must route through H1, not orientation, which the family fixes for all" | 14/14 | same | **FALLS** |
| 6 | "route (a) closes because m004 is amphichiral (mirror knot = same knot)" | m004 only | m004 aware True, CS=0 | SURVIVES |
| 7 | "meditation §A now family-wide: observer supplies orientation generically" | 14/14 | falls with 1 | **FALLS** as family-wide; survives for m004 |
| 8 | B8147 addendum: "83 of 83, zero exceptions; spot-verified 5/5 by mirror-isometry incl. o10_150700, t12840, s955" | mirror-isometry instrument | o10_150700 chiral (CS 5/12); seat's corrected count 38/112 | **FALLS** (same vacuous instrument; "CLOSED" reverts to open with a negative answer) |
| 9 | B8147 addendum: "core theorem untouched — the mirror-parity argument never used the family" | m004 only | m004 amphichiral | SURVIVES |
| 10 | Orientation-theorem addendum: D4 amphicheiral symmetry group of m004 => no canonical datum orients m004 | m004 only | aware True (D4 order not re-verified, out of scope) | SURVIVES; its closing "family-wide" parenthetical inherits the fall of 1 |
| 11 | FINDINGS headline geometric leg: "m004 is amphichiral (Re V(u0)=0, CS=0 exactly)" | m004 only | CS = 0.0, aware True | **MATCH** |
| 12 | FINDINGS §A: "the object is amphichiral: it cannot pick +Vol" | m004 only | same | SURVIVES |
| 13 | arc_verdict.json claim line | m004 only; family not mentioned | same | UNAFFECTED |
| 14 | `verification/reproduce.sh` line 20 prints "m004 amphichiral" | print statement only | not a computation | VACUITY of that line (asserts, does not test); the fact itself is true |

## B1163's own headline

Header claim: w0 is not constructed; the single missing datum is an object-canonical orientation / archimedean
embedding of m004, refused because the object is Galois-symmetric (V4 free orbit), analytically two-valued
({+Vol,-Vol}), and amphichiral (CS=0). The amphichirality leg is per-member (m004) and is confirmed under the
orientation-aware instrument. **The headline is not touched.** What is touched is only the strengthening
layer: "family-wide" (14/14 -> false; 83/83 -> false), the "no-sibling-escape via amphichirality" argument,
and the "family fixes orientation identically" typing.

## Notes

- `ADDENDUM_2026-09-01_amphichirality_instrument.md` already withdraws rows of family_wide; this cell adds
  that the B8147 "83-of-83 CLOSED" addendum is also invalid (its 5/5 spot-check used the same blind instrument
  and one of its three named witnesses, o10_150700, is chiral), and that the residual "no sibling escape"
  statement needs re-argument from the arithmetic route if it is to be kept.
- Gate 5: no measured values used. Nothing outside this cell dir was modified.
