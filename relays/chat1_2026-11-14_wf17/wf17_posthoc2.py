#!/usr/bin/env python3
"""W-F17, post hoc 2 (committed before its run). m = 5 by a second method, with m = 1-4 and 6 as controls.

NOT BLIND for m = 1-4 and 6: the sealed run's output there has been read, and the method was developed on those values.
BLIND for m = 5: no output of any analysis at m = 5 has been seen (the sealed run and post hoc 1 timed out). While the
method was developed, one identity was checked at m = 1-7, m = 5 included: that the three equations below are the
fixed ideal's generators up to sign (no decomposition, count or locus at m = 5 was computed).

THE METHOD (this seat's own; it shares the sealed script's maps Ta, Tb only through their definition). Ta^-1 fixes x
and acts on (y, z) linearly with coefficients in x; Tb fixes y and acts on (x, z) linearly with coefficients in y. So
Tb^m(p) = Ta^-m(p) is three equations linear in z:
    A_i(x, y) z = B_i(x, y),  i = 1, 2, 3,
    A = (S_(m-1)(y), S_(m-1)(x), S_m(y) + S_(m-2)(x)),
    B = ((1 + S_(m-2)(y)) x, (S_m(x) - 1) y, S_(m-1)(y) x + S_(m-1)(x) y),
S the Chebyshev polynomials of the sealed script (S_-1 = 0, S_0 = 1, S_(k+1) = t S_k - S_(k-1)). Projecting to (x, y):
  - the vertical part: {A = B = 0} x C_z (lines, if that plane set is finite);
  - over {A != 0}, z = B_i / A_i is unique and the condition is that the minors A_i B_j - A_j B_i vanish. Their common
    zeros are Z(G) (G their gcd) and the finite set Z(M') (M' = minors / G). A point of Z(M') off Z(G) with some
    A_i != 0 is an isolated point of the fixed locus; a factor F of G gives a curve unless every A_i vanishes on it
    (then a surface if every B_i does too, else nothing).
  So the decomposition is complete by construction: the vertical lines, one curve for each factor of G, and the
  isolated points (tested: the ideal M' + (1 - w G L) is the unit ideal, L a random combination of the A_i, two draws).
  kappa = x^2 + y^2 + z^2 - xyz - 2. Points on kappa = 2: the vertical lines' (z^2 - x y z + x^2 + y^2 - 4 = 0) plus
  the points off them: with K_i = A_i^2 (x^2 + y^2 - 4) + B_i^2 - x y A_i B_i, a point (x, y) with some A_i != 0 and
  the minors zero has kappa = 2 exactly when every K_i vanishes, and where every A_i vanishes the ideal (M, K) vanishes
  exactly on the vertical set; so the count off the lines is #V(M, K_1, K_2, K_3) - #(vertical set), distinct points. kappa constant on a geometric component: tested at
  every point where the curve meets a random line, by the derivative of kappa along the curve (-F_y, F_x) (50 digits;
  "varies" when its modulus exceeds 1e-20 at every such point).

EXPECTATIONS (the sealed card's, for m = 5, committed with the sealed script before any run; and post hoc 1's H1):
  E0  The three equations are the fixed ideal's generators up to sign, for m = 1..7.
  T4  m = 5: the four lines {x = r, y = r'}, r, r' roots of s^2 + s - 1, lie in the fixed locus and are components;
      lines over C: 4. H1: they form two Q-components, {x = y, x^2 + x - 1 = 0} and {x + y = -1, x^2 + x - 1 = 0}.
  T5  m = 5: no isolated point and no surface; the origin lies on a one-dimensional component.
  T6  m = 5: m^2 + 2 = 27 points on kappa = 2.
  T7  m = 5: kappa is not constant on any one-dimensional component (here: on any geometric component).
  Controls, m = 1-4 and 6 (the sealed output, read): components over Q 1, 2, 2, 4, 6; points on kappa = 2: 3, 6, 11,
      18, 38; no isolated point; kappa varies on every component.
  Plants: P1 S_(m-3) in place of S_(m-2) in A_3 fails E0 at every m >= 2; P2 the isolated-point test with G replaced
      by 1 reports isolated points at every m (the curves' points); P3 the derivative test applied to F itself (zero
      along the curve) reports "constant" for every curve.
  Reported, no expectation: m = 5's curves over Q (degree in (x, y), whether they contain (0, 0) and (2, 2)), their
  factorisation over Q(sqrt 5), and the time.

    python3 -I -u wf17_posthoc2.py
"""
import random
import time

