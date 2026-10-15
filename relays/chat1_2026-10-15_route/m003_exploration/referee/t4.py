import sys; sys.path.insert(0,'.')
from ref2 import *
mp.mp.dps = 30
tau = mp.mpc(0.23, 0.97); law = Rlaw(tau)
def V(q, a, b): return (mp.mpf(q*b)/5, mp.mpf(q*a)/5)
def up(a,b,**kw):
    _, o0, o = closure(tau, V(-3,a,b), V(5,a,b), law, **kw); return [ph5(x) for x in o]
print("(2) convention variants, up sector, ijk self-closure phase:")
for lab,(a,b),kw in [("base (1,2)",(1,2),{}), ("norm e^{pi i ab}",(1,2),dict(norm="ab")), ("norm no beta-phase",(1,2),dict(norm="none")),
                     ("reduce mod 1",(1,2),dict(red=True)), ("rep (6,2)",(6,2),{}), ("rep (1,7)",(1,7),{}), ("rep (4,3)=-(1,2)+(5,5)",(4,3),{}),
                     ("-w: (-1,-2)",(-1,-2),{}), ("rep (-4,-3)",(-4,-3),{}), ("rep (3,1)=3*(1,2) mod5",(3,1),{}), ("(2,4)",(2,4),{}), ("(4,3) red+ab",(4,3),dict(red=True,norm="ab"))]:
    print(f"  {lab:28s}", up(a,b,**kw))
# point-identification comparison: u(g tau;(1,2)) vs u(tau;(4,3)) (the gamma-image char), per convention
print("point-identified comparison u(g tau;(a,b)) sqrtJ / u(tau; image) / Rlaw, image=(2a+b,a+b):")
for kw in ({}, dict(norm="ab"), dict(norm="none")):
    J = C*tau+D
    ug = quat(g(tau), V(-3,1,2), V(5,1,2), **kw); u0 = quat(tau, V(-3,4,3), V(5,4,3), **kw)
    print("  ", kw, [ph5(ug[s]*mp.sqrt(J)/u0[law[s][0]]/law[s][1]) for s in (1,2,3)])
