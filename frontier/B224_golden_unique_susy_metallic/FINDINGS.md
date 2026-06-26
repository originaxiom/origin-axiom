# B224 — golden is the UNIQUE metallic mean whose chain is supersymmetric (closing the circle)

**Date:** 2026-06-26. **Status:** the family question (chat1's "close the circle"). B221/B222 found the golden
chain's emergent CFT is the tricritical Ising `M(4,5)` = the first N=1 superconformal minimal model. This asks
whether golden is the *only* metallic mean with a supersymmetric chain — and answers **yes, exactly**. Firewall:
dimensionless CFT / rep-theory; the SUSY is 2d superconformal, **not** a scale or spacetime SUSY (`S040`).
**Nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V227**.

## The result (exact)

```
   su(2)_k spin-1/2 anyon chain (AFM)  →  M(k+1, k+2),  c = 1 − 6/((k+1)(k+2))   [Feiguin–Trebst–Ludwig]
   among ALL unitary minimal models M(q,q+1):  ONLY M(4,5) (c=7/10) is N=1 superconformal  (= SM(3))
   metallic index m  ↔  level k_m = m²+2   (n = k+2 = m²+4 = the metallic discriminant)

      m=1 (golden): k=3  → M(4,5)   c = 7/10   SUPERSYMMETRIC
      m=2 (silver): k=6  → M(7,8)   c = 25/28
      m=3 (bronze): k=11 → M(12,13) c = 25/26
      m≥2: c_m → 1 from below; NONE superconformal but golden.
```

So **golden (m=1) is the unique metallic mean whose anyon chain is superconformal** — because the SUSY point
(the tricritical Ising `M(4,5)`) requires *exactly* the golden level `k=3`, which is `m²+2` at `m=1` (`n=5=m²+4`,
the golden discriminant, `2cos(π/5)=φ`, B218).

## Why it's unique (the mechanism)

The N=1 superconformal minimal models `SM(p)` have `c=(3/2)(1−8/(p(p+2)))`. Solving `c=1−6/(q(q+1))` (an ordinary
unitary minimal model) `= SM(p)`: the only solution with `c<1` is `p=3 → c=7/10 → q=4`, i.e. `M(4,5)`. Every
other `SM(p)` has `c≥1` (not an `M(q,q+1)`). So `M(4,5)` is the **unique** unitary Virasoro minimal model that is
also superconformal — hence `k=3` is the **unique** su(2)_k chain whose critical point is supersymmetric, and
`k=3` is golden.

## Closing the circle on golden

Golden (`m=1`, `n=m²+4=5`) is now characterized four independent ways, all through the number 5:
- **minimal** — smallest metallic discriminant (Level-0 of the family);
- **exceptional** — `E₈` via the monodromy field `ℚ(√5)` (`2I`) and `E₆` via the hyperbolic field `ℚ(√−3)`
  (`2T`) (B206/B210);
- **least-hierarchical** — smallest volume / permanently critical (B207/B181);
- **uniquely supersymmetric** — the only metallic chain whose critical CFT is N=1 superconformal (this finding).

## Honest status / tiers
- the su(2)_k chain → M(k+1,k+2) flow: **`[cited]`** (Feiguin–Trebst–Ludwig); the `k=3` case is **`[reproduced]`**
  in-sandbox (B220/B222).
- the central charges, the superconformal-uniqueness of `M(4,5)`, and the metallic-family SUSY selection: **all
  `[exact]`** (exact rational arithmetic; pytest-locked).
- the `m ↔ k=m²+2` identification (via `n=k+2=m²+4`, the metallic discriminant): the **motivated correspondence**
  (consistent with B204/B218's `n=5` at `m=1`); the superconformal-uniqueness itself does **not** depend on it
  (among *all* `k`, only `k=3` works). Novelty UNCHECKED.

## Reproduction
- `python coset_susy_uniqueness.py` (pyenv) — the four blocks.
- `tests/test_b224_golden_unique_susy_metallic.py` — 4 exact locks.

## Net
Golden is the **unique** metallic mean whose interaction produces supersymmetry — the SUSY tricritical-Ising point
exists only at the golden level `k=3` (`n=5=m²+4`), and the whole rest of the metallic family flows to ordinary
(non-superconformal) minimal models approaching `c=1`. This sharpens "golden is special" to its strongest form.
(`B218 → B221 → B222 → B224`; firewalled reading `S040`.)
