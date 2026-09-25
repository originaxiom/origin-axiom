"""R49 finite controls for the canonical adjoint end operator.

These exact model calculations do not independently certify the global
cusp, perturbation, elliptic estimates, or physical interpretation.
"""
from functools import lru_cache
from itertools import combinations
import json

import sympy as s

LAM, NU, Z = s.symbols("lambda nu z", real=True)
OM, Y = s.symbols("omega y", real=True, nonzero=True)
K = s.symbols("k", real=True, nonzero=True)
A_SCALE = s.Rational(3, 4)
H_INF = s.diag(s.Rational(3, 8), s.Rational(1, 4),
               s.Rational(3, 8), s.Rational(3, 8))
H0 = s.diag(1, 0, 0, -1)
D = s.diag(1, -3, 1, 1)
J = s.diag(5, -3, 1, -3)/8
N = s.zeros(4)
N[0, 2] = N[2, 3] = 1
P = N*N


def clean(value):
    if isinstance(value, s.MatrixBase):
        return value.applyfunc(s.factor)
    return s.factor(value)


def zero(value):
    if isinstance(value, s.MatrixBase):
        return all(s.cancel(x) == 0 for x in value)
    return s.cancel(value) == 0


def comm(a, b):
    return a*b-b*a


def unit(i, j):
    m = s.zeros(4)
    m[i, j] = 1
    return m


@lru_cache(None)
def basis():
    return tuple(unit(i, j) for i in range(4) for j in range(4)
                 if i != j) + tuple(unit(i, i)-unit(3, 3) for i in range(3))


def coordinates(m):
    if not zero(s.trace(m)):
        raise ValueError("Not traceless")
    return s.Matrix([m[i, j] for i in range(4) for j in range(4)
                     if i != j] + [m[i, i] for i in range(3)])


def ad(m):
    return s.Matrix.hstack(*(coordinates(comm(m, b)) for b in basis()))


def gram(h=H_INF):
    inv = h.inv()
    return s.Matrix([[s.trace(inv*x.conjugate().T*h*y)
                       for y in basis()] for x in basis()])


def adj(m, g):
    return clean(g.inv()*m.conjugate().T*g)


def geometry():
    x, z, y = s.symbols("x z y", positive=True)
    coords = (x, z, y)
    log_u = s.log(z)/4+3*s.log(x-y*y/2)/8
    grad = s.Matrix([s.diff(log_u, t) for t in coords])
    h = -s.hessian(log_u, coords)-grad*grad.T
    hp = clean(h.subs({x:1, z:1, y:0}))
    lp = grad.subs({x:1, z:1, y:0})
    w = s.Matrix([1, 1, 0, 1])
    frame = s.Matrix.hstack(w, *(s.eye(4)[:,i]-lp[i]*w for i in range(3)))
    ambient = clean(frame.inv().T*s.diag(s.ones(1), hp)*frame.inv())
    shear = s.Matrix([[2, 0, 0], [1, 0, -2], [0, 1, 0]])
    return hp, ambient, clean(shear.T*hp*shear)


@lru_cache(None)
def operators(wrong_metric=False, unsheared=False):
    h = H_INF.copy()
    if wrong_metric:
        h[2,2] *= 2
    g = gram(h)
    aa = ad(2*J if unsheared else H0)
    bb, ll = ad(N), ad(D)/2
    bs = adj(bb, g)
    tt = clean(aa*aa+aa+2*bs*bb+ll*ll)
    return g, aa, bb, ll, bs, tt


def forms(p):
    return tuple(combinations(range(3), p))


def wedge(i, form):
    if i in form:
        return None, 0
    return tuple(sorted((i,)+form)), (-1)**sum(j<i for j in form)


