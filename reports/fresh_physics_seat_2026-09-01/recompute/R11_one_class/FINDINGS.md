# R11 — B1183 THE ONE-CLASS THEOREM — recomputation (Ring R2)

**Cell verdict: MATCH** (41/41 own checks pass; banked reproduce.sh re-run byte-identical;
one partial-vacuity note on the banked script's coverage, discharged by this cell's
independent recompute; one non-mathematical metadata discrepancy noted).

## Blind-first record

**Read BEFORE writing my code:**
- `frontier/B1183_one_class_theorem/FINDINGS.md` (the claim text only).
- Source-arc committed data, as the cell brief instructs: `frontier/B1169_qualia_parity_synthesis/FINDINGS.md`
  (first 60 lines — to name the four probes), `frontier/B1174_z2_identification/FINDINGS.md` (first 60
  lines — the mirror=chirality=Gal leg), `frontier/B1163_w0_attempt/ADDENDUM_orientation_theorem.md`
  (grep excerpts — the amphichirality theorem), `frontier/B760_qp4_closure/compute.py` + `output.txt`
  (the chord data), `frontier/B238_su32_levelrank/su32_wrt.py` (loaded as the committed S/T source).
- NOT read before coding: anything in `frontier/B1183_one_class_theorem/verification/`,
  `arc_verdict.json`, `b1183_results.json`.

**Read AFTER my 41/41 pass:** `arc_verdict.json`, `b1183_results.json`,
`verification/reproduce.sh`, `verification/one_class.txt`, and the paper scope note
(`papers/P3_THE_PAPER/main.tex:708`, `SPEC.md:300`).

## The four probes, as reconstructed blind

From B1169 S1 ("four 'cannot self-close' probes") and B1183's restriction list:

| # | probe | source arc | the Z/2-set | freeness under c | non-collapse |
|---|-------|-----------|-------------|------------------|--------------|
| P1 | orientation | B1163 | {+Vol, −Vol} via K↪ℂ | Bloch–Wigner odd: D(z̄)=−D(z) (1e−12); m004 amphichiral, sym group order 8 (SnapPy) | Vol(m004)=2·D(e^{iπ/3})=2.0298832128 ≠ 0 |
| P2 | chord-sector sign | B760 pt 8 | {+√3, −√3} = sign Im f(ω), f=−2(2−u) | Im f(ω̄) = −Im f(ω), exact (sympy); general real-coeff lemma proved deg≤2 | Im f(ω) = √3 ≠ 0, exact |
| P3 | eigenvalue choice | B760 pts 2/7 | {ζ₅, ζ₅⁴} of the weld block | conj = σ₄ swaps them, exact | ζ₅ ≠ ζ₅⁴; weld block rebuilt from B238's committed su3_data(2): eigenvalues ζ₅^{±1} at 1e−10, tr=1/φ, det=1, conj(B)=εBε⁻¹ with ε²=−I |
| P4 | mirror/chirality | B1174/B942 | the two embeddings K=ℚ(√−3)↪ℂ | mirror conjugates m004's holonomy traces (SnapPy, traces a,b,ab at 1e−9) | Im tr(a) ≠ 0 (trace field genuinely imaginary) |

**The one involution c** (complex conjugation on ℂ) verified through its restrictions, exactly:
c|K: ω̄=ω² (Gal generator, flips √−3); c|ℚ(ζ₅): ζ̄₅=ζ₅⁴=σ₄, fixing √5=2(ζ₅+ζ₅⁴)+1 (exact);
c|ℝ trivial. Char poly x²−(1/φ)x+1 kills ζ₅ and ζ₅⁴ exactly; Φ₅=(x²−(1/φ)x+1)(x²+φx+1) exact;
the 15/32 coupling fraction is c-invariant at ω AND ω̄ (exact, from B760's committed d-list —
re-verified though B1183 only cites it).

## The vacuity boundary (the paper's own scope note), verified

