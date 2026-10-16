#!/usr/bin/env python3
"""B1666 -- THE LAYERS WITH A ROBUST PHASE (a scoreboard: B1664's and B1665's read-outs were seen; their gates failed
at D's two zeros, the cusp cut-off and omega). The one change: the period phase is the least-squares phase over a whole
period, sum g(s + l) conj(g(s)) / sum |g(s)|^2, computed over two consecutive periods, which no zero can spoil.
B1664 -- THE LAYERS (P-183 steps 1-2: the weave side against the constant wave). Every primitive thread (a cyclic class
of forward words in L, R with both letters; one Lyndon representative) with trace t <= TMAX, along its closed geodesic:
  - <f>, the time average of f = |D|/||R||^2 over one period;
  - the amplitude g(s) = D(z) (dz/ds)^(-1/2): D at the reduced point w = gamma z, carried back exactly,
    D(z) = chi(gamma)^-1 (c z + d) D(w), with chi the Higgs's character (chi(z -> z+1) = chi(z -> -1/z) = i); the square
    root continued along the period; the period phase g(s0 + l)/g(s0); and, on the threads whose phase is 1, the
    coherence |int g ds| / int |g| ds over one period.
  L0  plumbing: the layer sizes 1, 2, 2, 3 at t = 3..6; the period phase equals i^(#L - #R) on EVERY thread (to 1e-5; a wrong phase misses by >= |1 - i|);
      the coherences of LR, LLRR, LLLRRR, LLRLRR as S_THE_PUSH_BACK section 8.3b (0.637, 0.243, 0.259, 0.321, to 5e-3)
  L1  the constant wave: the layer averages A_t = mean <f> over the threads of trace t approach the typical motion's
      0.31500491: the mean of A_t over the top quarter of traces is within 0.03 of it, and closer than the mean over
      t in [3, 20]
  L2  no constant wave for the amplitude: the coherence of the phase-1 threads decays with length: over every phase-1
      thread with t >= 10, the slope of log(coherence) against log(length) is negative by more than 3 SE (a random-phase
      estimate gives -1/2)
  read-outs: A_t and C_t by layer; the fitted exponents; the fraction of phase-1 threads; the most coherent phase-1 thread
      and the cusp family L^(4m+1) R (seen before the seal: L^9 R at 0.717 out-coheres the root LR at 0.637)
Eight workers, single-threaded BLAS (the owner's rule). Writes the_layers.json and _run.txt."""
import os
for k in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[k] = "1"
import cmath, json, math, pathlib, time
from multiprocessing import Pool
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
OUT, RUN = HERE / "the_layers_robust.json", HERE / "the_layers_robust_run.txt"
TMAX = 600; STEP = 0.02; WORKERS = 8; LIOUVILLE = 0.31500491
REF = {"LR": 0.637, "LLRR": 0.243, "LLLRRR": 0.259, "LLRLRR": 0.321}
_N = np.arange(-12, 13); _K = np.arange(1, 60)
YCUT = 50.0
def Df(t):
    if t.imag > YCUT: return 0j, 0.0        # |D| < 4 y e^(-pi y / 2) < 1e-30 there; the theta series underflow near y = 225
    q = np.exp(1j*np.pi*t)
    t3 = np.sum(q**(_N**2)); t4 = np.sum((-1.0)**_N*q**(_N**2)); t2 = np.sum(np.exp(1j*np.pi*t*(_N + 0.5)**2))
    eta = np.exp(1j*np.pi*t/12)*np.prod(1 - np.exp(2j*np.pi*t*_K))
    lam = t2**4/t3**4; h = lam*np.log(abs(lam)) + (1 - lam)*np.log(abs(1 - lam))
    D = -t3**4*h/(4*np.pi*eta**6); Rn = (abs(t2)**4 + abs(t3)**4 + abs(t4)**4)/abs(2*np.pi*eta**3)**2
    return complex(D), float(abs(D)/Rn)
CHI_T, CHI_S = 1j, 1j
def reduce_track(z):
    a, b, c, d = 1, 0, 0, 1; chi = 1 + 0j
    for _ in range(400):
        n = round(z.real); z = z - n; a, b = a - n*c, b - n*d; chi *= CHI_T**(-n)
        if abs(z) < 1 - 1e-15: z = -1/z; a, b, c, d = -c, -d, a, b; chi *= CHI_S
        else: return z, (a, b, c, d), chi
    raise RuntimeError("reduction did not converge")
def lyndon_ok(w):
    return "L" in w and "R" in w and all(w < w[i:] + w[:i] for i in range(1, len(w)))
def threads_upto(T):
    out = []; stack = [("L", (1, 1, 0, 1)), ("R", (1, 0, 1, 1))]
    while stack:
        w, (a, b, c, d) = stack.pop()
        if a + d > T or len(w) > T: continue
        if lyndon_ok(w): out.append((w, a + d))
        stack.append((w + "L", (a, a + b, c, c + d))); stack.append((w + "R", (a + b, b, c + d, d)))
    return out
def thread(job):
    try:
        return _thread(job)
    except Exception as ex:
        return dict(w=job[0], t=job[1], failed=repr(ex)[:200])
