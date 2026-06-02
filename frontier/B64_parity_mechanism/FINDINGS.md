# B64 FINDINGS -- the parity mechanism + consolidated tower theory

Exact symbolic algebra (SL(3) full; SL(4) sector assignment). No physics, no
Origin-core claim.

## Verdict

```text
PROVEN (symbolic): the k(alpha) sector-assignment formula for the metallic tower.
  even-|k| char(M^k) -> P-symmetric sector (even root heights)
  odd-|k|  char(M^k) -> P-antisymmetric sector (odd root heights)
Mechanism = depth-n CH (Jacobian polynomial in m) + P=contragredient (m -> -m)
            + Dickson parity (L_k(-m) = (-1)^k L_k(m)).
Verified in full symbolic-m form for SL(3); applied to SL(4)'s factorization.
```

## The mechanism

`M = [[m,1],[1,0]]`, `L_k = tr(M^k)`. At the fixed line `c=n` the trace-map
Jacobian `J(m)` commutes with the exchange involution `P` (B54), so it
block-diagonalizes into P-symmetric (+1) and P-antisymmetric (-1) sectors. Three
facts pin which `char(M^k)` lands where:

1. **Depth-n CH** => `J(m)` entries are polynomials in `m` (the derivative
   sequences `∂τ_k/∂x_j` are polynomials in `k`, evaluated at `k=m,m±1,…`).
2. **`P` = contragredient** (`A ↔ A^-1`) sends `φ_m → φ_{-m}`, i.e. `m → -m`.
3. **Dickson parity:** `L_k(-m) = (-1)^k L_k(m)`.

Hence the symmetric sector's char poly is **even in `m`** and the antisymmetric
sector carries the **odd-in-`m`** content; `char(M^k)` (with `L_k` of parity
`(-1)^k`) is symmetric for even `|k|`, antisymmetric for odd `|k|`.

## What was verified

- **SL(3), full symbolic `m`.** From the depth-3 derivative sequences
  (`∂τ_k/∂trA = k(k^2-1)/2`, `∂τ_k/∂trB = 1-k^2`, `∂τ_k/∂trAB = k(k+1)/2`,
  `∂τ_k/∂trA^-1 = -k(k^2-1)/2`, `∂τ_k/∂trA^-1B = k(k-1)/2`, and `σ = P·τ`), the
  `8x8` Jacobian block-diagonalizes under `P` into

  ```text
  symmetric     = (t-1)(t+1) char(M^2)     [even in m; even k=2]
  antisymmetric = char(M^-1) char(M^3)     [odd k = -1, 3]
  ```

  exact polynomial identities in `m`.
- **Dickson parity** `L_k(-m)=(-1)^k L_k(m)` for `k=1..6` (symbolic).
- **SL(4) sector assignment.** B63's factorization splits, by the mechanism,
  into P-symmetric `{char(M^2), char(M^4), char(-M^2)}` (even `|k|`, `L_k` even in
  `m`) and P-antisymmetric `{char(M^-1), char(M), char(M^3)}` (odd `|k|`, `L_k`
  odd in `m`) -- verified factor-by-factor.
- **SL(4) depth-4 derivative sequences** built (seed/homogeneous degree 3
  "cubic", forced degree 4), the depth-4 analog of B54's depth-3.

## The localized obstruction (where a full symbolic SL(4) Jacobian needs Λ²V)

`tr((A^m B)^2) = (tr(A^m B))^2 - 2 tr(Λ^2(A^m B))`, and `tr(Λ^2(A^m B)) =
tr((Λ^2 A)^m (Λ^2 B))` is a single-block trace in the **6-dim exterior square**
(depth-6 recursion), not a fundamental `τ_k`. So the even-`k` (P-symmetric)
sector rows -- the `e_2 = tr(A^2)` coordinate and its kin -- need `Λ^2 V`. The
fundamental depth-4 sequences close the **odd-`k` (antisymmetric)** structure but
not the even-`k` one. This is exactly the residual hard core of B58, and it lies
in the sector the parity mechanism marks even.

## Consolidated tower theory (SL(n) metallic fixed line, m=1 unless noted)

```text
n  factorization                                                    status
2  char(M^2)                                                        exact
3  char(M^-1) char(M^2) char(M^3) (t-1)(t+1)                        symbolic, all m (B54)
4  char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2)      over Z[m] (B63);
     (t-1)^2(t+1)                                                     sectors proven (B64)
5  char(M^-1) char(M)^2 char(M^2)^2 char(M^3) char(M^4) char(M^5)   22 numeric (B61)
     char(-M^2) char(-M^3) (t-1)^2(t+1)^2                             + 2 structural (B62)
```

Structural theory now in hand:
- **Which factors / multiplicities:** the cross-n map (B59/B60/B61/B62).
- **Which sector each factor lives in (k(alpha)):** the parity mechanism (B64) --
  even `|k|` symmetric, odd `|k|` antisymmetric, proven.
- **m-dependence:** `L_k(m) = tr(M^k)` (B63), m-independent structure.

Open: a single from-first-principles symbolic proof for all `n` (the ambient
`SL(n,C)` trace ring with the `Λ^2`/multi-block machinery; B58). B64 reduces the
SL(4) gap to exactly the even-`k`/`Λ^2 V` sector.

## Reproduce

```bash
python frontier/B64_parity_mechanism/probe.py
python -m pytest tests/test_b64_parity_mechanism.py -q
```
