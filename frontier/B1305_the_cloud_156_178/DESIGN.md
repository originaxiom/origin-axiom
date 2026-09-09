# B1305 — THE CLOUD 156–182, SLICE A (memos 170, 172, and 169's census): DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-08 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 row B1305, parts (i) and (ii); part (iii) (the c_eff line, memos
173–178) and the four memos the cloud added today (179–182, head `ec15923d`) are SCHEDULED to slice B, with Phase 3's DESIGN ·
**Cloud head pinned:** `origin/outside-bench` @ `ec15923d` (2026-09-08), worktree `oa-audit-seat/cloud-seat-ec15923d` ·
**Read in full before this seal:** memo 172 THE_SENSE_CENSUS (79 lines) + `certificates/sense_census.py` (65 lines); memo 170
THE_ONE_WALL (270 lines, with its 2026-09-07 corrections and addendum) + `partial_filling_strict.py` (the grid: degrees 4–8, covers with
≥ 2 cusps, cusp 0 filled at slopes (1,0), (1,1), (2,1), (3,1), (1,2), (3,2); the predicate: all tetrahedra positively oriented, ≥ 1 cusp
left, CS ∉ {0, ¼} mod ½ by more than 10⁻⁶) + `six_cusp_reachability.py`; the cloud's INDEX rows 165–182; the cloud harvest-debt table
(inputs/, 2026-09-08: memos 165–178 all ABSENT on main). **Seat certificates re-run in the pinned worktree before the seal (receipts in
`verification/cloud_memo*_rerun.txt`, RC=0 each):** `sense_census.py` on the cloud's own tree (2417 files, 17.0 MB; `Chern-Simons` 73/34 =
46.6 %, `character` 3474/12 = 0.3 %, `logarithmic` 8/0, `non-semisimple` 18/0, `non-rational` 7/0, `resurgence` 71/12, `modular` 898/54;
two-sided control PASSED — the memo's numbers exactly); `six_cusp_reachability.py` (covers per degree 2–12: 1, 1, 2, 4, 11, 9, 10, 11,
38, 26, 62; max cusps 1, 1, 2, 3, 2, 3, 2, 3, 5, 4, 4; zero with ≥ 6); `partial_filling_strict.py` (98 candidates of 113, 27 distinct
(degree, cusps, slope) triples; m004 CS = 9.0e−17 and the unfilled degree-5 cover CS = 3.9e−16 both FAIL the predicate, correctly);
`partial_filling_repro.py` (the isosig table). Nothing below was computed with main's own code before the seal.

## 0. The rules' lines

