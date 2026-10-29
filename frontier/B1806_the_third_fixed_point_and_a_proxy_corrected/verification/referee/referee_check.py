"""Referee check for the draft B1806 (near tau = i), INDEPENDENT of B1691's q-series code.

Evaluation route: theta functions by direct summation with exact tau-derivatives termwise (an earlier version used mpmath
jtheta via the heat equation; same values for Re tau in (-1, 1]); R, DR, D^2R by second-order jets;
E2 by its Lambert series, E2' by Ramanujan, E4, E6 by Lambert series. Masses by an SVD of Y(a) = aR^T + Ra^T - (a.R)1
(B1646's definition m = s2/s1), and also B1691's proxy s1 s2/(s1^2 + s2^2), which is what `at()` returns.
    python3 referee_check.py      # writes referee_check.json beside itself
"""
import json, pathlib, random
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 50
HERE = pathlib.Path(__file__).resolve().parent
I = mp.mpc(0, 1)
out = {}


class J:  # second-order jet (f, f', f'') in tau
    def __init__(s, a, b=0, c=0): s.a, s.b, s.c = mp.mpc(a), mp.mpc(b), mp.mpc(c)
    def __add__(s, o): o = o if isinstance(o, J) else J(o); return J(s.a + o.a, s.b + o.b, s.c + o.c)
    __radd__ = __add__
    def __neg__(s): return J(-s.a, -s.b, -s.c)
    def __sub__(s, o): return s + (-(o if isinstance(o, J) else J(o)))
    def __mul__(s, o):
        o = o if isinstance(o, J) else J(o)
        return J(s.a * o.a, s.a * o.b + s.b * o.a, s.a * o.c + 2 * s.b * o.b + s.c * o.a)
    __rmul__ = __mul__
    def inv(s): a, b, c = s.a, s.b, s.c; return J(1 / a, -b / a ** 2, 2 * b * b / a ** 3 - c / a ** 2)
    def __truediv__(s, o): return s * (o if isinstance(o, J) else J(o)).inv()


def theta(n, tau, M=400):
    """theta_n(tau) and its first two tau-derivatives by direct summation over m (no branch of q^(1/4) involved):
    theta2 = sum exp(i pi tau (m+1/2)^2), theta3 = sum exp(i pi tau m^2), theta4 = sum (-1)^m exp(i pi tau m^2)."""
    f = d1 = d2 = mp.mpc(0)
    for m in range(-M, M + 1):
        e = (m + mp.mpf(1) / 2) ** 2 if n == 2 else mp.mpf(m * m)
        w = mp.exp(I * mp.pi * tau * e) * ((-1) ** m if n == 4 else 1)
        if abs(w) < mp.mpf(10) ** -70 and abs(m) > 3: continue
        f += w; d1 += I * mp.pi * e * w; d2 += (I * mp.pi * e) ** 2 * w
    return J(f, d1, d2)


def lam(k, tau, N=400):
    q = mp.exp(2 * I * mp.pi * tau)
    return mp.fsum(n ** k * q ** n / (1 - q ** n) for n in range(1, N))


def E2(t): return 1 - 24 * lam(1, t)
def E4(t): return 1 + 240 * lam(3, t)
def E6(t): return 1 - 504 * lam(5, t)


def basis(tau):
    """R, DR, D^2R at tau (3-vectors of mpc), independent route."""
    t2, t3, t4 = theta(2, tau), theta(3, tau), theta(4, tau)
    den = J(mp.pi) * t2 * t3 * t4
    Rj = [-(t2 * t2) / den, -(t4 * t4) / den, J(I) * (t3 * t3) / den]
    e2, e4 = E2(tau), E4(tau)
    e2p = 2 * I * mp.pi * (e2 * e2 - e4) / 12
    tpi = 2 * I * mp.pi
    R = [r.a for r in Rj]
    DR = [r.b / tpi + e2 * r.a / 24 for r in Rj]
    DRp = [r.c / tpi + (e2p * r.a + e2 * r.b) / 24 for r in Rj]
    D2R = [DRp[i] / tpi - e2 * DR[i] / 8 for i in range(3)]
    return [R, DR, D2R]


