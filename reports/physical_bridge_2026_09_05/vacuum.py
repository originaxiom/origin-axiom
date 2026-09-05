"""R4: exact compact-E6 vacuum, fluctuation and mixed-fermion-mass audit.

This is a chosen 4d classical field theory, not a derivation of its physical
inputs. Importing this module never runs the original producers or writes data.
"""
from collections import defaultdict
from functools import lru_cache
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
REP_PATH = ROOT / "frontier/B883_the_27/rep27.json"
REP_SHA256 = "ea36d0eb1b48354cc77f74f866d216727c31309849c65d29345cbda7df8ab1ee"
CARTAN = sp.Matrix([
    [2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0],
    [-1, 0, 2, -1, 0, 0], [0, -1, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2],
])


def comm(a, b):
    return a*b-b*a


def real_column(z):
    z = sp.Matrix(z)
    return z.applyfunc(sp.re).col_join(z.applyfunc(sp.im))


@lru_cache(maxsize=1)
def representation():
    raw = REP_PATH.read_bytes()
    if hashlib.sha256(raw).hexdigest() != REP_SHA256:
        raise ValueError("B883 input changed; audit its convention before reuse")
    data = json.loads(raw)
    w = [sp.Matrix(x) for x in data["weights"]]
    rep = [sp.Matrix(data["rep"][str(i)]) for i in range(78)]
    assert len(set(tuple(x) for x in w)) == 27
    for i in range(6):
        assert rep[i] == sp.diag(*(x[i] for x in w))
    roots = {}
    for m in rep[6:]:
        support = [(i, j) for i in range(27) for j in range(27) if m[i, j]]
        shifts = {tuple(w[i]-w[j]) for i, j in support}
        assert len(shifts) == 1
        label = next(iter(shifts))
        assert label not in roots
        roots[label] = m
    assert len(roots) == 72
    e = [roots[tuple(CARTAN[:, i])] for i in range(6)]
    for i in range(6):
        assert comm(e[i], e[i].T) == rep[i]
        for j in range(6):
            assert comm(rep[i], e[j]) == CARTAN[i, j]*e[j]
            if i != j:
                assert comm(e[i], e[j].T).is_zero_matrix
                z = e[j]
                for _ in range(1-int(CARTAN[i, j])):
                    z = comm(e[i], z)
                assert z.is_zero_matrix
    positive = []
    for label, m in roots.items():
        coeff = CARTAN.inv()*sp.Matrix(label)
        assert (coeff.T*CARTAN*coeff)[0] == 2
        if all(x >= 0 for x in coeff):
            opposite = roots[tuple(-x for x in label)]
            assert opposite == m.T or opposite == -m.T
            positive.append((tuple(coeff), label, m))
    positive.sort(key=lambda item: item[0])
    assert len(positive) == 36
    # Hermitian generators: i*T generates the compact form and preserves I27.
    compact = rep[:6]
    for _, _, m in positive:
        compact.extend((m+m.T, sp.I*(m-m.T)))
    assert all(t.H == t for t in compact)
    return w, rep, roots, positive, compact


@lru_cache(maxsize=1)
def cubic():
    w, rep, _, _, _ = representation()
    triples = [t for t in itertools.combinations_with_replacement(range(27), 3)
               if all(sum(w[a][k] for a in t) == 0 for k in range(6))]
    rows = []
    for m in rep:
        eq = defaultdict(lambda: defaultdict(int))
        for ci, t in enumerate(triples):
            # Direct polynomial derivative: dF(x)[M x], not a tensor-name test.
            for slot, a in enumerate(t):
                for b in range(27):
                    if m[a, b]:
                        key = tuple(sorted(t[:slot]+(b,)+t[slot+1:]))
                        eq[key][ci] += m[a, b]
        for terms in eq.values():
            row = [terms[j] for j in range(len(triples))]
            if any(row):
                rows.append(row)
    equations = sp.Matrix(rows)
    ns = equations.nullspace()
    assert len(ns) == 1
    coeff = ns[0]/next(x for x in ns[0] if x)
    assert equations*coeff == sp.zeros(equations.rows, 1)
    # All triples are distinct-index here; the symmetric tensor's first
    # coefficient is one. Its polynomial is 6 times the normalized polynomial.
    assert all(len(set(t)) == 3 for t in triples)
    tensor = {}
    for t, c in zip(triples, coeff):
        for p in itertools.permutations(t):
            tensor[p] = c
    return triples, coeff, equations, tensor


