"""B1303 Q4 -- sm:B1301 re-derived where main's own code can (DESIGN sealed 9f44f4c3).
(a) the deck-eigen law's ARITHMETIC with no Fox calculus: |H_1(Y_n)| = L_n^2 (n odd) or 5 F_n^2 (n even), its odd primes, the roots
    of Delta = t^2 - 3t + 1 mod p and their exact orders; the law's odd-order support count 2(p-1) per prime whose p-part is (Z/p)^2
    and whose roots have exact order d >= 3 with d | n; compared with the seat's table (odd part of 'support by order').
(b) the line census of Y_12 (and Y_9 as the control) from the seat's pinned support files with an OWN enumerator (the weight table
    verified in Q3): SM lines, full lines, the colour triplet's surviving generations, the letters' orders. PASS/FAIL per DESIGN Q4."""
import json, sys, math
from collections import Counter
from itertools import product
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)

# ---------------- (a) the arithmetic of the law ----------------
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
def lucas(n): return fib(n - 1) + fib(n + 1)
def factor(n):
    f = Counter(); d = 2
    while d * d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
def order(x, p):
    k, y = 1, x % p
    while y != 1: y = y * x % p; k += 1
    return k
seat_odd = {2: 0, 3: 0, 4: 0, 5: 20, 6: 0, 7: 56, 8: 0, 9: 36, 10: 20, 11: 396, 12: 0}     # the odd-order part of the seat's 'support by order'
seat_H1 = {2: [5], 3: [4, 4], 4: [3, 15], 5: [11, 11], 6: [8, 40], 7: [29, 29], 8: [21, 105], 9: [76, 76], 10: [55, 275], 11: [199, 199], 12: [144, 720]}
print("=== (a) the law's arithmetic, n = 2 .. 12 ===")
ok_a = True; rows = {}
for n in range(2, 13):
    N = lucas(n) ** 2 if n % 2 else 5 * fib(n) ** 2
    okN = N == math.prod(seat_H1[n])
    f = factor(N); pred = 0; detail = []
    for p in sorted(f):
        if p == 2: continue
        # the p-part of H_1 from the seat's invariant factors (used only to say whether it is (Z/p)^2)
        ppart = [x for x in (factor(t)[p] for t in seat_H1[n]) if x]
        roots = [t for t in range(p) if (t * t - 3 * t + 1) % p == 0]
        ords = sorted(set(order(r, p) for r in roots)) if roots else []
        square = (ppart == [1, 1])
        lawful = square and any(d >= 3 and n % d == 0 for d in ords)
        if lawful: pred += 2 * (p - 1)
        detail.append(f"p={p}: p-part exps {ppart}, roots {roots}, orders {ords}{' -> +%d' % (2 * (p - 1)) if lawful else ''}")
    rows[n] = dict(N=N, pred_odd=pred, seat_odd=seat_odd[n], detail=detail)
    print(f"   Y_{n}: |H_1| = {N} {'(= L_n^2)' if n % 2 else '(= 5 F_n^2)'} matches the seat's invariant factors: {okN}; odd-order support predicted by the law {pred}, seat {seat_odd[n]};  " + "; ".join(detail))
    ok_a &= okN and pred == seat_odd[n]
check("(a) |H_1(Y_n)| = L_n^2 / 5F_n^2 matches the seat's H_1 at every level, and the law's odd-order count equals the seat's support at every level 2..12", ok_a)
# beyond the table: the law read forward (the seat's list n = 13 .. 24), arithmetic only
fwd = {}
for n in range(13, 25):
    N = lucas(n) ** 2 if n % 2 else 5 * fib(n) ** 2
    new = []
    for p in sorted(factor(N)):
        if p == 2: continue
        roots = [t for t in range(p) if (t * t - 3 * t + 1) % p == 0]
        ords = sorted(set(order(r, p) for r in roots)) if roots else []
        if any(d >= 3 and n % d == 0 for d in ords): new.append((p, ords[0], 2 * (p - 1), "new" if ords[0] == n else f"from Y_{ords[0]}"))
    fwd[n] = new
print("   forward (arithmetic only; the seat's own list): " + "; ".join(f"Y_{n}: {v}" for n, v in fwd.items()))
check("(a') the forward reading reproduces the seat's list: new odd support at 13 (521, 1040), 15 (31, 60 + Y_5's 20), 17 (3571), 19 (9349), 20 (41), 21 (211 + Y_7's 56), 22 (89), 23 (139, 461); none new at 14, 16, 18, 24",
      [(p, c, k) for (p, d, c, k) in fwd[13]] == [(521, 1040, "new")] and sorted((p, k) for (p, d, c, k) in fwd[15]) == [(11, "from Y_5"), (31, "new")] and [p for (p, d, c, k) in fwd[17]] == [3571]
      and [p for (p, d, c, k) in fwd[19]] == [9349] and [p for (p, d, c, k) in fwd[20] if k == "new"] == [41] and sorted((p, k) for (p, d, c, k) in fwd[21]) == [(29, "from Y_7"), (211, "new")]
      and [p for (p, d, c, k) in fwd[22] if k == "new"] == [89] and sorted(p for (p, d, c, k) in fwd[23]) == [139, 461] and all(not [1 for (p, d, c, k) in fwd[n] if k == "new"] for n in (14, 16, 18, 24)))

# ---------------- (b) the census from a support file with an own enumerator ----------------
table = {'Q': (1, 0, 0), 'u^c': (0, 1, 0), 'L': (0, 0, 1), 'D': (-2, 0, 0), 'e^c': (2, -1, 0), 'H_u': (-1, -1, 0), 'd^c': (1, -1, 1),
         'H_d': (-2, 1, -1), 'Dbar': (-1, 0, -1), 'N': (3, 0, 1), 'nu^c': (1, 1, -1)}      # Q3's lattice table
