"""B405 -- verify the Chat-1 supersingular claims: point counts of 15a1
(y^2 + xy + y = x^3 + x^2 - 10x - 10) over F_p, p < 30; a_p = p + 1 - #E."""
import json, os

def count(p):
    n = 1  # infinity
    for x in range(p):
        rhs = (x*x*x + x*x - 10*x - 10) % p
        for y in range(p):
            if (y*y + x*y + y - rhs) % p == 0:
                n += 1
    return n

res = {}
for p in (2, 7, 11, 13, 17, 19, 23, 29):   # good-reduction primes (3, 5 are bad: conductor 15)
    N = count(p)
    ap = p + 1 - N
    res[str(p)] = dict(points=N, a_p=ap, supersingular=(ap == 0))
    print(f"p={p:2d}: #E(F_p) = {N:3d},  a_p = {ap:+d}{'   <-- SUPERSINGULAR' if ap == 0 else ''}")
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "counts_15a1.json"), "w"), indent=1)
print("DONE")
