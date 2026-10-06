"""Orbit-cached wrapper around B1432's census (instrument otherwise unchanged).

The root's deck tau is induced by a self-homeomorphism of level n, so H*(M; tau*V) = H*(M; V).  When h1(lambda) = 1
the non-split extension is unique up to isomorphism, so the census module at (tau lambda, tau alpha) IS tau*V and has
the same index triple.  We therefore compute `index` once per (deck orbit, prime) on loci with h1 = 1, and directly
everywhere else.  Validated against full-census cells before use (validate()).
"""
import sys, json
import os
import first_background as F
if os.environ.get('SHORT') == '1':
    import short_cover
    F.bundle_cover = short_cover.short_cover          # same group, short relators (validated)
CC = F.CC
_index = CC.index
_module = CC.module
STATE = {}

def install(phi, n):
    ng, rels, mu, lam, tau = F.bundle_cover(phi)(n)
    tors, _ = F.torsion(phi, n); N = F.exponent(tors)
    def tchar(c): return tuple(sum(e * x for e, x in zip(CC.expvec(tau[g], ng), c)) % N for g in range(1, ng + 1))
    STATE.update(tchar=tchar, cache={}, h1=None, rels=rels, ng=ng, N=N, hits=0, computed=0)
    def module(lam_exp, al_exp, ct, ng_, N_, zeta, p):
        V = _module(lam_exp, al_exp, ct, ng_, N_, zeta, p)
        V._key = (tuple(lam_exp), tuple(al_exp), p, zeta)
        return V
    def index(V, rels_, mu_, lam_, check=True):
        key = getattr(V, '_key', None)
        if key is None: return _index(V, rels_, mu_, lam_)
        lc, al, p, zeta = key
        h1 = STATE['h1cache'].setdefault((lc, p), CC.cocycle(lc, STATE['rels'], STATE['ng'], STATE['N'], zeta, p)[0])
        if h1 != 1:
            STATE['computed'] += 1; return _index(V, rels_, mu_, lam_)
        orb = []; k = (lc, al)
        while k not in orb: orb.append(k); k = (tchar(k[0]), tchar(k[1]))
        rep = min(orb)
        ck = (rep, p)
        if ck in STATE['cache']: STATE['hits'] += 1; return STATE['cache'][ck]
        r = _index(V, rels_, mu_, lam_); STATE['cache'][ck] = r; STATE['computed'] += 1
        return r
    STATE['h1cache'] = {}
    CC.module = module; CC.index = index

def run(name, n, pstart=5000):
    phi = F.mono(name)
    F.ROOTS[name] = name
    install(phi, n)
    r = F.run(name, n, pstart)
    r['orbit_cache'] = dict(hits=STATE['hits'], computed=STATE['computed'])
    return r

KEYS = ('firing', 'generation_backgrounds', 'lifted', 'loci', 'loci_nonsquare', 'backgrounds_by_orbit_size',
        'firing_modules_by_orbit_size', 'signs', 'nuc', 'differing_at_other_primes')

def validate():
    ref = {(r['root'], r['n']): r for f in ('control.json', 'family.json', 'orbit_law.json') for r in json.load(open(f))}
    for (name, n) in [('LR', 3), ('LR', 4), ('LR', 5), ('ILLRR', 3), ('LLR', 3), ('ILLRLLR', 2)]:
        key = {'LR': 'golden+', 'ILLRR': 'silver-'}.get(name, name)
        r = run(name, n); R = ref[(key, n)]
        same = all(r[k] == R[k] for k in KEYS)
        print(name, n, 'MATCH' if same else 'DIFF', {k: (r[k], R[k]) for k in KEYS if r[k] != R[k]}, r['orbit_cache'], r['seconds'], 's', flush=True)

if __name__ == '__main__':
    if sys.argv[1] == 'validate': validate()
    else:
        name, n = sys.argv[2], int(sys.argv[3]); ps = int(sys.argv[4]) if len(sys.argv) > 4 else 5000
        r = run(name, n, ps); print(json.dumps(r), flush=True)
        json.dump(r, open(f'heavy_{name}_{n}' + (f'_p{ps}' if ps != 5000 else '') + '.json', 'w'), indent=1)
