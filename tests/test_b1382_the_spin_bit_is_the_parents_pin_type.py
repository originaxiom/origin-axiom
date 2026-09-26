"""B1382 lock -- THE SPIN BIT IS THE PARENT'S PIN TYPE.  m004's two spin structures are the pullbacks of the Gieseking
manifold's Pin+ and Pin- structures, one each: B1141's lift (a -> +A, cusp traces (2,-2)) extends only into G_+ (Pin+),
the other (a -> -A, (-2,-2)) only into G_- (Pin-); only the square t^2 = a discriminates.  Exact over Q(w)."""
import importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1382_the_spin_bit_is_the_parents_pin_type" / "verification"
_spec = importlib.util.spec_from_file_location("b1382_pin", VER / "pin_types.py")
P = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(P)


def test_b1141_setup_reproduced_exactly():
    census = P.s1_holonomy()
    assert census[(1, 1)] == "+I" and census[(-1, -1)] == "+I" and census[(1, -1)] == "-I"
    W, d, mu = P.s2_intertwiner()
    assert d == P.ONE and mu == P.ONE                      # W conj(W) = +A with det W = 1 (B1141's W0)


def test_the_double_covers_are_pin_plus_and_pin_minus():
    covers = P.s3_the_double_covers()
    assert covers[1][0] == "Pin+" and covers[-1][0] == "Pin-"


def test_each_spin_lift_extends_as_exactly_one_pin_type():
    W, d, mu = P.s2_intertwiner()
    table, sign_mu = P.s4_table(W, mu)
    assert table[(1, 1)][0] and not table[(1, -1)][0]        # B1141's lift: Pin+ only
    assert table[(-1, -1)][0] and not table[(-1, 1)][0]      # the other lift: Pin- only
    assert all(parts[:3] == (True, True, True) for _, parts in table.values())


def test_topology_and_cusp_names():
    h1N, h1M, b2 = P.s5_topology()
    assert (h1N, h1M, b2) == ("Z", "Z", 0)
    word, names = P.s6_cusp_names()
    assert names[1] == (2, -2) and names[-1] == (-2, -2)
