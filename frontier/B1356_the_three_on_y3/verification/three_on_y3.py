#!/usr/bin/env python3
"""B1356 — the three on Y_3: the deck's fixed circle, the descent's forced local model, the charge lattice.

Stage A  (exact, rationals).  Y_3 = the Hantzsche-Wendt flat manifold R^3/Pi, Pi = P2_1 2_1 2_1 (ITA #19), with the
          deck sigma = the cyclic permutation (x,y,z) -> (z,x,y).  sigma normalises Pi; the extended group
          Pi^ = <Pi, sigma> is P2_1 3 (ITA #198) with point group T = A_4 = 2T/{+-1}.  We compute the fixed set of
          sigma on Y_3 (expected: exactly one closed geodesic, the lift of the branch knot), the torsion of Pi^
          (expected: only 3-fold rotations — every order-2 element is a 2_1 screw), and the number of singular
          circles of the orbifold R^3/Pi^ (expected: one — S^3 with the figure-eight as its 2pi/3 cone circle).

Stage B  (exact, Hurwitz quaternions; octonions for the G_2 form).  The local model of the descent along the knot:
          the SO(4) = Sp(1).Sp(1) inside G_2 acts on Im H + H; the E_6 fibre group is the 2T acting trivially on
          Im H; the deck at a point of the fixed circle is an element (l, r) rotating the normal plane e^perp of the
          circle by 2pi/3 and normalising the fibre group.  We enumerate the admissible (l, r) (r in 2O with r^3 in 2T
          forces r in 2T), generate the local group G on e^perp + H = C^3, verify |G| = 72 and G = 2T x Z_3 with the
          Z_3 the centre of SU(3), compute the strata (E_6 plane, two A_2 planes, the isolated origin), the McKay
          ages of the 21 conjugacy classes (b_2 = #age 1, b_4 = #age 2 of the crepant resolution), and check the
          non-compact divisor count b_2 - b_4 = 6 + 2 + 2.

Stage C  (exact).  The sum-rule lattice: Z^3 as the permutation module of the deck; the sum-zero sublattice A_2 has
          no invariants; the coset (1,1,-2) + 3A_2 = {sum 0, all = 1 mod 3}; the deck orbit of (1,1,-2) is an
          equilateral triangle = 3 x the weights of the 3-bar of the SU(3) whose Weyl group permutes the apexes.

Stage D  (exact).  On S^4/Gamma the element of the stabiliser of an E_6 point acting as -1 on the tangent space is
          diag(-1,-1,-1,-1,1) in O(5): it fixes the antipode too.  On CP^2 the point stabiliser U(2) meets the
          twistor-trivial group in the scalars only (2T cap U(1) = {+-1}): no E_6 point on any CP^2/Gamma.
"""
from fractions import Fraction as Fr
import itertools, sys
import numpy as np

# ----------------------------------------------------------------------------------------------------------------
# Stage A — the flat model
# ----------------------------------------------------------------------------------------------------------------
def frac_vec(*xs):
    return tuple(Fr(x) for x in xs)

def matvec(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(3)) for i in range(3))

def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def compose(g, h):
    """(A,t) o (B,s) : v -> A(Bv + s) + t."""
    A, t = g; B, s = h
    return (matmul(A, B), tuple(a + b for a, b in zip(matvec(A, s), t)))

def inverse(g):
    A, t = g
    # A is a signed permutation matrix: inverse = transpose
    At = tuple(tuple(A[j][i] for j in range(3)) for i in range(3))
    return (At, tuple(-x for x in matvec(At, t)))

