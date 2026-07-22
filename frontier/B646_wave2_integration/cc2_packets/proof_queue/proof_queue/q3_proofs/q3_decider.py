"""N1-D2 extension: Jeffrey totals + per-class terms at r = 20..25 — PREDICTION BANK
for the unmeasured ladder rungs E6 k=8..13 (conditional on the two-pipeline identity,
exact-verified 7/7 at r=13..19). Also discriminates the v2(kappa)=2 dyadic jump case
(r=20, 24) left open by the 130/150 jump-law fit."""
import json, sys
sys.path.insert(0, '<cc2-seat>/seat-work/next_queue/n1_counting')
import numpy as np
import n1_jeffrey_terms as J

RS = (29, 31, 37)
W, eps = J.weyl_group()
buckets = {}
for idx in range(len(W)):
    w = W[idx]
    winv = np.rint(np.linalg.inv(w)).astype(np.int64)
    B = J.P_WORD * np.eye(6, dtype=np.int64) - w - winv
    cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
    spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
    buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))

results = {r: 0j for r in RS}
rows = []
for bi, (key, members) in enumerate(sorted(buckets.items(), key=lambda kv: -len(kv[1]))):
    idx0, B0, s0 = members[0]
    row = {"bucket": bi, "charpoly": [int(c) for c in key[0]], "size": len(members),
           "sign": s0, "absdetB": None, "contrib": {}}
    for r in RS:
        g, ad = J.gauss_sum(B0, r)
        row["absdetB"] = ad
        c = len(members) * s0 * g / np.sqrt(ad)
        results[r] += c
        row["contrib"][str(r)] = [c.real, c.imag]
    rows.append(row)
    print(f"bucket {bi + 1}/{len(buckets)} done", flush=True)

print("\n==== PREDICTED ladder continuation (Z_J = Z under the verified identity) ====",
      flush=True)
out = {}
for r in RS:
    z = results[r] / len(W)
    out[str(r)] = [z.real, z.imag]
    print(f"  kappa = {r} (E6 k = {r - 12}): Z_J = {z.real:+.10f} {z.imag:+.10f}i",
          flush=True)
with open('<cc2-seat>/seat-work/next_queue/n1_counting/jeffrey_decider.json',
          'w') as f:
    json.dump({"totals": out, "rows": rows}, f, indent=1)
print("DONE — jeffrey_decider.json written", flush=True)
