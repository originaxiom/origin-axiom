"""POST-SEAL DIAGNOSIS (B1665's failed gate; labelled, not a cell): which threads give a large period-phase error, how
close their start sits to omega (D's other zero), and the phase measured robustly -- the least-squares phase over the
whole period, sum g(s + l) conj(g(s)) / sum |g(s)|^2, which no zero can spoil -- on every thread."""
import importlib.util, math, cmath, pathlib, json
from multiprocessing import Pool
import numpy as np
P = pathlib.Path(__file__).resolve().parents[1] / "the_layers_resealed.py"
spec = importlib.util.spec_from_file_location("b1665", P); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
OM = complex(-0.5, math.sqrt(3)/2)
def one(job):
    word, tr = job
    M = (1, 0, 0, 1)
    for ch in word:
        a, b, c, d = M; M = (a, a + b, c, c + d) if ch == "L" else (a + b, b, c + d, d)
    a, b, c, d = M; ell = 2*math.acosh(tr/2); disc = math.sqrt(tr*tr - 4)
    xa, xr = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c)
    n = max(200, int(ell/m.STEP)); ds = ell/n
    def g_at(s, prev):
        w_ = 1j*math.exp(s); z = (xa*w_ + xr)/(w_ + 1); v = (xa - xr)*w_/(w_ + 1)**2
        wz, (ga, gb, gc, gd), chi = m.reduce_track(z); Dw, _ = m.Df(wz); r = cmath.sqrt(v)
        if prev is not None and abs(r - prev) > abs(-r - prev): r = -r
        return (gc*z + gd)*Dw/chi/r, r, wz
    s0 = -ell/2; g, prev = [], None; w0 = None
    for j in range(2*n + 1):                                  # two periods, the root continued throughout
        val, prev, wz = g_at(s0 + j*ds, prev); g.append(val); w0 = w0 if w0 is not None else wz
    g = np.array(g); A, B = g[:n + 1], g[n:2*n + 1]
    phase = complex(np.sum(B*np.conj(A))/np.sum(np.abs(A)**2))
    nl, nr = word.count("L"), word.count("R")
    r = m.thread(job)
    return dict(w=word[:30], t=tr, sealed_ph_err=r["ph_err"], robust_err=abs(phase - 1j**(nl - nr)))
if __name__ == "__main__":
    th = m.threads_upto(m.TMAX)
    with Pool(8) as pool: res = pool.map(one, th, chunksize=16)
    big = [x for x in res if not (x["sealed_ph_err"] < 1e-6)]
    out = dict(n=len(res), n_sealed_fail=len(big), sealed_fail_examples=[(x["w"], round(x["sealed_ph_err"], 3)) for x in sorted(big, key=lambda x: -x["sealed_ph_err"])[:6]],
               robust_max_err=max(x["robust_err"] for x in res), robust_fail=sum(1 for x in res if not x["robust_err"] < 1e-6))
    print(json.dumps(out, indent=1)); pathlib.Path(__file__).with_name("gate_diagnosis_output.json").write_text(json.dumps(out, indent=1) + "\n")
