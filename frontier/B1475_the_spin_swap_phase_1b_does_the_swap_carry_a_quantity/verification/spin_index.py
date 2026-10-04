#!/usr/bin/env python3
"""B1475 C4: the class index (B1297/B1446 index_num) of the geometric rank-two lift twisted by every sign character, on the
once-punctured-torus bundles main's fibred instruments reach: m003 (-LR, level 1), m004 (+LR, level 1), t12839 (+LR, level 4).
Sign characters = fibre characters (a, b) with z^a, z^b in {+-1} (needs 2 | N) and the meridian sign lambda = +-1.
Built on B1465's draft (main's own route to the mirror-broken states), with V = rho itself instead of rho (x) conj(rho)."""
import sys, json, pathlib, glob, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = next((p for p in HERE.parents if p.name == "frontier"), pathlib.Path.cwd() / "frontier")
for d in ("B1444_*", "B1445_*", "B1446_*", "B1451_*"):
    sys.path.insert(0, glob.glob(str(FRONTIER / d / "verification"))[0])
import curve_engine as ce, mass_term as mt, index_num as ix, complete_points as cp
from mpmath import mp, mpc, mpf, exp, pi, nstr
mp.dps = 60


def run(state, k):
    L = mt.Level(state, k); P = cp.Points(L); z = exp(2j * pi / L.N)
    out = dict(state=state, k=k, N=L.N, points=[])
    sign_chars = [(a, b) for (a, b) in L.chars if abs(z ** a - round(float((z ** a).real))) < 1e-30 and abs(z ** b - round(float((z ** b).real))) < 1e-30]
    out["sign_fibre_characters"] = [list(c) for c in sign_chars]
    for ell in sorted(L.S):
        B, p, g, T, info = P.cusp(ell)
        if B is None or not info.get("reached") or info.get("kind") != "parabolic": continue
        pt = dict(ell=list(ell), tr_T=info["tr_meridian"][:12], rows=[])
        for (a, b) in sign_chars:
            for lam in (1, -1):
                h = {1: (z ** a) * g[1], 2: (z ** b) * g[2]}; Tm = mpc(lam) * T
                try:
                    I, A, Bm = ix.index(L.Phi, h, Tm)
                    pt["rows"].append(dict(chi=[a, b], lam=lam, I=int(I), h1=A["h1"], h1_dual=Bm["h1"], gap=(nstr(A["gaps"][1][0], 4), nstr(A["gaps"][1][1], 4))))
                except AssertionError as ex:
                    pt["rows"].append(dict(chi=[a, b], lam=lam, error=str(ex)[:80]))
        out["points"].append(pt); print(state, k, "ell", ell, [(r.get("chi"), r.get("lam"), r.get("I", r.get("error"))) for r in pt["rows"]], flush=True)
    return out


if __name__ == "__main__":
    jobs = [("-LR", 1), ("+LR", 1), ("+LR", 4)]
    res = [run(s, k) for s, k in jobs]
    json.dump(res, open(HERE / "spin_index.json", "w"), indent=1, default=str)
