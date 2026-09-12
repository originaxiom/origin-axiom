"""Run with sage -python. Separate exact-ring audit, not a physical vacuum solver."""
import json
from math import comb
from sage.all import GF, QQ, PolynomialRing, NumberField, matrix, vector, identity_matrix, zero_matrix, diagonal_matrix
from sage.env import SAGE_VERSION


GENS = ('a', 'b')
RELS = ('aabaBaaBab',)
PERIPH = ('AbAA', 'babA')


def stack(blocks):
    out = blocks[0]
    for b in blocks[1:]:
        out = out.stack(b)
    return out


def join(blocks):
    out = blocks[0]
    for b in blocks[1:]:
        out = out.augment(b)
    return out


def ev(w, rho):
    first = next(iter(rho.values()))
    out = identity_matrix(first.base_ring(), first.nrows())
    for c in w:
        out = out*(rho[c] if c.islower() else rho[c.lower()].inverse())
    return out


def sy(a, m):
    r = a.base_ring()
    out = zero_matrix(r, m+1)
    for j in range(m+1):
        for k in range(m-j+1):
            for l in range(j+1):
                out[k+l, j] += (comb(m-j, k)*comb(j, l)*a[0, 0]**(m-j-k)*
                                 a[1, 0]**k*a[0, 1]**(j-l)*a[1, 1]**l)
    return out


def word_cocycles(w, rho):
    """Compare Fox prefixes with right-to-left crossed-homomorphism recurrence."""
    first = next(iter(rho.values()))
    r, d = first.base_ring(), first.nrows()
    one = identity_matrix(r, d)
    prefix, fox = one, {g: zero_matrix(r, d) for g in GENS}
    for c in w:
        g = c.lower()
        if c.isupper():
            prefix = prefix*rho[g].inverse()
            fox[g] -= prefix
        else:
            fox[g] += prefix
            prefix = prefix*rho[g]
    fox = join([fox[g] for g in GENS])
    z = zero_matrix(r, d, len(GENS)*d)
    units = {g: zero_matrix(r, d, len(GENS)*d) for g in GENS}
    for k, g in enumerate(GENS):
        units[g][:, k*d:(k+1)*d] = one
    for c in reversed(w):
        g = c.lower()
        if c.isupper():
            z = rho[g].inverse()*(z-units[g])
        else:
            z = units[g]+rho[g]*z
    if z != fox:
        raise ArithmeticError("Independent cocycle constructions disagree")
    return z


def dual(rho):
    return {g: a.inverse().transpose() for g, a in rho.items()}


def cohomology(rho):
    first = next(iter(rho.values()))
    r, d = first.base_ring(), first.nrows()
    one = identity_matrix(r, d)
    if any(ev(w, rho) != one for w in RELS):
        raise ValueError("Relator is not +I")
    j = stack([word_cocycles(w, rho) for w in RELS])
    f = stack([word_cocycles(w, rho) for w in PERIPH])
    bq = stack([rho[g]-one for g in GENS])
    mu, la = [ev(w, rho) for w in PERIPH]
    bt, dt = (mu-one).stack(la-one), (one-la).augment(mu-one)
    z = j.right_kernel().basis_matrix().transpose()
    rz = f*z
    checks = dict(relations=all(ev(w, rho) == one for w in RELS),
                  differential_square=(j*bq).is_zero(), peripheral_commute=mu*la == la*mu,
                  boundary_square=(dt*bt).is_zero(), restriction_cocycles=(dt*rz).is_zero(),
                  restriction_coboundaries=f*bq == bt)
    if not all(checks.values()):
        raise ArithmeticError(checks)
    a0, a1 = d-bq.rank(), z.ncols()-bq.rank()
    r1 = rz.augment(bt).rank()-bt.rank()
    r1_stack = j.stack(f).rank()-j.rank()-bt.rank()
    if r1 != r1_stack:
        raise ArithmeticError("Restriction-rank constructions disagree")
    return dict(a0=a0, a1=a1, a2=j.nrows()-j.rank(), t0=d-bt.rank(),
                t1=2*d-dt.rank()-bt.rank(), r1=r1, n=a1-r1,
                checks=checks, restriction_stack=r1_stack,
                j=j, f=f, bq=bq, bt=bt, mu=mu, longitude=la)


