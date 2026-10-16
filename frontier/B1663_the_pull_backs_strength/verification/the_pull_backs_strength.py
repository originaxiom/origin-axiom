#!/usr/bin/env python3
"""B1663 -- THE PULL-BACK'S STRENGTH (P-183 step 3): does anything the motion picture uses depend on how strong the
pull-back is? The walk on SL(2, Z) (GENESIS v1.48: the pull-back acts on the records) with steps L, R each (1 - p)/2 and
L^-1, R^-1 each p/2, right-multiplied, for p in {0, 0.1, 0.2, 0.3, 0.4, 0.5} (p = 1/2: no preference).
  T0  plumbing: f's mirror invariance f(-conj t) = f(t); the ray instrument recovers the typical motion's average
      0.31500491 (S_THE_PUSH_BACK section 7) on Lebesgue-random rays (a control that can fail)
  T1  the character process: every step multiplies the Higgs's character chi (chi(L) = chi(R^-1) = i, chi(R) = chi(L^-1)
      = -i) by i with probability 1/2 for every p -- exact, and measured
  T2  the side: P(xi > 0) is 1 at p = 0, 1/2 at p = 1/2 (the mirror), and decreases between
  T3  the escape rate (1/n) log||X_n|| is positive at every p and differs between p = 0 and p = 1/2
  T4  the motion's averaged defect: <f> along the geodesic ray to the walk's limit xi, averaged over walks, E_p<f>:
      (a) at p = 0 it differs from the typical motion's 0.315 (the walk's exit law is not Lebesgue);
      (b) it differs between p = 0 and p = 1/2 -- the pull-back's strength is not idle;
      (c) at p = 1/2 it differs from 0.315 (Guivarc'h-Le Jan: a finitely supported walk on a non-cocompact lattice
          has a singular exit law)
      read-out: E_(1/2)<f>, the no-preference value
The ray average by digits: the geodesic coded by xi's continued-fraction digits, cut at its crossings of Re z = 0, each
arc on the semicircle with endpoints u_k = [a_k; a_k+1, ...], v_k = -[0; a_k-1, ...] (O(1): no precision loss); f set to
0 above height 7 (f(6i) < 3e-6). Eight workers, single-threaded BLAS (the owner's rule); seeds fixed.
Writes the_pull_backs_strength.json and _run.txt."""
import os
for k in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[k] = "1"
import json, math, pathlib, random, time
from multiprocessing import Pool
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
OUT, RUN = HERE / "the_pull_backs_strength.json", HERE / "the_pull_backs_strength_run.txt"
PS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5); WALKS = 320; CONTROL = 160; LOG10_TARGET = 60; LOOK = 20; DROP = 20; MIN_DIGITS = 40
YCUT = 7.0; LIOUVILLE = 0.31500491; WORKERS = 8
_N = np.arange(-12, 13); _K = np.arange(1, 60)
def f_raw(t):
    q = np.exp(1j*np.pi*t)
    t3 = np.sum(q**(_N**2)); t4 = np.sum((-1.0)**_N*q**(_N**2)); t2 = np.sum(np.exp(1j*np.pi*t*(_N + 0.5)**2))
    eta = np.exp(1j*np.pi*t/12)*np.prod(1 - np.exp(2j*np.pi*t*_K))
    lam = t2**4/t3**4; h = lam*np.log(abs(lam)) + (1 - lam)*np.log(abs(1 - lam))
    D = -t3**4*h/(4*np.pi*eta**6); Rn = (abs(t2)**4 + abs(t3)**4 + abs(t4)**4)/abs(2*np.pi*eta**3)**2
    return float(abs(D)/Rn)
def reduce(t):
    for _ in range(400):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-15: t = -1/t
        else: return t
    return t
def f(t):
    t = reduce(t)
    return 0.0 if t.imag > YCUT else f_raw(t)
GX, GW = np.polynomial.legendre.leggauss(24)
def cf_tail(ds):
    x = 0.0
    for a in reversed(ds): x = 1.0/(a + x)
    return x
