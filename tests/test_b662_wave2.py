"""B662 wave-2 locks (cells F, G, H) + this seat's independent
re-verification of the decisive cell-F identity (the sigma matrix
maps Y to Ybar, recomputed from the two persisted JSONs alone)."""
import json
import os
from fractions import Fraction as Fr
from itertools import permutations

_C = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B662_successor_campaign")
_S2 = os.path.join(os.path.dirname(__file__), "..", "frontier",
                   "B660_structure_campaign", "packet", "s2_cp",
                   "s2_results.json")


def _kmul(a, b):
    return (a[0] * b[0] - 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def _kadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def test_cell_f_sigma_maps_y_to_ybar_from_jsons_alone():
    M = json.load(open(os.path.join(_C, "cellC",
                                    "sigma_matrix_golden.json")))["matrix"]
    M = [[(Fr(e[0]), Fr(e[1])) for e in row] for row in M]
    Yc = json.load(open(_S2))["Y_components"]
    Y = {}
    for k, v in Yc.items():
        idx = tuple(int(x) for x in k.strip("()").split(","))
        val = (Fr(v[0]), Fr(v[1]))
        if val != (Fr(0), Fr(0)):
            Y[idx] = val

    def yfull(i, j, k):
        srt = tuple(sorted((i, j, k)))
        if len(set((i, j, k))) < 3 or srt not in Y:
            return (Fr(0), Fr(0))
        perm = (i, j, k)
        inv = sum(1 for a in range(3) for b in range(a + 1, 3)
                  if perm[a] > perm[b])
        sign = -1 if inv % 2 else 1
        v = Y[srt]
        return (sign * v[0], sign * v[1])

    for (i, j, k), v in Y.items():
        s = (Fr(0), Fr(0))
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    y = yfull(a, b, c)
                    if y == (Fr(0), Fr(0)):
                        continue
                    coef = _kmul(_kmul(M[i][a], M[j][b]), M[k][c])
                    s = _kadd(s, _kmul(coef, y))
        assert s == (v[0], -v[1]), (i, j, k)   # (g.Y)_ijk = conj(Y)_ijk


def test_cell_f_certificate_flags():
    d = json.load(open(os.path.join(_C, "cellF", "g_certificate.json")))
    assert d["verified_exactly"] is True
    assert d["stabilizer_dim_K"] == 15


def test_cell_g_minimal_period():
    r = json.load(open(os.path.join(_C, "cellG", "l100_results.json")))
    assert r["P_min"] == 175560
    assert r["N0_over_P_min"] == 13167000
    assert r["cancelled_q"] == []          # zero aggregate cancellations
    assert r["P_min_factorization"] == {"2": 3, "3": 1, "5": 1,
                                        "7": 1, "11": 1, "19": 1}


def test_cell_h_fourth_wall_output():
    out = open(os.path.join(_C, "cellH", "cellH_output.txt")).read()
    assert "MATCH: True" in out
    fnd = open(os.path.join(_C, "cellH", "FINDINGS_CELL.md")).read()
    assert "FULL" in fnd and "UNDEFINED" in fnd.upper() or "undefined" in fnd


def test_cell_i_weight5_mechanism_independent():
    """This seat's Molien check: both doublets first appear in
    Sym^n(2hat) at n ≡ 0 mod 5 exactly at n = 25 (weight 5)."""
    import cmath
    import numpy as np
    pi = np.pi
    classes = [(1, 0.0), (1, pi), (30, pi / 2), (20, pi / 3),
               (20, 2 * pi / 3), (12, pi / 5), (12, 2 * pi / 5),
               (12, 3 * pi / 5), (12, 4 * pi / 5)]

    def chi_sym(n, a):
        l, m = cmath.exp(1j * a), cmath.exp(-1j * a)
        if abs(l - m) < 1e-12:
            return (n + 1) * l**n
        return (l**(n + 1) - m**(n + 1)) / (l - m)

    chi2h = [2 * np.cos(a) for _, a in classes]
    chi2hp = list(chi2h)
    chi2hp[5], chi2hp[6], chi2hp[7], chi2hp[8] = (chi2h[7], chi2h[8],
                                                  chi2h[5], chi2h[6])
    for chi in (chi2h, chi2hp):
        n5 = []
        for n in range(0, 26):
            m = sum(sz * chi_sym(n, a) * chi[i]
                    for i, (sz, a) in enumerate(classes)) / 120
            if round(m.real) > 0 and n % 5 == 0:
                n5.append(n)
        assert n5[0] == 25          # weight 5, both doublets
