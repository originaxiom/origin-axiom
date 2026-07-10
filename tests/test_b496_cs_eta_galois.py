"""Locks for B496 (Gate A class 2b: the Chern-Simons / eta class, mirror-sealed).

Loads the banked JSON for the assembled claims and INDEPENDENTLY recomputes the decisive
facts: (1) the exact backbone with no SnapPy -- the 2-torsion fixed-point sets of the
mirror involution, the Lucas cover-torsion law |det(A^n - I)| = |L(2n) - 2| (B489), the
child trace-field quartic x^4 - x - 1 (disc -283, S4, no quadratic subfield -- B434), and
the independent dilogarithm volume anchor; (2) the banked value table's structure -- the
cusped multiset {0 x 13, 1/4} all 2-torsion (sigma-fixed), the exceptional +-rational
pairs summing to zero, the three-bin classification, verdict SEALED with the C-guardrail
phrasing and the NAMED eta TOOL-BLOCK; (3) live SnapPy recomputation (behind importorskip)
of the controls (cs(4_1) = 0, sister m003 = 1/4, a metallic sweep), the forced child pair
(+-0.07703818..., sum 0 mod 1), one exceptional rational recognition (1/84), and one
mirror-law pair from the B432 sample. Total runtime well under 60 s.
"""
import importlib.util
import json
import pathlib
from fractions import Fraction

import mpmath as mp
import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B496_cs_eta_galois"

_spec = importlib.util.spec_from_file_location("b496_probe", _DIR / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

R = json.load(open(_DIR / "b496_cs_eta.json"))


# ---------------- (1) the exact backbone, recomputed (no SnapPy) ----------------
def test_two_torsion_fixed_sets_of_the_mirror_involution():
    # orientation reversal negates cs; amphichiral => 2 cs = 0 in R/(mod)Z:
    assert [v for v in (sp.Rational(k, 4) for k in range(2))
            if (2 * v) % sp.Rational(1, 2) == 0] == [0, sp.Rational(1, 4)]
    assert [v for v in (sp.Rational(k, 2) for k in range(2))
            if (2 * v) % 1 == 0] == [0, sp.Rational(1, 2)]
    assert R["exact"]["fixed_cusped"] == ["0", "1/4"]
    assert R["exact"]["fixed_closed"] == ["0", "1/2"]


def test_lucas_cover_torsion_law_exact():
    A = sp.Matrix([[2, 1], [1, 1]])                     # the RL cat map (B489)
    for n, (lucas, tor) in {1: (3, 1), 2: (7, 5), 3: (18, 16), 4: (47, 45),
                            5: (123, 121), 8: (2207, 2205)}.items():
        assert int((A**n).trace()) == lucas             # = L(2n)
        assert int(abs((A**n - sp.eye(2)).det())) == tor == abs(lucas - 2)
    assert R["exact"]["torsion"] == {str(n): t for n, t in
                                     {1: 1, 2: 5, 3: 16, 4: 45, 5: 121, 8: 2205}.items()} \
        or R["exact"]["torsion"] == {1: 1, 2: 5, 3: 16, 4: 45, 5: 121, 8: 2205}


def test_child_quartic_disc_minus283_S4_no_quadratic_subfield():
    x = sp.Symbol('x')
    Pq = x**4 - x - 1                                   # the Meyerhoff trace field (B434)
    d = sp.discriminant(Pq, x)
    assert d == -283 and sp.isprime(283)
    assert sp.Poly(Pq, x).is_irreducible
    assert sp.Poly(x**3 + 4 * x - 1, x).is_irreducible  # resolvent cubic
    assert not sp.sqrt(sp.Abs(d)).is_integer            # => S4 => no quadratic subfield


def test_dilogarithm_volume_anchor_and_p9_constants():
    mp.mp.dps = 30
    vol = 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))
    assert abs(vol - mp.mpf("2.029883212819307250042405108549")) < mp.mpf("1e-27")
    from origin_axiom.constants import CS_FIG8, CS_SISTER, VOL_FIG8
    assert CS_FIG8 == 0.0 and CS_SISTER == 0.25
    assert abs(VOL_FIG8 - float(vol)) < 1e-9
    assert abs(R["exact"]["vol_dilog"] - float(vol)) < 1e-12


# ---------------- (2) the banked table's structure ----------------
def test_controls_banked_all_pass():
    C = R["controls"]
    assert C["all_pass"] is True
    assert abs(C["seed_cs"]) < 1e-12
    assert abs(C["sister_cs"] - 0.25) < 1e-9
    assert all(abs(v) < 1e-12 for v in C["metallic_cs"].values())
    assert len(C["metallic_cs"]) == 6
    assert abs(C["census_mix"]["m006"]) > 0.05          # the discriminating mix


