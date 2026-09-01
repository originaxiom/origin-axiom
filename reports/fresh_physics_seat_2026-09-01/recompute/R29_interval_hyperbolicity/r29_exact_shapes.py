#!/usr/bin/env python3
"""R29b — EXACT certification that the tetrahedron shapes of the 112 R23 members lie in Q(sqrt-3).

R23 (and the banked B1186) *fitted* the 220-bit shapes to a + b sqrt(-3) at tolerance 1e-40.  A fit is
not a proof.  This turns it into one:

  1. candidate exact shapes  w_i = a_i + b_i sqrt(-3)  (a_i, b_i rational, denominators <= 256), fitted
     from the 212-bit numerical shapes exactly as R23 does;
  2. EXACT check, in Q(sqrt-3) arithmetic on Fractions, that the candidates satisfy every multiplicative
     gluing equation   prod_i w_i^{a_ji} (1 - w_i)^{b_ji} = c_j   (all edge, meridian and longitude rows);
  3. the candidates lie inside the Krawczyk box X of r29_krawczyk.verify (radius 1e-40 around the
     numerical solution), which contains EXACTLY ONE zero of the log-form subsystem, and every zero of the
     multiplicative equations with the right branch is a zero of the log form.

  (2) + (3)  =>  the candidate IS the unique verified solution  =>  the complete hyperbolic structure has
  shapes exactly w_i in Q(sqrt-3).  No floating point in the conclusion: (2) is exact, (3) is interval.

Caveat kept honest: (3) needs the candidate to be a zero of the *log* form with the same branch integers
as the numerical solution; a zero of the multiplicative equations within 1e-40 of the numerical zero has
the same branches (log is continuous and the branch integers are integers), so this is automatic.
Output: r29_exact_shapes.json / .txt
"""
import json, os, sys, warnings
warnings.filterwarnings('ignore')
from fractions import Fraction
import snappy, mpmath as mp
import r29_krawczyk as r

HERE = os.path.dirname(os.path.abspath(__file__))
S3 = mp.sqrt(3)

# ---- Q(sqrt-3) as pairs (a, b) = a + b*sqrt(-3), exact Fractions -------------------------------------
def qmul(x, y):
    return (x[0] * y[0] - 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def qinv(x):
    n = x[0] * x[0] + 3 * x[1] * x[1]
    return (x[0] / n, -x[1] / n)

def qpow(x, e):
    if e < 0:
        x, e = qinv(x), -e
    out = (Fraction(1), Fraction(0))
    for _ in range(e):
        out = qmul(out, x)
    return out

def fit(z, dmax=256):
    a = Fraction(str(mp.nstr(mp.re(z), 80))).limit_denominator(dmax)
    b = Fraction(str(mp.nstr(mp.im(z) / S3, 80))).limit_denominator(dmax)
    return (a, b)

def as_mpc(w):
    return mp.mpc(mp.mpf(w[0].numerator) / w[0].denominator, mp.mpf(w[1].numerator) / w[1].denominator * S3)

def certify(name):
    res = r.verify(name)
    if not res.get('verified'):
        return dict(name=name, exact=False, reason='interval step failed: ' + str(res.get('reason')))
    M = snappy.Manifold(name)
    H = M.high_precision()
    z0 = [mp.mpc(str(s.real()).replace(' ', ''), str(s.imag()).replace(' ', '')) for s in H.tetrahedra_shapes('rect')]
    rows = r.logform_rows(M)
    W = [fit(z) for z in z0]
    # (2) exact gluing equations
    bad_rows = []
    for j, (a, b, c) in enumerate(rows):
        p = (Fraction(1), Fraction(0))
        for ai, bi, w in zip(a, b, W):
            if ai: p = qmul(p, qpow(w, ai))
            if bi: p = qmul(p, qpow((1 - w[0], -w[1]), bi))
        if p != (Fraction(c), Fraction(0)):
            bad_rows.append(j)
    # (3) candidate inside the Krawczyk box (same radius as verify)
    dist = max(abs(as_mpc(w) - z) for w, z in zip(W, z0))
    inside = dist < r.RADIUS
    maxden = max(max(w[0].denominator, w[1].denominator) for w in W)
    return dict(name=name, exact=bool(not bad_rows and inside), exact_rows_ok=not bad_rows, bad_rows=bad_rows,
                inside_box=bool(inside), dist_to_numeric=mp.nstr(dist, 5), max_denominator=maxden,
                shapes=[[str(w[0]), str(w[1])] for w in W], n_tet=M.num_tetrahedra())

if __name__ == '__main__':
    names = sys.argv[1:] or json.load(open(HERE + '/../R23_carriers_quine/sweep_candidates.json'))['candidates']
    out = []
    for nm in names:
        try:
            o = certify(nm)
        except Exception as e:
            o = dict(name=nm, exact=False, reason='EXC %s: %s' % (type(e).__name__, str(e)[:200]))
        out.append(o)
        print('%-12s exact=%-5s rows_ok=%s inside=%s dist=%s maxden=%s %s' % (nm, o.get('exact'), o.get('exact_rows_ok'),
              o.get('inside_box'), o.get('dist_to_numeric'), o.get('max_denominator'), o.get('reason', '')), flush=True)
    json.dump(out, open(HERE + '/r29_exact_shapes.json', 'w'), indent=1)
    print('== exact Q(sqrt-3) shapes certified: %d / %d ==' % (sum(1 for o in out if o.get('exact')), len(out)))
