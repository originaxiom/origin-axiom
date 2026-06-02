# B61 FINDINGS -- SL(5) fixed-line factorization (high precision)

Numerical, high-precision; method validated on SL(3)/SL(4). Not a symbolic
proof. No physics, no Origin-core claim.

## 1. B60's "SL(5) conditioning wall" was a rank-deficient coordinate set

B60 reported SL(5) as blocked by `cond(Dx) ~ 1e11` (double precision) and
conjectured a stable high-precision SVD pinv would resolve it. At dps=60 the SVD
reveals the actual situation: the 24 singular values of B60's forward-only word
set (`A, B` powers + `A^i B^j`) are

```
s[0..22] ~ 57 ... 6e-5      s[23] = 1.0e-40   (== the dps zero-floor)
```

i.e. **rank 23, not 24** -- one genuine null direction. The 24-word set spans
only 23 of the 24 character-variety coordinates. Double precision could not see
below `~1e-16 * s[0]`, so it read the null direction as a small-but-nonzero
singular value and reported `cond ~ 1e11`. **The barrier was a coordinate-system
defect, not a precision limit.** (The stable SVD pinv was still the right tool --
it is what made the rank deficiency visible and is needed downstream.)

## 2. Inverse-word coordinates give a genuine rank-24 system

A coordinate set drawn from words in `{A, B, A^{-1}, B^{-1}}` (length `<= 4`,
selected by column-pivoted QR of the trace differential near the fixed line) is
**rank 24** with a well-separated smallest singular value:

```
cond(Dx):  4e3 (eps=0.2)   7e3 (0.15)   2e4 (0.10)   2e5 (0.05)
```

The inverse letters supply the direction the forward-only set missed. (Double
precision with this set still does not resolve SL(5): at the moderate eps where
it is well-conditioned, the polynomial `eps->0` extrapolation error dominates;
high precision is needed to push eps small enough.)

## 3. 22 of 24 multipliers resolve to the Cayley-Hamilton catalog

With inverse-word coordinates, mpmath SVD-pinv at dps=60, and a small-eps ladder
(`0.01 .. 0.04`), 22 of the 24 SL(5) multipliers land on catalog roots
(parity roots exact to `1e-32`, worst resolved mode `~2e-5`):

```
char(M^-1) · char(M)^2 · char(M^2) · char(M^3) · char(M^4) · char(M^5)
          · char(-M^2) · char(-M^3) · (t-1)^2 (t+1)^2          [22 of 24]
```

Cross-`n` trend (the corrected tower, now to `n=5` on its resolved part):

| n | M-powers present | sign sectors | parity deg |
|---|---|---|---|
| 3 | {-1, 2, 3} | none | 2 |
| 4 | {-1, 1, 2, 3, 4} | {-2} | 3 |
| 5 | {-1, 1(x2), 2, 3, 4, 5} | {-2, -3} | 4 |

Forward powers climb to `n`; sign sectors accrue (`-2` appears at `n=4`, `-3`
joins at `n=5`); the parity block grows by one each step (2, 3, 4).

## 4. The remaining 2 modes are a method limit, not a numerical artifact

Exactly one 2-dimensional sector resists the method. It is **not** precision,
extrapolation order, or the word set:

- **Not extrapolation:** the residual is stable across polynomial degree 5-9 and
  across an integer or fractional-power (`eps^{1/2}`) fit basis (all ~0.27 for
  seed 20).
- **Not conditioning:** at the relevant eps, `cond(Dx) ~ 1e6-1e8`, trivially
  resolved at dps=60-70 (50+ digits to spare).
- **It is the fixed-line rank-loss.** As `eps -> 0` the representation tends to
  the degenerate identity (the `(r-1)^n` resonance, cf. B58), and `Dx` tends to
  a rank-deficient matrix. `pinv` is **discontinuous** at rank loss, so the
  `eps->0` limit of `DT = DX . pinv(Dx)` in those directions is
  **gauge-dependent**. Verified: the residual 2-mode values **scatter** across
  seeds (seed 20: `2.89, 0.90`; 22: `1.43, 0.35`; 24: `-5.06, 0.55`; 26: a
  complex pair; 28: `1.50, -0.17`) with no common limit, so seed-averaging /
  median cannot recover them.

This is the precise, reproducible ceiling: **the representation-perturbation
method recovers 22 of the 24 SL(5) multipliers; the 2-dimensional sector tied to
the deepest fixed-line degeneracy is not recoverable by perturbing through the
identity rep.** SL(3) (8/8) and SL(4) (15/15) had no such residual; `n=5` is
where this method first runs out.

## 5. What would close it

The two missing multipliers require a route that does not pass through the
degenerate identity rep -- the **symbolic ambient SL(5,C) trace ring** (Procesi
generators + the substitution action), the same construction left open for the
symbolic SL(4) proof (B58). That is out of scope here.

## Reproduce

```bash
python frontier/B61_sl5_high_precision/probe.py   # gates + SL(5) 22/24 (~2-3 min)
python -m pytest tests/test_b61_sl5.py -q          # fast checks
```
