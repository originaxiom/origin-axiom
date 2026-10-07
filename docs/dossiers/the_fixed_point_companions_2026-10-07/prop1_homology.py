#!/usr/bin/env python3
"""Proposition 1's description checked on H_1 (structure only): the companion N is the mapping torus of the lift of phi on
T' = R^2/(phi - I)Z^2 punctured at its |T| lattice points, which (phi - I)^-1 carries to (T^2 - Fix phi, phi). On every
generated state with at most 12 ends, from sm:B1538's cover code:
  - f_* on H_1(fibre) = Z^(|T|+1), in a basis (e_i, e_j, l_0, ..., l_(|T|-2)) adapted to the punctures: [[phi', 0], [C, I]];
  - the Smith form of f_* - 1 as it is (puncture corrections C included), and with C set to zero.
H_1(N) = Z + coker(f_* - 1). Main's remark of 2026-10-07 (torsion |det(phi - I)| in H_1) is the second column.

    python3 prop1_homology.py   ->  prop1_homology.json beside this file"""
import importlib.util
import itertools
import json
import sys
from pathlib import Path

from sympy import Matrix, ZZ, eye, zeros
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1538V = ROOT / "frontier" / "B1538_the_puncture_characters" / "verification"
spec = importlib.util.spec_from_file_location("punct_covers", B1538V / "punct_covers.py")
if str(B1538V) not in sys.path:
    sys.path.append(str(B1538V))
PC = importlib.util.module_from_spec(spec)
sys.modules["punct_covers"] = PC
spec.loader.exec_module(PC)


def states(nmax=8, dmax=12):
    def canon(w):
        sw = w.translate(str.maketrans("LR", "RL"))
        return min([w[i:] + w[:i] for i in range(len(w))] + [sw[i:] + sw[:i] for i in range(len(sw))])
    out = set()
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" in w and "R" in w and all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0):
                out.add(canon(w))
    res = []
    for w in sorted(out, key=lambda x: (len(x), x)):
        for sign in "+-":
            (a, b), (c, d_) = PC.State(sign + w).M
            if abs(2 - (a + d_)) <= dmax:
                res.append((sign + w, abs(2 - (a + d_))))
    return res


def companion(st, d):
    (a, b), (c, e) = st.M
    lats = [L for L in PC.lattices(st.M, d, d) if all(PC.in_lattice(L, v) for v in [(a - 1, c), (b, e - 1)])]
    hits = [C for C in (PC.Cover(st, lats[0], wl) for wl in range(d)) if len(C.cusps) == d]
    return hits[0]


def diag(S):
    return [int(S[k, k]) for k in range(min(S.shape))]


def main():
    rows = []
    for sw, d in states():
        C = companion(PC.State(sw), d)
        n = C.n
        F = Matrix(C.fstar)
        ells = [Matrix(v) for v in C.ell[:-1]] if d > 1 else []
        # complete the puncture span to a basis of Z^n with unit vectors
        basis = None
        for comb in itertools.combinations(range(n), n - len(ells)):
            B = Matrix.hstack(*([eye(n)[:, i] for i in comb] + ells)) if ells else eye(n)
            if abs(B.det()) == 1:
                basis = B
                break
        G = basis.inv() * F * basis
        k = n - len(ells)
        corr = G[k:, :k] if ells else zeros(0, 0)
        G0 = G.copy()
        if ells:
            G0[k:, :k] = zeros(len(ells), k)
        true_s = diag(smith_normal_form(G - eye(n), domain=ZZ))
        drop_s = diag(smith_normal_form(G0 - eye(n), domain=ZZ))
        rows.append({"state": sw, "ends": d, "fibre H1 rank": n, "upper-right block zero": G[:k, k:].is_zero_matrix if ells else True,
                     "corrections nonzero": (not corr.is_zero_matrix) if ells else False,
                     "torsion of coker(f_* - 1)": [x for x in true_s if x not in (0, 1)],
                     "torsion with the corrections dropped": [x for x in drop_s if x not in (0, 1)]})
        print(sw, d, rows[-1]["torsion of coker(f_* - 1)"], rows[-1]["torsion with the corrections dropped"], flush=True)
    out = {"rows": rows,
           "H1 free on every companion": all(not r["torsion of coker(f_* - 1)"] for r in rows),
           "torsion appears when the corrections are dropped (ends > 1)": all(r["torsion with the corrections dropped"] for r in rows if r["ends"] > 1)}
    (HERE / "prop1_homology.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}))


if __name__ == "__main__":
    main()
