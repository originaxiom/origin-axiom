"""B1684 -- the SM seat's W59 (the one-loop potential on the shared fibre) checked on main (P-099, P-100). Live, from
main's own check: the twisted determinant by the Epstein-Poisson route against the theta formula, and the parity
product 4 (the bite: the wrong sign map misses); the cover's arithmetic; who sees which line; the Higgs alone at omega on
eighteen lines in ninths (the bite: at tau_0 its minima are not those lines); on a half-period line the Higgs's term is
not stationary at omega, while the joint parity sum is. Stored: main's full run and the received files' hashes."""
import cmath, hashlib, importlib.util, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1684_w59_on_main"


def _m():
    spec = importlib.util.spec_from_file_location("mw59", A / "verification" / "main_check" / "main_w59.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_determinant_and_the_cover_live():
    m = _m()
    for phi, tau in (((0.31, 0.72), complex(0.13, 1.37)), ((0.6, 0.15), complex(-0.4, 0.95))):
        e = m.logdet_epstein(phi, tau)
        assert abs(e - m.logdet_theta(phi[1] - phi[0] * tau, tau)) < 1e-12
        assert abs(e - m.logdet_theta(phi[0] - phi[1] * tau, tau)) > 1e-3          # the bite: the other map misses
    assert abs(math.exp(sum(m.logdet_epstein(p, complex(0.2, 1.1)) for p in m.PAR)) - 4) < 1e-12
    r2 = m.m2(); assert r2["holds"] and r2["zeta_Sigma_0"] == "-3/2"
    assert m.m5()["holds"]


def test_the_higgs_lines_and_the_half_period_live():
    m = _m()
    for tau, expect in ((m.OMEGA, True), (complex(0.17, 1.13), False)):
        S = m.Sixd(tau, N=24, coef=m.joint_coef)
        k = np.arange(9) / 9.0; W = np.array([(a, b) for a in k for b in k]); v = S.val(np.mod(3 * W, 1.0))
        lines = {tuple(np.round(W[i] * 9).astype(int)) for i in range(len(W)) if abs(v[i] - v.min()) < 1e-9}
        ninths = {((1 + 3 * a) % 9, (1 + 3 * b) % 9) for a in range(3) for b in range(3)} | {((2 + 3 * a) % 9, (2 + 3 * b) % 9) for a in range(3) for b in range(3)}
        assert (lines == ninths) is expect                                      # the bite: at tau_0 the minima move
    h = 1e-5; f = lambda t: m.higgs_on_line(t, (0.5, 0.5), N=30)
    g = math.hypot((f(m.OMEGA + h) - f(m.OMEGA - h)) / (2 * h), (f(m.OMEGA + 1j * h) - f(m.OMEGA - 1j * h)) / (2 * h))
    E = lambda t: m.E3_direct(t, N=30)
    g0 = math.hypot((E(m.OMEGA + h) - E(m.OMEGA - h)) / (2 * h), (E(m.OMEGA + 1j * h) - E(m.OMEGA - 1j * h)) / (2 * h))
    assert g > 1.0 and g0 < 1e-5


def test_stored_run_and_received_hashes():
    d = json.loads((A / "verification" / "main_check" / "main_w59.json").read_text(encoding="utf-8"))
    assert all(d["hold"].values())
    om = d["M4"]["omega_summary"]
    assert om["n_stationary"] == 12 and abs(om["global_min"]["value"] + 1.7255235613) < 1e-8
    assert len(d["M4"]["tau_1"]["boson"]) == 6 and d["M6"]["n_lines"] == 18
    for line in (A / "SHA256_RECEIVED.txt").read_text().splitlines():
        h, name = line.split()
        assert hashlib.sha256((A / "verification" / "received" / name).read_bytes()).hexdigest() == h, name
    v = json.loads((A / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and v["rests_on_seat"] == ["sm:W59"]
