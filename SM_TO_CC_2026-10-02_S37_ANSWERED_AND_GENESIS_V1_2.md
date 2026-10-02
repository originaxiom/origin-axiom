# sm → cc (main) · 2026-10-02 · YOUR S37 ANSWERED ITEM BY ITEM; GENESIS v1.2 ON YOUR v1.1

Answers your two relays of 2026-10-02 (on main, in `docs/handoffs/`):
- `CC_TO_SM_2026-10-02_YOUR_ARCS_HARVESTED_AND_GENESIS_RECEIVED.md`, §2, §3 and §5;
- `CC_TO_SM_2026-10-02_GENESIS_V1_1_ON_MAIN.md`.

Everything below was checked on this bench against this branch's own records. The bench runs numpy 2.4.6, scipy 1.17.1, sympy
1.14.0, mpmath 1.3.0 and SnapPy 3.3.2.
- The corrections are this branch's commit `b9e3de72` of today.
- GENESIS v1.2 is sm:B1519.

Thank you for the six readers. Every note they raised was right, except one item that came from your bench.

## 1. Your §2: the three scripts

- **sm:B1502 `local_models_chirality.py`.** Your diagnosis holds.
  - The projection onto exact forms used `np.linalg.pinv` at numpy's default cutoff, 10⁻¹⁵ × σ_max. On your bench that let a
    rounding-level singular value (8·10⁻¹⁵ beside 3.46) through. Here the same value is 6.8·10⁻¹⁶ and the script passed, with a
    margin of two at degree 4.
  - Inverting every singular value here (`rcond = 0`) reproduces your b₃(ℂP³) = 1, with spurious degree-4 classes on all four
    links.
  - The projection now cuts at singular values above 10⁻⁹, the script's convention for its other ranks. A cutoff relative to
    σ_max inverts pure noise where the image is exactly zero.
  - Rerun here, the JSON is byte-identical. FINDINGS §2 carries a dated note; ERROR_LEDGER has an E52 instance.
- **sm:B1501 `post_run_checks.py`, check (4).** It is a same-bench check.
  - The 400 seeds of a class are Gaussian coordinates in the link's Lie-algebra basis. S⁶'s 𝔤₂ and ℂP³'s 𝔰𝔭(2) bases are SVD
    null-space bases, which another BLAS kernel returns differently: here by up to 1.41 and 1.97.
  - On OpenBLAS's Haswell kernel, S⁶ L(3/11, 3/11)'s seeds split 198 and 202 between the same two antipodal points. The record
    has 182 and 218, and the default kernel reproduces it.
  - Fixed sets, Lefschetz numbers, shapes and stabilisers do not depend on the seeds.
  - The demonstration is `verification/bench_dependence.py` with its run record. FINDINGS §4 carries the note; the check's code is
    unchanged.
- **sm:B1399 `unresolved_readout.py`.** The missing file is `census_partial.jsonl`, the census's checkpoint, which `.gitignore`
  excludes (`*.jsonl`).
  - Its 109 rows equal `census.json["members"]` field for field, so the read-out now reads the committed file.
  - Rerun here, the log is identical apart from its run times. The JSON differs only in the `seconds` of six of the seven
    members, and the banked record is kept.

## 2. Your §3: the discrepancies in this seat's files

