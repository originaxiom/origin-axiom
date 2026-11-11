"""B1885 -- the golden state on the whole, and where its density is greatest: main's own check.

Three seats reached this object on 2026-11-11.  The agy lane sealed and ran a read-out on the whole on its own branch (agy:B1881);
the advisor seat recomputed its state and its peak from a closed form; the web seat sealed its own card on it.  This is main's
check, with main's own code, of the data-free part: the state, its symmetries, its zeros, the place where its density is
greatest, and the same recipe at two other levels.  None of the seats' code is run or imported.

Data-free.  No value of the modulus on record is read or compared, and no frame is evaluated at any point found here.  The
lane's own comparison with measurement is not read and not repeated.

THE OBJECT (Maass 1949, for the field of sqrt p; here by main's own construction)
  K = Q(sqrt p), p = 5, 13 or 17: class number one, fundamental unit e > 1 of norm -1.  R = pi/(2 ln e).
  For an ideal (a) of the integers of K:   psi((a)) = sgn(N a) |a/a'|^(iR).
  c(n) = the sum of psi over the ideals of norm n.  Then
      f(z) = sqrt(y) * sum_{n >= 1} c(n) K_{iR}(2 pi n y) sin(2 pi n x),    z = x + iy,
  is a form for the moves with lower-left entry 0 modulo p, with the character (d/p), and an eigenfunction of the hyperbolic
  Laplacian with eigenvalue 1/4 + R^2.

NOT BLIND.  Before writing this main had read the web seat's sealed header, which prints the point the lane reports.  Main
compares its own point with that one at the end, and with nothing else.

EXPECTATIONS, WRITTEN BEFORE THE FIRST RUN (each says how it could fail)
 H1  psi is well defined: sgn(N e) e^(2iR ln e) = (-1)(-1) = 1.  The Euler product: c(p) = -1 at the ramified prime; at an inert
     prime c vanishes on odd powers and is 1 on even ones; at a split prime c(q) = 2 sgn(N pi) cos(R ln|pi/pi'|).  Checked
     against a direct enumeration of ideals for n <= 40.  Fails if the two computations of c(n) disagree.
 H2  Automorphy at level 5: f(g z) = chi(d) f(z) for g = [[2,-1],[5,-2]], [[3,-2],[5,-3]] (factor -1 each) and [[1,0],[5,1]]
     (factor +1), at three points, to 1e-18.  Negative control: the cosine series with the same coefficients fails.
 H3  By hand, before any number: (a) the series is in sines, so f vanishes on the lines x = 0 and x = 1/2, which are fixed
     lines of the mirror z -> -conj(z) and of its translate: THE STATE IS ODD UNDER THE MIRROR, so its density has no greatest
     place on a mirror line, and every greatest place comes as a mirror pair.  (b) at an elliptic point with stabiliser g,
     f = chi(d_g) f, so f vanishes there when chi(d_g) = -1: at level 5 that is both elliptic points (d = +-2).
     Checked numerically.  Fails if f is not zero there.
 H4  The dual involution: f(-1/(5z)) = s f(z) with one sign s at every point.  The sign is not predicted by main.
 H5  On the arc of |z|^2 = 1/5 between the elliptic point (2+i)/5 and i/sqrt 5 the density f^2 has exactly one local maximum,
     strictly inside; it is a critical point in both directions with a negative definite Hessian; on a grid of the strip
     0 < x < 1/2, y >= 0.16, no value exceeds it.  Fails if the greatest value of the grid lies off the circle.
 H6  Main's point agrees with the one the lane reports (read from the web seat's header) to 1e-9.
 H7  THE OTHER LEVELS.  By hand, before any number: at level 13 the points of order 2 have d = +-5 with (5/13) = -1, so f
     vanishes there, and the points of order 3 have d = 3 or 9 with (3/13) = +1, so f need not vanish there; at level 17 the
     points of order 2 have d = +-4 with (4/17) = +1, so f need not vanish there.  Level 5 has no point of order 3.  So at 5
     the state must vanish at every point with a symmetry of its own, and at 13 and 17 it need not.  The advisor seat
     reports, post hoc, that the same recipe's density is greatest at such points at 13 and 17.  Main checks the forced zeros
     and the non-zeros numerically, and does not search for the greatest place at those levels.

AFTER THE FIRST RUN (2026-11-11), DISCLOSED
 The first run had 26 checks and 3 failed.
 (i)  Two were MAIN'S OWN FAULT and are mended here.  At levels 13 and 17 the automorphy was tested at a point whose image
      lies at height 0.0096 and 0.0053.  There the series needs about 1400 and 2500 terms, and it was cut at 400.  The two
      checks read 2.9e-11 and 2.5e-6.  Now each move is tested at two points chosen so that the point and its image both lie
      near height 1/p, and three moves are tested at each level, not two.  And the series REFUSES to be evaluated at a
      height where its cut is not negligible, so the fault cannot recur unseen.  No statement about the state failed.
 (ii) H6 FAILED AS WRITTEN and stays failed: the distance is 1.5e-9, not below 1e-9.  The expectation was not blind (main had
      read, in a commit headline of the web seat, that the gradient at the lane's point is 1e-7 of the peak).  What the run
      shows is recorded below under A6.
 ADDED AFTER THE FIRST RUN, on reading the web seat's relay in full; none of these was an expectation of main's:
 A1  The trace test (the web seat's referee's): at a critical point of f^2 where f is not zero, the two second derivatives
     of f^2 sum to -2 (1/4 + R^2) f^2 / y^2.  Fails if main's Hessian is not that of an eigenfunction's density.
 A2  f vanishes on the second stretch of the arc, the circle |z - 1/2|^2 = 1/20 between the elliptic point and
     1/2 + i/(2 sqrt 5).
 A3  f is even under the reflection in |z|^2 = 1/5 and odd under the reflection in |z - 1/2|^2 = 1/20.  So in the cell
     bounded by x = 0, x = 1/2 and the two circles the state vanishes on three sides and has zero normal derivative on
     the fourth, the one the greatest place lies on.
 A4  On the grid's points inside that cell f has one sign.  (A grid, not a proof.  If f has no zero in the open cell it is
     the lowest state of its own class of symmetry; that is not the statement that it is the lowest twin-odd state.)
 A5  The density against the chart's Euclidean area, f^2/y^2, is greatest elsewhere: the read-out depends on the measure.
 A6  At the lane's reported point: the full gradient, how much lower the density is, and how far it lies off the circle.
"""
import itertools
import json
import math
import pathlib

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 30
OUT, RES = [], {}


