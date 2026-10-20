import mpmath as mp, numpy as np, itertools, math, sys, json
mp.mp.dps=30
om=mp.mpc(-0.5, mp.sqrt(3)/2)
def V(t): return -mp.log(t.imag*abs(mp.eta(t) if hasattr(mp,'eta') else 0)**4)
def eta(t):
    q=mp.exp(2j*mp.pi*t); return mp.exp(1j*mp.pi*t/12)*mp.qp(q)
def V(t): return -mp.log(t.imag*abs(eta(t))**4)
print("C1 V(om)",V(om),"V(i)",V(mp.mpc(0,1)),"dV",V(mp.mpc(0,1))-V(om),"V(4i)",V(mp.mpc(0,4)))
# fine grid in fundamental domain, + local hessian at i
best=(1e9,None)
for x in np.linspace(-0.5,0.5,201):
  for y in np.linspace(0.8,4,321):
    if x*x+y*y<1-1e-12: continue
    v=float(V(mp.mpc(x,y)))
    if v<best[0]: best=(v,(x,y))
print("grid min",best)
# is i a saddle in F or on boundary-identification? V along imaginary axis and Re direction
for d in [0.01,0.05]:
    print("i + d(real)",V(mp.mpc(d,1))-V(mp.mpc(0,1)),"i + id",V(mp.mpc(0,1+d))-V(mp.mpc(0,1)),"i - id", V(mp.mpc(0,1-d))-V(mp.mpc(0,1)))
# Osgood-Phillips-Sarnak: det' Laplacian ~ y|eta|^4 ; check eta(om)
# C2
def th1(u,t):
    return mp.jtheta(1,mp.pi*u,mp.exp(1j*mp.pi*t))
def G(w): return float(-mp.log(abs(th1(w,om)/eta(om))**2)+2*mp.pi*(w.imag**2)/om.imag)
pts=[(a,b) for a in range(9) for b in range(9) if (a,b)!=(0,0)]
g={}
for a,b in pts:
    w=mp.mpf(a)/9*om-mp.mpf(b)/9
    g[(a,b)]=G(w)
order9=[p for p in pts if p[0]%3 or p[1]%3]
print("n all nonzero",len(pts),"order9",len(order9))
vals=sorted(set(round(g[p],6) for p in pts))
print("distinct values all 80:",vals[:8])
mn=min(g[p] for p in order9)
gs=[p for p in order9 if abs(g[p]-mn)<1e-6]
print("min over order9",mn,"count",len(gs),gs)
print("min over ALL 80 incl 3-torsion",min(g.values()),[p for p in pts if abs(g[p]-min(g.values()))<1e-6])
print("sorted order9 distinct:",sorted(set(round(g[p],6) for p in order9))[:6])
# orbit structure under mu6 and conjugation
def mul(x,y):
    a,b=x;c,d=y  # (a w - b)/9 representation: elements a*w + b'*1 with b' = -b ; use coords (a,b) meaning a*w - b
    # (a w - b)(c w - d) = ac w^2 - (ad+bc) w + bd ; w^2=-w-1 => -ac w - ac -(ad+bc)w + bd
    return ((-a*c-a*d-b*c)%9,(a*c-b*d)%9)
def conj(x):
    a,b=x  # conj(w)=-1-w -> conj(a w - b)= -a -a w - b -> coeff of w: -a ; const: -(a+b) => b' = a+b
    return ((-a)%9,(a+b)%9)
# units: 1,w,w^2,... as (a,b) with element a w - b: 1=(0,-1)->(0,8); w=(1,0)
one=(0,8); w=(1,0)
units=[one]
for _ in range(5): units.append(mul(units[-1],(1,0)) if False else None)
# build mu6 = ±w^k
u=[one];cur=one
for _ in range(2):
    cur=mul(cur,w);u.append(cur)
mu6=u+[((-a)%9,(-b)%9) for a,b in u]
print("mu6",mu6)
# check sanity mul: w*w should be -w-1 = (-1, ... ) 
print("w*w",mul(w,w))
orbs=[]
seen=set()
for p in order9:
    if p in seen: continue
    orb={mul(x,p) for x in mu6}; orb|={mul(x,conj(p)) for x in mu6}
    seen|=orb; orbs.append((sorted(orb),round(g[p],6)))
for o in orbs: print(len(o[0]),o[1])
# reflections fixed: p fixed by z->zeta conj(z)
def cpeven(p): return any(mul(x,conj(p))==p for x in mu6)
print("GS cp-even",[cpeven(p) for p in gs], sum(cpeven(p) for p in gs))
print("arc's list match:", sorted(gs)==sorted([(2,3),(2,4),(3,2),(3,4),(4,2),(4,3),(5,6),(5,7),(6,5),(6,7),(7,5),(7,6)]))
# W59 lines
L18=[(b+i, b+j) for b in (1,2) for i in (0,3,6) for j in (0,3,6)]
print("W59 18 in GS:",[p for p in L18 if p in gs]); print("G on W59 lines",sorted(set(round(g[p],4) for p in L18)))
print("cp-even among all 72:",sum(cpeven(p) for p in order9))
print("W59 cpeven",sum(cpeven(p) for p in L18))
# GS under mu6 only orbit (without conj)
orb_mu={mul(x,gs[0]) for x in mu6}; print("mu6 orbit of gs0 size",len(orb_mu), "all in gs",orb_mu<=set(gs))
json.dump({"g":{str(k):v for k,v in g.items()}},open("g.json","w"))
