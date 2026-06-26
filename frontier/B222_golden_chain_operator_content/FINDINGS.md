# B222 / Act I — emergent SUSY confirmed: the golden chain's finite-size spectrum IS the tricritical Ising content (with the supercurrent)

**Date:** 2026-06-26. **Status:** the decisive Act I. B221 fixed the identity exactly (`c=7/10` = the first N=1
superconformal minimal model); B220 confirmed the central charge by entanglement. This goes the rest of the way:
**momentum-resolved exact diagonalization** extracts the *operator content* and finds the **h=3/2 supercurrent** —
the actual generator of the emergent supersymmetry. Firewall: dimensionless CFT spectrum only; a 2d
superconformal symmetry, not a scale or spacetime SUSY (`speculations/S040`). **Nothing to `CLAIMS.md`; P1–P16
untouched.** Ledger **V225**.

## The correctness gate (load-bearing)

Translation `T` permutes the cyclic golden-chain basis, so momentum `k=2πj/N` is good. Building complex-Hermitian
`H_k` per sector (orbit/representative method, period-ratio `√(R_r/R_{r'})` weights), the **union of all sector
spectra equals the full spectrum to `<1e-9`** at N=10,12,14, and every `H_k` is Hermitian. The momentum
decomposition is exact — this gates every dimension claim below.

## NS sector (even N) — the tricritical-Ising primaries + the supercurrent

Calibrating the sound velocity `v` once on the stress tensor (lowest spin-2 state, `x_T=2`), the spinless (`j=0`)
scaling dimensions `x_n = (N/2πv)(E_n−E_0)` converge to the **NS-sector** tricritical-Ising content:

| N | x₁ (→1/10·2) | x₂ (→3/5·2) | x₄ (→3/2·2, the supercurrent) |
|--:|------:|------:|------:|
| 16 | 0.210 | 1.239 | 3.000 |
| 18 | 0.208 | 1.230 | 2.998 |
| 20 | 0.206 | 1.224 | 2.996 |
| 22 | 0.205 | 1.220 | 2.996 |

target → **0.2** (`h=1/10`), **1.2** (`h=3/5`), **3.0** (`h=3/2`). (Level 3, `x≈2.2`, is the `L₋₁L̄₋₁`
descendant of `h=1/10`.) So the periodic even-N chain reproduces the NS primaries **{0, 1/10, 3/5, 3/2}**, and the
**`h=3/2` field sits at `x=3.0` essentially exactly** — its chiral half `(3/2,0)` is the **N=1 supercurrent `G`**,
the generator of the emergent SUSY. (The plan flagged the supercurrent as the genuine risk; it turned out to be
the *cleanest* level — `x=3` is well-separated.)

## R sector (odd N) — the Ramond primaries

The odd-N chain realizes the **Ramond (twisted) sector**. Its 2nd spinless level sits at
`Δx → 2(7/16 − 3/80) = 0.8` above the R ground (N=15,17,19,21: `0.858, 0.842, 0.831, 0.823` — monotonically
**decreasing toward 0.8**), i.e. the R ground is `h=3/80` and the next R primary is `h=7/16`, recovering
**{3/80, 7/16}**. Honest caveat: at small N (≤17) the value `~0.84` is ambiguous between the gap `0.8` and the
naive absolute `0.875` (the two candidates differ by only `0.075`, comparable to finite-size error); the trend
favours `0.8` only by `N≥19`. So the R sector is **`[consistent]`**, not cleanly locked (the odd-N velocity
calibration is also less clean than NS).

## What this establishes

NS `{0, 1/10, 3/5, 3/2}` + R `{3/80, 7/16}` = the **complete tricritical-Ising `M(4,5)` primary content**, with
the **`h=3/2` supercurrent** present and essentially exact — the decisive signature that the emergent CFT is the
**N=1 *superconformal*** minimal model, not merely a `c=7/10` theory. Multiplicity (golden, B218) → emergent
supersymmetry, now confirmed at the level of the spectrum.

## Honest status / tiers
- the momentum-ED correctness gate: **`[exact]`** (machine precision).
- NS primaries `{0,1/10,3/5,3/2}` + the **supercurrent `x=3.0`**: **`[reproduced]`** (clean; the supercurrent
  ~0.1% at N=22).
- R primaries `{3/80,7/16}` via `Δx→0.8`: **`[consistent]`** (noisier; odd-N calibration; full absolute R-ground
  pinning would need a cross-sector Casimir analysis — flagged).
- the physics (golden chain → tricritical Ising / emergent SUSY) is **classical** (Feiguin et al. 2007;
  Huijse–Schoutens). Contribution = the in-sandbox confirmation incl. the supercurrent. **Novelty UNCHECKED.**

## Reproduction
- `python momentum_ed.py` (pyenv) — the gate + NS dimensions + the R-sector gap.
- `tests/test_b222_golden_chain_operator_content.py` — the gate + NS primaries/supercurrent + the R gap.

## Net
The golden chain's emergent CFT has the **full superconformal `M(4,5)` operator content**, supercurrent included —
emergent N=1 SUSY confirmed from the spectrum. (`B218 → B220 → B221 → B222`; the lattice/external question is Act
II/B223; the firewalled reading is `S040`.)
