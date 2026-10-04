"""R87 actual E8 adjoint loop character, not empirical physics or selection."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent; SOURCE=HERE/'gluing_freedom.py'
if sha256(SOURCE.read_bytes()).hexdigest()!='501b3c87400f198035360dc760f19937a97c3d3bf6fd7801cecf325ae20f27f9':
    raise RuntimeError('Changed R86 primitives')
spec=importlib.util.spec_from_file_location('r87_retained_r86',SOURCE)
G=importlib.util.module_from_spec(spec); spec.loader.exec_module(G)
N=G.N; C=N.C; K=N.K
T_VALUES=(Fraction(1),Fraction(2),Fraction(3),Fraction(1,2))


def field(a):
    a=Fraction(a); return K.convert(a.numerator)/K.convert(a.denominator)


def roots():
    out=set()
    for i,j in combinations(range(8),2):
        for a,b in product((-2,2),repeat=2):
            v=[0]*8; v[i]=a; v[j]=b; out.add(tuple(v))
    for v in product((-1,1),repeat=8):
        if v.count(-1)%2==0:
            out.add(v)
    return out


def simple():
    e=[tuple(2*int(i==j) for j in range(8)) for i in range(8)]
    sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
    return [sub(e[i],e[i+1]) for i in range(4)]+[sub(e[6],e[7]),sub(e[5],e[6]),tuple(x+y for x,y in zip(e[6],e[7])),(-1,)*8]


def reps():
    f=[tuple(int(j==i)-int(j==i+1) for i in range(4)) for j in range(5)]
    neg=lambda w:tuple(-x for x in w)
    add=lambda a,b:tuple(x+y for x,y in zip(a,b))
    ten=[add(f[i],f[j]) for i,j in combinations(range(5),2)]
    return {'1':[(0,)*4],'5':f,'bar5':list(map(neg,f)),
            '10':ten,'bar10':list(map(neg,ten)),
            '24':[add(a,neg(b)) for i,a in enumerate(f) for j,b in enumerate(f) if i!=j]+[(0,)*4]*4}


BRANCHES=(('24','1'),('1','24'),('10','5'),('bar10','bar5'),('5','bar10'),('bar5','10'))


def roster(branches=BRANCHES):
    rs=reps(); return Counter(a+b for l,r in branches for a in rs[l] for b in rs[r])


def root_weights():
    ss=simple(); out=Counter(tuple(sum(x*y for x,y in zip(v,a))//4 for a in ss) for v in roots())
    out[(0,)*8]+=8; return out


def weight_value(w,vals):
    return product_values(vals[i]**sum(w[i:]) for i in range(4))


def product_values(values):
    out=Fraction(1)
    for z in values:
        out*=z
    return out


def torus_character(vals):
    return sum((mult*weight_value(w[4:],vals) for w,mult in root_weights().items()),Fraction(0))


def scalar_char(vals):
    a=sum(vals); b=sum(1/v for v in vals)
    c=sum(vals[i]*vals[j] for i,j in combinations(range(5),2))
    d=sum(1/(vals[i]*vals[j]) for i,j in combinations(range(5),2))
    return a*b+23+10*(a+b)+5*(c+d)


@lru_cache(None)
def parent_roots():
    rr=roots(); ss=simple(); actual=root_weights(); rs=roster()
    gram=[[sum(x*y for x,y in zip(a,b))//4 for b in ss] for a in ss]
    cartan=[[2 if i==j else -1 if abs(i-j)==1 else 0 for j in range(4)] for i in range(4)]
    wrong=BRANCHES[:4]+(('5','10'),('bar5','bar10'))
    central=lambda w:sum((i+1)*w[i] for i in range(4))
    kernel=[(a,b) for a,b in product(range(5),repeat=2) if all((a*central(w[:4])+b*central(w[4:]))%5==0 for w in actual)]
    vals=(Fraction(2),Fraction(3),Fraction(5),Fraction(7),Fraction(1,210))
    checks={'root_population240':len(rr)==240,'root_norm_two':all(sum(x*x for x in v)==8 for v in rr),
            'integral_actual_root_pairings':all(sum(x*y for x,y in zip(v,a))%4==0 for v in rr for a in ss),
            'all_simple_are_roots':all(a in rr for a in ss),
            'actual_a4_cartans':all([row[k*4:k*4+4] for row in gram[k*4:k*4+4]]==cartan for k in (0,1)),
            'a4_factors_orthogonal':not any(gram[i][j] for i in range(4) for j in range(4,8)),
            'whole_joint_weights_match':actual==rs and sum(actual.values())==248,
            'dimension_preserving_wrong_bars_rejected':sum(roster(wrong).values())==248 and actual!=roster(wrong),
            'center_kernel_matches':kernel==[(j,(-2*j)%5) for j in range(5)],
            'individual_factor_faithful':all((a==0)==(b==0) for a,b in kernel),
            'identity_character248':torus_character((Fraction(1),)*5)==248,
            'generic_torus_character_matches':torus_character(vals)==scalar_char(vals)}
    return {'checks':checks,'root_count':len(rr),'total_weights':sum(actual.values()),'center_kernel':kernel,
            'fixture_root_character':str(torus_character(vals))}


def end0(g):
    n=5; off=[(i,j) for i in range(n) for j in range(n) if i!=j]
    basis=[G.unit(n,i,j) for i,j in off]+[G.unit(n,i,i)-G.unit(n,4,4) for i in range(4)]
    gi=C.inv(g); cols=[]
    for e in basis:
        a=g*e*gi; aa=a.to_list(); coords=[aa[i][j] for i,j in off]+[aa[i][i] for i in range(4)]
        rebuilt=sum((v*b for v,b in zip(coords,basis)),C.zero(5,5,K))
        if G.trace(a)!=K.zero or not C.same(rebuilt,a):
            raise ValueError('Actual End0 action reconstruction failed')
        cols.append(coords)
    return N.rows_dm([list(r) for r in zip(*cols)],24)


def direct(g):
    hi=C.inv(g); a=G.trace(g); b=G.trace(hi)
    c=G.trace(N.exterior(g)); d=G.trace(N.exterior(hi)); e=G.trace(end0(g))
    return {'five':a,'dual_five':b,'ten':c,'dual_ten':d,'end0':e,
            'parent':e+K.convert(24)+10*(a+b)+5*(c+d)}


def poly_mul(a,b):
    out=[K.zero]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def exterior_coeffs(a,b):
    ts=[G.trace(a),G.trace(b)]; square=poly_mul(ts,ts)
    trsq=[G.trace(a*a),G.trace(a*b+b*a),G.trace(b*b)]
    return [(x-y)/K.convert(2) for x,y in zip(square,trsq)]


def polynomials(g0,g1,h0,h1):
    a=[G.trace(g0),G.trace(g1)]; b=[G.trace(h0),G.trace(h1)]
    c=exterior_coeffs(g0,g1); d=exterior_coeffs(h0,h1)
    p=poly_mul(a,b)
    p[0]+=K.convert(23)
    for i in range(3):
        p[i]+=5*(c[i]+d[i])+(10*(a[i]+b[i]) if i<2 else K.zero)
    return {'five':a,'dual_five':b,'ten':c,'dual_ten':d,'parent':p}


def evaluate(coeff,x):
    out=K.zero
    for z in reversed(coeff):
        out=out*x+z
    return out


def export_scalar(z):
    return N.export(N.rows_dm([[z]],1))


@lru_cache(None)
def case(ab):
    old=N.case(ab); left=old['_left']; right=old['_right']; a=left['x']; b=right['x']
    bb=b.to_list(); r0=N.rows_dm([[bb[i][j] if i<4 or j==4 else K.zero for j in range(5)] for i in range(5)],5)
    r1=b-r0; g0=a*r0; g1=a*r1; h0=C.inv(g0); h1=-h0*g1*h0
    polys=polynomials(g0,g1,h0,h1); p=polys['parent']; rows=[]
    all_direct=True; all_det=True; values={}
    for t in T_VALUES:
        x=K.one/(field(t)**5); actual=a*G.relative(right,N.s.Rational(t.numerator,t.denominator))['x']; inv=C.inv(actual); d=direct(actual)
        dchecks={k:evaluate(polys[k],x)==d[k] for k in polys}
        dchecks['end0_product_trace']=d['end0']==d['five']*d['dual_five']-K.one
        dchecks['actual_g_and_inverse']=C.same(actual,g0+x*g1) and C.same(inv,h0+x*h1)
        all_direct=all_direct and all(dchecks.values()); all_det=all_det and N.determinant(actual)==K.one
        values[str(t)]=export_scalar(d['parent']); rows.append({'t':str(t),'checks':dchecks,'parent':export_scalar(d['parent'])})
    derivative=p[1]+2*p[2]
    checks={'retained_actual_join':all(old['checks'].values()),'rank_one_update':C.rank(g1)==1,
            'nilpotent_update':C.same(g1*h0*g1,C.zero(5,5,K)),
            'both_inverse_constant':C.same(g0*h0,C.eye(5,K)) and C.same(h0*g0,C.eye(5,K)),
            'both_inverse_linear':C.same(g0*h1+g1*h0,C.zero(5,5,K)) and C.same(h0*g1+h1*g0,C.zero(5,5,K)),
            'both_inverse_quadratic':C.same(g1*h1,C.zero(5,5,K)) and C.same(h1*g1,C.zero(5,5,K)),
            'constant_determinant_one':N.determinant(g0)==K.one,'sample_determinants_one':all_det,
            'exterior_quadratic_coefficients_zero':polys['ten'][2]==polys['dual_ten'][2]==K.zero,
            'parent_character_nonconstant':any(z for z in p[1:]),
            'direct_actions_match_polynomial':all_direct,'parent_separates_one_two':values['1']!=values['2'],
            'dual_character_same':direct(a*right['x'])['parent']==direct(C.inv(a*right['x']))['parent']}
    return {'character':list(ab),'checks':checks,'parent_degree':2 if p[2] else 1 if p[1] else 0,
            'derivative_at_X_one':export_scalar(derivative),'derivative_zero':derivative==K.zero,
            'samples':rows,'witness':{'left_x':N.export(a),'right_x':N.export(b),'g0':N.export(g0),'g1':N.export(g1),
                                     'h0':N.export(h0),'h1':N.export(h1),
                                     'polynomials':{k:[export_scalar(z) for z in v] for k,v in polys.items()}}}


@lru_cache(None)
def fixtures():
    i=C.eye(5,K); a=i+G.unit(5,0,4); b=i+G.unit(5,4,0)
    changed=G.scale(2)*b*C.inv(G.scale(2)); sc=field(2)*i
    diagonal=N.rows_dm([[field((2,3,5,7,Fraction(1,210))[j]) if j==k else K.zero for j in range(5)] for k in range(5)],5)
    conj=(i+G.unit(5,0,1))*diagonal*C.inv(i+G.unit(5,0,1))
    update=G.unit(5,0,1); h1=-update; bad=G.unit(5,0,0)+G.unit(5,1,1)
    cs=polynomials(i,update,i,h1)
    checks={'identity_parent248':direct(i)['parent']==K.convert(248),
            'relative_parent_trace_changes':direct(a*b)['parent']!=direct(a*changed)['parent'],
            'scalar_relative_bend_invisible':C.same(sc*b*C.inv(sc),b),
            'actual_conjugation_invariant':direct(diagonal)['parent']==direct(conj)['parent'],
            'inverse_character_not_complete_classifier':direct(diagonal)['parent']==direct(C.inv(diagonal))['parent'],
            'omitted_dual_sector_rejected':direct(diagonal)['parent']-10*G.trace(C.inv(diagonal))!=direct(diagonal)['parent'],
            'rank_one_inverse_positive':C.same(update*update,C.zero(5,5,K)),
            'rank_two_inverse_shortcut_rejected':not C.same(bad*bad,C.zero(5,5,K)),
            'constant_parent_polynomial_control':cs['parent']==[K.convert(248),K.zero,K.zero],
            'degree_two_polynomial_positive':evaluate([K.one,K.one,K.one],field(2))!=evaluate([K.one,K.one,K.one],K.one)}
    return {'checks':checks}


def run():
    out=[]
    def emit(group,d):
        out.append(d); print(json.dumps({'group':group,**d},sort_keys=True),flush=True)
    emit('roots',parent_roots()); emit('fixtures',fixtures())
    for ab in N.CHARS:
        emit('case',case(ab))
    checks=[z for d in out for z in d['checks'].values()]+[z for d in out for row in d.get('samples',[]) for z in row['checks'].values()]
    result={'all':all(checks),'passed':sum(checks),'total':len(checks),'scope':'exact actual parent gauge-invariant character; no selection or observed physics'}
    print(json.dumps(result,sort_keys=True),flush=True); return result


if __name__=='__main__':
    raise SystemExit(0 if run()['all'] else 1)
