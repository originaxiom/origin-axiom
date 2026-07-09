#!/usr/bin/env python3
"""B494 — CL-1b duel: the held-breath field law (B479, corrected) vs Cantat's fixed-curve method.

Pre-registered in docs/CLOSURE_CAMPAIGN_2026-07.md (outcome enum: COROLLARY / NOT-BY-THAT-ROUTE /
PARTIAL). Adversarial protocol: every step is derived independently and machine-checked; the run
aborts INVALID if the mandatory control fails.

Pipeline under duel (Cantat, Duke 149 (2009), for the pseudo-Anosov Psi = [[2,1],[1,1]]):
    trace action on (x,y,z) = (trA, trB, trAB)  ->  fixed locus  ->  restrict the Fricke/commutator
    trace kappa = x^2+y^2+z^2-xyz-2  ->  minimal polynomial  ->  number field.

CONTROL (mandatory first): reproduce Cantat's own computation — fixed curve (x, x/(x-1), x),
quartic x^4-3x^3+x^2+4x-2 on kappa = 0, splitting over Q(sqrt(17)).

DUEL (steps 1-5): apply the same pipeline to the half-monodromy sigma_m: a -> a^m b, b -> a at the
cusp locus kappa = -2 and decide whether the corrected B479 law
    Fix(sigma_m) cap {kappa=-2} = trivial point  U  order-d torsion points (d | m, d >= 3, d != 4),
    field  Q(tau_d, sqrt(tau_d^2 (tau_d^2 - 8))),  tau_d = 2cos(2 pi k / d),
falls out as an easy corollary. Step 4 additionally adjudicates the banked m = 7 row ("Q(sqrt(-239))").

Everything is exact (sympy); cypari (when importable) supplies independent number-field ground truth.
"""
import sys
import time

import sympy as sp

T0 = time.time()
x, y, z, tau, u0, u1 = sp.symbols('x y z tau u0 u1')
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2          # tr[A,B]; the cusp locus is kappa = -2
FAILURES = []


def check(label, ok):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)
    return ok


# ----------------------------------------------------------------------------------------------
# Symbolic SL(2) machinery: generic determinant-1 matrices; trace polynomials are verified against
# honest matrix products, not assumed.
# ----------------------------------------------------------------------------------------------
_a1, _a2, _a3, _b1, _b2, _b3 = sp.symbols('_a1 _a2 _a3 _b1 _b2 _b3')
_A = sp.Matrix([[_a1, _a2], [_a3, (1 + _a2*_a3)/_a1]])       # det = 1
_B = sp.Matrix([[_b1, _b2], [_b3, (1 + _b2*_b3)/_b1]])       # det = 1
_X, _Y, _Z = sp.cancel(_A.trace()), sp.cancel(_B.trace()), sp.cancel((_A*_B).trace())


def word_matrix(word):
    M = sp.eye(2)
    for ch in word:
        M = M * (_A if ch == 'A' else _B)
    return M


def trace_poly_ok(word, poly):
    """Is poly(x,y,z) == tr(word(A,B)) identically on SL2 x SL2?"""
    return sp.cancel(poly.subs({x: _X, y: _Y, z: _Z}, simultaneous=True) - word_matrix(word).trace()) == 0


def t_recurrence(m, t0v, t1v, mult):
    """t_k = tr(a^k b): t_0 = tr b, t_1 = tr ab, t_{k+1} = tr(a) t_k - t_{k-1} (Cayley-Hamilton)."""
    t = {0: t0v, 1: t1v}
    for k in range(2, m + 2):
        t[k] = sp.expand(mult * t[k-1] - t[k-2])
    return t


_MINPOLY_CACHE = {}


def cheb_minpoly(d, var):
    """Minimal polynomial over Q of tau_d = 2 cos(2 pi / d) (degree phi(d)/2 for d >= 3)."""
    if d not in _MINPOLY_CACHE:
        _MINPOLY_CACHE[d] = sp.minimal_polynomial(2*sp.cos(2*sp.pi/d), tau)
    return _MINPOLY_CACHE[d].subs(tau, var)


