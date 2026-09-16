#!/usr/bin/env python3
"""B1374 (C'): the Standard-Model-frame census made complete on the torsion of H_1.  Main's B1418 searched characters into mu_12; a
member whose torsion has exponent e carries characters of order e that mu_12 cannot see (Z/16 on o10_150701, Z/15 on t12839, Z/5 on
o10_150697, Z/10 on m208).  Here N = lcm(12, e): every non-split locus chi in Hom(H_1, mu_N), every psi in Hom(H_1, mu_N), the doublet
module rho_chi (x) psi (m = 1) over one prime p = 1 mod N, every non-zero value and a sample of the zeros re-checked over two more
primes; then the SM-frame pair census (psi_Y, psi_gamma) in Hom(H_1, mu_N)^2, vectorised.  Usage: python3 torsion_complete.py [members]"""
import sys, os, json, time, math, random, warnings
warnings.filterwarnings("ignore")
import numpy as np
sys.argv, argv = ['x', 'none'], sys.argv
import importlib.util
spec = importlib.util.spec_from_file_location("cis", os.path.join(os.path.dirname(os.path.abspath(__file__)), "class_index_sm_frame.py"))
cis = importlib.util.module_from_spec(spec); spec.loader.exec_module(cis)
from index_lib import char_value
HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES_FOR = {12: (61, 181, 241), 24: (193, 241, 337), 48: (337, 433, 577), 60: (421, 541, 601)}   # p = 1 mod N
def torsion_exponent(H1):
    e = 1
    for part in H1.replace(' ', '').split('+'):
        if part.startswith('Z/'): e = e * int(part[2:]) // math.gcd(e, int(part[2:]))
    return e
names = argv[1:] if len(argv) > 1 else cis.MEMBERS
summary = {}
for name in names:
    t0 = time.time()
    H1 = cis.presentation(name)[4]; e = torsion_exponent(H1); N = 12 * e // math.gcd(12, e)
    primes = PRIMES_FOR[N]; benches = [cis.Bench(name, q, N=N) for q in primes]; B = benches[0]; gens = B.gens; F = B.F
    psis = B.chars; nH = len(psis)
    # a rank can only drop modulo p, so h^1(chi^2) can only rise: the locus set over one prime contains the true one; the true set is
    # the intersection over the three primes (a spurious locus would need the same drop on all three)
    keysets = [set(tuple(chi[g] for g in gens) for (chi, h1, ct) in Bq.loci) for Bq in benches]
    common = sorted(set.intersection(*keysets)); spurious = [len(k) - len(common) for k in keysets]
    idx = [{tuple(chi[g] for g in gens): i for i, (chi, h1, ct) in enumerate(Bq.loci)} for Bq in benches]
    li_of = [[ix[k] for k in common] for ix in idx]          # li_of[q][j] = index of the j-th common locus in bench q
    nloci = len(common)
    key = lambda psi: sum(psi[g] * N ** i for i, g in enumerate(gens))
    lookup = -np.ones(N ** len(gens), dtype=np.int64)
    for i, psi in enumerate(psis): lookup[key(psi)] = i
    E = np.array([[psi[g] for g in gens] for psi in psis], dtype=np.int64)          # exponent vectors, nH x #gens
    powers = np.array([N ** i for i in range(len(gens))], dtype=np.int64)
    # the m = 1 table over the first prime
    table = np.zeros((nloci, nH), dtype=np.int64)
    for j in range(nloci):
        for i, psi in enumerate(psis):
            table[j, i] = B.I(li_of[0][j], 1, psi)[0]
    nz = [(li, i) for li in range(nloci) for i in range(nH) if table[li, i] != 0]
    # re-check every non-zero and a sample of zeros over two more primes
    zeros = [(li, i) for li in range(nloci) for i in range(nH) if table[li, i] == 0]
    random.seed(1374); sample = random.sample(zeros, min(len(zeros), 300))
    bad = 0
    for (j, i) in nz + sample:
        if any(benches[q].I(li_of[q][j], 1, psis[i])[0] != table[j, i] for q in (1, 2)): bad += 1
    # cusp data of the loci
    loci = [B.loci[li_of[0][j]] for j in range(nloci)]
    cusp_order2 = sum(1 for (chi, h1, ct) in loci if pow(char_value(F, B.z, chi, B.mu), 2, F.p) == 1 and pow(char_value(F, B.z, chi, B.lam), 2, F.p) == 1)
    cusp_trivial = sum(1 for (chi, h1, ct) in loci if char_value(F, B.z, chi, B.mu) == 1 and char_value(F, B.z, chi, B.lam) == 1)
    # the SM-frame pair census, vectorised: for psi_Y = psis[a], psi_gamma = psis[b], sector exponents (sy * E[a] + sg * E[b]) mod N
    A = np.repeat(np.arange(nH), nH); Bi = np.tile(np.arange(nH), nH)
    sec_idx = []
    for (lab, sy, sg) in cis.SM_SECTORS:
        ex = (sy * E[A] + sg * E[Bi]) % N; k = ex @ powers; idx = lookup[k]; assert (idx >= 0).all(); sec_idx.append(idx)
    gen_shaped = 0; anomaly_free = 0; nonzero_pairs = 0; best = (0, None)
    for li in range(nloci):
        c = [table[li][idx] for idx in sec_idx]; kQ, ku, ke, kd, kL, kn = c
        charged = np.stack([kQ, ku, ke, kd, kL]); any_c = (np.abs(charged).sum(axis=0) + np.abs(kn)) > 0
        nonzero_pairs += int(any_c.sum())
        gs = (kQ == ku) & (ku == ke) & (ke == kd) & (kd == kL) & (kQ != 0); gen_shaped += int(gs.sum())
        af = (2 * kQ - ku - kd == 0) & (kQ - kL == 0) & (kQ - 2 * ku + kd == 0) & (kQ - 2 * ku + kd - kL + ke == 0) & (np.abs(charged).sum(axis=0) > 0)
        anomaly_free += int(af.sum())
        sc = np.abs(charged).sum(axis=0); j = int(sc.argmax())
        if sc[j] > best[0]: best = (int(sc[j]), (li, tuple(int(x) for x in E[A[j]]), tuple(int(x) for x in E[Bi[j]]), tuple(int(x[j]) for x in c)))
    print(f"  {name:11s} H1 = {H1:20s} N = {N:2d} p = {primes[0]:3d}: |Hom(H1, mu_N)| = {nH:5d}, non-split loci {nloci:4d} (spurious over single primes {spurious}; cusp-trivial {cusp_trivial}, chi^2 = 1 on the cusp {cusp_order2}); "
          f"doublet modules {nloci * nH:7d}, with I != 0: {len(nz):5d}; re-checked over {primes[1]}, {primes[2]}: {len(nz) + len(sample)} modules, differing {bad}; "
          f"SM pairs with a non-zero count {nonzero_pairs} of {nloci * nH * nH}; generation-shaped {gen_shaped}; anomaly-free non-zero {anomaly_free}; "
          f"largest pattern {best[1]}; {time.time() - t0:.0f} s", flush=True)
    summary[name] = dict(H1=H1, N=N, hom=nH, loci=nloci, spurious=spurious, cusp_trivial=cusp_trivial, cusp_order2=cusp_order2, nonzero=len(nz), rechecked=len(nz) + len(sample), differing=bad,
                         nonzero_pairs=nonzero_pairs, pairs=nloci * nH * nH, generation_shaped=gen_shaped, anomaly_free=anomaly_free, best=best)
json.dump(summary, open(os.path.join(HERE, 'torsion_complete.json'), 'w'), indent=1, default=str)
print("DONE")
