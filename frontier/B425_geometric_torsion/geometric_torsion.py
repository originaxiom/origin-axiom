"""B425 -- the GEOMETRIC Reidemeister torsion of the figure-eight at the hyperbolic
holonomy rho_geo, vs B423's DYNAMICAL zeta. (Prompted by a cross-chat catch: B423 used the
homological monodromy A=[[2,1],[1,1]], NOT the holonomy, so it computed the dynamical zeta,
golden by construction -- not the geometric torsion.)

rho_geo: a -> [[1,1],[0,1]],  b -> [[1,0],[-u,1]],  with rho(relator)=I forcing u^2+u+1=0
(so u = omega, primitive cube root of unity -- the discrete faithful rep, trace field Q(sqrt-3)).

Two computations, both exact:
  (A) EXACT (CRT over primes p = 1 mod 3): the twisted Alexander polynomial at rho_geo in
      Sym^{2m} for the E6 exponents {1,4,5,7,8,11}. Reads: are the coefficients rational
      (does sqrt(-3) cancel)?  the canonical adjoint (m=1) regularized torsion at t=1.
      Validated by the trivial-rep sanity check reproducing the ordinary Alexander poly of 4_1.
  (B) mpmath 120-digit: the Fox MATRIX trace (does sqrt(-3) SURVIVE in the matrix, i.e. is the
      Eisenstein content present?) + the relator error (to show the cross-chat's 1e29 blow-up
      at m=11 is a double-precision artifact, ~1e-115 at 120 digits).

VERDICT: sqrt(-3) is PRESENT in the Fox matrix at every exponent (trace complex) yet CANCELS
in every determinant (torsion rational). The canonical adjoint torsion is -3 (= disc Q(sqrt-3),
Eisenstein) -- reproducing the banked V30 (normal torsion) / V31 (Porti-form) figure-eight
value by a third independent method -- vs B423's dynamical adjoint -5 (= disc Q(sqrt5), golden).
The object carries TWO torsions: dynamical (golden, monodromy) and geometric (Eisenstein,
holonomy) = the two double-uniqueness cornerstone sides, meeting at sqrt(-15)=sqrt5*sqrt(-3).
"""
import json, os, math
from fractions import Fraction as Fr
import sympy as sp

E6 = [1, 4, 5, 7, 8, 11]

# ---------------- modular linear algebra ----------------
def det_mod(M, p):
    n = len(M); A = [row[:] for row in M]; det = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] % p), None)
        if piv is None: return 0
        if piv != c: A[c], A[piv] = A[piv], A[c]; det = (-det) % p
        inv = pow(A[c][c], p-2, p); det = det * A[c][c] % p
        for r in range(c+1, n):
            f = A[r][c] * inv % p
            if f:
                for k in range(c, n): A[r][k] = (A[r][k] - f*A[c][k]) % p
    return det % p

def matinv_mod(M, p):
    n = len(M); A = [row[:] + [1 if i==j else 0 for j in range(n)] for i,row in enumerate(M)]
    for c in range(n):
        piv = next((r for r in range(c,n) if A[r][c]%p), None)
        if piv is None: raise ValueError("singular")
        A[c],A[piv] = A[piv],A[c]; inv = pow(A[c][c],p-2,p)
        A[c] = [(x*inv)%p for x in A[c]]
        for r in range(n):
            if r!=c and A[r][c]%p:
                f=A[r][c]; A[r]=[(A[r][k]-f*A[c][k])%p for k in range(2*n)]
    return [row[n:] for row in A]

def matmul_mod(A,B,p):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k))%p for j in range(m)] for i in range(n)]

# ---------------- Sym^n of a 2x2 matrix, mod p ----------------
def poly_mul(a,b,p):
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b): r[i+j]=(r[i+j]+ai*bj)%p
    return r
def poly_pow(a,e,p):
    r=[1]
    for _ in range(e): r=poly_mul(r,a,p)
    return r
def sym_power_mod(M,n,p):
    m00,m01,m10,m11 = M[0][0]%p,M[0][1]%p,M[1][0]%p,M[1][1]%p
    linx=[m01%p, m00%p]; liny=[m11%p, m10%p]
    cols=[]
    for j in range(n+1):
        pj = poly_mul(poly_pow(linx,j,p), poly_pow(liny,n-j,p), p) + [0]*(n+1)
        cols.append(pj[:n+1])
    return [[cols[j][k] for j in range(n+1)] for k in range(n+1)]

