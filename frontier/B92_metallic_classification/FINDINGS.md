# B92 — the metallic family as a classification (Paper 0, Layer 1)

**Status: `proven` (computer-assisted, finite verification).** Standalone number theory / `GL(2,ℤ)`; no
physics, no Origin-core claim; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b92_metallic_classification.py`. (The *motivation* for characterizing the family rather than
choosing a seed is recorded in `paths/philosophical/METALLIC_FOUNDATIONS.md` and is **not** used here.)

## The classification
The metallic mean `λ_m=(m+√(m²+4))/2` is the dominant eigenvalue of the companion `M_m=[[m,1],[1,0]]`
(trace `m`, det `−1`). Three equivalent descriptions, all verified to give `λ_m`:
1. **self-reference** `x = m + 1/x` (the minimal one-shift-one-reciprocal equation);
2. **continued fraction** `λ_m = [m; m, m, …]` (purely periodic, period 1);
3. **Möbius** `z ↦ m + 1/z` = the action of `M_m` on `ℙ¹`, fixed point `λ_m`.

## The operative condition (the census)
Among non-negative hyperbolic unimodular `2×2` matrices, the dominant eigenvalue is **purely-periodic
period-1 ⟺ det = −1**; then `trace = m`, eigenvalue `= λ_m`. Verified for **all 66 such matrices with
entries ≤ 5** (the det=+1 cases all show a preperiod or longer period).

## MyCalc-2 — the conjugacy census
The CF period of the dominant eigenvalue is a `GL(2,ℤ)`-conjugacy invariant (the cutting sequence of the
geodesic). **Verified consistency:** the period is constant across all matrices of each `(trace, det)`
class over the census; for `det=−1`, every trace-`m` matrix has period 1 with repeat-block `(m)` and
eigenvalue `λ_m` — i.e. all are conjugate to the companion `M_m`. So the family is `{M_m : m≥1}` **up to
`GL(2,ℤ)` conjugacy (recoding), with `m` free** — a computed statement, not a posited one.

## Refinement (a) — det=−1 is the operative *extra* condition
The four naive premises (two letters, substitution, invertibility `det=±1`, expansion) do **not** select
the metallic family — they admit `det=+1` cases, e.g. `M_1²=[[2,1],[1,1]]` (positive, expanding,
automorphism, det `+1`). The operative extra condition is exactly **`det=−1`**; it is not derivable from
"simplest" without a metric.

## MyCalc-5 — the contingency / systole boundary
`m` is the conjugacy invariant (the trace), and **no conjugacy invariant distinguishes a single `m`** —
the family leaves `m` free. Selecting `m=1` (golden) requires a metric: `m=1` is the **systole**, the
shortest closed geodesic `2 log λ_m` on `H/GL(2,ℤ)`. The lengths
`0.962 < 1.763 < 2.390 < 2.887 < 3.294 …` increase with `m` and `m=1` minimizes. So **"the family is
determined; the member is contingent (on a metric)"** is a precise mathematical statement (handoff §5),
with no philosophy invoked.

## Scope (honest)
- `proven` here = a finite computer-assisted classification over entries ≤ 5 + the standard
  conjugacy-invariance of the CF cutting-sequence (cited in Phase G2). The *full* `GL(2,ℤ)`
  class-structure (ideal-class subtleties at larger trace) is not enumerated — the statement is "over the
  census + the known invariant," and the metallic det=−1 classes are the clean part.
- The link `det=−1 ⟺ the tower's parity` is **B93** (Phase C); G1 (universality) is **B94**.

```bash
python frontier/B92_metallic_classification/probe.py
python -m pytest tests/test_b92_metallic_classification.py -q
```
No physics; proven core P1–P16 untouched; outreach dormant.
