"""B1881 -- the web seat's two relays of 2026-11-11, verified on main with main's own code.

  (A) WHAT SYMMETRY ALLOWS A STATE OF THE WHOLE (its exact facts Q1 to Q7 and R1 to R9), and
  (B) THE READ-OUT AS A VALUE (its sealed card V0 to V3 and its checks after the review).

Data-free.  Part A is integers, exact algebra and numerics at 50 digits on classical objects (the two level-5 quotients and
their symmetries).  Part B is the record's flat-fibre instrument (B1857) on run sequences, in exact continued fractions.  No
value of tau on record is read, none is compared, and no frame is evaluated at any point named here.  Nothing of the seat's
code is run or imported; its printed numbers are typed below only as the things to be recomputed.
[CORRECTED 2026-11-12, found by a second reading of Review 79's mends: this header said 'reproduced' here and at E10.  The record
keeps that word for the same code run again; none of the seat's code was run, so every number here is recomputed.]

EXPECTATIONS, WRITTEN BEFORE THE FIRST RUN (each says how it could fail)
 E1  The quotients.  Rows (alpha, b) mod 5, a move g acting by u -> u g^-1, the mark v = (1, 3).  The moves keeping +-v have
     index 12 with cusp widths 1, 1, 5, 5 and no elliptic point; those keeping the line have index 6, widths 1, 5 and two
     elliptic points of order 2; both have genus 0.  Fails if the orbit of S and T on the twelve rows up to sign, or on the
     six lines, is not what is said.
 E2  The elliptic points of the line's quotient are i and -1 + i in the mark's frame, and the elliptic element exchanges the
     twins.  By hand: v S^-1 = 2v.  Fails if S fixes another pair of lines.
 E3  The dual involution W = g0^-1 [[0,-1],[5,0]] g0 is [[-3,-14],[1,3]]; its fixed points are the roots of forms of
     discriminant -20; exactly two classes under the group, one for each form class (1,0,5) and (2,2,3); at each the fixing
     matrix has square -5 and its kernel on the points of order 5 is the mark.  By hand the kernel is alpha = 0.  Fails if
     two fixed points with the same form class are NOT related by an element of the group (then there are more than two).
 E4  t = (eta(tau)/eta(5 tau))^6: t(tau) t(-1/(5 tau)) = 125; t = +5 sqrt 5 and -5 sqrt 5 at the two fixed points; the
     elliptic points are t = -11 +- 2i; the mirror is t -> conj t.  So W with the mirror fixes the circle |t|^2 = 125.
 E5  s, the fifth power of the Rogers-Ramanujan fraction: t = 1/s - 11 - s; the twin exchange is s -> -1/s; W lifts to
     s -> (beta s + 1)/(s - beta), beta = (-11 - 5 sqrt 5)/2.  The three holomorphic involutions have six fixed points in
     all, none common to two of them; the group they generate with the mirror has order 8 and the six points fall into
     exactly three pairs.  Fails if a point is fixed by both the twin exchange and W (then one place would be allowed).
 E6  j(tau) = j(5 tau) at exactly ten points of the line's quotient: the roots of (t^2-125)(t^2+22t+125)(t^2+4t+125)
     (t^2+18t+125)(t^2-14t+125), all on |t|^2 = 125.  By hand they are the tori with an endomorphism of norm 5, of
     discriminants -4, -11, -16, -19 and -20, so j there is 1728, -32768, 287496, -884736 and the two conjugates of
     discriminant -20; which factor carries which is not predicted.
 E7  The tick F = [[0,1],[1,1]]: F^2 is the ground, det F = -1, v F = 3v, F = S^-1 m with m = [[-1,-1],[0,1]] acting as
     tau -> -conj(tau) - 1; S keeps the line and exchanges the twins; m keeps +-v.
 E8  Weight 1 and weight 2 at the two elliptic points: each odd character's Eisenstein series vanishes at one and not the
     other; E2(tau) - 5 E2(5 tau) vanishes at both and is a constant times the product of the two.
 E9  The instrument.  H_i = (r_i + x_i + y_i)/2, the same number as B1875's sqrt(tr^2 - 4)/(2 c_i).  Own values:
     (6) 3.618034, (11) 6.118034, (2,1,2,1,2) 1.723607; a run of n has own value (n-1)/2 + sqrt5/2 exactly in the limit
     (by hand: n/2 + 1/phi); the runs 6, 11, 16, 21, 26 keep the line and 7 does not.
 E10 Copies and mixtures: every number the relay prints is recomputed to its printed digits.  The rate is DERIVED, not only
     observed: one golden period is the map x -> 1/(1 + 1/(1 + x)), whose derivative at its fixed point 1/phi is phi^-4.
     So the distance falls by a factor tending to phi^4 = 6.854102 per period.  Fails if the ratios tend elsewhere.
 E11 The short-gap facts: (6) with one period reads 3.6515; (6)_1(6)_2 reads 3.6371, below it; A = (2,1,1,4,4) and
     B = (2,1,2,4,4) keep the line with own values 2.418183 and 2.423508; in A_1 B_2 the apex is in A at 2.425956, and in
     A_2 B_3, A_4 B_5, A_8 B_9 it is in B.
 (After the first run: three of main's own checks failed and none of the seat's facts.  Two used a constant computed in double
  precision inside a 30-digit series, and one asked for a figure, 0.93 percent, that main had typed and the relay does not
  print.  The checks are mended in place and say so; no expectation above is changed.)
 E12 Main's own question, not the seat's: is 'keeps the line' the same set of run sequences in the seat's convention
     (rows, v = (1,3), the ground [[1,1],[1,2]]) and in B1872's (columns, v = (1,2), the ground [[2,1],[1,1]])?  Not
     predicted.  It decides whether the two arcs speak of one allowed set.
     [CORRECTED 2026-11-12, twice.  At Review 79: the second convention is not B1872's, whose run prints the seat's, rows.  It
     is this arc's own.  At the second reading of that mend: it is not the transpose either, as the mend said.  The seat's
     ground is symmetric, so its transpose is itself.  The second convention is the seat's with every matrix conjugated by
     the swap of the two coordinates, the order of the letters kept, read on the column (1,2).  That column is the swap of
     (2,1), the column the row (1,3) annihilates mod 5.  A row is kept by a matrix exactly when the column it annihilates
     is, so the two tests are one test on every matrix of determinant 1 mod 5, and the agreement asked for here could fail
     only by an error of coding.  The arc's lock computes this on all 120 matrices, with a mark for which it fails.]
"""
import itertools
import json
import pathlib
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 50
OUT, RES, FAILS = [], {}, []


def P(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s)


def check(name, ok, detail=""):
    RES[name] = bool(ok)
    if not ok:
        FAILS.append(name)
    P("   [%s] %s%s" % ("ok" if ok else "FAILS", name, (" -- " + str(detail)) if detail else ""))
    return ok


