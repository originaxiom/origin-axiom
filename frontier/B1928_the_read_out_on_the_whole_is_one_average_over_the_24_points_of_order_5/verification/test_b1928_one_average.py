"""The lock of B1928. Each test recomputes something, with a planted case that must fail.

1. SL(2, F_5) is perfect (its commutators generate it) and acts transitively on the 24 points of order 5: the two group
   facts the proof uses. Planted: the Borel subgroup is not perfect.
2. F-bar recomputed at two grid points equals the stored grid (a stored number moved by 1e-6 is caught).
3. P2 recomputed from the stored ergodic integral and B1924's stored read-outs: the median |z| at n = 28, the twin, is
   below 1; planted: the integral moved by three of its errors plus B1924's is caught (median above 2)."""
import itertools, json, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def sl2_f5():
    return [((a, b), (c, d)) for a, b, c, d in itertools.product(range(5), repeat=4) if (a * d - b * c) % 5 == 1]


def mul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) % 5 for j in range(2)) for i in range(2))


def inv(X):
    (a, b), (c, d) = X
    return ((d % 5, -b % 5), (-c % 5, a % 5))


def generated(gens):
    I = ((1, 0), (0, 1)); S = {I}; frontier = [I]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in S:
                    S.add(y); new.append(y)
        frontier = new
    return S


def test_group_facts():
    G = sl2_f5(); assert len(G) == 120
    comms = {mul(mul(x, y), mul(inv(x), inv(y))) for x in G for y in G}
    assert len(generated(list(comms))) == 120
    L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
    assert len(generated([L, R])) == 120
    orbit = {(1, 2)}; frontier = [(1, 2)]
    while frontier:
        new = []
        for v in frontier:
            for g in (L, R):
                w = ((g[0][0] * v[0] + g[0][1] * v[1]) % 5, (g[1][0] * v[0] + g[1][1] * v[1]) % 5)
                if w not in orbit:
                    orbit.add(w); new.append(w)
        frontier = new
    assert len(orbit) == 24
    borel = [g for g in G if g[1][0] == 0]
    bcomms = {mul(mul(x, y), mul(inv(x), inv(y))) for x in borel for y in borel}
    assert len(generated(list(bcomms))) < len(borel)          # planted: not perfect


def test_fbar_recomputed():
    import fiber_grid as FG
    grid = json.loads((HERE / "fiber_grid_fine.json").read_text())
    for g in (grid[5], grid[400]):
        d = FG.fbar(complex(*g["tau"]))
        dev = max(float(np.max(np.abs(np.array(d[m][k]) - np.array(g["F"][m][k])))) for m in d for k in d[m])
        assert dev < 1e-9
        planted = {m: {k: list(v) for k, v in g["F"][m].items()} for m in g["F"]}
        k0 = next(iter(planted["const"])); planted["const"][k0][0] += 1e-6
        dev2 = max(float(np.max(np.abs(np.array(d[m][k]) - np.array(planted[m][k])))) for m in d for k in d[m])
        assert dev2 > 1e-7


def test_p2_recomputed():
    E = json.loads((HERE / "fiber_ergodic_fine.json").read_text())["const"]
    ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    D = json.loads((next((ROOT / "frontier").glob("B1924_*")) / "verification" / "whole_average_4.json").read_text())["28 twin"]
    keys = list(E["R"].keys())
    flat = lambda d: np.concatenate([np.array(d[k]) for k in keys])
    Rb, sb, R, s = flat(E["R"]), flat(E["se"]), flat(D["R"]), flat(D["se"])
    z = np.abs(R - Rb) / np.sqrt(s ** 2 + sb ** 2)
    assert np.median(z) < 1.0
    zp = np.abs(R - (Rb + 3 * np.sqrt(s ** 2 + sb ** 2))) / np.sqrt(s ** 2 + sb ** 2)
    assert np.median(zp) > 2.0
