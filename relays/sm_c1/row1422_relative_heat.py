#!/usr/bin/env python3
"""SM-C1, harvest row 1422 (RELATIVE_HEAT_ADMISSION_AND_SCALE_DEPENDENCE @ e78a9be08): this seat's own check of
(3) Z(0) = -h, (4) L_rel(cP) = L_rel(P) - h log c and (7) I(mu) = L_rel(P) + h log mu^2, through the integral
representations (2) and (5) -- not through closed forms -- on finite relative spectra with zero modes, at 30 digits.
Model: operators P_q (q in a three-charge roster) and P_0 of equal dimension; r_q(s) = Tr e^{-sP_q} - Tr e^{-sP_0};
R = sum c_q r_q with sum c_q = 0 (so R(0) = 0); h = sum c_q (dim ker P_q - dim ker P_0).
Planted: a roster of unequal dimensions (R(0) != 0) must break Z(0) = -h."""
import json
import random
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 30


def model(seed, equal_dims=True):
    rng = random.Random(seed)
    N = 6
    def spec(nzero, n):
        return [mp.mpf(0)] * nzero + [mp.mpf(rng.uniform(0.3, 4.0)) for _ in range(n - nzero)]
    P0 = spec(1, N)
    Ps = {q: spec(rng.choice([0, 1, 2, 3]), N if equal_dims else N + q) for q in (1, 2, 3)}
    c = {1: mp.mpf(rng.uniform(-2, 2)), 2: mp.mpf(rng.uniform(-2, 2))}
    c[3] = -c[1] - c[2]
    return P0, Ps, c


def R_of(P0, Ps, c, scale=1):
    tr = lambda sp_, s: mp.fsum(mp.e ** (-s * scale * lam) for lam in sp_)
    return lambda s: mp.fsum(c[q] * (tr(Ps[q], s) - tr(P0, s)) for q in Ps)


def h_of(P0, Ps, c):
    z = lambda sp_: sum(1 for lam in sp_ if lam == 0)
    return mp.fsum(c[q] * (z(Ps[q]) - z(P0)) for q in Ps)


def Zfun(R, h):
    R0 = R(mp.mpf(0))
    def F(z):
        a = mp.quad(lambda s: s ** (z - 1) * (R(s) - R0), [0, 1])
        b = mp.quad(lambda s: s ** (z - 1) * (R(s) - h), [1, mp.inf])
        return a + (R0 - h) / z + b
    return lambda z: F(z) / mp.gamma(z)


def L_rel(R, h):
    Z = Zfun(R, h)
    return -mp.diff(Z, mp.mpf("1e-12") * 0 + mp.mpf(0), 1) if False else -(Z(mp.mpf("1e-8")) - Z(mp.mpf("-1e-8"))) / mp.mpf("2e-8")


def Z0(R, h):
    Z = Zfun(R, h)
    return (Z(mp.mpf("1e-10")) + Z(mp.mpf("-1e-10"))) / 2


def I_of(R, h, mu):
    f = lambda s: (R(s) - h * (1 - mp.e ** (-mu ** 2 * s))) / s
    return -mp.quad(f, [0, 1, mp.inf])


out = {"cases": []}
ok = True
for seed in (1422, 2024, 7):
    P0, Ps, c = model(seed)
    R, h = R_of(P0, Ps, c), h_of(P0, Ps, c)
    z0 = Z0(R, h)
    L = L_rel(R, h)
    cfac = mp.mpf("2.7")
    Rc = R_of(P0, Ps, c, scale=cfac)
    Lc = L_rel(Rc, h)
    mus = [mp.mpf("0.6"), mp.mpf("1.9")]
    Is = [I_of(R, h, m) for m in mus]
    rec = {"seed": seed, "h": mp.nstr(h, 12), "R(0)": mp.nstr(R(mp.mpf(0)), 5),
           "Z0_plus_h": mp.nstr(z0 + h, 5),
           "Lc_minus_(L - h log c)": mp.nstr(Lc - (L - h * mp.log(cfac)), 5),
           "I(mu)_minus_(L + h log mu^2)": [mp.nstr(Im - (L + h * mp.log(m ** 2)), 5) for Im, m in zip(Is, mus)]}
    tol = mp.mpf("1e-6")   # numerical differentiation at step 1e-8 with 30-digit quadrature
    good = (abs(z0 + h) < tol and abs(Lc - (L - h * mp.log(cfac))) < tol
            and all(abs(Im - (L + h * mp.log(m ** 2))) < tol for Im, m in zip(Is, mus)))
    rec["holds"] = bool(good)
    ok &= good
    out["cases"].append(rec)
# planted: unequal dimensions, R(0) != 0 -> Z(0) = R(0) - h, not -h
P0, Ps, c = model(1422, equal_dims=False)
R, h = R_of(P0, Ps, c), h_of(P0, Ps, c)
z0 = Z0(R, h)
out["PLANTED_unequal_dims"] = {"R(0)": mp.nstr(R(mp.mpf(0)), 8), "Z0_plus_h": mp.nstr(z0 + h, 8),
                               "caught": bool(abs(z0 + h) > mp.mpf("1e-3"))}
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_unequal_dims"]["caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
