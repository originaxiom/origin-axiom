"""Referee check 4 (T2(a)): is d? singular under x -> x + 1/3, by an independent route (Khinchin-type digit statistics)?
x ~ d? on (0,1) exactly (i.i.d. Geometric(1/2) digits, depth 400, as a Fraction); digits of x + c read exactly.
If the deep-digit law of x + c differs from Geometric(1/2) for d?-a.e. x, then (x + c)_* d? is singular to d?.
Controls: c = 1 (in the group: law unchanged); c = 0."""
import random
from fractions import Fraction as Fr
def cfd(num, den):
    out = []
    while den:
        q, r = divmod(num, den); out.append(q); num, den = den, r
    return out
def sample(rng, depth=400):
    ds = []
    for _ in range(depth):
        k = 1
        while rng.random() < 0.5: k += 1
        ds.append(k)
    x = Fr(0)
    for a in reversed(ds): x = 1 / (a + x)
    return x
rng = random.Random(99); xs = [sample(rng) for _ in range(1500)]
for name, c in (("c = 0", Fr(0)), ("c = 1 (in the group)", Fr(1)), ("c = 1/3", Fr(1, 3)), ("c = 1/2", Fr(1, 2))):
    digs = []
    for x in xs:
        y = x + c; d = cfd(y.numerator, y.denominator)[1:]
        digs += d[20:300]
    n = len(digs); f1 = digs.count(1) / n; mean = sum(digs) / n
    print("%-22s deep digits %d: freq(1) %.4f (Geom(1/2): 0.5000)  mean %.4f (2.0000)  freq(2) %.4f (0.25)" % (name, n, f1, mean, digs.count(2) / n))
