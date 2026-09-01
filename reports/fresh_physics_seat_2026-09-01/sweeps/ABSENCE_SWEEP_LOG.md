# ABSENCE SWEEP LOG — every "we don't have X" in the seat's reports, re-swept (2026-09-01)

**Governing rule (owner, 2026-09-01, verbatim):** *"one important rule: before you conclude we
dont have something, swipe the repo first"*.

**Procedure (`sweep_batch.sh` over `absence_claims.tsv`; raw evidence in `absence_sweep_raw.txt`,
2142 lines).** For each absence claim: (1) `git ls-remote --heads origin` → all 7 remote heads;
(2) per head, `git ls-tree -r --name-only <sha>` filtered by a filename regex, and
`git grep -I -l -E -i <content regex> <sha>` (this seat's own report directory excluded);
(3) `git log --all --diff-filter=D --name-only` filtered by the filename regex (deleted-file
history, all refs, 69 lines total); (4) a verdict that *quotes* the evidence. Heads swept:

| head | sha |
|---|---|
| main | a5138424 |
| audit/b775-braver-questions | 53da05f6 |
| claude/new-session-qor5up | 3851df2a |
| claude/outside-bench | d52bf025 |
| claude/physics-seat-evaluation-8dkbrl (this seat) | bda42afa |
| codex/seat-r001 | 9c2c2c9a |
| paper/structure-genesis-first | a31456d2 |

Verdict vocabulary: **STANDS** (absence confirmed on every head and in deleted history),
**NARROWED** (absent from main but present on another head, or a related-but-different artifact
exists — the claim survives with a scope clause), **CORRECTED** (the claim was wrong as stated;
a dated correction has been appended beside the original, original text untouched).

Ids are the seat's working numbering; gaps (A02, A08, A14, A15, A17, A18) are phrasings that
were merged into the rows below before the batch ran. One absence not in the batch — R3 P2, the
parent-keyed menus — was swept directly with `sweep_absence.sh` and resolved by a computation
(`p2_parent_menus_from_b869.py`); it is logged last.

**Tally: 15 batch rows + P2 = 16 claims → 9 STANDS · 4 NARROWED · 3 CORRECTED.**
Two of the three corrections and two of the narrowings are load-bearing for the seat's
findings (P2, V18/A04, A07, A21); none reverses a verdict, all change wording.

---

## A01 — "B994 has no committed generating script" (R1_REPORT l.85, l.226; R3 P3)
regex content `b994|rule_variation`, filename `b994|rule_variation`.
Per head: filename hits 3 on every head (FINDINGS.md, arc_verdict.json, results.json; 5 on this
seat = +2 addenda); no `.py`/`.sh`/`.sage` under `frontier/B994_*` on any head; content hits
25–50 per head are citations. Deleted history: 0.
**Verdict: STANDS.** The only solver in reach is B861's (`frontier/B861_fused_cascade`), and
B869's engine (see P2) — neither is keyed by B994's chains; B994's `results.json` remains
producer-less on every head.

## A03 — "B1148's certificates are not in the committed tree" (R3_REPORT l.100, l.292–293)
regex content `b1148|carrier_harvest`, filename same.
Per head: filename hits 0 on audit/b775, new-session, codex, paper; 5 on main and outside-bench
(FINDINGS, arc_verdict, b1148_results.json, verification/reproduce_new.sh, test). The
certificates themselves live only under `outside_bench/certificates/` on `claude/outside-bench`
(d52bf025; 100+ files there, e.g. `a2_glue64.py`, `b2_yukawa.py`, `menu_width.py`). Deleted: 0.
**Verdict: STANDS**, with a *new finding*: main's `verification/reproduce_new.sh` cites
`reproduce.log` and `our_uniqueness_chain.out` as its witnesses, and `.gitignore` ignores `*.log`
and `*.out` repo-wide — so the runner's own outputs cannot be committed as named. Recorded in
`frontier/B1148_carrier_harvest/ADDENDUM_2026-09-01_chain_conventions.md` (appended section).
Name collision to note: `our_uniqueness_chain` vs `frontier/B254_uniqueness_chain` (unrelated).

## A04 — "nothing committed enumerates cells or evaluates a forcing criterion" (R3 V18, l.272–274; B1011 addendum)
regex content `incoming enumeration|forced counts|992 `, filename `b1011`.
Per head: filename hits 10 (11 on this seat); content 35–39. On main
`frontier/B1011_mckay_tensor/b1011_cells.py` **does** enumerate the 2880 elements
(`enumerate_group(p)`, mod-61/241, `assert len(seen1)==len(seen2)==2880`); no file on any head
evaluates a forcing criterion on them (`992`/`284` appear only as literals in `b1011_match.py`
and the test). Deleted: 0.
**Verdict: NARROWED.** Corrected sentence (appended to
`frontier/B1011_mckay_tensor/ADDENDUM_2026-09-01_C5_lock_vacuity.md`, "## CORRECTION"): *the
enumeration exists (`b1011_cells.py`); nothing committed evaluates a forcing criterion on it, so
the 992/284 lock never touches the cells.* Same correction applies to R3_REPORT V18 (l.274),
appended there as a dated note.

## A05 — "`docs/CLAIMS.md` does not exist" (R3_REPORT l.368; B964 refile addendum)
regex content `adjoint higgs|supply a vev|supplies no vev`, filename `(^|/)CLAIMS\.md$`.
Per head: filename hits 3 on every head — root `CLAIMS.md` (231 lines),
`papers/P1_seam_form/CLAIMS.md`, `papers/P4_markov_stage/CLAIMS.md` (plus
`core/claims/{D4,P12,P15}.md` by directory); `docs/CLAIMS.md` on no head. Content hits 22–25,
none in any CLAIMS file (swept root CLAIMS.md for B964/B962/B952/B959/B960/VEV → 0).
Deleted: 0.
**Verdict: CORRECTED** (wording). The literal sentence was true but implied there is no claims
registry to patch; there is. Corrected sentence appended to
`frontier/B964_vev_correction/ADDENDUM_2026-09-01_PROPOSAL_refile_PROVED.md` ("## CORRECTION")
and to R3_REPORT as a dated note: *the claims registry is root `CLAIMS.md` + `core/claims/` +
the two paper CLAIMS files; none carries a B964/VEV row, so the refile touches none of them.*

## A06 — "the panel's rank-wall scan had no committed code" (R1_REPORT l.118, R07)
regex content `b955|rank.?wall|l133.?scout`, filename `b955|rank_wall|l133`.
Per head: `frontier/B955_l133_scout/`, `B956_l133_analysis/`, `B1079_wilson_menu/`,
`B952_gut_ledger_rank/` carry only FINDINGS/arc_verdict/results JSON on every head — no
`.py/.sage/.sh`. B1079's own `v` block states its checker ran against *"the prior session's
`e6_menu_*.py` files already sitting in this scratchpad"* — i.e. the scan code lived in a
scratchpad and was never committed. One related file exists on **audit/b775 only**:
`frontier/B796_coupling_campaign/h1_consumed/rank_wall_scope.py` — a *different* computation
(SnapPy: 3-rank of H₁ across m004's commensurability class, testing whether the knot-ness
argument is m004's or the class's), not the E₆ order-≤6 centralizer scan. Deleted: 0.
**Verdict: STANDS**, with the scope clause that `rank_wall_scope.py` (audit/b775) is a
committed class-scope probe of the same wall and should be cited when the wall is discussed.

## A07 — "the Yq = 0 clause is UNBANKED (in no committed file)" (R1_REPORT l.73; R03 FINDINGS l.78–81)
regex content `collapses to vector|Yq\s*=\s*0|Y_q\s*=\s*0`, filename `b1160|b1170`.
Per head: on **paper/structure-genesis-first only** (a31456d2), `frontier/B8143_anomaly_lane/`
(FINDINGS l.68–71, results.json l.48–50, step1_core.py l.8, 48) computes the third branch
*"{Yq = 0, Yd = −Yu, Yl = Ye = 0} ← a ONE-PARAMETER VECTOR-LIKE family"* and is the origin of
B1170's 252/222/2 counts; its relay claims the branch "= B864's third line". Checked B864 on
main: `results.json` `uniqueness.forced = [{b:0,c:0}]` in the ansatz Q = aY + bχ + cψ — **B864
has no third line**; the cross-reference is not borne out. Main/outside-bench filename hits (14)
are B1160/B1170's own files, none of which carries the branch (B1160 scale-fixes Yq = 1; B1170
drops the ray as "sterile"). Deleted: 0.
**Verdict: NARROWED.** Corrected sentence (appended to R1_REPORT and R03 FINDINGS): *unbanked
on main; computed on `paper/structure-genesis-first` in B8143 (never integrated), whose
"vector-like family" phrasing R03 refines (vector-like as a U(1) multiset; the full gauge
multiset is not literally vector-like, Q unpaired) and whose "= B864's third line" pointer does
not match B864's committed results.*

