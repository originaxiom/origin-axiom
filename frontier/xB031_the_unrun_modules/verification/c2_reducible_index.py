#!/usr/bin/env python3
"""B1418 cell 2 -- THE REDUCIBLE-LOCUS INDEX. B1413's exact instrument generalised to n generators and to any number field
K = Q(alpha) (primitive element with minimal polynomial MIN), with K-ranks computed exactly as Q-ranks of regular-representation
block matrices (rank_Q = deg(K) * rank_K). For a character chi: H_1 -> K^x, the reducible non-split rho = [[chi, c],[0, chi^-1]]
with c a non-coboundary 1-cocycle in Z^1(pi; K_{chi^2}) (existence decided by Fox calculus), V = Sym^m(rho) (x) psi, and
I = n(V) - n(V*), n = a_1 - r_1 (B1297's definition, B1413's stacked-rank identity). Usage: see main()."""
import sys, itertools, json, time
from fractions import Fraction as Fr
import sympy as sp, snappy
from sympy.polys.matrices import DomainMatrix
from sympy import QQ

class NF:
    """Number field Q[x]/(MIN), elements as tuples of Fractions (coefficients of 1, x, ..., x^(d-1))."""
    def __init__(self, minpoly_coeffs):        # monic, low -> high
        self.c=[Fr(x) for x in minpoly_coeffs]; assert self.c[-1]==1; self.d=len(self.c)-1
    def el(self, v):
        v=[Fr(x) for x in v]+[Fr(0)]*self.d; return tuple(v[:self.d])
    def const(self,q): return self.el([q])
    def alpha(self): return self.el([0,1])
    def add(self,a,b): return tuple(x+y for x,y in zip(a,b))
    def sub(self,a,b): return tuple(x-y for x,y in zip(a,b))
    def neg(self,a): return tuple(-x for x in a)
    def mul(self,a,b):
        d=self.d; p=[Fr(0)]*(2*d-1)
        for i,x in enumerate(a):
            if x==0: continue
            for j,y in enumerate(b):
                if y!=0: p[i+j]+=x*y
        for k in range(2*d-2,d-1,-1):          # reduce x^k using MIN
            if p[k]!=0:
                q=p[k]; p[k]=Fr(0)
                for i in range(d): p[k-d+i]-=q*self.c[i]
        return tuple(p[:d])
    def is_zero(self,a): return all(x==0 for x in a)
    def regmat(self,a):
        """d x d rational matrix of multiplication by a in the basis 1, x, .., x^(d-1) (columns = images of basis)."""
        cols=[]; x=self.const(1)
        for i in range(self.d):
            cols.append(self.mul(a,x)); x=self.mul(x,self.alpha())
        return [[cols[j][i] for j in range(self.d)] for i in range(self.d)]
    def inv(self,a):
        # solve a*b = 1 via the regular representation
        M=sp.Matrix(self.regmat(a)); e=sp.Matrix([1]+[0]*(self.d-1)); b=M.LUsolve(e); return tuple(Fr(int(x.p),int(x.q)) for x in b)
    def pw(self,a,n):
        r=self.const(1)
        for _ in range(n): r=self.mul(r,a)
        return r
def kmat_mul(K,P,Q):
    n=len(P); m=len(Q[0]); k=len(Q)
    return [[ (lambda i,j: __import__('functools').reduce(K.add,[K.mul(P[i][l],Q[l][j]) for l in range(k)],K.const(0)))(i,j) for j in range(m)] for i in range(n)]
def kmat_eye(K,n): return [[K.const(1) if i==j else K.const(0) for j in range(n)] for i in range(n)]
def kmat_sub(K,P,Q): return [[K.sub(P[i][j],Q[i][j]) for j in range(len(P[0]))] for i in range(len(P))]
def kmat_rank(K,P):
    if not P or not P[0]: return 0
    rows=[]
    for i in range(len(P)):
        for a in range(K.d):
            row=[]
            for j in range(len(P[0])):
                R=K.regmat(P[i][j]); row+= [QQ(int(R[a][b].numerator),int(R[a][b].denominator)) for b in range(K.d)]
            rows.append(row)
    dm=DomainMatrix(rows,(len(rows),len(rows[0])),QQ); r=dm.rank(); assert r%K.d==0, (r,K.d); return r//K.d
