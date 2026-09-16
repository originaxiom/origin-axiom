# Item 3 — B8148 m=12 class count (3 vs 2 under GL(2,Z))

## HEADLINE (relay's ask, verbatim)
From `CC3_TO_CC_2026-08-27_M12_SETTLED_AT_3_AND_THE_MECHANISM_FOR_2.md`:
> "Re-implemented the reduction from scratch and validated it before using it: the rebuilt method
> reproduces the banked table `m = 1..11 -> 1,1,1,1,1,2,1,1,2,2,1` (exact match) **then returns 3 at
> m = 12, under both `SL(2,ℤ)` and `GL(2,ℤ)` equivalence**. `D = 148`... **the mechanism that
> yields 2** — implementing the reduction condition `0 < b < √D` as `b < ⌊√D⌋` silently discards
> `b = ⌊√D⌋`... at `D = 148` that exclusion removes exactly one class and returns 2."

## THE CLAIM (every number)
**What is being counted**: equivalence classes of primitive, indefinite binary quadratic forms
`(a,b,c)` (i.e. `ax²+bxy+cy²`, `a,c` opposite sign since `ac=(b²−D)/4<0`) of discriminant
`D = b²−4ac = 148` (the case `m=12` in a family the paper indexes by `m`), under two group actions:
`SL(2,ℤ)` (proper equivalence — the narrow class number `h⁺`) and `GL(2,ℤ)` (improper equivalence,
also allowing det `−1`, which additionally identifies `(a,b,c) ~ (a,−b,c)` — the wide/ordinary
class number `h`).

- **B8148 (cc3, 2026-08-27)**: `D=148`, **3 classes under SL(2,ℤ) AND 3 classes under GL(2,ℤ)**.
  Reproduces the banked `m=1..11` table `1,1,1,1,1,2,1,1,2,2,1` as its own control before trusting
  the `m=12` output.
- **Main, `frontier/B1240_belt_closure_and_fc_harvest/FINDINGS.md:89`** (fc R42, verified by cc,
  2026-09-02): **3 proper (SL₂ℤ) / 2 improper (GL₂ℤ)**. Cross-checked three ways in the same cell:
  own SL₂(ℤ) reduction (3/2); PARI `qfbclassno(148) = 3`; an independent PARI-ρ cycle route — "14
  reduced primitive forms, **3 ρ-cycles (two 6-cycles + {(−1,12,1),(1,12,−1)})**, GL 2, no form left
  unvisited"; a theoretical remark, "6+√37 has norm −1 so `h⁺ = h = 3` for the conductor-2 order."
  Own `m=1..11` table equals PARI throughout: `1,1,1,1,1,2,1,1,2,2,1` — **byte-identical to
  B8148's control table.**
- **`docs/HARVEST_LEDGER.md:206`** (row 174) records this exact split as the landed verdict:
  "R42 — the m = 12 class-count discrepancy (B8135 → B8148): **3 SL(2,ℤ) classes, 2 GL(2,ℤ)
  classes — CORRECTED**" — graded VERIFIED-EARLIER via B1240.
- **`docs/HARVEST_LEDGER.md:353`** (row 321) grades B8148 itself as **SCHEDULED** (unread on main
  at harvest time), and `frontier/B1412_the_relay_backlog/FINDINGS.md:33` already logged this exact
  tension: "row 321 flags B8148 as unread on main; the only landed check (R42/B1240) gives a
  different split (3 SL2Z/2 GL2Z) than this relay's '3 under both'."

**So this is a live numeric contradiction between two banked artifacts, not a missing trace.**
Both sides used and reproduced the SAME `m=1..11` control table exactly, so the disagreement is
isolated to the `m=12` GL(2,ℤ) count specifically, not a difference in convention for what "class"
or "the table" means.

