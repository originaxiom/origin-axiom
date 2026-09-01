#!/usr/bin/env python3
"""Fresh physics seat (2026-09-01) — every computation cited in the report, re-runnable.

Requires: pip install snappy  (pure-Python parts run without it).
Each check prints PASS/FAIL against the value asserted in the report.
Nothing here writes to the repo; this is an outside seat's verification bench.
"""
import itertools

# ---------------------------------------------------------------- SL(2,p) tools
def sl2(p):
    return [(a, b, c, d)
            for a, b, c, d in itertools.product(range(p), repeat=4)
            if (a * d - b * c) % p == 1]

def mul(X, Y, p):
    a, b, c, d = X; e, f, g, h = Y
    return ((a*e + b*g) % p, (a*f + b*h) % p, (c*e + d*g) % p, (c*f + d*h) % p)

def inv(X, p):
    a, b, c, d = X
    return (d % p, -b % p, -c % p, a % p)

def count_surjections(rels, ngens, p):
    """Surjections of <x1..xn | rels> onto SL(2,p); rels use 'a','b',... and caps for inverses."""
    els = sl2(p); order = len(els); I = (1, 0, 0, 1)
    import string
    letters = string.ascii_lowercase[:ngens]
    homs = surj = 0
    for tup in itertools.product(els, repeat=ngens):
        m = {}
        for L, g in zip(letters, tup):
            m[L] = g; m[L.upper()] = inv(g, p)
        if any(_word(r, m, p) != I for r in rels):
            continue
        homs += 1
        if _generates(tup, order, p):
            surj += 1
    return homs, surj

def _word(w, m, p):
    R = (1, 0, 0, 1)
    for ch in w:
        R = mul(R, m[ch], p)
    return R

def _generates(gens, order, p):
    I = (1, 0, 0, 1)
    S = {I}; fr = [I]
    gg = [x for g in gens for x in (g, inv(g, p))]
    while fr:
        nf = []
        for x in fr:
            for g in gg:
                y = mul(x, g, p)
                if y not in S:
                    S.add(y); nf.append(y)
        fr = nf
    return len(S) == order

REL_M004 = ['aaabABBAb']   # SnapPy presentation of pi_1(m004) = pi_1(4_1)
REL_M000 = ['aabbAB']      # SnapPy presentation of pi_1(m000) = pi_1(Gieseking)

def check(label, got, want):
    tag = 'PASS' if got == want else 'FAIL'
    print(f'{tag}  {label}: got {got}, expected {want}')

# 1. 2T surjection counts identical pre/post squaring (A6-independence of the E6 entrance)
check('m004 (homs, surj) onto SL(2,3)=2T', count_surjections(REL_M004, 2, 3), (72, 48))
check('m000 (homs, surj) onto SL(2,3)=2T', count_surjections(REL_M000, 2, 3), (72, 48))

# 2. E6-vs-E8 selection at the manifold level: 2I is refused, 2T is not
check('m004 (homs, surj) onto SL(2,5)=2I', count_surjections(REL_M004, 2, 5), (600, 0))

# 3. SnapPy-dependent checks
try:
    import snappy
except ImportError:
    print('SKIP  snappy not installed — geometric checks skipped')
else:
    M004 = snappy.Manifold('m004')
    M000 = snappy.NonorientableCuspedCensus[0]
    check('Gieseking is m000, nonorientable', (M000.name(), M000.is_orientable()), ('m000', False))
    check('orientation cover of m000 is m004', M000.orientation_cover().is_isometric_to(M004), True)
    z = complex(M004.tetrahedra_shapes('rect')[0])
    check('m004 shape satisfies z^2-z+1=0 (field Q(sqrt-3))', abs(z*z - z + 1) < 1e-9, True)

    # 4. Orientation double covers are amphichiral 40/40 (and provably 100%:
    #    the deck involution of an orientation double cover is orientation-
    #    reversing; Mostow upgrades it to an isometry).
    amph = tot = 0
    for N in snappy.NonorientableCuspedCensus:
        if tot >= 40:
            break
        try:
            a = N.orientation_cover().symmetry_group().is_amphicheiral()
        except Exception:
            continue
        tot += 1; amph += bool(a)
    check('orientation covers amphichiral (first 40)', (amph, tot), (40, 40))

    # 5. Base rate of amphichirality among orientable census manifolds (~2-3%)
    base_a = base_t = 0
    for M in snappy.OrientableCuspedCensus:
        if base_t >= 300:
            break
        try:
            a = M.symmetry_group().is_amphicheiral()
        except Exception:
            continue
        base_t += 1; base_a += bool(a)
    print(f'INFO  orientable-census amphichiral base rate: {base_a}/{base_t}')

    # 6. B1136's 14-manifold Q(sqrt-3) family: volumes are integer multiples of
    #    the Gieseking volume — one commensurability class (with Neumann-Reid +
    #    arithmeticity, all are commensurable with the Bianchi group PGL(2,Z[w])).
    g = M000.volume()
    fam = ['m003', 'm004', 'm202', 'm203', 'm206', 'm207', 'm208',
           'm410', 'm412', 's118', 's119', 's594', 's595', 's596']
    mults = [round(float(snappy.Manifold(n).volume() / g)) for n in fam]
    ok = all(abs(float(snappy.Manifold(n).volume() / g) - m) < 1e-6 for n, m in zip(fam, mults))
    check('family volumes are integer multiples of vol(Gieseking)', ok, True)
    print('INFO  multiples:', dict(zip(fam, mults)))

    # 7. Genericity of the E6-selecting signature (onto 2T, not onto 2I)
    #    over the first 60 two-generator orientable census manifolds.
    both = any2t = tot = 0
    for M in snappy.OrientableCuspedCensus:
        if tot >= 60:
            break
        G = M.fundamental_group()
        if len(G.generators()) > 2:
            continue
        tot += 1
        if count_surjections(G.relators(), 2, 3)[1] > 0:
            any2t += 1
            if count_surjections(G.relators(), 2, 5)[1] == 0:
                both += 1
    print(f'INFO  census genericity: {any2t}/{tot} surject onto 2T; '
          f'{both}/{tot} carry the full m004 signature (onto 2T, not onto 2I)')
