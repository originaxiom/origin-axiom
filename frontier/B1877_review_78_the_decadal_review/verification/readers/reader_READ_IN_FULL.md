# Review 78 — the readers' full read of B1861, B1862, B1863, B1865 and B1872 (seeded by the anchor 10641a1b2)

*Two independent readers, fresh-context subagents spawned by main and told to read skeptically: one read B1861 and
B1872, the other B1862, B1863 and B1865. Neither edited a tracked file, ran a test suite, or read any branch but main.
Their reports are reproduced below, after main's dispositions, with the local path of the working copy removed and
nothing else changed. Main verified every must-fix item at its source before applying it. All five arcs are main's
own, written in the two days before the review, so the readers' independence is the point.*

## The readers' verdicts

| arc | verdict | must-fix |
|---|---|---|
| B1861, the closure programme | HOLDS WITH NOTES | 4 |
| B1862, the audit's first corrections | **FAILS** | 3 |
| B1863, the append-only gate reads history | HOLDS WITH NOTES | 0 |
| B1865, the planted violations run on main | HOLDS WITH NOTES | 1 |
| B1872, all histories together | **FAILS** on one claim and one vacuous check | 2 |

**Ten must-fix findings. Main checked each at its source: all ten are right.** One more place of the same kind was
found by main's own sweep while checking (the register's row P-738).

## Must-fix, and main's disposition

| # | the reader's finding | main's check at the source | applied |
|---|---|---|---|
| 1 | B1872: "the twins come together" is a tautology; the twin (2,1) is twice the mark (1,3) modulo 5, so the check cannot fail | verified: 2·(1,3) = (2,1) modulo 5; a matrix that keeps ±v keeps ±2v by linearity. Main wrote that check and counted it as a fact | corrected where it stands (three places and the verdict line). The count that can fail replaces it: of the positive words to 12 letters 1 376 keep the eigenline as a set, 694 keep the mark and 682 carry it to its twin. **That changes main's answer to the web seat's third fork:** which twin is a convention; one twin or both is not (index 12 against 6) |
| 2 | B1872: "four histories that the charge reading allows" is false for two of the four by the arc's own predicate | verified: `is_charge_form` is True for L⁶R(LR)^k and False for LR⁶(LR)^k. The seat's word is "charge-invisible" | made precise and now computed: two are of the charge reading's word form, two are its image under the exchange of the letters, all four are a power of LR modulo 5. The index 12 stands |
| 3 | B1861: "38 inputs: 8 axioms, 8 bits, …" does not sum and is stale (9 bits, 46 items) | verified against `build_run.txt` | dated correction; the generated page now says "38 inputs … counted by kind they are 46 items"; a line of live counts in the findings is compared with the builder by the lock |
| 4 | B1861: the exit table of § 5b is stale (forcing argued 6 and admitted 2, against 2 with 3 one clause short, and 3) | verified | dated correction at the table and in the verdict line |
| 5 | B1861: "the relayed rulings are thirteen" is stale (17: 11 confirmed, 2 not, 4 asked) | verified | dated correction in the findings and the verdict line |
| 6 | B1861: "All are corrected" overclaims; one move was declined | verified at the first reader's report, finding 8 | corrected |
| 7 | B1862: "the lemma's sentence stands in B952's findings only" is false | verified: it stood without "commuting" in B952's verdict line, its results file and the requirements ledger | carried to all three; B1862 carries a dated correction; its lock now fails wherever an old form stands without the correction beside it, with a planted control |
| 8 | B1862: B1856's verdict line still opens with the old form of the premise; the correction is a bracket at the end | verified | a pointer now stands where the old form stands |
| 9 | B1862: B854's verdict block is still unscoped | verified: § 6 was scoped, the block at the top of the same file was not | scoped there |
| 10 | B1865: the title says seven caught; the arc's own note says six | verified | corrected at the title and in the verdict line |

