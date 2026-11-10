# ADVISOR TO CC — independent audit, findings (2026-11-10)

**From:** the advisor seat (an audit session working at the owner's word; branch `cld/cool-hamilton-k9eqvo`).
**To:** cc (the banking seat). **Kind:** `result:` with `propose:` items — nothing here is a `go`.
**Role, as the owner set it on 2026-11-10:** this seat advises; cc fixes on main; the seat then re-audits and says
whether each item meets `ACCEPTANCE_CRITERIA.md` (same folder). This seat writes nothing to main.

**Audited commit:** `217e37c4f` (main, 2026-11-07). **Audit date:** 2026-11-10.
**Scope:** the load-bearing layer in full — gates and checkers, `GENESIS.md` and the proven core, the theorem chain,
the seal and look ledgers — plus a risk-weighted sample of 33 arcs (the most depended-on structural arcs, the most
depended-on value-layer arcs, and the twelve newest). Not a census of all 1,559 arcs.
**The audit changed nothing on main.** The census scripts and their outputs are in `tools/`.

**Verify, don't trust:** every finding below is to be reproduced on main's own code before anything is banked.
Findings graded [S] were demonstrated by one reader of this audit and not repeated by a second.

Evidence grades used below:
- **[V]** I verified it myself (re-ran, recomputed, or read the code line).
- **[S]** a strand of the audit demonstrated it (experiment or recomputation) and I did not repeat it.

---

## 1. Bottom line

1. **No mathematical error was found in the foundations.** `GENESIS.md` §2–§4 and the proven-core statements checked
   (P1–P11, P13, P15, P16) recompute correctly, and `GENESIS.md` labels its own postulates and choices honestly. [S]
2. **Every committed script that was re-run reproduced its committed output.** The arithmetic of the record is
   reliable. [S]
3. **The enforcement layer does not enforce what it says.** Several gates cannot fail on a committed violation,
   including the append-only gate and the seal gates for every seal since B1075. About a quarter of PROVED arcs are
   guarded only by locks that read stored text.
4. **Labels are stronger than content.** "PROVED" covers theorems, numerical estimates, pre-registered cells that came
   out, and administrative acts. Titles and claim lines routinely drop the caveats the arc bodies state.
5. **Corrections are found but not propagated.** The record catches its own errors, files a register row, and the
   outward pages, verdict files and locks keep the old statement for weeks.
6. **The value layer has no surviving positive.** By the record's own later arcs the final attack ran and failed, and
   the headline six-ratio fit rested on an end condition since retired. The nulls behind every quoted rarity have an
   unpriced window bias.
7. **Distance to "parameter-free":** by `GENESIS.md`'s own statuses, at least 14 postulated or chosen foundation
   items, a frame hypothesis, 20 unearned identifications, and 13 borrowed joints in the best frame. 0 of 19 derived.

---

## 2. What is sound

| Area | Result |
|---|---|
| Proven core P1–P11, P13, P15, P16 | recomputed by hand, sympy or SnapPy; all hold [S] |
| `GENESIS.md` §2 identities, §3 census (758 states to length 12), bundle identifications | hold [S] |
| LR/RL the only positive words of trace 3 | true for all lengths (monotonicity; brute force to 14) [S] |
| `GENESIS.md` labelling of SE1, SE2, frames, gaps | no choice presented as forced, apart from two status words (C14) [S] |
| Script reproducibility | B854, B883, B884, B892, B861, B862, B1291, B1297, B1028, B1851–B1857, B915, B1728, B1691, B1816: outputs identical on re-run [S] |
| Value-layer seals (12 checked) | hash matches, seal commit precedes results, no post-seal edit [S] |
| All 432 ledger sha8 values and 46 full digests | recompute correctly [S] |
| "0 of 19" | carried consistently on every surface checked; no synthesis document presents the six as derived [S] |
| `docs/THE_PROGRAMME_SO_FAR.md` | accurate for its date: about 2 overstatements in 46 sourced lines [S] |
| P9 paper draft | careful; discloses internal, AI-assisted verification; nothing since retracted found in it [S] |
| B1297 | the best-built arc sampled: its lock recomputes and it reports its own test's vacuity [S] |
| Gates that work | a crashing gate is reported as FAIL; hand edits to generated views are caught on a full clone; numeric baselines have only ever been lowered [S] |

---

## 3. Findings

### 3.1 Enforcement that does not enforce (gates and seals)

| ID | Sev. | Finding | Where | Grade |
|---|---|---|---|---|
| G1 | critical | **`append-only` cannot see a committed change.** It compares the working file with the same file at HEAD. Deleting 200 lines of `PROGRESS_LOG.md` and committing passes. | `scripts/gates/gates.py:126-136` | [V] code, [S] experiment |
| G2 | critical | **Post-seal edits are undetected for 317 of 361 sealed files**, including every seal from B1454 on. `seal-digests` recomputes only 44 hand-written rows (B890–B1075). A criterion appended to B1841's pre-registration and committed passes all four seal gates. A deleted sealed file is skipped. | `scripts/gates/gates.py:1118-1143` | [V] skip path, [S] experiment |
| G3 | major | **The seal ledger's "recorded elsewhere" column certifies itself**: the search corpus includes the previous ledger. Regenerating twice gives 142 unrecorded, then 0. 156 of 432 seal hashes appear in no other tracked file, including the live candidate B1841's. | `scripts/seal_ledger.py:36-46` | [S] |
| G4 | major | **The seal-order gate only sees files named `PREREGISTRATION.md`.** 15 arcs with other seal filenames were first committed together with their results and are not listed. B1297 (38 dependants) says "sealed … BEFORE evaluation"; `PREREG.md` and `FINDINGS.md` first appear in the same commit `120d272ac`. | `scripts/gates/gates.py:1036-1065` | [V] B1297, [S] the 15 |
| G5 | major | **"Gates fail closed" is false for at least 15 gates.** With no git, 45 of 49 pass and 10 checked nothing. Deleting the identification baseline lets new unearned rows through; deleting all arc tests leaves `test-vacuity` green; emptying `LAW_MAP`/`THEOREM_LEDGER` passes with "0 rows". | `WORKING_RULES.md:141`; many | [S] |
| G6 | major | **Four gates read today's date.** HEAD was green on 11-07 and red on 11-08 (`lead-debt` 78 > 77), with further failures scheduled through November. Undocumented `OA_*_TODAY` variables can force green. HEAD cannot pass its own pre-push hook. | `lead_debt.py`, `point_debt.py`, `relay_debt.py`, `harvest_debt.py` | [V] red today, [S] schedule |
| G7 | major | **`gate-controls` checks only that a function of that name exists.** Pointing all 49 entries at skipped trivial tests passes. Several registered controls do not exercise their gate's criterion (`attribution`, `append-only`, `views-generated`, `retraction-debt`). | `scripts/gates/gates.py:1629-1653` | [V] code, [S] experiment |
| G8 | major | **`retraction-sweep` reads 29 of about 49 registry phrases.** Every row added since 2026-10-07 is in a shape the parser drops. About 45 cue words exempt a whole line. | `scripts/checks/retraction_sweep.py:81-118` | [V] count, [S] experiment |
| G9 | major | **`attribution` never reads a commit message.** It checks the tip author's name and tokens in seven file types. History holds several hundred AI co-author trailers; the practice row says "no AI trailer — GATED". | `scripts/gates/gates.py:236-257`; `docs/PRACTICES.md:43` | [V] |
| G10 | major | **Eleven practices labelled GATED have a gate weaker than the practice** (forbidden artifacts, PROVEN rows without a lock, banned phrases outside `.md/.py/.txt`, atlas freshness, `seen-first`, law-map provenance, doc-facts, pretense phrases, supersession backlinks, fail-closed, seal ledger currency). | `docs/PRACTICES.md` | [S] |
| G11 | major | **`doc-currency` prints "18 living documents current" with 8 in permanent declared debt** (`CLAIMS.md` lag 569 arcs against a tolerance of 40). | `scripts/checks/doc_currency.py:100-124` | [S] |
| G12 | major | **"The gates also run on every push" is an honour system**: a hook each clone installs by hand, no CI, tip commit only, suite not run. | `README.md:71`; `scripts/gates/prepush.py` | [S] |
| G13 | major | **Results depend on clone depth and fetched refs.** A shallow clone fails two gates spuriously and passes `lead-debt` with "0 stale" (fail-open). The review's "fresh-clone: PASS" clones the local root and skips every seat. | `scripts/views/spine.py:15`; `scripts/review/review_tools.py:255-262` | [V] shallow effects, [S] rest |
| G14 | minor | Baselines are counts, not named sets; `ESCALATED` markers never expire (all 55 open leads currently exempt); substring id matches (`B18` inside `B18xx`); a malformed verdict file is skipped by seven gates. | various | [S] |

**Re-run by the seat (2026-11-10, after the table above was written):** `tools/planted_violations.py` plants the
violations behind G1, G2, G4, G5, G6, G7, G8, G9, G10, G13, G14 and L7 in a scratch clone of main and runs the named
gates. Five controls are caught; **21 of 21 planted violations are not** (`tools/planted_violations_out.txt`). Those
rows are therefore verified by a second run, whatever grade the table shows.

### 3.2 Locks that cannot fail

| ID | Sev. | Finding | Where | Grade |
|---|---|---|---|---|
| L1 | major | **242 of 1,068 PROVED arcs are guarded only by text-reading locks** (static census of 1,548 lock files: 715 compute, 367 run or import the arc script, 386 read committed text or JSON only). Share by era: 1% (B0–299), 44% (B900–1199), 39% (B1800+). Only 8 of the 386 label themselves as transcript checks. Includes B892 (23 dependants), B883 (21), B1600 (20), B884 (16), B952 (15). | `tests/` | [V] |
| L2 | major | **"Locks assert mathematics" (rule 7) is not in the practices register and has no gate.** `test-vacuity` catches only syntactically empty asserts. | `WORKING_RULES.md` rule 7; `docs/PRACTICES.md` | [V] |
| L3 | major | **Theorem-chain locks are mostly weaker than their links.** Of 16 links sampled, 2 locks recompute (C9, C47). `chain-locks` checks only that the file exists. Examples: C7 asserts `len({-3,5,-15}) == 3`; C45 hard-codes textbook charges. | `docs/THEOREM_LEDGER.md`; `scripts/gates/gates.py:755-783` | [S] |
| L4 | major | **B1854's lock fails in every clone**: it reads three `.log` files excluded by `.gitignore` and never committed. | `frontier/B1854_*/verification/test_b1854_*.py:14-17` | [V] |
| L5 | major | **B1847's lock has two assertions that cannot fail** (`lim = sorted(...); assert lim == sorted(lim)`; arithmetic on literals). | `frontier/B1847_*/verification/test_b1847_*.py:129-135` | [V] |
| L6 | major | **B1849 and B1850 locks compare printed floating-point round-off as strings** and fail on another machine. | their `verification/test_*.py` | [S] |
| L7 | major | **At least 11 tests are arithmetic on literals** (`assert 1 != 2`, `assert 48 == 2 * 24`); 97 "both-literal" asserts are reported but never enforced. | e.g. `tests/test_b710_thimbles.py` | [S] |
| L8 | major | **B892, B952, B866 have no computation of their headline in the arc.** B892's exact tower scripts are not in the repository or its history; B952's `results.json` is hand-written; B866's determinant interpolation was never committed. The mathematics checks out independently. | those arcs | [S] |
| L9 | minor | **Core tests that compare a value with itself** (`test_mobius_vector_field.py:39-43,72-75`); without SnapPy, P9 is tested against its own literals; 75 lock files skip silently without SnapPy. | `tests/` | [S], [V] skip count |
| L10 | minor | **The suite rewrites tracked evidence files** (`seal_census.json` in B1464, `main_w81_w83.json` in B1690). | `tests/test_b1464_aged_items.py` | [V] |

### 3.3 Errors and bugs in the mathematics or its code

None of these overturns a result the record depends on, but each is a wrong statement or broken check as written.

| ID | Sev. | Finding | Where | Grade |
|---|---|---|---|---|
| E1 | major | **B997's uniqueness theorem has a counterexample.** "The golden is the unique metallic grammar whose own-conductor shadow is a McKay group, proved for all m": at m = 4, ⟨R⁴, L⁴⟩ mod 20 has order 120 with the same element-order profile as the golden case. Known to the record since 2026-10-23 (P-318); B997 is still PROVED with no note, and the claim stands in `GENESIS.md`, `docs/THE_CLAIM.md`, `docs/LAW_MAP.md`, `docs/THEOREM_REGISTRY.md`. | `frontier/B997_*` | [V] |
| E2 | major | **The C9 lock asserts congruence level (8)**; the image already has the full index 12 at level (4). The ledger's own note of 2026-09-16 says level (4). | `tests/test_b734_m004_congruence.py` | [S] |
| E3 | major | **B1856 logic gap.** "Invisible to every state" is equated with E ≡ ±I mod 5, but ρ(−I) is +1 on the even sector and −1 on the odd, so −I is visible on mixed states unless a parity superselection rule is assumed. 305 of 643 rung-invisible defects have E ≡ −I. The run of 6 (E = +I) is unaffected. | `frontier/B1856_*/FINDINGS.md:16-18,36` | [S] |
| E4 | major | **B952's "theorem" is false as stated** ("the centralizer of a set of semisimple elements contains a maximal torus"); it needs "commuting". The repository's own 2T centralizer (rank 4) is a counterexample. The conclusion for the cascade survives. | `frontier/B952_*/FINDINGS.md:22,35` | [S] |
| E5 | major | **B892's real-line scan never refines.** The golden-section step sits under `if not found:` and a grid point is always found. The scan cannot exclude a real nullity-14 point; that exclusion rests on another arc's sign certificate. | `frontier/B892_*/wall_search.py:76-82` | [S] |
| E6 | major | **B862's "kernel computed exactly" computes nothing.** The function builds no map; the 6 is a literal in the test condition. The ℤ₆ fact itself is true. | `frontier/B862_global_form/global_form.py:24-35` | [V] |
| E7 | major | **B1028's "0.000 bits of designer freedom, machine-checked" is a sum of eleven typed zeros.** The check is a substring match in the cited arc's claim line. The arc's own addendum says one row is unpriced; the verdict was not updated. | `frontier/B1028_freedom_ledger/b1028_walk.py:46-106,179` | [V] |
| E8 | major | **B854's negative is scoped to the principal embedding only**, but its claim line says the electroweak-type centralizer "is refuted". The repository's own scratch table shows the centralizer is abelian for only 6 of 20 nilpotent classes. | `frontier/B854_*/FINDINGS.md:108,124` | [S] |
| E9 | major | **B1854's "6.070 ± 0.010" is not an error estimate** (an exact three-point interpolation); it differs from the seat's value by 0.012; no control at k = 2; "τ∞ = 6.06 ± 0.01 at main's resolution" was not computed on main. Labelled PROVED. | `frontier/B1854_*` | [S] |
| E13 | major | **B567 states "21 distinct eigenvalues" at level 165, and a lock pins it; the count is impossible.** The same test asserts projective order 20, which allows at most 20. The 21st is the eigenvalue at angle ±π split across the branch cut of `np.angle`; a re-run here gives 20. The arc's negative conclusion is unaffected. | `frontier/B567_hamiltonian_handoff/FINDINGS.md:20`; `tests/test_b567_hamiltonian.py:54` | [V] |
| E10 | minor | `README.md:40`: `query.py card B1812` ignores the arc id. | `scripts/atlas/query.py:192-195` | [V] |
| E11 | minor | P12's "golden factor" of the gluing equation depends on a slice and a triangulation labelling; P15/P16's "fixed points on H" lie on the boundary; `docs/LITERATURE_CONTEXT_2026-07-15.md:27` says sin(π/7) "has no radical closed form" (false). | `CLAIMS.md:58,60` | [S] |
| E12 | minor | B1857 "the two cheaper departures" is an infinite family; B1853's margins are range artifacts; B1852's "all 4 reversing involutions" is a window artifact (a two-line mod-2 proof exists); B884's calibration control does not calibrate and a filename bug would crash on a fresh tree; B915 uses a measured α_s its pre-registration says it does not. | those arcs | [S] |

### 3.4 Labels stronger than content

| ID | Sev. | Finding | Grade |
|---|---|---|---|
| M1 | major | **PROVED means at least five things.** 188 PROVED arcs have no script in their folder; B1848 (Review 76) is PROVED; B1741 is PROVED with 6 of 13 sealed cells failing; B1816's own scope says "not a proof". Tools that walk the dependency graph select on the word. | [V] counts, [S] examples |
| M2 | major | **The "forcing" theorem forces a matrix, not the figure-eight.** `docs/UNIQUENESS_THEOREM.md` and `docs/THE_CLAIM.md` present A1–A7 as forcing the object; `GENESIS.md` says four further inputs are needed. The "144 → 1" search is the filter `a*b == 1`. | [S] |
| M3 | major | **Three of the four "further filters" do not separate the figure-eight from its sister m003** (same volume, also amphichiral, same tetrahedron shapes). Code and test still say "five independent filters". | [V] |
| M4 | major | **`docs/THEOREM_LEDGER.md` says "no physics statement appears below"** and labels as [THEOREM] a link stating that a closing "carries the Standard-Model gauge algebra and three complete generations". | [S] |
| M5 | major | **"The flavour three is derived"** (`GENESIS.md:780`, `docs/THE_WEAVE.md:113`, K021) against identification I-31, UNEARNED. | [S] |
| M6 | major | **The ℤ₆ global form is "derived" and "not standard" in the P3 paper** after B1221 called it path-independent and not new. | [S] |
| M7 | major | **B1855's titles say "proved least" for a step main did not re-run** (thinnest margin 0.0017); its "every lcm ≥ 12" drops the scope S ⊆ {2,3,4,5}. | [S] |
| M8 | major | **B1850's "313 of 313 quotes found verbatim"**: 76 of 86 no-load closures quote the row's own title or memo. (A sample of 32 closures found none wrong in substance.) | [S] |
| M9 | major | **"EXTERNAL REVIEW" and "outside referee"** in the paper folders, against `PROVENANCE.md`: nothing is externally verified. | [S] |
| M10 | major | **The falsifier register cannot contradict the programme**: by its own grading most entries cannot fire, and the numeric ones are worded so a failure kills a reading, not the programme. | [S] |
| M11 | minor | **The generated reviewer page asserts false universals** ("Every PROVED arc names its test locks": 414 of 1,068 do not). | [S] |

### 3.5 Corrections found but not propagated

| ID | Finding | Grade |
|---|---|---|
| P1 | **The front door describes a plan that already ran and failed.** `README.md` and `docs/THE_PROGRAMME_SO_FAR.md` still present the final attack as ahead and the six ratios as reached at χ² 2.74; B1823 and B1825 are NEGATIVE, and B1838 (OPEN) records that the six pass only with the small-cut end and fail at the exact norms (31–54). None of the three is mentioned in either document or in the plan. | [V] |
| P2 | B997's counterexample (E1): one register row, P-318, bundles about 25 unapplied corrections. | [V] B997 |
| P3 | The endpoint correction (dimension 14, rank 6: SM × U(1)²) reached B892 but not B861, B862, B863, B994 or B1028. | [S] |
| P4 | `CLAIMS.md:147` keeps a "parameter-free prediction … consistent with measurement" that B653 voided; "16σ" stands on three pages where the paper now says about fifty; B723 is still PROVED after three retractions of its clause. | [S] |
| P5 | The withdrawn 6.153 tube value is still cited as support in B1847 §8; `docs/THE_TAU_READOUT_RULE.md:61-63` is stale after B1854. | [S] |
| P6 | `docs/INDEX.md` lists as "Living" four documents that are stale (`CLAIMS.md` last updated 2026-07-04); `docs/CAMPAIGN_STATUS.md` has 593 lines beginning "LATEST". | [S] |
| P7 | Stale numbers: "39 of 43" forced links on four pages (the gate prints 53 of 57); the `LAW_MAP` banner; duplicate arc ids (B58 three folders, B89 two), which is why the README counts 1,559 arcs and there are 1,556 ids. | [V] ids, [S] rest |

### 3.6 The value layer

| ID | Sev. | Finding | Grade |
|---|---|---|---|
| V1 | major | **Every "specificity" null for the six has an unpriced τ window.** 20% of random targets have their best fit at the top edge of the Im τ grid, while the data's optimum sits inside. All quoted rarities are biased low by an unmeasured amount. | [S] |
| V2 | major | **The plan's headline χ² values omit a 10% error floor on every ratio** (`ALLOW = 0.10`). With the data source's own uncertainties the same fits give χ² ≈ 55,700 and 23,800. The 2.74 row used an end condition corrected the day before the plan was written. | [V] floor, [S] arithmetic |
| V3 | major | **Evidence lives in the git-ignored `audit/` directory** (0 tracked files), cited in 83 lines of the point register, 65 `FINDINGS.md` files and the plan. "66% of random CKMs" rests on 64 draws with no tracked script. | [V] |
| V4 | major | **The only live candidate (B1840/B1841) has a forking path.** The winning end condition was added 75 minutes after the original declaration; it passes its screen at 0.885% against 1% and fails (1.053%) under the c ∈ {1, 3} arms the plan committed to; best c = 3.77 is fitted while the scoreboard says "nothing fitted". | [S] |
| V5 | minor | The look ledger omits three data contacts (B1658, B1659, B1724); two uncertainty standards are used for the same quantity D (±0.11 and ±1.19); two opposite line-label conventions exist in one pipeline. | [S] |

### 3.7 Governance against the goal

| ID | Finding | Grade |
|---|---|---|
| X1 | **Twelve places in the governing documents cap or contradict a parameter-free theory of everything**: `GOVERNANCE.md:23` ("The goal is not a theory of everything"), `:42-45`, `:59-64`; a gate that bans the phrase "toward the full SM"; `CLAIMS.md` O1–O7; `docs/THE_CLAIM.md:58-71`; and `GENESIS.md`'s own results FK11 and GAP6. | [S] |
| X2 | **Three documents each claim supremacy** (`GOVERNANCE.md:9`, `GENESIS.md:29`, `CLAIMS.md:3`), and `GOVERNANCE.md` §2 permits a stronger self-label than `GENESIS.md` allows. | [S] |
| X3 | **The printed "identification price 13" undercounts**, and the certificate script behind it currently exits with a failure and is run by nothing. | [V] failure, [S] count |
| X4 | Scope tags are absent from 1,280 of 1,556 verdict files. | [V] |

### 3.8 Reproducibility

| ID | Finding | Grade |
|---|---|---|
| R1 | Full suite on a clean full clone at HEAD: 14 failed, 8,099 passed, 72 skipped (section 6). One failure is a real error pinned by a lock (B567's "21 distinct eigenvalues", impossible at projective order 20). | [V] |
| R2 | The pinned environment (Python 3.12.1, numpy 2.4.0) exists only as prose; `pyproject.toml` has lower bounds and there is no lock file. | [V] |

---

### 3.9 The weave-versus-thread class (the owner's first priority)

The error the owner names as the most repeated: a result established on one thread, one slice, one point or one
embedding is stated about the whole. `docs/THE_WEAVE.md` already carries the rule and its three-question test. It
recurs for mechanical reasons:

| ID | Finding | Grade |
|---|---|---|
| W1 | **The `member-scope` gate is a count** (baseline 8). One new violation plus one reworded old line passes. | [S] |
| W2 | **Only 239 of 1,556 verdict files carry `weave_or_thread`**, and 276 carry `scope`. The quantifier of most claims is not machine-readable. | [V] |
| W3 | **"The object" still means m004 in `TERMINOLOGY.md`**, while `GENESIS.md` FK13 rules that the object is the word states. The default noun is a thread. | [S] |
| W4 | **No truncation is recorded.** What an arc removed from the carrier before computing (one embedding, one irreducible sector, h₀ = 0, positive words only, a τ window, a finite range) is stated in prose or not at all. | [V] |
| W5 | **Audit findings of this same class:** B854 (the principal embedding stated generally, E8), B1855 (S ⊆ {2,3,4,5} stated as "every", M7), B1853 (range artifacts, E12), B997 (a finite check behind "all m", E1), the nulls' τ window (V1), B1291's cusp count (re-scoped by B1292 but not in the verdict). | [V]/[S] as cited |
| W6 | **The plenitude principle ("everything allowed happens") is not a foundation item.** `GENESIS.md` §1 holds PF1–PF3 only; plenitude lives in a register row (P-485) and in `docs/THE_WEAVE.md`. What turns the whole into one number — a measure, an action, an operator — is not supplied: B1813 (the measure depends on how threads are counted) and B990 (an invariant of the whole cannot pick a point) are the record's own theorems on this. | [V] |
| W7 | **A weighting rule chosen by hand is the thread mistake one level up.** "Coherent interference", "the joint action" and "the operator's ground state" each need a named operator; main's B1857 marks the clock behind the state reading CHOSEN (B1815). Until the grammar forces the operator, its status is CHOSEN. | [V] B1857 |

---

## 4. The distance to "parameter-free", by the record's own statuses

| Layer | Still taken by postulate, choice or identification |
|---|---|
| Principle | PF1, PF2, PF3 — postulated |
| Grammar | GM1–GM4, GM5a postulated; GM5b an owner's ruling; GM5d chosen; GM5c open |
| Root | SE1 postulated; SE2 chosen ("the most fragile link"); the order bit A7; the minimality criterion C2b |
| State space | which state is physical, the join, the deck, the ends, the register — open forks |
| Frames | every frame is a named hypothesis; none derived |
| Dictionary | 20 identifications UNEARNED, 8 earned (all pure mathematics), 8 refuted |
| Best frame (A) | 13 borrowed joints for 6 mass ratios: τ and c fitted, 10 chosen, 1 ansatz |
| Result | 0 of 19 |

---

## 5. Practice reforms proposed (the owner agreed to items 1–5 on 2026-11-10; the rest are for discussion)

**The weave discipline**

1. **Every verdict declares its domain in machine-readable form:** one thread, a named finite set, all threads of a
   stated kind, or the weave.
2. **A truncation ledger.** Everything an arc removes from the carrier is listed and graded: forced by a theorem, a
   stated computational limit, or chosen.
3. **A gate on the dependency graph.** A thread-domain result cannot close a weave-level question, and a weave claim
   cannot rest on a thread result without a named lifting theorem.
4. **A second-thread control.** The same computation is run on another thread; if the quantity changes, the result is
   a thread result.
5. **Plenitude written into `GENESIS.md` as a postulate, with "allowed" defined, and the weighting rule listed
   separately as open.**

**Enforcement**

6. **Nothing is "enforced" until a planted violation, committed in a scratch clone, has turned it red — and that
   mutation test runs automatically.** Applies to gates, locks and seals alike.
7. **Declared lock tiers** (RECOMPUTE / RERUN / TRANSCRIPT) in each lock, enforced by a gate.
8. **A value-chain certificate before any seal:** the full dependency closure of the frame being read must have, for
   every arc, a recomputing lock, a declared domain, a truncation list and priced identifications.
9. **Seals as a machine-readable manifest** with a full hash per sealed file, covering every seal filename, and a
   check that the seal commit is a strict ancestor of the first result.
10. **Gates and suite are pure functions of a commit:** no date, no remote, no writes to tracked files; debt clocks
    move to a separate scheduled report.
11. **Evidence only in tracked files; locks read only tracked files; no float compared as text.**

**Labels and propagation**

12. **Split the verdict vocabulary:** theorem, exact computation, numerical estimate, sealed cells held, process.
13. **A correction is not closed until every surface carrying the claim has changed**, checked by a gate that reads
    the claim's dependants.
14. **One governing document**, amended to the goal the owner has set.
15. **Fewer rules:** each of the 77 practices either gets a gate that passes item 6 or is dropped.

**Value statistics**

16. **One uncertainty model per quantity, fixed before the fit; any error floor stated in the headline; a null shown
    not to pile up at a window edge; a menu priced as it stood before the answer was computable.**
17. **One independent reimplementation of the value pipeline.**

---

## 6. Suite baseline

Full clone of HEAD with all seat branches fetched, Python 3.13.18, numpy 2.5.3, sympy 1.14.0, SnapPy 3.3.2, no Sage,
`OA_SLOW` unset, 4 workers: **14 failed, 8,099 passed, 72 skipped** in 53 minutes. Review 76 recorded 6 failures on
its own fresh clone. [V]

| Failing test | Cause | Class |
|---|---|---|
| `tests/test_b567_hamiltonian.py::test_level165_spectrum_refutes_28_27` | asserts 21 distinct eigenvalues; this run finds 20. **21 is impossible**: the same test asserts projective order 20, so every eigenvalue is a 20th root of one constant and there are at most 20. The 21st is the eigenvalue at angle ±π split across the branch cut of `np.angle`. `frontier/B567_*/FINDINGS.md:20` states "21 distinct eigenvalues". The arc's negative conclusion is unaffected. | real error, pinned by a lock |
| `frontier/B1854_*/…::test_the_control_and_the_core_levels` | reads git-ignored `.log` files (L4) | broken lock |
| `frontier/B1849_*/…::test_the_cyclic_texture_check_reproduces`, `frontier/B1850_*/…::test_the_generating_pair_check_reproduces` | round-off digits compared as text (L6) | brittle lock |
| `tests/test_b1449_silent_receipts.py::test_the_decisive_test_of_b469_reproduces_with_the_fix_live` | expects `+0.00000000j`, gets `-0.00000000j` (sign of a floating zero compared as text) | brittle lock |
| `tests/test_repo_gates.py::test_all_gates_pass`, `tests/test_b887_gate_audit.py::test_all_twenty_gates_pass_now` | `lead-debt` and `harvest-debt` red by date and by missing tags (G6, G13) | date / ref dependence |
| `tests/test_harvest_debt_gate.py` (2 tests), `tests/test_b1306_the_older_debt.py`, `tests/test_b1035_receipts.py` | need archive tags of retired seats that an ordinary fetch does not bring | ref dependence |
| `tests/test_p3_verification_package.py::test_manifest_is_current` | `MANIFEST.json` is stale (156 locks recorded, 157 found) | stale artifact |
| `tests/test_b805_forcing.py` (2 tests) | graph counts outside the asserted bounds (1,451 attachment edges against 3,255 authored; 905 of 1,575 arcs on no face) | not diagnosed |

72 tests skipped (mostly `OA_SLOW` re-runs and Sage-only checks). The run rewrote two tracked evidence files (L10),
which were restored.

Re-run of the census: `python3 relays/advisor_2026-11-10_audit/tools/arc_stats.py`, then `lock_census.py`, then
`lock_map.py` (outputs beside them).

---

## 7. Not covered

- About 1,520 of the 1,559 arcs, beyond static checks.
- Chain links other than the 16 sampled; proven-core rows P17–P70.
- The numerical instruments of B1846/B1847 line by line; the seats' own branches and code.
- `story/`, `speculations/`, `philosophy/`, `legacy/`, `outside_bench/`.
- The P3 paper body beyond its abstract, summary and the sections named above.
- External confirmation of post-cutoff citations (e.g. arXiv:2609.37895, on which one falsification rests and which is
  not archived in the repository).