dot = lambda u, v: sum(x * y for x, y in zip(u, v))
nrm = lambda u: sum(abs(x) ** 2 for x in u)


def masses(a, R):
    Y = mp.matrix(3, 3)
    aR = dot(a, R)
    for i in range(3):
        for j in range(3):
            Y[i, j] = a[i] * R[j] + R[i] * a[j] - (aR if i == j else 0)
    s = sorted([abs(x) for x in mp.svd_c(Y, compute_uv=False)], reverse=True)
    proxy = nrm(R) * abs(dot(a, a)) / (2 * nrm(R) * nrm(a) + 2 * abs(dot(a, [mp.conj(x) for x in R])) ** 2 - abs(aR) ** 2)
    return s, s[1] / s[0], proxy


# ---- 1. the convention: rho(S), rho(T) checked on R, DR, D2R at a generic tau ---------------------------------------
Lm = mp.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]); Pm = mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
rS = mp.exp(I * mp.pi / 4) * Pm
rT = mp.exp(I * mp.pi / 4) * Lm ** -1
t0 = mp.mpc(-0.45, 1.1)
b0, bS, bT = basis(t0), basis(-1 / t0), basis(t0 + 1)
chk = {}
for j, k in ((0, mp.mpf(-1) / 2), (1, mp.mpf(3) / 2), (2, mp.mpf(7) / 2)):
    v = mp.matrix(b0[j])
    lhsS, rhsS = mp.matrix(bS[j]), (t0 ** k) * (rS * v)
    lhsT, rhsT = mp.matrix(bT[j]), rT * v
    chk[["R", "DR", "D2R"][j]] = {"S: |a(-1/tau) - tau^k rho(S) a(tau)| / |a|": mp.nstr(mp.norm(lhsS - rhsS) / mp.norm(lhsS), 3),
                                  "T: |a(tau+1) - rho(T) a(tau)| / |a|": mp.nstr(mp.norm(lhsT - rhsT) / mp.norm(lhsT), 3)}
out["1_convention_checks_at_tau0"] = chk
# order of rho(S)
pw, order = mp.eye(3), None
for n in range(1, 17):
    pw = pw * rS
    if mp.norm(pw - mp.eye(3)) < mp.mpf(10) ** -40: order = n; break
out["1_rho_S_order"] = order
out["1_rho_S_squared_is_i_times_1"] = mp.nstr(mp.norm(rS * rS - I * mp.eye(3)), 3)
# eigenspaces of rho(S): simple (e_i - e_j)/sqrt2, eigenvalue -e^{i pi/4}; double span{(e_i + e_j)/sqrt2, e_k}
vs = [mp.sqrt(2) / 2, -mp.sqrt(2) / 2, 0]
out["1_simple_eigenline_vdotv"] = mp.nstr(dot(vs, vs), 5)  # 1: NOT isotropic
out["1_simple_eigenvalue"] = mp.nstr(mp.exp(I * mp.pi / 4) * -1, 8)
Ps = (mp.eye(3) - Pm) / 2; Pd = (mp.eye(3) + Pm) / 2

# ---- 2. at tau = i: where R, DR, D2R lie; the selection rule a(i) = i^k rho(S) a(i) -----------------------------------
bi = basis(I)
sel = {}
for j, k in ((0, mp.mpf(-1) / 2), (1, mp.mpf(3) / 2), (2, mp.mpf(7) / 2)):
    v = mp.matrix(bi[j])
    sel[["R", "DR", "D2R"][j]] = {"|simple part|/|v|": mp.nstr(mp.norm(Ps * v) / mp.norm(v), 3),
                                  "|double part|/|v|": mp.nstr(mp.norm(Pd * v) / mp.norm(v), 3),
                                  "predicted eigenvalue e^{-i pi k/2}": mp.nstr(mp.exp(-I * mp.pi * k / 2), 6),
                                  "|v.v|/|v|^2": mp.nstr(abs(dot(bi[j], bi[j])) / nrm(bi[j]), 3), "|v|": mp.nstr(mp.sqrt(nrm(bi[j])), 8)}
