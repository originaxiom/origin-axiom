# B74 — higher-spin / W_N grading test (Path C)

Does the rank-`n` metallic **Dickson tower** literally match the **W_N higher-spin** spectrum of SL(N)
Chern–Simons (spins `2..N`)? Exact sympy test.

- **`probe.py`** — (1) verifies the W_N charge-conjugation grading `tr((−Xᵀ)^s)=(−1)^s tr(X^s)` on a
  generic traceless `X` (sl 3/4/5); (2) verifies the Dickson parity `L_s(−m)=(−1)^s L_s(m)` is the same
  `−w0`; (3) tabulates W_`n` spins `{2..n}` vs the rank-`n` Dickson positive powers and the extras.
- **`FINDINGS.md`** — the split verdict.

**Result.** The **parity grading** is a *literal shared object* (STRUCTURAL): both are `−w0` of
`A_{n−1}` acting on a degree-`k` invariant by `(−1)^k` (B62: `P=θ=−w0`; B64: proven). The **full
spectrum** is **not** a literal match — the Dickson tower (negative powers, sign sectors, growing
multiplicities) is strictly richer than the W_N spin list; clean bijection only at `n=3`. The
**dynamical** reading "metallic eigenvalues = higher-spin mode growth rates" has no supporting
computation → **SPECULATIVE-ANALOGY**. Real but 2+1D/representation-theoretic; no 3+1D bridge.

```bash
python frontier/B74_higher_spin_grading/probe.py
python -m pytest tests/test_b74_higher_spin_grading.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
