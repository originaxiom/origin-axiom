"""P-227, part 1 -- THE EXPONENTS AT THE TWO FIXED POINTS: for a Higgs whose direction in M is a covariant section of the
matter's representation rho_R (the tagged hypothesis H-cov; what fixes the direction is P-115), the leading exponents of
the record's mass ratios near the cusp (in |q|) and near omega (in |tau - omega|).  Mathematics only; no data.

The record's formulas (main's own arcs): the coupling Y(a) = a R^T + R a^T - (a.R) 1 with the theta triplet
R = (-th2^2, -th4^2, i th3^2)/(pi th2 th3 th4) (B1645); the massive pair's singular values s1 >= s2 with
s1 s2 = |R|^2 |a.a| and s1^2 + s2^2 = 2|R|^2|a|^2 + 2|a.conj R|^2 - |a.R|^2 (B1646 D3); the first generation's lift
L m1/m3 = |a.a||D||a.R|/(2 pi s1^2 s2) (B1654), so m1 = |D||a.R|/(2 pi L |R|^2); D's laws: D/(q_B|R|^2) -> 8 pi^2 Im tau
+ const at the cusp with q_B = e^{i pi tau} the nome (B1654's convention, its line q = exp(-pi y); here q = e^{2 pi i tau}), D vanishing linearly at omega (B1654); L of order one at both (B1667).  Here m3 = s1, m2 = s2.

Sections: rho_R's forms are a free module over M_*(SL2Z) on R (weight -1/2), DR, D^2R (Serre derivatives; checked
here by the Wronskian); at weight k = 2n - 1/2 a section is f0 R + f1 DR + f2 D^2R with f_j in M_{2n-2j}.
    python3 the_exponents.py      # writes the_exponents.json beside itself
"""
import json, math, pathlib, random
from fractions import Fraction as F
import mpmath as mp
from qseries import S, theta2, theta3, E2, E4, E6, serre

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 40
out = {}

th2, th3, th4 = theta2(), theta3(1), theta3(-1)
di = (th2 * th3 * th4).inv()
R = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * S.c(0, 1) * di]
e2, e4, e6 = E2(), E4(), E6()
B = [R, [serre(c, F(-1, 2), e2) for c in R]]
B.append([serre(c, F(3, 2), e2) for c in B[1]])
dot = lambda u, v: u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
nrm = lambda u: u[0] * u[0].conj() + u[1] * u[1].conj() + u[2] * u[2].conj()
fr = lambda p: [str(p[0]), str(p[1])]


def Mbasis(w):
    res = []
    for a in range(w // 4 + 1):
        for b in range(w // 6 + 1):
            if 4 * a + 6 * b == w:
                f = S.c(1)
                for _ in range(a): f = f * e4
                for _ in range(b): f = f * e6
                res.append(f)
    return res


# ---- C1: the identities and the basis -------------------------------------------------------------------------------
RR, RDR, DRDR, RD2R = dot(B[0], B[0]), dot(B[0], B[1]), dot(B[1], B[1]), dot(B[0], B[2])
det = (B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1]) - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0])
       + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]))
eta9 = th2 * th3 * th4 * th2 * th3 * th4 * th2 * th3 * th4          # = 8 eta^9
ratio = det * eta9.inv()
out["C1"] = {"R.R_identically_0": RR.ord() is None or RR.ord() > 200, "R.DR_identically_0": RDR.ord() is None or RDR.ord() > 200,
             "R.D2R_plus_DR.DR_identically_0": (RD2R + DRDR).ord() is None or (RD2R + DRDR).ord() > 200,
             "DR.DR_order_in_x": DRDR.ord(), "DR.DR_leading": fr(DRDR.lead()),
             "wronskian_over_8eta9_constant": len([k for k in ratio.d if k <= 150]) == 1 and ratio.ord() == 0,
             "wronskian_over_8eta9": fr(ratio.lead()),
             "R_orders_on_(e_i,e_j,e_k)": [c.ord() for c in R]}


