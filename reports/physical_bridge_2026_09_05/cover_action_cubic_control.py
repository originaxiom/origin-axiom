"""R58 separately sealed nonzero comparator; preserves the original run."""
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as s

spec=importlib.util.spec_from_file_location('r58_original',Path(__file__).with_name('cover_action.py'))
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def wedge_coefficient(mats):
    out=0
    for p in itertools.permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        out += (-1)**inv*s.trace(mats[p[0]]*mats[p[1]]*mats[p[2]])
    return s.simplify(out)


def run():
    _, aa, bb, _=old.fixtures()
    h=s.diag(1,-1); e=s.Matrix([[0,1],[0,0]]); f=e.T
    triples=[((i+1)*h,e,f) for i in range(3)]
    local=sum(s.trace(a*old.bracket(b,c)) for a,b,c in triples)
    pushed=[s.diag(*(t[j] for t in triples)) for j in range(3)]
    summed=[sum((t[j] for t in triples),s.zeros(2)) for j in range(3)]
    transported=s.trace(pushed[0]*old.bracket(pushed[1],pushed[2]))
    merged=s.trace(summed[0]*old.bracket(summed[1],summed[2]))
    wedge=wedge_coefficient(pushed)
    checks={
        'original_fixture_was_zero':all(old.equal(s.trace(a*b*a),0) for a,b in zip(aa,bb)),
        'nonzero_sheet_cubic':local==12,
        'faithful_transport':transported==local and transported!=0,
        'wrong_merge_opposite':merged==108 and merged!=transported,
        'nonzero_wedge_cubic':wedge==36 and wedge==sum(wedge_coefficient(t) for t in triples),
    }
    checks={k:bool(v) for k,v in checks.items()}
    return dict(checks=checks,passed=sum(checks.values()),total=len(checks),
        all_checks_pass=all(checks.values()),sheet_cubic=int(local),
        transported_cubic=int(transported),wrong_merged_cubic=int(merged),
        wedge_coefficient=int(wedge),physical_coupling_predicted=False)


if __name__=='__main__':
    d=run(); print(json.dumps(d,sort_keys=True))
    raise SystemExit(0 if d['all_checks_pass'] else 1)
