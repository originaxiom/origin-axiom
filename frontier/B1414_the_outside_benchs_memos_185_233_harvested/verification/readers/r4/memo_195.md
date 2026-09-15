# Reader r4 — Memo 195 (THE_COMPLEMENTARITY_JOINED.md)

## 1. HEADLINE
"WHAT EACH FACE LACKS, THE OTHER PROVIDES: one theorem, found five times, never joined." The
owner's question ("what Q√5 lacks Q√−3 provides and vice-versa") "HAS AN EXACT ANSWER AND IT
IS DIRICHLET'S UNIT THEOREM" — growth (unit rank 1, hearing/ℚ(√5)) and orientation (nontrivial
conjugation, being/ℚ(√−3)) "CANNOT CO-OCCUR ON ONE QUADRATIC FACE," stated in five arcs at four
levels with zero cross-citations among them. **Date 2026-09-10** (addendum 1 same day; addendum
2, 2026-09-11).

## 2. CLAIMS
1. Three quadratic faces (being ℚ(√−3), hearing ℚ(√5), meeting ℚ(√−15)) with unit ranks 0, 1, 0
   respectively; `N(φ)=−1`, regulator `log φ = 0.481211825…`; being's regulator ≡ 1 exactly. —
   PROVED (Dirichlet's unit theorem, standard)
2. Exclusivity theorem: for a quadratic field `r₁+2r₂=2`, so unit rank is 1 or 0 never both, and
   `c` (conjugation) is nontrivial exactly when rank is 0 — growth and orientation are mutually
   exclusive on one quadratic face. — PROVED
3. Five arcs (B318, B1069, B1216, B1222, B1276) state this at four different levels; measured by
   grep cross-citation: **20 ordered pairs, 0 citations**, with a non-vacuity control (B1276→
   B1174/B730 found). — MEASURED / "NEVER JOINED"
4. B1222's surviving residue ("symmetry redistributes … removing CS … while adding homological
   torsion") is the same complementarity from the other side (m003 vs m004, the golden 5
   relocated between archimedean field and finite torsion). — INTERPRETATION, tied to banked
   B1222/B781 facts
5. §4 HYPOTHESIS (explicitly not banked): the seven sealed value crossings' 7-for-7 miss rate is
   *structural* — every crossing asked a face for a commodity (magnitude vs orientation) it
   provably lacks. Four kill conditions (K1–K4) fixed in advance; K1/K2 return nothing on a
   first pass; **K3 not yet run** at time of writing. — HYPOTHESIS, FENCED, NOT BANKED
6. **ADDENDUM 1** (2026-09-10): re-reads against `docs/WHAT_WOULD_COUNT.md` §4A — the fourth
   retirement leg (the seven misses) is *"empirical exhaustion, not theorem"* per the doc's own
   words, and §4 is a candidate theorem for exactly that leg. Extends the cross-citation method
   to 8 arcs (+ B666, B1095, B1227): 56 ordered pairs, 16 citations, **all in one cell
   (B1069→B666)**, 55/56 empty. B1095 offered as a *positive* confirmation (hand spectrally
   invisible to 1.3e-15 across 2584 eigenvalues; energies P-invariant/forced, localization
   P-equivariant/free; breaks at odd Fibonacci index, 0.147). Re-grades own prior 8-row report
   (chirality: wall→theorem-with-named-escape; values: 3 of 4 closing legs are theorems, 4th is
   not; predictions: under-reported, Tier-INTERFACE live). — MEASURED + INTERPRETATION, NOT BANKED
7. **ADDENDUM 2** (2026-09-11): K3 run via `certificates/k3_the_crossings_sorted.py`. Sorts all
   seven crossings by face/commodity from the sealed text: B915 (being/running, MISS 15.97σ,
   α_s-dominated +0.041 vs +0.002), B925 (being/RG ladder, "RG-invisible"), B929 (being/CKM
   ratios, shape HIT, magnitude MISS 5–9×), B1027/B1063 (being-trit/continuous phase, MISS
   11.4σ/38σ), **B1066 R-A** (hearing/magnitude `sin²θ₁₂`, MISS 4.7σ), **B1066 R-B**
   (hearing/magnitude `|U_e1|`, MISS 3.4σ "unrescuable"), **B1075** (hearing/PMNS moduli, MISS
   at power). Three crossings asked hearing for its *own* commodity (magnitude) and missed →
   K3's FALSE branch fires → **§4's hypothesis is REFUTED**, not vacuous. — REFUTED (by its own
   pre-registered kill condition)
8. Consequence: §§1–3 (the unit-theorem complementarity and the 5-arcs/0-citations count) stand
   **untouched** by the refutation; §4A.0's fourth pillar (seven misses) **stays empirical**, not
   converted to theorem. — STANDS / NOT CONVERTED

## 3. CERTIFICATE
- `certificates/face_complementarity.py` — **EXISTS**; output `outputs/
  face_complementarity_out.txt` — **EXISTS**. Tail: `ordered pairs measured: 20  citations
  found: 0 -> B (NEVER JOINED...)` and `VERDICT: CELL 1 = B, CELL 2 = B` — **agrees** with the
  headline's "never joined."
