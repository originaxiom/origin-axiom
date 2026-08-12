"""B1048 locks — the seam cluster closed, and the scale wall's Galois proof.

These lock MATHEMATICS (WORKING_RULES §7), recomputed here rather than read from the arc's JSON.
"""
import glob
import json
import pathlib
import re

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
x, t = sp.Symbol("x"), sp.Symbol("t")


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _body(bid):
    return pathlib.Path(glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "FINDINGS.md"))[0]
                        ).read_text(encoding="utf-8")


def test_all_checks_pass():
    R = json.loads(_read("frontier/B1048_the_seam_cluster_closed/results.json"))
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 76


def test_the_scale_ratios_minimal_polynomial():
    """B426's closed form, re-derived. If this ever moves, the whole scale wall moves."""
    a = 2 * sp.cos(2 * sp.pi / 9)
    assert sp.expand(sp.minimal_polynomial(a, x) - (x ** 3 - 3 * x + 1)) == 0
    r = sp.expand(3 * a ** 2 + 4 * a - 1) / 10
    mp = sp.Poly(sp.minimal_polynomial(r, x), x)
    assert sp.expand(mp.as_expr() - (1000 * x ** 3 - 1500 * x ** 2 + 360 * x - 19)) == 0
    assert mp.is_irreducible


def test_the_orbits_exact_averages_are_all_below_one():
    e1, e2, e3 = sp.Rational(3, 2), sp.Rational(9, 25), sp.Rational(19, 1000)
    assert sp.simplify(e1 / 3 - sp.Rational(1, 2)) == 0                      # mean
    assert sp.simplify(sp.sqrt((e1 ** 2 - 2 * e2) / 3) - sp.sqrt(51) / 10) == 0   # RMS
    assert all(float(v) < 1 for v in (e1 / 3, sp.sqrt(51) / 10, sp.root(e3, 3)))
    assert float(e1) > 1        # ...but the SUM exceeds 1 — the slogan's over-broad half


def test_the_power_mean_crossover_is_where_B1048_says():
    """The correction that travels with the restoration. M_5 < 1 < M_6, crossing at ~5.5932."""
    rts = [float(sp.re(r)) for r in
           sp.Poly(1000 * x ** 3 - 1500 * x ** 2 + 360 * x - 19, x).nroots(n=40)]
    pm = lambda p: (sum(r ** p for r in rts) / 3) ** (1.0 / p)
    assert pm(5) < 1 < pm(6)
    lo, hi = 1.0, 200.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if sum(r ** mid for r in rts) < 3 else (lo, mid)
    assert abs(lo - 5.5932) < 1e-3, lo
    assert abs(max(rts) - 1.21702) < 1e-4          # B408's 1.217 IS the largest conjugate


def test_the_conductor_law():
    """B449: fiberedness decides whether the disc×disc formula names anything at all."""
    assert sp.Poly(2 * t ** 2 - 3 * t + 2, t).LC() == 2        # 5_2 not fibered
    assert sp.Poly(2 * t ** 2 - 5 * t + 2, t).LC() == 2        # 6_1 not fibered
    assert sp.expand((t ** 2 - 3 * t + 1)
                     - sp.Matrix([[2, 1], [1, 1]]).charpoly(t).as_expr()) == 0
    assert sp.discriminant(t ** 2 - 3 * t + 1, t) == 5
    assert sp.discriminant(t ** 2 - 6 * t + 1, t) == 32        # silver -> Q(sqrt2), cond 8
    assert sp.discriminant(t ** 2 - 11 * t + 1, t) == 117      # bronze -> Q(sqrt13), cond 13
    assert sp.ilcm(3, 5) == 15 and sp.ilcm(4, 8) == 8
    assert {int(sp.ilcm(3, 13)), int(sp.ilcm(4, 13))} == {39, 52}   # the unrun prediction


