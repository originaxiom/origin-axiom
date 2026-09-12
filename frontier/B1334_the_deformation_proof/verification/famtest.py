"""Test the deformation argument where the family is positive-dimensional.

On d10_4 and d10_35 the cusp-trivial character group has a FREE direction: a homomorphism
phi: pi_1 -> Z killing every relator and every peripheral curve, giving a 1-parameter family
chi_z(g) = z^{phi(g)}.  The argument predicts:

  * t_0, t_0*, t_1 CONSTANT along the family   (cusp-triviality: the cusp matrices never move)
  * r_1(z) CONSTANT = t_1/2                    (generic max + inversion symmetry + semicontinuity)
  * hence I = 0 identically, with no isotropy anywhere in the argument

Sampled at every z in F_p^* -- that is p-1 points of the family, not three.
"""
import sys, warnings, json, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from collections import Counter
from index_lib import *
from mc_lib import check
from family import expsum, dim_S

def free_direction(gens,rels,per):
    """integer vector v with sum_i e_i(r) v_i = 0 for every relator and peripheral word"""
    n=len(gens)
    rows=[expsum(r,gens) for r in rels]+[expsum(w,gens) for (mu,lam) in per for w in (mu,lam)]
    M=[[Fr(x) for x in r] for r in rows]; piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n)]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]
    if not free: return None
    fc=free[0]; v=[Fr(0)]*n; v[fc]=Fr(1)
    for i,pc in enumerate(piv): v[pc]=-M[i][fc]
    den=1
    for x in v: den=den*x.denominator//__import__('math').gcd(den,x.denominator)
    return [int(x*den) for x in v]

def roots(p):
    return (next((x for x in range(p) if (x*x-3)%p==0),None),
            next((x for x in range(p) if (x*x+1)%p==0),None))
class Bad(Exception): pass
def red(z,p,s,t):
    a,b,c,d=[Fr(x) for x in z]
    def f(q):
        if q.denominator%p==0: raise Bad()
        return (q.numerator*pow(q.denominator,p-2,p))%p
    return (f(a)+f(b)*s+t*(f(c)+f(d)*s))%p
def sym_p(A,m,p):
    from math import comb
    d=m+1; out=[[0]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    for j in range(d):
        coef=[0]*d
        for u in range(m-j+1):
            for v in range(j+1):
                coef[u+v]=(coef[u+v]+comb(m-j,u)*pow(a,m-j-u,p)*pow(c,u,p)*comb(j,v)*pow(b,j-v,p)*pow(dd,v,p))%p
        for i in range(d): out[i][j]=coef[i]
    return out

P=int(os.environ.get('P','37'))
db=json.load(open('/tmp/sweep/covcache.json'))
for tag in sys.argv[1:] or ['d10_4','d10_35']:
    v=db[tag]; gens=v['gens']; rels=v['rels']; per=[tuple(x) for x in v['per']]
    dS=dim_S(gens,rels,per); phi=free_direction(gens,rels,per)
    print(f"\n=== {tag} === cusps={v['cusps']} dim S={dS}  phi={phi}", flush=True)
    if phi is None: print("   no free direction"); continue
    s,t=roots(P)
    rp={g:[[red(v['rho'][g][i][j],P,s,t) for j in range(2)] for i in range(2)] for g in gens}
    for m in (1,2):
        if v['proj'] and m%2: continue
        base={g:sym_p(rp[g],m,P) for g in gens}; d=m+1
        rows=Counter(); bad=0
        for z in range(1,P):
            V={g:[[(pow(z,phi[i],P)*base[g][x][y])%P for y in range(d)] for x in range(d)]
               for i,g in enumerate(gens)}
            if any(word_eval(r,V,P,d)!=eye(d) for r in rels): bad+=1; continue
            A,B,ids=check(gens,rels,per,V,P,d)
            if not all(ids.values()): bad+=1; continue
            rows[(A['t0'],A['t1'],A['r1'],A['I_exact'])]+=1
        print(f"  Sym^{m}: sampled {sum(rows.values())} points of the family (skipped {bad})")
        for k in sorted(rows):
            t0,t1,r1,I=k
            print(f"     t0={t0} t1={t1} r1={r1} I={I}   {'r1 == t1/2' if 2*r1==t1 else '** r1 != t1/2 **'}   x{rows[k]}")
        print(f"     -> t_1 constant: {len(set(k[1] for k in rows))==1} | r_1 constant: {len(set(k[2] for k in rows))==1}")
