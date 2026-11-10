"""B1866 -- the scrutiny's computations reproduce, and its decisive facts are recomputed here, not read from the transcript."""
import cmath
import importlib.util
import math
import pathlib
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _run():
    return subprocess.run([sys.executable, "-B", str(HERE / "join_scrutiny.py")], capture_output=True, text=True, check=True, timeout=900).stdout


def test_the_scrutiny_reproduces():
    out = _run()
    assert out == (HERE / "join_scrutiny_run.txt").read_text(encoding="utf-8")       # integers and eighth roots only: no float is compared as text
    for s in ("orbits: [((0, 0),), ((0, 1), (1, 0), (1, 1))]", "the same pair: True", "that pair under the moves: 3 pairs",
              "a group of order 96; its scalars: 4", "with element orders [(1, 1), (2, 9), (3, 8), (4, 6)]",
              "equivalent to T at m = [15]; to conj T at m = [21]", "over the even twists the orders are [24, 48, 72, 144]: never 96",
              "M_L = [e(+1/8) 0 0; 0 0 e(-1/8); 0 e(-1/8) 0], M_R = [0 e(+1/8) 0; e(+1/8) 0 0; 0 0 e(-1/8)]",
              "psi = (-1, +1): a group of order 24, modulo scalars 24; equivalent to T after a twist chi_m for m = [9]",
              "psi = (+1, -1): a group of order 6, modulo scalars 6; equivalent to T after a twist chi_m for m = []"):
        assert s in out, s


def _triplet():
    spec = importlib.util.spec_from_file_location("hands_for_b1866", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
    H = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(H)
    TB = H.PIECES["T"]
    return TB.conj().T @ H.W.ML @ TB, TB.conj().T @ H.W.MR @ TB


def _group(gens, n):
    key = lambda M: tuple(np.round(M.flatten(), 7).view(float))
    I = np.eye(n, dtype=complex)
    seen = {key(I): I}
    fr = [I]
    while fr:
        nx = []
        for a in fr:
            for g in gens:
                x = a @ g
                if key(x) not in seen:
                    seen[key(x)] = x
                    nx.append(x)
                    assert len(seen) < 5000
        fr = nx
    return list(seen.values())


def test_the_triplet_is_the_odd_twist_and_no_even_one():
    """recomputed with this file's own short code: the group, S^4 = -1, and the twist census by characters"""
    TL, TR = _triplet()
    G = _group([TL, TR], 3)
    assert len(G) == 96
    S = TL @ np.linalg.inv(TR) @ TL
    assert np.abs(np.linalg.matrix_power(S, 4) + np.eye(3)).max() < 1e-10
    Hd = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    DL, DR = np.diag([1, 1j]), Hd @ np.diag([1, -1j]) @ Hd

    def sym2(M):
        a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        r = math.sqrt(2)
        return np.array([[a * a, r * a * b, b * b], [r * a * c, a * d + b * c, r * b * d], [c * c, r * c * d, d * d]])
    z = cmath.exp(2j * math.pi / 24)
    # a class function test without the group of pairs: compare traces on every word of length at most 7 in L, R and their inverses
    import itertools
    def words(AL, AR):
        gens = [AL, AR, np.linalg.inv(AL), np.linalg.inv(AR)]
        out = []
        for n in range(1, 8):
            for w in itertools.product(range(4), repeat=n):
                M = np.eye(3, dtype=complex)
                for k in w:
                    M = M @ gens[k]
                out.append(np.trace(M))
        return np.array(out)
    wT = words(TL, TR)
    hits = [m for m in range(24) if np.abs(words(z ** m * sym2(DL), z ** (-m) * sym2(DR)) - wT).max() < 1e-8]
    assert hits == [15]
    assert all(len(_group([z ** m * sym2(DL), z ** (-m) * sym2(DR)], 3)) != 96 for m in range(0, 24, 2))


def test_mains_exploratory_note_is_withdrawn_where_it_stood():
    src = (ROOT / "frontier" / "B1861_the_closure_programme" / "verification" / "programme_source.py").read_text(encoding="utf-8")
    assert "WITHDRAWN (B1866)" in src and "A first exploratory reading: of the two coherent lifts" not in src
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    assert "The sentence is withdrawn" in f and "is the odd character χ₉ physical" in f