import mpmath as mp
import sympy as sp
from sympy import QQ

mp.mp.dps = 50
x, y, z, w, s = sp.symbols("x y z w s")


def say(*a):
    print(*a, flush=True)


def S(n, t):
    a, b = sp.Integer(0), sp.Integer(1)
    if n == -1:
        return a
    for _ in range(n):
        a, b = b, sp.expand(t * b - a)
    return b


def system(m, plant=False):
    A = [S(m - 1, y), S(m - 1, x), sp.expand(S(m, y) + S(m - 3 if plant else m - 2, x))]
    B = [sp.expand((1 + S(m - 2, y)) * x), sp.expand((S(m, x) - 1) * y), sp.expand(S(m - 1, y) * x + S(m - 1, x) * y)]
    return A, B


def Ta_inv(p):
    X, Y, Z = p
    return (X, sp.expand(X * Y - Z), Y)


def Tb(p):
    X, Y, Z = p
    return (Z, Y, sp.expand(Y * Z - X))


def fixed(m):
    q = r = (x, y, z)
    for _ in range(m):
        q = Tb(q)
    for _ in range(m):
        r = Ta_inv(r)
    return [sp.expand(a - b) for a, b in zip(q, r)]


def e0(m, plant=False):
    A, B = system(m, plant)
    mine = [sp.expand(A[0] * z - B[0]), sp.expand(B[1] - A[1] * z), sp.expand(A[2] * z - B[2])]
    return all(sp.expand(f - g) == 0 or sp.expand(f + g) == 0 for f, g in zip(fixed(m), mine))


def P(f):
    return sp.Poly(f, x, y)


def divides(f, g):
    return sp.rem(P(g), P(f)).is_zero


def radical_count(gens, sat=None):
    """distinct points of V(gens) off V(sat), gens in x, y (zero-dimensional)"""
    if sat is not None:
        H = sp.groebner([sp.expand(g) for g in gens] + [sp.expand(1 - w * sat)], w, x, y, order="lex", domain=QQ)
        gens = [g for g in H.exprs if not g.has(w)]
    G = sp.groebner([sp.expand(g) for g in gens], x, y, order="grevlex", domain=QQ)
    if list(G.exprs) == [1]:
        return 0
    ex = [sp.sqf_part(next(g for g in sp.groebner(list(G.exprs), *o, order="lex", domain=QQ).exprs
                           if g.free_symbols <= {o[-1]})) for o in ((y, x), (x, y))]
    R = sp.groebner(list(G.exprs) + ex, x, y, order="grevlex", domain=QQ)
    LM = [P(sp.LM(g, x, y, order="grevlex")).monoms()[0] for g in R.exprs]
    bx = min(a for a, b in LM if b == 0)
    by = min(b for a, b in LM if a == 0)
    return sum(1 for i in range(bx) for j in range(by) if not any(i >= a and j >= b for a, b in LM))


def line_points(f, rng):
    """the points where f = 0 meets a random line y = c x + d, numerically"""
    c, d = sp.Rational(rng.randint(1, 97), rng.randint(1, 13)), sp.Rational(rng.randint(-50, 50), rng.randint(1, 7))
    u = sp.Poly(sp.expand(f.subs(y, c * x + d)), x)
    roots = mp.polyroots([mp.mpf(sp.Rational(a).p) / sp.Rational(a).q for a in u.all_coeffs()], maxsteps=400,
                         extraprec=400)
    return [(r, mp.mpf(c.p) / c.q * r + mp.mpf(d.p) / d.q) for r in roots]


def q_orbits(gens, c):
    """the number of Q-components of a finite set: irreducible factors of the minimal polynomial of x + c y on it"""
    H = sp.groebner([sp.expand(g) for g in gens] + [s - x - c * y], x, y, s, order="lex", domain=QQ)
    e = sp.sqf_part(next(g for g in H.exprs if g.free_symbols <= {s}))
    return len(sp.factor_list(e, s)[1])


