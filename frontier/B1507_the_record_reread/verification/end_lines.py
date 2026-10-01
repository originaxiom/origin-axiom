"""B1507 -- the audit lane's R60/R61 (2026-09-30) against this branch's B1504, own code.
(a) R60: 'a completion at a rotated hexagonal point must pick one of the three root lines' holds for the root-line orbit (B1502's
    smooth phases), not for every ideal line: on Z[omega] the order-3 rotation 3-cycles EVERY primitive line; the root lines are
    one orbit and (1, 3) is another.
(b) R61: complex rotation-invariant lines exist.  In an orthonormal frame of the link torus, with S the Hodge star on 1-forms
    (rotation by 90 degrees), the rotation's eigenline w = (1, -i) (S w = i w) is invariant under the rotations of order 3, 4 and 6,
    the data u = (w z, i conj(w) conj(z)) satisfy C u = u for C(a, b) = (S conj b, -S conj a), and the Hermitian current
    a^H b - b^H a vanishes on them.  The other eigenline passes with the phase -i, so the rotation chooses neither.  B1504's lattice
    lemma excludes REAL invariant lines only."""
import sympy as sp

RW = sp.Matrix([[0, -1], [1, -1]])          # multiplication by omega on Z[omega] in the basis (1, omega)


def _line(v):
    g = sp.gcd(v[0], v[1]); v = (v[0] // g, v[1] // g)
    return v if (v[0] > 0 or (v[0] == 0 and v[1] > 0)) else (-v[0], -v[1])


def orbit(v):
    out, w = [], sp.Matrix(v)
    for _ in range(3):
        out.append(_line((int(w[0]), int(w[1])))); w = RW * w
    return out


def lines():
    roots, other = orbit((1, 0)), orbit((1, 3))
    sample = [(1, 0), (0, 1), (1, 1), (1, 3), (2, 1), (1, -1), (3, 5)]
    return dict(root_orbit=roots, orbit_1_3=other, disjoint=not set(roots) & set(other),
                fixed_lines=[v for v in sample if orbit(v)[1] == _line(v)])


def complex_lines():
    S = sp.Matrix([[0, -1], [1, 0]])
    z = sp.symbols('z')
    out = {}
    for name, w, phase in (("w=(1,-i)", sp.Matrix([1, -sp.I]), sp.I), ("w=(1,i)", sp.Matrix([1, sp.I]), -sp.I)):
        inv = {}
        for k in (3, 4, 6):
            th = 2 * sp.pi / k
            R = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
            lam = sp.simplify((R * w)[0] / w[0])
            inv[k] = (R * w - lam * w).applyfunc(sp.simplify) == sp.zeros(2, 1)
        a = w * z; b = phase * w.conjugate() * sp.conjugate(z)
        Cu = ((S * b.conjugate() - a).applyfunc(sp.simplify) == sp.zeros(2, 1)) and \
             ((-S * a.conjugate() - b).applyfunc(sp.simplify) == sp.zeros(2, 1))
        cur = sp.simplify((a.H * b - b.H * a)[0])
        out[name] = dict(rotation_invariant=inv, C_invariant=Cu, current=str(cur))
    return out


if __name__ == "__main__":
    for k, v in lines().items():
        print("(a)", k, "=", v)
    for k, v in complex_lines().items():
        print("(b)", k, "=", v)
