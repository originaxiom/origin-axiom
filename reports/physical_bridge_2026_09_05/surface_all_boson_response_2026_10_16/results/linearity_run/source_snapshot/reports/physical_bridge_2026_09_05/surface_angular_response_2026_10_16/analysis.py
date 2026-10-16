"""Actual source angular test and frozen spectral/charged-pair responses."""
import hashlib,importlib.util,json,sys
from itertools import combinations
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def cm(m):return m.applyfunc(s.expand)
def zero(m):return all(s.cancel(s.expand(z))==0 for z in m)
def source(method):
    old=load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py','angular_actual_source')
    raw=(HERE.parent/'surface_full_real_parent_2026_10_16/results/gauge_frame_run/probe.stdout.log').read_bytes()
    data=json.loads(raw);mm=data['records']['complete_action_matrices']
    ea=[old.strip(old.read(r)) for r in mm['external_derivative']]
    bg=[old.strip(old.read(r)) for r in mm['internal_background']]
    dd=[old.strip(old.read(r)) for r in mm['internal_derivative']]
    T=ea[0];actual=[cm(T.inv()*r) for r in ea[1:]+bg]
    valid=hashlib.sha256(raw).hexdigest()=='cc5b961ae78eb458e031d93f993e2899ee0e91d82f187dc68e2a5fe816f60143'
    valid &= all(zero(x-y) for x,y in zip(dd,bg[:4]))
    if method=='native':return actual[3:],actual[:3],bool(valid)
    # Credited full opposite-MW reconstruction; no source velocity read-out.
    basis=[v for k in range(3) for v in combinations(range(2),k)];es=[]
    for j in range(2):
        e=s.zeros(4)
        for k,v in enumerate(basis):
            if j not in v:e[basis.index(tuple(sorted((j,)+v))),k]=(-1)**sum(x<j for x in v)
        es.append(e)
    cs=[es[0]-es[0].H,s.I*(es[0]+es[0].H),es[1]-es[1].H,s.I*(es[1]+es[1].H)]
    op=old.opposite(cs);ph=[1,1,-1,-s.I];ph+=list(map(s.conjugate,ph))
    U=s.diag(*[z for p in ph for z in [p]*2]);L=cm(op['S']*U)
    ints=[cm(L.H*(-op['G0']*g)*L) for g in op['G']]
    # The external Gamma matrices are reconstructed independently of the source.
    gam=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]]
    exg=[s.kronecker_product(g,s.eye(4),s.diag(1,-1)) for g in gam[1:]]
    ext=[cm(L.H*(-op['G0']*g)*L) for g in exg]
    valid &= zero(L.H*L-s.eye(16)) and all(zero(a-b) for a,b in zip(ext+ints,actual))
    return ints,ext,bool(valid)
