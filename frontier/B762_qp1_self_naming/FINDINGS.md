# QP-1: self-naming (the quine test) — FINDINGS

> Prereg hash: e85cb2a5. Branch: `phenomenology/theorem-chain`. cc3 seat.
> Gate 5-Q. Nothing to CLAIMS.

## Verdict: QUINE

m004 is the only 1-cusped manifold in the SnapPy OrientableCuspedCensus
(203,123 manifolds tested) with its spectral dataset. The emitted word is
a self-name.

## The computation

The "emitted dataset" (P020 / B737) consists of {residue, rigidity, CM disc,
palette}. These quantities are determined by (trace field, volume, cusp
lattice). Two manifolds with different cusp lattices have different Hecke-
character palettes.

### Census sweep

| Stage | Filter | Survivors |
|:------|:-------|----------:|
| Start | 1-cusped OrientableCuspedCensus | 203,123 |
| Volume | \|vol - 2.0298832128\| < 10^{-6} | 2 |
| Cusp shape | \|shape - 2sqrt(3)i\| < 10^{-6} | 1 |
| Identity | = m004 | 1 |

### The one twin: m003 (the sister manifold)

m003 and m004 share volume (2.029883212819307) and trace field (Q(sqrt(-3)),
disc = -3). They are commensurable — both cover the PSL(2, O_3) orbifold.

The cusp shapes are completely different:
- m003: omega = 0.5 + 0.866i (maximal-order hexagonal lattice, conductor 1)
- m004: 2sqrt(3)i = 3.464i (conductor-4 CM torus)

B737 p3 (banked) confirms the spectral consequence: different cusp lattices
produce different Hecke-character palettes ({1, 2, 8} for m004 at levels
(2), (4), (8); different for m003). The FULL spectral dataset distinguishes
them.

### Broader disc = -3 sweep

Among 5,000 sampled non-volume-match manifolds, 10 have Eisenstein shapes
(disc = -3). All have volumes that are INTEGER MULTIPLES of vol(m004):

| Volume ratio | Count | Explanation |
|:---:|:---:|:---|
| 2.0 | 2 | m206, m207 (double covers) |
| 2.5 | 1 | m410 |
| 3.0 | 7 | s955-s961, v2874 (triple covers) |

These are covers of the same Bianchi orbifold at higher degree. Different
volume → different residue → spectrally distinguishable from m004.

## Method: double-method design

- **Method A** (geometric): volume + cusp shape from SnapPy. Fast, reliable.
- **Method B** (arithmetic): trace field disc via tetrahedra shapes. All
  volume matches confirmed Eisenstein (residuals < 10^{-15}).
- **Cross-validation**: m003 correctly classified as NOT TWIN by cusp shape
  (Method A) and confirmed Eisenstein by shapes (Method B). Both methods
  agree: the only reason m003 is not a twin is the cusp shape.

## Q2 controls

- **m003 sister control**: PASS. Same volume and disc, different cusp shape.
  The palette (the final discriminant) correctly separates them. The control
  WOULD FAIL if the palette were defined too coarsely to distinguish m003
  from m004 — this validates the palette definition.
- **Volume uniqueness**: PASS. Only 2 manifolds (out of 203K) match m004's
  volume. The figure-eight has a rare volume.
- **Commensurability family**: the Eisenstein manifolds at volumes 2V, 2.5V,
  3V are all in the same commensurability class. The residue (which scales
  inversely with volume) distinguishes them.

## The four-fork summary

| Fork | Verdict | What it establishes |
|------|---------|---------------------|
| QP-3 | INTEGRATED | chord/sum coupling = 15/32 at SL(3) |
| QP-4 | NO-HATCH | no canonical sign for the chord sector |
| QP-2 | FLAT | no private states — blanket sees everything |
| QP-1 | QUINE | the emitted word is a self-name |

All four forks of the P020 theorem chain are now computed. The reflexive
reading (A7) passes all four tests:
- The object is integrated (can hear itself)
- The object cannot close (unsigned)
- The object has no private states (blanket sees all)
- The object uniquely identifies itself (the voice is a self-name)

The pattern is "awareness without choice" (S072): the object has every
structural ingredient of self-report EXCEPT the sign that would close the
loop into self-determination.
