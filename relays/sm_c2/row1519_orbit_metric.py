#!/usr/bin/env python3
"""SM-C2, harvest row 1519 (PARALLEL_FLAVOUR_ORBIT_METRIC_AND_HEAVY_RESPONSE @ 0dc9e65f9): this seat's own exact check of
(3) N0 = Area kappa(Q0^dag Q0)/g6^2 = pi kappa(E^dag E)/(2 g6^2) = 10 pi/g6^2 with Q0 = E/2, Area = 2 pi, kappa(E^dag E) = 20
(defining-five trace of the principal triple); (5) (1/2)([Q0^dag,[Q0,t]] + [Q0,[Q0^dag,t]]) = t/2 for t = H/2, in the five
and in the ten; (6) kappa(H^2) = 2 kappa(E^dag E) and 2 N0/Z_t = 1, so the vector mass squared is one; (4) -> (7) the
minimising A = Im(z^dag dz) and the Fubini-Study form G = N0/(1+|c|^2)^2 = d dbar [N0 log(1+|c|^2)], the same in the chart
d = 1/c; (8) W = (1/2) kappa(q Dbar r - r Dbar q) is unchanged under r -> r + c q (c constant), pointwise, for random
matrices; the two hand controls of section 6: the positive (h1 = -l^2, h2 = l^2, r1 = r2 = c l, W_eff = 0,
K_eff = |l|^2 + |c|^2 + 2|l|^4 + 2|cl|^2) and the rejecting one (W_eff = -c l^3). Planted: dropping the shear term from
the positive control must make W_eff nonzero."""
import json
import random
import sys
from pathlib import Path

import sympy as sp

out = {}


def sl2(n):
    j = sp.Rational(n - 1, 2)
    H = sp.diag(*[2 * (m - j) for m in range(n)])
    E = sp.zeros(n)
    for m in range(n - 1):
        mm = m - j
        E[m + 1, m] = sp.sqrt((j - mm) * (j + mm + 1))
    return E, H


comm = lambda A, B: A * B - B * A
res = {}
for n in (5, 3, 4):
    E, H = sl2(n)
    assert comm(E, E.H) == H and comm(H, E) == 2 * E
    Q0, t = E / 2, H / 2
    lhs = (comm(Q0.H, comm(Q0, t)) + comm(Q0, comm(Q0.H, t))) / 2
    res[f"dim{n}"] = {"(5)_eq_t/2": sp.simplify(lhs - t / 2) == sp.zeros(n),
                      "kappa(H^2)=2kappa(EdagE)": sp.simplify((H * H).trace() - 2 * (E.H * E).trace()) == 0}
E5, H5 = sl2(5)
kEE = (E5.H * E5).trace()
g6 = sp.Symbol("g6", positive=True)
area = 2 * sp.pi
N0 = area * (E5.H * E5).trace() / 4 / g6 ** 2
Zt = area * ((H5 / 2) ** 2).trace() / g6 ** 2
res["kappa(EdagE)_five"] = str(kEE)
res["N0"] = str(sp.simplify(N0))
res["2N0/Zt"] = str(sp.simplify(2 * N0 / Zt))
ok3_6 = (kEE == 20 and sp.simplify(N0 - 10 * sp.pi / g6 ** 2) == 0 and sp.simplify(2 * N0 / Zt) == 1
         and all(all(v.values()) for k, v in res.items() if k.startswith("dim")))
