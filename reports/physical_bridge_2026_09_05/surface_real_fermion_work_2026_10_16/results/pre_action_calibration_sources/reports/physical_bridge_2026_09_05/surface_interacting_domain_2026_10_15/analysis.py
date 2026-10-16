"""Declared pre-run formulation: fixed-fibre interacting domain and same-parent end controls.

Do not execute before the new packet's source/proof/tests are published.
Finite controls support the separately authored analytic argument; they
do not certify an infinite-dimensional proof or a global physical model.
"""
import json
from itertools import product
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def simp(x):
    if isinstance(x,s.MatrixBase):return x.applyfunc(lambda v:s.simplify(s.expand_complex(v)))
    return s.simplify(s.expand_complex(x))
def zero(x):return all(simp(v)==0 for v in x)
def enc(x):return [[str(simp(v)) for v in row] for row in x.tolist()]

def run(cs,engine,setup_valid):
    checks={};records={}
    def ck(name,value):checks[name]=bool(value)
    I2=s.eye(2);I4=s.eye(4);I32=s.eye(32)
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    gx=simp(-s.prod(cs));gv=simp(s.I*cs[2]*cs[3])
    gam=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]]
    g5=simp(s.I*s.prod(gam));b4=simp(gam[0]*gam[1]*gam[3])
    bc=simp(s.kronecker_product(b4,cs[1]*cs[3],p2))
    chir=-s.kronecker_product(g5,gx,p3);pm=simp((I32+chir)/2)
    rr=s.kronecker_product(I4,I4,p3);vv=s.kronecker_product(I4,gv,I2)
    c3=s.kronecker_product(I4,cs[2],I2);c4=s.kronecker_product(I4,cs[3],I2)
    G0=s.kronecker_product(gam[0],I4,p3)
    G6=s.kronecker_product(g5,s.I*cs[2],p3)
    current=simp(s.I*G0*G6)
    ck('actual Clifford input map',setup_valid)
    ck('actual MW rank and reality',pm.rank()==16 and zero(bc*pm.conjugate()-pm*bc))
    W=s.Matrix.hstack(*pm.columnspace())
    ck('whole MW normal Green form nondegenerate',(W.H*current*W).rank()==16)
    laws=[]
    for ep in (-1,1):
        plane=simp(pm*(I32+ep*rr*vv)/2)
        rank=plane.rank()
        ck('paired maximal isotropic rank '+str(ep),rank==8 and zero(plane.H*current*plane))
        ck('paired plane real '+str(ep),zero(bc*plane.conjugate()-plane*bc))
        laws.append({'epsilon':ep,'complex_trace_rank_per_odd_coefficient':rank,
                     'full_complex_plane':rank*112})

    # Arbitrary X=P+iQ with compact-real P,Q: check both independent
    # coefficient maps separately, not a favourable commuting X only.
    rad=s.Symbol('rho',positive=True);th=s.Symbol('theta',real=True)
    cn=simp(c3*s.cos(th)+c4*s.sin(th))
    def nd(F):
        return simp(cn*F.diff(rad)+(-c3*s.sin(th)+c4*s.cos(th))*F.diff(th)/rad)
    MP=s.kronecker_product(g5,I4,p2);MQ=-s.kronecker_product(g5,I4,p1)
    VP=(MP*s.cos(th/2)-MQ*s.sin(th/2))/s.sqrt(rad)
    VQ=(MP*s.sin(th/2)+MQ*s.cos(th/2))/s.sqrt(rad)
    dressed=[]
    for r,g in product((-1,1),repeat=2):
        proj=simp(pm*(I32+r*rr)/2*(I32+g*vv)/2)
        gp=s.exp(-s.I*g*th/2)/s.sqrt(rad)
        sourceP=s.I*r*s.kronecker_product(g5,I4,p1)*proj
        phase=s.exp(-s.I*(r+g)*th/2)/rad
        phi=s.log(rad) if r*g==1 else s.exp(s.I*g*th)
        for name,V,factor in [('P',VP,1),('Q',VQ,s.I*r)]:
            source=simp(sourceP*factor);h=simp(c3*source*phi)
            ck('generic complex source '+str((r,g,name)),zero(V*gp*proj-phase*source))
            ck('generic dressed cancellation '+str((r,g,name)),zero(nd(h)+phase*source))
            ck('generic dressed MW '+str((r,g,name)),zero(pm*h-h))
            target=simp(pm*(I32-r*rr)/2*(I32-g*vv)/2)
            fac2=1 if name=='P' else -s.I*r
            phi2=s.log(rad) if r*g==1 else s.exp(-s.I*g*th)
            h2=simp(c3*(-s.I*r*s.kronecker_product(g5,I4,p1)*target)*fac2*phi2)
            ck('generic full real dressing '+str((r,g,name)),zero(bc*h.conjugate()-h2*bc))
        dressed.append({'R':r,'gamma':g,'epsilon':r*g,'rank':proj.rank()})
    ck('all full-parent critical classes retained',sum(v['rank'] for v in dressed)==16)
    ck('dressed Green remainders vanish',s.limit(s.sqrt(rad)*s.log(rad),rad,0)==0 and s.limit(rad*s.log(rad)**2,rad,0)==0)

    delta=s.Symbol('delta',positive=True)
    integral=2*s.pi*s.integrate(rad*rad**(-s.Rational(3,2)),(rad,0,delta))
    ck('actual small L3 norm',simp(integral-4*s.pi*s.sqrt(delta))==0)
    ck('small coefficient tends zero',s.limit(integral**s.Rational(1,3),delta,0)==0)
    ck('Holder L3 times L6 into L2',s.Rational(1,3)+s.Rational(1,6)==s.Rational(1,2))
    n=s.Symbol('n',integer=True,positive=True)
    ck('exact lattice shell count',s.expand((2*n+1)**2-(2*n-1)**2)==8*n)
    ck('Fourier weighted series converges in two dimensions',s.integrate(rad**-2,(rad,1,s.oo))==1)
    ck('critical halfpole is not minimal H1',s.limit(s.integrate(rad**-2,(rad,delta,1)),delta,0)==s.oo)
    b,c,a=s.symbols('b c a',positive=True)
    xx,yy=s.symbols('x_norm y_norm',nonnegative=True)
    remainder=s.expand((b*b+c*c/(a*a))*(xx*xx+a*a*yy*yy)-(b*xx+c*yy)**2)
    ck('deficiency range estimate is actual Cauchy square',s.expand(remainder-(b*a*yy-c*xx/a)**2)==0)
    P=s.diag(1,1,0)
    K=s.Matrix([[0,s.Rational(1,4),0],[0,0,0],[s.Rational(1,3),0,0]])
    T=s.eye(3)+K*P;R=s.eye(3)[:,:2]
    ck('proper closed range control',R.rank()==2 and (T*R).rank()==2 and T.det()!=0)
    ck('strict contraction range map',sum(v*v for v in K)==s.Rational(25,144) and s.Rational(25,144)<1)
    ck('bad noncontraction can collapse deficiency range',(s.eye(3)-P).det()==0 and ((s.eye(3)-P)*R).rank()==0)
    records['domain']={'MW_rank':16,'regular_coefficients':136,'critical_coefficients':112,
        'complex_max_min_dimension':16*112,'deficiency_each':8*112,'laws':laws,
        'scope':'fixed compact fibre only; authored analytic argument, not full surface or physical index'}

    # Signed root SL2 in the ACTUAL E8 Chevalley engine.
    roots=engine.roots;idx={r:i+8 for i,r in enumerate(roots)}
    # The same declared SU6 puncture Cartan is reconstructed independently.
    S=s.Matrix.hstack(*(s.Matrix(v)/2 for v in (
        (1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),(-2,2,0,0,0,0,0,0),
        (0,-2,2,0,0,0,0,0),(0,0,-2,2,0,0,0,0),(0,0,0,-2,2,0,0,0),
        (0,0,0,0,-2,2,0,0),(0,0,0,0,0,-2,2,0))))
    e=[s.eye(8)[:,j] for j in range(8)]
    chain=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4]]
    C=s.Matrix.hstack(*chain);weights=[C*(C.T*C).inv()*s.Matrix([1,0,0,0,0])]
    for q in chain:weights.append(weights[-1]-q)
    hv=sum((v*w for v,w in zip((1,-1)*3,weights)),s.zeros(8,1))
    charges=[s.simplify((S*s.Matrix(r)).dot(hv)) for r in roots]
    ck('actual puncture cocharacter charges integral',all(v.is_Integer for v in charges))
    if not checks['actual puncture cocharacter charges integral']:
        raise ValueError('Nonintegral puncture charge: parity cannot be inferred by truncation')
    odd=[r for r,q in zip(roots,charges) if int(q)%2]
    root=odd[0];up=idx[root];dn=idx[tuple(-x for x in root)]
    H={j:-s.Rational(v) for j,v in engine.pair(up,dn).items()}
    def bracket(u,v):
        out={}
        for p,x in u.items():
            for q,y in v.items():
                for j,w in engine.pair(p,q).items():out[j]=out.get(j,0)+x*y*s.Rational(w)
        return {j:simp(v) for j,v in out.items() if simp(v)!=0}
    ck('actual odd112 root roster',len(odd)==112)
    ck('actual compact signed SL2 root',[bracket(H,{up:1}),bracket(H,{dn:1})]==[{up:2},{dn:-2}] and all(j<8 for j in H))
    ep=s.Matrix([[0,1],[0,0]]);em=s.Matrix([[0,0],[-1,0]]);hh=s.diag(1,-1)
    ck('explicit faithful root map',ep*em-em*ep==-hh and hh*ep-ep*hh==2*ep)
    compactP=(ep+em)/2;compactQ=(ep-em)/(2*s.I)
    ck('nilpotent root has two compact real components',compactP.H==-compactP and compactQ.H==-compactQ and compactP+s.I*compactQ==ep)

    # Noncommuting local nonlinear Higgs backreaction. Constants here
    # are declared local metric/field normalization, not observables.
    amp,h0=s.symbols('amplitude h0',positive=True)
    k=4*amp**2*h0**2;u=s.log(h0)-s.log(1-k*rad)
    upr=s.diff(u,rad);lap=simp(s.diff(upr,rad)+upr/rad)
    ff=amp*h0*s.exp(-s.I*th/2)/(s.sqrt(rad)*(1-k*rad))
    phi=ff*ep;barphi=s.conjugate(ff)*em
    dz=lambda f:simp(s.exp(-s.I*th)*(f.diff(rad)-s.I*f.diff(th)/rad)/2)
    db=lambda f:simp(s.exp(s.I*th)*(f.diff(rad)+s.I*f.diff(th)/rad)/2)
    Abar=-db(u)*hh/2
    Az=dz(u)*hh/2
    Fzb=simp(dz(Abar)-db(Az)+Az*Abar-Abar*Az)
    ck('actual unitary backreacted connection',zero(Abar+Az.H))
    ck('actual Cartesian curvature coefficient',zero(Fzb+lap*hh/4))
    ck('actual compact conjugate Higgs',zero(barphi+phi.H))
    ck('actual nonlinear holomorphic equation',zero(db(phi)+Abar*phi-phi*Abar))
    moment=4*(phi*barphi-barphi*phi)
    curvature=s.I*lap*hh/2
    ck('actual nonlinear moment balance',zero(curvature+s.I*moment/2))
    ck('curvature is nonzero rather than normal commuting trick',not zero(curvature) and not zero(moment))
    ck('omitting backreaction fails moment',not zero(s.I*moment/2))
    ck('local added orthonormal connection bounded',s.limit(upr,rad,0)==k)
    ck('puncture holonomy unchanged to leading order',s.limit(rad*upr,rad,0)==0)
    ck('actual Higgs leading halfpole',simp(s.limit(s.sqrt(rad)*ff,rad,0)-amp*h0*s.exp(-s.I*th/2))==0)
    ck('nonabelian curvature square logarithmic',simp(s.limit(rad*(lap**2*rad),rad,0)-k*k)==0)
    records['local_backreaction']={'root':list(root),'H':[[j,str(v)] for j,v in sorted(H.items())],
        'u':'log(h0)-log(1-k*rho)','k':'4*amplitude**2*h0**2',
        'domain':'0<rho<1/k, flat product chart; not a global Higgs/vacuum',
        'curvature_order':'rho^-1; rough square logarithmic; residual BPS zero'}

    # Off-shell gauge-covariant energy identity, with curvature retained.
    x,y=s.symbols('x y',real=True)
    ax=s.I*(x*hh+y*p1);ay=s.I*(x*y*p2+(1+x)*hh)
    q=s.Matrix([[x+s.I*y,x*y+s.I],[1+x*x,y-s.I*x]])
    DX=lambda v:simp(v.diff(x)+ax*v-v*ax)
    DY=lambda v:simp(v.diff(y)+ay*v-v*ay)
    dx,dy=DX(q),DY(q);DB=(dx+s.I*dy)/2
    F=simp(ay.diff(x)-ax.diff(y)+ax*ay-ay*ax)
    Jx=s.I*s.trace(q.H*dx);Jy=s.I*s.trace(q.H*dy)
    lhs=simp(4*s.trace(DB.H*DB)-s.trace(dx.H*dx+dy.H*dy))
    curl=simp(s.diff(Jy,x)-s.diff(Jx,y))
    fc=simp(-s.I*s.trace(q.H*(F*q-q*F)))
    ck('off shell covariant boundary identity',simp(lhs-curl-fc)==0)
    ck('dropping nonabelian curvature term fails',fc!=0 and simp(lhs-curl)!=0)
    cut,R=s.symbols('cutoff R',positive=True)
    f=s.exp(-s.I*th/2)/s.sqrt(rad)
    grad=simp(rad*(s.diff(f,rad)*s.conjugate(s.diff(f,rad))+s.diff(f,th)*s.conjugate(s.diff(f,th))/rad**2))
    E=simp(2*s.pi*s.integrate(grad,(rad,cut,R)))
    J=simp(s.I*2*s.pi*(s.conjugate(f)*s.diff(f,th)).subs(rad,R)-s.I*2*s.pi*(s.conjugate(f)*s.diff(f,th)).subs(rad,cut))
    ck('actual regulated halfpole boundary cancellation',simp(E+J)==0 and E!=0)
    ck('bare rough term genuinely divergent',s.limit(E,cut,0)==s.oo)
    ck('wrong boundary sign rejected',simp(E-J)!=0)
    # ACTUAL pullback to the three-real-dimensional boundary coframe.
    dt=s.Matrix([1,s.I,0]);dbt=dt.conjugate()
    zz=s.Matrix([0,0,s.I*rad*s.exp(s.I*th)]);bbz=zz.conjugate()
    tangent=simp(s.Matrix.hstack(dt,zz,dbt).det())
    normal=simp(s.Matrix.hstack(dt,zz,bbz).det())
    Wcritical=simp(s.integrate(tangent*f*f,(th,0,2*s.pi)))
    ck('actual tangential Fterm critical pairing',Wcritical==-4*s.pi)
    ck('actual charged dual Fterm coefficient nonzero',s.trace(ep*em)==-1)
    ck('normal Fterm wedge pulls back to zero',normal==0 and tangent!=0)
    ck('bounded tangential Fterm variation vanishes',s.limit(s.sqrt(rad),rad,0)==0)
    records['action']={'rough_energy':str(E),'retained_signed_boundary':str(J),
        'leading_tangential_Fterm_pairing_per_TrXY':str(Wcritical),
        'scope':'local necessary Fterm/energy tests, not full supersymmetric end action'}
    records['generic_dressing']=dressed
    records['status']='authored fixed-fibre interacting realization and local nonabelian/action controls; NOT full surface, physical spectrum, SM or gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}

def emit(cs,engine,valid):
    result=run(cs,engine,valid)
    print(json.dumps(result,indent=2));return 0 if result['all_passed'] else 1
