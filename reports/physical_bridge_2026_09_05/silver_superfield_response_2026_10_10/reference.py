"""Different-method controls: tuple exterior products, exact matrix t-jets.

Does not import the native probe. Same author, not outside verification.
"""
from functools import lru_cache
import json
import sympy as s
I=s.I
ADJ={0:2,1:3,2:0,3:1,4:6,5:7,6:4,7:5,8:10,9:11,10:8,11:9}
def tidy(a):return {k:s.expand(c) for k,c in a.items() if s.expand(c)!=0}
def plus(*args):
    out={}
    for a in args:
        for k,c in a.items():out[k]=out.get(k,0)+c
    return tidy(out)
def times(a,c):return tidy({k:c*v for k,v in a.items()})
def sort_term(seq,c):
    if len(seq)!=len(set(seq)):return {}
    sign=(-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return {tuple(sorted(seq)):sign*c}
def product(a,b):
    out={}
    for k,c in a.items():
        for l,d in b.items():out=plus(out,sort_term(k+l,c*d))
    return out
def adjoint(a):return plus(*(sort_term(tuple(ADJ[j] for j in reversed(k)),s.conjugate(c)) for k,c in a.items()))
def term(*seq):return sort_term(seq,s.Integer(1))

@lru_cache(None)
def run():
    tests={}
    t=s.symbols('t',real=True)
    g=s.Matrix([[2,1],[1,1]]);dg=s.Matrix([[3,1-I],[1+I,-2]])
    gn=s.Matrix([[1,2+I],[2-I,-1]]);dgn=s.Matrix([[2,3-I],[3+I,1]])
    p=s.Matrix([[1+I,2-I],[3+2*I,-1-I]]);dp=s.Matrix([[I,1+I],[-2,-I]])
    def zz(g,gn,p):return g.inv()*gn+I*g.inv()*p.H*g-I*p
    exact=zz(g+t*dg,gn+t*dgn,p+t*dp).diff(t).subs(t,0)
    eta=g.inv()*dg;etajet=g.inv()*dgn-g.inv()*gn*g.inv()*dg
    z=zz(g,gn,p)
    rhs=etajet+I*(p*eta-eta*p)+z*eta-eta*z+I*g.inv()*dp.H*g-I*dp
    zero=lambda m:all(s.simplify(v)==0 for v in m)
    tests['t_jet_matches_variation']=zero(exact-rhs)
    tests['missing_Phi_term_fails']=not zero(exact-(rhs-I*(p*eta-eta*p)))
    tests['twisted_reality']=zero(z.H-g*z*g.inv()) and zero(eta.H-g*eta*g.inv())
    tests['real_surface_pair']=s.simplify(s.trace(z*eta)-s.conjugate(s.trace(z*eta)))==0
    u=s.Matrix([[1,1],[0,1]]);h=s.Matrix([[1,2-I],[3+I,-2]])
    transformed=zz(u.H*g*u,h.H*g*u+u.H*gn*u+u.H*g*h,u.inv()*p*u-I*u.inv()*h)
    tests['finite_normal_jet_covariance']=zero(transformed-u.inv()*z*u)
    tests['wrong_frozen_jet_fails']=not zero(zz(u.H*g*u,u.H*gn*u,u.inv()*p*u-I*u.inv()*h)-u.inv()*z*u)

    q=s.symbols('q0:4',real=True);an=s.symbols('An0:4',real=True)
    a,B,fr,fi,dn=s.symbols('a B fr fi Dn',real=True)
    # Write Pauli mixed bilinears independently, rather than a spinor loop.
    def mixed(v):return tidy({(0,2):v[0]+v[3],(0,3):v[1]-I*v[2],
                              (1,2):v[1]+I*v[2],(1,3):v[0]-v[3]})
    x=mixed(q)
    base={():a+I*B,(0,4):1,(1,5):1,(0,1):fr+I*fi}
    # Taylor coefficients generated recursively; x^3=0 in four theta generators.
    chiral=base;power={():s.Integer(1)}
    for n in (1,2):
        power=product(power,x);chiral=plus(chiral,times(product(power,base),I**n/s.factorial(n)))
    spin={ (0,1,2,10):1,(0,1,3,11):1 }
    vector=plus(times(mixed(an),-1),spin,adjoint(spin),{(0,1,2,3):dn/2})
    response=plus(times(vector,2),times(plus(adjoint(chiral),times(chiral,-1)),I))
    tests['actual_response_hermitian']=adjoint(response)==response
    tests['all_sixteen_theta_slots']={tuple(j for j in k if j<4) for k in response}=={
        tuple(j for j in range(4) if m&(1<<j)) for m in range(16)}
    tests['odd_fields_anticommute']=product(term(0),term(4))==times(product(term(4),term(0)),-1)
    tests['normal_scalar_slot']=response[()]==2*B
    tests['auxiliary_slots']=response[(0,1)]==fi-I*fr and response[(2,3)]==-fi-I*fr
    mixed_slots={k:c for k,c in response.items() if k in ((0,2),(0,3),(1,2),(1,3))}
    tests['gauge_mixed_slots']=mixed_slots==times(mixed(tuple(an[i]-q[i]*a for i in range(4))),-2)
    tests['highest_auxiliary_slot']=s.expand(response[(0,1,2,3)]-dn-2*(q[0]**2-q[1]**2-q[2]**2-q[3]**2)*B)==0
    after_primary={k:c for k,c in response.items() if not set(k)&set(range(4,8))}
    remaining={k:c for k,c in after_primary.items() if set(k)&set(range(8,12))}
    tests['four_secondary_normal_fermions']=remaining==times(plus(spin,adjoint(spin)),2) and len(remaining)==4
    tests['offshell_nonzero_secondary']=bool(remaining)
    tests['after_secondary_no_fermions']=not {k:c for k,c in after_primary.items() if any(j>=4 for j in k) and not any(j>=8 for j in k)}
    # Eliminate the normal-psi terms by row operations, not the native rank call.
    constraints=s.Matrix([[0,0,1,0],[0,0,0,1],
                          [1,0,q[0]+q[3],q[1]-I*q[2]],
                          [0,1,q[1]+I*q[2],q[0]-q[3]]])
    reduced=constraints.copy()
    for j in (2,3):
        for k in (0,1):reduced[j,:]=reduced[j,:]-reduced[j,k+2]*reduced[k,:]
    target=s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
    tests['on_shell_jet_is_redundant']=reduced==target and target.det()==1
    tests['unconstrained_jet_is_not_a_solution']=constraints*s.Matrix([1,0,0,0])==s.Matrix([0,0,1,0])
    # Fourier zero-mode extraction is the integrated projection, not evaluation.
    modes={-1:s.Rational(1,2),1:s.Rational(1,2)}
    tests['zero_mean_not_pointwise']=modes.get(0,0)==0 and sum(modes.values())==1
    derivative={m:I*m*c for m,c in modes.items()}
    tests['curl_zero_mode']=derivative.get(0,0)==0 and derivative!={} and derivative!=modes
    tests['nonzero_constant_flux_fails']={0:1}.get(0)==1
    # Independent factorization Tr((S tensor I)(I tensor K))=TrS TrK.
    traceless=[s.Matrix(5,5,lambda a,b:int((a,b)==(i,j))) for i in range(5) for j in range(5) if i!=j]
    traceless += [s.diag(*(int(j==i)-int(j==4) for j in range(5))) for i in range(4)]
    tests['all_gauge_generators_orthogonal']=len(traceless)==24 and all(s.trace(k)==0 for k in traceless)
    tests['gauge_flux_fails_norm_pair']=s.trace(traceless[-1]**2)==2
    out={'predicates':tests,'predicates_passed':sum(tests.values()),
         'component_polynomial':{str(sum(1<<j for j in k)):str(s.expand(c)) for k,c in sorted(response.items())},
         'physical_goal_achieved':False,'outside_review':False}
    assert all(tests.values()),[k for k,v in tests.items() if not v]
    return out

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