# ------------------------------------------------------------------------------------------------ integers, 2 x 2
def mul(A, B):
    return (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])


def det(A):
    return A[0] * A[3] - A[1] * A[2]


def inv(A):
    d = det(A)
    assert d in (1, -1)
    return (A[3] * d, -A[1] * d, -A[2] * d, A[0] * d)


def rowmul(u, A, n=5):
    return ((u[0] * A[0] + u[1] * A[2]) % n, (u[0] * A[1] + u[1] * A[3]) % n)


def act(u, g):                      # the record's action on rows (B1733): u -> u g^-1
    return rowmul(u, inv(g))


def up_to_sign(u):
    return min((u[0] % 5, u[1] % 5), ((-u[0]) % 5, (-u[1]) % 5))


def line(u):
    return min(((k * u[0]) % 5, (k * u[1]) % 5) for k in (1, 2, 3, 4))


I2, S, T = (1, 0, 0, 1), (0, -1, 1, 0), (1, 1, 0, 1)
V = (1, 3)
ROWS = sorted({up_to_sign((a, b)) for a in range(5) for b in range(5) if (a, b) != (0, 0)})
LINES = sorted({line(u) for u in ROWS})


def cycles(perm):
    seen, out = set(), []
    for x in perm:
        if x in seen:
            continue
        n, y = 0, x
        while y not in seen:
            seen.add(y); y = perm[y]; n += 1
        out.append(n)
    return sorted(out)


def quotient(points, cls):
    """the quotient of the upper half-plane by the stabiliser of cls(V): index, cusp widths, elliptic points, genus"""
    pt = {p: cls(act(p, T)) for p in points}
    ps = {p: cls(act(p, S)) for p in points}
    pst = {p: cls(act(p, mul(S, T))) for p in points}
    orbit, todo = {cls(V)}, [cls(V)]
    while todo:
        x = todo.pop()
        for y in (pt[x], ps[x]):
            if y not in orbit:
                orbit.add(y); todo.append(y)
    mu, widths = len(orbit), cycles(pt)
    e2 = sum(1 for p in points if ps[p] == p)
    e3 = sum(1 for p in points if pst[p] == p)
    genus = Fr(1) + Fr(mu, 12) - Fr(e2, 4) - Fr(e3, 3) - Fr(len(widths), 2)
    return mu, widths, e2, e3, genus