# (7): z = (1, c)/sqrt(1+|c|^2), c = x + i y; L = |dz|^2 - |z^dag dz|^2 on a tangent vector
x, y, vx, vy = sp.symbols("x y v_x v_y", real=True)
c = x + sp.I * y
nrm = sp.sqrt(1 + x ** 2 + y ** 2)
z = sp.Matrix([1, c]) / nrm
dz = z.diff(x) * vx + z.diff(y) * vy
zd = (z.H * dz)[0]
L = sp.simplify((dz.H * dz)[0] - sp.expand_complex(zd * sp.conjugate(zd)))
G = 1 / (1 + x ** 2 + y ** 2) ** 2
fs_ok = sp.simplify(L - G * (vx ** 2 + vy ** 2)) == 0
# the minimising A: |dz - i A z|^2 minimised over real A at A = Im(z^dag dz)
A = sp.Symbol("A", real=True)
f = sp.expand_complex(((dz - sp.I * A * z).H * (dz - sp.I * A * z))[0])
Amin = sp.solve(sp.diff(sp.simplify(f), A), A)
A_ok = len(Amin) == 1 and sp.simplify(Amin[0] - sp.im(sp.expand_complex(zd))) == 0
re_zero = sp.simplify(sp.re(sp.expand_complex(zd))) == 0
# Kaehler potential: d dbar log(1+|c|^2) = (1/4) Laplacian in x, y
K = sp.log(1 + x ** 2 + y ** 2)
kahler_ok = sp.simplify((sp.diff(K, x, 2) + sp.diff(K, y, 2)) / 4 - G) == 0
# chart d = 1/c: pull the metric back
u, v = sp.symbols("u v", real=True)
cc = 1 / (u + sp.I * v)
X, Y = sp.re(sp.expand_complex(cc)), sp.im(sp.expand_complex(cc))
Jm = sp.Matrix([[sp.diff(X, u), sp.diff(X, v)], [sp.diff(Y, u), sp.diff(Y, v)]])
g_pull = sp.simplify(Jm.T * (G.subs({x: X, y: Y}) * sp.eye(2)) * Jm)
chart_ok = sp.simplify(g_pull - sp.eye(2) / (1 + u ** 2 + v ** 2) ** 2) == sp.zeros(2)
res.update({"(7)_FS": fs_ok, "(4)_A=Im(zdag dz)": A_ok, "Re(zdag dz)=0": re_zero, "(7)_Kahler": kahler_ok,
            "(7)_chart_d": chart_ok})
# (8) shear invariance with random matrices
random.seed(1519)
rm = lambda: sp.Matrix(4, 4, lambda i, j: sp.Rational(random.randint(-5, 5), random.randint(1, 3)))
q, r, Dq, Dr = rm(), rm(), rm(), rm()
cst = sp.Rational(3, 7)
kap = lambda P, Q_: (P * Q_).trace()
W = lambda qq, rr, Dqq, Drr: (kap(qq, Drr) - kap(rr, Dqq)) / 2
shear_ok = W(q, r + cst * q, Dq, Dr + cst * Dq) == W(q, r, Dq, Dr)
res["(8)_shear"] = shear_ok
# section 6 controls
l, cc_, h1, h2, r1, r2, rho, h = sp.symbols("l c h1 h2 r1 r2 rho h")


def eliminate(Wf, heavy):
    sol = sp.solve([sp.diff(Wf, v_) for v_ in heavy], heavy, dict=True)
    return sol, [sp.simplify(Wf.subs(s)) for s in sol]


Wpos = r1 * (h1 + l ** 2) + r2 * (h2 - l ** 2) - cc_ * l * (h1 + h2)
solp, Weff_p = eliminate(Wpos, [h1, h2, r1, r2])
lb, cb = sp.symbols("lb cb")
s0 = solp[0]
Keff = sp.expand(l * lb + cc_ * cb + s0[h1] * s0[h1].subs({l: lb}) + s0[h2] * s0[h2].subs({l: lb})
                 + s0[r1] * s0[r1].subs({l: lb, cc_: cb}) + s0[r2] * s0[r2].subs({l: lb, cc_: cb}))
Keff_ok = sp.expand(Keff - (l * lb + cc_ * cb + 2 * l ** 2 * lb ** 2 + 2 * cc_ * cb * l * lb)) == 0
Wrej = rho * (h + l ** 2) + cc_ * l * h
solr, Weff_r = eliminate(Wrej, [h, rho])
res.update({"positive_solution": {str(k): str(v) for k, v in s0.items()}, "positive_W_eff": str(Weff_p),
            "positive_K_eff_ok": Keff_ok, "rejecting_W_eff": str(Weff_r)})
ctrl_ok = (Weff_p == [0] and s0 == {h1: -l ** 2, h2: l ** 2, r1: cc_ * l, r2: cc_ * l} and Keff_ok
           and Weff_r == [-cc_ * l ** 3])
Wbad = r1 * (h1 + l ** 2) + r2 * (h2 - l ** 2) - cc_ * l * h1
_, Weff_bad = eliminate(Wbad, [h1, h2, r1, r2])
out.update(res)
out["PLANTED_shear_dropped_W_eff"] = str(Weff_bad)
out["PLANTED_caught"] = Weff_bad != [0]
ok = ok3_6 and fs_ok and A_ok and re_zero and kahler_ok and chart_ok and shear_ok and ctrl_ok
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
