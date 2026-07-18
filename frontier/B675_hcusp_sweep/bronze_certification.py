"""B675 follow-on — THE BRONZE EXACT CERTIFICATION.

Upgrades the banked corroborated-not-certified bronze claim (b675_hcusp.py
Part 4) to a certified one.  Claim under certification: the bronze object
(census s464 = the b++LLLRRR punctured-torus-bundle member; bronze =
metallic m = 3) has cusp shape tau (SnapPy default peripheral basis)
purely imaginary with u = (Im tau)^2 satisfying

    192 u^4 - 112 u^3 + 20 u^2 - 21 u + 7 = 0,

irreducible over Q, Galois group S4, disc primes {2, 7, 617}, hence
[Q(tau) : Q] = 8 and (Kronecker-Weber) tau lies in NO cyclotomic field.

METHOD (exact end-to-end):
 1. The gluing + completeness equations of the triangulation are exact
    integer data (SnapPy rect rows).  They are turned into polynomial
    equations over Q and ELIMINATED (rational linear solves + sympy
    resultants + gcd, all over Q) down to a univariate polynomial; its
    numerically selected irreducible factor p8 defines the shape field
    K = Q[t]/(p8).
 2. All six tetrahedron shapes are expressed EXACTLY in K, and ALL
    original gluing/completeness equations are re-verified EXACTLY in K
    (this discharges every numerics-guided branch/factor selection made
    during the elimination).
 3. The geometric root of p8 is certified by EXACT rational rectangle
    arithmetic on sympy's rigorous (Sturm-based) root isolation:
    Im z_i > 0 for all six shapes => positively oriented solution of
    gluing + completeness => THE complete hyperbolic structure (Mostow).
 4. The cusp cross-section is developed EXACTLY in K through SnapPy's
    generic (arithmetic-agnostic) ComplexCuspCrossSection, using the
    triangulation's own peripheral-curve data (= the SnapPy default
    basis); the development is checked exactly (all horotriangle side
    gluings match).  tau = conj(longitude/meridian translation) — the
    SnapPy kernel convention.
 5. Minimal polynomials of xi = l/m and v = -xi^2 over Q via resultants.
 6. Re tau = 0 EXACT: v is exactly a root of its quartic; rigorous
    rectangle arithmetic pins v to the unique REAL positive root
    compatible with its isolating box => tau = i sqrt(u) exactly.
 7. Galois: resolvent cubic + discriminant, all exact.
 8. The second triangulation (s464 census) is run through the same
    exact pipeline; u' is pinned to the unique compatible real root of
    the REVERSED quartic and u * u' = 1 is certified at root level by
    exact interval inversion + root isolation.

Floats appear ONLY as guidance for branch/factor/root selection; every
selected object is subsequently verified by exact rational arithmetic.
No file I/O; census names only.
"""
import functools
import time
import warnings
from fractions import Fraction as Fr

warnings.filterwarnings("ignore")

import sympy as sp
from sympy import Poly, symbols

T0 = time.time()
BAR = "=" * 72


def sec(t):
    print("\n" + BAR + "\n" + t + "\n" + BAR, flush=True)


X = symbols('X')
uu = symbols('u')

QUARTIC = 192 * uu**4 - 112 * uu**3 + 20 * uu**2 - 21 * uu + 7
OCTIC = 192 * X**8 + 112 * X**6 + 20 * X**4 + 21 * X**2 + 7

# ===========================================================================
# Exact number-field arithmetic  K = Q[t]/(p)  (dense Fraction vectors)
# ===========================================================================


