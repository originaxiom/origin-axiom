"""Exact five-point monomial gate; stdout only, no generated file writes."""
import json
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "finite_irreducible_sl5_2026_09_27"))
from verify_finite_seed import compose, even, generated_group, inverse
from verify_global_seed import (
    DEGREE, Rep, circle_restrictions, eye, hs, indexed, kron,
    null_columns, pullback, vs, wedge_over_field, zero,
)
from verify_topology import cover
from flint import fmpq, fmpq_mat


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def pword(word, gens):
    value = tuple(range(len(gens[0])))
    for x in word:
        value = compose(value, gens[x-1] if x > 0 else inverse(gens[-x-1]))
    return value


def pmat(p):
    return fmpq_mat([[int(i == p[j]) for j in range(len(p))] for i in range(len(p))])


def five_point_action(seed):
    gens = [tuple(seed[k]) for k in ("T", "B", "C")]
    group = generated_group(gens)
    one = tuple(range(6))
    involutions = sorted(g for g in group if g != one and compose(g, g) == one)
    subgroups = sorted({tuple(sorted((one, a, b, compose(a, b))))
                       for a, b in combinations(involutions, 2) if compose(a, b) == compose(b, a)})
    assert all(len(set(h)) == 4 for h in subgroups)
    assert len(subgroups) == 5, ("expected five V4 subgroups", len(subgroups))
    ids = {h: i for i, h in enumerate(subgroups)}
    actions = {g: tuple(ids[tuple(sorted(compose(compose(g, h), inverse(g)) for h in subgroup))]
                        for subgroup in subgroups) for g in group}
    for g in group:
        for h in gens:
            assert actions[compose(g, h)] == compose(actions[g], actions[h])
    image = set(actions.values())
    assert len(group) == len(image) == 60 and all(even(p) for p in image)
    assert len({p[0] for p in image}) == 5
    pg = [actions[g] for g in gens]
    rels, mu, lam = cover(2)
    assert all(pword(r, pg) == tuple(range(5)) for r in rels)
    assert pword(mu, pg) == pg[0]
    return pg, {"source_order": len(group), "involutions": len(involutions),
                "V4_count": len(subgroups), "faithful_even_image_order": len(image),
                "generators": pg, "longitude": pword(lam, pg)}


def rowperm(x, p):
    pi = inverse(p)
    return fmpq_mat([[x[pi[i], j] for j in range(x.ncols())] for i in range(len(p))])


def product(a, b):
    p, x = a
    q, y = b
    return compose(p, q), x+rowperm(y, p)


def minverse(a):
    p, x = a
    pi = inverse(p)
    return pi, -rowperm(x, pi)


def mword(word, generators):
    out = tuple(range(5)), zero(5, generators[0][1].ncols())
    for x in word:
        out = product(out, generators[x-1] if x > 0 else minverse(generators[-x-1]))
    return out


def orbits(generators):
    unseen, answer = set(range(5)), []
    while unseen:
        start = min(unseen)
        found, queue = {start}, [start]
        for i in queue:
            for g in generators:
                j = g[i]
                if j not in found:
                    found.add(j)
                    queue.append(j)
        unseen -= found
        answer.append(sorted(found))
    return answer


