"""F19 exact Q(q) witnesses, full-algebra determinant and specialization gates."""
from functools import lru_cache,reduce
from pathlib import Path
import importlib.util
import json
import sympy as s

path=Path(__file__).parent.parent/'projective_cover_characters_2026_09_25'/'verify.py'
spec=importlib.util.spec_from_file_location('f19_f17',path)
p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
v=p.v
q=v.f10.q
K=s.QQ.frac_field(q)


@lru_cache(None)
def generators():
    return tuple(v.dm(a,K) for a in v.f10.generators())


def primitive_polynomial_matrix(a):
    entries=[s.cancel(x) for x in a.to_Matrix()]
    den=s.lcm_list([s.denom(x) for x in entries])
    polynomials=[s.Poly(s.cancel(den*x),q,domain=s.QQ) for x in entries]
    common=reduce(s.gcd,polynomials)
    if common.is_zero: raise ValueError('zero candidate')
    return s.Matrix(a.shape[0],a.shape[1],[s.cancel(x.as_expr()/common.as_expr()) for x in polynomials])


def stripped_roots(poly):
    poly=s.Poly(poly,q,domain=s.QQ)
    if poly.is_zero: raise ValueError('zero polynomial has no finite root count')
    removed={}
    for value in (0,1):
        linear=s.Poly(q-value,q,domain=s.QQ); multiplicity=0
        while poly.eval(value)==0:
            poly=poly.exquo(linear); multiplicity+=1
        removed[str(value)]=multiplicity
    return dict(excluded_multiplicities=removed,remainder=s.factor(poly.as_expr()),
                positive_roots=int(poly.count_roots(0,s.oo)))


def domain_certificate(expr):
    expr=s.cancel(expr)
    if expr==0: return dict(identically_zero=True,valid=False)
    n,d=s.fraction(expr); numerator=stripped_roots(n); denominator=stripped_roots(d)
    return dict(identically_zero=False,numerator=numerator,denominator=denominator,
                valid=numerator['positive_roots']==denominator['positive_roots']==0)


def matrix_pole_certificate(matrix):
    denominators=sorted(set(s.denom(s.cancel(x)) for x in matrix),key=str)
    counts=[stripped_roots(d) for d in denominators]
    return dict(denominators=denominators,root_certificates=counts,
                valid=all(c['positive_roots']==0 for c in counts))


@lru_cache(None)
def intertwiner(name):
    if name not in ('theta','thetaT'): raise ValueError('outside declared candidates')
    rho=generators(); target=tuple(a.inv().transpose() for a in rho)
    source=tuple(p.word(w,rho) for w in p.MAPS[name])
    columns=[]
    for i in range(4):
        for j in range(4):
            e=s.zeros(4); e[i,j]=1; e=v.dm(e,K)
            columns.append(v.stack(*(p.flatten(a*e-e*b) for a,b in zip(target,source))))
    equations=v.cat(*columns); kernel=v.kernel(equations)
    if kernel.shape[1]!=1: raise ValueError(('unexpected generic dimension',name,kernel.shape[1]))
    primitive=primitive_polynomial_matrix(p.unvec(v.col(kernel,0)))
    jj=v.dm(primitive,K); det=s.factor(K.to_sympy(jj.det()))
    residuals=tuple(a*jj-jj*b for a,b in zip(target,source))
    return dict(matrix=primitive,J=jj,equations=equations,dimension=kernel.shape[1],determinant=det,
                domain=domain_certificate(det),residuals=residuals)


@lru_cache(None)
def word_algebra():
    rho=generators(); column=v.cat(*(p.flatten(p.word(w,rho)) for w in p.BASIS_WORDS))
    determinant=s.factor(K.to_sympy(column.det()))
    return dict(column=column,words=p.BASIS_WORDS,determinant=determinant,domain=domain_certificate(determinant))


@lru_cache(None)
def peripheral():
    rho=generators(); lam=p.word(p.LONG,rho)
    frame=v.dm(v.f10.cusp_conjugator(),K)
    normal=tuple(v.dm(a,K) for a in v.f10.normal_form())
    det=s.factor(K.to_sympy(frame.det()))
    return dict(frame=frame,determinant=det,domain=domain_certificate(det),finite=matrix_pole_certificate(frame.to_Matrix()),
                residues=(rho[0]*frame-frame*normal[0],lam*frame-frame*normal[1]))


def specialize(a,middle,embedding=1):
    k,value,_,_=v.context(middle,embedding)
    return v.dm(a.subs(q,value),k)


def report():
    out={}
    for name in ('theta','thetaT'):
        a=intertwiner(name)
        out[name]=dict(matrix=a['matrix'].tolist(),dimension=a['dimension'],determinant=a['determinant'],
                       domain=a['domain'],identities=all(r.is_zero_matrix for r in a['residuals']))
    b=word_algebra(); f=peripheral()
    out['word_algebra']=dict(words=b['words'],determinant=b['determinant'],domain=b['domain'])
    out['peripheral']=dict(determinant=f['determinant'],domain=f['domain'],finite=f['finite'],identities=all(r.is_zero_matrix for r in f['residues']))
    out['all_domain_gates']=all(out[x]['domain']['valid'] for x in out) and f['finite']['valid']
    return out


if __name__=='__main__':
    print(json.dumps(report(),default=str,sort_keys=True),flush=True)
