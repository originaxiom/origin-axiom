# R03 — Recomputation of B1160 (anomaly-forced hypercharge) + B1170 census (252/222/2)

**Verdict: MATCH** (both arcs; all banked numbers reproduced blind, exact arithmetic).
One clause of the cell brief (the "Y_q = 0 collapses to vector-like" statement) is **unbanked** —
it appears nowhere in the committed arcs; recomputed and characterized here anyway (see §4).

## Blind-first protocol log

**Read BEFORE computing** (claim statement + banked numbers only):
- `frontier/B1160_hypercharge_forced/FINDINGS.md` (first 80 lines)
- `frontier/B1170_arena_rescope/FINDINGS.md` (first 60 lines)

**Read AFTER my numbers were on disk** (`blind_output.json`, `controls_output.json`,
`controls2_output.json` all written first):
- `frontier/B1160_hypercharge_forced/verification/reproduce.sh` + `hypercharge_check.txt`
- `frontier/B1170_arena_rescope/verification/independent_enumeration.py`
- `tests/test_b1160_hypercharge_forced.py`, `tests/test_b1170_arena_rescope.py`
- greps of `b1160_results.json` / `b1170_results.json` for the Yq=0 clause (absent)

Their committed code was then re-run without modifying their files (B1160's heredoc extracted to
scratchpad because its `tee` would overwrite the committed `hypercharge_check.txt`).

## 1. B1160 core theorem — MATCH (identical conventions, identical numbers)

My blind setup (state counts q:6, u^c:3, d^c:3, l:2, e^c:1; conditions
[SU(3)]^2 Y: 2Yq+Yu+Yd, [SU(2)]^2 Y: 3Yq+Yl, grav^2 Y: 6Yq+3Yu+3Yd+2Yl+Ye, [Y]^3) gave, exactly:

| quantity | mine (blind) | banked |
|---|---|---|
| linear cut | Yl=-3Yq, Ye=6Yq, Yu+Yd=-2Yq | same |
| cubic at Yq=1, Yu=-1+t | **-18(t-3)(t+3)** | -18(t-3)(t+3) |
| roots | t = +-3 | t = +-3 |
| solutions | **(1,-4,2,-3,6)** and (1,2,-4,-3,6) | same two, zero non-SM |
| SM x6 check | (1/6,-2/3,1/3,-1/2,1)*6 = (1,-4,2,-3,6) | SM ratio pattern |

Their `reproduce.sh` uses the *same* conventions (a genuine E23 non-issue: conventions coincide)
and re-runs clean today. Fully homogeneous form (my addition): on the linear solution plane the
cubic factors as **-18*Yq*(Yu+4Yq)*(Yu-2Yq)** — three rays: SM, u^c<->d^c relabel, and Yq=0.

## 2. B1170 census — MATCH (252 / 222 / exactly 2, same survivors, same charges)

Mine (blind, per-slot rational charges, exact nullspace + homogeneous-cubic factorization):
- C(10,5) = **252** contents over the 6-letter alphabet {(3,2),(3b,2),(3,1),(3b,1),(1,2),(1,1)};
- pure [SU(3)]^3 kills **222**, leaving 30;
- exactly **2** contents admit an isolated (rigid), nonzero, chiral, mass-term-free ray:
  {(3,2),(3b,1),(3b,1),(1,2),(1,1)} = the SM 15-plet with charges prop. to (1,-4,2,-3,6)
  = (1/6,-2/3,1/3,-1/2,1) up to scale, and its conjugate — matching banked "both 15-state".

Criterion-robustness (stronger than the banked phrasing needs): among all 30 color-safe contents,
**the only isolated rational rays that exist anywhere are the 3 rays of the two SM-shaped
contents** (nullspace dim histogram 2:12, 3:16, 4:2; the other 10 dim-2 contents have the cubic
vanishing identically -> continuum). So the count "exactly 2" is insensitive to the exact chirality
filter (their sterility = all-charges-nonzero; my no-invariant-bilinear) and to the Witten filter
(they apply it; I did not; same answer). What IS load-bearing is **rigidity**: 4 continuum contents
(AABBE, AABDD, ABBCC, CCDDE in the obvious letters) contain chiral mass-free rational points inside
their solution families — non-rigid, correctly excluded by both codes.

## 3. Controls (exclusion claims must be able to fail)

- **Planted arena extension** (`controls.py`): adding an adjoint letter G=(8,1) -> 66 color-safe,
  **4** rigid survivors, the 2 new ones non-SM (charges prop. to (1, 13/5, -1, -3, -3/5) on
  A D D E G). The instrument finds non-SM survivors when they exist. Consistent in kind with cc3's
  banked robustness note (uniqueness alphabet-dependent; 7 with their adjoint set).
