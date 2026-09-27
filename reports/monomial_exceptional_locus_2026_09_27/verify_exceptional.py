"""Laurent-minor certificates and exact number-field exceptional diagnostics."""
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "five_point_monomial_gate_2026_09_27"))
from verify_monomial import monomial_matrices, offdiagonal_action
from verify_global_seed import Rep, eye, hs, kron, null_columns, pullback, vs, zero
from verify_topology import cover
from flint import fmpq, fmpq_mat
import sympy as sp
from sympy.polys.matrices import DomainMatrix

t = sp.Symbol("t")


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


def identity(n):
    return tuple(range(n)), (0,)*n, (1,)*n


def invperm(p):
    q = [0]*len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def mul(a, b):
    p, v, s = a
    q, w, r = b
    pi = invperm(p)
    return (tuple(p[q[i]] for i in range(len(p))),
            tuple(v[i]+w[pi[i]] for i in range(len(p))),
            tuple(s[i]*r[pi[i]] for i in range(len(p))))


def inverse(a):
    p, v, s = a
    return invperm(p), tuple(-v[p[i]] for i in range(len(p))), tuple(s[p[i]] for i in range(len(p)))


def word(w, gens):
    value = identity(len(gens[0][0]))
    for x in w:
        value = mul(value, gens[x-1] if x > 0 else inverse(gens[-x-1]))
    return value


def modules(seed):
    base = [(tuple(p), tuple(v), (1,)*5) for p, v in zip(seed["permutations"], seed["exponents"])]
    off_pairs = [(i, j) for i in range(5) for j in range(5) if i != j]
    wedge_pairs = list(combinations(range(5), 2))
    out = {"E": base, "off": [], "wedge2E": []}
    for p, v, s in base:
        for name, pairs in (("off", off_pairs), ("wedge2E", wedge_pairs)):
            ids = {pair: i for i, pair in enumerate(pairs)}
            op, ov, os = [0]*len(pairs), [0]*len(pairs), [0]*len(pairs)
            for k, (i, j) in enumerate(pairs):
                a, b = p[i], p[j]
                target = (a, b) if name == "off" else tuple(sorted((a, b)))
                dest = ids[target]
                op[k] = dest
                ov[dest] = v[a]-v[b] if name == "off" else v[a]+v[b]
                os[dest] = 1 if name == "off" or a < b else -1
            out[name].append((tuple(op), tuple(ov), tuple(os)))
    for gens in out.values():
        assert all(word(r, gens) == identity(len(gens[0][0])) for r in cover(2)[0])
        assert all(x == 0 for x in word(cover(2)[2], gens)[1])
    return out


def matrix(g):
    p, v, s = g
    out = sp.zeros(len(p))
    for j, i in enumerate(p):
        out[i, j] = s[i]*t**v[i]
    return out


def fox(w, which, gens):
    n = len(gens[0][0])
    prefix, result = identity(n), sp.zeros(n)
    for x in w:
        if x > 0:
            if x == which:
                result += matrix(prefix)
            prefix = mul(prefix, gens[x-1])
        else:
            prefix = mul(prefix, inverse(gens[-x-1]))
            if -x == which:
                result -= matrix(prefix)
    return result


def evaluate(expr, value):
    return fmpq_mat([[fmpq(str(x.subs(t, value))) for x in row] for row in expr.tolist()])


def pivots(a):
    rref, rank = a.rref()
    return [next(j for j in range(a.ncols()) if rref[i, j]) for i in range(rank)]


def selected_minor(a, control):
    numeric = evaluate(a, control)
    cols = pivots(numeric)
    restricted = fmpq_mat([[numeric[i, j] for j in cols] for i in range(numeric.nrows())])
    rows = pivots(restricted.transpose())
    square = a.extract(rows, cols)
    normalized, shifts = [], []
    for row in square.tolist():
        powers = [int(term.as_powers_dict().get(t, 0)) for x in row
                  for term in sp.expand(x).as_ordered_terms() if term != 0]
        shift = max(0, -min(powers, default=0))
        shifts.append(shift)
        normalized.append([sp.expand(x*t**shift) for x in row])
    dm = DomainMatrix.from_list_sympy(len(rows), len(cols), normalized)
    determinant = sp.Poly(dm.domain.to_sympy(dm.det()), t, domain=sp.QQ)
    assert not determinant.is_zero
    sub = fmpq_mat([[numeric[i, j] for j in cols] for i in rows])
    assert fmpq(str(determinant.eval(control))) == sub.det()*fmpq(control)**sum(shifts)
    _, factors = sp.factor_list(determinant.as_expr(), t)
    record = {"rank": len(cols), "rows": rows, "columns": cols,
              "row_shifts": shifts, "cleared_determinant": str(determinant.as_expr()),
              "factors": [{"coefficients": [str(c) for c in sp.Poly(f, t).monic().all_coeffs()],
                           "multiplicity": int(power)} for f, power in factors]}
    return record, determinant


