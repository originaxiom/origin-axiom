"""Post-intake control of W57's invariant-measure uniqueness premise.

The analytic counterexample is dmu_eps=(1+eps/(1+F)) dxdy/y^2,
F=sum |theta_p/eta|^4, eps>0. F is invariant by the S,T theta/eta
transformation laws. The density factor lies between1 and1+eps,
so the finite hyperbolic fundamental-domain measure stays finite.
Nonconstant F makes it different even after probability normalization.
Numerical evaluations below illustrate, not certify, the analytic laws.
"""
import importlib.util
import json
from pathlib import Path
import mpmath as mp

root=Path(__file__).resolve().parent
p=root/'frontier/B1638_the_golden_identity/verification/golden_identity.py'
spec=importlib.util.spec_from_file_location('frozen_golden_identity',p)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def F(t):
    return mp.fsum(abs(x)**2 for x in m.g(t))
pts=[mp.mpc('.13','1.2'),mp.mpc('-.31','1.7'),mp.mpc('.21','2.3')]
rows=[]
for t in pts:
    f=F(t)
    rows.append({'tau':[float(t.real),float(t.imag)],'F':float(f),
                 'S_residual':float(abs(F(-1/t)-f)),
                 'T_residual':float(abs(F(t+1)-f)),
                 'modified_density_factor':float(1+1/(1+f))})
fi=F(mp.j)
fo=F(mp.mpc(-mp.mpf(1)/2,mp.sqrt(3)/2))
out={'scope':'analytic bounded-density counterexample with numerical S/T controls; not an alternative physics model or a refit',
     'controls':rows,'F_i':float(fi),'F_omega':float(fo),
     'nonconstant':abs(fi-fo)>mp.mpf('.1'),
     'illustrative_invariance_passed':all(max(r['S_residual'],r['T_residual'])<1e-40 for r in rows)}
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['nonconstant'] and out['illustrative_invariance_passed'] else 1)