def part_a():
    P("PART A. WHAT SYMMETRY ALLOWS A STATE OF THE WHOLE")
    P("A1. the two quotients (the seat's Q1)")
    qpm, qln = quotient(ROWS, up_to_sign), quotient(LINES, line)
    P("   one twin up to sign: index %d, cusp widths %s, elliptic points of order 2: %d, of order 3: %d, genus %s" % qpm)
    P("   the line:            index %d, cusp widths %s, elliptic points of order 2: %d, of order 3: %d, genus %s" % qln)
    check("E1 the quotient of one twin: index 12, widths 1 1 5 5, no elliptic point, genus 0", qpm == (12, [1, 1, 5, 5], 0, 0, 0))
    check("E1 the quotient of the line: index 6, widths 1 5, two elliptic points of order 2, genus 0", qln == (6, [1, 5], 2, 0, 0))

    P("A2. the elliptic points of the line's quotient (Q2, Q3)")
    fixed = [l for l in LINES if line(act(l, S)) == l]
    P("   the lines that S keeps: %s; v S^-1 = %s = 2v: %s" % (fixed, act(V, S), act(V, S) == rowmul((2, 0), (V[0], V[1], 0, 0)) or act(V, S) == ((2 * V[0]) % 5, (2 * V[1]) % 5)))
    Tm = inv(T)
    check("E2 S keeps exactly two lines: the mark's, and the line of v T^-1", sorted(fixed) == sorted([line(V), line(rowmul(V, Tm))]), fixed)
    # a point g(i) is elliptic for the line's group exactly when the line of v g is one that S keeps: g = 1 gives i, g = T^-1 gives i - 1
    check("E2 so the elliptic points are i and -1 + i in the mark's frame", line(rowmul(V, I2)) in fixed and line(rowmul(V, Tm)) in fixed)
    check("E2 the elliptic element S sends v to 2v: it keeps the line and exchanges the twins", act(V, S) == ((2 * V[0]) % 5, (2 * V[1]) % 5))
    e2 = mul(mul(Tm, S), T)             # T^-1 S T fixes i - 1
    check("E2 the other elliptic element T^-1 S T squares to -1 and sends v to +-2v", mul(e2, e2) == (-1, 0, 0, -1) and up_to_sign(act(V, e2)) == up_to_sign(((2 * V[0]) % 5, (2 * V[1]) % 5)), e2)
    # the twin exchange is the class of any move keeping the line and not +-v; S is one; its square keeps +-v
    check("E2 the twin exchange squares into the group of one twin", up_to_sign(act(V, mul(S, S))) == up_to_sign(V))

    P("A3. the dual involution and its fixed points (Q4, Q5, Q6, R1, R2)")
    g0 = (0, -1, 1, 3)
    check("the frame change g0 has (0,1) g0 = v and determinant 1", rowmul((0, 1), g0) == V and det(g0) == 1)
    W5 = (0, -1, 5, 0)
    W = mul(mul(inv(g0), W5), g0)
    check("E3 W = g0^-1 [[0,-1],[5,0]] g0 = [[-3,-14],[1,3]], det 5, W^2 = -5", W == (-3, -14, 1, 3) and det(W) == 5 and mul(W, W) == (-5, 0, 0, -5), W)
    a, b, c, d = sp.symbols("a b c d")
    g = sp.Matrix([[a, b], [5 * c, d]])
    lhs = sp.Matrix([[0, -1], [5, 0]]) * g * sp.Matrix([[0, -1], [5, 0]]).inv()
    check("E3 (R1) W5 [[a,b],[5c,d]] W5^-1 = [[d,-c],[-5b,a]], symbolically", sp.simplify(lhs - sp.Matrix([[d, -c], [-5 * b, a]])) == sp.zeros(2, 2))
    # fixed points in the standard frame: M = W5 gamma with trace 0 is [[-5c,-d],[5a,5c]] with a d - 5 c^2 = 1; its fixed point is
    # the root of 5a x^2 + 10c x + d, of discriminant -20
    pts = []
    for cc in range(-12, 13):
        for aa in range(1, 60):
            num = 1 + 5 * cc * cc
            if num % aa:
                continue
            dd = num // aa
            M = (-5 * cc, -dd, 5 * aa, 5 * cc)
            assert det(M) == 5 and M[0] + M[3] == 0 and mul(M, M) == (-5, 0, 0, -5)
            gam = (aa, cc, 5 * cc, dd)                 # gamma = W5^-1 M, in the group: lower-left 0 mod 5
            assert det(gam) == 1 and mul(W5, gam) == M
            pts.append((aa, cc, dd))

    def reduce_form(A, B, C):
        """SL2(Z)-reduction of A x^2 + B x y + C y^2, returning the reduced form and the matrix g with (form o g) reduced"""
        g = I2
        while True:
            if C < A:
                A, B, C = C, -B, A; g = mul(g, S)
            elif B > A or B <= -A:
                k = (A - B) // (2 * A)
                A, B, C = A, B + 2 * k * A, A * k * k + B * k + C; g = mul(g, (1, k, 0, 1))
            else:
                break
        if A == C and B < 0:
            A, B, C = C, -B, A; g = mul(g, S)
        return (A, B, C), g
    classes = {}
    for (aa, cc, dd) in pts:
        red, g = reduce_form(5 * aa, 10 * cc, dd)
        classes.setdefault(red, []).append(((aa, cc, dd), g))
    P("   trace-0 matrices of determinant 5 in the coset found: %d; their forms reduce to: %s" % (len(pts), {str(k): len(v) for k, v in classes.items()}))
    check("E3 the fixed points fall into exactly the two form classes (1,0,5) and (2,2,3) of discriminant -20", sorted(classes) == [(1, 0, 5), (2, 2, 3)])
    # two fixed points with one reduced form: tau1 = g1(tau_red), tau2 = g2(tau_red), so tau2 = g2 g1^-1 tau1; the stabiliser of a
    # point of discriminant -20 is +-1, so they are one point of the quotient exactly when g2 g1^-1 has lower-left 0 mod 5
    one_class = True
    for red, lst in classes.items():
        g1 = lst[0][1]
        for (_, g2) in lst[1:]:
            h = mul(g2, inv(g1))
            if h[2] % 5:
                one_class = False
    check("E3 any two fixed points with the same form are related by an element of the group: exactly two fixed points", one_class)
    dres = {str(red): sorted({min(x[0][2] % 5, (-x[0][2]) % 5) for x in lst}) for red, lst in classes.items()}
    check("E3 (R2) gamma = W5^-1 M has d = +-1 mod 5 in the class (1,0,5) and +-2 in (2,2,3), for every one found", dres == {"(1, 0, 5)": [1], "(2, 2, 3)": [2]}, dres)
    # the kernel of the endomorphism mu = 5a tau + 5c on the points (alpha tau + b)/5: by hand it is alpha = 0.  In integers: with
    # 5a tau^2 = -(10 c tau + d), mu (alpha tau + b)/5 = (a b - c alpha) tau + (c b - alpha d / 5), a lattice point iff 5 | alpha d
    ker_ok = all(sorted((al, bb) for al in range(5) for bb in range(5) if (al * dd) % 5 == 0) == [(0, bb) for bb in range(5)] for (aa, cc, dd) in pts)
    check("E3 at every one the kernel of the fixing matrix on the points of order 5 is the mark (0, b)", ker_ok)
    # the mirror tau -> -conj(tau) is conjugation by diag(-1, 1): it keeps lower-left 0 mod 5
    # CORRECTED 2026-11-12 (Review 79): this check was passed the literal True.  It is computed now: for every matrix of the group
    # with entries in a box, the conjugate by diag(-1, 1) is multiplied out and compared with the stated form, and is in the group.
    def _conj_by_mirror(a, b, c5, d):
        m = [[a, b], [c5, d]]; j = [[-1, 0], [0, 1]]
        jm = [[sum(j[i][k] * m[k][l] for k in range(2)) for l in range(2)] for i in range(2)]
        return [[sum(jm[i][k] * j[k][l] for k in range(2)) for l in range(2)] for i in range(2)]          # j is its own inverse
    box = [(a, b, 5 * c, d) for a in range(-12, 13) for b in range(-12, 13) for c in range(-3, 4) for d in range(-12, 13) if a * d - 5 * b * c == 1]
    mirror_ok = all(_conj_by_mirror(a, b, c5, d) == [[a, -b], [-c5, d]] and (-c5) % 5 == 0 and a * d - (-b) * (-c5) == 1 for a, b, c5, d in box)
    check("E3 (Q5) the mirror normalises the group: [[a,b],[5c,d]] -> [[a,-b],[-5c,d]]", mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200, "%d matrices of the group multiplied out, %d of them with a lower-left entry that is not zero" % (len(box), sum(1 for x in box if x[2] != 0)))
    tau1, tau2 = mp.mpc(0, 1) / mp.sqrt(5), mp.mpf(1) / 2 + mp.mpc(0, 1) / (2 * mp.sqrt(5))
    check("E3 the fixed point i/sqrt5 is on the mirror's axis; the other, 1/2 + i/(2 sqrt5), goes to its translate by -1", abs(-mp.conj(tau1) - tau1) < mp.mpf(10) ** -45 and abs(-mp.conj(tau2) - (tau2 - 1)) < mp.mpf(10) ** -45)
    e_plus, e_minus = (2 + mp.mpc(0, 1)) / 5, (-2 + mp.mpc(0, 1)) / 5
    check("E3 W5 and the mirror each exchange the two elliptic points (+-2 + i)/5", abs(-1 / (5 * e_plus) - e_minus) < mp.mpf(10) ** -45 and abs(-mp.conj(e_plus) - e_minus) < mp.mpf(10) ** -45)

    P("A4. the coordinate t (Q7, R6)")
    def eta(tau):
        q = mp.exp(2j * mp.pi * tau)
        return mp.exp(2j * mp.pi * tau / 24) * mp.qp(q)

    def t_of(tau):
        return (eta(tau) / eta(5 * tau)) ** 6
    z = mp.mpc("0.137", "0.412")
    tol = mp.mpf(10) ** -40
    check("E4 t(z) t(-1/(5z)) = 125 at a point with no symmetry", abs(t_of(z) * t_of(-1 / (5 * z)) - 125) < tol)
    check("E4 t = +5 sqrt5 at i/sqrt5 and -5 sqrt5 at 1/2 + i/(2 sqrt5)", abs(t_of(tau1) - 5 * mp.sqrt(5)) < tol and abs(t_of(tau2) + 5 * mp.sqrt(5)) < tol)
    tp, tm = t_of(e_plus), t_of(e_minus)
    P("   t at (2+i)/5: %s ; t at (-2+i)/5: %s" % (mp.nstr(tp, 12), mp.nstr(tm, 12)))
    check("E4 the elliptic points are t = -11 +- 2i", {(round(float(x.real), 9), round(float(x.imag), 9)) for x in (tp, tm)} == {(-11.0, 2.0), (-11.0, -2.0)} and abs(tp - mp.conj(tm)) < tol)
    check("E4 the mirror is t -> conj t", abs(t_of(-mp.conj(z)) - mp.conj(t_of(z))) < tol)
    check("E4 so W with the mirror is t -> 125/conj t, with fixed set |t|^2 = 125; both fixed points and both elliptic points lie on it",
          all(abs(abs(x) ** 2 - 125) < tol for x in (t_of(tau1), t_of(tau2), tp, tm)))

    P("A5. the coordinate s of the quotient of one twin, and the three pairs (R3, R4, Q6)")
    def rr5(tau):                      # the fifth power of the Rogers-Ramanujan continued fraction
        q = mp.exp(2j * mp.pi * tau)
        prod = mp.mpf(1)
        for n in range(1, 400):
            leg = {0: 0, 1: 1, 4: 1, 2: -1, 3: -1}[n % 5]
            if leg:
                prod *= (1 - q ** n) ** leg
        return q * prod ** 5
    s_z = rr5(z)
    check("E5 t = 1/s - 11 - s at a point with no symmetry", abs(1 / s_z - 11 - s_z - t_of(z)) < mp.mpf(10) ** -35)
    gam = (2, -1, 5, -2)               # in the line's group (lower-left 0 mod 5), d = -2: not in the group of one twin
    gz = (gam[0] * z + gam[1]) / (gam[2] * z + gam[3])
    check("E5 the twin exchange is s -> -1/s (the move [[2,-1],[5,-2]])", det(gam) == 1 and abs(rr5(gz) + 1 / s_z) < mp.mpf(10) ** -35)
    check("E5 the mirror is s -> conj s", abs(rr5(-mp.conj(z)) - mp.conj(s_z)) < mp.mpf(10) ** -35)
    s, r5 = sp.symbols("s"), sp.sqrt(5)
    tt = lambda x: 1 / x - 11 - x
    beta = (-11 - 5 * r5) / 2
    Ws = (beta * s + 1) / (s - beta)
    Wds = sp.simplify(-1 / Ws)
    check("E5 s -> (beta s + 1)/(s - beta) is an involution and lifts t -> 125/t", sp.simplify(Ws.subs(s, Ws) - s) == 0 and sp.simplify(tt(Ws) * tt(s) - 125) == 0)
    check("E5 its product with the twin exchange is the other lift, also an involution", sp.simplify(Wds.subs(s, Wds) - s) == 0 and sp.simplify(tt(Wds) * tt(s) - 125) == 0)
    fix = {"the twin exchange": sp.solve(sp.Eq(s, -1 / s), s), "W": sp.solve(sp.Eq(s, Ws), s), "W with the twin exchange": sp.solve(sp.Eq(s, Wds), s)}
    for k, v in fix.items():
        P("   fixed by %s: %s, at t = %s" % (k, [sp.nsimplify(x) for x in v], sorted({str(sp.nsimplify(sp.simplify(tt(x)))) for x in v})))
    six = [x for v in fix.values() for x in v]
    numeric = [complex(sp.N(x, 30)) for x in six]
    distinct = all(abs(numeric[i] - numeric[j]) > 1e-9 for i in range(6) for j in range(i))
    check("E5 the three holomorphic involutions have two fixed points each, six in all, no point common to two", len(six) == 6 and distinct)
    check("E5 the twin exchange fixes s = +-i, over the two elliptic points t = -11 -+ 2i", {complex(sp.N(x)) for x in fix["the twin exchange"]} == {1j, -1j}
          and {str(sp.simplify(tt(x))) for x in fix["the twin exchange"]} == {"-11 - 2*I", "-11 + 2*I"})
    over = {k: {str(sp.nsimplify(sp.simplify(tt(x)))) for x in v} for k, v in fix.items()}
    check("E5 W fixes the two twins over one of t = +-5 sqrt5, and W with the twin exchange the two over the other", {frozenset(over["W"]), frozenset(over["W with the twin exchange"])} == {frozenset({"5*sqrt(5)"}), frozenset({"-5*sqrt(5)"})},
          {k: sorted(v) for k, v in over.items()})     # sorted 2026-11-12: a set was printed here, in an order that changed from run to run
    # the group of order 8 on the six points: orbits and stabilisers
    maps = {"d": lambda x: -1 / x, "W": lambda x: (beta * x + 1) / (x - beta), "m": lambda x: sp.conjugate(x)}
    def key(x):
        c = complex(sp.N(x, 30)); return (round(c.real, 9), round(c.imag, 9))
    words = [w for n in range(0, 4) for w in itertools.product("dWm", repeat=n)]
    group = {}
    samples = [sp.Rational(3, 7) + sp.I * sp.Rational(2, 5), sp.Rational(-5, 3) + sp.I * sp.Rational(1, 9)]
    for w in words:
        img = []
        for x0 in samples:
            x = x0
            for ch in w:
                x = maps[ch](x)
            img.append(key(x))
        group.setdefault(tuple(img), w)
    check("E5 the twin exchange, W and the mirror generate a group of order 8 on the sphere", len(group) == 8, len(group))
    orbs, stabs = {}, {}
    for x0 in six:
        orb, st = set(), 0
        for w in group.values():
            x = x0
            for ch in w:
                x = maps[ch](x)
            orb.add(key(x)); st += key(x) == key(x0)
        orbs[key(x0)] = frozenset(orb); stabs[key(x0)] = st
    P("   orbits of the six points: sizes %s; stabiliser orders %s" % (sorted(len(o) for o in set(orbs.values())), sorted(stabs.values())))
    check("E5 the six points fall into exactly three pairs, each point with a stabiliser of order 4; no point is fixed by the whole group",
          sorted(len(o) for o in set(orbs.values())) == [2, 2, 2] and set(stabs.values()) == {4})

    P("A6. where the torus is isomorphic to its quotient by the marked line (R5)")
    def jinv(tau):
        return 1728 * mp.kleinj(tau)
    tz = t_of(z)
    check("the classical formulas: j(tau) = (t^2+250t+3125)^3/t^5 and j(5 tau) = (t^2+10t+5)^3/t, at a point with no symmetry",
          abs(jinv(z) - (tz ** 2 + 250 * tz + 3125) ** 3 / tz ** 5) / abs(jinv(z)) < mp.mpf(10) ** -30 and abs(jinv(5 * z) - (tz ** 2 + 10 * tz + 5) ** 3 / tz) / abs(jinv(5 * z)) < mp.mpf(10) ** -30)
    t = sp.symbols("t")
    poly = sp.factor((t ** 2 + 250 * t + 3125) ** 3 - t ** 4 * (t ** 2 + 10 * t + 5) ** 3)
    want = -(t ** 2 - 125) * (t ** 2 + 22 * t + 125) * (t ** 2 + 4 * t + 125) * (t ** 2 + 18 * t + 125) * (t ** 2 - 14 * t + 125)
    P("   j(tau) - j(5 tau), cleared of denominators: %s" % poly)
    check("E6 it is -(t^2-125)(t^2+22t+125)(t^2+4t+125)(t^2+18t+125)(t^2-14t+125): ten points", sp.expand(poly - want) == 0)
    jt = (t ** 2 + 250 * t + 3125) ** 3 / t ** 5
    jvals = {}
    for fac in (t ** 2 + 22 * t + 125, t ** 2 + 4 * t + 125, t ** 2 + 18 * t + 125, t ** 2 - 14 * t + 125, t ** 2 - 125):
        roots = sp.solve(fac, t)
        jvals[str(fac)] = sorted({str(sp.nsimplify(sp.simplify(sp.expand(jt.subs(t, r))))) for r in roots})
        assert all(sp.simplify(sp.Abs(r) ** 2 - 125) == 0 for r in roots)
        P("   %-18s j = %s" % (fac, jvals[str(fac)]))
    rational = sorted(int(v[0]) for k, v in jvals.items() if len(v) == 1)
    check("E6 all ten lie on |t|^2 = 125, and j there is 1728, -32768, 287496, -884736 (discriminants -4, -11, -16, -19) and the two conjugates of discriminant -20",
          rational == sorted([1728, -32768, 287496, -884736]) and len(jvals["t**2 - 125"]) == 2, rational)
    check("E6 the pair over i is among the ten: t^2 + 22t + 125 has the roots -11 +- 2i and j = 1728 there", jvals["t**2 + 22*t + 125"] == ["1728"])

    P("A7. the tick (R7, R8)")
    L, R = (1, 0, 1, 1), (1, 1, 0, 1)
    ground = mul(L, R)
    F, m = (0, 1, 1, 1), (-1, -1, 0, 1)
    check("E7 the ground [[1,1],[1,2]] has v as its row line; F^2 is the ground; det F = -1; v F = 3v", rowmul(V, ground) == ((4 * V[0]) % 5, (4 * V[1]) % 5) and mul(F, F) == ground and det(F) == -1 and rowmul(V, F) == ((3 * V[0]) % 5, (3 * V[1]) % 5))
    check("E7 F = S^-1 m with m = [[-1,-1],[0,1]], m^2 = 1, and m keeps +-v", mul(inv(S), m) == F and mul(m, m) == I2 and up_to_sign(rowmul(V, m)) == up_to_sign(V))
    x = mp.mpc("0.31", "0.77")
    Fx = (F[0] * mp.conj(x) + F[1]) / (F[2] * mp.conj(x) + F[3])
    check("E7 on tau: F is tau -> 1/(conj tau + 1), which is S^-1 after tau -> -conj(tau) - 1", abs(Fx - (-1 / (-mp.conj(x) - 1))) < tol)
    check("E7 so if the tick is an act the mark's mirror is a move of the group that keeps the line (S keeps the line: v S^-1 = 2v)", line(act(V, S)) == line(V))
    P("   then the quotient is the line's with each point joined to its mirror image, t ~ conj t; W becomes t -> 125/t with 125/conj t,")
    P("   and its fixed set is the image of |t|^2 = 125: an arc from +5 sqrt5 through the point over i to -5 sqrt5")

    P("A8. weight 1 and weight 2 at the elliptic points (R9)")
    def chi(n, which):                 # the two odd characters mod 5: chi(2) = +i or -i
        n %= 5
        if n == 0:
            return 0
        k = {1: 0, 2: 1, 4: 2, 3: 3}[n]
        return mp.mpc(0, 1 if which > 0 else -1) ** k          # exact fourth roots of unity at the working precision

    def eis1(tau, which, terms=500):
        q = mp.exp(2j * mp.pi * tau)
        c0 = -sum(a * chi(a, which) for a in range(1, 5)) / mp.mpf(10)        # L(0, chi)/2 = -B_{1,chi}/2
        tot = mp.mpc(c0)
        for n in range(1, terms):
            sdiv = sum(chi(dv, which) for dv in range(1, n + 1) if n % dv == 0)
            if sdiv:
                tot += sdiv * q ** n
        return tot

    def e2(tau, terms=500):
        q = mp.exp(2j * mp.pi * tau)
        return 1 - 24 * sum(sum(dv for dv in range(1, n + 1) if n % dv == 0) * q ** n for n in range(1, terms))

    def w2(tau):
        return e2(tau) - 5 * e2(5 * tau)
    mp.mp.dps = 30
    vals = {(w, nm): abs(eis1(pt, w)) for w in (1, -1) for nm, pt in (("(2+i)/5", e_plus), ("(-2+i)/5", e_minus))}
    for k, v in vals.items():
        P("   |E1 with chi(2) = %si| at %s = %s" % ("+" if k[0] > 0 else "-", k[1], mp.nstr(v, 8)))
    small = sorted(k for k, v in vals.items() if v < mp.mpf(10) ** -20)
    check("E8 each odd character's weight-1 series vanishes at one elliptic point and not at the other, the two characters at different points",
          len(small) == 2 and small[0][0] != small[1][0] and small[0][1] != small[1][1] and all(v > mp.mpf("0.01") for k, v in vals.items() if k not in small), small)
    check("E8 E2(tau) - 5 E2(5 tau) vanishes at both elliptic points", abs(w2(e_plus)) < mp.mpf(10) ** -20 and abs(w2(e_minus)) < mp.mpf(10) ** -20)
    z1, z2 = mp.mpc("0.137", "0.412"), mp.mpc("-0.291", "0.553")
    ratio = [w2(zz) / (eis1(zz, 1) * eis1(zz, -1)) for zz in (z1, z2)]
    check("E8 and is a constant times the product of the two weight-1 series (the same ratio at two points)", abs(ratio[0] - ratio[1]) < mp.mpf(10) ** -18, mp.nstr(ratio[0], 10))
    mp.mp.dps = 50
    RES["A_numbers"] = {"quotient_one_twin": [qpm[0], qpm[1], qpm[2], qpm[3], str(qpm[4])], "quotient_line": [qln[0], qln[1], qln[2], qln[3], str(qln[4])],
                        "W": list(W), "fixed_point_matrices_found": len(pts), "form_classes": {str(k): len(v) for k, v in classes.items()},
                        "j_at_the_ten_points": jvals, "weight_2_over_product_of_weight_1": mp.nstr(ratio[0], 12)}


