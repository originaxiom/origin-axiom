#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
THE GOLDEN STATE ON THE WHOLE, AND WHERE ITS DENSITY PEAKS.   A sealed card; data-free; 40-digit arithmetic.

The web seat (chat1), 2026-11-11.  Kind: weave, conditional on stated choices.
At the owner's word to the seat.  The seat asked whether to compute, with its own code, where this state peaks,
"which reads a value of tau from the whole", and he answered: "yes please do it" (relayed, not confirmed to main).
Main's register has this card "at the owner's word only" (P-776, the seat's third fork).

WHAT IT CHECKS
  A branch of the agy lane, agy/stage4-sync-2026-11-11 at b4ddb600b (not on main), holds a sealed run for P-776.
  That lane numbers its arc B1881; main's B1881 is another arc.  Its weave part says: the lowest state of the
  hyperbolic Laplacian on the level-5 quotient that is odd under the exchange of the twins is Maass's form of the
  golden field, with spectral parameter pi/(2 ln phi); it vanishes at the two elliptic points and at the two points
  of discriminant -20; and its density has one greatest place, a mirror pair on the circle |z|^2 = 1/5.
  The seat read that part through the mask.  None of the lane's code was run and no output file of it was opened.
  This card builds the state from its classical definition and finds the peak with the seat's own code.

