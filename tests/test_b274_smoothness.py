"""B274 locks -- rho_prin is a smooth point of the E6 character variety of the figure-eight (all orders): the
boundary/cusp MFP criterion holds (certs {6,6,12} + regular meridian) AND the cubic 3rd-order obstruction vanishes
identically (exact mod 99991 & 100003). Upgrades B273's 2nd-order to unconditional existence. FIREWALLED; nothing to
CLAIMS.md. (Heavy computation reproduced by sage-python b274_smoothness_modp.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B274_all_orders_smoothness" / "b274_smoothness.py"
_spec = importlib.util.spec_from_file_location("b274", _PATH)
b274 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b274)


def test_smooth_point_unconditionally():
    assert b274.smooth_point_unconditionally()


def test_boundary_mfp_criterion():
    assert b274.boundary_criterion_holds()
    for p in b274.PRIMES:
        r = b274.RESULT[p]
        assert r["H1M"] == 6 and r["H2M"] == 6          # dim H1(M)=dim H2(M)=6
        assert r["merid_regular"] == 6                   # meridian regular = rank E6
        assert r["H1_boundary"] == 2 * r["merid_regular"]  # dim H1(dM)=12=2*rank


def test_cubic_obstruction_vanishes_non_vacuously():
    assert b274.cubic_obstruction_vanishes()
    for p in b274.PRIMES:
        # non-vacuous: eta kills eps^2, q3 is a nonzero cochain that is nonetheless a coboundary
        assert b274.RESULT[p]["generic_o2_zero"] and b274.RESULT[p]["generic_q3_nonzero"]
        assert all(b274.RESULT[p][f"cubic_exp{m}"] for m in b274.EXPONENTS)