def analyse(m, rng, plants=False):
    t0 = time.time()
    A, B = system(m)
    out = dict(m=m)
    M = [sp.expand(A[i] * B[j] - A[j] * B[i]) for i, j in ((0, 1), (0, 2), (1, 2))]
    G = sp.gcd(sp.gcd(M[0], M[1]), M[2])
    Mp = [sp.cancel(Mi / G) for Mi in M]
    # vertical part
    V0 = sp.groebner(A + B, x, y, order="grevlex", domain=QQ)
    v0_finite = list(V0.exprs) == [1] or radical_count(list(V0.exprs)) is not None
    nV = radical_count(list(V0.exprs)) if list(V0.exprs) != [1] else 0
    out["vertical lines"] = nV
    out["vertical ideal"] = [str(g) for g in V0.exprs]
    # curves
    fl = [f for f, _e in sp.factor_list(G, x, y)[1] if P(f).total_degree() > 0]
    curves, surfaces = [], 0
    for f in fl:
        a0 = all(divides(f, a) for a in A)
        if a0 and all(divides(f, b) for b in B):
            surfaces += 1
        elif not a0:
            curves.append(f)
    out["surfaces"] = surfaces
    # isolated points
    iso = []
    for k in (1, 2):
        L = sum(rng.randint(1, 50) * a for a in A)
        J = sp.groebner([sp.expand(p) for p in Mp] + [sp.expand(1 - w * G * L)], w, x, y, order="grevlex", domain=QQ)
        iso.append(list(J.exprs) == [1])
    out["no isolated point"] = iso
    if plants:
        L = sum(rng.randint(1, 50) * a for a in A)
        J = sp.groebner([sp.expand(p) for p in M] + [sp.expand(1 - w * L)], w, x, y, order="grevlex", domain=QQ)
        out["P2 fires"] = list(J.exprs) != [1]
    # origin
    on0 = [f for f in curves if f.subs({x: 0, y: 0}) == 0 and any(a.subs({x: 0, y: 0}) != 0 for a in A)]
    z0 = [sp.Rational(b.subs({x: 0, y: 0}), a.subs({x: 0, y: 0})) for a, b in zip(A, B) if a.subs({x: 0, y: 0}) != 0]
    out["origin on a curve"] = bool(on0) and all(v == 0 for v in z0)
    out["origin on a vertical line"] = all(g.subs({x: 0, y: 0}) == 0 for g in V0.exprs)
    # kappa = 2
    Ks = [sp.expand(a ** 2 * (x ** 2 + y ** 2 - 4) + b ** 2 - x * y * a * b) for a, b in zip(A, B)]
    cnt = radical_count(M + Ks) - nV
    vert_k2 = 0
    if nV:
        H = sp.groebner(list(V0.exprs) + [z ** 2 - x * y * z + x ** 2 + y ** 2 - 4], x, y, z, order="grevlex",
                        domain=QQ)
        ex = [sp.sqf_part(next(g for g in sp.groebner(list(H.exprs), *o, order="lex", domain=QQ).exprs
                               if g.free_symbols <= {o[-1]})) for o in ((y, z, x), (x, z, y), (x, y, z))]
        R = sp.groebner(list(H.exprs) + ex, x, y, z, order="grevlex", domain=QQ)
        LM = [sp.Poly(sp.LM(g, x, y, z, order="grevlex"), x, y, z).monoms()[0] for g in R.exprs]
        bd = [min(mo[i] for mo in LM if all(mo[j] == 0 for j in range(3) if j != i)) for i in range(3)]
        vert_k2 = sum(1 for i in range(bd[0]) for j in range(bd[1]) for k in range(bd[2])
                      if not any(i >= mo[0] and j >= mo[1] and k >= mo[2] for mo in LM))
    out["kappa=2 points (off the vertical lines)"] = cnt
    out["kappa=2 points (on the vertical lines)"] = vert_k2
    out["kappa=2 points"] = cnt + vert_k2
    # kappa along each curve, at the points where it meets a random line
    rows, varies, p3 = [], True, True
    for f in curves:
        i = next(i for i in range(3) if not divides(f, A[i]))
        kt = sp.together((x ** 2 + y ** 2 + (B[i] / A[i]) ** 2 - x * y * (B[i] / A[i]) - 2))
        fx, fy = sp.diff(f, x), sp.diff(f, y)
        dk = sp.diff(kt, x) * (-fy) + sp.diff(kt, y) * fx
        dkf = sp.lambdify((x, y), dk, "mpmath")
        dff = sp.lambdify((x, y), sp.diff(f, x) * (-fy) + sp.diff(f, y) * fx, "mpmath")
        Af = sp.lambdify((x, y), A[i], "mpmath")
        pts = [p for p in line_points(f, rng) if abs(Af(*p)) > mp.mpf(10) ** -20]
        mags = [abs(dkf(*p)) for p in pts]
        v = bool(pts) and min(mags) > mp.mpf(10) ** -20
        varies &= v
        if plants:
            p3 &= max(abs(dff(*p)) for p in pts) < mp.mpf(10) ** -20
        rows.append(dict(degree=P(f).total_degree(), poly=str(f) if P(f).total_degree() <= 3 else "(degree %d)"
                         % P(f).total_degree(), origin=f.subs({x: 0, y: 0}) == 0, trivial=f.subs({x: 2, y: 2}) == 0,
                         points=len(pts), min_dkappa=mp.nstr(min(mags), 3) if mags else None, varies=v))
    out["curves"] = rows
    out["kappa varies on every curve"] = varies
    if plants:
        out["P3 fires"] = p3
    out["vertical lines over Q (two draws)"] = [q_orbits(list(V0.exprs), c) if nV else 0 for c in (7, 19)]
    out["components over Q"] = len(curves) + out["vertical lines over Q (two draws)"][0]
    out["seconds"] = round(time.time() - t0, 1)
    out["_V0"], out["_curves"] = V0, curves
    return out