def irreducible_over(poly, var, ext=None):
    fl = sp.factor_list(poly, extension=ext) if ext is not None else sp.factor_list(poly)
    nontriv = [f for f, _ in fl[1] if f.free_symbols]
    return len(nontriv) == 1 and nontriv[0].as_poly(var).degree() == sp.Poly(poly, var).degree()


try:
    from cypari import pari

    def pari_str(e):
        return str(sp.expand(e)).replace('**', '^')
    HAVE_PARI = True
except Exception:                                            # pragma: no cover
    HAVE_PARI = False

# ================================================================================================
# CONTROL — Cantat's pseudo-Anosov Psi = [[2,1],[1,1]] (the duel is INVALID if this fails)
# ================================================================================================
print("== CONTROL: Cantat's fixed-curve computation for Psi = [[2,1],[1,1]] ==")

# Two automorphism representatives of the mapping class (homology written columns-as-images):
#   psi_n : A -> ABA, B -> BA    abelianization exactly [[2,1],[1,1]] in basis (A,B);
#   psi_c : A -> BA,  B -> BAB   abelianization [[1,1],[1,2]], SL(2,Z)-conjugate to [[2,1],[1,1]]
#                                (conjugator P = [[-2,-3],[-1,-2]], det 1) — this is the
#                                representative whose fixed curve is Cantat's parametrization.
ab_n = sp.Matrix([[2, 1], [1, 1]])
ab_c = sp.Matrix([[1, 1], [1, 2]])
P = sp.Matrix([[-2, -3], [-1, -2]])
check("psi_n abelianization = [[2,1],[1,1]]; psi_c = [[1,1],[1,2]] with det(P)=1, P psi_c P^-1 = psi_n",
      P.det() == 1 and P*ab_c*P.inv() == ab_n)

Tc = (z, y*z - x, y*z**2 - x*z - y)                      # trace action of psi_c
Tn = (x*z - y, z, x*z**2 - y*z - x)                      # trace action of psi_n
check("trace action of psi_c verified on honest SL2 words (BA, BAB, BABAB)",
      trace_poly_ok("BA", Tc[0]) and trace_poly_ok("BAB", Tc[1]) and trace_poly_ok("BABAB", Tc[2]))
check("trace action of psi_n verified on honest SL2 words (ABA, BA, ABABA)",
      trace_poly_ok("ABA", Tn[0]) and trace_poly_ok("BA", Tn[1]) and trace_poly_ok("ABABA", Tn[2]))
check("both trace actions preserve the Fricke polynomial kappa",
      all(sp.expand(KAPPA.subs(dict(zip((x, y, z), T)), simultaneous=True) - KAPPA) == 0 for T in (Tc, Tn)))

Gc = sp.groebner([sp.expand(Tc[0]-x), sp.expand(Tc[1]-y), sp.expand(Tc[2]-z)], z, y, x, order='lex')
check("Fix(psi_c) = the rational curve {z = x, y(x-1) = x} i.e. (x, x/(x-1), x) — Cantat's curve",
      set(map(sp.expand, Gc.exprs)) == {sp.expand(z - x), sp.expand(x*y - x - y)})
kappa_on_curve = sp.cancel(KAPPA.subs({y: x/(x-1), z: x}, simultaneous=True))
QUARTIC = sp.expand(sp.numer(kappa_on_curve))
check("kappa restricted to the curve = (x^4-3x^3+x^2+4x-2)/(x-1)^2 — Cantat's quartic at kappa = 0",
      QUARTIC == sp.expand(x**4 - 3*x**3 + x**2 + 4*x - 2)
      and sp.expand(sp.denom(kappa_on_curve) - (x - 1)**2) == 0)
check("quartic irreducible over Q", irreducible_over(QUARTIC, x))
fl17 = sp.factor_list(QUARTIC, extension=sp.sqrt(17))[1]
check("quartic splits over Q(sqrt(17)) into two quadratics",
      sorted(sp.Poly(f, x).degree() for f, _ in fl17) == [2, 2])
