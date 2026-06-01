# B51 -- SL(3) Symbolic-m Factorization

## Question

Can the `c=3` fixed-line Jacobian factorization in PC12 be proved with `m` as
a formal parameter, rather than checked case-by-case over integer rectangles?

## Status

```text
PROOF-HARDENING FRONTIER
PC12 SUPPORT
NO CLAIM PROMOTION
```

B51 strengthens the proof architecture for PC12. It does not make PC12
`DRAFTABLE`, does not promote any Origin-core claim, and does not create a
physics bridge.

## Run

```bash
python frontier/B51_sl3_symbolic_m_factorization/probe.py
```

## What It Checks

```text
closed-form derivative sequences at the c=3 triple-root fixed line
symbolic 8x8 Jacobian J(m) with entries polynomial in m
exchange involution P commutes with J(m)
block diagonalization into symmetric and antisymmetric sectors
symbolic characteristic polynomial identities:
  symmetric     (t-1)(t+1)(t^2-(m^2+2)t+1)
  antisymmetric (t^2+mt-1)(t^2-(m^3+3m)t-1)
```

This replaces the previous `m<=50` confidence check for the `c=3` block
factorization with a formal symbolic proof module.
