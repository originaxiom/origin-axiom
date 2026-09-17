"""B1336 lock -- the surviving gauge group: no flat connection of this kind leaves the SM algebra unbroken.

The paper's arena is built from the centraliser of the FINITE image 2T (abelian, dim 4). The geometric holonomy is
Zariski-dense in its SL(2), so its centraliser is that of the whole principal sl2 -- dim 0. Either way the
Standard-Model algebra (non-abelian, dim 12) is not what survives, which is why the SM algebra in this construction
arrives at the Wilson-line step on a closing and never from the geometric representation.

Runs the arc's own exact computation over Q (E6 Chevalley algebra, re-verified in the script before use)."""
import pathlib, re, subprocess, sys
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1336_the_surviving_gauge_group" / "verification" / "i26.py"


@pytest.fixture(scope="module")
def out():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0, r.stderr[-2000:]
    return r.stdout


def test_e6_and_principal_sl2_rebuilt(out):
    assert "e6 dimension 78  (78 expected)" in out
    assert "principal sl2 relations [h,e]=2e, [h,f]=-2f, [e,f]=h : True" in out


def test_geometric_holonomy_centralises_nothing(out):
    m = re.search(r"principal sl2 \(= the Zariski closure of a dense rho\(pi_1\)\)\s*: dim = (\d+)", out)
    assert m and int(m.group(1)) == 0


def test_finite_image_centraliser_is_abelian_of_dimension_four(out):
    m = re.search(r"2T, the FINITE McKay image \(B854, re-run above\)\s*: dim = (\d+), ABELIAN", out)
    assert m and int(m.group(1)) == 4


def test_positive_control_the_torus_alone_gives_rank_six(out):
    m = re.search(r"the principal torus h alone\s*: dim = (\d+)", out)
    assert m and int(m.group(1)) == 6          # the criterion can return something non-zero


def test_neither_is_the_standard_model_algebra(out):
    assert "principal sl2 (geometric holonomy)    : NO -- dim 0 != 12" in out
    assert "2T (finite quotient)                  : NO -- dim 4 != 12" in out
