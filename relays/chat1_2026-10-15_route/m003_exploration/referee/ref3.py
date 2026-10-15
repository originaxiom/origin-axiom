import mpmath as mp, math
mp.mp.dps = 30
H = mp.mpf(1)/2
JAC = {1: (H, H, -1), 2: (H, 0, 1), 3: (0, 0, 1), 4: (0, H, 1)}
CH = [1, 2, 4, 3]; CC = [-1j, -1, -1, 1j]
def T(n, al, be, tau, M=None):
    # e^{pi i al^2 tau + 2 pi i al be} theta_n(be + al tau | tau), summed well-conditioned around the peak
    c, d, sg = JAC[n]; s = c + al
    if M is None: M = int(mp.sqrt(80/(mp.pi*mp.im(tau)))) + 6
    m0 = int(mp.nint(-s))
    return sg*mp.exp(-2j*mp.pi*al*d)*mp.fsum(mp.exp(1j*mp.pi*(m+s)**2*tau + 2j*mp.pi*(m+s)*(be+d)) for m in range(m0-M, m0+M+1))
def th1p(tau):
    M = int(mp.sqrt(80/(mp.pi*mp.im(tau)))) + 6
    return -mp.fsum(2j*mp.pi*(m+H)*mp.exp(1j*mp.pi*(m+H)**2*tau + 1j*mp.pi*(m+H)) for m in range(-M, M+1))
def quat(tau, vu, vd):
    p = th1p(tau)
    return [c*T(n, vu[0], vu[1], tau)*T(n, vd[0], vd[1], tau)/p for n, c in zip(CH, CC)]
def word(w):
    M = [[1,0],[0,1]]
    for ch in w:
        X = [[1,0],[1,1]] if ch == "L" else [[1,1],[0,1]]
        M = [[M[0][0]*X[0][0]+M[0][1]*X[1][0], M[0][0]*X[0][1]+M[0][1]*X[1][1]],
             [M[1][0]*X[0][0]+M[1][1]*X[1][0], M[1][0]*X[0][1]+M[1][1]*X[1][1]]]
    return M[0][0], M[0][1], M[1][0], M[1][1]
SECT = {"up": (-3, 5), "down": (3, -1), "lepton": (3, -9)}
def run(g, N, maxlines=2, verbose=True):
    A,B,C,D = g
    tau = mp.mpc(-mp.mpf(D)/C, mp.mpf(1)/C) if C else mp.mpc(0.3,1.1)   # J = i, Im tau = Im g tau = 1/C
    tg = (A*tau+B)/(C*tau+D); J = C*tau+D
    R0, Rg = quat(tau,(0,0),(0,0)), quat(tg,(0,0),(0,0))
    law = {}
    for s in (1,2,3):
        t, f = min(((t, Rg[s]*mp.sqrt(J)/R0[t]) for t in (1,2,3)), key=lambda x: abs(abs(x[1])-1))
        law[s] = (t, f)
    res = []
    for eps in (1,-1):
        lines = [(a,b) for a in range(N) for b in range(N) if (a,b)!=(0,0) and math.gcd(math.gcd(a,b),N)==1
                 and ((a*D+b*B)-eps*a) % N == 0 and ((a*C+b*A)-eps*b) % N == 0]
        for (a,b) in lines[:maxlines]:
            row = {}
            for nm,(qu,qd) in SECT.items():
                vu = (mp.mpf(qu*b)/N, mp.mpf(qu*a)/N); vd = (mp.mpf(qd*b)/N, mp.mpf(qd*a)/N)
                u0, ug = quat(tau,vu,vd), quat(tg,vu,vd)
                r = [ug[s]*mp.sqrt(J)/u0[law[s][0]]/law[s][1] for s in (1,2,3) if abs(u0[law[s][0]]) > mp.mpf(10)**-18]
                row[nm] = [mp.nstr(x, 5) for x in r]
            res.append((eps,(a,b),row))
            if verbose: print(f"   eps={eps:+d} ({a},{b})/{N}:", row)
    return res