def make_field(mod_coeffs_desc):
    """mod_coeffs_desc: leading-first Fraction list of the (irreducible)
    modulus.  Returns the element class."""
    MOD = [Fr(c) for c in mod_coeffs_desc]
    DEG = len(MOD) - 1

    def reduce_desc(a):
        a = a[:]
        db = DEG
        while len(a) - 1 >= db and any(x != 0 for x in a):
            if a[0] == 0:
                a.pop(0)
                continue
            q = a[0] / MOD[0]
            for i in range(db + 1):
                a[i] -= q * MOD[i]
            a.pop(0)
        return a

    class ANF:
        __slots__ = ('c',)
        deg = DEG
        mod = MOD

        def __init__(s, c):
            s.c = c

        @staticmethod
        def const(q):
            q = Fr(q.p, q.q) if isinstance(q, sp.Rational) else Fr(q)
            return ANF([q] + [Fr(0)] * (DEG - 1))

        @staticmethod
        def gen():
            return ANF([Fr(0), Fr(1)] + [Fr(0)] * (DEG - 2))

        def _co(s, o):
            return o if isinstance(o, ANF) else ANF.const(o)

        def __add__(s, o):
            o = s._co(o)
            return ANF([a + b for a, b in zip(s.c, o.c)])
        __radd__ = __add__

        def __sub__(s, o):
            o = s._co(o)
            return ANF([a - b for a, b in zip(s.c, o.c)])

        def __rsub__(s, o):
            return s._co(o) - s

        def __neg__(s):
            return ANF([-a for a in s.c])

        def __mul__(s, o):
            o = s._co(o)
            prod = [Fr(0)] * (2 * DEG - 1)
            for i, a in enumerate(s.c):
                if a == 0:
                    continue
                for j, b in enumerate(o.c):
                    if b != 0:
                        prod[i + j] += a * b
            rem = reduce_desc(prod[::-1])[::-1]
            return ANF([rem[i] if i < len(rem) else Fr(0)
                        for i in range(DEG)])
        __rmul__ = __mul__

        def __pow__(s, n):
            r = ANF.const(1)
            for _ in range(n):
                r = r * s
            return r

        def inv(s):
            # solve s * x = 1 by exact Gaussian elimination on the
            # multiplication matrix (field => always invertible for != 0)
            cols = []
            for k in range(DEG):
                b = ANF([Fr(1) if i == k else Fr(0) for i in range(DEG)])
                cols.append((s * b).c)
            A = [[cols[j][i] for j in range(DEG)] +
                 [Fr(1) if i == 0 else Fr(0)] for i in range(DEG)]
            for c in range(DEG):
                piv = next(r for r in range(c, DEG) if A[r][c] != 0)
                A[c], A[piv] = A[piv], A[c]
                pv = A[c][c]
                A[c] = [v / pv for v in A[c]]
                for r in range(DEG):
                    if r != c and A[r][c] != 0:
                        f = A[r][c]
                        A[r] = [v - f * w for v, w in zip(A[r], A[c])]
            return ANF([A[r][DEG] for r in range(DEG)])

        def __truediv__(s, o):
            return s * s._co(o).inv()

        def __rtruediv__(s, o):
            return s._co(o) * s.inv()

        def __eq__(s, o):
            return s.c == s._co(o).c

        def is_zero(s):
            return all(a == 0 for a in s.c)

        def __hash__(s):
            return hash(tuple(s.c))

        def __repr__(s):
            return "ANF[" + ", ".join(str(a) for a in s.c) + "]"

        # --- stubs so SnapPy's generic cusp cross-section code runs; ---
        # --- they poison ONLY the (unused) triangle 'area' attribute ---
        def parent(s):
            return lambda q: ANF.const(q)

        def imag(s):
            return ANF.const(0)

        def __abs__(s):
            return ANF.const(0)

    return ANF


def eval_expr(expr, env, F):
    """evaluate a sympy rational expression exactly in the field F,
    env: {symbol: F-element}."""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    vs = sorted(expr.free_symbols, key=str)

    def poly_val(e):
        if not vs:
            return F.const(sp.Rational(e))
        p = Poly(e, *vs)
        tot = F.const(0)
        for mono, coef in p.terms():
            term = F.const(sp.Rational(coef))
            for v, ex in zip(vs, mono):
                for _ in range(ex):
                    term = term * env[v]
            tot = tot + term
        return tot

    return poly_val(num) / poly_val(den)


def anf_to_t_expr(a, t):
    return sum(sp.Rational(x.numerator, x.denominator) * t**i
               for i, x in enumerate(a.c))


def anf_num(a, tv):
    return sum(complex(x) * tv**i for i, x in enumerate(a.c))


