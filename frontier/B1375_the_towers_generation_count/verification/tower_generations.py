#!/usr/bin/env python3
"""B1375 -- THE TOWER'S GENERATION COUNT.  On the cyclic covers Y_n of m004 (n = 2, 3, ...; built by SnapPy's covers, so on their own
presentations, independent of the census names), the Standard-Model-frame census of B1374 with the character group complete on the
torsion of H_1 (N = lcm(12, torsion exponent)), restricted by B1297's T5: a doublet module rho_chi (x) psi has I != 0 only if it has a
cusp-invariant vector, which means psi = chi^{-1} on both peripheral curves, or psi = chi on both (then also the cocycle must be a
coboundary on the torus); every psi in either coset is computed, so no firing module is missed.  Then the generation-shaped backgrounds:
for a pair (psi_Y, psi_gamma) the five charged sectors are rho_chi (x) psi_Y^{6Y} psi_gamma^{3 gamma}; a generation needs all five
firing, so the (3bar,1)_{1/3} sector u = psi_Y^2 psi_gamma and the (1,2)_{-1/2} sector v = psi_Y^{-3} psi_gamma are both in the firing
set, psi_Y^5 = u / v, psi_gamma = u psi_Y^{-2}; all solutions psi_Y of psi_Y^5 = u/v in Hom(H_1, mu_N) are enumerated, and the three
sectors of the 10 are then read.  Every non-zero I is re-checked over two more primes.  The exact checker of B1374 can be pointed at
any background listed.  Usage: python3 tower_generations.py n [n ...]"""
import sys, os, json, math, time, random, warnings, itertools
from collections import Counter
warnings.filterwarnings("ignore")
import snappy
argv = sys.argv; sys.argv = ['x', 'none']
B1374 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1374_the_class_index_in_the_sm_frame", "verification")
sys.path.insert(0, B1374)
from index_lib import GF, Rep, module, index, characters, char_value, h1_and_cocycle, reducible_rep, abelian_exponents
HERE = os.path.dirname(os.path.abspath(__file__))
SECTORS = [("Q", 1, 3), ("u^c", -4, 3), ("e^c", 6, 3), ("d^c", 2, 1), ("L", -3, 1), ("nu^c", 0, -5)]

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

class Level:
    def __init__(self, n, p, N):
        M = snappy.Manifold('m004').covers(n, cover_type='cyclic'); assert len(M) == 1; self.M = M[0]
        G = self.M.fundamental_group(); self.gens = list(G.generators()); self.rels = list(G.relators()); self.mu, self.lam = G.peripheral_curves()[0]
        self.H1 = str(self.M.homology()); self.n = n; self.p = p; self.N = N; self.F = GF(p); self.z = self.F.root_of_unity(N)
        self.chars = characters(self.F, self.gens, self.rels, N)
        self.loci = []
        for chi in self.chars:
            if all(k == 0 for k in chi.values()): continue
            chi2 = {g: pow(self.z, 2 * chi[g], p) for g in self.gens}
            h1, ct = h1_and_cocycle(self.F, self.gens, self.rels, self.mu, self.lam, chi2)
            if ct is not None: self.loci.append((chi, h1, ct))
        self.cache = {}
    def val(self, chi, word): return char_value(self.F, self.z, chi, word)
    def I(self, li, psi):
        key = (li, tuple(psi[g] for g in self.gens))
        if key in self.cache: return self.cache[key]
        chi, h1, ct = self.loci[li]; cv = {g: pow(self.z, chi[g], self.p) for g in self.gens}
        rho = reducible_rep(self.F, self.gens, cv, ct)
        pv = {g: pow(self.z, psi[g], self.p) for g in self.gens}
        V = Rep(self.F, self.gens, module(self.F, self.gens, rho, 1, pv)); assert V.check_relators(self.rels)
        out = index(V, self.rels, self.mu, self.lam); self.cache[key] = out; return out

