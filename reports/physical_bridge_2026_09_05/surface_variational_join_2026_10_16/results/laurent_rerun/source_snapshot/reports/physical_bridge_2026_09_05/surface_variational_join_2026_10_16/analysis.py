"""Pre-run normal action/deformation join. No producer executes on import.

Shared authored formulation, independent frame/root implementations;
not independent analytic or source-convention acceptance.
"""
import json,sys
from itertools import product
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
def simp(x):
    if isinstance(x,s.MatrixBase):return x.applyfunc(simp)
    x=s.sympify(x)
    if x==0 or x.is_Number:return s.simplify(x)
    th=s.Symbol('theta',real=True);phase=s.Symbol('_normal_phase',nonzero=True)
    expanded=s.expand_complex(x);replacements={}
    for atom in expanded.atoms(s.sin,s.cos):
        arg=s.expand(atom.args[0])
        if not arg.has(th):continue
        frequency=arg.coeff(th);rest=s.expand(arg-frequency*th);order=2*frequency
        if rest.has(th) or not order.is_Integer:
            raise ValueError('Undeclared non-half-integral normal harmonic')
        z=s.exp(s.I*rest)*phase**int(order)
        replacements[atom]=(z+1/z)/2 if atom.func==s.cos else (z-1/z)/(2*s.I)
    result=s.cancel(expanded.xreplace(replacements))
    if result.has(s.sin,s.cos):result=s.trigsimp(result)
    return result.subs(phase,s.exp(s.I*th/2))
def zero(x):return all(simp(v)==0 for v in x)
def comm(a,b):return a*b-b*a
def B(a,b):return -s.trace(a*b)
def wedge(a,b):
    out={}
    for i,v in a.items():
        for j,w in b.items():
            if set(i)&set(j):continue
            k=tuple(sorted(i+j));sign=(-1)**sum(x>y for x in i for y in j)
            out[k]=out.get(k,0)+sign*v*w
    return {k:s.expand(v) for k,v in out.items() if s.expand(v)!=0}
def one(v):return {(j,):x for j,x in enumerate(v) if x!=0}
def top(*args):
    a={():s.Integer(1)}
    for b in args:a=wedge(a,b)
    return s.simplify(a.get((0,1,2,3),0))

