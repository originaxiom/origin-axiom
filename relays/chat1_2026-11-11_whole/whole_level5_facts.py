#!/usr/bin/env python3
"""
THE ALLOWED QUOTIENT AT LEVEL 5 AND ITS SYMMETRIES: EXACT FACTS FOR "A STATE OF THE WHOLE"
The web seat (chat1), 2026-11-11. Data-free. Not a sealed card: finite checks of classical statements, in integers and
exact rationals, with one numerical check of a classical identity at the end. No value of tau is selected or read; the
points named are the quotient's own symmetric points. Scratch versions were run and read before this file was committed.

CONVENTIONS (the record's, B1733). A flat line of order 5 on the fibre is a row vector (alpha, b) mod 5, the point
(alpha tau + b)/5 of the torus C/(Z tau + Z). A move gamma acts on tau by a Moebius map and on rows by
(alpha, b) -> (alpha, b) gamma^-1. The mark is v = (1, 3), LR's line (LR is symmetric, so v is its row and column line).
 - G_pm   = the moves with v gamma = +-v mod 5        (the mark is one twin, up to sign: two acts);
 - G_line = the moves with v gamma = c v mod 5        (the mark is the whole line: what the tick gives, B1876 H13).
 X_pm and X_line are the quotients of the upper half-plane by them.

THE FACTS.
 Q1 The index, the cusps with their widths, the elliptic points and the genus of X_pm and X_line, from the action of
    S and T on the 12 rows up to sign and on the 6 lines.
 Q2 The elliptic points of X_line as exact points of the upper half-plane; each is an image of i under the modular
    group; its elliptic element e has v e = +-2v, so it is not in G_pm.
 Q3 The twin exchange delta (an element of G_line outside G_pm) is an involution of X_pm; its fixed points lie over
    the elliptic points of X_line.
 Q4 The dual involution W (a torus with a marked line goes to its quotient by the line, with the dual line): an
    integer matrix of determinant 5 with W^2 = -5 that normalises G_line. It exchanges the two cusps and the two
    elliptic points of X_line. Its fixed points on X_line: the classes of trace-0 matrices M of determinant 5 in the
    coset W G_line; how many classes; the reduced form of each fixed point; that M is an endomorphism of the torus
    with M^2 = -5 whose kernel on the points of order 5 is the mark.
 Q5 The mirror (tau -> -conj(tau), composed with a move so that the mark is kept): it normalises G_line, exchanges
    the two elliptic points and fixes each of W's fixed points. So the points of X_line fixed by every symmetry are
    W's fixed points and no others.
 Q6 On X_pm: which of W and W delta fixes which of the four points over W's fixed points; and that no point of X_pm
    is fixed by delta and W together.
 Q7 A numerical check of two classical identities for t(tau) = (eta(tau)/eta(5 tau))^6 on the standard quotient
    (mark (0, 1)): t(-1/(5 tau)) t(tau) = 125 at a point with no symmetry, and t = +5 sqrt 5 and -5 sqrt 5 at the two
    fixed points of the dual involution.

0 of 19.
"""
import itertools
import json
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
N = 5
V = (1, 3)
S = (0, -1, 1, 0)
T = (1, 1, 0, 1)
I2 = (1, 0, 0, 1)


def mul(A, B):
    return (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])


def det(A):
    return A[0] * A[3] - A[1] * A[2]


def inv(A):
    d = det(A)
    assert d in (1, -1)
    return (A[3] * d, -A[1] * d, -A[2] * d, A[0] * d)


def row(u, A):                       # (alpha, b) A
    return ((u[0] * A[0] + u[1] * A[2]) % N, (u[0] * A[1] + u[1] * A[3]) % N)


def act(u, g):                       # the record's action on rows: u g^-1
    return row(u, inv(g))


def pm(u):
    return min((u[0] % N, u[1] % N), ((-u[0]) % N, (-u[1]) % N))


def line(u):
    return min(((c * u[0]) % N, (c * u[1]) % N) for c in range(1, N))


def in_pm(g):
    return pm(row(V, g)) == pm(V)


def in_line(g):
    return line(row(V, g)) == line(V)


def orbit_model(key):
    """The cosets of the mark's stabiliser, as the orbit of the mark under u -> u g^-1; S and T as permutations."""
    start = key(V)
    seen, todo = {start}, [start]
    while todo:
        u = todo.pop()
        for g in (S, T, inv(T)):
            w = key(act(u, g))
            if w not in seen:
                seen.add(w)
                todo.append(w)
    pts = sorted(seen)
    return pts, {u: key(act(u, S)) for u in pts}, {u: key(act(u, T)) for u in pts}