def reduce_mod1(v):
    return tuple(x - (x.numerator // x.denominator) for x in v)

def op_from_string(s):
    """'-x+1/2, -y, z+1/2' -> (A, t) with A a signed permutation matrix."""
    A = [[Fr(0)] * 3 for _ in range(3)]
    t = [Fr(0)] * 3
    for i, comp in enumerate(s.split(',')):
        comp = comp.replace(' ', '')
        sign = 1
        j = 0
        while j < len(comp):
            c = comp[j]
            if c == '+':
                sign = 1; j += 1
            elif c == '-':
                sign = -1; j += 1
            elif c in 'xyz':
                A[i]['xyz'.index(c)] += sign; sign = 1; j += 1
            else:
                k = j
                while k < len(comp) and (comp[k].isdigit() or comp[k] == '/'):
                    k += 1
                t[i] += sign * Fr(comp[j:k]); sign = 1; j = k
    return (tuple(tuple(r) for r in A), tuple(t))

P19 = ["x,y,z", "-x+1/2,-y,z+1/2", "-x,y+1/2,-z+1/2", "x+1/2,-y+1/2,-z"]                # Pi = P2_1 2_1 2_1 mod Z^3
P198 = P19 + ["z,x,y", "z+1/2,-x+1/2,-y", "-z+1/2,-x,y+1/2", "-z,x+1/2,-y+1/2",
              "y,z,x", "-y,z+1/2,-x+1/2", "y+1/2,-z+1/2,-x", "-y+1/2,-z,x+1/2"]          # Pi^ = P2_1 3 mod Z^3

def key(g):
    A, t = g
    return (A, reduce_mod1(t))

def closure_mod_lattice(ops):
    S = {key(g): g for g in ops}
    changed = True
    while changed:
        changed = False
        for g in list(S.values()):
            for h in list(S.values()):
                k = key(compose(g, h))
                if k not in S:
                    S[k] = (k[0], k[1]); changed = True
    return S

def stage_A():
    print("=" * 100)
    print("STAGE A — the flat model: Y_3 = R^3/Pi (Hantzsche-Wendt), the deck sigma, the orbifold R^3/Pi^")
    print("=" * 100)
    Pi = [op_from_string(s) for s in P19]
    Pih = [op_from_string(s) for s in P198]
    S19 = closure_mod_lattice(Pi); S198 = closure_mod_lattice(Pih)
    print(f"Pi mod Z^3 closes with {len(S19)} elements (point group V_4: {len(S19) == 4}); "
          f"Pi^ mod Z^3 closes with {len(S198)} elements (point group T = A_4: {len(S198) == 12})")
    sigma = op_from_string("z,x,y")
    # sigma normalises Pi
    ok = all(key(compose(compose(sigma, g), inverse(sigma))) in S19 for g in Pi)
    print(f"sigma = (x,y,z) -> (z,x,y) normalises Pi: {ok}; sigma^3 = 1: "
          f"{key(compose(sigma, compose(sigma, sigma))) == key(Pi[0])}")
    # Pi is torsion-free (every non-identity op is a screw: translation component along the axis is never 0 mod Z)
    # and Pi^'s torsion = the 3-fold rotations only.
    def axis_of(A):
        M = np.array([[float(x) for x in r] for r in A])
        w, v = np.linalg.eig(M)
        i = [k for k in range(3) if abs(w[k] - 1) < 1e-9]
        if not i:
            return None
        a = np.real(v[:, i[0]]); a = a / np.max(np.abs(a))
        return tuple(Fr(round(x)) for x in a)   # axes are (+-1,+-1,+-1) or coordinate axes here
    def order_of_linear(A):
        M = A; I = tuple(tuple(Fr(int(i == j)) for j in range(3)) for i in range(3))
        for n in range(1, 7):
            if M == I:
                return n
            M = matmul(M, A)
        return None
    print("\nTorsion census of Pi^ (an element (A, t+n), n in Z^3, has a fixed point iff the axis component of t+n is 0):")
    n3 = 0; n2_rot = 0; n2_screw = 0
    for k, g in S198.items():
        A, t = g
        o = order_of_linear(A)
        if o == 1:
            continue
        a = axis_of(A)
        # axis component of t + n: a.(t+n) = a.t + a.n, a.n ranges over Z (a primitive integer vector) -> vanishes for
        # some n iff a.t is an integer.
        at = sum(x * y for x, y in zip(a, t))
        has_fixed = (at.denominator == 1)
        if o == 2:
            if has_fixed: n2_rot += 1
            else: n2_screw += 1
        elif o == 3:
            n3 += 1
            assert has_fixed, "a 3_1 screw would break the count"
    print(f"  order-2 linear parts: {n2_screw} screws (2_1), {n2_rot} rotations  -> Pi torsion-free and no 2-fold cone "
          f"axes: {n2_rot == 0 and n2_screw == 3}")
    print(f"  order-3 linear parts: {n3} cosets, all pure rotations (3-fold cone axes): {n3 == 8}")

    # Fixed set of sigma on Y_3 = T^3/V_4: solve  P v = A v + t  (mod Z^3)  for (A,t) in Pi mod Z^3.
    P = sigma[0]
    print("\nFixed set of sigma on Y_3: for each coset (A,t) of Pi the solutions of (P - A) v = t mod Z^3 on T^3")
    comps = []   # (coset index, base point, direction) — each is a circle on T^3
    for idx, (k, g) in enumerate(S19.items()):
        A, t = g
        M = tuple(tuple(P[i][j] - A[i][j] for j in range(3)) for i in range(3))
        Mnp = np.array([[int(x) for x in r] for r in M])
        # Smith normal form by hand for a 3x3 integer matrix of rank 2: compute kernel direction and the torsion of coker
        rank = np.linalg.matrix_rank(Mnp)
        assert rank == 2, rank
        # kernel direction (integer)
        from sympy import Matrix
        Ms = Matrix([[int(x) for x in r] for r in M])
        ker = Ms.nullspace()[0]
        ker = ker / max(abs(x) for x in ker); ker = [Fr(str(x)) for x in ker]
        # solutions v of M v = t + n, n in Z^3: the solution set on the torus is (# of n classes giving distinct
        # circles) circles.  Count: torsion of coker(M restricted to the lattice) — Smith invariants d1, d2 -> d1*d2
        # circles if t lies in the image... we simply brute force n in a box and dedupe circles mod Z^3.
        circles = set()
        for n in itertools.product(range(-2, 3), repeat=3):
            rhs = [t[i] + n[i] for i in range(3)]
            # solve M v = rhs over Q (least squares exact: pick two independent rows)
            sol = None
            for rows in itertools.combinations(range(3), 2):
                sub = Matrix([[int(M[r][c]) for c in range(3)] for r in rows])
                # need a 2x2 invertible block
                for cols in itertools.combinations(range(3), 2):
                    blk = sub[:, list(cols)]
                    if blk.det() != 0:
                        free = [c for c in range(3) if c not in cols][0]
                        # set v[free] = 0 and solve
                        b = Matrix([rhs[r] for r in rows])
                        x = blk.solve(b)
                        v = [Fr(0)] * 3
                        v[cols[0]] = Fr(str(x[0])); v[cols[1]] = Fr(str(x[1]))
                        # verify the third equation
                        if all(sum(M[i][j] * v[j] for j in range(3)) == rhs[i] for i in range(3)):
                            sol = v
                        break
                if sol is not None:
                    break
            if sol is None:
                continue
            # canonical representative of the circle {sol + s*ker} mod Z^3: reduce sol mod Z^3 and mod the direction
            # (choose the point with the free coordinate == 0 along ker if possible)
            # project out the kernel direction: pick coordinate c with ker[c] != 0, shift sol so that sol[c] = 0
            c = [i for i in range(3) if ker[i] != 0][0]
            s = -sol[c] / ker[c]
            base = reduce_mod1(tuple(sol[i] + s * ker[i] for i in range(3)))
            # but shifting by lattice vectors along the circle changes base: the circle mod Z^3 closes after the
            # kernel direction's lattice period; base points differing by multiples of (ker period)/... dedupe by
            # sampling: two circles coincide iff base' - base is in Z^3 + R*ker  ->  test with a projection onto ker^perp
            circles.add(base)
        # dedupe circles: same circle iff difference in Z^3 + R ker.  Use the invariant: components orthogonal to ker
        # modulo the projected lattice.  Brute force: compare each pair.
        def same_circle(b1, b2):
            d = [b1[i] - b2[i] for i in range(3)]
            for n in itertools.product(range(-3, 4), repeat=3):
                dn = [d[i] + n[i] for i in range(3)]
                # dn parallel to ker?
                cross = [dn[1] * ker[2] - dn[2] * ker[1], dn[2] * ker[0] - dn[0] * ker[2], dn[0] * ker[1] - dn[1] * ker[0]]
                if all(x == 0 for x in cross):
                    return True
            return False
        reps = []
        for b in sorted(circles):
            if not any(same_circle(b, r) for r in reps):
                reps.append(b)
        for b in reps:
            comps.append((idx, b, tuple(ker)))
        print(f"  coset {idx}: A = diag({A[0][0]},{A[1][1]},{A[2][2]}) t = {tuple(str(x) for x in t)}: "
              f"kernel direction {tuple(str(x) for x in ker)}, {len(reps)} circle(s) on T^3")
    print(f"  total circles on T^3 (before the V_4 quotient): {len(comps)}")
    # V_4 acts on these circles; the fixed set of sigma on Y_3 is the union modulo V_4.  Count orbits.
    def image_circle(g, comp):
        A, t = g
        idx, b, d = comp
        b2 = reduce_mod1(tuple(x + y for x, y in zip(matvec(A, b), t)))
        d2 = matvec(A, d)
        return (b2, d2)
    def circle_eq(c1, c2):
        b1, d1 = c1; b2, d2 = c2
        # parallel directions?
        cross = [d1[1] * d2[2] - d1[2] * d2[1], d1[2] * d2[0] - d1[0] * d2[2], d1[0] * d2[1] - d1[1] * d2[0]]
        if any(x != 0 for x in cross):
            return False
        d = [b1[i] - b2[i] for i in range(3)]
        for n in itertools.product(range(-3, 4), repeat=3):
            dn = [d[i] + n[i] for i in range(3)]
            cross = [dn[1] * d1[2] - dn[2] * d1[1], dn[2] * d1[0] - dn[0] * d1[2], dn[0] * d1[1] - dn[1] * d1[0]]
            if all(x == 0 for x in cross):
                return True
        return False
    orbits = []
    for comp in comps:
        c = (comp[1], comp[2])
        found = False
        for orb in orbits:
            for g in S19.values():
                if circle_eq(image_circle(g, comp), orb[0]):
                    orb.append(c); found = True; break
            if found:
                break
        if not found:
            orbits.append([c])
    print(f"  V_4-orbits of these circles = components of Fix(sigma) on Y_3: {len(orbits)}  (expected 1: the branch knot)")
    # length of the fixed circle (lattice units): the circle {b + s d} closes when s d in Z^3 (or an element of Pi maps
    # the line to itself with a shift) — compute the minimal period along the line within Pi.
    b, d = orbits[0][0]
    dn = [int(x) for x in d]
    from math import gcd
    g = gcd(gcd(abs(dn[0]), abs(dn[1])), abs(dn[2]))
    dn = [x // g for x in dn]
    L2 = sum(x * x for x in dn)
    # is there an element of Pi (non-translation) mapping the line to itself? then the period halves etc.
    shorter = False
    for gg in S19.values():
        A, t = gg
        if A == Pi[0][0]:
            continue
        Ad = matvec(A, tuple(Fr(x) for x in dn))
        if tuple(abs(x) for x in Ad) == tuple(Fr(abs(x)) for x in dn) and all(Ad[i] == dn[i] or Ad[i] == -dn[i] for i in range(3)):
            # A preserves the direction up to sign: check whether it maps the line to itself
            # (needs A d = +-d exactly)
            if all(Ad[i] == dn[i] for i in range(3)) or all(Ad[i] == -dn[i] for i in range(3)):
                shorter = True
    print(f"  the fixed circle: direction {tuple(dn)}, squared length {L2} lattice units, no non-translational element "
          f"of Pi preserves the line: {not shorter}  -> length sqrt({L2}) (the lattice is Z^3, vol(Y_3) = 1/4)")

    # Singular circles of the orbifold R^3/Pi^: orbits of the 3-fold rotation axes under Pi^.
    axes = []   # (base point on T^3, direction) for every rotation (A, t+n) with n in a box, A of order 3
    for k, gg in S198.items():
        A, t = gg
        if order_of_linear(A) != 3:
            continue
        a = axis_of(A)
        for n in itertools.product(range(-2, 3), repeat=3):
            tn = [t[i] + n[i] for i in range(3)]
            if sum(x * y for x, y in zip(a, tn)) != 0:
                continue
            # fixed line of v -> A v + tn: solve (1 - A) v = tn (rank 2), v + s a
            from sympy import Matrix
            M = Matrix([[int(int(i == j) - A[i][j]) for j in range(3)] for i in range(3)])
            sol = None
            for rows in itertools.combinations(range(3), 2):
                for cols in itertools.combinations(range(3), 2):
                    blk = M[list(rows), list(cols)]
                    if blk.det() != 0:
                        bvec = Matrix([tn[r] for r in rows])
                        x = blk.solve(bvec)
                        v = [Fr(0)] * 3
                        v[cols[0]] = Fr(str(x[0])); v[cols[1]] = Fr(str(x[1]))
                        if all(sum(M[i, j] * v[j] for j in range(3)) == tn[i] for i in range(3)):
                            sol = v
                        break
                if sol is not None:
                    break
            assert sol is not None
            axes.append((reduce_mod1(tuple(sol)), a))
    # dedupe axes mod Z^3 (translations are in Pi^) and then mod the point-group cosets
    reps = []
    for ax in axes:
        if not any(circle_eq(ax, r) for r in reps):
            reps.append(ax)
    print(f"\n3-fold rotation axes of Pi^ modulo the lattice Z^3: {len(reps)} lines")
    orbs = []
    for ax in reps:
        found = False
        for orb in orbs:
            for gg in S198.values():
                A, t = gg
                img = (reduce_mod1(tuple(x + y for x, y in zip(matvec(A, ax[0]), t))), matvec(A, ax[1]))
                if circle_eq(img, orb[0]):
                    orb.append(ax); found = True; break
            if found:
                break
        if not found:
            orbs.append([ax])
    print(f"Pi^-orbits of the axes = singular circles of the orbifold R^3/Pi^: {len(orbs)}  "
          f"(expected 1: the figure-eight knot with cone angle 2pi/3, Y_3/deck = S^3(4_1; 3))")
    print(f"The point group of Pi^ is T = A_4 = 2T/{{+-1}}: the holonomy of the descent's E_6 locus is the object's "
          f"McKay group modulo its centre; Pi's holonomy V_4 = ker(T -> Z/3) is the part that acts freely (B1273).")
    return len(orbits) == 1 and len(orbs) == 1 and n2_rot == 0

# ----------------------------------------------------------------------------------------------------------------
# Stage B — the local model along the knot, via SO(4) subset G_2 on Im H + H
# ----------------------------------------------------------------------------------------------------------------
class Q:
    """Quaternion with Fraction coordinates."""
    __slots__ = ("a", "b", "c", "d")
    def __init__(self, a, b=0, c=0, d=0):
        self.a, self.b, self.c, self.d = Fr(a), Fr(b), Fr(c), Fr(d)
    def __mul__(s, o):
        return Q(s.a*o.a - s.b*o.b - s.c*o.c - s.d*o.d,
                 s.a*o.b + s.b*o.a + s.c*o.d - s.d*o.c,
                 s.a*o.c - s.b*o.d + s.c*o.a + s.d*o.b,
                 s.a*o.d + s.b*o.c - s.c*o.b + s.d*o.a)
    def __add__(s, o):
        return Q(s.a+o.a, s.b+o.b, s.c+o.c, s.d+o.d)
    def __sub__(s, o):
        return Q(s.a-o.a, s.b-o.b, s.c-o.c, s.d-o.d)
    def __neg__(s):
        return Q(-s.a, -s.b, -s.c, -s.d)
    def conj(s):
        return Q(s.a, -s.b, -s.c, -s.d)
    def norm2(s):
        return s.a*s.a + s.b*s.b + s.c*s.c + s.d*s.d
    def tup(s):
        return (s.a, s.b, s.c, s.d)
    def __eq__(s, o):
        return s.tup() == o.tup()
    def __hash__(s):
        return hash(s.tup())
    def __repr__(s):
        return f"({s.a},{s.b},{s.c},{s.d})"
    def scale(s, k):
        return Q(s.a*k, s.b*k, s.c*k, s.d*k)

ONE = Q(1); I = Q(0, 1); J = Q(0, 0, 1); K = Q(0, 0, 0, 1); ZERO = Q(0)

def hurwitz_units():
    U = []
    for i in range(4):
        for s in (1, -1):
            v = [0] * 4; v[i] = s; U.append(Q(*v))
    h = Fr(1, 2)
    for signs in itertools.product((1, -1), repeat=4):
        U.append(Q(*[h * s for s in signs]))
    assert len(U) == 24
    return U

TT = hurwitz_units()   # 2T as unit Hurwitz quaternions

# Octonions O = H + H (Cayley-Dickson): (a,b)(c,d) = (ac - d^ b, d a + b c^)
def omul(x, y):
    a, b = x; c, d = y
    return (a*c - d.conj()*b, d*a + b*c.conj())

def so4_action(l, r, x, convention):
    """Candidate embeddings SO(4) -> G_2 on Im O = Im H + H."""
    a, b = x
    if convention == 0:
        return (l*a*l.conj(), l*b*r.conj())
    if convention == 1:
        return (l*a*l.conj(), r*b*l.conj())
    if convention == 2:
        return (l*a*l.conj(), b*r.conj() if False else r*b*r.conj())
    raise ValueError

def is_automorphism(l, r, convention):
    basis = [(I, ZERO), (J, ZERO), (K, ZERO), (ZERO, ONE), (ZERO, I), (ZERO, J), (ZERO, K), (ONE, ZERO)]
    for x in basis:
        for y in basis:
            lhs = so4_action(l, r, omul(x, y), convention)
            rhs = omul(so4_action(l, r, x, convention), so4_action(l, r, y, convention))
            if lhs != rhs:
                return False
    return True

def vec7(x):
    a, b = x
    return [a.b, a.c, a.d, b.a, b.b, b.c, b.d]

def mat7(l, r, convention):
    basis = [(I, ZERO), (J, ZERO), (K, ZERO), (ZERO, ONE), (ZERO, I), (ZERO, J), (ZERO, K)]
    cols = [vec7(so4_action(l, r, e, convention)) for e in basis]
    return tuple(tuple(cols[j][i] for j in range(7)) for i in range(7))

def stage_B():
    print("\n" + "=" * 100)
    print("STAGE B — the descent's local model along the knot: the group generated by the E_6 fibre 2T and the deck")
    print("=" * 100)
    # (i) which embedding SO(4) -> G_2 is an automorphism of the octonions?
    conv = None
    for c in (0, 1):
        ok = all(is_automorphism(l, r, c) for l in TT[:6] for r in TT[:6])
        print(f"  convention {c}: (x,y) -> " + ("(l x l^, l y r^)" if c == 0 else "(l x l^, r y l^)") +
              f" is an octonion automorphism for the sampled pairs: {ok}")
        if ok and conv is None:
            conv = c
    assert conv is not None
    # the fibre group: elements acting trivially on Im H are (+-1, r): under convention conv they act on H by
    # y -> +- y r^ (conv 0) or y -> +- r y (conv 1)
    # (ii) the deck: rotation by 2pi/3 about e = (i+j+k)/sqrt3 on Im H is conjugation by l0 = (1+i+j+k)/2 (order 6)
    l0 = Q(Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2))
    e_dir = I + J + K
    assert l0 * e_dir * l0.conj() == e_dir
    print(f"  deck's Im H part: conjugation by l0 = (1+i+j+k)/2 fixes e = i+j+k and has order 3 on Im H: "
          f"{(l0*l0*l0) == -ONE}")
    # (iii) admissible r: normalise the fibre 2T (r in 2O) with (l0, r)^3 in the fibre group up to sign -> r^3 in +-2T
    # build 2O numerically: 2T plus the 24 elements (+-u +- v)/sqrt2 for u != v in {1,i,j,k}
    import math
    TTf = [np.array([float(x) for x in q.tup()]) for q in TT]
    units = [np.array([1., 0, 0, 0]), np.array([0, 1., 0, 0]), np.array([0, 0, 1., 0]), np.array([0, 0, 0, 1.])]
    O2 = list(TTf)
    for u, v in itertools.combinations(range(4), 2):
        for su in (1, -1):
            for sv in (1, -1):
                O2.append((su * units[u] + sv * units[v]) / math.sqrt(2))
    assert len(O2) == 48
    def qmul_f(p, q):
        a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
        return np.array([a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
                         a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2])
    def in_set(q, S):
        return any(np.allclose(q, s, atol=1e-9) for s in S)
    def conj_f(q):
        return np.array([q[0], -q[1], -q[2], -q[3]])
    # check 2O normalises 2T
    normalises = all(all(in_set(qmul_f(qmul_f(r, g), conj_f(r)), TTf) for g in TTf) for r in O2)
    print(f"  the 48 elements built are the normaliser 2O of 2T (each conjugates 2T to itself): {normalises}")
    admissible = [r for r in O2 if in_set(qmul_f(qmul_f(r, r), r), TTf)]
    print(f"  r in 2O with r^3 in 2T (so that the deck has order 3 modulo the fibre group): {len(admissible)} of 48, "
          f"all in 2T: {all(in_set(r, TTf) for r in admissible)}")
    # (iv) generate the group for a few choices of r in 2T and show the same group arises
    def gen_group(l, r):
        gens = [mat7(ONE, g, conv) for g in TT] + [mat7(l, r, conv)]
        G = {}
        frontier = list(gens)
        for m in gens:
            G[m] = m
        while frontier:
            new = []
            for a in frontier:
                for b in gens:
                    m = tuple(tuple(sum(a[i][k] * b[k][j] for k in range(7)) for j in range(7)) for i in range(7))
                    if m not in G:
                        G[m] = m; new.append(m)
            frontier = new
        return list(G.keys())
    groups = {}
    for r in [TT[0], TT[2], TT[8], TT[15]]:
        G = gen_group(l0, r)
        groups[r] = frozenset(G)
        print(f"  r = {r}: |<fibre 2T, (l0, r)>| = {len(G)}")
    same = len(set(groups.values())) == 1
    print(f"  the same group for every admissible r (the fibre group absorbs r): {same}")
    G = list(list(groups.values())[0])
    # (v) structure: central elements, the Z_3
    def mm(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(7)) for j in range(7)) for i in range(7))
    Id7 = tuple(tuple(Fr(int(i == j)) for j in range(7)) for i in range(7))
    centre = [g for g in G if all(mm(g, h) == mm(h, g) for h in G)]
    def order(g):
        m = g; n = 1
        while m != Id7:
            m = mm(m, g); n += 1
        return n
    print(f"  centre of the group: order {len(centre)} (expected 6 = Z_2 x Z_3: {len(centre) == 6}); "
          f"element orders in the centre: {sorted(order(g) for g in centre)}")
    z3 = [g for g in centre if order(g) == 3]
    # the fibre subgroup
    fibre = set(mat7(ONE, g, conv) for g in TT)
    print(f"  fibre subgroup order {len(fibre)}; group = fibre x <central order-3 element>: "
          f"{len(set(mm(f, z) for f in fibre for z in [Id7, z3[0], mm(z3[0], z3[0])])) == len(G)}")
    # (vi) the complex structure J = left octonion multiplication by e/|e| on e^perp, and the SU(3) check
    # work numerically for J (irrational normalisation), exact matrices cast to float
    e7 = np.array([1., 1., 1., 0, 0, 0, 0]) / math.sqrt(3)
    basis = [(I, ZERO), (J, ZERO), (K, ZERO), (ZERO, ONE), (ZERO, I), (ZERO, J), (ZERO, K)]
    ef = (I + J + K, ZERO)
    Jm = np.zeros((7, 7))
    for j, b in enumerate(basis):
        col = np.array([float(x) for x in vec7(omul(ef, b))]) / math.sqrt(3)
        Jm[:, j] = col
    # restrict to e^perp
    Pperp = np.eye(7) - np.outer(e7, e7)
    Jp = Pperp @ Jm @ Pperp
    # J^2 = -1 on e^perp?
    ok_J = np.allclose(Jp @ Jp, -Pperp, atol=1e-9)
    print(f"  J = L_e on e^perp squares to -1: {ok_J}")
    # complex basis of e^perp: pick 3 vectors v with v, Jv spanning e^perp
    # v1 in Im H perp e, v2 = (0,1), v3 = (0,j)?  need J-independence: check
    v1 = np.array([1., -1., 0, 0, 0, 0, 0]) / math.sqrt(2)
    v2 = np.array([0, 0, 0, 1., 0, 0, 0]); v3 = np.array([0, 0, 0, 0, 0, 1., 0])
    cb = [v1, v2, v3]
    B = np.column_stack([v1, Jp @ v1, v2, Jp @ v2, v3, Jp @ v3])
    assert abs(np.linalg.det(np.column_stack([B, e7]))) > 1e-6
    def complex_matrix(g):
        M = np.array([[float(x) for x in r] for r in g])
        # g commutes with J on e^perp and fixes e?
        assert np.allclose(M @ e7, e7, atol=1e-9)
        assert np.allclose(M @ Jp, Jp @ M, atol=1e-9)
        C = np.zeros((3, 3), dtype=complex)
        for j, v in enumerate(cb):
            w = M @ v
            # express w = sum_k (x_k v_k + y_k J v_k) -> complex coefficient x_k + i y_k
            coeff = np.linalg.lstsq(B, w, rcond=None)[0]
            for k in range(3):
                C[k, j] = coeff[2*k] + 1j * coeff[2*k + 1]
        return C
    dets = [np.linalg.det(complex_matrix(g)) for g in G]
    print(f"  every element is C-linear for J and has det 1 (the group lies in SU(3) = Stab_G2(e)): "
          f"{all(abs(d - 1) < 1e-9 for d in dets)}")
    # (vii) strata: fixed subspaces on e^perp (real dimension) and the generic stabilisers
    def fixed_dim(g):
        M = np.array([[float(x) for x in r] for r in g])
        Mp = Pperp @ M @ Pperp
        # fixed vectors in e^perp: (M - 1) v = 0 with v perp e
        A = np.vstack([Mp - Pperp, e7[None, :]])
        s = np.linalg.svd(A, compute_uv=False)
        return int(np.sum(s < 1e-9)) - 0  # nullity of A on R^7 = dim of fixed vectors in e^perp
    from collections import Counter
    dims = Counter(fixed_dim(g) for g in G)
    print(f"  fixed-subspace dimensions on e^perp = C^3 over the 72 elements: {dict(sorted(dims.items()))}")
    # the 2-dimensional fixed subspaces: which are they?  E_6 plane = e^perp cap Im H (fixed by the fibre group),
    # the others are complex lines in H.  Collect the distinct planes and the setwise stabilisers / orbits.
    planes = []
    for g in G:
        if fixed_dim(g) != 2:
            continue
        M = np.array([[float(x) for x in r] for r in g])
        A = np.vstack([Pperp @ M @ Pperp - Pperp, e7[None, :]])
        u, s, vt = np.linalg.svd(A)
        null = vt[s.size - 2:].T if False else vt[-2:].T
        # orthonormal basis of the plane
        Qb, _ = np.linalg.qr(null)
        Pplane = Qb @ Qb.T
        if not any(np.allclose(Pplane, p, atol=1e-8) for p in planes):
            planes.append(Pplane)
    print(f"  distinct 2-planes fixed by some element: {len(planes)}")
    # classify: in Im H (E_6 plane) or in H
    imH = np.diag([1., 1, 1, 0, 0, 0, 0])
    e6_planes = [p for p in planes if np.allclose(p @ imH, p, atol=1e-8)]
    a_planes = [p for p in planes if not np.allclose(p @ imH, p, atol=1e-8)]
    print(f"    in Im H (the E_6 plane through the knot direction): {len(e6_planes)}; in the fibre H: {len(a_planes)}")
    # pointwise stabiliser orders
    def pointwise_stab(p):
        return [g for g in G if np.allclose(np.array([[float(x) for x in r] for r in g]) @ p, p, atol=1e-8)]
    print(f"    pointwise stabiliser of the E_6 plane: order {len(pointwise_stab(e6_planes[0]))} (2T: "
          f"{len(pointwise_stab(e6_planes[0])) == 24})")
    stabs = Counter(len(pointwise_stab(p)) for p in a_planes)
    print(f"    pointwise stabilisers of the fibre planes: {dict(stabs)}  (Z_3 each -> A_2 loci)")
    # orbits of the fibre planes under G
    orbits = []
    for p in a_planes:
        found = False
        for orb in orbits:
            for g in G:
                M = np.array([[float(x) for x in r] for r in g])
                if np.allclose(M @ orb[0] @ M.T, p, atol=1e-8):
                    orb.append(p); found = True; break
            if found:
                break
        if not found:
            orbits.append([p])
    print(f"    G-orbits of the fibre planes = number of A_2 loci through the knot: {len(orbits)} "
          f"(sizes {[len(o) for o in orbits]})")
    # setwise stabiliser of an A_2 plane and its action on the plane (the locus is plane / setwise stabiliser)
    p0 = orbits[0][0]
    setwise = [g for g in G if np.allclose(np.array([[float(x) for x in r] for r in g]) @ p0 @
                                           np.array([[float(x) for x in r] for r in g]).T, p0, atol=1e-8)]
    print(f"    setwise stabiliser of one A_2 plane: order {len(setwise)}; it acts on the plane through a cyclic group "
          f"of order {len(setwise) // len(pointwise_stab(p0))} (the A_2 locus is C/Z_6 x R: {len(setwise) // len(pointwise_stab(p0)) == 6})")
    # the E_6 plane modulo its setwise stabiliser: the knot's normal disc modulo Z_3
    setwise_e6 = [g for g in G if np.allclose(np.array([[float(x) for x in r] for r in g]) @ e6_planes[0] @
                                              np.array([[float(x) for x in r] for r in g]).T, e6_planes[0], atol=1e-8)]
    print(f"    setwise stabiliser of the E_6 plane: order {len(setwise_e6)} = 72 (all of G): {len(setwise_e6) == 72}; "
          f"it acts on the plane through Z_{len(setwise_e6) // 24} (the E_6 locus near the knot is C/Z_3 x R)")
    # (viii) McKay ages
    def age(g):
        C = complex_matrix(g)
        w = np.linalg.eigvals(C)
        a = 0
        for lam in w:
            t = (np.angle(lam) / (2 * math.pi)) % 1.0
            t12 = round(t * 12)
            assert abs(t * 12 - t12) < 1e-6, t
            a += Fr(t12 % 12, 12)
        return a
    # conjugacy classes
    classes = []
    seen = set()
    inv = {g: None for g in G}
    for g in G:
        if g in seen:
            continue
        cl = set()
        for h in G:
            # h g h^-1 : find h^-1 by search
            hinv = None
            for k in G:
                if mm(h, k) == Id7:
                    hinv = k; break
            cl.add(mm(mm(h, g), hinv))
        classes.append(cl); seen |= cl
    ages = Counter(age(next(iter(cl))) for cl in classes)
    print(f"  conjugacy classes: {len(classes)} (7 x 3 = 21: {len(classes) == 21}); ages: {dict(sorted(ages.items()))}")
    b2 = ages.get(Fr(1), 0); b4 = ages.get(Fr(2), 0)
    print(f"  crepant resolution of C^3/G (Ito-Reid): b_2 = #age-1 classes = {b2}, b_4 = #age-2 classes = {b4}, "
          f"chi = {1 + b2 + b4}")
    print(f"  non-compact exceptional divisors b_2 - b_4 = {b2 - b4} = 6 (E_6) + 2 (A_2) + 2 (A_2): {b2 - b4 == 10}; "
          f"compact divisors (5d gauge rank along the knot) = {b4}")
    # (ix) the deck acts on the E_6 fibre C^2/2T through the scalar omega (centre of U(2)): inner, no diagram flip
    zc = z3[0]
    Mz = np.array([[float(x) for x in r] for r in zc])
    Hpart = Mz[3:, 3:]
    # is it a scalar in the complex structure J restricted to H?  J on H: check Mz restricted commutes and equals
    # cos(2pi/3) + sin(2pi/3) J
    JH = Jp[3:, 3:]
    scal = np.allclose(Hpart, math.cos(2*math.pi/3) * np.eye(4) + math.sin(2*math.pi/3) * JH, atol=1e-9) or \
           np.allclose(Hpart, math.cos(2*math.pi/3) * np.eye(4) - math.sin(2*math.pi/3) * JH, atol=1e-9)
    print(f"  the central order-3 element acts on the fibre H as the scalar omega^(+-1) for J (inner on the E_6 "
          f"singularity, no diagram automorphism): {scal}")
    # (x) the linear part of the descent's flat G_2 orbifold: the lifts of the locus holonomy to the first Sp(1)
    # factor are Q_8 = {+-1, +-i, +-j, +-k} (V_4 = conjugation by i, j, k) and the deck's l0; together they generate 2T.
    gens = [ONE, -ONE, I, J, K, l0]
    L = set(gens)
    frontier = list(L)
    while frontier:
        new = []
        for a in frontier:
            for b in gens:
                c = a * b
                if c not in L:
                    L.add(c); new.append(c)
        frontier = new
    print(f"  the locus holonomy V_4 (lifted to Q_8) together with the deck's l0 generates a group of order {len(L)} in "
          f"the first Sp(1): 2T itself ({set(L) == set(TT)}) -- the E_6 locus's holonomy and the E_6 fibre group are the "
          f"same finite group on the two Sp(1) factors of SO(4) c G_2")
    return same and len(G) == 72 and len(orbits) == 2 and b2 == 15 and b4 == 5 and set(L) == set(TT)

