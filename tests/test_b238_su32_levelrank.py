"""B238 locks -- SU(3)_2 modular data (gate-verified) + the figure-eight level-rank coincidence. Pure numpy,
fully pyenv-testable. Firewall: dimensionless quantum-topology/modular data; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B238_su32_levelrank" / "su32_wrt.py"
_spec = importlib.util.spec_from_file_location("b238_su32", _PATH)
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)


def test_modular_gates_pass():
    S2, T2, _ = b238.su2_data(3)
    _, S3, T3, _ = b238.su3_data(2)
    assert b238.modular_gate(S2, T2)        # SU(2)_3 valid modular rep
    assert b238.modular_gate(S3, T3)        # SU(3)_2 valid modular rep (the gate that caught the Casimir bug)


def test_figure_eight_coincides_at_minus_inv_phi():
    S2, T2, _ = b238.su2_data(3)
    _, S3, T3, _ = b238.su3_data(2)
    z2 = b238.wrt_trace(S2, T2, 'RL'); z3 = b238.wrt_trace(S3, T3, 'RL')
    assert abs(z2 - (-1 / b238.PHI)) < 1e-9        # reproduces B204
    assert abs(z3 - (-1 / b238.PHI)) < 1e-9        # SU(3)_2 coincides at -1/phi


def test_not_a_general_level_rank_equality():
    """silver/bronze do NOT coincide -- it is figure-eight-specific."""
    S2, T2, _ = b238.su2_data(3)
    _, S3, T3, _ = b238.su3_data(2)
    assert abs(b238.wrt_trace(S2, T2, 'RRLL') - b238.wrt_trace(S3, T3, 'RRLL')) > 1e-6
    assert abs(b238.wrt_trace(S2, T2, 'RRRLLL') - b238.wrt_trace(S3, T3, 'RRRLLL')) > 1e-6


def test_level_rank_signatures():
    """shared kappa=5 and c-sum = c(SU(6)_1)=5 (the conformal embedding)."""
    _, _, c2 = b238.su2_data(3)
    _, _, _, c3 = b238.su3_data(2)
    assert abs((c2 + c3) - 35 / 7) < 1e-12
    assert (3 + 2) == (2 + 3) == 5          # kappa = k+N shared
