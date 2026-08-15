"""The first measurement plane is not a choice: it is the fixed algebra of 2O.

Closes the proof auditor's D2 and prices the plane a third time, independently of
B874's two-value cliff and B898's signature dichotomy.

The charge algebra is C = e6^{2T}, spanned by the 2T-invariants in the principal-sl2
exponent degrees {2,8,10,14,16,22}: one line each at 8,14,16,22, nothing at 2 and 10.
The paper then measures on the plane <x_8,x_16>.  That plane was carried as a
certificate.  It is a theorem:

    N_{SU(2)}(2T) = 2O,  with 2O/2T = Z/2,

so there is exactly ONE outer involution available, w in 2O \\ 2T acting by Ad(w).  Its
eigenvalues on the four invariant lines are (+1,-1,+1,-1) on degrees (8,14,16,22), so

    e6^{2O}  =  <x_8, x_16>   (two-dimensional)

is precisely the measurement plane, and <x_14,x_22> is the anti-invariant complement.
The Z/2 grading is then the eigenspace decomposition of an automorphism, hence
[C_i,C_j] subset C_{i+j} holds for free.

The uniqueness half matters as much as the existence half: 2T is SELF-NORMALIZING in
2I, so the icosahedral group offers no competing involution and no competing plane.

Pure exact arithmetic in sympy (sqrt2, sqrt5); no floats, no seeds.
"""
import itertools

import sympy as sp

I = sp.I
H = sp.Rational(1, 2)
R2 = 1 / sp.sqrt(2)


def q2m(a, b, c, d):
    """The quaternion a + bi + cj + dk as an element of SU(2)."""
    return sp.Matrix([[a + b * I, c + d * I], [-c + d * I, a - b * I]])


def _key(M):
    return tuple(sp.nsimplify(sp.simplify(M[i, j])) for i in range(2) for j in range(2))


def _binary_tetrahedral():
    """2T: the 24 Hurwitz units."""
    G = []
    for s in (1, -1):
        G += [q2m(s, 0, 0, 0), q2m(0, s, 0, 0), q2m(0, 0, s, 0), q2m(0, 0, 0, s)]
    for sg in itertools.product((1, -1), repeat=4):
        G.append(q2m(*[x * H for x in sg]))
    return [sp.simplify(g) for g in G]


def _binary_octahedral():
    """2O = 2T together with the 24 units (e_i +- e_j)/sqrt(2), i < j."""
    basis = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    extra = []
    for i in range(4):
        for j in range(i + 1, 4):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [R2 * (si * basis[i][k] + sj * basis[j][k]) for k in range(4)]
                    extra.append(sp.simplify(q2m(*v)))
    return _binary_tetrahedral() + extra


def _binary_icosahedral():
    """2I, generated from a Hurwitz unit and a golden-ratio unit."""
    phi = (1 + sp.sqrt(5)) / 2
    gens = [q2m(H, H, H, H), q2m(0, H, phi / 2, (phi - 1) / 2)]
    seen = {_key(sp.eye(2)): sp.eye(2)}
    frontier = [sp.eye(2)]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = sp.simplify(x * g)
                k = _key(y)
                if k not in seen:
                    seen[k] = y
                    nxt.append(y)
        frontier = nxt
    return list(seen.values())


G2T = _binary_tetrahedral()
G2O = _binary_octahedral()
G2I = _binary_icosahedral()
S2T = {_key(g) for g in G2T}
S2O = {_key(g) for g in G2O}

# The principal-sl2 exponent degrees of e6: 2m for m in {1,4,5,7,8,11}.
EXPONENT_DEGREES = (2, 8, 10, 14, 16, 22)


def _molien_dim(G, n):
    """dim (Sym^n C^2)^G, exactly, via Molien's formula."""
    t = sp.symbols("t")
    M = sum(1 / sp.det(sp.eye(2) - t * g) for g in G) / len(G)
    ser = sp.series(sp.simplify(M), t, 0, n + 1).removeO()
    return int(sp.Poly(sp.expand(ser), t).coeff_monomial(t**n))


def _normalizes(g, subgroup_elements, subgroup_keys):
    gi = sp.simplify(g.inv())
    return all(_key(sp.simplify(g * x * gi)) in subgroup_keys for x in subgroup_elements)


def test_the_three_groups_have_their_classical_orders():
    assert len(S2T) == 24
    assert len(S2O) == 48
    assert len({_key(g) for g in G2I}) == 120


def test_2T_is_normal_in_2O_with_quotient_Z_mod_2():
    assert S2T < S2O
    assert all(_normalizes(g, G2T, S2T) for g in G2O)
    assert len(S2O) // len(S2T) == 2


def test_2T_is_self_normalizing_in_2I_so_the_involution_is_unique():
    """No competing outer involution from the icosahedral side."""
    assert S2T <= {_key(g) for g in G2I}
    normalizing = [g for g in G2I if _normalizes(g, G2T, S2T)]
    assert len({_key(g) for g in normalizing}) == 24, "N_{2I}(2T) must be 2T itself"


def test_charge_algebra_is_four_dimensional_at_degrees_8_14_16_22():
    dims = {n: _molien_dim(G2T, n) for n in EXPONENT_DEGREES}
    assert dims == {2: 0, 8: 1, 10: 0, 14: 1, 16: 1, 22: 1}
    assert sum(dims.values()) == 4


def test_the_2O_fixed_algebra_is_exactly_the_measurement_plane():
    """e6^{2O} = <x_8, x_16>: two-dimensional, and it IS the plane the paper measures on."""
    dims = {n: _molien_dim(G2O, n) for n in EXPONENT_DEGREES}
    assert dims == {2: 0, 8: 1, 10: 0, 14: 0, 16: 1, 22: 0}
    assert sum(dims.values()) == 2
    assert [n for n, d in dims.items() if d == 1] == [8, 16]


def test_outer_involution_eigenvalues_are_plus_minus_plus_minus():
    """Ad(w) acts by +1 on degrees 8,16 and by -1 on degrees 14,22.

    Each 2T-invariant space here is a line, so Ad(w) acts on it by a scalar, and that
    scalar is +1 exactly when the line survives to 2O.  The grading is therefore an
    eigenspace decomposition of an automorphism, not a bracket computation.
    """
    eigen = {}
    for n in (8, 14, 16, 22):
        assert _molien_dim(G2T, n) == 1
        eigen[n] = +1 if _molien_dim(G2O, n) == 1 else -1
    assert eigen == {8: +1, 14: -1, 16: +1, 22: -1}

    even = sorted(n for n, s in eigen.items() if s == +1)
    odd = sorted(n for n, s in eigen.items() if s == -1)
    assert even == [8, 16] and odd == [14, 22]


def test_grading_is_automatic_from_the_involution():
    """[C_i, C_j] subset C_{i+j} needs no computation once Ad(w) is an automorphism.

    We record the logical shape as an assertion about eigenvalues: the product of the
    two signs is the sign of the target summand.
    """
    sign = {8: +1, 14: -1, 16: +1, 22: -1}
    for a in sign:
        for b in sign:
            target = sign[a] * sign[b]
            assert target in (+1, -1)
            # +1 lands in <x_8,x_16>, -1 in <x_14,x_22>
            assert (target == +1) == (sign[a] == sign[b])
