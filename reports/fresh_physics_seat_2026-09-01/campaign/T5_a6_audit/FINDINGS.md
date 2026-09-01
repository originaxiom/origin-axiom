# T5 — THE A6 RELABELING FEASIBILITY AUDIT

**Cell:** T5 (outside evaluation seat campaign, 2026-09-01)
**Cell dir:** `reports/fresh_physics_seat_2026-09-01/campaign/T5_a6_audit/`
**Verdict: FEASIBLE** — class (a) [AXIOM-CONSUMER] is EMPTY over the swept corpus. One
near-witness examined and cleared with a typed residual (§6). Proposal: `PROPOSAL.md`.
**Gate 5:** clean — no measured SM value appears in any computation of this cell; no
object-side comparison was designed, so nothing needed to be HELD.

---

## 1. Conventions (stated per E23)

- **Census names:** SnapPy `NonorientableCuspedCensus` / `OrientableCuspedCensus` naming:
  `m000` = the Gieseking manifold (nonorientable, one ideal regular tetrahedron),
  `m004` = the figure-eight knot complement. Orientation of m004 = SnapPy's default
  triangulation orientation.
- **Double cover** = the orientation double cover, computed by SnapPy
  `Manifold.orientation_cover()`.
- **CS normalization:** all Chern–Simons values quoted in SnapPy's `chern_simons()`
  normalization (defined mod 1/2 on oriented cusped manifolds); "CS ∈ 2-torsion"
  means 2·CS ≡ 0 in ℝ/(1/2)ℤ, i.e. CS ∈ {0, 1/4}, matching B1224/B1227's usage.
- **Matrix conventions:** shears L = [[1,1],[0,1]], R = [[1,0],[1,1]]; the unsquared
  golden matrix M = [[1,1],[1,0]] (det = −1); M² = [[2,1],[1,1]] (the monodromy A; written "RL" as a matrix product R·L per LAW_MAP GC-3, "LR" in the word-order convention of UNIQUENESS_THEOREM — an E23-class two-convention collision in the corpus, flagged in VERIFICATION.md) (re-verified here,
  `reverify_gieseking.txt`). The record's LR-vs-RL order convention (A7 of
  `docs/UNIQUENESS_THEOREM.md`) is untouched by this audit.
- **"Orientation consumes"** is judged against the relabel target: orientation as
  **closing #0** (the observer's first closing: choosing the sheet of the double cover /
  squaring the monodromy), with the object = m000 / the ℚ(√−3) commensurability class.

## 2. Sweep and coverage modulus (honest statement)

Script: `sweep_orientation_consumers.py`. Outputs: `sweep_hits.tsv` (4648 hit lines),
`sweep_summary.txt`.

**Swept (1394 files):** all 1137 `frontier/*/FINDINGS.md` that exist; all top-level
`docs/*.md` plus `docs/{anatomy,atlas,audits,dossiers,handoffs,progress,views}/**/*.md`;
all `papers/**/*.tex` and `papers/**/*.md`. 629 files carried ≥ 1 hit.

**Skipped:** frontier artifacts other than FINDINGS.md (RESULTS.json, compute.py, etc. —
the FINDINGS is the banked claim surface this audit classifies); `reports/` (evaluation
output, not object record); `legacy/`, `story/`, `speculations/`, `knowledge/`, `src/`,
`core/`, `scripts/`, `philosophy/`; `tests/` (not swept — lock files assert banked
verdicts, they do not introduce new consumers). Root-level `.md` files were not in the
sweep glob; `CLAIMS.md` (P9/P10/P34/P35/P52) and `docs/UNIQUENESS_THEOREM.md` and
`docs/THEOREM_LEDGER.md` were read by hand and appear in the table below. Residual risk:
an orientation consumer living ONLY in a skipped artifact class (e.g. a compute.py with
no FINDINGS trace) would be missed; given the repo's banking discipline (nothing banked
without a FINDINGS), this risk is assessed low.

