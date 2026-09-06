"""Twisted cohomology of the figure-eight complement M = m004 by Fox calculus (own code; exact over F_p).
Presentation <a,b | a w = w b>, w = b a^-1 b^-1 a (a,b meridians). Riley rep a=[[1,1],[0,1]], b=[[1,0],[u,1]], u^2-u+1=0.

Checks: (1) the Menal-Ferrer--Porti dimension law h^1(M; Sym^n rho_geom) [even n -> 1, odd n -> 0 for the tr(lambda) = -2 lift];
        (2) THE NET-CHIRALITY LEMMA  h^1(M;V) - h^1(M;V*) = rank(res_V) - h^0(dM;V)  on the self-dual Sym^n.
Non-self-dual representations are treated in nonselfdual_psl27_extension.py and nonselfdual_w1w2.py.
Exact arithmetic mod two primes p = 1 (mod 3)."""
import itertools, sys
import mpmath as mp
mp.mp.dps = 50

# ---------------- presentation & Fox derivatives ----------------
GENS = ['a','b']
W = ['b','A','B','a']                 # w = b a^-1 b^-1 a  (capital = inverse)
REL = ['a'] + W + ['B'] + [c.swapcase() for c in reversed(W)]   # a w b^-1 w^-1
def inv_word(wd): return [c.swapcase() for c in reversed(wd)]

def fox(word, x):
    """Fox derivative d(word)/dx as list of (sign, prefix-word). Left convention:
    d(uv)/dx = du/dx + u dv/dx;  dx/dx = 1;  d(x^-1)/dx = -x^-1."""
    terms=[]; prefix=[]
    for c in word:
        if c==x: terms.append((+1, list(prefix)))
        elif c==x.upper(): terms.append((-1, list(prefix)+[c]))
        prefix.append(c)
    return terms

# ---------------- generic linear algebra over a 'field' ----------------
class ModP:
    def __init__(s,p): s.p=p
    def mat_word(s, rho, word):
        n=len(rho['a']); M=[[int(i==j) for j in range(n)] for i in range(n)]
        for c in word: M = s.mul(M, rho[c])
        return M
    def mul(s,X,Y):
        p=s.p; n=len(X); m=len(Y[0]); k=len(Y)
        return [[sum(X[i][t]*Y[t][j] for t in range(k))%p for j in range(m)] for i in range(n)]
    def add(s,X,Y,c=1): return [[(X[i][j]+c*Y[i][j])%s.p for j in range(len(X[0]))] for i in range(len(X))]
    def zeros(s,n,m): return [[0]*m for _ in range(n)]
    def eye(s,n): return [[int(i==j) for j in range(n)] for i in range(n)]
    def rank(s,M):
        p=s.p; M=[row[:] for row in M]; r=0
        if not M: return 0
        rows,cols=len(M),len(M[0])
        for c in range(cols):
            piv=next((i for i in range(r,rows) if M[i][c]%p), None)
            if piv is None: continue
            M[r],M[piv]=M[piv],M[r]
            inv=pow(M[r][c],-1,p); M[r]=[(x*inv)%p for x in M[r]]
            for i in range(rows):
                if i!=r and M[i][c]%p:
                    f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(cols)]
            r+=1
            if r==rows: break
        return r
    def inv(s,M):
        p=s.p; n=len(M); A=[row[:]+[int(i==j) for j in range(n)] for i,row in enumerate(M)]
        for c in range(n):
            piv=next(i for i in range(c,n) if A[i][c]%p); A[c],A[piv]=A[piv],A[c]
            iv=pow(A[c][c],-1,p); A[c]=[(x*iv)%p for x in A[c]]
            for i in range(n):
                if i!=c and A[i][c]%p:
                    f=A[i][c]; A[i]=[(A[i][j]-f*A[c][j])%p for j in range(2*n)]
        return [row[n:] for row in A]
    def hstack(s,blocks): return [sum((b[i] for b in blocks),[]) for i in range(len(blocks[0]))]
    def vstack(s,blocks): return [row for b in blocks for row in b]
    def transpose(s,M): return [list(r) for r in zip(*M)]

class Cplx:
    def mat_word(s, rho, word):
        n=rho['a'].rows; M=mp.eye(n)
        for c in word: M = M*rho[c]
        return M
    def mul(s,X,Y): return X*Y
    def add(s,X,Y,c=1): return X+c*Y
    def zeros(s,n,m): return mp.zeros(n,m)
    def eye(s,n): return mp.eye(n)
    def rank(s,M, tol=mp.mpf('1e-25')):
        if M.rows==0 or M.cols==0: return 0
        sv = mp.svd_r(M, compute_uv=False) if False else mp.svd_c(M, compute_uv=False)
        return int(sum(1 for x in sv if abs(x)>tol))
    def inv(s,M): return M**-1
    def hstack(s,blocks):
        R=mp.zeros(blocks[0].rows, sum(b.cols for b in blocks)); c=0
        for b in blocks:
            for i in range(b.rows):
                for j in range(b.cols): R[i,c+j]=b[i,j]
            c+=b.cols
        return R
    def vstack(s,blocks):
        R=mp.zeros(sum(b.rows for b in blocks), blocks[0].cols); r=0
        for b in blocks:
            for i in range(b.rows):
                for j in range(b.cols): R[r+i,j]=b[i,j]
            r+=b.rows
        return R
    def transpose(s,M): return M.T

