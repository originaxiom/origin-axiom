"""Locks for B499 (CL-3D / Gate D: the non-Hermitian spectral data package at the object's
kappa = sqrt(3) e^{+-i pi/6}).

The probe (frontier/B499_nonhermitian_dg_data/probe.py) runs ~2.5 min, so this lock does NOT
import it; it INDEPENDENTLY recomputes the decisive cheap facts with the same banked machinery
(B186 escape-rate estimator verbatim; B163/B165 MST max-gap; the exact sympy tier) and then
locks COARSE invariants of the banked JSON (verdict, brackets, monotonicity, labels), never
fragile floats:
 (1) [exact] invariant conservation; seed-on-surface; kappa-2 = zeta_3 (Phi_3 root, Eisenstein);
     coupling lam = e^{i pi/3} (6th root of unity); void Jacobian {phi^2, -1, phi^-2} (B124).
 (2) CONTROLS (prereg: fail => INVALID): gamma(lam=3) reproduces B186's banked early-window
     0.51; V=1 (kappa=3) gives gamma>0 vs band gamma~0; kappa=2 non-escaping real set = the
     band [-2,2] by measure (K010 dictionary).
 (3) the object's level set, coarse recompute: 2D escape rate > 0 (horseshoe signature),
     MST max-gap persistent and >> band at depth 11, spectrum strictly in Im E > 0 (no
     intra-kappa PT reality), conjugate pair exact, H complex symmetric, cond(V) mild.
 (4) banked-JSON coarse invariants + FINDINGS.md house-style/tier integrity.
Total runtime well under 60 s.
"""
import json
import pathlib

import numpy as np
import sympy as sp

np.seterr(over="ignore", invalid="ignore")

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B499_nonhermitian_dg_data"
R = json.load(open(_DIR / "b499_nonhermitian_dg.json"))

LAM = complex(np.exp(1j * np.pi / 3))  # kappa = 2 + LAM^2 = sqrt(3) e^{i pi/6}


# ---------------- shared banked machinery (small, recomputed here) ----------------
def _Tmap(p):
    xx, yy, zz = p
    return np.array([2 * xx * yy - zz, xx, yy])


def _survival(lmb, Egrid, Kmax=30, R_=20.0):  # B186 verbatim
    P = np.array([[(Ev - lmb) / 2, Ev / 2, 1.0] for Ev in Egrid], dtype=complex)
    alive = np.ones(len(P), bool)
    f = []
    for _ in range(Kmax):
        nrm = np.linalg.norm(P, axis=1)
        alive &= np.isfinite(nrm) & (nrm < R_)
        f.append(alive.mean())
        P[~alive] = 0.0
        P = np.array([_Tmap(p) for p in P])
    return np.array(f)


def _escape_rate(f):  # B186 verbatim
    K = np.arange(len(f))
    m = (f > 1e-3) & (f < 0.5)
    if m.sum() < 3:
        return 0.0
    return float(-np.polyfit(K[m], np.log(f[m]), 1)[0])


def _iterate_kt(x, y, z, Kmax=60, R_=20.0):
    alive = np.ones(x.shape, bool)
    kt = np.full(x.shape, Kmax, dtype=int)
    for k in range(Kmax):
        nrm = np.abs(x) + np.abs(y) + np.abs(z)
        esc = alive & ~(np.isfinite(nrm) & (nrm < R_))
        kt[esc] = k
        alive &= ~esc
        x = np.where(alive, x, 0)
        y = np.where(alive, y, 0)
        z = np.where(alive, z, 0)
        x, y, z = 2 * x * y - z, x, y
    return alive, kt


def _metallic_word(n, m=1):
    sub = "a" * m + "b"
    s = {-1: "b", 0: "a"}
    for k in range(1, n + 1):
        s[k] = "".join(sub if c == "a" else "a" for c in s[k - 1])
    return s[n]


