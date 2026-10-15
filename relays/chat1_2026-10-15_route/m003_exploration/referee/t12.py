import sys; sys.path.insert(0,'.')
from ref3 import *
mp.mp.dps = 30
tau = mp.mpc(0.17, 1.03); N=5; a,b = 1,3
for nm,(qL,qR) in {"up":(1,-4),"down":(1,2),"lepton":(-3,6)}.items():
    vu=(mp.mpf((qL+qR)*b)/N, mp.mpf((qL+qR)*a)/N); vd=(mp.mpf((qL-qR)*b)/N, mp.mpf((qL-qR)*a)/N)
    u = quat(tau,vu,vd); uu = u[1]**2+u[2]**2+u[3]**2
    print(f"{nm:6s} w=(1,3)/5: |u1|={mp.nstr(abs(u[0]),5)}  |u.u|={mp.nstr(abs(uu),5)}  |u1^2+u.u|={mp.nstr(abs(u[0]**2+uu),3)}  |u|^2={mp.nstr(sum(abs(x)**2 for x in u[1:]),5)}")
