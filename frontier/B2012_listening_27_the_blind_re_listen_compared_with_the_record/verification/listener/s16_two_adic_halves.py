# s16_two_adic_halves.py -- leaves mod 2^a that carry two equal orbits (e.g. k=5 mod 8,16,32): does the mirror tau
# (x,y,z)->(y,x,z) or a sign change swap them? and which simple quantity separates them?
import numpy as np
from modn import orbits
from collections import Counter
for n in (8, 16, 32, 64):
    x, y, z, Li, Ri, k, nc, lab = orbits(n); sizes = np.bincount(lab)
    for kv in (5, 13, 1, 9):
        if kv >= n: continue
        labs = np.unique(lab[k == kv])
        big = [l for l in labs if sizes[l] > 30]
        if len(big) < 2: 
            print("n=%d k=%d: big orbits %s" % (n, kv, [int(sizes[l]) for l in big])); continue
        A, B = big[0], big[1]
        idx = lambda a, b, c: ((a % n)*n + (b % n))*n + (c % n)
        memA = np.nonzero(lab == A)[0]
        tauA = lab[idx(y[memA], x[memA], z[memA])]
        s12A = lab[idx(-x[memA], -y[memA], z[memA])]
        s13A = lab[idx(-x[memA], y[memA], -z[memA])]
        # candidate invariant: for the unique even coordinate e (mod 2 the leaf k odd has exactly one even coord?),
        memB = np.nonzero(lab == B)[0]
        def even_count(mem): return Counter(int(((x[m] % 2 == 0) + (y[m] % 2 == 0) + (z[m] % 2 == 0))) for m in mem)
        def prod_mod(mem, q): return Counter(int((x[m]*y[m]*z[m]) % q) for m in mem)
        def sum_mod(mem, q): return Counter(int((x[m]+y[m]+z[m]) % q) for m in mem)
        print("n=%d k=%d: two big orbits of sizes %d,%d; tau maps A to %s; s12 maps A to %s; s13 maps A to %s" % (
            n, kv, sizes[A], sizes[B], sorted(set("A" if l == A else ("B" if l == B else "other") for l in tauA)),
            sorted(set("A" if l == A else ("B" if l == B else "other") for l in s12A)), sorted(set("A" if l == A else ("B" if l == B else "other") for l in s13A))))
        print("     #even coords A:", dict(even_count(memA)), " B:", dict(even_count(memB)))
        print("     xyz mod 8  A:", dict(sorted(prod_mod(memA, 8).items())), " B:", dict(sorted(prod_mod(memB, 8).items())))
        print("     x+y+z mod 4 A:", dict(sorted(sum_mod(memA, 4).items())), " B:", dict(sorted(sum_mod(memB, 4).items())))
