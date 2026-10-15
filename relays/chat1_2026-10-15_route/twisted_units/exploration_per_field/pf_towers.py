"""EXPLORATION (unsealed; excluded orders only): the per-field reading (W92's dressing, factored) on the L.R^n towers
at N = 3, 5, 7, line (0, 1). Written, with its prediction, before its run.

PREDICTION (derived by hand before this run; the cusp criterion of the 15:17 addendum plus the dressing's exponents):
  the dressing shifts a unit's component exponent by ||al + sigma_s||^2 - sigma_s^2 (sigma = 1/2 on theta2, 0 on theta4,
  theta3), al = q lb / N. W84's units, with growth exponents e = (7/8 on e_i [theta2], 1/8 on v+, 5/8 on v- [theta4,
  theta3]), become, for a field of charge q (a = |al| reduced to [0, 1/2]):
      e_+ = 1/8 - a^2,  e_- = 5/8 - a^2,  e_i = 7/8 + a - a^2.
  The Higgs modes stay decaying (h's lowest exponents 1/8, 3/8, 5/8 only rise or stay >= 1/8), so Y stays polynomial
  and K alone sets the exponents. Hence, wherever Y is generic:
      ln(m2/m3) ~ -2 pi y (1/2 + 1/2) = -2 pi y        in EVERY sector (unchanged by the dressing), and
      ln(m1/m3) ~ -2 pi y (3/2 + a_L + a_R)            per sector.
  Slopes per 2 pi dy predicted:  s2: -1 everywhere;  s3: N = 3: up = down -2.167, leptons -1.5 (untwisted);
  N = 5: up -1.9, down -2.1, leptons -2.1;  N = 7: up -2.071, down -1.929, leptons -2.071.
"""
import sys, json, math, pickle, time
import mpmath as mp, flint
sys.path.insert(0, sys.argv[1]); import units_cells as UC
P = pickle.load(open(sys.argv[2], "rb"))
t0 = time.time()
flint.ctx.prec = 800
src = UC.PerFieldFactoredSource(P)
out = {}
for n, N in ((9, 3), (18, 3), (27, 3), (25, 5), (50, 5), (49, 7)):
    tr = n + 2; rho = math.sqrt(tr * tr - 4) / 2
    npts = int(2 * math.acosh(tr / 2) * (2 * math.pi * rho + 60)) // 4 * 4
    r = UC.run(src, n, (0, 1), N, UC.SM, npts)
    out[f"L R^{n} N={N}"] = r
    print(f"L R^{n} N={N} rho={r['rho']:.3f} closure {r['closure']}  t={time.time()-t0:.0f}s", flush=True)
    for sec, row in r["sectors"].items():
        print("   ", sec, {c: (None if d is None else (round(d['ln R2'], 2), round(d['ln R1'], 2), f"{d['r_calc']:.0e}")) for c, d in row.items()}, flush=True)
json.dump(out, open("pf_towers.json", "w"), indent=1, default=float)
print("seconds", round(time.time() - t0, 1))