# same quartic from the other representative (its curve is the x<->y relabelling of Cantat's)
Gn = sp.groebner([sp.expand(Tn[0]-x), sp.expand(Tn[1]-y), sp.expand(Tn[2]-z)], z, y, x, order='lex')
kn = sp.cancel(KAPPA.subs({y: x/(x-1), z: x/(x-1)}, simultaneous=True))
check("psi_n gives the relabelled curve (x, x/(x-1), x/(x-1)) and the SAME quartic",
      set(map(sp.expand, Gn.exprs)) == {sp.expand(z - y), sp.expand(x*y - x - y)}
      and sp.expand(sp.numer(kn)) == QUARTIC)

# tie-in to the metallic family: Psi IS the m=1 (figure-eight) monodromy = sigma_1 squared
T1 = (z, x, sp.expand(x*z - y))                          # trace action of sigma_1: a -> ab, b -> a
T1sq = tuple(sp.expand(c.subs({x: T1[0], y: T1[1], z: T1[2]}, simultaneous=True)) for c in T1)
check("control map = T_1 o T_1 (Cantat's Psi is the m=1 metallic monodromy, sigma_1^2)", T1sq == Tn)
fix_T1 = sp.solve([sp.expand(T1[0]-x), sp.expand(T1[1]-y), sp.expand(T1[2]-z)], [x, y, z], dict=True)
check("Fix(sigma_1) = {(0,0,0), (2,2,2)}: on the cusp only the trivial point (B479 m=1 row: breathless)",
      sorted(tuple(s[v] for v in (x, y, z)) for s in fix_T1) == [(0, 0, 0), (2, 2, 2)])
# bonus foreign anchor: the SAME pipeline at kappa = -2 recovers the figure-eight trace field
fig8 = sp.factor(sp.numer(sp.cancel((KAPPA + 2).subs({y: x/(x-1), z: x/(x-1)}, simultaneous=True))))
check("full-monodromy fixed curve meets kappa = -2 in x^2-3x+3 (disc -3): the figure-eight "
      "trace field Q(sqrt(-3))",
      fig8 == sp.factor(x**2*(x**2 - 3*x + 3)) and sp.discriminant(x**2 - 3*x + 3, x) == -3)
if HAVE_PARI:
    check("pari: Galois group of the control quartic is D4 (resolvent field Q(sqrt(17)))",
          str(pari(f"polgalois({pari_str(QUARTIC)})[4]")).strip('"') == "D(4)")

if FAILURES:
    print("\nCONTROL FAILED — the duel is INVALID. Failing checks:", FAILURES)
    sys.exit(1)
print(f"CONTROL PASS ({time.time()-T0:.1f}s). The duel is valid; proceeding.\n")

# ================================================================================================
# STEP 1 — sigma_m's trace action and the PROVEN degeneration-to-swap mechanism (B479)
# ================================================================================================
print("== STEP 1: sigma_m: a -> a^m b, b -> a; trace action T_m = (t_m, x, t_{m+1}) ==")
ok = True
for m in range(1, 5):
    t = t_recurrence(m, y, z, x)
    ok &= trace_poly_ok("A"*m + "B", t[m]) and trace_poly_ok("A"*(m+1) + "B", t[m+1])
check("T_m(x,y,z) = (t_m, x, t_{m+1}) verified on honest SL2 words, m = 1..4 "
      "(t_0=y, t_1=z, t_{k+1} = x t_k - t_{k-1})", ok)
check("T_m preserves kappa, m = 1..6",
      all(sp.expand(KAPPA.subs({x: t_recurrence(m, y, z, x)[m], y: x,
                                z: t_recurrence(m, y, z, x)[m+1]}, simultaneous=True) - KAPPA) == 0
          for m in range(1, 7)))

# group level: ANY SL2 element with trace tau_d (d >= 3) is diagonalizable of order d, so a^m = I
# whenever d | m and sigma_m(a) = a^m b = b, sigma_m(b) = a — literally the swap.
ok = True
for d in (3, 4, 5, 6, 7, 8, 12):
    psi = cheb_minpoly(d, tau)
    Md = sp.Matrix([[tau, -1], [1, 0]])                  # companion matrix: the generic trace-tau_d element
    Pw = sp.eye(2)
    for _ in range(d):
        Pw = (Md*Pw).applyfunc(lambda e: sp.rem(sp.expand(e), psi, tau))
    ok &= Pw == sp.eye(2)