# ===========================================================================
# Exact rational interval arithmetic (rectangles)  — for root certification
# ===========================================================================
class RI:
    __slots__ = ('lo', 'hi')

    def __init__(s, lo, hi=None):
        s.lo = Fr(lo)
        s.hi = Fr(hi if hi is not None else lo)

    def __add__(s, o):
        return RI(s.lo + o.lo, s.hi + o.hi)

    def __sub__(s, o):
        return RI(s.lo - o.hi, s.hi - o.lo)

    def __neg__(s):
        return RI(-s.hi, -s.lo)

    def __mul__(s, o):
        ps = (s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi)
        return RI(min(ps), max(ps))

    def disjoint(s, o):
        return s.hi < o.lo or o.hi < s.lo

    def __repr__(s):
        return f"[{s.lo}, {s.hi}]"


class CI:
    __slots__ = ('re', 'im')

    def __init__(s, re, im):
        s.re = re
        s.im = im

    def __add__(s, o):
        return CI(s.re + o.re, s.im + o.im)

    def __mul__(s, o):
        return CI(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)

    def disjoint(s, o):
        return s.re.disjoint(o.re) or s.im.disjoint(o.im)


def anf_at_box(a, Tci):
    """Horner-evaluate the Fraction-coefficient polynomial a (ANF) on the
    complex rectangle Tci — fully rigorous rational arithmetic."""
    res = CI(RI(0), RI(0))
    for c in reversed(a.c):
        res = res * Tci
        res = CI(res.re + RI(c), res.im)
    return res


def to_fr(x):
    r = sp.Rational(x)
    return Fr(int(r.p), int(r.q))


def root_box(r, digits):
    """rigorous rational rectangle for a sympy CRootOf, refined to
    ~10^-digits.  Sturm/collins isolation => the box is certified."""
    d = sp.Rational(1, 10**digits)
    try:
        r.eval_rational(d, d)
    except TypeError:
        r.eval_rational(d)
    iv = r._get_interval()
    if hasattr(iv, 'ax'):
        return CI(RI(to_fr(iv.ax), to_fr(iv.bx)),
                  RI(to_fr(iv.ay), to_fr(iv.by)))
    return CI(RI(to_fr(iv.a), to_fr(iv.b)), RI(0))


# ===========================================================================
# The exact elimination engine
# ===========================================================================


def rect_polys(Mfd, Z, presub=None):
    """the gluing+completeness rows as cleared polynomials over Q
    (exact integer data), optionally with a branch pre-substitution."""
    rows = Mfd.gluing_equations("rect")
    out = []
    for a, b, c in rows:
        e = sp.Integer(1)
        for i in range(len(Z)):
            e *= Z[i]**a[i] * (1 - Z[i])**b[i]
        if presub:
            e = e.subs(presub)
        p = sp.expand(sp.numer(sp.together(e - c)))
        out.append(p)
    return rows, out


def vanishing_factors(exprs, pt, tol=1e-10):
    """numerics-GUIDED selection of the factor of each expression that
    vanishes at the approximate geometric point, evaluated at ~40 digits
    (discharged later by the exact in-field verification)."""
    sel = []
    for e in exprs:
        if e == 0:
            continue
        for f, _m in sp.factor_list(e)[1]:
            if abs(complex(sp.N(f.subs(pt), 20))) < tol:
                f = sp.expand(f)
                if f not in sel:
                    sel.append(f)
    return sel


