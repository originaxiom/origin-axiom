#!/usr/bin/env python3
"""B874 addendum -- the joint measurement from the enhanced point.

At each of the three enhancement points s1 = x8 + t* x16 (t* = 13 x banked cubic roots,
[[b854-pencil normalization]]), measure a second charge: the joint centralizer
ker(ad s1) cap ker(ad x14) and cap ker(ad x22), numerically at 40 digits with
relative-gap certification. Answers the B866 carried-forward step-2 question.
"""
import json
import os

import mpmath
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
CUBIC = [500716339200, -159667200, -28224, 1]


def main():
    mp.dps = 40
    src = open(B854, encoding="utf-8").read()
    g = {"__file__": B854, "__name__": "b854"}
    exec(compile(src, B854, "exec"), g)
    DIM, N = g["DIM"], g["N"]
    br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
    basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
    triples = {}
    for p in range(DIM):
        for q in range(DIM):
            v = br(basis[p], basis[q])
            for r, c in enumerate(v):
                if c:
                    triples.setdefault(p, []).append((q, r, c))

    def admat_num(vec):
        A = mp.zeros(DIM, DIM)
        for p in range(DIM):
            vp = vec[p]
            if abs(vp) < mp.mpf(10) ** (-mp.dps + 8):
                continue
            for q, r, c in triples.get(p, []):
                A[r, q] += vp * mp.mpf(c.numerator) / mp.mpf(c.denominator)
        return A

    def vnum(n):
        return [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g["INV"][n]]

    A8, A14, A16, A22 = (admat_num(vnum(n)) for n in (8, 14, 16, 22))
    roots_t = sorted(13 * mp.re(r) for r in mpmath.polyroots(
        [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))

    def nullity(M):
        U, S, Vt = mpmath.svd_r(M)
        smax = S[0]
        return sum(1 for i in range(min(M.rows, M.cols))
                   if S[i] < smax * mp.mpf("1e-25"))

    out = []
    for t in roots_t:
        A = A8 + t * A16
        row = dict(t=mp.nstr(t, 20), kern_s1=nullity(A))
        for name, B in (("x14", A14), ("x22", A22)):
            st = mp.matrix(2 * DIM, DIM)
            for i in range(DIM):
                for j in range(DIM):
                    st[i, j] = A[i, j]
                    st[DIM + i, j] = B[i, j]
            row[f"joint_{name}"] = nullity(st)
        out.append(row)
        print(f"  t = {row['t'][:14]}: kern(s1) = {row['kern_s1']}, "
              f"joint x14 = {row['joint_x14']}, joint x22 = {row['joint_x22']}")

    res = dict(rows=out,
               enhancement_confirmed_at_13x=all(r["kern_s1"] == 46 for r in out),
               no_26_stratum=all(r["joint_x14"] == 12 and r["joint_x22"] == 12
                                 for r in out))
    json.dump(res, open(os.path.join(HERE, "joint_results.json"), "w"),
              indent=1, sort_keys=True)
    print(f"  enhancement at 13x roots: {res['enhancement_confirmed_at_13x']}; "
          f"no 26 stratum: {res['no_26_stratum']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
