# B64 -- The parity mechanism: a proof of the tower's k(α) sector assignment

**Status:** exact symbolic algebra. SL(3): full symbolic-m proof. SL(4): sector
assignment proven (and the one obstruction to a full symbolic Jacobian
localized). Standalone trace-map / Lie-theory mathematics; no physics, no
Origin-core claim.

## What this proves

B62 identified the exchange involution `P` (`tr W <-> tr W^-1`) with the
opposition involution and placed each `char(M^k)` factor in a root-height sector.
B64 proves **why** that assignment holds, from three facts (`M=[[m,1],[1,0]]`,
`L_k=tr(M^k)`):

1. **Depth-n Cayley-Hamilton.** The fixed-line (`c=n`) Jacobian `J(m)` has entries
   that are polynomials in `m`: the derivative sequences `∂τ_k/∂x_j` are
   polynomials in `k`, evaluated at the image indices `k = m, m±1, …`.
2. **`P` is the contragredient** (`A ↔ A^-1`), which sends the substitution `φ_m`
   to `φ_{-m}` — i.e. `m → -m`.
3. **Dickson parity:** `L_k(-m) = (-1)^k L_k(m)`.

Since `J` commutes with `P` (B54), it block-diagonalizes into a P-symmetric (+1)
and P-antisymmetric (-1) sector. Facts 2-3 force the **symmetric sector's
characteristic polynomial to be even in `m`** and the antisymmetric one to carry
the odd-in-`m` content. As `char(M^k)` has `L_k` of parity `(-1)^k`:

```text
char(M^k)  with EVEN |k|  ->  P-symmetric sector       (even root heights)
char(M^k)  with ODD  |k|  ->  P-antisymmetric sector   (odd  root heights)
```

This is the proven `k(α)` sector-assignment formula.

## Verification

- **SL(3) (full symbolic-m).** Building `J(m)` from the depth-3 derivative
  sequences and block-diagonalizing under `P` gives, exactly:

  ```text
  symmetric     = (t-1)(t+1) · char(M^2)          [even in m; even k=2]
  antisymmetric = char(M^-1) · char(M^3)          [odd k = -1, 3]
  ```

- **SL(4) (sector assignment).** Applying the mechanism to B63's factorization
  `char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2(t+1)`:

  ```text
  P-symmetric      : char(M^2), char(M^4), char(-M^2)   (even |k|; L_k even in m)
  P-antisymmetric  : char(M^-1), char(M), char(M^3)     (odd  |k|; L_k odd  in m)
  ```

  verified factor-by-factor via Dickson parity. The depth-4 derivative sequences
  are built (seed/homogeneous degree 3 -- "cubic" -- plus forced degree 4), the
  depth-4 analog of B54's depth-3.

## The one obstruction to a full symbolic SL(4) Jacobian (localized)

A from-scratch symbolic Jacobian (which would upgrade B63 from computer-assisted
to a symbolic proof) needs more than the fundamental representation at exactly
one place: the `e_2 = tr(A^2)` (equivalently `tr(Λ^2 A)`) coordinate. Its
substitution image is

```text
tr((A^m B)^2) = (tr(A^m B))^2 - 2 tr(Λ^2(A^m B)),
tr(Λ^2(A^m B)) = tr((Λ^2 A)^m (Λ^2 B)),
```

a single-block trace in the **6-dimensional exterior square `Λ^2 V`** (a depth-6
recursion), not a fundamental `τ_k`. So the even-`k` (P-symmetric) sector rows
require `Λ^2 V`; the fundamental depth-4 sequences alone do not close them. This
is the precise residual hard core of B58 — and it sits exactly in the even-`k`
sector the parity mechanism predicts.

## Run

```bash
python frontier/B64_parity_mechanism/probe.py
python -m pytest tests/test_b64_parity_mechanism.py -q
```
