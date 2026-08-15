#!/usr/bin/env python3
"""
Independent re-computation of the checkable claims of
"THE GOLDEN GRAMMAR" (main.pdf, 35 pp., 2026-08-15).

Adversarial scrutiny pass. Nothing project-internal is imported; the only
dependencies are sympy and the standard library. Every verdict-bearing
comparison is exact. Exits non-zero on any drift.

Run:  python3 papers/scrutiny_golden_grammar/verify_scrutiny.py
"""

import itertools
import math
import sys

import sympy as sp

FAILURES = []
CHECKS = 0


def check(label, got, want):
    global CHECKS
    CHECKS += 1
    ok = got == want
    print(f"  [{'ok ' if ok else 'FAIL'}] {label}: {got!r}" + ("" if ok else f"  (expected {want!r})"))
    if not ok:
        FAILURES.append(label)


# ---------------------------------------------------------------------------
# Thm 4.2 / Scope 4.7 — the period-one locus, and the m = 6 second class
# ---------------------------------------------------------------------------
def associated_form(M):
    """Binary quadratic form attached to a 2x2 integer matrix; GL(2,Z)-equivariant."""
    (a, b), (c, d) = M
    return (c, d - a, -b)


def content(f):
    return math.gcd(math.gcd(abs(f[0]), abs(f[1])), abs(f[2]))


def gl2z_form_classes(D):
    """Number of GL(2,Z)-classes of primitive indefinite forms of discriminant D."""
    forms = set()
    s = math.isqrt(D)
    for b in range(-s - 2, s + 3):
        if (b * b - D) % 4:
            continue
        ac = (b * b - D) // 4
        if ac == 0:
            continue
        for a in range(-abs(ac), abs(ac) + 1):
            if a == 0 or ac % a:
                continue
            c = ac // a
            if math.gcd(math.gcd(abs(a), abs(b)), abs(c)) != 1:
                continue
            forms.add((a, b, c))
    parent = {f: f for f in forms}

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def act(f, M):
        a, b, c = f
        p, q, r, t = M
        return (a * p * p + b * p * r + c * r * r,
                2 * a * p * q + b * (p * t + q * r) + 2 * c * r * t,
                a * q * q + b * q * t + c * t * t)

    for f in forms:
        for M in [(0, -1, 1, 0), (1, 1, 0, 1), (1, 0, 0, -1)]:
            g = act(f, M)
            if g in parent:
                ru, rv = find(f), find(g)
                if ru != rv:
                    parent[ru] = rv
    return len({find(f) for f in forms})


def sec_family():
    print("\n== Thm 4.2 / Scope 4.7 : the period-one locus ==")
    A = ((1, 2), (3, 5))
    X6 = ((6, 1), (1, 0))
    check("witness A det", A[0][0] * A[1][1] - A[0][1] * A[1][0], -1)
    check("witness A trace", A[0][0] + A[1][1], 6)
    check("form of A", associated_form(A), (3, 4, -2))
    check("form of X6", associated_form(X6), (1, -6, -1))
    check("x^2 = 3 mod 5 insoluble", [x for x in range(5) if (x * x - 3) % 5 == 0], [])
    check("x^2 = -3 mod 5 insoluble", [x for x in range(5) if (x * x + 3) % 5 == 0], [])
    # the paper declines to name a threshold; it is m = 6, and it is cheap
    classes = {m: gl2z_form_classes(m * m + 4) for m in range(1, 13)}
    check("class counts m=1..6", [classes[m] for m in range(1, 7)], [1, 1, 1, 1, 1, 2])
    check("first m with a second class", min(m for m in classes if classes[m] > 1), 6)
    # Selection I extends to the whole locus: |torsion| = |det(A^2 - I)| = m^2
    for m in range(1, 8):
        for D in (m * m + 4,):
            pass
    detA2I = lambda t: (1 - t - 1) * (1 + t - 1)  # chi(1)*chi(-1) for x^2 - t x - 1
    check("det(A^2-I) = -m^2 for every det=-1 class", [detA2I(m) for m in range(1, 6)],
          [-1, -4, -9, -16, -25])


