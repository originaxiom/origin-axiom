#!/usr/bin/env python3
"""B1465 -- main's own route to sm:B1527 Part H on the first mirror-broken word states (R59-1 / L242 (e)).
Written as a draft before any run (sha256 of the draft b22aa96a98fd06fc..., kept in the arc as draft_sha.txt); the population,
the lambda set and the instrument were fixed there; this file differs from the draft only in its paths.
At every kappa = -2 point with parabolic meridian on the periodic curves of a level, V = rho (x) conj(rho) (x) chi with a
meridian twist lambda; I(V) by main's index instrument, for every fibre character chi and a spread of lambda.
B1459 covers lambda = 1 (a theorem); lambda != 1 is the untested half of 'every character'."""
import sys, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
for d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_of_the_frame", "B1446_the_parabolic_points_and_the_branch_points", "B1451_the_complete_points_on_other_levels"):
    import glob
    hits = glob.glob(str(ROOT / "frontier" / (d.split("_")[0] + "_*") / "verification"))
    sys.path.insert(0, hits[0])
import curve_engine as ce, mass_term as mt, index_num as ix, complete_points as cp
from mpmath import mp, mpc, mpf, matrix, exp, pi, nstr, conj
mp.dps = 60

def conj_mat(M): return matrix([[conj(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])

def main(state, k, lams):
    L = mt.Level(state, k); P = cp.Points(L); z = exp(2j * pi / L.N)
    out = dict(state=state, k=k, N=L.N, points=[], rows=0, nonzero=[])
    for ell in (sorted(L.S)[:1] if QUICK else sorted(L.S)):
        B, p, g, T, info = P.cusp(ell)
        if B is None or not info.get("reached") or info.get("kind") != "parabolic": continue
        gb = {1: conj_mat(g[1]), 2: conj_mat(g[2])}; Tb = conj_mat(T)
        pt = dict(ell=list(ell), X=info["X"][:20], tr_T=info["tr_meridian"][:12], rows=[])
        for (a, b) in L.chars:
            ax, ay = z ** a, z ** b          # a fibre character chi = (a, b): the factors' own v-twists cancel in rho (x) conj(rho)? no -- keep the module as built
            h = {1: ax * mt.kron(g[1], gb[1]), 2: ay * mt.kron(g[2], gb[2])}
            for lam in lams:
                Tm = mpc(lam) * mt.kron(T, Tb)
                try:
                    I, A, Bm = ix.index(L.Phi, h, Tm); gap = (nstr(A["gaps"][1][0], 4), nstr(A["gaps"][1][1], 4))
                except AssertionError as ex:
                    pt["rows"].append(dict(chi=[a, b], lam=str(lam), error=str(ex)[:60])); continue
                pt["rows"].append(dict(chi=[a, b], lam=str(lam), I=int(I), gap=gap)); out["rows"] += 1
                if I != 0: out["nonzero"].append(dict(ell=list(ell), chi=[a, b], lam=str(lam), I=int(I), gap=gap))
        out["points"].append(pt); print(state, "ell", ell, "parabolic point, %d rows, nonzero so far %d" % (len(pt["rows"]), len(out["nonzero"])), flush=True)
    return out

QUICK = "--quick" in sys.argv
if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    state = args[0] if args else "+LLRLRR"
    lams = [1, -1, 1j, exp(2j * pi / 3), mpc("0.6", "0.8"), mpc("1.3", "0"), mpc("0.7", "0.4")]
    if QUICK: lams = [1, mpc("1.3", "0")]
    out = main(state, 1, lams)
    json.dump(out, open(HERE / ("points_%s%s.json" % (state.replace("+", "p").replace("-", "m"), "_quick" if QUICK else "")), "w"), indent=1, default=str)
    print("rows", out["rows"], "nonzero", len(out["nonzero"]))
