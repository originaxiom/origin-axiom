import sys; sys.path.insert(0,'.')
from ref2 import *
mp.mp.dps = 30
tau = mp.mpc(0.23, 0.97); law = Rlaw(tau)
def V(q, a, b): return (mp.mpf(q*b)/5, mp.mpf(q*a)/5)
for kw in ({}, dict(red=True), dict(norm="ab"), dict(red=True,norm="ab"), dict(red=True,norm="none")):
    _, o0, o = closure(tau, V(-3,4,3), V(5,4,3), law, **kw)
    print(kw, [ph5(x) for x in o])
# check T(v+m)/T(v) tau-independence for the ab norm
for n in (2,3,4):
    for t in (tau, g(tau)):
        r = T(n, mp.mpf(-9)/5, mp.mpf(-12)/5, t, norm="ab")/T(n, mp.mpf(1)/5, mp.mpf(3)/5, t, norm="ab")
        print(n, mp.nstr(t,4), mp.nstr(r,8))
