"""Run 2: rebuild the census (primitive necklaces, length 2..12, both letters, a rotation with W_col^T v5 = +-v5 mod 5)
and test every member: all 24 nontrivial mu_5 characters, homology dims, Wada torsion; base line vs (t^2+t-1)^2/5."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from itertools import product as iprod
from collections import defaultdict
from tcore import *

V5 = (1, 2)
MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 12


def rotations(w):
    return [w[i:] + w[:i] for i in range(len(w))]


def primitive(w):
    n = len(w)
    return all(w != w[d:] + w[:d] for d in range(1, n) if n % d == 0) if n > 1 else True


def eps_of(M, transpose=True):
    if transpose:
        Mv = tuple(sum(M[k][i] * V5[k] for k in range(2)) % 5 for i in range(2))
    else:
        Mv = tuple(sum(M[i][k] * V5[k] for k in range(2)) % 5 for i in range(2))
    if Mv == V5:
        return 1
    if Mv == tuple((-x) % 5 for x in V5):
        return -1
    return 0


def census(transpose=True):
    seen = set()
    out = []
    for n in range(2, MAXLEN + 1):
        for tup in iprod('LR', repeat=n):
            w = ''.join(tup)
            if 'L' not in w or 'R' not in w:
                continue
            can = min(rotations(w))
            if can in seen:
                continue
            seen.add(can)
            if not primitive(can):
                continue
            hits = [(r, eps_of(mat_word(r), transpose)) for r in rotations(can)]
            hits = [(r, e) for r, e in hits if e != 0]
            if hits:
                out.append((can, sorted(hits)[0]))
    return out


cT = census(True)
cN = census(False)
print(f'census (W_col^T v5 = +-v5): {len(cT)} primitive necklaces of length 2..{MAXLEN}')
print(f'census (W_col   v5 = +-v5): {len(cN)} primitive necklaces of length 2..{MAXLEN}')
print(f'same necklace sets? {set(c for c, _ in cT) == set(c for c, _ in cN)}')
by_len = defaultdict(int)
for c, _ in cT:
    by_len[len(c)] += 1
print('by length:', dict(sorted(by_len.items())))


def qmul(u, v):
    return (u[0] * v[0] + 5 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])


S = {(Fr(5, 2), Fr(-1, 2)), (Fr(5, 2), Fr(1, 2))}
stats = defaultdict(int)
records = []
viol = []
for can, (w, eps) in cT:
    M = mat_word(w, eps)
    tr = M[0][0] + M[1][1]
    unip = ((M[0][0] - 1) % 5, M[0][1] % 5, M[1][0] % 5, (M[1][1] - 1) % 5)
    mult_one = unip != (0, 0, 0, 0)
    tors = smith_tors(((M[0][0] - 1, M[0][1]), (M[1][0], M[1][1] - 1)))
    phi = phi_word(w, eps)
    assert subst(phi, COMM) == COMM
    gens, rels = hnn(phi)
    chars = characters(gens, rels)
    dimH1 = {5: 1, 25: 2, 125: 3}[len(chars)]
    base_prod = (Fr(1), Fr(0))
    rec = dict(necklace=can, word=w, eps=eps, trace=tr, tors=str(tors), dimH1F5=dimH1, mult_one=mult_one)
    nfib = nmixed = 0
    for e in chars:
        f = (e['a'], e['b']) != (0, 0)
        if not f and e['t'] == 0:
            continue
        J, d1, h, ok = complex_data(gens, rels, e)
        if not ok:
            viol.append((w, e, 'd1d2'))
        tau, j = wada(gens, rels, e)
        # a second choice of j where possible: the Wada invariant must agree up to +-zeta^m
        others = [i for i, g in enumerate(gens) if e[g] % 5 != 0 and i != j]
        for i2 in others:
            tau2, _ = wada(gens, rels, e, j=i2)
            if is0(tau) != is0(tau2) or (not is0(tau) and unit_root(div(tau, tau2)) is None):
                viol.append((w, e, 'j-dependence'))
        if not f:
            base_prod = qmul(base_prod, abs2(tau))
            if h != (0, 0, 0):
                viol.append((w, e, 'base not acyclic'))
            continue
        if e['t'] == 0:
            nfib += 1
            if not (h == (0, 1, 1) and is0(tau)):
                viol.append((w, e, f'fibre k=0 h={h}'))
        else:
            nmixed += 1
            if not (h == (0, 0, 0) and unit_root(div(tau, sub(zpow(e['t']), ONE))) is not None):
                viol.append((w, e, f'mixed h={h}'))
            if abs2(tau) not in S:
                viol.append((w, e, 'mixed modulus'))
    pred = (Fr((tr * tr + tr - 1) ** 2, 5) ** 2, Fr(0))
    if base_prod != pred:
        viol.append((w, None, f'base product {base_prod} != {pred}'))
    rec['base_prod_abs'] = str(Fr((tr * tr + tr - 1) ** 2, 5))
    rec['n_fibre_k0'] = nfib
    rec['n_mixed'] = nmixed
    records.append(rec)
    stats['members'] += 1
    stats[f'dimH1F5={dimH1}'] += 1
    stats['mult_one' if mult_one else 'eps*W = I mod 5'] += 1
    stats['5 | tors'] += int(any(isinstance(x, int) and x % 5 == 0 for x in tors))
    stats['base product == 5'] += int(Fr((tr * tr + tr - 1) ** 2, 5) == 5)
    stats['golden field (disc = 5 * square)'] += 0

import math
golden = sum(1 for r in records if (lambda d: d > 0 and d % 5 == 0 and int(math.isqrt(d // 5)) ** 2 == d // 5)(r['trace'] ** 2 - 4))
print('stats:', dict(stats))
print(f'members whose trace field is Q(sqrt5): {golden}; non-golden: {len(records) - golden}')
print('members with base product 5:', [r['word'] + ('(+)' if r['eps'] == 1 else '(-)') for r in records
                                      if Fr(r['base_prod_abs']) == 5])
print('violations:', len(viol))
for v in viol[:20]:
    print('  ', v)
listed = ['b+-LR', 'b++LLLRLL', 'b+-RRRRRLR', 'b++LLLLLLRLR', 'b+-RRRRLRRLLR', 'b++LLLLLLLRRLLR', 'b++LLLLLRLLRRLR']
for nm in listed:
    sgn = 1 if nm[2] == '+' else -1
    w = nm[3:]
    ok = eps_of(mat_word(w), True) == sgn
    can = min(rotations(w))
    inC = any(c == can for c, _ in cT)
    print(f'  lane-listed {nm}: this rotation has eps = {eps_of(mat_word(w), True)} (sign in name {sgn}); '
          f'necklace in my census: {inC}')
json.dump(dict(census_size=len(cT), census_size_untransposed=len(cN), stats=dict(stats), violations=len(viol),
               records=records), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'run2_census.json'), 'w'),
          indent=1)
