"""Referee check 1 (B1815): EXACT test of the claimed exit law nu_p = (1-p) M + p F_*M as the mu_p-stationary measure.
M's CDF on [0, inf] is exact on rationals via Minkowski's ? (Stern-Brocot):
  G(n + f) = (1 - 2^-n) + 2^-(n+1) ?(f),  ?([0; a1..ak]) = 2 sum_j (-1)^(j+1) 2^-(a1+..+aj).
Then nu_p([a, b]) is an exact rational for rational a, b, and stationarity nu_p(I) = sum_s mu(s) nu_p(s^-1 I) is an
exact rational identity on intervals (which generate the Borel sets).  Controls: a moved side weight; Lebesgue-type
(Cauchy) law; the unequal-within-pair walk.  Also: the reduced identities of Proof 1, step 4."""
from fractions import Fraction as Fr
import random, math, sys

def cf(x):
    x = Fr(x); out = []
    while True:
        n = math.floor(x); out.append(n); f = x - n
        if f == 0: return out
        x = 1 / f

def qm(f):                                   # ? on [0, 1)
    f = Fr(f)
    if f == 0: return Fr(0)
    d = cf(f)[1:]; s = Fr(0); acc = 0
    for j, a in enumerate(d):
        acc += a; s += (1 if j % 2 == 0 else -1) * Fr(2, 2 ** acc)
    return s

def G(x):                                    # M([0, x]), x >= 0 rational
    n = math.floor(x); return (1 - Fr(1, 2 ** n)) + Fr(1, 2 ** (n + 1)) * qm(x - n)

def H(x, w_pos):                             # nu((-inf, x]) for nu = w_pos M + (1 - w_pos) F_*M
    if x < 0: return (1 - w_pos) * (1 - G(-x))
    return (1 - w_pos) + w_pos * G(x)

INF = None
def mob(m, x):                               # x rational, returns rational or INF
    a, b, c, d = m
    den = c * x + d
    return INF if den == 0 else (a * x + b) / den

def arc_mass(lo, hi, w_pos):                 # positively oriented arc from lo to hi on RP^1
    if lo is INF: return H(hi, w_pos)
    if hi is INF: return 1 - H(lo, w_pos)
    if lo < hi: return H(hi, w_pos) - H(lo, w_pos)
    return (1 - H(lo, w_pos)) + H(hi, w_pos)

L = (1, 1, 0, 1); R = (1, 0, 1, 1); Li = (1, -1, 0, 1); Ri = (1, 0, -1, 1)
INV = {L: Li, R: Ri, Li: L, Ri: R}

def defect(a, b, steps, w_pos):
    lhs = arc_mass(a, b, w_pos)
    rhs = sum(wt * arc_mass(mob(INV[s], a), mob(INV[s], b), w_pos) for s, wt in steps)
    return lhs - rhs

def rand_rat(rng):
    k = rng.choice([1, 2, 3, 5, 8, 13, 50, 300])
    return Fr(rng.randint(-40 * k, 40 * k), rng.randint(1, 4 * k)) if rng.random() < 0.8 else Fr(rng.randint(-6, 6))

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
pairs = []
while len(pairs) < 1500:
    a, b = rand_rat(rng), rand_rat(rng)
    if a == b or a in (1, -1) or b in (1, -1): continue
    pairs.append((min(a, b), max(a, b)))

print("reduced identity (a): ?(1-x) = 1 - ?(x) on rationals in (0,1):",
      max(abs(qm(1 - x) + qm(x) - 1) for x in (Fr(rng.randint(1, 999), 1000) for _ in range(500))))
xs = [Fr(rng.randint(1001, 40000), 1000) for _ in range(500)]
print("reduced identity (b): M([1,x]) = M([x/(x-1), inf]) for rational x > 1:",
      max(abs((G(x) - G(Fr(1))) - (1 - G(x / (x - 1)))) for x in xs))

for p in (Fr(0), Fr(1, 10), Fr(1, 3), Fr(1, 2), Fr(3, 4), Fr(9, 10), Fr(1)):
    q = 1 - p
    steps = [(L, q / 2), (R, q / 2), (Li, p / 2), (Ri, p / 2)]
    exact = max(abs(defect(a, b, steps, q)) for a, b in pairs)
    ctl = max(abs(defect(a, b, steps, min(Fr(1), q + Fr(1, 10)) if p > 0 else Fr(9, 10))) for a, b in pairs)
    print("p = %-5s claimed law: max |defect| = %s   control (side weight moved by 0.1): max |defect| = %.4g"
          % (p, exact, float(ctl)))

# control 2: unequal weights within a pair (L 0.3, R 0.2, L^-1 0.25, R^-1 0.25): the closed form must fail
steps = [(L, Fr(3, 10)), (R, Fr(2, 10)), (Li, Fr(1, 4)), (Ri, Fr(1, 4))]
print("unequal-within-pair walk, best side weight w in {0.40..0.60}: min over w of max|defect| =",
      min(float(max(abs(defect(a, b, steps, Fr(k, 100))) for a, b in pairs[:300])) for k in range(40, 61)))
