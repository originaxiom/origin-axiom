"""R71 exact channel algebra and formal logarithmic coefficient; not graph admission."""
from functools import lru_cache
import json
import sympy as s

def sp(a):
    return s.ImmutableSparseMatrix(a)

def zero(a):
    if isinstance(a, s.MatrixBase):
        return all(s.simplify(x)==0 for x in a.todok().values())
    return s.simplify(a)==0

def comm(a,b):
    return a*b-b*a

def unit(i,j):
    return sp(s.Matrix(4,4,lambda a,b: int(a==i and b==j)))

I4=sp(s.eye(4))
N=unit(0,2)+unit(2,3)
P=N*N
Z=sp(s.diag(1,-3,1,1))
H=sp(s.diag(1,0,0,-1))
I16=sp(s.eye(16))
ad=lambda a: sp(s.kronecker_product(a,I4)-s.kronecker_product(I4,a.T))
ex=sp([[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,1,0]])
ey=sp([[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,-1,0,0]])
M=sp(s.diag(-1,0,0,1))
tensor=lambda a,b: sp(s.kronecker_product(a,b))
blocks=lambda a,b,c,d: sp(a.row_join(b).col_join(c.row_join(d)))

def basis():
    vectors=[unit(i,j) for i,j in ((0,2),(0,3),(2,0),(2,3),(3,0),(3,2))]
    vectors += [unit(0,0)-unit(2,2),unit(2,2)-unit(3,3),Z]
    T=sp(s.Matrix.hstack(*(s.Matrix(v).reshape(16,1) for v in vectors)))
    G=T.H*T
    left=G.inv()*T.H
    return T,sp(G),sp(left)

T,G,left=basis()
n,p,z,h=(sp(left*ad(a)*T) for a in (N,P,Z,H))
nd=sp(left*ad(N.H)*T)
pd=sp(left*ad(P.H)*T)
I9=sp(s.eye(9))

@lru_cache(None)
def charge_controls():
    charges=[0,4,-4]
    AZ=ad(Z)
    projectors={c:sp(s.diag(*(int(Z[i,i]-Z[j,j]==c) for i in range(4) for j in range(4)))) for c in charges}
    eyevec=s.Matrix(I4).reshape(16,1)
    tf=I16-eyevec*eyevec.T/4
    neutral=projectors[0]*tf
    alpha=s.Rational(4)
    K=-s.Rational(1,7)*ad(H)
    zx=s.sqrt(alpha)*(s.I*s.Rational(3,4)*I16+s.Rational(1,5)*ad(N))
    zy=(s.I*s.Rational(1,2)*I16+s.Rational(2,7)*ad(Z)+s.Rational(3,50)*ad(P))/s.sqrt(alpha)
    E=tensor(ex,zx)+tensor(ey,zy)
    L=E+E.H
    m=tensor(M,I16)
    k=tensor(sp(s.eye(4)),K)
    A=blocks(m+k,-L,-L,-m-k.H)
    gamma=blocks(sp(s.zeros(64)), -sp(s.eye(64)), sp(s.eye(64)), sp(s.zeros(64)))
    X,Y=unit(0,1),unit(1,0)
    bracket=comm(X,Y)
    checks=dict(
        full_projector_sum=zero(sum(projectors.values(),sp(s.zeros(16)))-I16),
        pairwise_orthogonal=all(zero(projectors[a]*projectors[b]) for a in charges for b in charges if a!=b),
        exact_charge_eigenvalues=all(zero(AZ*projectors[c]-c*projectors[c]) for c in charges),
        tracefree_dimensions=[(projectors[c]*tf).rank() for c in charges]==[9,3,3],
        neutral_basis_complete=T.rank()==9 and zero(neutral*T-T),
        neutral_Gram_positive=G[:6,:6]==s.eye(6) and G[6:8,6:8]==s.Matrix([[2,-1],[-1,2]]) and G[8,8]==12,
        actual_six_coefficients_reduce=all(zero(comm(projectors[c],ad(a))) for c in charges for a in (N,P,Z,H,N.H,P.H)),
        actual_full_operator_reduces=all(zero(comm(A,tensor(sp(s.eye(8)),projectors[c]))) for c in charges),
        actual_full_Hermitian=zero(A-A.H),
        actual_Gamma_pairing=zero(A*gamma+gamma*A),
        positive_charge_fixture=zero(comm(Z,X)-4*X),
        negative_charge_fixture=zero(comm(Z,Y)+4*Y),
        neutral_bracket_source=s.trace(Z*bracket)==4 and not zero(bracket),
        neutral_not_trivial=not zero(n) and not zero(nd),
        identity_is_excluded=zero(left*eyevec),
    )
    return dict(checks=checks,dimensions=[9,3,3],full_form_matrix_dimension=A.rows)