check("group level: M(tau_d)^d = I identically mod Psi_d (d = 3,4,5,6,7,8,12) => a^m = I when d | m", ok)

# trace level: on the hyperplane {x = tau_d}, d | m, the map T_m IS the swap (x,y,z) -> (y,x,z)
ok = True
for (d, m) in [(3, 3), (3, 6), (3, 9), (3, 12), (5, 5), (5, 10), (5, 15), (6, 6), (4, 4), (4, 8),
               (8, 8), (8, 16), (7, 7), (7, 14), (9, 9), (12, 12)]:
    psi = cheb_minpoly(d, x)
    t = t_recurrence(m, y, z, x)
    ok &= sp.rem(sp.expand(t[m] - y), psi, x) == 0 and sp.rem(sp.expand(t[m+1] - z), psi, x) == 0
check("degeneration: T_m == swap on {x = tau_d} for d | m (16 (d,m) pairs incl. (7,7),(7,14))", ok)
ok = True
for (d, m) in [(5, 3), (7, 3), (3, 4), (5, 7), (8, 4), (9, 3)]:
    psi = cheb_minpoly(d, x)
    t = t_recurrence(m, y, z, x)
    ok &= sp.rem(sp.expand(t[m] - y), psi, x) != 0
check("negative control: T_m is NOT the swap on {x = tau_d} when d does not divide m (6 pairs)", ok)

# ================================================================================================
# STEP 2 — swap-fixed characters and the cusp quadratic (the field law in closed form)
# ================================================================================================
print("== STEP 2: Fix(swap) = {x=y}; on kappa = -2 with x = y = t: z^2 - t^2 z + 2 t^2 = 0 ==")
t_ = sp.symbols('t')
cusp_sym = sp.expand((KAPPA + 2).subs({x: t_, y: t_}, simultaneous=True))
check("cusp restricted to the symmetric locus: z^2 - t^2 z + 2 t^2 (as claimed)",
      cusp_sym == sp.expand(z**2 - t_**2*z + 2*t_**2))
check("discriminant = t^2 (t^2 - 8)  => z in Q(t, sqrt(t^2(t^2-8)))",
      sp.factor(sp.discriminant(cusp_sym, z)) == sp.factor(t_**2*(t_**2 - 8)))
check("d = 4 degenerates: tau_4 = 0 gives z^2 = 0, the trivial point (the d != 4 condition)",
      cusp_sym.subs(t_, 0) == z**2 and sp.expand(2*sp.cos(2*sp.pi/4)) == 0)
ok = True
for d in (3, 5, 7, 8, 9, 11, 12, 13, 16):
    psi = cheb_minpoly(d, tau)
    ok &= all(sp.sign(sp.expand((tau**2*(tau**2 - 8)).subs(tau, r))) == -1
              for r in sp.Poly(psi, tau).all_roots())
check("Delta_d = tau_d^2(tau_d^2-8) is TOTALLY NEGATIVE (all real conjugates) for d = 3..16, d != 4 "
      "=> [Q(tau_d, sqrt(Delta_d)) : Q(tau_d)] = 2 exactly (never collapses)", ok)


def E(d):
    """z-eliminant of the order-d symmetric cusp point: Res_tau(Psi_d, z^2 - tau^2 z + 2 tau^2)."""
    return sp.expand(sp.resultant(cheb_minpoly(d, tau), z**2 - tau**2*z + 2*tau**2, tau))


def norm_delta(d):
    """Norm_{Q(tau_d)/Q}(Delta_d): Psi_d monic => resultant = product over all conjugates."""
    return sp.resultant(cheb_minpoly(d, tau), sp.expand(tau**2*(tau**2 - 8)), tau)


