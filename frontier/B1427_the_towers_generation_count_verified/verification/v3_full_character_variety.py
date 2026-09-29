#!/usr/bin/env python3
"""COMPLETENESS + VACUITY, own code.  On Y_n the presentation has 3 generators and 2 relators, so for a
1-dimensional module psi the Fox Jacobian M(psi) is 2x3 and
        h^1 = (3 - rank M) - dim B^1,   dim B^1 = 0 if psi trivial else 1.
Hence h^1 >= 1  <=>  rank M <= 1  <=>  all three 2x2 minors vanish;  h^1 = 2  <=>  M = 0.
We solve BOTH conditions exactly over the WHOLE character torus Hom(H_1, C*) -- not only the finite group
Hom(H_1, mu_N) the record scans -- by writing the entries as Laurent polynomials in the free-part variable t
with coefficients in Q(zeta_e) (e = exponent of the torsion), and taking gcds."""
import sys, os, math, json, warnings, itertools
from fractions import Fraction
from collections import Counter
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import snappy
from cyclo import Cyc

# ---- Laurent polynomials over a Cyc field: dict exp -> field element ----
class LP:
    def __init__(s, F, d=None): s.F = F; s.d = {k: v for k, v in (d or {}).items() if not F.is_zero(v)}
    def __add__(s, o):
        r = dict(s.d)
        for k, v in o.d.items(): r[k] = s.F.add(r.get(k, s.F.zero()), v)
        return LP(s.F, r)
    def __sub__(s, o):
        r = dict(s.d)
        for k, v in o.d.items(): r[k] = s.F.sub(r.get(k, s.F.zero()), v)
        return LP(s.F, r)
    def __mul__(s, o):
        r = {}
        for k1, v1 in s.d.items():
            for k2, v2 in o.d.items():
                r[k1 + k2] = s.F.add(r.get(k1 + k2, s.F.zero()), s.F.mul(v1, v2))
        return LP(s.F, r)
    def is_zero(s): return not s.d
    def __repr__(s): return "LP(%d terms, exps %s)" % (len(s.d), sorted(s.d))

def const(F, c): return LP(F, {0: c})
def tvar(F, k=1): return LP(F, {k: F.one()})

# ---- univariate poly over Cyc as list (low first) ----
def to_poly(lp, F):
    if lp.is_zero(): return []
    lo = min(lp.d); hi = max(lp.d)
    p = [F.zero()] * (hi - lo + 1)
    for k, v in lp.d.items(): p[k - lo] = v
    while p and F.is_zero(p[-1]): p.pop()
    return p
def pdeg(p): return len(p) - 1
def pdivmod(a, b, F):
    a = list(a); q = [F.zero()] * max(0, len(a) - len(b) + 1)
    ib = F.inv(b[-1])
    while len(a) >= len(b) and any(not F.is_zero(x) for x in a):
        while a and F.is_zero(a[-1]): a.pop()
        if len(a) < len(b): break
        c = F.mul(a[-1], ib); d = len(a) - len(b); q[d] = c
        for i, bb in enumerate(b): a[d + i] = F.sub(a[d + i], F.mul(c, bb))
        while a and F.is_zero(a[-1]): a.pop()
    return q, a
def pgcd(a, b, F):
    a = [x for x in a]; b = [x for x in b]
    while a and F.is_zero(a[-1]): a.pop()
    while b and F.is_zero(b[-1]): b.pop()
    while b:
        _, r = pdivmod(a, b, F)
        while r and F.is_zero(r[-1]): r.pop()
        a, b = b, r
    if a:
        iv = F.inv(a[-1]); a = [F.mul(iv, x) for x in a]
    return a
def strip_t(p, F):
    """divide out the largest power of t (roots at t=0 are not characters)"""
    i = 0
    while i < len(p) and F.is_zero(p[i]): i += 1
    return p[i:]

def fox_LP(word, gens, val, ival, F):
    D = {g: LP(F) for g in gens}; pre = const(F, F.one())
    for ch in word:
        g = ch.lower()
        if ch.islower(): D[g] = D[g] + pre; pre = pre * val[g]
        else: pre = pre * ival[g]; D[g] = D[g] - pre
    return D