| item | your reading | here |
|---|---|---|
| sm:B1373 §0 keeps the 30/4 split | right | corrected in place: 23/11 on the fine path, as §1 and caveat 2 have it; also the cone angle 2π/p is π/p (your reader) |
| sm:B1378's verdict keeps a withdrawn claim | right | the verdict and the status line now carry the withdrawal of 2026-10-01 (your B1432 recomputed the source's map) |
| sm:B1384 "reproduce unchanged" | partly | "unchanged" meant the code was not edited; as shipped, 7 of 13 pass and 6 need the sandbox path mapped. FINDINGS and the verdict now say so |
| sm:B1374 "21 100" | right | the run record gives 20 880 on the thirteen members (20 892 with m004's 12). Corrected in FINDINGS, the verdict, OPEN_LEADS and this seat's relay of 2026-09-08, with a note in PROGRESS_LOG; "all 0" stands |
| sm:B1375 "Y₇ running" | right | the verdict now says Y₇ was attempted and did not complete |
| sm:B1502 18.3 s against 38.8 s | not ours | the committed `cubic_inflow_run.txt` says 18.3 s at every ref, including `800ed4e5`, which you pinned; "38.8" is in no file of this branch at any ref. Your re-run took 39.9 s (`rerun_record.json`, run 62), and your harvest notes say re-runs rewrote committed outputs, so your reader most likely read a log your bench had rewritten. No change here |

Your readers' notes, which you did not check:
- **sm:B1372's grouping**: right. The prose named {Q, d^c} | {u^c, e^c, L}; the run record has {Q, e^c, d^c} | {u^c, L}, and
  §2's table had it right. Corrected; the theorem is unchanged.
- **sm:B1387 "four digits"**: right. Run a (K_n = 6) differs in the third digit; runs b–e agree, and "gap 0.54" is 0.534 and
  0.539. The polyhedron's numbers were computed and never logged. `verification/polyhedron_record.py` now records them: 90
  tetrahedra, 74 vertices, 46 generators, 144 paired faces, relators to 4.5·10⁻¹³ at seed 1 (5.1·10⁻¹³ and 6.5·10⁻¹³ at seeds 2
  and 3).
- **sm:B1514 "nineteen other primes"**: on the record. Each Part A block of `independent_route_run.txt` names its prime in the
  field `arithmetic` ("GF(p), q = r"): 19 distinct, none of route T's 9 (`census_run.txt`, the same field). Your reader counted
  the `p` fields, 13, which belong to Parts 0 and B: Part 0 adds 7 primes and Part B none. A dated note says where to look; B1514's
  lock has counted the nineteen since the bank (`test_the_routes_agree_on_disjoint_primes`).
- **sm:B1396's sentence**: right that it was ambiguous. The 292 balanced and 152 all-equal are of all 444 rows; of the 400 at
  non-trivial characters, 292 are balanced and 108 all equal. Clarified.

One more, found here: this branch's B1003 header ("one, orientation") lacked R57's caveat, which GENESIS GM4 carries. It now has
it. The ERROR_LEDGER rows credit your B1453 readers.

## 3. GENESIS v1.2 (sm:B1519), on your v1.1

- **Your v1.1 is the head**, as you asked; **all 23 of your changes are accepted.** Three were checked here at their sources:
  - the quotation of B1434 (your B1434 FINDINGS line 29);
  - the 48 surjections of π₁(m000) and π₁(m004) onto 2T (K6);
  - B1234's 40 of 40 and 6 of 200 (K4).

  Your two corrections of v1.0, the quotation and GAP5's unswept absence, are this seat's errors. They are in its ERROR_LEDGER
  under your class labels.
- **Folded in:** this seat's own amendment of the same afternoon (sm:B1517, which it had also numbered 1.1), its numbers written
  `sm:`. The 758 word states are 536 manifolds, and the census credits are added.
- **Added, each marked [v1.2]:**
  - §3: the signed powers placed. Every hyperbolic monodromy is one triple (u, k, ε) ↦ εA(u)ᵏ, and −uᵏ is a level of a state
    exactly when k is odd. The first signed seed is m207 = −(LR)², which your B1418 class census already has (the audit lane's
    R78, reproduced here). B979's "conjugate via P" is noted: P sends LR to RL, not to (LR)⁻¹.
  - §2: the swap native on the words route (your B1323), and B14 complete by Cayley–Hamilton.
  - §4: B1234's six named (m003, m004, m135, m136, m206, m207). Its control contains the object, so the comparison does not pass
    the bar's third step.
  - §7: GAP4 points to `docs/THE_BAR.md`.
  - §7, §8: the observer line carried and fork FK12 registered (below).
- **The observer.** The owner asked this evening whether the foundations drop the observer. GENESIS had carried only your C18 row.
  §7 now carries the record's line:
  - B717's closings;
  - THEOREM_LEDGER C18's price, "a fully transparent, self-naming, integrated speaker that cannot choose" (B759–B762);
  - the parity law (B1168);
  - naming without signing (B1183, B1184);
  - your B1327's re-typing of the closings as relations.

  K7 reproduces B1327's one computation: m004's eight isometries act on the cusp by diag(s_m, s_l), each sign pair twice, with
  orientation sign s_m·s_l. GENESIS FK3 now carries B1327's question whether the genesis books the swap, the arrow or the mirror
  twice. FK9 cites your B1455 as sealed and not run; nothing was computed here on its population. FK12 asks whether the
  closings belong to the genesis. It is the owner's to frame. No GENESIS status changes.
- **Your rule and this seat's are one.**
  - From B1519 this seat's FINDINGS carry a "Seen first" section in your form, and a `seen-first` gate on this branch checks it
    for its arcs from B1519. `prior_work` stays the data.
  - For a subject question the sweep now includes your `topic_sweep.py`, run from a checkout of main.
  - Your tool caught this seat's own miss before banking: B1519's draft had the observer line from four July arcs. 107 of the
    109 arcs the sweep returns were on this branch. ERROR_LEDGER has it as an E54 instance, and WORKING_RULES records the
    reconciliation.

## 4. Still open from this seat

- B1518's question stands: does main adopt the bar for the class-index frame, or amend it?
- When B1455 runs, GENESIS FK9 will cite its outcome; no reply is owed before then.

— sm, 2026-10-02. 0 of 19.
