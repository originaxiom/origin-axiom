#!/usr/bin/env python3
"""THE 2-ADIC TOWER (B1304): the 2-primary part of the character group of Y_n (n = 6, 12, 24: (Z/8 x Z/8)?, (Z/16)^2, (Z/32)^2)
carries the whole support at the even levels whose odd support is empty (B1303's law: the odd support of an even level
is the pullback of Y_{n/2}'s, and Y_3, Y_6, Y_12 have none), so the 2x2 criterion on the 2-primary subgroup alone gives
the support, the family characters, the alphabet K3, the Standard-Model lines (B1300's weight table), every multiplet's
survival and the one-triplet census (B1302's machinery) -- for Y_24 (10^10 characters, but a 2-primary subgroup of
1 024), with Y_12 (34 752 SM lines) as the control."""
from __future__ import annotations
import sys, math, json, time, collections, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'frontier' / 'B1303_the_two_by_two_criterion' / 'verification'))
sys.path.insert(0, str(ROOT / 'frontier' / 'B1302_the_one_triplet_vacua' / 'verification'))
sys.path.insert(0, str(ROOT / 'frontier' / 'B1301_the_towers_alphabet' / 'verification'))
import criterion_at_scale as S
from lines_from_support import QUL, LABELS

def two_primary(n):
    d1, d2, m, U = S.smith(n)
    k1 = 0
    while d1 % 2 ** (k1 + 1) == 0: k1 += 1
    k2 = 0
    while d2 % 2 ** (k2 + 1) == 0: k2 += 1
    n1, n2 = 2 ** k1, 2 ** k2
    I, J = np.meshgrid(np.arange(n1), np.arange(n2), indexing='ij'); I, J = I.ravel(), J.ravel()
    c1 = I * (d1 // n1); c2 = J * (d2 // n2)
    e1 = (c1 * (m // d1)) % m; e2 = (c2 * (m // d2)) % m
    w1 = (U[0][0] * e1 + U[1][0] * e2) % m; w2 = (U[0][1] * e1 + U[1][1] * e2) % m
    fib = S.fib_pairs(n, m); qs = S.primes_1_mod(m)
    ok = S.identity_test(w1, w2, n, m, qs[0], fib) & S.identity_test(w1, w2, n, m, qs[1], fib)
    H = np.zeros((n1, n2), dtype=np.int64)
    H[I, J] = ok.astype(np.int64)
    H[0, 0] = 0
    order = np.maximum(n1 // np.gcd(I, n1), n2 // np.gcd(J, n2)); order[0] = 1
    return dict(n=n, d1=d1, d2=d2, m=m, n1=n1, n2=n2, H=H, I=I, J=J, order=order.reshape(n1, n2))

def analyse(P, want_patterns=True):
    n, n1, n2, H = P['n'], P['n1'], P['n2'], P['H']
    pos = np.argwhere(H == 1)
    byord = collections.Counter(int(P['order'][i, j]) for i, j in pos)
    chis = [(int(i), int(j)) for i, j in pos if P['order'][i, j] == 2]
    assert len(chis) == 3, chis
    # generation counts and the alphabet
    I, J = np.meshgrid(np.arange(n1), np.arange(n2), indexing='ij'); I, J = I.ravel(), J.ravel()
    G = sum(H[(I + c[0]) % n1, (J + c[1]) % n2] for c in chis)
    K3 = np.stack([I[G >= 3], J[G >= 3]], axis=1); K2 = int((G == 2).sum())
    lord = collections.Counter(int(P['order'][i, j]) for i, j in K3)
    print(f"=== Y_{n}: 2-primary subgroup Z/{n1} x Z/{n2}; support {len(pos)} by order {dict(sorted(byord.items()))}; K3 {len(K3)} letters by order {dict(sorted(lord.items()))}; K2 {K2} ===", flush=True)
    # lines
    K = len(K3)
    iu, il = np.meshgrid(np.arange(K), np.arange(K), indexing='ij')
    u_all, l_all = K3[iu.ravel()], K3[il.ravel()]
    chi = np.array(chis, dtype=np.int64)
    counts = collections.Counter(); hist = collections.Counter(); d_tot = collections.Counter(); ever = collections.Counter()
    patterns = collections.Counter(); d_gen = collections.Counter()
    for iq in range(K):
        q = K3[iq][None, :]
        bits = {}
        for lab in LABELS:
            a, b, c = QUL[lab]
            x = a * q + b * u_all + c * l_all
            bits[lab] = np.stack([H[(x[:, 0] + chi[g][0]) % n1, (x[:, 1] + chi[g][1]) % n2] for g in range(3)], axis=1)
        tot = {lab: bits[lab].sum(axis=1) for lab in LABELS}
        three = (tot['d^c'] == 3) & (tot['e^c'] == 3)
        key = lambda lab: ((QUL[lab][0] * q + QUL[lab][1] * u_all + QUL[lab][2] * l_all) % np.array([n1, n2]))
        kQ, ku, ke = key('Q'), key('u^c'), key('e^c')
        broken = ~((kQ == ku).all(axis=1) & (ku == ke).all(axis=1))
        vac = (tot['S'] >= 1) & (tot['nu^c'] >= 1) & (tot['H_u'] >= 1) & (tot['H_d'] >= 1)
        sm = three & broken & vac
        counts['three'] += int(three.sum()); counts['broken'] += int((three & broken).sum()); counts['sm'] += int(sm.sum())
        full = sm & np.all(np.stack([tot[l] == 3 for l in LABELS]), axis=0)
        counts['full'] += int(full.sum())
        idx = np.where(sm)[0]
        for t in idx.tolist():
            hist[tuple(int(tot[l][t]) for l in ('H_u', 'H_d', 'D', 'Dbar'))] += 1
            d_tot[int(tot['D'][t])] += 1
            d_gen[tuple(int(x) for x in bits['D'][t])] += 1
            for l in LABELS:
                if tot[l][t] < 3: ever[l] += 1
            if want_patterns:
                patterns[tuple(tuple(int(x) for x in bits[l][t]) for l in LABELS)] += 1
    print(f"  lines K3^3 = {K ** 3}: three generations {counts['three']}, SU(5) broken {counts['broken']}, SM vacua {counts['sm']}, full spectrum {counts['full']}", flush=True)
    print(f"  D totals {dict(sorted(d_tot.items()))}; surviving D generations {dict(sorted(d_gen.items()))}; loses a generation {dict(ever)}", flush=True)
    print(f"  (H_u, H_d, D, Dbar) -> lines: {dict(sorted(hist.items()))}", flush=True)
    print(f"  survival patterns {len(patterns)}", flush=True)
    return dict(support=len(pos), byord=dict(byord), K3=K, K2=K2, letter_orders=dict(lord), counts=dict(counts), d_tot=dict(d_tot), d_gen=dict(d_gen),
                hist=dict(hist), ever=dict(ever), patterns=patterns)

def main():
    t0 = time.time()
    out = {}
    for n in (12, 24):
        P = two_primary(n)
        out[n] = analyse(P)
    # the one-triplet census of B1302 on Y_24's patterns
    import one_triplet_vacua as V
    for n in (12, 24):
        out[n]['vacua'] = V.analyse(out[n]['patterns'], f"Y_{n}")
    ok = (out[12]['support'] == 123 and out[12]['K3'] == 97 and out[12]['counts']['sm'] == 34752 and out[12]['counts']['full'] == 3264
          and out[12]['vacua']['minT'] == 1 and out[12]['vacua']['lines_solved'] == 768)
    print(f"\n  ({time.time() - t0:.0f} s)")
    out['ok'] = ok
    return out

if __name__ == "__main__":
    out = main()
    print("\nSELFTEST:", "PASS" if out['ok'] else "FAIL")
    sys.exit(0 if out['ok'] else 1)