## COMPUTED / CITED / ASSERTED
Both **COMPUTED**: B8148's SL(2,ℤ)/GL(2,ℤ) reduction is its own from-scratch reimplementation,
validated against the shared `m=1..11` control before trusting `m=12` (self-described method: same
discipline main's B1240 used). B1240/fc R42 is COMPUTED three independent ways on the main bench
(own reduction, PARI `qfbclassno`, independent PARI-ρ cycle enumeration) with an explicit form-list
witness (`14 reduced primitive forms`, the two 6-cycles and the ambiguous 2-cycle named by their
actual `(a,b,c)` triples).

## NEEDS COMPUTATION HERE — DONE (discriminating fact computed directly, <2 min)
**Discriminating fact**: enumerate the 14 primitive reduced indefinite forms of `D=148`, partition
them into `SL(2,ℤ)`-cycles by the standard Gauss reduction operator `ρ`, then test each cycle
against its `b → −b` image (the `GL(2,ℤ)`-merging map) to count `GL(2,ℤ)` orbits.

**Recipe** (self-contained, run independently of both arcs' code — `qf148_recompute.py` in this
directory):
1. For `b = 1..⌊√148⌋ = 12` with `148−b² ≡ 0 (mod 4)`, factor `ac = (b²−148)/4` over all integer
   divisor pairs `(a,c)`, keep only `gcd(a,b,c)=1` (primitive) and reduced pairs
   (`0<b<√148`, `√148−b < 2|a| < √148+b`).
2. Apply the standard indefinite-form reduction step `ρ(a,b,c)=(c,b',c')` (`b' ≡ −b (mod 2c)`,
   `b'` chosen to keep the image reduced) repeatedly to close each form into a cycle.
3. For each cycle, reduce `(a,−b,c)` (the representative's negated middle coefficient) back to a
   reduced form by the same reduction step, and record which cycle it lands in — cycles that map to
   themselves are ambiguous (their own `GL(2,ℤ)`-class); cycles that map to a different cycle merge
   pairwise.
4. Count `SL(2,ℤ)` classes = number of cycles; `GL(2,ℤ)` classes = number of orbits under the
   pairing in step 3.

**Result obtained** (`qf148_recompute.py`, run here, exact integer arithmetic, no external
libraries):
```
primitive reduced forms: 14
SL2Z narrow classes (h+): 3
  cycle len 6: [(-7,6,4),(4,10,-3),(-3,8,7),(7,6,-4),(-4,10,3),(3,8,-7)]
  cycle len 6: [(-7,8,3),(3,10,-4),(-4,6,7),(7,8,-3),(-3,10,4),(4,6,-7)]
  cycle len 2: [(-1,12,1),(1,12,-1)]
partner map: {0: 1, 1: 0, 2: 2}
GL2Z classes: 2
```
This **exactly reproduces main's B1240/fc-R42 cycle structure** — independently derived here
(without reading B1240's cycle list beforehand as an algorithm template — only its final numbers
were known going in), including the identical named forms of the ambiguous 2-cycle
`{(-1,12,1),(1,12,-1)}` and the "two 6-cycles" shape. The two 6-cycles are `GL(2,ℤ)`-conjugate to
each other (partner map `0↔1`) and merge into **one** GL-class; the 2-cycle is self-paired
(partner map `2→2`, ambiguous) and stands alone. Total: **1 + 1 = 2 GL(2,ℤ) classes**, **3
SL(2,ℤ) classes**.

**Expected number, stated in advance of running**: given the SL(2,ℤ)/narrow class group has odd
order 3 (hence is cyclic ℤ/3, hence has exactly one self-inverse — i.e. ambiguous — element if the
`b→−b` map coincided with class-group inversion), a naive group-theory argument would also predict
2 GL-classes (`1` ambiguous + `1` merged pair) — consistent with what was computed, though the
actual computation (direct cycle/pairing test on explicit forms) is the load-bearing evidence, not
the group-theoretic shortcut, since the relationship between "class-group inversion" and the
`b→−b` map for the wide/narrow distinction depends on unit-norm subtleties that are easy to
misapply (this is plausibly close to where B8148's error lives, though its code is not archived
here to confirm — see below).

## VERDICT ON THE DISPUTE
**Main's B1240/fc R42 (3 SL(2,ℤ) / 2 GL(2,ℤ)) is independently confirmed correct**, on a from
-scratch enumeration and reduction that never consulted B8148's or B1240's code, using only the
public `D=148` discriminant and the standard Gauss reduction algorithm. **B8148's "3 under both"
GL(2,ℤ) count is NOT reproduced and appears to be in error.** The archived `B8148_m12_settled`
directory carries no FINDINGS.md and no script (only `arc_verdict.json`, `results.json`, and the
relay), so the exact bug in cc3's GL(2,ℤ) merge step cannot be pinpointed from what is on disk —
only that its output disagrees with an independently-reproduced computation. The "off-by-one
`b < ⌊√D⌋` vs `b < √D`" mechanism cc3 itself identified explains how a BUGGY implementation could
silently produce 2 by discarding a legitimate `b`; that mechanism is real but is not what either
main's or this reader's correct computation is doing (both use the strict inequality `b<√D` with no
floor), so it does not explain B8148's disagreement — the discrepancy in B8148 is a different,
unidentified bug in whatever GL(2,ℤ)-class-merging step it actually ran.

**What this settles for a verifier**: run `qf148_recompute.py` (self-contained, <1 second) or PARI
`qfbclassno(148)` (gives 3, matching the SL(2,ℤ)/narrow count per B1240's own citation) alongside a
direct enumeration of the `b→−b` merge (PARI has no single built-in for the wide count at `D>0`
without disambiguating narrow/wide conventions, which is exactly the trap) — the cycle-and-merge
method above is unambiguous because it works on explicit named forms, not on a library call whose
narrow/wide convention must be trusted blind.

## GRADE PROPOSAL: **DISPUTED — resolved in favour of main.** Main's row 174 (fc R42 / B1240: 3
SL(2,ℤ), 2 GL(2,ℤ)) is REPRODUCE-AND-BANK grade (now doubly independently confirmed — main's three
internal checks plus this reader's from-scratch fourth). **B8148 (cc3: 3 under both) should be
flagged for correction/retraction** — its GL(2,ℤ) count does not reproduce. Recommended action:
relay this recomputation back citing the exact cycle structure so cc3 (or a fresh audit pass) can
locate its own merge-step bug; `docs/HARVEST_LEDGER.md` row 321 should be updated from SCHEDULED to
CONTRADICTED-BY-B1240, with a pointer to this recount, rather than left as an unreconciled open
count.