- **Planted non-SM shape** (`controls2.py`): counts (q:6,u:3,d:3,l:4,e:1) -> cubic
  -(9/2)(4t^2-45), solutions irrational (-1 +- 3*sqrt(5)/2, Yl=-3/2, Ye=6) — the pipeline returns
  non-SM answers when the content is non-SM; the SM tuple is not baked in.
- **grav^2 Y-dropped control found NOTHING — and that is a theorem, not an instrument failure**:
  without grav^2 Y the system reduces to Ye^3 = 72Yq^3+36Yq^2*Yu+18Yq*Yu^2, which maps exactly
  (verified: a=2Ye, b=-12(Yu+Yq), Yq=1) to the Mordell/Fermat-cubic curve **b^2 = a^3 - 432** with
  the SM at (12, +-36). That curve has rank 0, torsion Z/3 (literature fact, FLT n=3; not
  re-proved here) — so over Q the SM rays remain the only solutions even without grav^2 Y.
  grav^2 Y is load-bearing over R, redundant over Q on this 15-plet. (Observation only; does not
  contradict B1170's *in-frame* statement about memo 78, which concerns a different system.)

## 4. The Yq=0 branch — computed; the brief's phrasing is UNBANKED and half-right

No committed file in either arc states the "collapses to vector-like, excluded by chirality"
claim (grepped FINDINGS, results JSONs, verification, locks: absent). What the committed code
actually does: B1160's script scale-fixes Yq=1 (silently discarding the branch); B1170's
enumerator sees it as the ray (0,1,-1,0,0) and drops it as "sterile" (a zero charge).
My exact characterization: the branch is the third cubic ray (0,s,-s,0,0);
- the **U(1) charge multiset** {+s x3, -s x3, 0 x9} is negation-symmetric — the hypercharge acts
  **vector-like as a U(1) rep**, and e^c=(1,1,0) acquires a gauge-invariant Majorana bilinear —
  so "excluded by chirality" is right in that sense;
- but the full SU(3)xSU(2)xU(1) content is **not** literally vector-like (Q=(3,2,0) has no
  conjugate partner in the multiset) — "collapses to vector-like" overstates it if read as the
  full gauge multiset. Correct exclusion reasons: sterile / partially-massable / non-chiral U(1).
Since the uniqueness theorem is stated "up to scale" with Yq=1, the banked claim is unaffected;
but "zero non-SM solutions" in B1160's header is exactly true only modulo this discarded ray —
worth one sentence in the arc if ever revised.

## 5. Lock quality note (not a vacuity verdict)

B1170's lock genuinely re-executes the committed enumerator (subprocess, asserts 252/222/2) — a
live check. B1160's lock asserts strings on *committed* text (results JSON + committed
`hypercharge_check.txt`); it would not catch the committed script rotting, though the script does
re-run clean today and its key assertions (factored cubic, SM tuple) are the real numbers. Both
arcs' claims are independently recomputed here, so: MATCH, with the mild note that B1160's lock is
text-asserting rather than re-executing.

## Files (this cell)

- `recompute_blind.py` -> `blind_output.json` (written before reading their verification)
- `controls.py` -> `controls_output.json`; `controls2.py` -> `controls2_output.json`
- `blind_err.txt`, `ctrl_err.txt`, `ctrl2_err.txt` (stderr logs)

## CORRECTION (2026-09-01, later; owner's rule: sweep before concluding an absence)

"UNBANKED — grepped FINDINGS, results JSONs, verification, locks: absent" was a main-only
search. Repo-wide sweep (`../../sweeps/ABSENCE_SWEEP_LOG.md`, row A07): the Yq = 0 branch is
computed in `frontier/B8143_anomaly_lane/` on `paper/structure-genesis-first` (a31456d2; FINDINGS
l.68–71, results.json l.48–50, step1_core.py l.8, 48) as *"{Yq = 0, Yd = −Yu, Yl = Ye = 0} ← a
ONE-PARAMETER VECTOR-LIKE family"*, never integrated to main. My characterization above (third
cubic ray (0,s,−s,0,0); vector-like as a U(1) multiset, not literally vector-like as a gauge
multiset) refines B8143's phrasing rather than supplying a first computation. B8143's claim that
the branch "= B864's third line" is not supported by B864's committed results (no third line
there). Verdict unchanged: on main the branch is silently discarded by B1160 and dropped as
"sterile" by B1170.
