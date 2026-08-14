import os
import io, contextlib, sympy as sp, numpy as np
from sympy.polys.matrices import DomainMatrix
rho, t = sp.symbols('rho t')
MU = [sp.Rational(500716339200), sp.Rational(-2075673600), sp.Rational(-4769856), sp.Rational(2197)]
mu = sp.Poly(sum(c*rho**(3-k) for k,c in enumerate(MU)), rho)
mum = mu.monic()
c1, c0m = mum.all_coeffs()[1], mum.all_coeffs()[3]
c2m = mum.all_coeffs()[2]
# companion matrix of monic mu: multiplication by rho in Q[rho]/mu
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'B854_centralizer_exact', 'e6_centralizer.py')).read(),'b854','exec'), globals())
print("rebuilt", flush=True)
import sympy as sp
CMP = sp.Matrix([[0,0,-mum.all_coeffs()[3]],[1,0,-mum.all_coeffs()[2]],[0,1,-mum.all_coeffs()[1]]])
ID3 = sp.eye(3)
tt = sp.Symbol('tt')
G = {n: sp.Matrix(ADS[n]) for n in ns}
def restrict(M, Nb):
    NT = Nb.T; return (NT*Nb).inv() * (NT*(M*Nb))
p = DomainMatrix.from_Matrix(G[14]).convert_to(sp.QQ).charpoly()
P = sp.Poly([sp.Rational(c) for c in p], t)
r = sp.div(P, sp.gcd(P, P.diff(t)))[0]
facs = [f for f,_ in sp.factor_list(r)[1] if f.degree() > 1]
D14 = DomainMatrix.from_Matrix(G[14]).convert_to(sp.QQ)
mx = max(f.degree() for f in facs)
pows=[sp.eye(78)]; acc=DomainMatrix.eye(78, sp.QQ)
for k in range(1,mx+1): acc=acc*D14; pows.append(acc.to_Matrix())
print("powers done", flush=True)
for f in facs:
    cs=f.all_coeffs()[::-1]; Pf=sp.zeros(78,78)
    for k,c in enumerate(cs):
        if c: Pf += sp.Rational(c)*pows[k]
    Nb=sp.Matrix.hstack(*Pf.nullspace()); d=Nb.shape[1]
    R8, R16 = restrict(G[8],Nb), restrict(G[16],Nb)
    # restriction of scalars: M = R8 (x) I3 + R16 (x) C  over Q, size 3d
    Mblow = sp.Matrix(3*d, 3*d, lambda a,b: 0)
    for i in range(d):
        for j in range(d):
            blk = R8[i,j]*ID3 + R16[i,j]*CMP
            for a in range(3):
                for b in range(3):
                    Mblow[3*i+a, 3*j+b] = blk[a,b]
    print(f"block {d}: blown matrix {3*d}x{3*d}; computing kernel...", flush=True)
    ker = DomainMatrix.from_Matrix(Mblow).convert_to(sp.QQ).nullspace().to_Matrix()
    kd = ker.shape[0]
    print(f"  Q-kernel dim {kd} (predict {3*(d//3)} = per-root {d//3} x deg 3)", flush=True)
    # F-kernel dim = kd/3; F-basis: interpret each Q-vector as F-vector (groups of 3 = coords in basis 1,rho,rho^2)
    # R16 restricted to F-kernel: compute R16blow action on kernel, express in kernel basis
    R16blow = sp.Matrix(3*d, 3*d, lambda a,b: 0)
    for i in range(d):
        for j in range(d):
            blk = R16[i,j]*ID3
            for a in range(3):
                for b in range(3):
                    R16blow[3*i+a, 3*j+b] = blk[a,b]
    
    # charpoly of the Q-linear map = Norm-type; the F-charpoly h(s) satisfies charpoly_Q = Res-type;
    # sum-free test done at the Q-level via mod-q arithmetic in F: pick prime q, root rq of mu, reduce
    import random
    def sumfree_mod(q):
        # find root of mu mod q
        rts = sp.Poly(mu.as_expr(), rho, modulus=q).ground_roots()
        if not rts: return None
        rq = int(list(rts.keys())[0]) % q
        R8q = np.array([[ (sp.Rational(R8[i,j]).p % q)*pow(sp.Rational(R8[i,j]).q % q,-1,q)%q for j in range(d)] for i in range(d)],dtype=np.int64)
        R16q= np.array([[ (sp.Rational(R16[i,j]).p % q)*pow(sp.Rational(R16[i,j]).q % q,-1,q)%q for j in range(d)] for i in range(d)],dtype=np.int64)
        Mq=(R8q+rq*R16q)%q
        # kernel mod q
        A=Mq.copy(); n=d; piv=[]; rr=0
        for c_ in range(d):
            pr=next((x for x in range(rr,n) if A[x,c_]%q),None)
            if pr is None: continue
            A[[rr,pr]]=A[[pr,rr]]; A[rr]=A[rr]*pow(int(A[rr,c_]),-1,q)%q
            for x in range(n):
                if x!=rr and A[x,c_]: A[x]=(A[x]-A[x,c_]*A[rr])%q
            piv.append(c_); rr+=1
        free=[c_ for c_ in range(d) if c_ not in piv]
        kerq=[]
        for fr_ in free:
            v=np.zeros(d,dtype=np.int64); v[fr_]=1
            for idx,c_ in enumerate(piv): v[c_]=(-A[idx,fr_])%q
            kerq.append(v%q)
        Kq=np.array(kerq)
        # eigenvalues of R16 on ker: charpoly of restricted map mod q via similar solve
        m_=Kq.shape[0]
        Rst=np.zeros((m_,m_),dtype=np.int64)
        for a in range(m_):
            w=(R16q@Kq[a])%q
            Aug=np.hstack([Kq.T, w[:,None]])%q
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
        # eigenvalues mod q via charpoly roots (m_ <= 12): brute roots
        cp=[1]
        Msym=sp.Matrix(Rst.tolist())
        chp=sp.Poly(Msym.charpoly(tt).as_expr(), tt, modulus=q)
        eig=[]
        for root,mlt in chp.ground_roots().items():
            eig += [int(root)%q]*mlt
        if len(eig)<m_: return ('nonsplit', None)
        S=set(eig)
        bad=[(a,b) for ii,a in enumerate(eig) for b in eig[ii:] if (a+b)%q in S and (a+b)%q not in (0,)]
        return ('ok', len(bad)==0, sorted(eig)[:6])
    for q in (40123, 40493, 40583):
        res = sumfree_mod(q)
        print(f"  sum-free test mod {q}:", res, flush=True)
print("DONE", flush=True)