def primitive(column):
    fracs = [Fraction(str(x)) for x in column]
    denominator = lcm(*(q.denominator for q in fracs))
    out = [int(q*denominator) for q in fracs]
    divisor = gcd(*out)
    assert divisor
    out = [x//divisor for x in out]
    if next(x for x in out if x) < 0:
        out = [-x for x in out]
    return out


def exponent_space(pg):
    z, b, c = zero(5, 10), zero(5, 10), zero(5, 10)
    for i in range(5):
        b[i, i] = c[i, i+5] = 1
    generators = list(zip(pg, (z, b, c)))
    rels, _, lam = cover(2)
    constraints = []
    for word in rels:
        p, x = mword(word, generators)
        assert p == tuple(range(5))
        constraints.append(x)
    p, longitude = mword(lam, generators)
    assert p == pword(lam, pg)
    constraints.append(longitude)
    constraints.append(fmpq_mat([[1]*5+[0]*5, [0]*5+[1]*5]))
    equations = vs(*constraints)
    solutions = null_columns(equations)
    cycles = orbits([pg[0]])
    s = fmpq_mat([[int(i in cycle) for cycle in cycles] for i in range(5)])
    gauge = vs(s-rowperm(s, pg[1]), s-rowperm(s, pg[2]))
    assert equations*gauge == zero(equations.nrows(), gauge.ncols())
    span, chosen = gauge, []
    for j in range(solutions.ncols()):
        candidate = fmpq_mat([[solutions[i, j]] for i in range(10)])
        if hs(span, candidate).rank() > span.rank():
            vector = primitive([candidate[i, 0] for i in range(10)])
            chosen.append(vector)
            span = hs(span, fmpq_mat([[x] for x in vector]))
    assert span.rank() == solutions.ncols()
    return chosen, {"equation_rank": equations.rank(), "solution_dimension": solutions.ncols(),
                    "gauge_rank": gauge.rank(), "quotient_dimension": len(chosen),
                    "primitive_directions": chosen, "peripheral_sheet_orbits": orbits([pg[0], p])}


def monomial_matrices(pg, direction, t):
    exponents = [[0]*5, direction[:5], direction[5:]]
    result = []
    for p, v in zip(pg, exponents):
        result.append(fmpq_mat([[fmpq(t)**v[i] if i == p[j] else 0 for j in range(5)] for i in range(5)]))
    return result


def algebra_dimension(matrices):
    basis = [eye(5)]
    rows = [[int(i == j) for i in range(5) for j in range(5)]]
    for a in basis:
        for g in matrices:
            candidate = a*g
            row = [candidate[i, j] for i in range(5) for j in range(5)]
            if fmpq_mat(rows+[row]).rank() > len(rows):
                rows.append(row)
                basis.append(candidate)
            if len(rows) == 25:
                return 25
    return len(rows)


def bilinear_nullity(matrices):
    columns = []
    for i in range(5):
        for j in range(5):
            q = zero(5, 5)
            q[i, j] = 1
            column = []
            for g in matrices:
                delta = g.transpose()*q*g-q
                column.extend(delta[a, b] for a in range(5) for b in range(5))
            columns.append(column)
    return 25-fmpq_mat(list(map(list, zip(*columns)))).rank()


def offdiagonal_action(matrices, pg):
    pairs = [(i, j) for i in range(5) for j in range(5) if i != j]
    ids = {p: i for i, p in enumerate(pairs)}
    actions = []
    for g, p in zip(matrices, pg):
        action = zero(20, 20)
        gi = g.inv()
        for k, (i, j) in enumerate(pairs):
            e = zero(5, 5)
            e[i, j] = 1
            y = g*e*gi
            pi, pj = p[i], p[j]
            action[ids[(pi, pj)], k] = y[pi, pj]
            assert all(y[a, b] == (y[pi, pj] if (a, b) == (pi, pj) else 0)
                       for a in range(5) for b in range(5))
        actions.append(action)
    return actions


def diagnose(pg, direction, t):
    matrices = monomial_matrices(pg, direction, t)
    rels, mu, lam = cover(2)
    raw = Rep(matrices)
    assert all(g.det() == 1 for g in matrices)
    assert all(raw.word(r) == eye(5) for r in rels)
    assert raw.word(mu) == pmat(pg[0])
    assert raw.word(lam) == pmat(pword(lam, pg))
    assert raw.word(mu)**3 == eye(5)
    e = Rep([kron(g, eye(DEGREE)) for g in matrices])
    wedge = Rep([wedge_over_field(g) for g in e.mats])
    out = {"parameter": t, "algebra_dimension": algebra_dimension(matrices),
           "bilinear_form_dimension": bilinear_nullity(matrices), "coefficients": {}}
    for name, rep in (("E", e), ("wedge2E", wedge)):
        down, up = indexed(rep, 2), indexed(pullback(rep), 6)
        out["coefficients"][name] = {"M2": down, "M6": up,
                                   "M6_interior": up["V"][1]-up["V"][4],
                                   "M6_dual_interior": up["dual"][1]-up["dual"][4]}
    off = Rep([kron(a, eye(DEGREE)) for a in offdiagonal_action(matrices, pg)])
    out["off_monomial"] = indexed(off, 2)
    out["off_monomial_restrictions"] = circle_restrictions(off, 2)
    return out


@lru_cache(None)
def one_seed(number):
    inp = inputs()
    pg, group = five_point_action(inp["seeds"][number])
    directions, exponents = exponent_space(pg)
    control = monomial_matrices(pg, [0]*10, inp["control_parameter"])
    assert algebra_dimension(control) < 25 and bilinear_nullity(control) > 0
    answer = {"seed": number, "action": group, "exponents": exponents,
              "finite_control": {"algebra_dimension": algebra_dimension(control),
                                 "bilinear_form_dimension": bilinear_nullity(control)},
              "candidates": []}
    for k, direction in enumerate(directions):
        answer["candidates"].append({"direction": k, "exponents": direction,
                                    "diagnostics": diagnose(pg, direction, inp["parameter"])})
    return answer


def main():
    for i in range(len(inputs()["seeds"])):
        print("SEED", i, json.dumps(one_seed(i)), flush=True)
    print("PASS: exact monomial ansatz gate; no physical or integrability claim")


if __name__ == "__main__":
    main()
