"""The side identity (DESIGN section 7): a0 = D^2 R - E4 R/48 (B1697) against eta^4 F_-2 / 6 (B1730's F_-2, eps = +1).
(1) EXACT, in B1691's own q-series machinery (copied: x = q^(1/8), Gaussian-rational coefficients, to x^240 = q^30):
    48 a0 == (th2 th3 th4)^3 (th2^-2, th4^-2, i th3^-2) = (th2 th3^3 th4^3, th2^3 th3^3 th4, i th2^3 th3 th4^3);
(2) numerically with the referee's independent forms (Serre derivatives by numerical differentiation, holomorphic eta by
    the product), at points with |Re tau| > 1 too;
(3) the ratio a0 / F_-2 in four conventions for F_-2, to locate main's mismatch:
    (a) B1730's F_-2 = eta^5 (th2^-2, th4^-2, i th3^-2) with Dedekind eta  -> eta^4/6
    (b) B1810's direction function (th2^-2, th4^-2, i th3^-2), no eta       -> eta^9/6 = (th2 th3 th4)^3/48
    (c) the draft's model.py convention |eta|^5 (th2^-2, ...)               -> eta^9/(6 |eta|^5) (a phase off |eta|^4/6)
    (d) eta^5 with eta = principal cube root of th2 th3 th4 / 2             -> differs from (a) by a cube root of unity
(4) the theta derivatives used in the referee's hand proof: D log th2 = (E2 + th3^4 + th4^4)/24,
    D log th3 = (E2 + th2^4 - th4^4)/24, D log th4 = (E2 - th2^4 - th3^4)/24 (D = q d/dq)."""
import sys, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp
from fractions import Fraction as Fr
import qseries_B1691_copy as qs
import ref_model as rm

out = {}
# (1) exact
S = qs.S
th2, th3, th4 = qs.theta2(), qs.theta3(1), qs.theta3(-1)
di = (th2 * th3 * th4).inv()
R = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * S.c(0, 1) * di]
e2, e4 = qs.E2(), qs.E4()
DR = [qs.serre(c, Fr(-1, 2), e2) for c in R]
D2R = [qs.serre(c, Fr(3, 2), e2) for c in DR]
a0 = [d + S.c(Fr(-1, 48)) * e4 * r for d, r in zip(D2R, R)]
P = th2 * th3 * th4
P3 = P * P * P
rhs = [P3 * (th2 * th2).inv() * S.c(Fr(1, 48)), P3 * (th4 * th4).inv() * S.c(Fr(1, 48)),
       P3 * (th3 * th3).inv() * S.c(0, Fr(1, 48))]
alt = [th2 * th3 * th3 * th3 * th4 * th4 * th4 * S.c(Fr(1, 48)), th2 * th2 * th2 * th3 * th3 * th3 * th4 * S.c(Fr(1, 48)),
       th2 * th2 * th2 * th3 * th4 * th4 * th4 * S.c(0, Fr(1, 48))]
NMAX = 200      # compare below the truncation's reach (products of inverses lose nothing below x^N for these orders)
def diff_ok(u, v):
    d = u - v
    return all(k > NMAX for k in d.d)
out["exact_qseries_a0_equals_P3_over_48_times_theta_minus2"] = [diff_ok(a, b) for a, b in zip(a0, rhs)]
out["exact_qseries_a0_equals_th2th3^3th4^3_etc_over_48"] = [diff_ok(a, b) for a, b in zip(a0, alt)]
out["exact_compared_up_to_x_power"] = NMAX
out["a0_leading_terms"] = [{str(k): [str(c.d[k][0]), str(c.d[k][1])] for k in sorted(c.d)[:2]} for c in a0]

# (2), (3) numerics
mp.mp.dps = 30
def serre_num(fvec, k, tau):
    """Serre derivative of a vector function of weight k, numerically"""
    E2 = rm.eisenstein(tau)[0]
    return [mp.diff(lambda t, j=j: fvec(t)[j], tau) / (2j * mp.pi) - mp.mpf(k) / 12 * E2 * fvec(tau)[j] for j in range(3)]
