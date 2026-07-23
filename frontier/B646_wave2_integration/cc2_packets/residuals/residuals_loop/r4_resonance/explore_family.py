"""
R4 -- DESIGN-STAGE EXPLORATION ONLY. Not part of the sealed record; no nesting cost is
computed anywhere in this file. Purpose: search a deterministic parametric family for 8
primitive substitutions spanning Perron root ~1.8 to ~4.2, with some decoupling between
the two candidate predictors (Perron root vs rotating-pair image-length sum), before
hand-selecting the 8 that go into the sealed prediction file.

FAMILY ("coupled Fibonacci-type", the recipe stated exactly):
  a -> 'a'*ia + 'A'*ja + 'b'
  A -> 'A'*iA + 'a'*jA + 'B'
  b -> bimg   (short, deterministic)
  B -> Bimg   (short, deterministic)
Backbone 4-cycle a->b->A->B->a (from the fixed trailing 'b'/'B' suffixes and b->A, B->a)
guarantees irreducibility for ANY (ia,ja,iA,jA); self-loops (ia>=1 or iA>=1) or the 3-cycles
created by ja>=1 / jA>=1 break the pure period-4 case, giving primitivity (checked, not
just argued, below).
"""
import itertools
import sys
import os

sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/veins/v2_resonance')
import numpy as np
import lib as L

def make_sub(ia, ja, iA, jA, bimg='A', Bimg='a'):
    a_img = 'a' * ia + 'A' * ja + 'b'
    A_img = 'A' * iA + 'a' * jA + 'B'
    return {'a': a_img, 'A': A_img, 'b': bimg, 'B': Bimg}

def perron(sub):
    M = L.incidence_matrix(sub)
    ev = np.linalg.eigvals(M)
    return float(ev[np.argmax(np.abs(ev))].real), M

rows = []
for ia in range(0, 5):
    for ja in range(0, 4):
        for iA in range(0, 5):
            for jA in range(0, 4):
                if ia + ja == 0 or iA + jA == 0:
                    continue  # a or A image would be just the bare suffix; keep some content
                for bimg, Bimg in [('A', 'a'), ('Ab', 'aB'), ('AB', 'aB')]:
                    sub = make_sub(ia, ja, iA, jA, bimg, Bimg)
                    p, M = perron(sub)
                    prim, k = L.is_primitive(M)
                    if not prim:
                        continue
                    rot_sum = len(sub['a']) + len(sub['A'])
                    rows.append(dict(ia=ia, ja=ja, iA=iA, jA=jA, bimg=bimg, Bimg=Bimg,
                                      perron=p, rot_sum=rot_sum, sub=sub, prim_k=k))

print(f"Total candidates enumerated & primitive: {len(rows)}")
rows_in_range = [r for r in rows if 1.75 <= r['perron'] <= 4.25]
print(f"In target Perron range [1.75,4.25]: {len(rows_in_range)}")

# bucket into 8 target Perron slots, roughly evenly spaced, pick closest candidate in each,
# preferring ones that decorrelate rot_sum from perron a bit (vary bimg/Bimg length)
targets = np.linspace(1.8, 4.2, 8)
chosen = []
used_subs = set()
for i, t in enumerate(targets):
    # prefer variety in bimg/Bimg across the 8 picks for decoupling
    pref_variants = ['A', 'Ab', 'AB'] if i % 3 == 0 else (['Ab', 'AB', 'A'] if i % 3 == 1 else ['AB', 'A', 'Ab'])
    best = None
    for variant_bimg in pref_variants:
        cands = [r for r in rows_in_range if r['bimg'] == variant_bimg and tuple(sorted(r['sub'].items())) not in used_subs]
        if not cands:
            continue
        cand = min(cands, key=lambda r: abs(r['perron'] - t))
        if best is None or abs(cand['perron'] - t) < abs(best['perron'] - t):
            best = cand
    if best is None:
        cands = [r for r in rows_in_range if tuple(sorted(r['sub'].items())) not in used_subs]
        best = min(cands, key=lambda r: abs(r['perron'] - t))
    used_subs.add(tuple(sorted(best['sub'].items())))
    chosen.append(best)
    print(f"target={t:.3f}  got perron={best['perron']:.4f}  rot_sum={best['rot_sum']:2d}  "
          f"params=(ia={best['ia']},ja={best['ja']},iA={best['iA']},jA={best['jA']},bimg={best['bimg']},Bimg={best['Bimg']})  "
          f"sub={best['sub']}")

print("\nSpread check -- perron values:", sorted(r['perron'] for r in chosen))
print("Spread check -- rot_sum values:", sorted(r['rot_sum'] for r in chosen))
pr = [r['perron'] for r in chosen]
rs = [r['rot_sum'] for r in chosen]
from scipy.stats import spearmanr
rho_self, p_self = spearmanr(pr, rs)
print(f"Spearman(perron, rot_sum) WITHIN the chosen 8 (decoupling check; want this NOT ~1.0): rho={rho_self:.4f} p={p_self:.4f}")
