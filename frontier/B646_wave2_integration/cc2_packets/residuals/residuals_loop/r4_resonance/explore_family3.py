"""
R4 -- DESIGN-STAGE EXPLORATION ONLY (round 3, efficient). Still no cost computation.
Restricts the per-target search to a small pool of near-target candidates (size K) so the
random search over 8-tuples is cheap, instead of rescanning the whole candidate list.
"""
import sys
import time
sys.path.insert(0, '<cc2-seat>/seat-work/veins/v2_resonance')
import numpy as np
from scipy.stats import spearmanr
import lib as L

t0 = time.time()

def make_sub(ia, ja, iA, jA, bimg, Bimg):
    a_img = 'a' * ia + 'A' * ja + 'b'
    A_img = 'A' * iA + 'a' * jA + 'B'
    return {'a': a_img, 'A': A_img, 'b': bimg, 'B': Bimg}

def perron(sub):
    M = L.incidence_matrix(sub)
    ev = np.linalg.eigvals(M)
    return float(ev[np.argmax(np.abs(ev))].real), M

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
                                          perron=p, rot_sum=rot_sum, sub=sub, prim_k=k,
                                          key=tuple(sorted(sub.items()))))
print(f"Candidate pool: {len(rows)}  [{time.time()-t0:.1f}s]")

targets = np.linspace(1.8, 4.2, 8)
K = 40
pools = []
for t in targets:
    cands = sorted(rows, key=lambda r: abs(r['perron'] - t))[:K]
    pools.append(cands)
    print(f"target={t:.3f}  pool perron range [{min(c['perron'] for c in cands):.3f},"
          f"{max(c['perron'] for c in cands):.3f}]  rot_sum options={sorted(set(c['rot_sum'] for c in cands))}")

rng = np.random.default_rng(44)
best = None
best_loss = None
N_TRIALS = 200000
for trial in range(N_TRIALS):
    idxs = [rng.integers(0, len(p)) for p in pools]
    picks = [pools[i][idxs[i]] for i in range(8)]
    keys = [p['key'] for p in picks]
    if len(set(keys)) < 8:
        continue
    pr_vals = [p['perron'] for p in picks]
    rs_vals = [p['rot_sum'] for p in picks]
    if len(set(rs_vals)) < 4:  # want decent variety in rot_sum too, not all identical
        continue
    rho, _ = spearmanr(pr_vals, rs_vals)
    rho = 0.0 if np.isnan(rho) else rho
    spread_loss = sum((p - t) ** 2 for p, t in zip(sorted(pr_vals), targets))
    loss = abs(rho) * 2.0 + spread_loss * 0.5
    if best_loss is None or loss < best_loss:
        best_loss = loss
        best = picks

print(f"\n[{time.time()-t0:.1f}s] Best over {N_TRIALS} trials, loss={best_loss:.4f}")
for c in sorted(best, key=lambda r: r['perron']):
    print(f"  perron={c['perron']:.4f}  rot_sum={c['rot_sum']:2d}  "
          f"(ia={c['ia']},ja={c['ja']},iA={c['iA']},jA={c['jA']},bimg={c['bimg']!r},Bimg={c['Bimg']!r})  "
          f"sub={c['sub']}")
pr_vals = [c['perron'] for c in best]
rs_vals = [c['rot_sum'] for c in best]
rho, pval = spearmanr(pr_vals, rs_vals)
print(f"\nSpearman(perron, rot_sum) within chosen 8: rho={rho:.4f} p={pval:.4f}")
print(f"Perron spread: {sorted(pr_vals)}")
print(f"rot_sum spread: {sorted(rs_vals)}")
print(f"Total elapsed: {time.time()-t0:.1f}s")
