#!/usr/bin/env python3
"""B1374 -- THE CLASS'S INDEX IN THE STANDARD-MODEL FRAME.  Main's B1418 computed the one-cusped index I = n(V) - n(V*) (B1297) on
reducible non-split modules Sym^m(rho_chi) (x) psi of thirteen one-cusped members of the family and two covers of m004, exactly over
Q(zeta_12) (and Q(phi), Q(phi, zeta_12) for m004), and found I = +-1 (t12835: +-2) on six members.  This script
  (A) recomputes every module main ran, with this seat's own code (index_lib.py) over three prime fields, and compares I and the
      four dimensions (a0, a1, t0, r1) of V and V* module by module;
  (B) computes the index of every rank-one module (m = 0) at every locus: the spin-0 sectors of the Standard-Model frame;
  (C) tabulates I(Sym^m(rho_chi) (x) psi) for every non-split locus chi (values in mu_12), every psi in Hom(H_1, mu_12), m in {0,1,2},
      and reads the table in the Standard-Model frame: the E_6 sectors of a flat connection with holonomy in c(SM) = SL(2)_beta x C*^2
      (B1368) are (spin under SL(2)_beta) (x) chi_w with chi_w = psi_Y^{6Y(w)} psi_gamma^{3 gamma(w)}; the net number of copies of an
      SM representation R is I of its sector module; the doublet sectors are the 78's 20 = 10 + 10bar (Q, u^c, e^c; gamma = 1) and the
      27's 6bar = 5bar + 5bar' + 1 + 1' (d^c-type, L-type, nu^c-type; gamma = 1/3, -5/3); the spin-0 sectors are the 27's 10 and 5 and
      the 78's 35 (B1372's spin split).  For every pair (psi_Y, psi_gamma) the six net counts are read off and the generation-shaped
      pattern (all five charged counts equal and non-zero) and the anomaly sums are tested.
Usage: python3 class_index_sm_frame.py [A|BC|all] [members...]  (all, every member: about eight minutes; the lock runs a subset)"""
import sys, os, json, cmath, math, time, itertools, warnings
warnings.filterwarnings("ignore")
import snappy
from index_lib import *

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES = (61, 181, 241)                      # p = 1 mod 60: GF(p) contains zeta_12 and sqrt(5)
MEMBERS = ['s958', 'v2873', 't12833', 'o10_150697', 'o10_150700', 'o10_150701', 't12837', 's956', 't11365', 't12835', 'm208', 's961', 't12839']
FIRING = ['s958', 'v2873', 't12833', 't12835', 'o10_150701', 't12839']
what = sys.argv[1] if len(sys.argv) > 1 else 'all'

def presentation(name):
    M = snappy.Manifold(name); G = M.fundamental_group()
    mu, lam = G.peripheral_curves()[0]
    return list(G.generators()), list(G.relators()), mu, lam, str(M.homology())

class Bench:
    """one member over one prime: characters into mu_12, the non-split loci, module indices with caching"""
    def __init__(self, name, p, N=12):
        self.name = name; self.p = p; self.N = N; self.F = GF(p); self.z = self.F.root_of_unity(N)
        self.gens, self.rels, self.mu, self.lam, self.H1 = presentation(name)
        self.chars = characters(self.F, self.gens, self.rels, N)          # dicts gen -> exponent
        self.loci = []                                                    # (chi exponents, h1, cocycle)
        for chi in self.chars:
            if all(k == 0 for k in chi.values()): continue
            chi2 = {g: pow(self.z, 2 * chi[g], p) for g in self.gens}
            h1, ct = h1_and_cocycle(self.F, self.gens, self.rels, self.mu, self.lam, chi2)
            if ct is not None: self.loci.append((chi, h1, ct))
        self.cache = {}
    def chi_values(self, chi): return {g: pow(self.z, chi[g], self.p) for g in self.gens}
    def rho(self, chi, ct):
        r = reducible_rep(self.F, self.gens, self.chi_values(chi), ct)
        assert Rep(self.F, self.gens, r).check_relators(self.rels), "rho_chi is not a representation"
        return r
    def I(self, li, m, psi, semisimple=False):
        """psi: dict gen -> exponent of zeta_N"""
        key = (li, m, tuple(psi[g] for g in self.gens), semisimple)
        if key in self.cache: return self.cache[key]
        chi, h1, ct = self.loci[li]; cv = self.chi_values(chi)
        base = {g: [[cv[g], 0], [0, self.F.inv(cv[g])]] for g in self.gens} if semisimple else self.rho(chi, ct)
        pv = {g: pow(self.z, psi[g], self.p) for g in self.gens}
        V = Rep(self.F, self.gens, module(self.F, self.gens, base, m, pv))
        assert V.check_relators(self.rels), "module is not a representation"
        out = index(V, self.rels, self.mu, self.lam)
        self.cache[key] = out; return out