def test_cusped_multiset_is_two_torsion_and_sigma_fixed():
    assert R["cusped"]["multiset"] == {"0": 13, "1/4": 1}
    rows = R["cusped"]["rows"]
    assert len(rows) == 14
    assert all(row["amphicheiral"] is True for row in rows)
    assert all("exact" in row["tier"] for row in rows)
    vals = [Fraction(row["cs_exact"]) for row in rows]
    # every value 2-torsion in R/(1/2)Z => sigma-FIXED:
    assert all((2 * v) % Fraction(1, 2) == 0 for v in vals)
    assert sorted(v % Fraction(1, 2) for v in vals) == \
        sorted((-v) % Fraction(1, 2) for v in vals)


def test_exceptional_pairs_and_child_pair_sum_zero():
    exc = {row["slope"]: Fraction(row["cs_exact"]) for row in R["interface"]["exceptional"]}
    assert exc["(0,1)"] == 0
    for p, f in [(1, Fraction(1, 84)), (2, Fraction(1, 40)), (3, Fraction(1, 24))]:
        assert exc[f"({p},1)"] == f and exc[f"({-p},1)"] == -f
    assert sum(exc.values()) == 0                       # the +-pairs cancel exactly
    child = R["interface"]["child"]
    assert abs(child["cs"] - 0.07703818) < 1e-7         # the banked B434 value
    assert child["pair_sum_mod1"] < 1e-9
    assert child["meyerhoff_identified"] is True and child["amphicheiral"] is False
    assert child["anti_recognition_q1000"] > 1e-9       # leaves the rational world


def test_eta_tool_blocked_named_not_skipped():
    assert R["interface"]["eta_api_scan"] == []         # the honest scan, banked
    assert "TOOL-BLOCKED" in R["interface"]["eta"]


def test_mirror_law_31_of_31_and_seal_bins():
    ML = R["mirror_law"]
    assert ML["n"] == 31 and ML["law_pass"] == 31
    assert ML["worst_law"] < 1e-9 and ML["banked_match_worst"] < 1e-6
    S = R["seal"]
    assert S["verdict"] == "SEALED"
    assert S["cusped_multiset_fixed"] is True
    assert S["pairs_sum_zero"] is True
    assert S["input_labeled_pass"] is True
    assert S["multiset_sigma_invariant"] is True
    assert sorted(S["forced_set"], key=Fraction) == \
        ["-1/24", "-1/40", "-1/84", "0", "1/84", "1/40", "1/24", "1/4"]


def test_verdict_sealed_with_guardrail_and_docs_integrity():
    assert R["verdict"]["outcome"] == "SEALED"
    assert "computable horizon" in R["verdict"]["phrasing"]
    assert any("TOOL-BLOCKED" in item for item in R["verdict"]["out_of_reach"])
    find = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")
    assert "SEALED" in find
    assert "Nothing to `CLAIMS.md`" in find
    assert "TOOL-BLOCKED" in find and "η" in find       # eta named, not silent
    assert "{0 ×13, ¼}" in find
    readme = (_DIR / "README.md").read_text(encoding="utf-8")
    assert "SEALED" in readme and "TOOL-BLOCKED" in readme   # the committed enum


# ---------------- (3) live SnapPy recomputation (optional dependency) ----------------
def test_snappy_controls_seed_sister_metallic():
    pytest.importorskip("snappy")
    import snappy
    M = snappy.Manifold("4_1")
    assert abs(float(M.chern_simons())) < 1e-12
    assert M.symmetry_group().is_amphicheiral()
    S = snappy.Manifold("m003")
    assert abs(float(S.chern_simons()) - 0.25) < 1e-9
    assert S.symmetry_group().is_amphicheiral()         # 1/4 = the other fixed point
    for m_ in range(1, 7):                              # the B127 K-A sweep
        W = snappy.Manifold("b++" + "R" * m_ + "L" * m_)
        assert abs(float(W.complex_volume().imag())) < 1e-9


def test_snappy_child_pair_exceptional_and_one_law_pair():
    pytest.importorskip("snappy")
    c_child = P.fcs(P.filled(5, 1))
    c_mirror = P.fcs(P.filled(-5, 1))
    assert abs(c_child - 0.07703818) < 1e-7
    assert P.mod_dist(c_child + c_mirror, 1.0) < 1e-9   # the forced +-pair, sum 0
    c1 = P.fcs(P.filled(1, 1))                          # exceptional flat: 1/84 exactly
    assert Fraction(c1).limit_denominator(100) == Fraction(1, 84)
    assert abs(c1 - 1 / 84) < 1e-12
    c34 = P.fcs(P.filled(3, 4))                         # one B432 sample pair
    c34m = P.fcs(P.filled(3, -4))
    assert P.mod_dist(c34 + c34m, 1.0) < 1e-9
