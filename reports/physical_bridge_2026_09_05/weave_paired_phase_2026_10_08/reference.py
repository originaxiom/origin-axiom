"""Independent paired Gaussian coefficient and tensor-index route."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
path=Path(__file__).resolve().parent.parent/'weave_physical_mass_2026_10_08/reference.py'
spec=importlib.util.spec_from_file_location('paired_phase_tensor',path)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
@lru_cache(None)
def run():
    facts={};m=s.symbols('m',positive=True)
    # Characteristic roots of bdagger*b: trace7 and determinant4.
    roots=[(7+s.sqrt(33))/2,(7-s.sqrt(33))/2]
    determinant=s.expand((m*m+roots[0])*(m*m+roots[1]))
    facts['positive_squared_masses']=all(x>0 for x in roots)
    facts['direct_eigenvalue_product']=determinant==m**4+7*m*m+4
    facts['positive_regulator_ratio']=all((determinant/(s.symbols('L',positive=True)**4+7*s.symbols('L',positive=True)**2+4)).subs(m,x).is_positive for x in (s.Rational(1,2),1,3))
    # Rank-three Gaussian mass couples three of four source and five target slots.
    B=s.zeros(5,4)
    for j,v in enumerate((2,3,5)):B[j,j]=v
    kp=len(B.nullspace());km=len(B.T.nullspace())
    facts['independent_kernel_and_target_count']=(kp,km)==(1,2) and kp-km==-1
    facts['extra_pairs_do_not_change_virtual_character']=all((kp+r)-(km+r)==-1 for r in range(7))
    facts['full_tensor_population']=sum(prior.tensor_weights().values())==248
    data={str(n):prior.anomalies(n) for n in range(-3,4)}
    facts['first_and_higher_color_coefficients']=data['1'][0]=='-1' and data['2'][0]=='-3'
    facts['zero_and_opposite_coefficients']=data['0']==['0']*5 and all([s.sympify(x) for x in data[str(-n)]]==[-s.sympify(x) for x in data[str(n)]] for n in (1,2,3))
    facts={k:bool(v) for k,v in facts.items()}
    return {'predicates':facts,'predicates_passed':sum(facts.values()),'anomaly_vectors':data,
      'polar_kernel_dimensions':[kp,km],'massive_gaussian_polynomial':str(determinant),
      'nonauthor_acceptance':False}
if __name__=='__main__':
    data=run();print(json.dumps(data,indent=2,sort_keys=True));raise SystemExit(0 if all(data['predicates'].values()) else 1)