def paired(rho):
    a, b = cohomology(rho), cohomology(dual(rho))
    i = a['n']-b['n']
    identities = dict(annihilator=a['r1']+b['r1'] == a['t1'],
                      torus=a['t1'] == a['t0']+b['t0'],
                      general_index=i == a['a0']-b['a0']+b['t0']-a['r1'],
                      euler=a['a0']-a['a1']+a['a2'] == b['a0']-b['a1']+b['a2'] == 0)
    return dict(V=a, dual=b, index=i, identities=identities,
                dimension_equalities=a['a0'] == b['a0'] and a['t0'] == b['t0'])


def algebra_dimension(rho):
    first = next(iter(rho.values()))
    r, d = first.base_ring(), first.nrows()
    basis = [identity_matrix(r, d)]
    flattened = matrix(r, [basis[0].list()])
    i = 0
    while i < len(basis):
        for a in rho.values():
            v = basis[i]*a
            trial = flattened.stack(matrix(r, [v.list()]))
            if trial.rank() > len(basis):
                basis.append(v)
                flattened = trial
        i += 1
    return len(basis)


def complement_to_first_line(rho):
    first = next(iter(rho.values()))
    r, d = first.base_ring(), first.nrows()
    if any(any(a[i, 0] != 0 for i in range(1, d)) for a in rho.values()):
        raise ValueError("First line is not invariant")
    columns = []
    for j in range(d):
        projector = zero_matrix(r, d)
        projector[0, j] = 1
        col = []
        for a in rho.values():
            col.extend((projector*a-a*projector).list())
        col.append(r(j == 0))
        columns.append(col)
    eq = matrix(r, columns).transpose()
    rhs = vector(r, [0]*(eq.nrows()-1)+[1])
    augmented = eq.augment(matrix(r, eq.nrows(), 1, list(rhs)))
    consistent = eq.rank() == augmented.rank()
    certificate = None
    if consistent:
        row = eq.solve_right(rhs)
        certificate = zero_matrix(r, d)
        certificate[0, :] = row
        assert certificate*certificate == certificate
        assert all(certificate*a == a*certificate for a in rho.values())
    return dict(equation_rank=eq.rank(), augmented_rank=augmented.rank(),
                invariant_complement=consistent, commuting_projection=certificate)


