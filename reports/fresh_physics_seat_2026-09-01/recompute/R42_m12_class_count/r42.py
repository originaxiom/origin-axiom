#!/usr/bin/env python3
"""R42 -- the m=12 class-count discrepancy (B8135 SCOPE: 'an independent count reports 2 primitive classes at m=12
where this gives 3'; B8148 settles it at 3).  Two independent counts of primitive classes of indefinite binary quadratic
forms of discriminant D = m^2+4 (the metallic family x^2 - m x - 1): (i) PARI quadclassunit(D).no and qfbclassno(D);
(ii) a from-scratch enumeration of reduced forms (0 < b < sqrt(D), |sqrt(D) - 2|a|| < b) with rho-cycles for SL(2,Z)
classes and improper identification (a,b,c) ~ (-a,b,-c) for GL(2,Z) classes."""
import math
from snappy import pari

def classes(D, narrow):
    sq = math.sqrt(D); forms = set()
    for b in range(1, math.isqrt(D) + 1):
        if b * b >= D or (b * b - D) % 4: continue
        ac = (b * b - D) // 4
        for a in range(1, math.isqrt(D) + b):
            if (-ac) % a: continue
            for aa in (a, -a):
                if abs(sq - 2 * abs(aa)) < b < sq: forms.add((aa, b, (b * b - D) // (4 * aa)))
    forms = {f for f in forms if math.gcd(math.gcd(abs(f[0]), f[1]), abs(f[2])) == 1}
    def rho(f):
        a, b, c = f; m = 2 * abs(c); bp = (-b) % m
        while bp <= sq - 2 * abs(c): bp += m
        while bp >= sq: bp -= m
        return (c, bp, (bp * bp - D) // (4 * c))
    seen, cycles = set(), []
    for f in sorted(forms):
        if f in seen: continue
        g, cur = f, []
        while g not in seen: seen.add(g); cur.append(g); g = rho(g)
        cycles.append(cur)
    if narrow: return len(cycles)
    idx = {g: k for k, cur in enumerate(cycles) for g in cur}
    parent = list(range(len(cycles)))
    def find(x):
        while parent[x] != x: x = parent[x]
        return x
    for (a, b, c) in forms: parent[find(idx[(a, b, c)])] = find(idx[(c, b, a)])   # improper equivalence (x,y)->(y,x): (a,b,c) ~ (c,b,a), both reduced
    return len({find(k) for k in range(len(cycles))})

if __name__ == '__main__':
    banked = [1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1]   # B8148's GL(2,Z) table for m = 1..11
    rows = []
    for m in range(1, 13):
        D = m * m + 4
        rows.append((m, D, int(pari(f'quadclassunit({D}).no')), int(pari(f'qfbclassno({D})')), classes(D, True), classes(D, False)))
    print('m  D    PARI.no qfbclassno  ownSL2Z ownGL2Z')
    for r in rows: print('%2d %4d %6d %8d %9d %8d' % r)
    assert [r[5] for r in rows[:11]] == banked, 'GL(2,Z) table m=1..11 does not match the banked table'
    assert rows[11][2] == rows[11][4] == 3 and rows[11][5] == 2
    print('m=1..11 GL(2,Z) table MATCHES the banked table; m=12 (D=148): h = h+ = 3, i.e. 3 SL(2,Z) classes but only 2 GL(2,Z) classes (the class group is Z/3; inversion pairs the two non-identity classes)')
