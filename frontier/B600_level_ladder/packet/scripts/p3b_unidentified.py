"""P3b — close the unidentified magnitude values (no silent gaps).

The level-4 even block had 1 value and the level-3 even block 6 values with no
minpoly found at degree <= 8, maxcoeff 1e8. Retry at degree <= 16, maxcoeff 1e14,
dps 80. Report minpoly + disc parity, or price the value out explicitly.
"""
import sys
sys.path.insert(0, 'scripts')

import mpmath as mp
import sympy as sp

from engine import Level, weyl_group, mp_odd_blocks
from p2_certify import mp_even_block
from p3_verdict import block_magnitudes

DPS = 80
mp.mp.dps = DPS


def identify(w, maxdeg=16, maxcoeff=10 ** 14):
    for deg in range(1, maxdeg + 1):
        p = mp.findpoly(w, deg, maxcoeff=maxcoeff, tol=mp.mpf(10) ** (-(DPS - 15)))
        if p:
            x = sp.Symbol('x')
            poly = sp.Poly(list(p), x)
            fac = sp.factor_list(poly.as_expr())
            for f, _ in fac[1]:
                pf = sp.Poly(f, x)
                val = abs(mp.fsum(mp.mpf(int(c)) * w ** i
                          for i, c in enumerate(reversed(pf.all_coeffs()))))
                if val < mp.mpf(10) ** (-(DPS - 25)):
                    return pf
    return None


def main():
    W, eps = weyl_group()
    jobs = []
    L4 = Level(4, W, eps)
    S_e4, _ = mp_even_block(L4, dps=DPS)
    jobs.append(('level-4 EVEN', L4.K, block_magnitudes(S_e4, L4.K)))
    L3 = Level(3, W, eps)
    S_e3, _ = mp_even_block(L3, dps=DPS)
    jobs.append(('level-3 EVEN', L3.K, block_magnitudes(S_e3, L3.K)))

    for label, K, ws in jobs:
        print(f"\n=== {label} (all {len(ws)} values, degree <= 16, dps {DPS}) ===")
        seen = set()
        for w in ws:
            pf = identify(w)
            if pf is None:
                print(f"  w = {mp.nstr(w, 30)}  ->  UNIDENTIFIED at degree <= 16, "
                      f"maxcoeff 1e14 (priced out; banked as numeric)")
                continue
            key = tuple(pf.all_coeffs())
            if key in seen:
                continue
            seen.add(key)
            disc = sp.discriminant(pf.as_expr(), sp.Symbol('x'))
            fac = sp.factorint(abs(int(disc))) if disc != 0 else {}
            bad = {p: e for p, e in fac.items() if p >= 5 and e % 2 == 1}
            flag = f"   *** ODD-EXP PRIME >= 5: {bad} ***" if bad else ""
            print(f"  deg {pf.degree()}: {pf.all_coeffs()}  disc {dict(fac)}{flag}")


if __name__ == '__main__':
    main()
