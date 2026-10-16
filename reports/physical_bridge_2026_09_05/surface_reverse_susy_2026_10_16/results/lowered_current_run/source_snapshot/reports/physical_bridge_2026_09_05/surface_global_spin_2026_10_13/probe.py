"""Full geometric transition/covariance checks; no physical kernel count."""
from functools import lru_cache
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def zero(m):
    if isinstance(m,s.MatrixBase):
        return all(s.trigsimp(s.simplify(s.expand_complex(v)))==0 for v in m)
    return s.trigsimp(s.simplify(s.expand_complex(m)))==0
def load(path):
    sp=importlib.util.spec_from_file_location('pinned_'+path.parent.name,path)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

@lru_cache(None)
def run():
    checks={}
    def ck(n,v):checks[n]=bool(v)
    geo=load(HERE.parent/'surface_parent_dictionary_2026_10_13/upstream_total_metric.py')
    cs=geo.gammas();I=s.eye(4)
    theta=s.Symbol('theta',real=True);C=s.cos(theta);S=s.sin(theta)
    KH,KV=cs[0]*cs[1],cs[2]*cs[3]
    G=KH+KV/2
    U=(C*I-S*KH)*(s.cos(theta/2)*I-s.sin(theta/2)*KV)
    K=-cs[1]/2+cs[0]*cs[2]*cs[3]/4
    Kcan=K+3*s.I*cs[0]/4
    R=s.diag(s.Matrix([[s.cos(2*theta),s.sin(2*theta)],[-s.sin(2*theta),s.cos(2*theta)]]),
             s.Matrix([[C,S],[-S,C]]))
    rotated=[sum((R[i,j]*cs[i] for i in range(4)),s.zeros(4)) for j in range(4)]
    grad=[-S*S,S*C,0,0]
    ck('unitary full spin lift',zero(U.H*U-I))
    for j in range(4):
        ck(f'actual Clifford transition {j}',zero(U*cs[j]*U.H-rotated[j]))
    source=sum((rotated[j]*G*grad[j] for j in range(4)),s.zeros(4))
    csource=sum((rotated[j]*(G+3*s.I*I/2)*grad[j] for j in range(4)),s.zeros(4))
    ck('whole ordinary differential covariance',zero(K-U*K*U.H-source))
    ck('whole canonical differential covariance',zero(Kcan-U*Kcan*U.H-csource))
    wrong=sum((rotated[j]*(G-3*s.I*I/2)*grad[j] for j in range(4)),s.zeros(4))
    ck('wrong R phase fails canonical covariance',not zero(Kcan-U*Kcan*U.H-wrong))
    vac=s.eye(4)[:,0]
    create=[(cs[0]-s.I*cs[1])/2,(cs[2]-s.I*cs[3])/2]
    F=s.Matrix.hstack(vac,create[0]*vac,create[1]*vac,create[0]*create[1]*vac)
    weights=[s.Rational(3,2),-s.Rational(1,2),s.Rational(1,2),-s.Rational(3,2)]
    cw=[w-s.Rational(3,2) for w in weights]
    ck('whole Fock spin generator',zero(F.H*(-G)*F-s.diag(*(s.I*w for w in weights))))
    ck('canonical exterior coefficient weights',cw==[0,-2,-1,-3])
    ck('spin central loop is not erased',zero(U.subs(theta,2*s.pi)+I))
    ck('R central loop is minus one',s.exp(-3*s.I*s.pi)==-1)
    ck('canonical central loop cancels',zero(-U.subs(theta,2*s.pi)-I))
    ck('geometric minusI spin square',zero(U.subs(theta,s.pi)**2+I))
    ck('geometric minusI canonical square',zero((s.I*U.subs(theta,s.pi))**2-I))
    ck('T geometric transition trivial',zero(U.subs(theta,0)-I))
    ck('omitted vertical rotation not a spin transition',not zero((C*I-S*KH)*cs[2]*(C*I-S*KH).H-rotated[2]))
    x,y,u,v=s.symbols('x y u v',real=True)
    yp=s.Symbol('yp',positive=True)
    # Substitute positive y before simplifying square roots of metric factors.
    y=yp;r2=x*x+y*y;r=s.sqrt(r2)
    coords=s.Matrix([x,y,u,v]);image=s.Matrix([-x/r2,y/r2,v,-u]);J=image.jacobian(coords)
    co=s.Matrix([[1/y,0,0,0],[0,1/y,0,0],[0,0,1/s.sqrt(y),x/s.sqrt(y)],[0,0,0,s.sqrt(y)]])
    transformed=co.subs(dict(zip(coords,image)),simultaneous=True)*J
    actualR=s.diag(s.Matrix([[(x*x-y*y)/r2,2*x*y/r2],[-2*x*y/r2,(x*x-y*y)/r2]]),
                   s.Matrix([[x/r,y/r],[-y/r,x/r]]))
    ck('S full coordinate coframe rotation',zero(transformed-actualR*co))
    tau=x+s.I*y
    hol=s.Matrix([[1,s.I,0,0],[v,s.I*v,1,tau]])
    hp=hol.subs(dict(zip(coords,image)),simultaneous=True)*J
    for a,b in combinations(range(4),2):
        ck(f'canonical frame determinant {a}{b}',zero(hp[:,[a,b]].det()-hol[:,[a,b]].det()/tau**3))
    dtheta=s.Matrix([-y/r2,x/r2,0,0]).T
    ar=s.Matrix([[3*s.I/(4*y),0,0,0]])
    arp=ar.subs(dict(zip(coords,image)),simultaneous=True)*J
    ck('actual Chern connection gauge law',zero(arp-ar-3*s.I*dtheta/2))
    ck('nonflat R line still retained',s.diff(3*s.I/(4*y),y)!=0)
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]])
    p13=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    p23=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    L=s.kronecker_product(p13,(s.eye(2)+a)/s.sqrt(2))
    RR=s.kronecker_product(p23,(s.eye(2)-b)/s.sqrt(2))
    SC=RR*L.H*RR
    ck('actual coefficient S square',zero(SC**2+s.eye(6)))
    ck('actual coefficient fourth power',zero(SC**4-s.eye(6)))
    ck('coefficient modular central relation',zero((SC*L)**3-SC**2))
    ck('inverse coefficient convention keeps fourth power',zero(SC.H**4-s.eye(6)))
    ck('ordinary full local6 loop is not cancelled',zero(s.kronecker_product(U.subs(theta,2*s.pi),SC**4)+s.eye(24)))
    ck('canonical full local6 loop cancels',zero(s.kronecker_product(-U.subs(theta,2*s.pi),SC**4)-s.eye(24)))
    ck('fibre puncture centre retained',zero(s.diag(-a,a,-a)*s.diag(b,-b,-b)*s.diag(-a,a,-a).H*s.diag(b,-b,-b).H+s.eye(6)))
    roster=load(HERE.parent/'weave_registered_embedding_2026_10_13/probe.py')
    actual,expected,char,_,_=roster.a5_roster()
    ck('whole E8 companions retained',actual==expected and sum(actual.values())==248)
    parities=[sum(m for w,m in char.items() if w%2==p) for p in range(2)]
    ck('whole adjoint central action not scalar',parities==[136,112])
    records={'spin_weights':[[int(w.p),int(w.q)] for w in weights],
             'canonical_weights':[int(w) for w in cw],
             'geometric_loop_signs':[-1,-1,1], 'coefficient_S_powers':[-1,1],
             'full_E8_central_parities':parities}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'geometric global transitions and separate local6 centre controls; not based coherence or physical index'}

if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));raise SystemExit(0 if r['all_passed'] else 1)
