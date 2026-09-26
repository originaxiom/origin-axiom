#!/usr/bin/env python3
"""B1379 -- DO THE CUSPED COVERS' INDEX BACKGROUNDS DESCEND TO THE CLOSED TOWER?  This record uses Y_n for two different
spaces: B1301/B1303 define Y_n as the n-fold cyclic BRANCHED covers of S^3 along the figure-eight (closed; the Fibonacci
manifolds, "z filled"), while B1374/B1375/B1377/B1378 used Y_n for the n-fold cyclic covers of m004 itself (cusped;
SnapPy's covers(n, 'cyclic') or the Reidemeister-Schreier presentation with z = a^n unfilled).  The closed Y_n is the
cusped cover Dehn-filled along the lifted meridian, so a representation descends iff it is trivial on that curve.

  M4: SnapPy's cover of m004 has peripheral curves (cACa, CB); filling CB gives |H1| = 45 = 5 F_4^2 and volume
      4 vol(m004(4,0)) -- the branched cover Y4 -- so CB is the lifted meridian.  Every one of B1375's 89 non-split
      loci (common to three primes, computed with B1375's own code) is tested: rho_chi(CB) = I ?
  M6: B1378's deck triplet, in its Reidemeister-Schreier presentation where z = a^6 is the lifted meridian: rho(z) = I ?
Usage: python3 descent_check.py"""
import sys, os, math, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
B1375 = os.path.join(HERE, "..", "..", "B1375_the_towers_generation_count", "verification")
B1378 = os.path.join(HERE, "..", "..", "B1378_the_m6_deck_triplet", "verification")
sys.path.insert(0, B1375)
sys.path.insert(0, B1378)
argv = sys.argv; sys.argv = ["x", "none"]
import tower_generations as T
import deck_triplet as D
from index_lib import GF, Rep, h1_and_cocycle, reducible_rep
sys.argv = argv


def filled_curve_M4():
    C = T.snappy.Manifold("m004").covers(4, cover_type="cyclic")[0]
    G = C.fundamental_group(); mer, lon = G.peripheral_curves()[0]
    O = T.snappy.Manifold("m004"); O.dehn_fill((4, 0)); target = 4 * float(O.volume())
    Y = C.copy(); Y.dehn_fill((0, 1))
    assert str(Y.homology()) == "Z/3 + Z/15" and abs(float(Y.volume()) - target) < 1e-8
    return lon, str(C.homology()), str(Y.homology()), float(Y.volume())


def m4_descent():
    word, H1c, H1y, vol = filled_curve_M4()
    n = 4
    e = T.torsion_exponent(H1c); N = 12 * e // math.gcd(12, e)
    Ls = [T.Level(n, p, N) for p in T.primes_for(N)]; L0 = Ls[0]; gens = L0.gens
    common = set.intersection(*[set(tuple(chi[g] for g in gens) for (chi, h1, ct) in Lq.loci) for Lq in Ls])
    total = descend = diag = 0
    for (chi, h1, ct) in L0.loci:
        if tuple(chi[g] for g in gens) not in common: continue
        total += 1
        R = Rep(L0.F, gens, reducible_rep(L0.F, gens, {g: pow(L0.z, chi[g], L0.p) for g in gens}, ct))
        W = R.word(word)
        diag += (W[0][0] == 1 and W[1][1] == 1)
        descend += (W == L0.F.eye(2))
    return word, H1c, H1y, vol, total, diag, descend


def m6_descent(p=601):
    F = GF(p); z = F.root_of_unity(D.N); out = []
    for j in range(3):
        cc = D.deck(D.SEED_CHI, 2 * j); yy = D.deck(D.SEED_Y, 2 * j); gg = D.deck(D.SEED_G, 2 * j)
        chi = dict(zip(D.GENS, cc))
        h1, ct = h1_and_cocycle(F, D.GENS, D.RELS, D.MU, D.LAM, {g: pow(z, 2 * chi[g], p) for g in D.GENS})
        R = Rep(F, D.GENS, reducible_rep(F, D.GENS, {g: pow(z, chi[g], p) for g in D.GENS}, ct))
        rz = R.word("a")                                       # z = a^6, the lifted meridian
        out.append((cc[0], yy[0], gg[0], rz, rz == F.eye(2)))
    return out


if __name__ == "__main__":
    word, H1c, H1y, vol, total, diag, descend = m4_descent()
    print(f"M4 = SnapPy's cyclic 4-cover of m004, H1 {H1c}; filling its curve {word} gives H1 {H1y}, volume {vol:.10f} = 4 vol(m004(4,0)): the closed branched Y4")
    print(f"M4 non-split loci (common to three primes): {total}; diagonal character trivial on the filled curve: {diag}; rho_chi trivial there (descends to Y4): {descend}")
    assert total == 89 and descend == 0
    for j, (cz, yz, gz, rz, ok) in enumerate(m6_descent()):
        print(f"M6 triplet member {j}: chi(z) = {cz}, psi_Y(z) = {yz}, psi_gamma(z) = {gz}; rho(z) = {rz}; descends to closed Y6: {ok}")
        assert cz == yz == gz == 0 and not ok
    print("DONE")
