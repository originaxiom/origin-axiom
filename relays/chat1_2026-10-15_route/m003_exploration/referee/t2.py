import sys; sys.path.insert(0,'.')
from ref import *
for tau in (mp.mpc(-1.37,2.6), mp.mpc(-0.37,2.6), mp.mpc(0.3,1.1)):
    J=C*tau+D; R0=quat(tau,(0,0),(0,0)); Rg=quat(g(tau),(0,0),(0,0))
    print(mp.nstr(tau,4), "g tau", mp.nstr(g(tau),5))
    for s in (1,2,3):
        print("  s",s,[mp.nstr(Rg[s]*mp.sqrt(J)/R0[t],8) for t in (1,2,3)])
    # check raw theta values sanity vs series
    q=mp.exp(1j*mp.pi*tau)
    print("  th3(0) jtheta vs sum:", mp.nstr(mp.jtheta(3,0,q),10), mp.nstr(mp.nsum(lambda n: mp.exp(1j*mp.pi*n*n*tau),[-mp.inf,mp.inf]),10))
    tg=g(tau); qg=mp.exp(1j*mp.pi*tg)
    print("  th3(0|g tau) jtheta vs sum:", mp.nstr(mp.jtheta(3,0,qg),10), mp.nstr(mp.nsum(lambda n: mp.exp(1j*mp.pi*n*n*tg),[-mp.inf,mp.inf]),10))