# ------------------------------------------------------------------------------------------------ PART B: the instrument
def cf_value(seq):
    """the purely periodic continued fraction [a1; a2, ..., an, a1, ...] as an mpf, from the exact integer matrix of one period"""
    p, q, r, s = 1, 0, 0, 1
    for a in seq:
        p, q, r, s = p * a + q, p, r * a + s, r
    disc = (p + s) ** 2 - 4 * (p * s - q * r)
    return ((p - s) + mp.sqrt(disc)) / (2 * r)


def heights(runs):
    """H_i = (r_i + x_i + y_i)/2 for a cyclic run sequence: x_i reads forward from run i, y_i backward"""
    n = len(runs)
    out = []
    for i in range(n):
        fwd = [runs[(i + 1 + k) % n] for k in range(n)]
        bwd = [runs[(i - 1 - k) % n] for k in range(n)]
        out.append((runs[i] + 1 / cf_value(fwd) + 1 / cf_value(bwd)) / 2)
    return out


def heights_by_matrix(runs):
    """the same by B1875's form: sqrt(tr^2 - 4)/(2 c_i), c_i the lower-left entry of the word started in the middle of... run i.
    Here: the word started at run i, conjugated to put half of run i on each side, has its fixed points symmetric about r_i/2."""
    n = len(runs)
    Lm, Rm = lambda k: (1, k, 0, 1), lambda k: (1, 0, k, 1)
    out = []
    for i in range(n):
        Wd = I2
        for k in range(n):
            j = (i + k) % n
            Wd = mul(Wd, Lm(runs[j]) if k % 2 == 0 else Rm(runs[j]))
        tr = Wd[0] + Wd[3]
        out.append(mp.sqrt(mp.mpf(tr * tr - 4)) / (2 * abs(Wd[2])))
    return out