def groebner_zelim_factors(m):
    """B479's own brute pipeline: z-eliminant factors of Fix(T_m) cap {kappa=-2} (y = x forced)."""
    tt = t_recurrence(m, x, z, x)
    eqs = [sp.expand(tt[m] - x), sp.expand(tt[m+1] - z), sp.expand(2*x**2 + z**2 - x*x*z)]
    G = sp.groebner(eqs, x, z, order='lex')
    elim = [g for g in G.exprs if g.free_symbols <= {z}]
    poly = sp.gcd(*elim) if len(elim) > 1 else elim[0]
    return set(sp.expand(f) for f, _ in sp.factor_list(poly)[1] if f.free_symbols)


# ================================================================================================
# STEP 3 — consistency against the banked B479 table (d = 3, 5, 8; growing degrees 11, 13)
# ================================================================================================
print("== STEP 3: the banked rows, rederived ==")
check("d=3: tau_3 = -1, eliminant z^2 - z + 2, disc -7 => Q(sqrt(-7)) (rows m = 3,6,9,12,15)",
      E(3) == sp.expand(z**2 - z + 2) and sp.discriminant(E(3), z) == -7)
check("d=6 gives the SAME quadratic z^2 - z + 2 (tau_6^2 = 1): B479's coincident d=3/d=6 z-point",
      E(6) == E(3))
E5 = E(5)
check("d=5: eliminating tau (tau^2+tau-1 = 0) gives EXACTLY the banked quartic z^4-3z^3+7z^2-4z+4",
      E5 == sp.expand(z**4 - 3*z**3 + 7*z**2 - 4*z + 4))
check("d=5 quartic irreducible over Q (so the field has degree 4, not 2)", irreducible_over(E5, z))
check("d=5 polynomial disc = 2^4 * 5^2 * 41", sp.discriminant(E5, z) == 16400)
check("d=5 quartic splits into two quadratics over Q(sqrt(5)) — the field CONTAINS Q(sqrt(5))",
      sorted(sp.Poly(f, z).degree() for f, _ in sp.factor_list(E5, extension=sp.sqrt(5))[1]) == [2, 2])
check("d=5 quartic stays IRREDUCIBLE over Q(sqrt(41)) — 'Q(sqrt(41))' was never the field",
      irreducible_over(E5, z, ext=sp.sqrt(41)))
check("d=5: Norm_{Q(sqrt5)/Q}(Delta_5) = 41 — the banked '41' is the NORM of the discriminant",
      norm_delta(5) == 41)
# sqrt(41) is not even in the quartic field: 41*Delta_5 is totally negative, no square in a real field
check("d=5: 41*Delta_5 totally negative => sqrt(41) not in Q(tau_5, sqrt(Delta_5)) (sign obstruction)",
      all(sp.sign(sp.expand((41*tau**2*(tau**2 - 8)).subs(tau, r))) == -1
          for r in sp.Poly(cheb_minpoly(5, tau), tau).all_roots()))
check("d=8: tau_8^2 = 2 is RATIONAL, eliminant collapses to (z^2-2z+4)^2, disc -12 => Q(sqrt(-3)) "
      "(explains the banked m = 8, 16 row)",
      sp.factor(E(8)) == sp.factor((z**2 - 2*z + 4)**2) and sp.discriminant(z**2 - 2*z + 4, z) == -12)
check("d=12: (z^2-3z+6)^2, disc -15 => Q(sqrt(-15)) (B479 addendum's Delta_12 = -15)",
      sp.factor(E(12)) == sp.factor((z**2 - 3*z + 6)**2)
      and sp.discriminant(z**2 - 3*z + 6, z) == -15)
check("d=11: eliminant irreducible of degree 10 = phi(11) (the banked m=11 'growing-degree' row)",
      sp.Poly(E(11), z).degree() == 10 and irreducible_over(E(11), z))
check("d=13: eliminant irreducible of degree 12 = phi(13) (the banked m=13 row)",
      sp.Poly(E(13), z).degree() == 12 and irreducible_over(E(13), z))
if HAVE_PARI:
    check("pari: d=5 field disc = 1025 = 5^2*41; unique quadratic subfield (degrees [1,2,4]); D4",
          int(pari(f"nfdisc({pari_str(E5)})")) == 1025
          and str(pari(f"apply(v->poldegree(v[1]), nfsubfields({pari_str(E5)}))")) == "[1, 2, 4]"
          and str(pari(f"polgalois({pari_str(E5)})[4]")).strip('"') == "D(4)")

