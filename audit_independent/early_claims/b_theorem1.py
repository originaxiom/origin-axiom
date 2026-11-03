"""(b) Theorem 1: my own implementation of the relay's closed form (written from the relay text, not agy's code),
compared with main's quadrature cA (b1656_funcs, B1691 correction) for all three sectors, many lines and tau.
Then: cusp vanishing locus, decay exponents (fitted from the closed form at high precision and cross-checked with cA),
and whether B1788 hypothesis (a) -- a LOWER bound on the decay rate, |E00 - E11| in exp(-E 2 pi Im tau) units -- is
actually violated."""
import json, math, pathlib, sys, time, itertools
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp

ROOT = pathlib.Path("/Users/dri/.gemini/antigravity/scratch/origin-axiom-independent-audit")
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction"))
import b1656_funcs as B
CH = {"1": (Fr(0), -1), "i": (Fr(0), 1), "j": (Fr(1, 2), -1), "k": (Fr(1, 2), 1)}
SECT = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}

def c_closed(tau, alpha, b, dps=30, N=200):
    mp.mp.dps = dps; t = mp.mpc(tau.real, tau.imag); b = mp.mpf(b.numerator)/b.denominator; out = {}
    for s, (as_, eta) in CH.items():
        nu = (3*Fr(alpha) + as_) % 1
        if nu == 0:
            den = abs(1 + eta*mp.exp(-6j*mp.pi*b))**2
            if den < mp.mpf(10)**(-20): out[s] = None; continue
            v = 4*mp.pi**2*mp.im(t)/den - 2*mp.pi*mp.log(2*mp.pi)
            for n in range(1, N):
                wp = -eta*mp.exp(2j*mp.pi*(n*t - 3*b)); wm = -eta*mp.exp(2j*mp.pi*(n*t + 3*b))
                v += 2*mp.pi*mp.re(wp/(1 - wp) + wm/(1 - wm))/n
        else:
            nu = mp.mpf(nu.numerator)/nu.denominator
            v = -2*mp.pi*(mp.log(2*mp.pi) + mp.euler) - mp.pi*(mp.digamma(nu) + mp.digamma(1 - nu))
            for n in range(N):
                wp = -eta*mp.exp(2j*mp.pi*((n + nu)*t - 3*b)); wm = -eta*mp.exp(2j*mp.pi*((n + 1 - nu)*t + 3*b))
                v += 2*mp.pi*mp.re(wp/((n + nu)*(1 - wp)) + wm/((n + 1 - nu)*(1 - wm)))
        out[s] = v
    return out

def c_lerch(tau, alpha, b, dps=30, M=60):
    """the Hurwitz-Lerch form (generic case only)"""
    mp.mp.dps = dps; t = mp.mpc(tau.real, tau.imag); bb = mp.mpf(b.numerator)/b.denominator; q = mp.exp(1j*mp.pi*t); out = {}
    for s, (as_, eta) in CH.items():
        nu = (3*Fr(alpha) + as_) % 1
        if nu == 0: out[s] = None; continue
        nu = mp.mpf(nu.numerator)/nu.denominator
        v = -2*mp.pi*(mp.log(2*mp.pi) + mp.euler) - mp.pi*(mp.digamma(nu) + mp.digamma(1 - nu))
        for m in range(1, M):
            v += 2*mp.pi*mp.re((-eta)**m*(mp.exp(-6j*mp.pi*m*bb)*q**(2*m*nu)*mp.lerchphi(q**(2*m), 1, nu)
                                          + mp.exp(6j*mp.pi*m*bb)*q**(2*m*(1 - nu))*mp.lerchphi(q**(2*m), 1, 1 - nu)))
        out[s] = v
    return out

res = {}
lines = [(Fr(2, 5), Fr(1, 10)), (Fr(3, 8), Fr(3, 8)), (Fr(1, 3), Fr(1, 9)), (Fr(1, 12), Fr(0)), (Fr(1, 12), Fr(1, 12)),
         (Fr(5, 12), Fr(1, 4)), (Fr(1, 7), Fr(2, 7)), (Fr(4, 9), Fr(1, 9)), (Fr(1, 4), Fr(1, 8)), (Fr(1, 6), Fr(1, 3)),
         (Fr(0), Fr(1, 8)), (Fr(1, 2), Fr(1, 5)), (Fr(2, 11), Fr(9, 11)), (Fr(7, 10), Fr(3, 10)), (Fr(5, 6), Fr(1, 12))]
