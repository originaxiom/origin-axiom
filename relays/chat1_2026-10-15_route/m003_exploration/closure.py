# EXPLORATION (unsealed, disclosed): closure of the twisted residue quaternion around -LR, with theta constants of
# rational characteristic: T_s(z = beta + alpha tau) = e^{pi i alpha^2 tau + 2 pi i alpha beta} theta_s(z|tau)
# (the quasi-periodicity removed; weight-1/2 modular forms of level dividing 2N, permuted by SL2(Z) up to roots of 1).
import mpmath as mp
mp.mp.dps = 30
CH = [("1", 1, -1j), ("i", 2, -1), ("j", 4, -1), ("k", 3, 1j)]
def th(n, z, tau): return mp.jtheta(n, mp.pi * z, mp.exp(1j * mp.pi * tau))
def th1p(tau): return mp.pi * mp.jtheta(1, 0, mp.exp(1j * mp.pi * tau), 1)
def T(n, al, be, tau): return mp.exp(1j*mp.pi*al*al*tau + 2j*mp.pi*al*be) * th(n, be + al*tau, tau)
def quat(tau, ub, de):   # ub, de = (alpha, beta) characteristics of ubar and delta
    return [c * T(n, ub[0], ub[1], tau) * T(n, de[0], de[1], tau) / th1p(tau) for _, n, c in CH]
A, B, C, D = 1, 1, 1, 2
mob = lambda t: (A*t + B) / (C*t + D)
SECT = {"up": (-3, 5), "down": (3, -1), "lepton": (3, -9)}
for tau in (mp.mpc(0.3, 1.1), mp.mpc(-0.2, 0.9)):
    tg = mob(tau); J = C*tau + D
    R0, Rg = quat(tau, (0,0), (0,0)), quat(tg, (0,0), (0,0))
    # untwisted permutation: find t with |Rg_s| |J|^{1/2} = |R0_t|
    perm = {}
    for s in range(1, 4):
        t = min(range(1, 4), key=lambda t: abs(abs(Rg[s]) * abs(J)**0.5 - abs(R0[t])))
        perm[s] = (t, Rg[s] * mp.sqrt(J) / R0[t])
    print(f"tau={mp.nstr(tau,4)}  untwisted: s<-t and the factor R_s(g tau) sqrt(J)/R_t(tau):",
          {CH[s][0]: (CH[t][0], mp.nstr(f, 6)) for s, (t, f) in perm.items()})
    for (a, b) in ((1, 2), (2, 4)):
        for name, (qs, qd) in SECT.items():
            ub, de = (qs*b/5., qs*a/5.), (qd*b/5., qd*a/5.)
            u0, ug = quat(tau, ub, de), quat(tg, ub, de)
            ratios = []
            for s in range(1, 4):
                t = perm[s][0]
                ratios.append(ug[s] * mp.sqrt(J) / u0[t] / perm[s][1] if abs(u0[t]) > 1e-25 else None)
            r1 = (ug[0] * mp.sqrt(J) / u0[0]) if abs(u0[0]) > 1e-25 else None
            print(f"   line ({a},{b})/5 {name:6s}: closure factors (i,j,k) relative to R's law:",
                  [mp.nstr(r, 6) if r is not None else '0/0' for r in ratios],
                  " identity channel u1(g)sqrtJ/u1:", mp.nstr(r1, 6) if r1 is not None else "u1 = 0",
                  " |u|:", mp.nstr(mp.sqrt(sum(abs(x)**2 for x in u0)), 4))
