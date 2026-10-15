import mpmath as mp
mp.mp.dps = 40
# channels s=1,i,j,k <-> jacobi theta index 1,2,4,3 ; c=(-i,-1,-1,i)
CH = [1, 2, 4, 3]; CC = [-1j, -1, -1, 1j]
def theta(n, z, tau):  # periods 1, tau
    return mp.jtheta(n, mp.pi*z, mp.exp(1j*mp.pi*tau))
def th1p(tau): return mp.pi*mp.jtheta(1, 0, mp.exp(1j*mp.pi*tau), 1)
def T(n, al, be, tau, norm="2ab", red=False):
    al = mp.mpf(al); be = mp.mpf(be)
    if red:  # reduce mod 1 into [0,1)
        al = al - mp.floor(al); be = be - mp.floor(be)
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
        t, f = min(cands, key=lambda x: abs(x[1]-1))
        law[s] = (t, f)
    return law
def closure(tau, vu, vd, **kw):
    J = C*tau+D; law = Rlaw(tau)
    u0 = quat(tau, vu, vd, **kw); ug = quat(g(tau), vu, vd, **kw)
    out = []
    for s in (1,2,3):
        t, f = law[s]
        out.append(ug[s]*mp.sqrt(J)/u0[t]/f if abs(u0[t])>mp.mpf(10)**-30 else None)
    out0 = ug[0]*mp.sqrt(J)/u0[0] if abs(u0[0])>mp.mpf(10)**-30 else None
    return law, out0, out
def ph5(z):  # phase as k/5 if a 5th root
    if z is None: return "0/0"
    a = mp.arg(z)/(2*mp.pi)*5
    return f"{mp.nstr(abs(z),8)} x zeta^{mp.nstr(a,10)}"
