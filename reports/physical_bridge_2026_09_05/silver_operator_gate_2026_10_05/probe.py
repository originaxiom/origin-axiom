"""Fixed coefficient, exact rational restriction and principal boundary gate."""
import json
from itertools import combinations
from pathlib import Path

import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parent
RT = s.sqrt(2)
GEN = 'abt'


def marked_relators():
    images = {'a':'a','b':'b'}
    for letter in reversed('LLRR'):
        step = {'a':'ab','b':'b'} if letter=='L' else {'a':'a','b':'ba'}
        images = {g:''.join(step[c] for c in w) for g,w in images.items()}
    images = {g:w.upper() for g,w in images.items()}
    return ['t'+g+'T'+images[g].swapcase()[::-1] for g in 'ab']


def clean(m):
    return m.applyfunc(s.expand)


def rank(m):
    return DomainMatrix.from_Matrix(m).convert_to(s.QQ).rank()


def inverse(m):
    return DomainMatrix.from_Matrix(m).convert_to(s.QQ).inv().to_Matrix()


def pairs(x):
    x = s.expand(x)
    b = x.coeff(RT)
    a = s.expand(x-b*RT)
    if not (a.is_Rational and b.is_Rational):
        raise ValueError('outside Q(sqrt2)')
    return a, b


def restrict(m):
    out = s.zeros(2*m.rows, 2*m.cols)
    for i in range(m.rows):
        for j in range(m.cols):
            a,b = pairs(m[i,j])
            out[2*i:2*i+2, 2*j:2*j+2] = s.Matrix([[a,2*b],[b,a]])
    return out


