# B446 — D1: the tower moment law + the twisted SFF (Thermodynamic Campaign, decisive probe 1)

**Status: banked (frontier). Firewalled; nothing to `CLAIMS.md`. Prereg: `PREREGISTRATION.md`
(committed before computation, PR #588). Verdict: LAUNDERS (burden-inversion satisfied, the
exhibited F passed both out-of-sample tests) + one NEW-MATH lemma (novelty pending the lit-gate).
No H1. Exactly the prereg's stated prediction.**

## What was computed (independent rebuild; the 2026-07-06 review pilot was NOT trusted)

The quantized golden cat map `U_N(A)`, `A=[[2,1],[1,1]]`, Weil-formula quantization at odd N;
Hecke desymmetrization by norm-one units `aI+bA` of `ℤ[A]/N` joint-diagonalized with parity;
matrix-element moments of `f = cos 2πx` over the eigenbasis; the SFF. Reproduce-gates passed:

| gate | target | measured |
|---|---|---|
| KR variance, prime N=241/1201/2003 | N·Var → 1.00 (arithmetically-enhanced; RMT would give 1/2) | 0.9959 / 1.0008 / 0.9995 |
| KR 4th moment (SU(2)/Sato–Tate) | m₄/m₂² → 2.00 | 1.929 / 2.020 / 2.003 |
| unitarity / commutators / joint-diag residual | machine zero | ≤5.6e-16 / ≤1.7e-16 / ≤1.5e-10 |
| commutant order at prime p | p−1 (5 split) or p+1 (5 inert) | 240, 1200 (p≡1 mod 5); 2004 (p≡3) ✓ |
| mpmath dps=40 cross-check (N=45 unitarity) | — | 2.3e-41 |

## THE LEMMA (the fixed-cofactor tower law — exact, derived, out-of-sample-verified)

**Setup.** `N = N₁N₂` odd coprime. Write `1/N = u₁/N₁ + u₂/N₂ (mod 1)` (CRT partial fractions,
`uᵢ = inv(N/Nᵢ) mod Nᵢ`). Then (all verified exactly):

1. **Observable factorization** [derived + verified]: `e(j/N) = e_{N₁}(u₁j)·e_{N₂}(u₂j)`, so
   `M_N = M_{N₁}^{u₁} ⊗ M_{N₂}^{u₂}` in the CRT basis.
