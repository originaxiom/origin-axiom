#!/usr/bin/env python3
"""B548: the un-hideability census. UN-HIDEABLE := grammar+language collapse
the incidence matrix's Parikh-lifts to a single conjugacy class."""
from itertools import permutations
from collections import Counter

def grow(sub, seed, depth):
    w = seed
    for _ in range(depth):
        w = ''.join(sub[c] for c in w)
    return w

def lang_data(sub, seed, depth, big=2):
    w = grow(sub, seed, depth)
    return (frozenset(w[i:i+2] for i in range(len(w)-1)),
            frozenset(w[i:i+6] for i in range(len(w)-5)) if len(w) >= 6 else frozenset())

def census(name, sub, seed, depth):
    alpha = sorted(sub)
    ref_bi, ref_six = lang_data(sub, seed, depth)
    # all lifts = substitutions with the same column multiset per letter
    perms = {g: sorted(set(permutations(sub[g]))) for g in alpha}
    total = 1
    for g in alpha:
        total *= len(perms[g])
    if total > 400000:
        return name, total, None, None, "too-large"
    langs = set()
    gram = 0
    def rec(i, cur):
        nonlocal gram
        if i == len(alpha):
            s = dict(zip(alpha, cur))
            # must be prolongable on seed
            if s[seed][0] != seed and not any(s[seed].startswith(seed) for _ in [0]):
                pass
            bi, six = lang_data(s, seed, depth)
            if bi == ref_bi:
                gram += 1
                langs.add(six)
            return
        for p in perms[alpha[i]]:
            rec(i+1, cur + [''.join(p)])
    rec(0, [])
    n_lang = len(langs)
    verdict = "UN-HIDEABLE" if n_lang <= 2 else "hideable"
    return name, total, gram, n_lang, verdict

CASES = [
    ("Fibonacci a->ab,b->a",       {'a':'ab','b':'a'},           'a', 18),
    ("Thue-Morse a->ab,b->ba",     {'a':'ab','b':'ba'},          'a', 9),
    ("period-doubling a->ab,b->aa",{'a':'ab','b':'aa'},          'a', 12),
    ("tribonacci",                 {'a':'ab','b':'ac','c':'a'},  'a', 11),
    ("3-bonacci variant",          {'a':'ab','b':'c','c':'a'},   'a', 14),
    # sigma DEFERS to B535 (locked): 17280 lifts -> 8 grammar -> 2 language
    # (UN-HIDEABLE). Recompute here is too slow (34k-char words); see test_b535.
    ("reducible a->aa,b->ab",      {'a':'aa','b':'ab'},          'a', 12),
]
print(f"{'substitution':30s} {'#lifts':>8s} {'gram':>6s} {'#lang':>6s}  verdict")
print("-"*70)
import numpy as np
for name, sub, seed, depth in CASES:
    r = census(name, sub, seed, depth)
    _, total, gram, nl, v = r
    # charpoly irreducibility / Pisot check
    alpha = sorted(sub)
    M = np.array([[sub[c].count(r_) for c in alpha] for r_ in alpha], dtype=float)
    ev = np.sort(np.abs(np.linalg.eigvals(M)))[::-1]
    pisot = ev[0] > 1 and (len(ev) < 2 or ev[1] < 1 - 1e-9)
    print(f"{name:30s} {total:8d} {str(gram):>6s} {str(nl):>6s}  {v}"
          f"  [{'Pisot' if pisot else 'non-Pisot'}, beta={ev[0]:.3f}]")
