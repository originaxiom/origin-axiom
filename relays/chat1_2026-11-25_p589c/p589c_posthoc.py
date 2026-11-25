#!/usr/bin/env python3
"""POST HOC (written after p589c_exact_rows_out.txt was read): is the order-12 electron's m1/m3 at the exact norms
(up to 8.8e-10, against at most 4.5e-15 at the small-cut norm) a lift, or the exact norms' quadrature error? Uses
p589c_exact_rows.py's functions; the same checkout rule. Data-free.

    python3 -B p589c_posthoc.py <a checkout of main at 88a1e9474>

At tau = 3.1i, on every order-12 line (up to sign), the leptons' m1/m3 with the exact twisted norms computed at the
instrument's quadrature (96 x 64 nodes per edge of the cell) and at twice it in each direction (192 x 128), both
horocycles, readings S and S~. Reading rule, stated before the run: if the largest m1/m3 falls by more than a factor
10 at the finer quadrature, the residue is quadrature error and the zero holds at the exact norms; if it changes by
less than a factor 2, it is a lift.
"""
import importlib.util
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rows", HERE / "p589c_exact_rows.py")
RW = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RW)


def main():
    EE, root = RW.load(sys.argv[1])
    B, K = EE.B, EE.K
    tau = complex(0, 3.1)
    G, Lcol, r = RW.at_tau(EE, tau)
    rd = EE.higgs(tau)
    lf, rf = K.SECT["lep"]
    worst = {}
    for nth, ns in ((96, 64), (192, 128)):
        vals = []
        for (a, b) in RW.lines_of_order(12):
            w = float(a) * tau + float(b)
            x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf])
            R = B.residues(x, yy, tau)
            for h in ("L_max", "L_2"):
                Nx, _ = EE.twisted_norms(tau, G["al"], G["be"], G[h], x, yy, R, nth=nth, ns=ns)
                u = {s: (math.sqrt(Nx[s]) * R[s] if Nx.get(s) is not None and Nx[s] > 0 else 0) for s in B.UNITS}
                Mw = B.weighted_M(u)
                for rn, H in rd.items():
                    sv = np.linalg.svd(B.coupling(H, Mw), compute_uv=False)
                    vals.append((float(sv[2] / sv[0]), str(a), str(b), h, rn))
        vals.sort(reverse=True)
        worst[(nth, ns)] = vals[0][0]
        print("quadrature %d x %d: largest lepton m1/m3 %.3e at line (%s, %s), %s, %s; lines above 1e-12: %d of %d"
              % (nth, ns, vals[0][0], vals[0][1], vals[0][2], vals[0][3], vals[0][4],
                 len({(v[1], v[2]) for v in vals if v[0] > 1e-12}), len(RW.lines_of_order(12))), flush=True)
    ratio = worst[(96, 64)] / worst[(192, 128)]
    print("the largest m1/m3 falls by a factor %.2f at the finer quadrature: %s" % (
        ratio, "quadrature error, the zero holds" if ratio > 10 else ("a lift" if ratio < 2 else "undecided")))


if __name__ == "__main__":
    main()
