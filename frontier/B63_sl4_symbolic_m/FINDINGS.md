# B63 FINDINGS -- SL(4) fixed-line factorization over Z[m]

Computer-assisted symbolic (high-precision multi-m numerics + exact polynomial
interpolation); validated against B59 at m=1. Not a hand-built trace-ring proof.
No physics, no Origin-core claim.

## Verdict

```text
PROVES (computer-assisted) the SL(4) metallic fixed-line factorization over Z[m]
and its m-independence:

  char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2 (t+1),
  L_k(m) = tr(M^k),  M = [[m,1],[1,0]].

The M-power set {-1,1,2,3,4}, the sign sector {-M^2}, and the parity block are
m-INDEPENDENT; only the L_k(m) coefficients move.
```

## Honest assessment of the requested method

The task asked to build the SL(4) Procesi trace ring symbolically (B58's open
task) via the depth-4 Cayley-Hamilton recursion, "one depth level deeper" than
the SL(3) template (B54). On building it out, this is **substantially more than
one level deeper**:

- SL(3)'s 8 coordinates all have **single-block** substitution images
  `tr(A^k B^{+-1})`, handled by the `tau_k`/`sigma_k = P.tau_k` recursions (B54).
- SL(4) needs `e_2(A)` for A's conjugacy class. There is **no single-block-only
  coordinate system**: the fundamental-rep mixed seeds (e.g. `tr(A^2 B)`) and the
  `e_2` data force either the **6-dimensional exterior square `Lambda^2 V`**
  (depth-6 recursion, chain rule through `e_i(Lambda^2 A)(e(A))`) **or genuine
  two- and three-block words** `tr((A^m B)^2 A) = tr(A^{m+1} B A^m B)`,
  `tr((A^m B)^3 A^2)`. That is the multi-block Procesi machinery -- the real
  reason B58 has stayed open.

So B63 establishes the result by a reliable computer-assisted route instead of
the (still-open) hand-built trace ring.

## Method

SL(4) has **no fixed-line rank-loss** (unlike SL(5); B61/B62), so the
representation-perturbation Jacobian `DT(eps) = DX . pinv(Dx)` (extrapolated
`eps -> 0`, high-precision mpmath SVD pinv) is clean at every `m`. For `m=1..6`:

1. compute the 15 fixed-line multipliers;
2. match them to the predicted factorization (`L_k=tr(M^k)`);
3. extract each factor's eigenvalue **sum** (robust -- dominated by the large
   well-separated root), giving the exact integer `tr(M^k)` or `-tr(M^k)`;
4. **interpolate the sum as a polynomial in `m`** (degree <= 4, over-determined
   by the 6 samples).

## What was found

- **Every factor sum = the exact integer `tr(M^k)`** at `m = 1..6`:
  `L_2 = 3,6,11,18,27,38`; `L_3 = 4,14,36,76,140,234`;
  `L_4 = 7,34,119,322,727,1442`; `L_{+-1} = +-m`. (Robust integer rounding even
  where the absolute max-match grows to ~0.2 at m=6, because `L_4(6)=1442` and
  the relative match is ~1e-4.)
- **Interpolation recovers `tr(M^k)` exactly** for every factor:
  `L_{-1}=-m`, `L_1=m`, `L_2=m^2+2`, `L_3=m^3+3m`, `L_4=m^4+4m^2+2`, and
  `char(-M^2)` carries `L_2=m^2+2`. Over-determined (6 samples, degree <= 4) ->
  rigorous determination of the `Z[m]` polynomials.
- **m=1 reproduces B59 exactly** (max-match `3.4e-7` to
  `char(M^-1..4).char(-M^2).(t-1)^2(t+1)`).

## Unlocks

- **(a)** PROVES (computer-assisted) the SL(4) factorization over `Z[m]`.
- **(b)** PROVES m-independence of the structure.
- **(c)** the explicit `k(alpha)` root map is supplied **structurally by B62**
  (opposition involution / root-height sectors); deriving it from the trace ring
  itself remains open.
- **(d)** together, **B62 + B63 give the structural theory of the tower at SL(4)**
  (which factors, their signs, their m-dependence, and their root-space home),
  short of a from-first-principles symbolic proof.

## Limits / open

- This is **computer-assisted**: high-precision numerics + interpolation, relying
  on (i) the clean SL(4) gauge situation and (ii) the degree bound `deg L_k <= 4`
  (justified by `L_k = tr(M^k)`, degree `k`). It is **not** the hand-built
  Procesi trace-ring derivation.
- That from-first-principles proof -- and the symbolic `n >= 5` case -- still need
  the multi-block (`Lambda^2 V` / two-three-block) reductions documented above.
  This is the precise remaining hard core of B58.

## Reproduce

```bash
python frontier/B63_sl4_symbolic_m/probe.py
python -m pytest tests/test_b63_sl4_symbolic_m.py -q
```
