import sys, os, pathlib, itertools, numpy as np, sympy as sp
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093
src = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "cell3_su5.py")).read_text().split("CBAR, res = restricted_cubic(VBAR)")[0]
src = src.replace("P = 1093", f"P = {PRIME}").replace(
 'Pop = E.ev((0, 0, 0, 0, 0, 0, 0, 1))\nQop = E.ev((-2, -3, -4, -6, -5, -4, -3, -1))',
 'POP27=E.ev((0,0,0,0,0,0,0,1)); QOP27=E.ev((-2,-3,-4,-6,-5,-4,-3,-1))\nPOPBAR=E.ev((2,3,4,6,5,4,3,1)); QOPBAR=E.ev((0,0,0,0,0,0,0,-1))\nPop,Qop=POP27,QOP27')
exec(compile(src, "c3", "exec"))
import e8_build as E
x_, y_ = sp.symbols('x y')
r3 = next(t for t in range(P) if (t*t + 3) % P == 0)
Phi = x_**4 + 2*r3*x_**2*y_**2 + y_**4
Psi = x_**4 - 2*r3*x_**2*y_**2 + y_**4
Wp  = x_**8 + 14*x_**4*y_**4 + y_**8
assert sp.Poly(sp.expand(Phi*Psi - Wp), x_, y_, modulus=P).is_zero, "Phi*Psi != W"
print(f"p = {P}   sqrt(-3) = {r3}   GATE Phi*Psi = W: PASS")

def hwv(block, n):
    cands=[r for r in block if int(list(E.br(h,E.ev(r)).values())[0] if E.br(h,E.ev(r)) else 0)==n]
    M=sp.zeros(E.DIM,len(cands))
    for j,r in enumerate(cands):
        for k,val in E.br(ee,E.ev(r)).items(): M[k,j]=sp.Rational(val.numerator,val.denominator)
    ns=M.nullspace(); v={}
    for j,r in enumerate(cands):
        co=sp.Rational(ns[0][j])
        if co: v=E.vadd(v,{E.N+E.IDX[r]:Fr(co)})
    return v

def embed_form(form, n, block):
    Pp=sp.Poly(sp.expand(form),x_,y_); out,cur={},hwv(block,n)
    for k in range(n+1):
        co=Pp.coeff_monomial(x_**(n-k)*y_**k)
        if co:
            out=E.vadd(out,E.vmul(Fr(sp.Rational(int(co)%P)*sp.factorial(n-k)/sp.factorial(n)),cur))
        cur=E.br(ff,cur)
    return out

def restricted(Vd,Pp_,Qq):
    pts,vals=[],[]
    for A_,B_,C_ in itertools.product(range(-2,3),repeat=3):
        if (A_,B_,C_)==(0,0,0): continue
        v={}
        for co,n in ((A_,0),(B_,8),(C_,16)):
            if co: v=E.vadd(v,E.vmul(co,Vd[n]))
        pts.append((A_,B_,C_)); vals.append(E.killing_pair(E.br(v,E.br(Pp_,v)),E.br(Qq,v)))
        if len(pts)>=40: break
    M=sp.Matrix([[sp.Rational(int(sp.Poly(m,a,b,c).eval({a:p[0],b:p[1],c:p[2]}))) for m in mons] for p in pts])
    return sp.expand(sum(M.solve_least_squares(sp.Matrix([sp.Rational(v.numerator,v.denominator) for v in vals]))[i]*mons[i] for i in range(len(mons))))

def idem(Vd,Pp_,Qq,ti,p=P):
    C=restricted(Vd,Pp_,Qq); D=sp.expand(C/sp.Poly(C,a,b,c).coeff_monomial(a**3))
    s2,s3_=sp.expand(D.coeff(a,1)),sp.expand(D.coeff(a,0))
    def red(e_,var):
        pl=sp.Poly(sp.expand(e_),var); o=0
        for (k,),co in pl.terms():
            r=sp.Rational(co); o+=(r.p%p)*pow(r.q%p,p-2,p)%p*var**k
        return sp.Poly(o,var,modulus=p)
    out=[]
    for bv in range(p):
        q2=red(s2.subs(b,bv)+sp.Rational(1,3),c); q3=red(s3_.subs(b,bv)-sp.Rational(2,27),c)
        g=sp.gcd(q2,q3)
        if g.degree()<1: continue
        for cv in sp.ground_roots(g.as_expr(),modulus=p):
            v={}; i3=pow(3,p-2,p)
            for co,n in ((i3,0),(bv,8),(int(cv)%p,16)): v=E.vadd(v,E.vmul(Fraction(co%p),Vd[n]))
            if 78-rank_mod_p(act(v,ti))==61: out.append(v)
    return out

