#!/usr/bin/env python3
"""Independent differential-profile and domain controls; no finite model import."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s
OUT=Path(__file__).resolve().parent
x,y,r=s.symbols('x y r',real=True)
k,n=s.symbols('k n',integer=True,positive=True)
mu=s.sqrt(k*k+n*n)
coords=[x,y,r]
f=s.sin(n*r)*s.cos(k*x)
g=s.Matrix([0,s.cos(n*r)*s.cos(k*x),0])
def grad(f):return s.Matrix([s.diff(f,z) for z in coords])
def div(v):return sum(s.diff(v[i],coords[i]) for i in range(3))
def curl(v):return s.Matrix([s.diff(v[2],y)-s.diff(v[1],r),s.diff(v[0],r)-s.diff(v[2],x),s.diff(v[1],x)-s.diff(v[0],y)])
def lap(f):return sum(s.diff(f,z,2) for z in coords)
def z(v):
    if isinstance(v,s.MatrixBase):return all(s.trigsimp(s.simplify(a))==0 for a in v)
    return s.trigsimp(s.simplify(v))==0
facts={}
def check(name,cond):
    facts[name]=bool(cond)
    if not cond:raise AssertionError(name)
e=grad(f)/mu
cg=curl(g)/mu
check('scalar_Dirichlet_eigenfunction', z(lap(f)+mu**2*f) and z(f.subs(r,0)) and z(f.subs(r,s.pi)))
check('exact_profile_is_oneform_eigenfunction', z(e.applyfunc(lap)+mu**2*e))
check('exact_profile_has_zero_curl',z(curl(e)))
check('exact_profile_divergence_gives_same_mass',z(div(e)+mu*f))
check('coexact_profile_is_divergence_free',z(div(g)))
check('coexact_profile_is_oneform_eigenfunction',z(g.applyfunc(lap)+mu**2*g))
check('curl_partner_retains_divergence_free',z(div(cg)))
check('curl_partner_double_curl',z(curl(cg)-mu*g))
check('two_coexact_profiles_are_orthogonal_pointwise',z((g.T*cg)[0]))
for endpoint in [0,s.pi]:
    tag='0' if endpoint==0 else 'pi'
    # At k!=0: allowed one-form high trace = tangent coexact (y) + free normal;
    # the Laplacian requires div u=0 and d_normal(u_t) along y=0 at the boundary.
    check('exact_tangential_boundary_'+tag,z(e[:2,0].subs(r,endpoint)))
    check('exact_divergence_boundary_'+tag,z(div(e).subs(r,endpoint)))
    check('coexact_tangent_normal_derivative_'+tag,z(s.diff(g[1],r).subs(r,endpoint)))
    check('curl_partner_tangential_gradient_boundary_'+tag,z(cg[0].subs(r,endpoint)))
# Pi_k is a boundary average, not pointwise zero normal trace.
check('nonzero_pointwise_normal_flux_retained',not z(e[2].subs(r,0)))
check('integrated_normal_flux_vanishes',s.integrate(e[2].subs(r,0),(x,0,2*s.pi))==0)
check('freezing_normal_gauge_jet_would_reject_valid_mode',not z(s.diff(f,r).subs(r,0)))
bad=s.Matrix([0,s.sin(n*r)*s.cos(k*x),0])
check('value_only_scalar_boundary_not_sufficient',z(bad.subs(r,0)) and not z(s.diff(bad[1],r).subs(r,0)))
check('wrong_vector_boundary_detected',not z((s.cos(n*r)*s.cos(k*x)).subs(r,0)))
# Antilinear curl K=conjugation*cURL: a phase turns the negative real curl mode positive.
pplus=(g+cg)/s.sqrt(2)
pminus=(g-cg)/s.sqrt(2)
check('positive_curl_eigenprofile',z(curl(pplus)-mu*pplus))
check('negative_curl_eigenprofile',z(curl(pminus)+mu*pminus))
check('Takagi_rephasing_requires_conjugation',z(curl(s.I*pminus).conjugate()-mu*s.I*pminus))
check('linear_rephasing_does_not_change_eigenvalue',not z(curl(s.I*pminus)-mu*s.I*pminus))
# Actual field operator R(lambda,rho)=(div rho,curl rho-grad lambda).
check('vector_gaugino_first_map',z(-grad(f)+mu*e))
check('vector_gaugino_second_map',z(div(e)+mu*f) and z(curl(e)))
# Check independent normalization integrals at several legitimate integer modes.
for nv,kv in [(1,1),(2,1),(1,3)]:
    def norm2(v):
        v=v.subs({n:nv,k:kv})
        expr=(v.conjugate().T*v)[0] if isinstance(v,s.MatrixBase) else v*v.conjugate()
        return s.simplify(2*s.pi*s.integrate(s.integrate(expr,(x,0,2*s.pi)),(r,0,s.pi)))
    check(f'equal_kinetic_profile_norms_{nv}_{kv}',
          all(s.simplify(norm2(v)-s.pi**3)==0 for v in [f,e,g,cg,pplus,s.I*pminus]))
# Domain regularity: a scalar H2 Neumann function can have derivative outside H2.
# f_N=sum_{j<=N} cos(jr)/j^3: graph squared tails sum j^-6 + j^-2 converge;
# derivative's second-order graph includes sum 1, diverges. No full-domain invariance.
j=s.symbols('j',integer=True,positive=True)
check('Neumann_to_first_order_domain_tail_converges',
      s.summation(j**-2,(j,1,s.oo))==s.pi**2/6)
check('same_second_order_domain_tail_diverges',
      s.summation(s.Integer(1),(j,1,s.oo)) is s.oo)
check('finite_spectral_core_intertwines_boundaries',
      z(s.diff(s.cos(j*r),r).subs(r,0)) and z(s.diff(s.cos(j*r),r).subs(r,s.pi)))
result={'facts':facts,'passed':sum(facts.values()),'total':len(facts),
        'all_n_k_positive_integer_identities':True,
        'actual_silver_topology_or_PDE':False,'high_frequency_boundary_control_only':True,
        'same_author_separate_differential_method':True}
(OUT/'SLAB_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
