"""R30 follow-on: the actual source-C3 locus, not merely order-three holonomy.

Observed-label correction. Original R30 source, design and first runs stay frozen.
No interval geometry or PDE spectrum is newly certified here.
"""
import itertools
import json
import sympy as sp

# Landed beside the frozen producer before execution.
import importlib.util
from pathlib import Path


def local(name,filename):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(filename))
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rf=local('r30_c3_frozen_fermion','resolved_fermion.py')
wc=local('r30_c3_frozen_words','holonomy_equivariance_word_control.py')


def run():
    actions=wc.word_actions()['actions']
    R=sp.Matrix(next(x['h1_matrix'] for x in actions if x['k']==1 and x['e']==0))
    A=R**2
    B=A.T-sp.eye(2)
    denominator=abs(int(B.det()))
    fixed=[]
    for i,j in itertools.product(range(denominator),repeat=2):
        h=sp.Matrix([sp.Rational(i,denominator),sp.Rational(j,denominator)])
        if all(x.is_Integer for x in B*h):
            fixed.append(h)
    # The adjugate proves all torus fixed points lie in this denominator grid.
    adjugate=B.adjugate()*B-B.det()*sp.eye(2)
    rows=[]
    for h in fixed:
        xy=[sp.simplify(sp.expand_complex(sp.exp(2*sp.pi*sp.I*x))) for x in h]
        full=rf.glued(*xy,3,1)
        split=rf.glued(*xy,3,0)
        P=sp.simplify(sp.expand_complex(rf.hs.identities()['polynomial'].subs(dict(zip((rf.hs.X,rf.hs.Y),xy)))))
        rows.append(dict(h=list(h),character=list(map(str,xy)),P=P,
                         base=full['base'],resolved=full['betti'],split=split['betti'],
                         relative=full['relative']))
    original=sp.Matrix([sp.Rational(1,3),0])
    bad=B*original
    checks=dict(actual_order_three=A**3==sp.eye(2) and A!=sp.eye(2),
                full_fixed_torus=denominator==3 and adjugate==sp.zeros(2) and len(fixed)==3,
                original_order_three_character_not_fixed=any(not x.is_Integer for x in bad),
                fixed_nontrivial_resolved=all(r['P']==-2 and r['resolved']==[0,0,0,0]
                    and r['split']==[3,3,0,0] and r['relative']==[0,3,0,0]
                    for r in rows if any(r['h'])),
                fixed_trivial_resolved=next(r for r in rows if not any(r['h']))['resolved']==[1,2,1,0])
    return dict(checks=checks,A=A,rows=rows,original_fixed_residual=bad,
                correction='R30 original cube-root samples are not the source-C3-fixed orbit; this separate control evaluates that orbit.')


if __name__=='__main__':
    d=run()
    print(json.dumps(d,default=str,indent=2,sort_keys=True))
    if not all(d['checks'].values()):
        raise SystemExit(1)
