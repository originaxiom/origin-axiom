"""B197 -- figure-eight volume-tie broken by torsion-freeness (V189). Fast locks.

P10's unresolved m003 volume-tie is broken by torsion-freeness: m003 has Z/5 torsion (not b++), so among
torsion-free bundles the figure-eight is the UNIQUE volume minimum -- a sharpening of P10's volume filter
(NOT an independent proof; trace-3 stays the sole proof). Combinatorial min re-derived without SnapPy.
Full version (incl. SnapPy volume enumeration + chiral CS) in volume_selection.py.
"""
import numpy as np, itertools
import pytest


def _mat(w):
    L = np.array([[1, 1], [0, 1]]); R = np.array([[1, 0], [1, 1]])
    M = np.eye(2, dtype=object)
    for c in w: M = M @ (L if c == "L" else R)
    return M
def _necklaces(maxlen):
    seen, out = set(), []
    for n in range(2, maxlen + 1):
        for w in itertools.product("LR", repeat=n):
            s = "".join(w)
            if "L" in s and "R" in s:
                c = min(s[i:] + s[:i] for i in range(len(s)))
                if c == s and c not in seen: seen.add(c); out.append(s)
    return out


def test_combinatorial_min_is_LR():
    ws = _necklaces(12)
    tr = {w: int(_mat(w).trace()) for w in ws}
    assert [w for w in ws if tr[w] == min(tr.values())] == ["LR"]   # unique min trace
    assert [w for w in ws if len(w) == 2] == ["LR"]                  # unique shortest
    assert [int(_mat("R"*m + "L"*m).trace()) for m in range(1, 5)] == [3, 6, 11, 18]  # metallic m^2+2


def test_volume_tie_broken_by_torsion_free():
    snappy = pytest.importorskip("snappy")
    # figure-eight unique volume min among b++ (small length for speed), m003 the cross-family torsion tie
    vols = sorted((float(snappy.Manifold("b++"+w).volume()), w) for w in _necklaces(8))
    assert [w for v, w in vols if abs(v - vols[0][0]) < 1e-6] == ["LR"]   # unique b++ min
    m3 = snappy.Manifold("m003")
    assert abs(float(m3.volume()) - vols[0][0]) < 1e-6                    # same volume (the tie)
    assert "Z/5" in str(m3.homology())                                   # ...but torsion -> excluded by torsion-free
    assert str(snappy.Manifold("b++LR").homology()) == "Z"               # figure-eight is torsion-free
