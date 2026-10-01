"""R71 separately sealed charpoly-generator repair; initial failures retained."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

spec=importlib.util.spec_from_file_location('r71_channel_original',Path(__file__).with_name('cone_channel.py'))
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
s=old.s
charge_controls,window_controls,limit_window,schur_controls,integration_controls=(
    old.charge_controls,old.window_controls,old.limit_window,old.schur_controls,old.integration_controls)

@lru_cache(None)
def scalar_controls():
    out=old.scalar_controls()
    checks=dict(out['checks'])
    x,y,w,a=s.symbols('xi zeta mass a',real=True)
    e=old.ex*(s.I*x)+old.ey*(w+s.I*y)
    l=e+e.H
    A=old.blocks(old.M,-l,-l,-old.M)
    polynomial=A.charpoly(a)
    lam=x*x+y*y+w*w
    target=((a*a-lam)**2-a*a)**2
    aligned=target.subs(a,polynomial.gen)
    checks['independent_scalar_charpoly']=old.zero(polynomial.as_expr()-aligned)
    checks['retained_original_generator_failure']=not out['checks']['independent_scalar_charpoly']
    checks['library_generator_assumptions_differ']=polynomial.gen!=a and str(polynomial.gen)==str(a)
    wrong=aligned.subs(lam,lam+1)  # use explicit construction to avoid composite substitution ambiguity
    wrong=((polynomial.gen**2-lam-1)**2-polynomial.gen**2)**2
    checks['wrong_mass_still_fails']=not old.zero(polynomial.as_expr()-wrong)
    fixture={x:2,y:3,w:1}
    av=5
    direct=(av*s.eye(8)-A.subs(fixture)).det()
    checks['independent_numeric_determinant']=direct==aligned.subs(fixture).subs(polynomial.gen,av)
    return dict(checks=checks,charpoly=old.s.factor(aligned),threshold=s.Rational(3,4),
                generator_normalization='actual PurePoly.gen; no changed eigenvalue target')

def run():
    groups={name:fn() for name,fn in [('charge',charge_controls),('window',window_controls),
        ('scalar',scalar_controls),('schur',schur_controls),('integration',integration_controls)]}
    checks={name+'/'+k:bool(v) for name,g in groups.items() for k,v in g['checks'].items()}
    summary={name:{k:v for k,v in g.items() if k!='B'} for name,g in groups.items()}
    return old.serial(dict(groups=summary,checks=checks,all_checks_pass=all(checks.values()),
        scope='Generator repair only; original two failures retained, no graph admission or physical spectrum'))

if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)

