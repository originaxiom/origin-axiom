"""All diagonal multipliers over fixed five-sheet actions, by integer lattices."""
from functools import lru_cache
from math import lcm
from pathlib import Path
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
import verify_admission as admission
from verify_topology import cover, data

HERE = Path(__file__).resolve().parent
ONE = tuple(range(5))


def inverse_perm(p):
    return tuple(p.index(i) for i in range(len(p)))


def multiply(a, b):
    p, x = a
    q, y = b
    pi = inverse_perm(p)
    return tuple(p[q[i]] for i in range(5)), x+y[list(pi), :]


def invert(a):
    p, x = a
    return inverse_perm(p), -x[list(p), :]


def word(w, generators):
    v = ONE, sp.zeros(5, generators[0][1].cols)
    for k in w:
        v = multiply(v, generators[k-1] if k > 0 else invert(generators[-k-1]))
    return v


def literal_evaluate(w, permutations, phases):
    # Independent scalar-entry implementation, phases indexed by output row.
    p, x = ONE, [sp.Rational(0)]*5
    for letter in w:
        q, y = permutations[abs(letter)-1], list(phases[abs(letter)-1])
        if letter < 0:
            old = q
            q, y = inverse_perm(old), [-y[old[i]] for i in range(5)]
        pi = inverse_perm(p)
        x = [x[i]+y[pi[i]] for i in range(5)]
        p = tuple(p[q[i]] for i in range(5))
    return p, sp.Matrix(x)


def seeds():
    return json.loads((HERE.parent / "monomial_exceptional_locus_2026_09_27" / "INPUTS.json").read_text())["seeds"]


def action_and_cocycle(number):
    seed = seeds()[number]
    down = [(tuple(p), sp.Matrix(v)) for p, v in zip(seed["permutations"], seed["exponents"])]
    up = [word(w, down) for w in data()["M6_generators_in_M2"]]
    assert all(sp.Matrix(5, 5, lambda i, j: int(i == p[j])).det() == 1 for p, _ in up)
    return [p for p, _ in up], sp.Matrix.vstack(*(x for _, x in up))


def rows(permutations, constraint):
    generators = []
    for j, p in enumerate(permutations):
        x = sp.zeros(5, 35)
        x[:, 5*j:5*j+5] = sp.eye(5)
        generators.append((p, x))
    rels, mu, lam = cover(6)
    words = [*rels]
    if constraint in ("mu", "both"):
        words.append(mu)
    if constraint == "both":
        words.append(lam)
    out = []
    for index, w in enumerate(words):
        p, x = word(w, generators)
        if index < len(rels):
            assert p == ONE
        for t in (sp.Matrix(range(35)), sp.Matrix([(-1)**i*(i+2) for i in range(35)])):
            phases = [list(t[5*j:5*j+5, 0]) for j in range(7)]
            direct_p, direct_x = literal_evaluate(w, permutations, phases)
            assert direct_p == p and direct_x == x*t
        det_row = sp.ones(1, 5)*x
        assert list(det_row) == [n for n in admission.exponent(w, 7) for _ in range(5)]
        out.append(x)
    return sp.Matrix.vstack(*out), generators, words


def smith_analysis(c, w):
    d, u, v = smith_normal_decomp(DomainMatrix.from_Matrix(c).convert_to(sp.ZZ))
    d, u, v = d.to_Matrix(), u.to_Matrix(), v.to_Matrix()
    assert d == u*c*v and abs(u.det()) == abs(v.det()) == 1
    r = sum(d[i, i] != 0 for i in range(min(d.shape)))
    assert all(d[i, j] == 0 for i in range(d.rows) for j in range(d.cols) if i != j)
    z = w*v
    assert all(z[0, i] == 0 for i in range(r, c.cols)), "obstruction unexpectedly has free component"
    ratios = [sp.Rational(z[0, i], d[i, i]) for i in range(r)]
    order = lcm(*(int(x.q) for x in ratios)) if ratios else 1
    multiplier = sp.zeros(1, c.rows)
    for i, x in enumerate(ratios):
        multiplier[0, i] = order*x
    certificate = multiplier*u
    assert all(x.q == 1 for x in certificate) and certificate*c == order*w
    witness = None
    if order > 1:
        i = next(i for i, x in enumerate(ratios) if x.q > 1)
        y = sp.zeros(c.cols, 1)
        y[i, 0] = 1/d[i, i]
        witness = v*y
        assert all(x.q == 1 for x in c*witness)
        assert (w*witness)[0].q > 1
    return {"rank": r, "free_dimension_before_conjugation": c.cols-r,
            "smith_factors": [abs(int(d[i, i])) for i in range(r)],
            "obstruction_order": order, "relation_certificate": [int(x) for x in certificate]}, witness


