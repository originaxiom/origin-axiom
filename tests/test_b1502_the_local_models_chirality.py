"""B1502 lock -- THE LOCAL MODELS' CHIRALITY.

B1501's two torus models force no chirality at a cusp point.  Whenever a finite quotient of the cones over the four homogeneous
nearly Kaehler 6-manifolds has a torus-linked ADE locus, the link has H^2 = H^4 = 0 rationally (no C-field U(1), no rational flux) and the
torus is null-homologous; S3 x S3's model is a Dehn filling along a shortest vector (an A2 root) in each of its three Bryant-Salamon
phases; the flag manifold's model has no equivariant phase (R_P permutes the three U(2) containing T)."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1502_the_local_models_chirality" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1502_local_models", VER / "local_models_chirality.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_recorded_run():
    r = json.load(open(VER / "local_models_chirality.json"))
    assert r["all checks pass"] and r["no C-field U(1) and no rational flux at the apex"]
    c = r["cohomology"]
    assert c["S3xS3"]["Betti"] == [1, 0, 0, 2, 0, 0, 1] and c["F12"]["Betti"] == [1, 0, 2, 0, 2, 0, 1]
    for o in ("R_P", "R_P^2"):
        for k in ("2", "4"):
            assert c["F12"]["outer"][o][k]["trace"] == -1.0 and c["F12"]["outer"][o][k]["invariants"] == 0
    assert c["S3xS3"]["outer"]["sigma"]["3"]["trace"] == -1.0                 # L(sigma) = 3, as in B1501
    assert [x["collapsing circle (q-vector)"] for x in r["M1 collapsing circles"]] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert all(x["shortest"] for x in r["M1 collapsing circles"])
    assert all(x["tangent dimension"] == 3 and x["fixed seeds"] >= 190 for x in r["M1 phases"])
    assert r["M2 phases"]["R_P"]["preserved"] == [] and r["M2 phases"]["R_P^2"]["preserved"] == []
    s = r["frame sectors at a cone point"]                                     # doublets acyclic on the cusp torus: no choice
    assert s["spin 1/2 link cohomology (all z sampled)"] == [[0, 0, 0]] and s["spin 0 link cohomology at z = 1"] == [1, 2, 1]


def test_the_doublets_are_acyclic_on_the_cusp_torus():
    import numpy as np
    M = _load()
    Ua = np.array([[1, 1], [0, 1]], dtype=complex)
    Ul = -np.array([[1, 2 * np.sqrt(3) * 1j], [0, 1]], dtype=complex)
    for z in (1.0, -1.0, 0.5 + 0.5j, np.exp(2j)):
        assert M.torus_cohomology(z * Ua, Ul) == [0, 0, 0]
    assert M.torus_cohomology(np.eye(1, dtype=complex), np.eye(1, dtype=complex)) == [1, 2, 1]


def test_the_flag_manifold_cohomology_and_the_three_u2():
    M = _load()
    T = M.T
    link = T.F12()
    betti, harm, d2 = M.relative_cohomology(link)
    assert betti == [1, 0, 2, 0, 2, 0, 1] and d2 < 1e-12
    for o in link.outer.values():
        A = M.outer_on_m(link, o)
        for k in (2, 4):
            a = M.action_on_cohomology(harm, A, k)
            assert a["invariants"] == 0 and abs(a["trace"] + 1) < 1e-9          # the reflection representation's 3-cycle
    ph = M.m2_phases()
    assert ph["R_P"]["preserved"] == [] and len(ph["transposition (12), excluded"]["preserved"]) == 1
    assert M.torus_fixed_points_on_f12()["worst |t.p - p| over the torus"] < 1e-12


def test_m1_fills_along_a_root():
    import numpy as np
    M = _load()
    r = M.m1_phase(3, np.pi / 5, np.random.default_rng(3), seeds=40)
    assert r["fixed seeds"] >= 35 and r["largest off-diagonal part"] < 1e-9 and r["tangent dimension"] == 3
    c = M.m1_collapsing_circle(2)
    assert c["collapsing circle (q-vector)"] == [0, 1, 0] and c["shortest"]
    ot = M.m1_orbit_types()
    assert ot["principal stabiliser dim (orbit dim 9 - s)"] == 3 and ot["zero-section stabiliser dim"] == 6
