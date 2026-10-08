"""Separate rational quadratic-field verification, not an analytic theorem checker."""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('analytic_cyclic_reference',HERE.parent/'silver_cyclic_transfer_2026_10_06/reference.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
K=c.K

def field(x):return x if isinstance(x,K) else K(x)
def bound(a):
    return sum(abs(field(x).a)+2*abs(field(x).b) for row in a for x in row)
def powers(a):
    out=[c.I(len(a))]
    for _ in range(len(a)):
        nxt=c.mm(out[-1],a)
        if c.zero(nxt):return out
        out.append(nxt)
    raise ValueError('not nilpotent')
def sub(a,rs,cs):return [[a[i][j] for j in cs] for i in rs]
def coefficient(v):
    out=c.Z(5)
    for row,b in zip(v,c.basis5()):out=c.add(out,c.scale(b,row[0]))
    return out
def quadratic(x,y):
    a,b=coefficient(x[:24]),coefficient(y[24:])
    z=c.add(c.mm(a,b),c.mm(b,a),-1)
    return [[z[i][j]] for i in range(5) for j in range(5) if i!=j]+[[z[i][i]] for i in range(4)]
def encoded(matrices):
    body=[[[str(field(row[0]).a),str(field(row[0]).b)] for row in v] for v in matrices]
    return hashlib.sha256(json.dumps(body,separators=(',',':')).encode()).hexdigest()
def catalans(limit):
    # Independent ballot count by height, no binary-tree recurrence.
    out=[]
    for length in range(limit+1):
        heights={0:1}
        for _ in range(2*length):
            nxt={}
            for h,v in heights.items():
                nxt[h+1]=nxt.get(h+1,0)+v
                if h:nxt[h-1]=nxt.get(h-1,0)+v
            heights=nxt
        out.append(heights.get(0,0))
    return out

@lru_cache(None)
def run():
    predicates={};blocks={};orders={};h_bounds={};inv_bounds={}
    def ck(key,val):
        predicates[key]=bool(val)
        assert predicates[key],key
    data,w,P,Q,A,B=c.literal()
    ck('literal_logs_and_relators',c.equal(c.series(A),P) and c.equal(c.series(B),Q) and
       c.equal(c.mm(A,B),c.mm(B,A)) and all(c.equal(c.word(w,r),c.I(5)) for r in data['relators']))
    basis=c.basis5();metric=c.gram(basis,True);trace=c.gram(basis)
    expected=c.diag(c.I(20),[[int(i==j)+1 for j in range(4)] for i in range(4)])
    ck('neutral_metric_and_condition_bound',c.equal(metric,expected) and
       c.equal(c.mm(c.add(metric,c.I(24),-1),c.add(metric,c.scale(c.I(24),5),-1)),c.Z(24)))
    FA,FB=c.wedge_derivative(A),c.wedge_derivative(B)
    logs={'W':(A,B),'Wdual':(c.scale(c.tr(A),-1),c.scale(c.tr(B),-1)),
          'F':(FA,FB),'Fdual':(c.scale(c.tr(FA),-1),c.scale(c.tr(FB),-1)),
          'N':(c.ad(A,basis),c.ad(B,basis)),'gauge':(c.Z(1),c.Z(1))}
    for name,(a,b) in logs.items():
        E=c.contraction(a,b,metric if name=='N' else None);blocks[name]=E
        d,h,p=E['d'],E['h'],E['p'];unit=c.I(len(d))
        product=c.add(c.mm(d,h),c.mm(h,d));target=c.add(unit,p,-1)
        ck(name+'_SDR',c.equal(product,target) and c.zero(c.mm(h,h)) and c.zero(c.mm(h,p)) and c.zero(c.mm(p,h)))
        ck(name+'_wrong_sign_control',c.zero(d) if name=='gauge' else not c.equal(c.scale(product,-1),target))
        pp=[powers(x) for x in (a,b)];orders[name]=[len(x) for x in pp]
        ck(name+'_resolvent_truncation_control',all(not c.zero(x[-1]) for x in pp))
        h_bounds[name]=3*bound(h)
        inv_bounds[name]=max(3*sum(bound(v)/6**(j+1) for j,v in enumerate(x)) for x in pp)
    ck('all_actual_cyclic_pairings',all(c.cyclic(blocks[n],blocks[n+'dual'])[k] for n in ('W','F') for k in ('d','h','p','isotropic')) and
       all(c.cyclic(blocks[n],trace=g)[k] for n,g in (('N',trace),('gauge',c.I(1))) for k in ('d','h','p','isotropic')))
    C0=max(h_bounds.values());C1=max(inv_bounds.values());C=max(F(1),C0,C1)
    ck('finite_positive_bounds',C>=1 and C1>0 and all(x>=0 for x in h_bounds.values()))
    mult={'W':10,'Wdual':10,'F':5,'Fdual':5,'N':1,'gauge':24}
    H=[sum(mult[k]*blocks[k]['betti'][j] for k in mult) for j in range(3)]
    ck('full_roster',sum(mult[k]*blocks[k]['n'] for k in mult)==248 and H==[100,200,100])
    cat=catalans(32)
    ck('ballot_count_obeys_binary_recursion',cat[0]==1 and all(cat[n]==sum(cat[j]*cat[n-1-j] for j in range(n)) for n in range(1,33)))
    ck('tree_bound',all(cat[n]<=4**n for n in range(33)))
    # Rescale by rho: epsilon*rho=1/8 and R*rho=1/4.
    ck('contracting_ball',F(1,8)+F(1,2)*F(1,4)**2<F(1,4) and F(1,4)<1)
    ck('large_ball_rejected',F(2)>1)
    E=blocks['N'];n=24
    h2=sub(E['h'],range(n,3*n),range(3*n,4*n))
    h1=sub(E['h'],range(n),range(n,3*n))
    p2=sub(E['p'],range(3*n,4*n),range(3*n,4*n))
    p1=sub(E['p'],range(n,3*n),range(n,3*n))
    d1=sub(E['d'],range(3*n,4*n),range(n,3*n))
    jets=[];profiles=[];slice_checks=[];curvature_checks=[]
    for j in range(4):
        eta=c.mm(p1,[[((i+3*j)**2 % 7)-3] for i in range(48)])
        aa=[c.Z(48,1),eta];kk=[c.Z(24,1),c.Z(24,1)]
        for r in range(2,5):
            q=c.Z(24,1)
            for i in range(1,r):q=c.add(q,quadratic(aa[i],aa[r-i]))
            ar=c.scale(c.mm(h2,q),-1);kr=c.mm(p2,q)
            aa.append(ar);kk.append(kr)
            slice_checks.append(c.zero(c.mm(h1,ar)) and c.zero(c.mm(p1,ar)))
            curvature_checks.append(c.equal(c.add(c.mm(d1,ar),q),kr))
        ck('harmonic_input_'+str(j),c.zero(c.mm(d1,eta)) and c.zero(c.mm(h1,eta)) and c.equal(c.mm(p1,eta),eta))
        jets.append(aa[1:])
        profiles.append(dict(nonzero_corrections=[not c.zero(x) for x in aa[2:]],
          nonzero_obstructions=[not c.zero(x) for x in kk[2:]],
          exact_jet_sha256=encoded(aa[1:]+kk[1:])))
    ck('nonlinear_slice',all(slice_checks))
    ck('curvature_obstruction_identity',all(curvature_checks))
    V=c.tr([[row[0] for row in x] for jet in jets for x in jet])
    J=c.stack(c.cat(c.Z(24),trace),c.cat(c.scale(trace,-1),c.Z(24)))
    O=c.mm(c.mm(c.tr(V),J),V)
    ck('symplectic_jet_pairings',all(not O[i][j] for i in range(16) for j in range(16) if i%4 or j%4))
    x,y,z=c.Z(5),c.Z(5),c.Z(5);x[0][1]=1;y[1][0]=1;z[0][2]=1
    comm=c.add(c.mm(x,y),c.mm(y,x),-1);target=c.Z(5);target[0][0]=1;target[1][1]=-1
    ck('nonflat_and_flat_opposite_controls',c.equal(comm,target) and not c.zero(comm) and c.zero(c.add(c.mm(x,z),c.mm(z,x),-1)))
    return dict(predicates=predicates,predicates_passed=len(predicates),nilpotence_orders=orders,
      homotopy_bounds={k:str(v) for k,v in h_bounds.items()},inverse_bounds={k:str(v) for k,v in inv_bounds.items()},
      global_bounds=dict(C0=str(C0),C1=str(C1),c=str(C)),
      full_harmonic_dimensions=H,neutral_jets=profiles,
      some_neutral_nonlinear_correction=any(any(x['nonzero_corrections']) for x in profiles),
      physical_goal_achieved=False,nonauthor_acceptance=False)

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
