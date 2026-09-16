#!/usr/bin/env python3
"""B1374: exact verification over the cyclotomic field Q(zeta_N) of the six Standard-Model sector counts at a generation-shaped pair
found over prime fields.  Own implementation: elements of K = Q(zeta_N) as coefficient vectors modulo the N-th cyclotomic polynomial,
K-ranks as Q-ranks of the regular-representation blow-up (sympy DomainMatrix over QQ) divided by [K : Q]; the same cohomology
definitions as index_lib.py (left Fox convention, H^0, H^1, the cusp torus, r_1, n = a_1 - r_1, I = n(V) - n(V*)).
Usage: python3 exact_check.py member N j psiY psiG   (j = index of the locus in the sorted intersection list; psi as exponent tuples)"""
import sys, os, math, itertools
from fractions import Fraction as Fr
argv = sys.argv; sys.argv = ['x', 'none']
import importlib.util
spec = importlib.util.spec_from_file_location("cis", os.path.join(os.path.dirname(os.path.abspath(__file__)), "class_index_sm_frame.py"))
cis = importlib.util.module_from_spec(spec); spec.loader.exec_module(cis)

from exact_lib import Cyc, KRep, data

name, N, j = argv[1], int(argv[2]), int(argv[3]); psiY = tuple(int(x) for x in argv[4].strip('()').split(',')); psiG = tuple(int(x) for x in argv[5].strip('()').split(','))
p = {60: 421, 48: 337, 12: 61}[N]
B = cis.Bench(name, p, N=N); gens = B.gens; rels = B.rels; mu, lam = B.mu, B.lam
common = sorted(set(tuple(chi[g] for g in gens) for (chi, h1, ct) in B.loci))     # the same ordering as the census on one prime
for q in ({60: (541, 601), 48: (433, 577), 12: (181, 241)}[N]):
    Bq = cis.Bench(name, q, N=N); common = sorted(set(common) & set(tuple(chi[g] for g in gens) for (chi, h1, ct) in Bq.loci))
chi_exp = common[j]; chi = dict(zip(gens, chi_exp))
K = Cyc(N); print(f"K = Q(zeta_{N}), degree {K.d}; {name}: gens {gens}, rels {rels}; locus chi = {chi_exp}, psi_Y = {psiY}, psi_gamma = {psiG}")
chi2 = {g: K.zeta(2 * chi[g]) for g in gens}
# H^1(pi; chi^2) and a non-coboundary cocycle, exactly
rep1 = KRep(K, gens, {g: [[chi2[g]]] for g in gens})
d1 = K.vstack(*[K.hstack(*[rep1.fox(r)[g] for g in gens]) for r in rels]); Z = K.nullspace(d1, len(gens))
bvec = [K.sub(chi2[g], K.const(1)) for g in gens]; rb = 0 if all(K.is_zero(x) for x in bvec) else 1
h1 = len(Z) - rb; ct = None
for z in Z:
    if rb == 0 or K.rank([bvec, z]) == 2: ct = dict(zip(gens, z)); break
print(f"h^1(pi; chi^2) = {h1} exactly; non-split cocycle found: {ct is not None}")
chiv = {g: K.zeta(chi[g]) for g in gens}
rho = {g: [[chiv[g], K.mul(ct[g], K.inv(chiv[g]))], [K.const(0), K.inv(chiv[g])]] for g in gens}
R = KRep(K, gens, rho); assert all(R.word(r) == K.eye(2) for r in rels), "rho is not a representation"
print("rho_chi is a representation over K (relators to the identity, exactly)", flush=True)
def I_of(psi_exp):
    psiv = {g: K.zeta(psi_exp[g]) for g in gens}
    V = KRep(K, gens, {g: K.mscale(psiv[g], rho[g]) for g in gens}); assert all(V.word(r) == K.eye(2) for r in rels)
    a0, a1, t0, t1, r1 = data(V, rels, mu, lam); b0, b1, s0, s1, q1 = data(V.dual(), rels, mu, lam)
    assert r1 + q1 == t1 == s1, "annihilator identity"
    I = (a1 - r1) - (b1 - q1); assert I == (a0 - b0) + s0 - r1, "B1297 identity"
    return I, (a0, a1, t0, r1), (b0, b1, s0, q1)
out = []
for (lab, sy, sg) in cis.SM_SECTORS:
    psi = {g: (sy * psiY[i] + sg * psiG[i]) % N for i, g in enumerate(gens)}
    I, dV, dVd = I_of(psi); out.append(I)
    print(f"  {lab:28s} psi = {tuple(psi[g] for g in gens)}: I = {I:+d}   (a0,a1,t0,r1) V = {dV}  V* = {dVd}")
print(f"EXACT counts (Q, u^c, e^c, d^c, L, nu^c) = {tuple(out)}")