2. **Parity-reality** [derived + verified ≤1.4e-15]: parity-definite eigenstates give REAL
   `⟨M^u⟩` (P M^u P = M^{−u} = (M^u)†) — this is the mechanism of KR's parity-coherent
   arithmetic enhancement (the prime gate's 1.00 vs generic 1/2), and it makes the product exact:
   `X = Y₁·Y₂` with both factors real.
3. **The twisted-factor structure** [the B355 "composite-level CRT-twist catch", now at the
   eigenbasis level]: the correct factor eigenbases are those of the **character-twisted** Weil
   reps `ψ_{u₁}, ψ_{u₂}` (twist = multiply all phase exponents by uᵢ), with factor observables at
   exponents `uᵢ`. With that bookkeeping the **matrix-element multiset factorizes EXACTLY**:
   at N=135, `X₁₃₅ = {Y₅,ᵢ·Y₂₇,ⱼ}` to 1.6e-13, and `kurt(135) predicted = measured = 4.904533`
   (all six digits). [The untwisted-basis shortcut fails when uᵢ is a non-square — the ~2%
   kurtosis "anomalies" during exploration were exactly this catch; documented as the trap.]
4. **The variance law** [rational, character-independent by Galois-rationality — the 2nd moment
   is fixed by Galois, the 4th is not]:
   `N·Var = S₅ · C₃` along `N = 15·3^k`, with
   - golden: **S₅ = 1/2** (the 5-factor multiset is EXACTLY `{±1/2, 0, 0, 0}` for every
     character — the degenerate/clean form), **C₃ = 3/4** (measured 0.750000 at N=3⁵, 3⁶, all
     characters), so **N·Var = 3/8 at every level** — verified at N = 15, 45, 135, 405, 1215
     and **out-of-sample at N = 3645 (predicted 0.375000, measured 0.375000)**.
   - **kurtosis = K₅·K₃^{(ψ)}(k)** with K₅ = 5/2 exact and the 3-power factor kurtosis drifting
     (3.32→3.70 at 3⁵→3⁶): tower kurtosis **3.75 → 4.59 → 4.90 → 6.51 → 8.09 → 9.24** —
     **the limiting law along the fixed-cofactor tower is a product deformation, NOT the KR
     SU(2)/semicircle law** (whose kurtosis is 2, confirmed at the prime gates).
5. **The m-dependence is exactly the whitelisted 5-splitting mechanism** [the same-class
   control, derived a priori]: silver `A₂=[[5,2],[2,1]]` has **C₃ = 3/4 (SHARED — the pure
   3-power constant is m-independent)** and **S₅ = 5/6** (a generic non-degenerate 5-multiset),
   predicting silver tower `N·Var = 5/8` — **measured 0.625000 at N = 45, 135, 405.** Golden's
   clean `{±1/2,0³}` vs silver's generic multiset is the splitting of 5 in `ℚ(√(m²+4))`:
   **ramified (m=1, 5=disc) vs inert (m=2)** — whitelist mechanism #3. The law's FORM is
   class-generic; every constant is whitelist-derivable.

## The SFF (Q-c): both channels launder, as pre-registered

- **Untwisted SFF = the banked P59 Pisano law, exactly**: full revival `SFF(t) = N` at
  `t = ord(A mod N) = π(N)/2` (60/180/540 at N=45/135/405). The pre-registered launder-control
  CONFIRMED — the quantum-chaos diagnostic reads back the object's known arithmetic.
- **Parity-twisted SFF: revivals annihilated** (SFF = 0.0 at t = ord; derivable —
  `|tr P|²/N = 1/N`), twisted mean ≈ 1/4 vs untwisted late-mean ≈ 2: the eigenphases carry a
  systematic **parity-balanced 2-fold pairing** (the untwisted mean-2 is the degeneracy, the
  twisted mean-1/4 its cancellation). All whitelist-derivable; no anomalous structure.

## Verdict (the campaign's three bins)

- **LAUNDERS — demonstrated, not asserted.** The exhibited F: `N·Var = S₅(m)·C₃` with
  `S₅(m)` determined by the splitting of 5 in `ℚ(√(m²+4))` and `C₃` the m-independent pure-3-power
  constant; kurtosis = the twisted-factor product; SFF = P59 + tr(P). Complexity-capped closed
  forms; **out-of-sample passed at BOTH a second level (N=3645, exact) and a second m (silver,
  derived a priori, exact)** — the burden-inversion rule's full requirement.
- **NEW-MATH (one item, lit-gate COMPLETE — APPARENTLY-UNWRITTEN, precisely scoped):** the
  fixed-cofactor tower law. The adversarial lit-gate (full-text grep of KR Duke 2000 / KR Annals
  2005 / Kelmer AHP 2008 / Olofsson 2008-2010 / KRR short windows / KORS CMP 2025 /
  Bhakta–Shparlinski 2026 + the full citation graphs) found: the CRT/tensor factorization at
  composite N is **KR Duke 2000 §4.1 folklore** (Kelmer states "it is sufficient to understand
  prime powers" and never returns to mixed N); **no paper treats matrix-element moments at any
  mixed composite N, and none works the tower direction p fixed, k→∞** (all prime-power results
  are k fixed, p→∞ — Kelmer's non-KR limit law at p^k is the orthogonal-direction precedent).
  **Referee-honest novelty scope:** (a) the fixed-cofactor tower regime itself, (b) the explicit
  constants S₅(m), C₃ and their arithmetic (5-splitting), (c) the kurtosis drift / product
  deformation of the limiting law. The pointwise factorization alone is a short corollary of KR
  §4.1 and is NOT claimed. Caution inherited from Kelmer Rmk 1.3: moments above the 6th can blow
  up from density-zero exceptional elements — this lemma stays at moments ≤ 4.
- **No H1.** No un-launderable structure. The object's "quantum temperature" layer (moments vs
  level N) reads back: CRT, Galois rationality, the 5-ramification of the golden field, and the
  Pisano order — its own banked frozen arithmetic, re-expressed warm. **The prereg's stated
  prediction, confirmed by computation.**

## Reproduce

```
python3 pipeline.py     # gates + 5-factor + C3 + tower + silver + SFF (~5 min; results.json)
pytest ../../tests/test_b446.py   # the lock
```
Key artifacts: `pipeline.py`, `results.json`, `run_log.txt`. Traps documented in the prereg
(LAPACK 1e-6 clustering; the θ_m-analog here: the character-twisted factor basis).