# ----------------------------------------------------------------------------------------------------------------
# Stage C — the charge lattice under the deck
# ----------------------------------------------------------------------------------------------------------------
def stage_C():
    print("\n" + "=" * 100)
    print("STAGE C — the sum-rule lattice: Z^3 (one integer per apex) as the deck's permutation module")
    print("=" * 100)
    from sympy import Matrix
    S = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])   # cyclic permutation of the three apexes
    inv = (S - Matrix.eye(3)).nullspace()
    print(f"  invariant vectors of Z^3: spanned by {tuple(inv[0].T)} — the all-equal charges")
    # sum-zero sublattice A_2
    A2 = Matrix([[1, -1, 0], [0, 1, -1]])   # rows span the sum-zero lattice
    # invariants inside A_2
    inv_A2 = [v for v in inv if sum(v) == 0]
    print(f"  invariants of the deck inside the sum-zero lattice A_2: {len(inv_A2)} (none: the sum rule kills every "
          f"invariant class at the apexes)")
    # the coset of vectors with sum 0 and all entries = 1 mod 3
    box = range(-4, 5)
    coset = [(a, b, c) for a in box for b in box for c in box if a + b + c == 0 and a % 3 == 1 and b % 3 == 1 and c % 3 == 1]
    base = (1, 1, -2)
    ok = all(((a - 1) % 3 == 0 and (b - 1) % 3 == 0 and (c + 2) % 3 == 0) for (a, b, c) in coset)
    print(f"  {{sum 0, all entries = 1 mod 3}} in the box: {len(coset)} vectors, every one = (1,1,-2) + 3 A_2: {ok}")
    orbit = [base, tuple(S * Matrix(base)), tuple(S * S * Matrix(base))]
    print(f"  deck orbit of (1,1,-2): {orbit}; sum of the orbit: {tuple(sum(v[i] for v in orbit) for i in range(3))}")
    # Gram matrix: equilateral
    G = [[sum(x * y for x, y in zip(u, v)) for v in orbit] for u in orbit]
    print(f"  Gram matrix of the orbit: {G} (equilateral: {G[0][0] == G[1][1] == G[2][2] and G[0][1] == G[0][2] == G[1][2]})")
    # 3 x weights of the 3-bar of SU(3): weights of 3 are e_i - (1,1,1)/3; of 3-bar: -(e_i - (1,1,1)/3)
    w3bar = [tuple(-(int(i == k)) + Fr(1, 3) for k in range(3)) for i in range(3)]
    three_w = [tuple(3 * x for x in w) for w in w3bar]
    print(f"  3 x weights of the 3-bar: {[tuple(int(x) for x in w) for w in three_w]}; equals the orbit as a set: "
          f"{set(tuple(int(x) for x in w) for w in three_w) == set(tuple(int(x) for x in v) for v in orbit)}")
    # charges under the pair (w, sigma^* w): apex alpha gets (q_alpha, q_{sigma^-1 alpha})
    q = base
    pairs = [(q[a], q[(a - 1) % 3]) for a in range(3)]
    print(f"  charge vectors of the three apexes under the pair (w, sigma^*w) with q = (1,1,-2): {pairs}; "
          f"each component = 1 mod 3: {all(x % 3 == 1 for p in pairs for x in p)}; sum = {tuple(sum(p[i] for p in pairs) for i in range(2))}")
    return len(inv_A2) == 0 and ok