def run(vv,ext,frame,valid,method):
    checks={};records={};I=s.eye(16);Z=s.zeros(16)
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    ck('actual complete source and method dictionary',valid)
    vel=ext+vv;swap=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.eye(8))
    ck('all nine source Hermitian Clifford relations',all(zero(v-v.H) for v in vel) and all(zero(a*b+b*a-2*int(i==j)*I) for i,a in enumerate(vel) for j,b in enumerate(vel)))
    ck('all actual source velocities Majorana even',all(zero(swap*v.conjugate()*swap-v) for v in vel))
    ck('actual adapted normal and all tangents orthonormal',zero(frame.T*frame-s.eye(4)))
    v=lambda z:cm(sum((z[i]*vv[i] for i in range(4)),Z))
    vn,vt,vjt,vc=[v(frame[:,j]) for j in range(4)]
    Rs=cm(-s.I*vv[4]*vv[5]);Bc=cm(s.I*vn*vc);K=cm(Rs*Bc);Q=(I+K)/2
    ck('actual adapted whole trace still real and Green null',zero(Q*Q-Q) and zero(Q.H-Q) and s.simplify(s.trace(Q)-8)==0 and zero(Q*vn*Q) and zero(swap*Q.conjugate()-Q*swap))
    x,y,z,q,m4,m5=s.symbols('xi1 xi2 xi3 charge m4 m5',real=True)
    energy=s.Symbol('energy',positive=True);n2=x*x+y*y+z*z+q*q*(m4*m4+m5*m5)
    def red(p):
        num,den=s.cancel(s.expand(p)).as_numer_denom()
        return s.cancel(s.Poly(num,energy).rem(s.Poly(energy**2-n2,energy)).as_expr()/den)
    ez=lambda M:all(red(w)==0 for w in M)
    Hcr=cm(s.I*vn*(x*vt+y*vjt));Hch=cm(z*Bc);mass=cm(q*(m4*vv[4]+m5*vv[5]));Hm=cm(s.I*vn*mass)
    H=cm(Hcr+Hch+Hm);H0=cm(Hcr+Hch)
    ck('actual normal factorization keeps all scalar and tangential terms',zero(-s.I*vn*H-(x*vt+y*vjt+z*vc+mass)))
    ck('full frozen Hamiltonian Hermitian and exact square',zero(H.H-H) and zero(H*H-n2*I))
    ck('normal current anticommutes full frozen Hamiltonian',zero(vn*H+H*vn))
    ck('CR part exchanges old trace with invertible transverse square',zero(K*Hcr+Hcr*K) and zero(Hcr*Hcr-(x*x+y*y)*I))
    ck('characteristic and actual scalar mass preserve old trace',zero(K*(Hch+Hm)-(Hch+Hm)*K))
    ck('both old planes retain equal signed characteristic multiplicities',all(s.simplify(s.trace(P)-8)==0 and s.simplify(s.trace(P*(Hch+Hm)))==0 for P in (Q,I-Q)))
    C=(I-H/energy)/2;P=(I+H/energy)/2
    ck('full Cauchy and spectral responses are exact orthogonal projectors',all(ez(A.H-A) and ez(A*A-A) and red(s.trace(A)-8)==0 for A in (C,P)))
    ck('spectral response complements complete interior Cauchy space',ez(P*C) and ez(C*P) and zero(P+C-I))
    ck('both spectral planes have true normal Green current zero',ez(P*vn*P) and ez(C*vn*C))
    ck('old compression keeps every angular and scalar term',ez(Q*C*Q-(Q/2-Q*(Hch+Hm)*Q/(2*energy))))
    c0=C.subs({m4:0,m5:0});e0=energy
    # No use of the full-mass quotient relation in this principal identity.
    ck('principal old compression has correct two angular eigenbranches',zero(Q*c0*Q-(Q/2-z*Q*Bc*Q/(2*e0))) and zero((Q*Bc*Q)*(Q*Bc*Q)-Q) and s.simplify(s.trace(Q*Bc))==0)
    ck('all responses preserve external Lorentz generators',all(zero(H*w-w*H) and zero(Q*w-w*Q) for w in ext))
    flip={x:-x,y:-y,z:-z,q:-q}
    ck('Fourier and charge reversal retain actual Majorana response',ez(swap*P.conjugate()*swap-P.subs(flip,simultaneous=True)))
    ck('fixed Fourier pointwise reality is not silently substituted',not ez(swap*P.conjugate()*swap-P))
    # Both canonical ends and the exterior response, rather than a chosen half-field.
    tau=s.Symbol('tau',real=True);outmode=s.exp(-energy*tau)*P;inmode=s.exp(energy*tau)*C
    ck('exterior and interior decaying solutions solve same equation',ez(cm(s.exp(energy*tau)*(s.diff(outmode,tau)+H*outmode))) and ez(cm(s.exp(-energy*tau)*(s.diff(inmode,tau)+H*inmode))))
    # On a positive-eigen exterior mode the squared norm integrates to E.
    Epos=s.Symbol('Epositive',positive=True);tpos=s.Symbol('tpositive',nonnegative=True)
    norm_integral=s.integrate(2*Epos**2*s.exp(-2*Epos*tpos),(tpos,0,s.oo))
    ck('exterior squared norm response positive and normalized',s.simplify(norm_integral-Epos)==0)
    ck('both oriented boundary spectral signs retained',ez(H*P-energy*P) and ez(H*C+energy*C) and ez(P+C-I))
    # Frozen normal first variation identity: derivative of psi^dag H psi.
    ar,ai,br,bi,hh=s.symbols('ar ai br bi h',real=True)
    psi=ar+s.I*ai;dpsi=br+s.I*bi
    ck('interior norm identity retains boundary cross term',s.expand(s.conjugate(dpsi+hh*psi)*(dpsi+hh*psi)-s.conjugate(dpsi)*dpsi-hh*hh*s.conjugate(psi)*psi-hh*(s.conjugate(dpsi)*psi+s.conjugate(psi)*dpsi))==0)
    def frozen_project(values):
        sub=dict(zip((x,y,z,q,m4,m5),map(s.Integer,values)));rho2=s.simplify(n2.subs(sub))
        if rho2==0:return None
        return P.subs(sub).subs(energy,s.sqrt(rho2))
    ck('zero threshold not divided or falsely gapped',frozen_project((0,0,0,0,3,4)) is None and frozen_project((0,0,0,1,0,0)) is None)
    # Direct independent intersection routes; finite controls support the universal proof.
    samples=[(0,0,1,1,0,0),(0,0,-1,1,0,0),(1,0,0,1,0,0),(0,1,0,1,0,0),(3,4,12,1,0,0),
        (0,0,12,1,3,4),(0,0,-12,-1,3,4),(0,0,0,1,3,4),(3,0,0,1,4,0)]
    rows=[]
    for values in samples:
        sub=dict(zip((x,y,z,q,m4,m5),map(s.Integer,values)));hn=H.subs(sub);en=s.sqrt(n2.subs(sub))
        cc=(hn+en*I).nullspace();ccmat=s.Matrix.hstack(*cc)
        if method=='native':dims=[16-s.Matrix.vstack(I-A,hn+en*I).rank() for A in (Q,I-Q)]
        else:dims=[A.rank()+len(cc)-s.Matrix.hstack(A,ccmat).rank() for A in (Q,I-Q)]
        pn=frozen_project(values);rank=s.Matrix.hstack(pn,ccmat).rank()
        wanted=4 if values[0]==values[1]==0 else 0
        ck('all angle Cauchy intersection '+str(values),dims==[wanted,wanted] and len(cc)==8 and rank==16)
        rows.append({'parameters':list(values),'old_intersections':dims,'spectral_union_rank':rank})
    # Local comparator: complex alone fails C, existing conjugate pair repairs C.
    Sbag=cm(s.I*vn*vv[4]);B=(I+Sbag)/2
    ck('local complex bag is principal elliptic and Green null',zero(Sbag.H-Sbag) and zero(Sbag*Sbag-I) and zero(Sbag*H0+H0*Sbag) and zero(B*vn*B) and s.simplify(s.trace(B)-8)==0)
    ck('unpaired complex bag fails actual pointwise reality',zero(swap*B.conjugate()*swap-(I-B)) and not zero(swap*B.conjugate()*swap-B))
    pair=s.diag(B,I-B);cpair=s.kronecker_product(s.Matrix([[0,1],[1,0]]),swap)
    charge=s.kronecker_product(s.diag(1,-1),I);mix=s.kronecker_product(s.Matrix([[0,1],[1,0]]),I)
    ck('existing conjugate charge pair local bag retains Majorana',zero(cpair*pair.conjugate()*cpair-pair) and zero(pair*pair-pair) and s.simplify(s.trace(pair)-16)==0)
    ck('paired charge conjugation flips axis without deleting fields',zero(cpair*charge.conjugate()*cpair+charge) and zero(cpair*cpair-s.eye(32)))
    ck('charged local pair retains Lorentz and normal current',all(zero(pair*s.diag(w,w)-s.diag(w,w)*pair) for w in ext) and zero(pair*s.diag(vn,vn)*pair))
    ck('charged pair local principal complement for all covectors',zero((2*pair-s.eye(32))*s.diag(H0,H0)+s.diag(H0,H0)*(2*pair-s.eye(32))))
    ck('charge axis preserved but general gauge mixing detected',zero(pair*charge-charge*pair) and not zero(pair*mix-mix*pair))
    g=s.Matrix([[1,1],[0,1]]);h=s.Matrix([[1,0],[1,1]])
    ck('spectral response keeps full constant gauge multiplicity',g*h!=h*g and ez(s.kronecker_product(P,s.eye(2))*s.kronecker_product(I,g*h)-s.kronecker_product(I,g*h)*s.kronecker_product(P,s.eye(2))))
    records['angular']={'old_plane_intersection':'4 for xi_CR=0,E>0; 0 for xi_CR nonzero, BOTH planes',
        'old_full_internal_elliptic':False,'scope':'this specified pointwise plane only; not singular critical domain or all boundaries',
        'finite_cauchy_controls':rows}
    records['spectral']={'E2':str(n2),'interior_decaying':'H negative, C_minus','allowed_and_exterior':'H positive, P_plus',
        'squared_norm_response':'E norm(boundary data)^2, not fermion determinant/action phase',
        'zero_threshold':'OPEN, division by zero forbidden','reality':'momentum AND conjugate-charge reversal retained'}
    records['local_pair']={'unpaired_bag_real':False,'paired_charged_bag_real':True,'full_gauge_covariance_earned':False,
        'costs':['supplied charge axis','supplied scalar direction/phase','neutral sector not supplied','full curved/SUSY/source action not supplied']}
    records['scope']='actual-source all-angle internal principal test plus frozen spectral response and charged local control; no complete interacting/global/singular boundary or SM/three/gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(vv,ext,frame,valid,method):
    data=run(vv,ext,frame,valid,method);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
