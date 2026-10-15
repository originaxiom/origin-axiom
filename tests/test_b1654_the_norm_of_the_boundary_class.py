"""B1654 -- the norm of the boundary class.  Sealed instrument unchanged; the stored cells; live (fresh numpy code,
independent of the sealed instrument): D = int_P sum_r R_r^2 |S_r|^2 dA needs no cutoff, vanishes at omega and equals the
stored value at i; the bite -- with a non-isotropic triplet R' the same integral, cut at eps, grows like
2 pi (R'.R') log(1/eps), so it is Jacobi's R.R = 0 that removes the log."""
import hashlib, json, math, pathlib
import numpy as np
from numpy.polynomial.legendre import leggauss
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1654_the_norm_of_the_boundary_class"


def _th(z, tau, K=20):
    q = np.exp(1j*np.pi*tau); n = np.arange(K); m = np.arange(1, K); z = np.asarray(z, dtype=complex)[..., None]
    t1 = 2*np.sum((-1)**n*q**((n+.5)**2)*np.sin((2*n+1)*np.pi*z), -1)
    t2 = 2*np.sum(q**((n+.5)**2)*np.cos((2*n+1)*np.pi*z), -1)
    t3 = 1 + 2*np.sum(q**(m**2)*np.cos(2*m*np.pi*z), -1)
    t4 = 1 + 2*np.sum((-1)**m*q**(m**2)*np.cos(2*m*np.pi*z), -1)
    return t1, t2, t3, t4


def _setup(tau):
    q = np.exp(1j*np.pi*tau); n = np.arange(20); tp = 2*np.pi*np.sum((-1)**n*(2*n+1)*q**((n+.5)**2))
    t0 = _th(np.array(0.0), tau)
    S = lambda r, z: _th(z, tau)[r-1]*tp/(t0[r-1]*_th(z, tau)[0])
    R = {2: -t0[1]**2/tp, 4: -t0[3]**2/tp, 3: 1j*t0[2]**2/tp}                      # B1644's triplet; R.R = 0
    return S, R, t0, tp


def _polar(f, tau, r0=0.0, nth=40, nr=40):
    v = [0.5+0.5*tau, -0.5+0.5*tau, -0.5-0.5*tau, 0.5-0.5*tau]
    br = sorted(float(np.mod(np.angle(x), 2*np.pi)) for x in v); br += [br[0] + 2*np.pi]
    xg, wg = leggauss(nth); xr, wr = leggauss(nr); tot = 0j
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        d = np.exp(1j*th); y1 = d.imag/tau.imag; x1 = d.real - y1*tau.real; rm = 0.5/np.maximum(abs(x1), abs(y1))
        if r0 == 0.0:
            rr = 0.5*rm[:, None]*(xr[None, :] + 1); w2 = 0.5*rm[:, None]*wr[None, :]; jac = rr
        else:                                                                    # s = log r on [log r0, log rm]
            lo = math.log(r0); hi = np.log(rm); s = 0.5*(hi-lo)[:, None]*xr[None, :] + 0.5*(hi+lo)[:, None]
            w2 = 0.5*(hi-lo)[:, None]*wr[None, :]; rr = np.exp(s); jac = rr**2
        tot += np.sum(wt[:, None]*w2*f(rr*d[:, None])*jac)
    return tot


def _D(tau):
    S, R, _, _ = _setup(tau)
    return _polar(lambda z: sum(R[r]**2*np.abs(S(r, z))**2 for r in (2, 3, 4)), tau) / sum(abs(R[r])**2 for r in R)


def test_live_D_needs_no_cutoff_vanishes_at_omega_and_matches_the_record():
    d = json.load(open(A / "verification" / "the_norm_of_the_boundary_class.json"))
    Di = _D(1j); Dw = _D(complex(np.exp(2j*np.pi/3)))
    assert abs(Dw) < 1e-9                                                         # D(omega) = 0
    stored = d["N5"]["D_over_R2"]["i"]
    assert abs(Di - complex(stored[0], stored[1])) < 1e-6 and abs(Di.real - 1.0888) < 1e-3   # D(i)/|R|^2 = 1.0888


def test_the_bite_a_non_isotropic_triplet_keeps_the_log():
    tau = 0.13+1.07j; S, R, t0, tp = _setup(tau)
    Rp = {2: t0[1]**2/tp, 4: 1j*t0[3]**2/tp, 3: t0[2]**2/tp}                       # another phase assignment: R'.R' != 0
    RpRp = sum(Rp[r]**2 for r in Rp); assert abs(RpRp) > 0.1*sum(abs(Rp[r])**2 for r in Rp)
    f = lambda z: sum(Rp[r]**2*np.abs(S(r, z))**2 for r in (2, 3, 4))
    g = lambda z: sum(R[r]**2*np.abs(S(r, z))**2 for r in (2, 3, 4))
    drift_p = _polar(f, tau, r0=1e-4) - _polar(f, tau, r0=1e-3)                   # grows like 2 pi (R'.R') log 10
    drift = _polar(g, tau, r0=1e-4) - _polar(g, tau, r0=1e-3)                     # Jacobi's R: no log
    assert abs(drift_p/(2*np.pi*RpRp*math.log(10)) - 1) < 1e-6
    assert abs(drift) < 1e-8*sum(abs(R[r])**2 for r in R)


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at 155959126")
    assert hashlib.sha256(open(A / "verification" / "the_norm_of_the_boundary_class.py", "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("9572fd2c")
    d = json.load(open(A / "verification" / "the_norm_of_the_boundary_class.json"))
    assert d["N0"]["void"] is False
    for cell in ("N1", "N2", "N2b", "N3", "N4", "N5", "N6"):
        assert d[cell]["holds"] is True, cell
    assert d["N5"]["omega_abs"] < 1e-10 and abs(d["N5"]["cusp_slope_over_8pi2"] - 1) < 1e-3
    assert abs(d["N5"]["cusp_K"] - 8*math.pi*(1 - 4*math.log(2))) < 1e-12 and abs(d["N5"]["cusp_dev_at_5"]) < 2e-3
    assert d["N6"]["limit_rel_err_at_2560_max"] < 0.02 and d["N6"]["P4prime_m1_m3_max"] < 1e-12
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
