# B1235 — THE TWO-SEAT HARVEST (2026-09-02)

**Verdict: PROVED** (every cell recomputed on this bench; nothing banked on a seat's word).
**Sources:** fab5cloud's rings R2/R3 (the physics-seat branch (`…/physics-seat-evaluation-8dkbrl`) @ 2ebdff8d, reply relay
FAB5_TO_CC_2026-09-01) and codex R034/R036 (`origin/codex/seat-r001` @ 4ec3e07f). Both seats work on their own
branches and merge main INTO them; nothing merges the other way (integrate-don't-merge). Every claim below carries the
seat that raised it and the cell that verified it here.

## THE PRIZE first

The family the paper leans on for its amphichirality story is **not** 83/83 amphichiral. It is **38/112**. The
headline theorem (m004 amphichiral, CS = 0, the arrow's ℤ/2) survives untouched; every *family-wide* strengthening
built on the census field falls, and the reason is a method the record had already flagged as unreliable in its own
reproducibility notes. That is E53's mechanism exactly — the assertion was pinned by a lock — and it is the second
instance of B1181's own one-way-family-test law. The harvest also turns codex's correct objection to B1234 into a
*positive* datum (A6's free deck lands on the CS = 0 stratum 40/40 against a 36 % base rate), reopens a relay loss
recorded as FINAL by exhibiting the nine files, and installs the owner's absence rule as an instrument.

## Cell 1 — the family is 38/112 amphichiral (fab5cloud D9/D5; recomputed)

`frontier/B1186_family_is_112/verification/family_census.py:96` decides amphichirality by
`M.is_isometric_to(W)` with `W` the mirror. SnapPy's isometry test is **orientation-blind**
(`REPRODUCIBILITY.md:73` says so in this repo's own words). So the field `amphichirality_failures = []` never tested
chirality at all, and B1181's "83 of 83 CLOSED" and B1163's ADDENDUM_family_denominator_B8147 ("5/5 by mirror-isometry")
inherited the blindness.

Proper test (`chirality_112.py`): `symmetry_group().is_amphicheiral()` on every member, CS recorded beside it.

| | count |
|---|---|
| members | 112 |
| amphichiral | **38** |
| chiral | **74** |
| chiral AND CS-silent (CS ∈ {0, ¼} mod ½) | **38** |
| B1224 violations (amphichiral with CS ∉ {0, ¼}) | 0 |

Named witnesses (the ones the B8147 addendum relied on): **o10_150700 chiral**, CS = −1/12, H₁ = ℤ, symmetry order 2
— the "83/83" killer. m202 and s118 chiral at CS = 1/12. t12840 (CS 0) and s955 (CS ¼) genuinely amphichiral. m004 and
m003 amphichiral. The 38 CS-silent chiral members are the population no CS-only screen can see, which is why B1224's
one-way law (amphichiral ⇒ CS ∈ {0, ¼}) was never going to catch this: it is the converse that was silently assumed.

**Consequences.** B1181 → RETRACTED (closure claim; its family-test law at LAW_MAP:263 stands — this is its second
instance). Its lock `tests/test_b1181_amphichirality_closure.py` pinned the string "83 of 83" AND asserted
`"is_isometric_to" in reproduce.sh` under the name `test_reproduce_uses_reliable_method` — the lock certified the
error. Re-pointed to pin the fact (38/112, RETRACTED, `is_amphicheiral`). Addenda beside B1163, B1186, B1181;
SPEC.md:306 and CAMPAIGN_STATUS:313 corrected by dated notes.

## Cell 2 — A6's free deck selects CS = 0 (codex R036 objection → recomputed → positive)

Codex: B1234's join "A6 ⇒ amphichiral ⇒ k-blind wall" skipped a step — amphichirality forces only CS ∈ {0, ¼}, and
the k-blind wall needs CS = 0. Correct. So the discriminating fact was computed (`a6_cover_cs.py`): the orientation
double covers of the first 40 non-orientable census manifolds **all** have CS = 0 (40 at 0, 0 at ¼), while among
amphichiral manifolds in general the ¼ class is common — 13/38 in the 112-family, 3/6 in the 200-census slice, 16/44
= 36 %. P(40/40 at zero by amphichirality alone) ≈ 0.64⁴⁰ ≈ 2 × 10⁻⁸. A6's free orientation-reversing deck selects
the CS = 0 stratum. **Data, not theorem** — registered as L194 (free deck ⇒ CS ≡ 0 mod ½?); `already_banked` finds
B605 (the involutions are free) and B1227 but not the implication. B1234 stands, its join now narrowed to what was
proved plus this datum; its slice is named (`NonorientableCuspedCensus[:40]`); the `same_trace_field` literal on line 71
is flagged in its addendum.

## Cell 3 — B1233 narrowed (codex R036; recomputed)

`origin_is_global_min` checked K(0) = −4 and Hessian 2I: a **local** statement. K(10,10,10) = −704. On the SU(2)
trace box [−2, 2]³ the origin IS the unique minimum, by the identity a² + b² + c² − abc = (a − b)² + c² + ab(2 − c)
with every term ≥ 0 on the box and equality only at the origin; critical locus = origin ∪ {(±2, ±2, ±2), sign product +1}
(five points). `markoff_box_minimum.py` checks the identity symbolically and 20 000 box points numerically. Also
withdrawn as a *principle*: "arithmetic cannot emit a continuum" (x² + y² = 1 has a real continuum); it stays as what
it was — an inventory of the corpus, no continuum among its emitted values. "Every checkable claim recomputed" was 14
booleans; said so in the addendum.

## Cell 4 — B994's exhibited chains are not subgroup chains; the endpoint survives (fab5cloud D10/P2; recomputed)

`B994_rule_variation/FINDINGS.md:27` shows `SU(3)³ → SU(5)×U(1) → SM` and `SU(3)³ → Pati-Salam → SM`. Impossible as
subgroup chains: a simple factor maps injectively or trivially, and dim su(4) = 15, dim su(5) = 24 exceed dim su(3) = 8.
B869's committed engine (`frontier/B869_false_positive_control/false_positive_control.py`, `all_descents`) run on the
three parents (`b994_parent_menus.py`): SU(3)³'s menu is `{su(2)+su(3)+su(3)+u(1)} × 3` — no PS, no SU(5) rung — and all
three parents cascade to `su(2) + su(3) + 3 u(1)`. The endpoint claim in B994 stands on a real subgroup basis; the
exhibited chains were rendering, not descent. Addendum beside B994 with the engine's output committed.

## Cell 5 — E51 reopened: the nine relays exist (fab5cloud E51; blobs verified)

The nine 2026-08-09 relays recorded as "UNRECOVERABLE — E51 closes FINAL" (RELAY_LEDGER:103, :114; rows 39–46
ESCALATED) sit at the root of `audit/b775-braver-questions` @ 53da05f6 — nine blobs, 88 060 bytes, sizes verified
here (`e51_manifest.json`; the branch carries 118 CC3_TO_CC_* files at that head). The FINAL verdict was an absence
claim made without sweeping the population it quantified over. That is the shape of the owner's 2026-09-01 rule,
and it is now (a) `WORKING_RULES.md` THE ABSENCE RULE, verbatim, (b) `scripts/checks/absence_sweep.py` — every
remote head, filenames and content, deleted-in-history, with planted controls — and (c) ERROR_LEDGER class **E54
ABSENCE-WITHOUT-SWEEP**, instances: RELAY_LEDGER rows 39–46, the paper branch's e99e2210 "missing" verdict, the seat
INDEX #34 entry, P2's "no engine" framing, and B1181's lock.

## Cell 6 — B1011's C5 lock was arithmetic on literals (fab5cloud V18/R26; recomputed)

`tests/test_b1011_mckay_tensor.py:58–59` asserted `8*120 + 24*2 − 8*2 == 992` — true of the integers, blind to the
tensor. The seat's `blind_forced_counts.py` enumerates the 2880 cells with stdlib only and returns 992/284 with the
control 1440 (a weaker criterion gives a different number, so the criterion is not vacuous). Re-run here (~30 s);
the lock now computes.

## Cell 7 — A03: the witness files were never committable

`.gitignore:20–21` ignores `*.log` and `*.out` repo-wide, so B1148's `reproduce.log` and `our_uniqueness_chain.out`
could not have been committed. Verified with `git check-ignore`. The fix is not to unignore the world; it is to
name witnesses with committable extensions. Addendum beside B1148 (its D11 convention claim — 6615→4→1 vs the full
tensor's 6615→9→1 — is seat-reported and **not** re-verified here; certs live on the `outside-bench` seat branch only).

## Cell 8 — ten A₂+A₁ sub-diagrams of E₆ (fab5cloud D12; recomputed)

Bourbaki E₆ edges {(1,3),(3,4),(4,5),(5,6),(2,4)}: an A₂+A₁ sub-diagram is an edge plus a vertex adjacent to neither
endpoint; 3+1+1+3+2 = **10**. The seat's claim that B1080's "six realizations" names five valid subsets is not
re-verified here beyond the count.

## Identifications (I-10, I-11; codex R034)

THE_ROAD prices "spin lift" as a physical observer bit; B1141/B1145 prove an internal odd-A₁/beat lift only. The
step "internal A₁ lift = physical 4d Lorentz spin" (I-10) and "boundary θ polarization = bulk/observer spin class"
(I-11; B1218 already records them NOT identified) are legacy UNEARNED identifications, registered now with the
baseline raised 3 → 5 by hand (`_baseline_raises`), the I-9 pattern.

## Held, not harvested

- Six main-lineage re-typings from the seat (THE_CLAIM regrade, README, THEOREM_LEDGER orientation re-typing,
  main.tex, TERMINALITY_SECTION_CANDIDATE, the T-election) — HELD until the owner confirms the election words the
  seat reports; a seat's report of an owner's words is not the owner's words.
- D11 (B1148's convention mix) — seat-reported; certs not on main.
- The seat's TERMINOLOGY RL/LR row IS harvested (same matrix [[2,1],[1,1]], A = LR as a word vs A₁ = RL as a matrix
  product; E23 hazard) — without the election annotation.
- Codex R035 (exact A1 SU(6) SM-shaped 27) — not yet read.

## Reproduce

`verification/reproduce.sh` — seven cells, two of them SnapPy (minutes), the rest seconds.
