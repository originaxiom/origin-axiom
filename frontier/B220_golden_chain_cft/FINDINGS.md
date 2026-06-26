# B220 — L41 CLOSED: the golden (Fibonacci anyon) chain CFT reproduced in-sandbox (c = 7/10)

**Date:** 2026-06-26. **Status:** the **B218 residual closed.** B218 banked the exact Jones-index
selection (golden = the unique anyon-realizable metallic mean) but **cited** the chain-level CFT
`c=7/10` rather than reproducing it — a first in-sandbox ED gave a **gapped artifact** (`c≈0`). This is
the corrected exact-diagonalization: the AFM golden chain is **gapless with `c ≈ 0.71 = 7/10`**.
Firewall: a dimensionless CFT (a central charge), **not** physical scale; **nothing to `CLAIMS.md`;
P1–P16 untouched.** Ledger **V223**.

## The model (correct this time)

`N` Fibonacci anyons (`τ`) on a ring; fusion-path basis `l_1…l_N ∈ {1, τ}` with the constraint **no
two adjacent identities** (`τ×τ = 1+τ`); Hilbert dimension = Lucas number `L_N`. The local term `ĥ_i`
projects anyons `(i,i+1)` onto the **identity** fusion channel, acting on link `l_i` conditioned on
`(l_{i−1}, l_{i+1})`. The only nontrivial piece is the `(τ,τ)` block — the rank-1 projector

```
   P = F · diag(1,0) · F ,   F = [[φ⁻¹, φ⁻¹ᐟ²],[φ⁻¹ᐟ², −φ⁻¹]]   ⇒   P = [[φ⁻², φ⁻³ᐟ²],[φ⁻³ᐟ², φ⁻¹]]
```

**The bug before:** the first attempt dropped the off-diagonal `φ⁻³ᐟ²` term, leaving a diagonal
operator → a trivially **gapped** chain (`c≈0`). The off-diagonal *is* the kinetic term that makes the
chain critical. (Feiguin–Trebst–Ludwig–Troyer–Kitaev–Wang–Freedman, PRL 98, 160409 (2007).)

## The result

`H_AFM = −Σ ĥ_i`, central charge from the PBC entanglement entropy `S(ℓ)=(c/3)ln[(N/π)sin(πℓ/N)]+b`
(slope → `c/3`; **no velocity needed**):

| N | dim | E₀/N | gap·N | c_ent |
|--:|----:|-----:|------:|------:|
| 14 | 843 | −0.7674 | 0.87 | 0.76 |
| 16 | 2207 | −0.7666 | 0.87 | 0.71 |
| 18 | 5778 | −0.7660 | 0.86 | 0.71 |
| 20 | 15127 | −0.7656 | 0.86 | 0.72 |
| 22 | 39603 | −0.7653 | 0.86 | 0.71 |

Two signatures, both contradicting the earlier artifact: **(1) gapless** — `gap·N ≈ 0.86` constant ⇒
`gap ~ 1/N → 0` (not a constant gap); **(2)** `c_ent ≈ 0.71`, i.e. **tricritical Ising `c = 7/10`**,
clearly distinct from `0` (gapped) and from `0.8` (Potts).

## Honest status / tiers
- AFM `c = 7/10` (tricritical Ising), gapless: **`[reproduced]`** in-sandbox (`c_ent ≈ 0.71`, the
  ~1.5% offset is ordinary finite-size at `N≤22`). This **upgrades B218's `c=7/10` from `[cited]`**.
- FM `H=+Σĥ_i` → 3-state Potts `c = 4/5`: **`[consistent]`** but noisier (`c_ent ≈ 0.74–0.75`, larger
  finite-size scatter, a level-crossing at `N=18`) — secondary, not the headline.
- the underlying physics (golden chain → TCI/Potts) is **classical** (Feiguin 2007); the contribution
  is the correct in-sandbox reproduction closing the B218 residual. Novelty UNCHECKED.

## Reproduction
- `python golden_chain.py` — AFM + FM, `N=14..22` (pyenv; uses scipy sparse `eigsh`).
- `tests/test_b220_golden_chain_cft.py` — locks: Fibonacci/Lucas Hilbert dim, **gaplessness**, and AFM
  `c ≈ 0.7` (bracketed `0.60<c<0.78`, closer to 0.7 than to 0 or 0.8).

## Net
The golden-chain CFT is now **reproduced**, not merely cited: multiplicity selects golden (B218,
Jones index), and the golden anyon chain flows to **tricritical Ising `c=7/10`** — computed here, the
gapped artifact gone. What is selected is a **dimensionless central charge**, not a physical scale
(firewall holds). (`B218 → B220`.)
