"""
R4 -- DESIGN-STAGE EXPLORATION ONLY (round 2). Still no cost computation. Broadens b/B
image content (which moves Perron root without moving rot_sum, since rot_sum is defined
ONLY from len(a)+len(A)) to reduce the within-set collinearity between the two predictors,
so the 8-point test can actually distinguish them rather than being degenerate.
"""
import sys
import itertools
sys.path.insert(0, '/Users/dri/oa-seat-cc2/seat-work/veins/v2_resonance')
import numpy as np
from scipy.stats import spearmanr
import lib as L

def make_sub(ia, ja, iA, jA, bimg, Bimg):
    a_img = 'a' * ia + 'A' * ja + 'b'
    A_img = 'A' * iA + 'a' * jA + 'B'
    return {'a': a_img, 'A': A_img, 'b': bimg, 'B': Bimg}

def perron(sub):
    M = L.incidence_matrix(sub)
    ev = np.linalg.eigvals(M)
    return float(ev[np.argmax(np.abs(ev))].real), M

# bimg must contain >=1 'A' (for the b->A backbone edge); Bimg must contain >=1 'a'.
bimg_opts = ['A', 'Ab', 'AB', 'AAB', 'ABB', 'AbB']
Bimg_opts = ['a', 'aB', 'ab', 'aaB', 'abb', 'aBb']

rows = []
for ia in range(0, 6):
    for ja in range(0, 4):
        for iA in range(0, 6):
            for jA in range(0, 4):
                if ia + ja == 0 or iA + jA == 0:
                    continue
                for bimg in bimg_opts:
                    for Bimg in Bimg_opts:
                        sub = make_sub(ia, ja, iA, jA, bimg, Bimg)
                        p, M = perron(sub)
                        if not (1.7 <= p <= 4.3):
                            continue
                        prim, k = L.is_primitive(M)
                        if not prim:
                            continue
                        rot_sum = len(sub['a']) + len(sub['A'])
                        rows.append(dict(ia=ia, ja=ja, iA=iA, jA=jA, bimg=bimg, Bimg=Bimg,
                                          perron=p, rot_sum=rot_sum, sub=sub, prim_k=k))

print(f"Candidate pool (primitive, in range): {len(rows)}")

targets = np.linspace(1.8, 4.2, 8)

rng = np.random.default_rng(44)  # fixed seed for this design-search only; not scientific content
best_selection = None
best_loss = None
for trial in range(20000):
    order = rng.permutation(len(rows))
    chosen = []
    used = set()
    ok = True
    for t in targets:
        cands = [rows[i] for i in order if tuple(sorted(rows[i]['sub'].items())) not in used]
        if not cands:
            ok = False
            break
        # take the 5 closest to target, then pick whichever best decorrelates so far
        cands.sort(key=lambda r: abs(r['perron'] - t))
        pool5 = cands[:6]
        if len(chosen) < 2:
            pick = pool5[0]
        else:
            pr_so_far = [c['perron'] for c in chosen]
            rs_so_far = [c['rot_sum'] for c in chosen]
            def trial_rho(cand):
                pr = pr_so_far + [cand['perron']]
                rs = rs_so_far + [cand['rot_sum']]
                r, _ = spearmanr(pr, rs)
                return abs(r) if not np.isnan(r) else 0.0
            pick = min(pool5, key=trial_rho)
        chosen.append(pick)
        used.add(tuple(sorted(pick['sub'].items())))
    if not ok or len(chosen) < 8:
        continue
    pr_vals = [c['perron'] for c in chosen]
    rs_vals = [c['rot_sum'] for c in chosen]
    rho, pval = spearmanr(pr_vals, rs_vals)
    spread_loss = sum((p - t) ** 2 for p, t in zip(sorted(pr_vals), targets))
    loss = abs(rho) * 3.0 + spread_loss
    if best_loss is None or loss < best_loss:
        best_loss = loss
        best_selection = chosen

print(f"\nBest selection found (loss={best_loss:.4f}):")
for c in sorted(best_selection, key=lambda r: r['perron']):
    print(f"  perron={c['perron']:.4f}  rot_sum={c['rot_sum']:2d}  "
          f"(ia={c['ia']},ja={c['ja']},iA={c['iA']},jA={c['jA']},bimg={c['bimg']!r},Bimg={c['Bimg']!r})  "
          f"sub={c['sub']}")
pr_vals = [c['perron'] for c in best_selection]
rs_vals = [c['rot_sum'] for c in best_selection]
rho, pval = spearmanr(pr_vals, rs_vals)
print(f"\nSpearman(perron, rot_sum) within chosen 8: rho={rho:.4f} p={pval:.4f}")
print(f"Perron spread: {sorted(pr_vals)}")
print(f"rot_sum spread: {sorted(rs_vals)}")
