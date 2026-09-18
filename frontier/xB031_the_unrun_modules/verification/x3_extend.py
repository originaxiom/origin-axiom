"""xB031 X3 -- THE EXTENSION.  m = 4, 5, 6 on the loci where B1418 found |I| = 2 at m = 3.

SEALED PREDICTION (19aa3866): |I| = ceil(m/2) on those loci, so m=4 -> 2, m=5 -> 3, m=6 -> 3.
KILL: |I| <= 2 throughout m <= 6 refutes the growth law and closes the last route this class has.
CONTROL: I^ss must stay 0 at every m.  A non-zero I^ss means the construction DRIFTED and the
numbers are VOID -- not that something was found.

PROVENANCE: the module computation is B1418's run_module(), imported from the byte-identical
c2_reducible_index.py (sha256 d4468ef1...).  The LOOP is this arc's; the twist construction is
transcribed from B1418's c2_run.run() so the twist set is the same one.
"""
import sys, json, time, itertools, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from c2_reducible_index import *
from c2_run import characters

TARGET_ORDERS = {(3, 12, 1), (3, 12, 2), (3, 4, 1), (3, 4, 2)}
MS = [int(x) for x in (sys.argv[1].split(',') if len(sys.argv) > 1 else ['4', '5', '6'])]
ALL_FIRING = len(sys.argv) > 2 and sys.argv[2] == 'all'


def order_of(K, v):
    for k in range(1, 13):
        if K.is_zero(K.sub(K.pw(v, k), K.const(1))):
            return k
    return None


K = NF([1, 0, -1, 0, 1]); z = K.alpha()
S = [K.pw(z, k) for k in range(12)]
M, gens, rels, mu, lam = presentation('t12835')
print(f"t12835: {len(gens)} generators, {len(rels)} relators", flush=True)
chars = characters(K, gens, rels, S)
loci = []
for chi in chars:
    if all(K.is_zero(K.sub(chi[g], K.const(1))) for g in gens):
        continue
    chi2 = {g: K.mul(chi[g], chi[g]) for g in gens}
    c, h1 = nonsplit_cocycle(K, gens, rels, chi2)
    if c is not None:
        loci.append((chi, c, h1, tuple(order_of(K, chi[g]) for g in gens)))
print(f"  reducible non-split loci: {len(loci)}", flush=True)
sel = [L for L in loci if ALL_FIRING or L[3] in TARGET_ORDERS]
print(f"  selected loci (orders in {sorted(TARGET_ORDERS)} unless 'all'): {len(sel)} "
      f"-> {[L[3] for L in sel]}", flush=True)

S6 = [s for s in S if K.is_zero(K.sub(K.pw(s, 6), K.const(1)))]
psis = characters(K, gens, rels, S6)
print(f"  twists: {len(psis)} characters of order | 6, plus chi^1..3", flush=True)

results = []
t0 = time.time()
for li, (chi, c, h1, orders) in enumerate(sel):
    lab = f'orders={orders} h1={h1}'
    twists = [('psi=' + ','.join(f'{g}:{tuple(map(str, p[g]))}' for g in gens), p) for p in psis]
    cj = {g: K.const(1) for g in gens}
    for j in range(1, 4):
        cj = {g: K.mul(cj[g], chi[g]) for g in gens}
        twists.append((f'psi=chi^{j}', dict(cj)))
    for m in MS:
        for tl, psi in twists:
            r = run_module(K, 't12835', gens, rels, mu, lam, chi, c, m, psi, f'{lab} m={m} {tl}')
            r.update({'locus': lab, 'orders': list(orders), 'm': m, 'twist': tl, 'status': 'RUN'})
            results.append(r)
        json.dump(results, open(pathlib.Path(__file__).with_name('x3_partial.json'), 'w'),
                  indent=1, default=str)
        cur = [abs(x['I']) for x in results if x['m'] == m]
        print(f"  ... locus {li+1}/{len(sel)} {orders} m={m} done, max|I| at this m so far: "
              f"{max(cur) if cur else 0}, elapsed {time.time()-t0:.0f}s", flush=True)

by_m = {}
for r in results:
    by_m.setdefault(r['m'], set()).add(r['I'])
print("\nX3 RESULT")
for m in sorted(by_m):
    vals = sorted(by_m[m])
    print(f"  m={m}: I values {vals}   max|I| = {max(abs(v) for v in vals)}")
ss = sorted({r['I_ss'] for r in results})
print(f"  CONTROL  I^ss values across every module: {ss}  (must be [0])")
mx = max(abs(r['I']) for r in results) if results else 0
print(f"  max |I| over m in {MS}: {mx}")
print(f"  SEALED PREDICTION |I| = ceil(m/2): "
      f"{ {m: (max(abs(v) for v in by_m[m]), -(-m//2)) for m in sorted(by_m)} }  (measured, predicted)")
json.dump({'MS': MS, 'by_m': {str(k): sorted(v) for k, v in by_m.items()},
           'I_ss_values': ss, 'max_abs_I': mx, 'n_modules': len(results),
           'selected_orders': [list(L[3]) for L in sel]},
          open(pathlib.Path(__file__).with_name('x3_summary.json'), 'w'), indent=1, default=str)
print("X3 DONE")