def a0_num(tau):
    D2 = serre_num(lambda t: rm.DRvec(t), mp.mpf(3) / 2, tau)
    E4 = rm.eisenstein(tau)[1]; Rv = rm.Rvec(tau)
    return [D2[j] - E4 * Rv[j] / 48 for j in range(3)]
rows = []
for tau in (mp.mpc("0.17", "1.23"), mp.mpc("1.7", "0.9"), mp.mpc("-2.3", "1.4"), mp.mpc("0.5", "0.87"), mp.mpc("0.05", "2.6")):
    mp.mp.dps = 40
    A = a0_num(tau)
    mp.mp.dps = 30
    t2, t3, t4 = rm.thetas(tau); et = rm.eta(tau)
    vec = [t2 ** -2, t4 ** -2, 1j * t3 ** -2]
    Fm2_a = [et ** 5 * c for c in vec]                                   # (a)
    Fm2_b = vec                                                           # (b)
    Fm2_c = [abs(et) ** 5 * c for c in vec]                              # (c)
    etp = mp.cbrt(t2 * t3 * t4 / 2)                                      # principal cube root
    Fm2_d = [etp ** 5 * c for c in vec]                                  # (d)
    P3n = (t2 * t3 * t4) ** 3 / 48
    rat = lambda F: [A[j] / F[j] for j in range(3)]
    ra, rb, rc, rd = rat(Fm2_a), rat(Fm2_b), rat(Fm2_c), rat(Fm2_d)
    row = dict(tau=str(tau),
               a0_vs_P3_over_48_theta_m2=float(max(abs(A[j] - P3n * vec[j]) / abs(A[j]) for j in range(3))),
               ratio_spread_a=float(max(abs(ra[j] - ra[0]) for j in range(3)) / abs(ra[0])),
               a_ratio_over_eta4_6=[float(mp.re(ra[0] / (et ** 4 / 6))), float(mp.im(ra[0] / (et ** 4 / 6)))],
               b_ratio_over_eta9_6=[float(mp.re(rb[0] / (et ** 9 / 6))), float(mp.im(rb[0] / (et ** 9 / 6)))],
               b_ratio_over_eta4_6=[float(mp.re(rb[0] / (et ** 4 / 6))), float(mp.im(rb[0] / (et ** 4 / 6)))],
               c_ratio_over_abseta4_6=[float(mp.re(rc[0] / (abs(et) ** 4 / 6))), float(mp.im(rc[0] / (abs(et) ** 4 / 6)))],
               d_ratio_over_eta4_6=[float(mp.re(rd[0] / (et ** 4 / 6))), float(mp.im(rd[0] / (et ** 4 / 6)))],
               d_ratio_over_etap4_6=[float(mp.re(rd[0] / (etp ** 4 / 6))), float(mp.im(rd[0] / (etp ** 4 / 6)))],
               eta_true_over_principal_cuberoot=[float(mp.re(et / etp)), float(mp.im(et / etp))])
    # (4) theta derivative formulas
    E2 = rm.eisenstein(tau)[0]
    def dlog(k):
        return mp.diff(lambda t: mp.log(rm.thetas(t)[k]), tau) / (2j * mp.pi)
    row["theta_dlog_formula_devs"] = [float(abs(dlog(0) - (E2 + t3 ** 4 + t4 ** 4) / 24)), float(abs(dlog(1) - (E2 + t2 ** 4 - t4 ** 4) / 24)),
                                      float(abs(dlog(2) - (E2 - t2 ** 4 - t3 ** 4) / 24))]
    rows.append(row)
    print(json.dumps(row), flush=True)
out["numeric"] = rows
out["identity"] = ("a0 = D^2 R - E4 R / 48 = (1/48)(th2 th3^3 th4^3, th2^3 th3^3 th4, i th2^3 th3 th4^3) "
                   "= (eta^9/6)(th2^-2, th4^-2, i th3^-2) = eta^4 F_-2 / 6, with eta the Dedekind eta (eta^3 = th2 th3 th4 / 2) "
                   "and F_-2 = eta^5 (th2^-2, th4^-2, i th3^-2) (B1730, eps = +1); componentwise a0_k = -(1/48) R_k x "
                   "(th3^4 th4^4, th2^4 th3^4, -th2^4 th4^4)")
(HERE / "t_a0.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: v for k, v in out.items() if k != "numeric"}, indent=1))