def closed(dep, g):
    return list(dep) + [1] * (2 * g + 1)


def composite(deps, k):
    runs, owner = [], []
    for j, dep in enumerate(deps):
        runs += list(dep); owner += [j] * len(dep)
        runs += [1] * (2 * (k + j) + 1); owner += [None] * (2 * (k + j) + 1)
    return runs, owner


def keeps_line_seat(runs):
    """the seat's convention: L = [[1,0],[1,1]], R = [[1,1],[0,1]], rows, v = (1,3)"""
    Wd = I2
    for k, r in enumerate(runs):
        Wd = mul(Wd, (1, 0, r % 5, 1) if k % 2 == 0 else (1, r % 5, 0, 1))
    return line(rowmul(V, Wd)) == line(V)


def keeps_line_main(runs):
    """this arc's second convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]], columns, v = (1,2).
    [CORRECTED 2026-11-12: this read "B1872's convention".  B1872 writes the seat's, rows.  These letters are the seat's
    conjugated by the swap of the two coordinates; see the note at E12 in the header.]"""
    Wd = I2
    for k, r in enumerate(runs):
        Wd = mul(Wd, (1, r % 5, 0, 1) if k % 2 == 0 else (1, 0, r % 5, 1))
    col = ((Wd[0] * 1 + Wd[1] * 2) % 5, (Wd[2] * 1 + Wd[3] * 2) % 5)
    return line(col) == line((1, 2))


