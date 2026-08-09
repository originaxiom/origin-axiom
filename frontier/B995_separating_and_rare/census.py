"""B995 -- the separating-and-rare census. Seal a356e987...  Run: sage-python census.py"""
import json, os, sys
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
FAMILY = ['m003', 'm206', 'm136', 'm129', 'm135']          # B855's two rows, sealed

def invariants(M):
    o = {}
    try:
        d = [int(x) for x in M.homology().elementary_divisors() if x]
        t = 1
        for x in d: t *= x
        o['h1_torsion'] = t
        o['h1_divisors'] = str(tuple(sorted(d)))
    except Exception: o['h1_torsion'] = o['h1_divisors'] = None
    try:
        a = M.alexander_polynomial()
        o['alex_coeffs'] = str(tuple(int(c) for c in a.coefficients()))
        o['alex_degree'] = int(a.degree())
    except Exception: o['alex_coeffs'] = o['alex_degree'] = None
    try:    o['isom_order'] = int(M.symmetry_group().order())
    except Exception: o['isom_order'] = None
    try:
        ls = M.length_spectrum(2.0)
        o['systole'] = round(float(ls[0].length.real()), 4) if len(ls) else None
    except Exception: o['systole'] = None
    for deg in (2, 3):
        try:
            tors = []
            for C in M.covers(deg):
                dd = [int(x) for x in C.homology().elementary_divisors() if x]
                p = 1
                for x in dd: p *= x
                tors.append(p)
            o[f'cover{deg}_torsions'] = str(tuple(sorted(tors)))
        except Exception: o[f'cover{deg}_torsions'] = None
    return o

KEYS = ['h1_torsion','h1_divisors','alex_coeffs','alex_degree','isom_order','systole',
        'cover2_torsions','cover3_torsions']

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    sep = {n: invariants(snappy.Manifold(n)) for n in ['m004'] + FAMILY}
    separates = {}
    print("SEPARATION against B855's two rows (m003, m206 | m136, m129, m135):\n")
    for k in KEYS:
        v = sep['m004'][k]
        ok = v is not None and all(sep[n][k] != v for n in FAMILY)
        separates[k] = ok
        print(f"  {k:17} m004={str(v)[:26]:28} SEPARATES={ok}")
    live = [k for k, ok in separates.items() if ok]
    print(f"\n  invariants that SEPARATE: {live if live else 'NONE'}")
    if not live:
        json.dump({'separation': sep, 'separates': separates, 'live': [],
                   'outcome': 'B', 'reason': 'no invariant separates m004 from both rows'},
                  open(os.path.join(HERE, 'results.json'), 'w'), indent=1)
        print("\n  => OUTCOME B at step 1: nothing to base-rate. Sealed logic requires BOTH.")
        return
    # base rate ONLY for separators -- sealed logic needs BOTH, so non-separators are already out
    print(f"\nBASE RATE over first {N} one-cusped census manifolds, for the separators only:\n")
    counts = {k: 0 for k in live}; n = 0; skipped = {k: 0 for k in live}
    for M in snappy.OrientableCuspedCensus(cusps=1):
        if n >= N: break
        iv = invariants(M); n += 1
        for k in live:
            if iv[k] is None: skipped[k] += 1
            elif iv[k] == sep['m004'][k]: counts[k] += 1
    res = {'separation': sep, 'separates': separates, 'live': live, 'population': n,
           'counts': counts, 'skipped': skipped,
           'rates': {k: counts[k] / n for k in live}}
    rare = []
    for k in live:
        r = counts[k] / n
        tag = "RARE (<=5%)" if r <= 0.05 else "COMMON"
        if r <= 0.05: rare.append(k)
        print(f"  {k:17} {counts[k]:5}/{n}  = {r:7.2%}  skipped={skipped[k]:4}  {tag}")
    res['rare'] = rare
    res['outcome'] = 'A' if rare else 'B'
    json.dump(res, open(os.path.join(HERE, 'results.json'), 'w'), indent=1)
    print(f"\n  SEPARATING **and** RARE: {rare if rare else 'NONE'}")
    print(f"  => OUTCOME {res['outcome']}")

if __name__ == '__main__':
    main()