# ----------------------------------------------------------------------------------------------------------------
# Stage D — the antipode on S^4/Gamma and the absence of E_6 points on CP^2/Gamma
# ----------------------------------------------------------------------------------------------------------------
def stage_D():
    print("\n" + "=" * 100)
    print("STAGE D — L212 (iii) in the global-quotient class: S^4/Gamma has an antipodal companion, CP^2/Gamma no E_6 point")
    print("=" * 100)
    # S^4: an isometry fixing p = e5 with derivative -1 on T_p is unique: diag(-1,-1,-1,-1,1); its fixed set is {+-e5}
    M = np.diag([-1., -1, -1, -1, 1])
    w, v = np.linalg.eig(M)
    fixed = [tuple(np.round(v[:, i], 6)) for i in range(5) if abs(w[i] - 1) < 1e-9]
    print(f"  O(5) element fixing e5 with derivative -1 on T_p S^4: fixed subspace of R^5 has dimension {len(fixed)} "
          f"-> fixed points on S^4: {{e5, -e5}} (the antipode is fixed with derivative -1 too)")
    # on HP^1 with 2T in Sp(1)_L acting by [q1:q2] -> [l q1 : q2]: the element -1 acts on the chart at [1:0] as -1
    # (B1355: L' fixed pointwise by -1 only, normal weights (-1,-1)) — the A_1 locus over the antipode.
    # CP^2: the twistor fibre over p (ASD orientation) is P(T_p) = P(C^2); the subgroup of U(2) acting trivially on
    # P(C^2) is the centre U(1).  Within 2T subset SU(2): only +-1.
    def su2(q):
        a, b, c, d = [float(x) for x in q.tup()]
        return np.array([[a + 1j*b, c + 1j*d], [-c + 1j*d, a - 1j*b]])
    trivial_on_P = []
    for g in TT:
        m = su2(g)
        # acts trivially on P(C^2) iff scalar
        if np.allclose(m, m[0, 0] * np.eye(2), atol=1e-12):
            trivial_on_P.append(g)
    print(f"  elements of 2T subset SU(2) subset U(2) acting trivially on the twistor fibre P(C^2) of CP^2: "
          f"{len(trivial_on_P)} ({trivial_on_P}) -> the twistor-trivial part of any point stabiliser on CP^2/Gamma is "
          f"cyclic (a subgroup of the scalars U(1)): no E_6 point; with Hitchin's theorem (S^4, CP^2 are the only "
          f"compact positive self-dual Einstein 4-manifolds) this covers every global quotient of a manifold.")
    return len(fixed) == 1 and len(trivial_on_P) == 2

if __name__ == "__main__":
    okA = stage_A()
    okB = stage_B()
    okC = stage_C()
    okD = stage_D()
    print("\n" + "=" * 100)
    print(f"SUMMARY: stage A (one fixed circle, one singular circle, no 2-fold axes): {okA}; "
          f"stage B (|G| = 72 = 2T x Z_3, two A_2 loci, ages 15/5): {okB}; stage C (no invariant charges, coset): {okC}; "
          f"stage D (antipode; no E_6 on CP^2/Gamma): {okD}")
    print("=" * 100)
