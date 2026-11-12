"""B1885 lock -- the golden state on the whole, the web seat's card verified on main.

What could fail: a check of the committed run other than main's own guess H6; the state not transforming with the character
when recomputed; the stored place not being a critical point, or failing the trace test; the series evaluated where its cut
is not negligible; the arc reading as a design, a selection or a value."""
import importlib.util
import json
import pathlib
from fractions import Fraction

import mpmath as mp
import pytest

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
_dps = mp.mp.dps
spec = importlib.util.spec_from_file_location("golden_state_on_main_lock", HERE / "golden_state_on_main.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
mp.mp.dps = _dps                      # the script sets its own precision on import; other locks keep theirs
RES = json.loads((HERE / "golden_state_on_main.json").read_text(encoding="utf-8"))
H6 = "H6 main's point agrees with the one the lane reports to 1e-9"


def test_the_committed_run_has_31_checks_and_only_mains_own_guess_fails():
    checks = {k: v for k, v in RES.items() if isinstance(v, bool)}
    assert len(checks) == 31                # 32 before 2026-11-12: a check over an empty list at level 17 is no longer counted (Review 79)
    assert [k for k, v in checks.items() if not v] == [H6] == RES["failing"]
    run = (HERE / "golden_state_on_main_run.txt").read_text(encoding="utf-8")
    assert "CHECKS: 31, FAILING: 1" in run and "kept as failed" in run
    assert RES["level_17_forced_zeros"] == "none: no check made" and "level 17: the character forces a zero at none of the 2 elliptic points" in run
    assert sum(1 for k in checks if k.startswith("A") and "(added)" in k) == 6          # the six added after the first run say so


def test_the_state_transforms_with_the_character_recomputed():
    with mp.workdps(20):
        F5 = m.Field(5)
        assert (F5.ea, F5.eb, F5.eps_norm) == (0, 1, -1) and abs(F5.R - mp.pi / (2 * mp.log((1 + mp.sqrt(5)) / 2))) < mp.mpf(10) ** -17
        f, fc = m.Form(F5, 300), m.Form(F5, 300, cosine=True)
        assert f.c[5] == -1 and f.c[2] == f.c[3] == f.c[7] == 0 and f.c[4] == f.c[9] == 1 and abs(f.c[11] - mp.mpf("-1.11318395792")) < mp.mpf(10) ** -11
        z = mp.mpc("0.137", "0.412")
        for g, chi in (((2, -1, 5, -2), -1), ((1, 0, 5, 1), 1)):
            assert abs(f(m.mob(g, z)) - chi * f(z)) < mp.mpf(10) ** -14 * abs(f(z))
        assert abs(fc(m.mob((2, -1, 5, -2), z)) + fc(z)) > mp.mpf(10) ** -3 * abs(fc(z))       # the control fails, as it must
        assert abs(f(-1 / (5 * z)) + f(z)) < mp.mpf(10) ** -14 * abs(f(z))                     # the sign under the dual involution is -1
        e1 = (2 + mp.mpc(0, 1)) / 5
        assert abs(f(e1)) < mp.mpf(10) ** -14 * abs(f(z))                                      # the forced zero at an elliptic point


def test_the_stored_place_is_a_critical_point_on_the_circle_and_passes_the_trace_test_recomputed():
    x0, y0 = mp.mpf(RES["level_5"]["z_star"][0]), mp.mpf(RES["level_5"]["z_star"][1])
    assert abs(x0 * x0 + y0 * y0 - mp.mpf(1) / 5) < mp.mpf(10) ** -15
    with mp.workdps(20):
        F5 = m.Field(5); f = m.Form(F5, 300)
        peak = f(mp.mpc(x0, y0)) ** 2
        gx = mp.diff(lambda x: f(mp.mpc(x, y0)) ** 2, x0); gy = mp.diff(lambda y: f(mp.mpc(x0, y)) ** 2, y0)
        assert abs(gx) / peak < mp.mpf(10) ** -9 and abs(gy) / peak < mp.mpf(10) ** -9
        hxx = mp.diff(lambda x: f(mp.mpc(x, y0)) ** 2, x0, 2); hyy = mp.diff(lambda y: f(mp.mpc(x0, y)) ** 2, y0, 2)
        want = -2 * (mp.mpf(1) / 4 + F5.R ** 2) / y0 ** 2
        assert hxx < 0 and hyy < 0 and abs((hxx + hyy) / peak - want) < mp.mpf(10) ** -6 * abs(want)
        # at the lane's reported point the gradient is far from zero: it is near the peak and is not the peak
        lx, ly = mp.mpf("0.251539778829130"), mp.mpf("0.369767144294671")
        gl = mp.sqrt(mp.diff(lambda x: f(mp.mpc(x, ly)) ** 2, lx) ** 2 + mp.diff(lambda y: f(mp.mpc(lx, y)) ** 2, ly) ** 2) / peak
        assert mp.mpf("5e-8") < gl < mp.mpf("3e-7")
        assert mp.mpf("1.4e-9") < abs(mp.mpc(lx, ly) - mp.mpc(x0, y0)) < mp.mpf("1.6e-9")


def test_the_series_refuses_a_height_where_its_cut_is_not_negligible():
    with mp.workdps(20):
        f = m.Form(m.Field(5), 60)
        f(mp.mpc("0.2", "0.4"))                                  # 34 terms are enough here
        with pytest.raises(ValueError):
            f(mp.mpc("0.1", "0.01"))                             # here 1353 would be needed: the first run's fault, now refused


def test_the_cell_and_where_the_character_forces_a_zero_by_hand():
    # CORRECTED 2026-11-12 (Review 79; found by a second reading).  Two lines stood here that did arithmetic on typed fractions:
    # they could not fail.  The two circles are now computed, as the mirrors of two reflections; that each reflection carries
    # the group to itself is checked on the group's generators; and the corner where they meet is computed and held to the
    # fixed point of the group's own element of order 2.  What could fail: a reflection that does not normalise the group, a
    # mirror that is not the circle the page names, an angle that is not right, a corner that is not the elliptic point.
    def mul2(A, B):
        return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
                (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))

    def in_group(A):                                   # an integer matrix of determinant 1 whose lower left entry is a multiple of 5
        return all(x.denominator == 1 for r in A for x in r) and A[0][0] * A[1][1] - A[0][1] * A[1][0] == 1 and A[1][0] % 5 == 0

    def carries_the_group_to_itself(a, b, c, d):       # z -> (a conj z + b) / (c conj z + d) is N after the mirror z -> -conj z, N = [[-a, b], [-c, d]]
        N = ((Fraction(-a), Fraction(b)), (Fraction(-c), Fraction(d)))
        det = N[0][0] * N[1][1] - N[0][1] * N[1][0]
        Ninv = ((N[1][1] / det, -N[0][1] / det), (-N[1][0] / det, N[0][0] / det))
        gens = (((1, 1), (0, 1)), ((2, -1), (5, -2)), ((3, -2), (5, -3)), ((1, 0), (5, 1)), ((11, 2), (5, 1)))
        out = []
        for g in gens:
            mirrored = ((Fraction(g[0][0]), Fraction(-g[0][1])), (Fraction(-g[1][0]), Fraction(g[1][1])))
            out.append(in_group(mul2(mul2(N, mirrored), Ninv)))
        return det > 0 and all(out)

    def mirror(a, b, c, d):                            # its fixed points: c |z|^2 - a (z + conj z) - b = 0, a circle centred on the real axis
        assert d == -a and c != 0
        return Fraction(a, c), Fraction(a * a + b * c, c * c)             # the centre and the radius squared
    R1, R2 = (0, 1, 5, 0), (5, -2, 10, -5)
    assert carries_the_group_to_itself(*R1) and carries_the_group_to_itself(*R2)
    assert not carries_the_group_to_itself(0, 1, 3, 0) and not carries_the_group_to_itself(2, -1, 5, -2)   # the control: two that do not
    (c1, r1), (c2, r2) = mirror(*R1), mirror(*R2)
    assert (c1, r1) == (0, Fraction(1, 5)) and (c2, r2) == (Fraction(1, 2), Fraction(1, 20))                # |z|^2 = 1/5 and |z - 1/2|^2 = 1/20
    assert (c2 - c1) ** 2 == r1 + r2                                                                        # they meet at a right angle
    x = (r1 - r2 + c2 * c2 - c1 * c1) / (2 * (c2 - c1)); y2 = r1 - (x - c1) ** 2                            # where they meet
    ea, eb, ec, ed = 2, -1, 5, -2                                                                           # the group's element of order 2
    assert in_group(((Fraction(ea), Fraction(eb)), (Fraction(ec), Fraction(ed)))) and ea + ed == 0
    assert (x, y2) == (Fraction(ea - ed, 2 * ec), Fraction(4 - (ea + ed) ** 2, 4 * ec * ec)) == (Fraction(2, 5), Fraction(1, 25))
    order2 = lambda p: [d for d in range(1, p) if (d * d + 1) % p == 0]
    order3 = lambda p: [d for d in range(1, p) if (d * d + d + 1) % p == 0]
    assert order2(5) == [2, 3] and order3(5) == [] and order2(13) == [5, 8] and order3(13) == [3, 9] and order2(17) == [4, 13] and order3(17) == []
    assert [m.legendre(d, 5) for d in order2(5)] == [-1, -1] and [m.legendre(d, 13) for d in order2(13)] == [-1, -1]
    assert [m.legendre(d, 13) for d in order3(13)] == [1, 1] and [m.legendre(d, 17) for d in order2(17)] == [1, 1]
    rows = {(13, o, d): (c, float(v)) for o, d, c, v in RES["level_13"]["elliptic_points"]}
    rows.update({(17, o, d): (c, float(v)) for o, d, c, v in RES["level_17"]["elliptic_points"]})
    assert all(v < 1e-20 for (p, o, d), (c, v) in rows.items() if c == -1) and all(v > 1 for (p, o, d), (c, v) in rows.items() if c == 1)
    assert len(rows) == 6 and RES["level_5"]["cell"]["negative"] == 0 and RES["level_5"]["cell"]["positive"] == RES["level_5"]["cell"]["points"] > 10000


