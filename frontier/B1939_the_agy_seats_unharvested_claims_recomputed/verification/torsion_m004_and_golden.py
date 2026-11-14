"""Run 1: core self-checks; R1 on m004 (base characters); R2 on the golden word's mark-preserving bundle; plants P1-P5."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from tcore import *

FAIL = []


def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name)
    if not cond:
        FAIL.append(name)
    return cond


def fmt(pq):
    p, q = pq
    return f"{p} + ({q})*sqrt5"


# ---- core self-checks
z = zpow(1)
check('zeta^5 = 1', is0(sub(mul(mul(mul(mul(z, z), z), z), z), ONE)))
check('1+z+z2+z3+z4 = 0', is0(add_all([zpow(i) for i in range(5)])))
S1 = (Fr(5, 2), Fr(-1, 2))   # |1-zeta|^2 = (5-sqrt5)/2 = (2 sin pi/5)^2
S2 = (Fr(5, 2), Fr(1, 2))    # |1-zeta^2|^2 = (5+sqrt5)/2 = (2 sin 2pi/5)^2
check('|1-zeta|^2 = (5-sqrt5)/2', abs2(sub(ONE, zpow(1))) == S1)
check('|1-zeta^2|^2 = (5+sqrt5)/2', abs2(sub(ONE, zpow(2))) == S2)
check('norm(1-zeta) = 5 = Phi_5(1)', norm(sub(ONE, zpow(1))) == 5)
import math
check('numeric 2sin(pi/5)^2', abs((2 * math.sin(math.pi / 5)) ** 2 - (2.5 - 0.5 * 5 ** 0.5)) < 1e-14)

# ---- automorphisms fix [a,b] exactly, abelianisations match
for name, phi in [('L', PHI['L']), ('R', PHI['R']), ('iota_fix', IOTA_FIX)]:
    check(f'{name} fixes [a,b] exactly', subst(phi, COMM) == COMM)
check('iota_naive does NOT fix [a,b] exactly (only up to conjugacy)', subst(IOTA_NAIVE, COMM) != COMM)
for w in ['LR', 'LLR', 'LRR', 'LLLLLRLLRR', 'LLLLLRLLRRLR']:
    for eps in (1, -1):
        check(f'abel(phi_{w},{eps}) = eps*W_col', abel(phi_word(w, eps)) == mat_word(w, eps))
        check(f'phi_{w},{eps} fixes [a,b]', subst(phi_word(w, eps), COMM) == COMM)

# ================= R1: m004 = b++LR, base characters t -> zeta^k
print('\n=== R1: m004 (monodromy +LR), characters of pi_1 through H_1 = Z')
W = 'LR'
gens, rels = hnn(phi_word(W, 1))
chars = characters(gens, rels)
check('m004: exactly 5 characters to mu_5 (H_1 = Z)', len(chars) == 5)
check('m004: all characters fibre-trivial', all(e['a'] == 0 and e['b'] == 0 for e in chars))


def milnor(k, tr=3, dt=1):
    x = zpow(k)
    D = add(sub(mul(x, x), scal(tr, x)), scal(dt, ONE))   # x^2 - tr x + det
    return div(D, sub(x, ONE)), D


r1 = {}
prod_abs2 = (Fr(1), Fr(0))


def qmul(u, v):
    return (u[0] * v[0] + 5 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])


for e in sorted(chars, key=lambda e: e['t']):
    k = e['t']
    J, d1, h, ok = complex_data(gens, rels, e)
    check(f'm004 k={k}: d1 o d2 = 0', ok)
    if k == 0:
        print(f'  k=0: trivial character, homology dims (H0,H1,H2) = {h}  -> not acyclic')
        check('m004 k=0 not acyclic (H0 = 1)', h[0] == 1)
        continue
    tau, j = wada(gens, rels, e)
    mt, D = milnor(k)
    u = unit_root(div(tau, mt))
    a2 = abs2(tau)
    r1[k] = a2
    prod_abs2 = qmul(prod_abs2, a2)
    print(f'  k={k}: H = {h}; Wada tau = {[str(c) for c in tau[:4]]}; |tau|^2 = {fmt(a2)} '
          f'~ {abs(to_complex(tau)):.12f}; tau / (Delta(z)/(z-1)) = {u}')
    check(f'm004 k={k} acyclic', h == (0, 0, 0))
    check(f'm004 k={k}: Wada = Milnor Delta(zeta^k)/(zeta^k-1) up to +-zeta^m', u is not None)
    claim = S1 if k in (1, 4) else S2
    print(f'      claimed |tau|^2 = (2 sin(pi k/5))^2 = {fmt(claim)};  equal? {a2 == claim}')
print(f'  product over k=1..4 of |tau_k|^2 = {fmt(prod_abs2)}  (so product of |tau_k| = sqrt of it)')
check('R1 product of |tau|^2 = (121/5)^2', prod_abs2 == (Fr(121, 5) ** 2, Fr(0)))
check('R1 |tau_1|^2 = 5 - 2 sqrt5/5', r1[1] == (Fr(5), Fr(-2, 5)))
check('R1 |tau_2|^2 = 5 + 2 sqrt5/5', r1[2] == (Fr(5), Fr(2, 5)))
P5 = all(r1[k] == (S1 if k in (1, 4) else S2) for k in (1, 2, 3, 4))
print(f'PLANT P5 (the claimed moduli 2 sin(pi k/5) applied to m004 base characters) holds? {P5} -> '
      f'{"NOT CAUGHT" if P5 else "CAUGHT (claim fails on m004)"}')

# ---- P2: planted wrong Fox derivative must break the Milnor match
bad = []
for e in chars:
    if e['t'] == 0:
        continue
    tau, j = wada(gens, rels, e, planted_bad_inverse=True)
    mt, D = milnor(e['t'])
    bad.append(unit_root(div(tau, mt)) is None if not is0(tau) else True)
print(f'PLANT P2 (wrong d(g^-1)/dg): Milnor match broken on {sum(bad)} of 4 characters -> '
      f'{"CAUGHT" if any(bad) else "NOT CAUGHT"}')
P2_caught = any(bad)

# ---- P1: non-golden monodromy [[3,1],[2,1]] = L R R (trace 4)
print('\n=== PLANT P1: non-golden monodromy [[3,1],[2,1]] = LRR (trace 4)')
check('LRR_col = [[3,1],[2,1]]', mat_word('LRR') == ((3, 1), (2, 1)))
g1, r1s = hnn(phi_word('LRR', 1))
ch1 = characters(g1, r1s)
print(f'  characters to mu_5: {len(ch1)} (all fibre-trivial: {all(e["a"]==0 and e["b"]==0 for e in ch1)})')
diff = []
for e in ch1:
    if e['t'] == 0:
        continue
    tau, _ = wada(g1, r1s, e)
    a2 = abs2(tau)
    mt, _ = milnor(e['t'], tr=4)
    print(f'  k={e["t"]}: |tau|^2 = {fmt(a2)}; Milnor(trace 4) match: {unit_root(div(tau, mt)) is not None}; '
          f'equal to LR value? {a2 == r1[e["t"]]}')
    diff.append(a2 != r1[e['t']])
P1_caught = all(diff)
print(f'PLANT P1: trace-4 base torsions differ from LR at all four k -> {"CAUGHT" if P1_caught else "NOT CAUGHT"}')

# ================= R2: the golden word's mark-preserving bundle
print('\n=== R2: the mark-preserving bundle of the golden word LR')
M = mat_word('LR')
v = (1, 2)
MT_v = tuple(sum(M[k][i] * v[k] for k in range(2)) % 5 for i in range(2))
eps = 1 if MT_v == v else (-1 if MT_v == tuple((-x) % 5 for x in v) else 0)
print(f'  LR_col^T v5 = {MT_v} mod 5  -> eps = {eps}  (lane: b+-LR glued by -LR)')
check('golden word LR has eps = -1', eps == -1)
gens, rels = hnn(phi_word('LR', -1))
check('t commutes with [a,b] (longitude = t)', subst(phi_word('LR', -1), COMM) == COMM)
chars = characters(gens, rels)
print(f'  characters to mu_5: {len(chars)} (H^1(M;F_5) dim = {round(math.log(len(chars), 5))})')
fib = [e for e in chars if (e['a'], e['b']) != (0, 0)]
print(f'  fibre values of fibre-nontrivial characters (a,b) mod 5: {sorted(set((e["a"], e["b"]) for e in fib))}')


def classify(e):
    f = (e['a'], e['b']) != (0, 0)
    tt = e['t'] != 0
    if not f and not tt:
        return 'trivial'
    if not f:
        return 'base'
    if not tt:
        return 'fibre(k=0)'
    return 'mixed'


def r2_table(word, eps, verbose=True, naive=False, label_by_t=True):
    phi = phi_word(word, eps, naive_iota=naive)
    gens, rels = hnn(phi)
    chars = characters(gens, rels)
    rows = []
    for e in chars:
        c = classify(e)
        if c == 'trivial':
            continue
        J, d1, h, ok = complex_data(gens, rels, e)
        assert ok
        tau, j = wada(gens, rels, e)
        rows.append((c, e, h, tau))
    return gens, rels, chars, rows


gens, rels, chars, rows = r2_table('LR', -1)
lines = {}
for c, e, h, tau in rows:
    acyc = h == (0, 0, 0)
    if c in ('fibre(k=0)', 'mixed'):
        # tau should be +-zeta^m (rho(t)-1)
        u = unit_root(div(tau, sub(zpow(e['t']), ONE))) if not is0(tau) else None
        print(f'  {c:10s} rho=(a,b,t)=({e["a"]},{e["b"]},{e["t"]}) H={h} acyclic={acyc} '
              f'|tau|^2={fmt(abs2(tau)) if not is0(tau) else "0 (Wada numerator vanishes)"} '
              f'tau/(rho(l)-1)={u}')
    else:
        a2 = abs2(tau)
        print(f'  {c:10s} rho=(a,b,t)=({e["a"]},{e["b"]},{e["t"]}) H={h} acyclic={acyc} |tau|^2={fmt(a2)} '
              f'~{abs(to_complex(tau)):.10f}')

fibre_ok = all(h == (0, 1, 1) and is0(tau) for c, e, h, tau in rows if c == 'fibre(k=0)')
mixed_ok = all(h == (0, 0, 0) and unit_root(div(tau, sub(zpow(e['t']), ONE))) is not None
               for c, e, h, tau in rows if c == 'mixed')
check('R2 b+-LR: fibre line (k=0) non-acyclic, H=(0,1,1), Wada numerator 0', fibre_ok)
check('R2 b+-LR: every mixed character acyclic with tau = +-zeta^m (rho(l)-1)', mixed_ok)
# product over each projective mixed line
from collections import defaultdict
L = defaultdict(list)
for c, e, h, tau in rows:
    if c == 'mixed':
        # projective class: normalise so that a-value (or b) = 1
        q = e['a'] if e['a'] else e['b']
        qi = pow(q, -1, 5)
        key = (e['a'] * qi % 5, e['b'] * qi % 5, e['t'] * qi % 5)
        L[key].append(tau)
for key, taus in sorted(L.items()):
    p = (Fr(1), Fr(0))
    for t_ in taus:
        p = qmul(p, abs2(t_))
    print(f'  mixed line {key}: {len(taus)} charges, product |tau|^2 = {fmt(p)}')
    check(f'mixed line {key}: product of |tau| = 5', p == (Fr(25), Fr(0)))
# base line product
pb = (Fr(1), Fr(0))
for c, e, h, tau in rows:
    if c == 'base':
        pb = qmul(pb, abs2(tau))
print(f'  base line [beta]: product |tau|^2 = {fmt(pb)} (E3 predicts ((t^2+t-1)^2/5)^2 with t=-3: 25)')
check('base line product of |tau| = 5 at t=-3 (coincidence)', pb == (Fr(25), Fr(0)))
base_moduli_claimed = all(abs2(tau) in (S1, S2) for c, e, h, tau in rows if c == 'base')
print(f'  base line individual moduli equal 2 sin(pi k/5)? {base_moduli_claimed}')

# ---- P3: naive iota (t not the longitude), label by rho(t)
print('\n=== PLANT P3: -I as a->a^-1, b->b^-1 (t is not the longitude), k read from rho(t)')
gens3, rels3 = hnn(phi_word('LR', -1, naive_iota=True))
ch3 = characters(gens3, rels3)
bad_label = 0
for e in ch3:
    if (e['a'], e['b']) == (0, 0):
        continue
    J, d1, h, ok = complex_data(gens3, rels3, e)
    acyc = h == (0, 0, 0)
    label0 = e['t'] == 0
    if acyc == label0:   # the rule "non-acyclic exactly when label 0" violated
        bad_label += 1
    # the true longitude here is (b a) t
    l_true = (e['a'] + e['b'] + e['t']) % 5
    assert (l_true == 0) == (not acyc), (e, h)
print(f'  fibre-nontrivial characters violating "non-acyclic iff rho(t)=1": {bad_label}; '
      f'all obey "non-acyclic iff rho(ba t)=1" (true longitude) -> {"CAUGHT" if bad_label else "NOT CAUGHT"}')
P3_caught = bad_label > 0

# ---- P4: a non-homomorphism must be rejected
e_bad = {'a': 1, 'b': 1, 't': 0}
P4_caught = not all(expsum(r, e_bad) == 0 for r in rels)
print(f'PLANT P4: (a,b,t)=(1,1,0) on b+-LR is not a homomorphism -> {"CAUGHT" if P4_caught else "NOT CAUGHT"}')

print('\nSUMMARY: fails =', FAIL)
print(f'PLANTS: P1 {"caught" if P1_caught else "MISSED"}, P2 {"caught" if P2_caught else "MISSED"}, '
      f'P3 {"caught" if P3_caught else "MISSED"}, P4 {"caught" if P4_caught else "MISSED"}, '
      f'P5 {"caught" if not P5 else "MISSED"}')
