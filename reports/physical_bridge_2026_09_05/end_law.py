"""R60 exact controls; no physical spectrum or global-domain certificate."""
import hashlib
import itertools
import json
import math
import subprocess
import sys
from pathlib import Path

import sympy as s

I = (1, 0, 0, 1)


def mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def order(a):
    b = I
    for n in range(1, 13):
        b = mul(b, a)
        if b == I:
            return n
    raise ValueError("not finite of order at most 12")


def line(v):
    a, b = map(int, v)
    g = math.gcd(a, b)
    if not g:
        raise ValueError("zero is not a line")
    a, b = a//g, b//g
    return (-a, -b) if a < 0 or (a == 0 and b < 0) else (a, b)


def image(a, v):
    return line((a[0]*v[0]+a[1]*v[1], a[2]*v[0]+a[3]*v[1]))


def eigenlines(a):
    A = s.Matrix(2, 2, a)
    out = set()
    for ev in (1, -1):
        for v in (A-ev*s.eye(2)).nullspace():
            den = s.ilcm(*[x.q for x in v])
            out.add(line(den*v))
    return out


def lattice():
    """Enumerate ALL subsets, not B1504's two-generator enumeration."""
    rows = []
    for name, r, f in (("D4", (0,-1,1,0), (1,0,0,-1)),
                       ("D6", (1,-1,1,0), (0,1,1,0))):
        powers, p = [], I
        for _ in range(order(r)):
            powers.append(p)
            p = mul(p, r)
        group = sorted(set(powers + [mul(x, f) for x in powers]))
        index = {a: i for i, a in enumerate(group)}
        table = [[index[mul(a,b)] for b in group] for a in group]
        identity = index[I]
        candidates = set().union(*(eigenlines(a) for a in group if a not in (I, (-1,0,0,-1))))
        for mask in range(1 << len(group)):
            if not (mask >> identity) & 1:
                continue
            ids = [i for i in range(len(group)) if (mask >> i) & 1]
            if any(not (mask >> table[i][j]) & 1 for i in ids for j in ids):
                continue
            H = [group[i] for i in ids]
            has_line = any(all(image(a,v) == v for a in H) for v in candidates)
            rotation = any(order(a) in (3,4,6) for a in H)
            rows.append(dict(ambient=name, size=len(H), has_line=has_line, rotation=rotation))
    return rows


def rank_union(A, B):
    return A.row_join(B).rank()


def domains():
    H = s.Matrix([[2,-1],[-1,2]])
    J = s.Matrix([[0,1],[-1,0]])
    R = s.Matrix([[0,-1],[1,-1]])
    Green = s.zeros(4)
    Green[:2,2:] = H
    Green[2:,:2] = -H
    R4 = s.diag(R,R)
    bases = (s.zeros(2,0), s.eye(2), s.Matrix([1,0]))
    records = []
    for W in bases:
        perp = s.Matrix.hstack(*(W.T*H).nullspace()) if W.cols else s.eye(2)
        if not (W.T*H).nullspace():
            perp = s.zeros(2,0)
        D = s.diag(W,perp)
        dualcols = (W.T*J).nullspace()
        dual = s.Matrix.hstack(*dualcols) if dualcols else s.zeros(2,0)
        records.append(dict(dim_W=W.cols, boundary_dim=D.cols,
                            isotropic=D.T*Green*D == s.zeros(D.cols),
                            rotation_invariant=rank_union(D,R4*D)==D.rank(),
                            poincare_self_dual=W.cols==dual.cols and rank_union(W,dual)==W.cols))
    wrong = s.Matrix([[1,0],[0,0],[0,1],[0,0]])
    return records, wrong.T*Green*wrong != s.zeros(2), R.T*H*R == H


def marking_and_slopes():
    L=s.Matrix([[1,1],[0,1]])
    R=s.Matrix([[1,0],[1,1]])
    e=s.Matrix([1,0])
    rotation=(0,-1,1,-1)
    roots={(1,0),(0,1),(1,1)}
    orbit={line((1,3))}
    for _ in range(2):
        orbit |= {image(rotation,v) for v in orbit}
    H=s.Matrix([[2,-1],[-1,2]])
    checks = dict(oriented_conjugacy=L.inv()*L*R*L == R*L and L.det()==1,
                  nonroot_orbit=len(orbit)==3 and not orbit & roots,
                  nonroot_length=all((s.Matrix(v).T*H*s.Matrix(v))[0]==14 for v in orbit),
                  root_orbit={image(rotation,v) for v in roots} == roots,
                  marking_changes_line=line(e)!=line(R*e),
                  marking_equivariance=all(line(g*B*e)==line(g*(B*e))
                      for g in (L,R,L*R) for B in (s.eye(2),L,R)))
    return checks, sorted(orbit)


def wedge(A,B):
    out={}
    for ia,a in A.items():
        for ib,b in B.items():
            if set(ia)&set(ib):
                continue
            sign=(-1)**sum(i>j for i in ia for j in ib)
            key=tuple(sorted(ia+ib))
            v=sign*a*b
            out[key]=out[key]+v if key in out else v
    return out


def add(*forms):
    out={}
    for f in forms:
        for k,v in f.items():
            out[k]=out[k]+v if k in out else v
    return out


def scale(f,c):
    return {k:c*v for k,v in f.items()}


def exterior(f,xyz):
    out={}
    for j,x in enumerate(xyz):
        for k,v in f.items():
            if j in k:
                continue
            idx=tuple(sorted((j,)+k))
            value=(-1)**sum(i<j for i in k)*v.diff(x)
            out[idx]=out[idx]+value if idx in out else value
    return out


