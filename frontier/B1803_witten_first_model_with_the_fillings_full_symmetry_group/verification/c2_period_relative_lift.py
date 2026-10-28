"""P-409 check: the period P's relative lift between its two circles (the axis A and the filling's core C) on the order-2
bundle, on many even fillings, against main's closed form epsilon = p/2 mod 2 (from H1^orb(Q/P) = Z/2<mu_A> x Z/p<mu'>,
psi(mu') = 0, rho(mu') = chi(mu) = 1, m_C = (p/2) mu' + q lambda', lambda' = 3 mu_A in homology, q odd).
Same construction as the referee's r5 (b): Q/P = L6a2 filled [(2, 0), (p, 2q)]."""
import snappy, itertools, math

def abel_vec(word, gens):
    v = [0] * len(gens)
    for ch in word:
        v[gens.index(ch.lower())] += 1 if ch.islower() else -1
    return v

def ev(vals, vec):
    return sum(a * b for a, b in zip(vals, vec)) % 2

rows = 0; bad = 0
for p in range(2, 31, 2):
    for q in [1, 3, 5, 7, -1, -3]:
        if math.gcd(p, q) != 1:
            continue
        O = snappy.Manifold("L6a2"); O.dehn_fill([(2, 0), (p, 2 * q)])
        G = O.fundamental_group(); gens = G.generators()
        R = [abel_vec(r, gens) for r in G.relators()]
        H = [v for v in itertools.product((0, 1), repeat=len(gens)) if all(ev(v, r) == 0 for r in R)]
        per = G.peripheral_curves()
        mA = abel_vec(per[0][0], gens); muK, laK = abel_vec(per[1][0], gens), abel_vec(per[1][1], gens)
        mC = [a * (p // 2) + b * q for a, b in zip(muK, laK)]
        psi = [h for h in H if ev(h, mA) == 1 and ev(h, mC) == 1 and ev(h, muK) == 0]
        assert len(psi) == 1, (p, q, len(psi)); psi = psi[0]
        rel = sorted(set((ev(h, mA) + ev(h, mC)) % 2 for h in H if h != psi and any(h)))
        ok = rel == [(p // 2) % 2]
        rows += 1; bad += (not ok)
        print("m004(%d,%d): |Hom| %d, relative lift of P (axis vs core) %s, p/2 mod 2 = %d %s" % (p, q, len(H), rel, (p // 2) % 2, "" if ok else "MISMATCH"))
print("fillings %d, mismatches %d" % (rows, bad))
print("c2 exit 0")
