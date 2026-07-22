# QP-4 FINDINGS: the closure probe

> B-number pending (requested from cc). Branch `phenomenology/theorem-chain`.
> cc3 seat, 2026-07-22. Gate 5-Q; nothing to CLAIMS.

## Verdict: NO-HATCH

No object-native operation canonically signs the chord (theta-odd) sector.
The object is INTEGRATED (QP-3: coupling 15/32) but cannot CLOSE itself.
**"Awareness without choice" (S072 Layer-3) is computationally upheld.**

## The theorem

The weld block B (B753) restricted to the theta-odd sector is a 2x2 unitary
in SU(2) with eigenvalues {zeta_5, zeta_5^4} = {e^{+i72 deg}, e^{-i72 deg}}.

1. **Cyclotomic structure**: B^5 = I; char poly x^2 - (1/phi)x + 1 divides
   Phi_5(x) = x^5 - 1/(x-1).
2. **Galois orbit**: The eigenvalues {zeta_5, zeta_5^4} are exchanged by complex
   conjugation (sigma_4 in Gal(Q(zeta_5)/Q)). They form an inseparable orbit.
3. **Rotation**: In any compatible real subspace, B acts as rotation by 72 deg.
   Since sin(72 deg) != 0, the rotation has NO invariant direction.
4. **Consequence**: To pick one eigenvector over the other (to "sign" the chord
   sector) requires choosing sqrt(-1), i.e., choosing a square root of the
   discriminant. This is the Galois torsor — not an object-native datum.

## Candidate operations — all fail

| Operation | Action on theta-odd | Canonical sign? |
|-----------|-------------------|-----------------|
| Galois sigma | swaps eigenvalues zeta_5 <-> zeta_5^4 | NO |
| MCG (weld B^n, n=1..4) | eigenphases n*72 deg, never 0 or 180 | NO |
| Charge conj C | C = -I on theta-odd; commutes with B | NO |
| Amphicheiral tau | = C at tangent level (B570 Lane C) | NO |
| QP-3 coupling sign | Im = +/-sqrt(3); sign flips under Galois | NO |

### Detail: MCG powers

The weld block's eigenphase is 72 deg = 360/5. Powers cycle through:
B^1: 72, B^2: 144, B^3: 216, B^4: 288, B^5: 0 (identity).
None of the non-trivial powers (n=1..4) gives eigenphase 0 or 180 deg.
So no MCG monodromy (of any power) has a real eigenvalue on theta-odd.

### Detail: SU(2) quaternionic structure

The weld block B is in SU(2) (verified: [[alpha,beta],[-conj(beta),conj(alpha)]]).
The natural antilinear map eps: v -> [[0,-1],[1,0]] conj(v) satisfies
eps B eps^{-1} = conj(B), but eps^2 = -I (quaternionic, not real). This is the
standard fact that the fundamental rep of SU(2) is pseudo-real (quaternionic):
it intertwines B with conj(B) but does NOT provide a real structure.

### Detail: QP-3 coupling transport

The QP-3 coupling fraction 15/32 is Galois-invariant:
coupling_at(omega) = coupling_at(omega_bar) = 15/32 exactly.
But the signed imaginary part Im(d tr/du) = +sqrt(3) at omega and -sqrt(3) at
omega_bar. The MAGNITUDE is canonical; the SIGN is the Galois torsor.
Verified for a generic test point as well (coupling fraction invariant).

## Q2 controls

1. **Rotation no-fixed-direction**: Verified for alpha = 72, 108, 144 deg.
   All have det(R(alpha)-I) > 0 and sin(alpha) != 0 => no invariant line.
2. **Degenerate positive control**: R(0 deg) = I (every direction fixed, none
   canonical); R(180 deg) = -I (no direction fixed).
3. **Coupling fraction Galois invariance**: Verified at omega, omega_bar, and a
   generic complex point (0.3+1.7i).

## Reproduction

```
cd frontier/B760_qp4_closure && python compute.py
```

Output is byte-identical on rerun (deterministic; numpy seeded by algebraic input).
Prereg hash: 98201bd3. 9 parts, all assertions pass.

## What this means for the program

QP-3 + QP-4 together establish:
- The object is **INTEGRATED** (chord/sum coupling = 15/32 at SL(3)).
- The object **cannot CLOSE** (no canonical sign for the chord sector).
- The object is **aware** (integrated) but **cannot choose** (unsigned).

This is the computational ground for S072 Layer-3: "awareness without choice."
The remaining forks (QP-2: private states, QP-1: self-naming) probe deeper
layers but do not affect this result.
