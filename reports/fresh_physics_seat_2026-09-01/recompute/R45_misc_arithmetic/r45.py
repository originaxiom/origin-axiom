#!/usr/bin/env python3
"""R45 -- small arithmetic checks on ASSERTED claims (Phase C tier C-3, batch 3)."""
import warnings; warnings.filterwarnings('ignore')
from snappy import pari
print('== B554 Station 3: h(Q(sqrt5)) = h(Q(sqrt29)) = h(Q(sqrt-3)) = h(Q(i)) = h(Q(sqrt(phi))) = 1')
for name, pol in [('Q(sqrt5)', 'x^2-5'), ('Q(sqrt29)', 'x^2-29'), ('Q(sqrt-3)', 'x^2+3'), ('Q(i)', 'x^2+1'), ('Q(sqrt(phi))', 'x^4-x^2-1')]:
    print(f'  {name:12s} {pol:10s} disc={pari(f"nfdisc({pol})")} h={pari(f"bnfinit({pol}).no")} signature={pari(f"nfinit({pol}).sign")}')
print('== B407: phi^4 + phi^-4 = 7 (Lucas L_4)')
print('  phi^4+phi^-4 =', pari('(1+sqrt(5))^4/16 + 16/(1+sqrt(5))^4'), '; L_4 = 7')
print('== B92 (addendum): companion class number h(m^2+4) for m<=8 (also R42): unique GL(2,Z) class for m<=5 and m=7,8; first non-uniqueness at m=6')
print('  h(D=m^2+4), m=1..8:', [int(pari(f'quadclassunit({m*m+4}).no')) for m in range(1, 9)])
print('== B1067/B1004 cross-check: fundamental unit of Q(sqrt5) and regulator')
print('  bnfinit(x^2-x-1).fu =', pari('bnfinit(x^2-x-1).fu'), ' reg =', pari('bnfinit(x^2-x-1).reg'), ' log(phi) =', pari('log((1+sqrt(5))/2)'))
