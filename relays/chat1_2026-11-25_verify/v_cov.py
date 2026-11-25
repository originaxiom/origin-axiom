#!/usr/bin/env python3
"""V-COV (chat1, 2026-11-25, evening; data-free): is frame C covariant OFF the imaginary axis, under S and under the act
M = [[2,1],[1,1]] moving tau and the point together? B1982 tested S only on the axis (three height pairs) and called frame C
SL(2, Z)-covariant; agy-002's card A2-B1978-ORDER30 claims joint SL(2, Z) and M covariance on its own code; B1978 left
joint covariance unchecked (the caveat carried by the seat's W-LV1, section 8). This test uses main's frame code at
18bb9e0da (duality_cov.parts_L / outputs: the nine log outputs, sector rates and |V| entries) and main's covariant end
(fricke_endlaw: L(tau) = L_2(tau_FD) + 1/2 log(Im tau_FD / Im tau), the record's law by construction). Not blind: B1982's
values were read through the mask first. Nothing is compared with data.

    python3 -B v_cov.py <checkout of main at 18bb9e0da>     (about 10 to 20 minutes on one core)

CONDITION, written before the run.
 Base points: tau1 = 0.3 + 1.2i and tau2 = -0.2 + 1.1i (both in the fundamental domain, heights below the clamp at 6).
 Moves: S (tau -> -1/tau) and M (tau -> (2 tau + 1)/(tau + 1)); the images have heights 0.78, 0.88 (S) and 0.38, 0.59 (M).
 Source: outputs at B1976's 96 points at tau, end L(tau). Target: outputs at all 899 nonzero points of E[30] at g tau,
 end L(g tau) from the same formula. d(w) = the least, over target points, of the largest relative difference of the nine
 outputs (main's dist). The worst d over the 96 sources is read.
 K1  S off the axis: worst d < 1e-8 at both base points.
 K2  M jointly (tau and point together): worst d < 1e-8 at both base points.
 K3  controls (each must FAIL the bar, worst d > 1e-3): (a) the M target read with the end NOT shifted (L(g tau) replaced by
     L(tau)); (b) a non-modular move tau -> tau + 1/2 at tau1 with the formula's end.
 K4  (informational, declared now) for K1 and K2, which of the eight maps w -> +-(w g), +-(w g^-1), +-(w g^T), +-(w g^-T)
     (w a row (a, b), mod 1) sends every source to a matching target (d < 1e-8); "none" is reported if none does.
 Reading: K1 and K2 pass and K3 fails as required -> frame C (with the law's end) is covariant off the axis under S and
 under the act jointly at these points, which confirms B1982 beyond the axis and agy-002's joint claim on main's code, and
 lifts B1978's caveat at these points (not a proof for every tau). K1 or K2 failing -> reported to main as a discrepancy.
 If a control passes the bar, the test cannot discriminate and says so.
"""
import sys, pathlib, math, time, json
from fractions import Fraction as Fr
from multiprocessing import Pool

main_dir = pathlib.Path(sys.argv[1]).resolve()
import subprocess
head = subprocess.run(["git", "-C", str(main_dir), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
if not head.startswith("18bb9e0da"):
    sys.exit("refused: checkout at %s" % head[:9])
sys.path.insert(0, str(next((main_dir / "frontier").glob("B1980_*")) / "verification"))
import duality_cov as D

def L_law(t):
    f = D.fd(t.real, t.imag)
    return D.FM.CR.canon(f)["L_2"] + 0.5 * math.log(f.imag / t.imag)

def ev(arg):
    t, a, b, L = arg
    return D.outputs((repr(t.real), t.imag, a, b, L))

def frac_row(w, g):
    a, b = w
    return ((a * g[0][0] + b * g[1][0]) % 1, (a * g[0][1] + b * g[1][1]) % 1)

def candidates(g):
    (p, q), (r, s) = g
    inv = ((s, -q), (-r, p))
    T = ((p, r), (q, s)); iT = ((s, -r), (-q, p))
    out = {}
    for name, h in (("w g", g), ("w g^-1", inv), ("w g^T", T), ("w g^-T", iT)):
        for sg in (1, -1):
            out[("+" if sg > 0 else "-") + name] = lambda w, h=h, sg=sg: tuple((sg * v) % 1 for v in frac_row(w, h))
    return out

if __name__ == "__main__":
    t0 = time.time()
    moves = {"S": (lambda t: -1 / t, ((0, -1), (1, 0))), "M": (lambda t: (2 * t + 1) / (t + 1), ((2, 1), (1, 1))),
             "half": (lambda t: t + 0.5, None)}
    bases = {"tau1": complex(0.3, 1.2), "tau2": complex(-0.2, 1.1)}
    res = {}
    with Pool(2) as pool:
        for bname, t in bases.items():
            Lt = L_law(t)
            src = dict(zip(D.P96, pool.map(ev, [(t, a, b, Lt) for (a, b) in D.P96], chunksize=8)))
            plan = [("S", "law"), ("M", "law")] + ([("M", "unshifted"), ("half", "law")] if bname == "tau1" else [])
            for mv, endk in plan:
                f, g = moves[mv]
                tp = f(t)
                Lp = L_law(tp) if endk == "law" else Lt
                par = dict(zip(D.E30, pool.map(ev, [(tp, a, b, Lp) for (a, b) in D.E30], chunksize=8)))
                ds = {w: min((D.dist(u, v), wp) for wp, v in par.items()) for w, u in src.items()}
                worst = max(d for d, _ in ds.values())
                k4 = None
                if g is not None and endk == "law":
                    k4 = [n for n, h in candidates(g).items() if all(D.dist(src[w], par[h(w)]) < 1e-8 for w in src if h(w) in par)
                          and all(h(w) in par for w in src)] or ["none"]
                res[(bname, mv, endk)] = (worst, k4)
                print("%s = %s, move %s to %s (end %s, L %.6f -> %.6f): worst d %.1e; maps on the point consistent with "
                      "every match: %s  [%.0f s]" % (bname, t, mv, tp, endk, Lt, Lp, worst, k4, time.time() - t0), flush=True)
    K1 = all(res[(b, "S", "law")][0] < 1e-8 for b in bases)
    K2 = all(res[(b, "M", "law")][0] < 1e-8 for b in bases)
    K3 = res[("tau1", "M", "unshifted")][0] > 1e-3 and res[("tau1", "half", "law")][0] > 1e-3
    print("SUMMARY K1 (S off the axis) %s; K2 (M jointly) %s; K3 (controls fail as required) %s" % (K1, K2, K3))
    out = {"%s|%s|%s" % k: {"worst": v[0], "maps": v[1]} for k, v in res.items()}
    pathlib.Path(__file__).with_name("v_cov.json").write_text(json.dumps(out, indent=1))
