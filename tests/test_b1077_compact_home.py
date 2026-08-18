"""B1077 locks -- the cascade's endpoint has a compact home in the object's own real form.

The census and the A2+A1 search are combinatorial and are RECOMPUTED here from the E6
Cartan matrix; the charge-algebra theta-stability is read from the arc's results.json,
since rebuilding C needs the principal-sl2 construction.
"""
import itertools
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B1077_compact_home")
sys.path.insert(0, os.path.join(ROOT, "frontier", "B1068_j2t_charge_field"))
import e8_build as E  # noqa: E402

R6 = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]
A = E.A


def _res():
    return json.load(open(os.path.join(ARC, "results.json")))


def _eps(sg):
    def f(r):
        s = 1
        for j in range(6):
            if r[j] % 2:
                s *= sg[j]
        return s
    return f


def _pair(r, s):
    return sum(r[i] * A[i][j] * s[j] for i in range(8) for j in range(8))


def _has_A2A1(kr, ch):
    for a, b in itertools.combinations(kr, 2):
        if _pair(a, b) != -1:
            continue
        s = tuple(a[i] + b[i] for i in range(8))
        if not (any(s) and s in E.IDX and ch(s) == 1):
            continue
        for c in kr:
            if c in (a, b) or tuple(-x for x in c) in (a, b):
                continue
            if _pair(c, a) == 0 and _pair(c, b) == 0:
                return True
    return False


def test_the_inner_census_reproduces_B907():
    census = {}
    for sg in itertools.product([1, -1], repeat=6):
        ch = _eps(sg)
        d = 6 + sum(1 for r in R6 if ch(r) == 1)
        census[d] = census.get(d, 0) + 1
    assert census == {78: 1, 46: 27, 38: 36}
    assert {int(k): v for k, v in _res()["census"].items()} == census


def test_the_SM_algebra_is_compact_in_every_e6_2_character():
    """8 roots (A2+A1) + 4 Cartan = 12 = su(3)+su(2)+u(1), inside the maximal compact."""
    n = 0
    for sg in itertools.product([1, -1], repeat=6):
        ch = _eps(sg)
        kr = [r for r in R6 if ch(r) == 1]
        if 6 + len(kr) != 38:
            continue
        assert _has_A2A1(kr, ch), f"no A2+A1 in k for e6(2) character {sg}"
        n += 1
    assert n == 36
    assert _res()["A2A1_in_k"]["38"] == [36, 36]


def test_b892s_fourteen_is_the_same_roots_plus_the_full_cartan():
    r = _res()
    assert r["sm_dim"] == 12 and r["b892_endpoint_dim"] == 14
    assert r["b892_endpoint_dim"] - r["sm_dim"] == 2      # the two dropped u(1)s


def test_so10_is_compact_in_exactly_two_characters():
    n = 0
    for sg in itertools.product([1, -1], repeat=6):
        ch = _eps(sg)
        kr = [r for r in R6 if ch(r) == 1]
        if 6 + len(kr) != 46:
            continue
        span = set()
        for rt in kr:
            for j in range(6):
                if rt[j]:
                    span.add(j)
        if len(kr) + len(span) == 45:
            n += 1
    assert n == 2
    assert _res()["so10_compact_characters"] == 2


def test_C_is_theta_stable_only_in_the_compact_form_and_e6_2():
    """The independent arrival at B907's sealed form."""
    r = _res()
    assert r["C_theta_stable_total"] == 4
    assert r["C_theta_stable_by_form"] == {"38": 3, "78": 1}


def test_existence_is_not_occupancy():
    scope = _res()["scope"]
    assert "does NOT show the object's specific subalgebra IS that one" in scope
    assert "NOT swept" in scope