def eliminate(polys, pt, allvars):
    """rational linear solves + factor selection + resultants + gcd,
    down to a univariate.  Each round keeps only the geometric factors
    (numerics-guided, discharged later) and prefers the SMALLEST factor
    for the next rational solve.  Returns (sol dict, univariate variable,
    univariate expr, kept factor list at the 2-var stage, remaining)."""
    sol = {}
    remaining = set(v for v in allvars
                    if any(v in e.free_symbols for e in polys))
    active = [e for e in polys if e != 0]
    while True:
        active = vanishing_factors(active, pt)
        active.sort(key=lambda e: (sp.total_degree(e), sp.count_ops(e)))
        found = None
        for e in active:
            for v in sorted(e.free_symbols & remaining, key=str):
                p = Poly(e, v)
                if p.degree() == 1:
                    A_, B_ = p.all_coeffs()
                    if abs(complex(sp.N(sp.sympify(A_).subs(pt), 20))) \
                            < 1e-10:
                        continue
                    found = (v, sp.cancel(-sp.sympify(B_) / A_))
                    break
            if found:
                break
        if found is None:
            break
        v, expr = found
        sol[v] = expr
        remaining.discard(v)
        active = [sp.expand(sp.numer(sp.together(sp.cancel(
            f.subs(v, expr))))) for f in active]
        active = [e for e in active if e != 0]
        for k in list(sol):
            sol[k] = sp.cancel(sol[k].subs(v, expr))
        print(f"    solved {v} rationally; remaining "
              f"{sorted(remaining, key=str)}  [{time.time()-T0:.0f}s]",
              flush=True)

    rem = sorted(remaining, key=str)
    print(f"    kept factors (final stage): "
          f"{[(sp.total_degree(f), sorted(f.free_symbols, key=str)) for f in active]}",
          flush=True)
    tvar = rem[0]
    stages = []          # [(eliminated var, factor list BEFORE elimination)]
    current = active
    curvars = rem[:]
    while len(curvars) > 1:
        evar = curvars[-1]
        stages.append((evar, current))
        withv = sorted([f for f in current if evar in f.free_symbols],
                       key=lambda e: (sp.total_degree(e), sp.count_ops(e)))
        rest = [f for f in current if evar not in f.free_symbols]
        res = []
        for cap in (24, 32, 44, 99):
            for i in range(len(withv)):
                for j in range(i + 1, len(withv)):
                    if (sp.total_degree(withv[i]) +
                            sp.total_degree(withv[j]) > cap):
                        continue
                    r = sp.resultant(withv[i], withv[j], evar)
                    if r != 0 and r not in res:
                        res.append(sp.expand(r))
                        print(f"    resultant (eliminating {evar}) from "
                              f"tdeg ({sp.total_degree(withv[i])}, "
                              f"{sp.total_degree(withv[j])})  "
                              f"[{time.time()-T0:.0f}s]", flush=True)
            if len(res) >= min(2, len(withv) - 1):
                break
        current = vanishing_factors(res + rest, pt)
        curvars.pop()
        print(f"    after eliminating {evar}: kept "
              f"{[(sp.total_degree(f), sorted(f.free_symbols, key=str)) for f in current]}"
              f"  [{time.time()-T0:.0f}s]", flush=True)
    gg = functools.reduce(sp.gcd, current) if len(current) > 1 \
        else current[0]
    return sol, tvar, sp.expand(gg), stages


def field_solve(facs, evar, env, F):
    """express evar exactly in K via the K[evar]-Euclidean gcd of the
    stage factors (the geometric point is a common root; the gcd of the
    branch is linear).  env maps every other variable to its exact
    K-value."""
    def kpoly(f):
        p = Poly(f, evar)
        cs = []
        for c in p.all_coeffs():
            c = sp.sympify(c)
            cs.append(eval_expr(c, {k: env[k] for k in c.free_symbols}, F)
                      if c.free_symbols else F.const(sp.Rational(c)))
        return cs

    def kmod(A, B):
        A = A[:]
        while B and B[0].is_zero():
            B = B[1:]
        db = len(B) - 1
        while len(A) - 1 >= db and not all(x.is_zero() for x in A):
            if A[0].is_zero():
                A.pop(0)
                continue
            q = A[0] / B[0]
            for i in range(db + 1):
                A[i] = A[i] - q * B[i]
            A.pop(0)
        while len(A) > 1 and A[0].is_zero():
            A.pop(0)
        return A

    polys = [kpoly(f) for f in facs if evar in f.free_symbols]
    g = polys[0]
    for h in polys[1:]:
        A, B = g, h
        while len(B) > 1 or (len(B) == 1 and not B[0].is_zero()):
            A, B = B, kmod(A, B)
            if len(A) == 1 and A[0].is_zero():
                break
        g = A
        if len(g) == 2:
            break
    assert len(g) == 2, f"K[{evar}] gcd not linear: degree {len(g)-1}"
    return -g[1] / g[0]


# ===========================================================================
# One full exact pipeline for one triangulation
# ===========================================================================


