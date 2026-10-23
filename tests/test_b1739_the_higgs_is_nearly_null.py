"""B1739 -- the Higgs is nearly null (P-344), PROVED.  Live: the censuses' Higgs (B1691's components) has h.h = eta^6/4 and
reality below 0.01 at Im tau 3.05; rho(T)'s (j, k) eigenlines are null; with u = 0 the left null vector of u1 [h]_x is
conj(h).  Stored: the census law (|V_ud| under the Standard Model's reading follows r^(1/2), log-correlation 0.996)."""
import importlib.util, json, pathlib
import numpy as np
V = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1739_the_higgs_is_nearly_null" / "verification"


def _m():
    spec = importlib.util.spec_from_file_location("b1739", V / "the_higgs_is_nearly_null.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_null_higgs_live():
    m = _m(); h = m.higgs(complex(0.35, 3.05))
    assert abs(h @ h) / np.vdot(h, h).real < 0.01
    fg = m.mods()["FG"]; rng = np.random.default_rng(1739)
    for _ in range(5):
        hh = rng.normal(size=3) + 1j * rng.normal(size=3); Y = (0.7 - 0.2j) * fg.cross(hh); U = np.linalg.svd(Y)[0]
        assert 1 - abs(np.vdot(np.conj(hh) / np.linalg.norm(hh), U[:, 2])) < 1e-12
    d = m.part_d()
    assert sorted(round(x["v.v"], 9) for x in d["rho_T_eigenlines"]) == [0.0, 0.0, 1.0]


def test_the_stored_law():
    r = json.loads((V / "the_higgs_is_nearly_null.json").read_text(encoding="utf-8"))
    assert r["A"]["R_reality_max_(Jacobi)"] < 1e-25
    assert all(abs(g["h.h_over_eta6/4"][0] - 1) < 1e-9 for g in r["A"]["grid"])
    c = r["C"]
    assert c["up S / down S"]["median"] > 0.99 and c["up St / down St"]["median"] > 0.99
    assert c["up St / down S"]["median"] < 0.3 and c["up St / down S"]["median_by_Im_tau"]["3.00-3.50"] < 0.11
    k = r["C_log_correlation_median_Vud_vs_r"]["up St / down S"]
    assert k["log_correlation"] > 0.99 and abs(k["slope_dlog_Vud_dlog_r"] - 0.52) < 0.05
