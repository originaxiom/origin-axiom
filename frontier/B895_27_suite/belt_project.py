# Diagnostic: do the 17 fine-cell triples project onto B884's 11 coarse couplings?
import json, pickle, itertools, io, contextlib
import numpy as np, sympy as sp
import os
RUN = os.environ['HANDOFF4_RUN']  # the solo handoff-4 run dir (session scratchpad)
CB=json.load(open(RUN+'cubic27.json'))
trip=[tuple(t) for t in CB['triples']]; coef=[int(sp.Rational(c)) for c in CB['coeffs']]
D=pickle.load(open(RUN+'rep27.pkl','rb')); REP=D['REP']
CJ=json.load(open(RUN+'cells_40639.json'))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open('/Users/dri/origin-axiom/frontier/B854_centralizer_exact/e6_centralizer.py').read(),'b854','exec'), globals())
q=40639; r1,g1,a1=CJ['tower']; bq=CJ['b']
def rq_(x):
    xr=sp.Rational(x); return (xr.p%q)*pow(xr.q%q,-1,q)%q
def repm(vec):
    M=np.zeros((27,27),dtype=np.int64)
    for k,c in enumerate(vec):
        cc=rq_(c)
        if cc:
            Rk=REP[k]
            for a in range(27):
                for b in range(27):
                    if Rk[a][b]: M[a][b]=(M[a][b]+cc*rq_(Rk[a][b]))%q
    return M
R27={n: repm([sp.Rational(c) for c in INV[n]]) for n in ns}
X1m=(R27[8]+r1*R27[16])%q; Ym=(g1*R27[14]+(q-a1)*R27[16])%q
W3=(bq*R27[16]+(q-g1)*R27[22])%q
combo=(3*X1m+7*Ym+13*W3+17*R27[14])%q
tt=sp.Symbol('tt')
chp=sp.Poly(sp.Matrix(combo.tolist()).charpoly(tt).as_expr(),tt,modulus=q)
def rn(A0):
    A=[[int(x)%q for x in row] for row in A0.tolist()]
    n_=len(A); m_=len(A[0]); piv=[]; rr=0
    for c in range(m_):
        pr=next((x for x in range(rr,n_) if A[x][c]%q),None)
        if pr is None: continue
        A[rr],A[pr]=A[pr],A[rr]
        iv=pow(A[rr][c],-1,q); A[rr]=[(e*iv)%q for e in A[rr]]
        for x in range(n_):
            if x!=rr and A[x][c]:
                f2=A[x][c]; A[x]=[(A[x][j]-f2*A[rr][j])%q for j in range(m_)]
        piv.append(c); rr+=1
    fr=[c for c in range(m_) if c not in piv]; K=[]
    for f3 in fr:
        v=[0]*m_; v[f3]=1
        for i,c in enumerate(piv): v[c]=int((-A[i][f3])%q)
        K.append(v)
    return rr,(np.array(K,dtype=np.int64)%q if K else np.zeros((0,m_),dtype=np.int64))
def ray(M,v):
    den=pow(int((v@v)%q),-1,q); return int((v@((M@v)%q))%q)*den%q
CC=[]
for ev,mlt in chp.ground_roots().items():
    _,V=rn((combo-int(ev)*np.eye(27,dtype=np.int64))%q)
    CC.append(((ray(X1m,V[0]),ray(Ym,V[0])),mlt,V))
print("fine cells:", len(CC))
# coarse label = the (X1,Y) charge pair only
lab={i:CC[i][0] for i in range(len(CC))}
coarse=sorted(set(lab.values()))
print("coarse (X1,Y) classes:", len(coarse), "(B884: 11 cells)")
def cub(u,v,w):
    s=0
    for (a,b,c),cf in zip(trip,coef):
        t=0
        for x,y,z in itertools.permutations((a,b,c)):
            t=(t+int(u[x])*int(v[y])%q*int(w[z]))%q
        s=(s+cf*t)%q
    return s%q
def allowed_with_seed(seed,k=3):
    rng=np.random.default_rng(seed)
    def cv(V):
        return [ (rng.integers(1,q,V.shape[0])@V)%q for _ in range(k) ]
    al=set()
    for i in range(len(CC)):
        for j in range(i,len(CC)):
            for kk in range(j,len(CC)):
                nz=False
                for u in cv(CC[i][2]):
                    for v in cv(CC[j][2]):
                        for w in cv(CC[kk][2]):
                            if cub(u,v,w): nz=True; break
                        if nz: break
                    if nz: break
                if nz: al.add(tuple(sorted((i,j,kk))))
    return al
for seed in (7,11):
    al=allowed_with_seed(seed)
    proj={tuple(sorted((lab[i],lab[j],lab[k]))) for (i,j,k) in al}
    print(f"seed {seed}: fine allowed {len(al)} -> coarse allowed {len(proj)} (B884: 11)")
