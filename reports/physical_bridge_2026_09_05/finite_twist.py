"""R27 exact controls. No imported other-seat implementation or physical index map."""
from functools import lru_cache
from itertools import combinations, product
from math import comb
import json
import platform

import sympy as sp
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix


def clean(a):
    return a.applyfunc(sp.simplify)


def symmetric_lie(m):
    if not isinstance(m, int) or m < 0:
        raise ValueError("A nonnegative integer symmetric power is required")
    d = m + 1
    e, f = sp.zeros(d), sp.zeros(d)
    for j in range(d):
        if j:
            e[j-1, j] = j
        if j < m:
            f[j+1, j] = m-j
    h = sp.diag(*[m-2*j for j in range(d)])
    metric = sp.diag(*[sp.Rational(1, comb(m, j)) for j in range(d)])
    x = (sp.I*h, e-f, sp.I*(e+f))
    y = tuple(sp.I*a for a in x)
    return e, f, h, metric, y


def wedge_matrix(i, p):
    src, dst = list(combinations(range(3), p)), list(combinations(range(3), p+1))
    out = sp.zeros(len(dst), len(src))
    for j, s in enumerate(src):
        if i not in s:
            out[dst.index(tuple(sorted((i,)+s))), j] = (-1)**sum(k < i for k in s)
    return out


@lru_cache(None)
def bochner(m):
    e, f, h, g, y = symmetric_lie(m)
    d = m+1
    metrics = [sp.kronecker_product(sp.eye(comb(3, p)), g) for p in range(4)]
    ts = [sum((sp.kronecker_product(wedge_matrix(i, p), y[i]) for i in range(3)),
              sp.zeros(comb(3, p+1)*d, comb(3, p)*d)) for p in range(3)]
    adjs = [metrics[p].inv()*ts[p].conjugate().T*metrics[p+1] for p in range(3)]
    rows = []
    for p in (1, 2):
        hp = clean(ts[p-1]*adjs[p-1]+adjs[p]*ts[p])
        hermitian_form = clean(metrics[p]*hp)
        minors = [sp.factor(hermitian_form[:k, :k].det()) for k in range(1, hp.rows+1)]
        rows.append(dict(degree=p, dimension=hp.rows, rank=hp.rank(),
                         hermitian=hermitian_form == hermitian_form.conjugate().T,
                         leading_minors=minors,
                         strictly_positive=all(v.is_positive is True for v in minors),
                         zero=hp == sp.zeros(hp.rows)))
    return dict(power=m, sl2_relations=(e*f-f*e == h and h*e-e*h == 2*e and h*f-f*h == -2*f),
                e_adjoint_is_f=clean(g.inv()*e.conjugate().T*g-f) == sp.zeros(d),
                y_hermitian=all(clean(g.inv()*a.conjugate().T*g-a) == sp.zeros(d) for a in y),
                degrees=rows)


def circle_transfer(r):
    roots = {1: sp.Integer(1), 2: sp.Integer(-1),
             3: (-1+sp.sqrt(3)*sp.I)/2, 4: sp.I, 6: (1+sp.sqrt(3)*sp.I)/2}
    z = roots[r]
    incidence = sp.zeros(r)
    for j in range(r):
        incidence[j, j] -= 1
        incidence[j, (j+1) % r] += 1
    pull = sp.Matrix([sp.expand(z**j) for j in range(r)])
    trace = sp.Matrix([[sp.simplify(z**(-j)) for j in range(r)]])
    proj = clean(pull*trace/r)
    return dict(degree=r, character=z, incidence=incidence,
                pullback_chain=clean(incidence*pull-pull*(z-1)) == sp.zeros(r, 1),
                trace_chain=clean(trace*incidence-(z-1)*trace) == sp.zeros(1, r),
                trace_pullback=clean(trace*pull)[0],
                projector=clean(proj*proj-proj) == sp.zeros(r), projector_rank=proj.rank(),
                wrong_character_pullback_rejected=(r == 1 or
                    clean(incidence*sp.ones(r, 1)-sp.ones(r, 1)*(z-1)) != sp.zeros(r, 1)))