def abvec(word, gens):
    v = {g: 0 for g in gens}
    for ch in word: v[ch.lower()] += 1 if ch.islower() else -1
    return [v[g] for g in gens]

def analyse(n, e_tors, free_gen=None, verbose=True):
    """e_tors: exponent of the torsion of H_1 (values of torsion characters lie in mu_{e_tors})."""
    Y = snappy.Manifold('m004').covers(n, cover_type='cyclic')[0]
    G = Y.fundamental_group(); gens = list(G.generators()); rels = list(G.relators())
    mu, lam = G.peripheral_curves()[0]
    A = [abvec(r, gens) for r in rels]
    assert len(gens) == 3 and len(rels) == 2, (gens, rels)
    F = Cyc(e_tors)
    # the free generator: a column of A that is zero in every relator has an unconstrained character value
    zero_cols = [j for j in range(3) if all(a[j] == 0 for a in A)]
    if free_gen is None:
        assert len(zero_cols) == 1, ("no unique free column", A)
        free_gen = zero_cols[0]
    # torsion characters: values in mu_{e} on the other two generators, satisfying A k = 0
    others = [j for j in range(3) if j != free_gen]
    sols = []
    for ka in range(e_tors):
        for kc in range(e_tors):
            k = [0, 0, 0]; k[others[0]] = ka; k[others[1]] = kc
            if all(sum(a[j] * k[j] for j in range(3)) % e_tors == 0 for a in A): sols.append(tuple(k))
    out = dict(n=n, H1=str(Y.homology()), gens=gens, rels=rels, free_gen=gens[free_gen],
               e_torsion=e_tors, n_torsion_chars=len(sols))
    loci_deg = 0; h1_2_found = []; per_comp = []
    for k in sols:
        val = {}; ival = {}
        for j, g in enumerate(gens):
            if j == free_gen: val[g] = tvar(F, 1); ival[g] = tvar(F, -1)
            else: val[g] = const(F, F.zeta(k[j])); ival[g] = const(F, F.zeta(-k[j]))
        M = []
        for r in rels:
            D = fox_LP(r, gens, val, ival, F)
            M.append([D[g] for g in gens])
        entries = [to_poly(M[i][j], F) for i in range(2) for j in range(3)]
        minors = []
        for (j1, j2) in ((0, 1), (0, 2), (1, 2)):
            minors.append(to_poly(M[0][j1] * M[1][j2] - M[0][j2] * M[1][j1], F))
        g_min = []
        for p in minors:
            p = strip_t(p, F)
            g_min = p if not g_min else pgcd(g_min, p, F)
        g_ent = []
        for p in entries:
            p = strip_t(p, F)
            g_ent = p if not g_ent else pgcd(g_ent, p, F)
        dmin = pdeg(g_min) if g_min else -1     # -1 means all minors identically 0 -> whole component is a locus
        dent = pdeg(g_ent) if g_ent else -1
        per_comp.append(dict(k=list(k), deg_gcd_minors=dmin, deg_gcd_entries=dent))
        if dmin < 0: loci_deg = -1 if loci_deg >= 0 else loci_deg
        elif loci_deg >= 0: loci_deg += dmin
        if dent != 0: h1_2_found.append((list(k), dent))
    out['total_roots_of_minor_gcd_over_all_of_C*'] = loci_deg
    out['components_where_all_six_Fox_entries_share_a_root (h^1 = 2)'] = h1_2_found
    out['per_component'] = per_comp
    if verbose: print(json.dumps({kk: vv for kk, vv in out.items() if kk != 'per_component'}, indent=1), flush=True)
    return out

if __name__ == '__main__':
    res = {}
    for n, e in [(4, 15), (2, 5), (3, 4), (5, 11)]:
        print("=== Y_%d, torsion exponent %d ===" % (n, e))
        res[n] = analyse(n, e)
    json.dump(res, open('<here>/v3_full_character_variety.json', 'w'), indent=1, default=str)
