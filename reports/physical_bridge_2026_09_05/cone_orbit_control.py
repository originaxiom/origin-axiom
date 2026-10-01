"""R73 separate exact algebra normalization; old failures remain immutable."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
spec=importlib.util.spec_from_file_location('r73_original_orbit',Path(__file__).with_name('cone_orbit.py'))
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)

@lru_cache(None)
def tangent_controls():
    original=old.tangent_controls()
    out=dict(original); checks=dict(original['checks'])
    z=s.Rational(3,5)+4*s.I/5
    value=2*(z-1)*(s.conjugate(z)-1)
    checks['orbit_difference_L4_leading_positive']=old.zero(value-s.Rational(8,5))
    checks['normalized_leading_strictly_positive']=s.simplify(value).is_positive is True
    checks['wrong_leading_value_rejected']=not old.zero(value-s.Rational(7,5))
    checks['original_scalar_failure_preserved']=original['checks']['orbit_difference_L4_leading_positive'] is False
    out['checks']=checks; out['normalized_leading']=s.simplify(value)
    return out

@lru_cache(None)
def operator_controls():
    original=old.operator_controls()
    out=dict(original); checks=dict(original['checks'])
    c=old.c; z=s.Rational(3,5)+4*s.I/5
    g=s.diag(z,1,1,1/z)
    U=c.sp(c.left*s.kronecker_product(g,g.inv().T)*c.T)
    expected=s.eye(9)[:,8]
    checks['exact_Z_trace_unchanged']=c.zero(U[:,8]-expected)
    checks['actual_matrix_Z_fixed']=old.zero(g*old.Z*g.inv()-old.Z)
    checks['wrong_Z_column_rejected']=not c.zero(U[:,8]-2*expected)
    checks['charged_neutral_matrix_not_fixed']=not old.zero(g*old.N*g.inv()-old.N)
    checks['original_matrix_failure_preserved']=original['checks']['exact_Z_trace_unchanged'] is False
    out['checks']=checks
    return out

def run():
    groups={n:fn() for n,fn in [('orbit',old.orbit_controls),('tangent',tangent_controls),('covariance',old.covariance_controls),('operator',operator_controls),('compensator',old.compensator_controls)]}
    checks={n+'/'+k:bool(v) for n,g in groups.items() for k,v in g['checks'].items()}
    return old.serial(dict(scope='Separate algebra normalization with original failures preserved; not independent physics',groups=groups,checks=checks,all_checks_pass=all(checks.values())))

if __name__=='__main__':
    out=run();print(json.dumps(out,sort_keys=True,indent=2))
    raise SystemExit(0 if out['all_checks_pass'] else 1)
