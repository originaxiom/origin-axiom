"""R85 exact K witnesses. R75 primitives retained; no received census import."""
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'cross_branch_positives.py'
if sha256(SOURCE.read_bytes()).hexdigest() != '57d52d0268cc8562522560029727026d5d0cc80e88bd0f464aee704858911731':
    raise RuntimeError('Changed R75 primitive source')
SPEC = importlib.util.spec_from_file_location('r85_retained_r75', SOURCE)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
K = C.MonogenicFiniteExtension(s.Poly(C.Q**6-34*C.Q**3+1,C.Q,domain=s.QQ))
CHARS = ((0,1),(1,1),(1,0))
LEFT_RELS = ('zxZ'+C.inverse_word(C.power_phi('x',3)),
             'zyZ'+C.inverse_word(C.power_phi('y',3)))
RENAME = str.maketrans('xyzXYZ','abcABC')
DOUBLE_RELS = LEFT_RELS + tuple(w.translate(RENAME) for w in LEFT_RELS) + ('zc','yXYxbABa')


def flat(a):
    return [v for row in a.to_list() for v in row]


def rows_dm(rows,ncols,k=K):
    return C.DomainMatrix(rows,(len(rows),ncols),k)


def dual(gens):
    return {name:C.inv(a).transpose() for name,a in gens.items()}


def exterior(a):
    n=a.shape[0]; pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    b=a.to_list()
    return rows_dm([[b[i][u]*b[j][v]-b[i][v]*b[j][u] for u,v in pairs]
                    for i,j in pairs],len(pairs),a.domain)


def equations(u,v):
    n=u.shape[0]; k=u.domain; cols=[]
    for i in range(n):
        for j in range(n):
            e=[[k.zero for _ in range(n)] for _ in range(n)]
            e[i][j]=k.one; a=rows_dm(e,n,k)
            cols.append(flat(u*a-a*u.transpose())+flat(v*a-a*v.transpose()))
    return rows_dm([list(row) for row in zip(*cols)],n*n,k)


def match(u,v):
    """Finite declared pool; none is INCONCLUSIVE, never an all-space no-go."""
    ker=C.kernel(equations(u,v)); n=u.shape[0]; d=ker.shape[1]; k=u.domain
    data=ker.to_list()
    weights=[[int(i==j) for i in range(d)] for j in range(d)]
    weights += [[1]*d]+[[t**i for i in range(d)] for t in range(2,10)]
    for num,ws in enumerate(weights):
        z=[sum((row[i]*ws[i] for i in range(d)),k.zero) for row in data]
        a=rows_dm([z[i*n:(i+1)*n] for i in range(n)],n,k)
        if C.rank(a)==n:
            return {'dimension':d,'pool_index':num,'s':a,'kernel':ker}
    return {'dimension':d,'pool_index':None,'s':None,'kernel':ker}


def span(gens):
    """Exact incremental row echelon and independent positive-word witness."""
    n=next(iter(gens.values())).shape[0]; k=next(iter(gens.values())).domain
    basis=[]; pivots={}; words=[]
    def add(a,w):
        row=flat(a)
        for p in sorted(pivots):
            if row[p]:
                z=row[p]; row=[x-z*y for x,y in zip(row,pivots[p])]
        p=next((i for i,v in enumerate(row) if v),None)
        if p is None:
            return False
        z=row[p]; pivots[p]=[v/z for v in row]
        basis.append(a); words.append(w)
        return True
    add(C.eye(n,k),'')
    i=0
    while i<len(basis) and len(basis)<n*n:
        a,w=basis[i]; i+=1
        for name,g in gens.items():
            add(a*g,w+name)
            if len(basis)==n*n:
                break
    return {'dimension':len(basis),'words':words,'closed':i==len(basis) or len(basis)==n*n}


def h1(gens,rels):
    names=list(gens); n=gens[names[0]].shape[0]; k=gens[names[0]].domain
    pairs=[C.field_word(w,gens) for w in rels]
    if not all(C.same(a,C.eye(n,k)) for a,_ in pairs):
        raise ValueError('Not a representation of declared relators')
    j=pairs[0][1].vstack(*(b for _,b in pairs[1:]))
    b=(gens[names[0]]-C.eye(n,k)).vstack(*(gens[t]-C.eye(n,k) for t in names[1:]))
    if not C.same(j*b,C.zero(len(rels)*n,n,k)):
        raise ValueError('Fox chain identity failed')
    rb=C.rank(b); rj=C.rank(j)
    return {'h0':n-rb,'h1':len(names)*n-rj-rb,'d0_rank':rb,'d1_rank':rj}


