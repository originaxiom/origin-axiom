"""Route A (verifier's own): census rebuilt from scratch; HNN presentation with NAIVE automorphism lifts
(L: a->a, b->ab; R: a->ba, b->b; -I: a->A, b->B) that fix [a,b] only up to conjugacy. The longitude is
l = g^-1 t where phi([a,b]) = g [a,b] g^-1. k is read from rho(l). Plants Q1-Q4."""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from itertools import product as iprod
from collections import Counter, defaultdict
from vcore import *

MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 12
COMM = 'abAB'
NAIVE = {'L': {'a': 'a', 'b': 'ab'}, 'R': {'a': 'ba', 'b': 'b'}}
MINUS_I = {'a': 'A', 'b': 'B'}
S_CLAIM = {(Fr(5, 2), Fr(-1, 2)), (Fr(5, 2), Fr(1, 2))}   # (2 sin pi/5)^2, (2 sin 2pi/5)^2


def ab_matrix(phi):
    """columns = images of a, b in H_1(F)"""
    ca = (phi['a'].count('a') - phi['a'].count('A'), phi['a'].count('b') - phi['a'].count('B'))
    cb = (phi['b'].count('a') - phi['b'].count('A'), phi['b'].count('b') - phi['b'].count('B'))
    return ((ca[0], cb[0]), (ca[1], cb[1]))


def phi_of(word, eps):
    phi = {'a': 'a', 'b': 'b'}
    for ch in word:                       # phi = phi_w1 o phi_w2 o ... : build right to left by post-composition
        phi = fcompose(phi, NAIVE[ch])    # (phi o phi_ch)
    if eps == -1:
        phi = fcompose(MINUS_I, phi)
    return phi


def bundle(word, eps):
    phi = phi_of(word, eps)
    assert ab_matrix(phi) == matw(word, eps), (word, eps, ab_matrix(phi), matw(word, eps))
    img = fsubst(phi, COMM)
    g = conjugator(img, COMM)
    assert g is not None and fred(g + COMM + finv(g)) == img, (word, eps, img)
    rels = [fred('t' + x + 'T' + finv(phi[x])) for x in ('a', 'b')]
    lon = fred(finv(g) + 't')
    return ['a', 'b', 't'], rels, lon, g, phi


def census(maxlen, transpose=True):
    seen = set()
    out = []
    for n in range(2, maxlen + 1):
        for tup in iprod('LR', repeat=n):
            w = ''.join(tup)
            if 'L' not in w or 'R' not in w:
                continue
            rots = [w[i:] + w[:i] for i in range(n)]
            can = min(rots)
            if can in seen:
                continue
            seen.add(can)
            if any(can == can[d:] + can[:d] for d in range(1, n) if n % d == 0):
                continue      # not primitive
            hits = []
            for r in sorted(set(rots)):
                M = matw(r)
                if not transpose:
                    M = ((M[0][0], M[1][0]), (M[0][1], M[1][1]))
                e = eps_mark(M)
                if e:
                    hits.append((r, e))
            if hits:
                out.append((can, hits[0]))
    return out


