import math
from mpmath import mp, mpf
mp.dps = 30
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()
def runs(w):
    n = len(w); k = next(i for i in range(n) if w[i] != w[i-1]); v = w[k:] + w[:k]; out = []; c = 1
    for i in range(1, n):
        if v[i] == v[i-1]: c += 1
        else: out.append(c); c = 1
    out.append(c); return out
def cf(seq):
    x = mpf(seq[-1])
    for a in reversed(seq[:-1]): x = a + 1/x
    return x
def lag(w):
    a = runs(w); m = len(a)
    return max(cf([a[(i+j) % m] for j in range(200)]) + 1/cf([a[(i-1-j) % m] for j in range(200)]) for i in range(m))
cnt = {}; tot = 0
for w in lyndon(12):
    if len(w) < 9: continue
    tot += 1
    if lag(w)/2 <= 3: cnt[len(w)] = cnt.get(len(w), 0) + 1
print("Lyndon words 9..12:", tot, " with exact y <= 3:", sum(cnt.values()), cnt)
