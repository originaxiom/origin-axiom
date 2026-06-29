"""B284 lock -- the figure-eight's finite-image 2T representation: object-specific point, GENERIC local structure.
Verifies chat-1's claim 3 (kernel right, stronger form fails) and reinforces B282. FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_DIR = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B284_2T_component"
def _load(name):
    spec = importlib.util.spec_from_file_location(name, _DIR / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
_tc = _load("twoT_component")
_v = _load("verdict")


def test_2T_rep_exact_and_finite():
    tt = _tc.twoT_rep()
    assert _tc.relator_residual(tt) < 1e-10        # genuine representation of pi_1(4_1)
    assert _tc.image_order(tt) == 24               # image = binary tetrahedral 2T


def test_local_structure_is_generic():
    geo, tt = _tc.geometric_rep(), _tc.twoT_rep()
    assert _tc.dim_H1(geo) == 1                     # matches B264
    assert _tc.dim_H1(tt) == 1                      # 2T point has the SAME local deformation -> generic, not anomalous


def test_verdict_object_specific_but_local_generic():
    assert _v.verdict()
    assert _v.NET_CORRECTIONS_TO_ME == [1, 2] and _v.NET_CORRECTIONS_TO_CHAT1 == [3, 4]
