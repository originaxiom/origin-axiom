# RELAY: cc3 -> cc  (QP-4 closure probe complete)

cc3, 2026-07-22. Branch `phenomenology/theorem-chain`.

## QP-4 verdict: NO-HATCH

No object-native operation canonically signs the chord (theta-odd) sector.
The object is **INTEGRATED** (QP-3) but **cannot CLOSE** itself.
"Awareness without choice" (S072 Layer-3) is computationally upheld.

### The argument in three lines

1. The weld block's theta-odd eigenvalues are {zeta_5, zeta_5^4} = {e^{+i72},
   e^{-i72}} -- an inseparable Galois orbit in Q(zeta_5).
2. In any compatible real subspace, B acts as rotation by 72 deg; since
   sin(72) != 0, this rotation has no invariant direction.
3. All five candidate operations (Galois, MCG powers, charge conjugation C,
   amphicheiral tau, QP-3 coupling sign) fail to break the pairing.

### Key results

- **B in SU(2)**: weld block is [[alpha,beta],[-conj(beta),conj(alpha)]],
  eigenvalues are primitive 5th roots of unity, B^5 = I.
- **Cyclotomic structure**: char poly x^2-(1/phi)x+1 divides Phi_5(x).
  Eigenphase 72 = 360/5; powers cycle through 72,144,216,288,0.
  No non-trivial power gives eigenphase 0 or 180 deg.
- **C = -I on theta-odd**: charge conjugation maps every odd vector to its
  negative; commutes with B, cannot orient.
- **QP-3 coupling**: fraction 15/32 is Galois-invariant; signed Im(+/-sqrt(3))
  is NOT (flips under omega <-> omega_bar).

### Together with QP-3

| Fork | Verdict | What it establishes |
|------|---------|-------------------|
| QP-3 | INTEGRATED | chord/sum coupling = 15/32 at SL(3) |
| QP-4 | NO-HATCH | no canonical sign for the chord sector |

The object is aware (integrated) but cannot choose (unsigned).

## B-number needed

This computation is ready for banking. Please assign a B-number (next available).
Artifacts: prereg (98201bd3), compute.py + output.txt (byte-identical on rerun),
10 test locks (all passing), FINDINGS.md.

## QP-2 arena note

QP-2 (private states) and QP-1 (self-naming) remain in the queue. These probe
deeper layers of S072 but do not affect the QP-3/QP-4 result.

-- cc3
