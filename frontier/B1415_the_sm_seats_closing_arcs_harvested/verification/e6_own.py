#!/usr/bin/env python3
"""Own check of B1364/B1365's root-system claims and B1363's Kac classes, B1360's E7 count.
E6 roots in SO(10) x U(1) coordinates: 40 D5 roots (u=0), 16 spinor (even # of minus, u=+sqrt3/2), 16bar (odd, u=-sqrt3/2)."""
import itertools, numpy as np, sympy as sp
from fractions import Fraction as Fr
s3=np.sqrt(3)
roots=[]
for i,j in itertools.combinations(range(5),2):
    for a in (1,-1):
        for b in (1,-1):
            v=np.zeros(6); v[i]=a; v[j]=b; roots.append(v)
for signs in itertools.product((1,-1),repeat=5):
    v=np.array([0.5*s for s in signs]+[0.0]); neg=sum(1 for s in signs if s<0)
    v[5]= s3/2 if neg%2==0 else -s3/2; roots.append(v)
R=np.array(roots); assert len(R)==72 and np.allclose((R**2).sum(1),2)
ip=R@R.T; assert set(np.round(ip.flatten()).astype(int))<= {-2,-1,0,1,2}
print('E6: 72 roots, norms 2, integral inner products OK; roots at +1 from a given root:', int((np.round(ip[0])==1).sum()))
# SM inside SU(5) c SO(10): su(3) on indices 0,1,2; su(2) on 3,4; Y = (-1/3,-1/3,-1/3,1/2,1/2,0)
def isroot(v): return any(np.allclose(v,r) for r in R)
su3=[r for r in R if r[5]==0 and abs(r[:3]).sum()==2 and abs(r[3:5]).sum()==0 and r[:3].sum()==0]
su2=[r for r in R if r[5]==0 and abs(r[3:5]).sum()==2 and abs(r[:3]).sum()==0 and r[3:5].sum()==0]
Y=np.array([-1/3,-1/3,-1/3,1/2,1/2,0]); SMroots=su3+su2; print('su3 roots',len(su3),'su2 roots',len(su2))
# SM-singlet roots: orthogonal to all SM roots and Y-neutral
sing=[r for r in R if all(abs(r@s)<1e-9 for s in SMroots) and abs(r@Y)<1e-9]
print('SM-singlet roots:', len(sing), [np.round(v,3).tolist() for v in sing])
beta=[r for r in sing if r[5]>0][0]
# centraliser of su(2)_beta: roots orthogonal to beta
perp=[r for r in R if abs(r@beta)<1e-9]; print('roots orthogonal to beta:', len(perp), '(su(6) has 30)')
# SM roots among them
smin=[r for r in perp if any(np.allclose(r,s) for s in SMroots)]; print('SM roots among them:', len(smin))
# Cartan complement: gamma = orthogonal to SM roots, to Y, to beta (in R^6)
Mrows=np.array(SMroots+[Y,beta]); u,s,vt=np.linalg.svd(Mrows); gamma=vt[-1]; gamma/=np.linalg.norm(gamma)
print('gamma (unit):', np.round(gamma,4), 'rank of SMroots+Y+beta:', np.linalg.matrix_rank(Mrows))
# order-4 elements of the torus exp(i*theta_Y Y + i*theta_g gamma) acting on su(6) roots: character chi(r)=exp(i(tY r.Y + tg r.gamma)); order 4 means chi^4=1 on all roots.
# Search over the lattice: parametrise by the charges of the 22 non-SM su(6) roots; require chi(r) in {1,i,-1,-i} with chi generating order exactly 4 and NO non-SM root with chi=1.
non=[r for r in perp if not any(np.allclose(r,s) for s in SMroots)]
Q=np.array([[r@Y, r@gamma] for r in non])
# generic search: angles (tY,tg) on a fine grid of multiples of pi/2 over the dual lattice: solve chi(r)=exp(2 pi i (n_r/4)) -> find (tY,tg) such that tY*Y.r + tg*g.r = pi/2 * n_r mod 2pi for integers n_r
found=set(); import math
for a in range(0,8):
    for b in range(0,8):
        pass
# simpler: sample the torus finely and test the order-4 condition numerically
sols=[]
for tY in np.linspace(0,2*np.pi,721)[:-1]:
    for tg in np.linspace(0,2*np.pi*4,2881)[:-1]:
        ph=(Q[:,0]*tY+Q[:,1]*tg)
        ph4=(ph*4)%(2*np.pi); ph4=np.minimum(ph4,2*np.pi-ph4)
        if ph4.max()<1e-6:
            ph1=ph%(2*np.pi); ph1=np.minimum(ph1,2*np.pi-ph1)
            ph2=(2*ph)%(2*np.pi); ph2=np.minimum(ph2,2*np.pi-ph2)
            if ph1.min()>1e-6 and ph2.max()>1e-6:   # no root fixed, and not of order 2
                sols.append((round(tY,4),round(tg,4)))