def rank_jump():
    rows = []
    for t in (1, 2):
        j, f = sp.Matrix([[t-1, 0]]), sp.Matrix([[1, 0]])
        n = sp.Matrix.hstack(*j.nullspace())
        rows.append(dict(parameter=t, rank_j=j.rank(), kernel_dimension=n.cols,
                         restriction_rank=(f*n).rank(), polynomial_map_rank=f.rank(),
                         stack_difference=j.col_join(f).rank()-j.rank()))
    return rows


def mod(a, p=13):
    return sp.Matrix(a).applyfunc(lambda x: int(x) % p)


def rref(a, p=13):
    a = mod(a, p)
    rows, cols = a.shape
    out, pivots, k = a.tolist(), [], 0
    for j in range(cols):
        pivot = next((i for i in range(k, rows) if out[i][j]), None)
        if pivot is None:
            continue
        out[k], out[pivot] = out[pivot], out[k]
        scale = pow(out[k][j], -1, p)
        out[k] = [v*scale % p for v in out[k]]
        for i in range(rows):
            if i != k:
                scale = out[i][j]
                out[i] = [(a-scale*b) % p for a, b in zip(out[i], out[k])]
        pivots.append(j)
        k += 1
        if k == rows:
            break
    return sp.Matrix(rows, cols, lambda i, j: out[i][j]), pivots


def rank(a, p=13):
    a = mod(a, p)
    first = len(rref(a, p)[1])
    second = DomainMatrix.from_Matrix(a).convert_to(GF(p)).rank()
    if first != second:
        raise ArithmeticError(f"Independent rank disagreement: {first}, {second}")
    return first


def kernel(a, p=13):
    a = mod(a, p)
    rr, pivots = rref(a, p)
    free = [j for j in range(a.cols) if j not in pivots]
    n = sp.zeros(a.cols, len(free))
    for k, j in enumerate(free):
        n[j, k] = 1
        for i, pivot in enumerate(pivots):
            n[pivot, k] = -rr[i, j] % p
    if mod(a*n, p) != sp.zeros(a.rows, n.cols) or rank(n, p) != a.cols-rank(a, p):
        raise ArithmeticError("Invalid kernel basis")
    return n


def inverse(a, p=13):
    a = mod(a, p)
    b = mod(a.inv_mod(p), p)
    if mod(a*b, p) != sp.eye(a.rows) or mod(b*a, p) != sp.eye(a.rows):
        raise ArithmeticError("Invalid matrix inverse")
    return b


def word(w, rho, p=13):
    d = next(iter(rho.values())).rows
    inv = {g: inverse(a, p) for g, a in rho.items()}
    out = sp.eye(d)
    for c in w:
        out = mod(out*(rho[c] if c.islower() else inv[c.lower()]), p)
    return out


def sym_power(a, m, p=13):
    """Column-vector substitution, independently expanded in two commuting variables."""
    x, y = sp.symbols('x y')
    a = mod(a, p)
    out = sp.zeros(m+1)
    for j in range(m+1):
        f = sp.Poly(sp.expand((a[0, 0]*x+a[1, 0]*y)**(m-j)*
                              (a[0, 1]*x+a[1, 1]*y)**j), x, y, modulus=p)
        for i in range(m+1):
            out[i, j] = int(f.coeff_monomial(x**(m-i)*y**i)) % p
    return out