def _thread(job):
    word, tr = job
    M = (1, 0, 0, 1)
    for ch in word:
        a, b, c, d = M
        M = (a, a + b, c, c + d) if ch == "L" else (a + b, b, c + d, d)
    a, b, c, d = M; ell = 2*math.acosh(tr/2); disc = math.sqrt(tr*tr - 4)
    xa, xr = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c)
    n = max(200, int(ell/STEP)); ds = ell/n
    s0 = -ell/2 + 0.123*ell; vals = np.empty(2*n + 1, dtype=complex); fs = np.empty(2*n + 1); prev = None
    for j in range(2*n + 1):
        s = s0 + j*ds; w_ = 1j*math.exp(s); z = (xa*w_ + xr)/(w_ + 1); v = (xa - xr)*w_/(w_ + 1)**2
        wz, (ga, gb, gc, gd), chi = reduce_track(z); Dw, fv = Df(wz)
        r = cmath.sqrt(v)
        if prev is not None and abs(r - prev) > abs(-r - prev): r = -r
        prev = r; vals[j] = (gc*z + gd)*Dw/chi/r; fs[j] = fv
    P1, P2 = vals[:n + 1], vals[n:2*n + 1]; F1 = fs[:n + 1]
    wts = np.full(n + 1, ds); wts[0] = wts[-1] = ds/2
    I = np.sum(wts*P1); A = np.sum(wts*np.abs(P1))
    phase = complex(np.sum(P2*np.conj(P1))/np.sum(np.abs(P1)**2))       # the least-squares period phase
    nl, nr = word.count("L"), word.count("R")
    return dict(w=word, t=tr, f=float(np.sum(wts*F1)/ell), coh=float(abs(I)/A), phase=[phase.real, phase.imag],
                ph_err=float(abs(phase - 1j**(nl - nr))), chi1=((nl - nr) % 4 == 0), finite=bool(np.isfinite(vals).all() and np.isfinite(fs).all()))
def log(msg):
    with open(RUN, "a") as fh: fh.write(msg + "\n")
def slope(x, y):
    x, y = np.log(np.asarray(x, float)), np.log(np.asarray(y, float)); X = np.vstack([x, np.ones_like(x)]).T
    beta, res, *_ = np.linalg.lstsq(X, y, rcond=None); r = y - X @ beta; s2 = r @ r/(len(x) - 2)
    cov = s2*np.linalg.inv(X.T @ X); return float(beta[0]), float(math.sqrt(cov[0, 0]))
if __name__ == "__main__":
    T0 = time.time(); RUN.write_text("")
    th = threads_upto(TMAX); log(f"threads with trace <= {TMAX}: {len(th)} [{time.time() - T0:.0f}s]")
    with Pool(WORKERS) as pool:
        res = pool.map(thread, sorted(th, key=lambda x: -len(x[0])), chunksize=8)
    log(f"computed [{time.time() - T0:.0f}s]")
    fails = [r for r in res if "failed" in r]; res = [r for r in res if "failed" not in r]
    by = {}
    for r in res: by.setdefault(r["t"], []).append(r)
    ts = sorted(by)
    sizes = [len(by.get(t, [])) for t in range(3, 7)]
    ph_max = max(r["ph_err"] for r in res); fin = all(r["finite"] for r in res)
    ref = {w: next(r["coh"] for r in res if r["w"] == w) for w in REF}
    L0 = dict(sizes_3_6=sizes, phase_err_max=ph_max, all_finite=fin, ref_coherence=ref, failures=[f["w"][:40] + ": " + f["failed"] for f in fails][:20],
              holds=(not fails and sizes == [1, 2, 2, 3] and ph_max < 1e-5 and fin and all(abs(ref[w] - REF[w]) < 5e-3 for w in REF)))
    A = {t: float(np.mean([r["f"] for r in by[t]])) for t in ts}
    q = ts[int(0.75*len(ts)):]; lo = [t for t in ts if t <= 20]
    top = float(np.mean([A[t] for t in q])); low = float(np.mean([A[t] for t in lo]))
    L1 = dict(top_quarter_mean=top, low_mean=low, top_traces=[q[0], q[-1]],
              holds=(abs(top - LIOUVILLE) < 0.03 and abs(top - LIOUVILLE) < abs(low - LIOUVILLE)))
    C = {t: float(np.mean([r["coh"] for r in by[t] if r["chi1"]])) for t in ts if any(r["chi1"] for r in by[t])}
    ct = sorted(C); cq = ct[int(0.75*len(ct)):]; clo = [t for t in ct if t <= 20]
    ctop = float(np.mean([C[t] for t in cq])); clow = float(np.mean([C[t] for t in clo]))
    p1 = [r for r in res if r["chi1"] and r["t"] >= 10]
    sl, se = slope([2*math.acosh(r["t"]/2) for r in p1], [r["coh"] for r in p1])
    L2 = dict(top_quarter_mean=ctop, low_mean=clow, per_thread_slope=sl, slope_se=se, n_threads=len(p1), holds=(sl < 0 and abs(sl) > 3*se))
    best = max((r for r in res if r["chi1"]), key=lambda r: r["coh"])
    cusp = {r["w"]: r["coh"] for r in res if r["chi1"] and r["w"].count("R") == 1}
    asl, ase = slope([t for t in ts if t >= 10], [abs(A[t] - LIOUVILLE) for t in ts if t >= 10])
    out = dict(TMAX=TMAX, n_threads=len(res), L0=L0, L1=L1, L2=L2,
               readouts=dict(A_by_t=A, C_by_t=C, f_deviation_slope=[asl, ase], phase1_fraction=sum(r["chi1"] for r in res)/len(res),
                             most_coherent=[best["w"][:60], best["coh"]], LR=ref["LR"], cusp_family_LnR=cusp))
    out["all_hold"] = all(out[k]["holds"] for k in ("L0", "L1", "L2")); out["seconds"] = time.time() - T0
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    for k in ("L0", "L1", "L2"): log(f"{k} {out[k]}")
    log(f"most coherent phase-1 thread {out['readouts']['most_coherent']}; LR {out['readouts']['LR']}")
    log(f"all_hold {out['all_hold']} [{out['seconds']:.0f}s]")
