# B1870 — The audit's backlog, reproduced on main

*Main, 2026-11-10 (S306o). The advisor seat's audit holds 73 findings. Its own rule, and main's: each is reproduced
on main before anything is banked or fixed on its strength. After B1862 to B1865, 34 findings had been reproduced by
nobody on main, and 12 by a reader only. The owner approved one multi-agent run for this backlog ("yes — on your
multi agent advice"). This arc is that run and main's own repeat of it. Bookkeeping only: no physical value is
computed and nothing is compared with measurement. 0 of 19.*

## 1. The answer first

- **The audit is right about main, almost everywhere.** Of the 34 findings, main's own re-runs confirm 24 as the
  audit states them and 9 in part. One could not be checked without a computation that belongs behind a sealed card,
  and stays open.
- **Seven more move from "a reader reproduced it" to "main reproduced it".** They are the findings whose planted
  violations main ran itself in B1865.
- **So the state of the 73 is now:** 9 fixed, 13 partly fixed, 45 reproduced by main, 5 by a reader only, 1 open.
  Before this arc: 9, 11, 7, 12, 34.
- **Nothing is fixed here.** Reproducing a defect is not repairing it. Each finding keeps its package in the
  programme, and each report carries the smallest fix and the test that would prove it.
- **The audit's own wording is stale or wrong in a number of details,** listed in § 4. None changes a finding's
  substance except one: a script the audit says fails does not fail.

## 2. How it was done

- **Eight read-only checkers,** one per class of finding, on the cheaper model tier the owner's standing rule sets.
  Each was told to find the finding in the audit, decide whether it is true on main today, and return the exact
  commands that show it. They were forbidden to edit, to commit, to copy the repository, to open the targets file,
  to read the masked lanes, to compute any physical value or to compare anything with data.
- **They are readers.** A checker's verdict is not a result on main. Main re-ran all 167 of their commands itself,
  after screening every command for anything that writes, and read each output against the checker's claim. A state
  changed only on main's own re-run.
- **One checker declined a finding,** correctly: deciding it needs a computation on the nulls of a comparison with
  data. That finding stays open, with the reason.
- **The reports are kept** (`verification/checkers_reports.json`): for each finding the commands, the files, what
  in the audit's wording is stale, the smallest fix, and the acceptance test. `verification/rerun.py` runs the
  commands again, read-only, and says which print what they printed today.

## 3. The 34, one line each

| | what the audit says | on main | what main's own re-run shows |
|---|---|---|---|
| E12 | five small slips of scope | PARTLY FIXED | Of its five slips, B1853's margins are corrected (B1855's dated note, Review 77). Left: B1857 is marked post hoc and still says 'exactly the two cheaper'; B1852's count of four reversing involutions carries its window and no note that the count is the window's; B884's control is printed and unused; B915's pre-registration still says no other measured number enters, against its own addendum |
| G11 | the currency check prints 'current' beside declared debts | REPRODUCED | The currency check prints 'ok (18 living documents current)' while 9 documents are declared debts and 8 of those are counted as current; CLAIMS.md lags 580 arcs under a tolerance of 40. The audit's 569 and 8 are 580 and 9 today |
| G12 | the gates at push are an honour system | REPRODUCED | README.md:71 says the gates run on every push; the hook is local and untracked, and the one CI workflow runs core tests and no gate |
| L1 | about a quarter of PROVED arcs are guarded only by locks that read text | REPRODUCED | No lock declares whether it recomputes, re-runs or reads a transcript, and no gate asks. A rough static count finds about 330 of 1518 lock files with no computing import; the audit's census tools are not on main and its 386 was not re-derived |
| L2 | 'locks assert mathematics' has no gate | REPRODUCED | The rule that locks assert mathematics has no row in PRACTICES.md and no gate; the vacuity gate fails only the no-assert and tautology classes and reports the both-literal class without failing it |
| L3 | the theorem chain's locks are mostly weaker than their links | REPRODUCED | In part. The chain-locks gate checks only that each link cites a test file that exists. Of the audit's two examples, C45's lock hard-codes its inputs and C7's last assertion is literal-only; but C7's lock also recomputes its three discriminants, and C45 is a no-go link, not a theorem |
| L8 | three depended-on arcs hold no computation of their headline | REPRODUCED | B892's tower scripts were never tracked (its wall scan is); B952 has a results file that its lock reads back and no script; B866's lock compares two literal cubics and its interpolation script is not tracked |
| M2 | the forcing theorem forces a matrix, not the manifold | REPRODUCED | In part. The two pages do not list the four further inputs and still call the collapse of 144 to 1 the content of the forcing; but both carry the banner that GENESIS is canonical, and the uniqueness page says it forces the matrix, conditionally. 'The object forced up to orientation' stands on THE_CLAIM.md:15 |
| M4 | a physics statement under 'no physics statement appears below' | REPRODUCED | THEOREM_LEDGER.md says no physics statement appears below, and its link C51, labelled a theorem, says a cover 'carries the Standard-Model gauge algebra and three complete generations'; unchanged since the audit |
| M5 | 'the flavour three is derived' against an unearned identification | REPRODUCED | 'the flavour three is derived' stands in GENESIS.md (line 456 today) and THE_WEAVE.md:113 with no pointer to the identification it rests on (I-31, unearned) |
| M6 | the global form called derived and not standard in a paper draft | REPRODUCED | In part. The paper's main.tex already says the derivation is standard and only the selection is not; its SPEC.md:115 still lists the global form 'derived rather than assumed' under what is not standard |
| M7 | B1855's titles say proved for a step main did not re-run | REPRODUCED | B1855's title says the run of 6 is 'proved least' though main re-ran neither of the seat's two lemmas (P-741, queued), and its claim line says 'every lcm(S) >= 12' without the range of S that its scope field carries |
| M8 | B1850's verbatim quotes mostly quote the row's own title | REPRODUCED | B1850 says every quote was found verbatim, 313 of 313; its checker tests only that a quote is a substring of the file named. The audit's 76 of 86 was not re-derived |
| M9 | an internal review called external in the paper folders | REPRODUCED | Papers/P3_THE_PAPER/EXTERNAL_REVIEW_2026-09-09.md is titled an external review, and 'outside referee' stands in two paper READMEs, against PROVENANCE § 0; the pretense gate scans docs and top-level pages only and lists neither phrase |
| M10 | the falsifier register cannot contradict the programme | REPRODUCED | In part. Two entries say a failure kills the reading and not the weave, and the eight first rows do not say what a failure would contradict; but 'most entries cannot fire' overstates: by the register's own grades it is 3 or 4 of 11 |
| M11 | a generated page asserts false universals | REPRODUCED | The reviewer page's sentence 'Every PROVED arc names its test locks' is a fixed string in the generator; on main 421 of 1079 PROVED arcs name no test file in their findings |
| P1 | the front door describes a plan that already ran and failed | REPRODUCED | THE_PROGRAMME_SO_FAR.md gives the six at their best figure and the final attack's two steps in the future tense, and names none of B1823, B1825, B1838; the plan carries one dated note, for B1823. The audit's claim about README is stale: README gives no outcome |
| P3 | an endpoint correction did not reach five arcs | REPRODUCED | B892 carries the correction (its 14-dimensional algebra is not the Standard Model's); B861, B862, B863 and B1028 carry no pointer to it, and B994's table still says its chains end at the Standard Model |
| P4 | a voided prediction and a stale significance on living pages | REPRODUCED | CLAIMS.md:147 still states the comparison without the adjudication that voided it as a held-out confirmation; B723 is still PROVED with no supersession; a withdrawn figure of sigmas stands on at least eight current pages |
| P6 | the index lists stale documents as living | REPRODUCED | INDEX.md lists CLAIMS.md as living while CLAIMS.md says it was last updated on 2026-07-04; CAMPAIGN_STATUS.md has 606 paragraphs that begin LATEST; one living entry is a path that does not exist |
| P7 | stale counts and duplicate arc ids | REPRODUCED | The forcedness check prints 53 of 57 while '39 of 43' stands as current on at least seven pages; the law map's banner says 113 rows against 329; two arc ids are each shared by more than one folder (1570 verdict files, 1567 ids) |
| R2 | the pinned environment is prose, not a lock file | REPRODUCED | The pinned versions are a prose table in REPRODUCIBILITY.md; requirements.txt and pyproject.toml carry lower bounds only; no lock file is tracked, and CI installs unpinned |
| V1 | every specificity null has an unpriced window | OPEN, not checked | Not checked, and why (B1870): the audit's figure has no tracked source, and deciding it needs a computation on the nulls that belongs behind a sealed card. Main's checker found that the later nulls take the best over 223 apexes and 266 lines and not over a plain grid, so the audit does not say which null it measured |
| V2 | the headline fits omit their error floor | REPRODUCED | In part. The allowance of ten per cent is in the compare scripts, is defined in TERMINOLOGY.md:763 and is priced in the framing ledger; the headline figures in THE_FINAL_ATTACK and THE_PROGRAMME_SO_FAR are quoted without it. The audit's two large figures have no tracked source and were not recomputed |
| V3 | evidence lives in an ignored directory | REPRODUCED | Audit/ is ignored and holds no tracked file; the register cites it on 83 lines and 68 findings files cite it; one calibration figure quoted on tracked pages rests on scripts that exist only there, and no tracked line says so |
| V5 | three looks missing from the look ledger; two conventions in one pipeline | REPRODUCED | In part. The look ledger has no row for B1658, B1659 or B1724. Only B1658 clearly reads seen data, by its own findings; B1659 says it uses none; B1724 re-reads earlier calibrations. Two error bars for one quantity stand on record |
| W2 | the quantifier of most claims is not machine-readable | REPRODUCED | 250 of 1570 verdict files carry weave_or_thread and 287 a scope; no gate requires either |
| W3 | 'the object' still names one thread in the terminology | REPRODUCED | TERMINOLOGY.md:11 defines 'the object' as the figure-eight complement, while GENESIS's fork on the family as object is ruled to the word states; the two do not agree on the default noun |
| W4 | no truncation is recorded | REPRODUCED | No verdict file has a field for a truncation, a range or a domain (27 distinct keys, none of them); the truncation ledger exists only as a planned item |
| W5 | six findings of this audit are of the same class | PARTLY FIXED | Of its six instances, four now carry dated scope notes (B854, B997, B1855, B1853; by B1859, B1862 and Review 77). Left: B1291's verdict file has no scope and no pointer to the arc that re-scoped it; the sixth, on the nulls, was not checked |
| X1 | twelve places in the governing documents cap the goal | REPRODUCED | GOVERNANCE.md:23 says the goal is not a theory of everything, and neither it nor CLAIMS.md has changed since the audit. The owner has confirmed the goal to main (P-758); amending the places is the first step of P-767. One of the audit's twelve places (THE_CLAIM.md, lines 58 to 71) is the anchor doctrine and is doubtful as a cap |
| X2 | three documents each claim supremacy | REPRODUCED | Three files each say they win a disagreement: GOVERNANCE.md:6-9, GENESIS.md:29, CLAIMS.md:3 |
| X3 | the printed identification price undercounts, and its script fails | REPRODUCED | In part. The certificate script does not fail on main: it exits 0, its four tests pass, and it is unchanged since the audited commit. What holds is that the '4' in '4 + 9 = 13' is a typed constant |
| X4 | scope tags are absent from most verdict files | REPRODUCED | 1283 of 1570 verdict files carry no scope, and none a domain |

**The seven that main had run itself** (B1865, the seat's planted violations in a scratch clone): G6, G7, G8, G9, G10,
G14 and L7 were each planted and not caught. They are recorded as reproduced by main.

**Still by a reader only** (five): E2, L6, L10, M1, W1. Their planted cases are not automated in the seat's script.

## 4. Where the audit's own details are stale or wrong

- **A script it says fails does not** (X3). The certificate script exits 0, its four tests pass, and it has not
  changed since the audited commit. What holds of that finding is that one of its two counts is typed.
- **Counts that have drifted since 2026-11-07**, in the same direction as the audit says: 580 arcs of lag where it
  says 569; 9 declared debts for 8; 421 of 1079 for 414 of 1068; 1570 verdict files for 1556; 606 paragraphs for
  593; at least seven pages for four; at least eight for three.
- **Things already corrected before the audit or since:** the paper's source already called the derivation standard
  (M6); the uniqueness page already said it forces a matrix, conditionally (M2); README gives no outcome for the six
  (P1, V2); four of the six instances of the truncation class now carry scope notes (W5); one of five slips is
  corrected (E12).
- **Examples that do not fit their class:** one chain link's lock does recompute its discriminants; another is a
  no-go link and not a theorem (L3). One of three arcs said to be missing from the look ledger uses no data by its
  own findings (V5). "Most entries cannot fire" is 3 or 4 of 11 (M10).
- **Its census tools are not on main,** so two of its counts could not be re-derived (L1, M8).

## 5. What this changes

- **The programme (B1861)** carries the new state of every finding, with the old state kept beside it.
- **The order of repair is unchanged:** enforcement first (the fifteen planted violations that still pass), then the
  corrections that are a sentence or a pointer, then the fields the owner's confirmed rulings add (a declared domain,
  a truncation ledger), which close four of these findings at once (W2, W4, X4, and W5's remainder).
- **Three findings are closed by rulings the owner has already confirmed,** once carried out (P-767): the goal in the
  governing documents (X1), one governing document (X2), and the count computed and not typed (X3's typed constant).

## Seen first

- **The repo sweep:** B1861 § 8 (every finding's state), B1862 to B1865 (the first corrections and the planted
  violations), the audit itself and its acceptance rows on the advisor seat's branch. No finding reproduced here had
  a main-side reproduction before.
- **The literature:** none needed.

## Disclosed

- **The checkers are instances of one model family, and cheaper ones.** Their agreement with the audit, itself a
  session of that family, is weaker evidence than a differently built reader's. Main's re-runs are of commands, and
  a command's output does not depend on who wrote it.
- **Nine findings are confirmed in part only,** and the table says which part.
- **Main read each checker's claim before reading its own output.** The outputs are mechanical; the reading of them
  was not blind.
- **Judgment remains in some findings** (what counts as a cap on the goal; what counts as a stronger self-label).
  Main confirms the text is there, not the judgment.

## Reproduce

```
python3 -B frontier/B1870_the_audits_backlog_reproduced_on_main/verification/rerun.py
python3 -m pytest -q frontier/B1870_the_audits_backlog_reproduced_on_main/verification/
```
