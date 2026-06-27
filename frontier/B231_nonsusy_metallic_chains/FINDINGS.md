# B231 — H15: the non-SUSY metallic anyon chains (an earned negative; golden's specialness is one boundary)

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Promotes hint **H15** (NOTICED → CHECKED). Run: `python nonsusy_chains.py` (pyenv).

## The question (H15)
B224 proved golden (`k=3`) is the **unique** metallic chain that is an `N=1` super minimal model; B218 found
golden is the **unique anyon-realizable** metallic mean (`λ_m<2 ⟺ m=1`). H15 asks the complement: do the *other*
metallic chains — the `su(2)_k` spin-½ anyon chains at the metallic levels `k=m²+2` (silver `k=6`, bronze `k=11`,
…) — have **their own** special structure at those levels?

## What was built (the toolkit gap)
The general **`su(2)_k` spin-½ anyon chain** (Feiguin–Trebst–Ludwig 2007) — the gap left by B220 (which built only
the Fibonacci/golden chain). Fusion-path basis = closed walks on the `su(2)_k` graph (vertices `2j=0..k`); the
local term is the identity-channel projector `(P_i)_{b,b'}=√(d_b d_{b'})/(d_a d_{1/2})` (nonzero only when the two
neighbours agree, `x_{i-1}=x_{i+1}=a`). `H_AFM=−ΣP_i → M(k+1,k+2)`; `H_FM=+ΣP_i → Z_k` parafermion.

**Build validated** (the only way to trust it): `H_AFM` reproduces the known benchmarks at largest N —
`k=2 → c=0.496` (Ising `M(3,4)`, target ½) and `k=3 → c=0.711` (TCI `M(4,5)`, target 7/10). The anyon chains
have a (physical) **near-degenerate ground state** (`gap≈0`), so `c` is read from the lowest eigenvector's
entanglement (PBC Calabrese–Cardy), exactly as B220.

**Silver (`k=6`, `m=2`)** AFM: `c` decreases `1.04 → 0.99 → 0.99 → 0.92 → 0.92` (N=10..18) toward `25/28=0.893`
(higher-`c` minimal models carry a larger upward finite-size bias). Silver is a **critical `c<1` minimal-model
chain consistent with `M(7,8)` — and NOT supersymmetric** (B224/B230). No size-ceiling hit (N=18, dim 127k, ran).

## The exact answer (the headline — exact, not numerical)
Tabulating the exact CFT data at the metallic levels `k=m²+2` (`n=k+2=m²+4` = the metallic discriminant):

| m | k | n=m²+4 | c_AFM=M(k+1,k+2) | c_FM=Z_k | λ_m | d_{1/2}=2cos(π/n) | λ_m a quantum dim? | λ_m<2? |
|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 5 | 7/10 | 4/5 | 1.6180 | 1.6180 | **yes** | **yes** |
| 2 | 6 | 8 | 25/28 | 5/4 | 2.4142 | 1.8478 | no | no |
| 3 | 11 | 13 | 25/26 | 20/13 | 3.3028 | 1.9419 | no | no |
| 4 | 18 | 20 | 187/190 | 17/10 | 4.2361 | 1.9754 | no | no |
| 5 | 27 | 29 | 403/406 | 52/29 | 5.1926 | 1.9883 | no | no |

**The metallic mean is a quantum dimension** (i.e. `λ_m = d_{1/2} = 2cos(π/(m²+4))`, the spin-½ anyon's dimension
at the metallic level) **if and only if `m=1`.** The structural reason: every `su(2)_k` quantum dimension is a
`2cos(π/n) < 2`, but `λ_m > 2` for all `m≥2` (`λ_2=1+√2`). So the metallic mean can *be* an anyon dimension only at
golden.

## Verdict — an earned negative that sharpens golden's uniqueness
The level `k=m²+2` confers **no special chain-level structure for `m≥2`**: the non-SUSY metallic chains are
**generic** `M(k+1,k+2)` (AFM) / `Z_k` parafermion (FM) CFTs; the "metallic" label of the level is invisible at the
chain level. Everything special about golden is an **`m=1`-only** phenomenon — and three independently-banked
"golden is special" facts collapse to **one boundary**:

> **`λ_m < 2  ⟺  m=1`** — the metallic mean is anyon-realizable (B218), the chain is supersymmetric (B224), and the
> metallic mean *is* the fundamental anyon's quantum dimension (B231) — all the same threshold.

This is the H15 answer (NOTICED → CHECKED): a clean negative (anti-blindness rule 7 satisfied — the negative was
*computed*, not assumed: the `su(2)_k` chain was built, validated, and the silver chain run), reinforcing
K019/B218/B224. Firewall: dimensionless CFT data / quantum dimensions; no physical scale (K018).

## Anchors
B218 (anyon-realizable selection, `λ_m<2`), B220 (golden-chain ED), B224 (golden uniquely SUSY), B230 (FM/parafermion
robustness), K019 (collective metallic spectrum). Literature: Feiguin–Trebst–Ludwig PRL 98 160409 (2007).
