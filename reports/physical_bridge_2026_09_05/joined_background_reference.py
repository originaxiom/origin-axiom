"""R85 same-author separate modular witness verifier. No SymPy/native import."""
from fractions import Fraction
import json
from pathlib import Path
import sys

PRIMES=(1009,1013,1019,1031,1033,1039,1049,1051,1061,1063)


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a,b,p):
    return [[sum(x*y for x,y in zip(row,col))%p for col in zip(*b)] for row in a]


def add(a,b,p,sign=1):
    return [[(x+sign*y)%p for x,y in zip(r,t)] for r,t in zip(a,b)]


def rref(a,p):
    a=[list(r) for r in a]; nr=len(a); nc=len(a[0]); piv=[]; row=0
    for col in range(nc):
        j=next((j for j in range(row,nr) if a[j][col]%p),None)
        if j is None:
            continue
        a[row],a[j]=a[j],a[row]; z=pow(a[row][col]%p,-1,p)
        a[row]=[(x*z)%p for x in a[row]]
        for j in range(nr):
            if j!=row and a[j][col]%p:
                z=a[j][col]%p; a[j]=[(x-z*y)%p for x,y in zip(a[j],a[row])]
        piv.append(col); row+=1
        if row==nr:
            break
    return a,piv


def rank(a,p):
    return len(rref(a,p)[1])


def inv(a,p):
    n=len(a); rr,piv=rref([r+t for r,t in zip(a,eye(n))],p)
    if piv[:n]!=list(range(n)):
        raise ValueError('Singular modular witness')
    return [r[n:] for r in rr]


def det(a,p):
    a=[r[:] for r in a]; d=1
    for i in range(len(a)):
        j=next((j for j in range(i,len(a)) if a[j][i]%p),None)
        if j is None:
            return 0
        if j!=i:
            a[i],a[j]=a[j],a[i]; d=-d
        z=a[i][i]%p; d=d*z%p; zi=pow(z,-1,p)
        for j in range(i+1,len(a)):
            t=a[j][i]*zi%p
            a[j]=[(x-t*y)%p for x,y in zip(a[j],a[i])]
    return d%p


def evaluate(a,p,r):
    out=[]
    for row in a:
        vals=[]
        for coeff in row:
            if len(coeff)!=6:
                raise ValueError('Polynomial coefficient dimension')
            z=0
            for c in reversed(coeff):
                f=Fraction(c)
                z=(z*r+f.numerator*pow(f.denominator%p,-1,p))%p
            vals.append(z)
        out.append(vals)
    return out


def inverse_word(w):
    return w[::-1].swapcase()


def reduce_word(w):
    out=[]
    for c in w:
        if out and out[-1]==c.swapcase():
            out.pop()
        else:
            out.append(c)
    return ''.join(out)


def phi(w):
    subst={'x':'y','y':'yXyy'}
    return reduce_word(''.join(subst[c] if c.islower() else inverse_word(subst[c.lower()]) for c in w))


def relators():
    x,y='x','y'
    for _ in range(3):
        x,y=phi(x),phi(y)
    left=('zxZ'+inverse_word(x),'zyZ'+inverse_word(y))
    tr=str.maketrans('xyzXYZ','abcABC')
    return left+tuple(w.translate(tr) for w in left)+('zc','yXYxbABa')


def word(w,gens,p):
    names=list(gens); n=len(gens[names[0]]); z=eye(n)
    jac=[[0]*(n*len(names)) for _ in range(n)]; inverses={}
    for c in w:
        i=names.index(c.lower()); g=gens[c.lower()]
        if c.islower():
            b=z; z=mul(z,g,p)
        else:
            if c.lower() not in inverses:
                inverses[c.lower()]=inv(g,p)
            z=mul(z,inverses[c.lower()],p); b=[[-x%p for x in row] for row in z]
        for j in range(n):
            for t in range(n):
                jac[j][i*n+t]=(jac[j][i*n+t]+b[j][t])%p
    return z,jac


def dual(gens,p):
    return {name:transpose(inv(g,p)) for name,g in gens.items()}


def exterior(a,p):
    n=len(a); pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    return [[(a[i][u]*a[j][v]-a[i][v]*a[j][u])%p for u,v in pairs] for i,j in pairs]


def cohomology(gens,rels,p):
    n=len(next(iter(gens.values()))); j=[]
    for w in rels:
        z,d=word(w,gens,p)
        if z!=eye(n):
            raise ValueError('Independent relator failure')
        j.extend(d)
    b=[row for g in gens.values() for row in add(g,eye(n),p,-1)]
    if any(x for row in mul(j,b,p) for x in row):
        raise ValueError('Independent Fox chain failure')
    rb=rank(b,p); rj=rank(j,p)
    return {'h0':n-rb,'h1':len(gens)*n-rj-rb,'d0_rank':rb,'d1_rank':rj}


def prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**.5)+1))


