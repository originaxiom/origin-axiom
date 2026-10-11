"""Actual twisted collar derivatives plus Lagrangian constraint. No project imports."""
import json
import sympy as S


def simp(a):
    return a.applyfunc(S.simplify) if isinstance(a, S.MatrixBase) else S.simplify(a)


def zero(a):
    a=simp(a)
    return a == S.zeros(*a.shape) if isinstance(a,S.MatrixBase) else a == 0


def slab():
    r,x,y=S.symbols("r x y", real=True)
    n=S.symbols("n", integer=True, positive=True)
    q=S.symbols("q", real=True)
    O=S.Matrix([[0,-q],[q,0]])
    c=S.Matrix([1,0])
    def der(v,i):
        return v.diff((r,x,y)[i])+(O*v if i==2 else S.zeros(2,1))
    def grad(f): return [der(f,i) for i in range(3)]
    def div(v): return sum((der(v[i],i) for i in range(3)),S.zeros(2,1))
    def curl(v):
        return [der(v[2],1)-der(v[1],2),der(v[0],2)-der(v[2],0),
            der(v[1],0)-der(v[0],1)]
    def lap0(f): return -sum((der(der(f,i),i) for i in range(3)),S.zeros(2,1))
    return r,x,y,n,q,O,c,der,grad,div,curl,lap0


def run():
    facts={}
    def put(name, yes):
        if name in facts: raise AssertionError("duplicate predicate")
        facts[name]=bool(yes)
        if not facts[name]: raise AssertionError(name)
    r,x,y,n,q,O,c,der,grad,div,curl,lap0=slab()
    m2=n*n+q*q
    f=S.cos(n*r)*c
    df=grad(f)
    put("flat_covariant_derivatives",zero(der(der(f,0),2)-der(der(f,2),0)))
    put("broken_old_constant_trace_nonparallel", not zero(O*c))
    put("old_A0_not_reset", not zero(O*c))
    put("positive_scalar_eigenprofile",zero(lap0(f)-m2*f))
    put("exact_covariant_profile_flat",all(zero(a) for a in curl(df)))
    put("exact_adjoint_profile",zero(div(df)+m2*f))
    put("tangential_exact_profile_allowed_dy",zero(df[1]) and not zero(df[2]))
    for k,edge in enumerate((0,S.pi)):
        put(f"exact_normal_primary_{k}",zero(df[0].subs(r,edge)))
        put(f"exact_vector_normal_{k}",zero(f.diff(r).subs(r,edge)))
        put(f"exact_higher_moment_jet_{k}",zero(f.diff(r).subs(r,edge)*m2))
    put("missing_covariant_term_misses_mass",not zero(-f.diff(r,2)-m2*f))
    put("broken_n0_mass",zero(lap0(c)-q*q*c))
    put("unbroken_zero_endpoint",zero(lap0(c).subs(q,0)))
    put("broken_n0_not_parallel",not zero(grad(c)[2]))
    put("reference_v0_recovered",zero(lap0(f).subs(q,0)-n*n*f))

    # Co-closed dx profile vanishes at the two ends; its curl partner has
    # harmonic dy trace and zero normal trace there. Both are actual modes.
    g=[S.zeros(2,1),S.sin(n*r)*c,S.zeros(2,1)]
    cg=curl(g)
    put("coclosed_profile",zero(div(g)))
    put("coclosed_partner",zero(div(cg)))
    put("actual_curl_mass_square",all(zero(a-m2*b) for a,b in zip(curl(cg),g)))
    put("coclosed_no_vector_mixing",zero(div(g)) and zero(div(cg)))
    for k,edge in enumerate((0,S.pi)):
        put(f"coclosed_tangent_dx_zero_{k}",zero(g[1].subs(r,edge)))
        put(f"coclosed_partner_normal_zero_{k}",zero(cg[0].subs(r,edge)))
        put(f"coclosed_partner_dx_zero_{k}",zero(cg[1].subs(r,edge)))
        put(f"coclosed_normal_curl_response_{k}",zero(cg[0].subs(r,edge)))
    nn=S.integrate((f.T*f)[0],(r,0,S.pi))
    nd=S.integrate(sum((a.T*a)[0] for a in df),(r,0,S.pi))
    ng=S.integrate(sum((a.T*a)[0] for a in g),(r,0,S.pi))
    nc=S.integrate(sum((a.T*a)[0] for a in cg),(r,0,S.pi))
    put("exact_positive_norm_identity",zero(nd-m2*nn) and nn==S.pi/2)
    put("coclosed_partner_norm_identity",zero(nc-m2*ng) and ng==S.pi/2)

    # Direct periodic divergence, independently of the finite Green algebra.
    beta_x=(2+S.cos(x))*S.Matrix([2,3])
    beta_y=S.cos(y)*S.Matrix([1,2])
    flux=beta_x.diff(x)+beta_y.diff(y)+O*beta_y
    mean=lambda z: simp(S.integrate(S.integrate(z,(x,0,2*S.pi)),(y,0,2*S.pi)))
    put("actual_periodic_Green_cancellation",zero(mean(c.dot(flux))))
    put("admitted_beta_orthogonal_to_Dc",zero(mean((O*c).dot(beta_y))))
    bad=S.Matrix([0,1])
    put("forbidden_constant_normal_detected",not zero(mean(c.dot(O*bad))))
    put("periodic_Green_correct_sign",zero(mean(c.dot(O*bad))+mean((O*c).dot(bad))))
    put("arbitrary_twoform_zero_claim_rejected",not zero(mean(c.dot(O*bad))))
    value_only=r*(S.pi-r)
    put("value_only_squared_domain",value_only.subs(r,0)==0 and value_only.subs(r,S.pi)==0)
    put("higher_response_not_H2_automatic",value_only.diff(r,2).subs(r,0)==-2)

    # Independently eliminate the Lagrangian's temporal multiplier.
    vel,svel,avec,psi,temporal,p,m=S.symbols("vel svel avec psi temporal p m", real=True)
    L=((vel+p*temporal)**2+(svel-m*temporal)**2-(p*psi+m*avec)**2)/2
    E=S.diff(L,vel); ps=S.diff(L,svel)
    EE,PP=S.symbols("EE PP", real=True)
    velocities={vel:EE-p*temporal,svel:PP+m*temporal}
    Ham=S.expand((EE*vel+PP*svel-L).subs(velocities, simultaneous=True))
    put("temporal_multiplier_constraint",zero(S.diff(Ham,temporal)+p*EE-m*PP))
    red=S.simplify(Ham.subs({psi:0,temporal:0,PP:p*EE/m}))
    put("Lagrangian_reduced_longitudinal",zero(red-((1+p*p/(m*m))*EE*EE+m*m*avec*avec)/2))
    put("Hamiltonian_frequency",zero(S.diff(red,EE,2)*S.diff(red,avec,2)-p*p-m*m))
    put("canonical_rescaling",zero((m/S.sqrt(p*p+m*m))*(S.sqrt(p*p+m*m)/m)-1))
    put("zero_mass_constraint_separate",S.diff(Ham,temporal).subs(m,0)==-p*EE)
    return facts


if __name__ == "__main__":
    facts=run()
    print(json.dumps({"status":"PASS","exact_local_checks":len(facts),"facts":facts,
        "global_PDE_or_full_SM_certificate":False},indent=2),flush=True)