def contract(v):
    """The symmetric 27x27 matrix d_abc v_c, with exact coefficients."""
    out = sp.zeros(27)
    for (a, b, c), value in cubic()[3].items():
        out[a, b] += value*v[c]
    return out


@lru_cache(maxsize=1)
def embedding():
    w, rep, roots, _, _ = representation()
    # Y is inside su5's Cartan and commutes with su3 (3,4) and su2 (6).
    ns = CARTAN.extract([2, 3, 5], [2, 3, 4, 5]).nullspace()
    assert len(ns) == 1
    h = sp.Matrix([0, 0, *ns[0]])
    psi = [3*(CARTAN.inv()*v)[0] for v in w]
    q = [i for i, v in enumerate(w)
         if psi[i] == 1 and v[5] != 0 and (v[2] != 0 or v[3] != 0)]
    assert len(q) == 6
    h /= 6*(h.T*w[q[0]])[0]
    y = [(h.T*v)[0] for v in w]
    assert all(y[i] == sp.Rational(1, 6) for i in q)
    ym = sp.diag(*y)
    su5_simple = [roots[tuple(CARTAN[:, i])] for i in [2, 3, 4, 5]]
    sm_simple = [roots[tuple(CARTAN[:, i])] for i in [2, 3, 5]]

    def singlets(generators):
        return sp.Matrix.vstack(*generators).nullspace()

    sm_inv = singlets([ym, *sm_simple, *(e.T for e in sm_simple)])
    su5_inv = singlets([*su5_simple, *(e.T for e in su5_simple)])
    assert len(sm_inv) == len(su5_inv) == 2
    assert sp.Matrix.hstack(*sm_inv, *su5_inv).rank() == 2
    si = next(i for i in range(27) if psi[i] == 4)
    ni = next(i for i in range(27) if psi[i] == 1 and y[i] == 0)
    s, n = sp.eye(27)[:, si], sp.eye(27)[:, ni]
    assert sp.Matrix.hstack(*sm_inv, s, n).rank() == 2
    return s, n, ym, h, y, psi


def mass_blocks(s, n):
    sv, nv, _, _, y, psi = embedding()
    m = contract(s*sv+n*nv)
    def indices(p, charge):
        return [i for i in range(27) if psi[i] == p and y[i] == charge]
    d = indices(-2, -sp.Rational(1, 3))
    db = indices(-2, sp.Rational(1, 3))+indices(1, sp.Rational(1, 3))
    l = indices(-2, sp.Rational(1, 2))
    lb = indices(-2, -sp.Rational(1, 2))+indices(1, -sp.Rational(1, 2))
    return m, m.extract(d, db), m.extract(l, lb)


def heavy_light(m_n, m_s):
    """General family mixing: F [M_N M_S] (fbar,Fbar); unitary kinetic norm.

    Returns the Dirac singular masses and an orthonormal right nullspace.
    Rank-deficient examples keep their extra light modes, not a fixed n by fiat.
    """
    mn, ms = np.asarray(m_n, complex), np.asarray(m_s, complex)
    if (mn.ndim != 2 or mn.shape[0] != mn.shape[1] or mn.shape != ms.shape
            or not np.isfinite(mn).all() or not np.isfinite(ms).all()):
        raise ValueError("expected equally sized finite square family matrices")
    block = np.hstack((mn, ms))
    _, masses, vh = np.linalg.svd(block, full_matrices=True)
    tol = np.finfo(float).eps*max(block.shape)*(masses[0] if masses.size else 0)
    rank = int(np.count_nonzero(masses > tol))
    return masses[:rank], vh.conj().T[:, rank:]