def cocycle_map(w, gens, rho, method, p=13):
    d = next(iter(rho.values())).rows
    if method == 'fox':
        prefix = sp.eye(d)
        blocks = {g: sp.zeros(d) for g in gens}
        inv = {g: inverse(a, p) for g, a in rho.items()}
        for c in w:
            g = c.lower()
            if c.isupper():
                prefix = mod(prefix*inv[g], p)
                blocks[g] = mod(blocks[g]-prefix, p)
            else:
                blocks[g] = mod(blocks[g]+prefix, p)
                prefix = mod(prefix*rho[g], p)
        return sp.Matrix.hstack(*(blocks[g] for g in gens))
    if method != 'affine':
        raise ValueError("Unknown cochain construction")
    out = sp.zeros(d, len(gens)*d)
    for j in range(out.cols):
        extended = {}
        for k, g in enumerate(gens):
            block = sp.eye(d+1)
            block[:d, :d] = rho[g]
            if k == j//d:
                block[j % d, d] = 1
            extended[g] = block
        out[:, j] = word(w, extended, p)[:d, d]
    return out


def validate_representation(gens, rels, rho, p=13):
    d = next(iter(rho.values())).rows
    if set(rho) != set(gens):
        raise ValueError("Generator mismatch")
    if any(rank(a, p) != d for a in rho.values()):
        raise ValueError("Singular generator")
    if any(word(w, rho, p) != sp.eye(d) for w in rels):
        raise ValueError("Relator is not +I")


def quotient_columns(z, b, p=13):
    span, chosen, previous = b, [], rank(b, p)
    for j in range(z.cols):
        candidate = span.row_join(z[:, j])
        current = rank(candidate, p)
        if current > previous:
            span, previous = candidate, current
            chosen.append(z[:, j])
    return sp.Matrix.hstack(*chosen) if chosen else sp.zeros(z.rows, 0)


def cohomology(gens, rels, peripheral, rho, p=13):
    """One cusp, a deficiency-one presentation; chain hypotheses are checked."""
    validate_representation(gens, rels, rho, p)
    if len(rels) != len(gens)-1:
        raise ValueError("The declared spine is deficiency one")
    d = next(iter(rho.values())).rows
    mu, la = [word(w, rho, p) for w in peripheral]
    if mod(mu*la-la*mu, p) != sp.zeros(d):
        raise ValueError("Peripheral matrices do not commute")
    bq = sp.Matrix.vstack(*(mod(rho[g]-sp.eye(d), p) for g in gens))
    bt = mod((mu-sp.eye(d)).col_join(la-sp.eye(d)), p)
    dt = mod((sp.eye(d)-la).row_join(mu-sp.eye(d)), p)
    maps = []
    for method in ('fox', 'affine'):
        j = sp.Matrix.vstack(*(cocycle_map(w, gens, rho, method, p) for w in rels))
        f = sp.Matrix.vstack(*(cocycle_map(w, gens, rho, method, p) for w in peripheral))
        maps.append((j, f))
    if maps[0] != maps[1]:
        raise ArithmeticError("Fox and affine cocycle maps disagree")
    j, f = maps[0]
    z = kernel(j, p)
    image = mod(f*z, p)
    checks = dict(relator_boundary_zero=mod(j*bq, p) == sp.zeros(j.rows, d),
                  restriction_of_coboundaries=mod(f*bq-bt, p) == sp.zeros(2*d, d),
                  torus_boundary_zero=mod(dt*bt, p) == sp.zeros(d),
                  restriction_is_cocycle=mod(dt*image, p) == sp.zeros(d, image.cols))
    if not all(checks.values()):
        raise ArithmeticError(f"Chain-map failure: {checks}")
    rb, rj = rank(bt, p), rank(j, p)
    r1 = rank(image.row_join(bt), p)-rb
    r1_stack = rank(j.col_join(f), p)-rj-rb
    if r1 != r1_stack:
        raise ArithmeticError("Restriction-rank methods disagree")
    a0, a1 = d-rank(bq, p), len(gens)*d-rj-rank(bq, p)
    representatives = quotient_columns(image, bt, p)
    if representatives.cols != r1:
        raise ArithmeticError("Incorrect quotient representative count")
    return dict(a0=a0, a1=a1, a2=len(rels)*d-rj, t0=d-rb,
                t1=2*d-rank(dt, p)-rb, t2=d-rank(dt, p), r1=r1,
                n=a1-r1, checks=checks, two_constructions_agree=True,
                restriction_stack_rank=r1_stack, representatives=representatives,
                matrices=dict(j=j, f=f, bq=bq, bt=bt, dt=dt, mu=mu, longitude=la))


