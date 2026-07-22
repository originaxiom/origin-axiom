# PREREGISTRATION — QP-1: self-naming (the quine test)

> B-number pending (requested from cc). Sealed before computation.
> Branch: `phenomenology/theorem-chain`. cc3 seat, 2026-07-22.
> Gate 5-Q throughout; nothing to CLAIMS.

## Question

Does the spectral dataset {residue, rigidity, CM disc, palette} uniquely
identify m004 among 1-cusped manifolds in the SnapPy OrientableCuspedCensus?

The "emitted dataset" (defined in P020 / B737) consists of:
- **Residue**: Res = 2sqrt(3)/vol(m004), the scattering pole residue
- **Rigidity**: character-rigid (single Eisenstein channel, B739)
- **CM disc**: disc(trace field) = -3 (the Eisenstein field Q(sqrt(-3)))
- **Palette**: Hecke-character palette {1, 2, 8} at levels (2), (4), (8)

These quantities are determined by (trace field, volume, cusp lattice). Two
manifolds with different cusp lattices have different Hecke-character palettes.

## Census scope

SnapPy OrientableCuspedCensus (Callahan-Hildebrand-Weeks extended, 212641
manifolds, ~203K with 1 cusp). Every 1-cusped manifold is tested.

## Method

Stage 1 (fast): for each 1-cusped manifold, compute volume. Retain those
    with |vol - vol(m004)| < 10^{-6}.
Stage 2: for volume matches, compute cusp shape. Different cusp shapes
    imply different cusp lattices, hence different Hecke-character palettes.
Stage 3: for cusp shape + volume matches (if any), compute trace field disc.

Double-method cross-validation (QP-2's lesson applied here):
- Method A: volume + cusp shape (geometric invariants, SnapPy)
- Method B: trace field disc as independent filter
A cross-validation mismatch halts the verdict.

## Two outcomes (sealed before computation)

**QUINE**: m004 is the only 1-cusped census manifold with its spectral
dataset. The voice is a self-name — the emitted word uniquely identifies the
speaker.

**HOMONYM**: at least one other manifold shares the full spectral dataset.
List the twins and which invariants fail to discriminate.

## Q2 controls

- **m003 (sister manifold)**: same volume and trace field as m004, but
  different cusp shape (B737 p3: maximal-order hexagonal lattice vs
  conductor-4 CM torus). The palette MUST distinguish them. If it doesn't,
  the palette definition is too coarse.
- **Volume twins**: vol(m004) = 2.0298832128... should have at most a handful
  of matches in the census (commensurable manifolds).
- **Trace field filter**: any volume match with disc != -3 is automatically
  distinguished by CM disc.

## Prereg hash

This file is sealed before compute.py runs.