# ---------------------------------------------------------------- decoding main's labels
def decode_zeta12(tup, theta=None):
    """a tuple of rationals = coordinates in 1, z, z^2, z^3 (z = zeta_12) -> exponent k with value = z^k, or None"""
    from fractions import Fraction as Fr
    if theta is None:
        z = cmath.exp(1j * math.pi / 6); val = sum(float(Fr(c)) * z ** i for i, c in enumerate(tup))
    else:
        val = sum(float(Fr(c)) * theta ** i for i, c in enumerate(tup))
    for k in range(12):
        if abs(val - cmath.exp(1j * math.pi * k / 6)) < 1e-9: return k, None
    return None, val
def parse_label(lab):
    """'chi#0=a:('1','0','0','0'),b:(...) h1=1' -> dict gen -> tuple of strings, h1"""
    body = lab.split('=', 1)[1]; h1 = None
    if ' h1=' in body: body, h = body.split(' h1='); h1 = int(h)
    out = {}
    for part in body.split('),'):
        part = part.strip()
        if not part: continue
        g, t = part.split(':(', 1); t = t.rstrip(')')
        out[g.strip()] = tuple(x.strip().strip("'") for x in t.split(','))
    return out, h1

# ================================================================ (A) module-by-module comparison with main's record
def cell_A(only=None):
    print("=== (A) main's B1418 cell 2 recomputed with own code over GF(61), GF(181), GF(241): every module main ran ===")
    rec = json.load(open(os.path.join(HERE, 'b1418_c2_modules_compact.json')))
    tot = agree = 0; dis = []; drops = 0; per_member = {}
    for name, rows in rec.items():
        if only and name not in only: continue
        run = [r for r in rows if r['status'] == 'RUN']
        if not run: continue
        benches = {p: Bench(name, p) for p in PRIMES}
        gens = benches[PRIMES[0]].gens
        # the golden field for m004: theta = phi + zeta_12 (compositum) or phi alone (degree 2)
        theta = None; golden = (name == 'm004')
        if golden:
            deg = len(parse_label(run[0]['locus'])[0][gens[0]])
            phi = (1 + 5 ** 0.5) / 2
            theta = phi + cmath.exp(1j * math.pi / 6) if deg == 8 else phi
        ok = bad = 0; mism = []
        # map main's loci to mine: by chi exponents
        for r in run:
            chi_t, h1_main = parse_label(r['locus']); psi_lab = r['twist']; m = r['m']
            # chi
            chi = {}; failed = False; gold = {}
            for g in gens:
                if golden:
                    from fractions import Fraction as Fr
                    val = sum(float(Fr(c)) * theta ** i for i, c in enumerate(chi_t[g]))
                    gold[g] = val; continue
                k, _ = decode_zeta12(chi_t[g]); 
                if k is None: failed = True; break
                chi[g] = k
            if failed: mism.append(('undecodable chi', r['locus'][:60])); continue
            if golden:
                # chi(g) = zeta_12^k * phi^e (e in {-1, 0, 1}); over GF(p) use sqrt(5)
                dec = {}
                for g in gens:
                    v = gold[g]; found = None
                    for k in range(12):
                        for e in (-1, 0, 1):
                            if abs(v - cmath.exp(1j * math.pi * k / 6) * ((1 + 5 ** 0.5) / 2) ** e) < 1e-7: found = (k, e)
                    if found is None: failed = True; break
                    dec[g] = found
                if failed: mism.append(('undecodable golden chi', r['locus'][:60])); continue
            # psi
            if psi_lab.startswith('psi=chi^'):
                j = int(psi_lab.split('^')[1]); psi_mode = ('chi', j)
            else:
                pt, _ = parse_label(psi_lab); psi = {}
                for g in gens:
                    if golden:
                        from fractions import Fraction as Fr
                        v = sum(float(Fr(c)) * theta ** i for i, c in enumerate(pt[g])); found = None
                        for k in range(12):
                            if abs(v - cmath.exp(1j * math.pi * k / 6)) < 1e-7: found = k
                        if found is None: failed = True; break
                        psi[g] = found
                    else:
                        k, _ = decode_zeta12(pt[g])
                        if k is None: failed = True; break
                        psi[g] = k
                if failed: mism.append(('undecodable psi', psi_lab[:60])); continue
                psi_mode = ('psi', psi)
            # compute over the three primes
            results = []
            for p, B in benches.items():
                if golden:
                    F = B.F; s5 = F.sqrt(5); phi_p = (1 + s5) * F.inv(2) % p
                    cv = {g: pow(B.z, dec[g][0], p) * (pow(phi_p, dec[g][1], p) if dec[g][1] >= 0 else F.inv(phi_p)) % p for g in gens}
                    chi2 = {g: cv[g] * cv[g] % p for g in gens}
                    h1, ct = h1_and_cocycle(F, gens, B.rels, B.mu, B.lam, chi2)
                    if ct is None: results.append(('no locus', h1)); continue
                    rho = reducible_rep(F, gens, cv, ct); assert Rep(F, gens, rho).check_relators(B.rels)
                    if psi_mode[0] == 'chi': pv = {g: pow(cv[g], psi_mode[1], p) for g in gens}
                    else: pv = {g: pow(B.z, psi_mode[1][g], p) for g in gens}
                    V = Rep(F, gens, module(F, gens, rho, m, pv)); assert V.check_relators(B.rels)
                    results.append((index(V, B.rels, B.mu, B.lam), h1))
                else:
                    li = next((i for i, (c, h, ct) in enumerate(B.loci) if all(c[g] == chi[g] for g in gens)), None)
                    if li is None: results.append(('no locus', None)); continue
                    if psi_mode[0] == 'chi': psi = {g: (psi_mode[1] * chi[g]) % 12 for g in gens}
                    else: psi = psi_mode[1]
                    results.append((B.I(li, m, psi), B.loci[li][1]))
            tot += 1
            Is = [x[0][0] if x[0] != 'no locus' else None for x in results]
            dims = [(x[0][1], x[0][2]) if x[0] != 'no locus' else None for x in results]
            h1s = [x[1] for x in results]
            mainV = tuple(r['V']); mainVd = tuple(r['V*'])
            exact = [d is not None and d[0] == mainV and d[1] == mainVd for d in dims]
            if all(i == r['I'] for i in Is) and all(exact) and all(h == h1_main for h in h1s): ok += 1; agree += 1
            else:
                # a rank drop on one prime shows as a difference on that prime only
                if any(i == r['I'] and e for i, e in zip(Is, exact)) : drops += 1
                bad += 1; mism.append((r['locus'][:50], psi_lab[:40], m, 'main I', r['I'], 'ours', Is, 'main dims', mainV, mainVd, 'ours', dims, 'h1', h1_main, h1s))
        per_member[name] = (len(run), ok, bad)
        print(f"  {name:11s} H1 = {benches[PRIMES[0]].H1:22s} loci (ours, mu_12) {len(benches[PRIMES[0]].loci):3d}: modules compared {len(run):5d}, identical on all three primes {ok:5d}, differing {bad}")
        for x in mism[:6]: print("     differs:", x)
        dis += mism
    print(f"\n  TOTAL modules compared: {tot}; I and all four dimensions of V and V* identical over the three primes: {agree}; differing: {len(dis)} (of which agreeing on at least one prime: {drops})")
    return per_member