def test_the_exchange_is_sigma_17_and_it_fixes_the_seam():
    assert [k for k in range(60) if (4 * k) % 60 == 8 and sp.gcd(k, 60) == 1] == [17, 47]

    def val(gen, k):
        z = lambda j: sp.exp(2 * sp.pi * sp.I * ((j * k) % 60) / 60)
        return complex(sp.N(gen(z), 40))

    g5 = lambda z: 2 * (z(12) + z(-12)) + 1
    g3 = lambda z: z(10) - z(-10)
    assert abs(val(lambda z: z(15), 1) - val(lambda z: z(15), 17)) < 1e-25       # i fixed
    assert abs(val(g5, 1) + val(g5, 17)) < 1e-25                                 # sqrt5 negated
    assert abs(val(g3, 1) + val(g3, 17)) < 1e-25                                 # sqrt-3 negated
    g15 = lambda z: g5(z) * g3(z)
    assert abs(val(g15, 1) - val(g15, 17)) < 1e-25                               # sqrt-15 FIXED


def test_the_par_conjugation_identity():
    """B478, over the whole level-15 range — an exact exponent identity, no floats."""
    bad = [(m, c, j) for m in range(1, 16) for c in range(1, 16) for j in range(15)
           if (c * m * ((-j % 15) * ((-j % 15) - 1) // 2)) % 15
           != (c * m * (j * (j - 1) // 2) + c * m * j) % 15]
    assert bad == [], bad[:5]
    j_, c_, m_ = sp.symbols("j c m", integer=True)
    assert sp.expand(c_ * m_ * (-j_) * (-j_ - 1) / 2
                     - (c_ * m_ * j_ * (j_ - 1) / 2 + c_ * m_ * j_)) == 0


def test_the_address_intensity_law():
    """B402: the s-cell count is a function of gcd(address, 15), and r=0 is the unique dark one."""
    LAND = json.loads(pathlib.Path(glob.glob(
        str(ROOT / "frontier" / "B402_*" / "q2_landscape.json"))[0]).read_text())
    assert len(LAND) == 15
    by = {}
    for r_, v in LAND.items():
        by.setdefault(int(sp.gcd(int(r_), 15)), set()).add(v["s_cells"])
    assert {k: list(v)[0] for k, v in by.items()} == {1: 44, 3: 32, 5: 36, 15: 0}
    assert sum(1 for v in LAND.values() if v["s_cells"] == 0) == 1


def test_the_declines_rest_on_the_arcs_own_words():
    add = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B459_*" / "ADDENDUM.md"))[0]).read_text()
    flat = re.sub(r"\s+", " ", add)
    assert "selection structure is the QR-class's at level 15, not the object's" in flat
    assert "corrects THIS record's own overreach" in flat
    b431 = json.loads(pathlib.Path(glob.glob(
        str(ROOT / "frontier" / "B431_*" / "arc_verdict.json"))[0]).read_text())["claim_one_line"]
    assert "y = 0 mod 3" in b431 and "x ≡ 0 mod 10" not in b431   # one line named, two in the body
    assert "x ≡ 0 mod 10: all dark" in _body("B431")
    assert "demands a mechanism" in _body("B474")


def test_the_restored_rows_carry_their_scope():
    lm = _read("docs/LAW_MAP.md")
    scale = [ln for ln in lm.splitlines()
             if "THE SCALE WALL CLOSES AT THE LEVEL OF GALOIS THEORY" in ln]
    assert len(scale) == 1 and "5.5932" in scale[0] and "B408" in scale[0]
    addr = [ln for ln in lm.splitlines() if "THE SEAM IS AN ADDRESS PROPERTY" in ln]
    assert len(addr) == 1 and "NUMERICAL" in addr[0]     # B363's tier must travel
    cond = [ln for ln in lm.splitlines()
            if "THE SEAM FIELD IS FORCED, AND ITS LEVEL IS A CONDUCTOR" in ln]
    assert len(cond) == 1 and "REGISTERED AND NOT RUN" in cond[0]


def test_the_cluster_stays_firewalled():
    claims = _read("CLAIMS.md")
    for b in ("B363", "B402", "B408", "B426", "B427", "B431", "B449", "B459", "B474", "B478"):
        assert not re.search(rf"\b{b}\b", claims), b
