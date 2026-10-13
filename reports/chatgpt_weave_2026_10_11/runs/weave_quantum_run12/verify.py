#!/usr/bin/env python3
"""Exact finite controls for Run 12; SymPy only, no network or repository code.

These are controls on an accompanying conditional analytic argument, not
certificates of infinite-dimensional PDE or quantum consistency claims.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import sympy as s

x, y, z, t = s.symbols('x y z t', real=True)
coords = (x, y, z)
I = s.I
zero = s.zeros(2)
p1 = s.Matrix([[0, 1], [1, 0]])
p2 = s.Matrix([[0, -I], [I, 0]])
p3 = s.diag(1, -1)
checks: dict[str, bool] = {}
details: dict[str, object] = {}

def simp(m):
    return m.applyfunc(s.simplify) if isinstance(m, s.MatrixBase) else s.simplify(m)

def iszero(m) -> bool:
    m = simp(m)
    return m == s.zeros(*m.shape) if isinstance(m, s.MatrixBase) else m == 0

def check(name: str, result: bool) -> None:
    checks[name] = bool(result)
    print(('PASS ' if result else 'FAIL ') + name, flush=True)

def comm(a, b):
    return a*b-b*a

def sm(items):
    return sum(items, zero)

def da(A, i, v):
    return v.diff(coords[i])+I*comm(A[i], v)

def minus(A, B, i, v):
    return da(A, i, v)-comm(B[i], v)

def plus(A, B, i, v):
    return da(A, i, v)+comm(B[i], v)

def div(A, u):
    return sm(da(A, i, u[i]) for i in range(3))

def moment(A, B):
    return div(A, B)

def curvature(phi):
    return [phi[j].diff(coords[i])-phi[i].diff(coords[j])+I*comm(phi[i],phi[j])
            for i,j in ((0,1),(0,2),(1,2))]

def extD(A, B, u):
    return [minus(A,B,i,u[j])-minus(A,B,j,u[i])
            for i,j in ((0,1),(0,2),(1,2))]

def norm2(v):
    return s.simplify(s.trace(v.H*v))

def origin(v):
    return simp(v.subs({x:0,y:0,z:0}))

# Generic noncommuting smooth jets. These are NOT asserted to be a vacuum.
A = [x*p1+p2, y*p2+p3, z*p3+p1]
B = [p1+y*p2, p2+z*p3, p3+x*p1]
a = [p1+x*p2, p2+y*p3, p3+z*p1]
b = [2*p2+y*p1, p3+x*p2, p1+z*p3]
u = [a[i]+I*b[i] for i in range(3)]
G = div(A,a)+I*sm(comm(B[i],b[i]) for i in range(3))
M = div(A,b)-I*sm(comm(B[i],a[i]) for i in range(3))
Dstar = -sm(plus(A,B,i,u[i]) for i in range(3))
check('Dstar_equals_minus_G_minus_iM', iszero(Dstar+G+I*M))
check('G_and_M_actual_Hermitian', iszero(G-G.H) and iszero(M-M.H))
check('moment_map_linearization', iszero(moment([A[i]+t*a[i] for i in range(3)],
                                                  [B[i]+t*b[i] for i in range(3)]).diff(t).subs(t,0)-M))
phi = [A[i]+I*B[i] for i in range(3)]
linear_H = [h.diff(t).subs(t,0) for h in curvature([phi[i]+t*u[i] for i in range(3)])]
check('curvature_linearization_full_brackets', all(iszero(v-w) for v,w in zip(linear_H,extD(A,B,u))))
check('Hermitian_norm_decomposition', iszero(norm2(origin(Dstar))-norm2(origin(G))-norm2(origin(M))))
check('wrong_G_commutator_detected', not iszero(Dstar+div(A,a)-I*sm(comm(B[i],b[i]) for i in range(3))+I*M))
check('wrong_M_commutator_detected', not iszero(Dstar+G+I*(div(A,b)+I*sm(comm(B[i],a[i]) for i in range(3)))))
check('controls_retain_noncommuting_background', any(not iszero(comm(A[i],B[j])) for i in range(3) for j in range(3)))

# General zero-form identity, including the unpaid term when mu != 0.
lam = (1+x)*p1+(y+z)*p2+(1+x*y)*p3
Delta0 = -sm(plus(A,B,i,minus(A,B,i,lam)) for i in range(3))
mu = moment(A,B)
realpart = -sm(da(A,i,da(A,i,lam)) for i in range(3))+sm(comm(B[i],comm(B[i],lam)) for i in range(3))
check('zero_form_Laplacian_with_moment_term', iszero(Delta0-realpart-comm(mu,lam)))
check('nonharmonic_reality_countercontrol', not iszero(Delta0-Delta0.H))

# An exactly flat harmonic Cartan background with genuinely noncommuting
# gauge perturbations; this is only a local identity control.
Ac = [p3,2*p3,-p3]
Bc = [2*p3,-p3,3*p3]
pc = [Ac[i]+I*Bc[i] for i in range(3)]
check('gauge_control_background_flat_harmonic', all(iszero(v) for v in curvature(pc)) and iszero(moment(Ac,Bc)))
g = [minus(Ac,Bc,i,lam) for i in range(3)]
ag = [(v+v.H)/2 for v in g]
bg = [(v-v.H)/(2*I) for v in g]
Mg = div(Ac,bg)-I*sm(comm(Bc[i],ag[i]) for i in range(3))
check('admitted_bulk_gauge_direction_Hessian_null', all(iszero(v) for v in extD(Ac,Bc,g)) and iszero(Mg))
D0c = -sm(plus(Ac,Bc,i,minus(Ac,Bc,i,lam)) for i in range(3))
check('harmonic_zero_form_operator_preserves_reality', iszero(D0c-D0c.H))
Gg = div(Ac,ag)+I*sm(comm(Bc[i],bg[i]) for i in range(3))
check('compact_gauge_G_variation_minus_Delta0', iszero(Gg+D0c))

# Decaying principal-symbol solution exp(i xi.x-s r) v. s>0.
x1,x2,decay = s.symbols('xi1 xi2 s', real=True, positive=True)
# Positivity of xi components is not used in any polynomial identity.
T = s.Matrix([[x1,x2,0],[-decay*x2,decay*x1,0],[I*x1,I*x2,-decay]])
determinant = s.factor(T.det())
check('all_covector_scalar_boundary_determinant', iszero(determinant+decay**2*(x1*x1+x2*x2)))
details['boundary_determinant'] = str(determinant)
check('missing_divergence_condition_has_decaying_kernel', iszero(T[:2,:]*s.Matrix([0,0,1])))
V = s.Matrix([[-x2,0,0],[x1,0,0],[0,1,0],[0,0,x1],[0,0,x2],[0,0,0]])
Green = s.zeros(6)
Green[:3,3:] = s.eye(3)
Green[3:,:3] = -s.eye(3)
check('second_order_Green_form_zero', iszero(V.T*Green*V))
check('second_order_boundary_half_dimension', iszero((V.T*V).det()-(x1*x1+x2*x2)**2))
wrong = V.row_join(s.Matrix([0,0,0,0,0,1]))
check('free_normal_derivative_Green_failure', not iszero(wrong.T*Green*wrong))

# Exact integrated boundary projection: mean zero does not mean pointwise 0.
q = s.symbols('q', real=True)
flux = s.sin(q)
check('integrated_projection_not_pointwise_condition', s.integrate(flux,(q,0,2*s.pi))==0
      and s.integrate(flux**2,(q,0,2*s.pi))==s.pi)
# k is parallel; codifferential two-form normal projection is a closed-
# boundary tangential divergence. This fixture retains nonzero local terms.
h = s.sin(x)*s.cos(y)
kfun = s.cos(2*x)*s.sin(y)
div2 = h.diff(x)+kfun.diff(y)
check('normal_codifferential_integrates_to_zero', not iszero(div2) and
      s.integrate(div2,(x,0,2*s.pi),(y,0,2*s.pi))==0)

# Graph-domain counterexample in the same differential boundary channel.
r,eps = s.symbols('r epsilon', positive=True, real=True)
f = r*(1-r)
check('operator_domain_not_extra_response_trace', f.subs(r,0)==0 and f.subs(r,1)==0
      and f.diff(r,2).subs(r,0)!=0 and f.diff(r,2).subs(r,1)!=0)
eig = s.sin(s.pi*r)
check('smooth_eigenfunction_has_secondary_response', iszero(-eig.diff(r,2)-s.pi**2*eig)
      and eig.diff(r,2).subs(r,0)==0 and eig.diff(r,2).subs(r,1)==0)
p = r**2*(1-r)**4
C0 = s.integrate(p*p,(r,0,1))
C1 = s.integrate(p.diff(r)**2,(r,0,1))
C2 = s.integrate(p.diff(r,2)**2,(r,0,1))
check('boundary_layer_cancels_response', p.subs(r,0)==0 and p.diff(r,2).subs(r,0)==2
      and all(p.diff(r,j).subs(r,1)==0 for j in range(4)))
check('boundary_layer_graph_error_vanishes', C0>0 and C2>0 and
      s.limit(2*(eps**5*C0+eps*C2),eps,0,dir='+')==0)
details['boundary_layer_integrals'] = {'C0':str(C0),'C1':str(C1),'C2':str(C2)}
details['squared_graph_error_two_layers'] = str(2*(eps**5*C0+eps*C2))
# Smooth polynomial approximants have finite C^3 pieces; a C-infinity
# cutoff supplies the proof version with the same scaling, not identical Cj.

# A retained flux control for the compact-gauge minimization boundary term.
f2 = 1+r+r*r
l2 = 1+2*r
lhs = s.integrate(f2*l2.diff(r),(r,0,1))
bulk = -s.integrate(f2.diff(r)*l2,(r,0,1))
surface = (f2*l2).subs(r,1)-(f2*l2).subs(r,0)
check('gauge_minimization_keeps_surface', lhs==bulk+surface and surface!=0 and lhs!=bulk)

out = {'status':'PASS' if all(checks.values()) else 'FAIL',
       'exact_checks_passed':sum(checks.values()),'exact_checks_total':len(checks),
       'checks':checks,'details':details,
       'global_analytic_argument_certified_by_tests':False,
       'silver_cohomology_recomputed':False,'repository_producers_rerun':False,
       'full_multiplet_domain_proved':False,'boundary_selected':False,
       'python_version':sys.version,'sympy_version':s.__version__}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','exact_checks_passed','exact_checks_total')},indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
