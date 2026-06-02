# B54 -- General-c Exchange Structure

## Question

B51 proved the exchange involution `P` block-diagonalizes the metallic `SL(3)`
fixed-line Jacobian at the representation point `c=3`. Does the commutation hold
along the **whole** fixed line, and what sector structure appears off `c=3`?

## Status

```text
FRONTIER EVIDENCE
PC12 SUPPORT
NO CLAIM PROMOTION
```

B54 strengthens the proof architecture for PC12 (a standalone trace-map note).
It does not promote any Origin-core claim, does not derive a selector, and does
not build a physics dictionary.

## Run

```bash
python frontier/B54_general_c_exchange_structure/probe.py
```

## What It Checks

```text
[J(m,c), P] = 0 for symbolic c (m=1,2,3)   -- generalizes B51 (c=3) to all c
c=1: symmetric sector  carries Eisenstein t^2-t+1   (discriminant -3)
     antisymmetric     carries golden     t^2-t-1   (discriminant 5)
m=1 sweep: symmetric quadratic t^2-ct+1 = Phi_3, Phi_4, Phi_6, (t-1)^2, char(A)
           at c = -1, 0, 1, 2, 3
c=3 regression: reproduces B51 sectors (t-1)(t+1)(t^2-(m^2+2)t+1)
                and (t^2+mt-1)(t^2-(m^3+3m)t-1) for m=1,2,3
```

## Why The Commutation Is General

`[J(m,c), P] = 0` for all `c` is structural, not a `c=3` coincidence: the trace
map is equivariant under the coordinate exchange `P` (forward `tau`-chain
<-> backward `sigma`-chain), and the fixed line `x_i = c` is `P`-invariant, so the
Jacobian commutes with `P` at every point of it. This is the
reversing/exchange-symmetry phenomenon standard for trace maps (cf.
Baake-Roberts, *Symmetries and reversing symmetries of trace maps*).

## Scope Notes

- The clean cyclotomic sweep is **`m=1`-specific**: for general `m` the symmetric
  `c=1` polynomial depends on `m` parity (`Phi_6` for odd `m`, `Phi_4` for even).
  The `m`-general `c=1` facts are the antisymmetric `char(M)=t^2-mt-1` and the
  `c=3` factorization.
- The `c=1` Eisenstein/golden pair has discriminants `-3` and `5` -- the same
  pair as the figure-eight gluing equation `z^2(z-1)^2 = (z^2-z+1)(z^2-z-1)`
  locked by `tests/test_gluing_equation.py` (claim P12). The coincidence is
  recorded as a structural echo, not promoted to a claim.
