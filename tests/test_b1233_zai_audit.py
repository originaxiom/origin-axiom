"""B1233 -- the external audit. Locks the REFUTATIONS especially: if a later seat resurrects
'j(m004's cusp) = 0' or 'the observer bit is the class group', the suite reds."""
import json, pathlib, subprocess, sys
import mpmath as mp
import pytest
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1233_zai_audit"
mp.mp.dps = 30


def test_the_golden_dilogarithm_partition():
    # precision is set INSIDE the test: a module-level mp.mp.dps is global state that another
    # test module can (and does) reset at import, which silently drops this to double precision.
    with mp.workdps(40):
        phi = (1 + mp.sqrt(5)) / 2
        L = lambda x: mp.polylog(2, x) + mp.log(x) * mp.log(1 - x) / 2
        tol = mp.mpf(10)**-30
        assert abs(L(1/phi) - mp.pi**2/10) < tol
        assert abs(L(1/phi**2) - mp.pi**2/15) < tol
        assert abs(L(1/phi) + L(1/phi**2) - mp.zeta(2)) < tol


def test_j_of_m004_cusp_is_NOT_zero_and_m003_is():
    """R1: the refutation. j = 0 belongs to the SISTER, not the object."""
    with mp.workdps(30):
        assert abs(mp.kleinj(mp.mpc(0, 2*mp.sqrt(3)))*1728) > 1e6        # m004: ~2.8e9
        assert abs(mp.kleinj(mp.mpc(0.5, mp.sqrt(3)/2))*1728) < 1e-20    # m003 = rho: 0


def test_disc15_j_values_are_quadratic_not_quartic():
    """R4: sum and product are rational integers => degree 2 over Q."""
    mp.mp.dps = 30
    r = [mp.kleinj((mp.mpc(-b, mp.sqrt(15)))/(2*a))*1728 for a, b, c in [(1, 1, 4), (2, 1, 2)]]
    assert abs(mp.re(r[0] + r[1]) + 191025) < 1e-6
    assert abs(mp.re(r[0]*r[1]) + 121287375) < 1e-3
    assert mp.re(r[0]*r[1]) < 0, "R5: the constant term is NEGATIVE"


def test_class_bit_is_not_our_c():
    """R7: in V4 = Gal(Q(sqrt-3,sqrt5)/Q), complex conjugation fixes sqrt5 (REAL) and flips
    sqrt-3; the class generator fixes sqrt-15 = sqrt-3*sqrt5 so flips BOTH. Different."""
    conj = (-1, +1)
    class_gen = (-1, -1)
    assert conj != class_gen
    assert conj[0]*conj[1] == -1 and class_gen[0]*class_gen[1] == +1   # action on sqrt-15


def test_the_void_is_a_2_1_saddle_and_origin_is_the_minimum():
    import sympy as sp
    x, y, z = sp.symbols('x y z')
    K = x**2 + y**2 + z**2 - x*y*z - 4
    H = sp.hessian(K, (x, y, z))
    assert sorted(sp.Matrix(H.subs({x: 2, y: 2, z: 2})).eigenvals()) == [-2, 4]
    assert K.subs({x: 2, y: 2, z: 2}) == 0
    assert K.subs({x: 0, y: 0, z: 0}) == -4
    assert list(sp.Matrix(H.subs({x: 0, y: 0, z: 0})).eigenvals()) == [2]


def test_two_is_inert_in_both_ends_and_splits_in_the_meeting():
    assert (-3) % 8 == 5 and 5 % 8 == 5      # inert
    assert (-15) % 8 == 1                     # splits


def test_the_kappa_convention_split_is_recorded():
    """The one real defect they found in OUR record. Until harmonized, it must stay named."""
    c = json.loads((ARC/"arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert "KAPPA CONVENTION SPLIT" in c and "HARMONIZATION OWED" in c


def test_audit_script_reproduces():
    r = subprocess.run([sys.executable, str(ARC/"audit.py")], capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL AUDIT ASSERTIONS HOLD" in r.stdout
