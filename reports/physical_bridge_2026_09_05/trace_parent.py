"""R95 exact same-parent transport safeguards. No file writes.

Import/run only after the pushed seal. This is conditional gauge theory,
not a selected SM, chiral spectrum, gravitational or quantum completion.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
import importlib.util
import json
from pathlib import Path
import sympy as sp


def zero(M):
    return all(sp.simplify(a)==0 for a in M)


def comm(X,Y):
    return X*Y-Y*X


@lru_cache(None)
def generators(n=4):
    E=sp.zeros(n+1)
    for j in range(n):E[j,j+1]=sp.sqrt((j+1)*(n-j))
    return E,E.T,sp.diag(*[n-2*j for j in range(n+1)])


def symmetric(M,n=4):
    u,v=sp.symbols('u v')
    columns=[]
    for j in range(n+1):
        poly=sp.Poly((M[0,0]*u+M[1,0]*v)**(n-j)*(M[0,1]*u+M[1,1]*v)**j,u,v)
        columns.append([poly.coeff_monomial(u**(n-k)*v**k) for k in range(n+1)])
    un=sp.Matrix(columns).T
    D=sp.diag(*[sp.sqrt(sp.binomial(n,j)) for j in range(n+1)])
    return sp.simplify(D.inv()*un*D)


def wedge(X):
    pairs=list(combinations(range(X.rows),2)); W=sp.zeros(len(pairs))
    for col,(i,j) in enumerate(pairs):
        for k in range(X.rows):
            for a,b,value in ((k,j,X[k,i]),(i,k,X[k,j])):
                if a!=b:W[pairs.index(tuple(sorted((a,b)))),col]+=(value if a<b else -value)
    return W


def adjoint(X):
    # Row-vectorization of XB-BX on ALL End, including its trivial scalar.
    return sp.kronecker_product(X,sp.eye(X.rows))-sp.kronecker_product(sp.eye(X.rows),X.T)


@lru_cache(None)
def sector_kernels(n=4,plus_line=False):
    G=generators(n)
    if plus_line:G=tuple(sp.diag(X,sp.zeros(1)) for X in G)
    kernel=lambda actions:len(sp.Matrix.vstack(*actions).nullspace())
    return (kernel(G),kernel(tuple(wedge(X) for X in G)),
            kernel(tuple(adjoint(X) for X in G))-1)


def trace248(X,Y):
    return sp.trace(adjoint(X)*adjoint(Y))+20*sp.trace(X*Y)+10*sp.trace(wedge(X)*wedge(Y))


@lru_cache(None)
def roots_roster():
    roots=[]
    for i,j in combinations(range(8),2):
        for a,b in product((-1,1),repeat=2):
            r=[0]*8;r[i]=a;r[j]=b;roots.append(sp.Matrix(r))
    for signs in product((-1,1),repeat=8):
        if sum(a==-1 for a in signs)%2==0:roots.append(sp.Matrix(signs)/2)
    e=[sp.eye(8)[:,j] for j in range(8)]
    gauge=[e[j]-e[j+1] for j in range(4)]
    structure=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-sum(e,sp.zeros(8,1))/2]
    f=[tuple(int(j==i)-int(j==i+1) for i in range(4)) for j in range(5)]
    neg=lambda x:tuple(-a for a in x)
    add=lambda x,y:tuple(a+b for a,b in zip(x,y))
    ten=[add(f[i],f[j]) for i,j in combinations(range(5),2)]
    adj=[add(f[i],neg(f[j])) for i,j in permutations(range(5),2)]+[(0,)*4]*4
    reps={'1':[(0,)*4],'5':f,'bar5':[neg(w) for w in f],
          '10':ten,'bar10':[neg(w) for w in ten],'24':adj}
    actual=Counter(tuple(r.dot(a) for a in gauge+structure) for r in roots)
    actual[(0,)*8]+=8
    branches=[('24','1'),('1','24'),('10','5'),('bar10','bar5'),('5','bar10'),('bar5','10')]
    expected=Counter(x+y for a,b in branches for x in reps[a] for y in reps[b])
    wrong=Counter(x+y for a,b in branches[:4]+[('5','10'),('bar5','bar10')]
                  for x in reps[a] for y in reps[b])
    q=sp.symbols('q0:4'); V=sum((a*b for a,b in zip(structure,q)),sp.zeros(8,1))
    trace_root=sp.expand(sum(r.dot(V)**2 for r in roots))
    trace5=sp.expand(sum(sum(a*b for a,b in zip(w,q))**2 for w in f))
    return dict(roots=roots,actual=actual,expected=expected,wrong=wrong,
                gauge=gauge,structure=structure,trace_root=trace_root,trace5=trace5)


@lru_cache(None)
def geometry(n=4):
    x,y=sp.symbols('x y',real=True);z=sp.Symbol('z',positive=True)
    coords=(x,y,z);E,F,H=generators(n);C=(E/z,sp.I*E/z,H/(2*z))
    curvature=[C[j].diff(coords[i])-C[i].diff(coords[j])+comm(C[i],C[j]) for i,j in combinations(range(3),2)]
    div=sp.simplify(z**3*sum(((a+a.H).applyfunc(lambda b:sp.diff(b/z,t)) for a,t in zip(C,coords)),sp.zeros(n+1)))
    bracket=sp.simplify(z**2*sum((comm(a,a.H) for a in C),sp.zeros(n+1)))
    phi=tuple((a+a.H)/2 for a in C);A=tuple((a-a.H)/2 for a in C)
    norm=sp.simplify(z**2*sum(sp.trace(a*a) for a in phi))
    flat_div=sum(((a+a.H).diff(t) for a,t in zip(C,coords)),sp.zeros(n+1))
    flat_moment=sp.simplify(flat_div+sum((comm(a,a.H) for a in C),sp.zeros(n+1)))
    J=sp.zeros(n+1)
    for j in range(n+1):J[j,n-j]=(-1)**j
    gauge_curv=[A[j].diff(coords[i])-A[i].diff(coords[j])+comm(A[i],A[j]) for i,j in combinations(range(3),2)]
    return dict(C=C,E=E,F=F,H=H,curvature=curvature,div=div,bracket=bracket,
                norm=norm,J=J,gauge_curvature=gauge_curv,flat_moment=flat_moment,z=z)


@lru_cache(None)
def prior_register():
    spec=importlib.util.spec_from_file_location('r95_r94_reused',Path(__file__).with_name('register_action.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


@lru_cache(None)
def checks():
    out={};G=generators();g=geometry();E,F,H=G
    for name,M in [('HE',comm(H,E)-2*E),('HF',comm(H,F)+2*F),('EF',comm(E,F)-H)]:
        out['sl2_'+name]=zero(M)
    t=sp.symbols('t');e=sp.Matrix([[0,1],[0,0]]);f=e.T;h=sp.diag(1,-1)
    for label,small,big in zip(('E','F','H'),(e,f,h),G):
        curve=sp.eye(2)+t*small if label!='H' else sp.diag(sp.exp(t),sp.exp(-t))
        out['derived_group_'+label]=zero(symmetric(curve).diff(t).subs(t,0)-big)
    out['PSL2_central_descent']=symmetric(-sp.eye(2))==sp.eye(5)
    out['odd_power_keeps_center']=symmetric(-sp.eye(2),3)==-sp.eye(4)
    a=sp.Matrix([[2,1],[1,1]]);b=sp.Matrix([[1,2],[0,1]])
    out['group_homomorphism']=symmetric(a*b)==symmetric(a)*symmetric(b)
    out['actual_SL5_determinant']=symmetric(a).det()==1
    rot=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5)],[-sp.Rational(4,5),sp.Rational(3,5)]])
    out['actual_SU2_positive_metric']=symmetric(rot).T*symmetric(rot)==sp.eye(5)
    un=symmetric(sp.eye(2)+e)-sp.eye(5)
    out['regular_unipotent_image']=zero(un**5) and not zero(un**4)
    for aa,bb in product((-1,1),repeat=2):
        out['central_lift_alias_'+str(aa)+str(bb)]=symmetric(aa*a)==symmetric(a) and symmetric(bb*b)==symmetric(b)
    r=roots_roster()
    out['R40_complete_roster']=len(r['roots'])==240 and sum(r['actual'].values())==248 and r['actual']==r['expected']
    out['wrong_bar_roster_rejected']=r['actual']!=r['wrong'] and sum(r['wrong'].values())==248
    out['R40_full_Cartan_trace60']=sp.expand(r['trace_root']-60*r['trace5'])==0
    out['omitted_E8_trace_factor_rejected']=sp.expand(r['trace_root']-r['trace5'])!=0
    a4=sp.Matrix(4,4,lambda i,j:2 if i==j else -1 if abs(i-j)==1 else 0)
    out['surviving_A4_root_system']=sp.Matrix(4,4,lambda i,j:r['gauge'][i].dot(r['gauge'][j]))==a4
    for i,j in product(range(3),repeat=2):
        out['trace20_'+str(i)+str(j)]=sp.simplify(sp.trace(G[i]*G[j])-20*sp.trace((e,f,h)[i]*(e,f,h)[j]))==0
        out['trace1200_'+str(i)+str(j)]=sp.simplify(trace248(G[i],G[j])-1200*sp.trace((e,f,h)[i]*(e,f,h)[j]))==0
    for i,j,k in product(range(3),repeat=3):
        out['CS_cubic_'+str(i)+str(j)+str(k)]=sp.simplify(trace248(G[i],comm(G[j],G[k]))-1200*sp.trace((e,f,h)[i]*comm((e,f,h)[j],(e,f,h)[k])))==0
    for k,M in enumerate(g['curvature']):out['flatness_'+str(k)]=zero(M)
    out['full_moment']=zero(g['div']+g['bracket']) and g['div']==-2*H and g['bracket']==2*H
    out['dropping_commutator_rejected']=not zero(g['div'])
    out['Euclidean_metric_rejected']=not zero(g['flat_moment'])
    out['actual_noncommuting_background']=any(not zero(M) for M in g['gauge_curvature'])
    area,Z=sp.symbols('area Z',positive=True)
    tail=sp.integrate(area*g['norm']/g['z']**3,(g['z'],Z,sp.oo))
    out['positive_norm30']=g['norm']==30
    out['finite_positive_cusp_tail']=tail==15*area/Z**2
    out['full_E8_norm1800']=60*g['norm']==1800
    out['R39_banked_norm15']=geometry(3)['norm']==15
    k0,k1,k2=sector_kernels()
    out['full_invariant_kernels']= (k0,k1,k2)==(0,0,0)
    out['complete248_gauge24']=24+20*k0+10*k1+k2==24
    w0,w1,w2=sector_kernels(3,True)
    out['four_plus_line_false_identification']=24+20*w0+10*w1+w2==55
    J=g['J'];out['symmetric_unitary_duality']=J.T==J and J.H*J==sp.eye(5)
    for i,C in enumerate(g['C']):
        out['flat_duality_'+str(i)]=zero(J*C+C.T*J)
        out['positive_adjoint_duality_'+str(i)]=zero(J*C.H+C.conjugate()*J)
        W=wedge(C);JW=sp.Matrix([[J[k,i]*J[l,j]-J[k,j]*J[l,i] for i,j in combinations(range(5),2)] for k,l in combinations(range(5),2)])
        out['exterior_duality_'+str(i)]=JW.H*JW==sp.eye(10) and zero(JW*W+W.T*JW)
    av=sp.Matrix(2,2,sp.symbols('a0:4'));bv=sp.Matrix(2,2,sp.symbols('b0:4'))
    bracket=sp.expand(sp.trace((av-sp.trace(av)*sp.eye(2)/2)*(bv-sp.trace(bv)*sp.eye(2)/2)))
    standard=sp.trace(av*bv)-sp.trace(av)*sp.trace(bv)/2
    out['Goldman_trace_gradient']=sp.expand(bracket-standard)==0
    out['R94_pairing_is_half_trace']=sp.expand(2*bracket-(2*sp.trace(av*bv)-sp.trace(av)*sp.trace(bv)))==0
    c,u,v=sp.symbols('c u v');theta_u=c*v;theta_v=-c*u
    boundary=sp.diff(theta_v,u)-sp.diff(theta_u,v)
    coefficient=-boundary/c*1200*2
    out['derived_boundary_scale4800']=coefficient==4800
    out['wrong_Goldman_half_factor_rejected']=coefficient!=2400
    s,Pprev,pnext=sp.symbols('s Pprev pnext')
    variation=4800*c*(-(-s)*Pprev-s*pnext)
    out['scaled_registered_first_variation']=sp.expand(variation-4800*c*s*(Pprev-pnext))==0
    out['unflipped_registered_relation_rejected']=sp.expand((-4800*c*s*(Pprev+pnext)).subs(Pprev,pnext))==-9600*c*s*pnext
    old=prior_register(); rg=old.generating()
    out['same_nonlinear_generating_primitive']=rg['normal'](rg['pQ']-rg['Pq'])==0 and rg['normal'](rg['cross'])!=0
    for i in range(3):out['actual_R94_trace_map_'+str(i)]=rg['normal'](rg['new'][i]-rg['target'][i])==0
    for i,row in enumerate(old.orbit()):out['nonreal_geometric_chart_'+str(i)]=row['discriminant']==-sp.Rational(3,16) and any(sp.simplify(x)!=0 for x in row['grad'])
    return {k:bool(v) for k,v in out.items()}


def report():
    values=checks()
    return dict(scope='R95 conditional local relative trace-sector transport and oriented hyperbolic parent baseline',
                checks=values,passed=sum(values.values()),total=len(values),failed=[k for k,v in values.items() if not v],
                source_action_coefficient_derived=False,global_faithful_register_map=False,
                non_author_acceptance=False,physical_goal_achieved=False)


if __name__=='__main__':
    data=report();print(json.dumps(data,sort_keys=True));raise SystemExit(0 if not data['failed'] else 1)
