#!/usr/bin/env python3
"""W20: THE WEAVE'S COUNT IN E6. The 27 carried by the weave's own SL(2), counted by the weave's Euler characteristic.

The rule is W20_RULE.md's, committed before this ran (ed43731d):
  - the weave's group G = Aut+(F2), every thread's group inside it (W19); the moves act on the two records through
    SL(2, Z) in its standard representation H, and the fibre's own group acts trivially there;
  - E6 from the common point (F-MC), one 27 per generation, and an SL(2) in E6 to carry H into E6;
  - the count -chi(G; 27) = h1 - h0 - h2.
The census is every nilpotent orbit of E6 (every SL(2) in E6 up to conjugacy, 21), with the 78 and the 27-bar as
controls and the SU(5) frame through its principal SL(2).

Two routes to h1(SL(2, Z); Sym^k):
  (A) the amalgam SL(2, Z) = Z/4 *_{Z/2} Z/6: h1 = dim V^(-I) - dim V^S - dim V^U + dim V^G (S of order 4, U of order 6);
  (B) Eichler-Shimura: h1(Sym^k) = dim M_{k+2} + dim S_{k+2} for even k >= 2, zero for odd k and for k = 0.
The fibre: H^*(G; V) = H^*(SL(2, Z); V) + H^{*-1}(SL(2, Z); H (x) V), so chi(G; V) = chi(V) - chi(H (x) V).
The orbits' h: 2 rho-check of the Levi for the Levi-type orbits; for D4(a1), D5(a1), E6(a1) and E6(a3) their weighted
diagrams (the last two found as the even diagrams with dim g0 = dim g2). Each orbit's dimension, 78 - dim g0 - dim g1,
is checked against E6's known list.

    python3 the_weaves_count_in_e6.py   ->  the_weaves_count_in_e6.json beside it
"""
import json
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent

# E6, Bourbaki: the chain 1-3-4-5-6 with 2 attached to 4
A = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0], [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1],
     [0, 0, 0, 0, -1, 2]]
N = 6


