"""B119 -- locking test: the M^k-scalar (centrality) mechanism, a sharp negative on "prove k=n on the principal".
The principal cusp order = order(a), a+1/a=3-n = {4,3,2,inf} (n=3..6); M^k central iff order(a)|k, so k=n is
non-central where the principal exists (n=3,4) but NOT the unique non-central k => centrality does not force k=n;
and for n>=5 the principal does not exist irreducibly (B95). The secondary (2n-type): M^n=-I central => exponent
n-1 (B111). Emergent: no clean {n-1,n+1,2n} cusp-order law (B111 ADD2 conflated components). NO physics; P1-P16
untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b119", _ROOT / "frontier" / "B119_mk_scalar_mechanism" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_principal_cusp_order_sequence():
    pc = B.principal_cusp_order(6)
    assert pc[3]["order_a"] == 4 and pc[4]["order_a"] == 3 and pc[5]["order_a"] == 2   # 4,3,2
    assert pc[6]["is_root_of_unity"] is False and pc[6]["order_a"] is None              # n>=6 hyperbolic


def test_kn_not_forced_by_scalarness():
    mc = B.mpower_central_principal(5)
    assert mc[3]["kn_noncentral"] is True and mc[4]["kn_noncentral"] is True     # k=n non-central where exists
    assert mc[3]["kn_is_unique_noncentral"] is False                            # but NOT the unique non-central k
    assert mc[4]["kn_is_unique_noncentral"] is False                            # => scalar-ness does not force k=n


def test_brave_kn_verdict_is_sharp_negative():
    bv = B.brave_kn_verdict()
    assert bv["kn_forced_by_scalarness"] is False        # the brave proof does NOT close
    assert bv["n5_principal_A2_is_I"] is True             # B95 wall: n=5 degenerates
    assert bv["n6plus_principal_finite_order"] is False   # n>=6 no finite-order spectrum
    assert "n in {3,4}" in bv["verdict"]


def test_secondary_exponent_n_minus_1():
    se = B.secondary_exponent_arithmetic()
    assert se["Mn_central"] is True                  # M^n=-I central on the secondary
    assert se["central_iff_n_divides_k"] is True      # central iff n|k
    assert se["exponent_forced"] == se["n"] - 1       # => exponent n-1 (B111)


def test_emergent_no_clean_cusp_order_law():
    cc = B.cusp_order_correction()
    assert cc["principal_order_sequence_n3to6"] == [4, 3, 2, "inf"]
    assert cc["clean_nm1_np1_2n_law"] is False        # B111 ADD2 conflated three components
