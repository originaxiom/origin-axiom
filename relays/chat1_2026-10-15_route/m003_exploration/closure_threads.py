# EXPLORATION (unsealed): closure phase of the twisted quaternion for lines fixed EXACTLY (gamma w = w) vs up to sign,
# on several threads; thetas summed directly as series in tau (no nome branch issue).
import mpmath as mp, math
mp.mp.dps = 30
def theta(n, z, tau, M=40):
    e = lambda x: mp.exp(1j * mp.pi * x)
    if n == 3: return mp.fsum(e(k*k*tau + 2*k*z) for k in range(-M, M+1))
    if n == 4: return mp.fsum((-1)**(k % 2) * e(k*k*tau + 2*k*z) for k in range(-M, M+1))
    if n == 2: return mp.fsum(e((k+0.5)**2*tau + 2*(k+0.5)*z) for k in range(-M, M+1))
    if n == 1: return mp.fsum(-1j * (-1)**(k % 2) * e((k+0.5)**2*tau + 2*(k+0.5)*z) for k in range(-M, M+1))
def th1p(tau, h=mp.mpf('1e-12')):
    return (theta(1, h, tau) - theta(1, -h, tau)) / (2*h)
CH = [(1, -1j), (2, -1), (4, -1), (3, 1j)]
def T(n, al, be, tau): return mp.exp(1j*mp.pi*al*al*tau + 2j*mp.pi*al*be) * theta(n, be + al*tau, tau)
def quat(tau, ub, de): return [c * T(n, *ub, tau) * T(n, *de, tau) / th1p(tau) for n, c in CH]
SECT = {"up": (-3, 5), "down": (3, -1), "lepton": (3, -9)}
def run(word, g, N, tau):
    A, B, C, D = g; tg = (A*tau + B)/(C*tau + D); J = C*tau + D
    R0, Rg = quat(tau, (0,0), (0,0)), quat(tg, (0,0), (0,0))
    perm = {s: min(range(1,4), key=lambda t: abs(abs(Rg[s])*abs(J)**0.5 - abs(R0[t]))) for s in range(1,4)}
    fac = {s: Rg[s]*mp.sqrt(J)/R0[perm[s]] for s in range(1,4)}
    for eps in (1, -1):
        lines = [(a,b) for a in range(N) for b in range(N) if (a,b) != (0,0) and math.gcd(math.gcd(a,b),N) == 1
                 and ((a*D + b*B) - eps*a) % N == 0 and ((a*C + b*A) - eps*b) % N == 0]
        for (a,b) in lines[:2]:
            out = []
            for name, (qs, qd) in SECT.items():
                ub, de = (qs*b/N, qs*a/N), (qd*b/N, qd*a/N)
                u0, ug = quat(tau, ub, de), quat(tg, ub, de)
                r = [ug[s]*mp.sqrt(J)/u0[perm[s]]/fac[s] for s in range(1,4) if abs(u0[perm[s]]) > 1e-20]
                ph = [mp.nstr(mp.arg(x)/(2*mp.pi)*N, 4) for x in r]    # phase in units of 2 pi / N
                out.append(f"{name}: {ph}")
            print(f"{word} N={N} eps={eps:+d} line ({a},{b})/{N}: phases x(2pi/N) per channel ->", "; ".join(out))
def mat(w):
    import numpy as np
    L = np.array([[1,0],[1,1]]); R = np.array([[1,1],[0,1]]); M = np.eye(2, dtype=int)
    for ch in w: M = M @ (L if ch == "L" else R)
    return tuple(int(x) for x in M.flatten())
tau = mp.mpc(0.31, 1.07)
for word, N in (("LR", 5), ("LLLLLRR", 5), ("LLRRRRR", 5), ("LLLLLRRR", 5), ("LLLR", 3), ("LLR", 2)):
    run(word, mat(word), N, tau)