def positive_roots():
    """in simple-root coordinates, by adding simple roots along strings (simply laced)"""
    simple = [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
    roots, frontier = set(simple), list(simple)
    while frontier:
        new = []
        for r in frontier:
            for j in range(N):
                # <r, alpha_j-check> = sum_i r_i A[i][j]; r + alpha_j is a root iff that is -1 (simply laced, r != alpha_j)
                if sum(r[i] * A[i][j] for i in range(N)) == -1:
                    s = tuple(r[i] + (1 if i == j else 0) for i in range(N))
                    if s not in roots:
                        roots.add(s)
                        new.append(s)
        frontier = new
    return sorted(roots, key=lambda r: (sum(r), r))


def minuscule_weights(top):
    """the weights (Dynkin labels) of a minuscule representation, from its highest weight"""
    seen, frontier = {tuple(top)}, [tuple(top)]
    while frontier:
        new = []
        for mu in frontier:
            for i in range(N):
                if mu[i] > 0:
                    nu = tuple(mu[k] - A[i][k] for k in range(N))
                    if nu not in seen:
                        seen.add(nu)
                        new.append(nu)
        frontier = new
    return sorted(seen)


def solve(M, b):
    """exact solution of M x = b"""
    n = len(M)
    aug = [[Fraction(M[i][j]) for j in range(n)] + [Fraction(b[i])] for i in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if aug[r][c] != 0)
        aug[c], aug[piv] = aug[piv], aug[c]
        aug[c] = [x / aug[c][c] for x in aug[c]]
        for r in range(n):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
    return [aug[i][n] for i in range(n)]


POS = positive_roots()
ROOTS = POS + [tuple(-x for x in r) for r in POS]
W27 = minuscule_weights([1, 0, 0, 0, 0, 0])
W27BAR = minuscule_weights([0, 0, 0, 0, 0, 1])


def h_levi(S):
    """2 rho-check of the Levi on the simple roots S, in simple-coroot coordinates (simply laced)"""
    c = [0] * N
    for r in POS:
        if all(r[i] == 0 for i in range(N) if i not in S):
            c = [c[i] + r[i] for i in range(N)]
    return [Fraction(x) for x in c]


def h_diagram(S, labels):
    """the h in the Cartan of the Levi on S with alpha_j(h) = labels[j] for j in S"""
    S = sorted(S)
    sub = [[A[i][j] for j in S] for i in S]
    cs = solve(sub, [labels[j] for j in S])
    c = [Fraction(0)] * N
    for k, i in enumerate(S):
        c[i] = cs[k]
    return c


def alpha_of(c):
    """alpha_j(h) for the simple roots"""
    return [sum(c[i] * A[i][j] for i in range(N)) for j in range(N)]


def root_values(c):
    d = alpha_of(c)
    return [sum(r[j] * d[j] for j in range(N)) for r in ROOTS]


def weight_values(c, weights):
    return [sum(c[i] * mu[i] for i in range(N)) for mu in weights]


def decompose(values):
    """the SL(2)-decomposition {k: multiplicity of Sym^k} from the multiset of h-eigenvalues"""
    vals = [int(v) for v in values]
    assert all(Fraction(v) == x for v, x in zip(vals, values)), "h has a non-integral eigenvalue"
    mult = {}
    for v in vals:
        mult[v] = mult.get(v, 0) + 1
    out = {}
    for k in sorted({v for v in vals if v >= 0}):
        m = mult.get(k, 0) - mult.get(k + 2, 0)
        assert m >= 0
        if m:
            out[k] = m
    assert sum((k + 1) * m for k, m in out.items()) == len(vals)
    return out


def orbit_dim(c):
    vals = root_values(c)
    g0 = N + sum(1 for v in vals if v == 0)
    g1 = sum(1 for v in vals if v == 1)
    return 78 - g0 - g1


# ---- SL(2, Z): h0 and h1 with coefficients in Sym^k, two routes
def inv_count(k, order):
    """dim of the invariants of an element whose eigenvalues on C^2 are e^(+-2 pi i / order), on Sym^k"""
    return sum(1 for j in range(k + 1) if (k - 2 * j) % order == 0)


def h_route_a(k):
    h0 = 1 if k == 0 else 0
    if k % 2:
        return h0, 0                                        # -I acts by -1
    h1 = (k + 1) - inv_count(k, 4) - inv_count(k, 6) + h0  # dim V^(-I) = k + 1 for even k
    return h0, h1


def dim_m(w):
    if w < 0 or w % 2:
        return 0
    return w // 12 if w % 12 == 2 else w // 12 + 1


def dim_s(w):
    return max(dim_m(w) - 1, 0) if w >= 4 else 0


def h_route_b(k):
    if k == 0:
        return 1, 0
    if k % 2:
        return 0, 0
    return 0, dim_m(k + 2) + dim_s(k + 2)


def chi_sl2(k, route):
    h0, h1 = (h_route_a if route == "A" else h_route_b)(k)
    return h0 - h1


def chi_weave(dec, route):
    """chi(G; V) = chi(SL2Z; V) - chi(SL2Z; H (x) V), H (x) Sym^k = Sym^(k+1) + Sym^(k-1)"""
    tot = 0
    for k, m in dec.items():
        fib = chi_sl2(k + 1, route) + (chi_sl2(k - 1, route) if k >= 1 else 0)
        tot += m * (chi_sl2(k, route) - fib)
    return tot


# ---- the 21 orbits
LEVI = {"0": [], "A1": [0], "2A1": [0, 5], "3A1": [0, 1, 5], "A2": [0, 2], "A2+A1": [0, 2, 5], "2A2": [0, 2, 4, 5],
        "A2+2A1": [0, 2, 1, 5], "A3": [0, 2, 3], "2A2+A1": [0, 2, 4, 5, 1], "A3+A1": [0, 2, 3, 5], "A4": [0, 2, 3, 4],
        "D4": [1, 2, 3, 4], "A4+A1": [0, 1, 3, 4, 5], "A5": [0, 2, 3, 4, 5], "D5": [0, 1, 2, 3, 4], "E6": list(range(6))}
KNOWN_DIM = {"0": 0, "A1": 22, "2A1": 32, "3A1": 40, "A2": 42, "A2+A1": 46, "2A2": 48, "A2+2A1": 50, "A3": 52,
             "2A2+A1": 54, "A3+A1": 56, "D4(a1)": 58, "A4": 60, "D4": 60, "A4+A1": 62, "A5": 64, "D5(a1)": 64,
             "E6(a3)": 66, "D5": 68, "E6(a1)": 70, "E6": 72}


def orbits():
    hs = {name: h_levi(S) for name, S in LEVI.items()}
    # D4(a1): 2 on the outer nodes of the Levi D4 (nodes 2, 3, 5 in Bourbaki), 0 on the trivalent node 4
    hs["D4(a1)"] = h_diagram([1, 2, 3, 4], {1: 2, 2: 2, 3: 0, 4: 2})
    # D5(a1): partition [7, 3] of so(10), 0 on the trivalent node, 2 elsewhere (Levi D5 on Bourbaki nodes 1..5)
    hs["D5(a1)"] = h_diagram([0, 1, 2, 3, 4], {0: 2, 1: 2, 2: 2, 3: 0, 4: 2})
    # the distinguished even orbits: the diagrams with labels in {0, 2} and dim g0 = dim g2
    dist = []
    for d in product((0, 2), repeat=N):
        c = h_diagram(list(range(N)), dict(enumerate(d)))
        vals = root_values(c)
        if N + vals.count(0) == vals.count(2):
            dist.append((orbit_dim(c), d, c))
    dist.sort()
    assert [x[0] for x in dist] == [66, 70, 72], [x[:2] for x in dist]
    hs["E6(a3)"], hs["E6(a1)"] = dist[0][2], dist[1][2]
    assert hs["E6"] == dist[2][2]
    return hs, {"E6(a3)": list(dist[0][1]), "E6(a1)": list(dist[1][1]), "E6": list(dist[2][1])}


def main():
    assert len(POS) == 36 and len(W27) == 27 and len(W27BAR) == 27
    hs, dist_diagrams = orbits()
    rows = {}
    for name, c in hs.items():
        dim = orbit_dim(c)
        d27 = decompose(weight_values(c, W27))
        d27b = decompose(weight_values(c, W27BAR))
        d78 = decompose(root_values(c) + [0] * N)
        row = {"orbit dimension": dim, "the known dimension": KNOWN_DIM[name],
               "weighted diagram": [int(x) for x in alpha_of(c)],
               "27 = (k: multiplicity of Sym^k)": {str(k): m for k, m in d27.items()},
               "27-bar the same": d27b == d27,
               "78 = (k: multiplicity)": {str(k): m for k, m in d78.items()}}
        for route in ("A", "B"):
            row[f"-chi(G; 27), route {route}"] = -chi_weave(d27, route)
            row[f"-chi(G; 78), route {route}"] = -chi_weave(d78, route)
        rows[name] = row
    # the routes agree on every Sym^k used, and further
    routes_agree = all(h_route_a(k) == h_route_b(k) for k in range(0, 61))
    su5 = {"5": {4: 1}, "10": {6: 1, 2: 1}}
    su5_counts = {rep: {r: -chi_weave(dec, r) for r in ("A", "B")} for rep, dec in su5.items()}
    count27 = {name: r["-chi(G; 27), route A"] for name, r in rows.items()}
    out = {"rule": "W20_RULE.md (ed43731d)",
           "the orbits' dimensions match E6's list": all(r["orbit dimension"] == r["the known dimension"] for r in rows.values()),
           "the two routes agree for every k to 60": routes_agree,
           "the routes agree on every orbit": all(r["-chi(G; 27), route A"] == r["-chi(G; 27), route B"]
                                                  and r["-chi(G; 78), route A"] == r["-chi(G; 78), route B"]
                                                  for r in rows.values()),
           "the distinguished even diagrams (Bourbaki order)": dist_diagrams,
           "h1(SL(2, Z); Sym^k), k = 0..24": {k: h_route_a(k)[1] for k in range(0, 25)},
           "-chi(G; 27) by orbit": count27,
           "orbits with -chi(G; 27) = 3": sorted(n for n, v in count27.items() if v == 3),
           "the principal orbit's count": count27["E6"],
           "the SU(5) frame's principal counts (5, 10)": su5_counts,
           "rows": rows}
    return out


if __name__ == "__main__":
    res = main()
    with open(HERE / "the_weaves_count_in_e6.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    for k in ("the orbits' dimensions match E6's list", "the two routes agree for every k to 60",
              "the routes agree on every orbit", "-chi(G; 27) by orbit", "orbits with -chi(G; 27) = 3",
              "the SU(5) frame's principal counts (5, 10)"):
        print(k, ":", json.dumps(res[k]))