if __name__ == "__main__":
    import sys
    MS = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 6, 5]
    say("E0 (the three equations are the fixed ideal up to sign), m = 1..7:", [e0(m) for m in range(1, 8)])
    say("P1 (S_(m-3) in A_3) fails E0 at every m >= 2:", all(not e0(m, plant=True) for m in range(2, 8)))
    rng = random.Random(1735)
    for m in MS:
        r = analyse(m, rng, plants=True)
        say("m", m, {k: v for k, v in r.items() if not k.startswith("_") and k != "curves"})
        for row in r["curves"]:
            say("    curve", row)
        if m == 5:
            r5 = [sp.Rational(-1, 2) + sp.sqrt(5) / 2, sp.Rational(-1, 2) - sp.sqrt(5) / 2]
            lines4 = all(all(sp.simplify(g.subs({x: a, y: b})) == 0 for g in r["_V0"].exprs) for a in r5 for b in r5)
            q1 = sp.groebner([x - y, x ** 2 + x - 1], x, y, order="grevlex", domain=QQ)
            q2 = sp.groebner([x + y + 1, x ** 2 + x - 1], x, y, order="grevlex", domain=QQ)
            both = sp.groebner([sp.expand(a * b) for a in q1.exprs for b in q2.exprs], x, y, order="grevlex",
                               domain=QQ)
            same = all(both.contains(g) for g in r["_V0"].exprs) and all(r["_V0"].contains(g) for g in both.exprs)
            say("T4 m 5: the four lines inside:", lines4, "| vertical lines over C:", r["vertical lines"],
                "| the vertical set is {x = y, x^2 + x - 1 = 0} and {x + y = -1, x^2 + x - 1 = 0} (H1):", same)
            for f in r["_curves"]:
                say("    curve of degree", P(f).total_degree(), "over Q(sqrt 5):",
                    [(P(g).total_degree(), e) for g, e in sp.factor_list(f, x, y, extension=sp.sqrt(5))[1]])
            say("T5 m 5 holds:", r["surfaces"] == 0 and all(r["no isolated point"]) and
                (r["origin on a curve"] or r["origin on a vertical line"]),
                "| T6 m 5 holds:", r["kappa=2 points"] == 27, "| T7 m 5 holds:", r["kappa varies on every curve"])