out["2_at_i"] = sel
out["2_R(i)_normalised"] = [mp.nstr(x / bi[0][0], 12) for x in bi[0]]
out["2_DR(i)_normalised"] = [mp.nstr(x / bi[1][0], 12) for x in bi[1]]
out["2_E4(i), E6(i)"] = [mp.nstr(E4(I), 15), mp.nstr(E6(I), 3)]

# cross-check against B1691's q-series evaluation (its ev()) at tau = i and at tau0
import sys, io, contextlib, importlib.util
Bdir = sorted(pathlib.Path(__file__).resolve().parents[3].glob("B1691_*"))[0] / "verification"
sys.path.insert(0, str(Bdir))
spec = importlib.util.spec_from_file_location("te", Bdir / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
mp.mp.dps = 50
dev = 0
for tau, bb in ((I, bi), (t0, b0)):
    for j in range(3):
        for c in range(3):
            x = te.ev(te.B[j][c], tau) / mp.pi   # B1691's code builds R without the 1/pi of its docstring: an overall scale, cancels in every ratio
            dev = max(dev, abs(x - bb[j][c]) / abs(bb[j][c]) if abs(bb[j][c]) > 1e-30 else abs(x))
out["2_max_rel_dev_from_B1691_qseries_over_pi"] = mp.nstr(dev, 3)


# ---- 3. the draft's own random sections, re-evaluated by this route; true m and the proxy --------------------------
def Mbasis(w):
    res = []
    for a in range(w // 4 + 1):
        for b in range(w // 6 + 1):
            if 4 * a + 6 * b == w: res.append((a, b))
    return res


def coeffs(n, seed):
    rng = random.Random(1000 * seed + n); cs = []
    for j in range(3):
        if 2 * n - 2 * j < 0: continue
        for ab in Mbasis(2 * n - 2 * j):
            re = F(rng.randint(-9, 9) or 1, rng.randint(1, 5)); im = F(rng.randint(-9, 9), rng.randint(1, 5))
            cs.append((j, ab, mp.mpc(mp.mpf(re.numerator) / re.denominator, mp.mpf(im.numerator) / im.denominator)))
    return cs


def section_at(cs, tau):
    b = basis(tau); e4, e6 = E4(tau), E6(tau)
    a = [mp.mpc(0)] * 3
    for j, (p, r), c in cs:
        f = c * e4 ** p * e6 ** r
        a = [a[i] + f * b[j][i] for i in range(3)]
    return a, b[0]


draft = json.loads((HERE / "near_i_draft_output.json").read_text())["near_i"]
C3 = {}
for n in range(0, 7):
    k = str(F(4 * n - 1, 2)); row = {}
    for seed in (1, 2):
        cs = coeffs(n, seed)
        a, R = section_at(cs, I)
        s, m, px = masses(a, R)
        rec = {"true_m2/m3_at_i": mp.nstr(m, 8), "proxy_at_i": mp.nstr(px, 8), "draft_value": draft[k]["seed%d" % seed]["m2/m3_at_omega"],
               "s3/s1": mp.nstr(s[2] / s[0], 3)}
        if n > 0:
            # closed form on the double eigenspace: singular values |a.R| and 2|a.conj R|
            aR, aRb = abs(dot(a, R)), 2 * abs(dot(a, [mp.conj(x) for x in R]))
            rec["closed_form_double: min/max(|a.R|, 2|a.Rbar|)"] = mp.nstr(min(aR, aRb) / max(aR, aRb), 8)
            rec["|simple part of a(i)|/|a(i)|"] = mp.nstr(mp.norm(Ps * mp.matrix(a)) / mp.norm(mp.matrix(a)), 3)
        # the approach in eps = |tau - i|, true m, e = 1..6, three directions
        dev = {}
        for th in (0.3, 1.9, 4.1):
            vals = []
            for e in (1, 2, 3, 4, 5, 6):
                ae, Re = section_at(cs, I + mp.mpf(10) ** -e * mp.exp(I * th))
                vals.append(masses(ae, Re)[1])
            dev[str(th)] = [mp.nstr(v, 8) for v in vals]
        rec["true_m_at_eps=1e-1..1e-6"] = dev
        row["seed%d" % seed] = rec
    C3[k] = row
out["3_draft_sections_true_vs_proxy"] = C3

# ---- 4. the closed form at i: simple eigenline -> m = 1 exactly; double eigenspace -> {|a.R|, 2|a.Rbar|} -------------
R = bi[0]
a = bi[1]  # weight 3/2 section DR
s, m, px = masses(a, R)
out["4_DR_at_i"] = {"singular_values": [mp.nstr(x, 15) for x in s], "true_m": mp.nstr(m, 20), "proxy": mp.nstr(px, 20),
                    "a.R": mp.nstr(abs(dot(a, R)), 3), "a.Rbar": mp.nstr(abs(dot(a, [mp.conj(x) for x in R])), 3)}
rng = random.Random(7); worst = 0
for _ in range(50):
    al, be = mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)), mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1))
    a = [al / mp.sqrt(2), al / mp.sqrt(2), be]
    s, m, _ = masses(a, R)
    pred = sorted([abs(dot(a, R)), 2 * abs(dot(a, [mp.conj(x) for x in R]))], reverse=True)
    worst = max(worst, abs(s[0] - pred[0]) / s[0], abs(s[1] - pred[1]) / s[0], s[2] / s[0])
