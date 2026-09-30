"""B1503 lock -- THE APEX INDEX RULE.

At a G2 cone point over a finite quotient of a nearly Kaehler manifold, for every automorphism gamma of finite order,
  sum over isolated fixed points of prod_j (1 - e^{-i theta_j})^{-1} + sum over fixed curves of (i/8) cot(theta/2) sin^{-2}(theta/2) (d1 - d2) = 0,
because the link has positive scalar curvature and its Dirac index vanishes; each curve enters through Witten's cubic inflow
n = (N/2)(d1 - d2).  Run as sealed on B1501's 694 classes: the rule holds on all 306 with fixed points; forced inflows occur only on
CP^3's two-sphere classes (pairs n = +-N at one angle) and on S^3 x S^3's 3-symmetry (n = +-3, balanced by an isolated point)."""
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1503_the_apex_index_rule"
VER = ARC / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1503_apex_index_rule", VER / "apex_index_rule.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_seal_and_the_recorded_run():
    M = _load()
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == M.SEALED_SHA256
    r = json.load(open(VER / "apex_index_rule.json"))
    assert r["sealed sha256"] == M.SEALED_SHA256 and r["rule holds"]
    assert r["classes"] == 694 and r["classes with fixed points"] == 306 and r["worst |S|"] < M.RULE_TOL
    assert r["component mismatches"] == [] and r["internal failures"] == []
    rd = r["reading"]
    assert rd["D1 S6 single spheres Delta = 0"] and rd["D2 torus classes n = 0"]
    assert rd["D3 holds (Delta = 2 for sigma, -2 for sigma^2)"]
    assert rd["P1"]["answer"] == "YES" and rd["P1"]["evaluated"] == 22
    assert all(row["pair"] and abs(row["n"][0]) == abs(row["n"][1]) >= 3 for row in rd["P1"]["rows"])
    assert rd["P2"]["answer"] == "YES" and rd["P2"]["evaluated"] == 22
    assert rd["P3"]["answer"] == "YES" and rd["P3"]["spheres evaluated"] == 132 and rd["P3"]["Delta != 0"] == []
    t = rd["P4"]
    assert t["S6"]["classes with n != 0"] == 0 and t["F12"]["classes with n != 0"] == 0
    assert t["CP3"]["classes with n != 0"] == 22 and t["CP3"]["largest |n|"] == 12
    assert t["S3xS3"]["classes with n != 0"] == 2 and t["S3xS3"]["largest |n|"] == 3
    assert sorted(t["S3xS3"]["curves balanced against points"]) == ["S3xS3 L(0,0,0) o sigma", "S3xS3 L(0,0,0) o sigma^2"]
    assert all(t[link]["curves balanced against points"] == [] for link in ("S6", "CP3", "F12"))
    spheres = 0
    for x in r["records"]:
        if x["components"]:
            assert abs(complex(*x["S"])) < M.RULE_TOL
        for c in x["components"]:
            if c["type"] == "sphere" and "d" in c:
                spheres += 1
                assert c["lattice agrees"] and c["integral"] and c["d1 + d2 = -2"]
    assert spheres == 222


def test_the_formula_controls():
    M = _load()
    for lam in (np.exp(0.7j), np.exp(2.1j), np.exp(-2.5j)):
        assert abs(M.point_term([lam]) + M.point_term([1 / lam]) - 1) < 1e-12                       # CP^1
        assert abs(M.point_term([1 / lam, 1 / lam]) + M.curve_term_general([lam], [1], 2) - 1) < 1e-12   # CP^2
    for th in (0.4, 2 * np.pi / 3, 2.9):
        for d1, d2, chi in ((0, -2, 2), (-1, -1, 2), (1, -1, 0)):
            assert abs(M.curve_term_general([np.exp(1j * th), np.exp(-1j * th)], [d1, d2], chi) - M.curve_term(th, d1 - d2)) < 1e-12


def test_the_three_symmetry_live():
    """D3: at e Delta the 3-symmetry acts on T^{1,0} as omega (term -i/(3 sqrt 3)); its fixed sphere has (d1, d2) = (0, -2) by
    isotropy weights and by lattice; the two terms cancel -- an SU(3) locus with n = 3 balanced by an isolated fixed point"""
    M = _load()
    T = M.T
    link = T.S3xS3()
    gam = ("aut", np.eye(6, dtype=complex), link.outer["sigma"])
    Q = M.t10(link)
    D3, leak = M.d_on_t10(link, gam, np.eye(6, dtype=complex), Q)
    pt = M.point_term(np.linalg.eigvals(D3))
    assert leak < 1e-12 and abs(pt + 1j / (3 * np.sqrt(3))) < 1e-12
    rng = np.random.default_rng(3)
    g, res = T.newton_fixed(link, gam, link.random_elements(rng, 24))
    sphere = [x for x, rr in zip(g, res) if rr < 1e-11 and 6 - T.rank_of(link.differential(gam, x) - np.eye(6), 1e-8) == 2]
    assert sphere
    rep = sphere[0]
    lines = M.curve_lines(M.d_on_t10(link, gam, rep, Q)[0])
    sw = M.sphere_weights(link, gam, rep, link.centraliser_basis(gam), Q, lines)
    assert abs(lines["theta"] - 2 * np.pi / 3) < 1e-12 and abs(sw["d1"]) < 1e-9 and abs(sw["d2"] + 2) < 1e-9
    lat = M.sphere_lattice(link, gam, rep, Q, lines["theta"], sw["moving"], (12, 24))
    s = 1.0 if lat["c1 T"] > 0 else -1.0
    assert abs(s * lat["c1 T"] - 2) < 1e-9 and abs(s * lat["c1 N1"]) < 1e-9 and abs(s * lat["c1 N2"] + 2) < 1e-9
    assert abs(pt + M.curve_term(lines["theta"], 2)) < 1e-12
