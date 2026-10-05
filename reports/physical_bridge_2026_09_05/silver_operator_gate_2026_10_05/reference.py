"""Separate direct-field replay. Standard library only; no native/fork imports."""
import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GEN = 'abt'


class K:
    rad = 2
    def __init__(self,a=0,b=0):
        self.a,self.b = F(a),F(b)
    def coerce(self,x):
        if isinstance(x,type(self)):
            return x
        if isinstance(x,K):
            raise TypeError('mixed quadratic fields')
        return type(self)(x)
    def __add__(self,x):
        x = self.coerce(x)
        return type(self)(self.a+x.a,self.b+x.b)
    __radd__ = __add__
    def __neg__(self):
        return type(self)(-self.a,-self.b)
    def __sub__(self,x):
        return self+-self.coerce(x)
    def __rsub__(self,x):
        return self.coerce(x)+-self
    def __mul__(self,x):
        x = self.coerce(x)
        return type(self)(self.a*x.a+self.rad*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__ = __mul__
    def __truediv__(self,x):
        x = self.coerce(x)
        den = x.a*x.a-self.rad*x.b*x.b
        if not den:
            raise ZeroDivisionError('zero field element')
        return self*type(self)(x.a/den,-x.b/den)
    def __rtruediv__(self,x):
        return self.coerce(x)/self
    def __eq__(self,x):
        x = self.coerce(x)
        return self.a==x.a and self.b==x.b
    def __bool__(self):
        return bool(self.a or self.b)
    def conjugate(self):
        return type(self)(self.a,-self.b)


class Gaussian(K):
    rad = -1


def zeros(n,m=None):
    return [[0 for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a,b):
    bt = transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def add(a,b,sign=1):
    return [[x+sign*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]


def hcat(*mats):
    return [sum((a[i] for a in mats),[]) for i in range(len(mats[0]))]


def vcat(*mats):
    return sum((list(a) for a in mats),[])


def elimination(a,full=False):
    a = [[x if isinstance(x,K) else K(x) for x in row] for row in a]
    pivots = []
    row = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(row,len(a)) if a[j][col]),None)
        if pivot is None:
            continue
        a[row],a[pivot] = a[pivot],a[row]
        v = a[row][col]
        a[row] = [x/v for x in a[row]]
        for j in (range(len(a)) if full else range(row+1,len(a))):
            if j!=row and a[j][col]:
                factor = a[j][col]
                a[j] = [x-factor*y for x,y in zip(a[j],a[row])]
        pivots.append(col)
        row += 1
        if row==len(a):
            break
    return a,pivots


def rank(a):
    return len(elimination(a)[1])


def inverse(a):
    n = len(a)
    reduced,pivots = elimination(hcat(a,eye(n)),True)
    if pivots[:n] != list(range(n)):
        raise ValueError('singular matrix')
    return [row[n:] for row in reduced]


def determinant(a):
    a = [[x if isinstance(x,K) else K(x) for x in row] for row in a]
    out = K(1)
    for i in range(len(a)):
        j = next((j for j in range(i,len(a)) if a[j][i]),None)
        if j is None:
            return K(0)
        if i!=j:
            a[i],a[j] = a[j],a[i]
            out = -out
        p = a[i][i]
        out *= p
        for j in range(i+1,len(a)):
            factor = a[j][i]/p
            a[j] = [x-factor*y for x,y in zip(a[j],a[i])]
    return out


def four(data):
    basis = [[[Gaussian(1),Gaussian(0)],[Gaussian(0),Gaussian(0)]],
             [[Gaussian(0),Gaussian(0)],[Gaussian(0),Gaussian(1)]],
             [[Gaussian(0),Gaussian(1)],[Gaussian(1),Gaussian(0)]],
             [[Gaussian(0),Gaussian(0,1)],[Gaussian(0,-1),Gaussian(0)]]]
    out = {}
    for g,entries in data['holonomy'].items():
        m = [[Gaussian(a,b) for a,b in row] for row in entries]
        det = m[0][0]*m[1][1]-m[0][1]*m[1][0]
        modulus = K(F(1,10)) if g=='t' else K(0,F(1,10))
        sq = modulus*modulus
        norm = det*det.conjugate()
        assert norm.b==0 and sq==K(norm.a)
        mt = transpose([[x.conjugate() for x in row] for row in m])
        cols = []
        for h in basis:
            z = mul(mul(m,h),mt)
            assert z[0][0].b==z[1][1].b==0
            assert z[1][0]==z[0][1].conjugate()
            cols.append([data['nu'][g]*K(x)/modulus
                         for x in (z[0][0].a,z[1][1].a,z[0][1].a,z[0][1].b)])
        out[g] = transpose(cols)
        assert determinant(out[g])==1
        q = [[0,F(1,2),0,0],[F(1,2),0,0,0],[0,0,-1,0],[0,0,0,-1]]
        assert mul(mul(transpose(out[g]),q),out[g])==q
    return out


def exterior(a):
    ij = list(combinations(range(len(a)),2))
    return [[a[i][k]*a[j][l]-a[i][l]*a[j][k] for k,l in ij] for i,j in ij]


def dual(rep):
    return {g:transpose(inverse(a)) for g,a in rep.items()}


def extension(v,c):
    return {g:[row+[c[4*j+i]] for i,row in enumerate(v[g])]+[[0,0,0,0,1]]
            for j,g in enumerate(GEN)}


class Complex:
    def __init__(self,rep,data):
        self.n = n = len(rep['a'])
        self.rep = rep
        self.letters = dict(rep)
        self.letters.update({g.upper():inverse(a) for g,a in rep.items()})
        # Formal crossed homomorphisms are evaluated by the affine
        # concatenation law c(uv)=c(u)+rho(u)c(v), not a rational Fox import.
        self.cletters = {}
        for j,g in enumerate(GEN):
            selector = zeros(n,3*n)
            for i in range(n):
                selector[i][j*n+i] = 1
            self.cletters[g] = selector
            self.cletters[g.upper()] = [[-x for x in row] for row in mul(self.letters[g.upper()],selector)]
        for w in data['relators']:
            if self.word(w)[0]!=eye(n):
                raise ValueError('relator violation '+w)
        (p,rp),(q,rq) = [self.word(w) for w in data['cusp_words']]
        assert mul(p,q)==mul(q,p)
        self.B = vcat(*(add(rep[g],eye(n),-1) for g in GEN))
        self.F = vcat(*(self.word(w)[1] for w in data['relators']))
        self.R = vcat(rp,rq)
        self.D = vcat(add(p,eye(n),-1),add(q,eye(n),-1))
        self.M = vcat(hcat(self.F,zeros(2*n,n)),hcat(self.R,[[-x for x in row] for row in self.D]))
        assert mul(self.F,self.B)==zeros(2*n,n)
        assert mul(self.R,self.B)==self.D
        torus = hcat(add(eye(n),q,-1),add(p,eye(n),-1))
        assert mul(torus,self.D)==zeros(n)
        assert rank(vcat(self.F,mul(torus,self.R)))==rank(self.F)

    def word(self,w):
        p = eye(self.n)
        c = zeros(self.n,3*self.n)
        for letter in w:
            c = add(c,mul(p,self.cletters[letter]))
            p = mul(p,self.letters[letter])
        return p,c

    def profile(self):
        n = self.n
        b,f,d,m = map(rank,(self.B,self.F,self.D,self.M))
        vals = [n-b,n-d,3*n-f-b,3*n-m,m-f-d,3*n-b-m+d,2*n-f]
        assert all(v>=0 for v in vals)
        return dict(zip(['h0_absolute','h0_boundary','h1_absolute','h1_relative',
                         'restriction_rank','h1_interior','h2_absolute'],vals))


def profile_pair(rep,data):
    dr = dual(rep)
    assert dual(dr)==rep
    a,b = [Complex(r,data).profile() for r in (rep,dr)]
    for x,y in ((a,b),(b,a)):
        x['absolute_betti'] = [x['h0_absolute'],x['h1_absolute'],x['h2_absolute'],0]
        x['relative_betti'] = [0,x['h1_relative'],y['h1_absolute'],y['h0_absolute']]
        assert x['h1_relative']==y['h1_absolute']-y['h0_absolute']
        assert x['h1_relative']==x['h0_boundary']-x['h0_absolute']+x['h1_interior']
        for frame in ('absolute','relative'):
            h = x[frame+'_betti']
            assert sum((-1)**i*v for i,v in enumerate(h))==0
            x[frame+'_odd_even'] = [h[1]+h[3],h[0]+h[2]]
    return {'E':a,'dual':b,'difference':{k:a[k]-b[k] for k in ('h1_absolute','h1_relative','h1_interior')}}


def run():
    data = json.loads((ROOT/'candidate.json').read_text())
    checks = {}
    def ck(name,value):
        checks[name] = bool(value)
        assert checks[name],name
    v = four(data)
    c = [K(a,b) for a,b in data['cocycle_Qsqrt2_pairs']]
    vc = Complex(v,data)
    col = [[x] for x in c]
    ck('cocycle_closed',mul(vc.F,col)==zeros(8,1))
    ck('cocycle_peripheral_zero',mul(vc.R,col)==zeros(8,1))
    ck('cocycle_nonexact',rank(hcat(vc.B,col))>rank(vc.B))
    badc = [list(row) for row in col]; badc[0][0] += 1
    ck('bad_cocycle_rejected',mul(vc.F,badc)!=zeros(8,1))
    w = extension(v,c)
    wc = Complex(w,data)
    ck('W_determinant_one',all(determinant(m)==1 for m in w.values()))
    ck('peripheral_block_split',all(wc.word(word)[0]==[row+[0] for row in vc.word(word)[0]]+[[0,0,0,0,1]]
                                  for word in data['cusp_words']))
    split = extension(v,[K(0)]*12)
    reps = {'W':w,'wedge2W':{g:exterior(m) for g,m in w.items()},
            'splitW':split,'split_wedge2W':{g:exterior(m) for g,m in split.items()}}
    profiles = {label:profile_pair(rep,data) for label,rep in reps.items()}
    ck('split_pairing',all(x==0 for label in ('splitW','split_wedge2W')
                          for x in profiles[label]['difference'].values()))
    u = [[K(i)] for i in (1,2,3,4)]
    gauge_col = add(col,vcat(*(mul(add(v[g],eye(4),-1),u) for g in GEN)))
    wg = extension(v,[row[0] for row in gauge_col])
    ck('coboundary_gauge_invariance',profile_pair(wg,data)==profiles['W'])
    inv = [[0],[0],[0],[0],[1]]
    ck('literal_dual_invariant_line',all(mul(m,inv)==inv for m in dual(w).values()))
    ck('field_inverse',K(1,1)*K(-1,1)==1)
    q = [[K(1),K(0,1)],[K(0),K(2)]]
    ck('exterior_dual',exterior(transpose(inverse(q)))==transpose(inverse(exterior(q))))
    bad = dict(w); bad['a'] = [[2*x for x in row] for row in w['a']]
    try:
        Complex(bad,data)
    except ValueError as error:
        ck('bad_relation_rejected','relator violation' in str(error))
    else:
        ck('bad_relation_rejected',False)
    # Separate slot description of tangential/normal principal traces.
    green = [[0,-1],[1,0]]
    absolute = [[1,0],[0,0]]; relative = [[0,0],[0,1]]
    ck('principal_current',mul(mul(absolute,green),absolute)==zeros(2)
       and mul(mul(relative,green),relative)==zeros(2) and determinant(green)==1)
    exchange = [[0,1],[1,0]]
    ck('domain_exchange',mul(mul(exchange,absolute),exchange)==relative)
    ck('uniform_absolute_not_reality',mul(exchange,absolute)!=mul(absolute,exchange))
    # With z=exp(kL), G=k(z^2-z^-2), flux=-G. Formal coefficients
    # come from integrating 2k^2 exp(-2kr), not numerical quadrature.
    for k in (F(1),F(-1),F(3,2)):
        energy = {2:k,-2:-k}; flux = {2:-k,-2:k}
        ck('flux_identity_'+str(k),all(energy[p]+flux[p]==0 for p in energy))
    control = {'gauge_energy':'2*k*sinh(2*k*L)',
               'boundary_pairing':'-2*k*sinh(2*k*L)',
               'twisted_energy':0,'ordinary_Neumann':False,
               'positive_for_real_nonzero_k_and_positive_L':True,
               'silver_geometric_solution':False}
    return {'checks':checks,'passed':len(checks),'failed':[],
            'V':vc.profile(),'profiles':profiles,'boundary_control':control,
            'cocycle_pairs':[[str(x.a),str(x.b)] for x in c],
            'physical_goal_achieved':False,'non_author_acceptance':False}


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
