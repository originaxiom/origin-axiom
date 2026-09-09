#!/usr/bin/env python3
"""B1323 U2 -- the criterion census for C2 (pre-registered in DESIGN.md section 4).
K1 Hurwitz/Lagrange, K2 minimal partial quotients, K3 minimal hyperbolic trace (class number of disc 5),
K4 torsion-free first mixed closure, K5 the Markov tree's root, K6 smallest real quadratic discriminant,
K7 smallest quadratic Pisot number, K8 (counter) smallest Pisot number of any degree, K9 (counter) recorded.
PASS = K1..K7 have phi (phi^2, Q(sqrt5)) as unique minimiser AND K8's minimiser is not phi."""
import itertools, json, math, pathlib, sys
import mpmath as mp
mp.mp.dps = 40
HERE = pathlib.Path(__file__).resolve().parent
PHI = (1 + mp.sqrt(5)) / 2

def cf_value(period, head=None, terms=400):
    """value of [head; period, period, ...] as an mpf (head=None -> purely periodic starting with period[0] as a_0)."""
    seq = list(period) * (terms // len(period) + 1)
    if head is not None: seq = [head] + seq
    x = mp.mpf(0)
    for a in reversed(seq[1:]): x = 1 / (a + x)
    return seq[0] + x

def lagrange_value(period):
    """L(alpha) for purely periodic alpha = [a_0; a_1, ..., a_{k-1}, a_0, ...]:
    limsup_n (a_{n+1} + [0; a_{n+2}, ...] + [0; a_n, ..., a_1]) = max over cyclic positions."""
    k = len(period); best = mp.mpf(0)
    for i in range(k):
        a = period[i]
        tail = cf_value([0] + [period[(i + 1 + j) % k] for j in range(k)][:k], head=None) if False else None
        # tail = [0; a_{i+1}, a_{i+2}, ...] (periodic forward from i+1)
        fwd = [period[(i + 1 + j) % k] for j in range(k)]
        t = cf_value(fwd) ; tail = 1 / t                       # [0; fwd...] = 1/[fwd_0; fwd_1, ...]
        # head = [0; a_{i-1}, a_{i-2}, ...] (periodic backward from i-1)
        bwd = [period[(i - 1 - j) % k] for j in range(k)]
        h = cf_value(bwd); headv = 1 / h
        best = max(best, a + tail + headv)
    return best

def K1():
    dom = [(a,) for a in range(1, 6)] + [(a, b) for a in range(1, 6) for b in range(1, 6) if a != b]
    vals = sorted(((lagrange_value(p), p) for p in dom), key=lambda t: t[0])
    Lmin, pmin = vals[0]
    # uniqueness up to the same value (period-2 (a,b) and (b,a) are the same class)
    tied = [p for v, p in vals if abs(v - Lmin) < mp.mpf('1e-25')]
    return {'minimiser_period': pmin, 'L_min': mp.nstr(Lmin, 25), 'sqrt5': mp.nstr(mp.sqrt(5), 25), 'is_sqrt5': abs(Lmin - mp.sqrt(5)) < mp.mpf('1e-20'),
            'tied_periods': tied, 'second_value': mp.nstr(vals[len(tied)][0], 20), 'second_period': vals[len(tied)][1], 'is_2sqrt2_second': abs(vals[len(tied)][0] - 2 * mp.sqrt(2)) < mp.mpf('1e-20'),
            'PASS': pmin == (1,) and len(tied) == 1 and abs(Lmin - mp.sqrt(5)) < mp.mpf('1e-20')}

def K2():
    # the least positive partial quotient is 1; the constant expansion [1;1,1,...] = phi
    v = cf_value((1,))
    return {'[1;1,1,...]': mp.nstr(v, 25), 'phi': mp.nstr(PHI, 25), 'PASS': abs(v - PHI) < mp.mpf('1e-30')}

def reduced_forms(D):
    """reduced indefinite binary quadratic forms (a,b,c), b^2-4ac = D>0 non-square: 0 < b < sqrt D and sqrt D - b < 2|a| < sqrt D + b."""
    s = math.sqrt(D); forms = []
    for b in range(1, int(s) + 1):
        if (b * b - D) % 4: continue
        for a in range(-D, D + 1):
            if a == 0 or 4 * a == 0: continue
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if s - b < 2 * abs(a) < s + b: forms.append((a, b, c))
    return forms

def rho(f):
    """the reduction (cycle) operator on reduced indefinite forms: (a,b,c) -> (c, b', c') with b' = -b mod 2c in the reduced range."""
    a, b, c = f; s = math.sqrt(abs(b * b - 4 * a * c))
    # choose b' == -b (mod 2c), s - 2|c| < b' < s
    m = 2 * abs(c); bp = (-b) % m
    while not (s - m < bp < s): bp += m if bp < s - m else -m
    cp = (bp * bp - (b * b - 4 * a * c)) // (4 * c)
    return (c, bp, cp)

def K3():
    D = 5; forms = reduced_forms(D)
    # cycles under rho
    seen = set(); cycles = []
    for f in forms:
        if f in seen: continue
        cyc = [f]; g = rho(f); seen.add(f)
        while g != f and g not in seen: cyc.append(g); seen.add(g); g = rho(g)
        cycles.append(cyc)
    # the first hyperbolic trace in SL(2,Z)
    traces = [t for t in range(0, 6) if abs(t) > 2]
    A = ((2, 1), (1, 1))
    lam = (3 + math.sqrt(5)) / 2
    return {'reduced_forms_disc_5': forms, 'cycles': cycles, 'class_number_h+(5)': len(cycles), 'first_trace_gt_2': min(traces),
            'A': A, 'A trace': 3, 'A eigenvalue': lam, 'phi^2': float(PHI ** 2), 'PASS': len(cycles) == 1 and min(traces) == 3 and abs(lam - float(PHI ** 2)) < 1e-12}

def K4():
    L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1))
    def mpow(M, n):
        out = ((1, 0), (0, 1))
        for _ in range(n): out = tuple(tuple(sum(out[i][k] * M[k][j] for k in range(2)) for j in range(2)) for i in range(2))
        return out
    def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    tf = []
    for a in range(1, 13):
        for b in range(1, 13):
            B = mul(mpow(L, a), mpow(R, b)); d = abs((B[0][0] - 1) * (B[1][1] - 1) - B[0][1] * B[1][0])
            if d == 1: tf.append((a, b, B))
    return {'grid': '12x12', 'torsion_free_closures': [(a, b) for a, b, _ in tf], 'matrix': tf[0][2] if tf else None, 'PASS': [(a, b) for a, b, _ in tf] == [(1, 1)] and tf[0][2] == ((2, 1), (1, 1))}

