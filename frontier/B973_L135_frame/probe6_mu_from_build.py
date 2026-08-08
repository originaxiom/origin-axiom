"""B973 probe 6: mu DERIVED FROM THE BUILD -- correct quotient construction.
core is killed by ad(g8 + t g16) for every t, so in the basis [core | complement]
the matrix is [[0,B],[0,Q]] and the induced quotient map is Q."""
import sys, json, time
sys.path.insert(0,"/Users/dri/origin-axiom/frontier/B961_frame_instrument")
import sympy as sp, frame
T0=time.time()
def log(m): print(f"[{time.time()-T0:6.1f}s] {m}",flush=True)
DIM=frame.DIM; INV=frame._G["INV"]; CH={n:INV[n] for n in (8,14,16,22)}
p=40883; R={}
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
AD8=matp(frame.ad(CH[8])); AD16=matp(frame.ad(CH[16]))
corev=[list(v) for v in sp.Matrix(frame.ad(CH[8])).nullspace()]
corec=[[redp(v[i]) for i in range(DIM)] for v in corev]     # 30 vectors, length 78
# complete to a basis: columns = core then unit vectors
cols=[c[:] for c in corec]
rows_,where_,rk=rref([list(x) for x in zip(*cols)])
for i in range(DIM):
    e=[0]*DIM; e[i]=1
    test=cols+[e]
    if rref([list(x) for x in zip(*test)])[2]>len(cols): cols.append(e)
    if len(cols)==DIM: break
assert len(cols)==DIM
T=[[cols[j][i] for j in range(DIM)] for i in range(DIM)]
# invert T mod p
aug=[T[i][:]+[1 if j==i else 0 for j in range(DIM)] for i in range(DIM)]
rr,wh,rk2=rref(aug); assert rk2==DIM
Ti=[[rr[wh[c]][DIM+j] for j in range(DIM)] for c in range(DIM)]
def qdet(t0):
    A=[[(AD8[i][j]+t0*AD16[i][j])%p for j in range(DIM)] for i in range(DIM)]
    AT=[[sum(A[i][k]*T[k][j] for k in range(DIM))%p for j in range(DIM)] for i in range(DIM)]
    B=[[sum(Ti[i][k]*AT[k][j] for k in range(DIM))%p for j in range(DIM)] for i in range(DIM)]
    Q=[[B[i][j] for j in range(30,DIM)] for i in range(30,DIM)]
    n=len(Q); det=1; A2=[r[:] for r in Q]
    for c in range(n):
        piv=next((i for i in range(c,n) if A2[i][c]),None)
        if piv is None: return 0
        if piv!=c: A2[c],A2[piv]=A2[piv],A2[c]; det=(-det)%p
        det=det*A2[c][c]%p; inv=pow(A2[c][c],p-2,p); A2[c]=[v*inv%p for v in A2[c]]
        for i in range(c+1,n):
            if A2[i][c]:
                f=A2[i][c]; A2[i]=[(a-f*b)%p for a,b in zip(A2[i],A2[c])]
    return det%p
# sanity: the top-left 30x30 block and lower-left must vanish (core is killed)
A=[[(AD8[i][j]+7*AD16[i][j])%p for j in range(DIM)] for i in range(DIM)]
AT=[[sum(A[i][k]*T[k][j] for k in range(DIM))%p for j in range(DIM)] for i in range(DIM)]
B=[[sum(Ti[i][k]*AT[k][j] for k in range(DIM))%p for j in range(DIM)] for i in range(DIM)]
R["core_is_killed"]=all(B[i][j]==0 for i in range(DIM) for j in range(30))
log(f"core killed by the pencil (first 30 columns zero): {R['core_is_killed']}")
xs=list(range(49)); ys=[qdet(x) for x in xs]
def lagrange(xs,ys):
    co=[0]*len(xs)
    for i in range(len(xs)):
        num=[1]; den=1
        for j in range(len(xs)):
            if j==i: continue
            num=[((([0]+num)[k] if k<len(num)+1 else 0)+((-xs[j])%p*((num+[0])[k])))%p for k in range(len(num)+1)]
            den=den*(xs[i]-xs[j])%p
        di=pow(den%p,p-2,p)
        for k in range(len(num)): co[k]=(co[k]+ys[i]*di%p*num[k])%p
    return co
Nco=lagrange(xs,ys)
deg=max(k for k,c in enumerate(Nco) if c)
ok=all(sum(c*pow(t0%p,k,p) for k,c in enumerate(Nco))%p==qdet(t0%p) for t0 in range(-6,0))
log(f"N(t) degree {deg} (48); extra-node checks {ok}")
mroots=sorted(t0 for t0 in range(p) if sum(c*pow(t0,k,p) for k,c in enumerate(Nco))%p==0)
log(f"N(t) roots = the noncompact (generation) walls, DERIVED: {mroots}")
mu_solo=[2197,-4769856,-2075673600,500716339200]
msr=sorted(t0 for t0 in range(p) if sum(c*pow(t0,k,p) for k,c in enumerate(mu_solo))%p==0)
log(f"  equal to mu's roots mod p: {mroots==msr}")
# multiplicity 16 check
c_lead=Nco[deg]; import random; random.seed(3); mult=True
for _ in range(8):
    t0=random.randrange(p)
    lhs=sum(c*pow(t0,k,p) for k,c in enumerate(Nco))%p
    rhs=c_lead
    for ri in mroots: rhs=rhs*pow((t0-ri)%p,16,p)%p
    if lhs!=rhs: mult=False
log(f"  N = c * prod(t-r_i)^16 at 8 random points: {mult}")
R.update(N_degree=deg,N_extra_checks=bool(ok),derived_wall_roots=mroots,
         equals_mu_roots=bool(mroots==msr),is_c_times_cubic_pow16=bool(mult))
json.dump(R,open("/Users/dri/origin-axiom/frontier/B973_L135_frame/scout_probe6_results.json","w"),indent=1,sort_keys=True)
log("DONE")
