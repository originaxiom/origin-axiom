"""B1419 -- the arithmetic filling census of m004 redone with the CLOSED criterion.

B288/B740 declared a closed filling 'arithmetic' iff its invariant trace field is imaginary quadratic.
That is the criterion for NON-COCOMPACT arithmetic Kleinian groups only.  For a closed hyperbolic
3-manifold M = H^3/Gamma the criterion (Maclachlan--Reid, Thm 8.3.2) is:
  (1) the invariant trace field k = Q(tr Gamma^(2)) has exactly one complex place;
  (2) every trace of Gamma is an algebraic integer;
  (3) the invariant quaternion algebra A = ((tr^2 g - 4, tr[g,h] - 2) / k), <g,h> irreducible in Gamma^(2),
      is ramified at every real place of k, i.e. both Hilbert-symbol entries are negative there.
Run with: sage -python arithmetic_census_closed.py [degree_cap]   (default cap 24, as B740)
Output: one JSON line per closed hyperbolic filling in the grid |p|,|q| <= 8, gcd = 1.
"""
import sys, json, itertools
import snappy, mpmath as mp
from sage.all import Integer, ComplexField, RealField

CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 24
mp.mp.dps = 300

def word_matrix(G, w):
    X = G.SL2C(w)
    return [[mp.mpc(str(X[i, j].real()), str(X[i, j].imag())) for j in range(2)] for i in range(2)]
def mul(X, Y):
    return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
            [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
def inv(X): return [[X[1][1], -X[0][1]], [-X[1][0], X[0][0]]]
def trc(X): return X[0][0]+X[1][1]

def recognise(v, K, roots):
    d = K.degree()
    for r in roots:
        vec = [v] + [r**i for i in range(d)]
        rel = mp.pslq([mp.re(x) for x in vec], maxcoeff=10**60, maxsteps=10**6, tol=mp.mpf(10)**-220)
        if rel is None or rel[0] == 0:
            continue
        elt = sum(-Integer(int(rel[i+1]))*K.gen()**i for i in range(d)) / Integer(int(rel[0]))
        val = sum(mp.mpf(str(c))*r**i for i, c in enumerate(elt.list()))
        if abs(val - v) < mp.mpf(10)**-150:
            return elt
    return None

def analyse(p, q):
    M = snappy.Manifold('m004(%d,%d)' % (p, q))
    try:
        vol = float(M.volume())
    except Exception:
        return None
    if vol < 0.5 or M.solution_type() != 'all tetrahedra positively oriented':
        return {'slope': [p, q], 'hyperbolic': False, 'solution': M.solution_type()}
    row = {'slope': [p, q], 'hyperbolic': True, 'volume': vol}
    res = None
    for prec, deg in ((400, min(CAP, 12)), (800, CAP)):
        try:
            res = M.invariant_trace_field_gens().find_field(prec=prec, degree=deg, optimize=True)
        except Exception as e:
            res = None
        if res:
            break
    if not res:
        row.update({'field': None, 'degree': '>%d' % CAP, 'arithmetic': 'undetermined'})
        return row
    K, _, igens = res
    row.update({'field': str(K.polynomial()), 'degree': int(K.degree()), 'signature': [int(x) for x in K.signature()],
                'disc': int(K.discriminant()), 'invariant_gens_integral': bool(all(g.is_integral() for g in igens))})
    if K.signature()[1] != 1:
        row['arithmetic'] = False; row['why'] = 'more than one complex place'
        return row
    # trace field integrality (all traces integral iff the trace-field generators are)
    tres = None
    for prec, deg in ((400, min(2*CAP, 24)), (800, 2*CAP)):
        try:
            tres = M.trace_field_gens().find_field(prec=prec, degree=deg, optimize=True)
        except Exception:
            tres = None
        if tres:
            break
    if tres:
        row['trace_field'] = str(tres[0].polynomial()); row['traces_integral'] = bool(all(g.is_integral() for g in tres[2]))
    else:
        row['trace_field'] = None; row['traces_integral'] = None
    # Hilbert symbol at the real places
    G = M.polished_holonomy(bits_prec=1000)
    roots = [mp.mpc(str(r.real()), str(r.imag())) for r in K.polynomial().change_ring(ComplexField(1200)).roots(multiplicities=False)
             if abs(r.imag()) > 1e-40]
    gens = G.generators()
    found = None
    for g_w, h_w in itertools.combinations(gens, 2):
        g = word_matrix(G, g_w + g_w); h = word_matrix(G, h_w + h_w)      # squares lie in Gamma^(2)
        a = trc(g)**2 - 4; b = trc(mul(mul(g, h), mul(inv(g), inv(h)))) - 2
        if abs(b) < mp.mpf(10)**-100:
            continue
        ae = recognise(a, K, roots); be = recognise(b, K, roots)
        if ae is not None and be is not None:
            found = (g_w, h_w, ae, be); break
    if not found:
        row['arithmetic'] = 'undetermined'; row['why'] = 'Hilbert symbol not recognised in k'
        return row
    g_w, h_w, ae, be = found
    ram = [bool(e(ae) < 0 and e(be) < 0) for e in K.real_embeddings(300)]
    row.update({'pair': [g_w, h_w], 'a': str(ae), 'b': str(be), 'a_b_integral': bool(ae.is_integral() and be.is_integral()),
                'ramified_at_real_places': ram})
    integral = row['traces_integral'] if row['traces_integral'] is not None else row['invariant_gens_integral']
    row['arithmetic'] = bool(integral and all(ram))
    if not row['arithmetic']:
        row['why'] = 'traces not integral' if not integral else 'unramified at a real place'
    return row

if __name__ == '__main__':
    out = open('arithmetic_census_closed.jsonl', 'w')
    n_hyp = 0; n_arith = 0; n_und = 0
    for p in range(-8, 9):
        for q in range(1, 9):
            from math import gcd
            if gcd(abs(p), q) != 1:
                continue
            row = analyse(p, q)
            if row is None:
                continue
            out.write(json.dumps(row) + '\n'); out.flush()
            if row.get('hyperbolic'):
                n_hyp += 1
                if row['arithmetic'] is True: n_arith += 1
                elif row['arithmetic'] == 'undetermined': n_und += 1
            print(json.dumps(row)[:200], flush=True)
    print('SUMMARY hyperbolic=%d arithmetic=%d undetermined=%d' % (n_hyp, n_arith, n_und), flush=True)
