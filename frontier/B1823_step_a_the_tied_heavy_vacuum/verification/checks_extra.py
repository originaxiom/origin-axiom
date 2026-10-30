"""STEP A v2 -- extra checks (data-free): python3 -I checks_extra.py -> checks_extra.json
 1  F'' = 2 log(1 + m0^2/u) > 0 (sympy), and u* against mu^2 (leading order only)
 2  an explicit weight / character assignment making every superpotential term of every copy invariant
 3  the cross product Y1 x Y2 of two triplets is itself covariant (weight 3): (Y1 x Y2)(gamma tau) ~ O(gamma) (Y1 x Y2)(tau)
 4  the n = 2 zero-mixing direction F_2 x F_6 against the record's declared directions (DR, a0, R, F_a): not proportional
 5  a side identity: a0 = D^2 R - E4 R/48 equals eta^4 F_-2 / 6 identically (B1809/B1810 record "a0 = F_-2" at tau = i only):
    the component ratios a0_k / (eta^4 F_-2,k) are 1/6 at every tau tested (holomorphic eta here, not |eta|)
"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np
import sympy as sp
import mpmath as mp
from fractions import Fraction as Fr
from model import Triplet, mp_form_values, mp_triplet, LINV, PMAT
from search import SINGLET_LIST, MENU_Z, MENU_H, u_star

mp.mp.dps = 30
out = {}

# 1 ------------------------------------------------------------------------------------------------------------------
u, m, mu = sp.symbols("u m mu", positive=True)
F = (u + m) ** 2 * (sp.log((u + m) / mu) - sp.Rational(3, 2)) - u ** 2 * (sp.log(u / mu) - sp.Rational(3, 2))
F2 = sp.simplify(sp.diff(F, u, 2) - 2 * sp.log(1 + m / u))
F2b = sp.simplify(sp.expand_log(F2, force=True))
out["F_second_derivative_minus_2log(1+m0^2/u)"] = str(F2b)
out["u_star_over_mu2"] = {str(r): u_star(1.0, r) for r in (0.001, 0.01, 0.1)}

# 2 ------------------------------------------------------------------------------------------------------------------
# weights: k_L + k_Lbar = w_L, k_E + k_Ebar = w_E, k_H + k_L + k_Ebar = w_3; one k_H for all copies.
# characters (powers of chi_eta, mod 24; the triplet pairing H^T Y3 carries chi_eta^(r_3 + r_H) with r_3 = 2a for F_a,
# 0 for DR, and r_H the Higgs's own twist): c_L + c_Lbar + s_L = 0, c_E + c_Ebar + s_E = 0, c_L + c_Ebar + r_3 + r_H = 0.
def wt(s, p, r):
    return Fr(s, 2) + 4 * p + 6 * r
rows = []
kH = Fr(0); rH = 0
for menu, trip in (("Z", MENU_Z), ("H", MENU_H)):
    for i in range(8):
        sL, sE = SINGLET_LIST[2 * i], SINGLET_LIST[2 * i + 1]
        wL, wE = wt(*sL), wt(*sE); w3 = Fr(3, 2)
        kind, a = trip[i]; r3 = (2 * a) % 24 if kind == "F" else 0
        kL = Fr(0); kLb = wL - kL; kEb = w3 - kH - kL; kE = wE - kEb
        cL = 0; cLb = (-cL - sL[0]) % 24; cEb = (-cL - r3 - rH) % 24; cE = (-cEb - sE[0]) % 24
        ok = (kL + kLb == wL and kE + kEb == wE and kH + kL + kEb == w3 and (cL + cLb + sL[0]) % 24 == 0
              and (cE + cEb + sE[0]) % 24 == 0 and (cL + cEb + r3 + rH) % 24 == 0)
        rows.append(dict(menu=menu, copy=i + 1, w_L=str(wL), w_E=str(wE), w_3=str(w3),
                         k=dict(L=str(kL), Lbar=str(kLb), E=str(kE), Ebar=str(kEb), H=str(kH)),
                         chi_eta_power=dict(L=cL, Lbar=cLb, E=cE, Ebar=cEb, H=rH, Y_L=sL[0], Y_E=sE[0], Y3=r3), invariant=ok))
out["weight_character_assignment"] = dict(rows=rows, all_invariant=all(r["invariant"] for r in rows),
                                          note="one solution of the linear conditions (k_H = 0, r_H = 0, k_L = 0, c_L = 0); "
                                               "the family of solutions is affine; hypercharges: H L Ebar = -1/2 - 1/2 + 1")

# 3 ------------------------------------------------------------------------------------------------------------------
def vec(T, tau):
    v, f = mp_triplet(T, mp_form_values(tau)); return [f * c for c in v]
def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
def proj_dev(u_, v_):
    """1 - |<u, v>| / (|u||v|): zero iff proportional"""
    ip = abs(sum(mp.conj(x) * y for x, y in zip(u_, v_)))
    return 1 - ip / (mp.sqrt(sum(abs(x) ** 2 for x in u_)) * mp.sqrt(sum(abs(x) ** 2 for x in v_)))
T2, T6 = Triplet("F", 2), Triplet("F", 6)
tau = mp.mpc("0.17", "1.23")
c0 = cross(vec(T2, tau), vec(T6, tau))
cT = cross(vec(T2, tau + 1), vec(T6, tau + 1)); cS = cross(vec(T2, -1 / tau), vec(T6, -1 / tau))
Lm = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]; Pm = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
app = lambda M, v: [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]
out["cross_F2_F6_covariant"] = dict(T_dev=float(proj_dev(cT, app(Lm, c0))), S_dev=float(proj_dev(cS, app(Pm, c0))))
# modulus: |cross(gamma tau)| (2 Im gamma tau)^(3/2 + 3/2) invariant (weight 3)
nrm = lambda v, t: mp.power(2 * mp.im(t), 3) * sum(abs(x) ** 2 for x in v)
out["cross_F2_F6_weight3_norm_invariant"] = dict(T=float(nrm(cT, tau + 1) / nrm(c0, tau) - 1),
                                                 S=float(nrm(cS, -1 / tau) / nrm(c0, tau) - 1))

# 4 ------------------------------------------------------------------------------------------------------------------
def R_vec(tau):
    th = mp_form_values(tau)[0]; t2, t3, t4 = th; d = t2 * t3 * t4
    return [-t2 ** 2 / d, -t4 ** 2 / d, 1j * t3 ** 2 / d]
decl = {"DR": lambda t: vec(Triplet("DR"), t), "a0": lambda t: vec(Triplet("A0"), t), "R": R_vec}
for a in (-10, -6, -2, 2, 6, 10, 14, 18, 22, 26):
    decl["F_%d" % a] = (lambda aa: (lambda t: vec(Triplet("F", aa), t)))(a)
taus = [mp.mpc("0.5", "1.244"), mp.mpc("0.5", "2.0"), mp.mpc("0.21", "1.37")]
cmp = {}
for name, f in decl.items():
    cmp[name] = [float(proj_dev(cross(vec(T2, t), vec(T6, t)), f(t))) for t in taus]
out["F2xF6_vs_declared_directions_1_minus_overlap"] = dict(taus=[str(t) for t in taus], dev=cmp,
                                                           min_dev=min(min(v) for v in cmp.values()))
# 5 ------------------------------------------------------------------------------------------------------------------
def eta_h(tau):
    return mp.exp(2j * mp.pi * tau / 24) * mp.fprod(1 - mp.exp(2j * mp.pi * tau * n) for n in range(1, 400))
dev5 = []
for tau in [mp.mpc("0", "1"), mp.mpc("0.5", "1.244"), mp.mpc("0.21", "1.37"), mp.mpc("-0.33", "0.97"), mp.mpc("0.05", "2.6"),
            mp.mpc("0.45", "0.9")]:
    fv = mp_form_values(tau); th = fv[0]; t2, t3, t4 = th; e = eta_h(tau)
    va, fa = mp_triplet(Triplet("A0"), fv)
    a0 = [c * fa * abs(t2 * t3 * t4) / (t2 * t3 * t4) for c in va]          # restore the holomorphic 1/(2 eta^3)
    Fm2 = [e ** 5 * c for c in (t2 ** -2, t4 ** -2, 1j * t3 ** -2)]          # B1730's F_-2 (eps = 1)
    dev5.append(float(max(abs(a0[k] / (e ** 4 * Fm2[k]) - mp.mpf(1) / 6) for k in range(3))))
out["a0_equals_eta4_Fm2_over_6"] = dict(max_abs_dev_of_ratio_from_1_6=max(dev5), per_tau=dev5,
                                        consequence="a0 and F_-2 define the same direction at every tau: B1810's thirteen "
                                                    "declared directions hold twelve distinct ones (its a0 and F_-2 rows agree "
                                                    "to 1.6e-16 in every mass ratio; |V| differs only where V is undefined)")
(HERE / "checks_extra.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
print(json.dumps({k: (v if k != "weight_character_assignment" else {"all_invariant": v["all_invariant"]}) for k, v in out.items()}, indent=1, default=str))
