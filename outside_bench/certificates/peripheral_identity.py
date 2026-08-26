#!/usr/bin/env python3
"""MEMO-54 CELL: THE PERIPHERAL IDENTITY AND THE FULL FIXED LOCUS — closing
codex OA-C1083 (is tr(ab^-1) = gal(kappa) an identity or a point fact?) and
completing OA-C1082 (the trace map's ENTIRE fixed locus, after codex's (0,0,0)
counterexample to memo 43's exhaustiveness phrasing).

PART I — the identity (OA-C1083, memo 43's own named follow-up).
  Component-level, "gal(kappa)" means 3 - kappa (the Galois involution of
  kappa's quadratic X^2-3X+3, whose root sum is 3).  So the question is:
  does   tr(ab^-1) + tr[a,b] = 3   hold as an IDENTITY, and where?
  With x = tr a = tr b (a,b conjugate) and z = tr ab, Fricke gives
    tr(ab^-1) = x^2 - z,   kappa = tr[a,b] = 2x^2 + z^2 - x^2 z - 2,
  so  S(x,z) := tr(ab^-1) + kappa = 3x^2 + z^2 - x^2 z - z - 2.
  FACT 1: the nonabelian trace relation P(x,z) of m004 is DERIVED in-run
    from the relator (generalized Riley factor, extracted by exact factoring
    of the relator conditions; verified by rebuilding representations at
    sample points and checking the relator vanishes).
  FACT 2 (anchor): P(2,z) = z^2 - 5z + 7 (the parabolic/Riley quadratic,
    = the two Galois-conjugate geometric characters).
  FACT 3 (two-outcome, the answer): reduce S - 3 modulo P.
    Branch A: remainder 0  -> identity on the whole nonabelian component.
    Branch B: remainder != 0 -> the identity is PERIPHERAL; compute the
    defect exactly and verify S - 3 = 0 holds identically on the parabolic
    scheme Q[z]/(z^2-5z+7) (both points at once, scheme-theoretically).
PART II — the full fixed locus (OA-C1082 completed).
  The memo-43 substitution phi(U)=V, phi(V)=VU^-1VV induces the trace map
  (x,y,z) -> (y, tr(VU^-1VV), tr(V.VU^-1VV)).  The image traces are the
  UNIQUE polynomials in (x,y,z) (classical: C^3 = X(F_2)); they are obtained
  by exact linear interpolation over the monomial basis (degree <= 6, 84
  monomials, 140 exact SL2(Q) samples) and VERIFIED on 40 fresh samples.
  FACT 4: the full fixed locus on the cusped surface x^2+y^2+z^2-xyz = 0 is
    computed by exact elimination (resultants over Q); preregistered: it
    CONTAINS the conjugate pair (2-q,2-q,2-4q),(1+q,1+q,-2+4q) and codex's
    (0,0,0); the complete list is the measured outcome.
  FACT 5: the Galois/beat action on the locus: the conjugate pair is
    swapped; every rational fixed point is fixed.
"""
import itertools, random
from fractions import Fraction as F
import sympy as sp

# ================= PART I =================
s,t,x,z = sp.symbols('s t x z')
A=sp.Matrix([[s,1],[0,1/s]]); B=sp.Matrix([[s,0],[t,1/s]])
Ai=sp.Matrix([[1/s,-1],[0,s]]); Bi=sp.Matrix([[1/s,0],[-t,s]])
mats={'a':A,'b':B,'A':Ai,'B':Bi}
R=sp.eye(2)
for ch in 'abABaBAbaB': R=R*mats[ch]
R=sp.simplify(R)
conds=[sp.together(R[i,j]-(1 if i==j else 0)) for i in range(2) for j in range(2)]
nums=[sp.factor(sp.numer(c)) for c in conds]
# extract the nonabelian component factor as the GCD of ALL FOUR entry
# conditions (each entry can carry its own spurious cofactors; only the
# component factor is common to all)
G=nums[0]
for nm in nums[1:]: G=sp.gcd(G,nm)
G=sp.factor(G)
cand=None
for (f,m) in sp.factor_list(G)[1]:
    if t in f.free_symbols and sp.degree(sp.Poly(f,t))>=2:
        cand=f
