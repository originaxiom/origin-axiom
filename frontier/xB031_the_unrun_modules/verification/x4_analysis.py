"""xB031 X4 -- aggregation and the WHY.  Written while X2/X3 were still running; not yet executed.

(a) CONTROL: compare the completed X2 run against B1418's banked c2_summary.json on the overlap.
(b) NOT RUN must be zero, or be reported as NOT RUN and never folded into zero (B1418's rule).
(c) X3 aggregate: I by m, against the sealed law |I| = ceil(m/2).
(d) THE WHY, post hoc and labelled as such.  Sym^m of a reducible non-split rho_chi is filtered with
    graded weights chi^(m-2j), j = 0..m.  Twisted by psi the weights are chi^(m-2j) psi.  The
    boundary-torus cohomology sees a weight only when it is trivial on the peripheral curves.
    HYPOTHESIS: I is controlled by the RESONANCE COUNT
        r(m, chi, psi) = #{ j in [0,m] : chi^(m-2j)psi(mu) = 1 and chi^(m-2j)psi(lambda) = 1 }
    and the decay in m is the weights spreading out of resonance.  Tested by correlation, not
    asserted.
"""
import sys, json, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from c2_reducible_index import *
from c2_run import characters

HERE = pathlib.Path(__file__).resolve().parent
TARGET_ORDERS = {(3, 12, 1), (3, 12, 2), (3, 4, 1), (3, 4, 2)}


def order_of(K, v):
    for k in range(1, 13):
        if K.is_zero(K.sub(K.pw(v, k), K.const(1))):
            return k
    return None


K = NF([1, 0, -1, 0, 1]); z = K.alpha()
S = [K.pw(z, k) for k in range(12)]
M, gens, rels, mu, lam = presentation('t12835')
chars = characters(K, gens, rels, S)
loci = []
for chi in chars:
    if all(K.is_zero(K.sub(chi[g], K.const(1))) for g in gens):
        continue
    chi2 = {g: K.mul(chi[g], chi[g]) for g in gens}
    c, h1 = nonsplit_cocycle(K, gens, rels, chi2)
    if c is not None:
        loci.append((chi, c, h1, tuple(order_of(K, chi[g]) for g in gens)))
S6 = [s for s in S if K.is_zero(K.sub(K.pw(s, 6), K.const(1)))]
psis = characters(K, gens, rels, S6)

print("=" * 78)
print("(a)+(b) X2 -- B1418's range, budget removed")
p2 = HERE / 'x2_t12835.json'
if p2.exists():
    x2 = json.load(open(p2))
    run = [r for r in x2 if r.get('status') == 'RUN']
    notrun = [r for r in x2 if r.get('status') != 'RUN']
    Is = sorted({r['I'] for r in run})
    print(f"  modules total {len(x2)}; RUN {len(run)}; NOT RUN {len(notrun)}")
    print(f"  I values {Is}; max|I| {max(abs(i) for i in Is)}")
    print(f"  I_ss values {sorted({r['I_ss'] for r in run})}  (control: must be [0])")
    b = json.load(open(HERE / '..' / '..' / 'B1418_the_family_as_the_object' /
                       'verification' / 'c2_summary.json'))['t12835']
    print(f"  B1418 banked: run {b['run']}, not_run {b['not_run']}, nonzero {b['nonzero']}, "
          f"I_values {b['I_values']}, loci_total(firing) {b['loci_total']}/{b['loci_firing']}")
    print(f"  THIS RUN     : run {len(run)}, not_run {len(notrun)}, "
          f"nonzero {sum(1 for r in run if r['I'] != 0)}, I_values {Is}")
    print(f"  CONTROL -- B1418's I value set is a subset of this run's: "
          f"{set(b['I_values']) <= set(Is)}")
    print(f"  B1418's rule honoured -- NOT RUN is {len(notrun)} and is reported, never folded "
          f"into zero")
else:
    print("  x2_t12835.json ABSENT -- X2 did not complete; nothing reported for it.")

print("=" * 78)
print("(c) X3 -- the extension, against the sealed law |I| = ceil(m/2)")
p3 = HERE / 'x3_partial.json'
x3 = json.load(open(p3)) if p3.exists() else []
by = collections.defaultdict(set)
for r in x3:
    by[r['m']].add(r['I'])
for m in sorted(by):
    got = max(abs(v) for v in by[m])
    print(f"  m={m}: I values {sorted(by[m])}   max|I| = {got}   sealed ceil(m/2) = {-(-m//2)}   "
          f"{'MATCH' if got == -(-m // 2) else 'MISMATCH'}")
print(f"  banked at m=3 (B1418): max|I| = 2")
print(f"  I_ss over every X3 module: {sorted({r['I_ss'] for r in x3})}  (drift control: must be [0])")

print("=" * 78)
print("(d) THE WHY -- resonance count, POST HOC and labelled")
# rebuild the exact (locus, m, twist) order x3_extend.py used
sel = [L for L in loci if L[3] in TARGET_ORDERS]
MSx = sorted(by)
twist_list = []
for p in psis:
    twist_list.append(('psi=' + ','.join(f'{g}:{tuple(map(str, p[g]))}' for g in gens), p))
rows = []
idx = 0
for (chi, c, h1, orders) in sel:
    tw = list(twist_list)
    cj = {g: K.const(1) for g in gens}
    for j in range(1, 4):
        cj = {g: K.mul(cj[g], chi[g]) for g in gens}
        tw.append((f'psi=chi^{j}', dict(cj)))
    for m in MSx:
        for tl, psi in tw:
            if idx >= len(x3):
                break
            rec = x3[idx]; idx += 1
            cm = char_on_word(K, mu, chi); cl = char_on_word(K, lam, chi)
            pm = char_on_word(K, mu, psi); pl = char_on_word(K, lam, psi)
            res = 0
            for j in range(m + 1):
                e = m - 2 * j
                wm = K.mul(K.pw(cm, e) if e >= 0 else K.inv(K.pw(cm, -e)), pm)
                wl = K.mul(K.pw(cl, e) if e >= 0 else K.inv(K.pw(cl, -e)), pl)
                if K.is_zero(K.sub(wm, K.const(1))) and K.is_zero(K.sub(wl, K.const(1))):
                    res += 1
            rows.append({'m': m, 'orders': list(orders), 'resonance': res,
                         'I': rec['I'], 'I_ss': rec['I_ss']})
print(f"  matched {len(rows)} of {len(x3)} X3 modules to a resonance count")
tab = collections.defaultdict(collections.Counter)
for r in rows:
    tab[r['resonance']][abs(r['I'])] += 1
print("  resonance count  ->  distribution of |I|")
for res in sorted(tab):
    print(f"    r={res}: {dict(sorted(tab[res].items()))}")
nz = [r for r in rows if r['I'] != 0]
print(f"  every module with I != 0 has resonance >= 1: "
      f"{all(r['resonance'] >= 1 for r in nz) if nz else 'no nonzero I in range'}")
byres = collections.defaultdict(set)
for r in rows:
    byres[r['m']].add(r['resonance'])
print(f"  resonance counts available at each m: {dict(sorted((m, sorted(v)) for m, v in byres.items()))}")
json.dump({'x3_by_m': {str(m): sorted(v) for m, v in by.items()},
           'resonance_table': {str(k): dict(v) for k, v in tab.items()},
           'rows': rows[:400]},
          open(HERE / 'x4_analysis.json', 'w'), indent=1, default=str)
print("X4 DONE")