- Addendum 2's certificate `certificates/k3_the_crossings_sorted.py` — **EXISTS**; output
  `outputs/k3_the_crossings_sorted_out.txt` — **EXISTS**. Tail: *"the object's numbers are not
  nature's numbers... the attempt to upgrade it fails"* — **agrees** with the addendum's
  "REFUTED" verdict.
- No seal is named for memo 195 or either addendum (Gate 5 untouched, no measured physical
  value; INDEX grades it "1B"), so there is no sha256 to verify.

## 4. ON MAIN ALREADY?
1. B318, B1069, B1216, B1222, B1276 (the five source arcs) — **(a) already on main**, all under
   `frontier/`; the individual quotes (e.g. B1276 "c acts nontrivially on a quadratic field IFF
   the field is IMAGINARY") are pre-existing banked arcs the memo only re-reads and cross-cites.
2. The "0-citation, never-joined" measurement itself is a **new synthesis fact about main's own
   directory structure** — it is not a claim main states anywhere else; grepping
   `docs/LAW_MAP.md`, `docs/THEOREM_LEDGER.md`, `docs/SEAL_LEDGER.md` etc. turns up mentions of
   being/hearing/meeting individually but no joined "0 citations among B318/B1069/B1216/B1222/
   B1276" statement — **(c) NOT on main** as a standalone claim outside this memo file itself
   (which is now part of main via the outside-bench merge, commit `80e3ec83`).
3. §4A's "empirical exhaustion, not theorem" framing for the seven sealed misses — **(a) already
   on main**, `docs/WHAT_WOULD_COUNT.md` line 208 ("This leg is empirical exhaustion, not
   theorem — the distinction matters") and line ~415, which shows the leg is *still* described
   that way at a **later** count (eight misses, the last being B1128 INSTRUMENT-NULL, via
   `outside_bench/certificates/require_and_test_cell9.py`) — i.e. main's own doc has moved past
   this memo's seven-count to an eight-count, consistent with, not contradicting, the memo's
   "stays empirical" conclusion.
4. K3's refutation (addendum 2) is **not separately cited** anywhere else in `docs/` — grep for
   `k3_the_crossings_sorted` or "K3" tied to this specific refutation returns nothing outside
   the memo/outputs pair and the owner register (`THE_OWNER_REGISTER.md` lines ~2333–2384,
   which is itself the outside-bench lane's own log, now merged) — **(b) applied via the merge
   as the memo/register text itself**, not independently re-derived or cited by a `frontier/`
   arc.
5. No contradiction of any claim was found on main — **no DISPUTED items in this memo.**

## 5. NEEDS COMPUTATION HERE
- Claim 3 (5 arcs, 20 pairs, 0 citations): re-run a `grep -rl` cross-citation count over
  `frontier/B318*/`, `frontier/B1069*/`, `frontier/B1216*/`, `frontier/B1222*/`,
  `frontier/B1276*/` for each arc's own directory naming the other four's arc numbers;
  expected 0/20 unless a later arc (post-2026-09-10) added a joining citation — check whether
  any arc number > B1324 now cites more than one of the five in the same file.
- Claim 7 (K3 sort): DOCUMENTARY in the sense that the sort itself is a literature/text-reading
  exercise over seven already-sealed prereg documents, not a new numeric computation; the
  discriminating fact to recheck is whether B1066 R-A/R-B and B1075 are correctly classified as
  "hearing asked for its own commodity" — re-read `frontier/B1066*/PREREG*.md` and
  `frontier/B1075*/PREREG*.md` to confirm each literally asks for a *magnitude* (not a phase or
  ratio-of-magnitudes that could be reclassified as orientation-flavoured).
- Claim 1/2 (Dirichlet unit rank formula and exclusivity): DOCUMENTARY — standard number theory,
  independently checkable in one line with `sympy`/`pari`: for `d<0` quadratic, unit group is
  finite (rank 0); for `d>0`, rank 1, verified already by many banked arcs (B1069, B1216).

## 6. SUPERSESSION
- §4 of the memo (the "structural" complementarity hypothesis explaining the seven misses) is
  **explicitly superseded by the memo's own addendum 2**, same file, one day later ("REFUTED BY
  ITS OWN CONDITION"). This is the single most important internal fact: **do not cite §4 or the
  memo's headline complementarity as extending to explain the value-crossing misses** — only
  §§1–3 (the pure unit-theorem fact and the citation count) survive.
- No later memo number in `INDEX.md` was found retracting §§1–3 or the citation count.
- The owner register (`THE_OWNER_REGISTER.md` ~line 4844) references "K3 ran the day after that
  sentence was written and was REFUTED — R100 / memo 195," confirming the refutation is treated
  as final within the corpus, not itself later reversed.

## 7. GRADE PROPOSAL
**REGISTER** for §§1–3 (documentary: a correct, checkable but non-computational unit-theorem
observation plus a citation-count measurement worth a row, not an arc) combined with
**SUPERSEDED** for §4 (the hypothesis is dead by the memo's own addendum 2, refuted on its own
pre-registered kill condition) — one sentence why: the load-bearing mathematical content
(Dirichlet unit theorem exclusivity, and the 5-arcs/0-citations gap) is real but small and
documentary, while the more ambitious claim built on top of it in the same memo was killed one
day later by its own author using its own pre-registered test, so nothing here should be banked
as an open arc beyond a citation-hygiene note.