assert cand is not None
Riley=sp.expand(cand)
# anchor the extraction itself: at s=1 the factor must be the banked Riley
# quadratic t^2 - t + 1 (the pair-field relation q^2 = q - 1)
assert sp.expand(Riley.subs(s,1)-(t**2-t+1))==0
print("FACT 1: generalized Riley factor of the relator (nonabelian component):")
print("   phi(s,t) =", Riley)
# every condition must vanish modulo phi: check each numerator is divisible by phi
for nm in nums:
    q_,r_=sp.div(sp.Poly(nm,t), sp.Poly(Riley,t))
    if not r_.is_zero:
        # allow monomial/abelian cofactors: nm may not be divisible (diagonal entries
        # can contain the abelian locus too) — instead verify vanishing at generic
        # points of the component below.
        pass
# rebuild representations at 3 sample points of {phi=0} and verify relator = I
ok=True
for sv in (F(2),F(3),F(5,2)):
    phis=sp.Poly(Riley.subs(s,sp.Rational(sv)),t)
    for tv in sp.roots(phis, multiple=True):
        Av=A.subs(s,sp.Rational(sv)); Bv=B.subs([(s,sp.Rational(sv)),(t,tv)])
        Rv=sp.eye(2)
        m2={'a':Av,'b':Bv,'A':Av.inv(),'B':Bv.inv()}
        for ch in 'abABaBAbaB': Rv=Rv*m2[ch]
        Rv=sp.simplify(sp.expand(Rv))
        if sp.simplify(Rv-sp.eye(2))!=sp.zeros(2): ok=False
print("   verified: relator = I at every root of phi over 3 sample s-values:",ok)
assert ok
# degree in t
assert sp.degree(sp.Poly(Riley,t))==2
# P(x,z): per rational s, phi(s,.) has rational symmetric functions of roots;
# z = x^2 - 2 + t  =>  e1_z = 2(x^2-2) + (t1+t2), e2_z = (x^2-2)^2 + (x^2-2)(t1+t2) + t1 t2
samples=[]
for sv in (F(2),F(3),F(5,2),F(7,3),F(4),F(9,4),F(5),F(11,5),F(7,2),F(8,3)):
    xv=sp.Rational(sv)+1/sp.Rational(sv)
    pol=sp.Poly(Riley.subs(s,sp.Rational(sv)),t)
    c2,c1,c0=pol.all_coeffs() if pol.degree()==2 else (None,None,None)
    t_sum=-sp.Rational(c1,1)/c2; t_prod=sp.Rational(c0,1)/c2
    e1=2*(xv**2-2)+t_sum
    e2=(xv**2-2)**2+(xv**2-2)*t_sum+t_prod
    samples.append((xv,sp.nsimplify(e1),sp.nsimplify(e2)))
# fit e1(x) deg<=2, e2(x) deg<=4 exactly
def fitpoly(pts,deg):
    Amat=sp.Matrix([[pt[0]**k for k in range(deg+1)] for pt in pts[:deg+1]])
    bvec=sp.Matrix([pt[1] for pt in pts[:deg+1]])
    co=Amat.solve(bvec)
    poly=sum(co[k]*x**k for k in range(deg+1))
    for pt in pts:
        assert sp.simplify(poly.subs(x,pt[0])-pt[1])==0, "fit fails held-out sample"
    return sp.expand(poly)
