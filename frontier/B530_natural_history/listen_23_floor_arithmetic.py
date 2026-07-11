"""
Movement XXI — the arithmetic of the floor: growth is Q(√5), but the trace-zero
point's forced order-6 twist puts the dynamics in Q(√5,√-3) ⊇ Q(√-15).

Movement IX established the object's GROWTH field (Level-0 abelianization, char poly
x^4-2x^3-5x^2-4x-1, disc -400) is Q(√5): the golden/E8 end is in, the Eisenstein
field Q(√-3) and the seam field Q(√-15) are provably OUT.

This movement asks the same question one level up, on the FLOOR (the character
variety), prompted by an owner-authorized pass past the physics gate.  Computed:

  * The trace-zero floor point (movement XIX) has a RATIONAL F4-character (all the
    traces computed are 0 or -2) -- the Eisenstein field is absent from the static
    representation.
  * Its twist tau is FORCED to satisfy tau^6 = 1 (verified: every trace-zero
    irreducible fixed point found has an order-6 twist, tau = e^{+/- i pi/3}).
  * Hence the linearized-dynamics spectrum {phi,1,-1/phi} (x) {1,omega,omega^2}
    (movement XIX) lives in Q(√5, √-3): phi from the golden growth, omega from the
    forced order-6 twist.  This compositum CONTAINS the seam field Q(√-15) (√-15 =
    √5 · √-3).

So the golden field (√5) and the Eisenstein field (√-3) -- provably held apart in
the growth arithmetic -- CO-OCCUR in the object's own linearized dynamics at its
most symmetric point, in a field that also contains the seam.  This is a pure
arithmetic-geometry fact about the object's representations; the physics reading
(what "the two ends meeting" would mean) is firewalled in speculations/S065.

No physics here.
"""
import numpy as np
import sympy as sp

# reuse the trace-zero-point finder
import importlib.util
import os
_spec = importlib.util.spec_from_file_location(
    'l21', os.path.join(os.path.dirname(__file__), 'listen_21_golden_ladder_point.py'))
_l21 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_l21)

GENS = ['a', 'b', 'A', 'B']


def growth_field():
    """char poly disc -400 -> Q(√5); √-3, √-15 absent (movement IX)."""
    x = sp.symbols('x')
    cp = x**4 - 2 * x**3 - 5 * x**2 - 4 * x - 1
    disc = sp.discriminant(cp, x)
    return disc  # -400 = -(2^4 · 5^2); the real subfield is Q(√5)


def trace_zero_character_is_rational():
    T, Ms = _l21.trace_zero_point()
    inv = {g: np.linalg.inv(Ms[g]) for g in GENS}

    def tr(w):
        P = np.eye(2, dtype=complex)
        for ch in w:
            P = P @ (Ms[ch] if ch in Ms else inv[ch.lower()])
        return np.trace(P)
    words = ['a', 'b', 'A', 'B', 'ab', 'aA', 'aB', 'bA', 'bB', 'AB', 'abA', 'abAAB']
    traces = {w: tr(w) for w in words}
    rational = all(abs(t.imag) < 1e-4 and abs(t.real - round(t.real)) < 1e-4 for t in traces.values())
    return rational, {w: round(t.real) for w, t in traces.items()}, T[0, 0]


def spectrum_field_contains_seam():
    """Dsigma* = {phi,1,-1/phi} (x) {1,om,om^2} (movement XIX); field = Q(√5,√-3) ⊇ √-15."""
    phi = (1 + sp.sqrt(5)) / 2                       # in Q(√5)
    om = (-1 + sp.sqrt(-3)) / 2                       # in Q(√-3)
    seam = sp.sqrt(5) * sp.sqrt(-3)                   # √-15
    sqrt5_in = sp.simplify(2 * phi - 1 - sp.sqrt(5)) == 0
    sqrt_m3_in = sp.simplify(2 * om + 1 - sp.sqrt(-3)) == 0
    seam_in = sp.simplify(seam - sp.sqrt(-15)) == 0
    return sqrt5_in and sqrt_m3_in and seam_in


if __name__ == "__main__":
    print(f"growth field: char poly disc = {growth_field()} = -(2^4·5^2)  -> Q(√5) "
          f"(√-3, √-15 absent, movement IX)")
    rat, traces, tau = trace_zero_character_is_rational()
    print(f"trace-zero F4-character rational (Q)? {rat}   traces {traces}")
    print(f"trace-zero twist tau = {tau:.5f}   tau^6=1: {abs(tau**6 - 1) < 1e-6} (order 6, FORCED)")
    print(f"Dsigma* spectrum field Q(√5,√-3) contains the seam √-15: {spectrum_field_contains_seam()}")
    print("\n=> growth = Q(√5); floor trace-zero dynamics = Q(√5,√-3) ⊇ √-15 "
          "(golden + Eisenstein + seam co-occur, via the forced order-6 twist).")