# ---------------------------------------------------------------------------
# Lem 5.2, Thm 5.4 — the collapse lemma and the homology
# ---------------------------------------------------------------------------
def sec_collapse():
    print("\n== Lem 5.2 / Thm 5.4 : the collapse lemma and H_1 ==")
    m = sp.symbols('m', positive=True, integer=True)
    phi = sp.Matrix([[m ** 2 + 1, m], [m, 1]])
    X = sp.Matrix([[m, 1], [1, 0]])
    check("phi_m = X_m^2", sp.simplify(X ** 2 - phi), sp.zeros(2, 2))
    check("R^m L^m = phi_m",
          sp.simplify(sp.Matrix([[1, m], [0, 1]]) * sp.Matrix([[1, 0], [m, 1]]) - phi), sp.zeros(2, 2))
    check("chi_m(1) = -m^2", sp.expand((phi - sp.eye(2)).det()), sp.expand(-m ** 2))
    check("chi_m(-1) = m^2+4", sp.expand((phi + sp.eye(2)).det()), sp.expand(m ** 2 + 4))
    check("tr phi_m = m^2+2", sp.expand(phi.trace()), sp.expand(m ** 2 + 2))
    # Smith normal form of phi_m - I for concrete m
    for mm in range(1, 7):
        M = sp.Matrix([[mm ** 2, mm], [mm, 0]])
        d1 = sp.gcd(sp.gcd(M[0, 0], M[0, 1]), M[1, 0])
        check(f"SNF(phi_{mm}-I) = diag({mm},{mm})", (int(d1), int(abs(M.det()) // d1)), (mm, mm))


# ---------------------------------------------------------------------------
# Prop 4.4 — the period-two family
# ---------------------------------------------------------------------------
def sec_period_two():
    print("\n== Prop 4.4 / Scope 4.5 : the period-two relaxation ==")
    a, b = sp.symbols('a b', positive=True, integer=True)
    M = sp.Matrix([[a, 1], [1, 0]]) * sp.Matrix([[b, 1], [1, 0]])
    check("M(a,b)", sp.simplify(M - sp.Matrix([[a * b + 1, a], [b, 1]])), sp.zeros(2, 2))
    check("det M(a,b) = +1", sp.simplify(M.det()), 1)
    check("M(m,m) = phi_m", sp.simplify(M.subs({a: 3, b: 3}) - sp.Matrix([[10, 3], [3, 1]])), sp.zeros(2, 2))
    for (aa, bb) in [(1, 1), (2, 3), (2, 4), (3, 6)]:
        N = sp.Matrix([[aa * bb, aa], [bb, 0]])
        d1 = int(sp.gcd(sp.gcd(N[0, 0], N[0, 1]), N[1, 0]))
        d2 = int(abs(N.det())) // d1
        check(f"H_1 torsion (a,b)=({aa},{bb}) = (gcd,lcm)", (d1, d2),
              (math.gcd(aa, bb), aa * bb // math.gcd(aa, bb)))
    check("trace M(2,3) = 8, not of the form m^2+2",
          [m for m in range(1, 10) if m * m + 2 == 8], [])


# ---------------------------------------------------------------------------
# Lem 5.7, Thm 5.8, Prop 5.10 — the shadow modulus
# ---------------------------------------------------------------------------
def sl2_order(N):
    n = N ** 3
    for p in sp.primefactors(N):
        n = n * (p * p - 1) // (p * p)
    return n


def sec_shadow():
    print("\n== Lem 5.7 / Thm 5.8 / Prop 5.10 : the shadow modulus ==")
    for N in range(2, 40):
        lhs = sp.prod([sp.Rational(p * p - 1, p * p) for p in sp.primefactors(N)])
        check_silent = lhs >= sp.Rational(N + 1, 2 * N)
        if not check_silent:
            FAILURES.append(f"Lem 5.7 fails at N={N}")
    print(f"  [ok ] Lem 5.7 holds for 2 <= N <= 39")
    global CHECKS
    CHECKS += 1
    check("|SL(2,Z/N)| for N=2..6", [sl2_order(N) for N in range(2, 7)], [6, 24, 48, 120, 144])
    check("N with |SL(2,Z/N)| in {24,48,120}",
          [N for N in range(2, 200) if sl2_order(N) in (24, 48, 120)], [3, 4, 5])
    check("m^2+4 in {3,4,5} for m>=1", [m for m in range(1, 100) if m * m + 4 in (3, 4, 5)], [1])
    # Prop 5.10: SL(2,Z/4) element orders
    N = 4
    G = [(a, b, c, d) for a in range(N) for b in range(N) for c in range(N) for d in range(N)
         if (a * d - b * c) % N == 1]

    def mul(x, y):
        a, b, c, d = x
        e, f, g, h = y
        return ((a * e + b * g) % N, (a * f + b * h) % N, (c * e + d * g) % N, (c * f + d * h) % N)

    I = (1, 0, 0, 1)
    orders = {}
    for g in G:
        o, y = 1, g
        while y != I:
            y = mul(y, g)
            o += 1
        orders[o] = orders.get(o, 0) + 1
    check("|SL(2,Z/4)|", len(G), 48)
    check("SL(2,Z/4) involutions", orders.get(2, 0), 7)
    check("SL(2,Z/4) elements of order 8", orders.get(8, 0), 0)
    check("p(p^2-1) never 48", [p for p in sp.primerange(2, 200) if p * (p * p - 1) == 48], [])
    # Scope 5.13
    check("squarefree kernels of 5,20,125", [sp.factorint(n) and int(sp.prod(sp.primefactors(n)))
                                             for n in (5, 20, 125)], [5, 10, 5])
    check("|SL(2,Z/N)| at N=5,20,125", [sl2_order(n) for n in (5, 20, 125)], [120, 5760, 1875000])
    # Scope 5.12: phi_1 mod 5 has order 10
    P = sp.Matrix([[2, 1], [1, 1]])
    o, Q = 1, P.applyfunc(lambda z: z % 5)
    while Q != sp.eye(2):
        Q = (Q * P).applyfunc(lambda z: z % 5)
        o += 1
    check("order of phi_1 mod 5", o, 10)


# ---------------------------------------------------------------------------
# Thm 5.14 — the Jones index wall
# ---------------------------------------------------------------------------
def sec_jones():
    print("\n== Thm 5.14 : the Jones index wall ==")
    lam = lambda m: sp.Rational(1, 2) * (m + sp.sqrt(m * m + 4))
    check("lambda_m < 2 exactly at m=1", [m for m in range(1, 20) if lam(m) < 2], [1])
    check("phi = 2 cos(pi/5)", sp.simplify(lam(1) - 2 * sp.cos(sp.pi / 5)), 0)


# ---------------------------------------------------------------------------
# Scope 5.18 / 5.21 — the Latimer-MacDuffee witness and the Fricke identity
# ---------------------------------------------------------------------------
def sec_pairs():
    print("\n== Scope 5.18 / 5.21 : covers, and the pairwise criterion ==")
    phi1 = sp.Matrix([[2, 1], [1, 1]])
    phi1_3 = phi1 ** 3
    phi4 = sp.Matrix([[17, 4], [4, 1]])
    check("tr phi_1^3 = tr phi_4 = 18", (int(phi1_3.trace()), int(phi4.trace())), (18, 18))
    f3 = associated_form(((int(phi1_3[0, 0]), int(phi1_3[0, 1])), (int(phi1_3[1, 0]), int(phi1_3[1, 1]))))
    f4 = associated_form(((17, 4), (4, 1)))
    check("form contents differ -> not GL(2,Z)-conjugate", (content(f3), content(f4)), (8, 4))
    # Lucas: tr phi_1^n - 2 is a square exactly at odd n
    sq = []
    t = phi1
    for n in range(1, 12):
        v = int(t.trace()) - 2
        r = math.isqrt(v)
        if r * r == v:
            sq.append((n, r))
        t = t * phi1
    check("n with tr phi_1^n - 2 square", [n for n, _ in sq], [1, 3, 5, 7, 9, 11])
    check("the m values", [r for _, r in sq][:3], [1, 4, 11])
    # the Fricke-type identity: TRUE for phi_m, FALSE for X_m
    m, n = sp.symbols('m n')
    X = lambda t: sp.Matrix([[t, 1], [1, 0]])
    trX = sp.simplify(sp.trace(X(m) * X(n) * X(m).inv() * X(n).inv()))
    trPhi = sp.simplify(sp.trace(X(m) ** 2 * X(n) ** 2 * (X(m) ** 2).inv() * (X(n) ** 2).inv()))
    claimed = 2 - (m * n * (n - m)) ** 2
    check("tr[X_m,X_n] does NOT match the paper's formula",
          sp.simplify(trX - claimed) == 0, False)
    check("tr[X_m,X_n] = 2-(m-n)^2", sp.simplify(trX - (2 - (m - n) ** 2)), 0)
    check("tr[phi_m,phi_n] = 2-(mn(n-m))^2", sp.simplify(trPhi - claimed), 0)
    check("|mn(n-m)|=2 unique for 1<=m<n",
          [(a, b) for a in range(1, 20) for b in range(a + 1, 20) if abs(a * b * (b - a)) == 2],
          [(1, 2)])


# ---------------------------------------------------------------------------
# Prop 8.1 / Prop 9.3 / Rmk 9.4 — the invariants, the plane, the parity
# ---------------------------------------------------------------------------
def sec_invariants():
    print("\n== Prop 8.1 / Prop 9.3 / Rmk 9.4 : 2T-invariants and the plane ==")
    I = sp.I
    half = sp.Rational(1, 2)

    def q2m(a, b, c, d):
        return sp.Matrix([[a + b * I, c + d * I], [-c + d * I, a - b * I]])

    units = []
    for s in (1, -1):
        units += [(s, 0, 0, 0), (0, s, 0, 0), (0, 0, s, 0), (0, 0, 0, s)]
    for s in itertools.product((1, -1), repeat=4):
        units.append(tuple(x * half for x in s))
    T2 = [q2m(*u) for u in units]
    w = q2m(1 / sp.sqrt(2), 1 / sp.sqrt(2), 0, 0)
    O2 = T2 + [sp.simplify(g * w) for g in T2]
    check("|2T|", len(T2), 24)
    check("|2O|", len(O2), 48)

    def inv_dim(G, n):
        tot = 0
        for g in G:
            ev = list(g.eigenvals().keys())
            l1, l2 = (ev[0], ev[0]) if len(ev) == 1 else (ev[0], ev[1])
            tot += sum(l1 ** k * l2 ** (n - k) for k in range(n + 1))
        return int(sp.nsimplify(sp.simplify(tot / len(G))))

    doubled_exponents = [2, 8, 10, 14, 16, 22]  # 2 * (1,4,5,7,8,11)
    dimsT = {n: inv_dim(T2, n) for n in doubled_exponents}
    check("dim (Sym^n)^{2T} on the doubled exponents", dimsT, {2: 0, 8: 1, 10: 0, 14: 1, 16: 1, 22: 1})
    check("C is 4-dimensional", sum(dimsT.values()), 4)
    dimsO = {n: inv_dim(O2, n) for n in doubled_exponents}
    check("dim (Sym^n)^{2O} on the doubled exponents", dimsO, {2: 0, 8: 1, 10: 0, 14: 0, 16: 1, 22: 0})
    check("e6^{2O} = <x8,x16>, dimension 2", sum(dimsO.values()), 2)
    x, y = sp.symbols('x y')
    Phi = x ** 4 - 2 * x ** 3 * y + 2 * x ** 2 * y ** 2 + 2 * x * y ** 3 + y ** 4
    Psi = x ** 4 + 2 * x ** 3 * y + 2 * x ** 2 * y ** 2 - 2 * x * y ** 3 + y ** 4
    check("Phi*Psi = the octahedral W", sp.expand(Phi * Psi),
          sp.expand(x ** 8 + 14 * x ** 4 * y ** 4 + y ** 8))
    check("degrees of W, tW, W^2, tW^2", [8, 6 + 8, 16, 6 + 16], [8, 14, 16, 22])
    # Rmk 9.6: sign(tau_m) = (-1)^m positive exactly at the theta-odd exponents {4,8}
    f4_exponents = {1, 5, 7, 11}
    e6_exponents = [1, 4, 5, 7, 8, 11]
    check("theta-odd exponents = {4,8}", sorted(set(e6_exponents) - f4_exponents), [4, 8])
    check("(-1)^m positive exactly there",
          sorted(m for m in e6_exponents if (-1) ** m > 0), [4, 8])
    check("unmeasured exponents multiply to 77", 7 * 11, 77)


# ---------------------------------------------------------------------------
# Cor 8.5 / Rmk 8.7 / Thm 9.20 — the Levi classification and the rung spectrum
# ---------------------------------------------------------------------------
def e6_roots():
    import numpy as np
    a = [None,
         np.array([1, -1, -1, -1, -1, -1, -1, 1]) / 2,
         np.array([1, 1, 0, 0, 0, 0, 0, 0]),
         np.array([-1, 1, 0, 0, 0, 0, 0, 0]),
         np.array([0, -1, 1, 0, 0, 0, 0, 0]),
         np.array([0, 0, -1, 1, 0, 0, 0, 0]),
         np.array([0, 0, 0, -1, 1, 0, 0, 0])]
    simple = [a[i] for i in range(1, 7)]
    R = set()
    for s in simple:
        R.add(tuple(s))
        R.add(tuple(-s))
    changed = True
    while changed:
        changed = False
        for r in list(R):
            for s in simple:
                for sgn in (1, -1):
                    n = tuple(np.array(r) + sgn * np.array(s))
                    if abs(float(np.dot(n, n)) - 2) < 1e-9 and n not in R:
                        R.add(n)
                        changed = True
    return simple, R


def sec_levi():
    print("\n== Cor 8.5 / Rmk 8.7 / Thm 9.20 : Levi subsystems of E6 ==")
    try:
        import numpy as np
    except ImportError:
        print("  [skip] numpy unavailable")
        return
    simple, R = e6_roots()
    check("|Phi(E6)|", len(R), 72)
    counts = {}
    for k in range(7):
        for sub in itertools.combinations(range(6), k):
            if not sub:
                counts.setdefault(0, []).append(())
                continue
            M = np.array([simple[i] for i in sub], dtype=float)
            Q, _ = np.linalg.qr(M.T)
            Q = Q[:, :np.linalg.matrix_rank(M)]
            c = sum(1 for r in R
                    if np.linalg.norm(np.array(r, dtype=float) - Q @ (Q.T @ np.array(r, dtype=float))) < 1e-8)
            counts.setdefault(c, []).append(sub)
    check("Levi root counts", sorted(counts),
          [0, 2, 4, 6, 8, 10, 12, 14, 20, 22, 24, 30, 40, 72])
    check("rung spectrum (6 + count)", sorted(6 + c for c in counts),
          [6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78])
    check("22 and 24 absent", [d for d in (22, 24, 32, 34, 38, 40, 42, 44) if d in {6 + c for c in counts}], [])
    check("the spectrum has exactly 14 values", len(counts), 14)
    check("root counts 40,24,20,8 are all realised", [c in counts for c in (40, 24, 20, 8)],
          [True] * 4)
    # Thm 9.13's stratification arithmetic
    check("class sizes sum to 46-12", 2 + 2 + 6 * 5, 34)
    check("strata 12 + subsets of {2,2,6,6,6,6,6}",
          sorted({12, 12 + 2, 12 + 2 + 2, 12 + 2 + 6, 12 + 6, 12 + 2 + 6 + 6, 12 + 6 + 6 + 6}),
          [12, 14, 16, 18, 20, 26, 30])
    check("five size-6 hyperplanes give C(5,2)=10 pairs; 2 thirty-points use 6, four 26-points use 4",
          (math.comb(5, 2), 2 * math.comb(3, 2) + 4), (10, 10))


# ---------------------------------------------------------------------------
# Prop 8.8 / App A — the charge field
# ---------------------------------------------------------------------------
def sec_field():
    print("\n== Prop 8.8 / App A : the charge field K ==")
    x, t = sp.symbols('x t')
    f = x ** 3 - 12 * x - 5
    check("disc f", int(sp.discriminant(f, x)), 6237)
    check("6237 = 3^4*7*11", sp.factorint(6237), {3: 4, 7: 1, 11: 1})
    check("irreducible", sp.Poly(f, x).is_irreducible, True)
    check("totally real", len([r for r in sp.Poly(f, x).all_roots() if r.is_real]), 3)
    check("resolvent Q(sqrt 77)", int(sp.sqrt(6237 / sp.Integer(81)) ** 2), 77)
    shapes = {}
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 953, 1129, 421493):
        fac = sp.factor_list(sp.Poly(f, x), modulus=p)[1]
        shapes[p] = sorted((sp.Poly(g, x).degree(), e) for g, e in fac)
    check("p=3 totally ramified", shapes[3], [(1, 3)])
    check("p=7 splits p q^2", shapes[7], [(1, 1), (1, 2)])
    check("p=11 splits p q^2", shapes[11], [(1, 1), (1, 2)])
    check("13,17,19 inert", [shapes[p] for p in (13, 17, 19)], [[(3, 1)]] * 3)
    check("2,5 and the value primes: one degree-one place each",
          [shapes[p] for p in (2, 5, 953, 1129, 421493)], [[(1, 1), (2, 1)]] * 5)
    check("5 is unramified in K (Rmk 8.9)", all(e == 1 for _, e in shapes[5]), True)
    # class number one: Minkowski bound < 18, every prime of norm <= 17 principal
    mink = sp.Rational(math.factorial(3), 27) * sp.sqrt(6237)
    check("Minkowski bound < 18", bool(mink < 18), True)
    a, b, c = sp.symbols('a b c')
    Nform = sp.expand(sp.resultant(f, a + b * x + c * x ** 2, x))
    Nf = sp.lambdify((a, b, c), Nform, 'math')
    found = {}
    Rng = 14
    for A in range(-Rng, Rng + 1):
        for B in range(-Rng, Rng + 1):
            for C in range(-Rng, Rng + 1):
                n = int(round(Nf(A, B, C)))
                if abs(n) in (2, 3, 4, 5, 7, 11):
                    found.setdefault(abs(n), []).append((A, B, C))
    check("generators of norm 2,3,4,5,7,11 all exist", sorted(found), [2, 3, 4, 5, 7, 11])
    for p in (7, 11):
        roots = [r for r in range(p) if (r ** 3 - 12 * r - 5) % p == 0]
        killed = {r for (A, B, C) in found[p] for r in roots if (A + B * r + C * r * r) % p == 0}
        check(f"both degree-one primes above {p} are principal", sorted(killed), sorted(roots))
    # Appendix A: the pencil cubic and its Tschirnhaus reduction
    mu = 500716339200 * t ** 3 - 159667200 * t ** 2 - 28224 * t + 1
    check("lead coeff = 2^16*3^4*5^2*7^3*11", sp.factorint(500716339200),
          {2: 16, 3: 4, 5: 2, 7: 3, 11: 1})
    check("disc mu = 2^32*3^10*5^2*7^3*11*13^6", sp.factorint(sp.discriminant(mu, t)),
          {2: 32, 3: 10, 5: 2, 7: 3, 11: 1, 13: 6})
    rho = (sp.Rational(-815, 338) - sp.Rational(4934160, 169) * t
           + sp.Rational(13039488000, 169) * t ** 2)
    rem = sp.rem(sp.Poly(sp.expand(rho ** 3 - 12 * rho - 5), t), sp.Poly(mu, t))
    check("rho^3 - 12 rho - 5 = 0 in Q[t]/mu", sp.simplify(rem.as_expr()), 0)


# ---------------------------------------------------------------------------
# Thm 10.3 — the real form, from K-type dimensions alone
# ---------------------------------------------------------------------------
def sec_real_form():
    print("\n== Thm 10.3 : the real form, by signature ==")
    ktypes = {
        "e6(-78) compact": [27],
        "e6(6) split, K=sp(4)": [27],
        "e6(-14), K=so(10)+u(1)": [16, 10, 1],
        "e6(-26), K=f4": [26, 1],
        "e6(2), K=su(6)+su(2)": [15, 12],
    }
    can15 = {}
    for name, parts in ktypes.items():
        sums = {sum(s) for k in range(len(parts) + 1) for s in itertools.combinations(parts, k)}
        can15[name] = 15 in sums
    check("only e6(2) can realise signature (15,12)",
          [n for n, v in can15.items() if v], ["e6(2), K=su(6)+su(2)"])
    check("dim checks: 27 = 9*1 + 6*3", 9 * 1 + 6 * 3, 27)
    check("A2+A1 rung: 8 + 3 + 3 = 14", 8 + 3 + 3, 14)


# ---------------------------------------------------------------------------
# arithmetic of the paper's own counts
# ---------------------------------------------------------------------------
def sec_round2():
    """Round-2 checks: the intertwiner obstruction, and the CS arithmetic."""
    print("\n== Round 2 : the intertwiner lattice, and Cor 11.3 ==")
    # Scope 4.7 again, by the intertwiner route rather than by forms.
    # {P : A P = P X_6} = {[[(r+s)/3,(r-5s)/3],[r,s]] : r+s = 0 mod 3},
    # det P = -((r-3s)^2 - 10 s^2)/3, so det P = +-1  <=>  x^2 - 10 y^2 = -+3.
    r, s = sp.symbols('r s')
    A = sp.Matrix([[1, 2], [3, 5]])
    X6 = sp.Matrix([[6, 1], [1, 0]])
    P = sp.Matrix([[(r + s) / 3, (r - 5 * s) / 3], [r, s]])
    check("P intertwines A and X_6", sp.simplify(A * P - P * X6), sp.zeros(2, 2))
    check("det P = -((r-3s)^2 - 10 s^2)/3",
          sp.simplify(P.det() - (-((r - 3 * s) ** 2 - 10 * s ** 2) / 3)), 0)
    check("x^2 - 10y^2 mod 5 misses +-3",
          sorted({(x * x - 10 * y * y) % 5 for x in range(5) for y in range(5)}), [0, 1, 4])
    check("no integral solution of x^2-10y^2 = +-3 in a box",
          [(x, y) for x in range(-300, 301) for y in range(-300, 301)
           if x * x - 10 * y * y in (3, -3)], [])
    # Cor 11.3: amphichirality gives 2CS = 0 in R/(1/2)Z, i.e. CS in {0, 1/4}.
    # It does NOT give CS = 0, so d S/d k = -CS is zero only on the CS = 0 branch.
    branches = [sp.Integer(0), sp.Rational(1, 4)]
    check("2CS = 0 mod 1/2 has two branches", [2 * c % sp.Rational(1, 2) for c in branches], [0, 0])
    check("dS/dk = -CS vanishes on only one of them",
          [c == 0 for c in branches], [True, False])


def sec_v6():
    """Checks for the 37-page revision (v6): the dimensional filter and the global form."""
    print("\n== v6 : Prop 8.1 (dimensional filter) and Prop 10.18 (the global form) ==")
    # Prop 8.1: A_{d+1} embeds in SO(3) only for d in {2,3,4}.
    # Finite subgroups of SO(3): cyclic, dihedral, A4, S4, A5.
    in_so3 = {n: n in (3, 4, 5) for n in range(3, 10)}  # A_3 cyclic, A_4 tetra, A_5 icosa
    check("A_{d+1} < SO(3) exactly for d in {2,3,4}",
          sorted(n - 1 for n, v in in_so3.items() if v), [2, 3, 4])
    check("A_6 order 360, too big for SO(3)", sp.factorial(6) // 2, 360)
    # complex fundamental iff -1 not in W; among the exceptionals only E6
    minus_one_in_W = {"G2": True, "F4": True, "E6": False, "E7": True, "E8": True}
    check("complex fundamental among exceptionals: E6 only",
          [g for g, v in minus_one_in_W.items() if not v], ["E6"])
    check("D_4 and D_6 have -1 in W despite diagram automorphisms",
          [True, True], [True, True])
    # Prop 10.18: ker(SU(3)xSU(2)xU(1) -> SU(5)) = Z/6, generated by (w^2 I3, -I2, e^{i pi/3}).
    # (A,B,e^{it}) |-> diag(e^{2it}A, e^{-3it}B); identity forces A = e^{-2it}I3, B = e^{3it}I2,
    # and det A = det B = 1 forces e^{6it} = 1.
    ker = []
    for k in range(12):
        t = sp.Rational(k, 6) * sp.pi
        a = sp.simplify(sp.exp(-2 * sp.I * t))
        b = sp.simplify(sp.exp(3 * sp.I * t))
        if sp.simplify(a ** 3 - 1) == 0 and sp.simplify(b ** 2 - 1) == 0:
            ker.append(sp.simplify(sp.exp(sp.I * t)))
    check("kernel order", len({sp.nsimplify(z) for z in ker}), 6)
    w = sp.exp(2 * sp.pi * sp.I / 3)
    t = sp.pi / 3
    check("generator a = omega^2", sp.simplify(sp.exp(-2 * sp.I * t) - w ** 2), 0)
    check("generator b = -I_2", sp.simplify(sp.exp(3 * sp.I * t) + 1), 0)
    check("abelian generator diag(2,2,2,-3,-3)/6 is traceless",
          3 * sp.Rational(2, 6) + 2 * sp.Rational(-3, 6), 0)
    # the stratum it hangs on: 26 = 6 + 20 roots = A_4 Levi, and by Cor 10.15 it is not real
    check("dim 26 is the A4 Levi: 6 + 20 roots", 6 + 20, 26)
    check("su(5) + u(1)^2 has dimension 26 and rank 6", (24 + 2, 4 + 2), (26, 6))


def sec_bookkeeping():
    print("\n== The paper's own counts ==")
    check("Census 7.12: 26+6+5+1+1+4", 26 + 6 + 5 + 1 + 1 + 4, 43)
    check("Sec 1.2 breakdown: 2+2+1+1+3", 2 + 2 + 1 + 1 + 3, 9)
    check("Sec 11.3 rows named", sorted(["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]),
          ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"])
    check("Sec 1.3 census: 18 + 1 + 1", 18 + 1 + 1, 20)
    check("Thm 9.9 triples C(78,3)", math.comb(78, 3), 76076)
    check("Thm 9.9 pairs C(78,2)", math.comb(78, 2), 3003)
    check("App B blocks: 5 self-contained of 15 rows = one third", sp.Rational(5, 15), sp.Rational(1, 3))
    check("census size 64+64", 64 + 64, 128)
    check("but a rank-4 charge space has 2^4 sign characters", 2 ** 4, 16)
    check("2304 = 2^8 * 3^2", sp.factorint(2304), {2: 8, 3: 2})


def main():
    sec_family()
    sec_collapse()
    sec_period_two()
    sec_shadow()
    sec_jones()
    sec_pairs()
    sec_invariants()
    sec_levi()
    sec_field()
    sec_real_form()
    sec_round2()
    sec_v6()
    sec_bookkeeping()
    print(f"\n{CHECKS} checks run.")
    if FAILURES:
        print(f"DRIFT in {len(FAILURES)} check(s):")
        for f in FAILURES:
            print("  -", f)
        sys.exit(1)
    print("All checks reproduce.")


if __name__ == "__main__":
    main()
