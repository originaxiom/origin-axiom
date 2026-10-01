#!/usr/bin/env python3
"""Two checks on every background of the law census:
 (1) the slope is the limit of the cusp shape along the curve:  log M / log l -> +-s  (M, l the eigenvalues of the
     meridian T and of the longitude rho([x,y]) in SL(2); the affine slope compares eigenvalue ratios m = M^2 against l^2);
 (2) the generation sectors' torsion vanishes identically  <=>  the meridian is +-(longitude)^(+-s) along the curve
     (the curve lies in the Dehn filling of slope s)."""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import curve_engine as ce
from mpmath import mpf, nstr, acosh, eye, inverse
src = json.load(open(HERE / "exploration_census.json"))
out = []; tot = dict(backgrounds=0, slope_limit_ok=0, zero_type=0, filling_type=0, agree=0)
for b in src["backgrounds"]:
    name, k, ell = b["state"], b["k"], tuple(b["ell"]); eps = 1 if name[0] == "+" else -1
    B = ce.Background(eps, name[1:], k, ell); s = ce.slope(B.Phi, ell[0], ell[1], B.N)
    zero = any(c.startswith("('zero'") for c in b["classes"])
    def periph(e):
        p, g, T = B.point(e); lam = g[1] * g[2] * inverse(g[1]) * inverse(g[2]); return lam, T
    lam, T = periph("1e-10"); xl, xm = acosh(ce.tr(lam) / 2), acosh(ce.tr(T) / 2)
    ratio = xm / xl if abs(xm) > mpf(10) ** (-40) else mpf(0)
    lim_ok = abs(abs(ratio) - abs(s)) < mpf("1e-6") * max(1, abs(s))
    filling = False
    if abs(s - round(s)) < mpf("1e-20"):
        try:
            lam, T = periph("0.02"); n = int(round(s)); P = eye(2); li = inverse(lam)
            for _ in range(abs(n)): P = P * lam
            d = min(max(abs((T - sg * Q)[i, j]) for i in range(2) for j in range(2)) for sg in (1, -1) for Q in (P, inverse(P)))
            filling = d < mpf("1e-25")
        except AssertionError as e:
            filling = None
    rec = dict(state=name, k=k, ell=list(ell), slope=nstr(s, 12), cusp_shape_limit=nstr(abs(ratio), 12), slope_limit_ok=bool(lim_ok), zero_type=zero, filling_type=filling)
    out.append(rec); tot["backgrounds"] += 1; tot["slope_limit_ok"] += lim_ok; tot["zero_type"] += zero; tot["filling_type"] += bool(filling); tot["agree"] += (filling is not None and bool(filling) == zero)
    print(rec, flush=True)
print(json.dumps(tot)); json.dump(dict(totals=tot, backgrounds=out), open(HERE / "exploration_checks.json", "w"), indent=1)
