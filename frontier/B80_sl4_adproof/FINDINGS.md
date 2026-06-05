# B80 (Phase 2) — the SL(4) metallic tower from first principles (CRT/F_p symbolic-m Jacobian)

**Date:** 2026-06-05. **Status:** computer-assisted (exact modular + CRT), with an **exact symbolic
factorization** over ℚ[m] as the final certificate; prime-stable and gate-checked vs B65. Standalone
Lie/invariant theory; **no Origin-core claim**; proven core P1–P16 untouched. Script: `build_jm.py`.
Test: `tests/test_b80_sl4_adproof.py`.

## The result

The SL(4) fixed-line Jacobian `J(m)`, reconstructed from first principles, satisfies — **exactly,
symbolically in `m`** —
```
char(J(m)) = char(M⁻¹)·char(M)·char(M²)·char(M³)·char(M⁴)·char(−M²)·(t−1)²·(t+1)
```
with `char(±Mᵏ)=t²∓L_k t+(−1)^k`, `L_k=tr([[m,1],[1,0]]^k)` (so `L_2=m²+2`, `L_3=m³+3m`,
`L_4=m⁴+4m²+2`). This is the **SL(4) metallic tower** — the `a_d=(−1,1,2,3,4)`, `b_d=(−2)`
multiplicities — now established from a from-first-principles construction (`sympy.factor` of the
reconstructed `J(m)` returns the tower; `MATCH = True`).

## Why this is new (vs B63/B65 and the stalled B70)

- **B63/B65** built `J(m)` by **rep-perturbation FLOAT numerics + rational guessing** (high-precision
  SVD-pinv at `m=1..7`, then interpolation). That is numerical reconstruction.
- **B70** tried the symbolic-`m` ε-series pinv-limit **directly over ℚ[m]** and **stalled at SL(4)
  (L=12)** — the ℚ series-inverse + Gauss–Jordan blew up.
- **B80 (this)** does the same ε-series least-squares pinv-limit but **over F_p** (the working
  B58_phaseA engine — *exact* modular arithmetic, no float, ~3 s/call), at integer `m=1..8`, then
  **interpolates in `m` over F_p and CRT + rational-reconstructs to ℚ[m]** across 5 primes. The final
  `char(J(m))` factorization is an **exact symbolic identity**, not a numerical fit.

The `e₂ = tr(Λ²A)` two-block barrier (B58/B64) needs **no hand-built trace ring**: the `n×n` matrix
arithmetic in the ε-series automatically enforces the Cayley–Hamilton / exterior-power closure.

## Rigor / what is certified

1. `DT_0(m)` over F_p is **exact** (modular), and **seed-canonical** — `m=1` over seeds 20, 99 gives
   *identical* entries, so `J(m)` in the fixed word basis is well-defined and `m`-interpolation is valid.
2. The entries are **polynomials in `m` of degree exactly 4** (verified: a degree-4 fit from 5 points
   reproduces `m=1..14`), so interpolation is exact.
3. **5 primes + Wang rational reconstruction** give `J(m)` over ℚ[m] unambiguously (coefficients are
   small rationals, e.g. `J₀₀=m⁴/2−3m³+11m²/2−3m`, far inside the reconstruction bound).
4. **Gate vs B65** (`jacobian_m.json`): the char poly is **identical** (basis-independent invariant);
   entries differ only because the word basis differs (`b66_select` vs B59) — as expected.

The only computer-assisted ingredients are the (basis-only) word selection and the exact modular/CRT
arithmetic; the closing factorization is a genuine symbolic identity over ℚ[m]. **This relabels the
SL(4) tower from "computer-assisted numerics" (B65) to "established from a first-principles ε-series
construction"** and opens the same CRT/F_p route to SL(5)/SL(6).

## Honest scope

This certifies `char(J(m)) =` the tower, where `J(m)` is the fixed-line Jacobian computed by the
ε-series least-squares pinv-limit (the B66/B58 method, justified there). It is **not** a hand proof of
the closed-form `a_d` formula for all `n` — that remains the general-`n` open item — but it is the
SL(4) tower derived rigorously from the construction, which B70 could not reach.

## Reproduce

```bash
python frontier/B80_sl4_adproof/build_jm.py          # ~2-3 min (40 F_p engine calls + CRT + factor)
python -m pytest tests/test_b80_sl4_adproof.py -q
```