def companion(coefficients):
    coeffs = [fmpq(str(c)) for c in coefficients]
    assert coeffs[0] == 1
    degree = len(coeffs)-1
    value = zero(degree, degree)
    for i in range(degree-1):
        value[i+1, i] = 1
    for i in range(degree):
        value[i, degree-1] = -coeffs[degree-i]
    total = zero(degree, degree)
    for c in coeffs:
        total = total*value+c*eye(degree)
    assert total == zero(degree, degree)
    return value


def specialization(gens, value):
    degree = value.nrows()
    reps = []
    for p, v, s in gens:
        n = len(p)
        a = zero(n*degree, n*degree)
        for j, i in enumerate(p):
            block = s[i]*(value**v[i])
            for k in range(degree):
                for l in range(degree):
                    a[i*degree+k, j*degree+l] = block[k, l]
        reps.append(a)
    return Rep(reps)


def scaled(values, degree):
    assert all(x % degree == 0 for x in values), values
    return tuple(x//degree for x in values)


def cohom(rep, n, degree):
    rels, mu, lam = cover(n)
    ng, d = len(rep.mats), rep.d
    assert ng == n+1
    assert all(rep.word(r) == eye(d) for r in rels)
    d0 = vs(*(a-eye(d) for a in rep.mats))
    d1 = vs(*(hs(*(rep.fox(r, g) for g in range(1, ng+1))) for r in rels))
    assert d1*d0 == zero(d1.nrows(), d0.ncols())
    cocycles = null_columns(d1)
    bd = vs(rep.word(mu)-eye(d), rep.word(lam)-eye(d))
    bd1 = hs(-(rep.word(lam)-eye(d)), rep.word(mu)-eye(d))
    restriction = vs(*(hs(*(rep.fox(w, g) for g in range(1, ng+1))) for w in (mu, lam)))
    assert restriction*d0 == bd and bd1*bd == zero(d, d)
    assert bd1*restriction*cocycles == zero(d, cocycles.ncols())
    r0, rb = d0.rank(), bd.rank()
    r1 = hs(restriction*cocycles, bd).rank()-rb
    result = scaled((d-r0, cocycles.ncols()-r0, d-rb, 2*d-bd1.rank()-rb, r1), degree)
    profile = {"H1": result[1], "torus_rank": result[4], "torus_kernel": result[1]-result[4]}
    for name, w in (("meridian", mu), ("longitude", lam)):
        bd = rep.word(w)-eye(d)
        restriction = hs(*(rep.fox(w, g) for g in range(1, ng+1)))
        rank = scaled((hs(restriction*cocycles, bd).rank()-bd.rank(),), degree)[0]
        profile[name+"_rank"] = rank
        profile[name+"_kernel"] = result[1]-rank
    return result, profile


def indexed(rep, n, degree):
    a, profile = cohom(rep, n, degree)
    b, _ = cohom(rep.dual(), n, degree)
    index = a[1]-a[4]-b[1]+b[4]
    assert a[4]+b[4] == a[3] == b[3]
    assert index == a[0]-b[0]+b[2]-a[4]
    return {"I": index, "V": a, "dual": b}, profile


def field_coordinates(a, degree):
    return [a[i*degree+k, j*degree] for i in range(5) for j in range(5) for k in range(degree)]


def algebra_dimension(rep, value):
    degree = value.nrows()
    scalars = [kron(eye(5), value**k) for k in range(degree)]
    basis = [eye(rep.d)]
    rows = [field_coordinates(s, degree) for s in scalars]
    for a in basis:
        for g in rep.mats:
            candidate = a*g
            expanded = [field_coordinates(s*candidate, degree) for s in scalars]
            rank = fmpq_mat(rows+expanded).rank()
            assert rank in (len(rows), len(rows)+degree)
            if rank > len(rows):
                rows += expanded
                basis.append(candidate)
            if len(rows) == 25*degree:
                return 25
    return len(rows)//degree


def bilinear_dimension(gens, value):
    degree = value.nrows()
    rows = []
    for p, v, s in gens:
        a = zero(25*degree, 25*degree)
        for i in range(5):
            for j in range(5):
                dest = 5*p[i]+p[j]
                source = 5*i+j
                block = s[p[i]]*s[p[j]]*(value**(v[p[i]]+v[p[j]]))
                for k in range(degree):
                    for l in range(degree):
                        a[source*degree+k, dest*degree+l] += block[k, l]
                    a[source*degree+k, source*degree+k] -= 1
        rows.append(a)
    return scaled((25*degree-vs(*rows).rank(),), degree)[0]


def point_diagnostics(mods, value):
    degree = value.nrows()
    e = specialization(mods["E"], value)
    out = {"field_degree": degree, "matrix_algebra_dimension": algebra_dimension(e, value),
           "invariant_bilinear_dimension": bilinear_dimension(mods["E"], value), "coefficients": {}}
    for name in ("E", "wedge2E"):
        rep = specialization(mods[name], value)
        down, _ = indexed(rep, 2, degree)
        up, _ = indexed(pullback(rep), 6, degree)
        out["coefficients"][name] = {"M2": down, "M6": up,
                                    "M6_interior": up["V"][1]-up["V"][4],
                                    "M6_dual_interior": up["dual"][1]-up["dual"][4]}
    off = specialization(mods["off"], value)
    out["off"], out["restrictions"] = indexed(off, 2, degree)
    jac = vs(*(hs(off.fox(r, 2), off.fox(r, 3)) for r in cover(2)[0]))
    fixed = null_columns(off.mats[0]-eye(off.d))
    gauge = vs(off.mats[1]-eye(off.d), off.mats[2]-eye(off.d))*fixed
    assert jac*gauge == zero(jac.nrows(), gauge.ncols())
    jr, gr, dim = scaled((jac.rank(), gauge.rank(), fixed.ncols()), degree)
    relative = 40-jr-gr
    assert dim == 8 and relative == out["restrictions"]["meridian_kernel"]
    out["fixed_meridian"] = {"J_rank": jr, "gauge_rank": gr, "relative_H1": relative}
    return out


@lru_cache(None)
def certificates(number):
    seed = inputs()["seeds"][number]
    mods = modules(seed)
    off = mods["off"]
    jac = sp.Matrix.vstack(*(sp.Matrix.hstack(fox(r, 2, off), fox(r, 3, off)) for r in cover(2)[0]))
    fixed = null_columns(evaluate(matrix(off[0])-sp.eye(20), 2))
    assert fixed.ncols() == 8
    basis = sp.Matrix([[sp.Rational(str(fixed[i, j])) for j in range(fixed.ncols())] for i in range(20)])
    gauge = sp.Matrix.vstack(matrix(off[1])-sp.eye(20), matrix(off[2])-sp.eye(20))*basis
    assert all(sp.expand(x) == 0 for x in jac*gauge)
    old = Rep(offdiagonal_action(monomial_matrices(seed["permutations"],
                                                  seed["exponents"][1]+seed["exponents"][2], 2),
                                seed["permutations"]))
    old_jac = vs(*(hs(old.fox(r, 2), old.fox(r, 3)) for r in cover(2)[0]))
    assert evaluate(jac, 2) == old_jac
    records, candidates = {}, {}
    for name, a in (("J", jac), ("gauge", gauge)):
        record, determinant = selected_minor(a, inputs()["generic_control"])
        records[name] = record
        assert record["rank"] == (32 if name == "J" else 8)
        for factor in record["factors"]:
            coeffs = factor["coefficients"]
            if coeffs == ["1", "0"]:
                continue
            candidates[tuple(coeffs)] = coeffs
    return mods, {"seed": number, "minors": records,
                  "candidate_factors": sorted(candidates.values(), key=lambda x: (len(x), x))}


def factor_metadata(coefficients):
    polynomial = sp.Poly.from_list([sp.Rational(c) for c in coefficients], t)
    cyclotomic = bool(polynomial.is_cyclotomic)
    order = None
    if cyclotomic:
        for k in range(1, 1025):
            if sp.Poly(sp.cyclotomic_poly(k, t), t) == polynomial:
                order = k
                break
        assert order is not None
    return {"coefficients": coefficients, "polynomial": str(polynomial.as_expr()),
            "cyclotomic": cyclotomic, "root_order_if_cyclotomic": order}


def main():
    for i in range(len(inputs()["seeds"])):
        mods, record = certificates(i)
        print("CERTIFICATE", i, json.dumps(record), flush=True)
        for coefficients in record["candidate_factors"]:
            meta = factor_metadata(coefficients)
            if len(coefficients)-1 > inputs()["max_factor_degree"]:
                print("UNANALYSED", i, json.dumps(meta), flush=True)
                continue
            diag = point_diagnostics(mods, companion(coefficients))
            print("ROOT", i, json.dumps({"factor": meta, "diagnostics": diag}), flush=True)
    print("PASS: exact minors and declared-degree exceptional diagnostics; no integrability claim")


if __name__ == "__main__":
    main()
