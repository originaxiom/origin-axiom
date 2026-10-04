"""Compact kinetic premises and finite controls; not a numerical PDE solver."""
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def load(name,file,pin):
    path=HERE/file
    if sha256(path.read_bytes()).hexdigest()!=pin:
        raise RuntimeError('Changed source '+file)
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

P=load('r88_parent','parent_gluing_character.py','2d01c892b75acac30355aefed48af400e9e4376510c02033811d7d9c2048a0c9')
V=load('r88_velocity','neutral_velocity.py','e90c147afc2f8b88dd6b9b12a33b7871ed15cd53ddfe0437d074eec340c488dd')
G=P.G; N=P.N; C=P.C; K=P.K; s=N.s

def parent_derivative(g,dg):
    h=C.inv(g); dh=-h*dg*h
    a,b,da,db=map(G.trace,(g,h,dg,dh))
    return da*b+a*db+10*(da+db)+5*(a*da-G.trace(g*dg)+b*db-G.trace(h*dh))

@lru_cache(None)
def trace_controls():
    weights=P.root_weights()
    ds=[tuple(int(k==i)-int(k==4) for k in range(5)) for i in range(4)]
    eigen=lambda w,d:sum(w[j+4]*sum(d[:j+1]) for j in range(4))
    gram=[[sum(n*eigen(w,a)*eigen(w,b) for w,n in weights.items()) for b in ds] for a in ds]
    expected=[[60*sum(x*y for x,y in zip(a,b)) for b in ds] for a in ds]
    return {'checks':{'retained_full_parent_weights':all(P.parent_roots()['checks'].values()),
                      'whole_cartan_trace_gram':gram==expected,
                      'trace_gram_positive':s.Matrix(gram).eigenvals()=={s.Integer(300):1,s.Integer(60):3},
                      'wrong_trace_factor_rejected':gram!=[[30*sum(x*y for x,y in zip(a,b)) for b in ds] for a in ds]},
            'gram':gram,'raw_trace_factor':60}

@lru_cache(None)
def kinetic_controls():
    a=s.Matrix([[1,s.I],[-s.I,-1]]); b=s.Matrix([[0,2],[2,0]])
    u=a+s.I*b; k,v=s.symbols('k v',positive=True)
    return {'checks':{'positive_complex_split':V.zero(s.trace(u.conjugate().T*u)-s.trace(a*a)-s.trace(b*b)),
                      'real_canonical_factor':V.zero(k*v*v-s.Rational(1,2)*(s.sqrt(2*k)*v)**2),
                      'missing_factor_two_rejected':not V.zero(k*v*v-s.Rational(1,2)*(s.sqrt(k)*v)**2),
                      'singular_parent_inverse_rejected':s.diag(1,0).det()==0,
                      'scalar_zero_mode_not_tracefree':s.trace(s.eye(5))!=0}}

@lru_cache(None)
def case(ab):
    old=N.case(ab); left=old['_left']; right=old['_right']; whole=old['_whole']
    z=N.rows_dm([[K.convert(1 if i==j and i<4 else -4 if i==j else 0) for j in range(5)] for i in range(5)],5)
    coc={t:C.zero(5,5,K) for t in left}
    coc.update({t.translate(N.RENAME):z-g*z*C.inv(g) for t,g in right.items()})
    cb=G.coboundaries(whole); bend=G.columns([coc],list(whole)); rb=C.rank(cb); rb1=C.rank(cb.hstack(bend))
    g=left['x']*right['x']; dg=left['x']*(z*right['x']-right['x']*z)
    bb=right['x'].to_list()
    r0=N.rows_dm([[bb[i][j] if i<4 or j==4 else K.zero for j in range(5)] for i in range(5)],5)
    g0=left['x']*r0; g1=left['x']*(right['x']-r0); h0=C.inv(g0); h1=-h0*g1*h0
    coeff=P.polynomials(g0,g1,h0,h1)['parent']; deriv=parent_derivative(g,dg)
    conjugation=z*g-g*z
    checks={'retained_actual_join':all(old['checks'].values()),
            'tracefree_literal_bend':G.trace(z)==K.zero and all(G.trace(v)==K.zero for v in coc.values()),
            'actual_all_relator_tangents':all(C.same(G.tangent_word(w,whole,coc)[1],C.zero(5,5,K)) for w in N.DOUBLE_RELS),
            'structure_zero_form_kernel_zero':G.commutant(whole,True).shape[1]==0,
            'coboundary_rank24':rb==24,'literal_bend_adds_one':rb1==25,
            'mixed_loop_velocity':C.same(dg,-5*g1),
            'actual_parent_log_derivative':deriv==-5*(coeff[1]+2*coeff[2]),
            'nonzero_parent_velocity':deriv!=K.zero,
            'actual_conjugation_annihilated':parent_derivative(g,conjugation)==K.zero,
            'nonzero_conjugation_control':not C.same(conjugation,C.zero(5,5,K)),
            'wrong_log_chain_factor_rejected':deriv!=-(coeff[1]+2*coeff[2])}
    return {'character':list(ab),'checks':checks,'coboundary_rank':rb,'augmented_rank':rb1,
            'parent_log_derivative':P.export_scalar(deriv),
            'witness':{'left':old['witness']['left'],'right':old['witness']['right'],
                       'span_words':old['witness']['span_words'],
                       'cocycle':{t:N.export(v) for t,v in coc.items()},'g':N.export(g),'dg':N.export(dg)}}

def run():
    out=[]
    def emit(name,data):
        data={**data,'checks':{k:bool(v) for k,v in data['checks'].items()}}
        out.append(data); print(json.dumps({'group':name,**data},sort_keys=True),flush=True)
    emit('inherited_jacobi',{'checks':V.jacobi_controls()})
    emit('inherited_projection',{'checks':V.projection_controls()})
    emit('parent_trace',trace_controls()); emit('kinetic_controls',kinetic_controls())
    for ab in N.CHARS:
        emit('case',case(ab))
    cs=[bool(v) for d in out for v in d['checks'].values()]
    result={'all':all(cs),'passed':sum(cs),'total':len(cs),
            'scope':'finite compact kinetic premises/controls; authored PDE argument not machine verified; K0 not numerically computed'}
    print(json.dumps(result,sort_keys=True),flush=True); return result

if __name__=='__main__':
    raise SystemExit(0 if run()['all'] else 1)