def analyse(word, eps, label_by='l', plant=None):
    gens, rels, lon, g, phi = bundle(word, eps)
    res = dict(base=[], fib0=[], mixed=[], viol=[])
    for e in chars(gens, rels):
        fib = (e['a'], e['b']) != (0, 0)
        if not fib and e['t'] == 0:
            continue
        J, d1, H, ok = twisted(gens, rels, e, plant)
        if not ok:
            res['viol'].append(('chain', e))
        hol = expo(lon, e) if label_by == 'l' else e['t']
        cands = [j for j, x in enumerate(gens) if e[x] != 0]
        mins = {j: minors(J, j) for j in cands}
        # Wada independence of the dropped column: minor_j (rho(g_k)-1) = +- zeta^m minor_k (rho(g_j)-1)
        for j in cands:
            for k in cands:
                if k > j:
                    lhs = gmul(mins[j], gsub(zp(e[gens[k]]), ONE))
                    rhs = gmul(mins[k], gsub(zp(e[gens[j]]), ONE))
                    if giszero(lhs) != giszero(rhs) or (not giszero(lhs) and unit_multiple(lhs, rhs) is None):
                        res['viol'].append(('column dependence', e))
        j = cands[-1]
        mn = mins[j]
        den = gsub(zp(e[gens[j]]), ONE)
        tau_abs2 = None if giszero(mn) else q5div(abs2(mn), abs2(den))
        rec = dict(e=(e['a'], e['b'], e['t']), H=H, hol=hol, tau_abs2=tau_abs2)
        if not fib:
            # Milnor: tau = Delta(z)/(z-1), Delta = z^2 - tr z + 1 with tr = trace(eps W); minor (with t column
            # dropped) must be +- zeta^m Delta(z)
            M = matw(word, eps)
            tr = M[0][0] + M[1][1]
            z = zp(e['t'])
            Delta = gadd(gsub(gmul(z, z), gscale(tr, z)), ONE)
            mt = minors(J, 2)
            rec['milnor'] = unit_multiple(mt, Delta) is not None
            if not rec['milnor']:
                res['viol'].append(('milnor', e))
            if H != (0, 0, 0):
                res['viol'].append(('base not acyclic', e))
            res['base'].append(rec)
        elif hol == 0:
            if not (H == (0, 1, 1) and tau_abs2 is None):
                res['viol'].append(('fibre k=0', e, H, tau_abs2))
            res['fib0'].append(rec)
        else:
            # claim: tau = +- zeta^m (rho(l) - 1): minor_j = +- zeta^m (rho(l)-1)(rho(g_j)-1)
            target = gmul(gsub(zp(hol), ONE), den)
            if not (H == (0, 0, 0) and unit_multiple(mn, target) is not None):
                res['viol'].append(('mixed identity', e, H))
            if tau_abs2 not in S_CLAIM:
                res['viol'].append(('mixed modulus', e, tau_abs2))
            res['mixed'].append(rec)
    return res


def line_products(recs):
    """group characters into projective lines (e ~ q e) and multiply |tau|^2 over each line."""
    lines = defaultdict(list)
    for r in recs:
        e = r['e']
        q = next(x for x in e if x)
        qi = pow(q, -1, 5)
        lines[tuple((x * qi) % 5 for x in e)].append(r['tau_abs2'])
    out = {}
    for key, vals in lines.items():
        p = (Fr(1), Fr(0))
        for v in vals:
            p = q5mul(p, v)
        out[key] = (len(vals), p)
    return out


