#!/usr/bin/env python3
"""B799 — in-sandbox computation of the discriminating facts for the COMPUTED-class doors.

Prereg 3243c1c219ea7ca0. Each function computes the fact the prereg named for that door, and
nothing else. A fact adjacent to the discriminating one does not count (prereg §4).
"""
import sympy as sp


# --- Door B332 -----------------------------------------------------------------------------
# Prereg's discriminating fact: det(A - I) = -1 for the deck element, forcing hyperbolic,
# hence g = -R*L^-1 is NOT the generation-cycling deck element.
def door_b332():
    R = sp.Matrix([[1, 1], [0, 1]])
    L = sp.Matrix([[1, 0], [1, 1]])
    g = -(R * L.inv())
    A = sp.Matrix([[1, 1], [1, 0]])                      # the golden/Fibonacci monodromy
    x = sp.Symbol("x")

    out = {}
    out["g"] = g
    out["g_trace"] = sp.trace(g)
    out["g_det"] = g.det()
    out["g_charpoly"] = sp.factor(g.charpoly(x).as_expr())
    # order of g: smallest k with g^k = I
    k, M = 1, g
    while M != sp.eye(2) and k < 24:
        M = sp.simplify(M * g)
        k += 1
    out["g_order"] = k
    # g is ELLIPTIC: |tr| < 2  =>  eigenvalues on the unit circle, finite order
    out["g_is_elliptic"] = bool(abs(sp.trace(g)) < 2)
    out["g_eigenvals"] = g.eigenvals()

    # the deck/monodromy element of a hyperbolic once-punctured-torus bundle
    out["A_trace"] = sp.trace(A)
    out["A_det"] = A.det()
    out["det_A_minus_I"] = (A - sp.eye(2)).det()          # the prereg's named fact
    out["A_charpoly"] = sp.factor(A.charpoly(x).as_expr())
    ev = sorted([sp.nsimplify(e) for e in A.eigenvals()], key=lambda e: float(sp.Abs(e)))
    out["A_eigenvals"] = ev
    out["A_is_hyperbolic"] = bool(sp.Abs(ev[-1]) > 1 and all(sp.im(e) == 0 for e in ev))
    return out


# --- Door W7-rebase ------------------------------------------------------------------------
# Prereg's discriminating fact: the E6 centre acts on the 27 as the scalar omega, hence
# splits nothing (so no Z/3 triality gives a 3+2 generation split of H^1(D;27)).
#
# Mechanism, computed rather than cited: for a simply-connected group the centre is P/Q
# (weight lattice mod root lattice), and by Schur it acts on an irrep with highest weight
# lambda by the scalar given by lambda's class in P/Q. So the fact reduces to Smith normal
# form of the E6 Cartan matrix plus the class of the 27's highest weight.
def _e6_cartan():
    # Bourbaki E6 numbering: 1-3-4-5-6 chain, node 2 attached to node 4.
    edges = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]
    C = sp.zeros(6, 6)
    for i in range(1, 7):
        C[i - 1, i - 1] = 2
    for a, b in edges:
        C[a - 1, b - 1] = -1
        C[b - 1, a - 1] = -1
    return C


def door_w7():
    C = _e6_cartan()
    out = {}
    out["cartan_det"] = C.det()                       # |P/Q| for E6
    # Smith normal form gives the abelian group structure of P/Q
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(sp.Matrix(C))
    divisors = [S[i, i] for i in range(6)]
    out["smith_divisors"] = divisors
    out["PQ_structure"] = [d for d in divisors if d not in (0, 1, -1)]
    # the 27 is the fundamental rep at node 1; its class in P/Q is the image of e_1
    # under Z^6 -> Z^6 / C Z^6.  Order of that class:
    order = None
    for k in range(1, 10):
        rhs = sp.Matrix([k, 0, 0, 0, 0, 0])
        sol = C.solve(rhs)
        if all(v.is_Integer for v in sol):
            order = k
            break
    out["order_of_27_class_in_PQ"] = order
    out["centre_acts_by_primitive_cube_root"] = (order == 3)
    # a scalar action has a single eigenvalue on the whole 27 => no invariant splitting
    out["scalar_so_splits_nothing"] = (order is not None and order > 1)
    return out


if __name__ == "__main__":
    print("=" * 78)
    print("DOOR B332 — is g = -R L^-1 the generation-cycling deck element?")
    b = door_b332()
    print(f"  g            = {b['g'].tolist()}")
    print(f"  tr g         = {b['g_trace']}   det g = {b['g_det']}")
    print(f"  charpoly(g)  = {b['g_charpoly']}")
    print(f"  order(g)     = {b['g_order']}      elliptic (|tr|<2): {b['g_is_elliptic']}")
    print(f"  eigenvals(g) = {b['g_eigenvals']}")
    print(f"  --- the deck element of a hyperbolic bundle ---")
    print(f"  A            = [[1,1],[1,0]]   tr = {b['A_trace']}  det = {b['A_det']}")
    print(f"  det(A - I)   = {b['det_A_minus_I']}          <-- the prereg's named fact")
    print(f"  charpoly(A)  = {b['A_charpoly']}")
    print(f"  eigenvals(A) = {b['A_eigenvals']}")
    print(f"  A hyperbolic = {b['A_is_hyperbolic']}")
    print(f"  => g has finite order {b['g_order']} (elliptic); the deck element is hyperbolic.")
    print(f"     An elliptic element of finite order CANNOT be the monodromy of a hyperbolic")
    print(f"     mapping torus, so g is not the generation-cycling deck element.")

    print("=" * 78)
    print("DOOR W7-rebase — does the E6 centre split the 27?")
    w = door_w7()
    print(f"  det Cartan(E6)          = {w['cartan_det']}   (= |P/Q| = |Z(E6)|)")
    print(f"  Smith divisors          = {w['smith_divisors']}")
    print(f"  P/Q structure           = Z/{w['PQ_structure']}")
    print(f"  order of 27's class     = {w['order_of_27_class_in_PQ']}")
    print(f"  centre acts by omega    = {w['centre_acts_by_primitive_cube_root']}")
    print(f"  => the centre acts on the 27 by a single primitive cube root of unity.")
    print(f"     A scalar has one eigenvalue on the whole 27: it SPLITS NOTHING,")
    print(f"     so no 3+2 generation split can come from the naive Z/3 triality.")
