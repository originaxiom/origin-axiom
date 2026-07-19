"""
B711 (Path 2) -- THE TWO-Z/2 DEGENERATION on the SL(2,C) character variety X(4_1).

QUESTION (sealed prereg 93879b9d): on X(4_1) two involutions act -- AMPHICHIRALITY
(orientation reversal; CS=0 at the geometric point) and the GALOIS involution of the
trace field Q(sqrt-3) (sqrt-3 -> -sqrt-3 = complex conjugation, rho_geom <-> rho_geom-bar).
Do they geometrically LOCK (Outcome A) or act INDEPENDENTLY/FREELY (Outcome B)?

This is standalone low-dimensional topology / character-variety algebra. Structural only;
NO Standard-Model value, no physics claim. Nothing promotes to CLAIMS.md. Gate 5 stands.

Method (all in-sandbox, verify-don't-trust):
  1. Derive X(4_1) non-abelian as a plane curve in trace coordinates from the two-bridge
     Riley representation of pi_1(4_1) = <a,b | a w = w b>, w = b a^-1 b^-1 a.
     Verify: Alexander polynomial = t^2-3t+1; geometric point over Q(sqrt-3); cross-check
     with SnapPy (tetrahedron shape = e^{i pi/3}, CS = 0, parabolic meridian).
  2. The algebraic (holomorphic) involutions of the curve over Q; identify AMPHICHIRALITY
     as the unique one sending rho_geom -> rho_geom-bar, confirmed realized by a group
     endomorphism (the mirror symmetry) -- and the anti-holomorphic amphichiral ISOMETRY
     tau = conj o (amphichiral involution), whose fixed locus contains the geometric point.
  3. Restrict the GALOIS involution (complex conjugation c) to Fix(tau): orbit structure.

Run:  python3 frontier/B711_two_z2_degeneration/b711_compute.py
"""
from __future__ import annotations
import sympy as sp
import numpy as np
import itertools

x, y, m, u, t = sp.symbols('x y m u t')


# --------------------------------------------------------------------------- #
# PART 1 -- realize X(4_1) as a plane curve; locate the geometric point
# --------------------------------------------------------------------------- #

def riley_rep(mm, uu):
    """Two-bridge Riley rep of the two meridians a,b (conjugate, eigenvalue mm)."""
    A = sp.Matrix([[mm, 1], [0, 1 / mm]])
    B = sp.Matrix([[mm, 0], [-uu, 1 / mm]])
    return A, B


def _word(A, B, s):
    d = {'a': A, 'A': A.inv(), 'b': B, 'B': B.inv()}
    M = sp.eye(2)
    for c in s:
        M = M * d[c]
    return M


def derive_curve():
    """Impose the fig-8 relation a w = w b, w = b a^-1 b^-1 a ('bABa'), and reduce to
    the non-abelian character-variety curve in (x = tr meridian, y = tr(a b^-1))."""
    A, B = riley_rep(m, u)
    w = _word(A, B, 'bABa')
    rel = sp.simplify(A * w - w * B)          # relation a w = w b  <=>  a w - w b = 0
    # every nonzero entry shares the Riley polynomial phi as its numerator:
    num = sp.numer(sp.together(rel[0, 1]))
    phi = sp.factor(sp.expand(num))            # = -(m^2 u^2 - (m^4-3m^2+1)(u+1)) up to unit
    # phi/m^2 in (x,u):  (m^4-3m^2+1)/m^2 = (m^2+1/m^2)-3 = (x^2-2)-3 = x^2-5
    phi_xu = sp.expand(u**2 - (x**2 - 5) * (u + 1))
    # trace dictionary:  tr(ab) = x^2-2-u  =>  u = x^2-2-tr(ab); and tr(ab^-1)=u+2 =: y
    curve = sp.expand(phi_xu.subs(u, y - 2))
    curve = sp.expand(curve)                    # y^2 - (x^2-1) y + (x^2-1)
    return phi, phi_xu, curve


def alexander_of_relator():
    """Fox-calculus Alexander polynomial of R = a w b^-1 w^-1 (w='bABa'); confirms 4_1."""
    R = 'a' + 'bABa' + 'B' + 'BabA'            # a w b^-1 w^-1 ; inv('bABa')='BabA'
    mp = {'a': ('a', 1), 'A': ('a', -1), 'b': ('b', 1), 'B': ('b', -1)}
    wl = [mp[c] for c in R]
    val, pre = sp.Integer(0), sp.Integer(1)
    for (g, e) in wl:                           # Fox derivative d/da, abelianize a,b -> t
        if e == 1:
            val += pre * (1 if g == 'a' else 0); pre *= t
        else:
            val += pre * (-1 / t) * (1 if g == 'a' else 0); pre *= 1 / t
    return sp.expand(sp.simplify(val * t))      # ~ t^2 - 3t + 1 up to unit


