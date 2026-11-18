"""B1957, P-873, question 2 (main's own computation, 2026-11-18; the physical lane's package C8 had shown one such direction, h*): every direction of frame D1's Higgs ground plane E = span(v+, v-) that has zero entries, and the cusp
exponents each gives at the 24 points of order 5, the four lifts and the three sectors.
Z1  the zero sets: a direction h = v+ - rho v- vanishes at mode k exactly when rho = v+_k / v-_k; modes with equal ratios
    vanish together. Listed with the direction's components (up to a common phase and scale).
Z2  for each such direction, by the dominant-term rule (the least sum of theta exponents 6 r^2 over the non-zero terms of
    the k x k minors, k = 1, 2, 3): the singular-value exponents and the two ratio exponents in all 288 cases; whether any
    case has three distinct exponents with E2 > 0 in the up sector.
Z3  the rule assumes the least terms do not cancel. For each direction main computes the exponents at the mark (2/5, 4/5)
    numerically (80 digits, heights 8, 11, 14, unshifted lift) and compares; and on every case where the rule's least
    term in a minor is a sum of more than one term, main sums their leading coefficients at Re tau = 0.13 and reports the
    least modulus found (zero would be a cancellation).
Z4  the up-sector cases of a full hierarchy (0 < E2 < E3), by point and lift, and a numerical check at two of them.
Z5  the one case at the mark that converges slowly (the direction with a zero at mode 0, down), carried to height 32."""
import itertools, functools
from fractions import Fraction as Fr
import numpy as np, mpmath as mp
print = functools.partial(print, flush=True)
k6 = np.arange(6); T6 = np.diag(np.exp(1j * np.pi * k6 ** 2 / 6)); S6 = np.exp(-1j * np.pi / 4) * np.exp(-2j * np.pi * np.outer(k6, k6) / 6) / np.sqrt(6)
inv = np.linalg.inv; U = T6 @ inv(S6) @ inv(T6) @ S6; ev, V = np.linalg.eig(U); ph = np.angle(ev) / np.pi
vp = V[:, int(np.argmin(abs(ph - 1 / 6)))]; vm = V[:, int(np.argmin(abs(ph + 1 / 6)))]; vp, vm = vp / np.linalg.norm(vp), vm / np.linalg.norm(vm)
rho = vp / vm
groups = []
for k in range(6):
    for g in groups:
        if abs(rho[g[0]] - rho[k]) < 1e-9: g.append(k); break
    else: groups.append([k])
dirs = []
for g in groups:
    h = vp - rho[g[0]] * vm; h = h / np.linalg.norm(h); i0 = int(np.argmax(np.abs(h))); h = h * np.exp(-1j * np.angle(h[i0]))
    dirs.append((tuple(g), h))
print("Z1: the zero sets of directions of E: %s" % [(g, [round(abs(x), 6) for x in h]) for g, h in dirs])
DELTA = {"up": 5, "down": -1, "lepton": -9}
def nearest(alpha):
    out = []
    for c in range(6):
        x = Fr(c, 6) + alpha; r = x - round(x); r = r if abs(r) <= Fr(1, 2) else r - (1 if r > 0 else -1); out.append(r)
    return out
def rule(h, a, sec):
    r = nearest(DELTA[sec] * a / 2); e = [6 * x * x for x in r]; terms = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                k = (i + j + 1 + 3 * m) % 6; c = (i - j + 3 * m) % 6
                if abs(h[k]) > 1e-12: terms.setdefault((i, j), []).append((e[c], k, c))
    best = []; multi = []
    for size in (1, 2, 3):
        cands = []
        for rows in itertools.combinations(range(3), size):
            for cols in itertools.combinations(range(3), size):
                for perm in itertools.permutations(cols):
                    sgn = np.linalg.det(np.eye(size)[[cols.index(p) for p in perm]])
                    lists = [terms.get((rw, cl), []) for rw, cl in zip(rows, perm)]
                    for choice in itertools.product(*lists): cands.append((sum(t[0] for t in choice), rows, cols, sgn, choice))
        m0 = min(t[0] for t in cands); best.append(m0)
        lead = [t for t in cands if t[0] == m0]
        by_minor = {}
        for t in lead: by_minor.setdefault((t[1], t[2]), []).append(t)
        multi += [(size, v) for v in by_minor.values() if len(v) > 1]
    s = [best[0], best[1] - best[0], best[2] - best[1]]; return s, (s[1] - s[0], s[2] - s[0]), multi, r
X = 0.13
def coeff(h, choice, sgn, r, b, sec):
    beta = DELTA[sec] * b / 2; z = sgn + 0j
    for (_, k, c) in choice: z *= h[k] * np.exp(2j * np.pi * k / 6) * np.exp(6j * np.pi * X * float(r[c]) ** 2 + 12j * np.pi * float(beta) * float(r[c]))
    return z
for g, h in dirs:
    tab = {}; hier = []; least_sum = None
    for i5, j5 in itertools.product(range(5), repeat=2):
        if (i5, j5) == (0, 0): continue
        for la, lb in itertools.product((0, 1), repeat=2):
            a, b = Fr(i5, 5) + la, Fr(j5, 5) + lb
            for sec in DELTA:
                s, rat, multi, r = rule(h, a, sec); tab[rat] = tab.get(rat, 0) + 1
                if sec == "up" and rat[0] > 0 and rat[1] > rat[0]: hier.append(((i5, j5), (la, lb), rat))
                for size, group in multi:
                    by_minor = {}
                    for t in group: by_minor.setdefault((t[1], t[2]), []).append(t)
                    for v in by_minor.values():
                        tot = abs(sum(coeff(h, t[4], t[3], r, b, sec) for t in v)); least_sum = tot if least_sum is None else min(least_sum, tot)
    print("Z2: direction zero at %s: ratio exponents over the 288 cases {(E2, E3): count}: %s; up-sector cases with 0 < E2 < E3: %d %s"
          % (g, {"(%s, %s)" % (str(k[0]), str(k[1])): v for k, v in sorted(tab.items())}, len(hier), hier[:3]))
    print("Z3: direction zero at %s: where a least term is a sum of several, the least modulus of the summed leading coefficients: %s" % (g, "none" if least_sum is None else "%.3e" % least_sum))
