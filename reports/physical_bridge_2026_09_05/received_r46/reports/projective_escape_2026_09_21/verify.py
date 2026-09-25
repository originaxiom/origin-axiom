"""F10 exact holonomy and local PDE checks; no global harmonic solve."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import sympy as s

q, z, length = s.symbols('q z L', positive=True)
beta, kappa = s.symbols('beta kappa', real=True)


def clean(m):
    return m.applyfunc(lambda x: s.factor(s.cancel(x)))


@lru_cache(None)
def generators(parameter=q):
    t = parameter/2
    return (s.Matrix([[1,0,1,t-1],[0,1,1,t],[0,0,1,t+s.Rational(1,2)],[0,0,0,1]]),
            s.Matrix([[1,0,0,0],[2+1/t,1,0,0],[2,1,1,0],[1,1,0,1]]))


def word(text, matrices):
    a,b = matrices
    letters = {'m':a,'n':b,'M':a.inv(),'N':b.inv()}
    out = s.eye(4)
    for letter in text:
        out = clean(out*letters[letter])
    return out


@lru_cache(None)
def longitude(parameter=q):
    return word('nMNmmNMn', generators(parameter))


def cusp_generators():
    n = s.zeros(4)
    n[0,2] = n[2,3] = 1
    p = n*n
    return n,p,s.diag(1,-3,1,1),s.diag(1,0,0,-1)


def normal_form(parameter=q):
    n,p,d,_ = cusp_generators()
    b = 6/(parameter-1/parameter)
    return s.eye(4)+n+n*n/2, s.diag(parameter,parameter**-3,parameter,parameter)*(s.eye(4)+b*p)


@lru_cache(None)
def cusp_conjugator():
    m,_ = generators()
    ell = longitude()
    a = q**-3-q
    projector = clean(((ell-q*s.eye(4))/a)**2)
    n = clean(m-s.eye(4)-(m-s.eye(4))**2/2)
    p3 = clean((s.eye(4)-projector)*s.eye(4)[:,3])
    return clean(s.Matrix.hstack(n*n*p3, projector*s.eye(4)[:,0], n*p3,p3))


def center_balanced():
    path = Path(__file__).parent.parent/'balanced_parent_2026_09_20'/'verify.py'
    spec = importlib.util.spec_from_file_location('f10_f08', path)
    f08 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f08)
    u = (1+s.I*s.sqrt(3))/2
    a,b = s.Matrix([[1,1],[0,1]]),s.Matrix([[1,0],[u,1]])
    return tuple(f08.balanced_group(g) for g in (a,b))


def intertwiner(left, right):
    xs = s.symbols('p0:16')
    p = s.Matrix(4,4,xs)
    equations = [e for a,b in zip(left,right) for e in a*p-p*b]
    matrix = s.linear_eq_to_matrix(equations,xs)[0]
    return tuple(s.Matrix(4,4,v) for v in matrix.nullspace())


def local_connection(wrong_radial=False):
    n,p,d,h = cusp_generators()
    u = z*z/4 if wrong_radial else z*z/4-beta*beta/length**2
    f = s.sqrt(u)  # declared real positive on the cusp tail
    return (-n/f, -kappa*d-beta*p/u, s.diff(u,z)*h/(2*u))


def local_flat(c):
    # Only z dependence. All entries real in the stated tail domain.
    out = []
    for i in range(3):
        for j in range(i+1,3):
            derivative = (c[j].diff(z) if i==2 else s.zeros(4))-(c[i].diff(z) if j==2 else s.zeros(4))
            out.append(s.simplify(derivative+c[i]*c[j]-c[j]*c[i]))
    return tuple(out)


def local_moment(c):
    weights = (1,length**-2,1)
    out = z**3*((c[2]+c[2].T)/z).diff(z)
    out += z*z*sum((weights[i]*(c[i]*c[i].T-c[i].T*c[i]) for i in range(3)),s.zeros(4))
    return s.simplify(out)


def local_norm_density(c):
    psi = tuple((x+x.T)/2 for x in c)
    return s.factor(length/z*sum(w*s.trace(x*x) for w,x in zip((1,length**-2,1),psi)))


def torus_complex(m, ell):
    x,y = m-s.eye(4),ell-s.eye(4)
    return x.col_join(y), (-y).row_join(x)


def torus_homotopy(ell):
    yinv = (ell-s.eye(4)).inv()
    return s.zeros(4).row_join(yinv), (-yinv).col_join(s.zeros(4))