def _H(word, lmb, periodic=True):
    L = len(word)
    V = np.array([lmb if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex)
    np.fill_diagonal(H, V)
    i = np.arange(L - 1)
    H[i, i + 1] = 1
    H[i + 1, i] = 1
    if periodic:
        H[0, L - 1] = 1
        H[L - 1, 0] = 1
    return H


def _mst_max_gap_over_diam(ev):  # B163/B165 verbatim
    P = np.c_[ev.real, ev.imag]
    n = len(P)
    intree = np.zeros(n, bool)
    mind = np.full(n, np.inf)
    mind[0] = 0.0
    edges = np.empty(n)
    for t_ in range(n):
        u = int(np.argmin(np.where(intree, np.inf, mind)))
        edges[t_] = mind[u]
        intree[u] = True
        d = np.sqrt(((P - P[u]) ** 2).sum(1))
        upd = (~intree) & (d < mind)
        mind[upd] = d[upd]
    diam = np.hypot(ev.real.max() - ev.real.min(), ev.imag.max() - ev.imag.min())
    return float(edges[1:].max()) / float(diam)


# ---------------- (1) the exact tier, recomputed ----------------
def test_exact_level_set_identities():
    x, y, z, lamS, ES = sp.symbols("x y z lam E")
    Tsym = (2 * x * y - z, x, y)
    I = lambda a, b, c: a**2 + b**2 + c**2 - 2 * a * b * c - 1
    assert sp.expand(I(*Tsym) - I(x, y, z)) == 0
    assert sp.simplify(I((ES - lamS) / 2, ES / 2, 1) - (lamS / 2) ** 2) == 0
    kappa = sp.sqrt(3) * sp.exp(sp.I * sp.pi / 6)
    zeta3 = sp.exp(2 * sp.I * sp.pi / 3)
    EC = sp.expand_complex
    assert EC(kappa - 2 - zeta3) == 0                       # kappa-2 = zeta_3 (K020 sec.5)
    assert EC((kappa - 2) ** 2 + (kappa - 2) + 1) == 0      # Phi_3 root: Eisenstein
    assert EC(sp.conjugate(kappa) - 2 - zeta3**2) == 0      # Galois Z/2 swaps the pair
    assert EC(sp.exp(sp.I * sp.pi / 3) ** 2 - (kappa - 2)) == 0  # coupling = 6th root of 1
    assert EC(sp.Abs(kappa - 2) - 1) == 0


def test_exact_fixed_points_and_void_jacobian():
    x, y = sp.symbols("x y")
    I = lambda a, b, c: a**2 + b**2 + c**2 - 2 * a * b * c - 1
    assert I(0, 0, 0) == -1 and I(1, 1, 1) == 0             # kappa=-2 (4_1, B67) / kappa=2
    J = sp.Matrix([[2 * y, 2 * x, -1], [1, 0, 0], [0, 1, 0]])
    ev = J.subs([(x, 1), (y, 1)]).eigenvals()
    phi = (1 + sp.sqrt(5)) / 2
    for v in [phi**2, sp.Integer(-1), phi**-2]:             # B124 void Jacobian
        assert any(sp.simplify(e - v) == 0 for e in ev)


# ---------------- (2) the controls, recomputed (prereg: fail => INVALID) ----------------
def test_controls_hermitian_anchors():
    reg = np.linspace(-4, 4, 400) + 0j
    g_anchor = _escape_rate(_survival(3.0, reg))
    assert abs(g_anchor - 0.51) < 0.05                      # B186 banked early-window value
    assert _escape_rate(_survival(1.0, reg)) > 0.05         # V=1 level set: DG Cantor, gamma>0
    assert _escape_rate(_survival(0.0, reg)) < 0.02         # kappa=2 band: no escape


def test_control_band_measure_k010_dictionary():
    Ereal = np.linspace(-3, 4, 4001) + 0j
    _, kt = _iterate_kt((Ereal - 0.0) / 2, Ereal / 2, np.ones_like(Ereal), Kmax=40)
    frac = float((kt >= 40).mean())
    assert abs(frac - 4 / 7) < 0.01                         # band [-2,2] has full measure


# ---------------- (3) the object's level set, coarse recompute ----------------
def test_object_exponential_escape_2d():
    re = np.linspace(-2.6, 3.2, 400)
    im = np.linspace(-0.4, 1.4, 150)
    E = re[None, :] + 1j * im[:, None]
    _, kt = _iterate_kt((E - LAM) / 2, E / 2 * np.ones_like(E), np.ones_like(E), Kmax=60)
    f = np.array([(kt >= K).mean() for K in range(61)])
    K = np.arange(61)
    m = (f > 1e-3) & (f < 0.5)
    g = float(-np.polyfit(K[m], np.log(f[m]), 1)[0])
    assert g > 0.25                                         # horseshoe escape signature
    assert (kt >= 40).sum() == 0 or (kt >= 40).mean() < 1e-4  # no pooling at this depth


def test_object_spectrum_cantor_signature_and_symmetries():
    w11 = _metallic_word(11)
    H = _H(w11, LAM)
    assert np.array_equal(H, H.T)                           # complex symmetric, exact
    assert np.array_equal(_H(w11, np.conj(LAM)), np.conj(H))  # conjugate pair, exact
    ev = np.linalg.eigvals(H)
    assert float(ev.imag.min()) > 0.1                       # cloud strictly above R: no PT reality
    gap_o = _mst_max_gap_over_diam(ev)
    gap_b = _mst_max_gap_over_diam(np.linalg.eigvals(_H(w11, 0.0)))
    assert gap_o > 0.08 and gap_o > 4 * gap_b               # B165 diagnostic at depth 11
    _, V = np.linalg.eig(_H(_metallic_word(10), LAM))
    assert 2 < np.linalg.cond(V) < 60                       # mild (polynomial) non-normality


# ---------------- (4) banked-JSON coarse invariants + documentation ----------------
def test_banked_controls_and_verdict():
    assert R["verdict"]["outcome"] == "DATA-BANKED"
    assert R["verdict"]["no_pooling_no_positive_measure"] is True
    assert sorted(R["verdict"]["enum"]) == ["DATA-BANKED", "SURPRISE"]
    assert R["controls"]["gamma_lam3_banked"] == 0.51
    assert abs(R["controls"]["gamma_lam3_anchor"] - 0.51) < 0.05
    assert R["controls"]["gamma_band"] < 0.02
    assert abs(R["controls"]["band_nonescaping_fraction"] - 4 / 7) < 0.01


def test_banked_object_brackets_not_fragile_floats():
    assert 0.3 < R["escape"]["gamma_2d_object"] < 0.75
    assert R["escape"]["real_section_survivors"] == 0
    mst = R["dimension"]["mst_object_d13_d14_d15"]
    assert all(0.08 < v < 0.20 for v in mst) and max(mst) - min(mst) < 0.02
    assert all(0.7 < d < 1.4 for d in R["dimension"]["boxdim_cloud_object"])
    slopes = [R["dimension"]["escape_boxcount"][str(k)]["slope"] for k in (10, 12, 14, 16)]
    assert all(slopes[i] > slopes[i + 1] for i in range(3))  # tightening toward ~1, never 2
    assert slopes[-1] < 1.4
    counts = R["escape"]["survivor_counts_K0_40_step4"]
    assert counts[-1] == 0 and all(a >= b for a, b in zip(counts, counts[1:]))  # zero area


def test_banked_pseudospectra_tameness():
    P = R["pseudospectra"]
    assert P["smin_validation_max_relerr"] < 0.08
    assert P["amplification_max"]["hermitian_control_233"] < 1.2
    assert 1.0 < P["amplification_max"]["object_233"] < 1.1 * P["condV"]["233"]
    assert 0.2 < P["condV_growth_exponent"] < 0.9           # polynomial, not exponential
    assert all(v < 100 for v in P["condV"].values())
    bc = P["obc_pbc_hausdorff_over_diam"]
    assert bc["object"] < 0.1 and bc["object"] < 3 * bc["control"]
    assert 0.7 < P["d_eff_from_eps_areas"] < 1.5


def test_banked_symmetry_block():
    S = R["symmetry"]
    assert S["conjugate_pair_exact"] is True
    assert S["complex_symmetric"] is True
    assert S["pt_reality"] is False and S["pt_asymmetry"] > 0.1
    assert S["min_Im_spec_233"] > 0.1                       # spectrum strictly off the real axis


def test_findings_house_style_and_tier_honesty():
    find = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")
    assert "DATA-BANKED" in find
    assert "DATA-SUPPORTED CONJECTURE" in find
    assert "SURPRISE" in find                               # the committed enum is stated
    assert "Nothing to `CLAIMS.md`; firewall untouched" in find
    assert "NEEDS-SPECIALIST" in find                       # the honest handoff tier
    for c in ("conjecture_D1", "conjecture_D2"):
        assert "DATA-SUPPORTED CONJECTURE" in R["verdict"][c]
        assert "not a claim" in R["verdict"][c]
