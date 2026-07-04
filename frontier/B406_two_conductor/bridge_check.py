"""B406 -- the two-conductor bridge: 15a1 vs 40a1 Hecke tables, agreement pattern,
and the mod-2 congruence (the testable content of 'level-raising at p=2')."""
import json, os

def count(p, f):
    n = 1
    for x in range(p):
        rhs = f(x) % p
        for y in range(p):
            if (y*y + (x*y + y if CURVE == "15a1" else 0) - rhs) % p == 0:
                n += 1
    return n

def ap_15a1(p):
    n = 1
    for x in range(p):
        rhs = (x*x*x + x*x - 10*x - 10) % p
        for y in range(p):
            if (y*y + x*y + y - rhs) % p == 0: n += 1
    return p + 1 - n

def ap_40a1(p):
    # candidate model for conductor 40: y^2 = x^3 - 7x - 6  (disc = 6400 = 2^8 5^2)
    n = 1
    for x in range(p):
        rhs = (x*x*x - 7*x - 6) % p
        for y in range(p):
            if (y*y - rhs) % p == 0: n += 1
    return p + 1 - n

CURVE = None
primes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
tab = {}
for p in primes:
    a15 = ap_15a1(p) if p not in (3, 5) else None      # 3,5 bad for 15
    a40 = ap_40a1(p) if p not in (2, 5) else None      # 2,5 bad for 40
    tab[p] = (a15, a40)
    print(f"p={p:2d}: a_p(15a1) = {a15}, a_p(40a1?) = {a40}"
          + ("   AGREE" if a15 is not None and a40 is not None and a15 == a40 else ""))
good = [p for p in primes if p not in (2, 3, 5)]
agree = [p for p in good if tab[p][0] == tab[p][1]]
disagree = [p for p in good if tab[p][0] != tab[p][1]]
mod2 = all((tab[p][0] - tab[p][1]) % 2 == 0 for p in good)
print("agree:", agree, " disagree:", disagree)
print("MOD-2 CONGRUENCE a_p(15) = a_p(40) mod 2 at all good primes:", mod2)
json.dump(dict(table={str(p): list(tab[p]) for p in primes}, agree=agree,
               disagree=disagree, mod2_congruent=mod2),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bridge.json"), "w"), indent=1)
print("DONE")
