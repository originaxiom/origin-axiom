# Repository State Report — whole-repo reaudit

**Date:** 2026-06-03. **Type:** MAPPING (not a refactor). **DoD:** this report + a punch-list;
trivially-safe fixes applied, everything non-trivial PROPOSED; no premature closes. Audited at
`main` @ `6d3b5f6` (PR #26).

## 0. Verdict

Foundation is clean. One branch (`main`), no orphans. The 15-claim proven core (P1–P16, P14
unused) is unchanged and test-locked. All SL(n) trace-map tower work lives in `frontier/`/PC12
with honest labels — **nothing from the tower is masquerading as proven core.** The refuted
formulas (`3n^2-10n+11`, `2(n-2)(n-3)`, `mult(3)=3`/`max(n-d,1)`) have **no surviving assertions
as true** — every occurrence is in a "refuted / corrected-misconception / brief's" context. The
new cotangent-subtraction kill is present and correctly stated. Suite green (141 passed, 1
intentional skip). One trivially-safe fix applied (stale `(uncommitted)` ledger statuses); 4
non-trivial items proposed below. Open doors are all honestly labeled — they are KNOWN, not
resolved.

## 1. Branch inventory

| branch | status | last commit | purpose |
|---|---|---|---|
| `main` | active | `6d3b5f6` (PR #26) | trunk |

After `git fetch --prune`, **only `origin/main` remains.** Every feature branch was merged and
deleted; the work is verified present in `main` (dirs `frontier/B55,B56,B60–B65,B66,B67,B68`,
`papers/candidates/PC12_*`, `paths/E21_*` all exist). Merged via PRs #16–#26 (this-session work)
and earlier-session merges (B55/B56 = c1-structure, B60, E21, pc12-literature, pc12-review-ready).
**No orphaned or abandoned branch.** (The transient pre-prune listing of b61…pc12-review-ready was
stale local remote-tracking refs, now pruned.)

## 2. Claims inventory (proof-status labels)

**Proven core — `CLAIMS.md`, 15 claims, each test-locked** (status labels: proven/conditional/open/dead):
- P1–P6, P8, P10–P13, P15, P16 — exact algebra / standard sieve. Correctly `proven`.
- **P7** — "Sympy-verified" exact gluing identity. `proven`; *computer-assisted-exact* (defensible).
- **P9** — figure-eight / m003 census data (vol, H1, CS, amphichirality). `proven`; *SnapPy/known-facts,
  software-verified* (these are established census facts, but the label rests on software + literature,
  not a hand proof). **FLAG (mild):** label as software-verified census data.
- Conditional: **C1, C5** — correctly `conditional` (axioms motivated, not forced).
- Field-theoretic lift (P15/P16 → field equation, B6–B9) — explicitly **"conjectured, not proven."** Correct.

**Frontier ledger (`VALIDATION_LEDGER`, V1–V23)** — labels reviewed; the SL(n) tower rows are
correctly qualified:
- V14 (B63) "**PROVEN (computer-assisted, over Z[m])**" — correctly qualified (good template).
- V16 (B65) "SYMBOLIC FACTORIZATION (computer-assisted entries)" — correct.
- V17 (B66) "REFUTED (numerical, high-precision)", V19 "VERIFIED (numerical, multi-axis)" — correctly numerical.
- V20 (B67) "VERIFIED (exact derivation)" — exact symbolic, correct.
- V21 (B58) "DEAD (route closed) + VALIDATED (cross-check)" — correct.
- V22 "VERIFIED (symbolic corollary)", V23 "CONSTRAINTS + NO-GO + OPEN" — correct.
- **FLAG: V15 (B64) "PROVEN (symbolic)"** — sympy-verified symbolically for SL(3) and applied as a
  *structural mechanism* (depth-n CH + P=contragredient + Dickson parity) for general n. The general-n
  statement is the mechanism, not a complete hand proof; the bare "PROVEN" mildly overstates it.
  **Proposed** requalification below.

No tower result (B59–B68) is labeled `proven` in the core; all are frontier/PC12 with qualified labels.

## 3. Open doors (located, honestly labeled — KNOWN, not resolved)

| door | status | what closing it takes |
|---|---|---|
| **B58 proper** — `a_d` multiplicities via exterior-power / multi-block (`e_j`, `Λ²V`) CH recursion | OPEN. The cotangent-subtraction and Sym^{2k}/principal-SL(2) routes are CLOSED (B58 Stage 1, V21); the hand proof is the remaining path. | The Λ²V multi-block trace-ring recursion (a from-first-principles symbolic derivation). |
| **m136 / m=2 framing** (overnight Job 3) | OPEN/INCONCLUSIVE. m=2 monodromy `[[5,2],[2,1]]=R^2L^2` bundle = census m136; the B67 (figure-eight) framing does not transfer (best framing residual ~6e-3). | The correct meridian/longitude framing for m≠1, or a symbolic elimination as in B67. |
| **Boundary-unipotent SL(3) figure-eight A-polynomial (GTZ)** (Job 2) | OPEN. The principal Sym^2 lift is the WRONG SL(3) component (NO-GO: nullity unstable 3/3/5/4); the geometric component is boundary-unipotent. | Build boundary-unipotent SL(3,C) reps and compare to Garoufalidis-Thurston-Zickert. |
| **AJ q=1 recursion limit** (Job 6, shelved) | OPEN. The colored Jones has a minimal order-2 recursion (= A's L-degree), but the exact `recursion|_{q=1} = A` identity is unresolved (convention M_rec=q^N=meridian^2; q→1 nullspace ill-conditioned). | The exact q-deformed recursion coefficients + a careful q=1 limit. |
| **SL(5) cotangent full count** (B58 n=5) | PARTIAL only: dim ≥ 111 at deg≤11, single prime, still rising — NOT a validated count. | Cyclic-word / Procesi reduction (brute-force `2^d` words to degree ~14 is memory-infeasible). |
| **PC12 Thm 4** (fixed-line integer splitting) | OPEN (external): `APPARENTLY_NEW`, specialist read pending (V12). | An independent character-variety / algebraic-dynamics specialist evaluation. |

Test "skips" are NOT open doors: `RUN_SLOW` (n=4 recompute) is an intentional opt-in;
`test_snapdata` uses `importorskip("snappy")` (SnapPy is installed, so it runs).

## 4. Consistency check (refuted claims + conventions)

- **`3n^2-10n+11` / excess `2(n-2)(n-3)`** — NO surviving assertion as true. All 8 hits are in
  corrected-misconception / "brief's" / refuted context (B58 FINDINGS, CHANGELOG, PROGRESS, ledger
  V21, step1_cotangent.py). ✓
- **`mult(3)=3` / `max(n-d,1)`** — NO surviving assertion as true. All hits labeled REFUTED (B66
  FINDINGS/README/VALIDATION/probe, CHANGELOG, PROGRESS, ledger V17/V19/V23, frontier/README). ✓
- **Parity-sign / pre-correction tower** — the SL(2)/n=2 parity correction `(t-1)→(t+1)` (V18) is
  consistent everywhere; the DRAFT_NOTE n=2 row reads `(t+1)`; no surviving n=2 `(t-1)`. The B66
  "9 odd-k / 6 even-k" relabel to root-HEIGHT (V18) is consistent across B66 docs + ledger. ✓
- **Probe-3 terminology** — the forward guard is present and correct in CHANGELOG (L301-302) and
  PROGRESS_LOG (L1931-1932): "`Σ|k|` spectral weight, NOT topological entropy (= n·log μ, linear);
  no n^2 scaling, no fixed antisymmetric fraction." No entropy-mislabel survivor. The PC12
  "algebraic entropy = log μ_m" (Bellon-Viallet, = log spectral radius) is the LEGITIMATE,
  distinct notion — no conflict with the guard. ✓
- **Stale (not contradictory) statuses found** — see punch-list: 11 ledger rows carried
  `(uncommitted)` though merged (FIXED); PC12 docs predate B58/B66/B67 (stale, not contradictory;
  PROPOSED update).

## 5. Test / suite state

- **142 collected; 141 passed, 1 skipped.** Suite green.
- Coverage: proven core P1–P16 (`test_algebra`…`test_derived_potential`, `test_uniqueness_theorem`,
  `test_snapdata`); the tower B61–B68 (`test_b61_sl5` … `test_b67_figure_eight_apolynomial`,
  `test_b58_stage1`); PC12 (`test_sl3_metallic_trace_maps`, `test_sl3_symbolic_m_factorization`,
  `test_pc12_draft_skeleton`, …); public-surface scan (`test_public_surface_scan`, 3 checks).
- Skips: `test_b58_stage1::test_n4_recompute_dim_30` (opt-in `RUN_SLOW`, ~40s); `test_snapdata`
  guarded by `importorskip("snappy")` (SnapPy 3.3.2 installed → runs).
- Forbidden tokens: `test_public_surface_scan` passes; no AI-assistant / surname hits in
  tracked surface. "Origin Axiom" in math code: the only hits are `from origin_axiom import …`
  PACKAGE imports in the OLD physics probes (B1/B5/B6/B8/B9) — legitimate code (the proven-core
  package is named `origin_axiom`), NOT promotional framing; the trace-map probes B48–B68 are clean.

## 6. Kill-ledger coherence

`docs/atlas/FAILURE_ATLAS.md` is a prose-category obstruction map; **there is no `#N` kill-counter
convention** in the repo (the "#25/#26/#27" numbering is external/informal — recorded here so it is
not mistaken for a repo invariant). Documented kills/obstructions: source-free-zero, commutative
cancellation, selector/measure/units-inserted, gauge/particle-dictionary-missing, 3+1D-bridge-missing,
observable-missing, numerology-killed-by-controls, **figure-eight I=1/4** (B56, ledger V4 DEAD),
**Aubry self-duality at λ=m** (B57, ledger V7 DEAD), **fixed-line Jacobian needs the ambient trace
map (SL(n)≥4)**, and the **NEW "Cotangent-Subtraction Route To The Tower Multiplicities — CLOSED"**
(B58, present and correctly stated, reinforcing: the Sym^{2k}/principal-SL(2) decomposition is dead
from the multiplicity side too, and the numerical rep-perturbation tower is exhausted at n≥6 by gauge
degeneracy). **No kill silently revived;** the ledger DEAD/route-closed rows (V4, V7, V21) match the
atlas.

---

## Punch-list

**APPLIED (trivially-safe):**
- [x] `VALIDATION_LEDGER`: 11 stale `(uncommitted)` commit-statuses → `(merged)` (branches verified
  deleted, work present in `main`). Stale text only; no claim content changed.
- [x] Verified the Probe-3 forward guard is present and correct (no edit needed).

**PROPOSED (non-trivial — NOT applied; review before changing):**
- [ ] **V15 (B64) label.** Requalify "PROVEN (symbolic)" → e.g. "computer-verified symbolic for
  SL(3); structural mechanism for general n" — the general-n statement is the mechanism, not a
  complete hand proof. (Claim-status judgment; do not silently downgrade.)
- [ ] **PC12 docs** (`DRAFT_NOTE.md`, `PAPER_CARD.md`, `FALSIFIABILITY_MATRIX.md`,
  `LITERATURE_POSITIONING.md`). They predate B58/B66/B67 and do not mention: the SL(6) multiplicity
  result (`|k|=3 = 2`, `max(n-d,1)` refuted, B66), the figure-eight A-polynomial derived from the
  trace map (B67), or the cotangent-route closure (B58). Stale, not contradictory — propose folding
  these into the PC12 appendix/positioning before any external hand-off.
- [ ] **CLAIMS.md "Last updated 2026-05-29"** — refresh, noting the proven core (P1–P16) is unchanged
  through all B58–B68 frontier work (so the date lag is not claim drift; a one-line note suffices).
- [ ] **CLAIMS.md P7/P9 provenance** — optional footnote that P7 is sympy-verified and P9 is SnapPy /
  census data (software/literature-verified), to keep the "proven" basis explicit. Minor.

**No premature closes:** every open door in §3 is left open and labeled; the goal was to KNOW them.
