#!/usr/bin/env python3
"""B1375: exact verification over Q(zeta_N) of the six Standard-Model sector counts of a background listed by tower_generations.py
(a level Y_n on its own presentation, a locus chi, a pair (psi_Y, psi_gamma)), with B1374's cyclotomic instrument.
Usage: python3 exact_check_cover.py n chi psiY psiG   (all as exponent tuples, e.g. "(24,66,12)"; n = the level)"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1374_the_class_index_in_the_sm_frame", "verification"))
from exact_lib import Cyc, KRep, data
import snappy
SECTORS = [("Q", 1, 3), ("u^c", -4, 3), ("e^c", 6, 3), ("d^c", 2, 1), ("L", -3, 1), ("nu^c", 0, -5)]
n = int(sys.argv[1]); tup = lambda s: tuple(int(x) for x in s.strip('()').split(','))
chi_e, pY, pG = tup(sys.argv[2]), tup(sys.argv[3]), tup(sys.argv[4])
M = snappy.Manifold('m004').covers(n, cover_type='cyclic')[0]; G = M.fundamental_group()
gens, rels = list(G.generators()), list(G.relators()); mu, lam = G.peripheral_curves()[0]
import math
def torsion_exponent(H1):
    e = 1
    for part in H1.replace(' ', '').split('+'):
        if part.startswith('Z/'): e = e * int(part[2:]) // math.gcd(e, int(part[2:]))
    return e
e = torsion_exponent(str(M.homology())); N = 12 * e // math.gcd(12, e)
K = Cyc(N); print(f"Y_{n} = {M.homology()}, K = Q(zeta_{N}) of degree {K.d}; gens {gens}, rels {rels}, mu {mu}, lambda {lam}; chi = {chi_e}, psi_Y = {pY}, psi_gamma = {pG}", flush=True)
chi = dict(zip(gens, chi_e)); chi2 = {g: K.zeta(2 * chi[g]) for g in gens}
rep1 = KRep(K, gens, {g: [[chi2[g]]] for g in gens})
d1 = K.vstack(*[K.hstack(*[rep1.fox(r)[g] for g in gens]) for r in rels]); Z = K.nullspace(d1, len(gens))
bvec = [K.sub(chi2[g], K.const(1)) for g in gens]; rb = 0 if all(K.is_zero(x) for x in bvec) else 1
h1 = len(Z) - rb; ct = None
for z in Z:
    if rb == 0 or K.rank([bvec, z]) == 2: ct = dict(zip(gens, z)); break
print(f"h^1(pi; chi^2) = {h1} exactly; non-split cocycle found: {ct is not None}", flush=True)
chiv = {g: K.zeta(chi[g]) for g in gens}
rho = {g: [[chiv[g], K.mul(ct[g], K.inv(chiv[g]))], [K.const(0), K.inv(chiv[g])]] for g in gens}
R = KRep(K, gens, rho); assert all(R.word(r) == K.eye(2) for r in rels); print("rho_chi is a representation over K (exactly)", flush=True)
out = []
for (lab, sy, sg) in SECTORS:
    psi = {g: (sy * pY[i] + sg * pG[i]) % N for i, g in enumerate(gens)}
    psiv = {g: K.zeta(psi[g]) for g in gens}
    V = KRep(K, gens, {g: K.mscale(psiv[g], rho[g]) for g in gens}); assert all(V.word(r) == K.eye(2) for r in rels)
    a0, a1, t0, t1, r1 = data(V, rels, mu, lam); b0, b1, s0, s1, q1 = data(V.dual(), rels, mu, lam)
    assert r1 + q1 == t1 == s1; I = (a1 - r1) - (b1 - q1); assert I == (a0 - b0) + s0 - r1
    out.append(I); print(f"  {lab:5s} psi = {tuple(psi[g] for g in gens)}: I = {I:+d}  V = {(a0, a1, t0, r1)}  V* = {(b0, b1, s0, q1)}", flush=True)
print(f"EXACT counts (Q, u^c, e^c, d^c, L, nu^c) = {tuple(out)}")
