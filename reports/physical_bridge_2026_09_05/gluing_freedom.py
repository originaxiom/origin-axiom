"""R86 exact relative-gluing and neutral-class witnesses, not a physics census."""
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'joined_background.py'
if sha256(SOURCE.read_bytes()).hexdigest()!='f1d6bfb9e998a3306ddb41757c9356f4e99757a93ebbfc474e84be9d49bee4c7':
    raise RuntimeError('Changed R85 native primitives')
spec=importlib.util.spec_from_file_location('r86_retained_r85',SOURCE)
N=importlib.util.module_from_spec(spec); spec.loader.exec_module(N)
C=N.C; K=N.K


def unit(n,i,j):
    a=[[K.zero for _ in range(n)] for _ in range(n)]; a[i][j]=K.one
    return N.rows_dm(a,n)


def trace(a):
    return sum((a.to_list()[i][i] for i in range(a.shape[0])),K.zero)


def commutant(gens,traceless=False):
    n=next(iter(gens.values())).shape[0]; cols=[]
    for i in range(n):
        for j in range(n):
            e=unit(n,i,j)
            col=[z for g in gens.values() for z in N.flat(g*e-e*g)]
            if traceless:
                col.append(trace(e))
            cols.append(col)
    return C.kernel(N.rows_dm([list(r) for r in zip(*cols)],n*n))


def matrices(ker,n):
    a=ker.to_list()
    return [N.rows_dm([[a[i*n+j][k] for j in range(n)] for i in range(n)],n)
            for k in range(ker.shape[1])]


def tangent_word(w,gens,cocycles):
    n=next(iter(gens.values())).shape[0]; p=C.eye(n,K); u=C.zero(n,n,K)
    inverses={t:C.inv(g) for t,g in gens.items()}
    for ch in w:
        t=ch.lower(); g=gens[t]; v=cocycles[t]
        if ch.isupper():
            g=inverses[t]; v=-g*v*gens[t]
        u=u+p*v*C.inv(p); p=p*g
    return p,u


def columns(cs,names):
    return N.rows_dm([list(r) for r in zip(*[[v for t in names for v in N.flat(c[t])] for c in cs])],len(cs))


def coboundaries(gens):
    n=next(iter(gens.values())).shape[0]
    cs=[]
    for i in range(n):
        for j in range(n):
            e=unit(n,i,j)
            cs.append({t:g*e*C.inv(g)-e for t,g in gens.items()})
    return columns(cs,list(gens))


def scale(t):
    z=K.convert(t)
    return N.rows_dm([[z if i==j and i<4 else K.one/(z**4) if i==j else K.zero
                       for j in range(5)] for i in range(5)],5)


def relative(right,t):
    a=scale(t); ia=C.inv(a)
    return {name:a*g*ia for name,g in right.items()}


def whole(left,right):
    return dict(left,**{t.translate(N.RENAME):g for t,g in right.items()})


def relators(gens):
    return all(C.same(C.field_word(w,gens)[0],C.eye(5,K)) for w in N.DOUBLE_RELS)


def parabolic(gens,upper):
    if upper:
        return all(not z for g in gens.values() for z in g.to_list()[4][:4])
    return all(not g.to_list()[i][4] for g in gens.values() for i in range(4))


def trace_witness(left,right,lwords,rwords):
    for u in lwords:
        a=C.field_word(u,left)[0]; aa=a.to_list()
        for v in rwords:
            b=C.field_word(v,right)[0]; bb=b.to_list()
            coeff=sum((aa[i][4]*bb[4][i] for i in range(4)),K.zero)
            if coeff:
                constant=trace(a*b)-coeff
                values={str(t):trace(a*C.field_word(v,relative(right,t))[0]) for t in (1,2,3)}
                return {'left_word':u,'right_word':v,
                        'coefficient':N.export(N.rows_dm([[coeff]],1)),
                        'constant':N.export(N.rows_dm([[constant]],1)),
                        'values':{t:N.export(N.rows_dm([[z]],1)) for t,z in values.items()},
                        'formula_pass':all(z==constant+coeff/(K.convert(int(t))**5) for t,z in values.items()),
                        'separates_one_two':values['1']!=values['2']}
    return None