def intertwiner_data(rho):
    first = next(iter(rho.values()))
    r, d = first.base_ring(), first.nrows()
    target = dual(rho)
    cols = []
    for i in range(d*d):
        e = zero_matrix(r, d)
        e[i//d, i % d] = 1
        col = []
        for g in GENS:
            col.extend((e*rho[g]-target[g]*e).list())
        cols.append(col)
    eq = matrix(r, cols).transpose()
    maps = [matrix(r, d, d, v) for v in eq.right_kernel().basis()]
    return dict(dimension=len(maps), matrices=maps, ranks=[a.rank() for a in maps],
                determinants=[a.det() for a in maps],
                equations=all(all(s*rho[g] == target[g]*s for g in GENS) for s in maps))


def defective_same_eigenvalue_filter(rho, p):
    one = identity_matrix(GF(p), 2)
    return all(stack([a-lam*one for a in rho.values()]).rank() == 2 for lam in range(p))


def field_case(r, u):
    rho = dict(a=matrix(r, [[0, 1], [-1, 1]]), b=matrix(r, [[0, u**2], [u, -2]]))
    chi = dict(a=u, b=-r(1))
    p = matrix(r, [[1, 0], [u, 1]])
    base_tri = {g: p.inverse()*a*p for g, a in rho.items()}
    assert rho['a']*vector(r, [1, u]) == u*vector(r, [1, u])
    assert rho['b']*vector(r, [1, u]) == -vector(r, [1, u])
    v = {g: chi[g]*sy(a, 3) for g, a in rho.items()}
    p3 = sy(p, 3)
    tri = {g: p3.inverse()*a*p3 for g, a in v.items()}
    upper = all(a[i, j] == 0 for a in tri.values() for i in range(4) for j in range(i))
    if not upper:
        raise ArithmeticError("Claimed simultaneous invariant flag failed")
    semisimple = {g: diagonal_matrix(r, a.diagonal()) for g, a in tri.items()}
    bnil = tri['b']-identity_matrix(r, 4)
    data = dict(characteristic=r.characteristic(), minimal_polynomial_relation=u*u-u+1,
                rho=rho, coefficient_matrices=v, character=chi,
                common_line=[r(1), u], common_line_eigenvalues=dict(a=u, b=-r(1)),
                change_of_basis=p, base_triangular=base_tri, symmetric_change_of_basis=p3,
                triangular=tri, invariant_full_flag=upper,
                base_algebra_dimension=algebra_dimension(rho),
                V_algebra_dimension=algebra_dimension(v),
                base_complement=complement_to_first_line(base_tri),
                V_complement=complement_to_first_line(tri),
                unipotent_ranks=[(bnil**k).rank() for k in range(1, 5)],
                dual_intertwiners=intertwiner_data(v),
                original=paired(v), semisimplification_matrices=semisimple,
                semisimplification=paired(semisimple),
                determinant_relators=[ev(w, rho) for w in RELS])
    if r.characteristic() == 13:
        data['defective_filter_accepts'] = defective_same_eigenvalue_filter(rho, 13)
    return data


def instrument_controls():
    r = GF(13)
    irreducible = dict(a=matrix(r, [[1, 1], [0, 1]]), b=matrix(r, [[1, 0], [1, 1]]))
    diagonal = dict(a=diagonal_matrix(r, [r(2), 1/r(2)]),
                    b=diagonal_matrix(r, [r(3), 1/r(3)]))
    return dict(irreducible_algebra_dimension=algebra_dimension(irreducible),
                semisimple_diagonal_complement=complement_to_first_line(diagonal),
                semisimple_diagonal_algebra_dimension=algebra_dimension(diagonal))


def serial(x):
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(a) for a in x]
    if hasattr(x, 'nrows'):
        return [[serial(x[i, j]) for j in range(x.ncols())] for i in range(x.nrows())]
    if isinstance(x, (str, int, bool, float)) or x is None:
        return x
    try:
        if x == int(x):
            return int(x)
    except (TypeError, ValueError):
        pass
    return str(x)


def run():
    print(json.dumps(dict(part='environment', sage_version=SAGE_VERSION)), flush=True)
    polynomial_ring = PolynomialRing(QQ, 'x')
    x = polynomial_ring.gen()
    k = NumberField(x*x-x+1, 'u')
    for name, r, u in [('F13', GF(13), GF(13)(4)), ('Q(u)', k, k.gen())]:
        data = field_case(r, u)
        print(json.dumps(dict(part=name, result=serial(data))), flush=True)
        assert data['minimal_polynomial_relation'] == 0 and data['invariant_full_flag']
        assert data['base_algebra_dimension'] == 3 and data['V_algebra_dimension'] == 9
        assert not data['base_complement']['invariant_complement'] and not data['V_complement']['invariant_complement']
        assert data['unipotent_ranks'] == [3, 2, 1, 0]
        assert data['dual_intertwiners']['dimension'] == 1 and data['dual_intertwiners']['ranks'] == [3]
        assert data['dual_intertwiners']['equations'] and data['dual_intertwiners']['determinants'] == [0]
        assert data['original']['index'] == 1 and all(data['original']['identities'].values())
        assert data['original']['dimension_equalities']
        assert data['semisimplification']['index'] == 0 and all(data['semisimplification']['identities'].values())
        if name == 'F13':
            assert data['defective_filter_accepts']
    controls = instrument_controls()
    print(json.dumps(dict(part='instrument_controls', result=serial(controls))), flush=True)
    assert controls['irreducible_algebra_dimension'] == 4
    assert controls['semisimple_diagonal_complement']['invariant_complement']
    assert controls['semisimple_diagonal_algebra_dimension'] == 2
    print(json.dumps(dict(part='conclusion', result='Exact complex positive, nonsemisimple; smooth geometric theorem is separate.')), flush=True)


if __name__ == '__main__':
    run()
