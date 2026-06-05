# B74 (Path C) — higher-spin / W_N vs the metallic Dickson tower: the literal-match test

**Date:** 2026-06-05. **Status:** exact sympy; the grading match is **STRUCTURAL** (a literal shared
Lie-theory object), the dynamical reading is **SPECULATIVE-ANALOGY**. Standalone trace-map / Lie-theory
mathematics; **no Origin-core / no thesis claim**; proven core P1–P16 untouched.
Script: `frontier/B74_higher_spin_grading/probe.py`. Test: `tests/test_b74_higher_spin_grading.py`.

## Question

SL(N) Chern–Simons in 2+1D has asymptotic symmetry the **W_N algebra** (higher-spin gravity /
Vasiliev): higher-spin currents of spins `s = 2,3,…,N`. The metallic trace-map tower factors over the
Dickson catalog `char(M^k) = t² − L_k t + (−1)^k`, `L_k = tr(M^k)`, `M=[[m,1],[1,0]]`, with powers `k`
running `1..n` (plus a contragredient `char(M^−1)`, sign sectors `char(−M^k)`, growing multiplicities).
**Is there a *literal* correspondence** between the rank-`n` Dickson spectrum and the W_N higher-spin
mode spectrum — spins `s ↔ powers k`, or `L_k ↔` mode data? (The speculative slogan to ground or kill:
"trace-map eigenvalues = growth rates of spin-`n` modes.")

## Verdict — split by layer, labelled honestly

```text
PARITY GRADING       : LITERAL shared object (STRUCTURAL).  The W_N charge-conjugation grading of
                       spin-s currents and the Dickson P-grading of char(M^k) ARE THE SAME involution
                       -- -w0 (the contragredient) of A_{n-1} -- acting on a degree-k invariant by
                       (-1)^k.  Same Lie algebra, same involution: not a coincidence.
FULL SPECTRUM        : NOT a literal match.  The Dickson tower is strictly RICHER: negative powers
                       char(M^-1), sign sectors char(-M^k), and growing multiplicities have NO W_N
                       higher-spin counterpart; W_N (sl, not gl) has no spin-1.  Clean bijection only
                       at n=3 ({2,3}={2,3}); n>=4 diverges.
DYNAMICAL reading    : SPECULATIVE-ANALOGY.  "metallic eigenvalues L_k = higher-spin mode growth
                       rates" has NO supporting computation -- the L_k are not shown to be any W_N CFT
                       spectrum.  The real kernel is invariant theory of sl(n) (2+1D/topological).
```

## What was computed (exact sympy, decisive)

**(1) The W_N charge-conjugation grading, from first principles.** In W_N Toda the spin-`s` current is
the **degree-`s` Casimir** `tr(X^s)` of `sl(N)`; charge conjugation `C` (the diagram automorphism
`= −w0 =` the contragredient `X ↦ −Xᵀ` on the Lie algebra) acts on it by `(−1)^s`. Verified on a
**generic traceless symbolic** `X` for `sl(3),sl(4),sl(5)`: `tr((−Xᵀ)^s) = (−1)^s tr(X^s)`, all `s`.

**(2) The Dickson grading is the SAME involution.** The metallic instance of `−w0`: `P = ` contragredient
`= (m ↦ −m)` (B62: `P = θ = −w0`), and the Dickson parity `L_s(−m) = (−1)^s L_s(m)` (verified `s=1..6`).
So `char(M^k)` sits in the `P`-even sector for even `|k|`, `P`-odd for odd `|k|` (B64, *proven*). The
degree-`k` metallic invariant flips by `(−1)^k` under exactly the involution of (1).

**(3) The literal spectrum comparison** (W_`n` spins `{2..n}` vs rank-`n` Dickson positive powers):

| `n` | W_`n` spins | Dickson positive powers `char(M^k)` | overlap | grading agrees | Dickson extras (no W_`n` current) |
|---|---|---|---|---|---|
| 3 | `{2,3}` | `{2,3}` | `{2,3}` | ✓ | — (only the neg power `char(M^−1)`) |
| 4 | `{2,3,4}` | `{1,2,3,4}` | `{2,3,4}` | ✓ | spin-1 `char(M)`; `char(M^−1)`; sign `char(−M²)` |
| 5 | `{2,3,4,5}` | `{1,1,2,2,3,4,5}` | `{2,3,4,5}` | ✓ | spin-1 `×2`, spin-2 `×1` extra; `char(M^−1)`; signs `char(−M²),char(−M³)` |

On every overlap the W_N charge-conjugation eigenvalue `(−1)^s` and the Dickson `P`-eigenvalue `(−1)^k`
**coincide** — sourced from the two *independent* verified facts (1) and (2), not from one formula. But
for `n ≥ 4` the spectra **diverge**: the Dickson tower carries structure (negative powers, sign
sectors, multiplicities) absent from the W_N higher-spin tower.

## Honest reading

- **The metaphor has a real kernel, and it is exactly identifiable.** The reason "higher-spin tower"
  feels right is that **both objects are the invariant theory of the same Lie algebra `sl(n)`**, graded
  by the same involution `−w0`. The spin-`s` W_N current and the `char(M^k)` factor carry the *same*
  `(−1)^{degree}` charge-conjugation grading because they are the same degree-`k` invariant under the
  same `θ = −w0`. This is **STRUCTURAL and literal** — it sharpens B62/B64 by naming their physics
  shadow precisely, and it is the honest content of the "higher-spin" intuition.
- **But it is representation theory, not a physical bridge.** The match lives entirely in the *static*
  invariant-theoretic grading of `A_{n−1}`. There is **no** computation making the metallic eigenvalues
  `L_k` a W_N CFT / higher-spin mode spectrum; the full Dickson tower is a strictly richer object than
  the W_N spin list. The dynamical slogan stays **SPECULATIVE-ANALOGY**.
- **Consistent with the prior negatives.** This is the same boundary the metallic-anyon probe hit (V28:
  categorifies only at `m=1`) and the `CS_INVARIANT_FAMILY` note (topology, *not* a physics crossing):
  the geometry/rep-theory layer is real and shared; the 3+1D-physics bridge is not there. The higher-spin
  link is **real but 2+1D/topological**, exactly the planned honest expectation.

## Disposition

Path C **resolved**: a *literal* STRUCTURAL grading match (same `−w0` of `A_{n−1}`), correctly **not**
elevated to a spectral identity or a physics claim; the dynamical reading labelled SPECULATIVE-ANALOGY.
No kill reopened, no metaphor dressed as a finding. Proven core untouched.

## Reproduce

```bash
python frontier/B74_higher_spin_grading/probe.py
python -m pytest tests/test_b74_higher_spin_grading.py -q
```
