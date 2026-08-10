r"""WIDEN THE CONDUCTOR BASE RATE — n=8 could not carry the 'onset' observation.

The onset arc found m004 uniquely at conductor 4 among EIGHT Q(sqrt-3)
manifolds, and said explicitly that eight is too small. This widens it.

Method: the numeric trace-field proxy (0 false positives across 565 exactly
decided cases, so proxy hits are genuine Q(sqrt-3) manifolds) over a large
census slice, then the CM conductor of each hit's cusp shape.

Question: among manifolds with trace field Q(sqrt-3), how often is the cusp
conductor 4 -- the onset of the class group? Is m004 distinguished or typical?

Gate 5-Q.
"""
import collections, json, math
from fractions import Fraction
import snappy

SQ3 = math.sqrt(3.0)

def _rat(v, maxden=40, tol=1e-7):
    if abs(v) < tol: return True
    return abs(float(Fraction(v).limit_denominator(maxden)) - v) < tol

def proxy_Qsqrt3(M, nwords=6):
    try:
        G = M.fundamental_group(); gens = G.generators()
        words = list(gens) + [a+b for a in gens for b in gens]
        for w in words[:nwords]:
            tr = complex(G.SL2C(w).trace())
            if not (_rat(tr.real) and _rat(tr.imag/SQ3)): return False
        return True
    except Exception: return None

def cm_conductor(tau, maxc=80, tol=1e-8):
    """smallest primitive a*tau^2+b*tau+c=0; return (disc, conductor) over d_K=-3."""
    for a in range(1, maxc):
        for b in range(-maxc, maxc+1):
            c = -(a*tau*tau + b*tau)
            if abs(c.imag) > tol: continue
            cr = round(c.real)
            if abs(c.real-cr) > tol: continue
            if math.gcd(math.gcd(a, abs(b)), abs(cr)) != 1: continue
            d = b*b - 4*a*cr
            if d < 0:
                if d % -3: return (d, None)
                f2 = d // -3
                f = int(round(math.sqrt(f2)))
                return (d, f if f*f == f2 else None)
    return None

def main(N=20000):
    C = snappy.OrientableCuspedCensus(cusps=1)
    hits, conds, n = [], collections.Counter(), 0
    for M in C:
        if n >= N: break
        n += 1
        if not proxy_Qsqrt3(M): continue
        try: tau = complex(M.cusp_info()[0]['shape'])
        except Exception: continue
        r = cm_conductor(tau)
        if r is None or r[1] is None: conds['non-CM/other']+=1; continue
        conds[r[1]] += 1
        hits.append((M.name(), r[1]))
    print(f'swept {n} one-cusped census manifolds')
    print(f'Q(sqrt-3) by proxy (0 false positives measured): {len(hits)}')
    print(f'\ncusp CM conductor distribution:')
    tot = sum(v for k,v in conds.items() if isinstance(k,int))
    for k in sorted([c for c in conds if isinstance(c,int)]):
        star = '  <== the onset (Cl becomes Z/2)' if k==4 else ''
        print(f'   f = {k:>3} : {conds[k]:>4}  ({100*conds[k]/tot:5.1f}%){star}')
    if 'non-CM/other' in conds: print(f'   other      : {conds["non-CM/other"]}')
    at4 = [h[0] for h in hits if h[1]==4]
    print(f'\nmanifolds at conductor 4: {len(at4)}   {at4[:20]}')
    print(f'is m004 unique at f = 4 ?  {at4 == ["m004"]}')
    json.dump({'swept':n,'hits':len(hits),'dist':{str(k):v for k,v in conds.items()},
               'at_4':at4}, open('conductor_base_rate.json','w'), indent=1)

if __name__ == '__main__':
    main()