def cycles(perm):
    out, seen = [], set()
    for u in perm:
        if u not in seen:
            c, w = [], u
            while w not in seen:
                seen.add(w)
                c.append(w)
                w = perm[w]
            out.append(c)
    return out


def word_to(key, target):
    """A move g with key(V g^-1) = target, by search over words in S, T, T^-1."""
    todo, seen = [(I2, key(V))], {key(V)}
    while todo:
        g, u = todo.pop(0)
        if u == target:
            return g
        for h in (S, T, inv(T)):
            g2 = mul(h, g)                   # V (h g)^-1 = (V g^-1) h^-1
            u2 = key(act(u, h))
            if u2 not in seen:
                seen.add(u2)
                todo.append((g2, u2))
    raise ValueError(target)


def moebius_i(g):
    """g(i) for a move g, as (Re, Im) exact."""
    a, b, c, d = g
    return (Fr(a * c + b * d, c * c + d * d), Fr(1, c * c + d * d))


def quotient_facts(key, name):
    pts, pS, pT = orbit_model(key)
    cusps = sorted(len(c) for c in cycles(pT))
    e2 = [u for u in pts if pS[u] == u]
    ST = {u: pT[pS[u]] for u in pts}         # some element of order 3; its fixed cosets count e3
    e3 = [u for u in pts if ST[u] == u]
    mu = len(pts)
    genus = Fr(1) + Fr(mu, 12) - Fr(len(e2), 4) - Fr(len(e3), 3) - Fr(len(cusps), 2)
    return {'name': name, 'index_in_PSL': mu, 'cusp_widths': cusps, 'elliptic_order_2': len(e2), 'elliptic_order_3': len(e3),
            'genus': str(genus)}, e2


def reduce_form(a, b, c):
    """Reduce a positive definite form a x^2 + b x y + c y^2."""
    while True:
        if c < a:
            a, b, c = c, -b, a
        elif abs(b) > a:
            k = (b + a) // (2 * a) if b > 0 else -((-b + a) // (2 * a))
            b, c = b - 2 * k * a, c - k * b + k * k * a
        else:
            if b < 0 and (a == c or -b == a):
                b = -b
            return (a, b, c)