# ================================================================================================
# STEP 4 — NEW: the banked m = 7 row ("Q(sqrt(-239))") adjudicated
# ================================================================================================
print("== STEP 4: the m = 7 row — norm-vs-field conflation check ==")
E7 = E(7)
check("d=7 eliminant = z^6 - 5z^5 + 16z^4 - 25z^3 + 30z^2 - 12z + 8 (recomputed from scratch)",
      E7 == sp.expand(z**6 - 5*z**5 + 16*z**4 - 25*z**3 + 30*z**2 - 12*z + 8))
check("d=7 eliminant irreducible over Q of degree 6 = phi(7): the true field has DEGREE 6, not 2",
      sp.Poly(E7, z).degree() == 6 and irreducible_over(E7, z))
ND7 = norm_delta(7)
check("Norm_{Q(tau_7)/Q}(Delta_7) = -239 EXACTLY — the banked -239 is the norm, same conflation "
      "as the corrected d=5 row", ND7 == -239)
D7 = sp.discriminant(E7, z)
sf = 1
for p, e in sp.factorint(D7).items():
    if e % 2:
        sf *= p
check("poly disc(E_7) = -2^12 * 7^4 * 239 with squarefree part -239: the exact output of B479's "
      "deg-2-only 'disc -> Q(sqrt(sf))' labelling heuristic (held_breath_tower.py), applied out of "
      "its validity range", D7 == -2350444544 and dict(sp.factorint(D7)) == {-1: 1, 2: 12, 7: 4, 239: 1}
      and sf == -239)
check("E_7 stays IRREDUCIBLE over Q(sqrt(-239)): Q(sqrt(-239)) is NOT EVEN A SUBFIELD of the true field",
      irreducible_over(E7, z, ext=sp.sqrt(-239)))
check("m=7 and m=14 banked rows are this same object: Gröbner z-eliminant nontrivial factor == E_7",
      all(groebner_zelim_factors(m) - {z} == {sp.expand(E7)} for m in (7, 14)))
if HAVE_PARI:
    check("pari ground truth: subfield degrees of the d=7 field are [1, 3, 6] — NO quadratic subfield; "
          "field disc = -7^4 * 239; Galois closure C2 wr C3 (order 24, where sqrt(Norm Delta) lives); "
          "Q(tau_7) embeds",
          str(pari(f"apply(v->poldegree(v[1]), nfsubfields({pari_str(E7)}))")) == "[1, 3, 6]"
          and int(pari(f"nfdisc({pari_str(E7)})")) == -573839 and -7**4*239 == -573839
          and int(pari(f"polgalois({pari_str(E7)})[1]")) == 24
          and str(pari(f"nfisincl(x^3+x^2-2*x-1, {pari_str(E7)})")) != "0")
print("  => The banked 'Q(sqrt(-239))' for m = 7, 14 is REFUTED as a field statement and explained as "
      "the norm: true field Q(tau_7, sqrt(Delta_7)), degree 6, no quadratic subfield. This EXTENDS the "
      "2026-07-09 B479/B491 erratum (d=5) to the d=7 rows, with the same mechanism.")

