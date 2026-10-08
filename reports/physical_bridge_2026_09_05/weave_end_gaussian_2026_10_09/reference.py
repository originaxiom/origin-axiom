"""Separate four-state Fock quantization and tensor spin-line boundary count."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/reference.py'
spec=importlib.util.spec_from_file_location('end_gaussian_tensor',path)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
zero=lambda A:all(s.simplify(x)==0 for x in A)

def annihilator(i):
    A=s.zeros(4)
    for state in range(4):
        if state & (1<<i):
            sign=(-1)**sum((state>>j)&1 for j in range(i))
            A[state^(1<<i),state]=sign
    return A

def line_masses(b):
    return [F(-b-1,2),F(1-b,2)] if b%2==0 else [F(b,2)]*2
def sign(x):return 1 if x>0 else -1

def end_indices(n):
    out=Counter()
    for (a,b,w,q,m),mult in prior.tensor_weights().items():
        out[a,b,w,q]+=mult*sum(sign(ref) for mu,ref in zip(line_masses(m+2*n*q),line_masses(m)) if mu*ref<0)
    return out

def profile(n):
    byq={}
    for (a,b,w,q),value in end_indices(n).items():
        if q>0:byq.setdefault(q,set()).add(value)
    assert all(len(v)==1 for v in byq.values())
    return {str(q):next(iter(v)) for q,v in sorted(byq.items())}

def anomaly(n):
    out=[F(0)]*5
    for (a,b,w,q),value in end_indices(n).items():
        if q<=0:continue
        terms=[F((a+2*b)**3,-6),F(q*a*a,4),F(q*w*w,4),F(q**3),F(q)]
        out=[x+value*y for x,y in zip(out,terms)]
    return [str(x) for x in out]

@lru_cache(None)
def run():
    facts={};ops=[annihilator(0),annihilator(1)]
    facts['canonical_anticommutators']=all(zero(A*B+B*A) and zero(A*B.adjoint()+B.adjoint()*A-(s.eye(4) if i==j else s.zeros(4))) for i,A in enumerate(ops) for j,B in enumerate(ops))
    overlaps=[];eigen=True;ground=True;projection=True
    for m,z in ((3,4*s.I),(12,3+4*s.I),(12,3-4*s.I)):
        E=s.sqrt(m*m+z*s.conjugate(z));states=[]
        for mass,anchor in ((m,2),(-m,1)):
            h=s.Matrix([[mass,s.conjugate(z)],[z,-mass]])
            HF=sum((ops[i].adjoint()*h[i,j]*ops[j] for i in range(2) for j in range(2)),s.zeros(4))
            null=(HF+E*s.eye(4)).nullspace();ground &= len(null)==1
            v=null[0]/null[0][anchor]
            v=v/s.sqrt((v.adjoint()*v)[0]);states.append(v)
            eigen &= HF.charpoly().as_expr().factor()==(HF.charpoly().gen**2*(HF.charpoly().gen-E)*(HF.charpoly().gen+E)).expand().factor()
            Pg=v*v.adjoint();Pone=s.diag(0,1,1,0);Pzero=s.eye(4)-Pone
            decay=s.symbols('decay',real=True)
            ev=Pg+decay*Pzero+decay**2*(Pone-Pg)
            projection &= zero(ev.subs(decay,0)-Pg) and zero(Pg*Pg-Pg) and s.trace(Pg)==1
            # Exact spectral decomposition, not an asserted exponential.
            projection &= zero(HF+E*s.eye(4)-E*Pzero-2*E*(Pone-Pg))
        overlaps.append(str(s.simplify((states[0].adjoint()*states[1])[0])))
    facts['fock_spectrum_and_unique_ground']=eigen and ground
    facts['gaussian_transfer_projects_to_ground']=projection
    facts['complex_overlap_not_absolute_value']=overlaps[0]=='-4*I/5' and overlaps[1]!=overlaps[2]
    pop=prior.tensor_weights()
    facts['whole_tensor_and_horizontal_population']=sum(pop.values())==248 and sum(2*v for v in pop.values())==496
    facts['balanced_reference_net_is_negative_physical_index']=all(end_indices(n)==Counter({k:-v for k,v in prior.gauge_indices(n).items()}) for n in range(-3,4))
    facts['all_five_anomalies_opposite']=all(anomaly(n)==[str(-F(v)) for v in prior.anomalies(n)] for n in range(-3,4))
    facts['zero_and_first_flux_endpoints']=profile(0)=={str(q):0 for q in range(1,7)} and profile(1)['1']==0 and profile(2)['1']==1
    facts={k:bool(v) for k,v in facts.items()}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),'overlap_examples':overlaps,
      'boundary_net_profiles':{str(n):profile(n) for n in range(-3,4)},
      'boundary_anomaly_vectors':{str(n):anomaly(n) for n in range(-3,4)},'nonauthor_acceptance':False}
if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,sort_keys=True));raise SystemExit(0 if all(data['predicates'].values()) else 1)