g27=idem(V27,POP27,QOP27,IDX27); gb=idem(VBAR,POPBAR,QOPBAR,IDXBAR)
so10=None
for i,v in enumerate(g27):
    for j,w in enumerate(gb):
        M=np.vstack([act(v,IDX27),act(w,IDXBAR)])%P
        if reductive_dim(M)==(45,45): so10=(M,i,j); break
    if so10: break
M,i0,j0=so10
ns=nullspace(M); ops=[]; elts=[]
for vv in ns:
    xx={}
    for co,Xb in zip(vv,E6_BASIS):
        if co%P: xx=E.vadd(xx,E.vmul(Fraction(int(co)%P),Xb))
    elts.append(xx)
    A_=np.zeros((27,27),dtype=np.int64)
    for ci,r in enumerate(TWENTYSEVEN):
        for k,val in E.br(xx,E.ev(r)).items():
            A_[IDX27[E.ROOTS[k-E.N]],ci]=(val.numerator%P)*pow(val.denominator%P,P-2,P)%P
    ops.append(A_%P)
G=np.array([[int(np.trace(ops[u].astype(object)@ops[w2].astype(object))%P) for w2 in range(45)] for u in range(45)],dtype=np.int64)
Gs=sp.Matrix(45,45,lambda r,c:int(G[r,c])).inv_mod(P)
Om=np.zeros((27,27),dtype=object)
for u in range(45):
    for w2 in range(45):
        g=int(Gs[u,w2])%P
        if g: Om=(Om+g*(ops[u].astype(object)@ops[w2].astype(object)))%P
Om=Om%P; Mo=sp.Matrix(27,27,lambda r,c:int(Om[r,c])); eig={}
for f,m in sp.factor_list(sp.Poly(Mo.charpoly(sp.Symbol('L')).as_expr(),sp.Symbol('L'),modulus=P).as_expr(),modulus=P)[1]:
    if sp.Poly(f,sp.Symbol('L')).degree()==1:
        r0=int(sp.ground_roots(f,modulus=P).popitem()[0])%P
        Kn=np.array([[int((Mo-r0*sp.eye(27))[rr,cc])%P for cc in range(27)] for rr in range(27)],dtype=np.int64)
        eig[r0]=27-rank_mod_p(Kn)
print(f"GATE Casimir multiplicities: {sorted(eig.values())}  (want [1,10,16])")
lam16=[l for l,mu in eig.items() if mu==16][0]
Pm16=np.eye(27,dtype=object)
for mu in eig:
    if mu!=lam16: Pm16=(Pm16@((Om-mu*np.eye(27,dtype=object))*pow((lam16-mu)%P,P-2,P)))%P

def vec(v):
    w=np.zeros(27,dtype=object)
    for k,val in v.items(): w[IDX27[E.ROOTS[k-E.N]]]=(val.numerator%P)*pow(val.denominator%P,P-2,P)%P
    return w

def stab_in_so10(s16):
    rows=[[int(t)%P for t in (A_.astype(object)@s16)%P] for A_ in ops]
    R=np.array(rows,dtype=np.int64).T%P
    d=45-rank_mod_p(R)
    ns2=nullspace(R); els=[]
    for vv in ns2:
        xx={}
        for co,Xb in zip(vv,elts):
            if co%P: xx=E.vadd(xx,E.vmul(Fraction(int(co)%P),Xb))
        els.append(xx)
    K=np.zeros((len(els),len(els)),dtype=np.int64)
    for r1,z1 in enumerate(els):
        for r2,z2 in enumerate(els):
            kv=E.killing_pair(z1,z2); K[r1,r2]=(kv.numerator%P)*pow(kv.denominator%P,P-2,P)%P
    return d, rank_mod_p(K)

print("\nSTABILISER IN so(10) OF THE 16-COMPONENT OF EACH omega-COVARIANT")
print("  pure spinor  =>  dim 34, reductive 24 = su(5)")
CAND={"Psi^2  (deg 8, omega)":(sp.expand(Psi**2),8),
      "Phi^2  (deg 8, omega^2)":(sp.expand(Phi**2),8),
      "Phi^4  (deg 16, omega)":(sp.expand(Phi**4),16),
      "Psi^4  (deg 16, omega^2)":(sp.expand(Psi**4),16),
      "W*Psi^2(deg 16, omega)":(sp.expand(Wp*Psi**2),16),
      "W*Phi^2(deg 16, omega^2)":(sp.expand(Wp*Phi**2),16)}
for nm,(form,n) in CAND.items():
    s16=(Pm16@vec(embed_form(form,n,TWENTYSEVEN)))%P
    if not np.count_nonzero(s16):
        print(f"  {nm:26s} 16-part ZERO"); continue
    d,kr = stab_in_so10(s16)
    tag = "   <<<<<< su(5) >>>>>>" if kr==24 else ""
    print(f"  {nm:26s} dim {d:2d}, reductive {kr:2d}{tag}")
