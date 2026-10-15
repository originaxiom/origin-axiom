"""validation of the stage-2 instrument before the seal (excluded orders only); usage: python3 <this> <forms.pkl>"""
import sys, pickle, math, flint, mpmath as mp
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, D)
import tlow2 as T2
P = pickle.load(open(sys.argv[1], "rb"))
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
for word, line, N in (("LLRRRLRLRLRR", (6, 3), 10), ("LLLRLLLRLR", (1, 7), 8)):
    rot, M, rho, kk, height = T2.thread_geometry(word)
    flint.ctx.prec = T2.bits_for(height)
    F = T2.Forms(P).prepare()
    a, b, c, d = M; Pl = 2 * math.acosh((a + d) / 2)
    res = {}
    for f in (15, 20, 30, 45):
        npts = int(Pl * f)
        conf = T2.configuration(F, word, line, N, {"SM": SM}, npts)
        m = T2.masses(conf, F, {"SM": SM}, N, mp)
        res[npts] = {(k, cell): [float(x) for x in v[cell]["s"]] for k, v in m.items() for cell in v if v[cell]}
        print(word, N, line, "rho", round(rho, 2), "height", round(height, 2), "bits", flint.ctx.prec, "rot line", conf["line_in_rotation"], "period", round(Pl, 2), "npts", npts, "closure", f"{max(conf['closure'].values()):.1e}", flush=True)
    ks = sorted(res); ref = res[ks[-1]]
    for n_ in ks[:-1]:
        worst = max(abs(math.log(res[n_][k][i] / ref[k][i])) for k in ref for i in range(3) if ref[k][i] > 0)
        print(f"   Npts {n_}: worst |ln s| change against {ks[-1]}: {worst:.1e}", flush=True)
