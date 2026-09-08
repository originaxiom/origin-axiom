#!/usr/bin/env python3
"""The Standard-Model Wilson lines of a closing Y_n from its h^1 support alone (B1301): given the characters of
H_1(Y_n) with their h^1 (a level file written by the sweep), the three family characters and the weight table of the 27
modulo the SM roots in the Z-basis (w_Q, w_u^c, w_L) (B1300), enumerate the three-generation alphabet K3, the lines
(psi_Q, psi_u, psi_L) in K3^3, every component's multiplicity, B1278's classes (three generations of d^c, e^c; SU(5)
broken; SM vacua; full spectrum) and the survival histogram -- and test the triplet's protection.  On Y_9 this must
reproduce B1278 and B1300 exactly; on Y_12 it is the enumeration."""
from __future__ import annotations
import sys, math, json, collections, pathlib, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
for arc in ("B1267_spectrum_law_rebuilt", "B1268_cusped_net_chirality_bound", "B1269_transport_computed",
            "B1273_the_three_fold_closing", "B1274_the_tower_and_its_doubles", "B1275_the_cubic_made_explicit",
            "B1276_the_relations_the_chain_forces", "B1277_the_vacuum_manifold_of_the_closing", "B1278_the_six_fold_closing"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))
import six_fold_closing as SF
TW = SF.TW
# the weights of the 27 modulo the SM roots in the basis (w_Q, w_u^c, w_L) -- B1300, the eleven cubic couplings
QUL = {'Q': (1, 0, 0), 'u^c': (0, 1, 0), 'L': (0, 0, 1), 'D': (-2, 0, 0), 'e^c': (2, -1, 0), 'H_u': (-1, -1, 0),
       'd^c': (1, -1, 1), 'Dbar': (-1, 0, -1), 'H_d': (-2, 1, -1), 'nu^c': (1, 1, -1), 'S': (3, 0, 1)}
LABELS = ('Q', 'u^c', 'd^c', 'L', 'e^c', 'H_u', 'H_d', 'D', 'Dbar', 'S', 'nu^c')


def load_level(path, n):
    """chars (raw tuples), coordinates in (+) Z/d_j, moduli, h1 array indexed by coordinate key, family characters' keys."""
    d = json.loads(pathlib.Path(path).read_text())
    assert d['n'] == n
    gens, rels = TW.presentation(n, branched=True)
    Rm = SF.relation_matrix(gens, rels)
    D, U, V = SF.smith_with_transforms(Rm)
    m = d['m']
    chars, coords, moduli = SF.characters(D, V, m, with_coords=True)
    if 'positives' in d:                       # a support file: the positives (h^1 = 1) and zero elsewhere
        h1_by_tuple = {a: 0 for a in chars}
        for a in d['positives']:
            h1_by_tuple[tuple(a)] = 1
    else:                                      # a full level file
        h1_by_tuple = {tuple(a): h for a, h in zip(d['chars'], d['h1'])}
    assert set(h1_by_tuple) == set(chars)
    mods = np.array(moduli, dtype=np.int64)
    strides = np.array([int(np.prod(moduli[:k])) for k in range(len(moduli))], dtype=np.int64)
    N = int(np.prod(moduli))
    key = lambda c: int(np.dot(np.array(c, dtype=np.int64), strides))
    H = np.zeros(N, dtype=np.int64)
    for a, c in zip(chars, coords):
        H[key(c)] = h1_by_tuple[a]
    c_of = {a: c for a, c in zip(chars, coords)}
    chis = [tuple(c) for c in d['chis']]
    chi_coords = np.array([c_of[c] for c in chis], dtype=np.int64)
    return dict(n=n, m=m, moduli=mods, strides=strides, N=N, H=H, coords=np.array(coords, dtype=np.int64), chi=chi_coords, tors=d['tors'])


def keys(arr, L):
    return (arr % L['moduli']) @ L['strides']


def alphabet(L):
    C = L['coords']; H = L['H']
    G = sum(H[keys(C + L['chi'][g], L)] for g in range(3))
    K3 = C[G >= 3]; K2 = C[G == 2]
    return K3, K2, collections.Counter(G.tolist())


