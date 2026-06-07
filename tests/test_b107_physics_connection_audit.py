"""B107 -- locking tests for the two computational anchors of the physics-connection audit.
A: the metallic trace map IS the KKT/Fibonacci trace map (phi_1 = (z,x,xz-y); tr[A,B] conserved for all m).
B (the headline negative): every SL(3) tower eigenvalue is +-phi^k -- one golden scale.
NO physics is tested or claimed here; the eigenvalues/invariant are standard mathematics. The A-E
classification (FINDINGS.md) is the deliverable; physics stays POSTULATED/firewalled."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b107", _ROOT / "frontier" / "B107_physics_connection_audit" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


# --- A: the quasicrystal anchor ----------------------------------------------
def test_fibonacci_map_is_z_x_xz_minus_y():
    """phi_1 trace map == (z, x, xz - y) exactly (the B67 / standard Fibonacci trace map)."""
    assert B.fibonacci_map_matches_B67() is True


def test_suto_invariant_conserved_all_m():
    """tr[A,B] = x^2+y^2+z^2-xyz-2 is conserved under phi_m for m=1..4 (symbolic, deviation == 0)."""
    dev = B.invariant_is_conserved((1, 2, 3, 4))
    for m, d in dev.items():
        assert d == 0, f"m={m} deviation {d}"


# --- B: the headline negative (one golden scale) -----------------------------
def test_sl3_tower_eigenvalues_are_pm_phi_powers():
    """Every SL(3) m=1 tower eigenvalue is +-phi^k (k integer) -- a single geometric scale log phi."""
    r = B.tower_roots_are_golden(3)
    assert r["num_eigs"] == 8
    assert r["all_pm_phi_power"] is True
    assert r["k_values"] == [-3, -2, -1, 0, 1, 2, 3]


def test_sl3_tower_eigenvalues_equal_catalog_multiset():
    """The 8 eigenvalues are exactly the +-phi^k multiset {1,-1,phi^2,phi^-2,phi^3,-phi,phi^-1,-phi^-3}."""
    phi = (1 + sp.sqrt(5)) / 2
    expected = sorted([sp.simplify(e) for e in
                       [1, -1, phi**2, phi**-2, phi**3, -phi, phi**-1, -phi**-3]], key=lambda t: float(t))
    got = sorted([sp.simplify(e) for e in B.tower_eigenvalues(3)], key=lambda t: float(t))
    assert all(sp.simplify(a - b) == 0 for a, b in zip(expected, got))