def matrix_algebra_dimension(rho, p=13):
    d = next(iter(rho.values())).rows
    basis = [sp.eye(d)]
    flattened = sp.eye(d).reshape(d*d, 1)
    i = 0
    while i < len(basis):
        for a in rho.values():
            candidate = mod(basis[i]*a, p)
            trial = flattened.row_join(candidate.reshape(d*d, 1))
            if rank(trial, p) > len(basis):
                basis.append(candidate)
                flattened = trial
        i += 1
    return len(basis)


def bilinear_sym(m, p=13):
    b = sp.zeros(m+1)
    for j in range(m+1):
        b[j, m-j] = (-1)**j*pow(comb(m, j), -1, p) % p
    return b


def image_cup(coh, pairing, p=13):
    mu, la = coh['matrices']['mu'], coh['matrices']['longitude']
    d = mu.rows
    if any(mod(a.T*pairing*a-pairing, p) != sp.zeros(d) for a in (mu, la)):
        raise ArithmeticError("Boundary pairing is not invariant")
    cup = sp.zeros(2*d)
    cup[:d, d:] = pairing*mu
    cup[d:, :d] = -pairing*la
    u = coh['representatives']
    gram = mod(u.T*cup*u, p)
    bt, dt = coh['matrices']['bt'], coh['matrices']['dt']
    zt = kernel(dt, p)
    if mod(bt.T*cup*zt, p) != sp.zeros(bt.cols, zt.cols):
        raise ArithmeticError("Cup form does not descend in first argument")
    if mod(zt.T*cup*bt, p) != sp.zeros(zt.cols, bt.cols):
        raise ArithmeticError("Cup form does not descend in second argument")
    return dict(gram=gram, rank=rank(gram, p), symmetric=gram == gram.T)


def mm2(a, b, p):
    return ((a[0]*b[0]+a[1]*b[2]) % p, (a[0]*b[1]+a[1]*b[3]) % p,
            (a[2]*b[0]+a[3]*b[2]) % p, (a[2]*b[1]+a[3]*b[3]) % p)


def enumerate_target(gens, rels, p=13, cap=300000):
    if gens != ['a', 'b']:
        raise ValueError("Received target requires ordered generators a,b")
    sl2 = [a for a in product(range(p), repeat=4) if (a[0]*a[3]-a[1]*a[2]) % p == 1]
    reps = []
    for examined, pair in enumerate(product(sl2, repeat=2), 1):
        if examined > cap:
            raise RuntimeError(f"Specified target not reached within {cap} candidate pairs")
        rho = dict(zip(gens, pair))
        rho.update({g.upper(): (a[3], -a[1] % p, -a[2] % p, a[0]) for g, a in zip(gens, pair)})
        valid = True
        for w in rels:
            out = (1, 0, 0, 1)
            for c in w:
                out = mm2(out, rho[c], p)
            if out != (1, 0, 0, 1):
                valid = False
                break
        if valid:
            reps.append({g: sp.Matrix(2, 2, rho[g]) for g in gens})
            if len(reps) == 4:
                return reps[1], examined
    raise RuntimeError("Four specified representations do not exist in enumerated population")


def dual(rho, p=13):
    return {g: inverse(a, p).T for g, a in rho.items()}


def pair_identities(a, b):
    i = a['n']-b['n']
    return dict(index=i, identities=dict(
        annihilator=a['r1']+b['r1'] == a['t1'],
        torus_duality=a['t1'] == a['t0']+b['t0'],
        general_index=i == a['a0']-b['a0']+b['t0']-a['r1'],
        euler_a=a['a0']-a['a1']+a['a2'] == 0,
        euler_b=b['a0']-b['a1']+b['a2'] == 0,
        antisymmetry=b['n']-a['n'] == -i),
        domain_equalities=a['a0'] == b['a0'] and a['t0'] == b['t0'])


