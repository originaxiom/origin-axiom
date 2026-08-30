# Progress bank — 2026-08-30 — R030 proper-specialization cover

## Result

The corrected height-308 subset `(Phi_1,Phi_3,Phi_5,Phi_9)` has empty common
base locus on the characteristic-zero hypersurface.  The result is theorem
grade and does not rely on reconstructing a giant `Q(zeta_12)` Bezout vector.

The committed payload contains the exact integral generators and a literal
`GF(1009)` Bezout identity on each of all 36 toric affine charts.  The portable
certificate independently reconstructs those generators from the source-locked
height-308 vector, norm coefficients and toric frames, reduces them modulo the
order-twelve root `160`, and verifies every sparse identity.  All 36 planted
multiplier perturbations fail.

Because the global common-zero scheme is closed in the projective toric model,
its map to `Spec Z[zeta_12]` is proper.  A nonempty generic fiber would give a
closed image containing the generic point and hence every special point,
contradicting the verified empty fiber above `(1009,zeta_12-160)`.  Therefore
the same four opens cover over `Q(zeta_12)`.

## Exact reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  certificates/r030_phi_cover_specialization/phi_cover_specialization.py
PYTHONDONTWRITEBYTECODE=1 python3 -O \
  certificates/r030_phi_cover_specialization/phi_cover_specialization.py
```

Pinned payload SHA-256:

```text
2efb53af4467fedaef5177f348e2c278311c88f736e4ddb03b843c16271b081e
```

## Boundary moved, not erased

R030 closes characteristic-zero coverage/basepoint-freeness.  It does not give
the explicit contracting homotopy needed to collapse a 144-open four-component
refinement into R027's 36-chart top-trace cycle.  A direct toric-residue bypass
would pay the same remaining obligation.  Until one route is constructed, the
18 connecting entries, mixed/tail blocks, down/lepton ranks and `P3` Higgs-line
fork remain open.