# ================================================================================================
# STEP 5 — the hard direction: COMPLETENESS, now proved for ALL m (elementary, no Gröbner)
# ================================================================================================
print("== STEP 5: completeness — Fix(T_m) classified for all m ==")
# THE ARGUMENT (short; each ingredient machine-verified below):
#   Fixed point => 2nd coordinate gives y = x; writing t_0 = x, t_1 = z, the remaining equations say
#   (t_m, t_{m+1}) = (t_0, t_1). Since the recurrence is order two, this makes t m-periodic:
#   explicitly t_{m+j} - t_j = F_j (t_{m+1}-t_1) - F_{j-1}(t_m - t_0)   [I2 below]
#   with F the Chebyshev-Fibonacci polynomials F_0=0, F_1=1, F_{k+1} = x F_k - F_{k-1}.
#   In transfer-matrix form, with M = [[x,-1],[1,0]] (det 1, tr x, eigenvalues l, 1/l, l+1/l = x):
#      M^m = [[F_{m+1}, -F_m],[F_m, -F_{m-1}]]        [I3]
#      fixed system == (M^m - I)(z, x)^T = 0          [I3]
#      det(M^m - I) = 2 - tr(M^m) = -(l^m - 1)^2 / l^m [I4]
#   so EITHER (z,x) = (0,0) — with y = x this is the trivial point (0,0,0) — OR l^m = 1:
#     l primitive d-th root, d | m, d >= 3  <=>  x = tau_{d,k}: M is then diagonalizable of order d,
#        M^m = I identically [line check], and the FULL line {(tau,tau,z)} is fixed;
#     l = 1 (x = 2):  M^m - I = m(M - I), kernel = span(1,1): the single point (2,2,2);
#     l = -1 (x = -2): m even: kernel = span(1,-1): the single point (-2,-2,2); m odd: no solution.
#   Eigenvalue locus as polynomial fact [F1]: 2 - tr(M^m) = -(x-2) (x+2)^[2|m] prod_{d|m,d>=3} Psi_d^2.
#   INTERSECT with the cusp kappa = -2: (2,2,2) and (-2,-2,2) have kappa = 2 (OFF); the d-line meets
#   it in z^2 - tau^2 z + 2 tau^2 = 0 (d = 4: z = 0 trivial). Hence, for EVERY m:
#      Fix(T_m) cap {kappa = -2} = {(0,0,0)} U {order-d torsion points : d | m, d >= 3, d != 4}.
#   This upgrades B479's Gröbner-verified (m <= 16) THEOREM to an unconditional one.
MAXM = 24
F = {0: sp.Integer(0), 1: sp.Integer(1)}
for k in range(2, 2*MAXM + 3):
    F[k] = sp.expand(x*F[k-1] - F[k-2])
Fm1 = sp.Integer(-1)                                        # F_{-1}

tg = t_recurrence(2*MAXM, u0, u1, x)
check("I1: t_k = F_k t_1 - F_{k-1} t_0 identically (k <= 2*24+1)",
      all(sp.expand(tg[k] - (F[k]*u1 - (F[k-1] if k >= 1 else Fm1)*u0)) == 0 for k in range(0, 2*MAXM + 2)))
check("I2: t_{m+j} - t_j = F_j (t_{m+1}-t_1) - F_{j-1} (t_m - t_0) identically (m, j <= 24: two "
      "consecutive coincidences force m-periodicity, with explicit cofactors)",
      all(sp.expand((tg[m+j] - tg[j]) - (F[j]*(tg[m+1] - tg[1]) - (F[j-1] if j >= 1 else Fm1)*(tg[m] - tg[0]))) == 0
          for m in range(1, MAXM + 1) for j in range(0, MAXM + 1)))
M = sp.Matrix([[x, -1], [1, 0]])
ok_I3 = ok_I4 = True
Mk = sp.eye(2)
for m in range(1, MAXM + 1):
    Mk = Mk*M
    Mk = Mk.applyfunc(sp.expand)
    ok_I3 &= Mk == sp.Matrix([[F[m+1], -F[m]], [F[m], -(F[m-1] if m >= 1 else Fm1)]])
    ok_I4 &= sp.expand((Mk - sp.eye(2)).det() - (2 - Mk.trace())) == 0
check("I3: M^m = [[F_{m+1},-F_m],[F_m,-F_{m-1}]], so the fixed system IS (M^m - I)(z,x)^T = 0 (m <= 24)",
      ok_I3)
check("I4: det(M^m - I) = 2 - tr(M^m) (m <= 24)", ok_I4)

ok_F1 = True
for m in range(1, MAXM + 1):
    Pm = sp.expand(2 - (F[m+1] - F[m-1]))
    got = {sp.expand(f): mult for f, mult in sp.factor_list(Pm)[1]}
    expect = {sp.expand(x - 2): 1}
    if m % 2 == 0:
        expect[sp.expand(x + 2)] = 1
    for d in sp.divisors(m):
        if d >= 3:
            expect[sp.expand(cheb_minpoly(d, x))] = 2
    ok_F1 &= (got == expect)
