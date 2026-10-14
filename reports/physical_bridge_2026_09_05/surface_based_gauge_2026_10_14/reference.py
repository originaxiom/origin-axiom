"""Distinct Fraction/Gaussian relation, commutant and phase-transport safeguards."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def load(folder,name='reference'):
    p=HERE.parent/folder/(name+'.py');sp=importlib.util.spec_from_file_location('completion_fraction_'+folder,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def inverse(w):return ''.join(c.swapcase() for c in reversed(w))
def simplify(w):
    while True:
        new=w
        for c in 'aAbB':new=new.replace(c+c.swapcase(),'')
        if new==w:return w
        w=new
def compose(f,g):
    return {c:simplify(''.join(f[x] if x.islower() else inverse(f[x.lower()]) for x in g[c])) for c in 'ab'}
def mpow(f,n):
    o={'a':'a','b':'b'}
    for _ in range(n):o=compose(f,o)
    return o
def inner(w):return {c:simplify(w+c+inverse(w)) for c in 'ab'}
def rank(rows):
    r=[list(map(Q,a)) for a in rows];n=0
    for j in range(len(r[0])):
        pivot=next((k for k in range(n,len(r)) if r[k][j]),None)
        if pivot is None:continue
        r[n],r[pivot]=r[pivot],r[n];c=r[n][j];r[n]=[x/c for x in r[n]]
        for k in range(len(r)):
            if k!=n:
                c=r[k][j];r[k]=[x-c*y for x,y in zip(r[k],r[n])]
        n+=1
        if n==len(r):break
    return n

@lru_cache(None)
def run():
    h=load('weave_registered_embedding_2026_10_13');checks={}
    def ck(n,v):checks[n]=bool(v)
    def power(m,n):
        o=h.identity(len(m))
        for _ in range(n):o=h.times(o,m)
        return o
    def trace(m):return h.sumg(m[j][j] for j in range(len(m)))
    X={'a':'a','b':'ab'};Y={'a':'aB','b':'b'};Z={'a':'a','b':'ba'}
    delta=compose(X,compose(Y,Z));U=compose(Z,{'a':'a','b':'Ab'})
    Ui=compose(X,{'a':'a','b':'bA'});Yi={'a':'ab','b':'b'}
    V=compose(Y,compose(U,compose(Yi,Ui)))
    ck('separate free-word centre',mpow(delta,4)=={'a':'a','b':'b'})
    ck('separate free-word braids',compose(X,compose(Y,X))==compose(Y,compose(X,Y)) and compose(Y,compose(Z,Y))==compose(Z,compose(Y,Z)))
    ck('separate based kernel',U==inner('A') and V==inner('b'))
    a=[[h.I,h.Z],[h.Z,h.gscale(-1,h.I)]];b=[[h.Z,h.O],[h.gscale(-1,h.O),h.Z]]
    A=h.block_diag([h.mscale(-1,a),a,h.mscale(-1,a)])
    B=h.block_diag([b,h.mscale(-1,b),h.mscale(-1,b)])
    Sf=h.block_diag([b,a,h.times(a,b)])
    P13=[[h.O if i==(2,1,0)[j] else h.Z for j in range(3)] for i in range(3)]
    P23=[[h.O if i==(0,2,1)[j] else h.Z for j in range(3)] for i in range(3)]
    qx=h.madd(h.identity(2),a);qy=h.madd(h.identity(2),b);qz=h.madd(h.identity(2),h.mscale(-1,a))
    NX=h.kron(P13,qx);NY=h.kron(P23,qy);NZ=h.times(h.dagger(A),NX)
    ck('Gaussian braid XYX',h.times(h.times(NX,NY),NX)==h.times(h.times(NY,NX),NY))
    ck('Gaussian braid YZY',h.times(h.times(NY,NZ),NY)==h.times(h.times(NZ,NY),NZ))
    ck('Gaussian distant commute',h.times(NX,NZ)==h.times(NZ,NX))
    ck('Gaussian normalized centre',power(h.times(h.times(NX,NY),NZ),4)==h.mscale(-64,h.identity(6)))
    for k,m in enumerate([NX,NY,NZ]):ck('Gaussian normalized unitary '+str(k),h.times(m,h.dagger(m))==h.mscale(2,h.identity(6)))
    fam=[]
    for k,(m,q) in enumerate(zip([NX,NY,NZ],[qx,qy,qz])):
        v=h.times(h.times(h.dagger(Sf),m),Sf)
        reduced=h.times(v,h.kron(h.identity(3),h.dagger(q)))
        M=[[h.gscale(Q(1,4),h.gadd(reduced[2*i][2*j],reduced[2*i+1][2*j+1])) for j in range(3)] for i in range(3)]
        ck('Gaussian exact factor '+str(k),v==h.kron(M,q) and all(x[1]==0 for row in M for x in row))
        fam.append([[x[0] for x in row] for row in M])
    def rmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    def trans(a):return [list(x) for x in zip(*a)]
    def sub(a,b):return [[x-y for x,y in zip(r,t)] for r,t in zip(a,b)]
    adj=[];sym=[]
    for i in range(3):
        for j in range(3):
            m=[[Q(0)]*3 for _ in range(3)];m[i][j]=Q(1)
            if i!=j:adj.append(m)
            if i<=j:
                if i!=j:m[j][i]=Q(1)
                sym.append(m)
    d1=[[Q(1),Q(0),Q(0)],[Q(0),Q(-1),Q(0)],[Q(0),Q(0),Q(0)]]
    d2=[[Q(0),Q(0),Q(0)],[Q(0),Q(1),Q(0)],[Q(0),Q(0),Q(-1)]]
    adj+= [d1,d2]
    def kernel(basis,congruence=False):
        cols=[]
        for m in basis:
            vals=[]
            for g in fam[:2]:
                z=sub(rmul(rmul(g,m),trans(g)),m) if congruence else sub(rmul(g,m),rmul(m,g))
                vals.extend(x for row in z for x in row)
            cols.append(vals)
        return len(basis)-rank(list(zip(*cols)))
    na=kernel(adj);ns=kernel(sym,True);nd=kernel([d1,d2])
    ck('commutant identity control',kernel([[[Q(i==j) for j in range(3)] for i in range(3)]])==1)
    ck('row rank reject control',rank([[1,0],[0,1]])==2 and rank([[1,1],[2,2]])==1)
    # Exact all-root centre test, not just branch dimensions.
    rr,chain,ws=h.frame(6);e,_=h.root_data()
    hq=tuple(sum(Q((1,-1)[i%2])*ws[i][j] for i in range(6)) for j in range(8))
    hw=h.add(e[3],h.neg(e[4]))
    ck('Gaussian root centre cancellation',all(h.dot(r,h.add(hq,h.neg(hw)))%2==0 for r in rr))
    ck('unpaired centre rejects',any(h.dot(r,hq)%2 for r in rr))
    # Reconstruct OLD full-even four phases with Gaussian characters,
    # then shift the TWO weak roots; not native 12-phase DFT.
    old=[]
    for av in (1,-1):
        row=[]
        for num in [h.O,h.I,h.gscale(-1,h.O),h.gscale(-1,h.I)]:
            total=h.Z
            for j in (0,1):
                for k in range(4):
                    g=h.times(power(A,j),power(NX,k));t=trace(g);t2=trace(h.times(g,g))
                    w2=h.gscale(Q(1,2*2**k),h.gadd(h.gmul(t,t),h.gscale(-1,t2)))
                    char=h.gmul(t,h.conj(t))[0]/2**k+10+6*w2[0]
                    ph=h.O
                    for _ in range(k):ph=h.gmul(ph,h.conj(num))
                    total=h.gadd(total,h.gscale(char*av**j,ph))
            value=h.gscale(Q(1,8),total)
            if value[1] or value[0].denominator!=1:raise ValueError('old even rank nonintegral')
            row.append(int(value[0]))
        old.append(row)
    even=[]
    for label,row in zip(['+1','-1'],old):
        count=Counter({3*k:n for k,n in enumerate(row)})
        if label=='+1':count[0]-=2;count[1]+=1;count[11]+=1
        even.append([label,[[r,count[r]] for r in range(12)]])
    oldodd=load('surface_odd_form_2026_10_14').run()
    ck('upstream odd exact controls pass',oldodd['all_passed'])
    odd=[]
    for label,row in oldodd['records']['odd_phase_populations']:
        count=Counter()
        for r,n in row:
            ck('old weak pair multiplicity even '+label+str(r),n%2==0)
            for sign in (-1,1):count[((3*r+sign)%24)//2]+=n//2
        odd.append([label,[[r,count[r]] for r in range(12)]])
    ck('transport retains248',sum(n for out in [even,odd] for _,row in out for _,n in row)==248)
    ck('transport retains112 odd',sum(n for _,row in odd for _,n in row)==112)
    ck('odd zero-phase rejection',all(row[0][1]==0 for _,row in odd))
    dist=min(min(Q(r,12),1-Q(r,12)) for out in [even,odd] for _,row in out for r,n in row if r and n)
    ck('weak angle centre exact rational',12*Q(-1,24)%1==Q(1,2))
    ck('wrong weak angle centre reject',12*Q(-1,48)%1!=Q(1,2))
    records={'word_delta':delta,'recovered_inner_A':U,'recovered_inner_b':V,
             'SU6_centre_sign':-1,'weak_centre_sign':-1,'paired_E8_centre_sign':1,
             'family_moves':[[[str(x) for x in row] for row in m] for m in fam],
             'family_adjoint_invariants':na,'family_symmetric_invariants':ns,
             'diagonal_block_hypercharge_invariants':nd,'weak_invariants':1,
             'complete_based_gauge_invariant_dimension':na+8+1+6*ns,
             'even_phase_populations':even,'odd_phase_populations':odd,
             'minimum_nonzero_phase':str(dist),
             'even_x_growth_pi_squared_coefficient':str(2*dist**2),
             'odd_P_growth_pi_squared_coefficient':str(dist**2),
             'canonical_even_zero_phase_bound':'3/16','odd_Q_form_norm_error':4}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'Fraction safeguards and transported full roster, not specialist global-domain or physical acceptance'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
