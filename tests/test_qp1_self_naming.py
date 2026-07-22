"""QP-1 self-naming / quine test -- locks for the census sweep."""
import cmath
import math

import numpy as np


def _snappy():
    import snappy
    return snappy


def test_m004_volume():
    """m004 volume is 2.0298832128..."""
    snappy = _snappy()
    M = snappy.Manifold("m004")
    assert abs(float(M.volume()) - 2.029883212819307) < 1e-8


def test_m004_cusp_shape():
    """m004 cusp shape is 2*sqrt(3)*i."""
    snappy = _snappy()
    M = snappy.Manifold("m004")
    cs = complex(M.cusp_info()[0].shape)
    assert abs(cs - 2j * math.sqrt(3)) < 1e-8


def test_m003_same_volume():
    """m003 (sister) has the same volume as m004."""
    snappy = _snappy()
    v3 = float(snappy.Manifold("m003").volume())
    v4 = float(snappy.Manifold("m004").volume())
    assert abs(v3 - v4) < 1e-10


def test_m003_different_cusp():
    """m003 has a different cusp shape from m004."""
    snappy = _snappy()
    cs3 = complex(snappy.Manifold("m003").cusp_info()[0].shape)
    cs4 = complex(snappy.Manifold("m004").cusp_info()[0].shape)
    assert abs(cs3 - cs4) > 1.0


def test_m003_cusp_is_omega():
    """m003 cusp shape is omega = e^{i pi/3} (hexagonal lattice)."""
    snappy = _snappy()
    cs = complex(snappy.Manifold("m003").cusp_info()[0].shape)
    omega = cmath.exp(1j * cmath.pi / 3)
    assert abs(cs - omega) < 1e-8


def test_m004_shapes_eisenstein():
    """m004 tetrahedra shapes satisfy x^2 - x + 1 = 0 (disc = -3)."""
    snappy = _snappy()
    shapes = [complex(s) for s in snappy.Manifold("m004").tetrahedra_shapes("rect")]
    for z in shapes:
        assert abs(z ** 2 - z + 1) < 1e-10


def test_m003_shapes_eisenstein():
    """m003 tetrahedra shapes also satisfy x^2 - x + 1 = 0 (same trace field)."""
    snappy = _snappy()
    shapes = [complex(s) for s in snappy.Manifold("m003").tetrahedra_shapes("rect")]
    for z in shapes:
        assert abs(z ** 2 - z + 1) < 1e-10


def test_only_two_volume_matches():
    """At most 2 manifolds in the census share m004's volume."""
    snappy = _snappy()
    target = float(snappy.Manifold("m004").volume())
    count = 0
    for M in snappy.OrientableCuspedCensus:
        if M.num_cusps() == 1 and abs(float(M.volume()) - target) < 1e-6:
            count += 1
    assert count == 2


def test_commensurable_family_volumes():
    """Eisenstein manifolds m206, m207 have volume = 2 * vol(m004)."""
    snappy = _snappy()
    v4 = float(snappy.Manifold("m004").volume())
    for name in ["m206", "m207"]:
        M = snappy.Manifold(name)
        ratio = float(M.volume()) / v4
        assert abs(ratio - 2.0) < 1e-6, f"{name}: ratio = {ratio}"


def test_verdict_quine():
    """No 1-cusped census manifold matches m004 on (vol, cusp shape)."""
    snappy = _snappy()
    target_vol = float(snappy.Manifold("m004").volume())
    target_cs = complex(snappy.Manifold("m004").cusp_info()[0].shape)
    twins = []
    for M in snappy.OrientableCuspedCensus:
        if M.num_cusps() != 1:
            continue
        if abs(float(M.volume()) - target_vol) >= 1e-6:
            continue
        cs = complex(M.cusp_info()[0].shape)
        if abs(cs - target_cs) < 1e-6 and M.name() != "m004":
            twins.append(M.name())
    assert twins == [], f"Unexpected twins: {twins}"