def certify_triangulation(name, presub_note, presub):
    import snappy
    sec(f"PIPELINE — {name}" + (f"   [branch: {presub_note}]"
                                if presub_note else ""))
    Mfd = snappy.Manifold(name)
    n = Mfd.num_tetrahedra()
    Z = symbols(f'z0:{n}')
    # ~45-digit guidance point (guidance only; never load-bearing)
    hp = Mfd.high_precision().tetrahedra_shapes('rect')
    pt = {Z[i]: (sp.Float(str(z.real()).replace(" ", ""), 45) +
                 sp.I * sp.Float(str(z.imag()).replace(" ", ""), 45))
          for i, z in enumerate(hp)}
    rows, polys = rect_polys(Mfd, Z, presub)
    print(f"  {n} tetrahedra; {len(rows)} rect rows (exact integer data); "
          f"solution type: {Mfd.solution_type()}", flush=True)

    # ---- exact elimination ----
    print("  elimination (rational solves + resultants + gcd over Q):",
          flush=True)
    sol, tvar, univ, stages = eliminate(polys, pt, Z)
    fl = sp.factor_list(univ)[1]
    print(f"    univariate gcd in {tvar}: factors "
          f"{[(sp.expand(f), m) for f, m in fl]}", flush=True)
    # numerics-guided selection of the geometric factor (discharged below)
    p8 = None
    for f, _m in fl:
        if abs(complex(sp.N(f.subs(pt), 20))) < 1e-10:
            p8 = sp.expand(f)
    assert p8 is not None
    P8 = Poly(p8, tvar)
    print(f"    geometric factor p(t) = {p8}")
    print(f"    degree {P8.degree()}, irreducible over Q: "
          f"{P8.is_irreducible}", flush=True)
    assert P8.is_irreducible

    # ---- the field and the exact shapes ----
    F = make_field([sp.Rational(c) for c in P8.all_coeffs()])
    tK = F.gen()
    env = {tvar: tK}
    for evar, facs in reversed(stages):
        env[evar] = field_solve(facs, evar, env, F)
        print(f"    {evar} expressed exactly in K (linear K[{evar}]-gcd "
              f"of the stage factors)  [{time.time()-T0:.0f}s]", flush=True)
    for v, e in sol.items():
        env[v] = eval_expr(e, {k: env[k] for k in e.free_symbols}, F)
    if presub:
        for v, e in presub.items():
            env[v] = env[e]
    shapesK = [env[Z[i]] for i in range(n)]

    # ---- EXACT verification of ALL original equations ----
    ok_all = True
    for a, b, c in rows:
        Nm = F.const(1)
        Dn = F.const(1)
        for i in range(n):
            zi = shapesK[i]
            wi = 1 - zi
            for _ in range(abs(a[i])):
                if a[i] > 0:
                    Nm = Nm * zi
                else:
                    Dn = Dn * zi
            for _ in range(abs(b[i])):
                if b[i] > 0:
                    Nm = Nm * wi
                else:
                    Dn = Dn * wi
        ok = (Nm - F.const(c) * Dn).is_zero()
        ok_all = ok_all and ok
    print(f"  ALL {len(rows)} gluing+completeness equations hold EXACTLY "
          f"in K: {ok_all}", flush=True)
    assert ok_all

    # ---- certified geometric root (positivity by exact rectangles) ----
    roots = P8.all_roots()
    geo_idx, status = None, []
    for k, r in enumerate(roots):
        if r.is_real:
            status.append((k, "real t => Im z = 0 exactly => NOT pos."))
            continue
        verdict = None
        for digits in (25, 50, 100):
            Tci = root_box(r, digits)
            signs = []
            for a in shapesK:
                Rz = anf_at_box(a, Tci)
                if Rz.im.lo > 0:
                    signs.append(1)
                elif Rz.im.hi < 0:
                    signs.append(-1)
                else:
                    signs.append(0)
            if 0 not in signs:
                verdict = "ALL Im z_i > 0 (POSITIVELY ORIENTED)" \
                    if all(s == 1 for s in signs) else \
                    f"decided, not all positive {signs}"
                break
        status.append((k, verdict or "undecided at cap"))
        if verdict and verdict.startswith("ALL"):
            geo_idx = k
    for k, s in status:
        print(f"    root {k}: {s}", flush=True)
    assert geo_idx is not None
    print(f"  => root {geo_idx} certified positively oriented: with the "
          f"exact equations this IS the complete", flush=True)
    print("     hyperbolic structure (Thurston gluing + completeness + "
          "Mostow rigidity).", flush=True)
    # corroboration vs SnapPy numerics (NOT load-bearing)
    r60 = complex(roots[geo_idx].evalf(60))
    print(f"  corroboration: |t_root - snappy {tvar}| = "
          f"{abs(r60 - complex(sp.N(pt[tvar], 20))):.2e} (double)",
          flush=True)

    # ---- exact cusp development (SnapPy default peripheral basis) ----
    from snappy.geometric_structure.cusp_neighborhood. \
        complex_cusp_cross_section import ComplexCuspCrossSection
    cs = ComplexCuspCrossSection.fromManifoldAndShapes(Mfd, shapesK)
    cs.check_cusp_development_exactly()
    print("  cusp cross-section develops EXACTLY consistently "
          "(all side gluings match): True", flush=True)
    vtx = cs.mcomplex.Vertices[0]
    mtr = ComplexCuspCrossSection._get_translation(vtx, 0)
    ltr = ComplexCuspCrossSection._get_translation(vtx, 1)
    xi = ltr / mtr          # tau = conj(xi): SnapPea kernel convention
    vK = -(xi * xi)         # if Re tau = 0 then u = (Im tau)^2 = vK
    tsym = symbols('t')
    p8t = p8.subs(tvar, tsym)
    mp_xi = sp.factor_list(sp.resultant(p8t, X - anf_to_t_expr(xi, tsym),
                                        tsym))[1]
    mp_v = sp.factor_list(sp.resultant(p8t, X - anf_to_t_expr(vK, tsym),
                                       tsym))[1]
    assert len(mp_xi) == 1 and len(mp_v) == 1
    oct_here = sp.expand(mp_xi[0][0] * sp.sign(sp.LC(mp_xi[0][0], X)))
    qua_here = sp.expand(mp_v[0][0] * sp.sign(sp.LC(mp_v[0][0], X)))
    print(f"  minpoly over Q of xi = l/m (EXACT, resultant): {oct_here}"
          f"   [irreducible, multiplicity {mp_xi[0][1]}]", flush=True)
    print(f"  minpoly over Q of v = -xi^2 (EXACT): {qua_here}"
          f"   [irreducible, multiplicity {mp_v[0][1]}]", flush=True)
    sh = complex(Mfd.cusp_info()[0].shape)
    print(f"  corroboration: conj(xi)(root) - snappy shape = "
          f"{abs(anf_num(xi, r60).conjugate() - sh):.2e} (double)",
          flush=True)
    return dict(F=F, P8=P8, tvar=tvar, shapesK=shapesK, xi=xi, vK=vK,
                geo_root=roots[geo_idx], octic=oct_here, quartic=qua_here,
                manifold=Mfd)