**Terms swept:** orientation, orientable, orientation-reversing, amphichiral,
Chern–Simons/CS, spin structure/spin lift/Pin, det = −1, Gieseking, m000, double cover,
complex volume, SL(2,ℂ)/PSL(2, lifts, knot complement/Reid.

## 3. MB12 — bite control, RUN, both directions

**Criterion:** the sweep is valid only if the KNOWN orientation-consumers appear in its
output (Chern–Simons; the spin payment B1141; complex volume; Reid/knot-in-S³;
Gieseking). If any is absent → sweep failed → DEGRADED regardless of the table's shape.
The verdict itself fails in the other direction if any class-(a) witness is found →
BLOCKED.

- **Positive run (this corpus):** ALL FIVE PRESENT (`sweep_summary.txt`):
  chern-simons PRESENT, B1141 PRESENT, complex-volume PRESENT, Reid/knot-in-S3 PRESENT,
  Gieseking PRESENT. Sweep valid.
- **Negative control (criterion CAN fire):** the same bite check run over a corpus slice
  that genuinely lacks the known consumers (`docs/ERROR_LEDGER.md` alone) **FIRED**:
  chern-simons ABSENT, complex-volume ABSENT → exit-2 / DEGRADED path taken
  (`negative_control_output.txt`). The criterion fails in both directions; MB12 satisfied.

**Independent re-verification of the decisive geometric facts** (`reverify_gieseking.txt`,
run in this cell with SnapPy): m000 nonorientable; vol(m000) = 1.01494160641 =
½·vol(m004) = ½·2.0298832128; orientation_cover(m000) ≅ m004 (`is_isometric_to` True);
H₁(m000) = H₁(m004) = ℤ; CS(m004) = 1.35e−16 ≈ 0; det M = −1, M² = [[2,1],[1,1]] (the monodromy A; written "RL" as a matrix product R·L per LAW_MAP GC-3, "LR" in the word-order convention of UNIQUENESS_THEOREM — an E23-class two-convention collision in the corpus, flagged in VERIFICATION.md).

## 4. The evidence table

Classes: **(a) AXIOM-CONSUMER** — requires orientation to exist before any
observer/closing vocabulary (breaks under the relabel). **(b) DATA-CONSUMER** — uses
orientation as an input of the oriented representative's description (survives with
orientation supplied as closing #0). **(c) NEUTRAL**.

| # | Consumer arc / surface | Where (citations) | Class | Why / relabel fate |
|---|---|---|---|---|
| 1 | Chern–Simons values, CS sign law, CP-sign = CS-sign | B128, B152, B289, B303, B458, B813, B1197, B1224–B1227; P9 (`CLAIMS.md`) | **(b)** | CS is defined only on ORIENTED manifolds — precisely "input of the oriented description." Under the relabel, CS is a function of (object, closing #0); the sign flip under the other sheet IS the B289 sign law. B1224: amphichirality pins CS to 2-torsion {0, ¼}; B1226/B1227: CS(m004) = 0 exactly is the further contingent datum "the complex volume is real." Survives. |
| 2 | Complex volume (Vol + i·CS) | B458, B813, B1226; `papers/metallic_one_object/PAPER.md` | **(b)** | Phase is mirror-odd; closing #0 fixes it. Magnitude (Vol) is object-side (B1168). Survives. |
| 3 | Spin structures / spin lift / Pin⁻ payment | P52 (B279), B1141 (spin payment), R021 verified as B1175 (Gieseking Pin⁻ restriction), B1208 | **(b)** | Spin structures live on the oriented representative — closing #0 must precede them. STRONGER: the selection itself (exactly one of m004's two spin structures extends to m000) consumes the PRE-closing object. The parent is an active computational site; the relabel matches how the mathematics is already used. |
| 4 | SL(2,ℂ) vs PSL(2,ℂ) lift | B1112 (projective hatch), B813 | **(b)** | The record itself banked: canonical holonomy is projective; the SL(2,ℂ) lift is a spin-structure choice — the same axiom→closing move one storey up. Survives verbatim. |
| 5 | Reid's theorem / knot-in-S³ statements | `papers/P2_trinity/PAPER.md` (double uniqueness), `papers/candidates/PC27_one_arithmetic_knot/`, `papers/P3_THE_PAPER/main.tex` l.147 | **(b)** | "The unique arithmetic knot" is a statement about an oriented S³ embedding — available only after closing #0. Checked: Reid is used downstream as naming/organizing (the trinity synthesis, PC27), NEVER as the genesis selection (the genesis is the C1–C6 construction; `CLAIMS.md` does not invoke Reid). The relabel keeps closing #0 prior to every invocation. |
| 6 | Amphichirality: census, criterion, involution identity | P34/P35 (B134/B136), P9, B152, B318, B605, B711; 83-member family census (`papers/P3_THE_PAPER/main.tex` l.673) | **(b)** | Under the relabel these become **theorems-of-the-construction**: every hyperbolic orientation double cover is amphichiral with mirror = deck involution (02_A6_VERDICT §4; B605 computed the m004 instance — the amphichiral involutions ARE the Gieseking deck transformations). The census converts from evidence to instances. |
| 7 | P10 sieve — amphichirality as one of four suggestive filters | `CLAIMS.md` P10 | **(b)**, reweighted | The proved content of P10 (trace-3 sieve) runs over SL(2,ℤ) monodromies — the oriented family, post-closing; fine. Honest note: the relabel REWEIGHTS the amphichirality filter (it is automatic for any orientation double cover, so it selects the construction-type, not 4₁ among covers). No breakage: P10 already marks these filters "documented, not proven to uniquely select." |
| 8 | Chirality / CP bit, orientation character | B713, B144, B944, B467 (F2: the one uncancelable bit IS the orientation character — the Gieseking bit), B1083 (P-bit as closing) | **(b)** | Already observer-side in the record's own doctrine. B467/F2 literally identifies the bit with the Gieseking descent. Corroborates. |
| 9 | The mirror-parity × dimension law | B1168 (C5 investigation) | **(b)** / corroboration | The record's own decider: object = mirror-even ∩ dimensionless; observer = mirror-odd ∪ dimensionful, with orientation the mirror-odd completion. This IS the relabel's content, independently derived. |
| 10 | W₀ obstruction | B1163 | **(b)** / corroboration | Three routes converge: the object CANNOT self-supply an orientation (amphichirality refuses it). The observer must — i.e., a closing. |
| 11 | Two-column law citing C5 | C11 (`docs/THEOREM_LEDGER.md`) | **(b)** | Consumes the representative choice after it is made ("the name is geometric and does not survive closure"). |
| 12 | Sister-pair separators (m003 at ¼ vs m004 at 0; mirror-odd cusp data of m003) | B1226, `papers/P3_THE_PAPER/main.tex` l.726–728 | **(b)** | Oriented-census data; post-closing by construction. |
| 13 | B530 "orientation axis" of the combinatorial object (symplectic part of golden growth) | B530 (firewalled reading) | **(c)** | The object supplies the mirror-odd SLOT (the axis), and B530 itself says "the object's one silence is on its own orientation axis" — the BIT is not self-supplied. Consistent with closing #0; not a consumer of the axiom. |
| 14 | Ledger/view mirrors (VERDICT_LEDGER, CAMPAIGN_STATUS, OPEN_LEADS, THE_SPINE, progress files — the top hit-count files) | `docs/views/`, `docs/progress/`, etc. | **(c)** | Restatements of the arcs above; no independent consumption. |
| 15 | F2 pricing frames the sibling family as det = +1 | B749/F2, B1003 | **(c)** | Fork-pricing methodology holds the other links fixed while varying A2; under the relabel it holds closing #0 fixed. Neutral. |
| 16 | `docs/UNIQUENESS_THEOREM.md` axiom A3 (det = +1, monoid ⊂ SL(2,ℤ)) | `docs/UNIQUENESS_THEOREM.md` §1; CLAIMS conditional C1 | **(b)** — the near-witness, examined in §6 | Orientation DOES appear in an axiom list before the object exists — but the theorem is CONDITIONAL, and relabeling its hypothesis A3 → closing #0 preserves the implication verbatim. Cleared with one typed residual (§6). |

## 5. The subtle candidate: does the GENESIS chain consume orientation before the object?

Checked against `docs/THEOREM_LEDGER.md` C1–C6, B749 (P019's fork table, read in full),
B1003.

- **C1 (Morse–Hedlund)** and **C2 (Hurwitz extremality)** are combinatorial — no
  orientation exists yet (no manifold exists yet).
- **C3 (inexhaustibility)** and **C4 (the geometric carrier)** are orientation-free: F8
  shows ℚ(√−3) is bought at geometrization, and geometrization of the UNSQUARED mapping
  torus already buys it — the Gieseking's shape field is ℚ(√−3)
  (02_A6_VERDICT, verified item 2; commensurability invariance).
- **Orientation enters exactly at C5**, as the choice between the det −1 primitive step
  (whose mapping torus is m000, hyperbolic, vol ½·vol(m004), dilatation φ — B749/F5,
  re-verified here) and its square (m004, dilatation φ²). The continued-fraction
  combinatorics of C1–C2 has the det −1 step as its PRIMITIVE period (one CF step matrix
  has det −1; M² = A = [[2,1],[1,1]], convention note above) — so the pre-squaring object is the one the combinatorics hands
  over, and the squaring is a choice made at C5 and nowhere earlier. **The chain runs to
  a well-defined hyperbolic object BEFORE the orientation choice.** C6 (Thurston/Riley,
  monodromy [[2,1],[1,1]]) is the oriented representative's realization, after the
  choice. **The genesis chain is NOT an axiom-consumer: C5 relabels to closing #0 with
  no reordering of any other link.**

## 6. The near-witness, cleared: `docs/UNIQUENESS_THEOREM.md` A3

This is the ONE place in the swept+hand-checked corpus where orientation sits inside an
axiom list prior to the object: A3 ("orientation-preserving, det = +1, update monoid in
SL(2,ℤ)") in the minimal-record axiomatization behind conditional claim C1. Why it is
class (b), not (a): the theorem is a conditional forcing ("given A1–A6, the persistent
sector A = LR is forced up to order convention"); re-typing the hypothesis A3 as closing
#0 leaves the implication and every lock untouched — it becomes a forcing theorem about
the oriented observer's description, exactly parallel to C5 → closing #0. Substantively,
A3's content is the exclusion of the pure swap S = [[0,1],[1,0]] from the primitive
monoid, and the unsquared golden matrix factors as M = L·S with M² = LR (verified:
det M = −1, M² = [[2,1],[1,1]]) — so A3 is literally the c-as-swap/deck-transformation
bit stated at matrix level, which is where the relabel already puts it.

**Typed residual (missing datum, non-blocking):** the GL(2,ℤ)-level uniqueness statement
— that A1, A2, A4–A6 WITHOUT A3 force M up to the swap (the matrix-level parent of the
forcing, whose mapping torus is m000) — is NOT computed anywhere in the record. B749/F5
supplies the manifold-level parent identification only. The relabel does not need this
datum (the conditional theorem survives as stated), but it is the one computation that
would upgrade closing #0's parent object from "identified" to "forced" at the matrix
level. Type: a finite symbolic computation over GL(2,ℤ) monoid words, same shape as the
existing `tests/test_uniqueness_theorem.py` lemmas.

## 7. Verdict

**FEASIBLE.** Class (a) is empty over the swept corpus (1394 files, 629 with hits, 4648
hit lines; bite control passed positively, and demonstrated able to fire on a negative
control). Every genuine orientation consumer found — Chern–Simons and its sign laws,
complex volume, spin/Pin and the B1141 payment, SL(2,ℂ) lifts, Reid/knot-in-S³
statements, the amphichirality corpus — consumes orientation as data of the oriented
representative, which is exactly where the relabel (A6 → closing #0) places it. The
genesis chain itself consumes orientation only at C5, the representative choice. Three
arcs (B1163, B1168, B467/F2) independently corroborate the observer-side placement, and
B1141/R021 already compute THROUGH the pre-closing object. One typed residual (§6),
non-blocking. The relabeled ledger is written in `PROPOSAL.md` and is proposed only —
per cell rules, no file outside this cell directory was modified.

## 8. Files in this cell

- `sweep_orientation_consumers.py` — the sweep + built-in bite control (exit 2 on failure)
- `sweep_hits.tsv`, `sweep_summary.txt` — raw hits and per-file counts
- `negative_control_output.txt` — MB12 negative control (bite criterion fires)
- `reverify_gieseking.txt` — independent SnapPy re-verification of the decisive facts
- `PROPOSAL.md` — the relabeled ledger
- `FINDINGS.md` — this file
