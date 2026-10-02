#!/usr/bin/env python3
"""B1454 -- GENESIS v1.0 (the SM seat's sm:B1516) re-derived on main with main's own code.

    python3 genesis_own.py            # prints the table and writes genesis_own.json; exit 1 if a check fails
    python3 genesis_own.py --quick    # without the SnapPy checks

Written without the seat's `foundations_checks.py` open, and by other routes where one exists:

  G1  the records route: the 12 x 12 positive grid, the two filters separately, and the grid without positivity.
  G2  T-ROOT for both determinants: torsion of H1 = |det(B - I)|, torsion-free hyperbolic matrices in a box; each is
      identified with LR, LP or (LP)^-1 by the CONTINUED FRACTION of its expanding fixed point (purely periodic part
      all ones) and then by an explicit unimodular conjugator found by LINEAR ALGEBRA (X B = T X), not by a box search.
  G3  the order bit: L^-1 (LR) L = RL; P (LR) P = RL with det P = -1; no SL(2,Z) statement rests on P; the based
      fixed-point polynomials.
  G4  the census by BURNSIDE'S LEMMA (binary primitive necklaces up to complement, both letters, two signs) against an
      explicit enumeration and against the counts GENESIS quotes; the torsion at every state.
  G5  SnapPy: the 24 states to length six by name; the orientation-reversing bundles to length six.
  G6  the levels of the root: torsion orders and names; m000 and its orientation double cover; (LP)^2 = LR.
  G7  the fillings (1,0), (0,1), (+-5,1) of m004.
  G8  each of the four inputs is needed (a witness for each).
  G9  the unit shears generate: every hyperbolic det-1 matrix in a box is +- a positive word with both letters, by the
      continued fraction of its fixed point, with a linear-algebra conjugator.
  G10 the metallic family L^m P: its square, and the two torsions by Smith normal form.
  G11 not in GENESIS v1.0 -- main's B14, cited by v1.1 at GM5c: +-LP are the only square roots of LR in GL(2,Z), and
      L_a R_b has an orientation-reversing integer square root exactly when a = b.
"""
import itertools, json, math, sys
from fractions import Fraction

I2 = ((1, 0), (0, 1)); L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1)); P = ((0, 1), (1, 0))


def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def det(A): return A[0][0] * A[1][1] - A[0][1] * A[1][0]
def tr(A): return A[0][0] + A[1][1]
def neg(A): return tuple(tuple(-x for x in r) for r in A)
def inv(A):
    d = det(A); assert d in (1, -1)
    return ((A[1][1] * d, -A[0][1] * d), (-A[1][0] * d, A[0][0] * d))
def power(A, n):
    M = I2
    for _ in range(n): M = mul(M, A)
    return M
def word(w):
    M = I2
    for c in w: M = mul(M, {"L": L, "R": R, "P": P}[c])
    return M
