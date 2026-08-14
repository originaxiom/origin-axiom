import os
import io, contextlib, sympy as sp, numpy as np
rho, tt = sp.symbols('rho tt')
mu = sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197, rho)
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'B854_centralizer_exact', 'e6_centralizer.py')).read(),'b854','exec'), globals())
import sympy as sp
print("rebuilt", flush=True)
t = sp.Symbol('t_')
G = {n: sp.Matrix(ADS[n]) for n in ns}
def restrict(M, Nb):
    NT = Nb.T; return (NT*Nb).inv() * (NT*(M*Nb))
from sympy.polys.matrices import DomainMatrix
p_ = DomainMatrix.from_Matrix(G[14]).convert_to(sp.QQ).charpoly()
P = sp.Poly([sp.Rational(c) for c in p_], t)
r = sp.div(P, sp.gcd(P, P.diff(t)))[0]
facs = [f for f,_ in sp.factor_list(r)[1] if f.degree() == 6]
D14 = DomainMatrix.from_Matrix(G[14]).convert_to(sp.QQ)
pows=[sp.eye(78)]; acc=DomainMatrix.eye(78, sp.QQ)
for k in range(1,7): acc=acc*D14; pows.append(acc.to_Matrix())
Rs = []
for f in facs:
    cs=f.all_coeffs()[::-1]; Pf=sp.zeros(78,78)
    for k,c in enumerate(cs):
        if c: Pf += sp.Rational(c)*pows[k]
    Nb=sp.Matrix.hstack(*Pf.nullspace()); d=Nb.shape[1]
    if d in (12,36):
        Rs.append((d, restrict(G[8],Nb), restrict(G[16],Nb)))
print("blocks restricted:", [d for d,_,_ in Rs], flush=True)
def eig_on_ker(R8s, R16s, d, rq, q):
    R8q = np.array([[ (sp.Rational(R8s[i,j]).p % q)*pow(sp.Rational(R8s[i,j]).q % q,-1,q)%q for j in range(d)] for i in range(d)],dtype=np.int64)
    R16q= np.array([[ (sp.Rational(R16s[i,j]).p % q)*pow(sp.Rational(R16s[i,j]).q % q,-1,q)%q for j in range(d)] for i in range(d)],dtype=np.int64)
    Mq=(R8q+rq*R16q)%q
    A=Mq.copy(); piv=[]; rr=0
    for c_ in range(d):
        pr=next((x for x in range(rr,d) if A[x,c_]%q),None)
        if pr is None: continue
        A[[rr,pr]]=A[[pr,rr]]; A[rr]=A[rr]*pow(int(A[rr,c_]),-1,q)%q
        for x in range(d):
            if x!=rr and A[x,c_]: A[x]=(A[x]-A[x,c_]*A[rr])%q
        piv.append(c_); rr+=1
    free=[c_ for c_ in range(d) if c_ not in piv]
    K=np.array([[1 if c_==f_ else (-A[[i for i,pc in enumerate(piv) if pc==c_][0],f_]%q if c_ in piv else 0) for c_ in range(d)] for f_ in free],dtype=np.int64)%q
    # fix construction
    K=[]
    for f_ in free:
        v=np.zeros(d,dtype=np.int64); v[f_]=1
        for idx,c_ in enumerate(piv): v[c_]=(-A[idx,f_])%q
        K.append(v%q)
    K=np.array(K); m_=K.shape[0]
    Rst=np.zeros((m_,m_),dtype=np.int64)
    for a in range(m_):
        w=(R16q@K[a])%q
        Aug=np.hstack([K.T, w[:,None]])%q
        A2=Aug.copy(); rr2=0; piv2=[]
        for c_ in range(m_):
            pr=next((x for x in range(rr2,d) if A2[x,c_]%q),None)
            if pr is None: continue
            A2[[rr2,pr]]=A2[[pr,rr2]]; A2[rr2]=A2[rr2]*pow(int(A2[rr2,c_]),-1,q)%q
            for x in range(d):
                if x!=rr2 and A2[x,c_]: A2[x]=(A2[x]-A2[x,c_]*A2[rr2])%q
            piv2.append(c_); rr2+=1
        sol=np.zeros(m_,dtype=np.int64)
        for idx,c_ in enumerate(piv2): sol[c_]=A2[idx,m_]%q
        Rst[:,a]=sol
    chp=sp.Poly(sp.Matrix(Rst.tolist()).charpoly(tt).as_expr(), tt, modulus=q)
    eig=[]
    for root,mlt in chp.ground_roots().items(): eig += [int(root)%q]*mlt
    return eig if len(eig)==m_ else None
for q in (40123, 40493):
    rts = [int(x)%q for x in sp.Poly(mu.as_expr(), rho, modulus=q).ground_roots()]
    all_ok = True
    for rq in rts:
        combined=[]
        for d,R8s,R16s in Rs:
            e = eig_on_ker(R8s,R16s,d,rq,q)
            if e is None: combined=None; break
            combined += e
        if combined is None: all_ok=None; break
        S=set(combined)
        bad=[(a,b) for i,a in enumerate(combined) for b in combined[i:] if (a+b)%q in S and (a+b)%q != 0]
        print(f"q={q} root {rq}: combined charge multiset size {len(combined)}; SUM-FREE: {len(bad)==0}", flush=True)
        all_ok = all_ok and len(bad)==0
    print(f"q={q}: ALL ROOTS SUM-FREE: {all_ok}", flush=True)
print("DONE", flush=True)
