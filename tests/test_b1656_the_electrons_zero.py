"""B1656 -- the electron's zero. The sealed instrument unchanged; the stored cells; live (numpy, independent of the
instrument): on W59's eighteen lines at omega, theta_1(9w) = 0 (the leptons' R_1), while the up and down twists 5w and w
are not lattice points (theta_1 != 0); the bite: the fictitious pair's 7w, and a line of order 7, lift."""
import hashlib, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1656_the_electrons_zero"


def _th1(z, tau, K=30):
    """theta_1 at z reduced modulo the lattice Z + Z tau (quasi-periodicity multiplies by a non-zero factor, so whether
    theta_1 vanishes is unchanged; the series is only accurate near the fundamental domain)"""
    y = z.imag/tau.imag; x = z.real - y*tau.real
    z = (x - round(x)) + (y - round(y))*tau
    q = np.exp(1j*np.pi*tau); n = np.arange(K)
    return 2*np.sum((-1)**n*q**((n+.5)**2)*np.sin((2*n+1)*np.pi*z))


def _lines():
    return [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]


def test_live_the_leptons_twist_is_a_lattice_point_and_the_quarks_are_not():
    w0 = np.exp(2j*np.pi/3)
    for p1, p2 in _lines():
        w = p1*w0 - p2
        assert abs(_th1(-9*w, w0)) < 1e-10                                  # the leptons: R_1 vanishes
        assert abs(_th1(5*w, w0)) > 1e-3 and abs(_th1(-w, w0)) > 1e-3        # up (5w) and down (-w) lifted
        assert abs(_th1(-7*w, w0)) > 1e-3                                   # the bite: the fictitious pair (-2, 5)
    # off omega R_1 still vanishes on these lines (9w is a lattice point at every tau; the SM seat's W89 read-out): the
    # leptons' lift there comes from the norms ceasing to be equal (E5(a)), which is in the stored cells, not here
    g = 0.13 + 1.07j; p1, p2 = _lines()[0]
    assert abs(_th1(-9*(p1*g - p2), g)) < 1e-10
    w7 = (1/7)*w0 - 2/7                                                     # the bite: a line of order 7, 9w not in the lattice
    assert abs(_th1(-9*w7, w0)) > 1e-3


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 27e7e7482")
    assert hashlib.sha256(open(A / "verification" / "the_electrons_zero.py", "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("c4cfc3c0")
    d = json.load(open(A / "verification" / "the_electrons_zero.json"))
    assert d["E0"]["void"] is False and d["E0"]["lines_exact_order_9"] is True
    for cell in ("E1", "E2", "E3", "E4", "E5", "E6"):
        assert d[cell]["holds"] is True, cell
    assert d["E4"]["lep_R1_rel_max"] < 1e-12 and d["E4"]["lep_D_rel_max"] < 1e-10
    assert sorted(round(x, 4) for x in d["E4"]["quark_D_values"]) == [1.0312, 2.4629, 2.7416]
    assert abs(d["E3"]["gap_minmax"][0] + 5.806896) < 1e-5 and d["E6"]["lift_law_rel_err_max"] < 0.02
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