def enumerate_lines(L, K3, chunk=2_000_000, want_hist=True, roots=None):
    """(psi_Q, psi_u, psi_L) in K3^3; multiplicities of the eleven multiplets; B1278's classes; the survival census."""
    H, chi = L['H'], L['chi']
    K = len(K3); n_lines = K ** 3
    Hg = [None] * 3
    counts = collections.Counter()
    hist = collections.Counter(); ever = collections.Counter(); hist_SNu = collections.Counter()
    d_totals = set(); proj_is_family = True; split = 0; nonfull_lost = collections.Counter()
    kept_hist = collections.Counter(); adj_hist = collections.Counter(); d_gen = collections.Counter()
    fam_keys = {int(keys(chi[g][None, :], L)[0]): g for g in range(3)}
    zero_key = 0
    # iterate over psi_Q; vectorize over (psi_u, psi_L)
    iu, il = np.meshgrid(np.arange(K), np.arange(K), indexing='ij'); iu, il = iu.ravel(), il.ravel()
    u_all, l_all = K3[iu], K3[il]
    for iq in range(K):
        q = K3[iq][None, :]
        mult = {}; kk = {}
        for lab in LABELS:
            a, b, c = QUL[lab]
            x = a * q + b * u_all + c * l_all
            kx = keys(x, L); kk[lab] = kx
            mult[lab] = sum(H[keys(x + chi[g], L)] for g in range(3))
        three = (mult['d^c'] >= 3) & (mult['e^c'] >= 3) & (mult['Q'] >= 3) & (mult['u^c'] >= 3) & (mult['L'] >= 3)
        broken = ~((kk['Q'] == kk['u^c']) & (kk['u^c'] == kk['e^c']))
        vac = (mult['S'] >= 1) & (mult['nu^c'] >= 1) & (mult['H_u'] >= 1) & (mult['H_d'] >= 1)
        sm = three & broken & vac
        full = sm & np.all(np.stack([mult[l] == 3 for l in LABELS]), axis=0)
        counts['three_gen'] += int(three.sum()); counts['su5_broken'] += int((three & broken).sum())
        counts['sm_vacua'] += int(sm.sum()); counts['full'] += int(full.sum())
        if sm.any():
            d_totals |= set(mult['D'][sm].tolist())
            split += int((sm & (mult['D'] == 0) & (mult['Dbar'] == 0)).sum())
            for lab in LABELS:
                ever[lab] += int((mult[lab][sm] < 3).sum())
                # a multiplet loses a generation iff its character is a family character?
                kx = kk[lab][sm]; ml = mult[lab][sm]
                isfam = np.isin(kx, list(fam_keys))
                proj_is_family &= bool(((ml < 3) == isfam).all())
            if want_hist:
                for t in zip(mult['H_u'][sm].tolist(), mult['H_d'][sm].tolist(), mult['D'][sm].tolist(), mult['Dbar'][sm].tolist()):
                    hist[t] += 1
                for t in zip(mult['S'][sm].tolist(), mult['nu^c'][sm].tolist()):
                    hist_SNu[t] += 1
            lost = sum((mult[l] < 3).astype(int) for l in LABELS)[sm & ~full]
            nonfull_lost.update(lost.tolist())
            # which generations of D survive on the SM lines (pattern of h^1(chi_g psi_D) over g)
            xD = (QUL['D'][0] * q + QUL['D'][1] * u_all + QUL['D'][2] * l_all)[sm]
            pat = np.stack([H[keys(xD + chi[g], L)] for g in range(3)], axis=1)
            for row in pat.tolist():
                d_gen[tuple(row)] += 1
            if roots is not None:
                # the roots' characters: kept iff trivial; adjoint chirals: h^1 of the root's character
                qs, us, ls = q, u_all[sm], l_all[sm]
                kept = np.zeros(int(sm.sum()), dtype=np.int64); adj = np.zeros(int(sm.sum()), dtype=np.int64)
                kept5 = np.zeros(int(sm.sum()), dtype=np.int64)
                for r in roots:
                    a, b, c = r['qul']
                    xr = a * qs + b * us + c * ls
                    kr = keys(xr, L)
                    kept += (kr == zero_key); adj += H[kr]
                    if r['su5']:
                        kept5 += (kr == zero_key)
                for kv, k5, av in zip(kept.tolist(), kept5.tolist(), adj.tolist()):
                    kept_hist[(k5, kv)] += 1; adj_hist[av] += 1
    return dict(n_lines=n_lines, K=K, counts=dict(counts), d_totals=sorted(d_totals), n_split=split, ever=dict(ever),
                hist=dict(sorted(hist.items())), hist_SNu=dict(sorted(hist_SNu.items())), proj_is_family=proj_is_family,
                nonfull_lost=dict(sorted(nonfull_lost.items())), d_gen=dict(sorted(d_gen.items())),
                roots_kept=dict(sorted(kept_hist.items())), adjoint_chirals=dict(sorted(adj_hist.items())))


