# Frontier — Quarantined Phase B Work

This directory holds **speculative, `open`-status** research — see `../CLAIMS.md`
(O1–O9) and `../GOVERNANCE.md`. Nothing here is a claim; results are logged
observations only.

A result moves from here into the proven core (`../src/`) **only** by passing the
`conditional → proven` gate in `GOVERNANCE.md` §5 — code, a test, scrutiny, and a
logged status change.

**Phase B is in progress.** Probes logged so far:

## Dependency Graph

```text
B13-B16 established the current kernel:
  A1-A6 -> A
  (L X)^2=A -> X=+/-P
  F=L P, F^2=A
  trace lift of F contains the A-sector

B18 trace-lift functoriality
  gates B20, B21, B23, B24

B19 exchange/half-step axiom audit
B17 alternation/persistence selector
B22 spectrum genericity controls

B20 operational awareness test
B21 spacetime / Weil-Petersson dictionary test
B23 BKL / gravity controls
B24 anyon / quantum bridge
```

- **B1–B5** — gluing vs. Chern–Simons flatness, moduli evolution, Regge complex,
  BKL/Gutzwiller, Wheeler–DeWitt.
- **B6–B9** — the field-theoretic lift of the derived potential (P15/P16):
  the field equation `□τ+κ(τ²−τ−1)=0` (B6), Fisher–KPP creation dynamics (B7),
  the particle spectrum and the non-exact `m/g≈φ` near-miss (B8), and the
  fusion–scattering shared polynomial (B9). Each carries its caveat; none is a
  claim. See `../PROGRESS_LOG.md` 2026-05-27.
- **B13** — the punctured-torus trace map on the fiber character variety. Exact
  algebra shows the trace-map linearization contains the `A` quadratic as a
  lattice-conjugate rank-2 sector, but the bridge to physical `3+1`, matter,
  gravity, or awareness remains an inserted dictionary.
- **B14** — the half-step square-root selector. Exact algebra shows `A` has only
  two `GL(2,Z)` square roots, `F=L P` and `-F`, and that mixed closures
  `B(a,b)=L_aR_b` admit an integer orientation-reversing square root iff `a=b`.
  The remaining gap is whether the record-swap `P` is forced or inserted.
- **B15** — trace-map invariant controls. Exact algebra confirms the
  Eisenstein-to-golden diagonal linearization family and the discrete
  Fricke-Vogt invariant; it rejects the naive continuum proxy and rejects a
  proposed `sqrt(5)` Fibonacci coupling under the current invariant
  normalization.
- **B16** — record-swap status. Exact algebra shows `P` is unique up to sign as
  the involution exchanging the primitive pair `{L,R}`, but the exchange
  symmetry itself is not forced by the current A1-A6 minimal-record axioms.
- **B17-B24** — half-step kernel campaign. B18 establishes the trace map as the
  canonical half-step trace lift; B19/B17/B22 control the exchange, alternation,
  and spectrum claims; B20/B21/B23/B24 test awareness, spacetime, gravity, and
  anyon dictionaries and leave them stalled where no dictionary is derived.
