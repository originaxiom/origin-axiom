"""validation of the stage-2 instrument before the seal (excluded orders only); usage: python3 <this> <forms.pkl>"""
import sys, pickle, numpy as np, flint
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, D)
import tlow2 as T2, units_cells as UC
P = pickle.load(open(sys.argv[1], "rb"))
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
def tonp(M): return np.array([[complex(float(x.real.mid()), float(x.imag.mid())) for x in row] for row in M])
n, N, line = 5, 5, (1, 2)
flint.ctx.prec = 800
ref = UC.configuration(UC.PerFieldFactoredSource(P), n, line, N, SM, 300)["acc"]
rot, M, rho, kk, height = T2.thread_geometry("L" + "R" * n); flint.ctx.prec = T2.bits_for(height)
F = T2.Forms(P).prepare()
conf = T2.configuration(F, "L" + "R" * n, line, N, {"SM": SM}, 300, readings=("per-field",))
la, lb = line
for sec, (fl, fr, hh) in T2.SECTORS.items():
    k_pf, _ = conf["plan"][("SM", sec)]
    qs = (SM[fl], SM[fr], SM["H"] if hh == "H" else -SM["H"])
    # predicted constant: D(q) = exp(4 pi i r lb la k / N)... use W92's rule iteratively: D(q) = e^{4 pi i q' lb la/N} D(q') per step q' -> q' + N
    ph = []
    for q in qs:
        r = q % N; p = 1.0 + 0j; cur = r
        while cur != q:
            if cur < q: p *= np.exp(4j * np.pi * cur * lb * la / N); cur += N
            else: cur -= N; p /= np.exp(4j * np.pi * cur * lb * la / N)
        ph.append(p)   # D(q) = p D(r)
    pred = ph[0] * ph[1] * np.conj(ph[2])
    for key in ("Y1", "Y2x", "Y3x"):
        A = tonp(ref[sec][key]); B_ = tonp(conf["pf"][k_pf][key])
        rat = A / B_
        print(sec, key, "ratio spread", f"{np.max(np.abs(rat - rat[0,0])):.1e}", "ratio", np.round(rat[0, 0], 12), "predicted", np.round(pred, 12))
    KA = tonp(ref[sec]["KL32"]); KB = tonp(conf["Kpf"][k_pf[0]]["K32"])
    print(sec, "K32 rel", f"{np.max(np.abs(KA - KB)) / np.max(np.abs(KA)):.1e}")
