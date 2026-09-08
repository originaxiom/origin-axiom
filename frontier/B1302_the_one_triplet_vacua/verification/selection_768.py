#!/usr/bin/env python3
"""THE SELECTION AMONG THE 768 (B1302 addendum, L210(iii)): the closing's own symmetries act on its characters -- the
deck t (multiplication by phi^2 on H_1 = Z[phi]/(sqrt5 F_12)), the half-deck Psi (multiplication by phi, induced by the
fibre automorphism a -> ab, b -> a which commutes with the monodromy up to inner automorphisms), the amphichiral
involution J = [[0,1],[-1,0]] (J Psi J^-1 = -Psi^-1: the Galois conjugation phi -> phibar of Z[phi], the orientation-
reversing symmetry of the figure-eight), and inversion psi -> psi^-1 (charge conjugation, which maps a line to the
mirror's line).  How many inequivalent one-triplet lines does Y_12 have under the group they generate?  Everything in
the fibre coordinates w = (psi(a), psi(b)) as exponents mod m = 720; the 2-primary subgroup (Z/16)^2 carries all letters."""
import sys, json, math, pathlib, itertools, collections
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'B1303_the_two_by_two_criterion' / 'verification'))
import criterion_at_scale as S

QUL = {'Q': (1, 0, 0), 'u^c': (0, 1, 0), 'L': (0, 0, 1), 'D': (-2, 0, 0), 'e^c': (2, -1, 0), 'H_u': (-1, -1, 0),
       'd^c': (1, -1, 1), 'Dbar': (-1, 0, -1), 'H_d': (-2, 1, -1), 'nu^c': (1, 1, -1), 'S': (3, 0, 1)}
LABELS = ('Q', 'u^c', 'd^c', 'L', 'e^c', 'H_u', 'H_d', 'D', 'Dbar', 'S', 'nu^c')

def main(n=12):
    d1, d2, m, U = S.smith(n)
    k1 = 0
    while d1 % 2 ** (k1 + 1) == 0: k1 += 1
    k2 = 0
    while d2 % 2 ** (k2 + 1) == 0: k2 += 1
    fib = S.fib_pairs(n, m); qs = S.primes_1_mod(m)
    chars = []
    for i in range(2 ** k1):
        for j in range(2 ** k2):
            c1 = i * (d1 // 2 ** k1); c2 = j * (d2 // 2 ** k2)
            e1 = (c1 * (m // d1)) % m; e2 = (c2 * (m // d2)) % m
            chars.append(((U[0][0] * e1 + U[1][0] * e2) % m, (U[0][1] * e1 + U[1][1] * e2) % m))
    W1 = np.array([w[0] for w in chars], dtype=np.int64); W2 = np.array([w[1] for w in chars], dtype=np.int64)
    ok = S.identity_test(W1, W2, n, m, qs[0], fib) & S.identity_test(W1, W2, n, m, qs[1], fib)
    supp = {w for w, h in zip(chars, ok.tolist()) if h and w != (0, 0)}
    order = lambda w: m // math.gcd(math.gcd(w[0], w[1]), m)
    chis = [w for w in supp if order(w) == 2]
    add = lambda a, b: ((a[0] + b[0]) % m, (a[1] + b[1]) % m)
    G = lambda w: sum(1 for c in chis if add(w, c) in supp)
    K3 = [w for w in chars if G(w) >= 3]
    assert len(supp) == 123 and len(chis) == 3 and len(K3) == 97, (len(supp), len(chis), len(K3))
    # the lines and the 768
    idx = {w: i for i, w in enumerate(chars)}
    Hs = np.zeros(len(chars), dtype=np.int64)
    for w in supp: Hs[idx[w]] = 1
    def surv(w):                      # survival bits of a component with character w
        return tuple(int(add(w, c) in supp) for c in chis)
    lines768 = []; n_sm = 0; sm_lines = []
    for q, u, l in itertools.product(K3, repeat=3):
        comp = {}
        for lab, (a, b, c) in QUL.items():
            comp[lab] = ((a * q[0] + b * u[0] + c * l[0]) % m, (a * q[1] + b * u[1] + c * l[1]) % m)
        tot = {lab: sum(surv(comp[lab])) for lab in LABELS}
        three = all(tot[x] == 3 for x in ('Q', 'u^c', 'd^c', 'L', 'e^c'))
        broken = not (comp['Q'] == comp['u^c'] == comp['e^c'])
        vac = tot['S'] >= 1 and tot['nu^c'] >= 1 and tot['H_u'] >= 1 and tot['H_d'] >= 1
        if not (three and broken and vac):
            continue
        n_sm += 1; sm_lines.append((q, u, l))
        if tot['D'] == 1 and tot['Dbar'] == 1 and tot['S'] == 1 and all(tot[x] == 3 for x in ('H_u', 'H_d', 'nu^c')):
            gD = surv(comp['D']).index(1); gDb = surv(comp['Dbar']).index(1); gN = surv(comp['S']).index(1)
            if len({gD, gDb, gN}) == 3:
                lines768.append((q, u, l))
    assert n_sm == 34752 and len(lines768) == 768, (n_sm, len(lines768))
    # the symmetries on exponent vectors w: psi o M  <->  M^T w
    Psi = lambda w: ((w[0] + w[1]) % m, w[0] % m)                       # Psi^T
    Jm = lambda w: ((-w[1]) % m, w[0] % m)                               # J^T, J = [[0,1],[-1,0]]
    Neg = lambda w: ((-w[0]) % m, (-w[1]) % m)
    def orbits(lines, gens):
        S_ = set(lines); seen = set(); orbs = []
        for L in lines:
            if L in seen:
                continue
            orb = {L}; frontier = [L]
            while frontier:
                nxt = []
                for x in frontier:
                    for g in gens:
                        y = tuple(g(w) for w in x)
                        if y not in orb:
                            orb.add(y); nxt.append(y)
                frontier = nxt
            assert orb <= S_, "a symmetry maps a one-triplet line outside the set"
            seen |= orb; orbs.append(len(orb))
        return orbs
    out = {}
    for name, gens in (("deck t = Psi^2", [lambda w: Psi(Psi(w))]), ("deck and half-deck <Psi>", [Psi]), ("<Psi, J>", [Psi, Jm]), ("<Psi, J, inversion>", [Psi, Jm, Neg])):
        orbs = orbits(lines768, gens)
        out[name] = (len(orbs), dict(collections.Counter(orbs)))
        print(f"  {name}: {len(orbs)} orbits on the 768 one-triplet lines, sizes {dict(sorted(collections.Counter(orbs).items()))}")
    # all 34 752 SM lines under the full group (B1279 counted Y_9's inequivalent SM vacua the same way)
    orbs_all = orbits(sm_lines, [Psi, Jm, Neg])
    out['all SM lines <Psi, J, inversion>'] = (len(orbs_all), dict(collections.Counter(orbs_all)))
    print(f"  all {len(sm_lines)} SM lines under <Psi, J, inversion>: {len(orbs_all)} orbits, sizes {dict(sorted(collections.Counter(orbs_all).items()))}")
    # sanity: J is a symmetry of the support (it must map the support to itself)
    print(f"  J preserves the support: {all(Jm(w) in supp for w in supp)}; Psi preserves it: {all(Psi(w) in supp for w in supp)}; inversion preserves it: {all(Neg(w) in supp for w in supp)}")
    return out

if __name__ == "__main__":
    out = main()
    ok = out["deck t = Psi^2"][0] == 64
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