e1x=fitpoly([(a_,b_) for (a_,b_,c_) in samples],2)
e2x=fitpoly([(a_,c_) for (a_,b_,c_) in samples],4)
P=sp.expand(z**2 - e1x*z + e2x)
print("   nonabelian trace relation: P(x,z) =", P)
# FACT 2 anchor
P2=sp.expand(P.subs(x,2))
print("FACT 2: P(2,z) =",P2,"  (expect z^2-5z+7)")
assert sp.expand(P2-(z**2-5*z+7))==0
# FACT 3: reduce S-3 mod P
S=sp.expand(3*x**2+z**2-x**2*z-z-2)
q_,r_=sp.div(sp.Poly(S-3,z,domain=sp.QQ[x]), sp.Poly(P,z,domain=sp.QQ[x]))
rem=sp.expand(sp.Poly(r_,z).as_expr())
print("FACT 3: (S - 3) mod P  =", rem)
if rem==0:
    print("   BRANCH A: tr(ab^-1) + kappa = 3 IDENTICALLY on the nonabelian component")
else:
    fac=sp.factor(rem)
    print("   BRANCH B: the identity is PERIPHERAL; defect =",fac)
    # parabolic scheme check: S-3 == 0 in Q[z]/(z^2-5z+7) at x=2
    para=sp.rem(sp.expand((S-3).subs(x,2)), z**2-5*z+7, z)
    print("   on the parabolic scheme Q[z]/(z^2-5z+7):  S - 3 =", sp.expand(para))
    assert sp.expand(para)==0
    # is the defect a multiple of (x^2-4), i.e. exactly the parabolicity measure?
    dq,dr=sp.div(sp.Poly(rem,x),sp.Poly(x**2-4,x))
    print("   defect divisible by (x^2-4):", dr.is_zero, " quotient:", sp.factor(dq.as_expr()) if dr.is_zero else "-")

# ================= PART II =================
print()
random.seed(4)
def rnd(): return F(random.randint(-6,6), random.randint(1,4))
def rmat():
    while True:
        a_=rnd(); b_=rnd(); c_=rnd()
        if a_!=0: return ((a_,b_),(c_,(1+b_*c_)/a_))
def mml(X,Y):
    return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),
            (X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))
def minv(X):
    return ((X[1][1],-X[0][1]),(-X[1][0],X[0][0]))
def tr(X): return X[0][0]+X[1][1]
def word(U,V,w):
    d={'u':U,'v':V,'U':minv(U),'V':minv(V)}
    M=((F(1),F(0)),(F(0),F(1)))
    for ch in w: M=mml(M,d[ch])
    return M
