"""R87 same-author modular witness checks with a separate E8 lattice enumeration."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sys

SOURCE=Path(__file__).with_name('joined_background_reference.py')
if sha256(SOURCE.read_bytes()).hexdigest()!='22e41effc4acf899172e4bd95c196c11542ebd58580d14ea9e20dbce49eae869':
    raise RuntimeError('Changed modular primitives')
spec=importlib.util.spec_from_file_location('r87_modular_primitives',SOURCE)
M=importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
PRIME_ROOTS=((1031,695),(1033,162))
T_VALUES=('1','2','3','1/2')


def zero(n):
    return [[0]*n for _ in range(n)]


def scalar(a,c,p):
    return [[z*c%p for z in row] for row in a]


def unit(n,i,j):
    a=zero(n); a[i][j]=1; return a


def trace(a,p):
    return sum(a[i][i] for i in range(len(a)))%p


def field(s,p):
    a=Fraction(s); return a.numerator*pow(a.denominator,-1,p)%p


def end0_trace(g,p):
    gi=M.inv(g,p); off=[(i,j) for i in range(5) for j in range(5) if i!=j]
    basis=[unit(5,i,j) for i,j in off]+[M.add(unit(5,i,i),unit(5,4,4),p,-1) for i in range(4)]
    total=0
    for k,e in enumerate(basis):
        a=M.mul(M.mul(g,e,p),gi,p)
        coords=[a[i][j] for i,j in off]+[a[i][i] for i in range(4)]
        rebuilt=zero(5)
        for z,b in zip(coords,basis):
            rebuilt=M.add(rebuilt,scalar(b,z,p),p)
        if trace(a,p) or rebuilt!=a:
            raise ValueError('Independent End0 reconstruction')
        total=(total+coords[k])%p
    return total


def direct(g,p):
    h=M.inv(g,p); a=trace(g,p); b=trace(h,p)
    c=trace(M.exterior(g,p),p); d=trace(M.exterior(h,p),p); e=end0_trace(g,p)
    return {'five':a,'dual_five':b,'ten':c,'dual_ten':d,'end0':e,
            'parent':(e+24+10*(a+b)+5*(c+d))%p}


def polynomial(a,b,h,k,p):
    tr=[trace(a,p),trace(b,p)]; td=[trace(h,p),trace(k,p)]
    def ext(g0,g1,ts):
        sq=[trace(M.mul(g0,g0,p),p),trace(M.add(M.mul(g0,g1,p),M.mul(g1,g0,p),p),p),trace(M.mul(g1,g1,p),p)]
        return [(z-s)*pow(2,-1,p)%p for z,s in zip([ts[0]**2,2*ts[0]*ts[1],ts[1]**2],sq)]
    c=ext(a,b,tr); d=ext(h,k,td)
    par=[tr[0]*td[0]+23,tr[0]*td[1]+tr[1]*td[0],tr[1]*td[1]]
    par=[(z+5*(c[i]+d[i])+(10*(tr[i]+td[i]) if i<2 else 0))%p for i,z in enumerate(par)]
    return {'five':tr,'dual_five':td,'ten':c,'dual_ten':d,'parent':par}


def evaluate(a,x,p):
    out=0
    for z in reversed(a):
        out=(out*x+z)%p
    return out


@lru_cache(None)
def roots_and_roster():
    # Different instrument: all norm-eight points in a bounded doubled lattice.
    roots={v for v in product(range(-2,3),repeat=8) if sum(z*z for z in v)==8
           and (all(z%2==0 for z in v) or all(z%2!=0 for z in v)) and sum(v)%4==0}
    e=[tuple(2*int(i==j) for j in range(8)) for i in range(8)]
    sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
    simple=[sub(e[i],e[i+1]) for i in range(4)]+[sub(e[6],e[7]),sub(e[5],e[6]),tuple(x+y for x,y in zip(e[6],e[7])),(-1,)*8]
    actual=Counter(tuple(sum(x*y for x,y in zip(v,a))//4 for a in simple) for v in roots); actual[(0,)*8]+=8
    f=[tuple(int(i==j)-int(i+1==j) for i in range(4)) for j in range(5)]
    add=lambda a,b:tuple(x+y for x,y in zip(a,b)); neg=lambda a:tuple(-z for z in a)
    ten=[add(a,b) for a,b in combinations(f,2)]
    rs={'1':[(0,)*4],'5':f,'bar5':list(map(neg,f)),'10':ten,'bar10':list(map(neg,ten)),
        '24':[add(a,neg(b)) for a in f for b in f if a!=b]+[(0,)*4]*4}
    branches=(('24','1'),('1','24'),('10','5'),('bar10','bar5'),('5','bar10'),('bar5','10'))
    roster=lambda bs:Counter(a+b for l,r in bs for a in rs[l] for b in rs[r])
    wrong=branches[:4]+(('5','10'),('bar5','bar10'))
    return roots,simple,actual,roster(branches),roster(wrong)


def root_controls(p):
    roots,ss,actual,expected,wrong=roots_and_roster()
    vals=[field(z,p) for z in ('2','3','5','7','1/210')]
    def weight(w):
        out=1
        for i in range(4):
            out=out*pow(vals[i],sum(w[i:]),p)%p
        return out
    direct_roots=sum(n*weight(w[4:]) for w,n in actual.items())%p
    diag=[[vals[i] if i==j else 0 for j in range(5)] for i in range(5)]
    return {'checks':{'independent_lattice_root_count':len(roots)==240,
                      'independent_pairings_integral':all(sum(x*y for x,y in zip(v,a))%4==0 for v in roots for a in ss),
                      'whole_joint_weights':actual==expected and sum(actual.values())==248,
                      'wrong_bars_same_dimension_rejected':sum(wrong.values())==248 and actual!=wrong,
                      'direct_root_character_matches_actions':direct_roots==direct(diag,p)['parent'],
                      'identity_character248':direct(M.eye(5),p)['parent']==248%p},'prime':p}


def verify(rec,p,r):
    w=rec['witness']; a=M.evaluate(w['left_x'],p,r); b=M.evaluate(w['right_x'],p,r)
    r0=[[b[i][j] if i<4 or j==4 else 0 for j in range(5)] for i in range(5)]; r1=M.add(b,r0,p,-1)
    g0=M.mul(a,r0,p); g1=M.mul(a,r1,p); h0=M.inv(g0,p); h1=scalar(M.mul(M.mul(h0,g1,p),h0,p),-1,p)
    ps=polynomial(g0,g1,h0,h1,p); exported={k:[M.evaluate(z,p,r)[0][0] for z in v] for k,v in w['polynomials'].items()}
    checks={'prime_root':M.prime(p) and (r**6-34*r**3+1)%p==0,
            'actual_constant_and_linear_matrices':all(M.evaluate(w[k],p,r)==v for k,v in (('g0',g0),('g1',g1),('h0',h0),('h1',h1))),
            'rank_one_nilpotent_update':M.rank(g1,p)==1 and M.mul(M.mul(g1,h0,p),g1,p)==zero(5),
            'both_inverse_constant':M.mul(g0,h0,p)==M.mul(h0,g0,p)==M.eye(5),
            'both_inverse_linear':M.add(M.mul(g0,h1,p),M.mul(g1,h0,p),p)==M.add(M.mul(h0,g1,p),M.mul(h1,g0,p),p)==zero(5),
            'both_inverse_quadratic':M.mul(g1,h1,p)==M.mul(h1,g1,p)==zero(5),
            'constant_determinant_one':M.det(g0,p)==1,
            'all_exported_polynomials_match':ps==exported,
            'exterior_quadratic_zero':ps['ten'][2]==ps['dual_ten'][2]==0,
            'parent_nonconstant':any(ps['parent'][1:])}
    vals=[]; samplechecks=[]
    if [x['t'] for x in rec['samples']]!=list(T_VALUES):
        raise ValueError('Wrong sample population')
    for row in rec['samples']:
        t=field(row['t'],p); x=pow(t,-5,p); diag=[[t if i==j and i<4 else pow(t,-4,p) if i==j else 0 for j in range(5)] for i in range(5)]
        g=M.mul(M.mul(M.mul(a,diag,p),b,p),M.inv(diag,p),p); ds=direct(g,p)
        samplechecks.append({'t':row['t'],'checks':{'actual_matrix_and_inverse':g==M.add(g0,scalar(g1,x,p),p) and M.inv(g,p)==M.add(h0,scalar(h1,x,p),p),
                            'sample_determinant':M.det(g,p)==1,
                            'all_direct_actions_match':all(ds[k]==evaluate(v,x,p) for k,v in ps.items()),
                            'actual_end0_trace':ds['end0']==(ds['five']*ds['dual_five']-1)%p,
                            'exported_parent_sample':ds['parent']==M.evaluate(row['parent'],p,r)[0][0]}})
        vals.append(ds['parent'])
    checks['parent_separates_one_two']=vals[0]!=vals[1]
    deriv=(ps['parent'][1]+2*ps['parent'][2])%p
    checks['derivative_export_matches']=deriv==M.evaluate(rec['derivative_at_X_one'],p,r)[0][0]
    return {'character':rec['character'],'prime':p,'root':r,'checks':checks,'samples':samplechecks}


def controls():
    p=1031; i=M.eye(5); a=M.add(i,unit(5,0,4),p); b=M.add(i,unit(5,4,0),p)
    diag=[[2 if j==k and j<4 else pow(2,-4,p) if j==k else 0 for j in range(5)] for k in range(5)]
    changed=M.mul(M.mul(diag,b,p),M.inv(diag,p),p)
    h=unit(5,0,1); constant=polynomial(i,h,i,scalar(h,-1,p),p)['parent']
    return {'checks':{'relative_parent_changes':direct(M.mul(a,b,p),p)['parent']!=direct(M.mul(a,changed,p),p)['parent'],
                      'inverse_parent_same':direct(M.mul(a,b,p),p)['parent']==direct(M.inv(M.mul(a,b,p),p),p)['parent'],
                      'constant_polynomial_control':constant==[248,0,0],
                      'nonconstant_polynomial_control':evaluate([1,1,1],2,p)!=evaluate([1,1,1],1,p),
                      'rank_two_inverse_rejected':M.mul(M.add(unit(5,0,0),unit(5,1,1),p),M.add(unit(5,0,0),unit(5,1,1),p),p)!=zero(5)}}


def run(path):
    recs=[json.loads(x) for x in Path(path).read_text().splitlines()]
    if not recs[-1].get('all'):
        raise ValueError('Native capture not passed')
    cases=[r for r in recs if r.get('group')=='case']
    if [r['character'] for r in cases]!=[[0,1],[1,1],[1,0]]:
        raise ValueError('Wrong character population')
    out=[]
    def emit(group,d):
        out.append(d); print(json.dumps({'group':group,**d},sort_keys=True),flush=True)
    emit('controls',controls())
    for p,r in PRIME_ROOTS:
        emit('roots',root_controls(p))
        for rec in cases:
            emit('case',verify(rec,p,r))
    cs=[v for d in out for v in d['checks'].values()]+[v for d in out for x in d.get('samples',[]) for v in x['checks'].values()]
    result={'all':all(cs),'passed':sum(cs),'total':len(cs),'scope':'same-author modular/root witness verification; not a second exact proof or physical completion'}
    print(json.dumps(result,sort_keys=True),flush=True); return result


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: parent_gluing_character_reference.py NATIVE_LOG')
    raise SystemExit(0 if run(sys.argv[1])['all'] else 1)
