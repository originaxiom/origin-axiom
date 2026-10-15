"""Main's check (draft, S127): B1651's pairing triplet as the puncture's residue transported by the even spin structures'
Szego kernels. B1651's conventions exactly: units (i, j, k) <-> thetas (2, 4, 3), c = (-1, -1, i), pi z convention
(periods pi, pi tau), th_1, th_2 built with the explicit nome root.
  S_r(z) := th_r(z) th_1'(0) / (th_r(0) th_1(z))       (the Szego kernel of the even spin structure r; ~ 1/z at 0)
  claim A: v_r(z) = R_r S_r(z) with R_r = c_r th_r(0)^2 / th_1'(0) = Res_{z=0} v_r   (a rewriting; checked)
  claim B: S_r(z)^2 = wp(z) - wp(w_r), w_r the half-period where th_r vanishes      (classical; checked, wp independent)
  so v.v = wp(z) (R.R) - sum_r R_r^2 wp(w_r): isotropy at every z <=> R.R = 0 (B1649) and sum R_r^2 e_r = 0 (B1650 O6)
  controls: a wrong half-period pairing (B fails, non-constant); a flipped sign in c (R.R != 0)
wp is computed independently of the thetas' quadratic identities: wp(z) = -(log th_1)''(z) + th_1'''(0) / (3 th_1'(0)).
"""
import mpmath as mp
mp.mp.dps = 40
C = [-1, -1, 1j]; TH = [2, 4, 3]


def th(n, z, t):
    q = mp.exp(1j * mp.pi * t)
    if n in (3, 4):
        return mp.jtheta(n, z, q)
    q4 = mp.exp(1j * mp.pi * t / 4); s = z + mp.pi * t / 2
    if n == 2:
        return q4 * mp.exp(1j * z) * mp.jtheta(3, s, q)
    return -1j * q4 * mp.exp(1j * z) * mp.jtheta(4, s, q)


def d1(t): return mp.diff(lambda z: th(1, z, t), 0)
def d3(t): return mp.diff(lambda z: th(1, z, t), 0, 3)
def wp(z, t): return -mp.diff(lambda w: mp.log(th(1, w, t)), z, 2) + d3(t) / (3 * d1(t))
def S(r, z, t): return th(TH[r], z, t) * d1(t) / (th(TH[r], 0, t) * th(1, z, t))
def v(r, z, t, c=C): return c[r] * th(TH[r], 0, t) * th(TH[r], z, t) / th(1, z, t)
def R(r, t, c=C): return c[r] * th(TH[r], 0, t) ** 2 / d1(t)
def half(t): return {2: mp.pi / 2, 4: mp.pi * t / 2, 3: mp.pi * (1 + t) / 2}   # th_n vanishes there


worst = {"A": 0, "B": 0, "RR": 0, "Re": 0, "iso": 0}; ctrl = {"B_wrong": [], "RR_c3_real": []}
for t in (mp.mpc(0, 1.1), mp.mpc(0.3, 0.9), mp.mpc(-0.2, 1.7)):
    H = half(t)
    e = [wp(H[TH[r]], t) for r in range(3)]
    Rv = [R(r, t) for r in range(3)]
    worst["RR"] = max(worst["RR"], abs(sum(x * x for x in Rv)) / sum(abs(x) ** 2 for x in Rv))
    worst["Re"] = max(worst["Re"], abs(sum(Rv[r] ** 2 * e[r] for r in range(3))) / (sum(abs(Rv[r]) ** 2 for r in range(3)) * max(abs(x) for x in e)))
    for z in (mp.mpc(0.31, 0.17), mp.mpc(1.1, -0.4) * 0.7, mp.pi * t * mp.mpf("0.37") + mp.mpf("0.21")):
        P = wp(z, t)
        for r in range(3):
            worst["A"] = max(worst["A"], abs(v(r, z, t) - Rv[r] * S(r, z, t)) / abs(v(r, z, t)))
            worst["B"] = max(worst["B"], abs(S(r, z, t) ** 2 - P + e[r]) / abs(P))
        vv = sum(v(r, z, t) ** 2 for r in range(3)); worst["iso"] = max(worst["iso"], abs(vv) / sum(abs(v(r, z, t)) ** 2 for r in range(3)))
        # control 1: pair th_2 with th_4's half-period -> S^2 - wp + e_wrong is not ~0
        ctrl["B_wrong"].append(float(abs(S(0, z, t) ** 2 - P + e[1]) / abs(P)))
    # control 2: replace c_3 = i by 1 (a sign flip would be vacuous: R.R sees only c_r^2) -> R.R != 0
    Rf = [R(r, t, c=[-1, -1, 1]) for r in range(3)]
    ctrl["RR_c3_real"].append(float(abs(sum(x * x for x in Rf)) / sum(abs(x) ** 2 for x in Rf)))
print({k: mp.nstr(x, 3) for k, x in worst.items()})
print("controls (must be O(1)):", {k: [round(x, 3) for x in vals] for k, vals in ctrl.items()})
