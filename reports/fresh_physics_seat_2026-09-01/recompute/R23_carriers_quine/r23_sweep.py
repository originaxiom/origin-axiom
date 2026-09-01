"""R23 blind-first sweep: rebuild the Q(sqrt-3) shape-field family from
snappy.OrientableCuspedCensus, then cusp shapes and quine.  Own code."""
import sys, json, math
from fractions import Fraction
from multiprocessing import Pool
import warnings; warnings.filterwarnings("ignore")
import snappy

S3 = math.sqrt(3.0)
DMAX = 256
TOL = 1e-9

def in_Qsqrt3(z):
    """double-precision prefilter: z = a + b*sqrt(3) i, a,b in Q, denom<=DMAX"""
    a = Fraction(z.real).limit_denominator(DMAX)
    b = Fraction(z.imag / S3).limit_denominator(DMAX)
    return abs(float(a) - z.real) < TOL and abs(float(b) - z.imag / S3) < TOL

def work(rng):
    lo, hi = rng
    out = []
    C = snappy.OrientableCuspedCensus
    for i in range(lo, hi):
        M = C[i]
        try:
            sh = M.tetrahedra_shapes('rect')
        except Exception as e:
            out.append((M.name(), 'ERR', str(e))); continue
        if all(in_Qsqrt3(complex(z)) for z in sh):
            out.append((M.name(), 'CAND', None))
    return out

if __name__ == '__main__':
    N = len(snappy.OrientableCuspedCensus)
    step = 2000
    rngs = [(a, min(a + step, N)) for a in range(0, N, step)]
    with Pool(4) as p:
        res = [r for chunk in p.imap_unordered(work, rngs) for r in chunk]
    cands = sorted(n for n, t, _ in res if t == 'CAND')
    errs = [(n, e) for n, t, e in res if t == 'ERR']
    print('census size', N, 'candidates', len(cands), 'errors', len(errs))
    json.dump({'N': N, 'candidates': cands, 'errors': errs},
              open(sys.argv[1], 'w'), indent=1)