def kmat_inv(K,P):
    n=len(P)
    # Gauss-Jordan over K
    A=[[P[i][j] for j in range(n)]+[K.const(1) if i==j else K.const(0) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv=next(r for r in range(col,n) if not K.is_zero(A[r][col])); A[col],A[piv]=A[piv],A[col]
        inv=K.inv(A[col][col]); A[col]=[K.mul(inv,x) for x in A[col]]
        for r in range(n):
            if r!=col and not K.is_zero(A[r][col]):
                f=A[r][col]; A[r]=[K.sub(x,K.mul(f,y)) for x,y in zip(A[r],A[col])]
    return [row[n:] for row in A]
def kmat_T(P): return [list(r) for r in zip(*P)]
def sym_power(K,P,m):
    """Sym^m of a 2x2 matrix on the basis x^m, x^(m-1) y, ..., y^m (column j = image of x^(m-j) y^j)."""
    a,b=P[0]; c,d=P[1]
    # (a x + c y)^(m-j) (b x + d y)^j expanded: coefficient of x^(m-i) y^i
    from math import comb
    cols=[]
    for j in range(m+1):
        coef=[K.const(0)]*(m+1)
        for s in range(m-j+1):
            for tt in range(j+1):
                term=K.mul(K.mul(K.const(comb(m-j,s)),K.mul(K.pw(a,m-j-s),K.pw(c,s))),K.mul(K.const(comb(j,tt)),K.mul(K.pw(b,j-tt),K.pw(d,tt))))
                coef[s+tt]=K.add(coef[s+tt],term)
        cols.append(coef)
    return [[cols[j][i] for j in range(m+1)] for i in range(m+1)]
def word_matrix(K,word,D):
    n=len(next(iter(D.values()))); R=kmat_eye(K,n)
    for ch in word: R=kmat_mul(K,R,D[ch])
    return R
def fox(K,word,D,gens):
    n=len(next(iter(D.values()))); val=kmat_eye(K,n); dd={g:[[K.const(0)]*n for _ in range(n)] for g in gens}
    for ch in word:
        g=ch.lower(); X=D[ch]
        if ch.islower(): dd[g]=[[K.add(dd[g][i][j],val[i][j]) for j in range(n)] for i in range(n)]
        else:
            vx=kmat_mul(K,val,X); dd[g]=[[K.sub(dd[g][i][j],vx[i][j]) for j in range(n)] for i in range(n)]
        val=kmat_mul(K,val,X)
    return val, dd
def hstack(*Ms): return [sum((list(M[i]) for M in Ms),[]) for i in range(len(Ms[0]))]
def vstack(*Ms): return [list(r) for M in Ms for r in M]
def counts(K,gens,rels,mu,lam,rep,label,verbose=True):
    """rep: dict generator -> K-matrix (n x n); returns n_int = a1 - r1, plus (a0,a1,t0,r1)."""
    n=len(rep[gens[0]]); I=kmat_eye(K,n); D={}
    for g in gens: D[g]=rep[g]; D[g.upper()]=kmat_inv(K,rep[g])
    for r in rels:
        val,_=fox(K,r,D,gens); assert all(K.is_zero(x) for row in kmat_sub(K,val,I) for x in row), label+' relator not identity'
    d0=vstack(*[kmat_sub(K,D[g],I) for g in gens]); r0=kmat_rank(K,d0); a0=n-r0
    d1=vstack(*[hstack(*[fox(K,r,D,gens)[1][g] for g in gens]) for r in rels]); r1d=kmat_rank(K,d1); a1=(len(gens)*n-r1d)-r0
    _,fm=fox(K,mu,D,gens); _,fl=fox(K,lam,D,gens)
    Rmu=hstack(*[fm[g] for g in gens]); Rlam=hstack(*[fl[g] for g in gens])
    Wm,Wl=word_matrix(K,mu,D),word_matrix(K,lam,D)
    BT=vstack(kmat_sub(K,Wm,I),kmat_sub(K,Wl,I)); R=vstack(Rmu,Rlam)
    zeros=[[K.const(0)]*n for _ in range(len(d1))]
    block=vstack(hstack(d1,zeros),hstack(R,BT))
    rT=kmat_rank(K,block)-r1d-kmat_rank(K,BT); t0=n-kmat_rank(K,BT)
    n_int=a1-rT
    if verbose: print(f'  {label:34s} a0={a0} a1={a1} t0={t0} r1={rT} n=a1-r1={n_int}', flush=True)
    return n_int,(a0,a1,t0,rT)
def dual(K,rep): return {g:kmat_T(kmat_inv(K,M)) for g,M in rep.items()}
def char_on_word(K,word,chi):
    v=K.const(1)
    for ch in word: v=K.mul(v, chi[ch.lower()] if ch.islower() else K.inv(chi[ch.lower()]))
    return v
def nonsplit_cocycle(K,gens,rels,chi2):
    """H^1(pi; K_{chi2}): one-dimensional Fox complex. Returns a cocycle c (dict gen -> K) that is NOT a coboundary, or None."""
    D={}
    for g in gens: D[g]=[[chi2[g]]]; D[g.upper()]=[[K.inv(chi2[g])]]
    d1=vstack(*[hstack(*[fox(K,r,D,gens)[1][g] for g in gens]) for r in rels])   # (#rels) x (#gens)
    d0=[[K.sub(chi2[g],K.const(1))] for g in gens]                               # (#gens) x 1
    r1=kmat_rank(K,d1); z1=len(gens)-r1; b1=kmat_rank(K,d0); h1=z1-b1
    if h1<=0: return None,h1
    # nullspace of d1 over K: solve via sympy over the regular representation is heavy; use K-Gauss elimination on d1 to get a kernel vector not in span(d0)
    # kernel by Gaussian elimination over K
    rows=[list(r) for r in d1]; n=len(gens); piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,len(rows)) if not K.is_zero(rows[i][c])),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]; inv=K.inv(rows[r][c]); rows[r]=[K.mul(inv,x) for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and not K.is_zero(rows[i][c]):
                f=rows[i][c]; rows[i]=[K.sub(x,K.mul(f,y)) for x,y in zip(rows[i],rows[r])]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]
    kernel=[]
    for fc in free:
        v=[K.const(0)]*n; v[fc]=K.const(1)
        for i,pc in enumerate(piv): v[pc]=K.neg(rows[i][fc])
        kernel.append(v)
    cob=[d0[i][0] for i in range(n)]
    for v in kernel:
        # is v a multiple of the coboundary vector?
        M=[[cob[i],v[i]] for i in range(n)]
        if kmat_rank(K,M)==2 or b1==0: return dict(zip(gens,v)),h1
    return None,h1