print('order-4 torus elements fixing no non-SM su(6) root (grid samples):', len(sols), sols[:6])
# B1365: gamma's charges on the 27 vs the eta model. 27 weights: 16 (odd # minus? choose the set paired with the 16bar roots) u=1/(2 sqrt3); 10: (+-e_i, -1/sqrt3); 1: (0, 2/sqrt3)
def build27(parity):
    W=[]
    for signs in itertools.product((1,-1),repeat=5):
        neg=sum(1 for s in signs if s<0)
        if neg%2==parity: W.append(np.array([0.5*s for s in signs]+[1/(2*s3)]))
    for i in range(5):
        for a in (1,-1):
            v=np.zeros(6); v[i]=a; v[5]=-1/s3; W.append(v)
    W.append(np.array([0,0,0,0,0,2/s3])); return np.array(W)
for parity in (0,1):
    W=build27(parity); ok=np.allclose((W**2).sum(1),4/3) and set(np.round((W@R.T).flatten()).astype(int))<= {-1,0,1}
    # closure: w + r must be a weight whenever <w,r> = -1
    clos=all(any(np.allclose(w+r,w2) for w2 in W) for w in W for r in R if abs(w@r+1)<1e-9)
    print('27 candidate parity',parity,'norms/ip ok',ok,'closed under roots',clos)
    if ok and clos: W27=W
# field types by SM charges: (su3 rep via weights on idx 0-2, su2 via 3-4, Y)
def typ(w):
    return (round(float(w@Y),4), tuple(np.round(w[:3]*0,0)))
Qy=W27@Y; Qg=W27@gamma; Qb=W27@beta
# group by (Y, gamma) charge
from collections import defaultdict
g=defaultdict(int)
for y,gg,b in zip(Qy,Qg,Qb): g[(round(float(y),4),round(float(gg),4),round(float(b),4))]+=1
print('27: (Y, gamma, beta) charge classes and multiplicities:'); 
for k,v in sorted(g.items()): print('  ',k,v)
# eta model: Q_eta = sqrt(3/8) Q_chi - sqrt(5/8) Q_psi with Q_psi = u-coordinate direction, Q_chi = SO(10)->SU(5) direction (1,1,1,1,1)/... normalised
psi=np.array([0,0,0,0,0,1.0]); chi=np.array([1,1,1,1,1,0.0])/np.sqrt(5)
eta=np.sqrt(3/8)*chi-np.sqrt(5/8)*psi; eta/=np.linalg.norm(eta)
print('gamma vs eta direction: |cos| =', abs(float(gamma@eta)), ' gamma.Y=',float(gamma@Y),' gamma.beta=',float(gamma@beta))
# Kac: order-3 inner automorphism classes of E6: affine marks a=(1,1,2,3,2,1,2) for nodes (0,1,2,3,4,5,6) with 3 the trivalent node; arms: 0-2-3, 1-4-3? use standard: nodes 1-2-3-4-5 chain, 6 attached to 3, 0 attached to 6.
marks={0:1,1:1,2:2,3:3,4:2,5:1,6:2}; edges=[(1,2),(2,3),(3,4),(4,5),(3,6),(6,0)]
def comps(nodes):
    nodes=set(nodes); seen=set(); out=[]
    for n in nodes:
        if n in seen: continue
        stack=[n]; comp=set()
        while stack:
            x=stack.pop()
            if x in comp: continue
            comp.add(x); stack+= [b for a,b in edges if a==x and b in nodes]+[a for a,b in edges if b==x and a in nodes]
        seen|=comp; out.append(frozenset(comp))
    return out
def dynkin_name(comp):
    n=len(comp); deg={x:sum(1 for a,b in edges if (a==x and b in comp) or (b==x and a in comp)) for x in comp}
    if max(deg.values())<=2: return f'A{n}'
    if n==4: return 'D4'
    if n==5: return 'D5'
    if n==6: return 'E6'
    return f'?{n}'
for order in (3,4):
    classes={}
    for s in itertools.product(range(order+1),repeat=7):
        if sum(marks[i]*s[i] for i in range(7))!=order: continue
        zero=[i for i in range(7) if s[i]==0]; fixed=sorted(dynkin_name(c) for c in comps(zero)); nu=sum(1 for i in range(7) if s[i]>0)-1
        key=('+'.join(fixed) if fixed else '') + (f'+{nu}u(1)' if nu else '')
        classes[key]=classes.get(key,0)+1
    print(f'Kac order-{order} inner classes (Kac coordinates, not yet modulo the diagram Z/2):', len(classes), sorted(classes))