rng = np.random.default_rng(7)
taus = [complex(rng.uniform(-0.5, 0.5), y) for y in (1.2, 2.0, 2.742578125, 3.6)]
rows = []; t0 = time.time()
for (a, b) in lines:
    for tau in taus:
        w = B.line_w(a, b, tau); cf = c_closed(tau, a, b)
        rec = {"line": [str(a), str(b)], "tau": [tau.real, tau.imag]}
        for sn, (ql, qr) in SECT.items():
            x, y = B.sector_twists(w, tau, ql, qr); R = B.residues(x, y, tau); cq = B.cA(x, y, tau, R)
            rec[sn] = {s: cq[s] for s in cq}
        diffs_cf = [abs(rec[sn][s] - float(cf[s])) for sn in SECT for s in CH if rec[sn][s] is not None and cf[s] is not None]
        diffs_sec = [abs(rec[sn][s] - rec["down"][s]) for sn in SECT for s in CH if rec[sn][s] is not None and rec["down"][s] is not None]
        nonematch = [(sn, s) for sn in SECT for s in CH if (rec[sn][s] is None) != (cf[s] is None)]
        rec["max|closed-cA|"] = max(diffs_cf) if diffs_cf else None
        rec["max|cA(sector)-cA(down)|"] = max(diffs_sec) if diffs_sec else None
        rec["None_mismatch"] = nonematch
        rows.append(rec)
print("closed vs cA:", len(rows), "configs,", round(time.time() - t0, 1), "s")
res["closed_vs_cA_max"] = max(r["max|closed-cA|"] for r in rows if r["max|closed-cA|"] is not None)
res["sector_indep_max"] = max(r["max|cA(sector)-cA(down)|"] for r in rows if r["max|cA(sector)-cA(down)|"] is not None)
res["None_mismatches"] = [(r["line"], r["tau"], r["None_mismatch"]) for r in rows if r["None_mismatch"]]
res["worst_rows"] = sorted(((r["max|closed-cA|"] or 0, r["line"], r["tau"]) for r in rows), reverse=True)[:5]
print({k: res[k] for k in ("closed_vs_cA_max", "sector_indep_max", "None_mismatches", "worst_rows")})
# Hurwitz-Lerch form vs series
hl = []
for (a, b) in lines[:6]:
    for tau in taus[:2]:
        c1 = c_closed(tau, a, b); c2 = c_lerch(tau, a, b)
        hl += [abs(c1[s] - c2[s]) for s in CH if c2[s] is not None and c1[s] is not None]
res["lerch_vs_series_max"] = float(max(hl)); print("lerch vs series", res["lerch_vs_series_max"])

# cusp combination D_inf(alpha) and its zeros; f = psi(nu)+psi(1-nu) concavity
f = lambda nu: mp.digamma(nu) + mp.digamma(1 - nu)
res["f_second_derivative_sign_at_0.3"] = float(mp.diff(f, mp.mpf("0.3"), 2))
zeros = []
for N in range(1, 61):
    for k in range(1, N):
        al = Fr(k, N)
        if not (0 < al < Fr(1, 2)) or math.gcd(k, N) != 1: continue
        x = (3*al) % 1; y = (3*al + Fr(1, 2)) % 1
        if x == 0 or y == 0: continue
        D = 2*mp.pi*(f(mp.mpf(x.numerator)/x.denominator) - f(mp.mpf(y.numerator)/y.denominator))
        if abs(D) < 1e-20: zeros.append(str(al))