@lru_cache(None)
def case(ab):
    old=N.case(ab); left=old['_left']; right=old['_right']; gs=old['_whole']
    ls=N.span(left); rs=N.span(right); names=list(gs)
    peripheral={'z':left['z'],'l':C.field_word('yXYx',left)[0]}
    kc=commutant(peripheral); kt=commutant(peripheral,True); zs=matrices(kt,5)
    coc=[]
    for z in zs:
        one={t:C.zero(5,5,K) for t in left}
        one.update({t.translate(N.RENAME):z-g*z*C.inv(g) for t,g in right.items()})
        coc.append(one)
    q=columns(coc,names); b=coboundaries(gs)
    rb=C.rank(b); rq=C.rank(q); joined=C.rank(b.hstack(q))
    changed=whole(left,relative(right,2)); alg=N.span(changed)
    witness=trace_witness(left,right,ls['words'],rs['words'])
    s=N.rows_dm([[K.convert(int(i==j)) for j in range(5)] for i in range(5)],5)
    # Explicit controls do not substitute for the tangent quotient test.
    scalar_coc=[s-g*s*C.inv(g) for g in right.values()]
    # S itself is exported by R85; evaluate its field entries without a new matching choice.
    match=N.match(peripheral['z'],peripheral['l'])['s']
    checks={'retained_r85_admission':all(old['checks'].values()),
            'matching_block_diagonal':not any(match.to_list()[i][4] or match.to_list()[4][i] for i in range(4)),
            'left_upper_shape':parabolic(left,True),'right_lower_shape':parabolic(right,False),
            'left_parabolic_dimension21':ls['dimension']==21,'right_parabolic_dimension21':rs['dimension']==21,
            'piece_scalar_commutants':commutant(left).shape[1]==commutant(right).shape[1]==1,
            'peripheral_centralizer5':kc.shape[1]==5,'traceless_peripheral_centralizer4':kt.shape[1]==4,
            'exported_zs_traceless':all(trace(z)==K.zero for z in zs),
            'bend_tangent_relators':all(C.same(tangent_word(w,gs,c)[1],C.zero(5,5,K)) for c in coc for w in N.DOUBLE_RELS),
            'bend_tangents_traceless':all(trace(z)==K.zero for c in coc for z in c.values()),
            'bend_columns_independent4':rq==4,'coboundary_rank24':rb==24,'quotient_adds_four':joined==rb+4==28,
            'scalar_bend_has_zero_tangent':all(C.same(z,C.zero(5,5,K)) for z in scalar_coc),
            'scale_determinant_one':N.determinant(scale(2))==K.one,
            'scale_commutes_with_seam':all(C.same(scale(2)*g,g*scale(2)) for g in peripheral.values()),
            'changed_join_relators':relators(changed),'changed_join_full_matrix25':alg['dimension']==25,
            'trace_pool_witness':witness is not None,
            'trace_formula':witness is not None and witness['formula_pass'],
            'trace_separates':witness is not None and witness['separates_one_two']}
    return {'character':list(ab),'checks':checks,'left_algebra_dimension':ls['dimension'],
            'right_algebra_dimension':rs['dimension'],'peripheral_centralizer_dimension':kc.shape[1],
            'neutral_h1_lower_bound':joined-rb,'coboundary_rank':rb,'joined_rank':joined,
            'trace_witness':witness,
            'witness':{'left':old['witness']['left'],'right':old['witness']['right'],
                       's':old['witness']['s'],'left_words':ls['words'],'right_words':rs['words'],
                       'changed_joint_words':alg['words'],'z_basis':[N.export(z) for z in zs]},
            '_left':left,'_right':right,'_cocycles':coc}


@lru_cache(None)
def trivial():
    gs={t:C.eye(1,K) for t in 'xyzabc'}
    out=N.h1(gs,N.DOUBLE_RELS)
    return {'counts':out,'checks':{'trivial_invariants_one':out['h0']==1,'trivial_h1_one':out['h1']==1}}


@lru_cache(None)
def fixtures():
    i=C.eye(2,K); a=i+unit(2,0,1); b=i+unit(2,1,0); d=N.rows_dm([[K.convert(2),K.zero],[K.zero,K.one]],2)
    h=N.rows_dm([[K.one,K.zero],[K.zero,-K.one]],2)
    r=d*b*C.inv(d); scalar=K.convert(2)*i
    seam=N.rows_dm([[K.convert(2),K.zero],[K.zero,K.convert(3)]],2)
    bad=unit(2,0,1); gc={'x':C.eye(1,K)}
    circle=N.h1(gc,('',)); point=N.h1(gc,('x',))
    checks={'upper_parabolic_positive':N.span({'a':a,'d':d})['dimension']==3,
            'lower_parabolic_positive':N.span({'b':b,'d':d})['dimension']==3,
            'full_join_positive':N.span({'a':a,'b':b})['dimension']==4,
            'proper_join_rejected':N.span({'a':a})['dimension']<4,
            'relative_trace_changes':trace(a*b)!=trace(a*r),
            'scalar_conjugation_trace_unchanged':C.same(scalar*b*C.inv(scalar),b),
            'scalar_tangent_zero':C.same(i-b*i*C.inv(b),C.zero(2,2,K)),
            'noncentral_seam_tangent_rejected':not C.same(seam*bad,bad*seam),
            'traceless_diagonal_seam_tangent_positive':C.same(seam*h,h*seam) and trace(h)==K.zero,
            'singular_rank_rejected':C.rank(unit(2,0,0))==1,
            'circle_trivial_h1_positive':circle['h1']==1,'point_trivial_h1_opposite':point['h1']==0,
            'retained_commutant_one_opposite':N.fixtures()['checks']['flag_algebra_not_full']}
    return {'checks':checks}


def run():
    groups=[]
    def emit(name,out):
        out={t:v for t,v in out.items() if not t.startswith('_')}; groups.append(out)
        print(json.dumps({'group':name,**out},sort_keys=True),flush=True)
    emit('fixtures',fixtures())
    for ab in N.CHARS:
        emit('case',case(ab))
    emit('trivial',trivial())
    cs=[v for out in groups for v in out['checks'].values()]
    result={'passed':sum(cs),'total':len(cs),'all':all(cs),'scope':'exact neutral lower bound and relative trace; no physical selection'}
    print(json.dumps(result,sort_keys=True),flush=True)
    return result


if __name__=='__main__':
    raise SystemExit(0 if run()['all'] else 1)
