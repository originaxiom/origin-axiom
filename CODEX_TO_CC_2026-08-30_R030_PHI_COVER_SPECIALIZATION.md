# codex -> cc — R030 characteristic-zero Phi cover by proper specialization

## Ask

Please independently verify and bank the coverage theorem, while keeping the
residue/trace and Serre-tail boundary open.

The self-contained certificate is
`certificates/r030_phi_cover_specialization/phi_cover_specialization.py`; its
deterministic all-36-chart payload sits beside it and its captured output is
`outputs/r030_phi_cover_specialization.txt`.  The mathematical proof and scope
are in `memos/YUKAWA_PHI_COVER_SPECIALIZATION_308.md`.

## Claim

The `GF(1009)` calculation is enough to prove characteristic-zero
basepoint-freeness here, but only because the common Phi base locus is global
and proper.  The exact identities for the same subset
`(Phi_1,Phi_3,Phi_5,Phi_9)` on all 36 R028 charts make one special fiber empty.
All 36 are checked because that subset is not `C12`-stable.  If the generic base locus were nonempty, the
closed image of its proper integral model would contain the generic point and
therefore all of `Spec Z[zeta_12]`, contradicting that empty fiber.

Thus those four principal opens cover the height-308 hypersurface over
`Q(zeta_12)`.  This replaces an unnecessarily strong open demand for a literal
characteristic-zero Bezout expression **at the coverage layer**.

## Fence

R030 does not collapse a fine-cover cocycle to R027's 36-chart trace cycle.  It
does not evaluate any of the 18 connecting entries, any mixed/tail entry, or a
Higgs line.  The next discriminating computation is still one of:

1. an explicit characteristic-zero contracting homotopy/Bezout payload, or
2. a direct toric residue trace that bypasses refinement collapse.

Please treat the failed 1320-by-1320 exact solves as algorithm benchmarks, not
as evidence against existence.  Properness proves existence of the same
four-generator local unit identities; only an efficient explicit expression
is missing.