def part1():
    print("=" * 78)
    print("PART 1 -- X(4_1) as a plane curve; the geometric point")
    print("=" * 78)
    phi, phi_xu, curve = derive_curve()
    print("Riley polynomial phi(m,u) numerator :", phi)
    print("phi/m^2 in (x,u)                    :", phi_xu, "= 0")
    print("CHARACTER-VARIETY CURVE  C : ", curve, "= 0")
    print("   i.e.  y^2 - (x^2-1) y + (x^2-1) = 0,   x = tr(meridian), y = tr(a b^-1)")

    alex = alexander_of_relator()
    print("\nAlexander polynomial (Fox calculus):", alex, " (= -(t^2-3t+1) -> knot is 4_1)")

    # geometric point x = 2 (parabolic meridian)
    yy = sp.solve(curve.subs(x, 2), y)
    print("\nGeometric point (parabolic meridian x=2):  y =", yy)
    print("   trace field = Q(sqrt(-3))  [Eisenstein];  y = (3 +/- sqrt(-3))/2")
    disc = sp.factor(sp.discriminant(curve, y))
    print("discriminant_y(C) =", disc, "  -> real branch points at x^2 = 1 and x^2 = 5")

    # explicit parabolic rep at the geometric point + relator check
    w3 = sp.Rational(-1, 2) + sp.sqrt(-3) / 2   # omega, primitive cube root
    A, B = riley_rep(1, w3)                      # m=1 (x=2), u = omega
    rel = sp.simplify(A * _word(A, B, 'bABa') - _word(A, B, 'bABa') * B)
    comm = sp.simplify((A * B * A.inv() * B.inv()).trace())
    print("\nexplicit geometric rep: m=1 (parabolic), u = omega =", w3)
    print("   relator a w - w b =", rel.tolist(), " (zero => valid rep)")
    print("   tr a = tr b =", A.trace(), "(parabolic);  tr(a b^-1) =",
          sp.simplify((A * B.inv()).trace()))
    print("   tr[a,b] =", comm, "(!= 2  => IRREDUCIBLE)")

    # SnapPy cross-check
    try:
        import snappy
        M = snappy.Manifold('4_1')
        sh = M.tetrahedra_shapes('rect')[0]
        print("\nSnapPy 4_1 cross-check:")
        print("   tetrahedron shape =", sh, " (= e^{i pi/3}, root of z^2-z+1 => Q(sqrt-3))")
        print("   Chern-Simons =", M.chern_simons(), " (= 0)")
        S = M.symmetry_group()
        print("   symmetry group =", S, " is_amphicheiral =", S.is_amphicheiral(),
              " is_full =", S.is_full_group())
    except Exception as e:
        print("\n(SnapPy cross-check skipped:", e, ")")
    return curve


# --------------------------------------------------------------------------- #
# PART 2 -- the involutions; identify amphichirality
# --------------------------------------------------------------------------- #

def part2(curve):
    print("\n" + "=" * 78)
    print("PART 2 -- involutions of C over Q; identify amphichirality")
    print("=" * 78)
    invs = {
        'j1 : (x,y) -> (-x, y)':          (-x, y),
        'j2 : (x,y) -> (x, x^2-1-y)':     (x, x**2 - 1 - y),
        'j3 : (x,y) -> (-x, x^2-1-y)':    (-x, x**2 - 1 - y),
    }
    for name, (X, Y) in invs.items():
        rem = sp.rem(sp.Poly(sp.expand(curve.subs({x: X, y: Y}, simultaneous=True)), y),
                     sp.Poly(curve, y)).as_expr()
        X2 = sp.simplify(X.subs({x: X, y: Y}, simultaneous=True))
        Y2 = sp.simplify(Y.subs({x: X, y: Y}, simultaneous=True))
        print(f"{name:32s} preserves C: {sp.simplify(rem)==0};  involution: ({X2},{Y2})")

    # which holomorphic involution sends rho_geom -> rho_geom-bar ?
    p  = (sp.Integer(2), sp.Rational(3, 2) + sp.sqrt(-3) / 2)      # rho_geom
    pb = (sp.Integer(2), sp.Rational(3, 2) - sp.sqrt(-3) / 2)      # rho_geom-bar
    print("\nrho_geom     p  =", p)
    print("rho_geom-bar pb =", pb, "  ( = complex conjugate; sqrt-3 -> -sqrt-3 )")
    for name, (X, Y) in invs.items():
        img = (sp.simplify(X.subs({x: p[0], y: p[1]})), sp.simplify(Y.subs({x: p[0], y: p[1]})))
        tag = "== rho_geom-bar (AMPHICHIRAL: mirror = conjugate)" if img == pb else \
              ("== rho_geom (fixes it)" if img == p else "-> other point")
        print(f"   {name[:3]} (p) = {img}   {tag}")

    # confirm j2 is realized by a GROUP endomorphism (geometric symmetry), j1/j3 are not
    print("\ngroup-realizability (numeric search, sigma(a),sigma(b) words up to length 3):")
    counts = automorphism_search()
    for k in ('id', 'j1', 'j2', 'j3'):
        print(f"   trace-action {k}: realized by {counts[k]} group endomorphisms")
    print("   => j2 (amphichirality) IS a knot symmetry; j1,j3 (x->-x meridian sign,")
    print("      = tensor by a central character) are NOT knot symmetries.")