def differential(p, omit_structure=False, unsheared=False):
    _, aa, bb, ll, _, _ = operators(False, unsheared)
    mats = (LAM*s.eye(15)+aa, bb, s.I*NU*s.eye(15)+ll)
    source, target = forms(p), forms(p+1)
    result = s.zeros(len(target)*15, len(source)*15)
    for col, form in enumerate(source):
        for i, m in enumerate(mats):
            dest, sign = wedge(i, form)
            if sign:
                row = target.index(dest)
                result[row*15:(row+1)*15, col*15:(col+1)*15] += sign*m
        if not omit_structure and 1 in form and 0 not in form:
            row = target.index((0,)+form)
            result[row*15:(row+1)*15, col*15:(col+1)*15] -= s.eye(15)
    return result


def form_gram(p, wrong_metric=False):
    g = operators(wrong_metric)[0]
    blocks = [(2 if 1 in form else 1)*g/A_SCALE**p for form in forms(p)]
    return s.diag(*blocks)


def formal_adjoint(d, p, volume_weight=1, wrong_metric=False):
    # partial_r^* = -partial_r + volume_weight.
    formal = d.subs(LAM, volume_weight-LAM).conjugate().T
    return clean(form_gram(p, wrong_metric).inv()*formal*form_gram(p+1, wrong_metric))


def laplacian(p, volume_weight=1, wrong_metric=False,
              omit_structure=False, unsheared=False):
    result = s.zeros(15*len(forms(p)))
    if p:
        prev = differential(p-1, omit_structure, unsheared)
        result += prev*formal_adjoint(prev, p-1, volume_weight, wrong_metric)
    if p<3:
        nxt = differential(p, omit_structure, unsheared)
        result += formal_adjoint(nxt, p, volume_weight, wrong_metric)*nxt
    return clean(result)


def expected(p):
    tt = operators()[5]
    block = ((-LAM*LAM+LAM+NU*NU)*s.eye(15)+tt)/A_SCALE
    return s.kronecker_product(s.eye(len(forms(p))), block)


def independent_degree_one():
    """Direct components, not the exterior construction above."""
    _, aa, bb, ll, bs, _ = operators()
    ident = s.eye(15)
    xx = LAM*ident+aa
    xs = (-LAM+1)*ident+aa
    zz, zs = s.I*NU*ident+ll, -s.I*NU*ident+ll
    blocks = [
        [xx*xs+2*bs*bb+zs*zz,
         2*(xx*bs-bs*(xx-ident)), xx*zs-zs*xx],
        [bb*xs-(xs-ident)*bb,
         2*bb*bs+(xs-ident)*(xx-ident)+zs*zz, bb*zs-zs*bb],
        [zz*xs-xs*zz, 2*(zz*bs-bs*zz),
         xx*xs+2*bs*bb+zz*zs],
    ]
    return clean(s.BlockMatrix(blocks).as_explicit()/A_SCALE)


def zero_weight_restriction():
    _, _, _, ll, _, tt = operators()
    cols = ll.nullspace()
    inclusion = s.Matrix.hstack(*cols)
    left = (inclusion.T*inclusion).inv()*inclusion.T
    restriction = clean(left*tt*inclusion)
    return inclusion, restriction, clean(tt*inclusion-inclusion*restriction)


def meridian_inverse():
    bb = operators()[2]
    ident = s.eye(15)
    inv = sum(((-Y)**j/(s.I*OM)**(j+1)*bb**j for j in range(5)), s.zeros(15))
    return s.I*OM*ident+Y*bb, clean(inv)


def power_integrable(exponent, power):
    """For exp(exponent*r) and measure exp(-r) dr on a half-line."""
    return bool(power*exponent-1 < 0)


