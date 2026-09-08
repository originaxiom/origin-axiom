#!/usr/bin/env python3
"""THE ONE-TRIPLET VACUA (B1302, L210(ii)): on Y_12's Standard-Model Wilson lines -- where the colour triplet D survives
in one generation only (B1301) -- does a tree-level vacuum branch of the one-coupling E8 theory leave NO light exotic
colour triplet while keeping a light Higgs pair?  On Y_9 (B1283, B1300) every maximal branch leaves generation g's light
Higgs pair together with generation g's light D pair, because the tree-level VEVs (<N_g>, <nu^c_g>, the flavons S_hk,
S_kh) never touch generation g's 27 and the Wilson line keeps D_g.  On Y_12 a line may keep D only in generation g0 != g.

(a) THE SURVIVAL PATTERNS.  From Y_12's support file (B1301) every SM line's survival bits -- eleven multiplets x three
    generations -- are recorded and the distinct patterns counted (the 27bars mirror the 27s: a mirror component survives
    iff its partner does, h^1(psi^-1) = h^1(psi)).  Y_9's patterns are the control.
(b) THE TREE-LEVEL MASS MATRICES.  On a pattern, the D- and F-flat VEV configurations of the SM-singlet sector are the
    unions of conjugate pairs {N_g, Nbar_g}, {nu^c_g, nubar^c_g}, {S_hk, S_kh} allowed by the squarefree-cubic F-flat rule
    (B1283: at most one N generation, at most one nu^c generation, at most one flavon pair, and a flavon pair {hk} only
    with generation g = the third one's N and nu^c) whose fields exist on the line.  For each configuration the holomorphic
    mass matrices of the colour-triplet sector ((3, -1/3) x (3bar, +1/3): D, the mirrors of d^c and Dbar; against d^c,
    Dbar, the mirror of D), the doublet sector ((2, +1/2) x (2, -1/2): H_u, the mirrors of L and H_d; against L, H_d, the
    mirror of H_u), and the flavon-only sectors (Q, u^c, e^c against their mirrors) are built from the cubic's terms that
    contain a VEV'd field -- N_i H_u,j H_d,k and N_i D_j Dbar_k, nu^c_i L_j H_u,k and nu^c_i d^c_j D_k with the family
    tensor |eps_ijk|, the mirror cubic with the conjugate VEVs, and the flavon couplings S_ij 27_j . 27bar_i pairing every
    component with its mirror -- with independent symbolic VEVs and couplings; the generic rank is computed exactly at
    random rational points (twice).  Light pairs in a sector = dimension - rank.
(c) THE CENSUS.  For every (pattern, configuration): the light colour-triplet pairs n_T (the light generation's own
    d^c pair counts as 1), the light doublet pairs n_H (its L, H_u, H_d pairs count as 3), and the flavon-only sectors.
    The question: is there a (pattern, configuration) with n_T = 1 and a light Higgs pair -- no light exotic triplet --
    and how many of Y_12's 34 752 lines admit one?  On Y_9 the answer must be no (n_T >= 2 on every branch, B1283/B1300).
"""
from __future__ import annotations
import sys, json, time, pathlib, collections, itertools, random
from fractions import Fraction
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1301 = ROOT / 'frontier' / 'B1301_the_towers_alphabet' / 'verification'
sys.path.insert(0, str(B1301))
import lines_from_support as LS

LABELS = LS.LABELS
G3 = (0, 1, 2)
OTHER = {g: tuple(h for h in G3 if h != g) for g in G3}


