#!/usr/bin/env python3
"""The sealed run: the torsion law on levels not touched before the seal.

For each level of POPULATION and each of up to six extension characters l of order above two (spread over the list of
characters in its fixed order), the periodic curve through the background is followed from the torsion point and

  (a) every sector's torsion is expanded at the reducible end: order and leading coefficient in e = 2 - kappa;
  (b) the cusp shape  log M / log l  of the curve is taken at e = 1e-10 and compared with the slope s(l);
  (c) for an integer slope, the meridian is compared with +-(longitude)^(+-s) at e = 0.02.

usage:  law_population.py <first> <last>      (a slice of POPULATION; one record file per level)
        law_population.py control            (the levels seen before the seal)
"""
import sys, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import curve_engine as ce
from mpmath import mpf, nstr, acosh, eye, inverse

POPULATION = [("-LLR", 1), ("-LLR", 2), ("-LRR", 1), ("+LRR", 2), ("-LRR", 2), ("+LLLR", 1), ("+LLLR", 2), ("-LLLR", 1), ("-LLLR", 2), ("-LLRR", 1),
              ("+LLRR", 2), ("-LLRR", 2), ("+LLRLR", 1), ("+LLLRR", 1), ("-LLLRR", 1), ("+LRLRR", 1), ("-LRLRR", 1), ("+LLLLR", 1), ("-LLLLR", 1),
              ("+LLLLR", 2), ("+LLRLRR", 1), ("-LLRLRR", 1), ("+LLLRLR", 1), ("-LLLRLR", 1), ("+LLRRLR", 1), ("+LLLRRR", 1), ("-LLLRRR", 1)]
CONTROL = [("+LR", 2), ("+LR", 3)]
PER_LEVEL = 6
TOL = mpf("1e-6")

def level(name, k):
    eps = 1 if name[0] == "+" else -1; word = name[1:]
    Phi = ce.monodromy(eps, word, k); N = ce.exponent(Phi); chars = [c for c in ce.level_characters(Phi, N) if c != (0, 0)]
    smooth = [c for c in chars if (2 * c[0]) % N or (2 * c[1]) % N]
    step = max(1, len(smooth) // PER_LEVEL); ells = smooth[::step][:PER_LEVEL]
    rec = dict(state=name, k=k, torsion=len(chars) + 1, exponent=N, backgrounds=[])
    for ell in ells:
        b = dict(ell=list(ell))
        try:
            B, sl, rows = ce.analyse(eps, word, k, ell)
        except (AssertionError, ZeroDivisionError) as e:
            b["error"] = str(e)[:120]; rec["backgrounds"].append(b); continue
        b["slope"] = nstr(sl, 15); b["sigma"] = list(B.sig); sect = []
        for r in rows:
            d = dict(beta=list(r["beta"]), index=r["index"], matches=r["matches"], order=r["order"], predicted_first=nstr(r["predicted"], 15))
            if r["order"] is not None:
                d["coeff"] = nstr(r["coeff"].real, 15); d["coeff_imag"] = nstr(abs(r["coeff"].imag), 3)
                if r["matches"] == 0: d["first_order_ok"] = bool(r["order"] == 1 and abs(r["coeff"] - r["predicted"]) < TOL * max(1, abs(r["predicted"])))
            sect.append(d)
        b["sectors"] = sect
        b["zero_type"] = any(d["order"] is None for d in sect)
        # (b) the cusp shape at the end
        try:
            p, g, T = B.point("1e-10"); lam = g[1] * g[2] * inverse(g[1]) * inverse(g[2])
            xl, xm = acosh(ce.tr(lam) / 2), acosh(ce.tr(T) / 2)
            ratio = abs(xm / xl) if abs(xm) > mpf(10) ** (-40) else mpf(0)
            b["cusp_shape_limit"] = nstr(ratio, 15); b["slope_limit_ok"] = bool(abs(ratio - abs(sl)) < TOL * max(1, abs(sl)))
        except (AssertionError, ZeroDivisionError) as e:
            b["slope_limit_error"] = str(e)[:120]
        # (c) the filling test
        b["filling_type"] = False
        if abs(sl - round(sl)) < mpf("1e-20"):
            try:
                p, g, T = B.point("0.02"); lam = g[1] * g[2] * inverse(g[1]) * inverse(g[2]); P = eye(2)
                for _ in range(abs(int(round(sl)))): P = P * lam
                dist = min(max(abs((T - sg * Q)[i, j]) for i in range(2) for j in range(2)) for sg in (1, -1) for Q in (P, inverse(P)))
                b["filling_type"] = bool(dist < mpf("1e-25"))
            except (AssertionError, ZeroDivisionError) as e:
                b["filling_type"] = None; b["filling_error"] = str(e)[:120]
        rec["backgrounds"].append(b)
        print("   %s level %d l = %s slope %s: %d sectors, zero-type %s, filling-type %s" % (name, k, ell, b["slope"], len(sect), b["zero_type"], b["filling_type"]), flush=True)
    return rec

if __name__ == "__main__":
    if sys.argv[1] == "control":
        for name, k in CONTROL:
            rec = level(name, k); json.dump(rec, open(HERE / ("law_control_%s_%d.json" % (name, k)), "w"), indent=1)
    else:
        for i in range(int(sys.argv[1]), min(int(sys.argv[2]), len(POPULATION))):
            name, k = POPULATION[i]; rec = level(name, k); json.dump(rec, open(HERE / ("law_population_%02d.json" % i), "w"), indent=1)
