import sys; sys.path.insert(0,'.')
from ref3 import *
def lawfit(g):
    A,B,C,D = g
    taus = [mp.mpc(-mp.mpf(D)/C, 0) + mp.mpc(0.37,0.8)/C, mp.mpc(-mp.mpf(D)/C, 0) + mp.mpc(-0.29,0.95)/C]
    vals = []
    for tau in taus:
        tg = (A*tau+B)/(C*tau+D); J = C*tau+D
        R0, Rg = quat(tau,(0,0),(0,0)), quat(tg,(0,0),(0,0))
        vals.append({(s,t): Rg[s]*mp.sqrt(J)/R0[t] for s in (1,2,3) for t in (1,2,3)})
    law = {}
    for s in (1,2,3):
        t = min((1,2,3), key=lambda t: abs(vals[0][(s,t)]-vals[1][(s,t)]))
        law[s] = (t, vals[0][(s,t)])
    return law, taus[0]
def run2(g, N, maxlines=2, qs=SECT, tag=""):
    A,B,C,D = g; law, tau = lawfit(g)
    tg = (A*tau+B)/(C*tau+D); J = C*tau+D
    out = []
    for eps in (1,-1):
        lines = [(a,b) for a in range(N) for b in range(N) if (a,b)!=(0,0) and math.gcd(math.gcd(a,b),N)==1
                 and ((a*D+b*B)-eps*a) % N == 0 and ((a*C+b*A)-eps*b) % N == 0]
        for (a,b) in lines[:maxlines]:
            row = {}
            for nm,(qu,qd) in qs.items():
                vu = (mp.mpf(qu*b)/N, mp.mpf(qu*a)/N); vd = (mp.mpf(qd*b)/N, mp.mpf(qd*a)/N)
                u0, ug = quat(tau,vu,vd), quat(tg,vu,vd)
                r = [ug[s]*mp.sqrt(J)/u0[law[s][0]]/law[s][1] for s in (1,2,3) if abs(u0[law[s][0]]) > mp.mpf(10)**-18]
                ks = [mp.nstr(mp.arg(x)/(2*mp.pi)*N,4) + ("" if abs(abs(x)-1)<1e-10 else f"|{mp.nstr(abs(x),4)}|") for x in r]
                row[nm] = ks
            out.append((eps,(a,b),row)); print(f"  {tag} eps={eps:+d} ({a},{b})/{N} k(units 2pi/N):", row)
    return out
