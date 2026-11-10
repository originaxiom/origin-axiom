"""B1871 -- the run's decisive facts recomputed with this file's own short code; the sealed run says what the findings quote."""
import importlib.util
import itertools
import pathlib

import numpy as np
import pytest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RUN = (HERE / "tick_on_main_run.txt").read_text(encoding="utf-8")


def _primitive(seq):
    return not any(len(seq) % d == 0 and seq == seq[:d] * (len(seq) // d) for d in range(1, len(seq)))


def _cyc(seq):
    return min(seq[s:] + seq[:s] for s in range(len(seq)))


def _compositions(n):
    for cuts in itertools.product((0, 1), repeat=n - 1):
        out, run = [], 1
        for c in cuts:
            if c:
                out.append(run)
                run = 1
            else:
                run += 1
        out.append(run)
        yield tuple(out)


def test_what_exists_under_each_grammar():
    two, tick = [], []
    for n in range(1, 11):
        words = {_cyc("".join(t)) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t}
        two.append(sum(1 for w in words if _primitive(w)))
        tick.append(sum(1 for c in {_cyc(c) for c in _compositions(n) if len(c) % 2 == 1} if _primitive(c)))
    assert two == [0, 1, 2, 3, 6, 9, 18, 30, 56, 99] and tick == [1, 1, 1, 2, 3, 5, 9, 16, 28, 51]
    # the control: counting run sequences without asking for primitivity gives other numbers (the seat's sealed script erred there)
    loose = [len({_cyc(c) for c in _compositions(n) if len(c) % 2 == 1}) for n in range(1, 7)]
    assert loose != tick[:6]


def test_the_exchange_at_the_levels_and_the_tick_on_the_line():
    def mul(A, B, N):
        return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N, (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)

    def order(gens, N):
        one = (1 % N, 0, 0, 1 % N)
        seen, fr = {one}, [one]
        while fr:
            nx = []
            for a in fr:
                for g in gens:
                    x = mul(a, tuple(v % N for v in g), N)
                    if x not in seen:
                        seen.add(x)
                        nx.append(x)
            fr = nx
        return len(seen)
    L, R, P = (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 0)
    assert [(order([L, R], N), order([L, P], N)) for N in (2, 3, 4, 5, 7, 8)] == [(6, 6), (24, 48), (48, 96), (120, 240), (336, 672), (384, 768)]
    F = (1, 1, 1, 0)                                              # the tick
    assert mul(F, F, 10 ** 6) == mul(L, R, 10 ** 6)
    v, orbit = (1, 2), []
    for _ in range(4):
        v = ((F[0] * v[0] + F[1] * v[1]) % 5, (F[2] * v[0] + F[3] * v[1]) % 5)
        orbit.append(v)
    assert orbit == [(3, 1), (4, 3), (2, 4), (1, 2)]              # multiplication by 3: a line goes to its twin
    assert abs((F[0] - 1) * (F[3] - 1) - F[1] * F[2]) == 1 and abs((F[0] + 1) * (F[3] + 1) - F[1] * F[2]) == 1
    disc = lambda M: (M[0] - M[3]) ** 2 + 4 * M[1] * M[2]
    assert [disc(M) for M in (L, R, P, F)] == [0, 0, 4, 5]        # 5 is not a square: the tick's fixed direction is irrational


def test_the_tick_joins_the_triplet_to_its_conjugate():
    spec = importlib.util.spec_from_file_location("hands_for_b1871_test", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
    H = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(H)
    L, R, P = H.W.ML, H.W.MR, H.W.MP
    T, Tc = H.PIECES["T"], H.PIECES["Tbar"]
    proj = lambda B: B @ np.linalg.pinv(B)
    into = lambda M, a, b: np.allclose(proj(b) @ (M @ a), M @ a, atol=1e-9)
    assert into(L, T, T) and into(R, T, T) and into(P, T, Tc) and into(P, Tc, T) and not into(P, T, T)

    def commutant(gens):
        n = gens[0].shape[0]
        rows = [np.kron(np.eye(n), g) - np.kron(g.T, np.eye(n)) for g in gens]
        return int(np.sum(np.linalg.svd(np.vstack(rows), compute_uv=False) < 1e-8))
    assert commutant([L, R]) == 2 and commutant([L, P]) == 1       # two pieces under the two acts; one piece with the exchange
    assert commutant([L]) > 2                                      # the control: one move alone leaves more


def test_against_the_manifolds():
    snappy = pytest.importorskip("snappy")
    g = snappy.Manifold("b-+L")
    assert g.is_isometric_to(snappy.Manifold("m000")) and not g.is_orientable()
    assert g.orientation_cover().is_isometric_to(snappy.Manifold("m004"))
    for runs, cover in (((2,), "LLRR"), ((3,), "LLLRRR"), ((1, 1, 2), "LRLLRLRR")):
        wd = "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs))
        M = snappy.Manifold("b-+" + wd)
        assert not M.is_orientable() and M.orientation_cover().is_isometric_to(snappy.Manifold("b++" + cover)), runs
    assert snappy.Manifold("b++LLRR").symmetry_group().is_amphicheiral() and not snappy.Manifold("b++LLR").symmetry_group().is_amphicheiral()


def test_the_sealed_run_and_the_findings_agree():
    for s in ("two-act histories:                       0 1 2 3 6 9 18 30 56 99 186 335",
              "added by the tick (an odd number of runs): 1 1 1 2 3 5 9 16 28 51 93 170",
              "its own mirror: 11 -- 5 by a rotation with the swap", "58 histories in 29 pairs",
              "5: 120, 240, no", "(1,2) -> (3,1) -> (4,3) -> (2,4) -> (1,2)",
              "with the exchange: 192 elements, commutant of dimension 1 (one piece)"):
        assert s in RUN, s
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "Nothing in the grammar forbids the tick, and nothing forces it", "Three debts", "is relayed"):
        assert s in f, s
