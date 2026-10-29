"""Referee check 2b: digit frequencies of the walk's exit point at p = 0.5 (fixed digits d3..d42 per walk), three seeds."""
import sys, math, random
from multiprocessing import Pool
sys.path.insert(0, ".")
from walk_exit_fixedK import cfd
def one(seed):
    rng = random.Random(seed); p = 0.5
    a, b, c, d = 1, 0, 0, 1; lim = 10 ** 60
    while max(abs(a), abs(b), abs(c), abs(d)) < lim:
        x = rng.random()
        if x < (1 - p) / 2: b, d = a + b, c + d
        elif x < 1 - p: a, c = a + b, c + d
        elif x < 1 - p / 2: b, d = b - a, d - c
        else: a, c = a - b, c - d
    ds = cfd(abs(a), abs(c)); return ds[3:43] if len(ds) >= 63 else None
if __name__ == "__main__":
    for s0 in (31000000, 32000000, 33000000):
        with Pool(4) as pool: res = [r for r in pool.map(one, range(s0, s0 + 16000), chunksize=50) if r]
        digs = [min(x, 5) for r in res for x in r]; n = len(digs); exp = [0.5, 0.25, 0.125, 0.0625, 0.0625]
        fr = [digs.count(j + 1) / n for j in range(5)]
        chi = sum((fr[j] - exp[j]) ** 2 * n / exp[j] for j in range(5))
        print("seed", s0, "walks", len(res), "freq 1..4,>=5:", [round(f, 4) for f in fr], "chi2 %.2f (4 df)" % chi, flush=True)
