"""B1100 exact pass v2: candidate joint weights from float; each verified as an
EXACT stacked-kernel dimension. No restrictions, no inverses."""
import json, random
from fractions import Fraction as F
from collections import Counter
import numpy as np
import sympy as sp

CERT="cloud_handoff/certificates/twisted_double.py"
G={}
s=open(CERT).read(); exec(s[:s.find('print(" IDENTITY double')], G)
br, DIM, rho27_Q = G['br'], G['DIM'], G['rho27_Q']
trip=json.load(open('/Users/dri/origin-axiom/frontier/B1098_nonabelian_hatch/b1098_a2_triple.json'))
de=lambda v:[F(a,b) for a,b in v]
X,H,Y=de(trip["X"]),de(trip["H"]),de(trip["Y"])
def adm_sp(Z):
    return sp.Matrix([[sp.Rational(c.numerator,c.denominator) for c in br(Z,[F(1) if j==i else F(0) for j in range(DIM)])] for i in range(DIM)]).T
cb=sp.Matrix.vstack(adm_sp(X),adm_sp(H),adm_sp(Y)).nullspace()
tofr=lambda v:[F(sp.Rational(x).p,sp.Rational(x).q) for x in v]
Cb=[tofr(v) for v in cb]
rng=random.Random(11)
Cmat=sp.Matrix.hstack(*cb)
xg=[F(0)]*DIM
for c_,b in zip([rng.randint(-5,5) or 1 for _ in Cb],Cb):
    for i in range(DIM): xg[i]+=F(c_)*b[i]
cols=[]
for b in Cb:
    img=br(xg,b)
    sol=Cmat.gauss_jordan_solve(sp.Matrix([sp.Rational(c.numerator,c.denominator) for c in img]))[0]
    cols.append(sol.subs({q:0 for q in sol.free_symbols}))
cartc=sp.Matrix.hstack(*cols).nullspace()
cart=[[sum(F(sp.Rational(t[k]).p,sp.Rational(t[k]).q)*Cb[k][i] for k in range(16)) for i in range(DIM)] for t in cartc]
print("exact Cartan dim:",len(cart))
H27=[sp.Matrix([[sp.Rational(v.numerator,v.denominator) for v in row] for row in rho27_Q(h)]) for h in cart]
Hs=sp.Matrix([[sp.Rational(v.numerator,v.denominator) for v in row] for row in rho27_Q(H)])
Ms=[Hs]+H27
# float candidates
Mf=[np.array(M.tolist(), dtype=float) for M in Ms]
comb=sum(rng.uniform(0.5,2.0)*m for m in Mf[1:])+0.001*Mf[0]
w,P=np.linalg.eig(comb); Pi=np.linalg.inv(P)
tups=[]
for i in range(27):
    tups.append(tuple(complex(np.round((Pi@m@P)[i,i],4)) for m in Mf))
# EXACT per-matrix spectra from charpolys; snap float coords to nearest exact root
spectra=[]
lam=sp.Symbol('lam')
for M in Ms:
    cp=sp.Matrix(M).charpoly(lam)
    roots=[]
    for fac,_ in sp.factor_list(cp.as_expr(), lam)[1]:
        d=sp.degree(fac, lam)
        if d==1:
            roots.append(sp.solve(fac, lam)[0])
        elif d==2:
            roots += sp.solve(fac, lam)
        else:
            roots += [sp.RootOf(fac, i) for i in range(d)]
    spectra.append(list(set(sp.simplify(r) for r in roots)))
print("spectrum sizes:", [len(s) for s in spectra])
def snap(x, spec):
    return min(spec, key=lambda e: abs(complex(e)-complex(x)))
cands=set()
for t in tups:
    cands.add(tuple(snap(t[k],spectra[k]) for k in range(len(Ms))))
cands=sorted(cands, key=lambda tt: [ (float(sp.re(z)),float(sp.im(z))) for z in tt ])
print("distinct candidate tuples:",len(cands))
total=0; table={}
for t in cands:
    stack=sp.Matrix.vstack(*[M-t[k]*sp.eye(27) for k,M in enumerate(Ms)])
    d=27-stack.rank()
    if d>0: table[t]=d; total+=d
print("EXACT multiplicities sum:",total,"(must be 27)")
cw=Counter()
for t,d in table.items(): cw[t[1:]]+=d
neg=Counter()
for w_,m in cw.items(): neg[tuple(sp.simplify(-x) for x in w_)]+=m
real=(cw==neg)
witness=None
for w_,m in cw.items():
    if neg.get(w_,0)!=m:
        witness=(tuple(str(x) for x in w_),m,cw.get(tuple(-x for x in w_),0)); break
sl2m=Counter()
for t,d in table.items(): sl2m[t[0]]+=d
print("sl2 multiset EXACT:", dict((str(k),v) for k,v in sl2m.items()))
print("EXACT REALITY: self-conjugate?",real,"| witness:",witness)
# hypercharge exact assignment on the EXACT weight classes
target=Counter([F(1,6)]*6+[F(-2,3)]*3+[F(1,3)]*3+[F(-1,2)]*2+[F(1)]+[F(0)]+[F(-1,3)]*3+[F(1,3)]*3+[F(1,2)]*2+[F(-1,2)]*2+[F(0)])
wt=sorted(cw.items(), key=lambda kv:-kv[1]); tv=sorted(target.items(), key=lambda kv:-kv[1])
print("weight-class sizes:",[m for _,m in wt],"| target sizes:",[m for _,m in tv])
from itertools import permutations, product as iproduct
by_w={}; by_v={}
for w_,m in wt: by_w.setdefault(m,[]).append(w_)
for v,m in tv: by_v.setdefault(m,[]).append(v)
match=None
if sorted(by_w)==sorted(by_v) and all(len(by_w[m])==len(by_v[m]) for m in by_w):
    keys=sorted(by_w)
    for choice in iproduct(*[list(permutations(by_v[m])) for m in keys]):
        pairs=[]
        for m,perm in zip(keys,choice): pairs+=list(zip(by_w[m],perm))
        A=sp.Matrix([[x for x in w_] for w_,_ in pairs])
        bv=sp.Matrix([sp.Rational(v.numerator,v.denominator) for _,v in pairs])
        try:
            sol,params=A.gauss_jordan_solve(bv)
            sol=sol.subs({q:0 for q in sol.free_symbols})
        except Exception: continue
        if all(sp.simplify(sum(sol[k]*w_[k] for k in range(4)) - sp.Rational(v.numerator,v.denominator))==0 for w_,v in pairs):
            match=[str(x) for x in sol]; break
print("HYPERCHARGE EXACT:", "MATCH t="+str(match) if match else "NO multiplicity-respecting exact assignment (typed)")
json.dump({"sum":total,"real":bool(real),"witness":str(witness),
           "sl2":dict((str(k),v) for k,v in sl2m.items()),
           "classes":[[ [str(sp.simplify(x)) for x in w_], m] for w_,m in wt],
           "match":match}, open('b1100_exact5.json','w'))
print("done")
