"""B1887 lock -- the web seat's check of the agy lane's loop, verified on main.

What could fail: a check of the committed run; a second root lattice of determinant 1 among the 95; the complete enumeration
disagreeing with a plain box search; the table's six-figure places moving; a declared word keeping the mark; the arc reading
as an adoption of anything of the lane's."""
import importlib.util
import itertools
import json
import pathlib

import mpmath as mp
import pytest

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
_dps = mp.mp.dps
spec = importlib.util.spec_from_file_location("loop_check_on_main_lock", HERE / "loop_check_on_main.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
RES = json.loads((HERE / "loop_check_on_main.json").read_text(encoding="utf-8"))


@pytest.fixture(autouse=True)
def _forty_digits():
    with mp.workdps(40):
        yield
    mp.mp.dps = _dps


def test_every_check_of_the_committed_run_holds():
    checks = {k: v for k, v in RES.items() if isinstance(v, bool)}
    assert len(checks) == 35 and all(checks.values())
    assert "CHECKS: 35, FAILING: 0" in (HERE / "loop_check_on_main_run.txt").read_text(encoding="utf-8")


def test_one_root_lattice_of_determinant_one_among_the_95_recomputed():
    systems = ([("A", n) for n in range(1, 25)] + [("B", n) for n in range(2, 25)] + [("C", n) for n in range(3, 25)]
               + [("D", n) for n in range(4, 25)] + [("E", 6), ("E", 7), ("E", 8), ("F", 4), ("G", 2)])
    assert len(systems) == 95
    one = [kn for kn in systems if m.det(m.gram(m.simple_roots(*kn))) == 1]
    assert one == [("E", 8)] == [("E", 8)] and RES["A"]["determinant_one"] == ["E8"]
    assert m.det(m.gram(m.simple_roots("B", 5))) == 32 and m.det(m.gram(m.simple_roots("A", 7))) == 8 and m.det(m.gram(m.simple_roots("G", 2))) == 3


def test_the_metallic_invariants_recomputed():
    for k in range(1, 13):
        W = m.word("L" * k + "R" * k)
        assert m.invariants((W[0] - 1, W[1], W[2], W[3] - 1)) == (k, k)
        assert m.invariants((W[0] + 1, W[1], W[2], W[3] + 1)) == ((1, k * k + 4) if k % 2 else (2, (k * k + 4) // 2))


def test_the_complete_enumeration_agrees_with_a_plain_box_at_one_golden_period():
    """a control that can fail: the classes of least |Q| in each sector, found by walking the parallelogram, are the ones
    a box of half-width 60 finds"""
    A = m.word("LLLLLLR" + "LR"); ax = m.Axis(A, m.by_rows)
    for q, want in ((1, 60), (2, 35)):
        allowed = m.sector((1, 3), q)
        low, classes = ax.least(allowed)
        box = [v for v in itertools.product(range(-60, 61), repeat=2) if v != (0, 0) and allowed(v) and abs(ax.Q(v)) == low]
        assert low == want and min(abs(ax.Q(v)) for v in itertools.product(range(-60, 61), repeat=2) if v != (0, 0) and allowed(v)) == low
        assert {ax.canonical(v) for v in box} == set(classes)
    # the invariant form is invariant, and the history sends the mark to itself
    assert all(ax.Q(m.by_rows(v, A)) == ax.Q(v) for v in ((1, 3), (2, 5), (-3, 7), (11, -4)))
    assert tuple(x % 5 for x in m.by_rows((1, 3), A)) == (1, 3)


def test_the_table_for_one_two_and_three_golden_periods_recomputed():
    want = {1: (("one", "0.5"), ("pair", "0.300865")), 2: (("pair", "0.391512"), ("pair", "0.225903")), 3: (("one", "0.5"), ("pair", "0.182225"))}
    fib = [1, 1]
    while len(fib) < 20:
        fib.append(fib[-1] + fib[-2])
    for k in (1, 2, 3):
        T = m.table("LLLLLLR" + "LR" * k, m.by_rows, (1, 3))
        assert T["sign"] == (1 if k % 2 else -1) and len(T["untwisted"][1]) == 1 and T["untwisted"][0] == fib[2 * k + 1]
        for q in (1, 2):
            kind, val = m.shape(T, q)
            assert kind == want[k][q - 1][0] and abs(val - mp.mpf(want[k][q - 1][1])) < mp.mpf("0.0000006")
            assert RES["C"]["table"][str(k)]["mark" if q == 1 else "twice_the_mark"][0] == kind
        # with columns the two sectors change places
        Tc = m.table("LLLLLLR" + "LR" * k, m.by_columns, (1, 3))
        assert all(m.shape(Tc, q)[0] == m.shape(T, 3 - q)[0] and abs(m.shape(Tc, q)[1] - m.shape(T, 3 - q)[1]) < mp.mpf(10) ** -25 for q in (1, 2))
    assert [RES["C"]["table"][str(k)]["least_Q"][0] for k in range(1, 9)] == [fib[2 * k + 1] for k in range(1, 9)] == [3, 8, 21, 55, 144, 377, 987, 2584]
    assert RES["C"]["apex_vector"] == [1, 0] and RES["C"]["pair_vectors"] == [[2, 1], [8, -1]]
    assert all(1.82 < float(RES["C"]["table"][str(k)]["pair_arclength"]) < 1.87 < 2.08 < float(RES["C"]["table"][str(k)]["tube"]) < 2.11 for k in range(1, 9))


def test_the_two_declared_words_recomputed():
    keeps = lambda w, act: tuple(x % 5 for x in act((1, 3), m.word(w))) in ((1, 3), (4, 2))
    for k in (1, 2, 3):
        d1, i1 = "LLRRLL" + "LR" * k, "LLRRLLR" + "LR" * k
        d2, i2 = "LL" + "RL" * 4 + "R" + "LL" + "R" + "LR" * k, "LL" + "RL" * 4 + "RR" + "LR" * k
        assert m.cyclic_runs(d1)[:4] == [2, 2, 3, 1] and m.cyclic_runs(i1)[:4] == [2, 2, 2, 1]
        assert m.cyclic_runs(d2)[:11] == [2] + [1] * 9 + [2] and m.cyclic_runs(i2)[:10] == [2] + [1] * 8 + [2]
        for act in (m.by_rows, m.by_columns):
            assert not keeps(d1, act) and not keeps(d2, act) and keeps(i1, act) and keeps(i2, act)
    M1 = m.word("LLRRLLLR")
    assert m.invariants((M1[0] - 1, M1[1], M1[2], M1[3] - 1)) == (1, 27) and m.invariants((M1[0] + 1, M1[1], M1[2], M1[3] + 1)) == (1, 31)
    assert abs(m.apex_in_the_golden_sea(8) - mp.mpf("1.617974")) < mp.mpf("0.0000006") and abs(m.apex_in_the_golden_sea(9) - mp.mpf("1.618057")) < mp.mpf("0.0000006")
    assert abs(m.apex_in_the_golden_sea(0) - (2 + (mp.sqrt(5) - 1) / 2 + 1 / (2 + (mp.sqrt(5) - 1) / 2)) / 2) < mp.mpf(10) ** -30


def test_the_reversal_in_integers_and_the_bundles_as_committed():
    g = (1, 0, 6, -1)
    assert g[0] * g[3] - g[1] * g[2] == -1 and m.mul(g, g) == m.I2 and tuple(x % 5 for x in m.by_rows((1, 3), g)) == (4, 2)
    assert all(m.mul(m.mul(g, m.word("LLLLLLR" + "LR" * k)), g) == m.inv(m.word("LLLLLLR" + "LR" * k)) for k in range(1, 9))
    F, I = RES["E"]["facts"], RES["E"]["isometries"]
    assert [round(F["(6), k = %d" % k]["cs"], 5) for k in (1, 2, 3)] == [-0.0736, -0.07519, -0.07552]
    assert all(F["(6), k = %d" % k]["group"] == "Z/2 + Z/2" and F["(6), k = %d" % k]["palindrome"] and not F["(6), k = %d" % k]["own_mirror"] for k in (1, 2, 3))
    assert [n for n, f in F.items() if f["amphicheiral"]] == ["the golden ground, twice"]
    assert all(sum(b for _, b in I["(6), k = %d" % k]) == 2 and all(a for a, _ in I["(6), k = %d" % k]) for k in (1, 2, 3))
    assert not any(b for _, b in I["[5,1,2,2] closed"])
    assert all(any(b for _, b in I[w]) and not any(a and b for a, b in I[w]) for w in ("LLRLRR", "LLLRLRRR"))


def test_the_bundle_of_the_run_of_6_recomputed_where_snappy_is_installed():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("b++LLLLLLRLR")
    G = M.symmetry_group()
    assert int(G.order()) == 4 and str(G) == "Z/2 + Z/2" and not G.is_amphicheiral() and abs(m.half(M.chern_simons()) + 0.0735980) < 1e-6
    iso = m.isometries(M)
    assert len(iso) == 4 and sum(b for _, b in iso) == 2 and all(a for a, _ in iso)


def test_the_arc_says_what_it_does_not_do():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("Nothing of the lane's is adopted", "It verifies none of the lane's spectra, overlaps or counts", "Main cannot tell which words the lane's code runs",
              "The labels depend on the convention", "Why the enumeration is complete", "is not judged here", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1887" and v["claim_one_line"].endswith("0 of 19.") and v["weave_or_thread"].startswith("thread")
    assert "Nothing of the lane's is adopted" in v["claim_one_line"]
