"""Referee B1802, r7.  (a) For the period involution P on m004(6,1) and m004(12,1)/(18,1) (3 | p): P-equivariant flat
Z/N-bundles (N = 6, 3) restricting on pi1(Q) = ker psi to an order-N line; their local actions at the two fixed circles.
(b) For an involution with fixed circles S1, S2 and an equivariant flat bundle rho, the relative action
rho(m1)^-1 rho(m2) = rho(m1^-1 m2) is a holonomy of Q (m1^-1 m2 lies in ker psi): computed values listed.
Abelian targets only (Z/N); the restriction to ker psi is read off on Reidemeister-Schreier generators of ker psi in H1^orb."""
import snappy, itertools, math
def abel_vec(word, gens):
    v = [0] * len(gens)
    for ch in word: v[gens.index(ch.lower())] += 1 if ch.islower() else -1
    return v
def homs(gens, R, N):
    return [vals for vals in itertools.product(range(N), repeat=len(gens)) if all(sum(a * b for a, b in zip(r, vals)) % N == 0 for r in R)]
def ev(vals, vec, N): return sum(a * b for a, b in zip(vals, vec)) % N
for (p, q) in [(6, 1), (6, 5), (12, 1), (18, 1)]:
    O = snappy.Manifold("L6a2"); O.dehn_fill([(2, 0), (p, 2 * q)])
    G = O.fundamental_group(); gens = G.generators(); R = [abel_vec(r, gens) for r in G.relators()]
    per = G.peripheral_curves()
    mA = abel_vec(per[0][0], gens); muK, laK = abel_vec(per[1][0], gens), abel_vec(per[1][1], gens)
    mC = [a * (p // 2) + b * q for a, b in zip(muK, laK)]
    psi = [h for h in homs(gens, R, 2) if ev(h, mA, 2) == 1 and ev(h, mC, 2) == 1 and ev(h, muK, 2) == 0]
    assert len(psi) == 1; psi = psi[0]
    # generators of ker psi (as vectors in the free abelian group on gens): x if psi(x)=0, x*g0 and x^2 otherwise, with g0 = mA
    kgens = []
    for i in range(len(gens)):
        e = [0] * len(gens); e[i] = 1
        if psi[i] == 0: kgens.append(e)
        else:
            kgens.append([a + b for a, b in zip(e, mA)]); kgens.append([2 * a for a in e])
    kgens.append([a - b for a, b in zip(mA, mC)])
    for N in (2, 3, 6):
        rows = []
        for h in homs(gens, R, N):
            # order of the restriction to ker psi
            vals = [ev(h, k, N) for k in kgens]
            g = N
            for v in vals: g = math.gcd(g, v)
            order = N // g
            if order == N:
                rows.append((ev(h, mA, N), ev(h, mC, N), ev(h, [a - b for a, b in zip(mC, mA)], N)))
        print("m004(%d,%d), P, Z/%d lines (restriction of order %d): (rho(m_A), rho(m_C), relative rho(m_A^-1 m_C)) = %s" % (p, q, N, N, sorted(set(rows))))
print("r7 exit 0")
