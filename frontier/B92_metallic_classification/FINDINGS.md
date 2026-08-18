# B92 — the metallic family as a classification (Paper 0, Layer 1)

**Status: `proven` (computer-assisted, finite verification).** Standalone number theory / `GL(2,ℤ)`; no
physics, no Origin-core claim; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b92_metallic_classification.py`. (The *motivation* for characterizing the family rather than
choosing a seed is recorded in `philosophy/METALLIC_FOUNDATIONS.md` and is **not** used here.)

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
eigenvalue `λ_m`. The proven statement is that **this period-1 eigenvalue-CF criterion (a `(tr,det)`
invariant) cuts out the metallic discriminants `m²+4`**, and the companion `M_m` realizes each.

> **⚠ CORRECTION (2026-06-15, self-audit).** The original inference "period 1 ⟹ **all** trace-`m` det=−1
> matrices are conjugate to the companion `M_m`" is **false at `m≥4`**. Period-1 is *necessary*, not
> *sufficient*, for conjugacy: by Latimer–MacDuffee the `GL(2,ℤ)`-conjugacy classes with char poly
> `x²−mx−1` are the ideal classes of `ℤ[λ_m]`, counted by the form class number `h(m²+4)`. Computed
> (Sage `BinaryQF_reduced_representatives`): `h = 1` for `m=1,2,3` (companion unique) but **`h=2` at `m=4`**
> (disc 20, the conductor-2 order over `ℚ(√5)`), and `h>1` again at `m=6,8,…`. So the honest statement is
> "the **companion `M_m` is one `GL(2,ℤ)` class** among `h(m²+4)`; the period-1 CF criterion (the proven
> invariant) does not pin a unique class beyond `m≤3`." The det=−1 ⟺ tower-parity result (B93) and the
> systole selection (MyCalc-5) are unaffected; only the "all conjugate to the companion" phrasing is
> corrected. The scope note below already flagged the "ideal-class subtleties at larger trace".

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


---

## ADDENDUM 2026-08-18 — the correction note's class-number table was itself wrong (caught by the W3 biography cell; bench-verified twice over)

The 2026-06-15 correction above is right about the *principle* (period-1 is necessary,
not sufficient; Latimer–MacDuffee counts the classes) but wrong about the *numbers* —
its Sage `BinaryQF_reduced_representatives` call counted an **imprimitive** form at
disc 20 ((2,±6,2) = 2·(1,±3,1), discriminant 4·5 inflated to 20) and the table
inherited the tool's convention instead of the theorem's. The exact primitive table
(this bench, two independent routes: direct Gauss reduced-cycle enumeration under the
ρ-operator, and the order class-number formula h·f·∏(1−(d|p)/p)/[unit index] — for
disc 20: 1·2·(3/2)/3 = 1 with unit index 3 via φ³ = 1+2φ; a third route in the W3
cell cross-validated against PARI):

| m | D = m²+4 | h (primitive, proper) |
|---|---|---|
| 1–5 | 5, 8, 13, 20, 29 | **1** |
| 6 | 40 | **2** |
| 7, 8 | 53, 68 | **1** |
| 9, 10 | 85, 104 | **2** |

**Corrected statements.** The companion `M_m` is the UNIQUE `GL(2,ℤ)` class for every
m ≤ 5 (and for m = 7, 8) — in particular **at m = 4, where the note claimed h = 2**;
the first genuine failure of uniqueness is **m = 6** (disc 40, h = 2), and the note's
"h > 1 again at m = 6, 8, …" is also wrong about m = 8 (h = 1). Through m = 10 the
non-unique cases are exactly m ∈ {6, 9, 10}.

**A structural rider the recomputation exposed.** λ_m·λ_m′ = −1 by the characteristic
polynomial's constant term, so every metallic order ℤ[λ_m] contains a unit of norm −1
and **narrow = wide class number for the entire family** — the defining det = −1
condition itself closes the narrow/wide gap, so the count above needs no convention
caveat.

**Scope.** The det = −1 ⟺ tower-parity result (B93), the systole selection, and every
downstream use were swept (2026-08-18): no other file consumes the wrong clause
(B533's Latimer–MacDuffee leg is over ℚ(√φ), unaffected). Registered: ERROR_LEDGER
E42 (default-call inflation); the W3 cell's catch is recorded in B1069's FINDINGS.
