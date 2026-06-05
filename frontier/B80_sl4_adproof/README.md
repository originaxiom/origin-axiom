# B80 — the SL(4) tower from first principles (Phase 2, the a_d proof at n=4)

Proves `char(J(m)) = char(M⁻¹)·char(M)·char(M²)·char(M³)·char(M⁴)·char(−M²)·(t−1)²(t+1)` for the SL(4)
fixed-line Jacobian — **exactly, symbolically in `m`** — via the **CRT/F_p** route.

- **`build_jm.py`** — computes `DT_0(m)` at integer `m=1..8` over 5 primes using the exact F_p ε-series
  engine (`B58_phaseA/jacobian_closure.py`), interpolates in `m` mod p, **CRT + rational-reconstructs**
  to `J(m)` over ℚ[m], then `sympy.factor(char(J(m)))` and gates vs the tower and B65.
- **`jacobian_m_crt.json`** — the reconstructed `J(m)`.
- **`FINDINGS.md`** — why this is new vs B65 (numerics) and B70 (stalled over ℚ[m]).

**Result.** `MATCH = True`: `char(J(m))` factors exactly as the SL(4) metallic tower, and the char poly
is **identical to B65** (basis-independent gate). This does what B70's symbolic-ℚ route couldn't — by
doing the linear algebra over F_p (exact, fast) and reconstructing ℚ[m] only at the end. The `e₂`
two-block barrier is bypassed (the `n×n` matrix arithmetic auto-enforces the closure). Relabels the
SL(4) tower from "computer-assisted numerics" to "from a first-principles ε-series construction."

```bash
python frontier/B80_sl4_adproof/build_jm.py
python -m pytest tests/test_b80_sl4_adproof.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
