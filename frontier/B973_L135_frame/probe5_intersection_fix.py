"""B973 probe 5: (i) fix the (b) intersection (basis-reduce first);
(ii) derive mu's roots FROM THE BUILD (deg-48 interpolation of
det(ad(g8+t g16)) on e6/core) so no incoming constant enters the chain."""
import sys, json, time, random
sys.path.insert(0,str(_REPO / "frontier/B961_frame_instrument"))
import sympy as sp, frame
from fractions import Fraction as Fr
import pathlib as _pl
_REPO = _pl.Path(__file__).resolve().parents[2]
T0=time.time()
def log(m): print(f"[{time.time()-T0:6.1f}s] {m}",flush=True)
DIM,N=frame.DIM,frame.N; ROOTS,BB,C=frame.ROOTS,frame.BB,frame.C
INV=frame._G["INV"]; CH={n:INV[n] for n in (8,14,16,22)}; R={}
p=40883
def redp(x):
    x=sp.Rational(x); return x.p%p*pow(x.q%p,p-2,p)%p
def matp(M): return [[redp(M[i,j]) for j in range(M.shape[1])] for i in range(M.shape[0])]
def rref(rows):
    rows=[r[:] for r in rows]; n=len(rows[0]) if rows else 0; where={}; r=0
    for c in range(n):
        piv=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        inv=pow(rows[r][c],p-2,p); rows[r]=[v*inv%p for v in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                f=rows[i][c]; rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[r])]
        where[c]=r; r+=1
    return rows,where,r
def rankp(rows): return rref(rows)[2] if rows else 0
def basis_of(vecs):
    rows,where,r=rref(vecs); return [rows[i] for i in range(r)]
def nullp(rows):
    n=len(rows[0]) if rows else DIM
    rows,where,r=rref(rows); free=[c for c in range(n) if c not in where]; out=[]
    for fc in free:
        v=[0]*n; v[fc]=1
        for c,rr in where.items(): v[c]=(-rows[rr][fc])%p
        out.append(v)
    return out
def inter(U,V): return len(U)+len(V)-rankp([list(x) for x in zip(*(U+V))])
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
AD14p,AD22p,AD8p,AD16p=matp(AD[14]),matp(AD[22]),matp(AD[8]),matp(AD[16])
def pen(A,B,t): return [[(A[i][j]+t*B[i][j])%p for j in range(DIM)] for i in range(DIM)]

# ---- mu DERIVED FROM THE BUILD: det of ad(g8 + t g16) on e6/core, deg <= 48 ----
comp=[i for i in range(DIM)]
Bcp=[[redp(Bc[i,j]) for j in range(Bc.shape[1])] for i in range(DIM)]
rowsC,whereC,rC=rref([[Bcp[i][j] for i in range(DIM)] for j in range(Bc.shape[1])])
pivc=sorted(whereC.keys())
compl=[i for i in range(DIM) if i not in pivc]        # 48 complement coords
def qdet(t0):
    A=pen(AD8p,AD16p,t0)
    # ad(x) maps e6 -> e6 and kills core; induced map on e6/core in the complement coords
    M=[[A[i][j] for j in compl] for i in compl]
    # reduce mod core: project rows -- use quotient by eliminating core pivots
    # build full matrix then quotient: image coords modulo core
    full=[[A[i][j] for j in compl] for i in range(DIM)]
    # express each column mod core: subtract core combination killing pivot rows
    Bmat=[[Bcp[i][k] for k in range(Bc.shape[1])] for i in range(DIM)]
    aug=[Bmat[i][:]+full[i][:] for i in range(DIM)]
    rows,where,r=rref(aug)
    nb=Bc.shape[1]
    out=[[rows[where[c]][nb+j] if c in where else 0 for j in range(len(compl))]
         for c in range(nb)]
    # residual after removing core part: rows not pivoted by core columns
    resid=[rows[i][nb:] for i in range(r) if all(rows[i][k]==0 for k in range(nb))]
    resid+= [rows[i][nb:] for i in range(r, len(rows))]
    M2=resid
    if len(M2)!=len(compl): return None
    _,_,rr=rref([row[:] for row in M2])
    # determinant via elimination
    A2=[row[:] for row in M2]; n=len(A2); det=1
    for c in range(n):
        piv=next((i for i in range(c,n) if A2[i][c]),None)
        if piv is None: return 0
        if piv!=c: A2[c],A2[piv]=A2[piv],A2[c]; det=-det%p
        det=det*A2[c][c]%p; inv=pow(A2[c][c],p-2,p)
        A2[c]=[v*inv%p for v in A2[c]]
        for i in range(c+1,n):
            if A2[i][c]:
                f=A2[i][c]; A2[i]=[(a-f*b)%p for a,b in zip(A2[i],A2[c])]
    return det%p
xs=list(range(49)); ys=[qdet(x) for x in xs]
if any(y is None for y in ys):
    log("quotient construction failed"); sys.exit(1)
def lagrange(xs,ys):
    co=[0]*len(xs)
    for i in range(len(xs)):
        num=[1]; den=1
        for j in range(len(xs)):
            if j==i: continue
            num=[(([0]+num)[k]+((-xs[j])%p*(num+[0])[k]))%p for k in range(len(num)+1)]
            den=den*(xs[i]-xs[j])%p
        di=pow(den%p,p-2,p)
        for k in range(len(num)): co[k]=(co[k]+ys[i]*di%p*num[k])%p
    return co
Nco=lagrange(xs,ys)
deg=max(k for k,c in enumerate(Nco) if c)
ok=all(sum(c*pow(t0,k,p) for k,c in enumerate(Nco))%p==qdet(t0) for t0 in range(-6,0))
log(f"N(t) interpolated: degree {deg} (48); 6 extra-node checks {ok}")
mroots=sorted(t0 for t0 in range(p) if sum(c*pow(t0,k,p) for k,c in enumerate(Nco))%p==0)
log(f"N(t) roots mod p (the mu-walls, DERIVED): {mroots}")
R["N_degree"]=deg; R["N_extra_checks"]=bool(ok); R["mu_wall_roots_derived"]=mroots
mu_solo=[2197,-4769856,-2075673600,500716339200]
msr=sorted(t0 for t0 in range(p) if sum(c*pow(t0,k,p) for k,c in enumerate(mu_solo))%p==0)
R["derived_roots_equal_mu_solo_roots"]=(mroots==msr)
log(f"  equal to mu_solo's roots mod p: {mroots==msr}")

# ---- (b) redone with a proper basis ----
kc=[-6859,-56402640,3033676800,2771822592000]
def rootsp(co): return [x for x in range(p) if sum(c*pow(x,k,p) for k,c in enumerate(co))%p==0]
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
BR=basis_of([brp(M12[i],M12[j]) for i in range(12) for j in range(i+1,12)])
R["dim_M12_M12"]=len(BR)
R["M12M12_cap_core"]=inter(BR,corec); R["M12M12_cap_floor"]=inter(BR,floorc)
R["M12M12_cap_M12"]=inter(BR,M12)
log(f"(b) dim[M12,M12] = {len(BR)}; cap core = {R['M12M12_cap_core']} (4); "
    f"cap floor = {R['M12M12_cap_floor']} (4); cap M12 = {R['M12M12_cap_M12']} (12)")
json.dump(R,open(str(_REPO / "frontier/B973_L135_frame/scout_probe5_results.json"),"w"),indent=1,sort_keys=True,default=str)
log("DONE")
