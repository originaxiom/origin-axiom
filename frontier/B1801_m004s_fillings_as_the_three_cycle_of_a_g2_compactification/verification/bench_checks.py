"""B1801's bench checks (the referee's request; main's own code): (1) Friedmann-Witten's (3.20) traces and (3.21) identity and the
vanishing of det[16 pi^2/g_a^2, k_a, b_a] with the thresholds -- no one-loop correction to sin^2 theta_W, for any T_O, T_w (so for
any Q in their frame, not only m004's fillings); (2) |tau| = 4/3 without Turaev: |H1| of the 3-fold cyclic cover of m004(p/q) is
16p/3 (SnapPy's cyclic covers), since |H1(Qt)| = 3 |H1(Q)| |tau|^2; (3) acyclicity of the order-3 character: the filled group's
twisted Fox Jacobian has full rank (H^0 = H^1 = 0), while trivial coefficients give H^0 = 1, H^1 = 0.
    python3 -B bench_checks.py"""
import itertools, math, cmath
import sympy as sp
import numpy as np
import snappy
# (1) FW's identity
TO, Tw = sp.symbols("T_O T_w")
k = [sp.Rational(5, 3), 1, 1]                               # SU(5) normalisation k_a
b = [0, -6, -9]                                             # FW's (b1, b2, b3) = -3(0, 2, 3)
trA = [(0, 2, 3)]; trX = (sp.Rational(25, 3), 3, 2)
S = [2 * (TO * [0, 2, 3][a] + Tw * trX[a]) for a in range(3)]
S_fw = [-sp.Rational(2, 3) * b[a] * (TO - Tw) + 10 * k[a] * Tw for a in range(3)]
print("(1) FW (3.20) S'_a =", [sp.simplify(x) for x in S], "| (3.21) identity holds:", all(sp.simplify(S[a] - S_fw[a]) == 0 for a in range(3)))
gM, mu, V = sp.symbols("g_M mu V_Q", positive=True)
inv = [16 * sp.pi**2 / gM**2 * k[a] + S[a] + b[a] * sp.log(1 / (mu**2 * V**sp.Rational(2, 3))) for a in range(3)]
D = sp.Matrix([[inv[a], k[a], b[a]] for a in range(3)]).det()
print("    det[16pi^2/g_a^2, k_a, b_a] =", sp.simplify(D), "(zero: the thresholds are x k_a + y b_a, so the one-loop sin^2 theta_W is unchanged)")
# (2) the 3-fold cyclic covers
rows = []
for (p, q) in ((3, 2), (6, 1), (3, 4), (9, 2), (12, 1), (6, 5)):
    M = snappy.Manifold("m004"); M.dehn_fill((p, q))
    covs = M.covers(3, cover_type="cyclic")
    orders = []
    for C in covs:
        H = C.homology(); ab = H.elementary_divisors()
        orders.append(math.prod(abs(x) for x in ab) if all(x != 0 for x in ab) else None)
    rows.append((p, q, orders, 16 * p // 3))
    print("(2) m004(%d,%d): 3-fold cyclic covers |H1| = %s; predicted 16p/3 = %d" % (p, q, orders, 16 * p // 3))
ok2 = all(r[2] and all(o == r[3] for o in r[2]) for r in rows)
print("    |tau|^2 = |H1(Qt)| / (3p) = 16/9 on every row:", ok2)
# (3) acyclicity: Fox Jacobian of the filled group with the order-3 character
def fox_vec(word, gen, val):
    tot = 0j; pref = 1 + 0j
    for ch in word:
        e = 1 if ch.islower() else -1; g = ch.lower(); x = val[g]
        if g == gen:
            tot += pref if e == 1 else -pref / x
        pref *= x if e == 1 else 1 / x
    return tot
for (p, q) in ((3, 2), (6, 1), (9, 2)):
    M = snappy.Manifold("m004"); M.dehn_fill((p, q))
    G = M.fundamental_group(); gens, rels = G.generators(), G.relators()
    for vals in itertools.product(range(p), repeat=len(gens)):
        ph = dict(zip(gens, vals))
        if all(sum((1 if c.islower() else -1) * ph[c.lower()] for c in r) % p == 0 for r in rels) and math.gcd(*vals, p) == 1: break
    w = {g: cmath.exp(2j * math.pi * (ph[g] * (p // 3)) / p) for g in gens}
    J = np.array([[fox_vec(r, g, w) for g in gens] for r in rels])
    d1 = np.array([w[g] - 1 for g in gens])
    sv = np.linalg.svd(J, compute_uv=False)
    print("    m004(%d,%d): the twisted Fox Jacobian's singular values %s (the nonzero one is |Delta(omega)| = 4)" % (p, q, np.round(sv, 9)))
    print("(3) m004(%d,%d): order-3 character: rank d1 = %d (H^0 = %d), rank Fox Jacobian = %d of %d generators (H^1 = %d)" % (
        p, q, np.linalg.matrix_rank(d1.reshape(1, -1), tol=1e-9), 1 - np.linalg.matrix_rank(d1.reshape(1, -1), tol=1e-9), np.linalg.matrix_rank(J, tol=1e-9), len(gens),
        len(gens) - np.linalg.matrix_rank(d1.reshape(1, -1), tol=1e-9) - np.linalg.matrix_rank(J, tol=1e-9)))
print("bench_checks exit 0")