out["4_double_eigenspace_closed_form_max_rel_err_50_random"] = mp.nstr(worst, 3)

# ---- 5. the non-generic sections at i: proximity hierarchies the draft's random sections miss -----------------------
def run(label, cs_fun):
    res = {}
    a, Ri = cs_fun(I); s, m0, _ = masses(a, Ri); res["true_m_at_i"] = mp.nstr(m0, 6)
    sl = []
    for th in (0.3, 1.9, 4.1):
        v = []
        for e in (4, 5, 6):
            ae, Re = cs_fun(I + mp.mpf(10) ** -e * mp.exp(I * th)); v.append(masses(ae, Re)[1])
        sl.append([round(float(mp.log(v[0] / v[1]) / mp.log(10)), 3), round(float(mp.log(v[1] / v[2]) / mp.log(10)), 3)])
    res["slopes_e4-5,e5-6_three_dirs"] = sl
    out["5_" + label] = res


def mk(terms):  # terms: list of (j, (p, r), coefficient)
    return lambda tau: section_at(terms, tau)


# (a) weight 15/2 with f2 = 0 (B1691's own 'no D2R' row): a = alpha E4^2 R + beta E6 DR
run("w15/2_f2=0", mk([(0, (2, 0), mp.mpc(1, 0.4)), (1, (0, 1), mp.mpc(-0.7, 1.3))]))
# (b) weight 23/2 with f2 = 0: a = alpha E4^3 R + gamma E6^2 R + beta E4 E6 DR
run("w23/2_f2=0", mk([(0, (3, 0), mp.mpc(0.8, -0.2)), (0, (0, 2), mp.mpc(0.3, 0.5)), (1, (1, 1), mp.mpc(1.1, 0.6))]))
# (c) weight 7/2, a = alpha E4 R + D2R with alpha tuned so that a(i) is proportional to conj R(i) (a.a(i) = 0)
d2, Ri, e4i = bi[2], bi[0], E4(I)
Rb = [mp.conj(x) for x in Ri]
# a(i) = alpha e4 R + d2 ; demand a(i).R(i)-component ... a(i) proportional to Rbar  <=>  a(i).Rbar(i) = 0
alpha_star = -dot(d2, Rb) / (e4i * dot(Ri, Rb))
out["5_w7/2_alpha_star"] = mp.nstr(alpha_star, 12)
run("w7/2_a(i)_on_conjR(i)", mk([(0, (1, 0), alpha_star), (2, (0, 0), mp.mpc(1))]))
# (d) the range at i over the weight-7/2 family: m(i) as alpha varies on a grid (true m)
grid = []
for re in (-3, -1, -0.3, 0, 0.3, 1, 3):
    for im in (-3, -1, 0, 1, 3):
        al = alpha_star * mp.mpc(1 + 0.0, 0) + mp.mpc(re, im) * abs(alpha_star)
        a = [al * e4i * Ri[c] + d2[c] for c in range(3)]
        grid.append(float(masses(a, Ri)[1]))
