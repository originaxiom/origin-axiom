# B55 -- c=1 Fixed-Line Structure (general m)

## Question

B54 characterized the metallic `SL(3)` fixed-line Jacobian at `c=1` only for
`m=1` (the Eisenstein/golden twins). What are both exchange sectors at `c=1` for
**general m**?

## Status

```text
FRONTIER EVIDENCE
PC12 SUPPORT
NO CLAIM PROMOTION
```

## Run

```bash
python frontier/B55_c1_fixed_line_structure/probe.py
```

## What It Checks

```text
symmetric sector (mod 4):
  m = 1, 3 (mod 4): (t-1)(t+1)(t^2 - t + 1)   Phi_6 (Eisenstein)
  m = 2     (mod 4): (t-1)(t+1)(t^2 + 1)        Phi_4 (Gaussian)
  m = 0     (mod 4): (t-1)^3 (t+1)              degenerate (parabolic)
antisymmetric sector (all m):
  (t-1)(t+1)(t^2 - m t - 1)                     char(M), universal
```

Proved per residue class mod 4 with `m` symbolic, then cross-checked
numerically for `m = 1..12`, with `m=1` reproducing B54's twins.

## Why mod 4

At `c=1` the fixed-line derivative recurrence
`dtau_k = dtau_{k-1} - dtau_{k-2} + dtau_{k-3} + (e_x1 - e_x4)` has characteristic
equation `(r-1)(r^2+1) = 0`, roots `{1, i, -i}`. The constant forcing resonates
with the root `r=1`, giving a single linear-in-k term (slope
`L = (1/2,0,0,-1/2,0,0,0,0)`, in the `x1, x4` coordinates only) on top of a
period-4 part. So `dtau_k = k*L + Q(k mod 4)` with `Q` periodic, hence
`dtau(k+4) = dtau(k) + 4L`. The period-4 part gives the mod-4 cyclotomic
symmetric sector; the linear term gives the `m`-dependent
`char(M) = t^2 - m t - 1` in the antisymmetric sector.

## Scope Note

The `c=1` Eisenstein factor `t^2-t+1` (discriminant `-3`) shares its polynomial
with the figure-eight ideal-tetrahedron shape, but that resemblance is a
**cyclotomic coincidence**, not an invariant-surface connection -- see
`frontier/B56_figure_eight_invariant_surface/` for the negative control. The
discriminant pair `(-3, 5)` of the `c=1` twins does coincide with the factors of
the figure-eight gluing equation `z^2(z-1)^2 = (z^2-z+1)(z^2-z-1)` (claim P12);
that is recorded as a structural echo only, not a promoted claim.
