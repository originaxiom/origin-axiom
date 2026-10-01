"""B1433 lock -- the signature dichotomy holds on the axes and the two pure planes, not on the torus.

C29 said "zero generic-complex on C". These assertions pin what is true: the four axes and the two pure sums have no
generic-complex eigenvalue, and every direction mixing a split charge with a compact one has 48. The live test
recomputes the spectra from the exact matrices; the recorded test pins the exact (Sturm) classification.
"""
import json
import pathlib
from fractions import Fraction

import numpy as np
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1433_the_signature_dichotomy_holds_on_the_axes" / "verification"
AX = [8, 14, 16, 22]


def _mats():
    d = json.loads((V / "ad_matrices.json").read_text())
    return {n: np.array([[float(Fraction(x)) for x in row] for row in d[str(n)]]) for n in AX}


def _type(A, tol=1e-6):
    ev = np.linalg.eigvals(A)
    z = sum(abs(e) < tol for e in ev)
    re = sum(abs(e.imag) < tol <= abs(e.real) for e in ev)
    im = sum(abs(e.real) < tol <= abs(e.imag) for e in ev)
    return int(z), int(re), int(im), int(len(ev) - z - re - im)


def test_the_axes_are_as_b898_found():
    M = _mats()
    assert _type(M[8]) == _type(M[16]) == (30, 48, 0, 0)
    assert _type(M[14]) == _type(M[22]) == (12, 0, 66, 0)


def test_the_two_pure_planes_keep_their_type():
    M = _mats()
    assert _type(M[8] + M[16]) == (30, 48, 0, 0)
    assert _type(M[14] + M[22]) == (12, 0, 66, 0)


@pytest.mark.parametrize("a,b", [(8, 14), (8, 22), (16, 14), (16, 22)])
def test_every_split_plus_compact_direction_has_48_generic_complex(a, b):
    """the clause C29 got wrong: a mixed direction is neither split nor compact"""
    M = _mats()
    assert _type(M[a] + M[b]) == (12, 0, 18, 48)
    assert _type(M[a] + 2 * M[b]) == (12, 0, 18, 48)


def test_the_margin_is_not_a_tolerance_artefact():
    """bite: the 48 mixed eigenvalues have real AND imaginary parts far from zero"""
    M = _mats()
    ev = np.linalg.eigvals(M[8] + M[14])
    mixed = [e for e in ev if abs(e.real) > 1e-6 and abs(e.imag) > 1e-6]
    assert len(mixed) == 48
    assert min(abs(e.real) for e in mixed) > 1e-2 and min(abs(e.imag) for e in mixed) > 1e-2


def test_the_exact_classification_is_recorded_and_consistent():
    d = json.loads((V / "mixed_directions.json").read_text())
    for name in ("x8+x14", "x8+x22", "x14+x16", "x16+x22", "x8+2*x14", "2*x8+3*x14+5*x16+7*x22"):
        r = d["mixed_exact"][name]
        assert (r["zero"], r["real"], r["imaginary"], r["generic_complex"]) == (12, 0, 18, 48), name
        assert sum(f.get("degree", 1) * f["mult"] for f in r["factors"]) == 78
    for name, want in (("x8+x16", (30, 48, 0, 0)), ("x14+x22", (12, 0, 66, 0))):
        r = d["mixed_exact"][name]
        assert (r["zero"], r["real"], r["imaginary"], r["generic_complex"]) == want, name


def test_no_joint_centraliser_has_dimension_14():
    d = json.loads((V / "joint_centralizers.json").read_text())
    assert d["z(x8)"] == d["z(x16)"] == d["z(x8,x16)"] == 30
    assert set(v for k, v in d.items() if k not in ("z(x8)", "z(x16)", "z(x8,x16)")) == {12}
    assert 14 not in d.values()