res["D_inf_zeros_alpha_in_(0,1/2)_den<=60"] = zeros; print("D_inf zeros:", zeros)
# finite-tau D on alpha = 1/12 and 5/12 lines vs a generic line, from main's cA
Dfin = []
for (a, b) in [(Fr(1, 12), Fr(0)), (Fr(1, 12), Fr(1, 12)), (Fr(5, 12), Fr(1, 4)), (Fr(2, 5), Fr(1, 10))]:
    for y in (1.5, 2.5, 3.5, 4.5):
        tau = complex(0.1, y); w = B.line_w(a, b, tau); x_, y_ = B.sector_twists(w, tau, 1, 2)
        R = B.residues(x_, y_, tau); cq = B.cA(x_, y_, tau, R)
        Dfin.append((str(a), str(b), y, cq["j"] + cq["k"] - cq["1"] - cq["i"]))
res["D_finite_cA_down"] = Dfin
for d in Dfin: print("D finite", d)

# decay exponents fitted from the closed form (verified above) at Im tau 6..10, Re tau fixed; convention exp(-4 pi E y)
def fit(a, b, which, ys=(6, 7, 8, 9, 10), x=0.137):
    L = []
    for y in ys:
        c = c_closed(complex(x, y), a, b, dps=60, N=60)
        d = (c["1"] - c["i"]) if which == "1i" else (c["j"] - c["k"])
        L.append(float(mp.log(abs(d))))
    sl = np.polyfit(ys, L, 1)[0]
    return -sl/(4*math.pi)
def dist(x): x = x % 1; return min(x, 1 - x)
ex = []
for (a, b) in [(Fr(2, 5), Fr(1, 10)), (Fr(1, 7), Fr(2, 7)), (Fr(4, 9), Fr(1, 9)), (Fr(3, 8), Fr(3, 8)), (Fr(1, 10), Fr(3, 10)),
               (Fr(2, 11), Fr(9, 11)), (Fr(1, 5), Fr(0)), (Fr(5, 12), Fr(1, 4))]:
    e1, e2 = fit(a, b, "1i"), fit(a, b, "jk")
    ex.append({"line": [str(a), str(b)], "E1i_fit": e1, "E1i_pred": float(dist(3*a))/2, "Ejk_fit": e2, "Ejk_pred": 0.25 - float(dist(3*a))/2})
    print(ex[-1])
res["exponents"] = ex
# cross-check one exponent with main's cA directly (down sector) at y = 3,4,5
xc = []
for (a, b) in [(Fr(2, 5), Fr(1, 10)), (Fr(4, 9), Fr(1, 9))]:
    L1, L2 = [], []
    for y in (3.0, 4.0, 5.0):
        tau = complex(0.137, y); w = B.line_w(a, b, tau); x_, y_ = B.sector_twists(w, tau, 1, 2)
        R = B.residues(x_, y_, tau); cq = B.cA(x_, y_, tau, R)
        L1.append(math.log(abs(cq["1"] - cq["i"]))); L2.append(math.log(abs(cq["j"] - cq["k"])))
    xc.append({"line": [str(a), str(b)], "E1i_cA": -np.polyfit((3, 4, 5), L1, 1)[0]/(4*math.pi), "Ejk_cA": -np.polyfit((3, 4, 5), L2, 1)[0]/(4*math.pi)})
    print(xc[-1])
res["exponents_cA_crosscheck"] = xc

# B1788 hypothesis (a): rate (2 pi convention) of c1-ci and cj-ck >= |E00 - E11|, E00-E11 = ||qL a|| + ||qR a|| - 1/2
viol = []; tot = 0
for N in range(1, 13):
    for k in range(N):
        al = Fr(k, N)
        if math.gcd(k, N) != 1 and k != 0: continue
        for sn, (ql, qr) in SECT.items():
            bound = abs(dist(ql*al) + dist(qr*al) - Fr(1, 2))
            r1i = dist(3*al); rjk = Fr(1, 2) - dist(3*al)      # 2 pi convention = 2 x agy's E
            tot += 1
            if (3*al) % Fr(1, 2) == 0: continue
            if r1i < bound or rjk < bound: viol.append((str(al), sn, str(r1i), str(rjk), str(bound)))
res["B1788_a_bound_cases"] = tot; res["B1788_a_bound_violations"] = viol
print("B1788 (a) as a lower bound: violations", len(viol), "of", tot, viol[:10])
json.dump(res, open(OUT / "b_theorem1.json", "w"), indent=1, default=str)
json.dump(rows, open(OUT / "b_theorem1_rows.json", "w"), indent=1, default=str)