# ---- C2: the cusp census ------------------------------------------------------------------------------------------
def cusp_exps(a):
    aa, aR, aRb, na = dot(a, a), dot(a, R), dot(a, [c.conj() for c in R]), nrm(a)
    s1 = nrm(R) * na * S.c(2) + aRb * aRb.conj() * S.c(2) - aR * aR.conj()
    d2 = None if aa.ord() is None else F(nrm(R).ord() + aa.ord() - s1.ord(), 8)
    d1 = None if aR.ord() is None else F(2 * (4 + aR.ord()) - s1.ord(), 16)   # |D|/|R|^2 ~ x^4 Im tau: B1654's q is the nome e^{i pi tau}
    return {"m2/m3_exponent_in_|q|": None if d2 is None else str(d2),
            "m1/m3_exponent_in_|q|_times_Im_tau": None if d1 is None else str(d1),
            "orders_x": [aa.ord(), aR.ord(), na.ord(), s1.ord()]}


def section(n, seed, drop=()):
    rng = random.Random(1000 * seed + n); a = [S(), S(), S()]; used = []
    for j in range(3):
        if j in drop or 2 * n - 2 * j < 0: continue
        for f in Mbasis(2 * n - 2 * j):
            c = S.c(F(rng.randint(-9, 9) or 1, rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5)))
            used.append(j)
            for i in range(3): a[i] = a[i] + c * f * B[j][i]
    return a, used


C2 = {}
for n in range(0, 7):
    k = F(4 * n - 1, 2); row = {}
    for seed in (1, 2):
        a, used = section(n, seed)
        row["seed%d" % seed] = cusp_exps(a); row["dim"] = len(used); row["carries_D2R"] = 2 in used
    if 2 in used:
        a, _ = section(n, 3, drop=(2,)); row["f2 = 0 (no D2R)"] = cusp_exps(a)
    C2[str(k)] = row
out["C2_cusp"] = C2

# controls: B1646's constant directions (no covariance) give no hierarchy at the cusp
ctrl = {}
for name, v in (("e_i", (1, 0, 0)), ("e_j", (0, 1, 0)), ("e_k", (0, 0, 1)), ("generic real", (3, -2, 5))):
    a = [S.c(v[0]), S.c(v[1]), S.c(v[2])]; ctrl[name] = cusp_exps(a)
out["C2_controls_constant_directions"] = ctrl


# ---- C3: near omega ---------------------------------------------------------------------------------------------
def ev(s, tau):
    x = mp.exp(2j * mp.pi * tau / 8)
    return mp.fsum(mp.mpc(mp.mpf(a.numerator) / a.denominator, mp.mpf(b.numerator) / b.denominator) * x ** kk for kk, (a, b) in s.d.items())


OM = mp.mpc(-0.5, mp.sqrt(3) / 2)


def at(a, tau):
    av = [ev(c, tau) for c in a]; Rv = [ev(c, tau) for c in R]
    aa = sum(u * u for u in av); aR = sum(u * v for u, v in zip(av, Rv)); aRb = sum(u * mp.conj(v) for u, v in zip(av, Rv))
    na = sum(abs(u) ** 2 for u in av); nR = sum(abs(v) ** 2 for v in Rv)
    s1sq = 2 * nR * na + 2 * abs(aRb) ** 2 - abs(aR) ** 2
    return nR * abs(aa) / s1sq, abs(aR) / mp.sqrt(s1sq) / nR, av, na


# rho(ST) on M: rho_R(T) = e^{i pi/4} L^-1, rho_R(S) = e^{i pi/4} P (W64), L the quarter-turn about e_i, P the i-j swap
Lm = mp.matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]); Pm = mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
ST = (mp.exp(1j * mp.pi / 4) ** 2) * Pm * Lm ** -1
ev_ST, V_ST = mp.eig(ST)
out["C3_rho_ST_eigenvalues"] = [mp.nstr(e, 8) for e in ev_ST]
out["C3_rho_ST_eigenlines_isotropic"] = [mp.nstr(abs(sum(V_ST[i, j] ** 2 for i in range(3))), 3) for j in range(3)]
C3 = {}
for n in range(0, 7):
    k = F(4 * n - 1, 2); row = {}
    for seed in (1, 2):
        a, _ = section(n, seed)
        a0 = at(a, OM)
        sl2, sl1 = [], []
        for th in (0.3, 1.9, 4.1):
            vals = [at(a, OM + mp.mpf(10) ** -e * mp.exp(1j * th)) for e in (5, 6)]
            f = lambda i: (mp.log(vals[0][i] / vals[1][i]) / mp.log(10)) if vals[1][i] > mp.mpf(10) ** -35 else None
            sl2.append(f(0)); sl1.append(f(1))
        rnd = lambda xs: None if any(x is None for x in xs) else [round(float(x), 3) for x in xs]
        # where a(omega) lies: its components on the eigenlines of rho(ST)
        comp = (V_ST ** -1) * mp.matrix(a0[2])
        row["seed%d" % seed] = {"|a(omega)|^2": mp.nstr(a0[3], 5), "m2/m3_at_omega": mp.nstr(a0[0], 6),
                                "slope_m2/m3_in_eps": rnd(sl2), "slope_lift_factor_in_eps": rnd(sl1),
                                "a(omega)_on_rho(ST)_eigenlines": [mp.nstr(abs(comp[i]), 3) for i in range(3)]}
    C3[str(k)] = row
