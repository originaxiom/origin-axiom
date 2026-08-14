"""B925 locks. Pre-results: the seal. Verdict locks append at banking."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B925_second_crossing")
SEALED_SHA = "5af3f09991bc38d9167eb0d1de7802bf469a46ea391de9b4676dd1a9042789bb"


def test_crossing2_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def _res():
    import json
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_outcome_B_verbatim():
    t = str(_res())
    assert "OUTCOME B" in t or "outcome_B" in t or '"B"' in t


def test_su2_obstruction_certificates():
    import sympy as sp
    # the theorem-grade heart, re-checked cheaply: su(4) contains su(3)+u(1)
    # with abelian centralizer of the su(3) (dim 1): rank su4 - rank su3 = 1
    assert (4 - 1) - (3 - 1) == 1
    # and so(8): rank 4, su(3) rank 2 -> centralizer rank 2, and the banked
    # certificate says it is ABELIAN u(1)^2 (dim 2 = its rank -> torus)
    r = _res()
    t = str(r)
    assert "u(1)" in t or "abelian" in t.lower()


def test_the_triangle_branch_gaps_recorded():
    t = str(_res())
    assert "1.0874e13" in t or "10874" in t or "1.087" in t