def minus_identity(B): return ((B[0][0] - 1, B[0][1]), (B[1][0], B[1][1] - 1))
def torsion(B): return abs(det(minus_identity(B)))
def hyperbolic(B): return abs(tr(B)) > 2 if det(B) == 1 else tr(B) != 0
def smith(M):
    """invariant factors of a 2 x 2 integer matrix: (d1, d2) with d1 | d2, d1 = gcd of the entries, d1 d2 = |det|"""
    g = math.gcd(math.gcd(abs(M[0][0]), abs(M[0][1])), math.gcd(abs(M[1][0]), abs(M[1][1])))
    return (g, abs(det(M)) // g) if g else (0, 0)
def fixed_poly(A):
    """the Moebius fixed points of tau -> (a tau + b)/(c tau + d): c tau^2 + (d - a) tau - b"""
    (a, b), (c, d) = A
    return (c, d - a, -b)


def conjugator(B, T, want=None):
    """an integer X with X B = T X and det X = +-1 (det X = want if given), from the lattice of solutions"""
    # unknowns x = (x11, x12, x21, x22); X B - T X = 0 is linear; solve over Q by elimination, then scan the lattice
    rows = []
    for i in range(2):
        for j in range(2):
            row = [0] * 4
            for k in range(2):
                row[2 * i + k] += B[k][j]          # (X B)_ij = sum_k X_ik B_kj
                row[2 * k + j] -= T[i][k]          # (T X)_ij = sum_k T_ik X_kj
            rows.append([Fraction(v) for v in row])
    piv = []; r = 0
    for c in range(4):
        p = next((i for i in range(r, 4) if rows[i][c] != 0), None)
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]; rows[r] = [v / rows[r][c] for v in rows[r]]
        for i in range(4):
            if i != r and rows[i][c] != 0: rows[i] = [a - rows[i][c] * b for a, b in zip(rows[i], rows[r])]
        piv.append(c); r += 1
    free = [c for c in range(4) if c not in piv]
    basis = []
    for f in free:
        v = [Fraction(0)] * 4; v[f] = Fraction(1)
        for i, c in enumerate(piv): v[c] = -rows[i][f]
        m = 1
        for x in v: m = m * x.denominator // math.gcd(m, x.denominator)
        v = [int(x * m) for x in v]; g = 0
        for x in v: g = math.gcd(g, abs(x))
        basis.append([x // g for x in v])
    if len(basis) != 2: return None
    # saturate the lattice spanned by the two primitive vectors: integer points of the plane
    best = None
    for s in range(-40, 41):
        for t in range(-40, 41):
            for den in (1, 2, 3, 4, 5, 6):
                v = [s * a + t * b for a, b in zip(*basis)]
                if any(x % den for x in v): continue
                X = ((v[0] // den, v[1] // den), (v[2] // den, v[3] // den))
                d = det(X)
                if d in (1, -1) and (want is None or d == want):
                    assert mul(X, B) == mul(T, X)
                    return X
    return best


def cf_period(B):
    """the purely periodic part of the continued fraction of the expanding fixed point of the hyperbolic B"""
    (a, b), (c, d) = B
    if c == 0: return None
    # fixed points: c x^2 + (d - a) x - b = 0 ; x = (a - d +- sqrt(D)) / (2c), D = (a - d)^2 + 4bc = tr^2 - 4 det
    D = (a - d) ** 2 + 4 * b * c
    s = math.isqrt(D)
    if s * s == D: return None
    # the expanding fixed point is the attracting one of the Moebius action: choose the root with |c x + d| > 1
    lam = lambda sign: abs((a + d + sign * math.sqrt(D)) / 2)
    sign = 1 if lam(1) > 1 else -1
    # x = (P0 + sqrt(D)) / Q0 with Q0 | D - P0^2 : multiply through
    P0, Q0 = (a - d), 2 * c
    if sign == -1: P0, Q0 = -P0, -Q0                     # (P - sqrt D)/Q = (-P + sqrt D)/(-Q)
    if (D - P0 * P0) % Q0: P0, Q0, D2 = P0 * abs(Q0), Q0 * abs(Q0), D * Q0 * Q0
    else: D2 = D
    sD = math.isqrt(D2); seen = {}; terms = []; Pn, Qn = P0, Q0
    while (Pn, Qn) not in seen:
        seen[(Pn, Qn)] = len(terms)
        an = (Pn + sD) // Qn if Qn > 0 else (Pn + sD + 1) // Qn
        terms.append(an); Pn = an * Qn - Pn; Qn = (D2 - Pn * Pn) // Qn
    return terms[seen[(Pn, Qn)]:]


def period_word(per):
    """the positive word L^a1 R^a2 ... of an even number of partial quotients"""
    if len(per) % 2: per = per * 2
    return "".join(("L" if i % 2 == 0 else "R") * a for i, a in enumerate(per))


def g1():
    grid = [(a, b) for a in range(1, 13) for b in range(1, 13)]
    B = lambda a, b: mul(((1, a), (0, 1)), ((1, 0), (b, 1)))
    hyp = [ab for ab in grid if hyperbolic(B(*ab))]
    tf = [ab for ab in grid if torsion(B(*ab)) == 1]
    mt = min(tr(B(*ab)) for ab in hyp); mn = [ab for ab in hyp if tr(B(*ab)) == mt]
    signed = [(a, b) for a in range(-12, 13) for b in range(-12, 13) if a and b]
    tfs = [ab for ab in signed if torsion(B(*ab)) == 1 and hyperbolic(B(*ab))]
    X = conjugator(B(-1, -1), mul(L, R), want=1)
    ok = (len(hyp) == 144 and tf == [(1, 1)] and mn == [(1, 1)] and mt == 3 and B(1, 1) == ((2, 1), (1, 1))
          and sorted(tfs) == [(-1, -1), (1, 1)] and X is not None
          and all(det(B(*ab)) == 1 and tr(B(*ab)) == 2 + ab[0] * ab[1] and det(minus_identity(B(*ab))) == -ab[0] * ab[1] for ab in signed))
    return ok, dict(grid=len(grid), hyperbolic=len(hyp), torsion_free=tf, minimal_trace=mn, trace=mt, without_positivity=sorted(tfs),
                    conjugator_of_B_minus1_minus1_to_LR=X, non_hyperbolic_torsion_free=sorted(ab for ab in signed if torsion(B(*ab)) == 1 and not hyperbolic(B(*ab))))


def g2(box=5):
    rng = range(-box, box + 1); LR = mul(L, R); LP = mul(L, P); LPi = inv(LP)
    n = {1: 0, -1: 0}; tf = []; formula = True
    for a, b, c, d in itertools.product(rng, repeat=4):
        B = ((a, b), (c, d)); e = det(B)
        if e not in (1, -1) or not hyperbolic(B): continue
        n[e] += 1
        formula &= torsion(B) == (abs(2 - tr(B)) if e == 1 else abs(tr(B)))
        if torsion(B) == 1: tf.append(B)
    out = {"LR": 0, "LP": 0, "LP^-1": 0}; allones = True; conj = True
    for B in tf:
        per = cf_period(B); allones &= per is not None and set(per) == {1}
        T, name = (LR, "LR") if det(B) == 1 else ((LP, "LP") if tr(B) == 1 else (LPi, "LP^-1"))
        conj &= (det(B), tr(B)) == (det(T), tr(T)) and conjugator(B, T) is not None
        out[name] += 1
    ok = formula and allones and conj and all(det(B) == -1 or tr(B) == 3 for B in tf) and all(det(B) == 1 or abs(tr(B)) == 1 for B in tf)
    return ok, dict(box=box, hyperbolic_det_plus=n[1], hyperbolic_det_minus=n[-1], torsion_free=len(tf), by_class=out,
                    formula_holds=formula, fixed_points_all_golden=allones, every_one_conjugated=conj,
                    traces_of_torsion_free_det_plus=sorted({tr(B) for B in tf if det(B) == 1}),
                    traces_of_torsion_free_det_minus=sorted({tr(B) for B in tf if det(B) == -1}))


def g3():
    LR, RL = mul(L, R), mul(R, L)
    by_L = mul(mul(inv(L), LR), L) == RL; by_P = mul(mul(P, LR), P) == RL
    K = mul(mul(L, LR), inv(L))
    polys = dict(LR=fixed_poly(LR), RL=fixed_poly(RL), K=fixed_poly(K))
    ok = by_L and by_P and det(P) == -1 and det(L) == 1 and polys == dict(LR=(1, -1, -1), RL=(1, 1, -1), K=(1, -3, 1)) \
        and mul(mul(P, L), P) == R and mul(mul(L, P), mul(L, P)) == LR and mul(mul(P, L), mul(P, L)) == RL
    return ok, dict(conjugate_by_L=by_L, conjugate_by_P=by_P, det_P=det(P), fixed_point_polynomials=polys,
                    LP_squared_is_LR=mul(mul(L, P), mul(L, P)) == LR, PL_squared_is_RL=mul(mul(P, L), mul(P, L)) == RL)


def mobius(n):
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r


def states(n):
    seen = set()
    for bits in itertools.product("LR", repeat=n):
        w = "".join(bits)
        if "L" not in w or "R" not in w: continue
        if any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n)): continue
        sw = w.translate(str.maketrans("LR", "RL"))
        seen.add(min(min(x[i:] + x[:i] for i in range(n)) for x in (w, sw)))
    return sorted(seen)


def count_formula(n):
    """Burnside on the aperiodic strings under rotation and the letter swap.  Rotation acts freely on them; the swap
    composed with a rotation fixes an aperiodic string only for the rotation by n/2, and those strings are u.swap(u).
    So the number of classes is (a + b) / (2n): a = aperiodic strings of length n (Moebius), b = aperiodic strings of
    the form u.swap(u) = sum over d | n/2 with (n/2)/d odd of mu((n/2)/d) 2^d.  A constant word is never aperiodic
    for n > 1, so both letters occur."""
    a = sum(mobius(n // d) * 2 ** d for d in range(1, n + 1) if n % d == 0)
    b = 0
    if n % 2 == 0:
        h = n // 2
        b = sum(mobius(h // d) * 2 ** d for d in range(1, h + 1) if h % d == 0 and (h // d) % 2 == 1)
    assert (a + b) % (2 * n) == 0
    return (a + b) // (2 * n)


def g4(maxlen=12, quoted=(2, 2, 4, 6, 10, 18, 32, 56, 102, 186, 340)):
    counts, formula, tfree, mintr = [], [], [], {}
    for n in range(2, maxlen + 1):
        st = states(n); counts.append(2 * len(st)); formula.append(2 * count_formula(n))
        for w in st:
            for eps in (1, -1):
                B = word(w) if eps == 1 else neg(word(w))
                assert torsion(B) == abs(2 - eps * tr(word(w)))
                if torsion(B) == 1: tfree.append(("+" if eps == 1 else "-") + w)
        mintr[n] = min(tr(word(w)) for w in st)
    ok = tuple(counts) == tuple(quoted) and counts == formula and sum(counts) == 758 and tfree == ["+LR"]
    return ok, dict(counts=counts, by_formula=formula, total=sum(counts), torsion_free=tfree, minimal_trace_by_length=mintr)


def g9(box=5):
    rng = range(-box, box + 1); n = 0; bad = []; lengths = {}
    for a, b, c, d in itertools.product(rng, repeat=4):
        B = ((a, b), (c, d))
        if det(B) != 1 or abs(tr(B)) <= 2: continue
        n += 1; eps = 1 if tr(B) > 2 else -1; Bp = B if eps == 1 else neg(B)
        per = cf_period(Bp)
        if per is None: bad.append(B); continue
        w = period_word(per); W = word(w); k = 1; T = W
        while tr(T) < tr(Bp) and k < 40: T = mul(T, W); k += 1
        X = conjugator(Bp, T) if tr(T) == tr(Bp) else None
        if X is None and tr(T) == tr(Bp): X = conjugator(Bp, inv(T))
        if X is None or "L" not in w or "R" not in w: bad.append(B); continue
        lengths[len(w) * k] = lengths.get(len(w) * k, 0) + 1
    return not bad and n > 0, dict(box=box, hyperbolic_det_plus=n, not_reached=len(bad), word_lengths=dict(sorted(lengths.items())))


def g10(mmax=8):
    rows = []; ok = True
    for m in range(1, mmax + 1):
        M = mul(power(L, m), P); S = mul(power(L, m), power(R, m))
        r = dict(m=m, matrix=M, square_is_LmRm=mul(M, M) == S, det=det(M), trace=tr(M),
                 torsion=smith(minus_identity(M)), torsion_of_square=smith(minus_identity(S)))
        ok &= r["square_is_LmRm"] and M == ((m, 1), (1, 0)) and r["torsion"] == (1, m) and r["torsion_of_square"] == (m, m)
        rows.append(r)
    return ok, dict(rows=rows, torsion_free_members=[r["m"] for r in rows if r["torsion"] == (1, 1)])


def g8_algebra():
    E = ((1, 1), (-1, 0)); out = {}
    out["order_six_trace_one"] = dict(matrix=E, det=det(E), trace=tr(E), order=next(k for k in range(1, 13) if power(E, k) == I2),
                                      torsion=torsion(E), hyperbolic=hyperbolic(E), char_poly="t^2 - t + 1")
    out["parabolic_L"] = dict(trace=tr(L), smith=smith(minus_identity(L)), hyperbolic=hyperbolic(L))
    A = mul(L, R); out["closed_torus_bundle_of_LR"] = dict(smith=smith(minus_identity(A)), note="H1 = Z + coker(A - I) = Z; Sol, not hyperbolic (G7)")
    ok = (out["order_six_trace_one"]["order"] == 6 and out["order_six_trace_one"]["torsion"] == 1 and not hyperbolic(E)
          and out["parabolic_L"]["smith"] == (1, 0) and not hyperbolic(L) and out["closed_torus_bundle_of_LR"]["smith"] == (1, 1))
    return ok, out


def g11(box=8, grid=12):
    """main's B14: the square roots of LR in GL(2,Z), and which L_a R_b have an orientation-reversing integer root.
    X^2 = tr(X) X - det(X) I gives X = (B + det(X) I) / tr(X) with tr(X)^2 = tr(B) + 2 det(X): exact, no search needed;
    the box enumeration is the control."""
    A = mul(L, R); exact = []
    for e in (1, -1):
        t2 = tr(A) + 2 * e; t = math.isqrt(t2) if t2 >= 0 else -1
        if t > 0 and t * t == t2:
            M = ((A[0][0] + e, A[0][1]), (A[1][0], A[1][1] + e))
            if all(v % t == 0 for r in M for v in r):
                X = tuple(tuple(v // t for v in r) for r in M)
                if mul(X, X) == A and det(X) == e: exact += [X, neg(X)]
    boxed = [X for X in (((a, b), (c, d)) for a, b, c, d in itertools.product(range(-box, box + 1), repeat=4))
             if det(X) in (1, -1) and mul(X, X) == A]
    diag = []
    for a in range(1, grid + 1):
        for b in range(1, grid + 1):
            B = mul(((1, a), (0, 1)), ((1, 0), (b, 1))); t = math.isqrt(a * b)      # det X = -1: tr(X)^2 = ab
            if t * t != a * b: continue
            M = minus_identity(B)
            if all(v % t == 0 for r in M for v in r):
                X = tuple(tuple(v // t for v in r) for r in M)
                if mul(X, X) == B and det(X) == -1: diag.append((a, b))
    LP = mul(L, P)
    ok = sorted(exact) == sorted(boxed) == sorted([LP, neg(LP)]) and diag == [(a, a) for a in range(1, grid + 1)]
    return ok, dict(square_roots_of_LR=sorted(exact), in_the_box=sorted(boxed), LP=LP, orientation_reversing_roots_of_LaRb=diag)


NAMES24 = ["m004", "m003", "m009", "m010", "m022", "m023", "m135", "m136", "m039", "m040", "m234", "m235", "m369", "m370",
           "s000", "s001", "s298", "s299", "s463", "s464", "s639", "s640", "s891", "s892"]


def snappy_checks():
    import snappy
    out = {}; ok = True

    def ident(M):
        for N in M.identify():
            return N.name()
        return None

    def bundle(code):
        return snappy.Manifold(code)
    # G5: the 24 states to length six
    found = {}; tets = True
    for n in range(2, 7):
        for w in states(n):
            for eps, s in ((1, "+"), (-1, "-")):
                M = bundle("b+" + s + w)
                nm = ident(M); found[s + w] = nm
                tets &= M.num_tetrahedra() == n
                tors = [c for c in M.homology().elementary_divisors() if c != 0]
                want = abs(2 - eps * tr(word(w)))
                got = 1
                for c in tors: got *= c
                ok &= got == want
    out["states_to_length_six"] = found; out["tetrahedra_equal_word_length"] = tets; ok &= tets
    ok &= sorted(v for v in found.values()) == sorted(NAMES24) and len(found) == 24
    # orientation-reversing bundles to length six: which are torsion-free
    nonor = {}; free = []; codes = 0; orientable = 0; formula = True
    for n in range(1, 7):
        for bits in itertools.product("LR", repeat=n):
            w = "".join(bits)
            for s, eps in (("+", 1), ("-", -1)):
                M = bundle("b-" + s + w); codes += 1
                if M.is_orientable(): orientable += 1; continue
                div = [c for c in M.homology().elementary_divisors() if c != 0]
                got = 1
                for c in div: got *= c
                B = mul(word(w), P) if eps == 1 else neg(mul(word(w), P))        # an orientation-reversing monodromy of the same word
                formula &= got in (abs(tr(B)), abs(tr(mul(P, word(w)))))
                key = ident(M) or ("b-" + s + w)
                nonor[key] = div
                if not div: free.append(key)
    out["orientation_reversing_codes_read"] = codes; out["orientable_among_them"] = orientable
    out["distinct_manifolds"] = len(nonor); out["torsion_free_among_them"] = sorted(set(free))
    out["torsion_is_abs_trace_of_wP"] = formula
    ok &= sorted(set(free)) == ["m000"] and orientable == 0 and codes == 252
    # G6: the levels of the root
    M = snappy.Manifold("m004"); lev = {}
    A = mul(L, R)
    for n in range(1, 13): lev[n] = abs(2 - tr(power(A, n)))
    names = {}
    for n in range(2, 7):
        cov = [C for C in M.covers(n, cover_type="cyclic")]
        names[n] = sorted({ident(C) for C in cov})
    out["torsion_orders_of_levels"] = lev; out["level_names"] = names
    ok &= [lev[n] for n in range(1, 7)] == [1, 5, 16, 45, 121, 320]
    ok &= names == {2: ["m206"], 3: ["s961"], 4: ["t12839"], 5: ["o10_150696"], 6: ["otet12_00013"]}
    G = snappy.Manifold("m000"); dc = G.orientation_cover()
    out["m000"] = dict(orientable=G.is_orientable(), volume=float(G.volume()), double_cover=ident(dc), tetrahedra=G.num_tetrahedra())
    ok &= (not G.is_orientable()) and ident(dc) == "m004" and abs(float(G.volume()) * 2 - float(M.volume())) < 1e-9
    m3 = snappy.Manifold("m003"); out["m003_torsion"] = [c for c in m3.homology().elementary_divisors() if c != 0]
    ok &= out["m003_torsion"] == [5] and ident(bundle("b+-LR")) == "m003"
    c4 = {ident(C) for C in M.covers(2)}; c3 = {ident(C) for C in m3.covers(2)}
    out["double_covers"] = dict(m004=sorted(c4), m003=sorted(c3)); ok &= bool(c4 & c3)
    # G7: the fillings
    fill = {}
    for sl in ((1, 0), (0, 1), (5, 1), (-5, 1)):
        F = snappy.Manifold("m004"); F.dehn_fill(sl)
        g = F.fundamental_group()
        fill[str(sl)] = dict(homology=str(F.homology()), generators=g.num_generators(), relators=g.relators(),
                             volume=float(F.volume()), solution=F.solution_type())
    out["fillings"] = fill
    ok &= fill["(1, 0)"]["generators"] == 0 and fill["(1, 0)"]["homology"] == "0"
    ok &= fill["(0, 1)"]["homology"] == "Z" and fill["(0, 1)"]["volume"] < 1e-6 and "positively oriented" not in fill["(0, 1)"]["solution"]
    ok &= all(fill[k]["homology"] == "Z/5" and abs(fill[k]["volume"] - 0.98137) < 1e-4 for k in ("(5, 1)", "(-5, 1)"))
    # G8: a knot complement that is hyperbolic and torsion-free without the carrier
    K = snappy.Manifold("5_2"); out["5_2"] = dict(homology=str(K.homology()), volume=float(K.volume()), solution=K.solution_type())
    ok &= str(K.homology()) == "Z" and K.volume() > 2 and "positively oriented" in K.solution_type()
    return ok, out


def main(argv):
    checks = [("G1 records route", g1), ("G2 T-ROOT", g2), ("G3 order bit", g3), ("G4 census", g4), ("G8 necessity (algebra)", g8_algebra),
              ("G9 unit shears generate", g9), ("G10 metallic family", g10),
              ("G11 the swap (main B14)", g11)]
    if "--quick" not in argv: checks.append(("G5-G7 SnapPy", snappy_checks))
    res = {}; allok = True
    for name, f in checks:
        ok, data = f(); res[name] = dict(ok=bool(ok), data=data); allok &= bool(ok)
        print("%-28s %s" % (name, "PASS" if ok else "FAIL"))
    if "--no-write" not in argv:
        import os
        json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "genesis_own.json"), "w"), indent=1, default=str)
    print("VERDICT genesis-own: %s" % ("PASS" if allok else "FAIL"))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