def constraints(phi1, phi2, adjoint):
    """Numerical constraint vector; V is its squared real norm, all weights 1."""
    p, q, a = (np.asarray(x, complex) for x in (phi1, phi2, adjoint))
    p, q = p.reshape(27), q.reshape(27)
    tensor = np.zeros((27, 27, 27), complex)
    for idx, val in cubic()[3].items():
        tensor[idx] = complex(val)
    _, _, ym, _, _, _ = embedding()
    w2 = complex(sp.trace(ym*ym)).real
    out = []
    def complex_part(x):
        z = np.atleast_1d(x).ravel()
        out.extend(z.real)
        out.extend(z.imag)
    out.extend((np.vdot(p, p).real-1, np.vdot(q, q).real-1))
    complex_part(np.vdot(p, q))
    for u, v in ((p, p), (p, q), (q, q)):
        complex_part(np.einsum("abc,b,c->a", tensor, u, v))
    out.append(np.trace(a@a).real-w2)
    complex_part(a@p)
    complex_part(a@q)
    return np.asarray(out, float)


def fields_at(displacement):
    """186 real coordinates; adjoint coordinates use a positive Gram metric."""
    z = np.asarray(displacement, float)
    if z.shape != (186,) or not np.isfinite(z).all():
        raise ValueError("expected 186 finite real scalar displacements")
    s, n, y, _, _, _ = embedding()
    p = np.array(s, complex).ravel()+z[:27]+1j*z[27:54]
    q = np.array(n, complex).ravel()+z[54:81]+1j*z[81:108]
    a = np.array(y, complex)
    for c, t in zip(z[108:], representation()[4]):
        a += c*np.array(t, complex)
    return p, q, a


@lru_cache(maxsize=1)
def fluctuation_matrices():
    s, n, y, _, charges, _ = embedding()
    _, _, _, positive, generators = representation()
    bs, bn = contract(s), contract(n)
    columns = []
    for k in range(186):
        p, q, a = sp.zeros(27, 1), sp.zeros(27, 1), sp.zeros(27)
        if k < 54:
            p[k % 27] = 1 if k < 27 else sp.I
        elif k < 108:
            q[(k-54) % 27] = 1 if k < 81 else sp.I
        else:
            a = generators[k-108]
        col = sp.Matrix([2*sp.re((s.H*p)[0]), 2*sp.re((n.H*q)[0])])
        for z in (p.H*n+s.H*q, 2*bs*p, bn*p+bs*q, 2*bn*q):
            col = col.col_join(real_column(z))
        col = col.col_join(sp.Matrix([2*sp.trace(y*a)]))
        for z in (a*s+y*p, a*n+y*q):
            col = col.col_join(real_column(z))
        columns.append(col)
    j = sp.Matrix.hstack(*columns)
    orbit = sp.zeros(186, 78)
    for k, t in enumerate(generators):
        orbit[:54, k] = real_column(sp.I*t*s)
        orbit[54:108, k] = real_column(sp.I*t*n)
    for r, (_, _, m) in enumerate(positive):
        i, k = next((i, k) for i in range(27) for k in range(27) if m[i, k])
        charge = charges[i]-charges[k]
        a, b = 6+2*r, 7+2*r
        orbit[108+b, a] = -charge
        orbit[108+a, b] = charge
    for k, t in enumerate(generators):
        rebuilt = sum((orbit[108+i, k]*u for i, u in enumerate(generators)), sp.zeros(27))
        assert rebuilt == sp.I*comm(t, y)
    assert (j*orbit).is_zero_matrix
    return j, orbit