Enumeration: for 2-element free ℤ/2-sets, **both** bijections are equivariant (2/2) — the
equivariance hypothesis is free, exactly as `papers/P3_THE_PAPER/main.tex:708` and `SPEC.md:300`
("2 of 2") state. Contrast control: at |G|=3 only 3/6 bijections are equivariant, so the vacuity
is |G|=2-specific. The load-bearing content is therefore the case-by-case freeness/non-collapse
under the SAME c — which is what the table above verifies.

## Planted-positive controls (all caught)

- **A** — ℚ(√5) value bit (B957/B1174's refuted leg): c fixes √5 ⇒ the set {±√5} is NOT free
  under c. My test flags it. (This is the real discriminating power: a probe on a REAL quadratic
  field cannot be the c-class.)
- **B** — collapsed set: sign Im f(u) at real u has Im=0 ⇒ non-collapse fails. Caught.
- **C** — wrong involution: σ₇ (z₁₂→z₁₂⁷) fixes ω (z₁₂²⁸=z₁₂⁴) and flips √3 — the orientation
  set is not free under it. Caught, matching B1174's leg-by-leg census.

## Diff against the banked record

1. **Arithmetic legs (a)–(c): MATCH, and strictly stronger.** Every assert in the banked
   `reproduce.sh` (2cos72=1/φ; root sum/product; ε²=−I; √5 identity; conj(ζ₅)=ζ₅⁴; conj(ω)=ω²;
   sign-carrier flip) is confirmed by my blind code — symbolically exact where the banked script
   used 50-digit numerics (1e−45). The banked sign-carrier uses a sample f=3z²−2z+7; I proved the
   general real-coefficient lemma (deg≤2, symbolic) AND B760's actual f=−2(2−u) with the ±√3 values.
2. **Banked reproduce.sh re-run** (byte-faithful, in `banked_rerun/` copy to avoid touching the
   committed tee target): exit 0, output **byte-identical** to the committed `one_class.txt`.
3. **Partial-vacuity note (does not change the verdict).** B1183's own verification script has
   machine content (asserts) only for legs (a)–(c); leg (d) — the torsor identification — and the
   freeness/non-collapse of P1 (orientation) and P4 (mirror-on-traces) are unconditional prose
   prints, inherited by citation from B1163/B1174. Within B1183's own script those legs could not
   have failed. This is fenced by the arc itself ("cited, not re-run") and by the paper's scope
   note relocating the content to freeness/non-collapse; this cell independently re-established
   the P1/P4 legs (SnapPy amphichirality + trace conjugation; Bloch–Wigner oddness; Vol≠0), so the
   theorem's full load-bearing surface is now machine-checked somewhere.
4. **Metadata discrepancy (non-mathematical).** `FINDINGS.md` header says `creates_law: false`
   while `arc_verdict.json` carries `creates_law: true` with the B1211 correction record
   (2026-08-29, was:false→true). The FINDINGS document (authored the same day, B1207) reproduces
   the stale pre-correction value. The claim, verdict and evidence are unaffected.
5. **Conventions (E23):** same ω=e^{2πi/3}, same σ₄, same ε=[[0,−1],[1,0]]. No mismatch.

## Artifacts (this cell only)

- `r11_blind_recompute.py` — the blind recomputation (41 checks). Three sympy zero-tests needed a
  `rewrite(cos)`/`expand_complex` route (exp-form vs radical simplification depth) — a CAS
  plumbing fix, not a math change; all pre-fix failures were of this kind.
- `r11_blind_output.txt` — full run log, 41/41 PASS.
- `banked_rerun/` — byte-faithful re-run of the committed `reproduce.sh` + its regenerated
  `one_class.txt` (diffs clean against the committed file).

Gate 5: clean — Galois/cyclotomic arithmetic, torsor combinatorics, SnapPy geometry of m004;
no measured SM value anywhere in this cell.
