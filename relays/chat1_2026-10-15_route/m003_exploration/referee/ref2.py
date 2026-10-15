import mpmath as mp
mp.mp.dps = 40
# own series, no nome branch: theta[c,d](z|tau) = sum_m exp(pi i (m+c)^2 tau + 2 pi i (m+c)(z+d))
def thc(c, d, z, tau, N=60):
    return mp.fsum(mp.exp(1j*mp.pi*(m+c)**2*tau + 2j*mp.pi*(m+c)*(z+d)) for m in range(-N, N+1))
H = mp.mpf(1)/2
JAC = {1: (H, H, -1), 2: (H, 0, 1), 3: (0, 0, 1), 4: (0, H, 1)}
def theta(n, z, tau):
    c, d, sg = JAC[n]; return sg*thc(c, d, z, tau)
def th1p(tau, N=60):
    return -mp.fsum(2j*mp.pi*(m+H)*mp.exp(1j*mp.pi*(m+H)**2*tau + 1j*mp.pi*(m+H)) for m in range(-N, N+1))
CH = [1, 2, 4, 3]; CC = [-1j, -1, -1, 1j]
def T(n, al, be, tau, norm="2ab", red=False):
    al = mp.mpf(al); be = mp.mpf(be)
    if red: al = al - mp.floor(al); be = be - mp.floor(be)
    ph = {"2ab": 2*al*be, "ab": al*be, "none": 0}[norm]
    return mp.exp(1j*mp.pi*al*al*tau + 1j*mp.pi*ph)*theta(n, be+al*tau, tau)
def quat(tau, vu, vd, **kw):
    return [c*T(n, vu[0], vu[1], tau, **kw)*T(n, vd[0], vd[1], tau, **kw)/th1p(tau) for n, c in zip(CH, CC)]
A,B,C,D = 1,1,1,2
g = lambda t: (A*t+B)/(C*t+D)
def Rlaw(tau):
    J = C*tau+D; R0 = quat(tau,(0,0),(0,0)); Rg = quat(g(tau),(0,0),(0,0))
    law = {}
    for s in (1,2,3):
        cands = [(t, Rg[s]*mp.sqrt(J)/R0[t]) for t in (1,2,3)]
        t, f = min(cands, key=lambda x: abs(abs(x[1])-1))
        law[s] = (t, f)
    return law
def closure(tau, vu, vd, law=None, **kw):
    J = C*tau+D; law = law or Rlaw(tau)
    u0 = quat(tau, vu, vd, **kw); ug = quat(g(tau), vu, vd, **kw)
    out = []
    for s in (1,2,3):
        t, f = law[s]
        out.append(ug[s]*mp.sqrt(J)/u0[t]/f if abs(u0[t])>mp.mpf(10)**-30 else None)
    out0 = ug[0]*mp.sqrt(J)/u0[0] if abs(u0[0])>mp.mpf(10)**-30 else None
    return law, out0, out
def ph5(z):
    if z is None: return "0/0"
    return f"|{mp.nstr(abs(z),6)}| z^{mp.nstr(mp.arg(z)/(2*mp.pi)*5,8)}"