**Carried the same day, because finding 8 is the fault the advisor seat's second re-audit had already named:** the
two cases under "the charge premise" are now stated where B1853, B1855, B1857 and the read-out rule's page use it
(P-772's item on the premise).

## Optional notes, and main's disposition

- **Applied:**
  - B1861: the reader listed fourteen refusals of the builder with no planted control. Main measured it on the
    commit before the review: of the builder's 72 refusals, 24 had never been issued by any test of its lock. All 77
    fire now. A new test runs every planting test with the builder recorded and fails if a refusal in the builder's
    source is never issued.
  - B1861: the test of the order asked only for the transitive "rests on", weaker than the rule it names. It now
    asks what the rule asks. A partly tautological equality is removed.
  - B1861: "refuses to write it in two cases" now says the builder has twenty rules.
  - B1872: the stabiliser's index was printed and not computed. It is computed.
  - B1872: "Nobody has shown it" (of closure under composition) carries a dated note pointing to B1875.
  - B1865: its test said it showed main's planted tests catch each violation; it checks that they exist by name. The
    docstring says so now, and the test also looks at the file the findings name for PV25.
  - B1862: its page now says that E8's lock reads a note back, and that the arc made a ninth change its verdict line
    does not list.
- **Recorded, not applied** (each is carried to the register row named):
  - B1863: two branches of the gate have no test (a deletion of the log; a rename of it), and the module's own
    list of waivers and its sentence are exercised only through an argument. The roll-up exception asks for a common
    suffix and does not check the text before the first dated heading, and it accepts any archive present at the
    commit, not only one added by it. These join the log's archives under P-772.
  - B1863: "1 512 earlier commits" is the count on the first-parent line; the page does not say so.
  - B1865: PV3 and PV4 are caught by the ledger gate; a reader would expect the sealed-file gate to be named.
  - B1865 against B1863: the script counts three gates as passing with no repository where the runner prints SKIP.
    The script reads the boolean and the runner the sentence. The page does not say so.
  - B1872: `scope.reach` is "general" for an arc most of whose counts are bounded at 12 letters. The index is a
    statement about the infinite group; the counts carry their bounds where they are quoted.

## What the readers did not check

Neither ran a test suite or an arc's long script; the fresh-clone suite of the review did. Neither read the seats'
relays, so reader A could not decide what the web seat means by the charge reading (main read the relay: finding 2).

---

## Reader A's report (B1861 and B1872)

All paths are under frontier/. I ran nothing except small read-only Python (B1872 words and counts) and greps. I did not run the arcs' scripts or tests.

## 1. Verdicts

- **B1861: HOLDS WITH NOTES.** The builder and its test machinery are sound. The prose, and the "[Added 2026-11-10 …]" tail of arc_verdict.json, carry stale hand-copied counts and one internal sum that does not add up.
- **B1872: FAILS on one claim and on a vacuous check.** The counts and the index 12 look reproducible. But one stated "fact" is a tautology, and one claim about "the charge reading" is contradicted by the arc's own `is_charge_form`.

## 2. MUST-FIX

### B1872-1. "The twins come together" is tautological, and its assertion cannot fail
- **Claim.**
  - `B1872_all_histories_together_the_exact_facts_verified/FINDINGS.md:39`: "**The twins come together** (F9). No history that keeps a line keeps it without its twin."
  - `:30` of FINDINGS adds "and every one of the 694 keeps the twin line too".
  - arc_verdict.json `claim_one_line` repeats it: "all 694 keep the twin line too … the twins come together."
- **Why it does not hold as a result.**
  - `verification/together_facts.py:10` and `:37-38` define the marked line as ±v0 with v0=(1,3), and the twin as ±(2,1).
  - The run (`together_facts_run.txt:1`) says "the line is +-(1, 3) and its twin +-(2, 1)".
  - (2,1) = 2·(1,3) mod 5, so the twin is a scalar multiple of v0.
  - Linearity gives M·v = ±v ⇒ M·(2v) = ±2v, so every matrix that keeps ±v keeps ±2v.
  - `keeps_twins` (together_facts.py:36) and the asserted `all(keeps_twins(...))` (:57), plus the test's `assert all(_keeps(_word(w), (2, 1)) ...)` (test file line 34), can never fail.
  - This is not an enumeration fact about the 694 words, and it is not a property of the allowed set.
  - It is also not what F9 is about. The bullet "No history that keeps a line keeps it without its twin" has nothing to do with the 694.
  - FINDINGS §3 builds on it: "The seat's third fork ('one twin or both as the mark')…".
  - "Together" is therefore a coordinate choice of ±v versus ±2v within one F5-line, not a derived coupling.
- **Command to decide.** This is read-only and reproduces my check:
  `nice -n 15 python3 -c "v=(1,3); print(tuple(2*x%5 for x in v))"`
  It prints (2,1). Then confirm in the test file that `_keeps(M,(2,1))` holds for every M with `_keeps(M,(1,3))`.

### B1872-2. "Four histories that the charge reading allows" is false for two of the four by the arc's own predicate
- **Claim.**
  - FINDINGS.md:28 (table F8): "four histories that the charge reading allows — L⁶R(LR)^k and LR⁶(LR)^k, k = 1, 2".
  - The same wording is in arc_verdict.json: "four histories the charge reading allows generate a subgroup of index 12".
  - FINDINGS:16-17 and :35 also rest on "the two readings … allow different words and generate one group".
- **Contradicting evidence.**
  - `is_charge_form` (together_facts.py:44-53) is the arc's only operationalisation of the "charge reading". It requires w = E(LR)^k with E ≡ ±1 mod 5.
  - I ran it on the four generators. Both LR⁶(LR)^k words return False:
    - LRRRRRRLR → False
    - LRRRRRRLRLR → False
    - LLLLLLRLR → True
    - LLLLLLRLRLR → True
  - The script header for F8 says "four charge-invisible histories" (together_facts.py:81). The FINDINGS says "allowed by the charge reading". These are different claims.
  - The script only asserts `keeps_line` for the four (:111), never `is_charge_form`.
  - So "generate one group" for the two readings is shown only for a mixed set. Two of the four words are not in the arc's `charge` list.
  - Whatever the relay means by "charge reading", this arc does not compute it for those two words.
- **Command to decide.** This is the same read-only check I ran:
  `cd frontier/B1872*/verification; nice -n 15 python3 - <<'E'\nsrc=open('together_facts.py').read().split('# ------------------------------------------------------------------ F8')[0]; exec(src)\nfor w in ['LLLLLLRLR','LLLLLLRLRLR','LRRRRRRLR','LRRRRRRLRLR']: print(w, is_charge_form(w))\nE`
  Check the relay `relays/CHAT1_TO_CC_2026-11-10_A_ALL_IN_WEAVE_FORM.md` @ a711bd189 for its own definition of the charge reading.

### B1861-1. Headline count sentence does not sum, and is stale against build_run.txt
- **Claim.**
  - `B1861_the_closure_programme/FINDINGS.md:17`: "Main's spine holds 38 inputs today, as the record lists them: 8 axioms, 8 bits, 16 discrete choices, 5 real numbers, 1 ansatz and 7 identifications."
  - FINDINGS.md:112: "38 choices as the record lists them, 45 items."
- **Contradicting evidence.**
  - `verification/build_run.txt` has `"bit": 9`, `"budget_items": 46`, `"independent_choices": 38`.
  - The test pins it: `test_b1861...py:365`: `assert st["budget"]["bit"] == 9 and st["budget_items"] == 46`.
  - 8+8+16+5+1+7 = 45, and the current count is 8+9+16+5+1+7 = 46. Neither is 38.
  - PROGRAMME.md:13 repeats the problem, in generated form: "holds 38 inputs … 8 axioms, 9 bits, …". The 38 counts budget entries (`len(S.INPUTS)`, build_programme.py `independent_choices=len(S.INPUTS)`), while the kinds sum to items, which is 46.
  - The page presents 38 as if it were the sum of the listed kinds.
- **Command to decide.** `python3 -B frontier/B1861_the_closure_programme/verification/build_programme.py | grep -A8 '"budget"'`
  Compare with `grep -n "bits" frontier/B1861*/FINDINGS.md`.

### B1861-2. FINDINGS §5b exit table is stale against the sealed run
- **Claim.** FINDINGS.md:145-146: "| forcing argued | 6 |", "| admitted | 2 |", and :154 (the correction note): "Of the six forcing arguments, main found three one clause short".
- **Contradicting evidence.**
  - `build_run.txt` has `"FORCING ARGUED": 2, "ONE CLAUSE SHORT": 3, "ADMITTED": 3` (PROGRAMME.md:101 agrees: FORCING ARGUED 2).
  - Both sets sum to 38, but the split differs: forcing 6 vs 2+3=5, admitted 2 vs 3.
  - The "[Corrected …]" bracket at FINDINGS.md:153 fixes only the "12 → 8" total and leaves the table rows uncorrected.
  - arc_verdict.json's tail repeats the stale split: "6 with a forcing argument, 2 admitted".
- **Command to decide.** `grep -n "FORCING ARGUED\|ADMITTED\|ONE CLAUSE" frontier/B1861*/verification/build_run.txt frontier/B1861*/PROGRAMME.md`

### B1861-3. Ruling counts stale
- **Claim.**
  - FINDINGS.md:160: "The relayed rulings are thirteen now".
  - arc_verdict.json: "the relayed rulings are thirteen, of which the owner confirmed eleven … two are asked."
- **Contradicting evidence.**
  - `build_run.txt` has `"relayed_rulings": 17, "rulings_confirmed_by_the_owner_to_main": 11, "rulings_not_confirmed": 2, "rulings_asked": 4`.
  - PROGRAMME.md:16 says "17 rulings … 4 more are asked".
  - The test pins 17 (test file :138, :141).
  - FINDINGS.md:164-166 says the two relayed after main asked were not confirmed, which is consistent with "2 not confirmed". It does not mention the four more.
  - "Thirteen" and "two are asked" are therefore stale in the findings and the verdict.
- **Command to decide.** `grep -n relayed_rulings frontier/B1861*/verification/build_run.txt`

### B1861-4. "All are corrected" overclaims
- **Claim.** FINDINGS.md:245-249: the first draft's thirteen faults, including "fifteen nodes sat in the wrong package … All are corrected."
- **Contradicting evidence.**
  - `verification/readers/reader_B1861.md:17` (finding 8): "thirteen accepted; one declined with the map's own edge as the reason … twelve nodes moved".
  - So 15 were reported, 13 accepted, 12 moved, and one was declined.
  - FINDINGS.md:7 also says "that reader's thirteen findings are applied". arc_verdict says "thirteen findings, each verified … and applied, one assignment declined" — that one is consistent. FINDINGS' "All are corrected" is not.
- **Command to decide.** `sed -n 17p frontier/B1861*/verification/readers/reader_B1861.md`

## 3. OPTIONAL notes

**B1861: refusal rules with no planted control** (test file `test_b1861_the_closure_programme.py`). I grepped the plants. Rules 1, 2 (partly), 3, 5, 6, 7, 8, 11, 12, 13 (partly), 14, 15, 16-20 are planted. These code paths exist but have no plant:
- Rule 4 ("a conditional result names no premise", build_programme.py ~line 330). No test string.
- Rule 5's "GIVEN holds an unknown id", "GIVEN names an unknown package" and "needs an unknown obligation".
- Rule 2's "ALSO names a node that is in no package" and "ALSO sends … to an unknown package".
- Rule 10: missing question, first, accept, owner; and a status outside the list. Only the "intent", "not a question" and DONE plants exist.
- Rule 9's "budget's joints are not the scoreboard's borrowed joints" has no direct plant. The kind-disagreement half is planted.
- Rule 13's "confirmed without owner's words/date" and "ruling marked not confirmed without words".
- Rule 8's "ANSATZ node not typed as an ansatz" (only the FITTED half is planted) and "unknown kind".
- Rule 12's "a state other than OPEN has no note" is planted, but only for "FIXED with no note".
- Rule 14's "a quoted word of the record is gone" is planted (MAIN_QUOTES). The "headline result not in the map" check is not.

**B1861: other points**
- Test line 78 checks `pk[b] in wp[...]["rests_on"]`, which is the transitive closure of needs plus given. The builder (rule 6) requires an ancestor in `needs` or a direct `given`. The test is weaker than the rule it names, so a transitive-given-only dependency would pass the test but not the builder. Probably benign.
- Test line 263 `sum(exits_by_kind.values()) == len(names) == independent_choices` is partly tautological, since `independent_choices = len(S.INPUTS)` and `names` is the same list. The first equality is not vacuous.
- The docstring lists 20 rules, but FINDINGS §1 says the builder "refuses to write it in two cases". A reader would take that as the full set.
- Rules 11, 13 and 14 read other seats' revisions. FINDINGS' last paragraph says the lock skips these when absent, and the test does (`SEATS`). I did not verify the pinned revisions exist in this clone. The build_run `not_checked_in_this_clone` is `[]`, so they were available at build time.
- FINDINGS §3 table: "Delivered here: for each choice, whether it is continuous or discrete, and its proposed elimination (the package that settles it)". The budget carries kinds, and the package column is "settled by", but nothing computes "continuous or discrete" except the typed kind. Wording only.
- Status labels: only WP-1.1 is DONE ("declared; GENESIS v1.5"), intent DECLARE, nodes POSTULATED/CHOSEN, so rule 10 holds. I found nothing in PROGRAMME.md that grades a source-"choice" item as "proved" or "forced". The "forced/proved" strings I grepped were in "Closed when" conditions or quoted ledger text ("forced up to the sign"), not asserted results. I did not read all 997 lines of PROGRAMME.md.
- arc_verdict `"verdict": "PROVED"` for a process arc. FINDINGS §8 itself says this is "the schema's only fit" and records WP-0.9 for it.

**B1872: other points**
- Scope. FINDINGS §2 table states "1 to 12 letters" and "2 to 12 letters", so counts are scoped. arc_verdict `scope.reach` is "general", which does not match the bounded 12-letter checks and level 5. The "general" label also covers the index-12 fact, which is a statement about an infinite group; that one is computed by coset enumeration and is not bounded.
- Hardcoded strings. In the run output, "the line's stabiliser has index 12 (it is the stabiliser mod 5, of order 10 in a group of order 120, up to sign)" is a printed constant (together_facts.py:115), not computed. The "order 10" half is computed in the following `g_plus` line. "Index 12 = whole stabiliser" needs the stabiliser's index. That is inferred (60/5 in PSL(2,5)) and not computed. Index 12 in the generated group plus containment in the stabiliser does imply equality, but only if the stabiliser's index is 12, which the code asserts as 12 without computing it.
- Test `test_the_sealed_run_and_the_findings_agree` (test file lines 79-85) checks substrings in the run file and four phrases in FINDINGS. It does not compare the numbers FINDINGS quotes with the run's. The FINDINGS numbers (694, 204, 330, 23, 120, 12) do match the run file by my reading.
- The test's index check (`test_the_index_in_the_modular_group`) is `importorskip`-guarded. Without sympy it is skipped.
- FINDINGS:22 says "The facts hold. All eleven reproduce on main." Only four are computed in this arc. The other seven are cited from B1868 and not recomputed here. The intro (line 7) says this correctly.
- FINDINGS:57 quotes "is not a world" from the record. I did not check that quote.
- F11's reading "one thread read from its two base points already keeps no line jointly" is shown only for LR and RL. `group([LR, RL])` has 120 elements, so no common line mod 5. That is for this one thread.
- FINDINGS:47-50 ("'One departure' and 'least' … Neither is closed under composition") and the claims about "single state" rely on B1875, which is later, and are not re-derived here. The §3 text says "Nobody has shown it", yet B1875 now shows it. The arc is dated before that, so no fault, but the text is stale.

## 4. Not checked / undecidable from reading
- I did not run any code. The counts (694, 204, 330, 23, index 12, 120) are taken from the sealed run file, and I verified only the F8 charge-form predicate and the twin tautology by small read-only Python. Command to decide the rest: `python3 -B frontier/B1872_all_histories_together_the_exact_facts_verified/verification/together_facts.py` and `python3 -m pytest -q frontier/B1872_*/verification/`. The B1861 equivalents are `build_programme.py` and its pytest, per its FINDINGS §Reproduce.
- I did not read the relay `relays/CHAT1_TO_CC_...ALL_IN_WEAVE_FORM.md`, so I cannot tell whether the "charge reading" admits LR⁶(LR)^k by some other criterion. It is the deciding source for B1872-2.
- I did not verify the pinned seat revisions, the B1858 NODES/EDGES contents, the 73 findings' states, or `programme_source.py` beyond the greps above.
- I did not check that PROGRAMME.md equals `render(B)`. The test does this, and the file mtime (00:27) is later than FINDINGS (23:17), which explains the drift.

---

## Reader B's report (B1862, B1863 and B1865)

Read-only review. I ran no tests and no git state-changing commands. Everything below comes from reading files plus a few grep/wc/git-log queries and one 8-row python read of B1847's table.

VERDICTS
- B1862: FAILS. Each correction is present at the place it targets, but the old wording still stands unmarked in other places, and FINDINGS asserts it does not.
- B1863: HOLDS WITH NOTES. The gate code matches FINDINGS in every branch I read. The notes are two untested "refused" cases the FINDINGS does not list, an untested claim, and a weak roll-up check.
- B1865: HOLDS WITH NOTES. The counts match the sealed output exactly. The headline and the arc's test have wording problems.

========== MUST-FIX ==========

1. [B1862] "The lemma's sentence stands in B952's findings only" is false.
Claim: frontier/B1862_the_audits_first_corrections/FINDINGS.md, "Seen first": `The lemma's sentence stands in B952's findings only.`
Contradicting evidence, each carrying the uncorrected lemma:
 - frontier/B952_gut_ledger_rank/arc_verdict.json line 5 (claim_one_line): `THE CENTRALIZER OF A SET OF SEMISIMPLE ELEMENTS CONTAINS A MAXIMAL TORUS AND THEREFORE HAS FULL RANK`. `grep -c B1862` on that file returns 0, so there is no correction note at all.
 - frontier/B952_gut_ledger_rank/results.json line 21: `"theorem": "the centralizer of a set of semisimple elements contains a maximal torus, hence has full rank; ...`
 - docs/GUT_REQUIREMENTS_LEDGER.md line 71: `> **The centralizer of a set of semisimple elements contains a maximal torus, hence has`
 - docs/views/VERDICT_LEDGER.md line 568 (generated from the verdict).
The FINDINGS.md correction (B952 lines 35-38) is real and says "COMMUTING". But B1862 corrected B854's and B1856's verdict lines and left B952's verdict line, results.json and the requirements ledger uncorrected.
Decide it with: `grep -rIn "semisimple elements contains a maximal torus" frontier docs | grep -v B1862`

2. [B1862] The old E3 wording still opens B1856's verdict line. The correction is only a bracket at the end.
Claim: B1862/FINDINGS.md table row E3 says the correction is in "B1856's findings (the sentence, and a third condition), its verdict line".
Evidence: frontier/B1856_charge_or_symmetry_at_five_verified/arc_verdict.json line 25 still begins `only +-I act as a scalar on both parity sectors (the charge premise = invisibility to every state)`. That is the equation B1862 says is false (E ≡ ±I = "invisible to every state"). The correction appears only as `[CORRECTED 2026-11-10 (B1862 ...): 'the charge premise = invisibility to every state' holds for E = +I only ...]` at the end of the same line. That is the "note at the end" pattern you asked me to flag. The generated VERDICT_LEDGER row 1081 reproduces it.
B1856/FINDINGS.md is correct at lines 16-26. Its line 33 `The run of 6 has E ≡ I mod 5: a scalar everywhere, so invisible to every state` is fine, since it is +I.
B1862 itself concedes the phrase stands in B1853, B1855, B1857 and the read-out rule page (see B1861 PROGRAMME.json line 741, "PARTLY FIXED"), but the B1862 title and row say "corrected".
Decide it with: `grep -n "invisibility to every state" frontier/B1856_charge_or_symmetry_at_five_verified/arc_verdict.json | cut -c1-200`

3. [B1862] B854's unscoped negative still stands as the headline verdict.
Claim: B1862/FINDINGS.md row E8: "B854's consequence ... read as general ... corrected in B854's findings (the sentence) and its verdict line".
Evidence: frontier/B854_centralizer_exact/FINDINGS.md line 17, in the VERDICT block: `> **There is no non-abelian continuous symmetry commuting with the holonomy's finite image inside E₆.**` There is no scope on it. The title on line 1, `the centralizer of 2T in 𝔢₆ is ABELIAN: u(1)⁴`, also has none. Only § 6 (line 109) and the claim_one_line carry the scoping note. The unscoped sentence is the more prominent one.
Decide it with: `sed -n 15,18p frontier/B854_centralizer_exact/FINDINGS.md`

4. [B1865] The headline says seven caught, and the arc's own later note says six.
Claim: frontier/B1865_the_planted_violations_run_on_main/FINDINGS.md line 1: `seven of twenty-one now caught, fourteen still pass`.
Evidence: the same file, "Disclosed": `One of its seven catches is an artefact of the instrument, as § 1 says. Main reports six.` The same section's "Added" note says the seat's re-audit reports 6 of 21 and corrects its shallow-clone test "under which that case is not caught". The sealed output (`verification/planted_violations_at_30dd1fea7_out.txt`) really does say `PV22 G13 CAUGHT ... full clone PASS, shallow clone PASS (ok)`, so "reported caught" is accurate. The unqualified title and the arc_verdict (`7 are reported caught`) are not. "Main reports six" contradicts the title.
Decide it with: `head -1 frontier/B1865_the_planted_violations_run_on_main/FINDINGS.md; grep -n "Main reports six" frontier/B1865_the_planted_violations_run_on_main/FINDINGS.md`

========== OPTIONAL NOTES ==========

B1862
- E6: FINDINGS says "The lock also runs the enumeration for another map and gets a different kernel". That check is in tests/test_b862_global_form.py (test_the_kernel_is_computed_from_the_map), not in B1862's own verification file. It also re-types the enumeration inline with a hand-copied loop and does not call `kernel_exact` on another map, so it shows nothing about the function. `kernel_exact` itself loops only over the centres (alpha in thirds, beta in halves) and q on a grid. That reduction is still derived by hand in its docstring, so "computed from the map" is partly true: the five phases are written by hand as `[(al-2q)%1]*3+[(be+3q)%1]*2`. The 3×2×n loop is explicit and the result is right.
- B1862's test: E3, E4, E8, E11, E13 and E6 each also assert that the corrected note string is present in the file. That is a string read-back. FINDINGS says each correction "has a lock that recomputes the corrected fact", which is true of the maths parts (the centralizer dimensions, the E3 split 338/305/643, the minimal polynomial, the eigenvalue multiplicities) but not of the E8 scope note (FINDINGS says "No computation"). No test asserts that the old wording is absent anywhere. That is why Must-fix 1-3 got through.
- B1862 has a ninth change, the tracked-deps gate (§ 2b). It is not in the arc_verdict claim_one_line list of eight, and its scope.object omits it. The CHANGELOG entry (commit message) does include it.
- B1847 and B567 corrections verified as stated. B1847's rise is on exactly 8 rows (`_rises` needs ≥8, and I confirmed 8 rows with Im τ rising 3.765 → 6.1446). B567 FINDINGS lines 20-24 and the lock (tests/test_b567_hamiltonian.py lines 7 and 61-65) are corrected, and "21 distinct" survives only inside the correction text.

B1863 (gate code: scripts/gates/gates.py lines 127-185, `append_only_problems` and `gate_append_only`)
- Branches, as read:
  - No repository: `rev-parse --git-dir` fails, so "cannot verify".
  - Root absent (shallow): "cannot verify ... shallow or partial".
  - HEAD does not descend from root: "cannot verify".
  - Deleted log: `deletes PROGRESS_LOG.md`. A rename of the log appears as a deletion at that commit and is flagged.
  - Waiver: skipped by full sha. The waiver map is empty (asserted in test_the_gate_is_green_on_this_repository).
- Not covered by any test in tests/test_append_only_history.py: the `deletes` branch and the log-rename case. Both are handled in code but untested. Neither is claimed "refused" in the FINDINGS tests table, so this is a gap rather than a false claim.
- Gaps in the tests that matter:
  - The waiver test passes a dict to the function. The module constant `APPEND_ONLY_WAIVED` and the "waived by name" output sentence are never exercised.
  - FINDINGS also says "the review tool's fresh clone counts a SKIP against the clone". That is implemented at scripts/review/review_tools.py:270-271 and no test in the suite exercises it. `grep -rn "SKIP" tests/` shows only the runner tests.
  - "It does not pass with nothing checked" holds for no repository, a shallow clone without the root, and an unrelated history. A shallow clone that holds the root but cuts history above it is untested.
- The roll-up exception is weak (`_rollup_ok`, lines 133-148). It only needs a non-empty common suffix. Text before the first "## 20" in the removed prefix is not required to be in the archive (`k = removed.find("## 20")`). The "archive" is every docs/progress/*.md at that commit, not files added in that commit, so a prefix already duplicated in an existing archive would pass. The FINDINGS describes it as "a roll-up, whose removed prefix must be found verbatim in that same commit's archives". Reasonably true, but the preamble is unchecked.
- If git is not installed, `subprocess.run(["git", ...])` raises, and nothing in the function catches it. The "fails closed" claim is tested for "not a repo", not for "no git binary".
- The runner's SKIP test keys on the words "skipped"/"unavailable"/"no review anchor" in a passing sentence (gates.py line ~2279). That is a text match.
- The test for "does not descend" uses `git checkout` inside its own tmp repo, which is safe.
- Counts: `1,512` earlier commits is right for `git log --first-parent f31729801 -- PROGRESS_LOG.md` (1512). Without `--first-parent` it is 1534. The FINDINGS wording ("commits that touched the log") is not qualified as first-parent.
- Consistency: the registered control (tests/GATE_CONTROLS.json) does name `test_the_gate_itself_fails_on_a_committed_deletion`, as claimed.

B1865
- The counts match the sealed output exactly:
  - 5 controls CAUGHT.
  - PV CAUGHT = PV1, PV2, PV3, PV4, PV6, PV8, PV22 (7).
  - PV NOT CAUGHT = PV9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 24 (14).
  - PV MANUAL = PV5, 7, 23, 25, 26, 27 (6).
  - 27 PV rows in all.
  - The group assignment (G5 ×5, G6, G7, G8, G9 ×2, G10 ×2, G14, L7) sums to 14. The "nine gates" in PV9 match the nine names in the output line.
- Its test (test_b1865...py) recomputes only counts by parsing the output text. It does not rerun the script, so FINDINGS' "holds the output" is accurate. FINDINGS does not say the test is a read-back.
- test_mains_own_planted_tests_exist_for_each_catch only greps for `def test_pv...` names in the test files. It does not show they pass, and the docstring ("that each violation it reports caught is caught by main's own planted tests too") overstates it. For PV25, FINDINGS says main automated it in tests/test_tracked_deps_locks.py. The test never checks that file, and that file has no test named for PV25 (nearest is `test_the_gate_fires_in_a_clean_checkout`).
- PV3 and PV4 are caught by `seal-ledger-current`. The output shows `seal-digests=PASS` and does not list `seal-immutable`, the gate B1864 introduced for exactly this. FINDINGS attributes both to "a gate that now does the work (B1864)". That is true of seal-ledger-current, which B1864 also changed, but a reader would expect seal-immutable.
- Apparent tension between B1863 and B1865: B1863's test says attribution, tracked-forbidden and log-changelog-paired print SKIP without a repository. B1865's PV9 line lists the same three under "gates that still PASS with no git". Probably the script reads the boolean and the runner reads the sentence. FINDINGS does not say so.
- The 2026-11-07 column of the table (21 not caught, 0 caught, main at `217e37c4f`) and the `c6c5f12e` script are not checkable here. relays/advisor_2026-11-10_audit/tools/ is not on main, which FINDINGS says. "24 undetected and 3 caught in part (B1861 § 6)" is quoted correctly from B1861/FINDINGS.md lines 181-182.

========== NOT CHECKED / UNDECIDABLE FROM READING ==========
- I did not run any test, so none of the new tests is shown to pass or to fail with the gate removed.
- The B1863 test that is claimed to fail without the fix: reading shows every table-listed test commits the violation and asserts on the function's result. I did not mutate the gate to confirm.
- I did not read the tracked-deps gate (§ 2b of B1862) beyond confirming `git check-ignore --no-index` is at gates.py line 635 and the `_plant` hook exists.
- I did not check the "three older locks' force-added files resolved to the repository's root" claim.
- I did not verify E4's sl(3) example beyond reading the test. A and B there are both diagonal and commute, so the test is consistent.
- I could not check the seat's script or its 2026-11-07 output (not on main).

Commands to decide the verdict-level issues:
- `python3 -m pytest -q tests/test_append_only_history.py` (B1863 tests; also run it with the gate neutered to confirm the planted tests fail)
- `grep -rIn "semisimple elements contains a maximal torus" frontier docs | grep -v B1862` (Must-fix 1)
- `python3 -c "import json;print(json.load(open('frontier/B1856_charge_or_symmetry_at_five_verified/arc_verdict.json'))['claim_one_line'][:200])"` (Must-fix 2)
