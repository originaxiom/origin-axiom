import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath("cell3_su5.py")))
import pathlib, itertools, numpy as np, sympy as sp, sys
from fractions import Fraction
PR_ = int(sys.argv[1])
src = pathlib.Path("cell3_su5.py").read_text().split("CBAR, res = restricted_cubic(VBAR)")[0]
src = src.replace("P = 1093", f"P = {PR_}").replace(
 'Pop = E.ev((0, 0, 0, 0, 0, 0, 0, 1))\nQop = E.ev((-2, -3, -4, -6, -5, -4, -3, -1))',
 'POP27=E.ev((0,0,0,0,0,0,0,1)); QOP27=E.ev((-2,-3,-4,-6,-5,-4,-3,-1))\nPOPBAR=E.ev((2,3,4,6,5,4,3,1)); QOPBAR=E.ev((0,0,0,0,0,0,0,-1))\nPop,Qop=POP27,QOP27')
exec(compile(src,"c3","exec"))
import e8_build as E
def restricted(Vd,Pp,Qq):
    pts,vals=[],[]
    for A_,B_,C_ in itertools.product(range(-2,3),repeat=3):
        if (A_,B_,C_)==(0,0,0): continue
        v={}
        for co,n in ((A_,0),(B_,8),(C_,16)):
            if co: v=E.vadd(v,E.vmul(co,Vd[n]))
        pts.append((A_,B_,C_)); vals.append(E.killing_pair(E.br(v,E.br(Pp,v)),E.br(Qq,v)))
        if len(pts)>=40: break
    M=sp.Matrix([[sp.Rational(int(sp.Poly(m,a,b,c).eval({a:p[0],b:p[1],c:p[2]}))) for m in mons] for p in pts])
    return sp.expand(sum(M.solve_least_squares(sp.Matrix([sp.Rational(v.numerator,v.denominator) for v in vals]))[i]*mons[i] for i in range(len(mons))))
def idem(Vd,Pp,Qq,ti,p=P):
    C=restricted(Vd,Pp,Qq); D=sp.expand(C/sp.Poly(C,a,b,c).coeff_monomial(a**3))
    s2,s3=sp.expand(D.coeff(a,1)),sp.expand(D.coeff(a,0))
    def red(e_,var):
        pl=sp.Poly(sp.expand(e_),var); o=0
        for (k,),co in pl.terms():
            r=sp.Rational(co); o+=(r.p%p)*pow(r.q%p,p-2,p)%p*var**k
        return sp.Poly(o,var,modulus=p)
    out=[]
    for bv in range(p):
        q2=red(s2.subs(b,bv)+sp.Rational(1,3),c); q3=red(s3.subs(b,bv)-sp.Rational(2,27),c)
        g=sp.gcd(q2,q3)
        if g.degree()<1: continue
        for cv in sp.ground_roots(g.as_expr(),modulus=p):
            v={}; i3=pow(3,p-2,p)
            for co,n in ((i3,0),(bv,8),(int(cv)%p,16)): v=E.vadd(v,E.vmul(Fraction(co%p),Vd[n]))
            if 78-rank_mod_p(act(v,ti))==61: out.append(v)
    return out
g27=idem(V27,POP27,QOP27,IDX27); gb=idem(VBAR,POPBAR,QOPBAR,IDXBAR)
print(f"p = {P}")
for i,v in enumerate(g27):
    for j,w in enumerate(gb):
        M=np.vstack([act(v,IDX27),act(w,IDXBAR)])%P
        if reductive_dim(M)!=(45,45): continue
        ns=nullspace(M); ops=[]
        for vv in ns:
            xx={}
            for co,Xb in zip(vv,E6_BASIS):
                if co%P: xx=E.vadd(xx,E.vmul(Fraction(int(co)%P),Xb))
            A_=np.zeros((27,27),dtype=np.int64)
            for ci,r in enumerate(TWENTYSEVEN):
                for k,val in E.br(xx,E.ev(r)).items():
                    A_[IDX27[E.ROOTS[k-E.N]],ci]=(val.numerator%P)*pow(val.denominator%P,P-2,P)%P
            ops.append(A_%P)
        G=np.array([[int(np.trace(ops[x].astype(object)@ops[y].astype(object))%P) for y in range(45)] for x in range(45)],dtype=np.int64)
        Gs=sp.Matrix(45,45,lambda r,c:int(G[r,c])).inv_mod(P)
        Om=np.zeros((27,27),dtype=object)
        for x in range(45):
            for y in range(45):
                g=int(Gs[x,y])%P
                if g: Om=(Om+g*(ops[x].astype(object)@ops[y].astype(object)))%P
        Om=Om%P
        Mo=sp.Matrix(27,27,lambda r,c:int(Om[r,c]))
        eig={}
        for f,m in sp.factor_list(sp.Poly(Mo.charpoly(sp.Symbol('L')).as_expr(),sp.Symbol('L'),modulus=P).as_expr(),modulus=P)[1]:
            if sp.Poly(f,sp.Symbol('L')).degree()==1:
                r0=int(sp.ground_roots(f,modulus=P).popitem()[0])%P
                Kn=np.array([[int((Mo-r0*sp.eye(27))[r,c])%P for c in range(27)] for r in range(27)],dtype=np.int64)
                eig[r0]=27-rank_mod_p(Kn)
        lam16=[l for l,mu in eig.items() if mu==16][0]
        Pm=np.eye(27,dtype=object)
        for mu in eig:
            if mu!=lam16: Pm=(Pm@((Om-mu*np.eye(27,dtype=object))*pow((lam16-mu)%P,P-2,P)))%P
        res=[]
        for k,vv2 in enumerate(g27):
            w2=np.zeros(27,dtype=object)
            for kk,val in vv2.items(): w2[IDX27[E.ROOTS[kk-E.N]]]=(val.numerator%P)*pow(val.denominator%P,P-2,P)%P
            res.append(int(np.count_nonzero((Pm@w2)%P)))
        print(f"  so(10)=Stab(e{i+1},eb{j+1}): Casimir mults {sorted(eig.values())} | "
              f"16-component nonzero-entry counts for e1,e2,e3 = {res}")
