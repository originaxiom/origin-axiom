#!/usr/bin/env python3
"""B1374 (C''): the generation-shaped pairs on t12839 at N = 60, listed and recomputed sector by sector with the scalar instrument over
three primes (independently of the vectorised pair census), with the locus data (chi on the cusp, h^1(chi^2)), the orders of psi_Y and
psi_gamma, the six counts and the semisimplified counts.  Saves the m = 1 table.  Usage: python3 generation_pairs.py [member] [N]"""
import sys, os, json, time, math, warnings, itertools
warnings.filterwarnings("ignore")
import numpy as np
argv = sys.argv; sys.argv = ['x', 'none']
import importlib.util
spec = importlib.util.spec_from_file_location("cis", os.path.join(os.path.dirname(os.path.abspath(__file__)), "class_index_sm_frame.py"))
cis = importlib.util.module_from_spec(spec); spec.loader.exec_module(cis)
from index_lib import char_value, Rep, module, index
HERE = os.path.dirname(os.path.abspath(__file__))
name = argv[1] if len(argv) > 1 else 't12839'; N = int(argv[2]) if len(argv) > 2 else 60
PR = {12: (61, 181, 241), 48: (337, 433, 577), 60: (421, 541, 601)}[N]
t0 = time.time()
benches = [cis.Bench(name, q, N=N) for q in PR]; B = benches[0]; gens = B.gens; F = B.F; psis = B.chars; nH = len(psis)
keysets = [set(tuple(chi[g] for g in gens) for (chi, h1, ct) in Bq.loci) for Bq in benches]
common = sorted(set.intersection(*keysets))
idx = [{tuple(chi[g] for g in gens): i for i, (chi, h1, ct) in enumerate(Bq.loci)} for Bq in benches]
li_of = [[ix[k] for k in common] for ix in idx]; nloci = len(common)
key = lambda psi: sum(psi[g] * N ** i for i, g in enumerate(gens))
lookup = {key(psi): i for i, psi in enumerate(psis)}
tab_path = os.path.join(HERE, f'table_{name}_N{N}.npy')
if os.path.exists(tab_path): table = np.load(tab_path)
else:
    table = np.zeros((nloci, nH), dtype=np.int64)
    for j in range(nloci):
        for i, psi in enumerate(psis): table[j, i] = B.I(li_of[0][j], 1, psi)[0]
    np.save(tab_path, table)
print(f"{name}: N = {N}, |Hom| = {nH}, loci {nloci}, table ready ({time.time() - t0:.0f} s); non-zero doublet modules {int((table != 0).sum())}", flush=True)
def power(psi, k): return {g: (k * psi[g]) % N for g in gens}
def prod(a, b): return {g: (a[g] + b[g]) % N for g in gens}
def order(psi): return min(k for k in range(1, N + 1) if all(k * psi[g] % N == 0 for g in gens))
SEC = cis.SM_SECTORS
# the pair search, vectorised as in torsion_complete.py (exponent arithmetic on the character group)
E = np.array([[psi[g] for g in gens] for psi in psis], dtype=np.int64); powers = np.array([N ** i for i in range(len(gens))], dtype=np.int64)
lk = -np.ones(N ** len(gens), dtype=np.int64)
for i, psi in enumerate(psis): lk[key(psi)] = i
A = np.repeat(np.arange(nH), nH); Bi = np.tile(np.arange(nH), nH)
sec_idx = [lk[((sy * E[A] + sg * E[Bi]) % N) @ powers] for (lab, sy, sg) in SEC]
found = []
for j in range(nloci):
    if int((table[j] != 0).sum()) < 2: continue
    c = [table[j][idx] for idx in sec_idx]
    gs = (c[0] == c[1]) & (c[1] == c[2]) & (c[2] == c[3]) & (c[3] == c[4]) & (c[0] != 0)
    for t in np.nonzero(gs)[0]: found.append((j, int(A[t]), int(Bi[t]), [int(x[t]) for x in c]))
print(f"generation-shaped pairs (from the table): {len(found)}", flush=True)
# recompute each with the scalar instrument over three primes (no vectorised mapping), and gather the structure
rows = []; bad = 0
loci_used = sorted(set(f[0] for f in found)); yorders = {}; gorders = {}; signs = {}
for (j, a, b, c) in found:
    pY, pG = psis[a], psis[b]; vals = []
    for q, Bq in enumerate(benches):
        v = [Bq.I(li_of[q][j], 1, prod(power(pY, sy), power(pG, sg)))[0] for (lab, sy, sg) in SEC]
        vals.append(v)
    if not (vals[0] == vals[1] == vals[2] == c): bad += 1
    yorders[order(pY)] = yorders.get(order(pY), 0) + 1; gorders[order(pG)] = gorders.get(order(pG), 0) + 1; signs[c[0]] = signs.get(c[0], 0) + 1
print(f"recomputed sector by sector over {PR}: differing {bad} of {len(found)}", flush=True)
print(f"loci carrying a generation-shaped pair: {len(loci_used)} of {nloci}; sign of the count: {signs}; orders of psi_Y: {yorders}; orders of psi_gamma: {gorders}")
print("the loci (chi exponents on the generators; chi(mu), chi(lambda) as zeta_N powers; h^1(chi^2)):")
for j in loci_used:
    chi, h1, ct = B.loci[li_of[0][j]]
    om = next(k for k in range(N) if pow(B.z, k, F.p) == char_value(F, B.z, chi, B.mu)); ol = next(k for k in range(N) if pow(B.z, k, F.p) == char_value(F, B.z, chi, B.lam))
    npairs = sum(1 for f in found if f[0] == j)
    print(f"  locus {j:3d}: chi = {tuple(chi[g] for g in gens)} order {order(chi):2d}; chi(mu) = z^{om}, chi(lambda) = z^{ol}; h1(chi^2) = {h1}; generation-shaped pairs {npairs}")
# a few explicit examples with the semisimplification and the untwisted-psi_Y cases
ex = [f for f in found if all(v == 0 for v in psis[f[1]].values())][:3] + found[:2]
print("examples (psi_Y, psi_gamma as exponent tuples; the six counts (Q, u^c, e^c, d^c, L, nu^c); semisimplified counts):")
for (j, a, b, c) in ex:
    pY, pG = psis[a], psis[b]
    ss = [B.I(li_of[0][j], 1, prod(power(pY, sy), power(pG, sg)), semisimple=True)[0] for (lab, sy, sg) in SEC]
    print(f"  locus {j}: psi_Y = {tuple(pY[g] for g in gens)} (order {order(pY)}), psi_gamma = {tuple(pG[g] for g in gens)} (order {order(pG)}): counts {tuple(c)}; semisimplified {tuple(ss)}")
json.dump({'name': name, 'N': N, 'found': found, 'loci_used': loci_used, 'signs': signs, 'yorders': yorders, 'gorders': gorders, 'differing': bad,
           'examples': [(j, tuple(psis[a][g] for g in gens), tuple(psis[b][g] for g in gens), c) for (j, a, b, c) in ex]},
          open(os.path.join(HERE, f'generation_pairs_{name}_N{N}.json'), 'w'), indent=1)
print("DONE")