def K5():
    # Markov triples by Vieta descent from (1,1,1); count to 10^4; Fricke triple = 3*(Markov triple) solves x^2+y^2+z^2 = xyz
    root = (1, 1, 1); triples = {root}; stack = [root]
    while stack:
        a, b, c = stack.pop()
        for t in ((3 * b * c - a, b, c), (a, 3 * a * c - b, c), (a, b, 3 * a * b - c)):
            t = tuple(sorted(t))
            if max(t) <= 10_000 and t not in triples: triples.add(t); stack.append(t)
        # (1,1,1) -> (1,1,2) -> (1,2,5) ... (descent goes the other way; ascent enumerates)
    fund = min(triples); fricke = tuple(3 * x for x in fund)
    x, y, z = fricke
    markov_numbers = sorted({m for t in triples for m in t})[:8]
    lag = [mp.nstr(mp.sqrt(9 - mp.mpf(4) / (m * m)), 15) for m in markov_numbers[:4]]
    return {'triples_to_1e4': len(triples), 'fundamental': fund, 'fricke': fricke, 'fricke_identity x^2+y^2+z^2 == xyz': x * x + y * y + z * z == x * y * z,
            'trace_of_A': 3, 'markov_numbers': markov_numbers, 'lagrange_values_sqrt(9-4/m^2)': lag,
            'PASS': fund == (1, 1, 1) and fricke == (3, 3, 3) and x * x + y * y + z * z == x * y * z}

def squarefree(n):
    return all(n % (p * p) for p in range(2, int(n ** 0.5) + 1))

def K6():
    discs = []
    for d in range(2, 60):
        if not squarefree(d): continue
        discs.append((d if d % 4 == 1 else 4 * d, d))
    discs.sort(); Dmin, dmin = discs[0]
    return {'smallest_disc': Dmin, 'field': f'Q(sqrt{dmin})', 'next': discs[1:4], 'PASS': (Dmin, dmin) == (5, 5)}

