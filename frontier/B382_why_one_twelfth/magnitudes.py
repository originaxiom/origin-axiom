"""B382 leg 4 (the named residue) -- |chi|^2 per det-class + per-(a,b) class partials.
Registered expectations (two-outcome): class-1 |chi|^2 = 1 (unit metaplectic characters)
=> the -1/16 is a pure phase-sum identity; class-5 |chi|^2 in {5-ish} pattern; per-(a,b)
partials uniform across the four slot cells."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

N=15
W1 = build_theta_W(1); W2 = build_theta_W(2)
o1,pow1 = matrix_order(W1); o2,pow2 = matrix_order(W2)
X  = [[E.ONE if i==(j+1)%N else E.ZERO for j in range(N)] for i in range(N)]
Z  = [[E.e15(j%15) if i==j else E.ZERO for j in range(N)] for i in range(N)]
Par= [[E.ONE if i==(-j)%N else E.ZERO for j in range(N)] for i in range(N)]
z6i= E.zeta(50)
Jm = E.mmul(E.mmul(X,Z),Par)
J  = [[E.mul(z6i, Jm[i][j]) for j in range(N)] for i in range(N)]
Jinv=[[E.ZERO]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if J[i][j]!=E.ZERO:
            for k in range(60):
                if J[i][j]==E.zeta(k): Jinv[j][i]=E.zeta((-k)%60); break
g1=[[2,1],[1,1]]; g2=[[5,2],[2,1]]
def m2(A,B): return [[(A[i][0]*B[0][j]+A[i][1]*B[1][j])%15 for j in range(2)] for i in range(2)]
G1=[[[1,0],[0,1]]]
for _ in range(19): G1.append(m2(G1[-1],g1))
G2=[[[1,0],[0,1]]]
for _ in range(11): G2.append(m2(G2[-1],g2))
def tr15(M):
    t=E.ZERO
    for i in range(N): t=E.add(t,M[i][i])
    return t
def conj(t): return SC.sigma(t,59)   # complex conjugation on Q(zeta60)

hist = {}
CV = {}
for j in range(o1):
    for l in range(o2):
        V = E.mmul(E.mmul(pow1[j],pow2[l]), Jinv)
        chi = tr15(V)
        gp = m2(G1[j],G2[l])
        det = ((-gp[0][0]-1)*(-gp[1][1]-1)-gp[0][1]*gp[1][0])%15
        cls = gcd(det,15)
        m2v = E.mul(chi, conj(chi))
        key = None
        # |chi|^2 should be rational: solve in H then read x
        sol = SC.solve_H(SC.H_avg(m2v))
        key = tuple(str(x) for x in sol) if sol else "nonH"
        hist.setdefault(cls,{}).setdefault(key,0)
        hist[cls][key]+=1
        CV[(j,l)] = par_trace(pow1[j],pow2[l])
print("|chi|^2 histogram per det-class:")
for c in sorted(hist): print(" class",c, dict(hist[c]))

# per-(a,b) class partials over the four slot cells
def tval_cls(a,b,cls):
    t=E.ZERO
    for j in range(o1):
        za=E.zeta((-3*j*a)%60)
        for l in range(o2):
            gp=m2(G1[j],G2[l])
            det=((-gp[0][0]-1)*(-gp[1][1]-1)-gp[0][1]*gp[1][0])%15
            if gcd(det,15)!=cls: continue
            t=E.add(t,E.mul(E.mul(za,E.zeta((-5*l*b)%60)),CV[(j,l)]))
    return E.scal(Fr(1,240),t)
out={}
for a in (6,14):
    for b in (2,10):
        for cls in (1,5):
            sol=SC.solve_H(SC.H_avg(tval_cls(a,b,cls)))
            out[f"{a},{b},cls{cls}"]=[str(x) for x in sol]
            print(f" t({a},{b}) class-{cls}:", [str(x) for x in sol])
json.dump(dict(hist={str(c):{("|".join(k) if isinstance(k,tuple) else k):v for k,v in h.items()} for c,h in hist.items()},
               partials=out), open(os.path.join(HERE,"magnitudes.json"),"w"), indent=1)
print("DONE")
