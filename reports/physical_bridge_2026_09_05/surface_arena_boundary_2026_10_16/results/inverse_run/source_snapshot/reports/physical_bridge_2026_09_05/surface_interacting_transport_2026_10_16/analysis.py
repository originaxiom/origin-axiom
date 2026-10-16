"""Actual source, nonnormal E8 root and coupled normal transport identities."""
import hashlib,importlib.util,json,sys
from itertools import product
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def cm(M):return M.applyfunc(s.expand)
def zz(z):return s.cancel(s.expand(s.expand_trig(z).rewrite(s.exp)))==0
def zero(M):return all(zz(z) for z in M.todok().values())
def setup(method):
    angular=load(HERE.parent/'surface_angular_response_2026_10_16/analysis.py','interacting_source_reader')
    vv,ext,valid=angular.source(method)
    old=load(HERE.parent/'surface_real_boundary_2026_10_15/analysis.py','interacting_credited_E8_loader')
    side=old.load(HERE.parent/'surface_real_boundary_2026_10_15'/('probe.py' if method=='native' else 'reference.py'),
                  'interacting_signed_'+method,analysis=old)
    if method=='native':
        raw=side.geo.gammas();vac=s.eye(4)[:,0];c0=(raw[0]-s.I*raw[1])/2;c1=(raw[2]-s.I*raw[3])/2
        F=s.Matrix.hstack(vac,c0*vac,c1*vac,c0*c1*vac);cs=[cm(F.H*c*F) for c in raw]
        valid &= zero(F.H*F-s.eye(4))
    else:
        basis=[(),(0,),(1,),(0,1)];es=[]
        for j in range(2):
            e=s.zeros(4)
            for k,v in enumerate(basis):
                if j not in v:e[basis.index(tuple(sorted((j,)+v))),k]=(-1)**sum(x<j for x in v)
            es.append(e)
        cs=[es[0]-es[0].H,s.I*(es[0]+es[0].H),es[1]-es[1].H,s.I*(es[1]+es[1].H)]
    return vv,ext,cs,side.Engine(),bool(valid),old