def full_rho(F, ra, rb):
    return {'a':ra,'b':rb,'A':F.inv(ra),'B':F.inv(rb)}

def rho_of_groupring(F, rho, terms, n):
    M=F.zeros(n,n)
    for sgn,wd in terms: M=F.add(M, F.mat_word(rho,wd), sgn)
    return M

def cochain_data(F, rho, gens, rel, n):
    """returns d0 (gn x n), d1 (n x gn) for presentation <gens | rel> and left module rho."""
    I=F.eye(n)
    d0 = F.vstack([F.add(rho[g], I, -1) for g in gens])
    d1 = F.hstack([rho_of_groupring(F, rho, fox(rel,g), n) for g in gens])
    return d0,d1

def h1(F, rho, gens, rel, n):
    d0,d1 = cochain_data(F,rho,gens,rel,n)
    # sanity: d1 d0 = 0
    z = F.mul(d1,d0)
    assert F.rank(z)==0, "d1*d0 != 0 -- convention error"
    return (len(gens)*n - F.rank(d1)) - F.rank(d0), F.rank(d0), F.rank(d1)

def cocycle_value(F, rho, f, word, n):
    """extend a 1-cocycle given on generators (dict letter->column) to a word: f(uv)=f(u)+rho(u)f(v), f(x^-1) = -rho(x^-1) f(x)."""
    val=F.zeros(n,1); pref=[]
    for c in word:
        if c.islower(): fc=f[c]
        else: fc = F.mul(rho[c], f[c.lower()]); fc=F.add(F.zeros(n,1), fc, -1)
        val=F.add(val, F.mul(F.mat_word(rho,pref), fc)) if pref else F.add(val,fc)
        pref.append(c)
    return val