def arc(u, v, a):
    c, r = (u + v)/2, (u - v)/2
    t0 = math.acos(max(-1.0, min(1.0, -c/r))); t1 = math.acos(max(-1.0, min(1.0, (a - c)/r)))
    s0, s1 = math.log(math.tan(t0/2)), math.log(math.tan(t1/2)); L = abs(s0 - s1); tot = 0.0
    n = max(1, int(math.ceil(L/0.6)))
    for j in range(n):
        lo, hi = s1 + (s0 - s1)*j/n, s1 + (s0 - s1)*(j + 1)/n
        for x, w in zip(GX, GW):
            s = (x + 1)/2*(hi - lo) + lo; th = 2*math.atan(math.exp(s))
            tot += w*(hi - lo)/2*f(complex(c + r*math.cos(th), r*math.sin(th)))
    return tot, L
def ray_average(digits):
    num = den = 0.0
    for k in range(1, len(digits) - LOOK):
        u = digits[k] + cf_tail(digits[k + 1:k + 1 + LOOK]); v = -cf_tail(digits[max(0, k - LOOK):k][::-1])
        t, L = arc(u, v, digits[k]); num += t; den += L
    return num/den
def digits_of(num, den):
    num, den = abs(num), abs(den); out = []
    while den:
        q, r = divmod(num, den); out.append(q); num, den = den, r
    return [a for a in out[1:] if a > 0]
STEPS = None
def walk(job):
    p, seed = job; rng = random.Random(seed)
    a, b, c, d = 1, 0, 0, 1; n = 0; phase = 0; up = 0
    while max(abs(a), abs(b), abs(c), abs(d)) < 10**LOG10_TARGET and n < 40000:
        x = rng.random()
        if x < (1 - p)/2: b, d = a + b, c + d; k = 1                        # L
        elif x < 1 - p: a, c = a + b, c + d; k = -1                         # R
        elif x < 1 - p/2: b, d = b - a, d - c; k = -1                      # L^-1
        else: a, c = a - b, c - d; k = 1                                    # R^-1
        n += 1; up += (k == 1)
    esc = 0.5*math.log(a*a + b*b + c*c + d*d)/n
    if c == 0: return dict(p=p, seed=seed, n=n, ok=False)
    ds = digits_of(a, c); ds = ds[:max(0, len(ds) - DROP)]
    side = (a*c > 0)
    if len(ds) < MIN_DIGITS: return dict(p=p, seed=seed, n=n, ok=False, esc=esc, side=side, up=up)
    fv = ray_average(ds)
    if not math.isfinite(fv): return dict(p=p, seed=seed, n=n, ok=False, esc=esc, side=side, up=up, nan=True)
    return dict(p=p, seed=seed, n=n, ok=True, esc=esc, side=side, up=up, f=fv, nd=len(ds))
def control(seed):
    rng = random.Random(seed); num, den = rng.getrandbits(600), 1 << 600
    ds = digits_of(num, den)[:160]
    return ray_average(ds)
def log(msg):
    with open(RUN, "a") as fh: fh.write(msg + "\n")