if __name__ == '__main__':
    print('=== census rebuilt (own code)')
    C = census(MAXLEN, True)
    C2 = census(MAXLEN, False)
    print(f'necklaces with a rotation W_col^T v5 = +-v5: {len(C)};  with W_col v5 = +-v5: {len(C2)}; '
          f'same set: {set(c for c, _ in C) == set(c for c, _ in C2)}')
    print('by length:', dict(sorted(Counter(len(c) for c, _ in C).items())))
    excep = [(w, e) for _, (w, e) in C if all(((matw(w, e)[i][j] - (i == j)) % 5 == 0) for i in range(2) for j in range(2))]
    print(f'members with eps*W = I mod 5: {len(excep)}: {excep}')

    print('\n=== R1: m004 = +LR (task card reading)')
    r = analyse('LR', 1)
    for rec in r['base']:
        print(f"  k={rec['e'][2]}: H={rec['H']} |tau|^2 = {rec['tau_abs2'][0]} + ({rec['tau_abs2'][1]}) sqrt5 "
              f"~ |tau| = {q5float(rec['tau_abs2']) ** 0.5:.12f}; Milnor match {rec['milnor']}")
    p = (Fr(1), Fr(0))
    for rec in r['base']:
        p = q5mul(p, rec['tau_abs2'])
    print(f'  product over k=1..4 of |tau|^2 = {p}  -> product of |tau| = {p[0]} ** 0.5 = 121/5? {p == (Fr(121, 5) ** 2, 0)}')
    print(f'  any base modulus equal to 2 sin(pi k/5)? {any(rec["tau_abs2"] in S_CLAIM for rec in r["base"])}')
    print(f'  fibre-nontrivial characters on m004: {len(r["fib0"]) + len(r["mixed"])}; violations {r["viol"]}')

    print('\n=== R2: b+-LR (golden word, eps from the mark)')
    print('  eps of LR:', eps_mark(matw('LR')))
    gens, rels, lon, g, phi = bundle('LR', -1)
    print(f'  naive phi = {phi}; phi([a,b]) = {fsubst(phi, COMM)}; conjugator g = {g}; longitude l = {lon}')
    r = analyse('LR', -1)
    print(f"  #base {len(r['base'])}, #fibre k=0 {len(r['fib0'])}, #mixed {len(r['mixed'])}, violations {len(r['viol'])}")
    for rec in r['fib0']:
        print(f"   fibre k=0 e={rec['e']} H={rec['H']} tau=0(numerator vanishes): {rec['tau_abs2'] is None}")
    for key, (n, p) in sorted(line_products(r['mixed']).items()):
        print(f'   mixed line {key}: {n} charges, product |tau|^2 = {p}')
    for key, (n, p) in sorted(line_products(r['base']).items()):
        print(f'   base line {key}: {n} charges, product |tau|^2 = {p}; individual |tau|^2 = '
              f"{[rec['tau_abs2'] for rec in r['base']]}")

    print('\n=== whole census, route A')
    tot = Counter()
    viol = []
    nongold_mixed_same = 0
    nongold = 0
    for can, (w, e) in C:
        r = analyse(w, e)
        tot['members'] += 1
        tot[(len(r['base']), len(r['fib0']), len(r['mixed']))] += 1
        viol += [(w, e, v) for v in r['viol']]
        tr = matw(w, e)[0][0] + matw(w, e)[1][1]
        d = tr * tr - 4
        golden = d % 5 == 0 and math.isqrt(d // 5) ** 2 == d // 5
        if not golden:
            nongold += 1
            if all(rec['tau_abs2'] in S_CLAIM for rec in r['mixed']) and r['mixed']:
                nongold_mixed_same += 1
        pb = (Fr(1), Fr(0))
        for rec in r['base']:
            pb = q5mul(pb, rec['tau_abs2'])
        if pb != (Fr((tr * tr + tr - 1) ** 2, 5) ** 2, 0):
            viol.append((w, e, 'base product formula'))
        tot['base product = 5'] += int(pb == (Fr(25), Fr(0)))
    print(' ', dict(tot))
    print(f'  violations: {len(viol)}', viol[:10])
    print(f'  non-golden members (eigenvalue field != Q(sqrt5)): {nongold}; of them with mixed moduli exactly the '
          f'claimed set: {nongold_mixed_same}')

    print('\n=== PLANTS')
    # Q1: non-golden monodromy LRR, eps=+1 (task card's control)
    r1 = analyse('LRR', 1)
    rLR = analyse('LR', 1)
    a = {rec['e'][2]: rec['tau_abs2'] for rec in r1['base']}
    b = {rec['e'][2]: rec['tau_abs2'] for rec in rLR['base']}
    diff = sum(1 for k in a if a[k] != b[k])
    print(f'  Q1 LRR (trace 4) base |tau|^2: {a}; differs from LR at {diff}/4 -> {"CAUGHT" if diff else "NOT CAUGHT"}')
    print(f'     LRR has fibre characters mod 5? {len(r1["fib0"]) + len(r1["mixed"])} (H_1 tors = coker(LRR - I))')
    # Q2: label k by rho(t) instead of rho(l)
    bad = 0
    tested = 0
    for can, (w, e) in C[:60]:
        r = analyse(w, e, label_by='t')
        tested += 1
        bad += int(bool(r['viol']))
    print(f'  Q2 (k read from rho(t), naive lifts): members with violations {bad}/{tested} -> '
          f'{"CAUGHT" if bad else "NOT CAUGHT"}')
    # Q3: wrong Fox rule on b+-LR (fibre characters carry rho != 1 on a, b)
    r3 = analyse('LR', -1, plant='sign')
    print(f'  Q3 (d(g^-1)/dg = +g^-1) on b+-LR: violations {len(r3["viol"])} '
          f'(kinds {sorted(Counter(v[0] for v in r3["viol"]).items())}) -> {"CAUGHT" if r3["viol"] else "NOT CAUGHT"}')
    # Q4: wrong mark (1,3) as fibre values on b+-LR
    gens, rels, lon, g, phi = bundle('LR', -1)
    e_bad = {'a': 1, 'b': 3, 't': 0}
    is_hom = all(expo(rr, e_bad) == 0 for rr in rels)
    print(f'  Q4 fibre values (1,3) on b+-LR is a homomorphism? {is_hom} -> {"NOT CAUGHT" if is_hom else "CAUGHT"}')
    json.dump(dict(census=[(c, w, e) for c, (w, e) in C]), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v1_census.json'), 'w'))