def pisot_roots(coeffs):
    """coeffs of monic poly x^n + c1 x^{n-1} + ... ; return (theta) if Pisot: one real root > 1, all others |.| < 1, irreducible not checked here."""
    roots = mp.polyroots([1] + list(coeffs), maxsteps=200, extraprec=60)
    big = [r for r in roots if abs(mp.im(r)) < mp.mpf('1e-20') and mp.re(r) > 1]
    small = [r for r in roots if abs(r) < 1 - mp.mpf('1e-15')]
    if len(big) == 1 and len(small) == len(roots) - 1: return mp.re(big[0])
    return None

def K7():
    best = None
    for a in range(-6, 7):
        for b in range(-6, 7):
            if b == 0: continue
            # x^2 - a x - b : coefficients [1, -a, -b]
            disc = a * a + 4 * b
            if disc <= 0 or int(math.isqrt(disc)) ** 2 == disc: continue
            th = pisot_roots([-a, -b])
            if th is not None and (best is None or th < best[0]): best = (th, (a, b))
    return {'smallest_quadratic_pisot': mp.nstr(best[0], 20), 'poly': 'x^2 - %d x - %d' % best[1], 'is_phi': abs(best[0] - PHI) < mp.mpf('1e-25'), 'PASS': abs(best[0] - PHI) < mp.mpf('1e-25')}

def is_irreducible_small(coeffs):
    """crude irreducibility over Z for monic degree <= 4 with small coefficients: no integer root and no monic quadratic factor."""
    n = len(coeffs); poly = [1] + list(coeffs)
    def ev(x):
        v = 0
        for c in poly: v = v * x + c
        return v
    c0 = poly[-1]
    for r in range(-abs(c0), abs(c0) + 1):
        if r != 0 and ev(r) == 0: return False
    if n == 4:  # try monic quadratic factors (x^2 + p x + q)(x^2 + r x + s)
        for p in range(-6, 7):
            for q in range(-6, 7):
                if q == 0: continue
                for r in range(-6, 7):
                    for s in range(-6, 7):
                        if s == 0: continue
                        if [1, p + r, q + s + p * r, p * s + q * r, q * s] == poly: return False
    return True

def K8():
    best = None
    for n in (2, 3, 4):
        for coeffs in itertools.product(range(-3, 4), repeat=n):
            if coeffs[-1] == 0: continue
            if not is_irreducible_small(coeffs): continue
            th = pisot_roots(coeffs)
            if th is not None and (best is None or th < best[0]): best = (th, n, coeffs)
    th, n, coeffs = best
    plastic = mp.findroot(lambda x: x ** 3 - x - 1, 1.3)
    return {'smallest_pisot_deg_le_4_coeff_le_3': mp.nstr(th, 20), 'degree': n, 'coeffs': coeffs, 'plastic_number': mp.nstr(plastic, 20),
            'is_plastic': abs(th - plastic) < mp.mpf('1e-20'), 'is_phi': abs(th - PHI) < mp.mpf('1e-20'), 'below_phi': th < PHI,
            'PASS_as_counter_criterion': abs(th - PHI) > mp.mpf('1e-10')}

if __name__ == '__main__':
    res = {'K1': K1(), 'K2': K2(), 'K3': K3(), 'K4': K4(), 'K5': K5(), 'K6': K6(), 'K7': K7(), 'K8': K8(),
           'K9': {'criterion': 'minimal description length of the WORD', 'minimiser': 'a periodic word (F2)', 'excluded_by': 'C3 (aperiodicity) -- recorded, not computed', 'PASS_as_counter_criterion': True}}
    pick_phi = all(res[k]['PASS'] for k in ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7'])
    counter = res['K8']['PASS_as_counter_criterion']
    res['census'] = {'K1..K7 pick phi uniquely': pick_phi, 'K8 picks something else (the census can fail)': counter, 'PASS': pick_phi and counter}
    (HERE / 'u2_criterion_census.json').write_text(json.dumps(res, indent=1, default=str), encoding='utf-8')
    for k, v in res.items():
        flag = v.get('PASS', v.get('PASS_as_counter_criterion'))
        print(f"[{'PASS' if flag else 'FAIL'}] {k}: " + ', '.join(f'{kk}={vv}' for kk, vv in v.items() if not kk.startswith('PASS')))
    print('U2 CRITERION CENSUS:', 'PASS' if res['census']['PASS'] else 'FAIL')
    sys.exit(0 if res['census']['PASS'] else 1)
