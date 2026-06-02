# B65 FINDINGS -- the symbolic SL(4) Jacobian, char poly factored over Z[m]

Computer-assisted (over-determined rational reconstruction of the entries) +
exact symbolic factorization. No physics, no Origin-core claim.

## Verdict

```text
The full 15x15 SL(4) fixed-line Jacobian J(m) is determined exactly over Z[m],
and char(J(m)) factors -- as exact symbolic algebra -- as

  char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2 (t+1).

This is the SL(4) factorization as a DIRECT symbolic factorization of the full
Jacobian (factorization derived, not matched). Matches B63/B64; m=1 = B59.
```

## How (entry-interpolation route)

A hand-built Procesi trace ring needs multi-block reductions: a rank check showed
single-block V + Λ^2 traces span only **12 of 15** character-variety dimensions,
so genuine mixed two-block words are unavoidable (this sharpened B64's
even-k/Λ^2 obstruction). The chosen route sidesteps that:

1. The Jacobian entries in the fixed B59 word basis are **canonical
   (seed-independent) rationals, polynomial in m of degree 4** (verified:
   `max|J(seed10)-J(seed11)| ~ 8e-6`, i.e. seed-independent to extrapolation
   precision).
2. Computed `DT(0)` at high precision (mpmath dps 50, tight eps-ladder; SL(4) is
   gauge-clean -- no fixed-line rank-loss, unlike SL(5)) for `m=1..7`, one seed.
3. Reconstructed each entry as an exact rational (worst error `~7e-5` at m=7,
   `~1e-12` at m=1; all entries reconstruct, denominators <= ~12).
4. Interpolated each entry to a degree-4 polynomial in m -- **over-determined**
   (degree 4 fixed by 5 points, verified on 7) -> `J(m)` rigorously fixed
   (`jacobian_m.json`).
5. `sympy.factor(char(J(m)))` over `Z[m]` -> the seven Dickson factors.

## What this adds over B63/B64

- **B63** matched the numerical spectrum to a predicted factorization
  (per-factor L_k interpolation) -- computer-assisted *verification*.
- **B64** proved the sector assignment symbolically (parity mechanism).
- **B65** reconstructs the **entire Jacobian** `J(m)` and **factors its
  characteristic polynomial directly** -- the factorization is the *output* of
  exact symbolic factoring of `J(m)`, not a matched template. This is the
  strongest available statement short of a hand-derived trace ring.

## Honest status / what remains

- **Computer-assisted but rigorous:** entries from high-precision numerics +
  exact over-determined reconstruction; factorization is exact symbolic algebra.
- **Not the hand-built Procesi trace ring.** The purist from-first-principles
  symbolic proof for all `n` (the ambient `SL(n,C)` trace ring with the
  multi-block / `Λ^2` machinery; B58) remains the open item. B64 reduced its SL(4)
  core to the mixed two-block sector; B65 obtains the factorization by
  reconstruction instead of deriving it from that ring.

## Tower theory status after B65

```text
n  factorization                                                  status
2  char(M^2)                                                      symbolic
3  char(M^-1)char(M^2)char(M^3)(t-1)(t+1)                         symbolic, all m (B54)
4  char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)         J(m) over Z[m] +
     (t-1)^2(t+1)                                                   factored (B65)
5  ...char(M)^2 char(M^2)^2 ... (t-1)^2(t+1)^2                    22 numeric (B61) +
                                                                    2 structural (B62)
```
Structural theory: which factors (B59-B62); the proven k(alpha) sector map (B64);
m-dependence L_k=tr(M^k) (B63); and now the full SL(4) Jacobian over Z[m] with a
direct char-poly factorization (B65).

## Reproduce

```bash
python frontier/B65_sl4_symbolic_jacobian/probe.py
python frontier/B65_sl4_symbolic_jacobian/compute.py   # regenerate J(m) (~5 min)
python -m pytest tests/test_b65_sl4_symbolic_jacobian.py -q
```
