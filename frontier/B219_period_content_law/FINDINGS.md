# B219 — L39 RESOLVED: the class-field period law is the form CONTENT (elementary), not genus-theoretic

**Date:** 2026-06-26. **Status:** **L39 closed** — B216's "`f≥8` needs-specialist (genus-theoretic)"
verdict is **overturned**. The period law is fully **elementary**. A *compute-before-deferring* win:
B216 deferred to a specialist prematurely; the actual answer is the binary-quadratic-form content.
Firewall: standalone quantum-topology / arithmetic; **nothing to `CLAIMS.md`; P1–P16 untouched.**
Ledger **V222**.

## The theorem (verified, elementary)

For `γ = [[a,b],[c,d]] ∈ SL(2,ℤ)` of trace `t`, the WRT level-period is

```
   P(γ) = lcm(t−2, t+2) / content(γ),     content(γ) = gcd(b, c, a−d)
```

`content(γ)` = the content of the associated binary quadratic form `(c, d−a, −b)` = **the largest
modulus `d'` such that `γ ≡ s·I (mod d')` for some scalar `s`** (`s²≡1 mod d'` automatically). The
period is a function of `(trace, content)` **only** — there is **no genus dependence**.

## What B216 got wrong (and why)

B215/B216 used `d(γ) = max{d'|f : γ ≡ ±I mod d'}` — only the scalars **±1**. This is correct for
conductor `f ≤ 4`, but **fails at `f = 8`** for a purely 2-adic reason:

```
  sqrt(1) mod 8  = {1, 3, 5, 7}      (four roots — (ℤ/2^k)^× has Klein-four 2-torsion for k≥3)
  sqrt(1) mod 16 = {1, 7, 9, 15}
  sqrt(1) mod 4  = {1, 3} = {±1};  sqrt(1) mod p^k (odd p) = {±1}   (so f≤4 and odd parts are fine)
```

`GAMMA_A = [[13,−8],[−8,5]] ≡ 5·I (mod 8)` — a scalar, but **not ±I** — so the `±I` test under-reports
`d = 4` when the true content is **8**. That is the *entire* B216 "obstruction": `A` has content 8
(period 10), `B = [[17,−4],[−4,1]]` has content 4 (period 20). The "identical scalar-depth, different
`d`" paradox dissolves once `d` is read as the content.

## The decisive check — no genus residue

The real worry was a *genus* split **among primitive (content-1) classes**. Tested exhaustively at
`f = 8` (`t=18`, `D=320=2⁶·5`, all four genera present):

| content | #class-reps | period | predicted `80/content` |
|--------:|------------:|-------:|----------------------:|
| 1 | 334 | 80 | 80 |
| 2 | 136 | 40 | 40 |
| 4 | 56 | 20 | 20 |
| 8 | 16 | 10 | 10 |

**Every** content-1 class has period 80 regardless of genus signature `(χ₄,χ₈,(·/5))` — so the period
cannot depend on any finer invariant. (B216's "period 80 is not minimal" flags were **short-window
numerical false positives** in the period detector; the robust detector — window 48, tol 2e-3 — gives
minimal period 80 for all.) The law **generalizes to `f=16`** (`t=66`, `D=4352=2⁸·17`): the content-16
class `≡ 9·I (mod 16)` (9²≡1) has period `1088/16 = 68`; content-8 → 136. And it **reproduces B204**'s
block-word formula for `RᵃLᵇ` exactly, with `content(RᵃLᵇ) = gcd(a,b)`.

## Honest status / tiers
- the law `P = lcm(t−2,t+2)/content`: **`[verified]`** — exhaustive at `f=8` (all classes/genera),
  spot-checked at `f=16`, consistent with B215 (`f≤4`) and B204 (`RᵃLᵇ`). A fully symbolic all-`t`
  Gauss-sum proof (à la B204) is the remaining `[proved]`-tier step; the genus-independence is settled.
- the 2-adic mechanism (extra `sqrt(1) mod 2^k`): **`[proved]`** elementary group theory.
- **overturns** B216/V219 (NEEDS-SPECIALIST → RESOLVED). Novelty UNCHECKED (the content/Latimer–MacDuffee
  link is classical; the WRT-period framing is the contribution).

## Reproduction
- `python period_content.py` — all five parts incl. the exhaustive `f=8` sweep (pyenv; ~1–2 min).
- `tests/test_b219_period_content_law.py` — fast locks (content law + high-content periods + `f=16`).

## Net
The `B204→B214→B215→B216` arc is **closed elementarily**: the period law is `lcm(t−2,t+2)/content`,
the content being the largest scalar-reduction modulus. B216's genus-theoretic deferral was an artifact
of the `±I`-only criterion (a 2-adic miss) compounded by period-detector false positives. (Chain:
`B204 → B214 → B215 → B216 → B219`; Latimer–MacDuffee = repo `B92`.)