def checks():
    hp, ambient, pulled = geometry()
    g, aa, bb, ll, bs, tt = operators()
    inc, restricted, residue = zero_weight_restriction()
    matrix, inv = meridian_inverse()
    d0, d1, d2 = (differential(p) for p in range(3))
    scalar = -LAM**2+LAM
    threshold = clean(scalar.subs(LAM, s.Rational(1,2)+s.I*NU))
    eig_poly = clean(tt.charpoly(Z).as_expr())
    zero_poly = clean(restricted.charpoly(Z).as_expr())
    positive = all(g[:i,:i].det()>0 for i in range(1,16))
    beta, rr = s.symbols("beta rho", real=True)
    # rho=exp(-2r); keep it algebraic, not an asymptotic numerical sample.
    exact_r = 2*J-D/4-beta*rr*P/(4*K)
    exact_v = D/2+beta*rr*P/(2*K)
    result = {
        "ambient_metric_from_radial_graph": zero(ambient-H_INF),
        "sheared_base_metric": zero(pulled-s.diag(A_SCALE,A_SCALE/2,A_SCALE)),
        "exact_connection_remainder": zero(exact_r-H0+beta*rr*P/(4*K))
            and zero(exact_v-D/2-beta*rr*P/(2*K)),
        "gram_positive": positive,
        "radial_and_longitudinal_self_adjoint": zero(adj(aa,g)-aa) and zero(adj(ll,g)-ll),
        "nilpotent_adjoint_uses_actual_metric": zero(bs-ad(N.T)),
        "flat_model_commutators": zero(comm(aa,bb)-bb) and zero(comm(aa,ll))
            and zero(comm(bb,ll)),
        "whole_exterior_d_squared": zero(d1*d0) and zero(d2*d1),
        "indicial_all_degrees": all(zero(laplacian(p)-expected(p)) for p in range(4)),
        "independent_degree_one_expansion": zero(independent_degree_one()-expected(1)),
        "potential_self_adjoint": zero(adj(tt,g)-tt),
        "potential_full_spectrum": zero(eig_poly-Z*(Z-2)**3*(Z-6)**11),
        "potential_semisimple": zero(tt*(tt-2*s.eye(15))*(tt-6*s.eye(15))),
        "zero_weight_restriction": inc.cols==9 and zero(residue)
            and zero(zero_poly-Z*(Z-2)**3*(Z-6)**5),
        "radial_pairs": all(zero(scalar.subs(LAM,l)+potential)
            for potential, roots in ((0,(0,1)),(2,(-1,2)),(6,(-2,3)))
            for l in roots),
        "positive_radial_threshold": zero(threshold-NU**2-s.Rational(1,4))
            and s.Rational(1,4)/A_SCALE==s.Rational(1,3),
        "wrong_volume_rejected": not zero(laplacian(1,volume_weight=0)-expected(1)),
        "missing_coframe_term_rejected": not zero(differential(1,True)*differential(0,True)),
        "unsheared_radial_rejected": not zero(laplacian(1,unsheared=True)-expected(1)),
        "wrong_positive_metric_rejected": not zero(laplacian(1,wrong_metric=True)-expected(1)),
        "wrong_fourier_sign_rejected": not zero(expected(0).subs(NU,1)
            -((-LAM*LAM+LAM-1)*s.eye(15)+tt)/A_SCALE),
        "nilpotence_exact_degree_five": zero(bb**5) and not zero(bb**4),
        "nonzero_meridian_two_sided_inverse": zero(matrix*inv-s.eye(15))
            and zero(inv*matrix-s.eye(15)),
        "zero_meridian_has_kernel": bb.det()==0 and bb.rank()<15,
        "l2_is_not_l4_control": power_integrable(s.Rational(3,8),2)
            and not power_integrable(s.Rational(3,8),4),
        "critical_power_not_integrable": not power_integrable(s.Rational(1,4),4),
        "covering_factor_l4_control": power_integrable(s.Rational(1,2)-s.Rational(3,8),4),
    }
    return result, {
        "base_metric":str(pulled), "coefficient_metric_up_to_scalar":str(ambient),
        "coefficient_potential_polynomial":str(eig_poly),
        "zero_longitude_potential_polynomial":str(zero_poly),
        "radial_threshold":str(threshold/A_SCALE),
        "scope":"Exact limiting end inputs only; authored analytic transfer and physical interpretation are separate."
    }


if __name__ == "__main__":
    outcomes, witnesses = checks()
    print(json.dumps({"checks":outcomes, "all_checks_pass":all(outcomes.values()),
                      "witnesses":witnesses}, indent=2))
    raise SystemExit(0 if all(outcomes.values()) else 1)
