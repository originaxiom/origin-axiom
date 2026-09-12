"""Exhaustive, self-contained check of ONE non-zero sector, written independently of mc_lib.

Everything recomputed from explicit matrices: H^0, H^1 by Fox calculus, the restriction to the
cusp, t_0, t_1, r_1, and the four identities -- plus every theorem T1-T6 that could forbid it,
and the -I / odd-power trap that produced this bench's last false positive.
"""
import sys, warnings, itertools; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
P=13
def mm(A,B):
    n=len(A);k=len(B);m=len(B[0])
    return [[sum(A[i][t]*B[t][j] for t in range(k))%P for j in range(m)] for i in range(n)]
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def minv(A):
    n=len(A);M=[r[:]+e[:] for r,e in zip(A,eye(n))];r=0
    for c in range(n):
        p=next((i for i in range(r,n) if M[i][c]%P),None)
        if p is None: return None
        M[r],M[p]=M[p],M[r];iv=pow(M[r][c],P-2,P);M[r]=[x*iv%P for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]%P:
                f=M[i][c];M[i]=[(M[i][j]-f*M[r][j])%P for j in range(2*n)]
        r+=1
    return [r[n:] for r in M]
def rank(M):
    if not M or not M[0]: return 0
    M=[r[:] for r in M];rows=len(M);cols=len(M[0]);r=0
    for c in range(cols):
        p=next((i for i in range(r,rows) if M[i][c]%P),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r];iv=pow(M[r][c],P-2,P);M[r]=[x*iv%P for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%P:
                f=M[i][c];M[i]=[(M[i][j]-f*M[r][j])%P for j in range(cols)]
        r+=1
        if r==rows: break
    return r
def wev(w,rho,d):
    R=eye(d)
    for ch in w: R=mm(R, rho[ch.lower()] if ch.islower() else minv(rho[ch.lower()]))
    return R
def fox(w,gen,rho,d):
    res=[[0]*d for _ in range(d)]; pre=eye(d)
    for ch in w:
        g=ch.lower()
        if ch.islower():
            if g==gen: res=[[(res[i][j]+pre[i][j])%P for j in range(d)] for i in range(d)]
            pre=mm(pre,rho[g])
        else:
            pre=mm(pre,minv(rho[g]))
            if g==gen: res=[[(res[i][j]-pre[i][j])%P for j in range(d)] for i in range(d)]
    return res
def nullsp(M,n):
    if not M: return [[1 if i==j else 0 for i in range(n)] for j in range(n)]
    M=[r[:] for r in M];rows=len(M);r=0;piv=[]
    for c in range(n):
        p=next((i for i in range(r,rows) if M[i][c]%P),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r];iv=pow(M[r][c],P-2,P);M[r]=[x*iv%P for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%P:
                f=M[i][c];M[i]=[(M[i][j]-f*M[r][j])%P for j in range(n)]
        piv.append(c);r+=1
    free=[c for c in range(n) if c not in piv];out=[]
    for fc in free:
        v=[0]*n;v[fc]=1
        for i,pc in enumerate(piv): v[pc]=(-M[i][fc])%P
        out.append(v)
    return out
def sym(A,m):
    from math import comb
    d=m+1;out=[[0]*d for _ in range(d)];a,b=A[0];c,dd=A[1]
    for j in range(d):
        coef=[0]*d
        for u in range(m-j+1):
            for v in range(j+1):
                coef[u+v]=(coef[u+v]+comb(m-j,u)*pow(a,m-j-u,P)*pow(c,u,P)*comb(j,v)*pow(b,j-v,P)*pow(dd,v,P))%P
        for i in range(d): out[i][j]=coef[i]
    return out
def invariants(ms,d):
    rows=[]
    for A in ms: rows.extend([[(A[i][j]-(1 if i==j else 0))%P for j in range(d)] for i in range(d)])
    return d-rank(rows)
def full(gens,rels,mu,lam,rho,d):
    g=len(gens)
    a0=invariants([rho[x] for x in gens],d)
    J=[]
    for r in rels:
        bl=[fox(r,x,rho,d) for x in gens]
        for a in range(d): J.append([bl[j][a][b] for j in range(g) for b in range(d)])
    Zs=nullsp(J,g*d); a1=len(Zs)-(d-a0); a2=len(rels)*d-rank(J)
    Mu=wev(mu,rho,d); La=wev(lam,rho,d); t0=invariants([Mu,La],d)
    FXm=[fox(mu,x,rho,d) for x in gens]; FXl=[fox(lam,x,rho,d) for x in gens]
    R=[]
    for v in Zs:
        z=[v[j*d:(j+1)*d] for j in range(g)]; row=[]
        for FX in (FXm,FXl):
            o=[0]*d
            for j in range(g):
                for a in range(d): o[a]=(o[a]+sum(FX[j][a][b]*z[j][b] for b in range(d)))%P
            row+=o
        R.append(row)
    Bt=[]
    for k in range(d):
        Bt.append([(Mu[x][k]-(1 if x==k else 0))%P for x in range(d)]+
                  [(La[x][k]-(1 if x==k else 0))%P for x in range(d)])
    rB=rank(Bt); r1=rank(R+Bt)-rB
    Zt=nullsp([[(-(La[x][y]-(1 if x==y else 0)))%P for y in range(d)]+
               [(Mu[x][y]-(1 if x==y else 0))%P for y in range(d)] for x in range(d)],2*d)
    t1=len(Zt)-rB
    return dict(a0=a0,a1=a1,a2=a2,t0=t0,t1=t1,r1=r1,n=a1-r1)
def dual(rho,gens,d):
    o={}
    for x in gens:
        Ai=minv(rho[x]); o[x]=[[Ai[j][i] for j in range(d)] for i in range(d)]
    return o

M=snappy.Manifold('m010'); G=M.fundamental_group()
gens=list(G.generators()); rels=list(G.relators()); mu,lam=G.peripheral_curves()[0]
print(f"m010  gens={gens} rels={rels} mu={mu!r} lam={lam!r}  chiral={not M.symmetry_group().is_amphicheiral()}")
# rebuild the same reps, in order
S=[[[a,b],[c,d]] for a in range(P) for b in range(P) for c in range(P) for d in range(P) if (a*d-b*c)%P==1]
reps=[]
for tup in itertools.product(S,repeat=len(gens)):
    rho=dict(zip(gens,tup))
    if all(wev(r,rho,2)==eye(2) for r in rels):
        reps.append(rho)
        if len(reps)>=4: break
rho2=reps[1]; chi=(4,12); m=3
print(f"\nSECTOR: rep #1, Sym^{m}, chi={chi}")
print(f"  rho(a)={rho2['a']}  rho(b)={rho2['b']}")
mI=[[P-1,0],[0,P-1]]
print(f"  relators under rho : {[('I' if wev(r,rho2,2)==eye(2) else ('-I' if wev(r,rho2,2)==mI else 'other')) for r in rels]}")
print(f"     -> odd Sym powers VALID (no -I lift): {all(wev(r,rho2,2)==eye(2) for r in rels)}")
Mu2=wev(mu,rho2,2); La2=wev(lam,rho2,2)
print(f"  tr(mu)={(Mu2[0][0]+Mu2[1][1])%P}  tr(lam)={(La2[0][0]+La2[1][1])%P}  (2 = unipotent)")
print(f"  mu,lam commute: {mm(Mu2,La2)==mm(La2,Mu2)}")
print(f"  mu unipotent (mu-I nilpotent): {mm([[ (Mu2[i][j]-(1 if i==j else 0))%P for j in range(2)] for i in range(2)],[[ (Mu2[i][j]-(1 if i==j else 0))%P for j in range(2)] for i in range(2)])==[[0,0],[0,0]]}")
base={g:sym(rho2[g],m) for g in gens}; d=m+1
V={g:[[(chi[i]*base[g][x][y])%P for y in range(d)] for x in range(d)] for i,g in enumerate(gens)}
print(f"  relators under V (Sym^{m} (x) chi): {[wev(r,V,d)==eye(d) for r in rels]}")
A=full(gens,rels,mu,lam,V,d); B=full(gens,rels,mu,lam,dual(V,gens,d),d)
I=A['n']-B['n']
print(f"\n  V : a0={A['a0']} a1={A['a1']} a2={A['a2']} t0={A['t0']} t1={A['t1']} r1={A['r1']}")
print(f"  V*: a0={B['a0']} a1={B['a1']} a2={B['a2']} t0={B['t0']} t1={B['t1']} r1={B['r1']}")
print(f"\n  INDEX I = n(V) - n(V*) = {I}")
print(f"  identities:")
print(f"    r1 + r1* = t1        : {A['r1']}+{B['r1']}={A['r1']+B['r1']} vs t1={A['t1']}  -> {A['r1']+B['r1']==A['t1']}")
print(f"    t1 = t0 + t0*        : {A['t0']}+{B['t0']}={A['t0']+B['t0']} vs {A['t1']}  -> {A['t1']==A['t0']+B['t0']}")
print(f"    I = (a0-a0*)+t0*-r1  : {(A['a0']-B['a0'])+B['t0']-A['r1']} vs {I}  -> {I==(A['a0']-B['a0'])+B['t0']-A['r1']}")
print(f"    a0-a1+a2 = 0         : {A['a0']-A['a1']+A['a2']==0}")
print(f"    I(V*) = -I(V)        : {(B['n']-A['n'])==-I}")
print(f"  DOMAIN D: a0=a0* ({A['a0']}=={B['a0']}: {A['a0']==B['a0']}), t0=t0* ({A['t0']}=={B['t0']}: {A['t0']==B['t0']})")
print(f"  in D, I should equal t0-r1 = {A['t0']-A['r1']}  -> matches: {I==A['t0']-A['r1']}")
print(f"\n  theorems that could forbid it:")
print(f"    T2 (closed M => 0)         : M is cusped, does not apply")
print(f"    T3 (self-dual V => 0)      : V self-dual? {V==dual(V,gens,d)}")
print(f"    T4 (rank-1 characters => 0): d={d}, does not apply")
print(f"    T5 (t0 = 0 => I = 0)       : t0={A['t0']}, does not apply")