# ------------------------------------------------------------------------------------------------ (a) the patterns
def patterns(support_path, n):
    """Counter of survival patterns over the SM lines of the closing: pattern = tuple over LABELS of 3 bits."""
    L = LS.load_level(support_path, n)
    K3, K2, dist = LS.alphabet(L)
    H, chi = L['H'], L['chi']
    K = len(K3)
    iu, il = np.meshgrid(np.arange(K), np.arange(K), indexing='ij')
    u_all, l_all = K3[iu.ravel()], K3[il.ravel()]
    pat = collections.Counter()
    for iq in range(K):
        q = K3[iq][None, :]
        bits = {}
        for lab in LABELS:
            a, b, c = LS.QUL[lab]
            x = a * q + b * u_all + c * l_all
            bits[lab] = np.stack([H[LS.keys(x + chi[g], L)] for g in G3], axis=1)      # (T, 3)
        tot = {lab: bits[lab].sum(axis=1) for lab in LABELS}
        three = (tot['d^c'] == 3) & (tot['e^c'] == 3)
        same = lambda A, B: (LS.keys(LS.QUL[A][0] * q + LS.QUL[A][1] * u_all + LS.QUL[A][2] * l_all, L)
                             == LS.keys(LS.QUL[B][0] * q + LS.QUL[B][1] * u_all + LS.QUL[B][2] * l_all, L))
        broken = ~(same('Q', 'u^c') & same('u^c', 'e^c'))
        vac = (tot['S'] >= 1) & (tot['nu^c'] >= 1) & (tot['H_u'] >= 1) & (tot['H_d'] >= 1)
        sm = three & broken & vac
        idx = np.where(sm)[0]
        if len(idx) == 0:
            continue
        stack = np.concatenate([bits[lab][idx] for lab in LABELS], axis=1)             # (T_sm, 33)
        for row in map(tuple, stack.tolist()):
            pat[tuple(tuple(row[3 * i:3 * i + 3]) for i in range(len(LABELS)))] += 1
    return pat, K


# ------------------------------------------------------------------------------------------------ (b) the mass matrices
def configurations(s):
    """D&F-flat VEV configurations available on a pattern s (dict label -> 3 bits): (gN, gnu, S-pair) with None allowed."""
    out = []
    for gN in (None,) + G3:
        if gN is not None and not s['S'][gN]:
            continue
        for gnu in (None,) + G3:
            if gnu is not None and not s['nu^c'][gnu]:
                continue
            for Sp in (None,) + G3:                    # S-pair {h, k} labelled by the third generation g = Sp
                if Sp is not None:
                    if gN not in (None, Sp) or gnu not in (None, Sp):
                        continue
                if gN is None and gnu is None and Sp is None:
                    continue
                out.append((gN, gnu, Sp))
    return out