def roots(p):
    return [r for r in range(p) if (r**6-34*r**3+1)%p==0]


def verify_case(rec,p,r,spec):
    w=rec['witness']; left={t:evaluate(a,p,r) for t,a in w['left'].items()}
    right={t:evaluate(a,p,r) for t,a in w['right'].items()}; a=evaluate(w['s'],p,r)
    ia=inv(a,p); n=5; ell=word('yXYx',left,p)[0]
    whole=dict(left); whole.update({t.translate(str.maketrans('xyz','abc')):g for t,g in right.items()})
    words=w['span_words']; rows=[[x for row in word(t,whole,p)[0] for x in row] for t in words]
    checks={'root':(r**6-34*r**3+1)%p==0,'prime':prime(p),
            'invertible_match':det(a,p)!=0,
            'meridian_match':mul(left['z'],a,p)==mul(a,transpose(left['z']),p),
            'longitude_match':mul(ell,a,p)==mul(a,transpose(ell),p),
            'literal_dual_not_transpose':all(right[t]==mul(mul(a,g,p),ia,p) for t,g in dual(left,p).items()),
            'both_pieces_and_join_relators':w['relators']==list(relators()) and all(word(t,whole,p)[0]==eye(n) for t in relators()),
            'determinant_one':all(det(g,p)==1 for g in whole.values()),
            'independent_word_basis_rank25':len(words)==25 and rank(rows,p)==25,
            'exported_coefficients_exact_length':all(len(c)==6 for row in w['s'] for c in row)}
    counts={}
    if rec['character']==[0,1]:
        b=cohomology(whole,relators(),p); bd=cohomology(dual(whole,p),relators(),p)
        ext={t:exterior(g,p) for t,g in whole.items()}
        e=cohomology(ext,relators(),p); ed=cohomology(dual(ext,p),relators(),p)
        checks.update({'direct_double_five_matches_exact':b==spec['rank_five'],
                       'direct_double_dual_five_matches_exact':bd==spec['dual_five'],
                       'direct_double_exterior_matches_mv':e['h0']==0 and e['h1']==spec['exterior_join_h1'],
                       'direct_double_dual_exterior_matches_mv':ed['h0']==0 and ed['h1']==spec['dual_exterior_join_h1'],
                       'actual_exterior_boundary_acyclic':rank(add(exterior(ell,p),eye(10),p,-1),p)==10})
        counts={'five':b,'dual_five':bd,'exterior':e,'dual_exterior':ed}
    return {'character':rec['character'],'prime':p,'root':r,'checks':checks,'counts':counts}


def controls():
    p=1009; a=[[1,1],[0,1]]; b=[[1,0],[1,1]]
    checks={'full_rank_opposite':rank(eye(3),p)==3,
            'singular_opposite':rank([[1,2],[2,4]],p)==1,
            'transpose_order_rejected':transpose(mul(a,b,p))!=mul(transpose(a),transpose(b),p),
            'dual_product_order':transpose(inv(mul(a,b,p),p))==mul(transpose(inv(a,p)),transpose(inv(b,p)),p),
            'exterior_determinant_one':det(exterior(eye(5),p),p)==1}
    return {'checks':checks}


def run(path):
    records=[json.loads(line) for line in Path(path).read_text().splitlines()]
    if not records[-1].get('all'):
        raise ValueError('Native first run did not pass')
    cases=[r for r in records if r.get('group')=='case']
    spec=next(r for r in records if r.get('group')=='spectrum')
    if [r['character'] for r in cases]!=[[0,1],[1,1],[1,0]]:
        raise ValueError('Wrong character population')
    out=controls(); groups=[out]; print(json.dumps({'group':'controls',**out},sort_keys=True),flush=True)
    accepted=[]
    for p in PRIMES:
        if not prime(p):
            raise ValueError('Declared nonprime')
        for r in roots(p):
            try:
                # Denominator validity must hold for the entire exported population.
                for rec in cases:
                    for a in list(rec['witness']['left'].values())+list(rec['witness']['right'].values())+[rec['witness']['s']]:
                        evaluate(a,p,r)
            except ValueError:
                continue
            accepted.append((p,r)); break
        if len(accepted)==2:
            break
    if len(accepted)!=2:
        raise ValueError('INCONCLUSIVE: two valid declared primes not found')
    for p,r in accepted:
        for rec in cases:
            out=verify_case(rec,p,r,spec); groups.append(out)
            print(json.dumps({'group':'witness',**out},sort_keys=True),flush=True)
    checks=[v for g in groups for v in g['checks'].values()]
    result={'passed':sum(checks),'total':len(checks),'all':all(checks),
            'selected_prime_roots':accepted,'scope':'separate modular witness verification, same author; not exact K proof or physical certificate'}
    print(json.dumps(result,sort_keys=True),flush=True)
    return result


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: joined_background_reference.py NATIVE_JSON_LINES_LOG')
    raise SystemExit(0 if run(sys.argv[1])['all'] else 1)
