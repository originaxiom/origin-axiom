"""Exact inputs/controls for an authored analytic construction; stdout only."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "monomial_exceptional_locus_2026_09_27"))
import verify_exceptional as ex
from verify_global_seed import Rep, eye, hs, pullback, vs, zero
from verify_topology import cover, data
from flint import fmpq_mat
import sympy as sp


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def as_flint(a):
    return fmpq_mat([[str(x) for x in row] for row in a.tolist()])


def diagonal(x):
    return sp.diag(*list(x), -sum(x))


def diagonal_representation(seed):
    gram = sp.eye(4)+sp.ones(4)
    matrices = []
    for p in seed["permutations"]:
        pmat = sp.Matrix(5, 5, lambda i, j: int(i == p[j]))
        a = sp.Matrix(4, 4, lambda i, j: int(i == p[j])-int(i == p[4]))
        assert pmat.det() == 1 and a.T*gram*a == gram
        for j in range(4):
            column = sp.eye(4)[:, j]
            assert pmat*diagonal(column)*pmat.T == diagonal(a*column)
        matrices.append(as_flint(a))
    assert gram.det() == 5
    assert all(gram[:i, :i].det() > 0 for i in range(1, 5))
    return Rep(matrices), gram


def differential_matrices(rep, n):
    rels, mu, lam = cover(n)
    ng, d = len(rep.mats), rep.d
    d0 = vs(*(g-eye(d) for g in rep.mats))
    d1 = vs(*(hs(*(rep.fox(r, j) for j in range(1, ng+1))) for r in rels))
    restriction = vs(*(hs(*(rep.fox(w, j) for j in range(1, ng+1))) for w in (mu, lam)))
    assert d1*d0 == zero(d1.nrows(), d)
    return d0, d1, restriction


def word_cocycle(rep, word, cocycle):
    ng = len(rep.mats)
    return hs(*(rep.fox(word, j) for j in range(1, ng+1)))*cocycle


@lru_cache(None)
def one_seed(number):
    seed = ex.inputs()["seeds"][number]
    assert all(sum(v) == 0 for v in seed["exponents"])
    down, gram = diagonal_representation(seed)
    c = fmpq_mat([[x] for v in seed["exponents"] for x in v[:4]])
    records = {"seed": number, "gram": gram.tolist(), "covers": {}}
    up = pullback(down)
    cu = vs(*(word_cocycle(down, w, c) for w in data()["M6_generators_in_M2"]))
    monomials = ex.modules(seed)["E"]
    for j, w in enumerate(data()["M6_generators_in_M2"]):
        _, v, _ = ex.word(w, monomials)
        assert fmpq_mat([[cu[j*4+i, 0]] for i in range(4)]) == fmpq_mat([[x] for x in v[:4]])
    for n, rep, cocycle in ((2, down, c), (6, up, cu)):
        rels, mu, lam = cover(n)
        assert all(rep.word(r) == eye(4) for r in rels)
        d0, d1, restriction = differential_matrices(rep, n)
        assert d1*cocycle == zero(d1.nrows(), 1)
        assert restriction*cocycle == zero(8, 1)
        rank, augmented = d0.rank(), hs(d0, cocycle).rank()
        assert rank == inputs()["expected_global_d0_rank"] and augmented == rank+1
        ordinary, profile = ex.cohom(rep, n, 1)
        assert list(ordinary) == inputs()["expected_diagonal_cohomology"]
        assert ordinary[1]-ordinary[4] == inputs()["expected_nonzero_interior_dimension"]
        metric = as_flint(gram)
        assert all(g.transpose()*metric*g == metric for g in rep.mats)
        assert all(g.inv().transpose()*metric == metric*g for g in rep.mats)
        records["covers"][str(n)] = {
            "matrices": [str(g) for g in rep.mats], "cocycle": str(cocycle),
            "ordinary": ordinary, "restriction_profile": profile,
            "d0_rank": rank, "adjoined_cocycle_rank": augmented,
            "cocycle_residual_zero": True, "peripheral_periods_zero": True,
            "positive_metric_preserved": True,
        }
    records["global_class_nonzero"] = True
    return records


def gauge_controls():
    rep, _ = diagonal_representation(ex.inputs()["seeds"][0])
    d0, d1, _ = differential_matrices(rep, 2)
    exact = d0*fmpq_mat([[1], [2], [-1], [3]])
    assert d1*exact == zero(d1.nrows(), 1)
    assert hs(d0, exact).rank() == d0.rank()
    bad = fmpq_mat([[int(i == 0)] for i in range(12)])
    assert d1*bad != zero(d1.nrows(), 1)
    return {"exact_cocycle_is_gauge": True, "arbitrary_cochain_rejected": True}


def finite_hodge_control():
    d = sp.Matrix([[1, 0], [1, 1], [0, 1], [0, 0]])
    d1 = sp.Matrix([[1, -1, 1, 0]])
    g0 = sp.Matrix([[2, 1], [1, 3]])
    v = sp.Matrix([1, -1, 2, 1])
    g1 = sp.eye(4)+v*v.T
    adjoint = g0.inv()*d.T*g1
    lap = adjoint*d
    alpha = sp.Matrix([0, 0, 0, 1])+d*sp.Matrix([2, -1])
    f = -lap.inv()*adjoint*alpha
    beta = alpha+d*f
    assert d1*d == sp.zeros(1, 2) and d1*beta == sp.zeros(1, 1)
    assert adjoint*beta == sp.zeros(2, 1) and beta != sp.zeros(4, 1)
    assert d.row_join(beta-alpha).rank() == d.rank()
    assert (beta.T*g1*beta)[0] > 0
    assert adjoint*(alpha-d*f) != sp.zeros(2, 1)
    exact = d*sp.Matrix([3, 1])
    assert exact-d*lap.inv()*adjoint*exact == sp.zeros(4, 1)
    return {"beta": beta, "norm_squared": (beta.T*g1*beta)[0],
            "wrong_sign_rejected": True, "exact_class_projects_to_zero": True}


@lru_cache(None)
def cusp_controls():
    r, y, k, x = sp.symbols("r y k x", real=True, positive=True)
    v = sp.Function("v")(r)
    f = sp.exp(r)*v
    positive_laplacian = -sp.diff(f, r, 2)+2*sp.diff(f, r)
    assert sp.simplify(positive_laplacian-sp.exp(r)*(-sp.diff(v, r, 2)+v)) == 0
    hardy = sp.diff(f, r)**2*sp.exp(-2*r)-sp.diff(v, r)**2-v**2-sp.diff(v**2, r)
    assert sp.simplify(hardy) == 0
    mode = y*sp.besselk(1, k*y)
    assert sp.besselsimp(sp.diff(mode, y)+k*y*sp.besselk(0, k*y)) == 0
    assert sp.besselsimp(sp.diff(mode, y, 2)-sp.diff(mode, y)/y-k*k*mode) == 0
    # The missing radial-degree term is discriminated, not just asserted.
    assert sp.besselsimp(sp.diff(mode, y, 2)-k*k*mode) != 0
    b = x**2*(1-x)**2
    moments = [sp.integrate(sp.diff(b, x, j)**2, (x, 0, 1)) for j in range(3)]
    assert moments == [sp.Rational(1, 630), sp.Rational(2, 105), sp.Rational(4, 5)]
    assert all(sp.diff(b, x, j).subs(x, side) == 0 for j in (0, 1) for side in (0, 1))
    assert moments[1]/moments[0] == 12 and moments[2]/moments[0] == 504
    # Constant torus 1-form: tangential inverse metric cancels cusp volume.
    norm_density = sp.exp(2*r)*sp.exp(-2*r)
    derivative_density = sp.exp(2*r)*sp.exp(-2*r)
    radial = -sp.diff(derivative_density*sp.diff(v, r), r)/norm_density
    assert radial == -sp.diff(v, r, 2)
    assert sp.integrate(sp.exp(-2*r), (r, 0, sp.oo)) == sp.Rational(1, 2)
    return {"scalar_conjugated_operator": "-d_r^2+1", "one_form_radial_operator": "-d_r^2",
            "bump_moments": moments, "rayleigh_constant": 12, "laplacian_norm_constant": 504,
            "bessel_derivative_and_equation": True, "constant_scalar_L2_norm_squared": sp.Rational(1, 2)}


def nonlinear_and_trace_controls():
    symbols = sp.symbols("b0:12", real=True)
    forms = [diagonal(symbols[4*j:4*j+4]) for j in range(3)]
    assert all(a*b-b*a == sp.zeros(5) for a, b in combinations(forms, 2))
    s, tau = sp.symbols("s tau", real=True)
    connection, higgs = [sp.I*tau*b for b in forms], [s*b for b in forms]
    assert all(a.conjugate().T == -a for a in connection)
    assert all(p.conjugate().T == p for p in higgs)
    assert sum((a*p-p*a for a, p in zip(connection, higgs)), sp.zeros(5)) == sp.zeros(5)
    noncommuting = sp.zeros(5)
    noncommuting[0, 1] = noncommuting[1, 0] = 1
    assert forms[0]*noncommuting-noncommuting*forms[0] != sp.zeros(5)
    x = list(sp.symbols("h0:4", real=True))
    x += [-sum(x)]
    fund = sum(a*a for a in x)
    adj = sum((a-b)**2 for a in x for b in x)
    wedge = sum((x[i]+x[j])**2 for i, j in combinations(range(5), 2))
    e8trace = adj+20*fund+10*wedge
    assert sp.expand(e8trace-60*fund) == 0
    assert sp.expand(e8trace-30*fund) != 0
    ds, dtau = sp.symbols("ds dtau", real=True)
    z = ds+sp.I*dtau
    kinetic = sp.trace((z*forms[0]).conjugate().T*(z*forms[0]))
    assert sp.expand(kinetic-(ds**2+dtau**2)*sp.trace(forms[0]**2)) == 0
    return {"all_commutator_residuals_zero": True, "noncommuting_control_rejected": True,
            "raw_E8_adjoint_trace_factor": 60, "complex_kinetic_real_split": True}


def serializable(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(v) for v in row] for row in value.tolist()]
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, dict):
        return {k: serializable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serializable(v) for v in value]
    return value


def main():
    for number in range(2):
        print("CLASS", json.dumps(serializable(one_seed(number))), flush=True)
    for label, function in (("GAUGE", gauge_controls), ("HODGE_CONTROL", finite_hodge_control),
                            ("CUSP", cusp_controls), ("NONLINEAR", nonlinear_and_trace_controls)):
        print(label, json.dumps(serializable(function())), flush=True)
    print("SCOPE", json.dumps({"finite_algebraic_inputs_verified": True,
          "global_PDE_numerically_solved": False, "analytic_argument": "authored, see PROOF.md",
          "physical_chirality_derived": False, "isolated_4d_EFT_established": False}), flush=True)
    print("PASS: finite prerequisites and analytic identity controls; not machine-certified global analysis")


if __name__ == "__main__":
    main()