def sector_matrices(s, cfg, vals):
    """The holomorphic mass matrices (rows: charge q fields; cols: charge -q fields) for the sectors, at numeric VEVs/couplings."""
    gN, gnu, Sp = cfg
    n = {g: (vals['n'][g] if g == gN else 0) for g in G3}; nb = {g: (vals['nb'][g] if g == gN else 0) for g in G3}
    v = {g: (vals['v'][g] if g == gnu else 0) for g in G3}; vb = {g: (vals['vb'][g] if g == gnu else 0) for g in G3}
    S = {(i, j): 0 for i in G3 for j in G3 if i != j}
    if Sp is not None:
        h, k = OTHER[Sp]
        S[(h, k)] = vals['s'][(h, k)]; S[(k, h)] = vals['s'][(k, h)]
    lam = vals['lam']
    ex = lambda lab, g: bool(s[lab[2:] if lab.startswith('m:') else lab][g])      # a mirror exists iff its partner does

    def build(rows, cols, terms):
        R = [f for f in rows if ex(f[0], f[1])]; Cc = [f for f in cols if ex(f[0], f[1])]
        ri = {f: i for i, f in enumerate(R)}; ci = {f: i for i, f in enumerate(Cc)}
        M = [[Fraction(0)] * len(Cc) for _ in R]
        for (r, c, val) in terms:
            if r in ri and c in ci and val != 0:
                M[ri[r]][ci[c]] += val
        return M, R, Cc
    # mirrors are labelled ('m:' + label, g): the mirror of component X of 27_g sits in 27bar_g with conjugate charge
    T_rows = [('D', g) for g in G3] + [('m:d^c', g) for g in G3] + [('m:Dbar', g) for g in G3]
    T_cols = [('d^c', g) for g in G3] + [('Dbar', g) for g in G3] + [('m:D', g) for g in G3]
    H_rows = [('H_u', g) for g in G3] + [('m:L', g) for g in G3] + [('m:H_d', g) for g in G3]
    H_cols = [('L', g) for g in G3] + [('H_d', g) for g in G3] + [('m:H_u', g) for g in G3]
    T, Hm = [], []
    for i in G3:
        j, k = OTHER[i]
        for (a, b) in ((j, k), (k, j)):
            T.append((('D', a), ('Dbar', b), lam['ND'] * n[i]))                      # N_i D_j Dbar_k
            T.append((('m:Dbar', b), ('m:D', a), lam['ND'] * nb[i]))                 # Nbar_i (mirror D)_j (mirror Dbar)_k
            T.append((('D', b), ('d^c', a), lam['nuD'] * v[i]))                       # nu^c_i d^c_j D_k
            T.append((('m:d^c', a), ('m:D', b), lam['nuD'] * vb[i]))                  # nubar^c_i (mirror d^c)_j (mirror D)_k
            Hm.append((('H_u', a), ('H_d', b), lam['NH'] * n[i]))                     # N_i H_u,j H_d,k
            Hm.append((('m:H_d', b), ('m:H_u', a), lam['NH'] * nb[i]))
            Hm.append((('H_u', b), ('L', a), lam['nuH'] * v[i]))                      # nu^c_i L_j H_u,k
            Hm.append((('m:L', a), ('m:H_u', b), lam['nuH'] * vb[i]))
    for (i, j), sij in S.items():                                                    # S_ij 27_j . 27bar_i
        T += [(('D', j), ('m:D', i), sij), (('m:Dbar', i), ('Dbar', j), sij), (('m:d^c', i), ('d^c', j), sij)]
        Hm += [(('H_u', j), ('m:H_u', i), sij), (('m:H_d', i), ('H_d', j), sij), (('m:L', i), ('L', j), sij)]
    mats = {'T': build(T_rows, T_cols, T), 'H': build(H_rows, H_cols, Hm)}
    for lab in ('Q', 'u^c', 'e^c'):
        rows = [(lab, g) for g in G3]; cols = [('m:' + lab, g) for g in G3]
        terms = [((lab, j), ('m:' + lab, i), sij) for (i, j), sij in S.items()]
        mats[lab] = build(rows, cols, terms)
    return mats


