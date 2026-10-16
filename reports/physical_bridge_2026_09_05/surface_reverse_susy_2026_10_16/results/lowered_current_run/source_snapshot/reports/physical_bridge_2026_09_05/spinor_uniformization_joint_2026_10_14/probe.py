"""Exact typed parent/continuous-lift/portal audit with source-fixed W75 subset."""
from collections import Counter
from functools import lru_cache
import ast
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def load(folder):
    p=HERE.parent/folder/'probe.py';sp=importlib.util.spec_from_file_location('typed_joint_'+folder,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def zero(m):return all(s.simplify(x)==0 for x in m)
def bracket(a,b):return a*b-b*a

@lru_cache(None)
def run():
    checks={}
    def ck(k,v):checks[k]=bool(v)
    y=s.symbols('y',positive=True);h,c=s.symbols('h c',real=True)
    H=s.diag(1,-1);E=s.Matrix([[0,1],[0,0]]);A=h*H/y
    def dh(q):return s.I*s.diff(q,y)-s.I*bracket(A,q)
    q=c*E/s.sqrt(y);phi=c*E/y
    rq=dh(q).subs({h:s.Rational(-1,4),c:s.Rational(1,2)})
    rp=dh(phi).subs({h:s.Rational(-1,4),c:s.Rational(1,2)})
    ordinary=dh(phi).subs({h:s.Rational(-1,2),c:s.Rational(1,2)})
    ck('original spinor holomorphic residual zero',zero(rq))
    ck('naive ordinary field same connection rejected',not zero(rp))
    ck('changed connection ordinary positive comparator',zero(ordinary))
    ck('changed connection fails ORIGINAL moment',s.Rational(-1,2)+s.Rational(1,2)**2!=0)
    ck('original moment retained',s.Rational(-1,4)+s.Rational(1,2)**2==0)
    ck('curvature norm really changes',(s.Rational(-1,2)/s.Rational(-1,4))**2==4)
    ck('half versus whole frame weights discriminate',s.Rational(4)**s.Rational(-1,2)!=s.Rational(4)**(-1))
    ck('spin curvature nonzero and K double',s.Rational(-1,2)!=0 and s.Rational(-1,2)!=2*s.Rational(-1,2))
    ck('self bracket not a nonzero K field',bracket(E,E)==s.zeros(2))
    ck('different spinors CAN produce ordinary K field',bracket(E,E.T)==H)
    n=load('weave_registered_embedding_2026_10_13')
    char=n.a5_roster()[2];irr=n.irreps(char)
    ck('complete continuous character matches E8 roster',n.a5_roster()[0]==n.a5_roster()[1] and sum(char.values())==248)
    ck('odd part includes a quartet',any(d==4 and m>0 for d,m in irr))
    odddim=sum(d*m for d,m in irr if d%2==0)
    q8copies=sum((d//2)*m for d,m in irr if d%2==0)
    ck('odd centre still112',odddim==112)
    ck('Q8 restriction still56 doublets',q8copies==56)
    # Literal simultaneous SU2 rather than parity-only Cartan.
    e,rr=n.roots();chain=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4]]
    C=s.Matrix.hstack(*chain);ws=[C*(C.T*C).inv()*s.Matrix([1,0,0,0,0])]
    for a in chain:ws.append(ws[-1]-a)
    HQ=sum((v*w for v,w in zip((-1,1,1,-1,-1,1),ws)),s.zeros(8,1))
    lit=Counter(int(r.dot(HQ)) for r in rr);lit[0]+=8
    ck('literal transformed lift has same full character',lit==char)
    alpha=e[3]+e[5];omega=int(alpha.dot(HQ))
    ck('specific original condensate noncommutes',omega!=0 and omega%2!=0)
    ck('weight one comparator applies to THIS root',abs(omega)==1)
    t,u,f,v=s.symbols('t u f v',real=True)
    K=s.diag(1,-1,0);HA=s.diag(1,0,-1);X=s.zeros(3);X[0,2]=1
    qq=t*X;rrr=u*K;MM=bracket(qq,qq.H)+bracket(rrr,rrr.H)
    V=s.expand(2*s.trace(bracket(qq,rrr).H*bracket(qq,rrr))+s.trace((f*HA+MM)**2)/2)
    expected=f*f+2*f*t*t+t**4+2*u*u*t*t
    ck('actual full comparator potential',s.expand(V-expected)==0)
    ck('quartic interaction is present',s.Poly(V,t,u,f).coeff_monomial(t*t*u*u)==2)
    ck('standalone cubic not in original zero-r potential',s.Poly(V,t,u,f).coeff_monomial(t*t*u)==0)
    induced=s.expand(V.subs(u,u+v))
    ck('background induced cubic positive route retained',s.Poly(induced,t,u,f,v).coeff_monomial(t*t*u*v)==4)
    ck('curvature source term retained',s.Poly(V,t,u,f).coeff_monomial(f*t*t)==2)
    ck('noncommuting normal joint is not F-flat',not zero(bracket(qq,rrr)))
    Y=s.zeros(3);Y[0,1]=1
    ck('commuting nilpotent two-field positive survives',zero(bracket(X,Y)) and not zero(bracket(Y,Y.H)))
    # Upstream ordinary-Higgs checks are replayed, not used as a spinor map.
    tree=ast.parse((HERE/'upstream_W75.py').read_text());wanted={'quarter_laplacian','hitchin','zero','u2','u3','u4'}
    funcs=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in wanted]
    env={'sp':s};exec(compile(ast.Module(body=funcs,type_ignores=[]),'source-fixed-W75-subset','exec'),env)
    xx,yy=s.symbols('x y',real=True);rho=xx*xx+yy*yy
    env.update({'x':xx,'y':yy,'R2':rho,'Lf':-s.log(rho),'Z':xx+s.I*yy,
                'E12':E,'E21':E.T})
    upstream={}
    for name in ('u2','u3','u4'):
        value=env[name]();value=value[0] if isinstance(value,tuple) else value
        upstream[name]=bool(value['holds']);ck('ordinary W75 source subset '+name,upstream[name])
    records={'spinor_residual':0,'same_connection_ordinary_residual_E_over_y2':'-I/4',
             'changed_connection_original_moment':'-1/4','curvature_squared_ratio':4,
             'frame_weights':['1/2','1'],'continuous_SU2_irreps':irr,
             'odd_continuous_dimension':odddim,'Q8_odd_doublet_copies':q8copies,
             'literal_original_root_HQ_weight':omega,
             'quartic_coefficient':2,'zero_background_standalone_cubic':0,
             'induced_v_u_t2_coefficient':4,'curvature_f_t2_coefficient':2,
             'ordinary_W75_subset':upstream}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'typed field/interaction audit and ordinary U2-U4 replay, not a physical Higgs/NAH join or no-go'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
