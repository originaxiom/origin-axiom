# B65 -- The symbolic SL(4) fixed-line Jacobian J(m), factored over Z[m]

**Status:** the full 15x15 SL(4) fixed-line Jacobian as an exact matrix over
`Z[m]`, with `char(J(m))` **factored directly** as symbolic algebra. Entries are
computer-determined (high-precision numerics + over-determined rational
reconstruction); the factorization is exact symbolic algebra. Standalone
trace-map mathematics; no physics, no Origin-core claim.

## Result

```text
char(J(m)) = char(M^-1) · char(M) · char(M^2) · char(M^3) · char(M^4)
           · char(-M^2) · (t-1)^2 (t+1)            (exact, over Z[m])
```

with `char(M^k)=t^2-L_k t+(-1)^k`, `char(-M^k)=t^2+L_k t+(-1)^k`, `L_k=tr(M^k)`,
`M=[[m,1],[1,0]]`. Explicitly the seven factors are

```text
t^2 + m t - 1                  (char M^-1)
t^2 - m t - 1                  (char M)
t^2 - (m^2+2) t + 1            (char M^2)
t^2 - (m^3+3m) t - 1           (char M^3)
t^2 - (m^4+4m^2+2) t + 1       (char M^4)
t^2 + (m^2+2) t + 1            (char -M^2)
(t-1)^2 (t+1)                  (parity)
```

This is the SL(4) factorization as a **direct symbolic factorization of the full
Jacobian** -- the strongest form: B63 matched the spectrum to a predicted form
(computer-assisted), B64 proved the sector assignment; B65 reconstructs the whole
`J(m)` and `sympy.factor`s its characteristic polynomial, so the factorization is
*output*, not matched.

## Method (entry-interpolation; the route chosen over the hand-built trace ring)

A from-first-principles symbolic trace ring needs multi-block (two-block)
reductions (B64 localized the gap; a rank check showed single-block V+Λ² traces
span only 12 of 15 dimensions). B65 sidesteps that: the Jacobian entries in the
fixed B59 word basis are **canonical (seed-independent) rationals, polynomial in
`m` of degree 4**, so they can be reconstructed from numerics:

1. **Compute** `DT(0) = lim_{eps->0} DX·pinv(Dx)` at high precision (mpmath
   dps 50, tight eps-ladder; SL(4) has no fixed-line rank-loss, so this is clean)
   for `m = 1..7` (one seed -- entries are seed-independent).
2. **Reconstruct** each entry as an exact rational (denominators up to ~12;
   worst reconstruction error `~7e-5` at `m=7`, `~1e-12` at `m=1`).
3. **Interpolate** each entry as a polynomial in `m`. Degree is 4, determined by
   5 points and **verified over-determined on 7** -- so `J(m)` is rigorously
   fixed. Stored in `jacobian_m.json`.
4. **Factor** `char(J(m))` over `Z[m]` symbolically -> the product above.

Validation: matches B63's factorization and B64's sector assignment over `Z[m]`;
`m=1` reproduces B59 exactly.

## Honest status

- **Computer-assisted, but rigorous.** The entries come from high-precision
  numerics + exact, over-determined rational reconstruction (degree-4 polynomials
  fixed by 5 points, checked on 7); the factorization is then exact symbolic
  algebra on `J(m)`. This is the route chosen over the hand-built trace ring.
- **Not the hand-derived Procesi trace ring.** The genuine from-first-principles
  symbolic proof for all `n` (the ambient `SL(n,C)` trace ring with multi-block /
  `Λ^2` machinery, B58) remains the purist open item; B64 reduced its SL(4) core
  to the mixed two-block sector, and B65 obtains the same factorization by
  reconstruction instead.

## Files

- `compute.py` -- regenerates `J(m)` from numerics and re-verifies (~5 min).
- `jacobian_m.json` -- the reconstructed `J(m)` (committed artifact).
- `probe.py` -- loads `J(m)`, factors `char(J(m))`, verifies the identity.

## Run

```bash
python frontier/B65_sl4_symbolic_jacobian/probe.py      # load J(m), factor, verify (fast)
python frontier/B65_sl4_symbolic_jacobian/compute.py    # regenerate J(m) from numerics (~5 min)
python -m pytest tests/test_b65_sl4_symbolic_jacobian.py -q
```