def frac_rank(M):
    M = [row[:] for row in M]
    if not M or not M[0]:
        return 0
    r = 0; nrow, ncol = len(M), len(M[0])
    for c in range(ncol):
        p = next((i for i in range(r, nrow) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == nrow:
            break
    return r


def random_vals(rng):
    rnd = lambda: Fraction(rng.randint(1, 10 ** 6), rng.randint(1, 10 ** 3))
    return dict(n={g: rnd() for g in G3}, nb={g: rnd() for g in G3}, v={g: rnd() for g in G3}, vb={g: rnd() for g in G3},
                s={(i, j): rnd() for i in G3 for j in G3 if i != j}, lam={k: rnd() for k in ('ND', 'nuD', 'NH', 'nuH')})


def light_pairs(s, cfg, rng, trials=2, names=False):
    """light pairs per sector = dimension - generic rank (max over random rational points); optionally the fields whose
    row (or column) is identically zero -- exactly massless at tree level -- per sector."""
    out = {}; zero_rows = {}; zero_cols = {}; dims = {}
    for t in range(trials):
        mats = sector_matrices(s, cfg, random_vals(rng))
        for sec, (M, R, Cc) in mats.items():
            assert len(R) == len(Cc), (sec, R, Cc)
            rk = frac_rank(M)
            out[sec] = max(out.get(sec, -1), rk); dims[sec] = len(R)
            if names:
                zero_rows[sec] = [R[i] for i in range(len(R)) if all(x == 0 for x in M[i])]
                zero_cols[sec] = [Cc[j] for j in range(len(Cc)) if all(M[i][j] == 0 for i in range(len(R)))]
    lp = {sec: dims[sec] - out[sec] for sec in out}
    if names:
        return lp, zero_rows, zero_cols
    return lp


# ------------------------------------------------------------------------------------------------ (c) the census
def analyse(pat, name):
    rng = random.Random(7)
    t0 = time.time()
    print(f"\n=== {name}: {sum(pat.values())} SM lines, {len(pat)} distinct survival patterns ===", flush=True)
    best = {}
    census = collections.Counter(); best_by_pattern = {}
    n_lines_solved = 0; solved_patterns = 0
    for p, cnt in pat.items():
        s = {lab: p[i] for i, lab in enumerate(LABELS)}
        results = []
        for cfg in configurations(s):
            lp = light_pairs(s, cfg, rng)
            results.append((cfg, lp))
            census[(lp['T'], lp['H'])] += cnt
        # the best configuration on this pattern: minimal light triplet pairs among those with a light doublet pair
        cands = [(lp['T'], -lp['H'], cfg, lp) for cfg, lp in results if lp['H'] >= 1]
        if cands:
            cands.sort(key=lambda x: (x[0], x[1]))
            bT, _, bcfg, blp = cands[0]
            best_by_pattern[p] = (bT, bcfg, blp, cnt)
            if bT <= 1:
                n_lines_solved += cnt; solved_patterns += 1
    minT = min(v[0] for v in best_by_pattern.values())
    print(f"  (light triplet pairs n_T, light doublet pairs n_H) over all (line, configuration) -> lines x configurations: {dict(sorted(census.items()))}", flush=True)
    print(f"  minimal n_T over the patterns' best configurations (n_H >= 1): {minT}; patterns reaching n_T <= 1: {solved_patterns} of {len(pat)}, covering {n_lines_solved} lines", flush=True)
    best_hist = collections.Counter()
    for p, (bT, bcfg, blp, cnt) in best_by_pattern.items():
        best_hist[bT] += cnt
    print(f"  best n_T per line (its best configuration with n_H >= 1) -> lines: {dict(sorted(best_hist.items()))}", flush=True)
    # more than one light generation of doublets: the best n_T among configurations with n_H >= 6
    multi = collections.Counter()
    for p, cnt in pat.items():
        s = {lab: p[i] for i, lab in enumerate(LABELS)}
        cands = [light_pairs(s, cfg, rng) for cfg in configurations(s)]
        good = [lp['T'] for lp in cands if lp['H'] >= 6]
        multi[min(good) if good else None] += cnt
    print(f"  with at least six light doublet pairs (two light generations' worth): best n_T -> lines: {dict(sorted(multi.items(), key=str))}", flush=True)
    # what the best two-generation configuration leaves massless (first pattern reaching the minimum)
    shown2 = 0
    for p, cnt in sorted(pat.items(), key=lambda kv: -kv[1]):
        s = {lab: p[i] for i, lab in enumerate(LABELS)}
        cands = [(light_pairs(s, cfg, rng)['T'], cfg) for cfg in configurations(s)]
        cands = [(t, cfg) for t, cfg in cands if light_pairs(s, cfg, rng)['H'] >= 6]
        if not cands or min(c[0] for c in cands) != min(k for k in multi if k is not None):
            continue
        t, cfg = min(cands, key=lambda c: c[0])
        lp, zr, zc = light_pairs(s, cfg, rng, names=True)
        fmt = lambda f: (f[0] if not f[0].startswith('m:') else f[0][2:] + "'") + str(f[1] + 1)
        desc = ', '.join(f"{lab} {''.join(map(str, s[lab]))}" for lab in LABELS if s[lab] != (1, 1, 1))
        print(f"    two-generation example [{desc or 'full spectrum'}] x {cnt} lines: configuration {tuple(None if x is None else x + 1 for x in cfg)} -> light pairs {lp}; exactly massless T rows {[fmt(f) for f in zr['T']]}, H rows {[fmt(f) for f in zr['H']]}; kernel beyond zero rows: T {lp['T'] - len(zr['T'])}, H {lp['H'] - len(zr['H'])}", flush=True)
        shown2 += 1
        if shown2 >= 2:
            break
    # the exactly-massless fields of the solved patterns' best configurations
    for p, (bT, bcfg, blp, cnt) in sorted(best_by_pattern.items(), key=lambda kv: (kv[1][0], -kv[1][3])):
        if bT > 1:
            break
        s = {lab: p[i] for i, lab in enumerate(LABELS)}
        lp, zr, zc = light_pairs(s, bcfg, rng, names=True)
        fmt = lambda f: (f[0] if not f[0].startswith('m:') else f[0][2:] + "'") + str(f[1] + 1)
        desc = ', '.join(f"{lab} {''.join(map(str, s[lab]))}" for lab in LABELS if s[lab] != (1, 1, 1))
        print(f"    solved pattern [{desc}]: configuration {tuple(None if x is None else x + 1 for x in bcfg)}; exactly massless: T rows {[fmt(f) for f in zr['T']]} cols {[fmt(f) for f in zc['T']]}; H rows {[fmt(f) for f in zr['H']]} cols {[fmt(f) for f in zc['H']]}; kernel beyond the zero rows: T {lp['T'] - len(zr['T'])}, H {lp['H'] - len(zr['H'])}", flush=True)
    # show the best patterns
    shown = 0
    for p, (bT, bcfg, blp, cnt) in sorted(best_by_pattern.items(), key=lambda kv: (kv[1][0], -kv[1][3])):
        if shown >= 6:
            break
        s = {lab: p[i] for i, lab in enumerate(LABELS)}
        desc = ', '.join(f"{lab} {''.join(map(str, s[lab]))}" for lab in LABELS if s[lab] != (1, 1, 1))
        print(f"    pattern [{desc or 'full spectrum'}] x {cnt} lines: best configuration (N gen, nu^c gen, flavon pair's third gen) = {tuple(None if x is None else x + 1 for x in bcfg)} -> light pairs {blp}", flush=True)
        shown += 1
    print(f"  ({time.time() - t0:.0f} s)", flush=True)
    return dict(n_patterns=len(pat), census={str(k): v for k, v in census.items()}, minT=minT, solved_patterns=solved_patterns, lines_solved=n_lines_solved,
                best=[(p, v[0], v[1], v[2], v[3]) for p, v in best_by_pattern.items()])


def main():
    t0 = time.time()
    out = {}
    for n in (9, 12):
        pat, K = patterns(B1301 / f"support_Y{n}.json", n)
        assert sum(pat.values()) == {9: 706464, 12: 34752}[n], sum(pat.values())
        out[n] = analyse(pat, f"Y_{n}")
    ok = out[9]['minT'] >= 2 and out[12]['n_patterns'] > 0
    print(f"\n  Y_9 control: no configuration reaches n_T <= 1 (the light D pair of B1283/B1300): {out[9]['minT'] >= 2}")
    print(f"  Y_12: minimal light triplet pairs {out[12]['minT']}; lines admitting a configuration with n_T <= 1 and a light doublet pair: {out[12]['lines_solved']} of 34752")
    print(f"\n  ({time.time() - t0:.0f} s)")
    out['ok'] = ok
    return out


if __name__ == "__main__":
    out = main()
    print("\nSELFTEST:", "PASS" if out['ok'] else "FAIL")
    sys.exit(0 if out['ok'] else 1)