out["5_w7/2_m(i)_range_on_grid"] = [min(grid), max(grid)]
# the alpha giving exact degeneracy |a.R| = 2|a.Rbar| exists (m(i) = 1): a.R = d2.R fixed, a.Rbar = alpha e4 |R|^2 + d2.Rbar
target = abs(dot(d2, Ri)) / 2
alpha_deg = (target - dot(d2, Rb)) / (e4i * dot(Ri, Rb))
a = [alpha_deg * e4i * Ri[c] + d2[c] for c in range(3)]
out["5_w7/2_m(i)_at_alpha_deg"] = mp.nstr(masses(a, Ri)[1], 12)
# draft's seeds at 7/2: alpha/gamma there, and |alpha e4 R(i)| vs |D2R(i)|
out["5_|E4(i)R(i)|_over_|D2R(i)|"] = mp.nstr(abs(e4i) * mp.sqrt(nrm(Ri)) / mp.sqrt(nrm(d2)), 8)

# ---- 6. at omega: B1691's '1/2 (no hierarchy)' for k = 3/2 mod 6 is the proxy; the true ratio --------------------------
OM = mp.mpc(-0.5, mp.sqrt(3) / 2)
bo = basis(OM)
s, m, px = masses(bo[1], bo[0])
out["6_DR_at_omega"] = {"true_m": mp.nstr(m, 15), "proxy": mp.nstr(px, 15)}
for n in (4,):
    for seed in (1, 2):
        a, Ro = section_at(coeffs(n, seed), OM); s, m, px = masses(a, Ro)
        out["6_w15/2_seed%d_at_omega" % seed] = {"true_m": mp.nstr(m, 15), "proxy": mp.nstr(px, 15)}
# B1691's S163 addendum (the_principles_points): the proxy vs the true value for DR on tau = iy and on LR's geodesic
pp = {}
for y in (1, 1.25, 1.5, 2, 2.5, 3):
    b = basis(mp.mpc(0, y)); s, m, px = masses(b[1], b[0]); pp[str(y)] = {"true": mp.nstr(m, 6), "proxy": mp.nstr(px, 6)}
out["6_DR_along_iy_true_vs_proxy"] = pp
c, r = mp.mpf(1) / 2, mp.sqrt(5) / 2
geo_t, geo_p = [], []
for jj in range(1, 80):
    th = mp.pi * jj / 80; b = basis(mp.mpc(c + r * mp.cos(th), r * mp.sin(th))); s, m, px = masses(b[1], b[0])
    geo_t.append(float(m)); geo_p.append(float(px))
out["6_DR_on_LR_geodesic_true_min_max"] = [min(geo_t), max(geo_t)]
out["6_DR_on_LR_geodesic_proxy_min_max"] = [min(geo_p), max(geo_p)]

# ---- 7. B1697's a0 = D2R - E4 R/48 at the cusp (its 'm2/m3 -> 1/2'): true vs proxy; B1691's geodesic ends (truncation) --
cusp = {}
for y in (2, 3, 5):
    b = basis(mp.mpc(0.1, y)); a0 = [b[2][c] - E4(mp.mpc(0.1, y)) * b[0][c] / 48 for c in range(3)]
    s, m, px = masses(a0, b[0]); cusp[str(y)] = {"true": mp.nstr(m, 8), "proxy": mp.nstr(px, 8)}
out["7_B1697_a0_at_tau=0.1+iy"] = cusp
ends = {}
for jj in (1, 2, 4, 8, 40):
    th = mp.pi * jj / 80; tau = mp.mpc(c + r * mp.cos(th), r * mp.sin(th))
    b = basis(tau); s, m, px = masses(b[1], b[0])
    ends["theta=pi*%d/80 (Im tau=%s)" % (jj, mp.nstr(tau.imag, 3))] = {"true": mp.nstr(m, 6), "proxy_this_route": mp.nstr(px, 6),
                                                                      "B1691_qseries_proxy": mp.nstr(te.at(te.B[1], tau)[0], 6)}
out["7_DR_on_LR_geodesic_by_point"] = ends

if __name__ == "__main__":
    (HERE / "referee_check.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(json.dumps(out, indent=1, default=str))
