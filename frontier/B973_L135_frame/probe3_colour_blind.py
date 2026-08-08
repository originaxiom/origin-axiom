"""B973 scout probe 3: is the FLOOR's su(3) the same object as B958/B961's
'su(3)_colour', and does M12 sit inside its centralizer?

Scout tier: one fresh prime, no banking. Uses only bench-owned material.
"""
import sys, json, time
sys.path.insert(0, "/Users/dri/origin-axiom/frontier/B961_frame_instrument")
import sympy as sp, frame
from fractions import Fraction as Fr
T0=time.time()
def log(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)
DIM, N = frame.DIM, frame.N
ROOTS, BB, C = frame.ROOTS, frame.BB, frame.C
INV = frame._G["INV"]; CH = {n: INV[n] for n in (8,14,16,22)}
R={}
AD={n: frame.ad(CH[n]) for n in (8,14,16,22)}
core=AD[8].nullspace(); Bc=sp.Matrix.hstack(*core)
P=(Bc.T*Bc).inv()*Bc.T; C14=P*AD[14]*Bc
Fc=sp.Matrix.hstack(*C14.nullspace()); Bf=Bc*Fc
floor=[[Fr(sp.Rational(Bf[i,j]).p, sp.Rational(Bf[i,j]).q) for i in range(DIM)] for j in range(Bf.shape[1])]
su3=frame.derived(floor)
log(f"su(3)_floor := derived(floor): dim {frame.dim_of(su3)}")
Z=frame.centralizer([[Fr(sp.Rational(x).p, sp.Rational(x).q) for x in v] for v in su3])
R["dim_su3_floor"]=int(frame.dim_of(su3))
R["dim_Z_su3_floor"]=len(Z)
log(f"dim Z_e6(su(3)_floor) = {len(Z)}   [B958/B961 got 16 for the STANDARD A2 Levi]")
# does the floor sit inside Z(su3_floor)?  (it must: floor = su3 + centre, su3 has centre 0
# so no -- su3 does NOT centralize itself.  report the honest containment test instead)
R["floor_dim"]=len(floor)

# ---- mod p: is M12 colour-blind, i.e. [su(3)_floor, M12] = 0 ? ----
p=40883
def redp(x):
    x=sp.Rational(x); return x.p % p * pow(x.q % p, p-2, p) % p
def matp(M): return [[redp(M[i,j]) for j in range(M.shape[1])] for i in range(M.shape[0])]
def rankp(rows):
    rows=[r[:] for r in rows]; n=len(rows[0]) if rows else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        inv=pow(rows[r][c],p-2,p); rows[r]=[v*inv%p for v in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                f=rows[i][c]; rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows): break
    return r
def nullp(rows):
    n=len(rows[0]) if rows else DIM
    rows=[r[:] for r in rows]; where={}; r=0
    for c in range(n):
        piv=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        inv=pow(rows[r][c],p-2,p); rows[r]=[v*inv%p for v in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                f=rows[i][c]; rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[r])]
        where[c]=r; r+=1
    free=[c for c in range(n) if c not in where]; out=[]
    for fc in free:
        v=[0]*n; v[fc]=1
        for c,rr in where.items(): v[c]=(-rows[rr][fc])%p
        out.append(v)
    return out
def rootsp(co):
    return [x for x in range(p) if sum(c*pow(x,k,p) for k,c in enumerate(co))%p==0]
kc=[-6859,-56402640,3033676800,2771822592000]   # kappa, re-derived in probe 2 this session
AD14p,AD22p=matp(AD[14]),matp(AD[22])
def pencil(A,B,t): return [[(A[i][j]+t*B[i][j])%p for j in range(DIM)] for i in range(DIM)]
W=[nullp(pencil(AD14p,AD22p,r0)) for r0 in sorted(rootsp(kc))]
K=[[0]*DIM for _ in range(DIM)]
for i in range(N):
    for j in range(N):
        K[i][j]=sum((sum(r[k]*C[i][k] for k in range(N)))*(sum(r[k]*C[j][k] for k in range(N))) for r in ROOTS)
for ri,r in enumerate(ROOTS):
    mi=ROOTS.index(tuple(-x for x in r)); tr=Fr(0)
    for k in range(DIM):
        w=BB[N+mi][k]; acc=Fr(0)
        for pdx,wp in enumerate(w):
            if wp: acc+=wp*BB[N+ri][pdx][k]
        tr+=acc
    K[N+ri][N+mi]=int(tr)
Kp=[[K[i][j]%p for j in range(DIM)] for i in range(DIM)]
rows=[[sum(v[i]*Kp[i][j] for i in range(DIM) if v[i])%p for j in range(DIM)] for v in W[0]+W[1]+W[2]]
M12=nullp(rows)
log(f"M12 dim {len(M12)}")
su3p=[[redp(x) for x in v] for v in su3]
ADsu3=[matp(frame.ad([Fr(sp.Rational(x).p, sp.Rational(x).q) for x in v])) for v in su3]
imgs=[]
for A in ADsu3:
    for v in M12:
        imgs.append([sum(A[i][k]*v[k] for k in range(DIM) if v[k])%p for i in range(DIM)])
esc=rankp(imgs)
R["rank_su3floor_on_M12"]=esc
log(f"rank of [su(3)_floor, M12] = {esc}   (0 <=> M12 is colour-BLIND, every su(3) weight (0,0))")
# control: the same test with the four charges must NOT be 0
imgs2=[]
for n in (8,14,16,22):
    A=matp(AD[n])
    for v in M12:
        imgs2.append([sum(A[i][k]*v[k] for k in range(DIM) if v[k])%p for i in range(DIM)])
R["control_rank_charges_on_M12"]=rankp(imgs2)
log(f"CONTROL rank of [torus, M12] = {R['control_rank_charges_on_M12']} (must be nonzero: the test can fail)")
# and a second control: su(3)_floor acting on the CORE must be nonzero
imgs3=[]
corep=[[redp(Bc[i,j]) for i in range(DIM)] for j in range(Bc.shape[1])]
for A in ADsu3:
    for v in corep:
        imgs3.append([sum(A[i][k]*v[k] for k in range(DIM) if v[k])%p for i in range(DIM)])
R["control_rank_su3floor_on_core"]=rankp(imgs3)
log(f"CONTROL rank of [su(3)_floor, core] = {R['control_rank_su3floor_on_core']} (nonzero: the operator is not the zero map)")
json.dump(R,open("/Users/dri/origin-axiom/frontier/B973_L135_frame/scout_probe3_results.json","w"),indent=1,sort_keys=True)
log("DONE")