def kernel_basis_modp(F, M):
    """basis of right kernel of M over F_p (list of column vectors)."""
    p=F.p; rows=len(M); cols=len(M[0]); A=[r[:] for r in M]; pivcols=[]; r=0
    for c in range(cols):
        piv=next((i for i in range(r,rows) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]; iv=pow(A[r][c],-1,p); A[r]=[(x*iv)%p for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][c]%p:
                f=A[i][c]; A[i]=[(A[i][j]-f*A[r][j])%p for j in range(cols)]
        pivcols.append(c); r+=1
        if r==rows: break
    free=[c for c in range(cols) if c not in pivcols]; basis=[]
    for fc in free:
        v=[0]*cols; v[fc]=1
        for i,pc in enumerate(pivcols): v[pc]=(-A[i][fc])%p
        basis.append([[x] for x in v])
    return basis

def kernel_basis_c(F, M, tol=mp.mpf('1e-25')):
    U,S,V = mp.svd_c(M)
    n=M.cols; basis=[]
    for i in range(n):
        if i>=len(S) or abs(S[i])<=tol:
            basis.append(V.H[:,i] if i < V.rows else None)
    return [b for b in basis if b is not None]

def net_chirality_report(F, ra, rb, n, mu_word, lam_word, label, kernel_basis):
    rho=full_rho(F,ra,rb)
    # dual rep: inverse transpose
    rad = F.transpose(F.inv(ra)); rbd = F.transpose(F.inv(rb)); rhod=full_rho(F,rad,rbd)
    out={}
    for tag,rr in [('V',rho),('V*',rhod)]:
        hV, r0, r1 = h1(F, rr, GENS, REL, n)
        # boundary torus <mu, lam | [mu,lam]>
        rmu=F.mat_word(rr,mu_word); rlam=F.mat_word(rr,lam_word)
        assert F.rank(F.add(F.mul(rmu,rlam),F.mul(rlam,rmu),-1))==0, "peripheral elements do not commute"
        rhoT={'a':rmu,'b':rlam,'A':F.inv(rmu),'B':F.inv(rlam)}
        relT=['a','b','A','B']
        hT, r0T, r1T = h1(F, rhoT, GENS, relT, n)
        h0T = n - r0T
        # restriction rank on cohomology: res(Z^1(M)) + B^1(dM) modulo B^1(dM)
        d0,d1 = cochain_data(F, rr, GENS, REL, n)
        Z = kernel_basis(F, d1)                    # cocycles on M as 2n-vectors (f_a; f_b)
        d0T,_ = cochain_data(F, rhoT, GENS, relT, n)
        cols=[]
        for z in Z:
            fa = [[z[i][0]] for i in range(n)] if F.__class__ is ModP else z[0:n,0]
            fb = [[z[n+i][0]] for i in range(n)] if F.__class__ is ModP else z[n:2*n,0]
            f={'a':fa,'b':fb}
            cols.append(F.vstack([cocycle_value(F,rr,f,mu_word,n), cocycle_value(F,rr,f,lam_word,n)]))
        resmat = F.hstack(cols+[d0T]) if cols else d0T
        rank_res = F.rank(resmat) - F.rank(d0T)
        out[tag]=dict(h1=hV, h1T=hT, h0T=h0T, rank_res=rank_res)
    N = out['V']['h1']-out['V*']['h1']
    lemma_ok = (N == out['V']['rank_res'] - out['V']['h0T'])
    print(f"  {label:38s} h1(V)={out['V']['h1']} h1(V*)={out['V*']['h1']}  N={N:+d} | h0(dM;V)={out['V']['h0T']} h0(dM;V*)={out['V*']['h0T']} h1(dM;V)={out['V']['h1T']} | rank res_V={out['V']['rank_res']} res_V*={out['V*']['rank_res']} | lemma N=rank res - h0: {'OK' if lemma_ok else 'VIOLATED'}")
    return out, N, lemma_ok

# ---------------- Sym^n of the Riley rep, exact mod p ----------------
def symn_modp(F, g, n):
    p=F.p; from math import comb
    a_,b_,c_,d_ = g[0][0],g[0][1],g[1][0],g[1][1]
    # substitution x -> a x + c y, y -> b x + d y ; basis x^{n-i} y^i
    M=F.zeros(n+1,n+1)
    for j in range(n+1):          # image of x^{n-j} y^j = (a x + c y)^{n-j} (b x + d y)^j
        poly=[0]*(n+1)            # coefficient of x^{n-i} y^i
        for s_ in range(n-j+1):
            for t_ in range(j+1):
                coef = comb(n-j,s_)*pow(a_,n-j-s_,p)*pow(c_,s_,p)*comb(j,t_)*pow(b_,j-t_,p)*pow(d_,t_,p)
                i = s_+t_
                poly[i]=(poly[i]+coef)%p
        for i in range(n+1): M[i][j]=poly[i]
    return M

def riley_modp(p):
    # u^2 - u + 1 = 0 mod p (p = 1 mod 3): u = 1 + omega
    u = next(x for x in range(p) if (x*x-x+1)%p==0)
    return [[1,1],[0,1]], [[1,0],[u,1]], u

def find_longitude_modp(F, ra, rb):
    rho=full_rho(F,ra,rb)
    for length in range(2,10):
        for word in itertools.product('aAbB', repeat=length):
            wd=list(word)
            if any(wd[i]==wd[i+1].swapcase() for i in range(len(wd)-1)): continue
            M=F.mat_word(rho,wd)
            if M[1][0]==0 and M[0][0]==M[1][1] and M[0][0] in (1,F.p-1) and M[0][1]!=0:
                # exclude powers of a: translation must not be an integer lift... mod p cannot tell; use word not a power of a
                if set(wd)-{'a','A'}: return wd, M
    return None

print("=== (1) MFP law: h^1(m004; Sym^n rho_geom), exact over F_p for two primes p = 1 mod 3 ===")
table={}
for p in [40123, 10009]:
    F=ModP(p); ra,rb,u = riley_modp(p)
    lam_word, lamM = find_longitude_modp(F, ra, rb)
    mu_word=['a']
    row=[]
    for n in range(0,17):
        Sa, Sb = symn_modp(F,ra,n), symn_modp(F,rb,n)
        hV,_,_ = h1(F, full_rho(F,Sa,Sb), GENS, REL, n+1)
        row.append(hV)
    table[p]=row
    print(f"  p={p}: u={u}, longitude word = {''.join(lam_word)} (tr = {(lamM[0][0]+lamM[1][1])%p} mod p -> {'-2' if (lamM[0][0]+lamM[1][1])%p==p-2 else '+2' if (lamM[0][0]+lamM[1][1])%p==2 else '?'})")
    print(f"        n = 0..16 : h^1 = {row}")
print("  agreement between primes:", table[40123]==table[10009])
print("  even n -> 1, odd n -> 0 :", all(table[40123][n]==(1 if n%2==0 else 0) for n in range(17)))
print("  27 = Sym16+Sym8+Sym0 (principal):  h^1 =", table[40123][16]+table[40123][8]+table[40123][0], " ; 27 = Sym12+Sym8+Sym4 (subregular): h^1 =", table[40123][12]+table[40123][8]+table[40123][4])

print("\n=== (2) the net-chirality lemma on Sym^n (self-dual: N must be 0) ===")
F=ModP(40123); ra,rb,u=riley_modp(40123); lam_word,_=find_longitude_modp(F,ra,rb)
for n in [0,1,2,3,4,8]:
    Sa,Sb = symn_modp(F,ra,n), symn_modp(F,rb,n)
    net_chirality_report(F, Sa, Sb, n+1, ['a'], lam_word, f"Sym^{n} (dim {n+1})", kernel_basis_modp)

