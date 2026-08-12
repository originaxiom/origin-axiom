"""B1051 locks — B0–B99 closed. Mathematics recomputed here, not read from the arc's JSON."""
import glob
import json
import pathlib
import re

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
t, m = sp.symbols("t m")
M = sp.Matrix([[m, 1], [1, 0]])


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _body(bid):
    return pathlib.Path(glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "FINDINGS.md"))[0]
                        ).read_text(encoding="utf-8")


def _claim(bid):
    return json.loads(pathlib.Path(
        glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))[0]
    ).read_text())["claim_one_line"]


def _row(tag):
    """The row whose HEADLINE this is — not any row that quotes it. Three arcs have now been
    bitten by the naive substring form, so the anchor is part of the lock."""
    hits = [ln for ln in _read("docs/LAW_MAP.md").splitlines()
            if ln.startswith("| **") and tag in ln[:200]]
    assert len(hits) == 1, (tag, len(hits))
    return hits[0]


def test_all_checks_pass():
    R = json.loads(_read("frontier/B1051_the_band_closed/results.json"))
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 57


def test_B27_is_the_tower_law_at_SL3():
    """The load-bearing identity: B27's SL(3) Jacobian charpoly IS Sym^3 + Sym^2 + trivial."""
    half = sp.solve(t ** 2 - t - 1, t)
    a, b = max(half, key=sp.N), min(half, key=sp.N)
    sym = lambda d: [sp.expand(a ** (d - i) * b ** i) for i in range(d + 1)]
    pred = sym(3) + sym(2) + [sp.Integer(1)]
    assert len(pred) == 8
    chi = sp.expand((t - 1) * (t + 1) * (t ** 2 - 4 * t - 1) * (t ** 2 - 3 * t + 1)
                    * (t ** 2 + t - 1))
    assert sp.expand(sp.prod([t - e for e in pred]) - chi) == 0
    assert sp.rem(sp.Poly(chi, t), sp.Poly(t ** 2 - 3 * t + 1, t)).as_expr() == 0
    assert "B27" in _row("THE TRIVIAL-POINT TOWER")


def test_B83_is_B77s_law_in_A_polynomial_language():
    assert "L=(-1)^{n-1}M^n" in _claim("B83").replace(" ", "")
    assert "peripheral eigenvalue shadow is an A-polynomial" in re.sub(r"\s+", " ", _body("B83"))
    assert "high-precision-numerical" in _body("B83")      # the tier must stay visible
    assert "B83" in _row("THE PERIPHERAL EXPONENT IS ORDER-DETERMINED")


def test_the_fingerprints_reach_them_and_not_the_false_positives():
    import importlib.util as ilu
    s = ilu.spec_from_file_location("_ls", ROOT / "scripts" / "checks" / "law_siblings.py")
    LS = ilu.module_from_spec(s); s.loader.exec_module(LS)
    assert re.search(LS.FINGERPRINTS["the tower (B1038)"], _claim("B27"), re.I)
    met = LS.FINGERPRINTS["the metallic exponent (B1039)"]
    for b in ("B76", "B83"):
        assert re.search(met, _claim(b), re.I), b
    # the six the first widening wrongly surfaced — both directions are the lock
    for b in ("B260", "B311", "B433", "B466", "B583", "B852"):
        assert not re.search(met, _claim(b), re.I), b
    assert LS.sweep() == []


def test_the_fixed_line_is_dickson():
    cp = lambda X: sp.expand(X.charpoly(t).as_expr())
    prod = sp.expand(sp.prod([cp(M.inv()), cp(M), cp(M ** 2), cp(M ** 3), cp(M ** 4), cp(-M ** 2)])
                     * (t - 1) ** 2 * (t + 1))
    assert sp.Poly(prod, t).degree() == 15                 # = dim sl(4)
    L = {k: sp.expand((M ** k).trace()) for k in range(1, 5)}
    assert L[1] == m and L[2] == sp.expand(m ** 2 + 2)
    assert L[3] == sp.expand(m ** 3 + 3 * m) and L[4] == sp.expand(m ** 4 + 4 * m ** 2 + 2)
    # B57's two universal splittings, and the cross-link to B63's Dickson trace
    c1 = sp.expand((t ** 2 - 1) * (t ** 2 - m * t - 1))
    c3 = sp.expand((t ** 2 + m * t - 1) * (t ** 2 - (m ** 3 + 3 * m) * t - 1))
    assert c1.coeff(t, 1) == -c1.coeff(t, 3) and c3.coeff(t, 1) == -c3.coeff(t, 3)
    assert sp.expand(L[3] - (m ** 3 + 3 * m)) == 0
    assert sp.expand(sp.cyclotomic_poly(6, t) - (t ** 2 - t + 1)) == 0
    assert sp.expand(sp.cyclotomic_poly(4, t) - (t ** 2 + 1)) == 0


def test_the_cusp_k_set_is_the_quantum_group_level_set():
    for k in range(3, 9):
        q = sp.exp(sp.I * sp.pi / k)
        assert sp.simplify(sp.expand_complex(q + 1 / q) - 2 * sp.cos(sp.pi / k)) == 0
        assert sp.simplify(q ** (2 * k) - 1) == 0
    kset = {mv: [k for k in range(3, mv + 3) if (k - mv) % 2 == 0] for mv in range(1, 7)}
    assert kset == {1: [3], 2: [4], 3: [3, 5], 4: [4, 6], 5: [3, 5, 7], 6: [4, 6, 8]}
    assert "SPECULATIVE-ANALOGY" in _body("B76")


def test_the_riders_that_must_travel():
    flat = lambda s: re.sub(r"\s+", " ", s)
    # B70 corrects itself on the (3,3) bound's scope
    assert "rests on the UNIPOTENT fixed-line object — not the generic ε-series" in flat(_body("B70"))
    assert "grows unbounded" in flat(_body("B70"))
    assert "unipotent" in _row("THE TWO-BLOCK OBSTRUCTION IS RANK-1").lower()
    # B55 corrects the earlier reading
    assert 'the earlier "odd -> Phi_6, even -> Phi_4" reading is corrected' in flat(_body("B55"))
    dick = _row("THE METALLIC FIXED LINE IS DICKSON")
    assert "mod 4" in dick and "is WRONG" in dick
    # B76's fence and the k-collision
    cusp = _row("THE CUSP k-SET IS THE QUANTUM-GROUP LEVEL SET")
    assert "SPECULATIVE-ANALOGY" in cusp and "different `k`" in cusp


def test_B61s_correction_of_B60_survives_the_decline():
    """A phantom wall left on the record is worse than a declined row."""
    flat = re.sub(r"\s+", " ", _body("B61"))
    assert "was a rank-deficient coordinate set" in flat
    assert "The barrier was a coordinate-system defect, not a precision limit" in flat
    led = re.sub(r"\s+", " ", _read("docs/consolidation/DEBT_LEDGER.md"))
    assert "phantom wall" in led


def test_the_band_is_closed_and_stays_firewalled():
    led = _read("docs/consolidation/DEBT_LEDGER.md")
    assert "§B0–B99 — CLOSED" in led
    assert "16 rows = 6 restored as the wall (B1050) + 5 restored here" in re.sub(r"\s+", " ", led)
    claims = _read("CLAIMS.md")
    for b in ("B27", "B55", "B57", "B59", "B60", "B61", "B63", "B70", "B76", "B83"):
        assert not re.search(rf"\b{b}\b", claims), b