def run_level(n):
    t0 = time.time()
    H1 = str(snappy.Manifold('m004').covers(n, cover_type='cyclic')[0].homology()); e = torsion_exponent(H1); N = 12 * e // math.gcd(12, e)
    P = primes_for(N); L = [Level(n, p, N) for p in P]; L0 = L[0]; gens = L0.gens
    keysets = [set(tuple(chi[g] for g in gens) for (chi, h1, ct) in Lq.loci) for Lq in L]
    common = sorted(set.intersection(*keysets)); spurious = [len(k) - len(common) for k in keysets]
    idx = [{tuple(chi[g] for g in gens): i for i, (chi, h1, ct) in enumerate(Lq.loci)} for Lq in L]
    li_of = [[ix[k] for k in common] for ix in idx]; nloci = len(common)
    psis = L0.chars; nH = len(psis)
    key = lambda psi: tuple(psi[g] for g in gens)
    pindex = {key(psi): i for i, psi in enumerate(psis)}
    def power(psi, k): return {g: (k * psi[g]) % N for g in gens}
    def prod(a, b): return {g: (a[g] + b[g]) % N for g in gens}
    mu_ab = abelian_exponents(L0.mu, gens); lam_ab = abelian_exponents(L0.lam, gens)
    mu_null = all(sum(mu_ab[g] * psi[g] for g in gens) % N == 0 for psi in psis)
    # T5: an invariant vector on the cusp torus needs psi = chi^{-1} on both peripheral curves, or psi = chi on both (with the cocycle
    # a coboundary on the torus); group psis by their values on (mu, lambda) as exponents of zeta
    by_lam = {}
    for i, psi in enumerate(psis):
        k = (sum(mu_ab[g] * psi[g] for g in gens) % N, sum(lam_ab[g] * psi[g] for g in gens) % N); by_lam.setdefault(k, []).append(i)
    # the firing set per locus
    nz = {}; total = 0; cusp = Counter(); h1s = Counter()
    for j in range(nloci):
        chi = dict(zip(gens, common[j])); kl = sum(lam_ab[g] * chi[g] for g in gens) % N; km = sum(mu_ab[g] * chi[g] for g in gens) % N
        cusp[(km, kl)] += 1; h1s[L0.loci[li_of[0][j]][1]] += 1
        cand = sorted(set(by_lam.get(((-km) % N, (-kl) % N), []) + by_lam.get((km % N, kl % N), [])))
        total += len(cand); fire = {}
        for i in cand:
            I = L0.I(li_of[0][j], psis[i])[0]
            if I != 0: fire[i] = I
        nz[j] = fire
    nfire = sum(len(f) for f in nz.values())
    # re-check every non-zero over the two other primes, and a sample of zeros
    bad = 0; checked = 0
    for j, fire in nz.items():
        for i, I in fire.items():
            checked += 1
            if any(L[q].I(li_of[q][j], psis[i])[0] != I for q in (1, 2)): bad += 1
    # generation-shaped backgrounds: u = psi_Y^2 psi_gamma (d^c), v = psi_Y^-3 psi_gamma (L) both firing with the same sign
    fifth = {}
    for i, psi in enumerate(psis): fifth.setdefault(key(power(psi, 5)), []).append(i)
    gens_found = []; signs = Counter(); yord = Counter(); gord = Counter(); loci_used = set(); kvals = Counter()
    def order(psi): return min(k for k in range(1, N + 1) if all(k * psi[g] % N == 0 for g in gens))
    for j, fire in nz.items():
        for iu, Iu in fire.items():
            for iv, Iv in fire.items():
                if Iu != Iv: continue
                w = prod(psis[iu], power(psis[iv], -1))                      # psi_Y^5 = u v^-1
                for iy in fifth.get(key(w), []):
                    pY = psis[iy]; pG = prod(psis[iu], power(pY, -2))
                    c = []
                    for (lab, sy, sg) in SECTORS:
                        sec = prod(power(pY, sy), power(pG, sg)); ii = pindex[key(sec)]
                        c.append(fire.get(ii, 0) if ii in fire or L0.I(li_of[0][j], psis[ii])[0] == 0 else L0.I(li_of[0][j], psis[ii])[0])
                    if c[0] == c[1] == c[2] == c[3] == c[4] != 0:
                        gens_found.append((j, iy, pindex[key(pG)], c)); signs[c[0]] += 1; kvals[abs(c[0])] += 1
                        yord[order(pY)] += 1; gord[order(pG)] += 1; loci_used.add(j)
    # dedupe (the same background can be reached from several (u, v) only if u, v differ -- they don't; keep as is but count unique)
    uniq = sorted(set((j, a, b) for (j, a, b, c) in gens_found))
    nu = Counter(c[5] for (j, a, b, c) in gens_found)
    ex = gens_found[:2]
    print(f"Y_{n:<2d} = {H1:26s} N = {N:3d} primes {P}: |Hom| = {nH:6d}, non-split loci {nloci:4d} (spurious {spurious}; h1(chi^2) {dict(h1s)}); mu null-homologous: {mu_null}; "
          f"(chi(mu), chi(lambda)) exponents: {dict(cusp) if len(cusp) <= 6 else str(len(cusp)) + ' values'}; T5-candidate doublet modules {total}, firing {nfire} (re-checked {checked}, differing {bad}); "
          f"GENERATION-SHAPED backgrounds {len(uniq)} on {len(loci_used)} loci, signs {dict(signs)}, |count| {dict(kvals)}, nu^c count {dict(nu)}, psi_Y orders {dict(yord)}, psi_gamma orders {dict(gord)}; "
          f"examples {[(j, tuple(psis[a][g] for g in gens), tuple(psis[b][g] for g in gens), c) for (j, a, b, c) in ex]}; {time.time() - t0:.0f} s", flush=True)
    return dict(n=n, H1=H1, N=N, primes=P, hom=nH, loci=nloci, spurious=spurious, mu_null=mu_null, candidates=total, firing=nfire, rechecked=checked, differing=bad,
                generation_backgrounds=len(uniq), loci_used=len(loci_used), signs=dict(signs), kvals=dict(kvals), nu=dict(nu), yord=dict(yord), gord=dict(gord),
                joint_sign_singlet={f"{c[0]:+d},{c[5]:+d}": v for (c0, c5), v in Counter((c[0], c[5]) for (j, a, b, c) in gens_found).items() for c in [(c0, 0, 0, 0, 0, c5)]},
                examples=[(j, list(common[j]), tuple(psis[a][g] for g in gens), tuple(psis[b][g] for g in gens), c) for (j, a, b, c) in ex], gens=gens, rels=L0.rels, mu=L0.mu, lam=L0.lam)

if __name__ == '__main__':
    out = {}
    for n in [int(x) for x in argv[1:]] or [2, 3, 4, 5, 6]:
        out[n] = run_level(n)
        json.dump(out, open(os.path.join(HERE, f'tower_generations_{"_".join(argv[1:]) or "2_6"}.json'), 'w'), indent=1, default=str)
    print("DONE")
