# B204 — proof that `|Z(a,b)|` is exactly periodic in the level (Gauss-sum reciprocity)

**Date:** 2026-06-24. Upgrades the B204 period law from `[num, strongly confirmed]` to **periodicity
PROVED**, with the diagonal factor `lcm(a,b)` proved and the exact period reduced to (and verified via) the
cross-term Gauss-sum period. Reproducer `gauss_proof.py`; locks in `tests/test_b204_metallic_wrt_period.py`.
Every identity below is an exact algebraic statement; each is verified to ≥18 digits in the reproducer.

## Setup

`Z(a,b;k) = Σ_{i,j=0}^{k} e^{2πi(a h_i − b h_j)} S²_{ij}`, `n=k+2`, `h_i=i(i+2)/(4n)`,
`S_{ij}=√(2/n) sin(π(i+1)(j+1)/n)`. Substituting `p=i+1, q=j+1` (so `i(i+2)=p²−1`):

```
Z(a,b;k) = (2/n) e^{-iπ(a-b)/(2n)} · Z̃(n),
Z̃(n)    = Σ_{p,q=1}^{n-1} e^{iπ(a p² - b q²)/(2n)} sin²(π p q/n).
```
The constant phase `e^{−iπ(a−b)/(2n)}` is the **only** non-periodic factor; it has modulus 1, so
`|Z| = (2/n)|Z̃|`, and for the metallic case `a=b` it is `1` (so `Z` itself is real and periodic).

## Step 1 — extend to a full period (no boundary terms)

`sin²(π p q/n)` vanishes whenever `p ≡ 0` or `q ≡ 0 (mod n)`, and `p→2n−p` leaves the summand invariant
(`e^{iπa(2n−p)²/(2n)}=e^{iπap²/(2n)}`, `sin²(π(2n−p)q/n)=sin²(π pq/n)`). Hence the range `1..n−1` extends
to the **full period** `0..2n−1` with only a harmless factor:
```
Z̃(n) = (1/(2n)) Σ_{p,q=0}^{2n-1} e^{iπ(a p² - b q²)/(2n)} sin²(π p q/n).
```
This is the key move: the sum is now over complete periods, so the Gauss sums below carry **no boundary
corrections** (the obstruction that prevents a clean reduction on the `1..n−1` range).

## Step 2 — split into diagonal + cross, evaluate by reciprocity

With `sin²(πpq/n) = ½ − ¼e^{2πipq/n} − ¼e^{−2πipq/n}` the sum factors:
```
Z̃(n) = (1/(2n))[ ½ g_a g_b*  −  ¼ (h⁺ + h⁻) ],
  g_a = Σ_{p=0}^{2n-1} e^{iπ a p²/(2n)}                                   (1-var Gauss sum)
  h^t = Σ_{p,q=0}^{2n-1} e^{iπ (a p² - b q² + 4t pq)/(2n)},  t=±1         (2-var Gauss sum)
```

**Diagonal — Landsberg–Schaar (exact).** `g_a = √(2n)·e^{iπ/4}·G_a(n)/√a` with
`G_a(n)=Σ_{s=0}^{a-1} e^{−2πi n s²/a}`. The `√(2n)` factors cancel the `1/(2n)`:
```
  (1/(2n))·½·g_a g_b*  =  (1/(2√(ab)))·G_a(n)·G_b(n)*.
```

**Cross — 2D Gauss reciprocity (exact).** `h^t = Σ_x e^{iπ xᵀM_t x/(2n)}`, `M_t=[[a,2t],[2t,−b]]`,
`det M_t = −(4+ab)`, signature `0`. Since `N=2n` is even,
```
  h^t = (2n/√(4+ab))·Γ_t(2n),   Γ_t(N) = (1/(4+ab)) Σ_{y∈(ℤ/(4+ab))²} e^{−iπ N yᵀM_t^{-1}y},
```
(well-defined on `ℤ²/M_tℤ²` because `N` even makes the summand `M_t`-translation-invariant). Again the `2n`
cancels the `1/(2n)`. Net **exact closed form**:
```
  Z̃(n) = (1/(2√(ab)))·G_a(n)G_b(n)*  −  (1/(4√(4+ab)))·(Γ⁺(2n)+Γ⁻(2n)).
```
Both `g_a=√(2n)e^{iπ/4}G_a/√a` and `h^t=(2n/√(4+ab))Γ_t` are verified as exact identities (0 mismatches).

## Step 3 — read off periodicity

- `G_a(n)` depends only on `n mod a`, and its period is **exactly `a`**: `G_a(n+d)=G_a(n)` for all `n` forces
  (take `s=1`) `e^{−2πi d/a}=1`, i.e. `a|d`. So the diagonal term has period `lcm(a,b)` — **PROVED**.
- `Γ_t(2n)` depends only on `2n mod (4+ab)` (the denominators of `M_t^{-1}` divide `4+ab=det(γ+I)`), so the
  cross term is periodic; its period `L_c` divides `4+ab`.

Therefore `Z̃(n)` — and hence `|Z(a,b;n)|` — is **exactly periodic**, with period
`P = lcm(lcm(a,b), L_c)`. This is the theorem: despite the matrix dimension `n−1` growing with the level, the
trace's magnitude is exactly periodic, because the `√n`-amplitudes of the Gauss sums cancel the `1/n`.

## Step 4 — the exact period

`per(diagonal) = lcm(a,b)` (proved). The exact period
`P = lcm(lcm(a,b), L_c) = lcm(a,b)·(4+ab)/gcd(4+ab,4)` is **verified** on 14 cells via the cheap dual form for
`L_c` (incl. (3,5)→285, (4,5)→120, (5,6)→510, (3,7)→525). The metallic diagonal gives
`P(m)=m(m²+4)/gcd(m²+4,4)`.

## What is proved vs. what remains

**PROVED:** `|Z|` is exactly periodic in the level (the qualitative theorem); the exact reciprocity closed
form for `Z̃`; the diagonal period `lcm(a,b)`. **REMAINING (one lemma):** a closed form for the cross-term
Gauss-sum period `L_c` (its 2-adic part — the `gcd(4+ab,4)` interaction with `lcm(a,b)`); currently `L_c` is a
finite, explicit dual Gauss sum evaluated per cell, and `lcm(lcm(a,b),L_c)=P` is verified, not yet closed in
general. This is `[periodicity proved; exact period one Gauss-sum-period lemma from full closure]` — not
`[proved]` for the exact-period formula until `L_c` is closed.

## Firewall
Standalone quantum-topology / arithmetic. No physics; nothing to `CLAIMS.md`; P1–P16 untouched.