## A09 — "the W1 = 11,720 tier-rule enumerator is not committed" (R1_REPORT l.46, l.228, l.246)
regex content `11.?720|tier.?rule`, filename `b1225|selector|enumerat`.
Per head: filename hits 42–53 (the regex is broad); content hits on main restricted to machine
files: `frontier/B1227_one_theorem_two_regimes/two_regimes.py:49` — *"the atom LIST is cloud's;
only the count 11720 and 'all 17 real' were reproduced here"* — plus B1203/B1204/B1225
`reproduce.sh` lines that *state* the count. `outside_bench/certificates/menu_width.py` on
outside-bench (recorded earlier, internalization INDEX #34) is the enumerator; nothing on main
generates 11,720. Deleted: 0.
**Verdict: STANDS on main; NARROWED overall** (already so recorded in INDEX #34 — the
enumerator is branch-only on outside-bench). Nothing new.

## A10 — "`certify_yukawa_down_tail_cech_308.sage` is uncommitted" (T1 FINDINGS l.69, l.121; BATCH1_REPORT l.56)
regex content `cech_308|yukawa_down_tail|certify_yukawa|Φ.{0,20}44 coeff`, filename `\.sage$|cech|yukawa`.
Per head: no `.sage` file on any head; content hits (5–8 on main/outside-bench/codex/this seat,
0 on the other three) are the memos that *mention* the file
(`memos/YUKAWA_CUP_PRODUCTS_308.md`, B1212's copies, B1150/B1185 verification text). Deleted: 0.
**Verdict: STANDS.** The E51 debt is real on every head.

## A11 — "B1231's 61/52-candidate list is not committed" (01_MAP l.244–248; CAMPAIGN S9)
regex content `52 BARE|61 candidates|bare_identif`, filename `b1231|bare`.
Per head: B1231 exists only on main and this seat (4 files); no list artifact anywhere.
The *generator* is committed: `scripts/checks/identification_audit.py --extract/--triage`.
Re-run here on the current tree: **63 candidates / 3 map / 6 typed / 54 BARE**; the two
additions since B1231's own run are **B1231 and B1232 themselves** (both BARE by the tool's own
criterion), so 63 − 2 = **61** and 54 − 2 = **52** reproduce B1231's numbers exactly. Deleted: 0.
**Verdict: STANDS (list) — with the count reproduced from committed code.** Recommend the
list be committed as an artifact (`docs/IDENTIFICATION_CANDIDATES_<date>.json`) so Phase C can
be diffed against it.

## A12 — "S064 points at a file that does not exist" (S5_speculations_vs_bank l.122–123, flag 13)
regex content `S064`, filename `S064`.
Per head: filename hits 0 on all 7; content hits 4 on every head (`PROGRESS_LOG.md`,
`speculations/CATALOG.md`, `frontier/B571_day0_internalization/{BURIED_ITEMS.json,REPORT.md}`)
— all mentions, no file. Deleted: 0.
**Verdict: STANDS.** The phantom catalog entry is on every head.

## A13 — "B1217's cloud V-NEG headline is not reproducible as committed" (INDEX #22, stale-corrected by #34)
regex content `involves_regulator|V-NEG|vol_basis_extended`, filename `vol_basis|vneg|regulator`.
Per head: on outside-bench (and this seat, which carries copies under `recovered_artifacts/`):
`outside_bench/certificates/vol_basis_probe.py`, `outside_bench/outputs/vol_basis_probe_out.txt`,
`outside_bench/memos/VOL_BASIS_PROBE.md`, `outside_bench/seals/VOL_BASIS_PREREG.md`. On main:
only B1137 regulator-probe files and `B1198/.../regulator_checks.txt` — no vol_basis artifact.
**Deleted history: 2 hits** — `outside_bench/GOLDEN_EXCESS_IN_PROGRESS.md` and
`outside_bench/VOL_BASIS_RUN_IN_PROGRESS.md`, both deleted at 7ff41915 (2026-08-29, "Volume-
in-basis probe returns V-NEG: the corner is closed negatively") — in-progress memos replaced by
the certificate, not lost results.
**Verdict: NARROWED (as INDEX #34 already says): absent on main, committed on outside-bench.**
Nothing new beyond the deleted-history provenance, now recorded.

## A16 — "`basis_hygiene_check.py` is not committed in the arc dir" (R2_REPORT l.254, l.296)
regex content `basis_hygiene|384.?cell|96/H|100/H`, filename `basis_hygiene|b1137`.
Per head: filename hits are B1137's own files (13–14 on main/outside-bench/codex/this seat; 0 on
audit/b775, new-session, paper — B1137 postdates them); no `basis_hygiene*` file on any head.
Deleted: 0.
**Verdict: STANDS.** The hygiene certificate remains an owner action (cheap; PSLQ/LLL on 25
elements).

## A19 — "no test lock anywhere for B994" (R1_REPORT l.85, l.226)
regex content `test_b994`, filename `test_b994`. Per head: 0/0 on all 7. Deleted: 0.
**Verdict: STANDS.**

## A20 — "`docs/PROGRESS_LOG.md` does not exist (root `PROGRESS_LOG.md` is the log)" (S4a; owner's "both the one in main and in docs")
regex content `(^|/)docs/PROGRESS_LOG`, filename `docs/PROGRESS_LOG`.
Per head: 0/0 on all 7. **Deleted history: 2 hits** — `docs/PROGRESS_LOG.md` and
`docs/REVIEWS.md` deleted at 3145551d (B827). Their successors are
`docs/progress/PROGRESS_2026-Q2.md` and `docs/progress/REVIEWS.md` (present on main).
**Verdict: STANDS**, with the pointer: the owner's "the one in docs" = `docs/progress/`
(read in Phase B, W1).

## A21 — "C2's F3 test still does not exist" (S2b l.689, per the stamped note in `tests/test_b749_genesis_forks.py`)
regex content `F3 (lock|test)|test_.*_f3`, filename `_f3`.
Per head: the only `_f3` filename on every head is
`frontier/B651_wave3_integration/.../f3_twisted/PREREG_F3.md`. A direct filename sweep for
`c2_self|test_c2` finds **`tests/test_c2_self_selection.py` on `paper/structure-genesis-first`
only** (a31456d2; commits 87d56bae "C2 … had no executable lock; tests/test_c2_self_selection.py
supplies one, mutation-tested" and e99e2210 *"CORRECTION: 'C2 had no executable lock' was
OVERSTATED — partial coverage exists in B176 and B179; cc3 claimed absence without searching,
third instance today"*). Not on main. Deleted: 0.
**Verdict: NARROWED.** On main the stamped note is still true (no F3/C2 lock beyond the partial
B176/B179 coverage); on the paper branch an exact-arithmetic C2 lock exists and was never
integrated. **Precedent:** the paper branch's own e99e2210 is a prior instance of exactly the
error class the owner's rule targets, recorded by the record itself ("claimed absence without
searching, third instance today").

## P2 — "menus for parents SU(6)×SU(2), SU(3)³, Pati-Salam exist in no committed file" (R3_REPORT l.185, l.286)
Swept with `sweep_absence.sh 'pati.?salam|su\(6\).?x.?su\(2\)|su\(3\)\^3'` (all heads + deleted
history): no committed *output* keys a menu by these parents on any head; committed *code* does
generate them — `frontier/B869_false_positive_control/false_positive_control.py` (`all_descents`,
`SO_MENUS`, `descend_su`) on main. Ran that engine unmodified on the three parents
(`p2_parent_menus_from_b869.py`, output `p2_parent_menus_from_b869_output.txt`): SU(6)×SU(2) →
{SU(5)×SU(2)×U(1) 28, SU(4)×SU(2)²×U(1) 22, SU(3)²×SU(2)×U(1) 20, SU(6)×U(1) 36}; SU(3)³ →
{su(2)+su(3)+su(3)+u(1) 20 ×3} — **no Pati-Salam, no SU(5)×U(1) rung**; Pati-Salam×U(1) →
{su(3)+su(2)²+2u(1) 16, su(2)⁴+2u(1) 14 ✗, su(2)+su(4)+2u(1) 20 ×2}; all three cascade endpoints
su(2)+su(3)+3u(1).
**Verdict: CORRECTED.** Corrected wording (appended to
`frontier/B994_rule_variation/ADDENDUM_2026-09-01_witness_chain_and_provenance.md` §5 and to
R3_REPORT as a dated note): *the parent-keyed menus have a committed generator (B869) but were
never run for these parents and are in no committed output; B994 did not use them.* The
computation **strengthens D10** (B994's SU(3)³→SU(5)×U(1)/Pati-Salam rungs are not subgroup
descents) and supports B994's endpoint claim on a real subgroup basis. P3 (no generator for
B994's `results.json`) stands.

---

## What the sweep changed, and what it did not

- No verdict of the seat's reports reverses. Three sentences were wrong (P2, A05's implication,
  and the "nothing enumerates the cells" half of V18); four were true on main but false on
  another head (A07, A09, A13, A21). All seven now carry a dated correction beside the original.
- The class is real and recurrent in this record: the seat's own INDEX #34 (2026-09-01, earlier),
  and the paper branch's e99e2210 (cc3, "third instance today") are prior instances. This is the
  basis for proposing the rule to cc as an ERROR_LEDGER/PRACTICES row (relay
  `relays/FAB5_TO_CC_2026-09-01_reply.md` §9).
- Self-caught, same class, other direction: 23 of this seat's *own* R-cell run outputs
  (`*.out`, `*.log`) were never committed because `.gitignore` ignores those suffixes — the
  defect flagged against B1148's runner (A03). Fixed by committing `<name>.txt` twins (see
  `recompute/README.md`).
