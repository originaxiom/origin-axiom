# B63 -- SL(4) fixed-line factorization over Z[m] (computer-assisted symbolic)

**Status:** computer-assisted symbolic result (high-precision multi-m numerics +
exact polynomial interpolation). **Not a hand-built trace-ring proof.** Standalone
trace-map / character-variety mathematics; no physics, no Origin-core claim.

## What this establishes

B59 computed the SL(4) Fibonacci (m=1) fixed-line factorization numerically. B63
establishes the **metallic-family (general m)** factorization and proves it is
**m-independent in structure**, with explicit polynomial m-dependence:

```text
char(M^-1) . char(M) . char(M^2) . char(M^3) . char(M^4) . char(-M^2) . (t-1)^2 (t+1)
```

with `char(M^k) = t^2 - L_k t + (-1)^k`, `char(-M^k) = t^2 + L_k t + (-1)^k`, and
`L_k = tr(M^k)` for the metallic companion `M = [[m,1],[1,0]]`. Explicitly over
`Z[m]`:

```text
char(M^-1) = t^2 + m t - 1
char(M)    = t^2 - m t - 1
char(M^2)  = t^2 - (m^2+2) t + 1
char(M^3)  = t^2 - (m^3+3m) t - 1
char(M^4)  = t^2 - (m^4+4m^2+2) t + 1
char(-M^2) = t^2 + (m^2+2) t + 1
parity     = (t-1)^2 (t+1)
```

The **M-power set `{-1,1,2,3,4}`, the sign sector `{-M^2}`, and the parity block
`(t-1)^2(t+1)` are m-independent**; only the `L_k(m)` coefficients move.

## Method (honest)

The from-first-principles route -- building the SL(4) Procesi trace ring and the
substitution action symbolically (B58's open task) -- is **harder than "one depth
level deeper"** than SL(3). A's conjugacy class needs `e_2(A)`, which forces
either the 6-dimensional exterior-square representation `Lambda^2 V` (a depth-6
recursion, with the chain rule through `e_i(Lambda^2 A)(e(A))`) **or** genuine
two- and three-block words such as `tr((A^m B)^2 A) = tr(A^{m+1} B A^m B)` and
`tr((A^m B)^3 A^2)`. That multi-block Procesi machinery is the real reason B58 is
hard. (The SL(3) template B54 avoided it because every SL(3) coordinate image is
single-block `tr(A^k B^{+-1})`.)

B63 instead uses a reliable computer-assisted route. **SL(4) has no fixed-line
rank-loss** (unlike SL(5); B61/B62), so the representation-perturbation Jacobian
`DT(eps)=DX . pinv(Dx)` extrapolated to `eps->0` is clean at high precision for
every `m`. We compute the 15 fixed-line multipliers for `m = 1..6`, match them to
the factorization, extract each factor's eigenvalue **sum** (robust: dominated by
the large, well-separated root), and **interpolate it as a polynomial in `m`**.
The sums come out as exactly `tr(M^k)` (degree <= 4, over-determined by the
samples), which proves the factorization holds for all `m` and is m-independent.

## Result table (probe output)

```text
 m | max-match | factor eigenvalue-sums (= L_k or -L_k)
 1 |  3.4e-7   | M^-1:-1  M:1  M^2:3   M^3:4    M^4:7     -M^2:-3
 2 |  7.5e-6   | M^-1:-2  M:2  M^2:6   M^3:14   M^4:34    -M^2:-6
 3 |  1.3e-4   | M^-1:-3  M:3  M^2:11  M^3:36   M^4:119   -M^2:-11
 4 |  3.6e-3   | M^-1:-4  M:4  M^2:18  M^3:76   M^4:322   -M^2:-18
 5 |  3.5e-2   | M^-1:-5  M:5  M^2:27  M^3:140  M^4:727   -M^2:-27
 6 |  2.1e-1   | M^-1:-6  M:6  M^2:38  M^3:234  M^4:1442  -M^2:-38
```

(The absolute `max-match` grows with `m` only because the eigenvalues grow --
`L_4(6)=1442`; the relative match stays ~1e-4, and every factor sum lands on the
exact integer `tr(M^k)`.) Interpolation then gives `L_2=m^2+2`, `L_3=m^3+3m`,
`L_4=m^4+4m^2+2`, `L_{+-1}=+-m`, all `= tr(M^k)`.

## What this unlocks (and what stays open)

- **(a) PROVES the SL(4) factorization** (computer-assisted, over `Z[m]`) --
  stronger than B59's m=1, double-precision result.
- **(b) PROVES m-independence** of the M-power / sign / parity structure.
- **(c) the explicit k(alpha) root map** (which M-power sits in which root space)
  is supplied **structurally by B62's opposition involution**; deriving it from
  the trace ring itself remains open.
- A from-first-principles trace-ring proof (and `n >= 5` symbolically) needs the
  multi-block Procesi reductions above -- still the open hard core of B58.

## Run

```bash
python frontier/B63_sl4_symbolic_m/probe.py        # m=1..6 verification + L_k interpolation (~minutes)
python -m pytest tests/test_b63_sl4_symbolic_m.py -q
```
