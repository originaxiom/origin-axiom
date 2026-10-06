"""First level with a background, across the metallic family and its sign twins (PREREG sealed before running).

Instrument: B1432's census (cover_census.py, main's myindex.py) imported UNCHANGED; only its `cover` is replaced by
a direct bundle presentation (the lesson of the listening log: build each level from its monodromy, never pick a
cyclic cover by search).  Level n of a root with monodromy phi is the bundle of phi^n:
    pi_1 = < T, x, y | T x T^-1 = phi^n(x), T y T^-1 = phi^n(y) >,  meridian T, longitude c = x y x^-1 y^-1,
with phi built from L: x->x, y->yx ; R: x->xy, y->y ; iota: x->y X Y, y->y x Y X Y (all fix c letter for letter, so
T and c commute exactly).  The root's deck on level n is conjugation by the root's t: T->T, x->phi(x), y->phi(y).
Generators are numbered 1 = T, 2 = x, 3 = y; negative = inverse (B1432's convention).
"""
import sys, json, math, pathlib, itertools, time
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / 'frontier/B1432_the_three_fold_cover_fires_off_the_lift/verification'))
import cover_census as CC                      # imports myindex from B1427 itself

def red(w):
    o = []
    for L in w:
        if o and o[-1] == -L: o.pop()
        else: o.append(L)
    return o
def inv(w): return [-L for L in reversed(w)]
def app(phi, w): return red([L2 for L in w for L2 in (phi[L] if L > 0 else inv(phi[-L]))])
def compose(f, g): return {k: app(f, g[k]) for k in (2, 3)}          # f o g
ID = {2: [2], 3: [3]}
GEN = {'L': {2: [2], 3: [3, 2]}, 'R': {2: [2, 3], 3: [3]}, 'I': {2: [3, -2, -3], 3: [3, 2, -3, -2, -3]}}
C = [2, 3, -2, -3]
for k, f in GEN.items(): assert app(f, C) == C, k

def mono(word):
    phi = ID
    for ch in word: phi = compose(phi, GEN[ch])
    return phi
def power(phi, n):
    out = ID
    for _ in range(n): out = compose(out, phi)
    return out

def bundle_cover(phi):
    def cover(n):
        pn = power(phi, n)
        rels = [red([1, 2, -1] + inv(pn[2])), red([1, 3, -1] + inv(pn[3]))]
        tau = {1: [1], 2: phi[2], 3: phi[3]}
        return 3, rels, [1], C, tau
    return cover

def h1_matrix(phi):
    def ab(w): return [sum(1 if L == g else -1 if L == -g else 0 for L in w) for g in (2, 3)]
    return [ab(phi[2]), ab(phi[3])]           # rows = images of x, y

def torsion(phi, n):
    ng, rels, mu, lam, tau = bundle_cover(phi)(n)
    A = [CC.expvec(r, ng) for r in rels] + [CC.expvec(mu, ng)]
    diag, _ = CC.smith_cols(A, ng)
    return [d for d in diag if d > 1], (0 if len([d for d in diag if d]) == ng else 1)

ROOTS = {'golden+': 'LR', 'golden-': 'ILR', 'silver+': 'LLRR', 'silver-': 'ILLRR', 'bronze+': 'LLLRRR', 'bronze-': 'ILLLRRR'}
SNAPPY = {'golden+': 'b++LR', 'golden-': 'b+-LR', 'silver+': 'b++LLRR', 'silver-': 'b+-LLRR', 'bronze+': 'b++LLLRRR', 'bronze-': 'b+-LLLRRR'}

def construction_check(maxlev):
    """Our level n vs SnapPy's bundle of the n-th power of the same word: fibre torsion must agree."""
    import snappy, re
    rows = []
    for name, wd in ROOTS.items():
        phi = mono(wd)
        for n in range(1, maxlev[name] + 1):
            tors, _ = torsion(phi, n)
            sgn = SNAPPY[name][1:3]
            sgn_n = '++' if (sgn == '++' or n % 2 == 0) else '+-'
            S = snappy.Manifold('b' + sgn_n + SNAPPY[name][3:] * n)
            h = str(S.homology())
            st = sorted(int(m) for m in re.findall(r'Z/(\d+)', h))
            try: nm = str(S.identify()[0]) if S.identify() else '?'
            except Exception: nm = '?'
            rows.append((name, n, sorted(tors), st, h, nm, sorted(tors) == st))
    return rows

def exponent(tors): return math.lcm(*tors) if tors else 1

def run(name, n, pstart=5000):
    phi = mono(ROOTS[name]); CC.cover = bundle_cover(phi)
    tors, _ = torsion(phi, n); N = exponent(tors)
    out, bgs, I, chars, _ = CC.census(n, N, pstart, verbose=False)
    keep = {k: out[k] for k in ('n', 'N', 'primes', 'characters', 'loci', 'loci_nonsquare', 'candidates', 'firing',
                                'firing_on_nonsquare_loci', 'differing_at_other_primes', 'generation_backgrounds', 'lifted',
                                'not_lifted', 'signs', 'abs_counts', 'nuc', 'index_deck_invariant', 'background_orbits_closed',
                                'backgrounds_by_orbit_size', 'firing_modules_by_orbit_size', 'seconds')}
    keep['root'] = name; keep['torsion'] = tors
    return keep

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'check':
        for r in construction_check(eval(sys.argv[2])): print(r)
    else:
        jobs = eval(sys.argv[2]); res = []
        for (name, n) in jobs:
            r = run(name, n); res.append(r); print(json.dumps(r), flush=True)
        if len(sys.argv) > 3: json.dump(res, open(sys.argv[3], 'w'), indent=1)
