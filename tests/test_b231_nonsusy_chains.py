"""B231 locks -- H15: the non-SUSY metallic anyon chains. The headline is EXACT (the quantum-dimension
boundary lambda_m = d_{1/2} <=> m=1); plus a light ED determinism/validation check. Firewall: dimensionless
CFT data; nothing to CLAIMS.md."""
import importlib.util
import pathlib

import pytest

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B231_nonsusy_metallic_chains" / "nonsusy_chains.py"
_spec = importlib.util.spec_from_file_location("b231_nonsusy", _PATH)
b231 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b231)


def test_quantum_dimension_boundary_is_golden_only():
    """EXACT headline: lambda_m = d_{1/2} (a quantum dimension) and lambda_m<2 BOTH hold iff m=1."""
    tbl = b231.cft_table()
    assert tbl[0]["m"] == 1
    assert tbl[0]["lambda_is_qdim"] and tbl[0]["lambda_lt_2"]              # golden: yes
    assert all((not r["lambda_is_qdim"]) and (not r["lambda_lt_2"]) for r in tbl[1:])  # m>=2: no


def test_golden_dhalf_is_phi_and_metallic_means():
    """d_{1/2} at the golden level is exactly the golden ratio; metallic means exceed 2 for m>=2."""
    assert abs(b231.qdim(1, 3) - b231.PHI) < 1e-12        # 2cos(pi/5) = phi
    assert b231.metallic_mean(1) < 2 < b231.metallic_mean(2)
    assert abs(b231.metallic_mean(2) - (1 + 2 ** 0.5)) < 1e-12  # silver = 1+sqrt(2)


def test_exact_central_charges_at_metallic_levels():
    """the AFM/FM central charges at k=m^2+2 are the exact rationals (golden 7/10, silver 25/28 & 5/4)."""
    from fractions import Fraction as Fr
    tbl = {r["m"]: r for r in b231.cft_table()}
    assert tbl[1]["c_AFM"] == Fr(7, 10) and tbl[1]["c_FM"] == Fr(4, 5)     # golden
    assert tbl[2]["c_AFM"] == Fr(25, 28) and tbl[2]["c_FM"] == Fr(5, 4)    # silver


def test_ed_build_validates_on_tci():
    """the general su(2)_k ED reproduces a known CFT: k=3 AFM -> TCI c=7/10 (light size, deterministic)."""
    rows = b231.run_chain(3, sizes=(12, 14), sign=-1.0)
    c_large = rows[-1]["c"]
    assert 0.6 < c_large < 0.85   # TCI c=0.70, finite-size band at N=14