def trace(f):
    return {k:s.expand(s.trace(v)) for k,v in f.items()}


def action():
    x,y,z,t=s.symbols('x y z t')
    xyz=(x,y,z)
    A={(0,):s.Matrix([[x,1],[0,-x]]), (1,):s.Matrix([[0,y],[1,0]]),
       (2,):s.Matrix([[z,0],[1,-z]])}
    eta={(0,):s.diag(1,-1), (1,):s.Matrix([[0,0],[x,0]]), (2,):s.diag(y,-y)}
    At=add(A,scale(eta,t))
    cubic=trace(wedge(A,wedge(A,A)))[(0,1,2)]
    CS=trace(add(wedge(At,exterior(At,xyz)),scale(wedge(At,wedge(At,At)),s.Rational(2,3))))
    variation=s.diff(CS[(0,1,2)],t).subs(t,0).expand()
    curvature=add(exterior(A,xyz),wedge(A,A))
    bulk=2*trace(wedge(eta,curvature))[(0,1,2)]
    boundary=exterior(trace(wedge(A,eta)),xyz)[(0,1,2)]
    u,v,k=s.symbols('u v k')
    theta=s.Matrix([v,-u])
    graph=lambda form:s.expand(form[0].subs(v,-k*u)-k*form[1].subs(v,-k*u))
    total=theta+s.Matrix([s.diff(u*v+k*u*u,u),s.diff(u*v+k*u*u,v)])
    checks=dict(nonabelian_variation=s.expand(variation-bulk+boundary)==0,
                wrong_boundary_sign_rejected=s.expand(variation-bulk-boundary)!=0,
                cubic_nonzero=cubic!=0,
                omitted_cubic_rejected=s.expand(variation-2*trace(wedge(eta,exterior(A,xyz)))[(0,1,2)]+boundary)!=0,
                boundary_symplectic=s.diff(theta[1],u)-s.diff(theta[0],v)==-2,
                graph_stationarity=graph(total)==0,
                different_potentials_different_graphs=(-u)!=(-2*u),
                wrong_graph_rejected=s.expand(total[0].subs(v,k*u))!=0)
    return checks,dict(bulk_variation=str(variation), boundary_derivative=str(s.expand(boundary)),
                       cubic=str(cubic), graph_equation=str(total[0]))


def metric():
    rho=s.symbols('rho',positive=True)
    cusp=s.diag(rho**-2,rho**2,rho**2)
    cone=s.diag(1,rho**2,rho**2)
    tang=lambda g:s.simplify(s.sqrt(g.det())*g.inv()[1,1])
    p=s.symbols('p',real=True)
    return dict(cusp_density=tang(cusp)==1/rho,
                cone_density=tang(cone)==1,
                cone_constant_integrable=s.integrate(tang(cone),(rho,0,1))==1,
                cusp_constant_not_integrable=s.integrate(tang(cusp),(rho,0,1))==s.oo,
                cusp_distance_infinite=s.integrate(s.sqrt(cusp[0,0]),(rho,0,1))==s.oo,
                cone_distance_finite=s.integrate(s.sqrt(cone[0,0]),(rho,0,1))==1,
                norms_not_identified=s.simplify(tang(cusp)*rho**(2*p)-tang(cone)*rho**(2*p))!=0)


def run():
    rows=lattice()
    records, bad, invariant=domains()
    checks,orbit=marking_and_slopes()
    checks.update(lattice_count=len(rows)==26, lattice_rotations=sum(r['rotation'] for r in rows)==7,
                  lattice_equivalence=all(r['rotation'] != r['has_line'] for r in rows),
                  doubled_domains_maximal_isotropic=all(r['boundary_dim']==2 and r['isotropic'] for r in records),
                  extreme_domains_invariant=all(r['rotation_invariant'] for r in records[:2]),
                  extremes_not_poincare_self_dual=not any(r['poincare_self_dual'] for r in records[:2]),
                  line_poincare_self_dual=records[2]['poincare_self_dual'],
                  wrong_domain_rejected=bad, hexagonal_metric_preserved=invariant)
    ac, detail=action()
    checks.update(ac)
    checks.update(metric())
    return dict(scope='Exact local algebra and norm controls, not a physical completion',
                checks={k:bool(v) for k,v in checks.items()},
                all_checks_pass=all(checks.values()), subgroup_entries=rows,
                cauchy_domains=records, nonroot_orbit=orbit, action=detail)


def foreign_lemma():
    manifest=json.loads(Path(__file__).with_name('END_LAW_INPUTS.json').read_text())
    entry=next(r for r in manifest['inputs'] if r['path'].endswith('/end_choice.py'))
    source=subprocess.check_output(['git','show',entry['commit']+':'+entry['path']])
    if hashlib.sha256(source).hexdigest()!=entry['sha256']:
        raise ValueError('foreign producer digest mismatch')
    namespace={'__name__':'b1504_replay','__file__':str(Path.cwd()/entry['path'])}
    exec(compile(source,entry['path'],'exec'),namespace)
    rows=namespace['lemma']()
    return dict(scope='Unchanged B1504 lattice lemma only, not its geometric census',
                entries=len(rows), rotations=sum(r['rotation'] for r in rows),
                all_checks_pass=all(r['rotation'] != r['common_line'] for r in rows))


if __name__=='__main__':
    data=foreign_lemma() if '--foreign-lemma' in sys.argv else run()
    print(json.dumps(data,indent=2))
    sys.exit(0 if data['all_checks_pass'] else 1)
