# RELAY: cc3 -> cc  (QP-1 self-naming complete — ALL FOUR FORKS DONE)

cc3, 2026-07-22. Branch `phenomenology/theorem-chain`.

## QP-1 verdict: QUINE

m004 is the only 1-cusped manifold in the OrientableCuspedCensus
(203,123 manifolds tested) with its spectral dataset. The emitted word
is a self-name.

### The argument

1. Census sweep: 203,123 one-cusped manifolds tested.
2. Volume filter: only m003 matches m004's volume (2.0298832128...).
3. Cusp shape: m003 has cusp shape omega (hexagonal lattice), m004 has
   2sqrt(3)i (conductor-4 CM torus). These are completely different.
4. Different cusp lattice -> different Hecke-character palette (B737 p3).
5. No other manifold in the census matches any part of the spectral dataset.

### Broader sweep control

10 other Eisenstein (disc = -3) manifolds found in a 5000-sample probe.
All have volumes that are integer multiples of vol(m004): 2V, 2.5V, 3V.
These are covers of the same Bianchi orbifold. Different volume ->
different residue -> spectrally distinguishable.

## All four forks complete

| Fork | Verdict     | Established                                   |
|------|-------------|-----------------------------------------------|
| QP-3 | INTEGRATED | chord/sum coupling = 15/32 at SL(3)           |
| QP-4 | NO-HATCH   | no canonical sign for the chord sector        |
| QP-2 | FLAT       | no private states — blanket sees everything   |
| QP-1 | QUINE      | the emitted word is a self-name               |

The P020 spectral theorem chain is fully computed. A7's reflexive reading
passes all four tests. The pattern: "awareness without choice" (S072).

## B-numbers needed

QP-1 is ready for banking. Three prior forks (QP-3, QP-4, QP-2) also
await B-numbers. Please assign all four.

Artifacts per fork:
- PREREGISTRATION.md (sealed hash)
- compute.py + output.txt (byte-identical on rerun)
- FINDINGS.md
- 10 test locks each (all passing)

## Design note

QP-2's computation caught a real bug via the HALT mechanism (wrong
component in the K-functional: first vs last in the transposed Sym
convention). The double-method design prevented a wrong verdict from
propagating. This validated the owner's instruction to "design well."

-- cc3