def run(method):
    vv,ext,cs,engine,valid,old=setup(method);checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    I=s.eye(16);I32=s.eye(32);C=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.eye(8))
    ck('actual source all nine Clifford coefficients and Hermiticity',valid and all(zero(v-v.H) for v in ext+vv) and all(zero(a*b+b*a-2*int(i==j)*I) for i,a in enumerate(ext+vv) for j,b in enumerate(ext+vv)))
    twist=load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py','interacting_actual_opposite_MW')
    op=twist.opposite(cs);ph=[1,1,-1,-s.I];ph+=list(map(s.conjugate,ph))
    L=cm(op['S']*s.diag(*[x for p in ph for x in [p]*2]));MW=op['MW'];G0=op['G0'];Gs=op['G'];R=op['R'];BC=op['B']
    Rs=cm(-s.I*vv[4]*vv[5]);B=cm(s.I*vv[2]*vv[3]);K=cm(Rs*B)
    gv=s.kronecker_product(s.eye(4),s.I*cs[2]*cs[3],s.eye(2))
    gh=s.kronecker_product(s.eye(4),s.I*cs[0]*cs[1],s.eye(2))
    ck('actual complementary MW isometry and Majorana map',zero(L.H*L-I) and zero(L*L.H-MW) and zero(BC*L.conjugate()-L*C))
    extG=[s.kronecker_product(s.I*cs[j],s.eye(4),s.diag(1,-1)) for j in range(1,4)]
    ck('all actual source velocities intertwine complementary MW',all(zero(-G0*g*L-L*v) for g,v in zip(extG+Gs,ext+vv)))
    ck('critical sign map is explicit not old label matching',zero(R*L-L*Rs) and zero(gv*L+L*B) and all(zero(L*((I+sig*K)/2)*L.H-MW*(I32-sig*R*gv)/2) for sig in (1,-1)))
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    gam=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]];g5=cm(s.I*s.prod(gam))
    N=-s.kronecker_product(g5,s.eye(4),p3);F=cm(G0*N)
    c3=s.kronecker_product(s.eye(4),cs[2],s.eye(2));c4=s.kronecker_product(s.eye(4),cs[3],s.eye(2))
    MP=s.kronecker_product(g5,s.eye(4),p2);MQ=-s.kronecker_product(g5,s.eye(4),p1)
    ck('full graph to source coefficients retain scalar coordinates',all(zero(F*c*L+s.I*L*v) for c,v in zip((c3,c4,MP,MQ),vv[2:])))
    r=s.Symbol('r',positive=True);th=s.Symbol('theta',real=True)
    cn=cm(c3*s.cos(th)+c4*s.sin(th));ct=cm(-c3*s.sin(th)+c4*s.cos(th))
    nd=lambda H:cm(cn*s.diff(H,r)+ct*s.diff(H,th)/r)
    VP=(MP*s.cos(th/2)-MQ*s.sin(th/2))/s.sqrt(r);VQ=(MP*s.sin(th/2)+MQ*s.cos(th/2))/s.sqrt(r)
    dress=[]
    for rr,gg in product((1,-1),repeat=2):
        proj=cm(MW*(I32+rr*R)/2*(I32+gg*gv)/2)
        gp=s.exp(-s.I*gg*th/2)/s.sqrt(r);phase=s.exp(-s.I*(rr+gg)*th/2)/r
        SP=cm(s.I*rr*s.kronecker_product(g5,s.eye(4),p1)*proj)
        phi=s.log(r) if rr*gg==1 else s.exp(s.I*gg*th)
        for name,V,fac in [('P',VP,1),('Q',VQ,s.I*rr)]:
            src=cm(SP*fac);h=cm(c3*src*phi)
            ck('actual MW generic dressed cancellation '+str((rr,gg,name)),zero(V*gp*proj-phase*src) and zero(nd(h)+phase*src) and zero(MW*h-h))
        dress.append({'R':rr,'GammaV':gg,'source_sigma':-rr*gg,'correction':'log' if rr*gg==1 else 'bounded angular'})
    # Canonical root coordinates; actual248 action, not a toy replacement.
    roots=sorted(engine.roots);ix={v:j for j,v in enumerate(engine.roots)}
    ind=list(range(8))+[8+ix[v] for v in roots];back={p:j for j,p in enumerate(ind)}
    pair=lambda p,q:{back[j]:s.Rational(w) for j,w in engine.pair(ind[p],ind[q]).items() if w}
    S=s.Matrix.hstack(*(s.Matrix(v)/2 for v in old.SIMPLE_DOUBLED));cart=s.Matrix(engine.cartan)
    e=[s.eye(8)[:,j] for j in range(8)];chain=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4]]
    chainM=s.Matrix.hstack(*chain);ws=[chainM*(chainM.T*chainM).inv()*s.Matrix([1,0,0,0,0])]
    for a in chain:ws.append(ws[-1]-a)
    hv=sum((a*w for a,w in zip((1,-1)*3,ws)),s.zeros(8,1));charges=[s.simplify((S*s.Matrix(v)).dot(hv)) for v in roots]
    integral=all(q.is_Integer for q in charges);ck('actual E8 charges integral before parity',integral)
    if not integral:raise ValueError('Cannot truncate nonintegral charges to parity')
    parity=[1]*8+[1 if int(q)%2==0 else -1 for q in charges];eta=s.diag(*parity)
    up=8+next(j for j,q in enumerate(charges) if int(q)%2);dn=8+roots.index(tuple(-z for z in roots[up-8]))
    hd={j:-z for j,z in pair(up,dn).items()}
    def adj(d):
        out={}
        for a,w in d.items():
            for b in range(248):
                for j,z in pair(a,b).items():out[j,b]=out.get((j,b),0)+w*z
        return s.SparseMatrix(248,248,out)
    ap=adj({up:s.Rational(1,2),dn:s.Rational(1,2)});aq=adj({up:1/(2*s.I),dn:-1/(2*s.I)});ah=adj(hd)
    ep=adj({up:1});em=adj({dn:1});G=s.SparseMatrix(s.diag(cart,s.eye(240)))
    tau=s.SparseMatrix(248,248,{(j,j):-1 for j in range(8)}|{(8+roots.index(tuple(-z for z in v)),8+j):1 for j,v in enumerate(roots)})
    eta=s.SparseMatrix(eta)
    ck('actual full coefficient metric positive and parity complete',len(roots)==240 and S.T*S==cart and all(cart[:j,:j].det()>0 for j in range(1,9)) and parity.count(1)==136 and parity.count(-1)==112)
    ck('actual E8 adjoint root is faithful noncommuting SL2',zero(ep*em-em*ep+ah) and zero(ah*ep-ep*ah-2*ep) and zero(ah*em-em*ah+2*em) and not zero(ap*aq-aq*ap))
    ck('compact adjoint metric not naive identity',zero(ap.H*G+G*ap) and zero(aq.H*G+G*aq) and zero(ah.H*G-G*ah) and not zero(ap.H+ap))
    ck('actual root Yukawa flips gauge parity and keeps compact reality',zero(eta*ap+ap*eta) and zero(eta*aq+aq*eta) and zero(eta*ah-ah*eta) and zero(tau*ap.conjugate()*tau-ap) and zero(tau*aq.conjugate()*tau-aq) and zero(tau*ah.conjugate()*tau+ah))
    # Exact scalar-plane rotation; it is a frame with a changed transition.
    U=s.cos(th/4)*I+s.I*s.sin(th/4)*Rs
    ck('scalar rotating frame keeps both physical Higgs vertices',zero(U*vv[4]*U.H-s.cos(th/2)*vv[4]+s.sin(th/2)*vv[5]) and zero(U*vv[5]*U.H-s.sin(th/2)*vv[4]-s.cos(th/2)*vv[5]))
    ck('rotating frame angular connection is retained',zero(-s.I*vv[3]*U.H*s.diff(U,th)-vv[3]*Rs/4))
    ck('rotating frame monodromy is not deleted',zero(U.subs(th,2*s.pi)-s.I*Rs) and not zero(U.subs(th,2*s.pi)-I))
    ck('all quarter shifted angular lattices match transition',all(s.exp(2*s.pi*s.I*(n+s.Rational(sig,4)))==s.I*sig for sig in (1,-1) for n in range(-3,4)))
    ck('Majorana keeps angular conjugate coupled sectors',zero(C*Rs.conjugate()*C+Rs) and zero(C*B.conjugate()*C+B) and zero(C*U.conjugate()*C-U) and zero(tau*eta*tau-eta))
    ts=[cm(vv[2]*vv[j]) for j in (4,5)]
    ck('coupled root sectors close without angular truncation',all(zero(Rs*T+T*Rs) and zero(B*T+T*B) and zero(K*T-T*K) for T in ts) and zero(eta*ap+ap*eta) and zero(eta*aq+aq*eta))
    ck('radial interacting current conserved in actual metric',all(zero(T.H+T) and zero(T*vv[2]+vv[2]*T) for T in ts) and zero(B.H-B) and zero(B*vv[2]+vv[2]*B) and zero((B*Rs)*vv[2]+vv[2]*(B*Rs)) and zero(ap.H*G+G*ap) and zero(aq.H*G+G*aq))
    # Canonical background normalization and all scalar profile equations.
    g=s.Symbol('g',positive=True);k=g*g;ur=k/(1-k*r);lap=s.diff(ur,r)+ur/r
    f=g*s.exp(-s.I*th/2)/(s.sqrt(r)*(1-k*r))
    db=lambda z:s.exp(s.I*th)*(s.diff(z,r)+s.I*s.diff(z,th)/r)/2
    ck('canonical root background balances full moment not commuting mass',zz(lap-g*g/(r*(1-k*r)**2)) and not zz(lap))
    ck('same background holomorphic equation and scalar normalization',zz(db(f)-s.exp(s.I*th)*ur*f/2) and zz(g-2*(g/2)))
    ck('halving real scalar but not backreaction fails',not zz(lap-(g/2)**2/(r*(1-k*r)**2)))
    t=s.Symbol('t',positive=True)
    ck('full radial change keeps Higgs gauge and horizontal terms',zz(2*t*ur.subs(r,t*t)/2-k*t/(1-k*t*t)) and zz((2*t*g/(s.sqrt(r)*(1-k*r))).subs(r,t*t)-2*g/(1-k*t*t)))
    for rr,bb in product((1,-1),repeat=2):
        q=(I+rr*Rs)/2*(I+bb*B)/2;j=-s.Rational(rr,4);C0=cm(2*B*(j*I+Rs/4));sig=rr*bb
        ck('critical coupled indicial sector '+str((rr,bb)),zero(C0*q) and all(zero(C0*T*q-sig*T*q) for T in ts))
        good=True
        for T in ts:
            jet=-g*t*T*q if sig==1 else -2*g*t*s.log(t)*T*q
            good &= zero(s.diff(jet,t)+C0*jet/t+2*g*T*q)
        ck('actual bounded or log dressed first jet '+str((rr,bb)),good)
    ck('undressed critical Yukawa residual is not discarded',all(not zero(T*((I+Rs)/2*(I+B)/2)) for T in ts))
    # Actual complementary-MW supersymmetric tangent, all ordered jets.
    Pi=cm(MW*(I32+R*gh)/2*(I32+R*gv)/2);normG=Gs[2:]
    ck('actual scalar supercharge real and nonzero',s.trace(Pi)==4 and zero(Pi*Pi-Pi) and zero(BC*Pi.conjugate()-Pi*BC))
    J01=normG[0]*normG[1];J02=normG[0]*normG[2];J03=normG[0]*normG[3]
    coeffs=[{(0,1):1,(1,0):-1,(2,3):1,(3,2):-1},
            {(0,2):1,(2,0):-1,(1,3):-1,(3,1):1},
            {(0,3):1,(3,0):-1,(1,2):1,(2,1):-1}]
    rhs=lambda a,b:(int(a==b)*I32+sum((J*co.get((a,b),0) for J,co in zip((J01,J02,J03),coeffs)),s.zeros(32)))*Pi
    ck('all16 ordered BPS tangent coefficients in actual MW',all(zero(normG[a]*normG[b]*Pi-rhs(a,b)) for a,b in product(range(4),repeat=2)))
    qs=[cm(L.H*G0*Ga*Pi) for Ga in normG]
    ck('source BPS tangent preserves full reality and positive norm',all(zero(C*q.conjugate()-q*BC) for q in qs) and all(zero(qs[a].H*qs[b]+qs[b].H*qs[a]-2*int(a==b)*Pi) for a,b in product(range(4),repeat=2)))
    qp=(I+K)/2;qm=I-qp
    ck('actual scalar tangent enters plus critical source plane',all(zero(qp*q-q) for q in qs[2:]) and all(not zero(qm*q-q) for q in qs[2:]))
    # Differentiate the exact nonlinear background, not just its free limit.
    ck('full nonlinear parameter tangent residual vanishes',zz(s.diff(lap-g*g/(r*(1-k*r)**2),g)) and zz(s.diff(db(f)-s.exp(s.I*th)*ur*f/2,g)))
    ath=s.I*r*ur/2;dath=s.diff(ath,g);ax=-s.sin(th)*dath/r;ay=s.cos(th)*dath/r
    div=s.cos(th)*s.diff(ax,r)-s.sin(th)*s.diff(ax,th)/r+s.sin(th)*s.diff(ay,r)+s.cos(th)*s.diff(ay,th)/r
    ck('actual connection tangent is gauge fixed and retained',zz(div) and not zz(dath) and s.limit(dath/r,r,0)==s.I*g and zz(s.diff(f,g)/f-(1+k*r)/(g*(1-k*r))))
    # Under the stated fixed-fibre analytic domain hypotheses, these are the
    # actual bounded symmetry identities needed for the new norm argument.
    xi0,xi1=s.symbols('xi0 xi1',real=True);Mx=xi0*vv[0]+xi1*vv[1]
    ck('horizontal symbol anticommutes full interacting coefficients',all(zero(Mx*v+v*Mx) for v in vv[2:]))
    ck('horizontal symbol preserves both dressed leading trace planes',zero(Mx*Mx-(xi0**2+xi1**2)*I) and all(zero(Mx*Q-Q*Mx) for Q in (qp,qm)))
    ck('horizontal symmetry respects polar and rotating frames',zero(Mx*Rs-Rs*Mx) and zero(Mx*B-B*Mx))
    ck('wrong horizontal scalar shortcut fails trace preservation',not zero(vv[4]*qp-qp*vv[4]))
    enc=lambda M:[[i,j,str(z)] for (i,j),z in sorted(M.todok().items()) if z!=0]
    raw=json.dumps([enc(ap),enc(aq),enc(ah)],separators=(',',':')).encode()
    records['source']={'MW':'actual complementary projector, not isometric to old chirality',
        'critical_map':'source sigma=-old epsilon; GammaV maps to -B; same scalar coordinates',
        'dressed':dress}
    records['gauge']={'root':list(roots[up-8]),'H':[[j,str(z)] for j,z in sorted(hd.items())],
        'regular':136,'odd':112,'adjoint_matrix_sha256':hashlib.sha256(raw).hexdigest(),
        'normalization':'real scalar amplitude g=2lambda, k=g^2; not an observed coupling'}
    records['radial']={'j':'Z+l/4, l=eta R_s=+/-1; Majorana pairs l and -l',
        'exact':'B(j+R/4)/r+(uprime/2) B adH+g T/(sqrt(r)(1-g^2 r))+A',
        'first_jets':'source sigma+ bounded angular; sigma- log; both critical laws remain',
        'finite_radius_full_response_computed':False,'global_boundary_domain_proved':False}
    records['tangent']={'map':'actual complementary MW/source all16ordered jets, real positive norm',
        'leading_plane':'source sigma+; other sign not killed','status':'local nonlinear BPS tangent, not global modulus/physical particle/full boundary SUSY'}
    records['normal_bound']={'formula':'||N_xi u||^2=||D_sigma u||^2+|xi|^2||u||^2, inverse<=1/|xi| for xi!=0',
        'scope':'authored conditional fixed-flat-fibre dressed-domain proof, not whole curved surface or physical mass gap'}
    records['scope']='supplied interacting local normal source/BPS/dressed transport framework; not full finite-radius boundary response, common nonlinear curved SUSY domain, global charged spectrum, SM/three or gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(method):
    d=run(method);print(json.dumps(d,indent=2));return 0 if d['all_passed'] else 1