- `already_banked.py "sense census" "false comfort" "technical sense" "partial filling" "six cusps" "amphichirality inherited" "three regimes"`:
  no settled arc ≥ 6 of 7 terms (nearest at 5: B1273, main's B1276 — the latter is the Klein-four join, relevant to Q2(g)). Admissible.
- `absence_sweep.py`: "sense census" PRESENT (5 heads — the cloud's branch and the intake surfaces; **no instrument on main**); "false
  comfort" PRESENT (2 heads, same); "six-cusp" PRESENT (6 heads: B1190/GC-6, B1295, the cloud); "partial filling" PRESENT (4 heads —
  on main exactly ONE hit, `frontier/B738_pathfinder_compiler/kill_graph.json`, "B172 partially filled them", about matrix cells: memo
  170's corrected count, confirmed here). So: the sense census is a new instrument for main; partial Dehn filling of a multi-cusped
  cover is a move no main arc has made or killed; the six-cusp question is main's own (B1190) and B1295's.
- **E53 found at the read (Phase 0's item was half-done):** the plan said "cite B1227 in B1294 and B1297". B1294 has the anchor (1 hit);
  **B1297 has 0.** Memo 170's sentence "B1294 … does not cite B1227 once" was true when written and is false now; B1297's omission is
  live and is fixed in this arc.

## 1. The view from above

The cloud's lane 1B is the σ-bridge lane (Vol ≠ 0 / c = 6 / the quantum face). Its two memos here are not σ results: memo 172 is an
INSTRUMENT that fixes a defect in THE ABSENCE RULE ("is the word there?" is not "is the concept there?"), and memo 170 is a JOIN
(B1227's theorem in three value groups: CS, ℝ, ℤ) plus one existence computation (partial fillings break amphichirality while keeping
a cusp) plus its own same-day kill of that computation as a σ route (six cusps unreachable to degree 12). For the main goal this means:
(a) the instrument is adopted if and only if its two-sided control passes on MAIN's tree and my own implementation reproduces theirs on
the cloud's tree — then it becomes the second half of THE ABSENCE RULE; (b) the join is registered at the theorem row (T-MIRROR-ODD-
VANISHES) so the three walls are read as one, which is v3.1 §0's own sentence made a registry fact; (c) the partial-filling move is
exactly v3.1 Phase 2 Arc B's "partial-filling route, priced before anything is computed" — this arc verifies the existence computation
and registers the price (three discrete choices) without opening the route; (d) the six-cusp negative is B1295's census extended by two
degrees, re-derived with main's code. If (a) fails on main's tree the instrument is NOT adopted and the reason is recorded (the cloud's
memos 164/166 set the precedent). Nothing here moves the chirality bit; everything here is hygiene, join, and priced options.

## 2. Pre-registered questions — predictions before the scripts exist; PASS and FAIL both reachable

**Q1 — memo 172, the sense census, adopted or not** (`b1305_sense_census.py`, an INDEPENDENT implementation: file walk, term matching,
marker-in-window test written from the memo's description, not copied).
(a) On the cloud's tree (the pinned worktree, `outside_bench/` excluded as the memo excludes it) with the memo's seven terms, markers
and window ±130: predicted counts EQUAL the cloud's for all seven (occurrence and technical), i.e. their computation is reproduced by
a second implementation. FAIL = any count differs (then the difference is the finding: tokenisation or scope).
(b) On MAIN's tree at HEAD `1ff529f7` (prose `.md`/`.tex` under `frontier/ docs/ papers/`): the two-sided control PASSES (`Chern-Simons`
≥ 10 % technical; `logarithmic` and `non-semisimple` each < 2 %); `character` remains FALSE COMFORT (< 2 %). Counts will differ from
the cloud's (main's tree is larger and now contains the intake text); predicted `character` occurrences > 3474. FAIL = the control
fails on main's tree (then NOT ADOPTED).
(c) MB12 planted controls, both directions, in a scratch copy: a planted file with `logarithmic CFT` raises `logarithmic`'s technical
count by exactly 1; a planted `logarithmic` with no marker within ±130 characters leaves it unchanged; a planted marker just OUTSIDE
the window (131+ characters away) leaves it unchanged. FAIL = any of the three.
(d) If (a)–(c) PASS: adopt as a new checks script (sense census) with `--selftest` (the two-sided control on the live tree + the three
planted controls) and a CLI `sense_census.py "<term>" "<marker regex>"`; WORKING_RULES' ABSENCE RULE gains its second half ("the
concept, not the word": run the sense census whenever the term is a technical notion); PRACTICES gets the note; the cloud is credited
(memo 172 @ ec15923d). The register's `character` finding (3474 occurrences, 12 technical) is recorded as the instrument's first
result on main and as the reason B1191's "no boundary character" sentence must be re-read in Phase 3.

**Q2 — memo 170, THE ONE WALL: the join, the census, the move, the price.**
(a) The join REGISTERED at `T-MIRROR-ODD-VANISHES` (B1227): a regimes note naming the three value groups with their arcs — ℝ/½ℤ (CS ∈
{0, ¼}: B1012, B1064), ℝ (no real selector: B1225), ℤ (net chirality 0 on every closing: B1294) — credited to memo 170; B1297 gains the
B1227 anchor it lacks (E53, dated addendum); B1294's anchor stands. No computation.
(b) Six-cusp reachability re-derived with main's code (`b1305_covers_11_12.py`, B1295's enumeration extended): predicted covers per
degree **11: 26, 12: 62**; max cusps **4 and 4**; cusp-count multisets recorded; degrees 2–10 reproduce main's own B1295 (87 covers,
201 cusps: per degree 1, 1, 2, 4, 11, 9, 10, 11, 38; max cusps 1, 1, 2, 3, 2, 3, 2, 3, 5) as the positive control. PASS = the two new
rows match the cloud's; FAIL = a different count (SnapPy's `covers(d)` is deterministic in count; a mismatch would be a real finding).
(c) The partial-filling existence computation re-derived with main's own SnapPy loop over the SAME grid (degrees 4–8, ≥ 2 cusps, cusp 0,
the six slopes) and the SAME predicate: predicted **27 distinct (degree, cusps, slope) triples** (the stable quantity; the candidate
count is run-dependent and is reported as a range, not asserted); the cleanest witness reproduced from its isosig
`kLLLPLQkcefegijjiijiieldllxtxa_aBbBabBbbacb` (degree 5, 3 cusps): fill cusp 0 with (2,1) → 2 cusps left, all tetrahedra positively
oriented, **CS = +0.157590 ± 10⁻⁶**, distance 0.0924 from {0, ¼}; the two controls (m004 unfilled; the degree-5 two-cusped cover
unfilled) have |CS| < 10⁻⁹ and FAIL the predicate; the withdrawn ±1/24 case reproduces as `contains negatively oriented tetrahedra`
(rejected). PASS = 27 triples and the witness's CS to 6 decimals; FAIL = otherwise. These are SnapPy's unverified numerical CS values
(the memo says so; so does this arc): strong numerical evidence, not certified — Phase 2 Arc B, if it opens the route, certifies.
(d) The price REGISTERED (no I-row, no arc opened): a partially filled cover spends three discrete choices — which cover, which cusp,
which slope — on top of I-26; v3.1 Phase 2 Arc B's text already says the route is priced before computed; this arc writes the price
into OPEN_LEADS L202(b)'s note with memo 170 credited, and the addendum's own kill (six cusps unreachable ⇒ not a σ route) recorded
beside it, so nobody opens it for σ.
(e) §6(a) hexagonal cusps at degree 10 — AGREES with B1295 (16 of 201, in 14 degree-10 covers): VERIFIED by reading; §6(b) "ν^c does two
jobs" — main's B1096 ("ν^c … is exactly what cancels the last non-vanishing invariant (the global B−L pair)") and sm:B1276's cubic
table (row `H_u L ν^c`): VERIFIED by reading, the cross-reference registered as a hint; §5's bench error #20 (a label asserting the
conclusion) and #21 (a "zero" that was one): the seat's own, recorded as SUPERSEDED-BY-SEAT in the ledger.
(f) §6(c) THE FUSION THAT MUST NOT BE MADE, checked on main: main's B1276 identifies B1174's legs with B730's faces, V₄ =
Gal(ℚ(√−3, √5)/ℚ) (quadratic subfields √−3, √5, √−15); B1182 identifies its frame ⟨c, r⟩ with Gal(ℚ(ζ₁₂)/ℚ) (subfields √−3, √3, √−1).
Prediction: **no main surface identifies B1174's legs / B730's faces with B1182's frame / Gal(ℚ(ζ₁₂)/ℚ)** — the two V₄s share only
ℚ(√−3) and are different groups of automorphisms; a grep over docs/ and frontier/*/FINDINGS.md for sentences joining "legs" or
"faces" with "ζ₁₂" or "⟨c, r⟩" returns none that asserts equality. FAIL = such a sentence exists (then it is an instance of B1231's
label-matching class and is corrected at source).
(g) The addendum's fork REGISTERED for Phase 3's DESIGN: the σ bridge cannot be crossed inside the tower to degree 12 (count half dead,
CS = 0 inherited); the live branch is a non-abelian T[M] / a different boundary sector (memo 168 §4's fence; Q11, sent 2026-08-31,
reply pending). No verdict on main changes.

**Q3 — the cloud's memo 169 census (the seat's own six-cusp census to degree 8, which B1295 reproduced independently):** its row in the
harvest ledger reads VERIFIED (B1295 = main's independent derivation; this arc's (b) extends it). Memos 165–168, 171, 173–182 are
SCHEDULED to slice B with their dispositions (173 and 176 partially self-retracted; 164 and 166 NOT ADOPTED by the seat).

## 3. Priors

Q1(a) exact reproduction: 85 % (a second implementation of a regex census usually agrees; the risk is file-set or encoding drift);
Q1(b) control passes on main: 90 %; Q1(c): 95 %. Q2(b): 90 %; Q2(c) 27 triples and the witness: 75 % (SnapPy's cover enumeration order
and numerical solutions vary across runs — the memo says so; the triple set should not); Q2(f) no fusion on main: 80 %.
Expected verdict: **ADOPTED (the sense census) + VERIFIED (six-cusp census; the partial-filling witness) + REGISTERED (the join at
the theorem row; the price; the fork) + E53 fixed (B1297's anchor).**

## 4. Method, controls, discipline

Own implementations only for the re-derivations; the cloud's certificates re-run in the pinned worktree with their own controls
(receipts kept); every count that could have differed is printed; PASS and FAIL branches exist in every script; pytest's own rc; the
seat credited by memo number and pin; the harvest ledger gets one row per memo touched; no seat grade lowered without a computation;
loose relay files never at root. Out of scope: opening the partial-filling route (Phase 2 Arc B), the c_eff line (slice B / Phase 3),
Q11's reply, any σ claim.
