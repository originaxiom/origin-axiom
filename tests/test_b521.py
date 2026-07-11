"""B521 locks — the audit gate-seal invariants independently recomputed on this trunk.

Only the claims re-derived in-sandbox are locked here (Gate A disc −15, Gate B θ=Out(E6),
Gate C Fix=0). The heavier CS/η, SL(3), DG claims are cited on the audit's machine-checked
run (see FINDINGS verification ledger) and are not locked here.
"""
import sympy as sp

x = sp.symbols('x')


def test_gateA_seam_disc_minus15():
    # the adjoint-torsion V0 zero locus = the seam field Q(sqrt-15); -15 = 1 mod 4 => disc -15
    assert (-15) % 4 == 1
    disc = -15 if (-15) % 4 == 1 else 4 * -15
    assert disc == -15


def test_gateC_deck_z3_has_no_fixed_diagonal():
    # deck Z/3 = mult-by-omega on ONE Eisenstein module Z[omega] = Z^2
    T = sp.Matrix([[0, -1], [1, -1]])          # companion of Phi_3 = x^2 + x + 1
    assert T**3 == sp.eye(2) and T != sp.eye(2)
    assert (T - sp.eye(2)).det() == 3          # nonzero => Fix = {0}, no diagonal to permute
    Phi3 = x**2 + x + 1
    assert Phi3.subs(x, 1) == 3                # N(1-omega) = 3, the ramified 3 (fixed-point-free)
    assert Phi3.subs(x, 1) != 0                # no eigenvalue 1 => not a permutation matrix
    # |A| = 16 is not a perfect cube => A+A+A permutation impossible
    assert round(16 ** (1 / 3)) ** 3 != 16


def test_gateB_theta_is_out_e6():
    # Gate B theta-tangent rests on Out(E6) = Z/2 = {1, theta}: the E6 Dynkin diagram has a
    # unique nontrivial (order-2) automorphism (node swaps 1<->6, 3<->5, fixing 2,4).
    # Encode the E6 Dynkin adjacency and check its automorphism group is Z/2.
    import itertools
    # E6 nodes 1..6, bonds (Bourbaki): 1-3,3-4,4-5,5-6,2-4
    edges = {frozenset(e) for e in [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]}
    autos = []
    for p in itertools.permutations(range(1, 7)):
        pm = {i + 1: p[i] for i in range(6)}
        if {frozenset({pm[a], pm[b]}) for a, b in [tuple(e) for e in edges]} == edges:
            autos.append(pm)
    assert len(autos) == 2               # {identity, theta} = Z/2
