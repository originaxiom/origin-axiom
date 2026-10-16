"""Pre-run actual completed-source/Hessian map; no science on import."""
import importlib.util,json,sys
from itertools import product
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod);return mod
source=load(HERE.parent/'surface_source_operator_2026_10_16/analysis.py','weighted_source')
clean=source.clean;zero=source.zero;sparse=source.sparse
def bracket(a,b):return a*b-b*a
def pair(a,b):return -s.trace(a*b)
def run(cs,valid):
    checks={};records={}
    def ck(k,v):
        checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    I2=s.eye(2);I4=s.eye(4);I32=s.eye(32)
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    gam=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]];g5=clean(s.I*s.prod(gam))
    G0=s.kronecker_product(gam[0],I4,p3)
    Gall=[s.kronecker_product(g5,s.I*c,p3) for c in cs]+[s.kronecker_product(I4,I4,p1),s.kronecker_product(I4,I4,p2)]
    G=[Gall[j] for j in (2,3,4,5)]
    C=clean(s.kronecker_product(gam[0]*gam[1]*gam[3],cs[1]*cs[3],p2))
    MW=clean((I32-s.kronecker_product(g5,-s.prod(cs),p3))/2)
    L=s.Matrix.hstack(*((I4+g5)/2).columnspace())
    W=s.Matrix.hstack(*[s.kronecker_product(L,s.eye(4)[:,i],s.eye(2)[:,r]) for i,r in ((3,1),(1,0),(2,0),(0,1))])
    S=W.row_join(C*W.conjugate());Bn=clean(S.T*C.H*S)
    eta=clean(W[:,:2]*W[:,:2].H+(C*W[:,:2].conjugate())*(C*W[:,:2].conjugate()).H)
    R=s.kronecker_product(I4,I4,p3)
    Hh=s.kronecker_product(I4,s.I*cs[0]*cs[1],I2)
    V=s.kronecker_product(I4,s.I*cs[2]*cs[3],I2)
    Pi=clean(MW*(I32+R*Hh)/2*(I32+R*V)/2)
    t=s.Symbol('t',positive=True)
    T=clean(I32+(1/t-1)*eta+(t-1)*(MW-eta))
    ck('actual frame supplied',valid)
    ck('actual full normalized MW frame',zero(S.H*S-s.eye(16)) and zero(S*S.H-MW))
    ck('parameter IS actual eta projector',Pi.rank()==4 and zero(Pi-eta) and zero(C*Pi.conjugate()-Pi*C))
    can=[clean(s.kronecker_product(-s.I*S.T*C.H*G0*g*S,source.J)) for g in Gall]
    base=[source.source_internal(j,s.Integer(2),1,1,s.Integer(1)) for j in range(6)]
    phases,why=source.phase_map(base,can)
    ck('actual favourable chiral phase map REQUIRED',phases is not None and why is None and all(clean(a-b)==0 for a,b in zip(phases,(1,-s.I,-s.I,1))))
    Bfull=s.kronecker_product(Bn,s.eye(source.NC))
    ck('actual graded signed time REQUIRED',zero(source.source_time(1)-s.I*s.kronecker_product(Bn,source.J)))
    # Use the displayed fixed phases even if the independently recovered map fails.
    # A failure then stays a false check; it cannot skip the physical comparison.
    ph=(1,-s.I,-s.I,1);U=s.diag(*[v for a in list(ph)+[s.conjugate(x) for x in ph] for v in [a]*(2*source.NC)])
    Ui=U.inv();variable=[source.source_internal(j,2*t*t,1,1,s.Integer(1)) for j in range(6)]
    H=[];printed=[]
    for j,a in enumerate(variable):
        aligned=clean(Ui.T*source.complete(a)*Ui)
        hj=clean(-Bfull*aligned)
        h16=s.Matrix(16,16,lambda i,k:hj[i*source.NC,k*source.NC+1])
        h32=clean(S*h16*S.H);H.append(h32)
        ck('actual aligned source completion coefficient '+str(j),zero(h32-T*(s.I*G0*Gall[j])*T*MW))
        printed.append(clean((Ui.T*a*Ui-can[j]).subs(t,1)))
    oldwitness=next(([j,source.witness(a)] for j,a in enumerate(printed) if not zero(a)),None)
    ck('printed conjugate remains distinct nonzero control',oldwitness is not None)
    q=[clean(G0*g*Pi) for g in G]
    O=[Pi,clean(G[0]*G[1]*Pi),clean(G[0]*G[2]*Pi),clean(G[0]*G[3]*Pi)]
    weights=[1,1,t*t,t*t]
    for j,o in enumerate(O):
        want=1/t if j<2 else t
        ck('actual weighted output eta type '+str(j),zero(T*o-want*o))
    for a,b in product(range(4),repeat=2):
        ck('actual q real kinetic polarization '+str((a,b)),zero(q[a].H*q[b]+q[b].H*q[a]-(2*Pi if a==b else s.zeros(32))))
        ck('actual output real polarization '+str((a,b)),zero(O[a].H*O[b]+O[b].H*O[a]-(2*Pi if a==b else s.zeros(32))))
        want=Pi if a==b else s.zeros(32)
        for j,(c,d,sign) in enumerate(((0,1,1),(2,3,1),(0,2,1),(1,3,-1),(0,3,1),(1,2,1))):
            k=j//2+1
            if (a,b)==(c,d):want+=sign*weights[k]*O[k]
            if (a,b)==(d,c):want-=sign*weights[k]*O[k]
        ck('actual completed source ordered derivative '+str((a,b)),zero(H[(2,3,4,5)[a]]*q[b]-s.I*want))
    for j in range(4):
        ck('actual q reality and common T '+str(j),zero(C*q[j].conjugate()-q[j]*C) and zero(T*q[j]-t*q[j]))
    weighted_gram=[[clean((weights[j]*O[j]).H*(weights[k]*O[k])+(weights[k]*O[k]).H*(weights[j]*O[j])) for k in range(4)] for j in range(4)]
    for j,k in product(range(4),repeat=2):
        ck('full weighted quadratic norm '+str((j,k)),zero(weighted_gram[j][k]-(2*weights[j]**2*Pi if j==k else s.zeros(32))))
    ck('complex cross terms not silently zero',not zero(O[0].H*O[1]) and zero(O[0].H*O[1]+O[1].H*O[0]))
    ck('canonical t1 recovered',zero(T.subs(t,1)-I32))
    ck('printed weight changes nonzero Hessian',s.simplify((t**4-1).subs(t,1/s.sqrt(2)))==-s.Rational(3,4))

    # Noncommuting polynomial fields retain full quartic/curvature/end, off shell.
    x,y=s.symbols('x y',real=True)
    AX=s.I*(x*p3+y*p1);AY=s.I*(x*y*p2+(1+x)*p3)
    UU=s.I*((1+x*y)*p1+y*y*p3);VV=s.I*(x*x*p2+(1+y)*p1)
    DX=lambda a:s.expand(a.diff(x)+bracket(AX,a))
    DY=lambda a:s.expand(a.diff(y)+bracket(AY,a))
    F=s.expand(AY.diff(x)-AX.diff(y)+bracket(AX,AY));UV=bracket(UU,VV)
    C1=F+UV;C2=DX(UU)-DY(VV);C3=DX(VV)+DY(UU)
    residual=s.expand(pair(C1,C1)+t**4*(pair(C2,C2)+pair(C3,C3)))
    gradient=sum(pair(a,a) for a in (DX(UU),DY(UU),DX(VV),DY(VV)))
    extra=s.expand(2*(1-t**4)*pair(F,UV))
    E=s.expand(pair(F,F)+pair(UV,UV)+t**4*gradient+extra)
    jx=pair(UU,DY(VV))-pair(VV,DY(UU));jy=-pair(UU,DX(VV))+pair(VV,DX(UU))
    div=s.expand(s.diff(jx,x)+s.diff(jy,y))
    ck('full weighted nonlinear energy end identity',s.expand(E-residual-t**4*div)==0)
    ck('weighted curvature omission detected',extra!=0 and s.expand(E-extra-residual-t**4*div)!=0)
    ck('weighted end omission detected',div!=0 and s.expand(E-residual)!=0)
    ck('weighted quartic omission detected',pair(UV,UV)!=0 and s.expand(E-pair(UV,UV)-residual-t**4*div)!=0)

    # Exact second variation at a nonzero commuting BPS background.
    z=s.Symbol('variation',real=True)
    bg=[s.I*k*p3 for k in (1,2,3,5)]
    aa=[s.I*p1,s.I*p2,s.I*(p1+p2),s.I*(p1-p2)]
    def residuals(A):
        return [bracket(A[0],A[1])+bracket(A[2],A[3]),
            bracket(A[0],A[2])-bracket(A[1],A[3]),
            bracket(A[0],A[3])+bracket(A[1],A[2])]
    cc=residuals([b+z*a for b,a in zip(bg,aa)])
    dc=[a.diff(z).subs(z,0) for a in cc]
    potential=s.expand(pair(cc[0],cc[0])+t**4*(pair(cc[1],cc[1])+pair(cc[2],cc[2])))
    norm=s.expand(pair(dc[0],dc[0])+t**4*(pair(dc[1],dc[1])+pair(dc[2],dc[2])))
    gf=-sum((bracket(b,a) for b,a in zip(bg,aa)),s.zeros(2))
    ck('nonzero BPS control all residuals vanish',all(zero(a.subs(z,0)) for a in cc) and all(not zero(a) for a in bg))
    ck('actual BPS Hessian half second variation',s.expand(potential.diff(z,2).subs(z,0)/2-norm)==0 and norm!=0 and pair(gf,gf)!=0)
    bad=residuals([s.zeros(2),s.zeros(2),(1+z)*s.I*p1,(1+z)*s.I*p2])
    bv=s.expand(sum(pair(a,a) for a in bad));linear=sum(pair(a.diff(z).subs(z,0),a.diff(z).subs(z,0)) for a in bad)
    remainder=s.expand(bv.diff(z,2).subs(z,0)/2-linear)
    ck('nonBPS Hessian squared linearization false control',remainder!=0 and bv.subs(z,0)!=0)

    lam,rho,eps,outer=s.symbols('lambda rho epsilon outer_radius',positive=True)
    k=4*lam**2;b=2*lam**2*(3*k*rho-1)/(rho*(1-k*rho)**3)
    bulk=t**4*2*s.pi*(b.subs(rho,outer)-b.subs(rho,eps));end=-bulk
    ck('both weighted root ends retained',s.simplify(bulk+end)==0 and bulk!=0)
    ck('weighted root divergence and variation',s.limit(eps*bulk,eps,0)==4*s.pi*lam**2*t**4 and s.simplify(s.diff(bulk+end,lam))==0)
    records['maps']={'eta_and_parameter_projector':sparse(Pi),'actual_aligned_completed_H_six':[sparse(a) for a in H],
        'q_four':[sparse(a) for a in q],'outputs_four':[sparse(a) for a in O],
        'weights':[str(a) for a in weights],'ordered_derivatives':16,'real_norm_weights':['1','1','t**4','t**4']}
    records['source']={'explicit_required_chiral_phases':None if phases is None else [str(a) for a in phases],
        'printed_conjugate_witness':oldwitness,'scope':'Hermitian completion ONLY, not the unmatched full printed source'}
    records['variation']={'BPS_half_Hessian':str(norm),'gauge_fix_norm':str(pair(gf,gf)),
        'nonBPS_extra_Hessian_coefficient':str(remainder),'scope':'actual supplied residual functional, stationary BPS only'}
    records['end']={'curvature_coefficient':'2*(1-t**4)','bulk_divergence':'4*pi*lambda**2*t**4/epsilon',
        'scope':'both local annulus ends; credited root profile/current not independently rederived'}
    records['status']='conditional local quadratic boson/completed-fermion/end join; not full printed action/nonlinear SUSY/global spectrum/SM/three/gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(cs,valid):
    data=run(cs,valid);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
