# B76 (Path F2/F3) — cusp-torsion × quantum group at roots of unity (the speculative-tail closure)

**Date:** 2026-06-05. **Status:** exact sympy; the number/level correspondence is literal
(computer-assisted/STRUCTURAL), the categorical "anyonic TQFT" reading is SPECULATIVE-ANALOGY (V28).
Standalone low-dim topology / TQFT mathematics; **no Origin-core claim**; proven core P1–P16 untouched.
Script: `probe.py`. Test: `tests/test_b76_cusp_quantum_group.py`.

## F2 — does the cusp k-set connect to a quantum group at a root of unity?

The cusp-torsion law (B69, `m=1..6`) puts the cusps of the metallic-`m` bundle's trace-relation curve
at `x = 2cos(π/k)`, `k ∈ {3,…,m+2}`, `k ≡ m (mod 2)` (at `x=2cos(π/k)` the generator `a` is elliptic
of order `2k`). Roots of unity are exactly where quantum groups / anyonic TQFT live.

**The literal identification (exact).** `2cos(π/k) = [2]_q`, the quantum integer at `q = e^{iπ/k}`
(`[2]_q = q + q⁻¹ = 2cos(π/k)`, verified `k=3..8`). So the cusp value at `k` is exactly the SU(2)
quantum-group `[2]`-value at the primitive `2k`-th root of unity `q=e^{iπ/k}` — the
**SU(2)\_{k−2} (WZW level `k−2`)** Temperley–Lieb–Jones special value. The map:

| `m` | cusp k-set `{3..m+2}`, `k≡m(2)` | SU(2) WZW levels `{k−2}` | torsion orders `{2k}` |
|---|---|---|---|
| 1 | `{3}` | `{1}` | `{6}` |
| 2 | `{4}` | `{2}` | `{8}` |
| 3 | `{3,5}` | `{1,3}` | `{6,10}` |
| 4 | `{4,6}` | `{2,4}` | `{8,12}` |
| 5 | `{3,5,7}` | `{1,3,5}` | `{6,10,14}` |
| 6 | `{4,6,8}` | `{2,4,6}` | `{8,12,16}` |

`a` elliptic of order `2k` (geometry) ↔ `q` a primitive `2k`-th root of unity (quantum group): the
**same order-`2k` cyclotomic torsion** on both sides. The **golden/Fibonacci** point
`φ = 2cos(π/5)` sits at `k=5 → SU(2)₃` — and it appears **not** at `m=1` (whose cusp is `k=3`,
`2cos(π/3)=1`, `SU(2)₁`) but for **odd `m≥3`** (the `k=5` member of `{3,5}`,`{3,5,7}`).

**The categorification barrier (V28, cited).** The metallic *fusion* rule `τ²=1+m·τ` is a unitary
anyon model **only for `m=1`** (golden = Fibonacci; Ostrik's rank-2 classification). For `m≥2` there is
**no** unitary fusion category — no metallic-anyon / MTC family.

### F2 verdict (split, labelled)

- **LITERAL at the level of the special numbers / torsion orders (STRUCTURAL).** The cusp `k`-set **is**
  the SU(2) quantum-group root-of-unity level set — both are the cyclotomic values `2cos(π/k)`,
  order-`2k` torsion. This **closes B69's open "reconciliation" item** (the metallic eigenvalue vs the
  torsion points `2cos(π/k)`): they coincide because both are the SU(2)\_{k−2} root-of-unity data.
- **NO categorical lift (SPECULATIVE-ANALOGY).** There is no MTC/TQFT realization of the metallic
  *family* (V28): no functor from the metallic-bundle cusps to a modular tensor category for `m≥2`. The
  deeper "anyonic TQFT" reading rests on nothing more than "both are roots of unity" (cyclotomic) — the
  thin geometry↔TQFT boundary B69/V28 already flagged. Honest expectation matched.

## F3 — parity mechanism × Chern–Simons (disposition: subsumed by V56)

Already answered by **V56 (B74)**: the proven even/odd-`|k|` → P-symmetric/antisymmetric split (B64)
**is** the W_N charge-conjugation grading of the spin-`k` current by `(−1)^k` — both are `−w0` of
`A_{n−1}` acting on a degree-`k` invariant. STRUCTURAL, recorded under V56; no separate computation.
Noted here so Path F is banked in one place.

## Disposition

Path F **closed**: F1 (the m-axis of degree=rank) banked under V57/B75; F2 (this) = literal
number/level coincidence + V28 categorification barrier; F3 = subsumed by V56. No kill reopened, no
metaphor dressed as a finding. Proven core untouched.

## Reproduce

```bash
python frontier/B76_cusp_quantum_group/probe.py
python -m pytest tests/test_b76_cusp_quantum_group.py -q
```