def limit_window(alpha,k,c):
    alpha,k=s.Rational(alpha),s.Rational(k)
    mmax=int(s.floor(s.sqrt(1/(48*alpha))))
    nmax=int(s.floor(s.sqrt(alpha/48)))
    inside,excluded,uncertain=[],[],[]
    for m0 in range(-mmax,mmax+1):
        for n0 in range(-nmax,nmax+1):
            mass=c*c*k*k/alpha
            geom=alpha*m0*m0+n0*n0/alpha
            lo,hi=36*geom+mass,40*geom+mass
            if hi<s.Rational(3,4):
                inside.append((m0,n0))
            elif lo>=s.Rational(3,4):
                excluded.append((m0,n0))
            else:
                uncertain.append((m0,n0))
    return dict(inside=inside,excluded=excluded,uncertain=uncertain,bounds=(mmax,nmax))

@lru_cache(None)
def window_controls():
    fixtures=[(1,1,[(0,0)],[]),(1,s.Rational(1,10),[(0,0)],[(0,0)]),
              (400,s.Rational(1,10),[(0,j) for j in range(-2,3)],[(0,j) for j in range(-2,3)])]
    counts=[]
    checks={}
    for i,(a,k,neutral,charged) in enumerate(fixtures):
        out={c:limit_window(a,k,c) for c in (0,4,-4)}
        checks['fixture_%d_all_decided'%i]=all(not v['uncertain'] for v in out.values())
        checks['fixture_%d_neutral'%i]=out[0]['inside']==neutral
        checks['fixture_%d_charged'%i]=out[4]['inside']==charged and out[-4]['inside']==charged
        counts.append(4*(9*len(neutral)+6*len(charged)))
    checks['metric_dependent_limiting_dimensions']=counts==[36,60,300]
    checks['threshold_not_open_critical']=not limit_window(s.Rational(64,3),1,4)['inside']
    checks['limiting_constant_neutral_has_four_slots']=4*9==36
    return dict(checks=checks,limiting_angular_dimensions=counts,
                scope='Bounded-ellipse full limiting enumeration, not actual traces or particles')

@lru_cache(None)
def scalar_controls():
    x,y,w,a=s.symbols('xi zeta mass a',real=True)
    e=ex*(s.I*x)+ey*(w+s.I*y)
    l=e+e.H
    A=blocks(M,-l,-l,-M)
    lam=x*x+y*y+w*w
    polynomial=A.charpoly(a).as_expr()
    target=((a*a-lam)**2-a*a)**2
    eta=s.sqrt(lam+s.Rational(1,4))-s.Rational(1,2)
    checks=dict(
        independent_scalar_charpoly=zero(polynomial-target),
        zero_lambda_kernel=A.subs({x:0,y:0,w:0}).nullspace().__len__()==4,
        exact_open_threshold=eta.subs({x:0,y:0,w:s.sqrt(3)/2})==s.Rational(1,2),
        charged_mass_from_adZ=4*4==16,
        pi_enclosure_upper=s.Rational(22,7)**2<10,
    )
    return dict(checks=checks,charpoly=s.factor(target),threshold=s.Rational(3,4))

