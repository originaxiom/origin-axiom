"""B973 scout probe 4 (SCOUT TIER, one fresh prime p=40883, NOT a banking):
the structural half of the presence side's seven claims, on the bench's own
reconstruction of frame/floor/M12.  Every check paired with a control that
could make it fail.
"""
import sys, json, time
sys.path.insert(0,"/Users/dri/origin-axiom/frontier/B961_frame_instrument")
import sympy as sp, frame
from fractions import Fraction as Fr
T0=time.time()
def log(m): print(f"[{time.time()-T0:6.1f}s] {m}",flush=True)
DIM,N=frame.DIM,frame.N; ROOTS,BB,C=frame.ROOTS,frame.BB,frame.C
INV=frame._G["INV"]; CH={n:INV[n] for n in (8,14,16,22)}; R={}
p=40883
def redp(x):
    x=sp.Rational(x); return x.p%p*pow(x.q%p,p-2,p)%p
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
AD={n:frame.ad(CH[n]) for n in (8,14,16,22)}
core=AD[8].nullspace(); Bc=sp.Matrix.hstack(*core)
P=(Bc.T*Bc).inv()*Bc.T; Fc=sp.Matrix.hstack(*(P*AD[14]*Bc).nullspace()); Bf=Bc*Fc
corec=[[redp(Bc[i,j]) for i in range(DIM)] for j in range(Bc.shape[1])]
floorc=[[redp(Bf[i,j]) for i in range(DIM)] for j in range(Bf.shape[1])]
triples={}
for a in range(DIM):
    for b in range(DIM):
        for r_,c_ in enumerate(BB[a][b]):
            if c_: triples.setdefault(a,[]).append((b,r_,int(c_)))
def brp(u,v):
    out=[0]*DIM
    for a,ua in enumerate(u):
        if not ua: continue
        for b,r_,c_ in triples.get(a,[]):
            if v[b]: out[r_]=(out[r_]+ua*v[b]*c_)%p
    return out
def inter(U,V): return len(U)+len(V)-rankp([list(x) for x in zip(*(U+V))])
kc=[-6859,-56402640,3033676800,2771822592000]
def rootsp(co): return [x for x in range(p) if sum(c*pow(x,k,p) for k,c in enumerate(co))%p==0]
AD14p,AD22p,AD8p,AD16p=matp(AD[14]),matp(AD[22]),matp(AD[8]),matp(AD[16])
def pen(A,B,t): return [[(A[i][j]+t*B[i][j])%p for j in range(DIM)] for i in range(DIM)]
W=[nullp(pen(AD14p,AD22p,r0)) for r0 in sorted(rootsp(kc))]
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
M12=nullp([[sum(v[i]*Kp[i][j] for i in range(DIM) if v[i])%p for j in range(DIM)] for v in W[0]+W[1]+W[2]])
log(f"M12 dim {len(M12)}")
# (a) [M12,M12]
BR=[brp(M12[i],M12[j]) for i in range(12) for j in range(i+1,12)]
dBR=rankp(BR); R["dim_M12_M12"]=dBR
R["escape_beyond_M12"]=rankp([list(x) for x in zip(*(M12+[b for b in BR if any(b)]))])-len(M12)
log(f"(a) dim [M12,M12] = {dBR} (16); escape beyond M12 = {R['escape_beyond_M12']} (4)")
BRb=[b for b in BR if any(b)]
R["escape_cap_floor"]=inter(BRb,floorc)-inter(M12,floorc) if False else None
# (b) the escape is the torus: [M12,M12] cap core and cap floor
R["M12M12_cap_core"]=inter(BRb,corec); R["M12M12_cap_floor"]=inter(BRb,floorc)
log(f"(b) [M12,M12] cap core = {R['M12M12_cap_core']}, cap floor = {R['M12M12_cap_floor']} (4 and 4)")
# (c) module over the floor, zero escape
imgs=[]
for f_ in floorc:
    for v in M12: imgs.append(brp(f_,v))
R["rank_floor_on_M12"]=rankp(imgs)
R["floor_escape"]=rankp([list(x) for x in zip(*(M12+[i_ for i_ in imgs if any(i_)]))])-len(M12)
log(f"(c) rank [floor,M12] = {R['rank_floor_on_M12']} (12); escape = {R['floor_escape']} (0)")
# (d) NOT a module over the FMT so(10): escape 50.  so(10)+u(1) = z(g8 + rho g16) at a mu-wall
mu=[2197,-4769856,-2075673600,500716339200]
mr=sorted(rootsp(mu)); log(f"    mu roots mod p: {mr}")
Z1=nullp(pen(AD8p,AD16p,mr[0])); log(f"    z(x_1) dim = {len(Z1)} (46)")
imgs2=[]
for z_ in Z1:
    for v in M12: imgs2.append(brp(z_,v))
R["so10_escape"]=rankp([list(x) for x in zip(*(M12+[i_ for i_ in imgs2 if any(i_)]))])-len(M12)
log(f"(d) escape of [z(x_1),M12] beyond M12 = {R['so10_escape']} (50)")
# (e) centre of M12
rows=[]
for j in range(12):
    cols=[brp(M12[a],M12[j]) for a in range(12)]
    for i in range(DIM):
        row=[cols[a][i] for a in range(12)]
        if any(row): rows.append(row)
R["M12_centre"]=len(nullp(rows)) if rows else 12
log(f"(e) centre of M12 = {R['M12_centre']} (0)")
# (f) the generation bijection: each mu-wall kills exactly 4 dims of M12
kd=[]
for r0 in mr:
    A=pen(AD8p,AD16p,r0)
    img=[[sum(A[i][k]*v[k] for k in range(DIM) if v[k])%p for i in range(DIM)] for v in M12]
    kd.append(12-rankp(img))
R["kernel_dims_at_mu_walls"]=kd
log(f"(f) dim ker((ad8 + rho_i ad16)|M12) at the three mu-walls = {kd} (4,4,4)")
# CONTROL: a generic rho must give kernel 0
import random; random.seed(5)
g0=random.randrange(p)
while g0 in mr: g0=random.randrange(p)
A=pen(AD8p,AD16p,g0)
img=[[sum(A[i][k]*v[k] for k in range(DIM) if v[k])%p for i in range(DIM)] for v in M12]
R["control_generic_kernel"]=12-rankp(img)
log(f"    CONTROL generic rho: kernel = {R['control_generic_kernel']} (must be 0 -- the test can fail)")
json.dump(R,open("/Users/dri/origin-axiom/frontier/B973_L135_frame/scout_probe4_results.json","w"),indent=1,sort_keys=True,default=str)
log("DONE")
