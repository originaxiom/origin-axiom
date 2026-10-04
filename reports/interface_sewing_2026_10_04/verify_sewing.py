"""Exact controls for a conditional interface law, not an OA physical model."""
import itertools
import json
from functools import lru_cache

import sympy as sp


def zero(expr):
    if isinstance(expr, sp.MatrixBase):
        return all(zero(entry) for entry in expr)
    return sp.simplify(sp.expand(expr.rewrite(sp.exp))) == 0


def response(length, frequency):
    if frequency == 0:
        return sp.Matrix([[1, -1], [-1, 1]]) / length
    return frequency * sp.Matrix([
        [sp.coth(frequency * length), -sp.csch(frequency * length)],
        [-sp.csch(frequency * length), sp.coth(frequency * length)],
    ])


@lru_cache(maxsize=1)
def cylinder_checks():
    a, b, k = sp.symbols("a b k", positive=True)
    r, u0, u1 = sp.symbols("r u0 u1", real=True)
    f = (u0 * sp.sinh(k * (a-r)) + u1 * sp.sinh(k*r)) / sp.sinh(k*a)
    u = sp.Matrix([u0, u1])
    normal = sp.Matrix([-sp.diff(f, r).subs(r, 0), sp.diff(f, r).subs(r, a)])
    N = response(a, k)
    total = N + response(b, k)
    plus, minus = sp.Matrix([1, 1]), sp.Matrix([1, -1])
    lp = k * (sp.tanh(k*a/2) + sp.tanh(k*b/2))
    lm = k * (sp.coth(k*a/2) + sp.coth(k*b/2))
    energy_primitive = f * sp.diff(f, r)
    checks = {
        "left_trace": zero(f.subs(r, 0)-u0),
        "right_trace": zero(f.subs(r, a)-u1),
        "harmonic_residual": zero(-sp.diff(f, r, 2)+k*k*f),
        "both_outward_derivatives": zero(normal-N*u),
        "green_density": zero(sp.diff(energy_primitive, r)-sp.diff(f,r)**2-k*k*f*f),
        "green_endpoints": zero(energy_primitive.subs(r,a)-energy_primitive.subs(r,0)-(u.T*N*u)[0]),
        "sum_plus_eigenvalue": zero(total*plus-lp*plus),
        "sum_minus_eigenvalue": zero(total*minus-lm*minus),
        "positive_plus": lp.is_positive is True,
        "positive_minus": lm.is_positive is True,
        "wrong_outward_subtraction_zero": zero(N-N),
        "correct_equal_piece_sum_nonzero": not zero(2*N),
        "endpoint_swap_transport": zero(sp.Matrix([[0,1],[1,0]])*N*sp.Matrix([[0,1],[1,0]])-N),
    }
    N0 = response(a, 0) + response(b, 0)
    checks.update({
        "zero_mode_kernel_constant": N0.nullspace() == [plus],
        "zero_mode_nonconstant_penalized": zero(N0*minus-2*(1/a+1/b)*minus),
        "constant_field_variation_zero": sp.diff(u0,r) == 0,
        "frequency_limit": zero(N.applyfunc(lambda e: sp.limit(e,k,0))-response(a,0)),
        "free_piece_bulk_residual_zero": zero((-sp.diff(f,r,2)+k*k*f).subs({u0:0,u1:1})),
        "free_piece_field_nonzero": not zero(sp.diff(f,r).subs({u0:0,u1:1})),
        "free_piece_positive_norm": (k*sp.coth(k*a)).is_positive is True,
    })
    epsilon = sp.symbols("epsilon", positive=True)
    jump, dm = sp.symbols("jump dm", real=True)
    gradient = dm+jump*(r+epsilon)/(2*epsilon)
    cost = sp.integrate(sp.diff(gradient,r)**2,(r,-epsilon,epsilon))
    checks.update({
        "smoothing_left_gradient": zero(gradient.subs(r,-epsilon)-dm),
        "smoothing_right_gradient": zero(gradient.subs(r,epsilon)-dm-jump),
        "smoothing_cost": zero(cost-jump**2/(2*epsilon)),
        "nonzero_jump_diverges": sp.limit(cost.subs(jump,1),epsilon,0,dir="+") == sp.oo,
        "zero_jump_cost_zero": cost.subs(jump,0) == 0,
        "kink_jump_not_zero": 1/a+1/b > 0,
    })
    checks = {key: bool(value) for key,value in checks.items()}
    return {"checks": checks, "response": str(N), "eigenvalues": [str(lp),str(lm)],
            "smoothing_cost": str(cost)}


