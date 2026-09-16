#!/usr/bin/env python3
"""B1374: the structure of the generation-shaped pairs found on a member (from generation_pairs_<member>_N<N>.json): for a sample of
pairs, (i) the 78's conjugate sectors -- the net count of an SM representation R of the 78 is n(V_R) - n(V_{Rbar}) with V_{Rbar} the
sector of the opposite weight, rho_chi (x) psi_R^{-1}; it equals I(V_R) = n(V_R) - n(V_R^*) iff rho_chi is self-dual, which holds when
h^1(chi^2) = 1 -- compared with I; (ii) the counts of every sector of the 27 and the 78 in the pair's background (the full net
spectrum); (iii) the distribution of the singlet count and of psi_Y over all pairs.  Usage: python3 generation_structure.py member N"""
import sys, os, json, random, warnings
warnings.filterwarnings("ignore")
argv = sys.argv; sys.argv = ['x', 'none']
import importlib.util
spec = importlib.util.spec_from_file_location("cis", os.path.join(os.path.dirname(os.path.abspath(__file__)), "class_index_sm_frame.py"))
cis = importlib.util.module_from_spec(spec); spec.loader.exec_module(cis)
from index_lib import Rep, module, index, cohomology_data
HERE = os.path.dirname(os.path.abspath(__file__))
name, N = argv[1], int(argv[2]); p = {60: 421, 48: 337, 12: 61}[N]
J = json.load(open(os.path.join(HERE, f'generation_pairs_{name}_N{N}.json')))
B = cis.Bench(name, p, N=N); gens = B.gens; F = B.F; psis = B.chars
common = sorted(set(tuple(chi[g] for g in gens) for (chi, h1, ct) in B.loci))
for q in ({60: (541, 601), 48: (433, 577), 12: (181, 241)}[N]):
    Bq = cis.Bench(name, q, N=N); common = sorted(set(common) & set(tuple(chi[g] for g in gens) for (chi, h1, ct) in Bq.loci))
li_index = {tuple(chi[g] for g in gens): i for i, (chi, h1, ct) in enumerate(B.loci)}
def power(psi, k): return {g: (k * psi[g]) % N for g in gens}
def prod(a, b): return {g: (a[g] + b[g]) % N for g in gens}
def n_of(li, psi):
    """n(V) for V = rho_chi (x) psi, and n(V*)"""
    I, dV, dVd = B.I(li, 1, psi); return dV[1] - dV[3], dVd[1] - dVd[3], I
# every sector of the 27 and the 78 with its (6Y, 3gamma, spin): from B1372's typing
SECTORS27 = [("27: Q (10, spin 0)", 1, -2, 0), ("27: u^c (10, spin 0)", -4, -2, 0), ("27: e^c (10, spin 0)", 6, -2, 0), ("27: D (5, spin 0)", -2, 4, 0), ("27: H_u (5, spin 0)", 3, 4, 0),
             ("27: d^c/Dbar (5b, doublet)", 2, 1, 1), ("27: L/H_d (5b, doublet)", -3, 1, 1), ("27: nu^c/N (1, doublet)", 0, -5, 1)]
SECTORS78 = [("78: Q (10, doublet)", 1, 3, 1), ("78: u^c (10, doublet)", -4, 3, 1), ("78: e^c (10, doublet)", 6, 3, 1),
             ("78: Qbar (10b, doublet)", -1, -3, 1), ("78: u (10b, doublet)", 4, -3, 1), ("78: e (10b, doublet)", -6, -3, 1),
             ("78: d^c/Dbar (5b, spin 0)", 2, 6, 0), ("78: L/H_d (5b, spin 0)", -3, 6, 0), ("78: D (5, spin 0)", -2, -6, 0), ("78: H_u (5, spin 0)", 3, -6, 0),
             ("78: 24 (spin 0)", 0, 0, 0), ("78: SL(2)_beta adjoint (triplet)", 0, 0, 2)]
found = J['found']; random.seed(1374); sample = random.sample(found, min(len(found), 6))
print(f"{name}, N = {N}: generation-shaped pairs {len(found)} on {len(J['loci_used'])} loci; signs {J['signs']}; psi_Y orders {J['yorders']}; psi_gamma orders {J['gorders']}")
# (iii) singlet count and psi_Y distribution over all pairs
nu = {}; for_y = {}
for (j, a, b, c) in found:
    nu[c[5]] = nu.get(c[5], 0) + 1
print(f"singlet (nu^c/N) count among the generation-shaped pairs: {nu}")
# (i), (ii) on the sample
for (j, a, b, c) in sample:
    li = li_index[common[j]]; chi, h1, ct = B.loci[li]; pY, pG = psis[a], psis[b]
    print(f"\n locus {j} chi = {common[j]} h1(chi^2) = {h1}; psi_Y = {tuple(pY[g] for g in gens)}, psi_gamma = {tuple(pG[g] for g in gens)}; counts {tuple(c)}")
    for (lab, sy, sg, spin) in SECTORS27 + SECTORS78:
        psi = prod(power(pY, sy), power(pG, sg))
        if spin == 1:
            nV, nVd, I = n_of(li, psi); nR = n_of(li, power(psi, -1))[0]
            conj = f"n(V_R) - n(V_Rbar) = {nV - nR:+d}" if lab.startswith("78") else ""
            print(f"    {lab:34s} n(V) = {nV}, n(V*) = {nVd}, I = {I:+d}  {conj}")
        elif spin == 0:
            I, dV, dVd = B.I(li, 0, psi); print(f"    {lab:34s} n(V) = {dV[1] - dV[3]}, n(V*) = {dVd[1] - dVd[3]}, I = {I:+d}")
        else:
            I, dV, dVd = B.I(li, 2, psi); print(f"    {lab:34s} n(V) = {dV[1] - dV[3]}, n(V*) = {dVd[1] - dVd[3]}, I = {I:+d}")
# self-duality of rho_chi at the generation loci: h1(chi^2) over the loci used
h1s = {}
for j in J['loci_used']:
    li = li_index[common[j]]; h1s[B.loci[li][1]] = h1s.get(B.loci[li][1], 0) + 1
print(f"\nh^1(chi^2) over the {len(J['loci_used'])} generation loci: {h1s}")
print("DONE")