def obstruction_row():
    w = sp.zeros(1, 35)
    w[0, 5:10] = 8*sp.ones(1, 5)
    a = sp.Matrix(admission.topology_control()["relation_matrix"])[:, 1:]
    generator = sp.zeros(1, 6)
    generator[0, 0] = 1
    assert all(x.q == 1 for x in 40*generator*a.inv())
    assert any(x.q > 1 for x in 8*generator*a.inv())
    return w


@lru_cache(None)
def analyze(number, constraint):
    permutations, real_cocycle = action_and_cocycle(number)
    c, generators, words = rows(permutations, constraint)
    assert c*real_cocycle == sp.zeros(c.rows, 1)
    assert all(sum(real_cocycle[5*j:5*j+5, 0]) == 0 for j in range(7))
    gauge = sp.Matrix.vstack(*(sp.eye(5)-sp.eye(5)[list(inverse_perm(p)), :] for p in permutations))
    relation_rows = 30
    assert c[:relation_rows, :]*gauge == sp.zeros(relation_rows, 5)
    w = obstruction_row()
    assert w*gauge == sp.zeros(1, 5)
    result, witness = smith_analysis(c, w)
    assert result["obstruction_order"] in (1, 5)
    result.update({"seed": number, "constraint": constraint, "matrix_shape": list(c.shape),
                   "original_traceless_real_cocycle_retained": True,
                   "all_complex_multipliers_covered": True})
    if witness is not None:
        denominator = lcm(*(int(x.q) for x in witness))
        phases = [list(witness[5*j:5*j+5, 0]) for j in range(7)]
        for word_input in words:
            _, value = literal_evaluate(word_input, permutations, phases)
            assert all(x.q == 1 for x in value)
        result["witness"] = {"modulus": denominator,
                              "generator_output_phases": [[int(denominator*x) % denominator for x in p] for p in phases],
                              "determinant_on_order5_cycle": str((w*witness)[0] % 1),
                              "unitary_seed_only": True}
    else:
        result["witness"] = None
    return result


def controls():
    w = obstruction_row()
    p = [ONE]*7
    for constraint in ("free", "mu", "both"):
        c, _, _ = rows(p, constraint)
        answer, witness = smith_analysis(c, w)
        assert answer["obstruction_order"] == 5 and witness is not None
    permutations, _ = action_and_cocycle(0)
    c, _, _ = rows(permutations, "free")
    determinant_rows = sp.zeros(7, 35)
    for j in range(7):
        determinant_rows[j, 5*j:5*j+5] = sp.ones(1, 5)
    answer, witness = smith_analysis(sp.Matrix.vstack(c, determinant_rows), w)
    assert answer["obstruction_order"] == 1 and witness is None
    for diagonal, expected in [(1, 1), (5, 5)]:
        answer, _ = smith_analysis(sp.Matrix([[diagonal]]), sp.Matrix([[1]]))
        assert answer["obstruction_order"] == expected
    return {"trivial_permutation_admits_all_three_domains": True,
            "honest_SL5_constraint_forces_liftability": True,
            "synthetic_order1_order5_controls": True}


def run():
    print("CONTROLS", json.dumps(controls()), flush=True)
    for number in range(2):
        for constraint in ("free", "mu", "both"):
            print("LATTICE", json.dumps(analyze(number, constraint)), flush=True)
    print("PASS: exact lattice admission, not a chiral spectrum")


if __name__ == "__main__":
    run()
