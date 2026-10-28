"""P-408 (Witten's discrete doublet-triplet splitting on m004's fillings; data-free).  Computed: (1) the hyperbolic fillings
m004(p/q) with p even, their volumes, H1 and symmetry groups (SnapPy); (2) the unique order-2 character and its Reidemeister
torsion |tau| = |Delta(-1)| / (|-1-1| |(-1)^r - 1|) = 5/4 (the figure-eight's Delta(t) = t - 3 + 1/t), checked without Turaev:
the 2-fold cyclic cover has |H1| = 2 |H1(Q)| |tau| = 5p/2; (3) Smith's bound: sum of dim H_*(Q; Z/2) is 4 for p even (so an
involution's fixed set may be two circles) and 2 for p odd (at most one circle); (4) the orbifold lift: in
Z/2 = <W> the assignment mu1 -> 0, mu2 -> 1 is a homomorphism of H1(S^3 - L) = Z^2 killing mu_i^2, nonzero on mu1 mu2 in pi1(Q)
(stated; the algebra is one line).  W = diag(1,1,1,-1,-1): det 1, commutant S(U(3) x U(2)), doublet -1, triplet +1."""
import math, cmath
import numpy as np
import snappy
Delta = lambda z: z - 3 + 1 / z
print("Delta(-1) =", Delta(-1.0), "| W = diag(1,1,1,-1,-1): det", np.prod([1, 1, 1, -1, -1]))
rows = []
for p in range(2, 21, 2):
    for q in range(1, 15):
        if math.gcd(p, q) != 1: continue
        M = snappy.Manifold("m004"); M.dehn_fill((p, q))
        if M.solution_type() != "all tetrahedra positively oriented": continue
        r = (-pow(q, -1, p)) % p if p > 1 else 0
        z = -1.0
        tau = abs(Delta(z)) / (abs(z - 1) * abs(z**r - 1))
        covs = M.covers(2, cover_type="cyclic")
        cov_orders = []
        for C in covs:
            ab = C.homology().elementary_divisors(); cov_orders.append(math.prod(abs(x) for x in ab) if all(x != 0 for x in ab) else None)
        H = M.homology(); ed = H.elementary_divisors()
        z2rank = sum(1 for x in ed if x % 2 == 0)
        try: sym = str(M.symmetry_group())
        except Exception as e: sym = "?"
        rows.append((float(M.volume()), p, q, str(H), tau, cov_orders, 5 * p // 2, z2rank, sym))
rows.sort()
for V, p, q, H, tau, cov, pred, z2, sym in rows[:12]:
    print("  m004(%2d,%2d): vol %.6f H1 %-6s | order-2 |tau| %.4f | 2-fold cover |H1| %s (5p/2 = %d) | H1(Q;Z/2) rank %d -> sum dim H_*(Q;Z/2) = %d | Sym %s" % (
        p, q, V, H, tau, cov, pred, z2, 2 + 2 * z2, sym))
ok = all(abs(r[4] - 1.25) < 1e-12 and r[5] and all(o == r[6] for o in r[5]) for r in rows)
print("order-2 torsion 5/4 and the cover orders 5p/2 on all %d listed fillings: %s" % (len(rows), ok))
for p, q in ((3, 2), (5, 1)):
    M = snappy.Manifold("m004"); M.dehn_fill((p, q)); ed = M.homology().elementary_divisors()
    print("  control p odd m004(%d,%d): H1 %s, Z/2 rank %d -> sum dim H_*(Q;Z/2) = %d (at most one fixed circle)" % (p, q, M.homology(), sum(1 for x in ed if x % 2 == 0), 2 + 2 * sum(1 for x in ed if x % 2 == 0)))
print("checks exit 0")
