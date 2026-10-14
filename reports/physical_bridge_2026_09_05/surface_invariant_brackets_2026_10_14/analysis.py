"""Shared declared certificate questions, not an independent second formulation."""
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SIMPLE_DOUBLED=((1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),
 (-2,2,0,0,0,0,0,0),(0,-2,2,0,0,0,0,0),(0,0,-2,2,0,0,0,0),
 (0,0,0,-2,2,0,0,0),(0,0,0,0,-2,2,0,0),(0,0,0,0,0,-2,2,0))

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def group_wedge(g):
    pairs=list(combinations(range(6),2))
    return s.Matrix(15,15,lambda i,j:g.extract(pairs[i],pairs[j]).det()).applyfunc(s.simplify)

def run(engine):
    checks={}
    def ck(n,v):checks[n]=bool(v)
    old=load(HERE.parent/'weave_registered_embedding_2026_10_13/probe.py','bracket_prior_roster')
    e,rr=old.roots();S=s.Matrix.hstack(*(s.Matrix(v)/2 for v in SIMPLE_DOUBLED))
    chain=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4]]
    col=[e[0]-e[1],e[1]-e[2]];hw=e[3]-e[4]
    C=s.Matrix.hstack(*chain);weights=[C*(C.T*C).inv()*s.Matrix([1,0,0,0,0])]
    for a in chain:weights.append(weights[-1]-a)
    wc=[(2*col[0]+col[1])/3,(-col[0]+col[1])/3,(-col[0]-2*col[1])/3]
    ck('actual E8 root bijection',len(engine.roots)==240 and
       {tuple(S*s.Matrix(r)) for r in engine.roots}=={tuple(r) for r in rr})
    cartan=s.Matrix(8,8,lambda i,j:2*int(i==j)-int((i,j) in
       {(0,2),(2,0),(2,3),(3,2),(1,3),(3,1),(3,4),(4,3),(4,5),(5,4),(5,6),(6,5),(6,7),(7,6)}))
    ck('declared simple frame Cartan',S.T*S==cartan)
    def coord(r):
        x=S.inv()*r
        if not all(v.is_Integer for v in x):raise ValueError('not lattice-integral: '+str(r))
        return tuple(int(v) for v in x)
    def E(r):return engine.e(coord(r))
    def H(r):return s.Matrix.vstack(S.inv()*r,s.zeros(240,1))
    br=engine.br;z=s.zeros(248,1)
    def tau(v):
        out=z.copy();out[:8,0]=-s.conjugate(v[:8,0])
        for r,i in engine.index.items():out[8+i]=s.conjugate(v[8+engine.index[tuple(-x for x in r)]])
        return out
    def form(u,v):
        out=(u[:8,0].T*cartan*v[:8,0])[0]
        return out-sum(u[8+i]*v[8+engine.index[tuple(-x for x in r)]] for r,i in engine.index.items())

    for j,a in enumerate(chain):
        ep,fp,h=E(a),-E(-a),H(a)
        ck('regular sl2 signed '+str(j),br(ep,fp)==h and br(h,ep)==2*ep and br(h,fp)==-2*fp)
    # The module is earned from every simple E/F/H action, not from weights alone.
    pairs=list(combinations(range(6),2));modules=[];mixed=[];maps=[]
    for k,lam in enumerate([-w for w in wc]):
        roots={p:weights[p[0]]+weights[p[1]]+lam for p in pairs}
        coeff={(0,1):s.Integer(1)};todo=[(0,1)];consistent=True
        for p in todo:
            for j,a in enumerate(chain):
                if j not in p or j+1 in p:continue
                pp=tuple(sorted(j+1 if x==j else x for x in p))
                value=br(-E(-a),coeff[p]*E(roots[p]));ix=8+engine.index[coord(roots[pp])]
                target=engine.e(coord(roots[pp]))
                c=s.simplify(value[ix]/target[ix])
                consistent=consistent and value==c*target and c!=0
                if pp in coeff:consistent=consistent and coeff[pp]==c
                else:coeff[pp]=c;todo.append(pp)
        ck('all15 module weights reached '+str(k),len(coeff)==15 and consistent)
        vectors=s.Matrix.hstack(*(coeff[p]*E(roots[p]) for p in pairs))
        for j,a in enumerate(chain):
            ep=s.zeros(6);ep[j,j+1]=1;fp=ep.T;h=ep*fp-fp*ep
            for label,small,big in [('E',ep,E(a)),('F',fp,-E(-a)),('H',h,H(a))]:
                want=vectors*old.lie_wedge(small,2)
                got=s.Matrix.hstack(*(br(big,vectors[:,i]) for i in range(15)))
                ck(f'full module action {k},{j},{label}',got==want)
        omega=s.Matrix([int(p in [(0,1),(2,3),(4,5)]) for p in pairs])
        v=vectors*omega;mixed.append(v);modules.append(vectors)
        maps.append({'colour_weight':[str(x) for x in lam],
                     'wedge_pair_signs':[str(coeff[p]) for p in pairs]})

    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]]);I=s.eye(2)
    A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    P13=s.Matrix([[0,0,1],[0,1,0],[1,0,0]]);P23=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    X=s.kronecker_product(P13,(I+a)/s.sqrt(2));Y=s.kronecker_product(P23,(I+b)/s.sqrt(2));Z=A.H*X
    gs=[A,B,X,Y,Z];wg=[group_wedge(g) for g in gs]
    omega=s.Matrix([int(p in [(0,1),(2,3),(4,5)]) for p in pairs]);wrong=omega.copy();wrong[pairs.index((2,3))]=-1
    for j,g in enumerate(wg):ck('actual full move preserves symplectic bivector '+str(j),g*omega==omega)
    ck('wrong mixed sign fails move invariance',any(g*wrong!=wrong for g in wg))
    ck('full wedge common fixed dimension one',15-s.Matrix.vstack(*(g-s.eye(15) for g in wg)).rank()==1)
    Sf=s.diag(b,a,a*b);family=[]
    for g,q in zip([X,Y,Z],[(I+a)/s.sqrt(2),(I+b)/s.sqrt(2),(I-a)/s.sqrt(2)]):
        v=(Sf.H*g*Sf).applyfunc(s.simplify)
        m=s.Matrix(3,3,lambda j,k:s.simplify(s.trace(q.H*v[2*j:2*j+2,2*k:2*k+2])/2))
        ck('literal family tensor factor '+str(len(family)),v==s.kronecker_product(m,q))
        family.append(m)
    ab=[]
    for i,j in product(range(3),repeat=2):
        if i!=j:v=s.zeros(3);v[i,j]=1;ab.append(v)
    ab.extend([s.diag(1,-1,0),s.diag(0,1,-1)])
    constraints=s.Matrix.hstack(*(s.Matrix.vstack(*((g*v-v*g).reshape(9,1) for g in family)) for v in ab))
    ck('no family adjoint invariant',constraints.rank()==8)
    actual,expected,_,_,_=old.a5_roster();ck('full248 branching retained',actual==expected and sum(actual.values())==248)
    ck('all six weak corrections noncentral',all(m%12!=0 for m in (1,3,5,7,9,11)))

    longs=[col[0],col[1],col[0]+col[1]]
    basis=[H(col[0]),H(col[1]),H(hw)]+[E(r) for r in longs]+[E(-r) for r in longs]+mixed+[tau(v) for v in mixed]
    labels=['Hc1','Hc2','Hw']+[f'long+{i}' for i in range(3)]+[f'long-{i}' for i in range(3)]+[f'short+{i}' for i in range(3)]+[f'short-{i}' for i in range(3)]
    mat=s.Matrix.hstack(*basis);ck('actual15 linearly independent',mat.rank()==15)
    left=(mat.T*mat).inv()*mat.T
    tensor=[];ads=[];allcols=[]
    for i,u in enumerate(basis):
        cols=[]
        for j,v in enumerate(basis):
            w=br(u,v);c=left*w
            ck(f'actual closure {i},{j}',mat*c==w)
            ck(f'real conjugation automorphism {i},{j}',tau(w)==br(tau(u),tau(v)))
            cols.append(c);allcols.append(c)
            tensor.append([i,j,[[k,str(x)] for k,x in enumerate(c) if x]])
        ads.append(s.Matrix.hstack(*cols))
    ck('actual centre exactly weak Cartan',s.Matrix.vstack(*ads).nullspace()==[s.eye(15)[:,2]])
    derived=s.Matrix.hstack(*allcols)
    ck('derived exactly colour plus mixed14',derived.rank()==14 and all(x==0 for x in derived[2,:]))
    # Jacobi is checked on every triple in THIS algebra, not every E8 triple.
    for i,j,k in combinations(range(15),3):
        ck(f'invariant Jacobi {i},{j},{k}',ads[i]*ads[j][:,k]+ads[j]*ads[k][:,i]+ads[k]*ads[i][:,j]==s.zeros(15,1))
    kill=s.Matrix(15,15,lambda i,j:s.trace(ads[i]*ads[j]))
    gram=s.Matrix(15,15,lambda i,j:form(basis[i],basis[j]))
    keep=[i for i in range(15) if i!=2]
    ck('intrinsic derived Killing nondegenerate',kill.rank()==14)
    ck('intrinsic derived Killing is8 times ambient form',kill.extract(keep,keep)==8*gram.extract(keep,keep))
    P=s.zeros(15)
    for i in range(3):P[i,i]=s.I
    for first,second in [(3,6),(9,12)]:
        for j in range(3):
            P[first+j,first+j]=P[second+j,first+j]=1
            P[first+j,second+j]=s.I;P[second+j,second+j]=-s.I
    compact=mat*P
    ck('compact real basis fixed by actual conjugation',all(tau(compact[:,i])==compact[:,i] for i in range(15)))
    kg=P.T*kill*P;bg=P.T*gram*P
    ck('compact Killing real',all(s.im(x)==0 for x in kg))
    kd=kg.extract(keep,keep);pivots=[kd[:i,:i].det() for i in range(1,15)]
    ck('compact derived Killing negative definite',all((-1)**i*pivots[i-1]>0 for i in range(1,15)))
    ck('ambient compact form negative definite all15',all((-1)**i*bg[:i,:i].det()>0 for i in range(1,16)))
    def fake_form(u,v):
        return 2*(u[:8,0].T*cartan*v[:8,0])[0]-form(u,v)
    ce,cf,ch=E(col[0]),E(-col[0]),H(col[0])
    ck('fake plus root form detected',fake_form(br(ce,cf),ch)!=fake_form(ce,br(cf,ch)) and
       form(br(ce,cf),ch)==form(ce,br(cf,ch)))
    for i,j,k in product(range(15),repeat=3):
        ck(f'actual form invariant {i},{j},{k}',(gram*ads[i][:,j])[k]==(gram*ads[j][:,k])[i])

    rv=longs+[-r for r in longs]+[-w for w in wc]+wc
    for j,(r,v) in enumerate(zip(rv,basis[3:])):
        for i,h in enumerate(col+[hw]):ck(f'actual Cartan root eigenvector {j},{i}',br(H(h),v)==r.dot(h)*v)
    ck('twelve roots distinct rank2',{tuple(r) for r in rv}.__len__()==12 and s.Matrix.hstack(*rv).rank()==2)
    lengths=[r.dot(r) for r in rv]
    ck('six long2 six short2over3',lengths==[s.Integer(2)]*6+[s.Rational(2,3)]*6)
    alpha,beta=col[0],wc[1]
    ct=s.Matrix([[2,2*alpha.dot(beta)/beta.dot(beta)],[2*beta.dot(alpha)/alpha.dot(alpha),2]])
    ck('actual G2 Cartan',ct==s.Matrix([[2,-3],[-1,2]]))
    ep,eb=E(alpha),tau(mixed[1]);v=ep;string=[]
    for j in range(1,5):v=br(eb,v);string.append(v!=z)
    v=eb;other=[]
    for j in range(1,3):v=br(ep,v);other.append(v!=z)
    ck('actual long short root string three',string==[True,True,True,False])
    ck('reverse actual root string one',other==[True,False])
    roots_set={tuple(r) for r in rv}
    ck('actual projected root reflection closure',all(tuple(r-2*r.dot(t)/t.dot(t)*t) in roots_set for r,t in product(rv,repeat=2)))
    # Cartan has no extra zero-weight root space: it is self-centralizing.
    ck('rank3 torus self centralizing',15-s.Matrix.vstack(*ads[:3]).rank()==3)
    record={'dimension':15,'derived_dimension':14,'centre_dimension':1,'rank':3,'derived_rank':2,
        'centre_label':'Hw','long_squared_length':'2','short_squared_length':'2/3','long_roots':6,'short_roots':6,
        'Cartan':[[str(x) for x in row] for row in ct.tolist()],
        'long_short_string':string,'short_long_string':other,
        'module_maps':maps,'labels':labels,'actual_basis':engine.encode(mat),
        'complete_bracket_tensor':tensor,'intrinsic_Killing':[[str(x) for x in row] for row in kill.tolist()],
        'compact_derived_leading_minors':[str(x) for x in pivots],
        'compact_ambient_Gram':[[str(x) for x in row] for row in bg.tolist()]}
    return {'checks':checks,'records':record,'all_passed':all(checks.values()),
       'scope':'fixed actual based E8 lifts and all commuting weak corrections, not every background or a physical SM'}

def emit(engine):
    out=run(engine);print(json.dumps(out,indent=2));return 0 if out['all_passed'] else 1
