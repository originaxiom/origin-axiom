#!/usr/bin/env python3
"""The class index of the triplets R (x) chi at the boundary-parabolic point of the branch.  R is a representation
into SL(3) and is not self-dual, so the vanishing seen for self-dual modules (B1329-B1332, B1446) is not expected
on any general ground here."""
import sys, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
for _d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves", "B1446_the_parabolic_points_and_the_branch_points"):
    sys.path.insert(0, str(HERE.parents[1] / _d / "verification"))
sys.path.insert(0, str(HERE))
import index_num as ix
import branch_obstruction as bo, branch_parabolic as bp, branch_follow as bf
from mpmath import mp, mpf, mpc, matrix, nstr, exp, pi, inverse, eye, zeros, norm
mp.dps = 60
d = json.load(open(HERE / "parabolic_point.json"))["matrices"]
R = {g: matrix([[mpc(mpf(e[0]), mpf(e[1])) for e in row] for row in d[name]]) for g, name in ((1, "x"), (2, "y"), (3, "t"))}
c1, c2, c3 = bp.coeffs(R[3]); t0 = c1 / 3; Tn = R[3] / t0; z4 = exp(2j * pi / 4); Phi = bo.Phi; out = []
def same_as_dual(h, T):
    """is the module isomorphic to its dual?  solve  X h(g) = h*(g) X  for X; non-zero solution space <=> isomorphic (irreducible case)"""
    hd, Td = ix.dual(h, T); rows = []
    for A, B in ((h[1], hd[1]), (h[2], hd[2]), (T, Td)):
        for i in range(3):
            for j in range(3):
                row = [mpc(0)] * 9
                for a in range(3):
                    for b in range(3):
                        if a == i: row[3 * a + b] += A[b, j]
                        if b == j: row[3 * a + b] -= B[i, a]
                rows.append(row)
    return ix.nullity(matrix(rows))[0]
for (i, j) in itertools.product(range(4), repeat=2):
    h = {1: z4 ** i * R[1], 2: z4 ** j * R[2]}
    try:
        I, a, b = ix.index(Phi, h, Tn); iso = same_as_dual(h, Tn)
        rec = dict(chi=[i, j], index=I, V=dict(h0=a["h0"], t0=a["t0"], h1=a["h1"], interior=a["interior"]), Vdual=dict(h0=b["h0"], t0=b["t0"], h1=b["h1"], interior=b["interior"]),
                   smallest_kept=nstr(a["gaps"][1][0], 4), largest_dropped=nstr(a["gaps"][1][1], 4), isomorphic_to_its_dual=bool(iso))
    except AssertionError as ex: rec = dict(chi=[i, j], error=str(ex)[:80])
    out.append(rec); print(rec, flush=True)
json.dump(out, open(HERE / "triplet_index.json", "w"), indent=1)
