# B896 — M1: the S₃-harmonic analysis — the dictionary is one table (trivial 99.96%); the asymmetry is near-maximally frame-breaking

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** computed (float, on banked B889/B890/B891 artifacts; exact pass registered as follow-up)

## The question (M1, the meditation's highest-yield item)

Every banked frame-indexed structure decomposes under S₃ (the Galois group of
μ permuting the three frames) into isotypics: **trivial** (frame-symmetric),
**standard** (frame-breaking, 2-dim — mixing-shaped), **sign** (orientation).
The meditation's conjecture: physics = trivial; the small leakages = standard;
the ℤ₂ obstruction = sign. Computed here on B889's three dictionary tables and
B890/B891's sealed-cell deviations.

## The alignment had to be SOLVED, not assumed (a caught model error)

The naive model — one block permutation per frame, rows fixed — left a bimodal
residue (6 rows aligned, 5 stuck at ~0.44 standard fraction). The error: under
a frame relabeling the **rows permute too** (the SM pieces attached to foreign
sectors reshuffle). The joint solve (3!×3! block perms × Hungarian row
assignment, dim-matched) gives per-frame relabelings with residuals
1.7×10⁻² (frame 1) and 4.6×10⁻⁴ (frame 2) — the recurring per-frame asymmetry
visible already in the alignment residuals (36× ratio).

**The representative note:** the best-fit relabelings are transposition-like
(frame 1: singlets (0 2 1), octets (2 0 1); frame 2: singlets (1 0 2), octets
(1 0 2)) and do NOT compose cyclically. Not an anomaly: in a Galois S₃ orbit
the frame-to-frame identifications are coset representatives, and each frame's
stabilizer is a transposition — representative choice is not canonical. The
exact determination of the induced S₃ 1-cocycle is registered (N7).

## Result 1 — the dictionary is ONE table: trivial fraction 0.9996281

Jointly aligned, the three 11×6 mass tables stack to a family whose
**trivial (frame-symmetric) fraction is 0.99963; standard fraction 3.72×10⁻⁴**.
Per-row standard fractions: three rows at 10⁻²¹–10⁻⁹ (exactly symmetric —
the law rows), the rest at 10⁻⁶–3.3×10⁻³ — **the frame-breaking content is
concentrated precisely in B889's leakage rows**. The conjecture's first
clause holds with numbers: the laws are trivial-isotypic; the mixing-shaped
content is standard-isotypic and small.

## Result 2 — the deviation patterns are near-maximally frame-breaking

The sealed cells' per-frame max-deviations, split into mean + standard:

| cell | values (frames 0,1,2) | standard fraction | of the max 2/3 |
|------|----------------------|-------------------|----------------|
| B890 (vacua)  | 1.05×10⁻², 1.66×10⁻⁴, 1.72×10⁻³ | **0.549** | 82% |
| B891 (matter) | 7.23×10⁻³, 4.60×10⁻³, 1.17×10⁻¹ | **0.598** | 90% |

(For nonnegative 3-vectors the standard fraction is bounded by 2/3.) The
per-frame asymmetry — recorded without interpretation in B885/B890/B891 —
now has its number: **the operational S₃-breaking magnitudes live almost
maximally in the standard isotypic**, while the tables themselves are 99.96%
trivial. The breaking is small in size and near-maximally mixing-shaped in
pattern.

## Result 3 — the sign placement (rep theory, exact)

Functions on the three frames contain NO sign isotypic (ℂ³ = trivial ⊕
standard as an S₃ rep) — so no single-frame table can carry it. The sign
class lives in oriented pair data, and the banked ℤ₂ commutation cocycle
(∏c = −1, B892) **is** the nontrivial sign-class there. The meditation's
third clause is a placement theorem, not a computation.

## Files

- `s3_harmonics.py` → `results.json`
- Locks: `tests/test_b896_s3.py`

## Depends on

B889 (tables), B890/B891 (deviations), B892 (the ℤ₂ cocycle), B866/P69
(the S₃ orbit). Follow-up registered: N7 (the exact cocycle pass).
