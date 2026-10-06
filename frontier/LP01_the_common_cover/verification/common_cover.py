#!/usr/bin/env python3
"""LP01 -- THE COMMON COVER: the smallest finite manifold covering both m004 and a target (m202, s959, o10_150726),
and what it carries.

Usage:  python3 common_cover.py control     # m206 and m003 against m004 (known common covers)
        python3 common_cover.py all         # the three targets of B1418 Q1.2

Search: for degree pairs (a, b) with a*vol(m004) = b*vol(target) and a <= DMAX, enumerate the connected covers of m004 of
degree a and of the target of degree b (SnapPy's low-index enumeration, one per conjugacy class), filter by number of
cusps and H1, and match by canonical isometry signature.  The first a with a match is the minimal degree; every match at
that degree is reported.

Measured on each common cover found, with B1418 c1_class_census.py's definitions unchanged:
  chiral -- no self-isometry whose map on cusp 0 has det -1;
  three  -- some cusp-fixing self-isometry with det +1 on that cusp and |det(X - I)| = 3;
  door   -- number of surjections onto SL(2,3) (computed only when pi1 has <= 4 generators, else None);
  cover type over m004 and over the target (cyclic / regular / irregular), and whether the cover factors through a
  level of m004 (m206, s961, t12839: the cyclic levels M2-M4).
"""
import sys, itertools, json, time, pathlib, warnings
warnings.filterwarnings('ignore')
import snappy

HERE = pathlib.Path(__file__).resolve().parent
DMAX = 24
LEVELS = ['m206', 's961', 't12839']


def det2(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]


def cm(iso, i):
    c = iso.cusp_maps()[i]; return [[int(c[0][0]), int(c[0][1])], [int(c[1][0]), int(c[1][1])]]


els = [(a, b, c, d) for a, b, c, d in itertools.product(range(3), repeat=4) if (a*d-b*c) % 3 == 1]
def mul(x, y):
    a, b, c, d = x; e, f, g, h = y; return ((a*e+b*g) % 3, (a*f+b*h) % 3, (c*e+d*g) % 3, (c*f+d*h) % 3)
INV = {x: next(y for y in els if mul(x, y) == (1, 0, 0, 1)) for x in els}
def gen_order(S):
    seen = {(1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
    while fr:
        nx = []
        for s in fr:
            for g in S:
                t = mul(s, g)
                if t not in seen: seen.add(t); nx.append(t)
        fr = nx
    return len(seen)
def door(G):
    gens = G.generators(); rels = G.relators()
    if len(gens) > 4: return None
    cnt = 0
    for imgs in itertools.product(els, repeat=len(gens)):
        img = dict(zip(gens, imgs)); ok = True
        for r in rels:
            x = (1, 0, 0, 1)
            for ch in r: x = mul(x, img[ch.lower()] if ch.islower() else INV[img[ch.lower()]])
            if x != (1, 0, 0, 1): ok = False; break
        if ok and gen_order(imgs) == 24: cnt += 1
    return cnt


def measure(M):
    L = M.is_isometric_to(M, return_isometries=True); nc = M.num_cusps()
    amph = any(det2(cm(iso, 0)) == -1 for iso in L)
    vals = set()
    for iso in L:
        for i in range(nc):
            if iso.cusp_images()[i] != i: continue
            X = cm(iso, i)
            if det2(X) != 1: continue
            vals.add(abs(det2([[X[0][0]-1, X[0][1]], [X[1][0], X[1][1]-1]])))
    return {'cusps': nc, 'H1': str(M.homology()), 'vol': float(M.volume()), 'sym': len(L), 'chiral': not amph,
            'three': 3 in vals, 'det_values': sorted(vals), 'gens': len(M.fundamental_group().generators()),
            'door': door(M.fundamental_group())}


def sig(M):
    try: return M.isometry_signature()
    except Exception: return None


def covers(M, d):
    out = []
    for C in M.covers(d):
        out.append((C, C.num_cusps(), str(C.homology()), C.cover_info().get('type')))
    return out


def factors_through_level(C):
    hits = []
    for nm in LEVELS:
        Lv = snappy.Manifold(nm); r = C.volume()/Lv.volume(); k = round(float(r))
        if k < 1 or abs(float(r)-k) > 1e-6: continue
        s = sig(C)
        for D in Lv.covers(k):
            if D.num_cusps() == C.num_cusps() and str(D.homology()) == str(C.homology()) and sig(D) == s:
                hits.append((nm, k)); break
    return hits


def search(target_name, base_name='m004', dmax=DMAX):
    B = snappy.Manifold(base_name); T = snappy.Manifold(target_name)
    ratio = float(T.volume()/B.volume())
    t0 = time.time(); cacheB = {}; cacheT = {}
    for a in range(1, dmax+1):
        b = a/ratio
        if abs(b-round(b)) > 1e-6 or round(b) < 1: continue
        b = round(b)
        CB = cacheB.setdefault(a, covers(B, a)); CT = cacheT.setdefault(b, covers(T, b))
        keysT = {}
        for C, nc, h, ty in CT: keysT.setdefault((nc, h), []).append((C, ty))
        matches = []
        for C, nc, h, ty in CB:
            if (nc, h) not in keysT: continue
            s = sig(C)
            for D, tyT in keysT[(nc, h)]:
                if s is not None and s == sig(D):
                    matches.append((C, ty, tyT)); break
        print(f'  {target_name}: degree {a} over {base_name}, {b} over target: {len(CB)} x {len(CT)} covers, '
              f'{len(matches)} common ({round(time.time()-t0)} s)', flush=True)
        if matches:
            rows = []
            for C, ty, tyT in matches:
                r = measure(C); r.update({'deg_over_base': a, 'deg_over_target': b, 'type_over_base': ty,
                                          'type_over_target': tyT, 'signature': sig(C),
                                          'factors_through_level': factors_through_level(C)})
                rows.append(r); print('   ', json.dumps(r), flush=True)
            return rows
    print(f'  {target_name}: no common cover with degree <= {dmax} over {base_name}', flush=True)
    return []


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'control'
    targets = ['m206', 'm003'] if mode == 'control' else ['m202', 's959', 'o10_150726']
    out = {}
    for t in targets:
        print('target', t, json.dumps(measure(snappy.Manifold(t))), flush=True)
        out[t] = search(t)
    print('base m004', json.dumps(measure(snappy.Manifold('m004'))))
    json.dump(out, open(HERE/f'common_cover_{mode}.json', 'w'), indent=1, default=str)