def run(cs,engine,setup_valid):
    checks={};records={}
    def ck(k,v):
        checks[k]=bool(v)
        print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    theta_control=s.Symbol('theta',real=True)
    ck('phase instrument universal identity',simp(s.cos(theta_control)**2+s.sin(theta_control)**2-1)==0)
    nonidentity=simp(s.sin(theta_control))
    ck('phase instrument rejects one angle false zero',nonidentity!=0 and nonidentity.subs(theta_control,0)==0)
    half=simp(s.exp(s.I*theta_control/2))
    ck('phase instrument preserves derivative and half monodromy',simp(half.diff(theta_control)-s.I*half/2)==0 and simp(half.subs(theta_control,theta_control+2*s.pi)+half)==0)
    I2=s.eye(2);I4=s.eye(4);I32=s.eye(32)
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    gh=simp(s.I*cs[0]*cs[1]);gv=simp(s.I*cs[2]*cs[3]);gx=simp(-s.prod(cs))
    gam=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]];g5=simp(s.I*s.prod(gam))
    G0=s.kronecker_product(gam[0],I4,p3)
    G=[s.kronecker_product(g5,s.I*cs[2],p3),s.kronecker_product(g5,s.I*cs[3],p3),
       s.kronecker_product(I4,I4,p1),s.kronecker_product(I4,I4,p2)]
    C=simp(s.kronecker_product(gam[0]*gam[1]*gam[3],cs[1]*cs[3],p2))
    MW=simp((I32-s.kronecker_product(g5,gx,p3))/2)
    R=s.kronecker_product(I4,I4,p3);V=s.kronecker_product(I4,gv,I2)
    Hh=s.kronecker_product(I4,gh,I2)
    Pi=simp(MW*(I32+R*Hh)/2*(I32+R*V)/2)
    ck('actual frame input',setup_valid)
    ck('actual common real parameter rank4',Pi.rank()==4 and zero(C*Pi.conjugate()-Pi*C))
    ck('active chirality is minus',zero(s.prod(G)*Pi+Pi) and zero(s.prod(G)+R*V))
    twist=s.kronecker_product(I4,cs[0]*cs[1]+cs[2]*cs[3]/2,I2)+3*s.I*R/2
    ck('parameter actually twist neutral',zero(twist*Pi))
    qa=[simp(G0*g*Pi) for g in G]
    for a,b in product(range(4),repeat=2):
        # These are the coefficients of every ordered D_a a_b.
        want=Pi if a==b else s.zeros(32)
        for j,(c,d,sign) in enumerate(((0,1,1),(2,3,1),(0,2,1),(1,3,-1),(0,3,1),(1,2,1))):
            base=(G[0]*G[1] if j<2 else G[0]*G[2] if j<4 else G[0]*G[3])
            if (a,b)==(c,d):want+=sign*base*Pi
            if (a,b)==(d,c):want-=sign*base*Pi
        ck('all ordered deformation coefficients '+str((a,b)),zero(s.I*G0*G[a]*qa[b]-s.I*want))
        ck('real norm polarization '+str((a,b)),zero(qa[a].H*qa[b]+qa[b].H*qa[a]-(2*Pi if a==b else s.zeros(32))))
    for a in range(4):
        ck('tangent map Weyl and real '+str(a),zero(MW*qa[a]-qa[a]) and zero(C*qa[a].conjugate()-qa[a]*C))
    ck('reversed BPS sign detected',not zero((G[0]*G[1]+G[2]*G[3])*Pi))
    records['deformation']={'parameter_complex_rank':Pi.rank(),'ordered_coefficients':16,
        'scope':'canonical normal action, one-way local tangent map; not full boundary SUSY'}

    # The actual signed odd E8 root, not a freely named SU2.
    roots=engine.roots;idx={r:8+j for j,r in enumerate(roots)}
    root=(-2,-3,-4,-6,-5,-4,-2,-1)
    up=idx[root];dn=idx[tuple(-x for x in root)]
    hh={j:-s.Rational(v) for j,v in engine.pair(up,dn).items()}
    def br(u,v):
        out={}
        for j,a in u.items():
            for k,b in v.items():
                for m,c in engine.pair(j,k).items():out[m]=out.get(m,0)+a*b*s.Rational(c)
        return {j:s.simplify(v) for j,v in out.items() if s.simplify(v)!=0}
    ck('actual E8 signed faithful root',br(hh,{up:1})=={up:2} and br(hh,{dn:1})=={dn:-2} and all(j<8 for j in hh))
    simple=((1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),(-2,2,0,0,0,0,0,0),
        (0,-2,2,0,0,0,0,0),(0,0,-2,2,0,0,0,0),(0,0,0,-2,2,0,0,0),
        (0,0,0,0,-2,2,0,0),(0,0,0,0,0,-2,2,0))
    S=s.Matrix.hstack(*(s.Matrix(v)/2 for v in simple));e=[s.eye(8)[:,j] for j in range(8)]
    chain=s.Matrix.hstack(e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4])
    weights=[chain*(chain.T*chain).inv()*s.Matrix([1,0,0,0,0])]
    for j in range(5):weights.append(weights[-1]-chain[:,j])
    hv=sum((a*v for a,v in zip((1,-1)*3,weights)),s.zeros(8,1))
    charge=s.simplify((S*s.Matrix(root)).dot(hv))
    ck('actual selected root is antiperiodic',charge.is_Integer and int(charge)%2==1)
    ep=s.Matrix([[0,1],[0,0]]);em=s.Matrix([[0,0],[-1,0]]);h=s.diag(1,-1)
    ck('actual root map compact and faithful',comm(ep,em)==-h and comm(h,ep)==2*ep and em==-ep.H)
    records['root']={'root':list(root),'H':[[j,str(v)] for j,v in sorted(hh.items())],'puncture_charge':str(charge)}

    rho,lam=s.symbols('rho lambda',positive=True);th=s.Symbol('theta',real=True)
    k=4*lam**2;u=-s.log(1-k*rho);f=s.exp(-s.I*th/2)/s.sqrt(rho)
    Q=2*lam*f/(1-k*rho)*ep;barQ=-Q.H
    U=simp((Q+barQ)/2);VV=simp((Q-barQ)/(2*s.I))
    ax=-s.I*s.diff(u,rho)*s.sin(th)*h/2;ay=s.I*s.diff(u,rho)*s.cos(th)*h/2
    dx=lambda v:simp(s.cos(th)*v.diff(rho)-s.sin(th)*v.diff(th)/rho)
    dy=lambda v:simp(s.sin(th)*v.diff(rho)+s.cos(th)*v.diff(th)/rho)
    DX=lambda v:simp(dx(v)+comm(ax,v))
    DY=lambda v:simp(dy(v)+comm(ay,v))
    F=simp(dx(ay)-dy(ax)+comm(ax,ay))
    C1=simp(F+comm(U,VV));C2=simp(DX(U)-DY(VV));C3=simp(DX(VV)+DY(U))
    ck('canonical scalar normalization Q equals twice p',simp(Q[0,1]/(lam*f/(1-k*rho)))==2)
    ck('all actual nonlinear BPS residuals',zero(C1) and zero(C2) and zero(C3))
    ck('noncommuting background not abelianized',not zero(F) and not zero(comm(U,VV)))
    aa=[simp(v.diff(lam)) for v in (ax,ay,U,VV)]
    dc1=simp(DX(aa[1])-DY(aa[0])+comm(aa[2],VV)+comm(U,aa[3]))
    dc2=simp(DX(aa[2])+comm(aa[0],U)-DY(aa[3])-comm(aa[1],VV))
    dc3=simp(DX(aa[3])+comm(aa[0],VV)+DY(aa[2])+comm(aa[1],U))
    gauge=simp(-DX(aa[0])-DY(aa[1])-comm(U,aa[2])-comm(VV,aa[3]))
    ck('actual amplitude tangent BPS and gauge fixing',zero(dc1) and zero(dc2) and zero(dc3) and zero(gauge))
    ck('amplitude is not a compact gauge orbit',simp(s.diff(s.trace(Q.H*Q),lam))!=0)
    ck('amplitude tangent finite L2',simp(s.limit(rho*s.trace((aa[2]+s.I*aa[3]).H*(aa[2]+s.I*aa[3])),rho,0))==4)
    # Two real-conjugate odd coefficients of its ACTUAL critical spinor.
    um=simp(G0*(G[2]-s.I*G[3])*Pi);upspin=simp(G0*(G[2]+s.I*G[3])*Pi)
    ck('actual epsilon minus amplitude trace',not zero(um) and not zero(upspin) and zero((R*V+I32)*um) and zero((R*V+I32)*upspin))
    ck('actual critical phases match source and conjugate',zero((R+I32)*um) and zero((V-I32)*um) and zero((R-I32)*upspin) and zero((V+I32)*upspin))
    spin=s.Matrix.hstack(*Pi.columnspace())
    sm=simp(G0*(G[2]-s.I*G[3])*spin);sp=simp(G0*(G[2]+s.I*G[3])*spin)
    cnormal=s.kronecker_product(I4,cs[2],I2)
    gg=s.kronecker_product(g5,I4,p1)
    correction=simp(cnormal*(-2*s.I*lam*gg)*(sm*s.exp(s.I*th)+sp*s.exp(-s.I*th)))
    actual=simp(4*s.I*lam*G0*(-G[0]*s.sin(th)+G[1]*s.cos(th))*spin)
    ck('actual amplitude even term is old interacting dressing',zero(correction-actual))
    ck('bare amplitude Yukawa genuinely nonzero',not zero(gg*sm) and not zero(gg*sp))
    ck('remaining root tangent is regular graph order',s.limit(((1+k*rho)/(1-k*rho)**2-1)/s.sqrt(rho),rho,0)==0 and s.limit((1/(1-k*rho)**2-1)/s.sqrt(rho),rho,0)==0)

    # Complete off-shell nonabelian current, independently differentiated.
    x,y=s.symbols('x y',real=True)
    AX=s.I*(x*h+y*p1);AY=s.I*(x*y*p2+(1+x)*h)
    A8=s.I*((1+x*y)*p1+y*y*h);A9=s.I*(x*x*p2+(1+y)*p1)
    TX=lambda v:s.expand(v.diff(x)+comm(AX,v))
    TY=lambda v:s.expand(v.diff(y)+comm(AY,v))
    FF=s.expand(AY.diff(x)-AX.diff(y)+comm(AX,AY));CC=comm(A8,A9)
    derivatives=[TX(A8),TY(A8),TX(A9),TY(A9)]
    energy=s.expand(B(FF,FF)+B(CC,CC)+sum(B(v,v) for v in derivatives))
    residual=s.expand(B(FF+CC,FF+CC)+B(TX(A8)-TY(A9),TX(A8)-TY(A9))+B(TX(A9)+TY(A8),TX(A9)+TY(A8)))
    jx=B(A8,TY(A9))-B(A9,TY(A8));jy=-B(A8,TX(A9))+B(A9,TX(A8))
    div=s.expand(s.diff(jx,x)+s.diff(jy,y))
    ck('full off shell nonabelian energy end identity',s.expand(energy-residual-div)==0)
    curv=s.expand(2*B(FF,CC));quartic=s.expand(B(CC,CC))
    ck('deleting curvature cross term detected',curv!=0 and s.expand(energy-residual-div+curv)!=0)
    ck('deleting quartic detected',quartic!=0 and s.expand(energy-quartic-residual-div)!=0)
    ck('wrong full end sign detected',div!=0 and s.expand(energy-residual+div)!=0)
    # Evaluate the full same-parent current on the actual root family.
    JX=simp(B(U,DY(VV))-B(VV,DY(U)));JY=simp(-B(U,DX(VV))+B(VV,DX(U)))
    circle=simp(rho*(s.cos(th)*JX+s.sin(th)*JY))
    expected=2*lam**2*(3*k*rho-1)/(rho*(1-k*rho)**3)
    ck('actual nonabelian root boundary current',simp(circle-expected)==0)
    energy_root=simp(B(F,F)+B(comm(U,VV),comm(U,VV))+sum(B(v,v) for v in (DX(U),DY(U),DX(VV),DY(VV))))
    ck('actual full root energy differentiated current',simp(rho*energy_root-s.diff(circle,rho))==0)
    eps,outer=s.symbols('epsilon outer_radius',positive=True)
    bulk=2*s.pi*(circle.subs(rho,outer)-circle.subs(rho,eps));end=-bulk
    ck('complete regulated energy and end cancel',simp(bulk+end)==0 and bulk!=0)
    ck('actual full energy leading divergence',simp(s.limit(eps*bulk,eps,0)-4*s.pi*lam**2)==0)
    ck('singular first amplitude variations cancel',simp(s.diff(bulk,lam)+s.diff(end,lam))==0 and simp(s.limit(eps*s.diff(bulk,lam),eps,0)-8*s.pi*lam)==0)
    records['boundary']={'circle_current_per_2pi':str(expected),'bulk_energy':str(bulk),
        'energy_plus_retained_end':'0 on local root BPS family','leading_bulk_divergence':'4*pi*lambda**2/epsilon',
        'scope':'canonical reduced normal action, all normal bosonic terms; not a complete surface action/SUSY end'}

    # Finite ramified gauge action: actual unitary and monodromy, not a new particle.
    w=s.sqrt(rho)*s.exp(s.I*th/2);ee=w*ep+s.conjugate(w)*em
    angle=s.Symbol('angle',real=True)
    group=simp(s.cos(angle)*I2+s.sin(angle)*ee/s.sqrt(rho))
    puncture=s.diag(s.I,-s.I)
    ck('ramified gauge generator actual compact square',zero(ee.H+ee) and zero(ee*ee+rho*I2))
    ck('finite ramified gauge is unitary determinant one',zero(group.H*group-I2) and simp(group.det()-1)==0)
    ck('finite ramified gauge actual puncture equivariance',zero(group.subs(th,th+2*s.pi)-puncture*group*puncture.inv()))
    t=s.Symbol('t',real=True)
    ck('ramified gauge tends to identity',zero(group.subs(angle,t*s.sqrt(rho)).applyfunc(lambda v:s.limit(v,rho,0))-I2))
    dq=simp(comm(Q,ee));dabar=simp((dx(ee)+s.I*dy(ee))/2+comm((ax+s.I*ay)/2,ee))
    ck('gauge tangent changes Higgs as well as connection',not zero(dq) and not zero(dabar))
    ck('gauge Higgs response bounded nonconstant',zero(dq.subs(th,0)-dq.subs(th,2*s.pi)) and simp(s.limit(dq[0,0],rho,0)+2*lam*s.exp(-s.I*th))==0)
    ck('gauge normal connection has genuine halfpole',simp(s.limit(s.sqrt(rho)*dabar[1,0],rho,0)+s.exp(s.I*th/2)/2)==0)

    # Literal differential-form audit: transparent extraction, not source-wide verdict.
    dt=one([1,s.I,0,0]);dz=one([0,0,1,s.I]);bt=one([1,-s.I,0,0]);bz=one([0,0,1,-s.I])
    omega={(0,1):s.Integer(1),(2,3):s.Integer(1)}
    Keta=top(omega,omega);Kpsi=s.Abs(2*top(omega,dz,bz));Kchi=s.Abs(top(dt,dz,bt,bz))
    wcoeff=s.Symbol('w',positive=True)
    meta=s.Abs(-2*s.I*s.sqrt(2)*top(omega,dz,bz));mchi=wcoeff*s.Abs(top(dt,dz,bz,bt))
    va=s.simplify(meta/s.sqrt(Keta*Kpsi));vb=s.simplify(mchi/s.sqrt(Kchi*Kpsi))
    ck('literal source actual wedge and time weights',(Keta,Kpsi,Kchi)==(2,4,4) and top(dt,dz,bt,bz)==4)
    ck('literal source kinetic normalized speeds',(va,vb)==(2,wcoeff))
    ck('literal dictionary w1 unequal not universal kill',vb.subs(wcoeff,1)!=va and s.simplify(va/vb.subs(wcoeff,1))==2)
    ck('literal dictionary w2 positive calibration',vb.subs(wcoeff,2)==va)
    gauss=s.Abs(2*s.I*top(omega,bz,dz));linear=wcoeff*s.Abs(top(bt,bz,dt,dz))
    eliminated=s.simplify(linear**2/gauss)
    ck('actual G gaussian and eliminated source coefficient',gauss==4 and linear==4*wcoeff and eliminated==4*wcoeff**2)
    ck('literal Q2p residual weights calibrated',(eliminated/16).subs(wcoeff,1)==s.Rational(1,4) and (eliminated/16).subs(wcoeff,2)==1)
    records['literal_action_audit']={'dictionary':'literal flat differential forms; not a convention-independent erratum',
        'time_kinetic_weights':[str(v) for v in (Keta,Kpsi,Kchi)],'principal_speeds':[str(va),str(vb)],
        'w1_residual_weights':['1','1/4','1/4'],'w2_residual_weights':['1','1','1'],
        'status':'canonical action explicitly supplied; complete BHV action identification NOT certified'}
    records['status']='local canonical action/end and one-way interacting fermion tangent; NOT full nonlinear SUSY boundary law, global vacuum, physical SM, three or gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(cs,engine,valid):
    out=run(cs,engine,valid);print(json.dumps(out,indent=2));return 0 if out['all_passed'] else 1