mp.mp.dps = 80
def Ymp(tau, xi):
    y = mp.im(tau); pre = (3 * y) ** mp.mpf("0.25"); res = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                kk = (i + j + 1 + 3 * m) % 6; aa = mp.mpf((i - j + 3 * m) % 6) / 6; n0 = mp.nint(aa + mp.im(xi) / y); s = mp.mpf(0)
                for n_ in range(-25, 26):
                    n = n_ + aa - n0; s += mp.exp(6j * mp.pi * xi * mp.im(xi) / y + 6j * mp.pi * n ** 2 * tau + 12j * mp.pi * n * xi)
                res[(i, j, kk)] = pre * mp.exp(2j * mp.pi * kk / 6) * s
    return res
def svals(tau, a, b, sec, h):
    fm = lambda q: mp.mpf(q.numerator) / q.denominator
    xi = mp.mpf(DELTA[sec]) * (fm(a) * tau + fm(b)) / 2; Y = Ymp(tau, xi)
    hz = [mp.mpc(0) if abs(h[kk]) < 1e-12 else mp.mpc(complex(h[kk])) for kk in range(6)]      # a zero entry is exactly zero: a residue of 1e-16 would dominate e^(-4 pi y/3)
    M = mp.matrix([[sum(Y.get((i, j, kk), 0) * hz[kk] for kk in range(6)) for j in range(3)] for i in range(3)])
    return sorted((abs(x) for x in mp.svd_c(M, compute_uv=False)), reverse=True)
for g, h in dirs:
    out = []
    for sec in ("up", "down"):
        L = {y: svals(mp.mpc("0.13", y), Fr(2, 5), Fr(4, 5), sec, h) for y in (8, 11, 14)}
        E = lambda y0, y1, i: float(-(mp.log(L[y1][i] / L[y1][0]) - mp.log(L[y0][i] / L[y0][0])) / (mp.pi * (y1 - y0)))
        s, rat, _, _ = rule(h, Fr(2, 5), sec)
        out.append("%s: numerical (%.4f, %.4f) from 11 -> 14, rule (%s, %s)" % (sec, E(11, 14, 1), E(11, 14, 2), rat[0], rat[1]))
    print("Z3: direction zero at %s, at the mark: %s" % (g, "; ".join(out)))
# Z4: the up-sector cases of a full hierarchy (0 < E2 < E3), by point and lift, and a numerical check at two of them
for g, h in dirs:
    cases = []
    for i5, j5 in itertools.product(range(5), repeat=2):
        if (i5, j5) == (0, 0): continue
        for la, lb in itertools.product((0, 1), repeat=2):
            s, rat, _, _ = rule(h, Fr(i5, 5) + la, "up")
            if rat[0] > 0 and rat[1] > rat[0]: cases.append(((i5, j5), (la, lb), "(%s, %s)" % rat))
    if not cases: continue
    pts = sorted({c[0] for c in cases}); lifts = sorted({c[1] for c in cases}); rats = sorted({c[2] for c in cases})
    print("Z4: direction zero at %s: up-sector full hierarchies at %d cases: points (5a, 5b) %s, lifts (a, b shifts) %s, ratio exponents %s" % (g, len(cases), pts, lifts, rats))
    for (i5, j5), (la, lb), rt in cases[:2]:
        a, b = Fr(i5, 5) + la, Fr(j5, 5) + lb
        L = {y: svals(mp.mpc("0.13", y), a, b, "up", h) for y in (8, 11, 14)}
        E = lambda y0, y1, i: float(-(mp.log(L[y1][i] / L[y1][0]) - mp.log(L[y0][i] / L[y0][0])) / (mp.pi * (y1 - y0)))
        print("Z4: at (5a, 5b) = (%d, %d), lift (%d, %d), up: numerical (%.4f, %.4f) from 8 -> 11 and (%.4f, %.4f) from 11 -> 14; rule %s" % (i5, j5, la, lb, E(8, 11, 1), E(8, 11, 2), E(11, 14, 1), E(11, 14, 2), rt))
# Z5: the one slow case at the mark (the direction with a zero at mode 0, down sector), carried higher
for g, h in dirs:
    if g != (0,): continue
    mp.mp.dps = 120
    L = {y: svals(mp.mpc("0.13", y), Fr(2, 5), Fr(4, 5), "down", h) for y in (14, 20, 26, 32)}
    E = lambda y0, y1, i: float(-(mp.log(L[y1][i] / L[y1][0]) - mp.log(L[y0][i] / L[y0][0])) / (mp.pi * (y1 - y0)))
    print("Z5: direction zero at %s, down at the mark, E3 from 14 -> 20, 20 -> 26, 26 -> 32: %.4f, %.4f, %.4f (rule 3/10); E2: %.4f, %.4f, %.4f (rule 0)" % (g, E(14, 20, 2), E(20, 26, 2), E(26, 32, 2), E(14, 20, 1), E(20, 26, 1), E(26, 32, 1)))
