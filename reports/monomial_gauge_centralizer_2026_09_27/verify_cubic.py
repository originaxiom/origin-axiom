"""Symmetric-coefficient cubic overlap controls; no file writes."""
from functools import lru_cache
from itertools import combinations, permutations, product
import json
import sympy as sp
from flint import fmpq_mat
import verify_centralizer as c


def as_sympy(a):
    return sp.Matrix([[sp.Rational(str(a[i, j])) for j in range(a.ncols())] for i in range(a.nrows())])


def vec(a):
    return sp.Matrix(list(a))


def restrict(end_mats, projector):
    basis = sp.Matrix.hstack(*projector.columnspace())
    rows = list(basis.T.rref()[1])
    inverse = basis.extract(rows, range(basis.cols)).inv()
    result = []
    for a in end_mats:
        target = a*basis
        action = inverse*target.extract(rows, range(basis.cols))
        assert basis*action == target
        result.append(c.hb.as_flint(action))
    return c.Rep(result)


@lru_cache(None)
def symmetric_mode_control(number):
    down, gram = c.hb.diagonal_representation(c.ex.inputs()["seeds"][number])
    u = c.pullback(down)
    columns, traces = [], []
    for i in range(4):
        for j in range(4):
            a = sp.zeros(4)
            a[i, j] = 1
            columns.append(vec(gram.inv()*a.T*gram))
            traces.append(vec(sp.trace(a)*sp.eye(4)/4))
    transpose = sp.Matrix.hstack(*columns)
    scalar = sp.Matrix.hstack(*traces)
    symmetric = (sp.eye(16)+transpose)/2-scalar
    skew = (sp.eye(16)-transpose)/2
    assert transpose*transpose == sp.eye(16)
    assert symmetric*symmetric == symmetric and skew*skew == skew
    assert symmetric*skew == sp.zeros(16)
    assert symmetric+skew+scalar == sp.eye(16)
    assert (symmetric.rank(), skew.rank(), scalar.rank()) == (9, 6, 1)
    end = [as_sympy(c.kron(g, g.inv().transpose())) for g in u.mats]
    assert all(a*transpose == transpose*a for a in end)
    records = {"symmetric_tracefree": c.cohom_record(restrict(end, symmetric)),
               "skew": c.cohom_record(restrict(end, skew))}
    assert records["skew"]["n"] == records["skew"]["n_dual"] == 0
    assert records["symmetric_tracefree"]["n"] == records["symmetric_tracefree"]["n_dual"] == 3
    group = c.permutation_group([g[0] for g in c.coefficient_modules(number)["E"]])
    rows = []
    for g in group:
        ch = sum(i == g[i] for i in range(5))-1
        gg = c.compose(g, g)
        ch2 = sum(i == gg[i] for i in range(5))-1
        ch5 = (ch*ch+ch2)//2-1-ch
        rows.append((ch, ch5))
    assert sum(v for _, v in rows) == 0
    assert sum(a*b for a, b in rows) == 0
    assert sum(b*b for _, b in rows) == 60
    assert max(b for _, b in rows) == 5
    assert c.enhanced_matter(number)["coefficients"]["U"]["n"] == 1
    return {"seed": number, "projector_ranks": [9, 6, 1], "cohomology": records,
            "neutral_finite_coefficient_split": {"U": 1, "irreducible_five": 2},
            "all_harmonic_neutral_profiles_symmetric": True}


def symmetric_matrix(prefix):
    diag = sp.symbols(prefix+"d0:3")
    a = sp.diag(*diag, -sum(diag))
    values = sp.symbols(prefix+"o0:6")
    for value, (i, j) in zip(values, combinations(range(4), 2)):
        a[i, j] = a[j, i] = value
    return a


def sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))