# ===========================================================================
def pin_to_real_root(vK, geo_root, quartic_expr):
    """vK is EXACTLY a root of quartic_expr (proved by the resultant).
    Pin WHICH root by rigorous rectangles: refine until the rectangle of
    vK at the certified geometric root box intersects the isolation box
    of exactly ONE quartic root.  If that root is real, vK is EXACTLY
    real at the geometric embedding."""
    qroots = Poly(quartic_expr, X).all_roots()
    for digits in (25, 50, 100):
        Rv = anf_at_box(vK, root_box(geo_root, digits))
        cands = []
        for j, rho in enumerate(qroots):
            if not Rv.disjoint(root_box(rho, digits)):
                cands.append(j)
        if len(cands) == 1:
            j = cands[0]
            rho = qroots[j]
            box = root_box(rho, digits)
            return j, rho, box, digits
    raise RuntimeError("pinning failed at cap")


# ===========================================================================
sec("PART I — THE BRONZE TRIANGULATION b++LLLRRR (exact chain)")
Zb = symbols('z0:6')
# branch selection (numerics-guided, discharged by the exact verification):
# the geometric point lies on the symmetric locus z3=z0, z2=z1, z5=z4
A = certify_triangulation(
    "b++LLLRRR", "symmetric locus z3=z0, z2=z1, z5=z4 (numerics-guided, "
    "discharged by the exact in-field verification of all rows)",
    {Zb[3]: Zb[0], Zb[2]: Zb[1], Zb[5]: Zb[4]})

sec("PART II — CERTIFICATION OF THE BANKED BRONZE CLAIMS")
print(f"(a) quartic: eliminated minpoly(v) == 192u^4-112u^3+20u^2-21u+7: "
      f"{sp.expand(A['quartic'] - QUARTIC.subs(uu, X)) == 0}", flush=True)
