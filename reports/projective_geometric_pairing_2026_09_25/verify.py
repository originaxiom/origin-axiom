"""F14 exact geometric candidates and intertwiners; analytic bridge separate."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import importlib.util
import sympy as s

ROOT=Path(__file__).parent.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


f12=load('f14_f12',ROOT/'projective_global_metric_2026_09_21'/'verify.py')
f05=load('f14_f05',ROOT/'parent_twist_gap_2026_09_20'/'verify.py')
field=f12.f11
f11=field.v
f10=f12.f10
q,z,L,beta,k=f12.q,f12.z,f12.L,f12.beta,f12.k
CANDIDATES={
    'id':('m','n',1,1),
    'T':('n','m',1,1),
    'theta':('M','N',-1,1),
    'thetaT':('N','M',-1,1),
    'R+':('M','nMN',-1,-1),
    'R-':('M','NMn',-1,-1),
    'G+':('m','nmN',1,-1),
    'G-':('m','Nmn',1,-1),
}
LONGITUDE='nMNmmNMn'


def clean(a):
    return a.applyfunc(lambda x:s.factor(s.cancel(x)))


def geo_clean(a):
    return a.applyfunc(lambda x:s.simplify(s.expand_complex(x)))


def inverse_word(w):
    return w.swapcase()[::-1]


def substitute(w,images):
    return ''.join(images['mn'.index(c)] if c.islower()
                   else inverse_word(images['mn'.index(c.lower())]) for c in w)


def word(w,matrices,geometric=False):
    out=s.eye(matrices[0].rows)
    letters={g:a for g,a in zip('mn',matrices)}
    letters.update({g.upper():a.inv() for g,a in zip('mn',matrices)})
    simplify=geo_clean if geometric else clean
    for c in w:
        out=simplify(out*letters[c])
    return out


def geometry():
    u=(1+s.I*s.sqrt(3))/2
    m=s.Matrix([[1,1],[0,1]])
    n=s.Matrix([[1,0],[u,1]])
    d=s.diag(-1,1)
    swap=s.Matrix([[0,1],[u,0]])
    plus=s.Matrix([[1,s.conjugate(u)],[0,1]])
    minus=s.Matrix([[1,-s.conjugate(u)],[0,1]])
    # Conjugator, antiholomorphic flag, positive power, Gamma word for that power.
    maps={'id':(s.eye(2),False,1,''),'T':(swap,False,2,''),
          'theta':(d,False,2,''),'thetaT':(d*swap,False,2,''),
          'R+':(plus*d,True,4,LONGITUDE),
          'R-':(minus*d,True,4,inverse_word(LONGITUDE)),
          'G+':(plus,True,2,'m'),'G-':(minus,True,2,'M')}
    return (m,n),maps


def psl_equal(a,b):
    ratio=geo_clean(a*b.inv())
    return ratio[0,0]!=0 and geo_clean(ratio-ratio[0,0]*s.eye(2))==s.zeros(2)


def isometry_power(matrix,anti,power):
    out=s.eye(2)
    parity=False
    for _ in range(power):
        out=geo_clean(out*(matrix.conjugate() if parity else matrix))
        parity ^= anti
    return out,parity


@lru_cache(None)
def geometric_certificate(name):
    rho,maps=geometry()
    matrix,anti,power,powerword=maps[name]
    images=CANDIDATES[name][:2]
    matches=[]
    for a,w in zip(rho,images):
        lhs=geo_clean(matrix*(a.conjugate() if anti else a)*matrix.inv())
        matches.append(psl_equal(lhs,word(w,rho,True)))
    raised,parity=isometry_power(matrix,anti,power)
    return {'name':name,'orientation':-1 if anti else 1,
            'generator_actions':all(matches),'power':power,'power_word':powerword,
            'power_in_Gamma':not parity and psl_equal(raised,word(powerword,rho,True)),
            'conjugator':matrix}


def intertwiner_equations(left,right):
    n=left[0].rows
    # Row-major vectorization: vec(B X-X A)=(B tensor I-I tensor A^T) vec(X).
    return s.Matrix.vstack(*(s.kronecker_product(b,s.eye(n))-
                             s.kronecker_product(s.eye(n),a.T)
                             for b,a in zip(left,right)))


@lru_cache(None)
def candidate_certificate(middle,name):
    p=q*q-middle*q+1
    rho=f10.generators()
    source=tuple(word(w,rho) for w in CANDIDATES[name][:2])
    target=tuple(clean(a.inv().T) for a in rho)
    equations=field.reduce_matrix(intertwiner_equations(target,source),p)
    null=field.kernel(equations,p)
    result={'middle':middle,'name':name,'dimension':null.cols,'rank':16-null.cols}
    if null.cols:
        matrix=null[:,0].reshape(4,4)
        determinant=f12.determinant_field(matrix,p)
        result.update({'matrix':matrix,'determinant':determinant,
          'entrywise':all(field.reduce_matrix(b*matrix-matrix*a,p)==s.zeros(4)
                         for b,a in zip(target,source))})
    return result


@lru_cache(None)
def generic_inversion():
    rho=f10.generators()
    source=tuple(clean(a.inv()) for a in rho)
    target=tuple(a.T for a in source)
    null=intertwiner_equations(target,source).nullspace()
    matrices=tuple(clean(a.reshape(4,4)) for a in null)
    return matrices


def phase_factor(phase,name,antilinear=False):
    exponent=CANDIDATES[name][2]
    return s.simplify(phase**(1-exponent if antilinear else 1+exponent))


def cusp_reflector():
    r=s.eye(4)
    r.row_swap(0,3)
    return r


def cusp_centralizer():
    n,p,d,h=f10.cusp_generators()
    pi=s.diag(0,1,0,0)
    a,b,c,e=s.symbols('a b c d')
    u=s.symbols('u',positive=True)
    zmat=a*s.eye(4)+b*n+c*p+e*pi
    inv=s.eye(4)/a-b*n/a**2+(b*b/a**3-c/a**2)*p+(1/(a+e)-1/a)*pi
    scale=s.diag(s.sqrt(u),1,1,1/s.sqrt(u))
    return (n,p,d,h,pi),(a,b,c,e,u),zmat,inv,scale


def volume_pairing():
    pairs=tuple(combinations(range(4),2))
    return s.Matrix(6,6,lambda i,j:s.LeviCivita(*pairs[i],*pairs[j]))


def parent_weyl():
    eye=s.eye(8)
    roots=(eye[:,0]+eye[:,5],eye[:,0]-eye[:,5],
           eye[:,6]+eye[:,7],eye[:,6]-eye[:,7])
    out=s.eye(8)
    for root in roots:
        out=out*(s.eye(8)-2*root*root.T/(root.dot(root)))
    return out,roots


if __name__=='__main__':
    for name in CANDIDATES:
        print('GEOMETRY',geometric_certificate(name),flush=True)
    for middle in (14,34):
        for name in CANDIDATES:
            print('FIELD',candidate_certificate(middle,name),flush=True)
    for matrix in generic_inversion():
        print('GENERIC_THETA',matrix,'determinant',s.factor(matrix.det()),flush=True)
