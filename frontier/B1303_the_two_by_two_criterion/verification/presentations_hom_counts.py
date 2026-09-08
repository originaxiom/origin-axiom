#!/usr/bin/env python3
"""Which presentation is pi_1(Y_n)?  Count homomorphisms to small groups from (i) the fixed quotient of phi^n,
(ii) the fixed quotient of phi'^n (phi' = c_{a^-1} o phi, boundary-fixing), (iii) B1274's Reidemeister-Schreier
presentation of the branched cover."""
import sys, itertools, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'frontier' / 'B1274_the_tower_and_its_doubles' / 'verification'))
sys.path.insert(0, str(ROOT / 'frontier' / 'B1267_spectrum_law_rebuilt' / 'verification'))
sys.path.insert(0, str(ROOT / 'frontier' / 'B1268_cusped_net_chirality_bound' / 'verification'))
sys.path.insert(0, str(ROOT / 'frontier' / 'B1269_transport_computed' / 'verification'))
sys.path.insert(0, str(ROOT / 'frontier' / 'B1273_the_three_fold_closing' / 'verification'))
import tower_and_doubles as TW
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup

# free-group words as lists of +-1 (a), +-2 (b)
def inv(w): return [-x for x in reversed(w)]
def phi(w):                       # a -> a a b, b -> a b
    out = []
    for x in w:
        img = {1: [1, 1, 2], 2: [1, 2]}[abs(x)]
        out += img if x > 0 else inv(img)
    return out
def phi_prime(w):                 # c_{a^-1} o phi: x -> a^-1 phi(x) a
    return [-1] + phi(w) + [1]
def power(f, n, w):
    for _ in range(n): w = f(w)
    return w
def reduce_word(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out

def hom_count(gens_n, rels, G):
    elems = list(G.elements)
    cnt = 0
    for imgs in itertools.product(elems, repeat=gens_n):
        ok = True
        for r in rels:
            p = Permutation(G.degree - 1)
            for x in r:
                g = imgs[abs(x) - 1]
                p = p * (g if x > 0 else g ** -1)
            if not p.is_Identity:
                ok = False; break
        cnt += ok
    return cnt

groups = {'S3': SymmetricGroup(3), 'A4': AlternatingGroup(4), 'S4': SymmetricGroup(4), 'A5': AlternatingGroup(5)}
for n in (2, 3, 4, 5):
    rels_i = [reduce_word(power(phi, n, [1]) + [-1]), reduce_word(power(phi, n, [2]) + [-2])]
    rels_ii = [reduce_word(power(phi_prime, n, [1]) + [-1]), reduce_word(power(phi_prime, n, [2]) + [-2])]
    gens, rels_iii = TW.presentation(n, branched=True)
    row = []
    for name, G in groups.items():
        if len(gens) > 4 and name in ('A5', 'S4'):
            row.append(f"{name}: (i) {hom_count(2, rels_i, G)} (ii) {hom_count(2, rels_ii, G)} (iii) skipped"); continue
        row.append(f"{name}: (i) {hom_count(2, rels_i, G)} (ii) {hom_count(2, rels_ii, G)} (iii) {hom_count(len(gens), rels_iii, G)}")
    print(f"n = {n}: " + "; ".join(row), flush=True)