THE STATE (Maass 1949; the seat's own construction from the definition)
  K = Q(sqrt 5), integers Z[phi], phi the golden unit of norm -1, R = pi/(2 ln phi).  On the ideal (alpha):
      psi((alpha)) = sgn(N alpha) |alpha/alpha'|^(iR).
  It is well defined because sgn(N phi) phi^(2iR) = (-1)(e^(i pi)) = 1.  With c(n) the sum of psi over the ideals of
  norm n (real, multiplicative),
      f(z) = sqrt(y) sum_{n>=1} c(n) K_{iR}(2 pi n y) sin(2 pi n x),        z = x + iy.
  Frame: the standard one, the group c = 0 modulo 5, the mark (0, 1); the character is chi(d) = (d/5).

CHOICES THIS RESTS ON (none removed here)
  Level 5.  The mark.  The sector odd under the exchange of the twins.  This state within it: that it is the
  lowest is the lane's statement and Maass's construction, and is NOT verified by this card.  The clock: the
  hyperbolic Laplacian uses the area clock, which the record has as CHOSEN (B1815).  The read-out: the greatest
  place of the density f^2.

CELLS AND PREDICTIONS (each decided by a stated tolerance)
  G0  Controls.  (a) psi is unchanged when alpha is multiplied by a unit, on 12 cases.  (b) For n <= 60 the number of
      ideals of norm n found by enumeration equals sum_{d|n} chi(d).  (c) For n <= 60 the coefficient c(n) from the
      enumeration equals the one from the Euler product, to 1e-30.
  G1  Automorphy.  At four points, f(g z) = chi(d) f(z) for g = E1 = rows (2,-1),(5,-2); E2 = rows (3,-2),(5,-3);
      P0 = rows (1,0),(5,1): factors -1, -1, +1; relative error below 1e-25.  E1, E2 and the translation generate
      the group, and the series is periodic by its form.  Negative control: the cosine series with the same
      coefficients fails the test on E1 and E2 (error above 1e-3).
  G2  The dual involution: f(-1/(5z)) = -f(z) at two points, to 1e-25.  (The sign is the lane's; the seat has not
      derived it.)
  G3  Zeros, relative to the peak value: at the elliptic points (2 + i)/5 and (-2 + i)/5 (forced by G1); at
      i/sqrt 5 (forced by G2); at 1/2 + i/(2 sqrt 5) (the lane's statement; not derived by the seat): below 1e-25.
  G4  On the arc of |z|^2 = 1/5 from the elliptic point (2 + i)/5 to i/sqrt 5 the density has exactly one local
      maximum, strictly inside.
  G5  That point is a strict local maximum in two dimensions (both eigenvalues of the Hessian of f^2 negative).
      On a grid of the rectangle 0 < x < 1/2, 0.16 <= y <= 2 no value exceeds it, and the grid's greatest value
      is within 0.012 of it.  On the part of the grid in the region D (outside the circle |z|^2 = 1/5 and outside
      the circle |z - 1/2|^2 = 1/20) there is exactly one local maximum above one twentieth of the peak.
  G6  The peak agrees with the point the lane reports, 0.251539778829130 + 0.369767144294671 i, to 1e-13.
  REPORTED: the angle on the circle, the point to about 18 digits, its distance from the circle, and its coordinate
  t = (eta(z)/eta(5z))^6, in which the seat's relay 8ff3f7e53 writes the arc as |t|^2 = 125.

WHAT EACH OUTCOME MEANS (written before the run)
  If G0 or G1 fails, the seat has not built the form, the card is void, and it says nothing of the lane.
  If G1 to G5 hold, this state exists as described and its density has one greatest place up to the mirror, on
  the circle, away from the elliptic point and from i/sqrt 5.  By main's criterion (P-776, main's B1881 section 6)
  a place of that kind is a pair the mirror exchanges.
  If G6 holds as well, the lane's peak is reproduced.
  NOT SHOWN: that this is the lowest twin-odd state; that any of the choices above is forced; anything about the
  frame.  The point is compared with the lane's reported point and with nothing else: with no value of tau on
  record, and no frame is evaluated at it.  It is not a derived value of anything.

SEEN FIRST (swept from main at 16b82acda; each line is cut before its list of other lanes)
  VERDICT topic-sweep /Maass|dihedral|Grössenchara|Grossenchara|Hecke character|real multiplication|golden regulator|regulator/ (full text): 77 of 1627 arcs on main match (NEGATIVE 23, OPEN 13, PROVED 41); 9 register rows match (DONE 4, QUEUED 5)
  VERDICT topic-sweep /twin-odd|odd under the exchange of the twins|quadratic character|nebentypus|χ_5|chi_5|Legendre symbol/ (full text): 9 of 1627 arcs on main match (NEGATIVE 2, PROVED 7); 1 register rows match (QUEUED 1)
  VERDICT topic-sweep /Fricke circle|central circle|\|z\|\^2 = 1/5|\|t\|² = 125|anti-nodal|peak of the density|density peaks|where its density/ (full text): 0 of 1627 arcs on main match (none); 1 register rows match (QUEUED 1)
  On main: P-776 (QUEUED) names the candidate, "the lowest state that is odd under the exchange of the twins", and
  main's B1881 verifies the seat's relay on what symmetry allows and adds its criterion.  The Maass arcs the first
  sweep finds are of the figure-eight complement and of other groups; the seat found no state on either level-5
  curve on main.  Literature: Maass, Math. Ann. 121 (1949); one web search for a table of the lowest
  eigenvalues at level 5 with this character found none the seat could use.

DISCLOSED
  Not blind.  Before writing this the seat had read, through the mask, the lane's reported peak and its table of
  the first states, with their Hecke values at 2, 3, 4, 5, 11 and 19.  The seat had also told the owner, from
  memory and before reading the lane, that Maass's golden form lies in this sector and vanishes at the points
  over i.  Worked by hand before the seal: the well-definedness of psi, c at inert primes and at 5, the fixed
  points of E1 and E2.  Nothing of the card was run before the seal; the script was parsed for syntax.  To bound
  the run time the seat timed the library's Bessel function at another order, 2.5i, at four arguments.
"""
import sys

import mpmath as mp

mp.mp.dps = 40
SQ5 = mp.sqrt(5)
PHI = (1 + SQ5) / 2
PHIC = (1 - SQ5) / 2
LNPHI = mp.log(PHI)
R = mp.pi / (2 * LNPHI)
NCOEF = 720
LANE = mp.mpc('0.251539778829130', '0.369767144294671')


def chi(d):
    r = d % 5
    return 0 if r == 0 else (1 if r in (1, 4) else -1)


def norm(a, b):
    return a * a + a * b - b * b


def psi(a, b):
    al = a + b * PHI
    alc = a + b * PHIC
    return mp.sign(norm(a, b)) * mp.expj(R * mp.log(abs(al / alc)))


def primes_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(n + 1) if s[i]]


def generator(p):
    for b in range(0, 80):
        for a in range(-160, 161):
            if abs(norm(a, b)) == p:
                return a, b
    raise SystemExit('no generator found for %d' % p)


def euler_coefficients(nmax):
    c = [mp.mpf(0)] * (nmax + 1)
    c[1] = mp.mpf(1)
    ppow = {}
    for p in primes_upto(nmax):
        vals = [mp.mpf(1)]
        if p == 5:
            cp = mp.mpf(-1)
            k = 1
            while p ** k <= nmax:
                vals.append(mp.mpf((-1) ** k))
                k += 1
        elif p % 5 in (2, 3):
            k = 1
            while p ** k <= nmax:
                vals.append(mp.mpf(1 if k % 2 == 0 else 0))
                k += 1
        else:
            a, b = generator(p)
            cp = 2 * psi(a, b).real
            vals.append(cp)
            k = 2
            while p ** k <= nmax:
                vals.append(cp * vals[k - 1] - vals[k - 2])
                k += 1
        ppow[p] = vals
    for n in range(2, nmax + 1):
        m = n
        v = mp.mpf(1)
        for p in ppow:
            if p * p > m:
                break
            if m % p == 0:
                k = 0
                while m % p == 0:
                    m //= p
                    k += 1
                v *= ppow[p][k]
        if m > 1:
            v *= ppow[m][1]
        c[n] = v
    return c


def direct_coefficients(nmax, box=48):
    """ideals of norm <= nmax by enumeration of generators; returns (count, coefficient) per norm"""
    seen = {}
    scale = mp.mpf(10) ** 25
    for a in range(-box, box + 1):
        for b in range(-box, box + 1):
            n = norm(a, b)
            if n == 0 or abs(n) > nmax:
                continue
            al = a + b * PHI
            alc = a + b * PHIC
            u = mp.log(abs(al / alc)) / (2 * LNPHI)
            u = mp.nint(u * scale) / scale
            k = mp.floor(u)
            frac = u - k
            s0 = (1 if n > 0 else -1) * (1 if int(k) % 2 == 0 else -1)
            key = (abs(n), mp.nstr(frac, 22))
            val = s0 * mp.cos(mp.pi * frac)
            if key in seen:
                if abs(seen[key] - val) > mp.mpf(10) ** -20:
                    raise SystemExit('enumeration: two generators of one ideal disagree at norm %d' % abs(n))
            else:
                seen[key] = val
    count = [0] * (nmax + 1)
    coef = [mp.mpf(0)] * (nmax + 1)
    for (n, _), val in seen.items():
        count[n] += 1
        coef[n] += val
    return count, coef


C = None


def nterms(y):
    return int(mp.ceil((mp.mp.dps * mp.log(10) + 12) / (2 * mp.pi * y))) + 3


def series(z, trig):
    x, y = mp.re(z), mp.im(z)
    n_max = nterms(y)
    if n_max > NCOEF:
        raise SystemExit('too many terms needed at y = %s' % mp.nstr(y, 6))
    s = mp.mpf(0)
    for n in range(1, n_max + 1):
        if C[n] == 0:
            continue
        s += C[n] * mp.re(mp.besselk(1j * R, 2 * mp.pi * n * y)) * trig(2 * mp.pi * n * x)
    return mp.sqrt(y) * s


def f(z):
    return series(z, mp.sin)


def fcos(z):
    return series(z, mp.cos)


def moeb(g, z):
    return (g[0][0] * z + g[0][1]) / (g[1][0] * z + g[1][1])


def on_circle(theta):
    return (mp.cos(theta) + 1j * mp.sin(theta)) / SQ5


def eta(z):
    q = mp.exp(2j * mp.pi * z)
    prod = mp.mpf(1)
    n = 1
    while True:
        term = q ** n
        if abs(term) < mp.mpf(10) ** -(mp.mp.dps + 5):
            break
        prod *= (1 - term)
        n += 1
    return mp.exp(2j * mp.pi * z / 24) * prod


RESULTS = []


def verdict(name, ok, note=''):
    RESULTS.append((name, bool(ok)))
    print('%s: %s%s' % (name, 'HOLDS' if ok else 'FAILS', (' -- ' + note) if note else ''))


def main():
    global C
    print('THE GOLDEN STATE ON THE WHOLE, AND WHERE ITS DENSITY PEAKS')
    print('R = pi/(2 ln phi) = %s;  1/4 + R^2 = %s' % (mp.nstr(R, 25), mp.nstr(mp.mpf(1) / 4 + R * R, 25)))
    print()

    # ------------------------------------------------------------------ G0
    print('G0  controls')
    worst = mp.mpf(0)
    cases = 0
    for a, b in ((3, 1), (1, 3), (4, -1), (7, 2)):
        for unit in ((0, 1), (1, 1), (-1, 1)):          # phi, phi^2, phi^-1 = phi - 1
            ua, ub = unit
            # (a + b phi)(ua + ub phi) = a ua + b ub + (a ub + b ua + b ub) phi
            a2 = a * ua + b * ub
            b2 = a * ub + b * ua + b * ub
            worst = max(worst, abs(psi(a2, b2) - psi(a, b)))
            cases += 1
    print('    (a) psi unchanged by units: %d cases, worst difference %s' % (cases, mp.nstr(worst, 5)))
    C = euler_coefficients(NCOEF)
    count, cdir = direct_coefficients(60)
    bad_count = [n for n in range(1, 61) if count[n] != sum(chi(d) for d in range(1, n + 1) if n % d == 0)]
    worst_c = max(abs(cdir[n] - C[n]) for n in range(1, 61))
    print('    (b) ideal counts for n <= 60 against sum of chi over divisors: mismatches %s' % bad_count)
    print('    (c) coefficients for n <= 60, enumeration against Euler product: worst difference %s' % mp.nstr(worst_c, 5))
    print('    c(2), c(3), c(4), c(5), c(9), c(11), c(19) = %s' % ', '.join(mp.nstr(C[n], 15) for n in (2, 3, 4, 5, 9, 11, 19)))
    ok0 = worst < mp.mpf(10) ** -30 and cases == 12 and not bad_count and worst_c < mp.mpf(10) ** -30
    verdict('G0', ok0)
    print()
    if not ok0:
        print('The card is void: the controls fail.')
        return 0

    # ------------------------------------------------------------------ G1
    print('G1  automorphy at four points')
    pts = [mp.mpc('0.11', '0.71'), mp.mpc('0.27', '0.52'), mp.mpc('-0.18', '0.83'), mp.mpc('0.39', '0.44')]
    els = [('E1', ((2, -1), (5, -2))), ('E2', ((3, -2), (5, -3))), ('P0', ((1, 0), (5, 1)))]
    worst1 = mp.mpf(0)
    worst_cos = mp.mpf(0)
    for z in pts:
        fz = f(z)
        fc = fcos(z)
        for name, g in els:
            assert g[0][0] * g[1][1] - g[0][1] * g[1][0] == 1 and g[1][0] % 5 == 0
            w = moeb(g, z)
            fac = chi(g[1][1])
            err = abs(f(w) - fac * fz) / abs(fz)
            worst1 = max(worst1, err)
            if name in ('E1', 'E2'):
                worst_cos = max(worst_cos, abs(fcos(w) - fac * fc) / abs(fc))
    print('    worst relative error of f(g z) - chi(d) f(z): %s' % mp.nstr(worst1, 5))
    print('    the cosine series, same test on E1 and E2: worst relative error %s' % mp.nstr(worst_cos, 5))
    ok1 = worst1 < mp.mpf(10) ** -25 and worst_cos > mp.mpf(10) ** -3
    verdict('G1', ok1)
    print()
    if worst1 >= mp.mpf(10) ** -25:
        print('The card is void: the series is not the form.')
        return 0

    # ------------------------------------------------------------------ G2
    print('G2  the dual involution z -> -1/(5z)')
    worst2 = mp.mpf(0)
    ratios = []
    for z in pts[:2]:
        r = f(-1 / (5 * z)) / f(z)
        ratios.append(r)
        worst2 = max(worst2, abs(r + 1))
    print('    f(-1/(5z)) / f(z) = %s' % ', '.join(mp.nstr(r, 30) for r in ratios))
    verdict('G2', worst2 < mp.mpf(10) ** -25)
    print()

    # ------------------------------------------------------------------ G4 (the arc)
    print('G4  the arc of |z|^2 = 1/5 from the elliptic point to i/sqrt 5')
    th_e = mp.atan(mp.mpf(1) / 2)
    th_f = mp.pi / 2
    nscan = 120
    with mp.workdps(20):
        ths = [th_e + (th_f - th_e) * mp.mpf(j) / nscan for j in range(nscan + 1)]
        vals = [f(on_circle(t)) ** 2 for t in ths]
    loc = [j for j in range(1, nscan) if vals[j] > vals[j - 1] and vals[j] > vals[j + 1]]
    print('    %d samples; local maxima at sample(s) %s' % (nscan + 1, loc))
    if len(loc) != 1:
        verdict('G4', False, 'not exactly one local maximum on the arc')
        return 0
    j = loc[0]
    lo, hi = ths[j - 1], ths[j + 1]
    gr = (mp.sqrt(5) - 1) / 2
    x1 = hi - gr * (hi - lo)
    x2 = lo + gr * (hi - lo)
    g1 = f(on_circle(x1)) ** 2
    g2 = f(on_circle(x2)) ** 2
    for _ in range(140):
        if g1 < g2:
            lo = x1
            x1, g1 = x2, g2
            x2 = lo + gr * (hi - lo)
            g2 = f(on_circle(x2)) ** 2
        else:
            hi = x2
            x2, g2 = x1, g1
            x1 = hi - gr * (hi - lo)
            g1 = f(on_circle(x1)) ** 2
        if hi - lo < mp.mpf(10) ** -10:
            break
    th_star = (lo + hi) / 2
    hh = mp.mpf(10) ** -10
    for _ in range(4):                       # Newton on the derivative along the circle
        ga = f(on_circle(th_star + hh)) ** 2
        gb = f(on_circle(th_star - hh)) ** 2
        g0 = f(on_circle(th_star)) ** 2
        d1 = (ga - gb) / (2 * hh)
        d2 = (ga - 2 * g0 + gb) / hh ** 2
        th_star = th_star - d1 / d2
    z_star = on_circle(th_star)
    peak = f(z_star) ** 2
    print('    the maximum: theta = %s (in units of pi: %s); last Newton step %s' % (mp.nstr(th_star, 20), mp.nstr(th_star / mp.pi, 20), mp.nstr(abs(d1 / d2), 3)))
    print('    z* = %s + %s i;   |z*|^2 - 1/5 = %s;   f(z*)^2 = %s (not normalised)'
          % (mp.nstr(mp.re(z_star), 19), mp.nstr(mp.im(z_star), 19), mp.nstr(abs(z_star) ** 2 - mp.mpf(1) / 5, 3), mp.nstr(peak, 15)))
    inside = (th_star - th_e) > mp.mpf('0.01') and (th_f - th_star) > mp.mpf('0.01')
    verdict('G4', inside)
    print()

    # ------------------------------------------------------------------ G3
    print('G3  zeros, relative to the peak value')
    root = mp.sqrt(peak)
    zs = [('(2 + i)/5', mp.mpc(2, 1) / 5), ('(-2 + i)/5', mp.mpc(-2, 1) / 5), ('i/sqrt 5', 1j / SQ5), ('1/2 + i/(2 sqrt 5)', mp.mpf(1) / 2 + 1j / (2 * SQ5))]
    worst3 = mp.mpf(0)
    for name, z in zs:
        v = abs(f(z)) / root
        worst3 = max(worst3, v)
        print('    |f| at %-20s / |f(z*)| = %s' % (name, mp.nstr(v, 5)))
    verdict('G3', worst3 < mp.mpf(10) ** -25)
    print()

    # ------------------------------------------------------------------ G5
    print('G5  two dimensions')
    h = mp.mpf(10) ** -9

    def dens(dx, dy):
        return f(z_star + dx + 1j * dy) ** 2
    d0 = dens(0, 0)
    fxx = (dens(h, 0) - 2 * d0 + dens(-h, 0)) / h ** 2
    fyy = (dens(0, h) - 2 * d0 + dens(0, -h)) / h ** 2
    fxy = (dens(h, h) - dens(h, -h) - dens(-h, h) + dens(-h, -h)) / (4 * h ** 2)
    gx = (dens(h, 0) - dens(-h, 0)) / (2 * h)
    gy = (dens(0, h) - dens(0, -h)) / (2 * h)
    trh = fxx + fyy
    dth = fxx * fyy - fxy ** 2
    e1 = (trh + mp.sqrt(trh ** 2 - 4 * dth)) / 2
    e2 = (trh - mp.sqrt(trh ** 2 - 4 * dth)) / 2
    print('    gradient of f^2 at z*, relative to the peak: (%s, %s)' % (mp.nstr(gx / peak, 3), mp.nstr(gy / peak, 3)))
    print('    Hessian eigenvalues of f^2 at z*, relative to the peak: %s, %s' % (mp.nstr(e1 / peak, 8), mp.nstr(e2 / peak, 8)))
    with mp.workdps(20):
        ys = [mp.mpf('0.16') + mp.mpf('0.01') * i for i in range(45)] + [mp.mpf('0.65') + mp.mpf('0.05') * i for i in range(28)]
        xs = [mp.mpf('0.01') * i for i in range(1, 50)]
        grid = {}
        for iy, y in enumerate(ys):
            n_max = nterms(y)
            ks = [(n, C[n] * mp.re(mp.besselk(1j * R, 2 * mp.pi * n * y))) for n in range(1, n_max + 1) if C[n] != 0]
            for ix, x in enumerate(xs):
                s = mp.mpf(0)
                for n, kv in ks:
                    s += kv * mp.sin(2 * mp.pi * n * x)
                grid[(ix, iy)] = y * s * s
        gmax_key = max(grid, key=lambda kk: grid[kk])
        gmax = grid[gmax_key]
        gz = mp.mpc(xs[gmax_key[0]], ys[gmax_key[1]])

        def in_d(ix, iy):
            x, y = xs[ix], ys[iy]
            return x * x + y * y >= mp.mpf(1) / 5 and (x - mp.mpf(1) / 2) ** 2 + y * y >= mp.mpf(1) / 20
        locs = []
        for (ix, iy), v in grid.items():
            if not in_d(ix, iy) or v < peak / 20:
                continue
            nb = [grid.get((ix + a, iy + b)) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
            if all(w is None or w < v for w in nb):
                locs.append((mp.nstr(xs[ix], 4), mp.nstr(ys[iy], 4), mp.nstr(v / peak, 6)))
    print('    grid of %d points: greatest value / peak = %s at %s + %s i; distance from z*: %s'
          % (len(grid), mp.nstr(gmax / peak, 10), mp.nstr(mp.re(gz), 4), mp.nstr(mp.im(gz), 4), mp.nstr(abs(gz - z_star), 4)))
    print('    local maxima on the grid inside D above one twentieth of the peak (x, y, value/peak): %s' % locs)
    ok5 = e1 < 0 and e2 < 0 and gmax <= peak and abs(gz - z_star) < mp.mpf('0.012') and len(locs) == 1
    verdict('G5', ok5)
    print()

    # ------------------------------------------------------------------ G6 and the reported coordinate
    print('G6  against the point the lane reports')
    dist = abs(z_star - LANE)
    print('    |z* - the lane\'s point| = %s' % mp.nstr(dist, 5))
    verdict('G6', dist < mp.mpf(10) ** -13)
    print()
    t = (eta(z_star) / eta(5 * z_star)) ** 6
    print('REPORTED  z* = %s + %s i' % (mp.nstr(mp.re(z_star), 19), mp.nstr(mp.im(z_star), 19)))
    print('          the mirror image is -conj(z*); the two are one orbit of the mirror')
    print('          t(z*) = %s;  |t|^2 = %s;  arg t / pi = %s' % (mp.nstr(t, 20), mp.nstr(abs(t) ** 2, 25), mp.nstr(mp.arg(t) / mp.pi, 20)))
    print()
    held = sum(1 for _, ok in RESULTS if ok)
    print('PREDICTIONS: %d of %d hold  (%s)' % (held, len(RESULTS), ', '.join('%s %s' % (n, 'holds' if ok else 'FAILS') for n, ok in RESULTS)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
