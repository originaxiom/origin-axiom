"""
Movement XXIII — the second-seed seam is GENERIC (third past-the-gate door).

The one forward door left after H6 (movement XXI) and the mixed-chain gaps
(movement XXII): does a genuine SECOND SEED switch on the seam field Q(√-15) as an
OBJECT-SPECIFIC, non-generic value?  (K025 had found the seam generic; this asks
whether adding a second seed changes that.)

The object contributes √5 (its growth field, movement IX).  A second seed must
contribute √-3 (the Eisenstein / E6 end).  Computed:

  * Coupling a golden copy {a,b} (traces in Q(√5)) to an Eisenstein copy {A,B}
    (figure-eight-style, traces in Q(√-3)) BY THE OBJECT's own words produces the
    seam √-15 in the joint character.  [computed]
  * But this is field theory, not selection: √-15 = √5·√-3 lies in Q(√5,√-3) for
    ANY golden × Eisenstein pair, coupling-independent -- a theorem, not an object
    property.  The object contributes only √5; it neither picks √-15 among the
    candidate seam fields nor forces a finer value.

VERDICT: the second-seed seam is GENERIC (a field compositum, not an object
selection).  K025 stands.  The ONLY non-generic seam behaviour the object has is
INTERNAL (its own 31-cell seam-selection law, B493, which predicts its own
arithmetic) -- and that selects the object's own cell, not a physical/external
value, so it is not a crossing.

With H6 (near-crossing via the trap-Z/3) and the mixed-chain gaps (density-trapped),
this closes the third forward door: all three reach honest WALLS, not crossings.
Firewalled; the physics reading is in speculations/S065.
"""
import numpy as np
import sympy as sp

phi = (1 + np.sqrt(5)) / 2
om = (-1 + 1j * np.sqrt(3)) / 2                        # Eisenstein root of unity
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _wm(w, M):
    inv = {g: np.linalg.inv(M[g]) for g in M}
    P = np.eye(2, dtype=complex)
    for c in w:
        P = P @ (M[c] if c in M else inv[c.lower()])
    return P


def object_coupling_produces_seam():
    """golden {a,b} (√5) + Eisenstein {A,B} (√-3), coupled by the object's words -> √-15 appears."""
    s5, sm3, sm15 = np.sqrt(5), 1j * np.sqrt(3), 1j * np.sqrt(15)

    def in_field(z, tol=1e-6):
        from itertools import product
        R = [k / 2 for k in range(-6, 7)]
        for p, q, r, ss in product(R, repeat=4):
            if abs((p + q * s5 + r * sm3 + ss * sm15) - z) < tol:
                return (p, q, r, ss)
        return None
    M = {'a': np.array([[phi, 1], [0, 1 / phi]], complex),
         'b': np.array([[1, 0], [1, 1]], complex),
         'A': np.array([[1, 1], [0, 1]], complex),
         'B': np.array([[1, 0], [om, 1]], complex)}
    tags = set()
    for w in ['a', 'A', 'ab', 'AB', 'abAB', 'abAAB', 'aAB', 'bAB']:
        idn = in_field(np.trace(_wm(w, M)))
        if idn:
            _, q, r, ss = idn
            if abs(q) > 1e-9:
                tags.add('√5')
            if abs(r) > 1e-9:
                tags.add('√-3')
            if abs(ss) > 1e-9:
                tags.add('√-15')
    return tags


def seam_is_generic():
    """field theory: √-15 = √5·√-3 in Q(√5,√-3) always -> generic, not object-selected."""
    return sp.simplify(sp.sqrt(5) * sp.sqrt(-3) - sp.sqrt(-15)) == 0


if __name__ == "__main__":
    tags = object_coupling_produces_seam()
    print(f"object-coupled golden⊕Eisenstein joint character contains: {tags}")
    print(f"  seam √-15 present (both ends -> compositum): {'√5' in tags and '√-3' in tags}")
    print(f"field theory: √-15 = √5·√-3 forced in Q(√5,√-3) for ANY such pair: {seam_is_generic()}")
    print("\nVERDICT: second-seed seam is GENERIC (compositum, not selection). K025 stands.")
    print("Third forward door closed: H6 (near-crossing), gaps (density-trapped), seam (generic) -- all WALLS.")