out["C3_omega"] = C3

# ---- C2b: the cusp exponents by a second route, direct evaluation along tau = i y ------------------------------------
C2b = {}
for n in (2, 4, 5, 6):
    k = F(4 * n - 1, 2); a, _ = section(n, 1); vals = {}
    for y in (3, 4, 5):
        m2, lf, _, _ = at(a, mp.mpc(0, y))
        nR = sum(abs(ev(c, mp.mpc(0, y))) ** 2 for c in R)
        nome = mp.exp(-mp.pi * y); vals[y] = (m2, lf * nR * nome * (8 * mp.pi ** 2 * y - 44.55))   # D = nome |R|^2 (8 pi^2 y + K), B1654
    sl = lambda i: [round(float(-mp.log(vals[y2][i] / vals[y1][i]) / (2 * mp.pi * (y2 - y1))), 3) for y1, y2 in ((3, 4), (4, 5))]
    C2b[str(k)] = {"m2/m3_slope_in_|q|": sl(0), "m1/m3_slope_in_|q|_with_D_law": sl(1)}
out["C2b_cusp_direct"] = C2b

# ---- C4: W72's Higgs surface mode is eta^6 R (weight 5/2 for rho' = rho_R (x) chi_i): its coefficients on the eigenlines
# v+ = e_j - i e_k, e_i, v- = e_j + i e_k against the seat's stored ones (row 1134; its first nine, read at e1724317)
eta6 = (th2 * th3 * th4) * (th2 * th3 * th4) * S.c(F(1, 4))           # (2 eta^3)^2 / 4
h = [eta6 * c for c in R]
vp = (h[1] + h[2] * S.c(0, 1)) * S.c(F(1, 2)); ei = h[0]; vm = (h[1] - h[2] * S.c(0, 1)) * S.c(F(1, 2))
lead = vp.lead(); inv_lead = S({0: lead}).inv()
coef = lambda ser, kk: ((ser * inv_lead).d.get(kk, (F(0), F(0))))
mine = {"v+:1/8": coef(vp, 1), "e_i:3/8": coef(ei, 3), "v-:5/8": coef(vm, 5), "v+:9/8": coef(vp, 9), "e_i:11/8": coef(ei, 11),
        "v-:13/8": coef(vm, 13), "v+:17/8": coef(vp, 17), "e_i:19/8": coef(ei, 19), "v-:21/8": coef(vm, 21)}
seat = {"v+:1/8": 1, "e_i:3/8": 4, "v-:5/8": -4, "v+:9/8": 1, "e_i:11/8": -4, "v-:13/8": 12, "v+:17/8": -8, "e_i:19/8": -20, "v-:21/8": -8}
out["C4_h_is_eta6_R"] = {"coefficients": {kk: [str(v[0]), str(v[1])] for kk, v in mine.items()},
                         "equal_to_the_seats": all(mine[kk] == (F(seat[kk]), F(0)) for kk in seat),
                         "h.h_identically_0": dot(h, h).ord() is None or dot(h, h).ord() > 200}
out["notes"] = ("m1/m3 = |D| x (the lift factor) / (2 pi L); |D|/|R|^2 ~ |q|^(1/2) (8 pi^2 Im tau + const) at the cusp (q = e^{2 pi i tau}; "
                "B1654's nome) and |D| ~ |tau - omega| at omega (B1654), L of order one (B1667): so near omega m1/m3's exponent is the "
                "lift factor's plus 1; the control: a constant direction falls as |q|^(1/2) Im tau = e^(-pi Im tau) Im tau, B1667's T4 law")
if __name__ == "__main__":
    json.dump(out, open(HERE / "the_exponents.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str)[:6000])
