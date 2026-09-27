"""B1390 lock -- THE EISENSTEIN AXES (PROVED).

For M cusped with shape field K = Q(sqrt-3): every symmetry lies in PGL(2, K); an elliptic of order 3 or 6 there has both fixed points
in P^1(K), of order 4 neither; with integral traces no loxodromic fixes a point of P^1(K).  So in m004's commensurability class an
isometry of order 3 or 6 fixes only cusp-to-cusp arcs (one rotating no cusp acts freely: sL-7's clean target does not exist), order 4
only closed geodesics, and every other order above 2 acts freely.  The dichotomy is sharp: o10_143602 (tr(c^2) = -5/2, non-arithmetic)
has an order-3 isometry with a closed fixed geodesic.  13 of B1186's 112 are non-arithmetic: the family is not the class."""
import importlib.util
import json
import random
import warnings
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1390_the_eisenstein_axes" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1390_eisenstein_axes", VER / "eisenstein_axes.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_elliptic_axes_in_Q_sqrt_minus_3():
    EA = _load()
    K, S = EA.K, EA.S
    assert not EA.is_square_in_K(K(-1)) and EA.is_square_in_K(K(-3))
    rnd = random.Random(7)
    for _ in range(300):
        a, c, d = EA.rand_K(rnd), EA.rand_K(rnd), EA.rand_K(rnd)
        t = a + d
        if c.iszero() or t.iszero():
            continue
        for factor, k in ((Fr(1), 3), (Fr(1, 3), 6), (Fr(1, 2), 4)):
            b = (a * d - factor * (t * t)) / c                          # t^2 = det / factor: order k in PGL(2)
            det = a * d - b * c
            D = t * t - 4 * det
            if k == 4:
                assert not EA.is_square_in_K(D)                          # the axis never ends at a cusp point
                continue
            root = t * S if k == 3 else t * S / 3
            assert root * root == D
            for r in (root, -root):                                     # both fixed points K-rational
                z = (a - d + r) / (2 * c)
                assert (c * z * z + (d - a) * z - b).iszero()


def test_orders_3_and_6_fix_only_arcs_in_the_class():
    import snappy
    EA = _load()
    base = snappy.Manifold("o10_150725").covers(3)[4]
    cases = [("s960", snappy.Manifold("s960")), ("o10_150725", snappy.Manifold("o10_150725")),
             ("m202", snappy.Manifold("m202")), ("cube~3.162", base.covers(3)[162])]
    seen_free = seen_arcs = 0
    for name, M in cases:
        FS, rows, agree = EA.analyse(name, M)
        assert agree                                                    # ends = |det(A - I)| of SnapPy's cusp maps
        for (k, o, r) in rows:
            if o != 1 or k not in (3, 6):
                continue
            assert r["closed"] == 0 and not r["anomalies"]
            if not r["rotated"]:
                assert r["arcs"] == 0                                   # rotates no cusp -> acts freely
                seen_free += 1
            else:
                assert r["arcs"] > 0 and sum(r["ends"].values()) % 2 == 0   # B1371's pairing
                seen_arcs += 1
    assert seen_free >= 8 and seen_arcs >= 4


def test_the_dichotomy_is_sharp_and_the_controls_fire():
    import snappy
    EA = _load()
    w = EA.nonintegral_witness(snappy.ManifoldHP("o10_143602"))
    assert w is not None and w[0] == "c" and w[1] == Fr(-5, 2) and w[2] == 0      # tr(c^2) = -5/2: non-arithmetic
    assert EA.nonintegral_witness(snappy.ManifoldHP("o10_150725")) is None          # B1386's base: integral traces
    FS, rows, agree = EA.analyse("o10_143602", snappy.Manifold("o10_143602"))
    o3 = [r for (k, o, r) in rows if o == 1 and k == 3]
    assert len(o3) == 2 and all(r["closed"] == 1 and r["arcs"] == 3 for r in o3)
    FS, rows, agree = EA.analyse("L6a4", snappy.Manifold("L6a4"))                  # Borromean rings, Q(i)
    o3 = [r for (k, o, r) in rows if o == 1 and k == 3]
    assert agree and len(o3) == 8 and all(r["closed"] >= 1 and not r["rotated"] for r in o3)
    FS, rows, agree = EA.analyse("m004", snappy.Manifold("m004"))                  # order 2 is unconstrained
    assert sum(r["closed"] for (k, o, r) in rows if o == 1 and k == 2) == 1


def test_the_family_is_not_the_class():
    import snappy
    EA = _load()
    fam = json.load(open(ROOT / "frontier" / "B1186_family_is_112" / "verification" / "family_census.json"))
    nonarith = sorted(n for n in fam["members_B"] if EA.nonintegral_witness(snappy.ManifoldHP(n)))
    assert nonarith == sorted(["v2875", "t06828", "t06829", "t11365", "o9_41000", "o9_41003", "o9_41004", "o9_41005", "o9_41006",
                               "o9_41008", "o10_143600", "o10_143601", "o10_143602"])
    assert not set(nonarith) & set(fam["members_A"])                # every regular member is arithmetic
    for n in ("o10_150704", "o10_150725", "o10_150729", "s958", "v2873", "t12833", "t12835", "o10_150701"):
        assert n not in nonarith                                    # B1385/B1386's members and B1418's firing members
