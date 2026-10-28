"""Referee B1803, b4: Witten's first model (hep-ph/0201018 eqs. 2.1-2.9, read at source) re-implemented without r8's code,
then placed on the F'-fixed points of m004(p/q), p even.
Characters of F' = Z/2 x Z/2 written as bit pairs (value on h1, value on P); h2 = h1 P.
Field at a fixed point x of character c_x (normalised at E+) with free F-charge f: a 5 or 5bar has triplet f, doublet f + c_x;
a 10 has Q f + c_x, (u^c, e^c) f.  First model: V (5) unsplit with charge alpha, all three 10's uniform with a common sigma,
all three 5bar's uniform with a common tau; V~ (5bar) at a point with c = w relative to V, triplet gamma, doublet delta.
(a) the abstract solutions; (b) placements on the four points, with and without distinct points; (c) the minimum number of
multiplets per point; (d) the 'V may be split' variant; (e) Z/2 alone (Witten's caveat)."""
import itertools
Z = (0, 0)
A = [(0, 0), (1, 0), (0, 1), (1, 1)]
add = lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)
def first_model(alpha, sigma, tau, gamma, delta):
    c = {}
    c["split: QQ~ allowed"] = add(alpha, gamma) == Z
    c["split: HH~ forbidden"] = add(alpha, delta) != Z
    c["(2.3) H 10 10"] = add(alpha, add(sigma, sigma)) == Z
    c["(2.4) H~ 10 5bar"] = add(delta, add(sigma, tau)) == Z
    c["(2.5) H H 5bar 5bar"] = add(add(alpha, tau), add(alpha, tau)) == Z
    c["(2.6) no H 5bar mass"] = add(alpha, tau) != Z
    c["(2.8) no 10 5bar 5bar"] = add(sigma, add(tau, tau)) != Z
    c["(2.9) no 10^3 5bar"] = add(add(sigma, add(sigma, sigma)), tau) != Z
    return c
sols = []
for alpha, sigma, tau, gamma, w in itertools.product(A, A, A, A, A[1:]):
    delta = add(gamma, w)
    if all(first_model(alpha, sigma, tau, gamma, delta).values()):
        sols.append((alpha, sigma, tau, w))
print("(a) full first-model solutions over Z/2 x Z/2: %d" % len(sols))
for w in A[1:]:
    print("    w = %s: %s" % (w, [(s[1], s[2]) for s in sols if s[3] == w]))
print("    alpha = 0 in all: %s" % all(s[0] == Z for s in sols))

tables = {"p = 2 mod 4": {"E+": (0, 0), "E-": (1, 0), "C1": (0, 1), "C2": (1, 1)},
          "p = 0 mod 4": {"E+": (0, 0), "E-": (1, 0), "C1": (0, 0), "C2": (1, 0)}}
# (h1, h2, P) table of b3 converted to (h1, P): E- = (1,1,0) -> (1,0); C1 = (0,1,1) -> (0,1); C2 = (1,0,1) -> (1,1)
print("(b)-(c) placements: V, 3 x 10, 3 x 5bar at points of one class, V~ at a point of class + w (w from a solution)")
for res, ch in tables.items():
    pts = list(ch)
    ws = set(s[3] for s in sols)
    best = None
    count_distinct = 0; count_any = 0
    for xV, xVt in itertools.product(pts, pts):
        w = add(ch[xV], ch[xVt])
        if w not in ws:
            continue
        same = [x for x in pts if ch[x] == ch[xV]]
        for mat in itertools.product(same, repeat=6):
            occ = {}
            for x in [xV, xVt] + list(mat):
                occ[x] = occ.get(x, 0) + 1
            k = max(occ.values())
            count_any += 1
            if k == 1:
                count_distinct += 1
            if best is None or k < best[0]:
                best = (k, xV, xVt, mat)
    print("  %s: points per class %s; placements with distinct points: %d; with coincidences allowed: %d; "
          "min multiplets at one point = %d (e.g. V at %s, V~ at %s, matter at %s)" % (
              res, sorted([sum(1 for x in pts if ch[x] == c) for c in set(ch.values())]), count_distinct, count_any,
              best[0], best[1], best[2], best[3]))
    print("     total fields 8 vs F'-fixed points %d: distinct placement impossible before any character is used" % len(pts))

print("(d) variant: V may sit at a point of another class (V split by c_V); matter uniform at one class")
nsol = 0
for aD, cV, sigma, tau, w in itertools.product(A, A, A, A, A):
    aT = add(aD, cV); gamma = aT          # QQ~ allowed: aT + gamma = 0 (gamma = -aT = aT)
    delta = add(gamma, w)
    ok = (add(aD, delta) != Z and add(aD, add(sigma, sigma)) == Z and add(delta, add(sigma, tau)) == Z
          and add(aD, tau) != Z and add(sigma, add(tau, tau)) != Z and add(add(sigma, add(sigma, sigma)), tau) != Z)
    nsol += ok
print("  solutions with c_V free: %d; matter still needs six multiplets at one class (at most 2 points per class)" % nsol)

print("(e) F' = Z/2 alone (any of h1, h2; P only when p = 2 mod 4; P on the Z/6 line: twist W^3, still order 2)")
B = [0, 1]
full = nofull = 0
for alpha, sigma, tau, gamma in itertools.product(B, B, B, B):
    delta = (gamma + 1) % 2
    base = [(alpha + gamma) % 2 == 0, (alpha + delta) % 2 != 0, (alpha + 2 * sigma) % 2 == 0, (delta + sigma + tau) % 2 == 0,
            (2 * (alpha + tau)) % 2 == 0, (alpha + tau) % 2 != 0, (3 * sigma + tau) % 2 != 0]
    if all(base):
        nofull += 1
        if (sigma + 2 * tau) % 2 != 0:
            full += 1
        print("  solution without (2.8): alpha %d sigma %d tau %d gamma %d delta %d" % (alpha, sigma, tau, gamma, delta))
print("  Z/2: full %d, without (2.8) %d" % (full, nofull))
print("b4 exit 0")