def dual(rep):
    n = rep['a'].rows
    t = s.diag(*([2,4]*(n//2)))
    return {g: inverse(t)*inverse(m).T*t for g,m in rep.items()}


def wedge(m):
    ij = list(combinations(range(m.rows),2))
    return s.Matrix([[s.expand(m[i,k]*m[j,l]-m[i,l]*m[j,k])
                      for k,l in ij] for i,j in ij])


def four(data):
    basis = [s.diag(1,0), s.diag(0,1), s.Matrix([[0,1],[1,0]]),
             s.Matrix([[0,s.I],[-s.I,0]])]
    metric = s.Matrix([[0,s.Rational(1,2),0,0], [s.Rational(1,2),0,0,0],
                       [0,0,-1,0],[0,0,0,-1]])
    out = {}
    for g,entries in data['holonomy'].items():
        m = s.Matrix([[s.Rational(a)+s.I*s.Rational(b) for a,b in row] for row in entries])
        modulus = s.sqrt(s.expand(m.det()*s.conjugate(m.det())))
        cols = []
        for h in basis:
            z = (m*h*m.conjugate().T/modulus).applyfunc(s.simplify)
            cols.append(s.Matrix([z[0,0],z[1,1],(z[0,1]+z[1,0])/2,
                                  (z[0,1]-z[1,0])/(2*s.I)]).applyfunc(s.simplify))
        a = s.Matrix.hstack(*cols)
        restrict(a)
        assert s.simplify(a.det()) == 1
        assert clean(a.T*metric*a-metric) == s.zeros(4)
        out[g] = data['nu'][g]*a
    return out


def extension(v,c):
    return {g:v[g].row_join(c[4*j:4*j+4,:]).col_join(s.zeros(1,4).row_join(s.ones(1)))
            for j,g in enumerate(GEN)}


class Complex:
    def __init__(self,rep,data):
        self.n = n = rep['a'].rows
        self.letters = dict(rep)
        self.letters.update({g.upper():inverse(m) for g,m in rep.items()})
        for word in data['relators']:
            if self.evaluate(word) != s.eye(n):
                raise ValueError('relator violation '+word)
        p,q = [self.evaluate(w) for w in data['cusp_words']]
        assert p*q == q*p
        self.B = s.Matrix.vstack(*(rep[g]-s.eye(n) for g in GEN))
        self.F = s.Matrix.vstack(*(self.fox(w) for w in data['relators']))
        self.R = s.Matrix.vstack(*(self.fox(w) for w in data['cusp_words']))
        self.D = s.Matrix.vstack(p-s.eye(n),q-s.eye(n))
        self.M = self.F.row_join(s.zeros(2*n,n)).col_join(self.R.row_join(-self.D))
        assert self.F*self.B == s.zeros(2*n,n)
        assert self.R*self.B == self.D
        tr = (s.eye(n)-q).row_join(p-s.eye(n))
        assert tr*self.D == s.zeros(n)
        assert rank(self.F.col_join(tr*self.R)) == rank(self.F)

    def evaluate(self,w):
        out = s.eye(self.n)
        for letter in w:
            out = out*self.letters[letter]
        return out

    def fox(self,w):
        p = s.eye(self.n)
        blocks = [s.zeros(self.n) for _ in GEN]
        for letter in w:
            j = GEN.index(letter.lower())
            if letter.islower():
                blocks[j] += p
                p = p*self.letters[letter]
            else:
                p = p*self.letters[letter]
                blocks[j] -= p
        return s.Matrix.hstack(*blocks)

    def profile(self):
        n = self.n
        b,f,d,m = [rank(a) for a in (self.B,self.F,self.D,self.M)]
        raw = [n-b,n-d,3*n-f-b,3*n-m,m-f-d,3*n-b-m+d,2*n-f]
        assert all(v>=0 and v%2==0 for v in raw)
        keys = ['h0_absolute','h0_boundary','h1_absolute','h1_relative',
                'restriction_rank','h1_interior','h2_absolute']
        return dict(zip(keys,[v//2 for v in raw]))


def profile_pair(rep,data):
    dr = dual(rep)
    assert dual(dr) == rep
    a,b = [Complex(r,data).profile() for r in (rep,dr)]
    for x,y in ((a,b),(b,a)):
        x['absolute_betti'] = [x['h0_absolute'],x['h1_absolute'],x['h2_absolute'],0]
        x['relative_betti'] = [0,x['h1_relative'],y['h1_absolute'],y['h0_absolute']]
        assert x['h1_relative'] == y['h1_absolute']-y['h0_absolute']
        assert x['h1_relative'] == x['h0_boundary']-x['h0_absolute']+x['h1_interior']
        for frame in ('absolute','relative'):
            h = x[frame+'_betti']
            assert h[0]-h[1]+h[2]-h[3] == 0
            x[frame+'_odd_even'] = [h[1]+h[3],h[0]+h[2]]
    diff = {k:a[k]-b[k] for k in ('h1_absolute','h1_relative','h1_interior')}
    return {'E':a,'dual':b,'difference':diff}


def boundary_matrices():
    # Basis indexed by wedge-mask in dx,dy,dr order, normal dr.
    e = s.zeros(8)
    for mask in range(8):
        if not mask&4:
            e[mask|4,mask] = (-1)**((mask&3).bit_count())
    green = e-e.T
    pa = s.diag(*[int(not (mask&4)) for mask in range(8)])
    pr = s.eye(8)-pa
    star = s.zeros(8)
    for mask in range(8):
        left = [i for i in range(3) if mask&(1<<i)]
        right = [i for i in range(3) if not mask&(1<<i)]
        seq = left+right
        sign = (-1)**sum(seq[i]>seq[j] for i in range(3) for j in range(i+1,3))
        degree = len(left)
        star[7^mask,mask] = sign*([1,-1,-1,1][degree])
    parity = s.diag(*[(-1)**mask.bit_count() for mask in range(8)])
    return green,pa,pr,star,parity


def boundary_control():
    k,L = s.symbols('k L',real=True,nonzero=True)
    r = s.symbols('r',real=True)
    u = s.exp(-k*r)
    energy = s.integrate(s.diff(u,r)**2+k**2*u**2,(r,-L,L))
    flux = k*(u.subs(r,L)**2-u.subs(r,-L)**2)
    assert s.simplify(energy+flux) == 0
    assert s.diff(u,r)+k*u == 0
    assert s.simplify((energy-2*k*s.sinh(2*k*L)).rewrite(s.exp)) == 0
    return {'gauge_energy':'2*k*sinh(2*k*L)',
            'boundary_pairing':'-2*k*sinh(2*k*L)',
            'twisted_energy':0,'ordinary_Neumann':False,
            'positive_for_real_nonzero_k_and_positive_L':True,
            'silver_geometric_solution':False}


def run():
    data = json.loads((ROOT/'candidate.json').read_text())
    v = four(data)
    c = s.Matrix([s.Rational(a)+RT*s.Rational(b) for a,b in data['cocycle_Qsqrt2_pairs']])
    vc = Complex({g:restrict(m) for g,m in v.items()},data)
    cr = s.Matrix([x for entry in c for x in pairs(entry)])
    checks = {}
    def ck(name,value):
        checks[name] = bool(value)
        assert checks[name],name
    ck('free_word_marking',data['relators']==marked_relators() and data['cusp_words']==['abAB','abt'])
    ck('cocycle_closed',vc.F*cr == s.zeros(vc.F.rows,1))
    ck('cocycle_peripheral_zero',vc.R*cr == s.zeros(vc.R.rows,1))
    ck('cocycle_nonexact',rank(vc.B.row_join(cr)) > rank(vc.B))
    changed = cr.copy(); changed[0] += 1
    ck('bad_cocycle_rejected',vc.F*changed != s.zeros(vc.F.rows,1))
    w = extension(v,c)
    wc = Complex({g:restrict(m) for g,m in w.items()},data)
    ck('W_determinant_one',all(s.simplify(m.det())==1 for m in w.values()))
    ck('peripheral_block_split',all(wc.evaluate(word)==s.diag(vc.evaluate(word),s.eye(2))
                                    for word in data['cusp_words']))
    split = extension(v,s.zeros(12,1))
    reps = {'W':w,'wedge2W':{g:wedge(m) for g,m in w.items()},
            'splitW':split,'split_wedge2W':{g:wedge(m) for g,m in split.items()}}
    profiles = {label:profile_pair({g:restrict(m) for g,m in rep.items()},data)
                for label,rep in reps.items()}
    ck('split_pairing',all(x==0 for label in ('splitW','split_wedge2W')
                          for x in profiles[label]['difference'].values()))
    u = s.Matrix([1,2,3,4])
    gauge_c = c+s.Matrix.vstack(*((v[g]-s.eye(4))*u for g in GEN))
    wg = extension(v,gauge_c)
    ck('coboundary_gauge_invariance',profile_pair({g:restrict(m) for g,m in wg.items()},data)==profiles['W'])
    dr = dual({g:restrict(m) for g,m in w.items()})
    inv = s.zeros(10,1); inv[8] = 1
    ck('literal_dual_invariant_line',all(m*inv==inv for m in dr.values()))
    q = s.Matrix([[1,RT],[0,2]])
    ck('field_dual',dual({'a':restrict(q)})['a']==restrict(q.inv().T))
    ck('wrong_field_dual_rejected',inverse(restrict(q)).T != restrict(q.inv().T))
    bad = {g:restrict(m) for g,m in w.items()}; bad['a'] *= 2
    try:
        Complex(bad,data)
    except ValueError as error:
        ck('bad_relation_rejected','relator violation' in str(error))
    else:
        ck('bad_relation_rejected',False)
    green,pa,pr,j,parity = boundary_matrices()
    ck('principal_current_nondegenerate',green.det()==1)
    ck('absolute_relative_current',pa*green*pa==s.zeros(8) and pr*green*pr==s.zeros(8))
    ck('trace_half_dimension',pa.rank()==pr.rank()==4)
    ck('degree_parity',pa*parity==parity*pa and pr*parity==parity*pr)
    ck('combined_reality_square',j*j==s.eye(8))
    ck('combined_reality_domain_exchange',j*pa*j==pr and j*pr*j==pa)
    ck('uniform_absolute_not_reality',j*pa!=pa*j)
    control = boundary_control()
    ck('Robin_flux_identity',control['twisted_energy']==0)
    ck('dual_flux_even',s.simplify((-2*(-s.Symbol('k'))*s.sinh(-2*s.Symbol('k')*s.Symbol('L')))-(-2*s.Symbol('k')*s.sinh(2*s.Symbol('k')*s.Symbol('L'))))==0)
    return {'checks':checks,'passed':len(checks),'failed':[],
            'V':vc.profile(),'profiles':profiles,'boundary_control':control,
            'cocycle_strings':[str(x) for x in c],
            'physical_goal_achieved':False,'non_author_acceptance':False}


if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