if __name__ == "__main__":
    T0 = time.time(); RUN.write_text(""); out = dict(PS=PS, WALKS=WALKS, CONTROL=CONTROL, LOG10_TARGET=LOG10_TARGET)
    pts = [complex(0.13, 1.1), complex(-0.31, 0.92), complex(0.4, 1.7), complex(0.05, 2.3), complex(-0.45, 1.3)]
    mir = max(abs(f(-t.conjugate()) - f(t))/f(t) for t in pts)
    inv = max(max(abs(f_raw(t + 1) - f_raw(t)), abs(f_raw(-1/t) - f_raw(t)))/f_raw(t) for t in pts)
    with Pool(WORKERS) as pool:
        ctl = pool.map(control, range(900001, 900001 + CONTROL))
        cm, cse = float(np.mean(ctl)), float(np.std(ctl)/math.sqrt(len(ctl)))
        ctl_ok = all(math.isfinite(x) for x in ctl)
        out["T0"] = dict(mirror_max=mir, TS_invariance_max=inv, control_mean=cm, control_se=cse, control_finite=ctl_ok,
                         holds=(mir < 1e-12 and inv < 1e-10 and ctl_ok and abs(cm - LIOUVILLE) < 3*cse))
        log(f"T0 {out['T0']} [{time.time() - T0:.0f}s]")
        res = pool.map(walk, [(p, 1000*int(round(10*p)) + 17*w + 5) for p in PS for w in range(WALKS)])
    by = {p: [r for r in res if r["p"] == p] for p in PS}
    T1, T2, T3, T4 = {}, {}, {}, {}
    for p in PS:
        rs = by[p]; ok = [r for r in rs if r.get("ok")]
        steps = sum(r["n"] for r in rs); ups = sum(r.get("up", 0) for r in rs)
        T1[p] = dict(freq=ups/steps, se=math.sqrt(0.25/steps))
        sides = [r["side"] for r in rs if "side" in r]; T2[p] = dict(P_pos=float(np.mean(sides)), se=float(np.std(sides)/math.sqrt(len(sides))))
        esc = [r["esc"] for r in rs if "esc" in r]; T3[p] = dict(rate=float(np.mean(esc)), se=float(np.std(esc)/math.sqrt(len(esc))))
        fs = [r["f"] for r in ok]; T4[p] = dict(mean=float(np.mean(fs)), se=float(np.std(fs)/math.sqrt(len(fs))), n_ok=len(fs), n_fail=len(rs) - len(fs),
                                                 mean_digits=float(np.mean([r["nd"] for r in ok])))
        log(f"p={p}: chi-step {T1[p]}  side {T2[p]}  escape {T3[p]}  <f> {T4[p]} [{time.time() - T0:.0f}s]")
    exact = {"L": 1, "R^-1": 1, "R": -1, "L^-1": -1}         # the +-1 each letter adds to #L - #R
    out["T1"] = dict(by_p=T1, exact_rule=exact, holds=all(abs(T1[p]["freq"] - 0.5) < 4*T1[p]["se"] for p in PS))
    mono = all(T2[PS[i]]["P_pos"] >= T2[PS[i + 1]]["P_pos"] - 3*max(T2[PS[i]]["se"], T2[PS[i + 1]]["se"], 1e-9) for i in range(len(PS) - 1))
    out["T2"] = dict(by_p=T2, holds=(T2[0.0]["P_pos"] == 1.0 and abs(T2[0.5]["P_pos"] - 0.5) < 3*T2[0.5]["se"] and mono))
    out["T3"] = dict(by_p=T3, holds=abs(T3[0.0]["rate"] - T3[0.5]["rate"]) > 10*math.hypot(T3[0.0]["se"], T3[0.5]["se"]))
    a = abs(T4[0.0]["mean"] - LIOUVILLE) > 5*math.hypot(T4[0.0]["se"], cse)
    b = abs(T4[0.0]["mean"] - T4[0.5]["mean"]) > 5*math.hypot(T4[0.0]["se"], T4[0.5]["se"])
    c = abs(T4[0.5]["mean"] - LIOUVILLE) > 5*math.hypot(T4[0.5]["se"], cse)
    fok = all(T4[p]["n_fail"] <= 0.1*WALKS for p in PS)
    spread = max(T4[p]["mean"] for p in PS) - min(T4[p]["mean"] for p in PS)
    out["T4"] = dict(by_p=T4, a_p0_not_typical=a, b_p_not_idle=b, c_half_not_typical=c, readout_half=T4[0.5],
                     readout_spread_over_p=spread, failures_ok=fok, holds=(a and b and c and fok))
    out["all_hold"] = all(out[k]["holds"] for k in ("T0", "T1", "T2", "T3", "T4")); out["seconds"] = time.time() - T0
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n"); log(f"all_hold {out['all_hold']} [{out['seconds']:.0f}s]")