def P(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s, flush=True)


def check(name, ok, detail=""):
    RES[name] = bool(ok)
    P("   [%s] %s%s" % ("ok" if ok else "FAILS", name, (" -- " + str(detail)) if detail else ""))


def legendre(d, p):
    d %= p
    if d == 0:
        return 0
    return 1 if pow(d, (p - 1) // 2, p) == 1 else -1


class Field:
    """Q(sqrt p) for p = 1 mod 4: integers Z[w], w = (1 + sqrt p)/2, with N(a + b w) = a^2 + a b - (p-1)/4 b^2"""

    def __init__(self, p):
        self.p = p; self.m = (p - 1) // 4
        self.sq = mp.sqrt(p); self.w = (1 + self.sq) / 2; self.wc = (1 - self.sq) / 2
        # the fundamental unit: the smallest a + b w > 1 of norm +-1
        best = None
        for b in range(1, 40):
            for a in range(-40, 40):
                if abs(self.norm(a, b)) == 1 and a + b * self.w > 1:
                    v = a + b * self.w
                    if best is None or v < best[0]:
                        best = (v, a, b)
        self.eps, self.ea, self.eb = best
        self.eps_norm = self.norm(self.ea, self.eb)
        self.R = mp.pi / (2 * mp.log(self.eps))

    def norm(self, a, b):
        return a * a + a * b - self.m * b * b

    def psi(self, a, b):
        al, alc = a + b * self.w, a + b * self.wc
        return mp.sign(self.norm(a, b)) * mp.expj(self.R * mp.log(abs(al / alc)))

    def generator(self, q):
        """an element of norm +-q for a prime q that splits or ramifies"""
        for b in range(0, 400):
            for a in range(-400, 400):
                if abs(self.norm(a, b)) == q:
                    return a, b
        raise ValueError(q)

    def coefficients(self, nmax):
        """c(n) for n <= nmax, from the Euler product"""
        c = [mp.mpf(0)] * (nmax + 1); c[1] = mp.mpf(1)
        primes = [q for q in range(2, nmax + 1) if all(q % r for r in range(2, int(q ** 0.5) + 1))]
        local = {}
        for q in primes:
            ks = [k for k in range(0, 60) if q ** k <= nmax]
            if q == self.p:
                a, b = self.generator(q); s = self.psi(a, b)                  # one prime above p; psi is real there
                local[q] = [mp.re(s) ** k for k in ks]
            elif legendre(q, self.p) == -1:
                local[q] = [mp.mpf(1) if k % 2 == 0 else mp.mpf(0) for k in ks]
            else:
                a, b = self.generator(q); s = self.psi(a, b); th = mp.arg(s)
                local[q] = [mp.mpf(1)] + [mp.sin((k + 1) * th) / mp.sin(th) for k in ks[1:]]
        for n in range(2, nmax + 1):
            v, m = mp.mpf(1), n
            for q in primes:
                if q * q > m and m > 1 and m != n and False:
                    break
                k = 0
                while m % q == 0:
                    m //= q; k += 1
                if k:
                    v *= local[q][k]
                if m == 1:
                    break
            c[n] = v
        return c

    def direct(self, nmax, box=60):
        """c(n) by enumerating elements a + b w up to units: one generator for each ideal, found by its place in a unit's period"""
        seen = {}
        le = mp.log(self.eps)
        for a in range(-box, box + 1):
            for b in range(-box, box + 1):
                n = self.norm(a, b)
                if n == 0 or abs(n) > nmax:
                    continue
                al, alc = a + b * self.w, a + b * self.wc
                u = mp.log(abs(al / alc)) / (2 * le)                           # multiplying by the unit moves u by one
                key = (abs(n), int(mp.nint((u - mp.floor(u)) * 10 ** 12)) % 10 ** 12)      # the place within one period, to 12 digits; 1 is 0
                seen.setdefault(key, self.psi(a, b))
        cnt = [0] * (nmax + 1); c = [mp.mpc(0)] * (nmax + 1)
        for (n, _), v in seen.items():
            cnt[n] += 1; c[n] += v
        return cnt, c


class Form:
    def __init__(self, field, nmax, cosine=False):
        self.F = field; self.c = field.coefficients(nmax); self.nmax = nmax; self.cosine = cosine; self.nu = mp.mpc(0, field.R)

    def bessel(self, y):
        """K_{iR}(2 pi n y) for n = 1 .. as far as the terms matter at this precision"""
        out = [mp.mpf(0)]
        for n in range(1, self.nmax + 1):
            t = 2 * mp.pi * n * y
            if t > 85:
                break
            out.append(mp.re(mp.besselk(self.nu, t)))
        else:
            # the loop ran out of coefficients before the terms became negligible: the first run's fault, now refused
            raise ValueError("the series is cut at %d terms, before its terms are negligible at height %s" % (self.nmax, mp.nstr(y, 5)))
        return out

    def __call__(self, z):
        x, y = mp.re(z), mp.im(z)
        K = self.bessel(y)
        tr = mp.cos if self.cosine else mp.sin
        return mp.sqrt(y) * mp.fsum(self.c[n] * K[n] * tr(2 * mp.pi * n * x) for n in range(1, len(K)))


def mob(g, z):
    return (g[0] * z + g[1]) / (g[2] * z + g[3])


def level_five():
    P("LEVEL 5: THE GOLDEN STATE")
    F5 = Field(5)
    check("the fundamental unit is the golden one, of norm -1, and R = pi/(2 ln phi)", (F5.ea, F5.eb, F5.eps_norm) == (0, 1, -1) and abs(F5.R - mp.pi / (2 * mp.log((1 + mp.sqrt(5)) / 2))) < mp.mpf(10) ** -25, mp.nstr(F5.R, 15))
    check("H1 psi does not change when its argument is multiplied by the unit (12 cases)", all(abs(F5.psi(a, b) - F5.psi(b, a + b)) < mp.mpf(10) ** -25 for a, b in itertools.product(range(1, 4), range(1, 5))))
    c = F5.coefficients(720)
    cnt, cd = F5.direct(40)
    check("H1 for n <= 40 the ideals of norm n are as many as the sum of (d/5) over the divisors of n", all(cnt[n] == sum(legendre(d, 5) for d in range(1, n + 1) if n % d == 0) for n in range(1, 41)))
    err = max(abs(cd[n] - c[n]) for n in range(1, 41))
    check("H1 for n <= 40 the coefficient from the enumeration is the one from the Euler product", err < mp.mpf(10) ** -18, mp.nstr(err, 3))
    check("H1 c(5) = -1; c(2) = c(3) = c(7) = 0 and c(4) = c(9) = 1; c(11) = 2 sgn cos(...)", c[5] == -1 and c[2] == c[3] == c[7] == 0 and c[4] == c[9] == 1 and abs(c[11]) <= 2, mp.nstr(c[11], 12))
    f = Form(F5, 720); fc = Form(F5, 720, cosine=True)
    pts = [mp.mpc("0.137", "0.412"), mp.mpc("-0.291", "0.553"), mp.mpc("0.4021", "0.3377")]
    gens = {"[[2,-1],[5,-2]]": ((2, -1, 5, -2), -1), "[[3,-2],[5,-3]]": ((3, -2, 5, -3), -1), "[[1,0],[5,1]]": ((1, 0, 5, 1), 1)}
    worst, neg = mp.mpf(0), mp.mpf(0)
    for name, (g, chi) in gens.items():
        assert g[0] * g[3] - g[1] * g[2] == 1 and legendre(g[3], 5) == chi
        for z in pts:
            worst = max(worst, abs(f(mob(g, z)) - chi * f(z)) / abs(f(z)))
            if chi == -1:
                neg = max(neg, abs(fc(mob(g, z)) - chi * fc(z)) / abs(fc(z)))
    check("H2 f(g z) = (d/5) f(z) on the three generators, at three points", worst < mp.mpf(10) ** -18, mp.nstr(worst, 3))
    check("H2 negative control: the cosine series with the same coefficients fails on the two generators with factor -1", neg > mp.mpf(10) ** -3, mp.nstr(neg, 3))
    e1, e2 = (2 + mp.mpc(0, 1)) / 5, (-2 + mp.mpc(0, 1)) / 5
    w1, w2 = mp.mpc(0, 1) / mp.sqrt(5), mp.mpf(1) / 2 + mp.mpc(0, 1) / (2 * mp.sqrt(5))
    # the scale: the greatest value on a coarse set of points of the arc
    arc = lambda th: mp.expj(th) / mp.sqrt(5)
    th_e = mp.atan(mp.mpf(1) / 2)
    coarse = [(th, f(arc(th)) ** 2) for th in mp.linspace(th_e, mp.pi / 2, 41)]
    top = max(v for _, v in coarse)
    check("H3 f vanishes on the mirror's lines x = 0 and x = 1/2 (a sine series): the state is odd under the mirror", abs(f(mp.mpc(0, "0.7"))) == 0 and abs(f(mp.mpc("0.5", "0.61"))) < mp.mpf(10) ** -25 * mp.sqrt(top))
    check("H3 f(-conj z) = -f(z)", abs(f(-mp.conj(pts[0])) + f(pts[0])) < mp.mpf(10) ** -25)
    check("H3 f vanishes at both elliptic points (2+i)/5 and (-2+i)/5, where the stabiliser has d = +-2 and (2/5) = -1", abs(f(e1)) ** 2 / top < mp.mpf(10) ** -30 and abs(f(e2)) ** 2 / top < mp.mpf(10) ** -30, mp.nstr(abs(f(e1)) ** 2 / top, 3))
    s1, s2 = f(-1 / (5 * pts[0])) / f(pts[0]), f(-1 / (5 * pts[1])) / f(pts[1])
    check("H4 under the dual involution f(-1/(5z)) = s f(z) with one sign s at both points", abs(s1 - s2) < mp.mpf(10) ** -18 and abs(abs(s1) - 1) < mp.mpf(10) ** -18, "s = %s" % mp.nstr(s1, 6))
    check("so f vanishes at i/sqrt5 if s = -1; and it vanishes at 1/2 + i/(2 sqrt5), which lies on x = 1/2", abs(f(w1)) ** 2 / top < mp.mpf(10) ** -30 if s1 < 0 else True, "f^2/top at i/sqrt5: %s" % mp.nstr(abs(f(w1)) ** 2 / top, 3))
    # H5: the arc
    vals = [v for _, v in coarse]
    locmax = [i for i in range(1, len(vals) - 1) if vals[i] > vals[i - 1] and vals[i] > vals[i + 1]]
    check("H5 on 41 points of the arc from the elliptic point to i/sqrt5 the density has exactly one local maximum, strictly inside", len(locmax) == 1, locmax)
    i0 = locmax[0]
    th_star = mp.findroot(lambda th: mp.diff(lambda t: f(arc(t)) ** 2, th), coarse[i0][0])
    z_star = arc(th_star); peak = f(z_star) ** 2
    P("   the greatest place on the arc: angle %s degrees; z = %s" % (mp.nstr(mp.degrees(th_star), 12), mp.nstr(z_star, 18)))
    gx = mp.diff(lambda x: f(mp.mpc(x, mp.im(z_star))) ** 2, mp.re(z_star))
    gy = mp.diff(lambda y: f(mp.mpc(mp.re(z_star), y)) ** 2, mp.im(z_star))
    check("H5 it is a critical point in both directions (the gradient of f^2 is below 1e-15 of the peak)", abs(gx) / peak < mp.mpf(10) ** -15 and abs(gy) / peak < mp.mpf(10) ** -15, "%s, %s" % (mp.nstr(gx / peak, 3), mp.nstr(gy / peak, 3)))
    hxx = mp.diff(lambda x: f(mp.mpc(x, mp.im(z_star))) ** 2, mp.re(z_star), 2)
    hyy = mp.diff(lambda y: f(mp.mpc(mp.re(z_star), y)) ** 2, mp.im(z_star), 2)
    hxy = mp.diff(lambda x, y: f(mp.mpc(x, y)) ** 2, (mp.re(z_star), mp.im(z_star)), (1, 1))
    tr_, det_ = hxx + hyy, hxx * hyy - hxy ** 2
    check("H5 with a negative definite Hessian", tr_ < 0 and det_ > 0, "trace %s, determinant %s (in units of the peak)" % (mp.nstr(tr_ / peak, 5), mp.nstr(det_ / peak ** 2, 5)))
    check("H3 the greatest place is off the mirror's lines: a pair, z and -conj z", 0 < mp.re(z_star) < mp.mpf(1) / 2 and abs(f(-mp.conj(z_star)) ** 2 - peak) < mp.mpf(10) ** -25 * peak, mp.nstr(mp.re(z_star), 8))
    # A1 (added): the trace test.  At a critical point of f^2 with f not zero, grad f = 0, so the Euclidean Laplacian of f^2 is
    # 2 f Lap f = -2 (1/4 + R^2) f^2 / y^2.
    lam = mp.mpf(1) / 4 + F5.R ** 2
    want = -2 * lam / mp.im(z_star) ** 2
    check("A1 (added) the two second derivatives of the density sum to -2 (1/4 + R^2) / y^2 times the peak", abs(tr_ / peak - want) < mp.mpf(10) ** -10 * abs(want),
          "%s against %s" % (mp.nstr(tr_ / peak, 12), mp.nstr(want, 12)))
    disc = mp.sqrt((hxx - hyy) ** 2 + 4 * hxy ** 2)
    ev = sorted([(tr_ - disc) / (2 * peak), (tr_ + disc) / (2 * peak)])
    P("   the Hessian's two eigenvalues, in units of the peak: %s and %s" % (mp.nstr(ev[0], 6), mp.nstr(ev[1], 6)))
    # A2 (added): the second stretch, |z - 1/2|^2 = 1/20 from the elliptic point (angle pi - atan 2) to 1/2 + i/(2 sqrt 5) (angle pi/2)
    second = [mp.mpf(1) / 2 + mp.expj(mp.radians(a)) / (2 * mp.sqrt(5)) for a in (93, 99, 105, 111, 116)]
    worst2 = max(abs(f(z)) for z in second) / mp.sqrt(top)
    check("A2 (added) f vanishes on the second stretch of the arc, the circle |z - 1/2|^2 = 1/20 (five points)", worst2 < mp.mpf(10) ** -25, mp.nstr(worst2, 3))
    # A3 (added): the two reflections
    r1 = lambda z: 1 / (5 * mp.conj(z))
    r2 = lambda z: mp.mpf(1) / 2 + (mp.mpf(1) / 20) / (mp.conj(z) - mp.mpf(1) / 2)
    assert abs(abs(r1(arc(mp.mpf(1))))  ** 2 - mp.mpf(1) / 5) < mp.mpf(10) ** -25 and abs(r2(second[0]) - second[0]) < mp.mpf(10) ** -25
    e1r = max(abs(f(r1(z)) - f(z)) / abs(f(z)) for z in pts[:2])
    e2r = max(abs(f(r2(z)) + f(z)) / abs(f(z)) for z in pts[:2])
    check("A3 (added) f is even under the reflection in |z|^2 = 1/5 and odd under the reflection in |z - 1/2|^2 = 1/20", e1r < mp.mpf(10) ** -18 and e2r < mp.mpf(10) ** -18,
          "%s, %s" % (mp.nstr(e1r, 3), mp.nstr(e2r, 3)))
    # the grid: for each height the Bessel values once, then every x
    mp.mp.dps = 18
    fg = Form(F5, 720)
    xs = [mp.mpf(i) / 200 for i in range(1, 100)]
    ys = [mp.mpf("0.16") * mp.mpf("1.0125") ** j for j in range(0, 205)]              # 0.16 up to about 2.0
    best = (mp.mpf(0), None); count_above = 0
    cell = {"points": 0, "positive": 0, "negative": 0, "least": None}; eu = (mp.mpf(0), None)
    for y in ys:
        K = fg.bessel(y)
        for x in xs:
            val = mp.sqrt(y) * mp.fsum(fg.c[n] * K[n] * mp.sin(2 * mp.pi * n * x) for n in range(1, len(K)))
            v = val ** 2
            if v > best[0]:
                best = (v, mp.mpc(x, y))
            if v > peak:
                count_above += 1
            # A4: the cell outside both circles
            if x * x + y * y > mp.mpf(1) / 5 and (x - mp.mpf(1) / 2) ** 2 + y * y > mp.mpf(1) / 20:
                cell["points"] += 1; cell["positive" if val > 0 else "negative"] += 1
                if cell["least"] is None or abs(val) < cell["least"]:
                    cell["least"] = abs(val)
            # A5: the density against the chart's Euclidean area, within 0.15 of the peak
            if abs(mp.mpc(x, y) - z_star) < mp.mpf("0.15") and v / (y * y) > eu[0]:
                eu = (v / (y * y), mp.mpc(x, y))
    mp.mp.dps = 30
    check("A4 (added) on the grid's points inside the cell outside both circles f has one sign", cell["points"] > 5000 and (cell["positive"] == 0 or cell["negative"] == 0),
          "%d points: %d positive, %d negative; least |f| there %s of the peak's" % (cell["points"], cell["positive"], cell["negative"], mp.nstr(cell["least"] / mp.sqrt(peak), 3)))
    d_eu = abs(eu[1] - z_star)
    check("A5 (added) against the chart's Euclidean area the density f^2/y^2 is greatest elsewhere: between 0.04 and 0.07 from the peak, inside the window, off the circle",
          mp.mpf("0.04") < d_eu < mp.mpf("0.07") and abs(abs(eu[1]) ** 2 - mp.mpf(1) / 5) > mp.mpf("0.01"), "at z = %s, %s from the peak, |z|^2 = %s" % (mp.nstr(eu[1], 5), mp.nstr(d_eu, 3), mp.nstr(abs(eu[1]) ** 2, 5)))
    P("   the grid (99 values of x in (0, 1/2), 205 heights from 0.16 to %s): greatest value %s of the peak, at z = %s, |z|^2 = %s" % (
        mp.nstr(ys[-1], 4), mp.nstr(best[0] / peak, 8), mp.nstr(best[1], 6), mp.nstr(abs(best[1]) ** 2, 6)))
    check("H5 on the grid no value exceeds the peak found on the arc, and the grid's greatest value is within 2 per cent of it and beside it",
          count_above == 0 and best[0] / peak > mp.mpf("0.98") and abs(best[1] - z_star) < mp.mpf("0.02"), "above: %d" % count_above)
    # H6: the point the lane reports, read from the web seat's sealed header
    lane = mp.mpc("0.251539778829130", "0.369767144294671")
    check("H6 main's point agrees with the one the lane reports to 1e-9", abs(z_star - lane) < mp.mpf(10) ** -9, "distance %s" % mp.nstr(abs(z_star - lane), 3))
    glx = mp.diff(lambda x: f(mp.mpc(x, mp.im(lane))) ** 2, mp.re(lane))
    gly = mp.diff(lambda y: f(mp.mpc(mp.re(lane), y)) ** 2, mp.im(lane))
    gl = mp.sqrt(glx ** 2 + gly ** 2) / peak; gm = mp.sqrt(gx ** 2 + gy ** 2) / peak
    deficit = (peak - f(lane) ** 2) / peak
    off = abs(lane) ** 2 - mp.mpf(1) / 5
    P("   A6 (added) at the lane's reported point: the gradient of f^2 is %s of the peak (at main's point %s); the density is lower by %s of the peak;"
      " |z|^2 - 1/5 = %s" % (mp.nstr(gl, 3), mp.nstr(gm, 3), mp.nstr(deficit, 3), mp.nstr(off, 3)))
    check("A6 (added) the lane's reported point is within 2e-9 of the greatest place and is not it: the gradient there is above 1e-8 of the peak, and the point is off the circle by more than 1e-9",
          abs(z_star - lane) < mp.mpf(2) * mp.mpf(10) ** -9 and gl > mp.mpf(10) ** -8 and deficit > 0 and abs(off) > mp.mpf(10) ** -9, "distance %s" % mp.nstr(abs(z_star - lane), 3))
    # the coordinate t on the quotient of the line
    def eta(tau):
        q = mp.exp(2j * mp.pi * tau)
        return mp.exp(2j * mp.pi * tau / 24) * mp.qp(q)
    t_star = (eta(z_star) / eta(5 * z_star)) ** 6
    check("the point lies on |t|^2 = 125 and off the real axis of t (the mirror's fixed set there)", abs(abs(t_star) ** 2 - 125) < mp.mpf(10) ** -18 and abs(mp.im(t_star)) > 1, "t = %s" % mp.nstr(t_star, 12))
    RES["level_5"] = {"R": mp.nstr(F5.R, 20), "sign_under_the_dual_involution": mp.nstr(mp.re(s1), 3), "angle_degrees": mp.nstr(mp.degrees(th_star), 15),
                      "z_star": [mp.nstr(mp.re(z_star), 20), mp.nstr(mp.im(z_star), 20)], "t_star": [mp.nstr(mp.re(t_star), 15), mp.nstr(mp.im(t_star), 15)],
                      "hessian_trace_over_peak": mp.nstr(tr_ / peak, 8), "grid_greatest_over_peak": mp.nstr(best[0] / peak, 8),
                      "distance_from_the_lanes_reported_point": mp.nstr(abs(z_star - lane), 3),
                      "hessian_eigenvalues_over_peak": [mp.nstr(ev[0], 8), mp.nstr(ev[1], 8)], "trace_wanted": mp.nstr(want, 12),
                      "cell": {k: (int(v) if k != "least" else mp.nstr(v / mp.sqrt(peak), 3)) for k, v in cell.items()},
                      "euclidean_density_greatest_at": [mp.nstr(mp.re(eu[1]), 6), mp.nstr(mp.im(eu[1]), 6)], "its_distance_from_the_peak": mp.nstr(d_eu, 3),
                      "at_the_lanes_point": {"gradient_over_peak": mp.nstr(gl, 3), "deficit_over_peak": mp.nstr(deficit, 3), "off_the_circle": mp.nstr(off, 3)}}


def other_levels():
    P("")
    P("THE SAME RECIPE AT LEVELS 13 AND 17: WHERE THE STATE MUST VANISH")
    for p in (13, 17):
        Fp = Field(p)
        f = Form(Fp, 400)
        ok_unit = Fp.eps_norm == -1
        # automorphy on one generator with character -1 and one with +1, built from d
        d_minus = next(d for d in range(2, p) if legendre(d, p) == -1)
        d_plus = next(d for d in range(2, p - 1) if legendre(d, p) == 1)
        tests = []
        for d in (d_minus, d_plus, 1):
            # a move [[a, b], [p, d]] with a d - b p = 1
            a = pow(d, -1, p); b = (a * d - 1) // p
            g = (a, b, p, d)
            assert g[0] * g[3] - g[1] * g[2] == 1
            # mended after the first run: p z + d of modulus near 1, so that z and its image both lie near height 1/p
            for w in (mp.mpc("0.13", "1.07"), mp.mpc("-0.31", "0.83")):
                z = (w - d) / p
                assert mp.im(z) > mp.mpf("0.7") / p and mp.im(mob(g, z)) > mp.mpf("0.7") / p
                tests.append(abs(f(mob(g, z)) - legendre(d, p) * f(z)) / abs(f(z)))
        check("level %d: the unit has norm -1 and f(g z) = (d/%d) f(z) on three moves (d = %d with factor -1, d = %d and d = 1 with factor +1), at two points each" % (p, p, d_minus, d_plus),
              ok_unit and len(tests) == 6 and max(tests) < mp.mpf(10) ** -18, mp.nstr(max(tests), 3))
        scale = max(abs(f(mp.mpc(x, y))) for x in ("0.11", "0.23", "0.37") for y in ("0.15", "0.27", "0.4"))
        rows = []
        for order, poly in ((2, lambda d: (d * d + 1) % p), (3, lambda d: (d * d + d + 1) % p)):
            for d in [d for d in range(1, p) if poly(d) == 0]:
                # the elliptic point fixed by [[a, b], [p, d]] with the right trace: for order 2 trace 0 (a = -d), for order 3 trace -1 (a = -1 - d)
                a = -d if order == 2 else -1 - d
                b = (a * d - 1) // p
                assert a * d - b * p == 1
                z0 = (a - d + mp.sqrt(mp.mpc((a + d) ** 2 - 4))) / (2 * p)
                if mp.im(z0) < 0:
                    z0 = mp.conj(z0)
                rows.append((order, d, legendre(d, p), abs(f(z0)) / scale))
        for order, d, chi, v in rows:
            P("   level %d, a point of order %d with d = %d: (d/%d) = %+d; |f| there is %s of the scale" % (p, order, d, p, chi, mp.nstr(v, 3)))
        forced = [r for r in rows if (r[0] == 2 and r[2] == -1) or (r[0] == 3 and r[2] != 1)]
        free = [r for r in rows if r not in forced]
        check("level %d: f vanishes at every elliptic point where the character forces it" % p, all(r[3] < mp.mpf(10) ** -15 for r in forced), len(forced))
        check("level %d: and at the others it does not vanish (%s)" % (p, "the points of order 3" if p == 13 else "the points of order 2"), len(free) > 0 and all(r[3] > mp.mpf(10) ** -3 for r in free), len(free))
        RES["level_%d" % p] = {"R": mp.nstr(Fp.R, 15), "elliptic_points": [[o, d, c, mp.nstr(v, 3)] for o, d, c, v in rows]}
    check("H7 by hand: (2/5) = -1; (5/13) = -1 and (3/13) = +1; (4/17) = +1; and level 5 has no point of order 3",
          legendre(2, 5) == -1 and legendre(5, 13) == -1 and legendre(3, 13) == 1 and legendre(4, 17) == 1 and not [d for d in range(1, 5) if (d * d + d + 1) % 5 == 0])


if __name__ == "__main__":
    level_five()
    other_levels()
    n = sum(1 for v in RES.values() if isinstance(v, bool)); bad = [k for k, v in RES.items() if v is False]
    P(""); P("CHECKS: %d, FAILING: %d%s" % (n, len(bad), (" -- " + "; ".join(bad)) if bad else ""))
    P("H6 is main's expectation as written before the first run; it fails by a factor of 1.5 and is kept as failed.  A6 records what the run shows.")
    RES["failing"] = bad
    (HERE / "golden_state_on_main.json").write_text(json.dumps(RES, indent=1) + "\n", encoding="utf-8")
    (HERE / "golden_state_on_main_run.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
