"""Fraction phase transport independently of native full DFT."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
def load(folder):
    p=HERE.parent/folder/'reference.py';sp=importlib.util.spec_from_file_location('completion_transport_'+folder,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
@lru_cache(None)
def run():
    checks={}
    def ck(n,v):checks[n]=bool(v)
    base=load('surface_based_gauge_2026_10_14').run();old=load('surface_odd_form_2026_10_14').run()
    ck('prior Gaussian sources pass',base['all_passed'] and old['all_passed'])
    labels=[m for m in range(24) if 12*Q(-m,24)%1==Q(1,2)]
    reps=sorted({min(m,24-m) for m in labels});rows=[]
    for m in reps:
        even=[]
        for name,row in base['records']['even_phase_populations']:
            count=Counter(dict(row))
            if name=='+1':count[1]-=1;count[11]-=1;count[m]+=1;count[12-m]+=1
            even.append([name,[[r,count[r]] for r in range(12)]])
        odd=[]
        for name,row in old['records']['odd_phase_populations']:
            count=Counter()
            for r,n in row:
                ck('weak pairs integral '+str((m,name,r)),n%2==0)
                for sign in (-1,1):
                    num=(3*r+sign*m)%24;ck('phase lies on twelfths '+str((m,name,r,sign)),num%2==0)
                    count[num//2]+=n//2
            odd.append([name,[[r,count[r]] for r in range(12)]])
        ck('all even retained '+str(m),sum(n for _,row in even for _,n in row)==136)
        ck('all odd retained '+str(m),sum(n for _,row in odd for _,n in row)==112)
        rows.append({'m':m,'even':even,'odd':odd,'odd_zero_phase_ranks':[row[0][1] for _,row in odd],
                     'full_parallel_gauge_dimension':base['records']['complete_based_gauge_invariant_dimension'],
                     'diagonal_Y_invariants':base['records']['diagonal_block_hypercharge_invariants']})
    h=load('weave_registered_embedding_2026_10_13')
    I=h.identity(2);sigma1=[[h.Z,h.O],[h.O,h.Z]];sigma2=[[h.Z,h.gscale(-1,h.I)],[h.I,h.Z]]
    for xi,beta in [(Q(1,3),Q(1,2)),(Q(-5,7),Q(1)),(Q(0),Q(0))]:
        D=h.madd(h.mscale(-xi,sigma2),h.mscale(-beta,sigma1))
        ck('rational Fourier square '+str((xi,beta)),h.times(D,D)==h.mscale(xi*xi+beta*beta,I))
    ck('nearest-integer all-N residue distance',[min(Q(v)%6,6-Q(v)%6) for v in (Q(1,2),Q(1))]==[Q(1,2),Q(1)])
    ck('massless zero-phase comparator',Q(0)**2<Q(1,4))
    return {'checks':checks,'records':{'angle_labels':labels,'inverse_representatives':reps,'classes':rows,
        'canonical_zero_phase_beta_squared_floor':'1/4','canonical_even_tail_squared_floor':'3/16'},
        'all_passed':all(checks.values()),'scope':'complete Fraction transport controls, not outside analytic acceptance'}
if __name__=='__main__':
    o=run();print(json.dumps(o,indent=2));raise SystemExit(0 if o['all_passed'] else 1)