def sm_generator_coordinates():
    """Columns explicitly spanning color, weak, then hypercharge generators."""
    columns = []
    for k in [2, 3, 5]:
        columns.append(sp.eye(78)[:, k])
    for r, (coeff, _, _) in enumerate(representation()[3]):
        support = {i for i, x in enumerate(coeff) if x}
        if support <= {2, 3} or support <= {5}:
            columns.extend((sp.eye(78)[:, 6+2*r], sp.eye(78)[:, 7+2*r]))
    h = embedding()[3]
    columns.append(sp.Matrix([*h, *([0]*72)]))
    return sp.Matrix.hstack(*columns)


def analyze():
    triples, coeff, equations, _ = cubic()
    sv, nv, y, _, _, _ = embedding()
    s, n = sp.symbols("s n", real=True)
    m, md, ml = mass_blocks(s, n)
    assert sp.simplify(md*md.H-(s*s+n*n)*sp.eye(3)).is_zero_matrix
    assert sp.simplify(ml*ml.H-(s*s+n*n)*sp.eye(2)).is_zero_matrix
    assert contract(sv)*nv == sp.zeros(27, 1)
    assert contract(sv)*sv == contract(nv)*nv == sp.zeros(27, 1)
    j, orbit = fluctuation_matrices()
    rank = j.rank()
    gauge_rank = orbit.rank()
    sm = sm_generator_coordinates()
    assert sm.rank() == 12 and (orbit*sm).is_zero_matrix
    # Eleven non-abelian adjoint fluctuations; their group action is the
    # su3+su2 adjoint action, since these are the subalgebra's own matrices.
    flat = sp.zeros(186, 11)
    flat[108:, :] = sm[:, :11]
    assert (j*flat).is_zero_matrix
    additional = sp.Matrix.hstack(orbit, flat).rank()-gauge_rank
    jfloat = np.array(j, float)
    numerical_rank = int(np.linalg.matrix_rank(jfloat, tol=1e-9))
    assert numerical_rank == rank
    zero_value = float(np.dot(constraints(*fields_at(np.zeros(186))),
                              constraints(*fields_at(np.zeros(186)))))
    assert zero_value < 1e-25
    return {
        "scope": "R4 chosen compact-E6 classical model; no empirical inputs",
        "input_rep_sha256": REP_SHA256,
        "cubic": {"monomials": len(triples), "nullity": 1,
                  "abs_coefficients": sorted({int(abs(c)) for c in coeff}),
                  "invariance_equations": equations.rows},
        "singlet_indices": {"S": list(sv).index(1), "N": list(nv).index(1)},
        "hypercharge_cartan": [str(x) for x in embedding()[3]],
        "fermion_mass": {
            "triplet_block": [[str(x) for x in md.row(i)] for i in range(md.rows)],
            "doublet_block": [[str(x) for x in ml.row(i)] for i in range(ml.rows)],
            "pure_S_rank": contract(sv).rank(), "pure_N_rank": contract(nv).rank(),
            "mixed_symbolic_rank": m.rank(),
            "nonzero_dirac_mass": "sqrt(abs(s)**2+abs(n)**2), five equal copies",
        },
        "compact_stabilizer_dimensions": {
            "S": 78-orbit[:54, :].rank(),
            "S_plus_2N_single_field": 78-(orbit[:54, :]+2*orbit[54:108, :]).rank(),
            "S_and_N_distinct_fields": 78-orbit[:108, :].rank(),
            "S_N_and_Y": 78-gauge_rank,
        },
        "potential": {
            "value_at_candidate": zero_value,
            "real_scalar_coordinates": 186, "real_constraints": j.rows,
            "exact_hessian_rank": rank, "independent_numeric_rank": numerical_rank,
            "hessian_zero_modes": 186-rank, "gauge_goldstone_modes": gauge_rank,
            "nongauge_tree_level_zero_modes": 186-rank-gauge_rank,
            "exhibited_octet_plus_triplet_modes": additional,
            "all_zero_modes_accounted": bool(186-rank-gauge_rank == additional),
            "stability_scope": "global classical minimum; not an isolated or quantum-stable vacuum",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze()
    payload = json.dumps(result, indent=2, allow_nan=False)+"\n"
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
