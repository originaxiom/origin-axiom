#!/usr/bin/env python3
"""The Standard-Model lines of a closing whose h^1 support is (S x V_4) minus 1 with S a set of odd-order characters
(closed under multiplication by units) and V_4 the family group -- Y_9 (S = the 36 eigencharacters of order 19), Y_15,
Y_21 ...: the multiplicity of a component is 3 if its odd part is in S, 3 or 2 (one generation projected) if its odd part
is trivial according to its 2-part, 0 otherwise.  The odd triples (f_Q, f_u, f_L) in (S u 0)^3 are enumerated in chunks,
reduced to signatures, and the 64 sign assignments counted per signature.  Reproduces B1278/B1300 on Y_9."""
import sys, math, json, time, collections, pathlib, itertools
import numpy as np
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2] / 'B1301_the_towers_alphabet' / 'verification'))
from lines_from_support import QUL, LABELS

def load(path):
    d = json.loads(pathlib.Path(path).read_text())
    m = d['m']; pos = [tuple(w) for w in d['positives']]; chis = [tuple(c) for c in d['chis']]
    order = lambda w: m // math.gcd(math.gcd(w[0], w[1]), m)
    a = 0
    while m % (2 ** (a + 1)) == 0: a += 1
    m_odd = m // 2 ** a
    S = sorted(w for w in pos if order(w) % 2 == 1)
    # closure of the support under the family group, and the form (S x V4) minus 1
    Sset = set(pos)
    add = lambda x, y: ((x[0] + y[0]) % m, (x[1] + y[1]) % m)
    form = all(add(s, c) in Sset for s in S for c in chis) and len(pos) == 4 * (len(S) + 1) - 1
    # S closed under units coprime to m_odd
    units_ok = all(((k * s[0]) % m, (k * s[1]) % m) in set(S) for s in S[:50] for k in (2, 3, 5, 7) if math.gcd(k, m_odd) == 1)
    return dict(m=m, S=S, chis=chis, form=form, units_ok=units_ok, n=d['n'], pos=pos)

def keyf(W, m):
    return W[:, 0] * m + W[:, 1]

def run(path, name):
    t0 = time.time()
    L = load(path); m = L['m']; S = L['S']; chis = L['chis']
    print(f"=== {name}: support {len(L['pos'])} = (S x V4) minus 1 with |S| = {len(S)}: {L['form']}; S closed under units: {L['units_ok']} ===", flush=True)
    Sarr = np.array(S + [(0, 0)], dtype=np.int64)            # S u {0}
    Skeys = np.sort(keyf(np.array(S, dtype=np.int64), m))
    n0 = len(Sarr)
    iu, il = np.meshgrid(np.arange(n0), np.arange(n0), indexing='ij')
    fu, fl = Sarr[iu.ravel()], Sarr[il.ravel()]
    sig = collections.Counter()
    comp = {lab: QUL[lab] for lab in LABELS}
    for iq in range(n0):
        fq = Sarr[iq][None, :]
        states = []
        vals = {}
        for lab in LABELS:
            a, b, c = comp[lab]
            x = (a * fq + b * fu + c * fl) % m
            k = keyf(x, m); vals[lab] = k
            zero = (k == 0)
            inS = np.isin(k, Skeys)
            states.append(np.where(zero, 1, np.where(inS, 2, 0)).astype(np.int8))     # 0 outside, 1 zero, 2 in S
        # encode the signature (eleven ternary states and the SU(5)-equality bit) as one integer and count by bincount
        code = np.zeros(len(fu), dtype=np.int64)
        for st_i in states:
            code = code * 3 + st_i.astype(np.int64)
        eq = ((vals['Q'] == vals['u^c']) & (vals['u^c'] == vals['e^c'])).astype(np.int64)
        code = code * 2 + eq
        bc = np.bincount(code, minlength=2 * 3 ** 11)
        for cval in np.nonzero(bc)[0]:
            c = int(cval); e = c % 2; c //= 2
            digits = []
            for _ in range(11):
                digits.append(c % 3); c //= 3
            sig[tuple(reversed(digits)) + (e,)] += int(bc[cval])
    print(f"  odd triples {n0 ** 3}, distinct signatures {len(sig)} ({time.time() - t0:.0f} s)", flush=True)
    # signs: V4 = {0, v1, v2, v3} as 2-bit vectors; family character chi_g <-> v_g
    V = [(0, 0), (1, 0), (0, 1), (1, 1)]
    counts = collections.Counter(); hist = collections.Counter(); d_tot = collections.Counter(); ever = collections.Counter()
    patterns = collections.Counter(); n_sm = 0; n_full = 0; n_three = 0; n_broken = 0
    for r, c in sig.items():
        st = r[:11]; eq = r[11]
        for sq, su, sl in itertools.product(V, repeat=3):
            # letters: a trivial odd part needs a trivial 2-part (else generation count 2)
            if (st[0] == 1 and sq != (0, 0)) or (st[1] == 1 and su != (0, 0)) or (st[3] == 1 and sl != (0, 0)):
                continue
            mult = {}; surv = {}
            for i, lab in enumerate(LABELS):
                a, b, cc = comp[lab]
                s2 = ((a * sq[0] + b * su[0] + cc * sl[0]) % 2, (a * sq[1] + b * su[1] + cc * sl[1]) % 2)
                if st[i] == 2:
                    mult[lab] = 3; surv[lab] = (1, 1, 1)
                elif st[i] == 1:
                    if s2 == (0, 0):
                        mult[lab] = 3; surv[lab] = (1, 1, 1)
                    else:
                        g = V.index(s2) - 1
                        mult[lab] = 2; surv[lab] = tuple(0 if h == g else 1 for h in range(3))
                else:
                    mult[lab] = 0; surv[lab] = (0, 0, 0)
            three = all(mult[l] == 3 for l in ('Q', 'u^c', 'd^c', 'L', 'e^c'))
            if not three:
                continue
            n_three += c
            # SU(5) broken: not (odd parts equal and 2-parts equal)
            s2Q = sq; s2u = su
            a, b, cc = comp['e^c']; s2e = ((a * sq[0] + b * su[0] + cc * sl[0]) % 2, (a * sq[1] + b * su[1] + cc * sl[1]) % 2)
            broken = not (eq == 1 and s2Q == s2u == s2e)
            if not broken:
                continue
            n_broken += c
            if not (mult['S'] >= 1 and mult['nu^c'] >= 1 and mult['H_u'] >= 1 and mult['H_d'] >= 1):
                continue
            n_sm += c
            full = all(mult[l] == 3 for l in LABELS)
            n_full += c * full
            hist[(mult['H_u'], mult['H_d'], mult['D'], mult['Dbar'])] += c
            d_tot[mult['D']] += c
            for l in LABELS:
                if mult[l] < 3: ever[l] += c
            patterns[tuple(surv[l] for l in LABELS)] += c
    print(f"  three generations {n_three}; SU(5) broken {n_broken}; SM vacua {n_sm}; full spectrum {n_full}", flush=True)
    print(f"  D totals {dict(sorted(d_tot.items()))}; loses a generation {dict(ever)}; (H_u,H_d,D,Dbar) {dict(sorted(hist.items()))}", flush=True)
    print(f"  survival patterns {len(patterns)}  ({time.time() - t0:.0f} s)", flush=True)
    return dict(n_three=n_three, n_broken=n_broken, n_sm=n_sm, n_full=n_full, d_tot=dict(d_tot), hist=dict(hist), patterns=patterns, form=L['form'])

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
