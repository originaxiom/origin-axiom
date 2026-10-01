"""B1512 lock -- THE SELF-COINCIDENT ORBITS (2026-10-01).  m004's symmetries act on Ballas' family (the fibre's hyperelliptic involution
fixes it; the dual family is the family at 1/q; the strong inversion and the amphichiral map send q to 1/q), and B1511's 32 unresolved
case-(b) pairs on M5 and M6 all fire; sealed at b8ddbb66 before any polynomial of the twelve orbits was computed.  Locked here:
- the seal's digest and markers;
- the controls' record (K1-K10);
- the four symmetries live: the exact intertwiners for iota, the duality, eps and alpha, and the sign table;
- M5's one polynomial live (reconstructed over Q, palindromic, its closed form in w = q + 1/q);
- two counts live over GF(p): an M5 member at its Jordan point (lam = -1) and at its double point (lam = 1, w = 7), both +1;
- the decided items D1-D10 and the predictions P1-P7 from the record, and the post-run record;
- the findings' load-bearing sentences.
The controls' full rerun is marked slow (about seventy seconds); the sealed census (fourteen minutes) is not rerun by the lock."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1512_the_self_coincident_orbits"
VER = ARC / "verification"
SEALED_SHA = "7d0a41429144effd0eee0792f40413d43809cb237917b8d75b612ad63edf47f6"


def _load(name):
    if str(VER) not in sys.path:
        sys.path.insert(0, str(VER))
    spec = importlib.util.spec_from_file_location(name, VER / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _record(name):
    return json.loads((VER / f"{name}_run.txt").read_text(encoding="utf-8"))


def _norm(x):
    return json.loads(json.dumps(x, sort_keys=True, default=str))


def test_the_seal_is_unchanged():
    """PREREGISTRATION.md is byte-identical to the sealed text (SEAL_LEDGER) and carries the provenance markers"""
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEALED_SHA
    txt = (ARC / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
    assert SEALED_SHA in (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")


def test_the_controls_record():
    """K1-K10 as recorded before the seal"""
    c = _record("controls")
    assert all(v for v in c["K1"].values() if isinstance(v, bool)) and c["K1"]["det C"] == "16*q**2" and c["K1"]["C^2"] == "4*q"
    assert all(x["characters not killing it"] == 0 for x in c["K2"])
    assert c["K3"]["level_5"]["classes"] == [[12, 19], [15, 18]]
    assert c["K3"]["level_6"]["classes"] == [[1, 3], [31, 53], [32, 34], [33, 47]]
    assert c["K3"]["the 32 pairs"] == {"banked": 32, "here": 32, "match": True}
    assert all(x["equals Res(Q, s - r^n)"] and x["fresh_agree"] for x in c["K4"]["untwisted"])
    assert all(x["equals B1511 Part A"] for x in c["K4"]["s961"]) and all(x["equals B1511 Part C1"] for x in c["K4"]["M4"])
    assert all(x["B1511's row reproduced"] for x in c["K5"])
    assert all(x["ker_dims"] == ([1, 2, 2, 2] if x["nu"] == [0, 0] else [1, 1, 1, 1]) for x in c["K6"])
    assert c["K8"]["all hold"] and c["K8"]["lemmas"]["det D"] == "-16*q*(q**2 + q + 1)" and c["K8"]["lemmas"]["det E"] == "16*q**4"
    assert all(x["pairs differing"] == 0 and x["swap maps characters to characters"] for x in c["K9"]["levels 2-4"])
    assert c["K10"]["all hold"] and c["K10"]["lemma"]["det A"] == "-16*q**3" and c["K10"]["lemma"]["det M"] == -1
    assert c["K10"]["class map under alpha"]["level_5"] == {"12": 19, "15": 15, "18": 18, "19": 12}


def test_the_four_symmetries_live():
    """iota fixes rho_q; rho_q^-T ~ rho_(1/q); rho_q ~ rho_(1/q) o eps and o alpha; the sign table (main's B1324 patterns)"""
    L = _load("selfco_lib")
    i = L.involution_checks()
    assert i["intertwiner: dimension of the solution space"] == 1 and i["C rho(g) C^-1 = rho(iota g) for g = m, n"]
    assert i["iota(R) is a cyclic conjugate of R^-1 (free group)"] and i["iota^2 = id on m and n (free group)"]
    d = L.duality_checks()
    assert d["D rho_q(g)^-T D^-1 = rho_1/q(g), g = m, n"] and d["E rho_q(g) E^-1 = rho_1/q(eps g), g = m, n"]
    a = L.amphichiral_checks()
    assert a["A rho_q(g) A^-1 = rho_1/q(alpha g), g = m, n"] and a["rho_q(alpha(R)) = 1 (over Q(q))"]
    assert a["psi phi (g) = y phi psi (g) y^-1 for g = x, y (free group)"] and a["M^2 = Phi^-1"] and a["det M"] == -1
    t = L.symmetry_table()
    assert [t[k]["orientation"] for k in ("iota", "eps", "alpha", "theta (F14)")] == ["preserving", "preserving", "reversing", "preserving"]
    assert t["theta = iota phi^-2 eps on H_1(F)"]


def test_m5_one_palindromic_polynomial_live():
    """M5's eigenline class reconstructed over Q equals the record, is palindromic, and has the closed form in w = q + 1/q"""
    L = _load("selfco_lib")
    q, s = L.q, L.s
    P, rec = L.reconstruct_P((1, 5), 5, 11)
    assert rec["all_fresh_agree"]
    banked = [c for c in _record("census")["B"]["level_5"]["classes"] if c["class_orbits"] == [12, 19]][0]
    assert sp.simplify(P - sp.sympify(banked["P(q,s)"], locals={"q": q, "s": s})) == 0
    assert L.symmetries(P)["palindromic in s"] and L.reciprocal_in_q_identity(P)
    w = q + 1 / q
    closed = s ** 4 + 4 * (w ** 2 - 14) * (s ** 3 + s) - (w ** 5 - 14 * w ** 4 + 46 * w ** 3 + 48 * w ** 2 - 119 * w - 208) * s ** 2 + 1
    assert sp.simplify(sp.expand(P - closed)) == 0
    assert sp.simplify(P.subs(s, 1) + (w - 7) ** 2 * (w - 2) * (w + 1) ** 2) == 0


def test_two_m5_counts_live():
    """over GF(p) at one root each: an M5 member at its lam = -1 Jordan point (fibre (1, 2, 2, 2)) and at its lam = 1 double point
    (w = 7, fibre (2, 2, 2, 2), h1 = 2): I(W1) = +1, I(W2) = -1, I(L2 W) = 0"""
    L = _load("selfco_lib")
    q = L.q
    cc = L.CoverCache(5)
    g_jordan = q ** 10 - 14 * q ** 9 + 51 * q ** 8 + 29 * q ** 6 - 294 * q ** 5 + 29 * q ** 4 + 51 * q ** 2 - 14 * q + 1
    for g0, l, fib in ((g_jordan, 2, [1, 2, 2, 2]), (q ** 2 - 7 * q + 1, 0, [2, 2, 2, 2])):
        p, roots = L.primes_with_roots(g0, 44, 1)[0]
        rows = L.counts_at(cc, p, roots[0], [(1, 5)], 11, (l,))
        r = rows[f"(1, 5)|{l}"]
        assert r["fibre"]["rank_B"] == 4 and r["fibre"]["ker_dims"] == fib
        assert {v["I"] for v in r["counts"]["W1"].values()} == {1} and {v["I"] for v in r["counts"]["W2"].values()} == {-1}
        assert {v["I_L2"] for k in ("W1", "W2") for v in r["counts"][k].values()} == {0}


def test_the_record():
    """D1-D10 and P1-P7 as read in FINDINGS sections 3-4"""
    r = _record("census")
    assert r["banked_identity"]["pass"]
    assert all(v for v in r["A"]["involution"].values() if isinstance(v, bool))
    assert all(v for v in r["A"]["duality_and_strong_inversion"].values() if isinstance(v, bool))
    assert all(v for v in r["A"]["amphichirality"].values() if isinstance(v, bool))
    for lv, n in (("level_5", 5), ("level_6", 6)):
        for c in r["B"][lv]["classes"]:
            assert c["reconstruction"]["all_fresh_agree"] and c["every member of the class agrees mod p"]
            assert all(c["independent of the root-of-unity choice (k: ok)"].values())
            assert c["symmetries"]["constant term"] == "1" and c["Lemma D: P(1/q, s) = s^4 P(q, 1/s) / P(q, 0)"]
            assert c["banked_degrees_all_agree"] and c[f"equals Q(q^{n}, s)"] is False
            assert c["symmetries"]["palindromic in s"] is (n == 5)
        assert all(x["P_image(q, s) = P(1/q, s)"] for x in r["B"][lv]["D9 (Lemma A)"])
    assert r["B"]["level_5"]["relations"][0]["equal"]
    assert all(x["positive roots closed under q -> 1/q (Lemma D)"] for lv in ("level_5", "level_6") for x in r["C"][lv])
    assert all(not x["positive root not 1"] for x in r["E"]["pairs outside the sealed set (B1511 resolved them; a check)"])
    for x in r["D"]:
        assert x["uniform"] and x["W1 values"] == [1] and x["W2 values"] == [-1] and x["L2 values"] == [0]
        assert [f[0] for f in x["fibre values mod p"]] == [4] and x["numeric_fibre_values"] == x["fibre values mod p"]
    fib = {(x["level"], x["lam"]): x["fibre values mod p"][0][1] for x in r["D"]}
    assert fib[(5, "1")] == [2, 2, 2, 2] and fib[(5, "-1")] == [1, 2, 2, 2] and fib[(5, "i")] == [1, 1, 1, 1]
    assert all(v == [1, 1, 1, 1] for (lv, lam), v in fib.items() if lv == 6)
    E = r["E"]
    assert E["count"] == 32 and all(p["fires"] for p in E["pairs"]) and E["fires_by_level"] == {"level_5": True, "level_6": True}
    assert E["D8 holds everywhere"] and E["D10 holds everywhere"]


def test_the_post_run_record():
    """(a) M5's closed forms in w; (b) the only coincidence between different families is w = 7 (M4 and M5, lam = 1);
    (c) at M5's double point every class tried counts +1 (W1) and -1 (W2)"""
    r = _record("post_run_checks")
    a5 = r["a_closed_forms_in_w"]["level_5"][0]
    assert a5["P(q, 1) in w"] == "-(w - 7)**2*(w - 2)*(w + 1)**2" and a5["c1 = c3 (in w)"] == "4*(w**2 - 14)"
    cross = [c for c in r["b_coincidences_across_the_tower"]["coincidences"]
             if c["a"].split(" ")[0] != c["b"].split(" ")[0] or "pullback" in c["a"] or "triplet" in c["a"]]
    assert cross and all(c["common w-factor"] == "w - 7" and c["a"].startswith("M4") for c in cross)
    for row in r["c_M5_double_point_classes"]:
        assert row["W1 classes tried"] == ["c1", "c1+c2", "c2"] and all(v == 1 for _, v in row["W1 (class, I)"])
        assert all(v == -1 for _, v in row["W2 (class, I)"])


def _strip_timing(x):
    if isinstance(x, dict):
        return {k: _strip_timing(v) for k, v in x.items() if k != "seconds"}
    if isinstance(x, list):
        return [_strip_timing(v) for v in x]
    return x


@pytest.mark.slow
def test_the_controls_reproduce():
    """controls.main() equals the committed record, wall-clock fields aside (about seventy seconds)"""
    rec = _record("controls")
    out = _norm(_load("controls").main())
    assert _strip_timing(out) == _strip_timing(rec)


def test_findings_verdict_and_hygiene():
    """the verdict is PROVED, creates no law, keeps 0 of 19; the findings carry the symmetries, the 32 pairs, the predictions, the
    slip and the leads; the owner's private term is absent"""
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1512" and v["verdict"] == "PROVED" and v["creates_law"] is False and v["instrument"] is False
    assert "0 of 19" in v["claim_one_line"] and "I-26 stays UNEARNED" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for needle in ("**The answer (the sealed run).** Every one of the 32 pairs fires.", "| P1 | M₅'s polynomial is Q(q⁵, s) (~25%) | **NO**",
                   "| P6 | every real exceptional point is a simple fibre root (~55%) | **NO**",
                   "**The only coincidence between different families is w = 7**", "**A design slip, caught before the seal (ERROR_LEDGER).**",
                   "Nothing is UNRESOLVED on levels 1–6.", "post_run_checks_run.txt", SEALED_SHA, "I-26 stays UNEARNED", "0 of 19"):
        assert needle in f, needle
    term = bytes([98, 114, 97, 118, 101]).decode()  # the owner's private term, kept out of the source text
    for path in (ARC / "FINDINGS.md", ARC / "PREREGISTRATION.md"):
        assert term not in path.read_text(encoding="utf-8").lower()
    assert term not in v["claim_one_line"].lower()
