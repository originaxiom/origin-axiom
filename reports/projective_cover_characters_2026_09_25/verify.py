"""F17: exact marked unfilled cover, characters, pairings and SL4 H1."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import importlib.util
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

path=Path(__file__).parent.parent/'projective_deformation_tangent_2026_09_25'/'verify_v2.py'
spec=importlib.util.spec_from_file_location('f17_f15_adapter',path)
adapter=importlib.util.module_from_spec(spec); spec.loader.exec_module(adapter)
v=adapter.v
REL=v.REL
LONG='nMNmmNMn'
MAPS={'id':('m','n'),'T':('n','m'),'theta':('M','N'),
      'thetaT':('N','M'),'R+':('M','nMN'),'R-':('M','NMn'),
      'G+':('m','nmN'),'G-':('m','Nmn')}
PAIR_NAMES=('theta','thetaT','G+','G-')
WORDS=('mmm','nM','mnMM','mmn')
BASIS_WORDS=('','m','n','mm','nm','mn','nn','nmm','mnm','nnm',
             'mmn','nmn','mnn','mnmm','nnmm','nnmn')


def inverse(w):
    return w.swapcase()[::-1]


def reduce_word(w):
    out=[]
    for c in w:
        if out and out[-1]==c.swapcase(): out.pop()
        else: out.append(c)
    return ''.join(out)


def subst(w,name):
    images=MAPS[name]
    return ''.join(images['mn'.index(c.lower())] if c.islower()
                   else inverse(images['mn'.index(c.lower())]) for c in w)


def rewrite(w,start=0):
    k=start; out=[]
    for c in w:
        if c=='m':
            if k==2: out.append(1)
            k=(k+1)%3
        elif c=='M':
            if k==0: out.append(-1)
            k=(k-1)%3
        elif c=='n':
            out.append(k+2); k=(k+1)%3
        elif c=='N':
            k=(k-1)%3; out.append(-(k+2))
        else: raise ValueError('not a base letter')
    return tuple(out),k


def expand(w):
    return ''.join(WORDS[abs(g)-1] if g>0 else inverse(WORDS[abs(g)-1]) for g in w)


RELS=tuple(rewrite(REL,k)[0] for k in range(3))


def exponents(w):
    return tuple(sum((1 if g>0 else -1) for g in w if abs(g)==j) for j in range(1,5))


RELATION_MATRIX=s.Matrix([exponents(w) for w in RELS])


def valid_character(a):
    return len(a)==4 and all(sum(x*y for x,y in zip(row,a))%4==0
                            for row in RELATION_MATRIX.tolist())


@lru_cache(None)
def characters():
    return tuple(a for a in product(range(4),repeat=4) if valid_character(a))


def base_characters():
    return tuple(tuple(t*sum(1 if c.islower() else -1 for c in w)%4
                       for w in WORDS) for t in range(4))


@lru_cache(None)
def lift_words(name,j):
    return tuple('m'*j+subst(w,name)+'M'*j for w in WORDS)


@lru_cache(None)
def action(name,j):
    rows=[]
    for w in lift_words(name,j):
        rw,end=rewrite(w)
        if end: raise ValueError('map does not preserve the cover')
        rows.append(exponents(rw))
    return tuple(rows)


def act(a,name,j):
    return tuple(sum(x*y for x,y in zip(row,a))%4 for row in action(name,j))


def pairing_labels(a):
    out=[]
    for name in PAIR_NAMES:
        for j in range(3):
            b=act(a,name,j)
            if b==tuple(-x%4 for x in a): out.append((name,j,'linear'))
            if b==a: out.append((name,j,'antilinear'))
    return tuple(out)


def geometric_linear(labels):
    return tuple(t for t in labels if t[0] in ('theta','thetaT') and t[2]=='linear')


def word(w,rho):
    k=rho[0].domain; out=v.eye(rho[0].shape[0],k)
    letters={g:a for g,a in zip('mn',rho)}
    letters.update({g.upper():a.inv() for g,a in zip('mn',rho)})
    for c in w: out=out*letters[c]
    return out


def cover_word(w,rho):
    k=rho[0].domain; out=v.eye(rho[0].shape[0],k)
    inv=tuple(a.inv() for a in rho)
    for g in w: out=out*(rho[g-1] if g>0 else inv[-g-1])
    return out


def fox(w,rho):
    k=rho[0].domain; d=rho[0].shape[0]
    prefix=v.eye(d,k); out=[v.zero(d,d,k) for _ in rho]
    inv=tuple(a.inv() for a in rho)
    for g in w:
        j=abs(g)-1
        if g>0: out[j]=out[j]+prefix; prefix=prefix*rho[j]
        else: prefix=prefix*inv[j]; out[j]=out[j]-prefix
    return v.cat(*out)


def direct_cocycle(w,rho,values):
    """Independent generator-value recursion, using the inverse cocycle law."""
    k=rho[0].domain; d=rho[0].shape[0]
    value=v.zero(d,1,k)
    # Right-to-left f(gv)=f(g)+rho(g)f(v), unlike Fox's prefix loop.
    for g in reversed(w):
        j=abs(g)-1
        if g>0: value=values[j]+rho[j]*value
        else: value=rho[j].inv()*(value-values[j])
    return value


@lru_cache(None)
def cover_rho(middle,embedding=1):
    k,q,rho,j=v.context(middle,embedding)
    return tuple(word(w,rho) for w in WORDS)


def twisted(middle,a,embedding=1,dual=False):
    if not valid_character(a): raise ValueError('not a character')
    rho=cover_rho(middle,embedding); k=rho[0].domain
    out=tuple(g.scalarmul(k.from_sympy(s.I**x)) for g,x in zip(rho,a))
    return tuple(g.inv().transpose() for g in out) if dual else out


@lru_cache(None)
def complex_data(middle,a,embedding=1,dual=False):
    rho=twisted(middle,a,embedding,dual); k=rho[0].domain
    b=v.stack(*(g-v.eye(4,k) for g in rho))
    r=v.stack(*(fox(w,rho) for w in RELS))
    rb,rr=b.rank(),r.rank()
    return dict(rho=rho,B=b,R=r,h0=4-rb,h1=16-rb-rr,ranks=(rb,rr),
                chain_zero=(r*b).is_zero_matrix,
                relators=all((cover_word(w,rho)-v.eye(4,k)).is_zero_matrix for w in RELS))


def flatten(a):
    return v.DM([[x] for row in a.to_list() for x in row],(a.shape[0]*a.shape[1],1),a.domain)


def unvec(a):
    values=[row[0] for row in a.to_list()]
    return v.DM([values[4*i:4*i+4] for i in range(4)],(4,4),a.domain)


@lru_cache(None)
def base_intertwiner(middle,name,embedding=1):
    k,q,rho,_=v.context(middle,embedding)
    target=tuple(g.inv().transpose() for g in rho)
    source=tuple(word(w,rho) for w in MAPS[name])
    columns=[]
    for i in range(4):
        for j in range(4):
            e=s.zeros(4); e[i,j]=1; e=v.dm(e,k)
            columns.append(v.stack(*(flatten(a*e-e*b) for a,b in zip(target,source))))
    equations=v.cat(*columns); basis=v.kernel(equations)
    if basis.shape[1]!=1: raise ValueError(('unexpected base pairing dimension',name,basis.shape))
    jmat=unvec(v.col(basis,0))
    if jmat.det()==k.zero: raise ValueError('singular base pairing')
    return jmat,equations


@lru_cache(None)
def untwisted_lift(middle,name,j,embedding=1):
    k,q,rho,_=v.context(middle,embedding)
    jj=base_intertwiner(middle,name,embedding)[0]
    for _ in range(j): jj=jj*rho[0].inv()
    images=tuple(word(w,rho) for w in lift_words(name,j))
    return jj,images


def pairing_residuals(middle,a,label,embedding=1):
    name,j,kind=label; jj,images=untwisted_lift(middle,name,j,embedding)
    k=jj.domain; target=twisted(middle,a,embedding,dual=True)
    phases=act(a,name,j)
    if kind=='antilinear': phases=tuple(-x%4 for x in phases)
    elif kind!='linear': raise ValueError('unknown linearity')
    source=tuple(g.scalarmul(k.from_sympy(s.I**x)) for g,x in zip(images,phases))
    return tuple(t*jj-jj*g for t,g in zip(target,source))


def matrix_algebra_determinant(middle,embedding=1):
    k,q,rho,_=v.context(middle,embedding)
    return v.cat(*(flatten(word(w,rho)) for w in BASIS_WORDS)).det()


def recover_from_cube(a):
    k=a.domain; one=v.eye(4,k); b=a*a*a-one
    return one+b.scalarmul(k(s.Rational(1,3)))-(b*b).scalarmul(k(s.Rational(1,9)))+(b*b*b).scalarmul(k(s.Rational(5,81)))


def report(middle):
    rows=[]
    for a in characters():
        pair=pairing_labels(a)
        e=complex_data(middle,a); d=complex_data(middle,a,dual=True)
        rows.append(dict(character=a,h0=e['h0'],h1=e['h1'],dual_h0=d['h0'],dual_h1=d['h1'],
                         ranks=e['ranks'],dual_ranks=d['ranks'],
                         relators=e['relators'] and d['relators'],chain_zero=e['chain_zero'] and d['chain_zero'],
                         pairings=pair,linear_inversions=geometric_linear(pair),
                         exact_pairings=all(all(r.is_zero_matrix for r in pairing_residuals(middle,a,label)) for label in pair)))
    return dict(middle=middle,embedding=1,relators=RELS,relation_matrix=RELATION_MATRIX.tolist(),
                smith_diagonal=list(smith_normal_form(RELATION_MATRIX,domain=s.ZZ).diagonal()),
                base_characters=base_characters(),characters=len(rows),
                matter_characters=sum(r['h1']>0 for r in rows),
                paired_by_linear_inversion=sum(bool(r['linear_inversions']) for r in rows),
                matter_without_linear_inversion=[r['character'] for r in rows if r['h1'] and not r['linear_inversions']],
                rows=rows)


if __name__=='__main__':
    for middle in (14,34):
        print(json.dumps(report(middle),default=str,sort_keys=True),flush=True)
