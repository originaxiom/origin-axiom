"""B1420 A5 (scale check): does ANY firing module in B1418's record have a self-inverse twist (psi^2 = 1)?

The lemma says none can: rho has det 1 by construction, so J rho J^-1 = (rho^-1)^T, Sym^m(rho) is self-dual,
V* = Sym^m(rho) (x) psi^-1, and psi^2 = 1 forces V = V* hence I = n(V) - n(V*) = 0.
Twist labels come in two forms: explicit coefficient tuples, and 'psi=chi^j' (j = 1,2,3) where chi is the locus
character, whose tuples are in the locus label.  Both are evaluated here in the run's own number field.
Run: python3 firing_twists.py"""
import json, re, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'B1418_the_family_as_the_object' / 'verification'))
from c2_reducible_index import NF
from fractions import Fraction

FIELDS = {'m004': NF([-1, -1, 1]), 'default': NF([1, 0, -1, 0, 1])}     # Q(phi) for the m004 run, Q(zeta_12) for the class

def parse_tuples(s):
    return {g: tuple(Fraction(x.strip().strip("'")) for x in v.split(','))
            for g, v in re.findall(r"([a-z]):\(([^)]*)\)", s)}

def is_one(K, e):  return K.is_zero(K.sub(e, K.const(1)))

def order_of(K, e, cap=24):
    p = K.const(1)
    for k in range(1, cap + 1):
        p = K.mul(p, e)
        if is_one(K, p): return k
    return None

d = json.load(open(pathlib.Path(__file__).resolve().parents[2] / 'B1418_the_family_as_the_object' / 'verification' / 'c2_modules_compact.json'))
tot = firing = 0; violations = []; orders = collections.Counter()
for name, mods in d.items():
    K = FIELDS.get(name, FIELDS['default'])
    for rec in mods:
        tot += 1
        if rec.get('I') in (0, None): continue
        firing += 1
        chi = {g: K.el(list(v)) for g, v in parse_tuples(rec['locus']).items()}
        tw = rec['twist']
        mj = re.match(r'psi=chi\^(\d+)$', tw)
        psi = {g: K.pw(chi[g], int(mj.group(1))) for g in chi} if mj else {g: K.el(list(v)) for g, v in parse_tuples(tw).items()}
        sq_is_one = all(is_one(K, K.mul(psi[g], psi[g])) for g in psi)
        orders[tuple(sorted(order_of(K, psi[g]) or 0 for g in psi))] += 1
        if sq_is_one: violations.append((name, rec['m'], tw, rec['I']))
print('modules recorded: %d   firing (I != 0): %d' % (tot, firing))
print('firing modules with psi^2 = 1 (each would refute the lemma): %d' % len(violations), violations[:4])
print('orders of psi on the generators, over the firing modules:', dict(orders))
