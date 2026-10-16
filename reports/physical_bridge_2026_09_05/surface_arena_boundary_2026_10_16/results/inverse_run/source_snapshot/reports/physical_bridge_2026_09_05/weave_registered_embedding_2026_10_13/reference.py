"""Fraction weight and Gaussian block reconstruction. No native or SymPy import."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
import json


def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def scale(a,x): return tuple(a*b for b in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))


def solve(matrix, rhs):
    rows = [list(map(Q,row))+[Q(v)] for row,v in zip(matrix,rhs)]
    for j in range(len(rows)):
        p = next(k for k in range(j,len(rows)) if rows[k][j])
        rows[j],rows[p] = rows[p],rows[j]
        rows[j] = [x/rows[j][j] for x in rows[j]]
        for k in range(len(rows)):
            if k != j:
                a = rows[k][j]; rows[k] = [x-a*y for x,y in zip(rows[k],rows[j])]
    return [row[-1] for row in rows]


def root_data():
    unit = [tuple(Q(j == k) for j in range(8)) for k in range(8)]
    rr = []
    for j,k in combinations(range(8),2):
        for a,b in product((-1,1),repeat=2): rr.append(add(scale(a,unit[j]),scale(b,unit[k])))
    rr += [tuple(Q(a,2) for a in v) for v in product((-1,1),repeat=8) if v.count(-1)%2 == 0]
    return unit,rr


def frame(n):
    e,rr = root_data()
    chain = [add(e[6],neg(e[7])),add(e[5],neg(e[6])),add(e[6],e[7]),tuple(Q(-1,2) for j in range(8))]
    if n == 6: chain.append(add(e[3],e[4]))
    gram = [[dot(a,b) for b in chain] for a in chain]
    coefficients = solve(gram,[1]+[0]*(n-2))
    first = tuple(sum(c*a[j] for c,a in zip(coefficients,chain)) for j in range(8))
    weights = [first]
    for a in chain: weights.append(add(weights[-1],neg(a)))
    return rr,chain,weights


def character(n, h):
    rr,chain,weights = frame(n)
    vector = tuple(sum(a*w[j] for a,w in zip(h,weights)) for j in range(8))
    values = [dot(r,vector) for r in rr]
    if any(x.denominator != 1 for x in values): raise ValueError('nonintegral sl2 weights')
    out = Counter(map(int,values)); out[0] += 8
    return out


def decomposition(char):
    dims = []
    for m in range(max(char)+1):
        count = char[m]-char[m+2]
        if count: dims.append([m+1,count])
    return dims


# All blocks here lie in Q(i). The shared sqrt2 of a lift cancels in
# the factorization equation; Gram=2I checks its actual normalization.
Z=(Q(0),Q(0)); O=(Q(1),Q(0)); I=(Q(0),Q(1))
def gadd(a,b): return (a[0]+b[0],a[1]+b[1])
def gmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gscale(c,a): return (c*a[0],c*a[1])
def conj(a): return (a[0],-a[1])
def matrix(n): return [[Z for j in range(n)] for i in range(n)]
def identity(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def times(a,b):
    return [[sumg(gmul(a[i][k],b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sumg(values):
    out=Z
    for v in values: out=gadd(out,v)
    return out
def dagger(a): return [[conj(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]
def madd(a,b): return [[gadd(x,y) for x,y in zip(row,other)] for row,other in zip(a,b)]
def mscale(c,a): return [[gscale(c,x) for x in row] for row in a]
def kron(a,b): return [[gmul(x,y) for x in ar for y in br] for ar in a for br in b]
def block_diag(parts):
    out=matrix(sum(len(a) for a in parts)); start=0
    for a in parts:
        for i,row in enumerate(a):
            for j,x in enumerate(row): out[start+i][start+j]=x
        start+=len(a)
    return out
def encode(a): return [[[str(x),str(y)] for x,y in row] for row in a]


def run():
    checks={}
    def check(name,value): checks[name]=bool(value)
    new,old=character(6,(1,-1)*3),character(5,(4,2,0,-2,-4))
    idx=[sum(w*w*m for w,m in char.items())//2 for char in (new,old)]
    check('root weights reconstruct both dimensions', sum(new.values()) == sum(old.values()) == 248)
    check('positive symmetric weight multiplicities', all(m>0 and char[-w]==m for char in (new,old) for w,m in char.items()))
    check('exact distinct invariant pairings', idx == [180,1200])
    check('complete sl2 decompositions', all(sum(d*m for d,m in decomposition(c))==248 and all(m>0 for d,m in decomposition(c)) for c in (new,old)))
    rr,chain,weights=frame(6)
    for i,j in product(range(5),repeat=2):
        check(f'Cartan polarization {i}{j}', sum(dot(r,chain[i])*dot(r,chain[j]) for r in rr)==60*sum(dot(w,chain[i])*dot(w,chain[j]) for w in weights))
    remove=next(j for j,r in enumerate(rr) if dot(r,chain[0]))
    check('missing root changes trace control', sum(dot(r,chain[0])**2 for j,r in enumerate(rr) if j!=remove) != sum(dot(r,chain[0])**2 for r in rr))
    check('old centre erased', all(w%2==0 for w in old))
    check('new centre nontrivial in E8', sum(m*((-1)**w) for w,m in new.items()) == 24)
    a=[[I,Z],[Z,gscale(-1,I)]]; b=[[Z,O],[gscale(-1,O),Z]]
    s=block_diag([b,a,times(a,b)])
    aa=block_diag([mscale(-1,a),a,mscale(-1,a)])
    bb=block_diag([b,mscale(-1,b),mscale(-1,b)])
    check('literal simultaneous map', times(times(s,kron(identity(3),a)),dagger(s))==aa and times(times(s,kron(identity(3),b)),dagger(s))==bb)
    check('literal map unitary', times(s,dagger(s))==identity(6))
    check('literal quaternion centre retained', times(times(times(aa,bb),dagger(aa)),dagger(bb))==mscale(-1,identity(6)))
    permutations=((2,1,0),(0,2,1)); small=(madd(identity(2),a),madd(identity(2),mscale(-1,b)))
    families=[]
    for j,(perm,g) in enumerate(zip(permutations,small)):
        p=[[O if r==perm[c] else Z for c in range(3)] for r in range(3)]
        lift=kron(p,g); transport=times(times(dagger(s),lift),s)
        reduced=times(transport,kron(identity(3),dagger(g)))
        fm=[[gscale(Q(1,4),gadd(reduced[2*r][2*c],reduced[2*r+1][2*c+1])) for c in range(3)] for r in range(3)]
        check(f'actual family factor {j}', transport==kron(fm,g))
        check(f'lift normalization {j}', times(lift,dagger(lift))==mscale(2,identity(6)))
        check(f'family unitarity {j}', times(fm,dagger(fm))==identity(3))
        families.append(encode(fm))
    qchars=[]
    group=[identity(2),mscale(-1,identity(2)),a,mscale(-1,a),b,mscale(-1,b),times(a,b),mscale(-1,times(a,b))]
    for g in group:
        powers=[g,times(g,g),times(times(g,g),g)]
        traces=[3*(p[0][0][0]+p[1][1][0]) for p in powers]
        p1,p2,p3=traces
        qchars.append(int(10+p1*p1+3*(p1*p1-p2)+12*p1+(p1**3-3*p1*p2+2*p3)/3))
    check('complete Q8 character recovered', qchars==[248,24,28,28,28,28,28,28])
    check('Q8 invariant multiplicity recovered', sum(qchars)==8*55)
    check('registered primitive from both scale factors', 2*idx[0]*2==720 and 2*idx[1]*2==4800)
    records={'new_sl2_irreps':decomposition(new),'old_sl2_irreps':decomposition(old),
             'trace_indices':idx,'boundary_primitive_scale':2*idx[0]*2,
             'q8_characters':qchars,'family_moves':families,
             'new_full_weights':sorted([w,m] for w,m in new.items()),
             'old_full_weights':sorted([w,m] for w,m in old.items())}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'separate exact character and block safeguards, not outside physical acceptance'}


if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