def part_b():
    P("")
    P("PART B. THE READ-OUT AS A VALUE")
    mp.mp.dps = 120
    phi = (1 + mp.sqrt(5)) / 2
    D6, D11, D5 = (6,), (11,), (2, 1, 2, 1, 2)
    P("B1. the instrument, two ways")
    test = closed(D5, 2)
    h1, h2 = heights(test), heights_by_matrix(test)
    check("E9 (r + x + y)/2 is sqrt(tr^2 - 4)/(2c) for the word started at that run, on (2,1,2,1,2) closed by two periods", max(abs(a - b) for a, b in zip(h1, h2)) < mp.mpf(10) ** -100)
    own = {}
    for name, dep in (("(6)", D6), ("(11)", D11), ("(2,1,2,1,2)", D5)):
        own[name] = max(heights(closed(dep, 60)))
        P("   own value of %-12s %s" % (name, mp.nstr(own[name], 12)))
    check("E9 (V0) own values 3.618034, 6.118034 and 1.723607", [mp.nstr(own[k], 7) for k in ("(6)", "(11)", "(2,1,2,1,2)")] == ["3.618034", "6.118034", "1.723607"])
    P("B2. the single runs (V3)")
    runs_ok = []
    for n in (6, 11, 16, 21, 26):
        v = max(heights(closed((n,), 60)))
        exact = mp.mpf(n - 1) / 2 + mp.sqrt(5) / 2
        runs_ok.append(abs(v - exact) < mp.mpf(10) ** -40 and all(keeps_line_seat(closed((n,), g)) for g in range(0, 6)))
        P("   run of %2d: own value %s, (n-1)/2 + sqrt5/2 to 1e-40: %s, keeps the line: %s" % (n, mp.nstr(v, 10), abs(v - exact) < mp.mpf(10) ** -40, keeps_line_seat(closed((n,), 1))))
    check("E9 (V3) the runs 6, 11, 16, 21, 26 keep the line; their own values are (n-1)/2 + sqrt5/2 to 1e-40 and increase", all(runs_ok))
    check("E9 (V3) the control, a run of 7, does not keep the line", not any(keeps_line_seat(closed((7,), g)) for g in range(0, 6)))
    check("E9 a run of n keeps the line exactly when n = 1 mod 5 (n to 40)", all(keeps_line_seat(closed((n,), 1)) == (n % 5 == 1) for n in range(1, 41)))
    check("E9 by hand: n/2 + 1/phi = (n-1)/2 + sqrt5/2", abs(mp.mpf(3) + 1 / phi - (mp.mpf(5) / 2 + mp.sqrt(5) / 2)) < mp.mpf(10) ** -100)

    P("B3. copies of one departure (V1)")
    KS = (1, 2, 4, 8, 16)
    table, rates, spreads = {}, {}, {}
    for name, dep in (("(6)", D6), ("(11)", D11), ("(2,1,2,1,2)", D5)):
        for m in (2, 3, 4):
            ds, off, sp_ = [], [], []
            for k in KS:
                runs, owner = composite([dep] * m, k)
                h = heights(runs)
                # each copy's reading: the greatest height among its own runs
                reads = [max(h[i] for i in range(len(runs)) if owner[i] == j) for j in range(m)]
                apex_i = max(range(len(runs)), key=lambda i: h[i])
                assert owner[apex_i] is not None
                ds.append(max(abs(x - own[name]) for x in reads))
                sp_.append(max(reads) - min(reads))
            table[(name, m)] = ds; spreads[(name, m)] = sp_
            rates[(name, m)] = mp.log(ds[3] / ds[4]) / 8
            P("   %d copies of %-12s distance from the own value at k = 1, 2, 4, 8, 16: %s ; rate %s" % (m, name, " ".join(mp.nstr(x, 2) for x in ds), mp.nstr(rates[(name, m)], 7)))
    six2 = [mp.nstr(x, 2) for x in table[("(6)", 2)]]
    check("E10 (V1) copies of (6): 0.019, 0.0028, 5.9e-5, 2.7e-8, 5.4e-15, the same for two, three and four copies to two figures",
          six2 == ["0.019", "0.0028", "5.9e-5", "2.7e-8", "5.4e-15"] and all([mp.nstr(x, 2) for x in table[("(6)", m)]] == six2 for m in (3, 4)), six2)
    check("E10 (V1) copies of (11): 0.023 at k = 1; copies of (2,1,2,1,2): 0.00069 at k = 1", mp.nstr(table[("(11)", 2)][0], 2) == "0.023" and mp.nstr(table[("(2,1,2,1,2)", 2)][0], 2) == "0.00069")
    check("E10 (V1) the distances fall strictly with k and are below 1e-12 at k = 16, in all nine cases", all(all(ds[i] > ds[i + 1] for i in range(4)) and ds[4] < mp.mpf(10) ** -12 for ds in table.values()))
    check("E10 (V1) the rate between k = 8 and 16 is 1.924847 per golden period in all nine cases, against 4 ln phi = %s" % mp.nstr(4 * mp.log(phi), 7),
          all(mp.nstr(r, 7) == "1.924847" for r in rates.values()) and mp.nstr(4 * mp.log(phi), 7) == "1.924847")
    check("E10 (V1) two copies tie exactly (to 1e-100); the spread of three and of four falls with k", all(max(spreads[(n_, 2)]) < mp.mpf(10) ** -100 for n_ in ("(6)", "(11)", "(2,1,2,1,2)"))
          and all(all(s_[i] > s_[i + 1] for i in range(4)) for (n_, m_), s_ in spreads.items() if m_ > 2))
    # the rate, derived: one golden period is x -> 1/(1 + 1/(1 + x)); its derivative at the fixed point 1/phi
    xs = sp.symbols("x")
    per = 1 / (1 + 1 / (1 + xs))
    dphi = sp.simplify(sp.diff(per, xs).subs(xs, (sp.sqrt(5) - 1) / 2))
    check("E10 the rate derived: the derivative of one golden period at its fixed point is phi^-4, so the factor tends to phi^4 = %s" % mp.nstr(phi ** 4, 7),
          sp.simplify(per.subs(xs, (sp.sqrt(5) - 1) / 2) - (sp.sqrt(5) - 1) / 2) == 0 and sp.simplify(dphi - ((sp.sqrt(5) - 1) / 2) ** 4) == 0)
    steps = []
    for k in range(1, 7):
        d = []
        for kk in (k, k + 1):
            runs, owner = composite([D6, D6], kk)
            h = heights(runs)
            d.append(max(abs(max(h[i] for i in range(len(runs)) if owner[i] == j) - own["(6)"]) for j in (0, 1)))
        steps.append(d[0] / d[1])
    P("   step ratios for two copies of (6), k to k + 1, k = 1..6: %s" % " ".join(mp.nstr(x, 5) for x in steps))
    check("E10 the step ratios for two copies of (6) are 6.935, 6.866, 6.856, 6.8543, 6.8541, tending to phi^4",
          [mp.nstr(steps[0], 4), mp.nstr(steps[1], 4), mp.nstr(steps[2], 4), mp.nstr(steps[3], 5), mp.nstr(steps[4], 5)] == ["6.935", "6.866", "6.856", "6.8543", "6.8541"], [mp.nstr(x, 6) for x in steps])

    P("B4. different departures (V2)")
    mixes = {"(6)(11)": [D6, D11], "(11)(2,1,2,1,2)": [D11, D5], "(6)(6)(11)": [D6, D6, D11], "(11)(6)(2,1,2,1,2)": [D11, D6, D5], "(6)(2,1,2,1,2)": [D6, D5]}
    names = {D6: "(6)", D11: "(11)", D5: "(2,1,2,1,2)"}
    v2 = True
    for label, deps in mixes.items():
        deepest = max(deps, key=lambda dd: own[names[dd]])
        ds = []
        for k in KS:
            runs, owner = composite(deps, k)
            h = heights(runs)
            top = max(h)
            at = [i for i in range(len(runs)) if h[i] == top]
            if len(at) != 1 or owner[at[0]] is None or deps[owner[at[0]]] != deepest:
                v2 = False
            ds.append(abs(top - own[names[deepest]]))
        if not (all(ds[i] > ds[i + 1] for i in range(4)) and ds[4] < mp.mpf(6) * mp.mpf(10) ** -15):
            v2 = False
        P("   %-20s apex at a run of %-5s at every k; distance from its own value: %s" % (label, names[deepest], " ".join(mp.nstr(x, 2) for x in ds)))
    check("E10 (V2) in all five the apex is unique, at a run of the deepest departure; the distance falls strictly and is below 6e-15 at k = 16", v2)

    P("B5. short gaps (the seat's checks after its review)")
    one6 = max(heights(closed(D6, 1)))
    one11 = max(heights(closed(D11, 1)))
    # main's first run of this check asked for "0.93" percent, a figure main had typed and the relay does not print; the relay says
    # "nearly one percent" and "0.65%".  The offset is 0.9245 percent.  The check now asks what the relay says.
    # CORRECTED 2026-11-12 (Review 79): it did not; it asked for main's own figure, 0.92.  It asks for both now: main's figure, and
    # that the figure is what the relay calls nearly one percent, between 0.9 and 1.
    check("E11 (6) with one period on both sides reads 3.6515 against 3.6180, nearly one percent (0.92); (11) is 0.65 percent off",
          mp.nstr(one6, 5) == "3.6515" and mp.nstr(own["(6)"], 5) == "3.618" and mp.nstr((one6 - own["(6)"]) / own["(6)"] * 100, 2) == "0.92" and mp.mpf("0.9") < (one6 - own["(6)"]) / own["(6)"] * 100 < 1 and mp.nstr((one11 - own["(11)"]) / own["(11)"] * 100, 2) == "0.65",
          "%s, %s%%, %s%%" % (mp.nstr(one6, 6), mp.nstr((one6 - own["(6)"]) / own["(6)"] * 100, 3), mp.nstr((one11 - own["(11)"]) / own["(11)"] * 100, 3)))
    runs, owner = composite([D6, D6], 1)
    two = max(heights(runs))
    check("E11 a composite can read below its factor: (6)_1 (6)_2 reads 3.6371, below (6)_1 alone", mp.nstr(two, 5) == "3.6371" and two < one6, mp.nstr(two, 6))
    A, B = (2, 1, 1, 4, 4), (2, 1, 2, 4, 4)
    ownA, ownB = max(heights(closed(A, 60))), max(heights(closed(B, 60)))
    check("E11 A = (2,1,1,4,4) and B = (2,1,2,4,4) keep the line; own values 2.418183 and 2.423508", all(keeps_line_seat(closed(X, g)) for X in (A, B) for g in range(0, 5))
          and mp.nstr(ownA, 7) == "2.418183" and mp.nstr(ownB, 7) == "2.423508", "%s %s" % (mp.nstr(ownA, 8), mp.nstr(ownB, 8)))
    where = {}
    for k in (1, 2, 4, 8):
        runs, owner = composite([A, B], k)
        h = heights(runs)
        i = max(range(len(runs)), key=lambda q_: h[q_])
        where[k] = ("A" if owner[i] == 0 else "B", h[i])
    P("   A_k B_(k+1): the apex is in %s" % ", ".join("%s at k = %d (%s)" % (where[k][0], k, mp.nstr(where[k][1], 7)) for k in where))
    check("E11 the apex can sit at the shallower departure: in A_1 B_2 it is in A at 2.425956; in A_2 B_3, A_4 B_5, A_8 B_9 it is in B",
          where[1][0] == "A" and mp.nstr(where[1][1], 7) == "2.425956" and all(where[k][0] == "B" for k in (2, 4, 8)))
    gaps = {}
    for g in range(1, 13):
        runs = list(A) + [1] * (2 * g + 1) + list(B) + [1] * (2 * (g + 1) + 1)
        owner = [0] * 5 + [None] * (2 * g + 1) + [1] * 5 + [None] * (2 * (g + 1) + 1)
        h = heights(runs)
        gaps[g] = "A" if owner[max(range(len(runs)), key=lambda q_: h[q_])] == 0 else "B"
    check("E11 and for every gap from 2 to 12 it is in B (the referee's statement)", all(gaps[g] == "B" for g in range(2, 13)) and gaps[1] == "A", "".join(gaps[g] for g in range(1, 13)))

    P("B6. no greatest, and a least")
    lows = []
    for n in range(1, 7):
        for seq in itertools.product(range(1, 6), repeat=n):
            if n % 2 == 0:
                lows.append(max(heights(list(seq))))
    floor = min(lows)
    # CORRECTED 2026-11-12, found by a second reading of Review 79's mends: this label read "over every cyclic run sequence ...
    # (16275 sequences)".  16275 is the number of sequences as written.  The page was corrected at Review 79 and this label,
    # which the run and its file print, was not.  The counts up to rotation are computed here and not typed.
    seqs = [seq for n in (2, 4, 6) for seq in itertools.product(range(1, 6), repeat=n)]
    by_all = len({min(seq[i:] + seq[:i] for i in range(len(seq))) for seq in seqs})
    by_even = len({min(seq[i:] + seq[:i] for i in range(0, len(seq), 2)) for seq in seqs})
    RES["B_counts"] = {"sequences_as_written": len(lows), "up_to_every_rotation": by_all, "up_to_rotations_that_keep_the_letters": by_even}
    check("the least apex over every run sequence of length 2, 4, 6 with runs to 5, each read as a cycle, is the ground's own, sqrt5/2 "
          "(%d sequences as written; %d up to rotation; %d up to the rotations that keep which letter a run is)" % (len(lows), by_all, by_even),
          len(seqs) == len(lows) and abs(floor - mp.sqrt(5) / 2) < mp.mpf(10) ** -100, mp.nstr(floor, 10))
    # CORRECTED 2026-11-12 (Review 79): this check was passed the literal True, pointing at E9.  It is computed here.
    single = [max(heights(closed((5 * m + 1,), 60))) for m in range(1, 6)]
    single_ok = all(abs(v - (mp.mpf(5 * m) / 2 + mp.sqrt(5) / 2)) < mp.mpf(10) ** -40 for m, v in zip(range(1, 6), single)) and all(x < y for x, y in zip(single, single[1:]))
    check("the own values of the allowed single runs increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1", single_ok, "computed for m = 1..5, to 1e-40; the formula is unbounded in m")

    P("B7. main's own question: one allowed set in the two conventions?")
    agree = disagree = 0
    first = None
    for n in (2, 4, 6):
        for seq in itertools.product(range(1, 7), repeat=n):
            a_, b_ = keeps_line_seat(list(seq)), keeps_line_main(list(seq))
            if a_ == b_:
                agree += 1
            else:
                disagree += 1
                first = first or seq
    rev = sum(1 for n in (2, 4, 6) for seq in itertools.product(range(1, 7), repeat=n) if keeps_line_seat(list(seq)) != keeps_line_main(list(seq)[::-1]))
    rot = sum(1 for n in (2, 4, 6) for seq in itertools.product(range(1, 7), repeat=n) if keeps_line_seat(list(seq)) != keeps_line_main(list(seq)[1:] + list(seq)[:1]))
    P("   run sequences of length 2, 4, 6 with runs to 6: the two conventions agree on %d and differ on %d (first: %s)" % (agree, disagree, first))
    P("   against main's convention read on the REVERSED sequence they differ on %d; on the sequence ROTATED by one run, on %d" % (rev, rot))
    RES["B_numbers"] = {"own": {k: mp.nstr(v, 12) for k, v in own.items()}, "copies_of_6_distances": six2, "rate": mp.nstr(rates[("(6)", 2)], 10), "four_ln_phi": mp.nstr(4 * mp.log(phi), 10),
                        "step_ratios": [mp.nstr(x, 7) for x in steps], "phi4": mp.nstr(phi ** 4, 10), "A_then_B_apex_by_gap": gaps,
                        "conventions": {"agree": agree, "differ": disagree, "differ_against_reversed": rev, "differ_against_rotated": rot, "first_difference": list(first) if first else None}}
    # CORRECTED 2026-11-12 (main's own re-reading while mending the label above): this check passed if ANY of the three readings
    # agreed (disagree == 0 or rev == 0 or rot == 0), which is weaker than the page's sentence.  It asks now for what the page
    # says: no difference as written and none on the reversed sequence.  The rotated reading differs and is printed.
    name = "E12 the two conventions name one allowed set: no sequence differs as written, and none on the reversed sequence"
    RES[name] = (disagree == 0 and rev == 0 and agree == 6 ** 2 + 6 ** 4 + 6 ** 6)
    if not RES[name]:
        FAILS.append(name)
    P("   [%s] %s (as written %d differ of %d; reversed %d; rotated by one run %d)" % ("ok" if RES[name] else "FAILS", name, disagree, agree + disagree, rev, rot))


if __name__ == "__main__":
    part_a()
    part_b()
    P("")
    n = sum(1 for k, v in RES.items() if isinstance(v, bool))
    P("CHECKS: %d, FAILING: %d%s" % (n, len(FAILS), (" -- " + "; ".join(FAILS)) if FAILS else ""))
    (HERE / "whole_and_value_on_main.json").write_text(json.dumps({k: (v if isinstance(v, (bool, dict, list, str, int)) else str(v)) for k, v in RES.items()}, indent=1, default=str) + "\n", encoding="utf-8")
    (HERE / "whole_and_value_on_main_run.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