@lru_cache(None)
def finite_field_witness():
    import snappy
    p = 13
    manifold = snappy.Manifold('m010')
    group = manifold.fundamental_group()
    gens, rels = list(group.generators()), list(group.relators())
    peripheral = list(group.peripheral_curves()[0])
    rho2, examined = enumerate_target(gens, rels, p)
    base = {g: sym_power(a, 3, p) for g, a in rho2.items()}
    chi = dict(zip(gens, (4, 12)))
    v = {g: mod(chi[g]*base[g], p) for g in gens}
    vi = {g: mod(pow(chi[g], -1, p)*base[g], p) for g in gens}
    vd = dual(v, p)
    a, b = [cohomology(gens, rels, peripheral, r, p) for r in (v, vd)]
    inverse_character = cohomology(gens, rels, peripheral, vi, p)
    un = cohomology(gens, rels, peripheral, base, p)
    und = cohomology(gens, rels, peripheral, dual(base, p), p)
    pairing = bilinear_sym(3, p)
    intertwiners = sp.Matrix.vstack(*(sp.kronecker_product(sp.eye(4), v[g].T)-
                                     sp.kronecker_product(vd[g], sp.eye(4)) for g in gens))
    trace_obstruction = None
    for length in range(1, 5):
        for letters in product(gens, repeat=length):
            w = ''.join(letters)
            t, td = int(sp.trace(word(w, v, p))) % p, int(sp.trace(word(w, vd, p))) % p
            if t != td:
                trace_obstruction = dict(word=w, trace=t, dual_trace=td)
                break
        if trace_obstruction:
            break
    mu2, la2 = [word(w, rho2, p) for w in peripheral]
    nil = mod(mu2-sp.eye(2), p)
    at = next((i for i, x in enumerate(nil) if x), None)
    multiple = None if at is None else int((la2-sp.eye(2))[at])*pow(int(nil[at]), -1, p) % p
    chars = {g: sp.Matrix([[chi[g]]]) for g in gens}
    invalid = None
    for i, j in product(range(4), repeat=2):
        mutant = {g: m.copy() for g, m in v.items()}
        mutant['a'][i, j] = (mutant['a'][i, j]+1) % p
        try:
            validate_representation(gens, rels, mutant, p)
        except ValueError as error:
            invalid = dict(generator='a', row=i, col=j, rejection=str(error))
            break
    return dict(manifold='m010', snappy_version=snappy.__version__,
                isosig=manifold.triangulation_isosig(), prime=p, power=3,
                generators=gens, relators=rels, peripheral=peripheral,
                rho2=rho2, character=chi, coefficient_matrices=v,
                candidate_pairs_examined=examined, target_ordinal=2,
                base_pairing_invariant=all(mod(t.T*pairing*t-pairing, p) == sp.zeros(4)
                                           for t in base.values()),
                inverse_character_intertwines_dual=all(mod(pairing*vi[g]-vd[g]*pairing, p)
                                                      == sp.zeros(4) for g in gens),
                generated_algebra_dimension=matrix_algebra_dimension(v, p),
                intertwiner_dimension=intertwiners.cols-rank(intertwiners, p),
                trace_obstruction=trace_obstruction,
                cusp=dict(mu=mu2, longitude=la2, nilpotent_square=mod(nil*nil, p),
                          mu_nontrivial=nil != sp.zeros(2), longitude_multiple=multiple,
                          one_parameter=multiple is not None and
                              mod(la2-sp.eye(2)-multiple*nil, p) == sp.zeros(2),
                          character_trivial=all(word(w, chars, p) == sp.eye(1) for w in peripheral),
                          character_relators=all(word(w, chars, p) == sp.eye(1) for w in rels)),
                V=a, dual=b, pair=pair_identities(a, b),
                inverse_character=inverse_character,
                untwisted_pair=pair_identities(un, und),
                cup_V=image_cup(a, pairing, p), cup_dual=image_cup(b, inverse(pairing, p), p),
                invalid_mutation=invalid)


