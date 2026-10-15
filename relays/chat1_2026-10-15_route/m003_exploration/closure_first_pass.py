# FIRST PASS, superseded by closure.py: raw thetas at moving points (quasi-periodic and Gaussian factors not removed) and lines from the other marking; kept as run.
# EXPLORATION (unsealed, disclosed): does B1653's twisted residue quaternion close around the -LR thread?
# u_s(tau) = c_s theta_s(ubar|tau) theta_s(delta|tau) / theta1'(0|tau), s = 1, i, j, k <-> theta1, theta2, theta4, theta3,
# c = (-i, -1, -1, i); z-convention periods 1 and tau (mpmath's jtheta(n, pi z, q), q = e^{i pi tau}).
# w(tau) = (a + b tau)/5 with (a, b) fixed up to sign by the thread's action. No mass, no data.
import mpmath as mp
mp.mp.dps = 30
CH = [("1", 1, -1j), ("i", 2, -1), ("j", 4, -1), ("k", 3, 1j)]
def th(n, z, tau):
    return mp.jtheta(n, mp.pi * z, mp.exp(1j * mp.pi * tau))
def th1p(tau):
    return mp.pi * mp.jtheta(1, 0, mp.exp(1j * mp.pi * tau), 1)
def quat(tau, ub, de):
    return [c * th(n, ub, tau) * th(n, de, tau) / th1p(tau) for _, n, c in CH]
A, B, C, D = 1, 1, 1, 2                      # gamma = L.R = [[1,1],[1,2]], tau -> (A tau + B)/(C tau + D)
mob = lambda t: (A * t + B) / (C * t + D)
# lines (a, b) with (a', b') = (a D + b B, a C + b A) = eps (a, b) mod 5
for eps in (1, -1):
    fx = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)
          and ((a * D + b * B) - eps * a) % 5 == 0 and ((a * C + b * A) - eps * b) % 5 == 0]
    print("eps", eps, "lines (a,b)/5 returning as eps*w:", fx)
tau = mp.mpc(0.3, 1.1); tg = mob(tau); J = C * tau + D
# untwisted: the channel permutation and signs of R under gamma
R0, R1_ = quat(tau, 0, 0), quat(tg, 0, 0)
print("untwisted |R_s(g tau)| / |R_t(tau)| matrix (rows s, cols t):")
for s in range(4):
    print("  ", [mp.nstr(abs(R1_[s]) / abs(R0[t]), 6) if abs(R0[t]) > 1e-20 else "  -  " for t in range(4)])
# twisted, per sector, on a line returning as -w: ubar = qs*w, delta = qd*w
lines = [(1, 3), (2, 1)]
SECT = {"up": (-3, 5), "down": (3, -1), "lepton": (3, -9)}
for (a, b) in lines:
    w = (a + b * tau) / 5; wg = (a + b * tg) / 5
    for name, (qs, qd) in SECT.items():
        u0, u1 = quat(tau, qs * w, qd * w), quat(tg, qs * wg, qd * wg)
        print(f"line ({a},{b})/5 {name:6s} |u_s(tau)|:", [mp.nstr(abs(x), 5) for x in u0],
              " |u_s(g tau)|:", [mp.nstr(abs(x), 5) for x in u1])