def census(path):
    j = json.load(open(path)); m = j['m']; g = j['gens']
    supp = set(tuple(v) for v in j['positives']); chis = [tuple(c) for c in j['chis']]
    def mul(*vs):
        return tuple(sum(v[i] for v in vs) % m for i in range(g))
    def pw(v, k): return tuple((k * x) % m for x in range(g)) if False else tuple((k * v[i]) % m for i in range(g))
    def gc(v): return sum((mul(v, c) in supp) for c in chis)
    # letters: psi with gc = 3 must satisfy chi_1 psi in supp, so psi = chi_1 * s for s in supp
    cand = set(mul(c, s) for c in chis for s in supp) | {tuple([0] * g)}
    K3 = sorted(v for v in cand if gc(v) == 3); K2 = sorted(v for v in cand if gc(v) == 2)
    def order_of(v):
        k = 1
        while any((k * x) % m for x in v): k += 1
        return k
    orders = Counter(order_of(v) for v in K3)
    print(f"   {path}: n = {j['n']}, H_1 = {j['tors']}, support {len(supp)}, K3 = {len(K3)} letters by order {dict(sorted(orders.items()))}, K2 = {len(K2)}")
    idx = {v: i for i, v in enumerate(K3)}
    # enumerate lines
    n = len(K3); res = Counter(); Dsurv = Counter(); hist = Counter(); loses = Counter(); Dtot = Counter()
    cache = {}
    def cnt(v):
        r = cache.get(v)
        if r is None:
            r = tuple(int(mul(v, c) in supp) for c in chis); cache[v] = r
        return r
    K3l = [list(v) for v in K3]
    for a in range(n):
        va = K3l[a]
        for b in range(n):
            vb = K3l[b]
            su5b = (a != b)
            for c in range(n):
                vc = K3l[c]
                counts = {}
                for nm, (cq, cu, cl) in table.items():
                    v = tuple((cq * va[i] + cu * vb[i] + cl * vc[i]) % m for i in range(g))
                    counts[nm] = cnt(v)
                tot = {nm: sum(x) for nm, x in counts.items()}
                three = all(tot[x] == 3 for x in ('Q', 'u^c', 'd^c', 'L', 'e^c'))
                if not three: continue
                res['three_gen'] += 1
                if not su5b: continue
                res['su5_broken'] += 1
                if not (tot['N'] >= 1 and tot['nu^c'] >= 1 and tot['H_u'] >= 1 and tot['H_d'] >= 1): continue
                res['sm_vacua'] += 1
                if all(tot[x] == 3 for x in table): res['full'] += 1
                Dsurv[counts['D']] += 1; Dtot[tot['D']] += 1
                hist[(tot['H_u'], tot['H_d'], tot['D'], tot['Dbar'])] += 1
                for x in table:
                    if tot[x] < 3: loses[x] += 1
    print(f"      lines K3^3 = {n ** 3}: {dict(res)};  D total on SM lines {dict(Dtot)};  D surviving generations {dict(Dsurv)};  loses {dict(loses)}")
    return dict(n=j['n'], K3=len(K3), K2=len(K2), orders={str(k): v for k, v in orders.items()}, census=dict(res), Dtot={str(k): v for k, v in Dtot.items()},
                Dsurv={str(k): v for k, v in Dsurv.items()}, hist={str(k): v for k, v in hist.items()}, loses=dict(loses))
print("=== (b) the census from the pinned support files ===")
y9 = census("inputs/support_Y9.json")
check("(b) Y_9 control: 145 letters (orders 1, 19, 38), SM vacua 706 464, full 568 656, D total 3 on all SM lines (= Q3's model census and sm:B1300)",
      y9['K3'] == 145 and y9['orders'] == {'1': 1, '19': 36, '38': 108} and y9['census'].get('sm_vacua') == 706464 and y9['census'].get('full') == 568656 and y9['Dtot'] == {'3': 706464})
y12 = census("inputs/support_Y12.json")
check("(b) Y_12: 97 letters of orders {1: 1, 16: 96}; three-generation 190 849, SU(5) broken 181 440, SM vacua 34 752, full 3 264",
      y12['K3'] == 97 and y12['orders'] == {'1': 1, '16': 96} and y12['census'] == dict(three_gen=190849, su5_broken=181440, sm_vacua=34752, full=3264))
check("(b) Y_12: the colour triplet D is thinned to exactly ONE generation on 31 488 SM lines (10 496 per generation) and kept in all three on 3 264",
      y12['Dsurv'] == {'(0, 0, 1)': 10496, '(0, 1, 0)': 10496, '(1, 0, 0)': 10496, '(1, 1, 1)': 3264} and y12['Dtot'] == {'1': 31488, '3': 3264})
check("(b) Y_12: D loses a generation on 31 488 SM lines, D-bar on 18 528, H_u 15 744, H_d 16 608, N 12 000, nu^c 0 (the seat's table)",
      y12['loses'].get('D') == 31488 and y12['loses'].get('Dbar') == 18528 and y12['loses'].get('H_u') == 15744 and y12['loses'].get('H_d') == 16608 and y12['loses'].get('N') == 12000 and y12['loses'].get('nu^c', 0) == 0)
json.dump(dict(arith={str(k): v for k, v in rows.items()}, forward={str(k): v for k, v in fwd.items()}, Y9=y9, Y12=y12, fails=fails), open("b1303_tower.json", "w"), indent=1)
print("Q4:", "PASS" if not fails else f"FAIL ({len(fails)})")
sys.exit(0 if not fails else 1)