print(f"    octic:   eliminated minpoly(xi) == 192X^8+112X^6+20X^4+21X^2+7: "
      f"{sp.expand(A['octic'] - OCTIC) == 0}", flush=True)
print(f"    identity octic(X) == quartic(-X^2): "
      f"{sp.expand(OCTIC - QUARTIC.subs(uu, -X**2)) == 0}   "
      f"(the octic is EVEN)", flush=True)

Q4 = Poly(QUARTIC, uu)
print(f"(b) quartic irreducible over Q: {Q4.is_irreducible}", flush=True)

# (c) Galois group S4, fully exact
disc = Q4.discriminant()
dfac = sp.factorint(disc)
print(f"(c) disc(quartic) = {disc} = {dfac}", flush=True)
print(f"    disc < 0 => NOT a square in Q  (=> Gal not inside A4): "
      f"{disc < 0}", flush=True)
b_, c_, d_, e_ = [sp.Rational(x, 192) for x in (-112, 20, -21, 7)]
resolvent = sp.expand(X**3 - c_ * X**2 + (b_ * d_ - 4 * e_) * X
                      - (b_**2 * e_ - 4 * c_ * e_ + d_**2))
Rc = Poly(sp.numer(sp.together(resolvent * 192**2)), X)  # integral model
print(f"    resolvent cubic (monic model): {resolvent} = 0", flush=True)
print(f"    resolvent cubic irreducible over Q: {Rc.is_irreducible}",
      flush=True)
from sympy.polys.numberfields.galoisgroups import galois_group
Gg, _alt = galois_group(Q4)
print(f"    [quartic irred + resolvent irred => Gal in {{A4, S4}}; "
      f"disc non-square => Gal = S4]", flush=True)
print(f"    corroboration (sympy galois_group): order {Gg.order()}, "
      f"abelian {Gg.is_abelian}", flush=True)
# independent S4 witness (Dedekind: Frobenius factorization types mod p;
# a transitive subgroup of S4 containing a transposition and a 3-cycle
# is S4 itself)
types_seen = {}
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for pr in sp.primerange(5, 60):
        if 192 % pr == 0 or sp.Integer(disc) % pr == 0:
            continue
        fl2 = sp.factor_list(Poly(QUARTIC, uu, modulus=pr))[1]
        typ = tuple(sorted(f.degree() for f, _m in fl2 for _ in range(_m)))
        types_seen.setdefault(typ, pr)
print(f"    independent S4 witness (Dedekind, exact mod-p factorization): "
      f"types {types_seen};", flush=True)
print(f"    3-cycle at p = {types_seen.get((1, 3))}, transposition at "
      f"p = {types_seen.get((1, 1, 2))}; with transitivity => Gal = S4",
      flush=True)
assert (1, 3) in types_seen and (1, 1, 2) in types_seen
assert Q4.is_irreducible and Rc.is_irreducible and disc < 0

# (d) degrees
Oc = Poly(OCTIC, X)
Yoct = Poly(sp.expand(QUARTIC.subs(uu, X**2)), X)
print(f"(d) octic (minpoly of tau AND of xi; even, rational) irreducible: "
      f"{Oc.is_irreducible}  =>  [Q(tau):Q] = 8", flush=True)
print(f"    y-octic 192y^8-112y^6+20y^4-21y^2+7 (minpoly of y = Im tau) "
      f"irreducible: {Yoct.is_irreducible}", flush=True)
print(f"    tower: [Q(u):Q] = 4 (quartic), tau^2 = -u => [Q(tau):Q(u)] = 2; "
      f"8 = 4 x 2 consistent", flush=True)
assert Oc.is_irreducible

# (e) Re tau = 0 EXACT via root pinning
j, rho, box, dig = pin_to_real_root(A['vK'], A['geo_root'], QUARTIC.subs(uu, X))
qroots = Poly(QUARTIC.subs(uu, X), X).all_roots()
nreal = len([r for r in qroots if r.is_real])
print(f"(e) v = -xi^2 is EXACTLY a root of the quartic (resultant); "
      f"quartic has {nreal} real roots (Sturm-exact).", flush=True)
print(f"    rigorous rectangles (refined to 1e-{dig}) pin v to root #{j}: "
      f"real = {rho.is_real}, isolation box re = {box.re}", flush=True)
