"""Actual source charge/connection/Weyl dictionary; no science on import."""
import hashlib,importlib.util,json,sys
from pathlib import Path
from itertools import combinations
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
PARENT=HERE.parent/'surface_full_real_parent_2026_10_16'
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
sys.path.insert(0,str(PARENT))
try:prior=load(PARENT/'analysis.py','curved_real_action_prior')
finally:sys.path.pop(0)
source=prior.source
def cm(m):return m.applyfunc(s.expand)
def zero(m):
    return all(v==0 or s.trigsimp(s.simplify(s.expand_complex(v)))==0 for v in m)
def sparse(m):return [[i,j,str(s.simplify(v))] for (i,j),v in sorted(m.todok().items()) if v!=0]
def read(rows):return s.SparseMatrix(48,48,{(i,j):s.sympify(v) for i,j,v in rows})
def strip(m):
    n=s.Matrix(16,16,lambda i,j:m[3*i,3*j+1])
    if not zero(m-s.kronecker_product(n,source.J)):raise ValueError('nonuniform coefficient tensor')
    return n
def opposite(cs):
    i4=s.eye(4);p3=s.diag(1,-1);p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]])
    gam=[-cs[0],s.I*cs[1],s.I*cs[2],s.I*cs[3]];g5=cm(s.I*s.prod(gam))
    L=s.Matrix.hstack(*((i4+g5)/2).columnspace())
    G0=s.kronecker_product(gam[0],i4,p3)
    ext=[s.kronecker_product(gam[j],i4,p3) for j in range(1,4)]
    G=[s.kronecker_product(g5,s.I*c,p3) for c in cs]+[s.kronecker_product(i4,i4,p1),s.kronecker_product(i4,i4,p2)]
    B=cm(s.kronecker_product(gam[0]*gam[1]*gam[3],cs[1]*cs[3],p2))
    MW=cm((s.eye(32)+s.kronecker_product(g5,-s.prod(cs),p3))/2)
    W=s.Matrix.hstack(*[s.kronecker_product(L,i4[:,j],s.eye(2)[:,rr]) for j,rr in ((0,0),(2,1),(1,1),(3,0))])
    S=W.row_join(B*W.conjugate());Bn=cm(S.T*B.H*S)
    ia=[cm(-s.I*S.T*B.H*G0*g*S) for g in G]
    ea=[s.I*Bn]+[cm(-s.I*S.T*B.H*G0*g*S) for g in ext]
    return {'S':S,'MW':MW,'B':B,'Bn':Bn,'G0':G0,'G':G,'ia':ia,'ea':ea,'R':s.kronecker_product(i4,i4,p3)}
def emit(cs,gk,valid):
    data=run(cs,gk,valid);print(json.dumps(data,indent=2));return 0 if data['all_passed'] else 1
