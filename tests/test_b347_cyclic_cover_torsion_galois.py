"""B347 lock -- gate A extension: the cyclic-cover (abelian) torsion class is a Galois orbit.

The n-fold cyclic cover torsion module is coker(A^n - I) (P8); the orders are the P8/C5
Lucas ladder; the Alexander factor multiset {Delta(zeta_n^j)} is Galois-closed with integer
symmetric functions; the deck action is fixed-point-free for every n (det(A-I) = Delta(1) =
-1, a unit -- an MB8 generic-knot mechanism, honestly tiered). No forced choice in this
class. CONDITIONAL per the C-guardrail; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
         / "B347_cyclic_cover_torsion_galois" / "cyclic_cover_torsion.py")
_spec = importlib.util.spec_from_file_location("b347", _PATH)
b347 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b347)


def test_torsion_orders_are_the_P8_C5_lucas_ladder():
    orders = b347.torsion_orders(8)
    assert orders == {2: (5, 5), 3: (16, 16), 4: (45, 45), 5: (121, 121),
                      6: (320, 320), 7: (841, 841), 8: (2205, 2205)}
    # and they are literally the P8 torsion orders from the proven core
    from origin_axiom.topology import torsion_order
    for n, (Tn, _) in orders.items():
        assert Tn == torsion_order(n)


def test_resultant_identity_exact():
    for n, (prod, det) in b347.resultant_identity(6).items():
        assert prod == det, f"n={n}"


def test_factor_multiset_is_a_symmetrizable_galois_orbit():
    for n in (3, 4, 5, 6):
        perm_ok, esf, esf_int = b347.factor_orbit_is_galois_closed(n)
        assert perm_ok, f"n={n}: Galois index permutation failed"
        assert esf_int, f"n={n}: symmetric functions not all integers: {esf}"


def test_torsion_groups_smith_normal_form():
    groups = b347.torsion_groups(6)
    assert groups[2] == (1, 5)          # Z/5
    assert groups[3] == (4, 4)          # (Z/4)^2 -- independently re-derives B326
    assert groups[4] == (3, 15)
    assert groups[5] == (11, 11)
    assert groups[6] == (8, 40)


def test_deck_action_fixed_point_free_uniformly():
    # nmax=5 in the lock (the n=6 brute-force count is ~100k lattice solves; the
    # probe's __main__ still runs it) -- the structural certificate (lattice
    # equality + det(A-I) unit) is what carries the uniform claim.
    unit, results = b347.deck_action_fixed_point_free(5)
    assert unit                                   # det(A - I) = -1
    for n, (lattice_eq, n_fixed) in results.items():
        assert lattice_eq, f"n={n}: N*Z^2 != im(A^n - I)"
        assert n_fixed == 1, f"n={n}: deck action has nonzero fixed classes"


def test_generic_tier_honesty():
    # Delta(1) = -1: the fixed-point-freeness mechanism is generic-knot (MB8), and the
    # probe must say so rather than claim object-specific forcing.
    assert b347.generic_tier_note() == -1
