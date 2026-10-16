"""POST-SEAL EXPLORATION (B1663's reading; labelled, not a cell): is the law of the limit's continued-fraction digits the
same at every pull-back strength? Digits of |xi| (the sealed instrument's walk and digits, first 120 after the first 3),
at p = 0 and p = 1/2, 200 walks each (seeds distinct from the run's): frequencies of 1, 2, 3, 4, >= 5, against the
geometric law 2^-k (the p = 0 walk's, exactly) and the Gauss-Kuzmin law (Lebesgue)."""
import importlib.util, math, pathlib, random
import numpy as np
P = pathlib.Path(__file__).resolve().parents[1] / "the_pull_backs_strength.py"
spec = importlib.util.spec_from_file_location("b1663", P); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def digits_for(p, seed):
    rng = random.Random(seed); a, b, c, d = 1, 0, 0, 1
    while max(abs(a), abs(b), abs(c), abs(d)) < 10**m.LOG10_TARGET:
        x = rng.random()
        if x < (1 - p)/2: b, d = a + b, c + d
        elif x < 1 - p: a, c = a + b, c + d
        elif x < 1 - p/2: b, d = b - a, d - c
        else: a, c = a - b, c - d
    return m.digits_of(a, c)[3:123]
gk = lambda k: -math.log2(1 - 1/(k + 1)**2)
for p in (0.0, 0.5):
    ds = [x for s in range(200) for x in digits_for(p, 777000 + 13*s + int(10*p))]
    n = len(ds); fr = [sum(1 for x in ds if x == k)/n for k in (1, 2, 3, 4)] + [sum(1 for x in ds if x >= 5)/n]
    print(f"p = {p}: n = {n}; P(1..4, >=5) = " + ", ".join(f"{v:.4f}" for v in fr))
print("geometric 2^-k:   " + ", ".join(f"{2.0**-k:.4f}" for k in (1, 2, 3, 4)) + f", {2.0**-4:.4f}")
print("Gauss-Kuzmin:     " + ", ".join(f"{gk(k):.4f}" for k in (1, 2, 3, 4)) + f", {1 - sum(gk(k) for k in (1, 2, 3, 4)):.4f}")
