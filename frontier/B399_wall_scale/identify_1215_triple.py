"""Phase 1a solver -- the 1215 triple, three primes, NO orbit assumption.

Gate 0: the sum-rule test — v(121)+v(256)+v(391) ≡ 0 mod every prime? (Σ_support = 1
requires the triple to sum to 0, given the 12 × 1/12 line.)
Method 1: the Galois-conjugate 3x3 solve (as at 405) with 3-prime CRT.
Method 2 (no assumptions): per-value grid solve — v = (X + Y c1 + Z c2)/D with integer
X,Y,Z bounded and D from the smooth-denominator list; a true solution gives consistent
small X across all three primes via CRT."""
import json, os, sys, math, itertools
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B391_existence_general"))
from census_big import primitive_root

A = json.load(open(os.path.join(HERE, "singles_1215.json")))
B = json.load(open(os.path.join(HERE, "singles_1215_p3.json")))
DATA = {**A, **B}
primes = sorted(map(int, DATA))
assert len(primes) == 3, primes
CELLS = (121, 256, 391)

def cvals(p):
    g = primitive_root(p)
    z9 = pow(g, (p-1)//9, p)
    return ((z9 + pow(z9,8,p)) % p, (pow(z9,2,p) + pow(z9,7,p)) % p)

# Gate 0
for p in primes:
    s = sum(int(DATA[str(p)][str(c)]) for c in CELLS) % p
    print(f"gate 0 (sum) mod {p}: {'ZERO — sum rule consistent' if s == 0 else f'NONZERO ({s}) — sum rule FAILS'}")

def crt3(vs):
    M = 1
    for p in primes: M *= p
    r = 0
    for v, p in zip(vs, primes):
        Mi = M // p
        r = (r + v * Mi * pow(Mi, -1, p)) % M
    return r, M
def ratrec(r, M):
    a, b = M, r; x0, x1 = 0, 1
    bound = math.isqrt(M // 2)
    while b > bound:
        q = a // b; a, b = b, a - q*b; x0, x1 = x1, x0 - q*x1
    den = abs(x1); num = b if x1 > 0 else -b
    if den == 0 or math.gcd(den, M) != 1: return None
    return Fr(num, den)

# Method 1: conjugate solve over all orderings
def m1():
    for order in itertools.permutations(CELLS):
        sols = []
        for p in primes:
            c1, c2 = cvals(p); c4 = (-c1-c2) % p
            rows = [(1,c1,c2),(1,c2,c4),(1,c4,c1)]
            v = [int(DATA[str(p)][str(b)]) for b in order]
            Ax = [list(r)+[vv] for r, vv in zip(rows, v)]
            ok = True
            for c in range(3):
                piv = next((i for i in range(c,3) if Ax[i][c] % p), None)
                if piv is None: ok = False; break
                Ax[c], Ax[piv] = Ax[piv], Ax[c]
                inv = pow(Ax[c][c], p-2, p)
                Ax[c] = [x*inv % p for x in Ax[c]]
                for i in range(3):
                    if i != c and Ax[i][c]:
                        f = Ax[i][c]; Ax[i] = [(x-f*y) % p for x, y in zip(Ax[i], Ax[c])]
            if not ok: break
            sols.append([Ax[i][3] for i in range(3)])
        if len(sols) < 3: continue
        coeffs = []
        for i in range(3):
            r, M = crt3([s[i] for s in sols])
            coeffs.append(ratrec(r, M))
        if all(c is not None and abs(c.numerator) < 10**6 and c.denominator < 10**6 for c in coeffs):
            return order, coeffs
    return None, None

order, coeffs = m1()
if coeffs:
    print("METHOD 1 HIT: orbit order", order, "-> v = x + y c1 + z c2, (x,y,z) =", [str(c) for c in coeffs])
else:
    print("method 1: no small conjugate-orbit solution — running method 2")
    DENOMS = [12, 24, 36, 48, 72, 96, 108, 144, 216, 288, 432, 480, 576, 864, 1152]
    Bnd = 400
    cv = {p: cvals(p) for p in primes}
    for cell in CELLS:
        found = None
        vv = {p: int(DATA[str(p)][str(cell)]) for p in primes}
        for D in DENOMS:
            for Y in range(-Bnd, Bnd+1):
                for Z in range(-Bnd, Bnd+1):
                    Xs = [ (D*vv[p] - Y*cv[p][0] - Z*cv[p][1]) % p for p in primes ]
                    r, M = crt3(Xs)
                    X = r if r <= M//2 else r - M
                    if abs(X) <= Bnd:
                        found = (D, X, Y, Z); break
                if found: break
            if found: break
        print(f"cell {cell}: ", f"v = ({found[1]} + {found[2]} c1 + {found[3]} c2)/{found[0]}" if found else "NO small form found")
print("SOLVER DONE")