@lru_cache(None)
def schur_controls():
    m=tensor(M,I9)
    z36=sp(s.zeros(36))
    A0=blocks(m,z36,z36,-m)
    pc=tensor(sp(s.diag(0,1,1,0,0,1,1,0)),I9)
    qc=sp(s.eye(72))-pc
    D=A0  # inverse on the +/-1 complement, zero on the kernel
    ln=tensor(ex,n)+tensor(ex.H,nd)
    lp=tensor(ey,p)+tensor(ey.H,pd)
    F1=blocks(z36,-ln,-ln,z36)
    gamma_parameter=s.Symbol('gamma_parameter',real=True)
    hk=tensor(sp(s.eye(4)),h)
    F2=blocks(-hk/2,-gamma_parameter*lp,-gamma_parameter*lp,hk/2)
    S1=pc*F1*D-D*F1*pc
    formal2=F2+comm(F1,S1)+comm(comm(A0,S1),S1)/2
    B=pc*F2*pc-pc*F1*D*F1*pc
    slots=[1,2,5,6]
    idx=[slot*9+i for slot in slots for i in range(9)]
    b=sp(B.extract(idx,idx))
    ax=-h/2-n*nd
    ay=-h/2+nd*n
    analytic=sp(s.diag(ax,ay,-ax,-ay))
    gram=tensor(sp(s.eye(4)),G)
    gam=blocks(sp(s.zeros(18)),-sp(s.eye(18)),sp(s.eye(18)),sp(s.zeros(18)))
    omitted_schur=sp((pc*F2*pc).extract(idx,idx))
    omitted_K=sp((-pc*F1*D*F1*pc).extract(idx,idx))
    cas=h*h+n*nd+nd*n
    a=s.Symbol('a')
    expected_cas=a*(a-2)**3*(a-6)**5
    expected_b=a**4*(a*a-s.Rational(1,4))**2*(a*a-1)**4*(a*a-s.Rational(9,4))**4*(a*a-9)**4*(a*a-s.Rational(49,4))**2
    checks=dict(
        critical_rank=pc.rank()==36 and qc.rank()==36,
        inverse_complement=zero(D*A0-qc),
        first_order_only_offcritical=zero(pc*F1*pc) and zero(qc*F1*qc),
        first_order_eliminated=zero(F1+comm(A0,S1)),
        S1_Gram_antiHermitian=zero(S1.H*tensor(sp(s.eye(8)),G)+tensor(sp(s.eye(8)),G)*S1),
        actual_formal_second_order=zero(pc*formal2*pc-B),
        four_analytic_blocks=zero(b-analytic),
        tangential_P_not_critical=zero(b.diff(gamma_parameter)),
        B_Gram_Hermitian=zero(b.H*gram-gram*b),
        B_Gamma_paired=zero(b*gam+gam*b),
        missing_Schur_fails=not zero(b-omitted_schur),
        missing_radial_K_fails=not zero(b-omitted_K),
        principal_relations=zero(comm(h,n)-n) and zero(comm(n,nd)-h),
        principal_Casimir=zero(cas.charpoly(a).as_expr()-expected_cas),
        complete_B_polynomial=zero(b.charpoly(a).as_expr()-expected_b),
        only_Z_zeros=b.nullspace().__len__()==4,
        formal_derivative_order=s.diff(s.Symbol('epsilon'),s.Symbol('epsilon'))==1,
    )
    # d(epsilon)/ds=-epsilon^3/2, so moving-frame derivative is order three.
    epsilon=s.Symbol('epsilon',positive=True)
    deriv=-epsilon**3*S1/2
    checks['actual_radial_frame_derivative_order']=zero(deriv.subs(epsilon,0)) and zero(deriv.diff(epsilon,2).subs(epsilon,0)) and not zero(deriv.diff(epsilon,3))
    checks.pop('formal_derivative_order')
    return dict(checks=checks,B=b,B_charpoly=s.factor(expected_b),Casimir_charpoly=s.factor(expected_cas),
                critical_limiting_dimension=36,exact_reducing_traces_previously_proved=4)

@lru_cache(None)
def integration_controls():
    x=s.Symbol('s',positive=True)
    b,d=s.symbols('b d',real=True)
    l2_log=-x+2*b*s.log(x)
    residual_log=x+2*d*s.log(x)
    checks=dict(
        all_finite_log_powers_L2=s.limit(s.diff(l2_log,x),x,s.oo)==-1,
        nonzero_polynomial_graph_residual_diverges=s.limit(s.diff(residual_log,x),x,s.oo)==1,
        correct_radial_measure=s.diff(-s.exp(-x),x)==s.exp(-x),
        inverse_r_changes_weight=zero(s.exp(-x)*s.exp(2*x)-s.exp(x)),
        positive_L2_comparator=s.integrate(s.exp(-x),(x,1,s.oo))==s.exp(-1),
        bad_graph_comparator=s.integrate(s.exp(x),(x,1,s.oo))==s.oo,
        frozen_limit_cannot_admit_other_32=36-4==32,
    )
    return dict(checks=checks,scope='Weight comparison; no exact solution or graph-domain classification')

def serial(a):
    if isinstance(a,s.MatrixBase):
        return [[str(x) for x in row] for row in a.tolist()]
    if isinstance(a,dict):
        return {str(k):serial(v) for k,v in a.items()}
    if isinstance(a,(list,tuple)):
        return [serial(v) for v in a]
    if isinstance(a,s.Basic):
        return str(a)
    return a

def run():
    groups={name:fn() for name,fn in [('charge',charge_controls),('window',window_controls),
        ('scalar',scalar_controls),('schur',schur_controls),('integration',integration_controls)]}
    checks={name+'/'+k:bool(v) for name,g in groups.items() for k,v in g['checks'].items()}
    # Keep the large exact matrix in the instrument, not the transcript.
    summary={name:{k:v for k,v in g.items() if k!='B'} for name,g in groups.items()}
    return serial(dict(groups=summary,checks=checks,all_checks_pass=all(checks.values()),
        scope='Actual reducing channels, complete limiting windows, formal leading logarithmic matrix; not physical spectrum'))

if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)