def protection(L, K3):
    """squares of the letters: are they letters, and is any a family character?"""
    sq = (2 * K3) % L['moduli']
    letters = {int(k) for k in keys(K3, L)}
    sqk = keys(sq, L)
    fam = {int(keys(L['chi'][g][None, :], L)[0]) for g in range(3)}
    return dict(squares_in_alphabet=all(int(k) in letters for k in sqk), square_is_family=any(int(k) in fam for k in sqk),
                letter_orders=dict(collections.Counter(order_of(K3, L).tolist())))


def order_of(C, L):
    o = np.ones(len(C), dtype=np.int64)
    for j, d in enumerate(L['moduli'].tolist()):
        g = np.gcd(C[:, j] % d, d)
        o = np.lcm(o, d // g)
    return o


def run(path, n, roots=None):
    t0 = time.time()
    L = load_level(path, n)
    if roots is not None:
        rd = json.loads(pathlib.Path(roots).read_text())
        assert {k: tuple(v) for k, v in rd['table27'].items()} == QUL, "the roots file's table of the 27 must be B1300's"
        roots = rd['roots']
    K3, K2, dist = alphabet(L)
    print(f"=== Y_{n}: H_1 = {L['tors']}; support {int((L['H'] > 0).sum())}; generation-count distribution {dict(sorted(dist.items()))}; K3 = {len(K3)} letters by order {dict(collections.Counter(order_of(K3, L).tolist()))}; K2 = {len(K2)} ===", flush=True)
    out = dict(n=n, K3=len(K3), K2=len(K2), dist=dict(dist))
    if len(K3) > 1:
        E = enumerate_lines(L, K3, roots=roots)
        print(f"  lines K3^3 = {E['n_lines']}: {E['counts']}", flush=True)
        print(f"  SM lines: D totals {E['d_totals']}; split lines {E['n_split']}; loses-a-generation {E['ever']}; (H_u,H_d,D,Dbar) {E['hist']}; (N,nu^c) {E['hist_SNu']}; projected iff family character: {E['proj_is_family']}; multiplets lost per non-full line {E['nonfull_lost']}", flush=True)
        print(f"  SM lines: surviving generations of D (h^1(chi_g psi_D) for g = 1, 2, 3) -> lines: {E['d_gen']}; (SU(5) roots, E6 roots) with trivial character -- 8 SU(5) roots = exactly the SM's at the <N>, <nu^c> point (B1278); the extra E6 roots are broken by those VEVs -> lines: {E['roots_kept']}; adjoint chirals from the broken roots -> lines: {E['adjoint_chirals']}", flush=True)
        out.update(E); out['K'] = len(K3)
    P = protection(L, K3)
    out.update(squares_are_letters=P['squares_in_alphabet'], square_is_family=P['square_is_family'], letter_orders=P['letter_orders'])
    print(f"  protection: squares of letters are letters: {P['squares_in_alphabet']}; some square is a family character: {P['square_is_family']}; letter orders {P['letter_orders']}  ({time.time() - t0:.0f} s)", flush=True)
    out['protection'] = P
    return out


if __name__ == "__main__":
    path, n = sys.argv[1], int(sys.argv[2])
    run(path, n)