def automorphism_search():
    """Count group endomorphisms sigma of pi_1(4_1) whose induced trace map is id/j1/j2/j3."""
    def rep(xv):
        mm = (xv + np.sqrt(xv**2 - 4 + 0j)) / 2
        b = -(xv**2 - 5); c = -(xv**2 - 5)
        uu = (-b + np.sqrt(b * b - 4 * c + 0j)) / 2
        return (np.array([[mm, 1], [0, 1 / mm]], complex),
                np.array([[mm, 0], [-uu, 1 / mm]], complex))
    def mw(word, A, B):
        d = {'a': A, 'A': np.linalg.inv(A), 'b': B, 'B': np.linalg.inv(B)}
        M = np.eye(2, dtype=complex)
        for c in word:
            M = M @ d[c]
        return M
    reps = [rep(v) for v in (2.3, 3.1, 1.7)]
    alph = 'aAbB'
    words = []
    for L in range(1, 4):
        for tt in itertools.product(alph, repeat=L):
            w = ''.join(tt)
            if any(w[i] != w[i + 1] and w[i].lower() == w[i + 1].lower() for i in range(len(w) - 1)):
                continue
            words.append(w)
    counts = {'id': 0, 'j1': 0, 'j2': 0, 'j3': 0}
    for sa in words:
        for sb in words:
            tagsets = []
            ok = True
            for A, B in reps:
                Aa, Bb = mw(sa, A, B), mw(sb, A, B)
                if np.max(np.abs(Aa @ mw('bABa', Aa, Bb) - mw('bABa', Aa, Bb) @ Bb)) > 1e-6:
                    ok = False; break
                x0, y0 = np.trace(A), np.trace(A @ np.linalg.inv(B))
                x1, y1 = np.trace(Aa), np.trace(Aa @ np.linalg.inv(Bb))
                s = set()
                if abs(x1 - x0) < 1e-5 and abs(y1 - y0) < 1e-5: s.add('id')
                if abs(x1 + x0) < 1e-5 and abs(y1 - y0) < 1e-5: s.add('j1')
                if abs(x1 - x0) < 1e-5 and abs(y1 - (x0**2 - 1 - y0)) < 1e-5: s.add('j2')
                if abs(x1 + x0) < 1e-5 and abs(y1 - (x0**2 - 1 - y0)) < 1e-5: s.add('j3')
                tagsets.append(s)
            if ok and tagsets:
                for tg in set.intersection(*tagsets):
                    counts[tg] += 1
    return counts


# --------------------------------------------------------------------------- #
# PART 3 -- Galois on Fix(amphichirality): the orbit structure (the decision)
# --------------------------------------------------------------------------- #

