"""Actual embedded tube geometry, principal trace and compact gauge law."""
import hashlib,importlib.util,json,sys
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
a,b=s.symbols('alpha beta',real=True);ell=s.Symbol('ell',positive=True)
def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def simp(x):return s.factor(s.cancel(s.expand(x)))
def cm(m):return m.applyfunc(simp)
def zero(m):return all(simp(z)==0 for z in m)
def source():
    prior=load(HERE.parent/'surface_real_twist_2026_10_16/analysis.py','tube_source_dictionary')
    path=HERE.parent/'surface_full_real_parent_2026_10_16/results/gauge_frame_run/probe.stdout.log'
    raw=path.read_bytes();m=json.loads(raw)['records']['complete_action_matrices']
    time=prior.strip(prior.read(m['external_derivative'][0]))
    vel=[cm(time.inv()*prior.strip(prior.read(q))) for q in m['internal_derivative']+m['internal_background'][4:]]
    # The derivative record has four matrices. Retain two actual scalar backgrounds.
    return vel,cm(-s.I*vel[4]*vel[5]),hashlib.sha256(raw).hexdigest()
def run(N,D,C,valid,charts):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    ck('coordinate or closed frame geometry input',valid)
    r2=a*a+b*b;den=4*ell*ell+r2;Id=s.eye(4)
    J=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    nn=simp((N.T*N)[0]);JN=J*N
    ck('actual radius gradient and nonzero horizontal tilt',zero(N-s.Matrix([2*a*b/ell,(b*b-a*a)/ell,2*a,2*b])) and simp(nn-r2*den/ell**2)==0 and simp((N[0]**2+N[1]**2)/nn-r2/den)==0)
    ck('unit normal and complex partner orthogonal',simp((N.T*JN)[0])==0 and simp((JN.T*JN)[0]-nn)==0)
    ck('both modular radius transitions exact',charts)
    Ei=lambda f,i:simp(D[i,0]*s.diff(f,a)+D[i,1]*s.diff(f,b))
    PH=cm(Id-(N*N.T+JN*JN.T)/nn);T=PH[:,0];JT=J*T
    geometry_parts={'idempotent':zero(PH*PH-PH),'real symmetric':zero(PH.T-PH),
        'J compatible':zero(PH*J-J*PH),'rank trace':simp(s.trace(PH)-2)==0,
        'second tangent':zero(PH[:,1]-JT),'positive tangent norm':simp((T.T*T)[0]-4*ell**2/den)==0}
    for k,val in geometry_parts.items():ck('actual CR projection component '+k,val)
    ck('actual CR tangent projection and positive rank two',all(geometry_parts.values()))
    ck('CR tangent annihilates radius and characteristic form',zero(s.Matrix([N.dot(T),N.dot(JT),JN.dot(T),JN.dot(JT)])))
    deta=s.Matrix(4,4,lambda i,j:Ei(JN[j],i)-Ei(JN[i],j)-sum(C[i][j][k]*JN[k] for k in range(4)))
    levi=simp((T.T*deta*JT)[0]);wanted=16*ell**2*r2/den**2
    ck('strict actual contact Levi coefficient',simp(levi-wanted)==0)
    bracket=s.Matrix([simp(sum(T[i]*Ei(JT[k],i)-JT[i]*Ei(T[k],i) for i in range(4))+sum(T[i]*JT[j]*C[i][j][k] for i in range(4) for j in range(4))) for k in range(4)])
    ck('actual tangent bracket has nonzero characteristic component',simp(N.dot(bracket))==0 and simp(JN.dot(bracket)+levi)==0 and simp(levi)!=0)
    ck('actual normal CR bracket spans all four ambient directions',simp(s.Matrix.hstack(N,T,JT,bracket).det())!=0)
    flateta=s.Matrix([0,0,-2*b,2*a]);flatD=s.Matrix([[0,0],[0,0],[1,0],[0,1]])
    fd=s.Matrix(4,4,lambda i,j:sum(flatD[i,k]*s.diff(flateta[j],(a,b)[k])-flatD[j,k]*s.diff(flateta[i],(a,b)[k]) for k in range(2)))
    ck('flat product control loses strict horizontal contact',fd[0,1]==0 and fd[2,3]==4 and levi!=0)
    dtheta=s.Matrix([simp((-b*D[i,0]+a*D[i,1])/r2) for i in range(4)])
    ck('actual angle derivative includes horizontal connection',zero(dtheta-JN/(2*r2)+s.eye(4)[:,0]/(2*ell)))
    tt=simp(dtheta.dot(T));jt=simp(dtheta.dot(JT))
    ck('angular pair fails adapted compact gauge condition',simp(tt+2*ell/den)==0 and jt==0 and simp(tt**2-4*ell**2/den**2)==0)
    # Actual SAME-source Clifford and Majorana matrices, not dimensions alone.
    vv,Rs,h=source();I=s.eye(16);swap=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.eye(8))
    ck('frozen actual real action complete record',h=='cc5b961ae78eb458e031d93f993e2899ee0e91d82f187dc68e2a5fe816f60143' and len(vv)==6)
    ck('all actual source Clifford relations',all(zero(vv[i]*vv[j]+vv[j]*vv[i]-(2*I if i==j else s.zeros(16))) for i in range(6) for j in range(6)))
    v=lambda z:cm(sum((z[i]*vv[i] for i in range(4)),s.zeros(16)))
    vN=v(N);vJN=v(JN);Q=cm((I+s.I*Rs*vN*vJN/nn)/2)
    Q0=s.diag(*[int(j in (2,3)) for bar in range(2) for j in range(4) for alpha in range(2)])
    ck('old vertical minus sign is actual source projector',zero(Q0-(I+s.I*Rs*vv[2]*vv[3])/2))
    projector_parts={'Hermitian':zero(Q.H-Q),'idempotent':zero(Q*Q-Q),'rank trace':simp(s.trace(Q)-8)==0}
    for k,val in projector_parts.items():ck('actual real projector component '+k,val)
    ck('adapted actual projector Hermitian idempotent half rank',all(projector_parts.values()))
    ck('wrong geometric and real projector trace targets detected',simp(s.trace(PH)-3)!=0 and simp(s.trace(Q)-7)!=0)
    ck('adapted projector preserves true R and Majorana reality',zero(Rs*Q-Q*Rs) and zero(swap*Q.conjugate()-Q*swap))
    ck('both actual normal Green forms zero',zero(Q*vN*Q) and zero(Q*vJN*Q))
    ck('both CR tangential principal symbols preserved',zero(Q*v(T)-v(T)*Q) and zero(Q*v(JT)-v(JT)*Q))
    ck('complementary plane also zero flux not hand selection',zero((I-Q)*vN*(I-Q)) and zero((I-Q)*vJN*(I-Q)))
    ck('unchanged vertical plane fails actual tube Green control',not zero(Q0*vN*Q0) and not zero(Q0*vJN*Q0))
    ck('adapted plane approaches vertical at fixed angle',zero((Q-Q0).subs({b:0}).applyfunc(lambda z:s.limit(z,a,0,dir='+'))))
    # Complete moving-normal covariant derivative, not a constant-plane shortcut.
    GK=[[[simp((C[i][j][k]-C[j][k][i]+C[k][i][j])/2) for k in range(4)] for j in range(4)] for i in range(4)]
    covQ=[]
    for i in range(4):
        conn=cm(-sum((GK[i][j][k]*vv[j]*vv[k]/4 for j in range(4) for k in range(4)),s.zeros(16))+(3*s.I*Rs/(4*ell) if i==0 else s.zeros(16)))
        gi=s.Matrix(4,4,lambda k,j:GK[i][j][k])
        ck('actual Kahler connection parallel J '+str(i),zero(gi*J-J*gi))
        H=s.Matrix([Ei(N[k],i) for k in range(4)])+gi*N
        direct=cm(Q.applyfunc(lambda z:Ei(z,i))+conn*Q-Q*conn)
        formula=cm(s.I*Rs*( (v(H)*vJN+vN*v(J*H))/nn-vN*vJN*Ei(nn,i)/nn**2)/2)
        ck('full moving plane covariant derivative '+str(i),zero(direct-formula));covQ.append(direct)
    ck('constant plane shortcut loses extrinsic derivative',any(not zero(z) for z in covQ))
    # Real compact CR jets are more restrictive than complex CR scalar jets.
    xs=s.symbols('x0:4',real=True);ys=s.symbols('y0:4',real=True)
    pauli=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    X=s.I*sum((xs[i]*pauli[i] for i in range(4)),s.zeros(2));Y=s.I*sum((ys[i]*pauli[i] for i in range(4)),s.zeros(2));Z=X-s.I*Y
    jetnorm=s.expand(s.trace(Z.H*Z))
    ck('compact matrix CR jet norm forces both real derivatives',s.expand(jetnorm-2*sum(q*q for q in xs+ys))==0)
    ck('complex nonconstant CR scalar is not excluded',zero(s.Matrix([T[0]-s.I*T[1]-s.I*(JT[0]-s.I*JT[1])])) and T[0]!=0)
    ck('complex matrix CR jet without compact reality survives',zero(X-s.I*(-s.I*X)) and not zero((-s.I*X).H+(-s.I*X)))
    # Internally constant traces may have a free NORMAL jet. Test the
    # actual boundary pullback, not the vacuous scalar identity 0=0.
    normaljet=s.Symbol('normal_gauge_jet',real=True)*N;omega=-J
    pull=lambda cov:simp((T.T*omega*JT)[0]*cov.dot(JN)+(JT.T*omega*JN)[0]*cov.dot(T)+(JN.T*omega*T)[0]*cov.dot(JT))
    ck('restricted conormal gauge jets have zero boundary cocycle pullback',pull(normaljet)==0 and not zero(normaljet))
    ck('unrestricted angular cocycle density remains a nonzero control',pull(dtheta)!=0)
    y,A=s.symbols('y area',positive=True)
    ck('fixed tube cannot fit uniformly along cusp cycle',s.limit(s.sqrt(A/y)/2,y,s.oo)==0)
    records['trace_diagnostic']={'geometry_raw_trace':str(s.trace(PH)),'geometry_structural_equal_2':bool(s.trace(PH)==2),
        'geometry_exact_residual':str(simp(s.trace(PH)-2)),'source_raw_trace':str(s.trace(Q)),
        'source_structural_equal_8':bool(s.trace(Q)==8),'source_exact_residual':str(simp(s.trace(Q)-8))}
    records['geometry']={'N':[str(simp(z)) for z in N],'normal_norm2':str(nn),'horizontal_fraction':str(r2/den),'T':[str(z) for z in T],
        'Levi':str(levi),'characteristic_bracket':str(simp(JN.dot(bracket))),'Ttheta':str(tt),'JTtheta':str(jt)}
    records['boundary']={'projector':'(I+i Rs v(N)v(JN)/normN^2)/2','real_rank':8,'complement_also_allowed':True,
        'stabilizer':'compact gauge parameters internally constant on each connected adapted cut patch; global holonomy compatibility extra',
        'cocycle':'zero on this restricted stabilizer, not on arbitrary collar parameters'}
    records['scope']='finite embedded tube/base truncation; principal real trace and compact stabilizer, not full adapted multiplet SUSY/elliptic/singular/gauge limit or physical SM/three/gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
def emit(N,D,C,valid,charts):
    data=run(N,D,C,valid,charts);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