def export(a):
    out=[]
    for row in a.to_list():
        vals=[]
        for z in row:
            coeff=[str(c) for c in reversed(z.rep.to_list())]
            vals.append(coeff+['0']*(6-len(coeff)))
        out.append(vals)
    return out


@lru_cache(None)
def case(ab):
    m,n=C.literal(); rx=C.clean(n*m.inv()); ry=C.clean(m*n*m.inv()**2)
    vs={'x':C.dm((-1)**ab[0]*rx,K),'y':C.dm((-1)**ab[1]*ry,K),
        'z':C.dm(-m**3,K)}
    ker=C.kernel(C.dm(C.cycle(ab),K)+C.eye(8,K))
    if ker.shape[1]!=1:
        raise ValueError('R75 actual transport kernel changed')
    coc=ker.extract(list(range(8)),[0])
    def lift(v,c):
        return v.hstack(c).vstack(C.zero(1,4,K).hstack(C.eye(1,K)))
    left={'x':lift(vs['x'],coc.extract(list(range(4)),[0])),
          'y':lift(vs['y'],coc.extract(list(range(4,8)),[0])),
          'z':lift(vs['z'],C.zero(4,1,K))}
    ell=C.field_word('yXYx',left)[0]; u=left['z']; out=match(u,ell); a=out['s']
    if a is None:
        return {'character':list(ab),'outcome':'INCONCLUSIVE_MATCH_POOL',
                'match_dimension':out['dimension'],'checks':{'invertible_match':False}}
    ia=C.inv(a); right={name:a*g*ia for name,g in dual(left).items()}
    whole=dict(left); whole.update({name.translate(RENAME):g for name,g in right.items()})
    algebra=span(whole)
    def relators(gs,rels):
        return all(C.same(C.field_word(w,gs)[0],C.eye(5,K)) for w in rels)
    vb=(vs['x']-C.eye(4,K)).vstack(vs['y']-C.eye(4,K))
    checks={'invertible_match':C.rank(a)==5,
            'meridian_match':C.same(u*a,a*u.transpose()),
            'longitude_match':C.same(ell*a,a*ell.transpose()),
            'left_relators':relators(left,LEFT_RELS),
            'right_relators':relators(right,LEFT_RELS),
            'double_relators':relators(whole,DOUBLE_RELS),
            'torus_commutes':C.same(u*ell,ell*u),
            'cusp_literally_split':not any(row[4] for row in ell.to_list()[:4]),
            'vz_minus_one_invertible':C.rank(vs['z']-C.eye(4,K))==4,
            'nonzero_cocycle':any(flat(coc)),
            'nontrivial_fibre_class':C.rank(vb.hstack(coc))==C.rank(vb)+1,
            'determinant_one':all(g.det()==K.one for g in whole.values()),
            'full_matrix_algebra':algebra['dimension']==25,
            'span_closed':algebra['closed']}
    witness={'left':{t:export(g) for t,g in left.items()},
             'right':{t:export(g) for t,g in right.items()},'s':export(a),
             'span_words':algebra['words'],'relators':list(DOUBLE_RELS)}
    return {'character':list(ab),'outcome':'FULL_MATRIX_ADMISSION_PREMISE' if all(checks.values()) else 'PREMISE_NOT_ACCEPTED',
            'match_dimension':out['dimension'],'pool_index':out['pool_index'],
            'algebra_dimension':algebra['dimension'],'checks':checks,'witness':witness,
            '_left':left,'_right':right,'_whole':whole}