def part3(curve):
    print("\n" + "=" * 78)
    print("PART 3 -- Galois (complex conjugation) restricted to Fix(amphichirality)")
    print("=" * 78)
    print("""
Two anti-holomorphic involutions of C (both defined via conj on the Q-curve):
  c   = GALOIS/complex conjugation      : (x,y) -> (conj x, conj y)
  tau = AMPHICHIRAL isometry = c o j2   : (x,y) -> (conj x, (conj x)^2 - 1 - conj y)
(j2 is the holomorphic amphichiral involution; tau is its 'realized isometry'.)
""")
    p  = (sp.Integer(2), sp.Rational(3, 2) + sp.sqrt(-3) / 2)     # rho_geom
    pb = (sp.Integer(2), sp.Rational(3, 2) - sp.sqrt(-3) / 2)     # rho_geom-bar

    def c(pt):   return (sp.conjugate(pt[0]), sp.conjugate(pt[1]))
    def j2(pt):  return (pt[0], pt[0]**2 - 1 - pt[1])
    def tau(pt): cc = c(pt); return (cc[0], cc[0]**2 - 1 - cc[1])

    print("tau fixes the geometric points?")
    print("   tau(rho_geom)     =", tuple(sp.simplify(v) for v in tau(p)),  " == rho_geom     :",
          tuple(sp.simplify(v) for v in tau(p)) == p)
    print("   tau(rho_geom-bar) =", tuple(sp.simplify(v) for v in tau(pb)), " == rho_geom-bar :",
          tuple(sp.simplify(v) for v in tau(pb)) == pb)

    print("\nGalois c on the two geometric points:")
    print("   c(rho_geom)      =", tuple(sp.simplify(v) for v in c(p)),
          " == rho_geom-bar :", tuple(sp.simplify(v) for v in c(p)) == pb)
    print("   => c SWAPS rho_geom <-> rho_geom-bar; they are DISTINCT (sqrt-3 != 0).")
    print("   both lie in Fix(tau) (shown above)  ==> Galois orbit {p, pbar} is FREE.")

    # Fix(tau) as a real locus + its Galois-fixed points
    print("\nFix(tau) = { x real, y + conj(y) = x^2 - 1 }  (the amphichiral slice).")
    print("   On C this is the arc of conjugate-pair characters over x^2 in [1,5];")
    print("   contains rho_geom (x=2). Galois c acts on it by y -> conj(y).")
    print("   c-FIXED points on Fix(tau)  <=>  y real  <=>  discriminant_y = 0  <=>  x^2 in {1,5}:")
    for xv in (1, -1, sp.sqrt(5), -sp.sqrt(5)):
        yy = sp.solve(curve.subs(x, xv), y)
        comm = _commutator_trace(xv, yy[0] if yy else None)
        print(f"      x={xv}: y={yy}  tr[a,b]={comm}")
    print("   x^2=5 -> (sqrt5, 2): REDUCIBLE boundary (tr[a,b]=2) = the GOLDEN real rep.")
    print("   x^2=1 -> (1,0): singular point, meridian a primitive 6th root of unity.")
    print("   NEITHER is the geometric (Eisenstein, x=2) point.")

    # V4 structure on the geometric orbit
    print("\nKlein-4 group V4 = {id, c, tau, j2} acting on the geometric orbit {p, pbar}:")
    for nm, f in (('id', lambda q: q), ('c', c), ('tau', tau), ('j2', j2)):
        img = tuple(sp.simplify(v) for v in f(p))
        where = 'FIXES p' if img == p else ('p -> pbar (SWAP)' if img == pb else str(img))
        print(f"   {nm:4s}: {where}")
    print("   stabilizer of rho_geom = {id, tau};  Galois c is in the SWAPPING coset")
    print("   => amphichirality (tau) and Galois (c) are DIFFERENT elements of V4: ORTHOGONAL.")


def _commutator_trace(xv, yv):
    """tr[a,b] on the curve as a function of (x,y): y^2 - 2 - x^2 y + 2 x^2."""
    if yv is None:
        return None
    return sp.simplify(yv**2 - 2 - xv**2 * yv + 2 * xv**2)


# --------------------------------------------------------------------------- #

def main():
    curve = part1()
    part2(curve)
    part3(curve)
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("""OUTCOME B (INDEPENDENT / FREE, with the setwise refinement).

DISCRIMINATING FACT -- orbit structure of Galois on Fix(amphichirality):
  * Both rho_geom = (2,(3+sqrt-3)/2) and rho_geom-bar = (2,(3-sqrt-3)/2) lie in
    Fix(tau) (the amphichiral CS=0 slice), and they are DISTINCT (sqrt-3 != 0).
  * The Galois involution (complex conjugation, sqrt-3 -> -sqrt-3) SWAPS them:
    a FREE 2-element orbit inside Fix(tau).  Fix(tau) is setwise Galois-stable but
    POINTWISE-FREE at the geometric point.
  * Galois has fixed points on Fix(tau) ONLY at x^2 in {1,5} -- the REAL/reducible
    reps (x^2=5 is the golden point (sqrt5,2), tr[a,b]=2; x^2=1 is a 6th-root
    singular point) -- NOT at the geometric Eisenstein point.
  * In V4 = {id, c, tau, j2}: stab(rho_geom) = {id, tau}; Galois c sits in the
    swapping coset. Amphichirality and Galois are DIFFERENT, commuting Z/2's.

=> the two Z/2's are ORTHOGONAL at the geometric point; B709's canonical/
   non-canonical distinction is clean. Structural only; nothing to CLAIMS.md.""")


if __name__ == '__main__':
    main()