check("F1: 2 - tr(M^m) = -(x-2)(x+2)^[2|m] prod_{d|m, d>=3} Psi_d(x)^2 exactly (m <= 24) — the "
      "eigenvalue locus l^m = 1 is EXACTLY the divisor-torsion trace locus plus x = +-2", ok_F1)
check("lines: M^m == I identically mod Psi_d for every d | m, d >= 3 (m <= 24) — the whole z-line "
      "{(tau_d, tau_d, z)} is fixed",
      all(sp.Matrix([[F[m+1], -F[m]], [F[m], -F[m-1]]]).applyfunc(
          lambda e: sp.rem(sp.expand(e), cheb_minpoly(d, x), x)) == sp.eye(2)
          for m in range(1, MAXM + 1) for d in sp.divisors(m) if d >= 3))
ok_bd = True
for m in range(1, MAXM + 1):
    tt = t_recurrence(m, x, z, x)
    e1, e2 = sp.expand(tt[m] - x), sp.expand(tt[m+1] - z)
    g2 = sp.gcd(e1.subs(x, 2), e2.subs(x, 2))
    gm2 = sp.gcd(e1.subs(x, -2), e2.subs(x, -2))
    ok_bd &= sp.degree(g2, z) == 1 and sp.solve(g2, z) == [2]          # only (2,2,2)
    if m % 2 == 0:
        ok_bd &= sp.degree(gm2, z) == 1 and sp.solve(gm2, z) == [2]    # only (-2,-2,2)
    else:
        ok_bd &= sp.degree(gm2, z) == 0                               # no solution
check("boundary: at x = 2 only (2,2,2); at x = -2 only (-2,-2,2) and only for even m (m <= 24)", ok_bd)
check("both isolated points are OFF the cusp: kappa(2,2,2) = kappa(-2,-2,2) = 2 != -2",
      KAPPA.subs({x: 2, y: 2, z: 2}) == 2 and KAPPA.subs({x: -2, y: -2, z: 2}) == 2)
check("trivial point (0,0,0) is fixed for every m and IS on the cusp (it is the order-4 character)",
      all(t_recurrence(m, 0, 0, 0)[m] == 0 for m in range(1, 8)) and KAPPA.subs({x: 0, y: 0, z: 0}) == -2)


def predicted_factors(m):
    """The theorem's prediction: {z} U eliminant factors of every divisor d >= 3 of m."""
    out = {z}
    for d in sp.divisors(m):
        if d >= 3:
            out |= set(sp.expand(f) for f, _ in sp.factor_list(E(d))[1] if f.free_symbols)
    return out


check("cross-check: brute Gröbner z-eliminants == divisor-union prediction, m = 1..16 (the ENTIRE "
      "banked B479 table reproduced from the theorem)",
      all(groebner_zelim_factors(m) == predicted_factors(m) for m in range(1, 17)))
check("out-of-sample (beyond B479's banked range): m = 17..20 also match the prediction",
      all(groebner_zelim_factors(m) == predicted_factors(m) for m in (17, 18, 19, 20)))

# ================================================================================================
# VERDICT
# ================================================================================================
print()
if FAILURES:
    print(f"DUEL INCOMPLETE — {len(FAILURES)} failing check(s):")
    for f in FAILURES:
        print("  -", f)
    sys.exit(1)
print("VERDICT: COROLLARY.")
print("  Cantat's pipeline (fixed locus of the trace action -> restrict kappa -> field) transfers")
print("  verbatim to sigma_m at kappa = -2 and yields the corrected held-breath law, including the")
print("  divisor indexing, the d != 4 condition, and the closed-form field Q(tau_d, sqrt(tau_d^2")
print("  (tau_d^2-8))). The completeness direction did NOT resist: it follows for ALL m from the")
print("  elementary transfer-matrix lemma above (the one supplement not in Cantat, at or below the")
print("  difficulty of the control computation). m = 7 banked row corrected: field = degree 6,")
print("  Norm(Delta_7) = -239; 'Q(sqrt(-239))' was the d=5-style norm-vs-field conflation.")
print(f"[total {time.time()-T0:.1f}s]")
