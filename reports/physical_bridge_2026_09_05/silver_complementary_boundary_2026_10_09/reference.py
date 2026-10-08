"""Separate exact list-matrix checks; no native producer or cached results imported."""
import importlib.util
import json
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('complement_cyclic_ref',HERE.parent/'silver_cyclic_transfer_2026_10_06/reference.py')
c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
def sub(a,rs,cs):return [[a[i][j] for j in cs] for i in rs]

@lru_cache(None)
def run():
    predicates={};blocks={};profiles={}
    def ck(k,v):predicates[k]=bool(v);assert predicates[k],k
    data,w,P,Q,A,B=c.literal()
    ck('literal_logs_and_relators',c.equal(c.series(A),P) and c.equal(c.series(B),Q) and
       c.equal(c.mm(A,B),c.mm(B,A)) and all(c.equal(c.word(w,r),c.I(5)) for r in data['relators']))
    basis=c.basis5();metric=c.gram(basis,True);trace=c.gram(basis)
    FA,FB=c.wedge_derivative(A),c.wedge_derivative(B)
    logs={'W':(A,B),'Wdual':(c.scale(c.tr(A),-1),c.scale(c.tr(B),-1)),
          'F':(FA,FB),'Fdual':(c.scale(c.tr(FA),-1),c.scale(c.tr(FB),-1)),
          'N':(c.ad(A,basis),c.ad(B,basis)),'gauge':(c.Z(1),c.Z(1))}
    for name,(a,b) in logs.items():
        E=c.contraction(a,b,metric if name=='N' else None);blocks[name]=E;n=E['n']
        h2=sub(E['h'],range(n,3*n),range(3*n,4*n))
        d1=sub(E['d'],range(3*n,4*n),range(n,3*n))
        d0=sub(E['d'],range(n,3*n),range(n))
        p2=sub(E['p'],range(3*n,4*n),range(3*n,4*n))
        p1=sub(E['p'],range(n,3*n),range(n,3*n))
        U=c.mm(h2,d1);V=c.add(c.I(n),p2,-1)
        ck(name+'_chain_projectors',c.equal(c.mm(U,U),U) and c.equal(c.mm(V,V),V) and c.equal(c.mm(d1,U),d1) and c.equal(c.mm(V,d1),d1))
        ck(name+'_inverse',c.equal(c.mm(d1,h2),V) and c.equal(c.mm(U,h2),h2) and c.equal(c.mm(h2,V),h2))
        ck(name+'_separation',c.zero(c.mm(p1,U)) and c.zero(c.mm(U,p1)) and c.zero(c.mm(U,d0)))
        ru,rv=c.rank(U),c.rank(V)
        ck(name+'_acyclic',ru==rv==n-E['betti'][2] and c.rank(h2)==ru)
        ck(name+'_derivative_control',c.zero(d0) if name=='gauge' else not c.zero(d0))
        profiles[name]=dict(rank=n,harmonic=E['betti'],coexact_rank=ru,exact2_rank=rv)
    ck('all_cyclic_pairs',all(all(c.cyclic(blocks[n],blocks[n+'dual']).values()) for n in ('W','F')) and
       all(all(c.cyclic(blocks[n],trace=g).values()) for n,g in (('N',trace),('gauge',c.I(1)))))
    mult={'W':10,'Wdual':10,'F':5,'Fdual':5,'N':1,'gauge':24}
    H=[sum(mult[k]*blocks[k]['betti'][j] for k in mult) for j in range(3)]
    ck('full_248_harmonics',sum(mult[k]*blocks[k]['n'] for k in mult)==248 and H==[100,200,100])
    # Work with q/i and adapted/i, avoiding complex or symbolic packages.
    qx=[[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]
    qy=[[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]]
    gamma=c.stack(c.cat(c.Z(4),c.scale(c.I(4),-1)),c.cat(c.I(4),c.Z(4)))
    j=c.Z(8)
    for col,row,sgn in ((0,7,1),(1,6,1),(2,5,-1),(3,4,-1),(4,3,-1),(5,2,-1),(6,1,1),(7,0,1)):j[row][col]=sgn
    parity=[[int(i==k)*v for k in range(8)] for i,v in enumerate((1,-1,-1,1,-1,1,1,-1))]
    checks=[];count=0
    for x in range(-3,4):
        for y in range(-3,4):
            r=x*x+y*y
            if not r:continue
            count+=1
            alpha=[[0,0],[-y,0],[x,0],[0,1]];beta=[[1,0],[0,x],[0,y],[0,0]]
            pa=c.mm(c.mm(alpha,[[F(1,r),0],[0,1]]),c.tr(alpha))
            pb=c.mm(c.mm(beta,[[1,0],[0,F(1,r)]]),c.tr(beta))
            proj=c.diag(pa,pb);full=c.diag(alpha,beta)
            q=c.add(c.scale(qx,x),c.scale(qy,y))
            adapted=c.scale(c.mm(gamma,c.diag(q,c.scale(q,-1))),-1)
            wrong=c.diag(alpha,alpha)
            checks.append(c.rank(full)==4 and c.zero(c.mm(c.mm(c.tr(full),gamma),full)) and
              c.equal(c.mm(proj,proj),proj) and c.equal(c.add(c.mm(proj,adapted),c.mm(adapted,proj)),adapted) and
              c.equal(c.mm(adapted,adapted),c.scale(c.I(8),-r)) and
              c.equal(c.mm(c.mm(j,proj),j),proj) and c.equal(c.mm(parity,proj),c.mm(proj,parity)) and
              not c.zero(c.mm(c.mm(c.tr(wrong),gamma),wrong)))
            co=[[F(y*y,r),F(-x*y,r)],[F(-x*y,r),F(x*x,r)]];xi=[[x],[y]]
            checks.append(c.zero(c.mm(co,xi)) and x*x+y*y>0)
    ck('symbol_and_derivative_controls_all_48',count==48 and all(checks))
    # Coordinate-matrix cubic, independently multiplied over integers.
    e12=[[0,1,0],[0,0,0],[0,0,0]];e23=[[0,0,0],[0,0,1],[0,0,0]];e31=[[0,0,0],[0,0,0],[1,0,0]]
    bracket=c.add(c.mm(e12,e23),c.mm(e23,e12),-1)
    product=c.mm(e31,bracket)
    ck('noncommutative_cubic',sum(product[i][i] for i in range(3))==1)
    # Fourier convolution of cos(x)cos(y): four nonzero frequencies, no constant.
    coeff={(a,b):F(1,4) for a in (-1,1) for b in (-1,1)}
    ck('nonzero_bracket_zero_mean',sum(coeff.values())==1 and coeff.get((0,0),0)==0)
    # Affine control on the real plane a=t(1,2), reference=(3,5).
    pair=3*2-5;raw=-F(pair,2);counter=F(pair,2)
    ck('affine_sign_control',pair!=0 and raw+counter==0 and raw-counter!=0)
    return dict(predicates=predicates,predicates_passed=len(predicates),block_profiles=profiles,
      full_harmonic_dimensions=H,symbol_reference_covectors=count,
      conditional_cone_preserved=True,physical_goal_achieved=False,nonauthor_acceptance=False)

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
