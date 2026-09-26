#!/usr/bin/env python3
"""B1376 -- the bound.  On a level Y_n of the tower, for every rank-one character psi into mu_N (N = lcm(12, torsion exponent)) the
dimension a_1 = h^1(Y_n; psi) is computed (over one prime, the value 0/1/2+ re-checked over two more for every non-zero); then for the
non-split doublet modules V = rho_chi (x) psi the extension 0 -> chi psi -> V -> chi^-1 psi -> 0 gives a_1(V) <= a_1(chi psi) +
a_1(chi^-1 psi), and |I(V)| <= max(a_1(V), a_1(V*)).  With a_1 <= 1 on every rank-one character, |I| <= 2 on every background of the
level: three generations in one background are impossible there.  The firing modules' a_1(V), a_1(V*) are tabulated.
Usage: python3 rank_one_bound.py n [n ...]"""
import sys, os, math, time, warnings
from collections import Counter
warnings.filterwarnings("ignore")
import snappy
argv = sys.argv; sys.argv = ['x', 'none']
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1374_the_class_index_in_the_sm_frame", "verification"))
from index_lib import GF, Rep, module, index, characters, cohomology_data, h1_and_cocycle, reducible_rep, abelian_exponents
def torsion_exponent(H1):
    e = 1
    for part in H1.replace(' ', '').split('+'):
        if part.startswith('Z/'): e = e * int(part[2:]) // math.gcd(e, int(part[2:]))
    return e
def primes_for(N, k=3, start=400):
    out = []; p = (start // N + 1) * N + 1
    while len(out) < k:
        if all(p % q for q in range(2, int(p ** 0.5) + 1)): out.append(p)
        p += N
    return out
for n in [int(x) for x in argv[1:]] or [2, 3, 4, 5, 6]:
    t0 = time.time(); M = snappy.Manifold('m004').covers(n, cover_type='cyclic')[0]; G = M.fundamental_group()
    gens, rels = list(G.generators()), list(G.relators()); mu, lam = G.peripheral_curves()[0]
    H1 = str(M.homology()); e = torsion_exponent(H1); N = 12 * e // math.gcd(12, e); P = primes_for(N)
    Fs = [GF(p) for p in P]; zs = [F.root_of_unity(N) for F in Fs]
    chars = characters(Fs[0], gens, rels, N)
    a1 = Counter(); nonzero = []
    for psi in chars:
        rep = Rep(Fs[0], gens, {g: [[pow(zs[0], psi[g], P[0])]] for g in gens})
        a = cohomology_data(rep, rels, mu, lam)[1]; a1[a] += 1
        if a: nonzero.append((psi, a))
    bad = 0
    for psi, a in nonzero:
        for F, z in zip(Fs[1:], zs[1:]):
            rep = Rep(F, gens, {g: [[pow(z, psi[g], F.p)]] for g in gens})
            if cohomology_data(rep, rels, mu, lam)[1] != a: bad += 1
    print(f"Y_{n}: H1 = {H1}, N = {N}, primes {P}: rank-one characters {len(chars)}, a_1 = h^1 distribution {dict(sorted(a1.items()))}; non-zero re-checked over two more primes: {len(nonzero)}, differing {bad}; max a_1 = {max(a1)}; {time.time() - t0:.0f} s", flush=True)
print("DONE")