# ================================================================ (B), (C): the SM-frame census
SM_SECTORS = [  # name, 6Y, 3gamma, source
    ('Q      (3,2)_{1/6}   78:10', 1, 3), ('u^c    (3b,1)_{-2/3} 78:10', -4, 3), ('e^c    (1,1)_{1}     78:10', 6, 3),
    ("d^c-type (3b,1)_{1/3} 27:5b", 2, 1), ("L-type (1,2)_{-1/2}  27:5b", -3, 1), ("nu^c-type (1,1)_0    27:1", 0, -5)]
def cell_BC(names):
    print("\n=== (B) the rank-one modules (m = 0): the spin-0 sectors of the Standard-Model frame ===")
    print("=== (C) I(Sym^m(rho_chi) (x) psi) for every non-split locus, every psi in Hom(H_1, mu_12), m in {0, 1, 2}; then the SM-frame table ===")
    summary = {}
    for name in names:
        t0 = time.time()
        B = {p: Bench(name, p) for p in PRIMES}; B0 = B[PRIMES[0]]; gens = B0.gens
        psis = B0.chars                      # Hom(H_1, mu_12) as exponent dicts
        nloci = len(B0.loci); assert all(len(B[p].loci) == nloci for p in PRIMES)
        table = {}                           # (li, m, psi_key) -> I (agreed over primes) or 'X' (disagreement)
        m0_nonzero = 0; m0_total = 0; disagree = 0; fired = {1: 0, 2: 0}
        for li in range(nloci):
            for m in (0, 1, 2):
                for psi in psis:
                    key = tuple(psi[g] for g in gens)
                    vals = [B[p].I(li, m, psi)[0] for p in PRIMES]
                    if len(set(vals)) != 1: table[(li, m, key)] = 'X'; disagree += 1; continue
                    table[(li, m, key)] = vals[0]
                    if m == 0: m0_total += 1; m0_nonzero += (vals[0] != 0)
                    elif vals[0] != 0: fired[m] += 1
        # the SM frame: pairs (psi_Y, psi_gamma); sector characters psi_Y^{6Y} psi_gamma^{3 gamma}
        def power(psi, k): return {g: (k * psi[g]) % 12 for g in gens}
        def prod(a, b): return {g: (a[g] + b[g]) % 12 for g in gens}
        best = None; gen_shaped = []; nonzero_pairs = 0; anomaly_free_nonzero = []
        for li in range(nloci):
            for pY in psis:
                for pG in psis:
                    counts = []
                    for (lab, sy, sg) in SM_SECTORS:
                        sec = prod(power(pY, sy), power(pG, sg)); key = tuple(sec[g] for g in gens)
                        counts.append(table[(li, 1, key)])
                    if any(c == 'X' for c in counts): continue
                    kQ, ku, ke, kd, kL, kn = counts
                    if any(counts): nonzero_pairs += 1
                    charged = (kQ, ku, ke, kd, kL)
                    if len(set(charged)) == 1 and kQ != 0: gen_shaped.append((li, tuple(pY[g] for g in gens), tuple(pG[g] for g in gens), counts))
                    A3 = 2 * kQ - ku - kd; A2 = kQ - kL; A31 = kQ - 2 * ku + kd; AY = kQ - 2 * ku + kd - kL + ke   # SU(3)^3, SU(2)^2 U(1), SU(3)^2 U(1) (x3), grav-U(1)
                    if any(charged) and A3 == 0 and A2 == 0 and A31 == 0 and AY == 0: anomaly_free_nonzero.append((li, counts))
                    score = sum(abs(c) for c in charged)
                    if best is None or score > best[0]: best = (score, li, tuple(pY[g] for g in gens), tuple(pG[g] for g in gens), counts)
        cusp_trivial = sum(1 for (chi, h1, ct) in B0.loci if char_value(B0.F, B0.z, chi, B0.mu) == 1 and char_value(B0.F, B0.z, chi, B0.lam) == 1)
        print(f"  {name:11s} H1 = {B0.H1:22s} |Hom(H1, mu_12)| = {len(psis):4d}, non-split loci in mu_12: {nloci:3d} (cusp-trivial {cusp_trivial}); "
              f"m = 0 modules {m0_total} with I != 0: {m0_nonzero}; doublet modules (m = 1) with I != 0: {fired[1]}; adjoint (m = 2) with I != 0: {fired[2]}; "
              f"prime disagreements {disagree}; {time.time() - t0:.0f} s")
        print(f"      SM frame: pairs (psi_Y, psi_gamma) with some net count non-zero: {nonzero_pairs} of {nloci * len(psis) ** 2}; generation-shaped (Q = u^c = e^c = d^c = L != 0): {len(gen_shaped)}; "
              f"anomaly-free with a non-zero charged count: {len(anomaly_free_nonzero)}")
        print(f"      largest |net| pattern: locus {best[1]} psi_Y = {best[2]} psi_gamma = {best[3]} -> (Q, u^c, e^c, d^c, L, nu^c) = {tuple(best[4])}")
        for x in anomaly_free_nonzero[:5]: print("      anomaly-free non-zero:", x)
        for x in gen_shaped[:5]: print("      GENERATION-SHAPED:", x)
        summary[name] = dict(H1=B0.H1, loci=nloci, cusp_trivial_loci=cusp_trivial, m0_total=m0_total, m0_nonzero=m0_nonzero, m1_nonzero=fired[1], m2_nonzero=fired[2],
                             nonzero_pairs=nonzero_pairs, pairs=nloci * len(psis) ** 2, generation_shaped=len(gen_shaped), anomaly_free_nonzero=len(anomaly_free_nonzero), best=best, disagreements=disagree)
    return summary

if __name__ == '__main__' and what != 'none':
    out = {}
    names = sys.argv[2:] if len(sys.argv) > 2 else None
    if what in ('A', 'all'): out['A'] = cell_A(names)
    if what in ('B', 'C', 'BC', 'all'): out['BC'] = cell_BC(names or MEMBERS)
    json.dump(out, open(os.path.join(HERE, f'class_index_sm_frame_{what}.json'), 'w'), indent=1, default=str)
    print("DONE")