def run(cs,gk,valid):
    checks={};records={}
    def ck(k,v):checks[k]=bool(v);print(('PASS ' if checks[k] else 'FAIL ')+k,file=sys.stderr,flush=True)
    raw=(PARENT/'results/gauge_frame_run/probe.stdout.log').read_bytes()
    ck('credited complete real action record hash',hashlib.sha256(raw).hexdigest()=='cc5b961ae78eb458e031d93f993e2899ee0e91d82f187dc68e2a5fe816f60143')
    data=json.loads(raw);mm=data['records']['complete_action_matrices']
    ea=[strip(read(x)) for x in mm['external_derivative']];eb=[strip(read(x)) for x in mm['external_background']]
    ia=[strip(read(x)) for x in mm['internal_background']];dd=[strip(read(x)) for x in mm['internal_derivative']]
    ck('credited all local covariant coefficient tensors',all(zero(a-b) for a,b in zip(ea,eb)) and all(zero(a-b) for a,b in zip(ia,dd)))
    ck('complete coordinate or exterior geometry input',valid)
    I=s.eye(16);vel=[cm(ea[0].inv()*m) for m in ia]
    Rs=cm(-s.I*vel[4]*vel[5]);swap=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.eye(8))
    named=s.diag(*[v for bar in range(2) for j in range(4) for v in [(-1 if j in (0,3) else 1)*(-1)**bar]*2])
    ck('actual scalar Noether charge is opposite old label',zero(Rs+named))
    ck('actual scalar charge Hermitian involution C odd',zero(Rs.H-Rs) and zero(Rs*Rs-I) and zero(swap*Rs.conjugate()+Rs*swap))
    ck('actual scalar generator acts on both scalar vertices',zero((s.I*Rs*vel[4]-vel[4]*s.I*Rs)/2+vel[5]) and zero((s.I*Rs*vel[5]-vel[5]*s.I*Rs)/2-vel[4]))
    ck('actual scalar charge preserves all geometric and external velocities',all(zero(Rs*v-v*Rs) for v in vel[:4]+[cm(ea[0].inv()*m) for m in ea[1:]]))
    op=opposite(cs);S=op['S'];B=op['B'];MW=op['MW'];R=op['R']
    ck('opposite normalized MW rank16 frame',zero(S.H*S-I) and zero(S*S.H-MW) and MW.rank()==16)
    ck('opposite full Majorana and Nambu time',zero(B*S.conjugate()-S*swap) and zero(op['Bn']-swap) and zero(ea[0]-op['ea'][0]))
    ph,why=source.phase_map([s.kronecker_product(m,source.J) for m in ia],[s.kronecker_product(m,source.J) for m in op['ia']])
    ck('same named flavours opposite Weyl unit phase map',ph is not None)
    if ph is None:
        records['failed_map']=why
        return {'checks':checks,'records':records,'all_passed':False}
    U=s.diag(*[v for z in ph+[s.conjugate(x) for x in ph] for v in [z]*2]);L=cm(S*U)
    ck('all six full scalar and derivative coefficients mapped',all(zero(a-U.T*b*U) for a,b in zip(ia,op['ia'])) and all(zero(a-U.T*b*U) for a,b in zip(dd,op['ia'][:4])))
    ck('all external kinetic and gauge coefficients mapped',all(zero(a-U.T*b*U) for a,b in zip(ea,op['ea'])) and all(zero(a-U.T*b*U) for a,b in zip(eb,op['ea'])))
    ck('actual physical isometry reality and true R map',zero(L.H*L-I) and zero(L*L.H-MW) and zero(B*L.conjugate()-L*swap) and zero(R*L-L*Rs))
    # Whole source connection from actual velocities; independent tensor rule.
    omega=[cm(-sum((gk[i][j][k]*vel[j]*vel[k]/4 for j in range(4) for k in range(4)),s.zeros(16))) for i in range(4)]
    cspin=[cm(sum((gk[i][j][k]*cs[j]*cs[k]/4 for j in range(4) for k in range(4)),s.zeros(4))) for i in range(4)]
    spin32=[s.kronecker_product(s.eye(4),w,s.eye(2)) for w in cspin]
    ar=[3*s.I/4,0,0,0]
    full=[cm(omega[i]+ar[i]*Rs) for i in range(4)]
    physical=[cm(spin32[i]+ar[i]*R) for i in range(4)]
    cov=s.Matrix([[1,0],[s.I,0],[0,1],[0,s.I]])/s.sqrt(2)
    direct=[]
    for i in range(4):
        act=s.Matrix(4,4,lambda k,j:-gk[i][k][j]);one=cm(cov.H*act*cov)
        ck('actual holomorphic covector connection '+str(i),zero(act*cov-cov*one))
        left=s.zeros(4);left[1:3,1:3]=one;left[3,3]=s.conjugate(s.trace(one))
        tensor=s.diag(s.kronecker_product(left,s.eye(2)),s.kronecker_product(left.conjugate(),s.eye(2)));direct.append(cm(tensor))
        ck('all actual tensor field connection entries '+str(i),zero(full[i]-tensor))
        ck('all actual opposite MW spin R connection entries '+str(i),zero(physical[i]*L-L*full[i]))
        for j in range(4):ck('source connection actual Clifford compatibility '+str((i,j)),zero(omega[i]*vel[j]-vel[j]*omega[i]-sum((gk[i][j][k]*vel[k] for k in range(4)),s.zeros(16))))
    K=cm(sum((vel[j]*full[j] for j in range(4)),s.zeros(16)))
    Kd=cm(sum((vel[j]*direct[j] for j in range(4)),s.zeros(16)))
    ck('whole contracted curved source expression agrees',zero(K-Kd))
    lam=s.diag(*[int(j==0) for bar in range(2) for j in range(4) for alpha in range(2)])
    ck('actual scalar supersymmetry lambda connection parallel',all(zero(m*lam) for m in full))
    wrong=[cm(omega[i]-ar[i]*Rs) for i in range(4)]
    ck('reversed and omitted R fail tensor and lambda comparisons',any(not zero(wrong[i]-direct[i]) for i in range(4)) and any(not zero(omega[i]-direct[i]) for i in range(4)) and any(not zero(wrong[i]*lam) for i in range(4)))
    onlydensity=-vel[1]/2
    ck('dropping full mixed term fails curved action comparison',not zero(K-(onlydensity+3*s.I*vel[0]*Rs/4)))
    # Actual geometric transitions, including arbitrary-angle connection law.
    theta=s.Symbol('theta',real=True)
    Gs=cm(-vel[0]*vel[1]-vel[2]*vel[3]/2);Gt=cm(Gs+3*s.I*Rs/2)
    weights=[0,2,1,-3];W=s.diag(*[v for bar in range(2) for w in weights for v in [s.I*w*(-1)**bar]*2])
    ck('full actual source geometric weights not named by analogy',zero(-Gt-W))
    ts=(s.cos(theta)*I+s.sin(theta)*vel[0]*vel[1])*(s.cos(theta/2)*I+s.sin(theta/2)*vel[2]*vel[3])
    tr=s.cos(3*theta/2)*I-s.I*s.sin(3*theta/2)*Rs;T=ts*tr
    tf=s.diag(*[v for bar in range(2) for w in weights for v in [s.cos(w*theta)+s.I*(-1)**bar*s.sin(w*theta)]*2])
    ck('whole variable angle source tensor transition',zero(T-tf))
    cp=s.eye(4);gs=cs[0]*cs[1]+cs[2]*cs[3]/2
    targetspin=s.kronecker_product(s.eye(4),(s.cos(theta)*cp-s.sin(theta)*cs[0]*cs[1])*(s.cos(theta/2)*cp-s.sin(theta/2)*cs[2]*cs[3]),s.eye(2))
    targetR=s.cos(3*theta/2)*s.eye(32)-s.I*s.sin(3*theta/2)*R
    ck('full global chart intertwiner including MW and true R',zero(targetspin*targetR*L-L*T))
    rotations=s.diag(s.Matrix([[s.cos(2*theta),s.sin(2*theta)],[-s.sin(2*theta),s.cos(2*theta)]]),s.Matrix([[s.cos(theta),s.sin(theta)],[-s.sin(theta),s.cos(theta)]]))
    rotated=[sum((rotations[i,j]*vel[i] for i in range(4)),s.zeros(16)) for j in range(4)]
    gradient=[-s.sin(theta)**2,s.sin(theta)*s.cos(theta),0,0]
    rhs=sum((rotated[j]*Gt*gradient[j] for j in range(4)),s.zeros(16))
    ck('full variable angle curved differential covariance',zero(K-T*K*T.H-rhs))
    badrhs=sum((rotated[j]*(Gs-3*s.I*Rs/2)*gradient[j] for j in range(4)),s.zeros(16))
    ck('wrong chart R inhomogeneous term rejected',not zero(K-T*K*T.H-badrhs))
    ck('actual source central spin and R signs cancel',zero(ts.subs(theta,2*s.pi)+I) and zero(tr.subs(theta,2*s.pi)+I) and zero(T.subs(theta,2*s.pi)-I))
    ck('geometric S4 and ST central angle relations',zero(T.subs(theta,s.pi)**2-I) and zero(T.subs(theta,2*s.pi)-I))
    ck('source chart C reality',zero(swap*T.conjugate()-T*swap))
    # Finite cutoff is mapped rather than inferred from ranks or labels.
    Q=s.diag(*[int(j in (2,3)) for bar in range(2) for j in range(4) for alpha in range(2)])
    image=cm(L*Q*L.H);gv=s.kronecker_product(s.eye(4),s.I*cs[2]*cs[3],s.eye(2))
    target=cm(MW*(s.eye(32)-R*gv)/2)
    ck('actual whole cutoff maps to opposite MW minus plane',zero(image-target) and image.rank()==8 and zero(B*image.conjugate()-image*B))
    ck('both real normal physical Green forms vanish',all(zero(image.H*(s.I*op['G0']*op['G'][j])*image) for j in (2,3)))
    ck('actual cutoff geometric charts glue',zero(Q*T-T*Q))
    ck('wrong unchanged old MW cutoff rejected',not zero(image-prior.frame(cs)['MW']*(s.eye(32)-R*gv)/2))
    # Gauge transport commutes as a tensor factor, never an abelianization.
    h=s.Matrix([[1,1],[0,1]]);k=s.Matrix([[1,0],[1,1]])
    ck('noncommuting gauge coefficient factor retained',h*k!=k*h and zero(s.kronecker_product(L,s.eye(2))*s.kronecker_product(I,h*k)-s.kronecker_product(s.eye(32),h*k)*s.kronecker_product(L,s.eye(2))))
    records['physical_map']={'phases':[str(x) for x in ph],'flavour_permutation':'identity','scalar_reflection':False,
        'target':'opposite10D MW, same Gamma and true scalar-plane R','matrix':sparse(L)}
    records['charges']={'source_left_R':[str(Rs[2*j,2*j]) for j in range(4)],'geometric_weights':weights,
        'source_fields':['scalar lambda','holomorphic one-form psi0','holomorphic one-form psi1','anti-canonical psi2'],
        'scalar_C2_connection':'2a_R = conjugate canonical connection, supplied canonical twist'}
    records['connections']={'source':[sparse(m) for m in full],'direct_tensor':[sparse(m) for m in direct],'contracted':sparse(K)}
    records['metric_units']='orthonormal ell units; all geometric spin and R coefficients carry common inverse ell'
    records['boundary']={'epsilon':-1,'rank':8,'same_scalar_coordinates':True,'normal_bosonic_end':'credited 2E-2div J, BOTH ends unchanged in this new dictionary',
        'scope':'smooth finite local trace and actual global chart bundle, not singular graph/gauge limit'}
    records['old_gate']='same oriented old MW identification remains false; earlier reflected dictionaries and reversed end remain valid in their own scope'
    records['scope']='explicit supplied curved fermion spin/R/tensor connection on stated orbifold; not full curved bosonic/SUSY completion, singular domain or SM/three/gravity'
    return {'checks':checks,'records':records,'all_passed':all(checks.values())}
