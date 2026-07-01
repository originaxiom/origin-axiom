"""B321 lock -- adjudication of the cross-chat self-realizability / seam-geometry arc. VERIFIED: |cusp shape|^2 = 12 =
h(E6) (SnapPy cusp = 2 sqrt3 i; both Q(sqrt-3)) -- a real certificate (basis-dependent, firewalled). REFUTED splices:
'CP phase pi/6 = core length of (6,3)' ((6,3) non-primitive gcd 3; core/3 is trivial Q(3z)=9Q(z) scaling; angle !=
length) and 'democratic rank-1 forced by Z/3' (contradicts B320: Z/3->circulant rank 3, rank-1 needs S3). REFRAME:
self-realizability = B285/B318 (CP sign=chirality) + B313 (scale k=3); the flow-selection version correctly killed
(sigma orientation-preserving). RESIDUE: the sharpened relational commensurator-Z/3 generation gate (refutation
condition) -> OPEN_PROBLEMS. Firewalled; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B321_seam_geometry_adjudication" / "seam_geometry_adjudication.py"
_spec = importlib.util.spec_from_file_location("b321", _PATH)
b321 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b321)


def test_verified_cusp_norm_is_he6():
    assert b321.cusp_norm() == 12 and b321.h_e6() == 12            # |2 sqrt3 i|^2 = h(E6), SnapPy-confirmed
    assert b321.CUSP_NORM_IS_HE6 and b321.CUSP_NORM_IS_BASIS_DEPENDENT


def test_cp_phase_core_length_is_splice():
    assert not b321.is_primitive(6, 3)                             # gcd(6,3)=3, non-primitive
    assert b321.q_scaling_is_trivial()                            # Q(6,3)=9 Q(2,1), trivial scaling
    assert b321.CP_PHASE_EQ_CORE_LENGTH_IS_SPLICE


def test_democratic_rank1_contradicts_b320():
    assert b321.DEMOCRATIC_RANK1_FROM_Z3_CONTRADICTS_B320          # Z/3 -> circulant rank 3; rank-1 needs S3


def test_reframe_and_residue():
    assert b321.SELF_REALIZABILITY_IS_REFRAME_OF_BANKED           # B285/B318 + B313
    assert b321.FLOW_SELECTION_SPLICE_CORRECTLY_KILLED           # sigma orientation-preserving
    assert b321.SHARPENED_MULTIPLICITY_GATE_IS_THE_RESIDUE       # relational commensurator-Z/3 -> OPEN_PROBLEMS
    assert b321.DERIVES_SM_VALUES is False
    assert b321.verdict()