@lru_cache(None)
def spectrum():
    out=case((0,1)); left=out['_left']; right=out['_right']; whole=out['_whole']
    a=h1(whole,DOUBLE_RELS); b=h1(dual(whole),DOUBLE_RELS)
    xl={t:exterior(g) for t,g in left.items()}; xr={t:exterior(g) for t,g in right.items()}
    ell=C.field_word('yXYx',xl)[0]
    pieces=[h1(gs,LEFT_RELS) for gs in (xl,xr,dual(xl),dual(xr))]
    ae=pieces[0]['h1']+pieces[1]['h1']; be=pieces[2]['h1']+pieces[3]['h1']
    checks={'charged_invariants_zero':a['h0']==b['h0']==0,
            'charged_degree_one_balanced':a['h1']==b['h1'],
            'exterior_torus_acyclic':C.rank(ell-C.eye(10,K))==10,
            'exterior_piece_invariants_zero':all(p['h0']==0 for p in pieces),
            'exterior_degree_one_balanced':ae==be}
    return {'representative':[0,1],'rank_five':a,'dual_five':b,
            'exterior_piece_counts':pieces,'exterior_join_h1':ae,'dual_exterior_join_h1':be,
            'exterior_join_method':'exact piece Fox H1 plus verified acyclic-torus Mayer-Vietoris',
            'checks':checks}


@lru_cache(None)
def fixtures():
    eye=lambda n:C.eye(n,K)
    def e(n,i,j):
        a=[[K.zero for _ in range(n)] for _ in range(n)]; a[i][j]=K.one
        return rows_dm(a,n)
    u=eye(3)+e(3,0,1); v=eye(3)+e(3,0,2); ker=C.kernel(equations(u,v)).to_list()
    forced=all(not x for pos in (4,5,7,8) for x in ker[pos])
    full={'a':eye(2)+e(2,0,1),'b':eye(2)+e(2,1,0)}
    diag=C.dm(s.diag(2,3,5,7,s.Rational(1,210)),K)
    upper=eye(5)+sum((e(5,i,i+1) for i in range(4)),C.zero(5,5,K))
    flag={'a':diag,'b':upper}
    # Centralizer equations are independent of the span test.
    commcols=[]
    for i in range(5):
        for j in range(5):
            t=e(5,i,j); commcols.append(flat(diag*t-t*diag)+flat(upper*t-t*upper))
    comm=C.kernel(rows_dm([list(r) for r in zip(*commcols)],25)).shape[1]
    pos=match(C.dm(s.diag(2,3),K),C.dm(s.diag(5,7),K))
    singular=C.zero(3,3,K)
    checks={'commuting_counterpair':C.same(u*v,v*u),
            'entire_counterpair_kernel_singular':forced,
            'counterpair_kernel_dimension':len(ker[0])==3,
            'diagonal_positive_match':pos['s'] is not None,
            'singular_match_rejected':C.rank(singular)<3,
            'full_two_algebra':span(full)['dimension']==4,
            'proper_two_algebra':span({'a':full['a']})['dimension']==2,
            'flag_commutant_one':comm==1,
            'flag_algebra_not_full':span(flag)['dimension']==15,
            'transpose_not_homomorphism':not C.same((full['a']*full['b']).transpose(),full['a'].transpose()*full['b'].transpose()),
            'inverse_transpose_is_homomorphism':C.same(C.inv(full['a']*full['b']).transpose(),C.inv(full['a']).transpose()*C.inv(full['b']).transpose())}
    return {'checks':checks,'flag_algebra_dimension':15,'flag_commutant_dimension':comm}


def public(out):
    return {k:v for k,v in out.items() if not k.startswith('_')}


def run():
    groups=[('fixtures',fixtures())]
    print(json.dumps({'group':'fixtures',**groups[0][1]},sort_keys=True),flush=True)
    for ab in CHARS:
        out=public(case(ab)); groups.append(('case',out))
        print(json.dumps({'group':'case',**out},sort_keys=True),flush=True)
    out=spectrum(); groups.append(('spectrum',out))
    print(json.dumps({'group':'spectrum',**out},sort_keys=True),flush=True)
    checks=[v for _,g in groups for v in g['checks'].values()]
    result={'passed':sum(checks),'total':len(checks),'all':all(checks),
            'scope':'exact candidate admission premises/representative counts, not derived physics'}
    print(json.dumps(result,sort_keys=True),flush=True)
    return result


if __name__=='__main__':
    raise SystemExit(0 if run()['all'] else 1)
