# B135 — The Lee–Yang bridge is m=1-specific; the m=1 match is at modular-data level (V124)

Phase D of the approved program (the Lee–Yang physics push), done honestly and firewalled. B132/S8 + S030 established
that at level k=3 the σ₃ Galois conjugate of the SU(2)_3 even part (Fibonacci) gives the Yang–Lee / M(2,5) data
(`d_τ=−1/φ`). Phase D asks: is there a metallic *family* of Lee–Yang realizations, and at what level does the m=1 match
hold? Re-derived in-sandbox.

**One-line result.** The Lee–Yang bridge is **m=1-specific**: only the golden mean `λ₁ = φ < 2` is a quantum dimension
(`2cos(π/(k+2)) < 2` forces m=1); for m≥2, `λ_m > 2`, so **there is no metallic family of Lee–Yang CFTs**. The metallic
*family* is the family of distinct aperiodic **spectral** objects (`K010`, trace field ℚ(√(m²+4))), **not** a family of
Lee–Yang minimal models. The single golden bridge (m=1 → M(2,5)) is real at **modular-data level** (fusion rule +
quantum dimension + S-matrix Galois conjugate + central charge) — stronger than fusion-rule-only — but it is **emergent
non-equilibrium physics** (the Lee–Yang edge), firewalled from fundamental physics. MATH + emergent-physics tier
(POSTULATED). Nothing to `CLAIMS.md`; P1–P16, B85, S031, the merged B124–B134 untouched.

## Results

- **D1 — m-specificity.** `λ_m = (m+√(m²+4))/2 < 2` only for m=1 (golden `= 2cos(π/5)`); m≥2 have `λ_m > 2`, not a
  `2cos(π/(k+2))` quantum dimension → no Lee–Yang/minimal-model realization. So **no metallic family** of Lee–Yang CFTs;
  the bridge is the single golden case. (Re-confirms B127/M-3 in the Lee–Yang framing.)
- **D2 — the m=1 match at modular-data level.** The σ₃ Galois conjugate (ζ₅→ζ₅³) of the Fibonacci MTC
  (`1, τ; τ²=1+τ; d_τ=φ`) is the Yang–Lee MTC (`d_τ=−1/φ`); the rank-2 S-matrix `S=(1+d²)^{−1/2}[[1,d],[d,−1]]`
  Galois-conjugates Fibonacci → Yang–Lee (verified, S⁴=I both); central charges Fibonacci (G₂)₁ `c=+14/5` → Yang–Lee
  M(2,5) `c=−22/5` (`c_eff = c − 24h_min = 2/5`). The modular data is **standard** (audit R3: Jeffrey 1992,
  Dong–Lin–Ng 2015, Lawrence–Zagier 1999); the framework supplies the fusion rule + the golden dimension.
- **D3 — honest calibration of S030.** The match is at the level of {fusion rule, quantum dimension, S-matrix Galois
  conjugate, central charge} — **not** a full RCFT identification (no torus partition-function / character match; the
  framework's object is the hyperbolic, non-unitary complex-CS quantization, related to M(2,5) via the quantum
  dimension/fusion, not a proven RCFT equality). S030 stays **TESTED-POSITIVE** but **scoped to modular-data level,
  m=1-specific, emergent**.

## Reproduce

```
python frontier/B135_lee_yang_m_specific/probe.py
python -m pytest tests/test_b135_lee_yang_m_specific.py -q
```

**Tier.** MATH + emergent-physics (POSTULATED). S030 sharpened (m=1-specific, modular-data level). Nothing to
`CLAIMS.md`; P1–P16, B85, S031, B124–B134 untouched. Ledger **V124**.

**Anchors:** B132/S8 + `S030` (the σ₃ realization), B127/M-3 (λ_m<2 iff m=1), `K010` (the spectral family — what the
"family" actually is), `docs/NOVELTY_AUDIT.md` (R3). External: Jeffrey 1992; Dong–Lin–Ng 2015; Lawrence–Zagier 1999;
Lee–Yang / M(2,5); Peng et al. 2015 (the observed Lee–Yang edge).