@lru_cache(None)
def overlap_control():
    symmetric = [symmetric_matrix("s"+str(i)) for i in range(3)]
    commutator = symmetric[1]*symmetric[2]-symmetric[2]*symmetric[1]
    assert sp.expand(sp.trace(symmetric[0]*commutator)) == 0
    alpha = [sp.Matrix(sp.symbols("a"+str(i)+"_0:4")) for i in range(3)]
    mixed = sum(sign(p)*(alpha[p[1]].T*symmetric[p[0]]*alpha[p[2]])[0]
                for p in permutations(range(3)))
    assert sp.expand(mixed) == 0
    skew = sp.zeros(4)
    skew[0, 1], skew[1, 0] = 1, -1
    diag = sp.diag(1, -1, 0, 0)
    off = sp.zeros(4)
    off[0, 1] = off[1, 0] = 1
    bad_cubic = sp.trace(skew*(diag*off-off*diag))
    assert bad_cubic == -4
    e = [sp.eye(4)[:, i] for i in range(4)]
    a = [e[0], e[1], sp.zeros(4, 1)]
    bad_s = [sp.zeros(4), sp.zeros(4), skew]
    bad_mixed = sum(sign(p)*(a[p[1]].T*bad_s[p[0]]*a[p[2]])[0]
                    for p in permutations(range(3)))
    assert bad_mixed == 2
    # Even a symmetric singlet need not vanish for independent profiles.
    independent = [sp.zeros(4, 1), e[0], sp.zeros(4, 1)]
    singlet = [sp.zeros(4), sp.zeros(4), diag]
    wrong_shared = sum(sign(p)*(a[p[1]].T*singlet[p[0]]*independent[p[2]])[0]
                       for p in permutations(range(3)))
    assert wrong_shared == 1
    return {"all_symmetric_singlet_cubic_zero": True,
            "shared_profile_mixed_cubic_zero": True,
            "skew_singlet_counterexample": int(bad_cubic),
            "skew_mixed_counterexample": int(bad_mixed),
            "independent_profile_counterexample": int(wrong_shared)}


@lru_cache(None)
def gauge_weight_control():
    # Twice the weights makes all parity/invariant tests integer-exact.
    spins = [set(v for v in product((-1, 1), repeat=5) if v.count(-1) % 2 == p)
             for p in range(2)]
    assert all(len(s) == 16 for s in spins)
    neg = lambda v: tuple(-x for x in v)
    assert {neg(v) for v in spins[0]} == spins[1]
    assert all(neg(v) not in s for s in spins for v in s)
    assert all(all((a+b+c) % 2 != 0 for a, b, c in zip(u, v, w))
               for u, v, w in product(spins[0] | spins[1], repeat=3))
    return {"spinor_pairing_opposite_only": True,
            "no_three_spinor_zero_weight": True,
            "possible_cubic_types": ["singlet^3", "singlet*16*16dual"]}


@lru_cache(None)
def result_locks():
    expected = {
        ("1", "-1"): ({"E": 1, "dual_E": 1, "wedge2E": 0, "dual_wedge2E": 0, "off": 1}, 45),
        ("1", "1", "1", "1", "1"): ({"E": 0, "dual_E": 0, "wedge2E": 0, "dual_wedge2E": 0, "off": 1}, 25),
        ("1", "1"): ({"E": 0, "dual_E": 0, "wedge2E": 0, "dual_wedge2E": 0, "off": 0}, 24),
        ("1", "0", "1"): ({"E": 0, "dual_E": 0, "wedge2E": 0, "dual_wedge2E": 0, "off": 0}, 24),
    }
    for number in range(2):
        cert = c.certificate(number)
        for factor in cert["candidate_factors"]:
            h0, dimension = expected[tuple(factor)]
            actual = c.point(number, tuple(factor))
            assert actual["H0"] == h0 and actual["full_parent_dimension"] == dimension
        spectrum = c.enhanced_matter(number)
        assert spectrum["conditional_D5_degree_one_spectrum"] == {"45": 0, "1": 3, "16": 1, "16_dual": 1, "10": 0}
        assert spectrum["full_degree_one_dimension"] == 35
    return {"post_result_gauge_and_matter_locks": True}


def main():
    print("LOCKS", json.dumps(result_locks()), flush=True)
    for number in range(2):
        print("SYMMETRIC", json.dumps(symmetric_mode_control(number)), flush=True)
    print("OVERLAPS", json.dumps(overlap_control()), flush=True)
    print("WEIGHTS", json.dumps(gauge_weight_control()), flush=True)
    print("SCOPE", json.dumps({"background": "t=1, trivial common line",
          "tensor": "direct classical holomorphic cubic among degree-one zero modes",
          "gauge_interactions_zero": False, "quantum_vanishing_claimed": False,
          "all_zero_modes_integrable": False, "isolated_4d_EFT": False}), flush=True)
    print("PASS: symmetric-mode overlap controls and original result locks")


if __name__ == "__main__":
    main()