assert rho.is_real and box.re.lo > 0
print(f"    => v real and POSITIVE exactly; tau = conj(xi), xi^2 = -v "
      f"=> tau = i*sqrt(u), Re tau = 0 EXACT, u = (Im tau)^2 = v.",
      flush=True)
print(f"    u = the root of 192u^4-112u^3+20u^2-21u+7 in "
      f"[{box.re.lo}, {box.re.hi}]", flush=True)
print(f"    u ~ {float(rho):.15f}", flush=True)

print("""
(f) Kronecker-Weber conclusion (now on certified input): every subfield
    of every cyclotomic field Q(zeta_n) is abelian Galois over Q.  If
    Q(u) lay in some Q(zeta_n), Q(u)/Q would be abelian with Galois
    closure of degree 4; but its Galois closure has degree |S4| = 24.
    Hence Q(u) — and a fortiori Q(tau) containing it — lies in NO
    cyclotomic field.  The H-CUSP deafness input is CERTIFIED.""",
      flush=True)

# ===========================================================================
sec("PART III — THE SECOND TRIANGULATION (census s464), exact chain")
B = certify_triangulation("s464", None, None)
REV_QUARTIC = sp.expand(X**4 * QUARTIC.subs(uu, 1 / X))
print(f"\n  reversed quartic (exact identity x^4*q(1/x)): {REV_QUARTIC}",
      flush=True)
print(f"  eliminated minpoly(v') == reversed quartic: "
      f"{sp.expand(B['quartic'] - REV_QUARTIC) == 0}", flush=True)
j2, rho2, box2, dig2 = pin_to_real_root(B['vK'], B['geo_root'], REV_QUARTIC)
print(f"  v' pinned (1e-{dig2}) to root #{j2} of the reversed quartic: "
      f"real = {rho2.is_real}, box re = {box2.re}", flush=True)
assert rho2.is_real and box2.re.lo > 0
print(f"  => Re tau' = 0 EXACT as well; u' = v' real positive.", flush=True)

# u * u' = 1 at root level: 1/u' is EXACTLY a root of the quartic
# (reversal identity); its rigorous interval must isolate the SAME real
# root the bronze u was pinned to.
inv_box = RI(Fr(1) / box2.re.hi, Fr(1) / box2.re.lo)
hits = []
for jj, rr in enumerate(qroots):
    bb = root_box(rr, dig2)
    if not bb.re.disjoint(inv_box) and (not rr.is_real or True):
        if not (bb.re.disjoint(inv_box)):
            hits.append(jj)
print(f"  1/u' interval {inv_box} intersects quartic-root boxes: {hits}",
      flush=True)
assert hits == [j]
print(f"  1/u' is exactly a quartic root (reversal identity) and its "
      f"interval isolates root #{j} = u", flush=True)
print(f"  =>  u * u' = 1  CERTIFIED EXACTLY (root level, both "
      f"triangulations).", flush=True)

# ===========================================================================
sec("VERDICT")
print(f"""
  CERTIFIED (exact end-to-end; floats only guided branch/factor/root
  selection, every selection discharged by exact rational arithmetic):
    1. b++LLLRRR: shape field K = Q[t]/(p8), all gluing+completeness
       rows hold EXACTLY in K; the geometric root is certified
       positively oriented by rigorous rational rectangles => THE
       complete hyperbolic structure (Mostow).
    2. tau (SnapPy default basis, kernel convention tau = conj(l/m)):
       minpoly(tau) = 192X^8+112X^6+20X^4+21X^2+7, irreducible
       => [Q(tau):Q] = 8.
    3. u = (Im tau)^2 = -xi^2: minpoly = 192u^4-112u^3+20u^2-21u+7,
       irreducible; Re tau = 0 EXACT (v pinned to the positive real
       quartic root).
    4. Galois group S4 exactly (resolvent cubic irreducible + disc
       = -2^24*7*617 < 0 non-square); disc primes {{2, 7, 617}}.
    5. Kronecker-Weber: Q(u), hence Q(tau), lies in NO cyclotomic
       field — the H-CUSP bronze deafness input is now CERTIFIED.
    6. s464 census triangulation (independent): u' satisfies the
       reversed quartic EXACTLY and u * u' = 1 EXACTLY (root level).

  total time: {time.time() - T0:.0f}s
""", flush=True)
