"""B1857 (data-free): the explore seat's 'read-out by a state' (row 1617), its checkable claims re-derived with main's code.
(1) the cosh law: along a hyperbolic geodesic tau(t) of H (unit speed), the flat-torus energy of a primitive class
    c = (m, n), f_c(t) = |m + n tau|^2 / Im tau, is f_min cosh 2(t - t_c) -- so the separated Laplacian's wells are
    q_c cosh 2(t - t_c) with q_c ~ f_min; checked on LR's axis for several classes;
(2) by Hellmann-Feynman dE0/dq = <cosh 2(t - t_c)> > 0, so the lightest state sits at the class with the least f_min,
    i.e. the greatest height H_c = 1/f_min: the apex (analytic; stated, not computed);
(3) uniqueness = the apex attained once per period: the number of positions of the cyclic quotient sequence attaining
    the maximal height (x+ - x-)/2, for (6), (2,1,1,1,2), (2,1,2,1,2), (2,1^8,2);
(4) HS6 by length: (2,1,1,1,2) [degenerate] then (2,1,2,1,2) [unique] among the line-invisible, against (6);
(5) post hoc by volume: excess volume of (2,1^8,2) at k = 10, and its multiplicity."""
import math, warnings
warnings.filterwarnings("ignore")
import mpmath as mp
mp.mp.dps = 40
phi = (1 + mp.sqrt(5)) / 2
out = []
# (1) the cosh law on LR's axis: fixed points of tau -> (2 tau + 1)/(tau + 1) are x+- = (1 +- sqrt5)/2
xp, xm = (1 + mp.sqrt(5)) / 2, (1 - mp.sqrt(5)) / 2
c0, r = (xp + xm) / 2, (xp - xm) / 2
def tau(t):                                    # unit-speed geodesic on the semicircle: angle theta with tan(theta/2) = e^t
    th = 2 * mp.atan(mp.e ** t); return c0 + r * mp.cos(th) + 1j * r * mp.sin(th)
worst = 0
for m, n in ((1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (3, 2)):
    ts = [mp.mpf(x) / 10 for x in range(-40, 41)]
    f = [abs(m + n * tau(t)) ** 2 / tau(t).imag for t in ts]
    i0 = min(range(len(f)), key=lambda i: f[i])
    # fit f = A cosh 2(t - tc) through the exact minimum: tc from the vertex, A = min
    g = lambda t: abs(m + n * tau(t)) ** 2 / tau(t).imag
    tc = mp.findroot(lambda t: mp.diff(g, t), ts[i0]); A = g(tc)
    dev = max(abs(g(t) - A * mp.cosh(t - tc)) for t in ts)       # hyperbolic arclength t = 2 x Sol (Teichmuller) time
    worst = max(worst, dev)
out.append("(1) cosh law on LR's axis, 7 classes: max |f_c - f_min cosh(t - t_c)| over hyperbolic arclength t in [-4, 4] = %.1e, i.e. f_min cosh 2(s - s_c) in Sol time s = t/2" % float(worst))
# (3) apex multiplicity: heights at each position of the cyclic quotient sequence (runs + golden 1s)
def heights(runs, golden=200):
    seq = list(runs) + [1] * golden; n = len(seq); H = []
    for i in range(n):
        fw = seq[i:] + seq[:i]; bw = (seq[:i][::-1] + seq[i:][::-1])
        x = mp.mpf(0)
        for a in reversed(fw[1:120]): x = 1 / (a + x)
        xpl = fw[0] + x
        y = mp.mpf(0)
        for a in reversed(bw[:120]): y = 1 / (a + y)
        H.append((xpl + y) / 2)
    return H
def mult(runs):
    H = heights(runs); top = max(H)
    return float(top), sum(1 for h in H if abs(h - top) < mp.mpf(10) ** -15)
for runs in ((6,), (2, 1, 1, 1, 2), (2, 1, 2, 1, 2), (2,) + (1,) * 8 + (2,)):
    h, k = mult(runs)
    out.append("(3) %-28s apex height %.6f attained at %d position(s): %s" % (runs, h, k, "unique" if k == 1 else "degenerate (mirror)"))
# (4) and (5): lengths (B1853's) and volumes
def mul(A, B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]), (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def pw(A, n):
    X = ((1, 0), (0, 1))
    for _ in range(n): X = mul(X, A)
    return X
L, R, I = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1)); LR = mul(L, R)
def D(runs):
    M = I
    for i, x in enumerate(runs): M = mul(M, pw(L if i % 2 == 0 else R, x))
    return M
def excess(runs, k=20):
    m = len(runs); X = R if m % 2 else I
    W = mul(mul(D(runs), X), pw(LR, k)); G = mul(mul(D([1] * m), X), pw(LR, k))
    t = lambda A: abs(mp.mpf(A[0][0] + A[1][1]))
    return 2 * mp.acosh(t(W) / 2) - 2 * mp.acosh(t(G) / 2)
def E(runs): return mul(D(runs), ((D([1] * len(runs))[1][1], -D([1] * len(runs))[0][1]), (-D([1] * len(runs))[1][0], D([1] * len(runs))[0][0])))
def m5(A): return tuple(tuple(x % 5 for x in r) for r in A)
def line_inv(runs): A = E(runs); return m5(mul(A, LR)) == m5(mul(LR, A))
for runs in ((2, 1, 1, 1, 2), (2, 1, 2, 1, 2), (6,), (2,) + (1,) * 8 + (2,)):
    out.append("(4) %-28s line-invisible %s; excess length %.4f" % (runs, line_inv(runs), float(excess(runs))))
import snappy
V4 = float(snappy.Manifold("m004").volume()); K = 10
def word(r, k=K): return "".join(("L" if i % 2 == 0 else "R") * x for i, x in enumerate(r)) + ("R" if len(r) % 2 else "") + "LR" * k
for runs in ((2, 1, 1, 1, 2), (2,) + (1,) * 8 + (2,), (6,)):
    M = snappy.Manifold("b++" + word(runs))
    out.append("(5) %-28s excess volume %.4f (%s)" % (runs, float(M.volume()) - (K + (len(runs) + 1) // 2) * V4, M.solution_type()))
print("\n".join(out))