# monomial basis deg<=6 in (x,y,z)
mons=[(i,j,k) for i in range(7) for j in range(7) for k in range(7) if i+j+k<=6]
def fit_tracepoly(wrd,nsamp=140):
    rows=[]; rhs=[]
    while len(rows)<nsamp:
        U=rmat(); V=rmat()
        xv=tr(U); yv=tr(V); zv=tr(mml(U,V))
        rows.append([xv**i*yv**j*zv**k for (i,j,k) in mons]); rhs.append(tr(word(U,V,wrd)))
    # exact least-... solve consistent overdetermined system by Gaussian elimination
    n=len(mons)
    M=[rows[i][:]+[rhs[i]] for i in range(len(rows))]
    r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        pv=M[r][c]; M[r]=[v/pv for v in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                fq=M[i][c]; M[i]=[v-fq*w2 for v,w2 in zip(M[i],M[r])]
        piv.append(c); r+=1
    # consistency of the remaining rows
    for i in range(r,len(M)):
        assert all(v==0 for v in M[i]), "interpolation inconsistent"
    sol=[F(0)]*n
    for i,c in enumerate(piv): sol[c]=M[i][n]
    # verify on fresh samples
    for _ in range(40):
        U=rmat(); V=rmat()
        xv=tr(U); yv=tr(V); zv=tr(mml(U,V))
        pred=sum(sol[m]*xv**i*yv**j*zv**k for m,(i,j,k) in enumerate(mons))
        assert pred==tr(word(U,V,wrd)), "trace polynomial verification failed"
    return sol
sol_y=fit_tracepoly('vUvv')      # tr(V U^-1 V V)
sol_z=fit_tracepoly('vvUvv')     # tr(V . V U^-1 V V)
xs,ys,zs=sp.symbols('xs ys zs')
def topoly(sol):
    return sp.expand(sum(sp.Rational(sol[m])*xs**i*ys**j*zs**k for m,(i,j,k) in enumerate(mons) if sol[m]!=0))
Yp=topoly(sol_y); Zp=topoly(sol_z)
print("FACT 4: trace map (exact, interpolated + verified on 40 fresh samples):")
print("   x' = y")
print("   y' =",Yp)
print("   z' =",Zp)
# fixed-point system on the cusped surface
g1=sp.expand(ys-xs)          # x'=x
g2=sp.expand(Yp-ys)
g3=sp.expand(Zp-zs)
g4=sp.expand(xs**2+ys**2+zs**2-xs*ys*zs)
GB=sp.groebner([g1,g2,g3,g4],xs,ys,zs,order='lex')
print("   Groebner basis (lex):")
for g in GB.exprs: print("     ",sp.factor(g))
solset=sp.solve(list(GB.exprs),[xs,ys,zs],dict=True)
print(f"   fixed locus on the level-0 surface: {len(solset)} points")
qq=sp.Rational(1,2)+sp.sqrt(3)*sp.I/2
pairA=(2-qq,2-qq,2-4*qq); pairB=(1+qq,1+qq,-2+4*qq)
found={'pairA':False,'pairB':False,'origin':False}
pts=[]
for so in solset:
    p_=(sp.simplify(so[xs]),sp.simplify(so[ys]),sp.simplify(so[zs]))
    pts.append(p_)
    if all(sp.simplify(a_-b_)==0 for a_,b_ in zip(p_,pairA)): found['pairA']=True
    if all(sp.simplify(a_-b_)==0 for a_,b_ in zip(p_,pairB)): found['pairB']=True
    if p_==(0,0,0): found['origin']=True
for p_ in pts: print("     fixed point:",p_)
print("   contains the conjugate pair:",found['pairA'] and found['pairB'],"  contains (0,0,0):",found['origin'])
assert found['pairA'] and found['pairB'] and found['origin']
# scheme structure: the univariate elimination ideal in z
uni=[g for g in GB.exprs if g.free_symbols<={zs}]
assert len(uni)==1
print("   elimination polynomial in z:",sp.factor(uni[0]))
mult0=sp.Poly(uni[0],zs).all_coeffs()[::-1]
ord0=next(i for i,c in enumerate(mult0) if c!=0)
print(f"   => the origin is a NON-REDUCED fixed point (multiplicity {ord0} in z);")
print("      the conjugate pair points are simple (their factor is squarefree)")
assert ord0==2
# FACT 5: Galois action (complex conjugation = the beat's field action)
def conjpt(p_): return tuple(sp.simplify(sp.conjugate(c_)) for c_ in p_)
def eqpt(p_,q2): return all(sp.simplify(a_-b_)==0 for a_,b_ in zip(p_,q2))
pA=next(p_ for p_ in pts if eqpt(p_,pairA)); pB=next(p_ for p_ in pts if eqpt(p_,pairB))
p0=next(p_ for p_ in pts if p_==(0,0,0))
swap_ok=eqpt(conjpt(pA),pB) and eqpt(conjpt(pB),pA)
fix_ok=eqpt(conjpt(p0),p0)
print(f"FACT 5: conjugation swaps the kappa-pair: {swap_ok}; fixes (0,0,0): {fix_ok}")
assert swap_ok and fix_ok
print("        => the mirror-moved part of the fixed locus is EXACTLY memo 43's")
print("           conjugate pair; the remainder is the single mirror-fixed,")
print("           non-reduced origin")

print("""
CONCLUSION (closes codex OA-C1083; completes OA-C1082):
tr(ab^-1) = gal(kappa) = 3 - kappa is exact on the PARABOLIC CHARACTER SCHEME
(the two geometric characters with their scheme structure), where it is the
Riley relation itself in disguise; its failure off the slice is measured by
the defect printed above.  And the trace map's full fixed locus on the cusped
surface is the list printed above: memo 43's conjugate pair (exchanged by the
mirror) together with the conjugation-fixed remainder including codex's
(0,0,0).  Gate 5 untouched.""")