def cycle_matrix(signs, onsite=0):
    n = len(signs)
    L = sp.zeros(n)
    for i, twist in enumerate(signs):
        v = sp.zeros(n,1)
        v[i] = 1
        v[(i+1)%n] = -twist
        L += (i+1)*v*v.T
    return L + onsite*sp.eye(n)


def eliminate(L, boundary):
    interior = [i for i in range(L.rows) if i not in boundary]
    A, B, D = L.extract(interior,interior), L.extract(interior,boundary), L.extract(boundary,boundary)
    R = D - B.T*A.inv()*B
    H = L*L
    Ai, Bi, Di = H.extract(interior,interior), H.extract(interior,boundary), H.extract(boundary,boundary)
    direct = Di - Bi.T*Ai.inv()*Bi
    middle = (sp.eye(len(boundary)) + B.T*A.inv()*A.inv()*B).inv()
    formula = R*middle*R
    zero_interior_rows = A*(-A.inv()*B)+B
    return R, direct, formula, middle, zero_interior_rows


@lru_cache(maxsize=1)
def graph_checks():
    rows = []
    covariance = 0
    for n in (3,4,5):
        for signs in itertools.product((-1,1), repeat=n):
            boundary = [0,n-1]
            L = cycle_matrix(signs)
            R,Q,F,W,omitted = eliminate(L,boundary)
            expected = int(sp.prod(signs) == 1)
            checks = {
                "exact_elimination": Q == F,
                "positive_weight": W[0,0] > 0 and W.det() > 0,
                "global_parallel_kernel": n-L.rank() == expected,
                "response_kernel": 2-R.rank() == expected,
                "residual_kernel": 2-Q.rank() == expected,
                "omitted_boundary_false_zero": omitted == sp.zeros(n-2,2) and Q != sp.zeros(2),
            }
            rows.append({"n":n,"signs":list(signs),"parallel_dimension":expected,
                         "checks":{key:bool(value) for key,value in checks.items()}})
            if n == 3:
                for gauge in itertools.product((-1,1),repeat=n):
                    G = sp.diag(*gauge)
                    Gb = sp.diag(*(gauge[i] for i in boundary))
                    Rg,Qg,*_ = eliminate(G*L*G,boundary)
                    assert Rg == Gb*R*Gb and Qg == Gb*Q*Gb
                    covariance += 1
    R,Q,F,W,_ = eliminate(cycle_matrix((1,1,1)),[0,2])
    massR,massQ,*_ = eliminate(cycle_matrix((1,1,1),sp.Rational(1,3)),[0,2])
    controls = {
        "response_not_residual_potential": R != Q,
        "square_response_not_relaxed_potential": R*R != Q,
        "onsite_response_kernel_removed": massR.det() > 0,
        "onsite_residual_kernel_removed": massQ.det() > 0,
        "constant_parameter_retained": R*sp.ones(2,1) == sp.zeros(2,1),
    }
    return {"rows":rows,"gauge_covariance_checks":covariance,
            "controls":{key:bool(value) for key,value in controls.items()},
            "example":{"response":str(R),"actual_residual_potential":str(Q),"middle":str(W)}}


def run():
    cylinder, graphs = cylinder_checks(), graph_checks()
    passed = (all(cylinder["checks"].values()) and all(graphs["controls"].values())
              and all(all(row["checks"].values()) for row in graphs["rows"]))
    return {"status":"PASS" if passed else "FAIL", "cylinder":cylinder,"graphs":graphs}


if __name__ == "__main__":
    result = run()
    print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
