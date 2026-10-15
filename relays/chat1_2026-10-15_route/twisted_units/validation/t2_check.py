"""validation of the stage-2 instrument before the seal (excluded orders only); usage: python3 <this> <forms.pkl>"""
import sys, pickle, time, math, numpy as np, flint
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, D)
import tlow2 as T2, tlow as T1, units_cells as UC
P = pickle.load(open(sys.argv[1], "rb"))
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
def tonp(M): return np.array([[complex(float(x.real.mid()), float(x.imag.mid())) for x in row] for row in M])
# (a) against stage 1 (double) on a low thread at an excluded order, both readings
for word, line, N, npts in (("LLRLR", (1, 2), 5, 200), ("LRR", (0, 1), 7, 200)):
    rot, M, rho, kk, height = T2.thread_geometry(word)
    flint.ctx.prec = T2.bits_for(height)
    F = T2.Forms(P).prepare()
    t0 = time.time()
    conf = T2.configuration(F, word, line, N, {"SM": SM}, npts)
    dt = time.time() - t0
    F1 = T1.Forms(P); Tun, w, M1, rot1 = T1.thread_points(word, npts); EU = T1.evaluate_unreduced(F1, Tun)
    worst = 0.0
    for sec, (fl, fr, hh) in T2.SECTORS.items():
        qL, qR = SM[fl], SM[fr]; qH = SM["H"] if hh == "H" else -SM["H"]
        k_pf, k_mn = conf["plan"][("SM", sec)]
        for reading, Y, K in (("per-field", conf["pf"][k_pf], conf["Kpf"]), ("minimal", conf["mn"][k_mn], conf["Kmn"])):
            r1 = T1.integrals(EU, Tun, w, line, N, (qL, qR, qH), reading)
            for key in ("Y1", "Y2x", "Y3x"):
                A = tonp(Y[key]); worst = max(worst, float(np.max(np.abs(r1[key] - A)) / np.max(np.abs(A))))
            KK = K[k_pf[0]] if reading == "per-field" else K
            A = tonp(KK["K32"]); worst = max(worst, float(np.max(np.abs(r1["KL32"] - A)) / np.max(np.abs(A))))
    print(f"(a) {word} N={N} line {line} rho={rho:.2f} bits={flint.ctx.prec}: stage2 vs stage1 worst {worst:.1e}; {dt/npts*1000:.1f} ms/point; closure {max(conf['closure'].values()):.1e}", flush=True)
# (b) against the ball-arithmetic tower instrument (units_cells, forms at the unreduced point directly) where double failed
for n, N, line in ((4, 3, (0, 1)), (5, 5, (1, 2))):
    word = "L" + "R" * n
    rot, M, rho, kk, height = T2.thread_geometry(word)
    flint.ctx.prec = 800
    ref = {rd: UC.configuration(src, n, line, N, SM, 600)["acc"] for rd, src in (("per-field", UC.PerFieldFactoredSource(P)), ("minimal", UC.UntwistedSource(P)))}
    flint.ctx.prec = T2.bits_for(height)
    F = T2.Forms(P).prepare()
    t0 = time.time(); conf = T2.configuration(F, word, line, N, {"SM": SM}, 600); dt = time.time() - t0
    worst = {"per-field": 0.0, "minimal": 0.0}
    for sec in T2.SECTORS:
        k_pf, k_mn = conf["plan"][("SM", sec)]
        for reading, Y in (("per-field", conf["pf"][k_pf]), ("minimal", conf["mn"][k_mn])):
            for key in ("Y1", "Y2x", "Y3x"):
                A = tonp(ref[reading][sec][key]); B_ = tonp(Y[key])
                worst[reading] = max(worst[reading], float(np.max(np.abs(A - B_)) / np.max(np.abs(A))))
    print(f"(b) L R^{n} N={N} line {line} rho={rho:.2f} bits={flint.ctx.prec}: stage2 vs tower instrument {worst}; {dt/600*1000:.1f} ms/point", flush=True)