def lift_and_duality_controls():
    p = 13
    a = sp.Matrix([[0, -1], [1, 0]])
    j = sp.Matrix([[0, 1], [-1, 0]])
    u = sp.Matrix([[1, 1], [0, 1]])
    ud = inverse(u, p).T
    minus_identity = mod(word('aa', {'a': mod(a, p)}, p), p)
    return dict(psl_relator=minus_identity,
                not_honest_sl2=minus_identity != sp.eye(2),
                odd_power_relator=mod(sym_power(a, 3, p)**2, p),
                even_power_relator=mod(sym_power(a, 2, p)**2, p),
                literal_dual_inequality=u != ud,
                actual_self_duality=mod(j*u-ud*j, p) == sp.zeros(2) and rank(j, p) == 2,
                characteristic_three_degree_three_trace=3 % 3,
                characteristic_thirteen_degree_six_invertible=pow(6, -1, 13))


def serial(x):
    if isinstance(x, sp.MatrixBase):
        return [[serial(a) for a in row] for row in x.tolist()]
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [serial(a) for a in x]
    if isinstance(x, sp.Integer):
        return int(x)
    if isinstance(x, sp.Basic):
        return str(x)
    return x


def run():
    print(json.dumps(dict(part='environment', python=platform.python_version(), sympy=sp.__version__)), flush=True)
    for m in range(7):
        r = bochner(m)
        print(json.dumps(dict(part='bochner', result=serial(r))), flush=True)
        assert r['sl2_relations'] and r['e_adjoint_is_f'] and r['y_hermitian']
        assert all(v['hermitian'] and (v['zero'] if m == 0 else v['strictly_positive']) for v in r['degrees'])
    for degree in (1, 2, 3, 4, 6):
        r = circle_transfer(degree)
        print(json.dumps(dict(part='transfer', result=serial(r))), flush=True)
        assert r['pullback_chain'] and r['trace_chain'] and r['trace_pullback'] == degree
        assert r['projector'] and r['projector_rank'] == 1 and r['wrong_character_pullback_rejected']
    print(json.dumps(dict(part='rank_jump', result=rank_jump())), flush=True)
    assert [r['restriction_rank'] for r in rank_jump()] == [1, 0]
    r = lift_and_duality_controls()
    print(json.dumps(dict(part='scope_controls', result=serial(r))), flush=True)
    assert r['not_honest_sl2'] and r['odd_power_relator'] == mod(-sp.eye(4))
    assert r['even_power_relator'] == sp.eye(3) and r['literal_dual_inequality'] and r['actual_self_duality']
    r = finite_field_witness()
    print(json.dumps(dict(part='finite_field', result=serial(r))), flush=True)
    assert r['pair']['index'] == 1 and all(r['pair']['identities'].values()) and r['pair']['domain_equalities']
    assert r['generated_algebra_dimension'] == 16 and r['intertwiner_dimension'] == 0 and r['trace_obstruction']
    assert r['base_pairing_invariant'] and r['inverse_character_intertwines_dual'] and r['invalid_mutation']
    assert r['cusp']['nilpotent_square'] == sp.zeros(2) and r['cusp']['mu_nontrivial']
    assert r['cusp']['one_parameter'] and r['cusp']['character_trivial'] and r['cusp']['character_relators']
    assert r['inverse_character']['n'] == r['dual']['n'] and r['untwisted_pair']['index'] == 0
    assert r['cup_V']['rank'] == 0 and r['cup_dual']['rank'] == 2
    print(json.dumps(dict(part='conclusion', result='Exact finite controls pass; theorem and physical scope are separate.')), flush=True)


if __name__ == '__main__':
    run()
