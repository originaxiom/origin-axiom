"""B1507 -- the deck on the closed tower, read against B502/B521's Gate C (July) and B350 (iv): own code.

H_1(Y_n) = coker(phi^n - 1) for the fibre monodromy phi = [[2,1],[1,1]] (B1303), and the deck acts as phi.
  (1) det(phi - 1) = -1 = Delta(1): phi - 1 is invertible over Z, so the deck fixes no non-zero class on any Y_n (B350 (iv); its
      tier note: Delta(1) = +-1 for every knot, so this is generic to knots, not special to the object).
  (2) Y_3: H_1 = (Z/4)^2, phi^2 + phi + 1 = 0 there (the deck is the scalar omega: Gate C's 'scalar omega within one Eisenstein
      module'); Gate C's det(T - 1) = Phi_3(1) = 3 for the companion T of x^2 + x + 1 is -1 mod 4, the same unit.
  (3) Orbit sizes of the deck on H_1(Y_n) (the dual action on characters has the same ones): Y_3 gives 1 + 5 x 3, B1506's loci
      orbits [1,3,3,3,3,3]; and (omega - 1) v has the order of v, B1506's 'the three blocks differ by characters of the same order'.
  (4) The Klein 2-torsion of H_1(Y_3) is 3-cycled with no fixed element (B343's step 2: Phi_3 irreducible mod 2)."""
from sympy import Matrix, Poly, symbols
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy import ZZ
from collections import Counter

PHI = Matrix([[2, 1], [1, 1]])


def _reducer(n):
    A = PHI**n - Matrix.eye(2)
    H = hermite_normal_form(A)
    a, b, c = int(H[0, 0]), int(H[0, 1]), int(H[1, 1])
    assert H[1, 0] == 0

    def red(v):
        x, y = int(v[0]), int(v[1])
        k = y // c
        y -= k * c; x -= k * b
        return (x % a, y)
    elems = sorted({red((x, y)) for x in range(a) for y in range(c)})
    assert len(elems) == abs(A.det())
    return A, red, elems


def tower(n):
    A, red, elems = _reducer(n)
    act = lambda v: red(tuple(PHI * Matrix(v)))
    seen, sizes = set(), Counter()
    for v in elems:
        if v in seen:
            continue
        orb, w = [v], act(v)
        while w != v:
            orb.append(w); w = act(w)
        seen |= set(orb); sizes[len(orb)] += 1
    S = smith_normal_form(A, domain=ZZ)
    return dict(n=n, smith=sorted(abs(int(S[i, i])) for i in range(2)), order=len(elems),
                fixed=sum(1 for v in elems if act(v) == v), orbit_sizes=dict(sorted(sizes.items())))


def y3_details():
    A, red, elems = _reducer(3)
    kills = all(red(tuple((PHI**2 + PHI + Matrix.eye(2)) * Matrix(v))) == (0, 0) for v in elems)

    def order(v):
        k, w = 1, v
        while w != (0, 0):
            k += 1; w = red((w[0] + v[0], w[1] + v[1]))
        return k
    same_order = all(order(v) == order(red(tuple((PHI - Matrix.eye(2)) * Matrix(v)))) for v in elems)
    T = Matrix([[0, -1], [1, -1]])
    klein = [v for v in elems if red((2 * v[0], 2 * v[1])) == (0, 0)]
    act = {v: red(tuple(PHI * Matrix(v))) for v in klein}
    t = symbols('t')
    return dict(det_phi_minus_1=int((PHI - Matrix.eye(2)).det()), omega_scalar=kills, gate_c_det=int((T - Matrix.eye(2)).det()),
                gate_c_det_mod4=int((T - Matrix.eye(2)).det()) % 4, unit_mod4=int((PHI - Matrix.eye(2)).det()) % 4,
                difference_same_order=same_order, klein=klein, klein_action=act,
                klein_fixed=[v for v in klein if v != (0, 0) and act[v] == v],
                phi3_irreducible_mod2=Poly(t**2 + t + 1, t, modulus=2).is_irreducible,
                delta_is_phi3_mod4=Poly(t**2 - 3 * t + 1 - (t**2 + t + 1), t).trunc(4).is_zero)


if __name__ == "__main__":
    for n in (2, 3, 4, 5, 6):
        print("tower", tower(n))
    for k, v in y3_details().items():
        print("Y3", k, "=", v)