def test_the_arc_says_what_it_is_and_is_not():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("It selects nothing and derives no value", "It is not main's design", "\"Lowest\" and \"simple\" are not verified on main", "A grid is not a proof",
              "One clause of P-776 is no longer kept", "compared with no value of τ on record, and no frame is evaluated at it", "Main's own expectation H6 fails as written",
              "The place depends on the measure", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1885" and v["claim_one_line"].endswith("0 of 19.") and v["weave_or_thread"].startswith("weave")
    assert "selects nothing" in v["claim_one_line"] and "not main's design" in v["claim_one_line"]


# ------------------------------------------------------------------------------------------------ added 2026-11-12 (Review 80)
# A session that built none of this planted against the lock.  The verdict changed to another word passed; the note on the
# grid's precision taken out of the verdict line passed; and the peak was held to two negative second derivatives with no
# determinant.  Each is held now.

def test_the_verdict_and_the_note_on_the_grids_precision_are_held():
    import re
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED"
    assert "18 for the grid and the three checks made on it, A4, A5 and H5" in v["claim_one_line"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "the grid is made at 18 digits, and three checks are made on it: A4, A5 and H5" in f
    # the three are the script's: the checks it makes on the grid's values, after the precision is put back to 30
    src = (HERE / "golden_state_on_main.py").read_text(encoding="utf-8")
    a = src.index("mp.mp.dps = 18"); b = src.index("mp.mp.dps = 30", a); c = src.index("H6 main's point", b)
    assert re.findall(r'check\("(A4|A5|H5) ', src[b:c]) == ["A4", "A5", "H5"]


def test_the_peak_is_a_maximum_by_the_determinant_as_well():
    x0, y0 = mp.mpf(RES["level_5"]["z_star"][0]), mp.mpf(RES["level_5"]["z_star"][1])
    with mp.workdps(20):
        F5 = m.Field(5); f = m.Form(F5, 300)
        hxx = mp.diff(lambda x: f(mp.mpc(x, y0)) ** 2, x0, 2); hyy = mp.diff(lambda y: f(mp.mpc(x0, y)) ** 2, y0, 2)
        hxy = mp.diff(lambda x, y: f(mp.mpc(x, y)) ** 2, (x0, y0), (1, 1))
        assert hxx < 0 and hxx * hyy - hxy ** 2 > 0
