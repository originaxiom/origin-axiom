# T5_a6_audit — ADVERSARIAL VERIFICATION

**Verifier seat, 2026-09-01. Verdict on the cell's claimed FEASIBLE: CONFIRMED**
(one non-load-bearing E23-class labeling defect found and typed below; it must be
corrected before PROPOSAL.md is adopted, but it does not touch the verdict logic).

Nothing in this cell dir was modified except the addition of this file. Nothing outside
this cell dir was modified.

## 1. Re-runs (everything reproduced)

- **Sweep** (`sweep_orientation_consumers.py`): re-run from a scratchpad copy (OUT
  redirected so the cell's banked outputs were not overwritten). Result:
  `files swept: 1394; files with hits: 629; hit lines: 4648`, bite control all-PRESENT,
  exit 0. `diff` against the banked artifacts: **`sweep_hits.tsv` and
  `sweep_summary.txt` are byte-identical** (hits compared sorted; summary compared raw).
- **File-count decomposition independently verified**: 1137 `frontier/*/FINDINGS.md`
  (of 1191 frontier dirs) + 88 top-level `docs/*.md` + 38 in the seven docs subdirs +
  131 `papers/**/*.{tex,md}` = 1394. Exact match.
- **SnapPy re-verification** (fresh in-verifier run, not a re-read of
  `reverify_gieseking.txt`): m000 nonorientable; vol(m000) = 1.01494160641,
  vol(m004) = 2.0298832128 (ratio exactly ½ to printed precision);
  `orientation_cover(m000).is_isometric_to(m004)` = True; H₁ = ℤ both sides;
  CS(m004) = 1.3498693e−16; det M = −1, M² = [[2,1],[1,1]]; M = L·S verified
  ([[1,1],[0,1]]·[[0,1],[1,0]] = [[1,1],[1,0]]). All match the cell's numbers.
- **Sister-pair separator (table row 12) re-verified**: CS(m003) = 0.25000000 = ¼,
  CS(m004) ≈ 0. Matches the {0, ¼} 2-torsion framing of B1224 and PROPOSAL T2.

## 2. MB12 attack

- **Was the control run?** Yes. The positive direction is built into the sweep script
  (exit 2 on any absent known consumer) and ran (exit 0, all five PRESENT). The
  negative control output is banked (`negative_control_output.txt`).
- **Reproducibility gap, closed**: the negative-control *script* was NOT banked — only
  its output. I reconstructed it (same TERMS regexes run over `docs/ERROR_LEDGER.md`
  alone) and reproduced the banked state exactly for chern-simons (False), spin (True),
  complex-volume (False), knot-in-s3 (True). The banked `B1141: True` reproduces under
  a content-based check (`docs/ERROR_LEDGER.md` contains the string "B1141" once, in
  the E53 row) but not under the main script's path-based check (`"B1141" in h[0]`) —
  so the control used a slightly different B1141 criterion than the main sweep. This
  does not affect the FIRED conclusion: the criterion fires on ANY absent item, and
  chern-simons + complex-volume are absent on the slice under both readings. The
  criterion demonstrably fails in both directions; MB12 is satisfied.
- **Residual MB12 limitation (noted, not degrading)**: the bite control validates the
  sweep's RECALL only. The (a)/(b)/(c) classification is judgment, not automated, and
  no control can make a misclassified (b)→(a) fire mechanically. Mitigation checked:
  the cell genuinely applied the class-(a) test to a candidate (the A3 near-witness,
  §6) rather than rubber-stamping, and my spot-checks of the load-bearing
  classification anchors (below) all held.

## 3. Classification spot-checks (scope attack)

- **Genesis claim (§5)** checked against `docs/THEOREM_LEDGER.md`: C1/C2 are THEOREMs
  (combinatorial), C3/C4 are pre-orientation axioms (C4: "ℚ(√−3) is bought at
  geometrization and nowhere earlier"), C5 is literally headed "[AXIOM — orientation;
  PRICED, the most expensive]" with "Orientation = choosing the child of the parent",
  C6 the oriented realization. The cell's claim "orientation enters exactly at C5"
  matches the ledger verbatim.
- **Near-witness A3** checked against `docs/UNIQUENESS_THEOREM.md`: the theorem
  self-describes as conditional ("This is a *conditional* result"); A3 is
  "Orientation-preserving, det = +1, monoid ⊂ SL(2,ℤ)"; A7 explicitly reserves the
  LR-vs-RL order as the irreducible labeled input. M = L·S verified numerically. The
  class-(b) reading (retype the hypothesis, implication survives) is sound; the typed
  residual (GL(2,ℤ)-level forcing uncomputed) is accurately typed — I confirmed no
  such computation exists (`tests/test_uniqueness_theorem.py` lemmas are SL(2,ℤ)-side).
- **Row 3 (B1141)**: `frontier/B1141_*/FINDINGS.md` contains "the Gieseking extension
  exists over EXACTLY ONE of the two spin structures" — the parent IS an active
  computational site, as claimed.
- **Row 1/T2 (B1224)**: its FINDINGS header is literally "amphichirality forces CS to
  be 2-TORSION". Matches.
- **Row 10 (B1163)**: "The object is amphichiral: it *cannot* pick" — the
  cannot-self-orient obstruction is as cited.
- **Row 5 (Reid)**: `CLAIMS.md` contains ZERO occurrences of "Reid" — the claim that
  the genesis never invokes Reid is verified, not just asserted.
- **Coverage-modulus attack**: the 54 frontier dirs WITHOUT any FINDINGS.md (1191−1137)
  are entirely outside the sweep. I grepped all 54 for orientation/CS/Gieseking/m000
  content: hits exist (B1_gluing_chern_simons, B263, B502, B571 CHIRALITY_DOSSIER,
  etc.) but on inspection they are speculative/non-banked probes (B1's own header:
  "Nothing in this directory is promoted to CLAIMS.md") or restatements of banked
  arcs that WERE swept (B571 cites B469; B469's FINDINGS is in the sweep). No
  class-(a) witness found there. The cell's "risk assessed low" caveat survives an
  actual look.

## 4. Convention attack (E23) — ONE REAL DEFECT FOUND

**The LR/RL label is used inconsistently and, in four places, incorrectly under the
cell's own stated convention.** With the cell's §1 conventions (identical to the
repo's: L = [[1,1],[0,1]], R = [[1,0],[1,1]]), matrix products are
LR = [[2,1],[1,1]] and RL = [[1,1],[1,2]]. `docs/UNIQUENESS_THEOREM.md` line 11 pins
the record's naming: "A = LR = [[2,1],[1,1]]". But:

- FINDINGS §1: "M² = [[2,1],[1,1]] = RL" — **wrong label** (should be LR);
- FINDINGS §3 and §5: "M² = RL = [[2,1],[1,1]]", "M² = RL" — **wrong label**;
- `reverify_gieseking.txt`: "(= RL = [[2,1],[1,1]])" — **wrong label**;
- PROPOSAL.md closing #0 statement: "M → M² = RL = [[2,1],[1,1]]" — **wrong label,
  and this is the line that would enter the record on adoption**;
- FINDINGS §6 and PROPOSAL bookkeeping item 3: "M² = LR" — **correct**, contradicting
  the above within the same documents.

Assessment: the NUMERIC matrix [[2,1],[1,1]] is correct in every occurrence and is the
correct object (the record's A); the audit explicitly holds the A7 order convention
untouched; no classification, no count, and the class-(a)-emptiness verdict depend in
any way on which word names the matrix. So this is a labeling slip of exactly the
repo's E23 class — internal to the deliverable, self-contradicted, non-load-bearing —
NOT a verdict-changing error. **Required correction before adoption**: replace "RL"
with "LR" in the four locations above (or re-derive under an explicitly stated
temporal/left-action word convention — but the repo's pinned naming is LR).

Other conventions checked and clean: CS normalization (SnapPy `chern_simons`, mod ½ on
oriented cusped manifolds; {0, ¼} 2-torsion usage matches B1224 and reproduces
numerically on m003/m004); census naming (m000/m004 verified live in SnapPy); the
"double cover = orientation_cover()" convention (verified isometric to m004).

## 5. Gate 5

The cell's computations are a text sweep and SnapPy geometric invariants — value-free.
Grep of all cell files for measured SM values (fine structure, Weinberg, masses,
GeV/MeV, 137, 0.23...) returns only "1137" (a file count). No object-side comparison
was designed, so nothing needed to be HELD. Gate 5 clean, as claimed. (The T2 item in
PROPOSAL.md — CS ∈ {0, ¼} — is a mathematical statement about SnapPy invariants, not a
measured value; the B1226/B1227 contingency split is honestly kept.)

`git status`: no modified tracked files; the only untracked entries are other cells'
verification artifacts and `reports/recompute/`. The cell's "no file outside the cell
dir modified" claim holds.

## 6. Verdict

**CONFIRMED.** Every number reproduces byte-identically; the MB12 control ran and
demonstrably bites in both directions (negative control reconstructed and reproduced);
the genesis, near-witness, and all spot-checked classification anchors hold against
their source documents; the coverage caveats are honest and survive an adversarial
look at the unswept dirs; Gate 5 is clean. Two defects, neither verdict-changing:
(1) the E23-class RL/LR mislabel (§4 above — fix before PROPOSAL adoption);
(2) the negative-control script was output-banked only (reconstructed here; bank the
script alongside the output in any future cell).
