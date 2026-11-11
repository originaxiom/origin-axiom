#!/usr/bin/env python3
"""SM-C1, harvest row 1418 (the physical lane @ 9185cb169, SAME_ACTION_GAUGE_COMPLEX_AND_THRESHOLD_CANCELLATION_CONTROLS):
this seat's own check. Symbolic (sympy) where possible, 30-digit quadrature otherwise. Planted errors must be caught."""
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

t, s, k = sp.symbols("t s k", real=True)
a_const = sp.Symbol("a", real=True)
u, z1, z2 = (sp.Function(n)(t) for n in ("u", "z1", "z2"))
out = {}


def D(f, a):
    return sp.diff(f, t) + a * f


def Ddag(f, a):
    return -sp.diff(f, t) + a * f


def checks(a, kk):
    d0 = lambda f: (D(f, a), -kk * f)
    d1 = lambda g1, g2: kk * g1 + D(g2, a)
    d0dag = lambda g1, g2: Ddag(g1, a) - kk * g2
    d1dag = lambda f: (kk * f, Ddag(f, a))
    r = {}
    r["d1d0"] = sp.simplify(d1(*d0(u)))
    L = lambda f: -sp.diff(f, t, 2) + a ** 2 * f + kk ** 2 * f
    r["Delta0_minus_L"] = sp.simplify(d0dag(*d0(u)) - L(u))
    r["Delta2_minus_L"] = sp.simplify(d1(*d1dag(u)) - L(u))
    g = d0(d0dag(z1, z2)) if False else None
    A = d0(d0dag(z1, z2))
    Bv = d1dag(d1(z1, z2))
    r["Delta1_minus_diagL"] = [sp.simplify(A[0] + Bv[0] - L(z1)), sp.simplify(A[1] + Bv[1] - L(z2))]
    return r


# (1)-(2) at constant a, constant k
c = checks(a_const, k)
out["eq1_d1d0_constant"] = str(c["d1d0"])
out["eq2_constant_a"] = {k_: str(v) for k_, v in c.items() if k_ != "d1d0"}
# main's extension: a(t) varying, k constant -> d1 d0 = 0 still; Laplacians split into partners
a_t = sp.Function("a")(t)
v = checks(a_t, k)
out["varying_a_d1d0"] = str(v["d1d0"])
out["varying_a_residuals"] = {k_: str(val) for k_, val in v.items() if k_ != "d1d0"}
# (4) heat ratios 1:2:1 and the two alternating sums
H = sp.Symbol("H", positive=True)
tr = [H, 2 * H, H]
out["eq4_alt_sum"] = str(sp.simplify(sum((-1) ** p * tr[p] for p in range(3))))
out["eq4_p_weighted_alt_sum"] = str(sp.simplify(sum((-1) ** p * p * tr[p] for p in range(3))))
# (5) F_pair + F_ext = F_weak (the predecessor SM_PARALLEL_WEAK_WEIGHTED_MASS_THRESHOLDS.md eq. (4))
E = lambda c_: sp.exp(-sp.Rational(c_, 4) * s)
Fpair = 2 * E(5) + 6 * E(9) + 6 * E(13) + 4 * E(21) + 2 * E(25)
Fext = 6 * E(1) + 4 * E(9)
Fweak = 6 * E(1) + 2 * E(5) + 10 * E(9) + 6 * E(13) + 4 * E(21) + 2 * E(25)
out["eq5_sum_minus_Fweak"] = str(sp.simplify(Fpair + Fext - Fweak))
out["eq5_weights_at_0"] = [int(Fpair.subs(s, 0)), int(Fext.subs(s, 0)), int(Fweak.subs(s, 0))]
# (6) the determinant integral, 30 digits, three cases
mp.mp.dps = 30
cases = []
for mu, nu in ((mp.mpf("1.3"), mp.mpf("0.4")), (mp.mpf("2.7"), mp.mpf("2.2")), (mp.mpf("0.05"), mp.mpf("3"))):
    val = mp.quad(lambda p: mp.log((p ** 2 + mu ** 2) / (p ** 2 + nu ** 2)), [-mp.inf, 0, mp.inf]) / (2 * mp.pi)
    cases.append({"mu": str(mu), "nu": str(nu), "integral": mp.nstr(val, 25), "mu_minus_nu": mp.nstr(mu - nu, 25),
                  "abs_dev": mp.nstr(abs(val - (mu - nu)), 5)})
out["eq6_cases"] = cases
# the deciding check of (6), exact (sympy): integral over R of log((p^2+mu^2)/(p^2+nu^2)) dp / (2 pi) = mu - nu
pp = sp.Symbol("p", real=True)
mu_s, nu_s = sp.symbols("mu nu", positive=True)
exact = sp.simplify(sp.integrate(sp.log((pp ** 2 + mu_s ** 2) / (pp ** 2 + nu_s ** 2)), (pp, -sp.oo, sp.oo)) / (2 * sp.pi))
out["eq6_exact"] = str(exact)
# planted errors (must be caught)
kt = sp.Function("k")(t)
pl = checks(a_const, kt)
out["PLANTED_varying_k_d1d0_nonzero"] = str(pl["d1d0"])
Fbad = Fpair + Fext - 2 * E(9)
out["PLANTED_wrong_histogram_caught"] = bool(sp.simplify(Fbad - Fweak) != 0)
bad_tr = [H, 3 * H, H]
out["PLANTED_wrong_ratio_caught"] = bool(sp.simplify(sum((-1) ** p * bad_tr[p] for p in range(3))) != 0)
# POST HOC (written after the first run, disclosed): the first aggregate compared the list entry "[0, 0]" as the string
# "0" and held the quadrature to 1e-20, below what 30-digit quadrature reaches on infinite tails (about 1e-19); every value
# held. The aggregate now reads the list entry by entry, decides (6) by the exact integral, and keeps the quadrature as a
# read-out at 1e-15.
ok = (out["eq1_d1d0_constant"] == "0"
      and all(str(c["Delta0_minus_L"]) == "0" for _ in [0]) and str(c["Delta2_minus_L"]) == "0"
      and all(sp.simplify(x) == 0 for x in c["Delta1_minus_diagL"])
      and out["varying_a_d1d0"] == "0" and out["eq4_alt_sum"] == "0" and out["eq4_p_weighted_alt_sum"] == "0"
      and out["eq5_sum_minus_Fweak"] == "0" and out["eq6_exact"] == "mu - nu"
      and all(mp.mpf(c_["abs_dev"]) < mp.mpf("1e-15") for c_ in cases)
      and out["PLANTED_varying_k_d1d0_nonzero"] != "0" and out["PLANTED_wrong_histogram_caught"]
      and out["PLANTED_wrong_ratio_caught"])
out["all_claims_hold_and_plants_caught"] = bool(ok)
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