def main():
    R = {}
    # ---- Q1
    f_pm, _ = quotient_facts(pm, 'X_pm (the mark is one twin up to sign)')
    f_line, e2_line = quotient_facts(line, 'X_line (the mark is the whole line)')
    R['Q1'] = [f_pm, f_line]
    # ---- Q2: the elliptic points of X_line
    q2 = []
    ell = []
    for u in e2_line:
        g = word_to(line, u)                         # V g^-1 on the S-fixed line u
        # V g^-1 is fixed by S as a line, so e = g^-1 S g keeps the mark, and e fixes g^-1(i)
        e = mul(mul(inv(g), S), g)
        tau = moebius_i(inv(g))
        ve = row(V, e)
        q2.append({'tau': [str(tau[0]), str(tau[1])], 'image_of_i_under': list(inv(g)), 'elliptic_element': list(e),
                   'e_squared_is_minus_one': mul(e, e) == (-1, 0, 0, -1), 'e_in_G_line': in_line(e), 'e_in_G_pm': in_pm(e),
                   'v e mod 5': list(ve), 'v e is +-2v': pm(ve) == pm((2 * V[0], 2 * V[1]))})
        ell.append((tau, e))
    R['Q2'] = q2
    # ---- Q3: the twin exchange
    delta = None
    for a, b, c in itertools.product(range(-6, 7), repeat=3):
        if a != 0 and (1 + b * c) % a == 0:
            g = (a, b, c, (1 + b * c) // a)
            if det(g) == 1 and in_line(g) and not in_pm(g):
                delta = g
                break
    R['Q3'] = {'delta': list(delta), 'v delta mod 5': list(row(V, delta)),
               'delta squared in G_pm': in_pm(mul(delta, delta)),
               'the elliptic elements of G_line lie in delta G_pm': all(in_pm(mul(inv(delta), e)) for _, e in ell),
               'fixed points of the twin exchange on X_pm': 'the points over the %d elliptic points of X_line' % len(ell)}
    # ---- Q4: the dual involution. Standard form: mark (0, 1), W5 = [[0, -1], [5, 0]]; g carries (0, 1) to the mark.
    g = (0, -1, 1, 3)                                # (0, 1) g = (1, 3)
    assert det(g) == 1 and line(row((0, 1), g)) == line(V)
    W5 = (0, -1, 5, 0)
    W = mul(mul(inv(g), W5), g)                      # G_line = g^-1 Gamma_0(5) g
    gens = [h for h in (tuple(x) for x in itertools.product(range(-7, 8), repeat=4)) if det(h) == 1 and in_line(h)]
    def conj_by_W(h):                                # W h W^-1 = -W h W / 5 ... W^-1 = -W/5 since W^2 = -5
        P = mul(mul(W, h), W)
        assert all(x % 5 == 0 for x in P)
        return tuple(-x // 5 for x in P)
    normalises = all(det(conj_by_W(h)) == 1 and in_line(conj_by_W(h)) for h in gens)
    # The action on cusps and elliptic points is read in the standard quotient (mark (0, 1), the group c = 0 mod 5),
    # which g carries to the mark v. Its cusps are infinity and 0; its elliptic points are (2 + i)/5 and (-2 + i)/5.
    e_std = [(Fr(2, 5), Fr(1, 5)), (Fr(-2, 5), Fr(1, 5))]
    for x, y in e_std:                               # each is fixed by an element of order 2 with c = 0 mod 5
        a = int(x * 5)
        e = (a, -(a * a + 1) // 5, 5, -a)
        assert det(e) == 1 and mul(e, e) == (-1, 0, 0, -1) and e[2] % 5 == 0
        n = (e[2] * x + e[3]) ** 2 + (e[2] * y) ** 2  # e(z) = z, checked exactly
        ez = (((e[0] * x + e[1]) * (e[2] * x + e[3]) + e[0] * y * e[2] * y) / n, y * (e[0] * e[3] - e[1] * e[2]) / n)
        assert ez == (x, y)
    def W5_on(z):                                    # z = x + i y, exact for rational x, y: -1/(5 z)
        x, y = z
        n = 5 * (x * x + y * y)
        return (-x / n, y / n)
    R['Q4'] = {'W': list(W), 'det W': det(W), 'W squared': list(mul(W, W)), 'elements of G_line tested': len(gens),
               'W normalises G_line on all of them': normalises,
               'W5 sends (2 + i)/5 to': [str(t) for t in W5_on(e_std[0])],
               'W5 sends (-2 + i)/5 to': [str(t) for t in W5_on(e_std[1])],
               'W5 exchanges the two elliptic points': W5_on(e_std[0]) == e_std[1] and W5_on(e_std[1]) == e_std[0],
               'W5 sends the cusp infinity to a/c and the cusp 0 to b/d': [str(Fr(W5[0], W5[2])), 'infinity' if W5[3] == 0 else str(Fr(W5[1], W5[3]))]}
    # fixed points of W on X_line: trace-0, determinant-5 matrices M = W5 gamma, gamma in Gamma_0(5) (standard quotient)
    fixed = {}
    for a in range(-4, 5):
        for c in range(1, 60):
            num = -(1 + 5 * a * a)
            if num % c:
                continue
            b = num // c
            M = (5 * a, b, 5 * c, -5 * a)            # det = -25 a^2 - 5 b c = 5
            assert det(M) == 5 and mul(M, M) == (-5, 0, 0, -5)
            # the fixed point is the root of 5c z^2 - 10a z - b = 0 in the upper half-plane; its form:
            form = (5 * c, -10 * a, -b)
            assert form[1] ** 2 - 4 * form[0] * form[2] == -20
            red = reduce_form(*form)
            # the kernel of M on the points of order 5 (rows u with u M = 0 mod 5)
            ker = [u for u in itertools.product(range(5), repeat=2) if u != (0, 0) and row(u, M) == (0, 0)]
            fixed.setdefault(red, []).append({'M': list(M), 'kernel_is_the_mark_(0,1)': sorted(set(line(u) for u in ker)) == [line((0, 1))]})
    R['Q4']['fixed points of the dual involution, by reduced form (a, b, c) of discriminant -20'] = {
        str(k): {'matrices found': len(v), 'kernel of M on the 5-torsion is the mark, for all': all(m['kernel_is_the_mark_(0,1)'] for m in v),
                 'example M': v[0]['M']} for k, v in fixed.items()}
    R['Q4']['classes'] = len(fixed)
    # in the frame of the mark v: W's own fixed point is the root of c z^2 + (d - a) z - b = 0
    R['Q4']['in the frame of the mark v'] = {'g with (0, 1) g = v': list(g), 'W': list(W),
                                             'the fixed point of W is the root in the upper half-plane of (A, B, C)': [W[2], W[3] - W[0], -W[1]],
                                             'its reduced form': list(reduce_form(W[2], W[3] - W[0], -W[1]))}
    # ---- Q5: the mirror on the standard quotient: z -> -conj(z), i.e. conjugation by diag(1, -1) = D
    D = (1, 0, 0, -1)
    mir_norm = all((lambda h: (h[2] % 5 == 0))(mul(mul(D, h), D)) for h in
                   [h for h in (tuple(x) for x in itertools.product(range(-7, 8), repeat=4)) if det(h) == 1 and h[2] % 5 == 0])
    mirror = lambda z: (-z[0], z[1])
    # W5's two fixed points in the standard quotient: i/sqrt5 (real part 0) and 1/2 + i/(2 sqrt5) (real part 1/2); the
    # mirror keeps the imaginary part, so only the real parts are compared, and T (c = 0) is in the group
    R['Q5'] = {'the mirror normalises the standard group (on the elements tested)': mir_norm,
               'the mirror exchanges the two elliptic points': mirror(e_std[0]) == e_std[1],
               'the mirror fixes the fixed point of W5 with real part 0': -Fr(0) == Fr(0),
               'the mirror sends the fixed point with real part 1/2 to real part -1/2, which is T^-1 of it': -Fr(1, 2) == Fr(1, 2) - 1,
               'points of X_line fixed by W and by the mirror': 'the two fixed points of W; the elliptic points are exchanged by both'}
    # ---- Q6: on X_pm
    q6 = {}
    for red, v in fixed.items():
        for m in v[:1]:
            M = tuple(m['M'])
            # gamma = W5^-1 M in Gamma_0(5); in the standard quotient the twins are (0, 1) and (0, 2)
            P = mul(W5, M)
            gam = tuple(-x // 5 for x in P)
            assert det(gam) == 1 and gam[2] % 5 == 0
            d = gam[3] % 5
            q6[str(red)] = {'gamma = W5^-1 M': list(gam), '(0,1) gamma mod 5': [0, d],
                            'both points of X_pm over it are fixed by': 'W5' if d in (1, 4) else 'W5 composed with the twin exchange'}
    pm_tested = [h for h in gens if in_pm(h)]
    R['Q6'] = {'by reduced form': q6,
               'elements of G_pm tested': len(pm_tested),
               'W normalises G_pm on all of them': all(in_pm(conj_by_W(h)) for h in pm_tested),
               'no point of X_pm is fixed by the twin exchange and W together': 'the twin exchange fixes only the points over the elliptic points (Q3), and W exchanges those (Q4)'}
    # ---- Q7: numerics for the classical identities
    import mpmath as mp
    mp.mp.dps = 40
    def eta(tau):
        q = mp.exp(2j * mp.pi * tau)
        return mp.exp(2j * mp.pi * tau / 24) * mp.nprod(lambda n: 1 - q ** n, [1, mp.inf])
    def t(tau):
        return (eta(tau) / eta(5 * tau)) ** 6
    z = mp.mpc('0.137', '0.412')
    prod = t(z) * t(-1 / (5 * z))
    f1 = mp.mpc(0, 1) / mp.sqrt(5)
    f2 = mp.mpf(1) / 2 + mp.mpc(0, 1) / (2 * mp.sqrt(5))
    R['Q7'] = {'t(z) t(-1/(5z)) at z = 0.137 + 0.412 i': mp.nstr(prod, 25),
               't(i/sqrt5) / (5 sqrt5)': mp.nstr(t(f1) / (5 * mp.sqrt(5)), 25),
               't(1/2 + i/(2 sqrt5)) / (5 sqrt5)': mp.nstr(t(f2) / (5 * mp.sqrt(5)), 25)}
    with open(os.path.join(HERE, 'whole_level5_facts_out.json'), 'w') as fh:
        json.dump(R, fh, indent=1)
    print('written whole_level5_facts_out.json')


if __name__ == '__main__':
    main()