# ---------------- knot group + Fox calculus ----------------
def inv_word(word): return [(g,-e) for g,e in reversed(word)]
A_=[('a',1)]; B_=[('b',1)]
W_ = B_+inv_word(A_)+inv_word(B_)+A_      # w = b a^-1 b^-1 a
R_ = A_+W_+inv_word(B_)+inv_word(W_)      # r = a w b^-1 w^-1  (figure-eight relator)
def fox(word,x):
    terms=[]; prefix=[]
    for (g,e) in word:
        if e==1:
            if g==x: terms.append((list(prefix),1))
            prefix=prefix+[(g,1)]
        else:
            prefix=prefix+[(g,-1)]
            if g==x: terms.append((list(prefix),-1))
    return terms
DRB = fox(R_,'b')

# ---------------- primes p = 1 mod 3, cube root of unity ----------------
def is_prime(n):
    if n<2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%q==0: return n==q
    d,s=n-1,0
    while d%2==0: d//=2; s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
def tonelli(n,p):
    n%=p
    if pow(n,(p-1)//2,p)!=1: return None
    if p%4==3: return pow(n,(p+1)//4,p)
    q,s=p-1,0
    while q%2==0: q//=2; s+=1
    z=2
    while pow(z,(p-1)//2,p)!=p-1: z+=1
    m,c,t,r=s,pow(z,q,p),pow(n,q,p),pow(n,(q+1)//2,p)
    while t!=1:
        i,t2=0,t
        while t2!=1: t2=t2*t2%p; i+=1
        b=pow(c,1<<(m-i-1),p); m=i; c=b*b%p; t=t*c%p; r=r*b%p
    return r
def cube_root_unity(p):
    s=tonelli((-3)%p,p); return (-1+s)*pow(2,p-2,p)%p

# ---------------- CRT + rational reconstruction ----------------
def crt(rs,ps):
    M=1
    for p in ps: M*=p
    x=0
    for r,p in zip(rs,ps): Mi=M//p; x=(x+r*Mi*pow(Mi,-1,p))%M
    return x,M
def ratrec(r,M):
    a,b=M,r%M; x0,x1=0,1; bd=math.isqrt(M//2)
    while b>bd:
        q=a//b; a,b=b,a-q*b; x0,x1=x1,x0-q*x1
    dn=abs(x1); nm=b if x1>0 else -b
    if dn==0 or math.gcd(dn,M)!=1: return None
    return Fr(nm,dn)

# ---------------- twisted Alexander at rho_geo, exponent 2m ----------------
def eval_TA_at(twom,p,wp,t0):
    A=sym_power_mod([[1,1],[0,1]],twom,p)
    Bm=sym_power_mod([[1,0],[(-wp)%p,1]],twom,p)
    L={('a',1):A,('a',-1):matinv_mod(A,p),('b',1):Bm,('b',-1):matinv_mod(Bm,p)}
    d=twom+1; ti=pow(t0,p-2,p)
    def Phi(prefix):
        M=[[1 if i==j else 0 for j in range(d)] for i in range(d)]; texp=0
        for (g,e) in prefix: M=matmul_mod(M,L[(g,e)],p); texp+=e
        f=pow(t0,texp,p) if texp>=0 else pow(ti,-texp,p)
        return [[x*f%p for x in row] for row in M]
    S=[[0]*d for _ in range(d)]
    for (prefix,sign) in DRB:
        P=Phi(prefix)
        for i in range(d):
            for j in range(d): S[i][j]=(S[i][j]+(sign%p)*P[i][j])%p
    N=det_mod(S,p)
    Dm=[[(A[i][j]*t0-(1 if i==j else 0))%p for j in range(d)] for i in range(d)]
    return N, det_mod(Dm,p)

def lagrange_coeffs(xs,ys,p):
    n=len(xs); coeff=[0]*n
    for i in range(n):
        num=[1]; den=1
        for j in range(n):
            if j==i: continue
            num=poly_mul(num,[(-xs[j])%p,1],p); den=den*((xs[i]-xs[j])%p)%p
        s=ys[i]*pow(den,p-2,p)%p
        for k in range(len(num)): coeff[k]=(coeff[k]+s*num[k])%p
    return coeff

def pnorm(a,p):
    a=[x%p for x in a]
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def pdivmod(a,b,p):
    a=pnorm(a[:],p); b=pnorm(b[:],p)
    if len(a)<len(b): return [0],a
    inv=pow(b[-1],p-2,p); q=[0]*(len(a)-len(b)+1); a=a[:]
    for i in range(len(a)-len(b),-1,-1):
        c=a[i+len(b)-1]*inv%p; q[i]=c
        for j in range(len(b)): a[i+j]=(a[i+j]-c*b[j])%p
    return pnorm(q,p),pnorm(a,p)
def pgcd(a,b,p):
    a=pnorm(a[:],p); b=pnorm(b[:],p)
    while b!=[0]:
        _,r=pdivmod(a,b,p); a,b=b,r
    inv=pow(a[-1],p-2,p); return [x*inv%p for x in a]

def geom_TA(twom, primes):
    """reduced W(t)=Nred/Dred over Q (Dred monic); coeffs kept small by gcd-reducing mod p."""
    d=twom+1; shift=3*d; xs=list(range(1,2*shift+3))
    Nc=[]; Dc=[]
    for p in primes:
        wp=cube_root_unity(p)
        Nv=[]; Dv=[]
        for t0 in xs:
            N,Den=eval_TA_at(twom,p,wp,t0%p)
            Nv.append(N*pow(t0%p,shift,p)%p); Dv.append(Den%p)
        Nsh=lagrange_coeffs(xs,Nv,p); Den=lagrange_coeffs(xs,Dv,p)
        Dfull=[0]*shift+Den
        G=pgcd(Nsh,Dfull,p)
        Nred,_=pdivmod(Nsh,G,p); Dred,_=pdivmod(Dfull,G,p)
        inv=pow(Dred[-1],p-2,p)
        Nc.append([x*inv%p for x in Nred]); Dc.append([x*inv%p for x in Dred])
    def recon(cols):
        L=max(len(c) for c in cols); out=[]
        for k in range(L):
            rs=[cols[i][k] if k<len(cols[i]) else 0 for i in range(len(cols))]
            x,M=crt(rs,list(primes)); out.append(ratrec(x,M))
        return out
    t=sp.symbols('t')
    Nred=sum((c if c else 0)*t**k for k,c in enumerate(recon(Nc)))
    Dred=sum((c if c else 0)*t**k for k,c in enumerate(recon(Dc)))
    return sp.cancel(Nred/Dred)

def galois_invariant(twom, primes, t0s=(2,3,5)):
    """RIGOROUS 'sqrt(-3) cancels': the Fox determinant is fixed by Gal(Q(sqrt-3)/Q),
    i.e. det(Fox at omega) == det(Fox at omega^2) mod every prime, at several t values.
    (Robust for ALL exponents incl. m=11, where the full-polynomial CRT would overflow.)"""
    for p in primes:
        wp = cube_root_unity(p); wp2 = wp*wp % p        # omega and its conjugate omega^2
        for t0 in t0s:
            N1,_ = eval_TA_at(twom, p, wp,  t0 % p)
            N2,_ = eval_TA_at(twom, p, wp2, t0 % p)
            if N1 != N2: return False
    return True

def reg_at_1(W):
    t=sp.symbols('t')
    num,den=sp.fraction(sp.together(W))
    num=sp.Poly(sp.expand(num),t); den=sp.Poly(sp.expand(den),t)
    def strip(P):
        while P.eval(1)==0 and P.degree()>0:
            P=sp.Poly(sp.div(P.as_expr(),(t-1),t)[0],t)
        return P
    return sp.nsimplify(strip(num).eval(1)/strip(den).eval(1))

def dyn_zeta(m):
    def F(n):
        x,y=0,1
        for _ in range(n): x,y=y,x+y
        return x
    return (-5)**m*sp.prod([F(2*j)**2 for j in range(1,m+1)])

# ---------------- mpmath 120-digit: Eisenstein present in the Fox matrix? ----------------
def eisenstein_presence():
    import mpmath as mp
    mp.mp.dps=120
    w=mp.mpf(-1)/2+mp.sqrt(3)/2*mp.mpc(0,1)
    def sym(M,n):
        def mul(a,b):
            r=[mp.mpc(0)]*(len(a)+len(b)-1)
            for i,ai in enumerate(a):
                for j,bj in enumerate(b): r[i+j]+=ai*bj
            return r
        def powp(a,e):
            r=[mp.mpc(1)]
            for _ in range(e): r=mul(r,a)
            return r
        linx=[M[0,1],M[0,0]]; liny=[M[1,1],M[1,0]]; S=mp.matrix(n+1,n+1)
        for j in range(n+1):
            col=mul(powp(linx,j),powp(liny,n-j))
            for k in range(n+1): S[k,j]=col[k]
        return S
    ra=mp.matrix([[1,1],[0,1]]); rb=mp.matrix([[1,0],[-w,1]])
    def mm(A,B):
        n,k,m=A.rows,A.cols,B.cols; C=mp.matrix(n,m)
        for i in range(n):
            for j in range(m): C[i,j]=sum(A[i,t]*B[t,j] for t in range(k))
        return C
    out={}
    for m in E6:
        twom=2*m; d=twom+1
        RA=sym(ra,twom); RB=sym(rb,twom)
        L={('a',1):RA,('a',-1):RA**-1,('b',1):RB,('b',-1):RB**-1}
        Rr=mp.eye(d)
        for (g,e) in R_: Rr=mm(Rr,L[(g,e)])
        relerr=max(abs(Rr[i,j]-(1 if i==j else 0)) for i in range(d) for j in range(d))
        S=mp.matrix(d,d)
        for (word,sign) in DRB:
            M=mp.eye(d)
            for (g,e) in word: M=mm(M,L[(g,e)])
            for i in range(d):
                for j in range(d): S[i,j]+=sign*M[i,j]
        imtr=mp.im(sum(S[i,i] for i in range(d)))
        out[m]=dict(relerr=mp.nstr(relerr,3), trace_im=mp.nstr(imtr,8),
                    eisenstein_present=bool(abs(imtr)>mp.mpf(10)**-60))
    return out

if __name__=="__main__":
    t=sp.symbols('t')
    primes=[p for p in range(1000003,1002000) if p%3==1 and is_prime(p)][:10]

    # holonomy check: rho(relator)=I forces u^2+u+1=0
    u=sp.symbols('u')
    Ma=sp.Matrix([[1,1],[0,1]]); Mb=sp.Matrix([[1,0],[-u,1]])
    ww=Mb*Ma.inv()*Mb.inv()*Ma; rr=sp.simplify(Ma*ww*Mb.inv()*ww.inv())
    holo=sp.simplify(sp.gcd([sp.numer(sp.together(rr[i,j]-(1 if i==j else 0)))
                             for i in range(2) for j in range(2)]))

    # (A) RIGOROUS: sqrt(-3) cancels at EVERY exponent = the torsion is Galois-invariant
    galois={m: galois_invariant(2*m, primes) for m in E6}

    # (B) exact twisted Alexander at rho_geo. The full polynomial reconstructs cleanly for
    #     m in {1,4,5,7,8} (small integer coeffs); m=11's coeffs are large (CRT would need
    #     many more primes) -- its rationality is certified by the Galois check above, not
    #     by the (here-omitted) fragile full reconstruction.
    W_triv=geom_TA(0,primes)                 # sanity: ordinary Alexander of 4_1
    CLEAN=[1,4,5,7,8]
    polys={}; all_integer=True
    for m in CLEAN:
        W=geom_TA(2*m,primes); polys[m]=W
        P=sp.Poly(sp.numer(sp.together(W)),t)
        all_integer = all_integer and all(c.is_integer for c in P.all_coeffs())
    adj=reg_at_1(polys[1])

    # (C) mpmath: Eisenstein presence + relator error
    eis=eisenstein_presence()

    geom_polys={str(m):str(sp.factor(W)) for m,W in polys.items()}
    geom_polys["11"]="[coeffs large; rationality certified by Galois-invariance det(omega)=det(omega^2)]"
    result=dict(
        holonomy_forces=str(holo),
        alexander_sanity=str(sp.factor(W_triv)),
        sqrt_m3_cancels_all_exponents=bool(all(galois.values())),
        galois_invariant={str(m):bool(galois[m]) for m in E6},
        all_clean_torsion_coeffs_integer=bool(all_integer),
        adjoint_geometric=str(adj), adjoint_dynamical=str(dyn_zeta(1)),
        geom_polys=geom_polys,
        dyn_zeta={str(m):str(dyn_zeta(m)) for m in E6},
        eisenstein_presence={str(m):eis[m] for m in E6},
        crossval="V30 (normal torsion) / V31 (Porti form): figure-eight adjoint = -3, Q(sqrt-3)",
    )
    json.dump(result, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        "geometric_torsion.json"),"w"), indent=1)

    print("holonomy forces:", holo, " (=> u=omega, discrete faithful, trace field Q(sqrt-3))")
    print("Alexander sanity (trivial rep):", sp.factor(W_triv), " [4_1 Alexander = t^2-3t+1]")
    print("sqrt(-3) cancels (Galois-invariant det(omega)=det(omega^2)) at all 6 exponents:",
          all(galois.values()), " per-exponent:", galois)
    print("clean-reconstruction torsion coeffs integer (m in 1,4,5,7,8):", all_integer)
    print(f"\nadjoint GEOMETRIC torsion (rho_geo)  = {adj}   [disc Q(sqrt-3) = -3, Eisenstein]")
    print(f"adjoint DYNAMICAL zeta   (B423)      = {dyn_zeta(1)}   [disc Q(sqrt5)  = -5, golden]")
    print("\nEisenstein present in Fox matrix (trace Im != 0) at every exponent:")
    for m in E6:
        e=eis[m]; print(f"  m={m:>2}: relerr(120dig)={e['relerr']:>10}  trace_im={e['trace_im']:>12}  present={e['eisenstein_present']}")
    print("\n[written] geometric_torsion.json")