def reducible_rep(K,gens,chi,c):
    """rho(g) = [[chi(g), c(g)], [0, chi(g)^-1]] is a representation iff ctilde(g) := c(g) chi(g) is a 1-cocycle for the
    left action of chi^2 (ctilde(gh) = chi(g)^2 ctilde(h) + ctilde(g)); nonsplit_cocycle returns ctilde, so c = ctilde / chi."""
    return {g:[[chi[g],K.mul(c[g],K.inv(chi[g]))],[K.const(0),K.inv(chi[g])]] for g in gens}
def module(K,gens,rep2,m,psi):
    V={g:sym_power(K,rep2[g],m) for g in gens}
    return {g:[[K.mul(psi[g],x) for x in row] for row in V[g]] for g in gens}
def semisimplification(K,gens,chi,m,psi):
    return module(K,gens,{g:[[chi[g],K.const(0)],[K.const(0),K.inv(chi[g])]] for g in gens},m,psi)
def run_module(K,name,gens,rels,mu,lam,chi,c,m,psi,label):
    rep2=reducible_rep(K,gens,chi,c)
    V=module(K,gens,rep2,m,psi); nV,dV=counts(K,gens,rels,mu,lam,V,label+' V')
    nVd,dVd=counts(K,gens,rels,mu,lam,dual(K,V),label+' V*')
    S=semisimplification(K,gens,chi,m,psi); nS,_=counts(K,gens,rels,mu,lam,S,label+' V^ss'); nSd,_=counts(K,gens,rels,mu,lam,dual(K,S),label+' V^ss*')
    I=nV-nVd; Iss=nS-nSd
    print(f'==> {name} {label}: I(V) = {I}   I(V^ss) = {Iss}', flush=True)
    return {'name':name,'label':label,'I':I,'I_ss':Iss,'V':dV,'V*':dVd}
def presentation(name):
    M=snappy.Manifold(name); G=M.fundamental_group(); mu,lam=G.peripheral_curves()[0]
    return M,G.generators(),G.relators(),mu,lam
def control_m010():
    K=NF([1,-1,1])   # u^2 - u + 1
    M,gens,rels,mu,lam=presentation('m010'); u=K.alpha()
    chi={'a':u,'b':K.const(-1)}
    print('m010', gens, rels, (mu,lam), 'chi on relators/mu/lambda:', [char_on_word(K,r,chi) for r in rels], char_on_word(K,mu,chi), char_on_word(K,lam,chi))
    # the lane's A, B: A = [[0,1],[-1,1]], B = [[0,u^2],[u,-2]] -- use them directly (a known reducible non-split rep) and ALSO our cocycle construction
    A=[[K.const(0),K.const(1)],[K.const(-1),K.const(1)]]; B=[[K.const(0),K.pw(u,2)],[u,K.const(-2)]]
    rep={'a':A,'b':B}; psi={'a':K.const(1),'b':K.const(1)}
    V={g:[[K.mul(chi[g],x) for x in row] for row in sym_power(K,rep[g],3)] for g in gens}
    nV,_=counts(K,gens,rels,mu,lam,V,'lane witness V=Sym3(x)chi'); nVd,_=counts(K,gens,rels,mu,lam,dual(K,V),'lane witness V*')
    print('==> m010 lane witness I =', nV-nVd, '[expected +1]')
    ok=(nV-nVd)==1
    # our construction: the diagonal character of the lane's rep is (u, -1) in the flag basis; chi^2 = (u^2, 1)
    chi2={g:K.mul(chi[g],chi[g]) for g in gens}
    c,h1=nonsplit_cocycle(K,gens,rels,chi2); print('  H^1(pi; K_{chi^2}) dim =', h1, ' non-split cocycle found:', c is not None)
    if c is not None:
        # the lane's module is Sym^3(rho) (x) chi with chi = rho's own diagonal character (the twist is chi, not trivial)
        r=run_module(K,'m010',gens,rels,mu,lam,chi,c,3,chi,'own construction Sym3(rho_chi)(x)chi'); ok&= r['I']==1 and r['I_ss']==0
        r0=run_module(K,'m010',gens,rels,mu,lam,chi,c,3,psi,'own construction Sym3(rho_chi), untwisted')
    print('CONTROL', 'PASS' if ok else 'FAIL'); return ok
if __name__=='__main__':
    if control_m010(): print('BANKED IDENTITY reproduced')
    else: sys.exit(1)
