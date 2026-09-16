import math
from math import gcd

D = 148
sqrtD = math.sqrt(D)

def is_reduced(a,b,c):
    if b<=0 or b>=sqrtD: return False
    lo = sqrtD - b; hi = sqrtD + b
    return lo < 2*abs(a) < hi

def reduce_forms():
    reduced=[]
    for b in range(1, int(sqrtD)+1):
        if (D-b*b) % 4 != 0: continue
        ac = (b*b-D)//4
        if ac==0: continue
        n=abs(ac)
        for a in range(-n,n+1):
            if a==0: continue
            if ac % a != 0: continue
            c = ac//a
            if gcd(gcd(abs(a),abs(b)),abs(c)) != 1: continue
            if is_reduced(a,b,c):
                reduced.append((a,b,c))
    return sorted(set(reduced))

forms = reduce_forms()
print("primitive reduced forms:", len(forms))

def rho(f):
    a,b,c = f
    # rho(a,b,c) = (c, b', c') where b' is the unique value with
    # b' ≡ -b (mod 2c), and sqrtD - 2|c| < b' < sqrtD  (this makes (c,b',*) reduced)
    aprime = c
    twoa = 2*aprime
    results=[]
    for k in range(-20,21):
        bpp = (-b) % abs(twoa) if twoa!=0 else None
        if bpp is None: continue
        bpp = bpp + k*abs(twoa)
        if bpp<=0: continue
        num = bpp*bpp - D
        if num % (4*aprime) != 0: continue
        cpp = num // (4*aprime)
        if is_reduced(aprime,bpp,cpp):
            results.append((aprime,bpp,cpp))
    assert len(set(results))==1, (f, results)
    return results[0]

visited=set()
cycles=[]
for f in forms:
    if f in visited: continue
    cyc=[f]; visited.add(f)
    g=rho(f)
    while g!=f:
        cyc.append(g); visited.add(g)
        g=rho(g)
    cycles.append(cyc)

print("num SL2Z narrow classes (h+):", len(cycles))
for c in cycles:
    print(" cycle len", len(c), c)

# GL2Z: (a,b,c) ~improper~ (a,-b,c). Reduce (a,-b,c) to canonical reduced form via repeated general reduction, then find which cycle it's in.
def general_reduce(a,b,c):
    # bring any form (with disc D) to a reduced one using the same rho-like step but starting from non-reduced
    steps=0
    while not is_reduced(a,b,c):
        steps+=1
        if steps>1000: raise Exception("stuck",(a,b,c))
        # choose new b' congruent to -b mod 2c (pivot on c), pick the one making result reduced eventually;
        # standard trick: b' is the representative of -b mod 2c closest to sqrtD from below among those with correct parity, else iterate towards it
        if c==0: raise Exception("c0")
        twoc=2*c
        base = (-b) % abs(twoc)
        cands=[]
        for k in range(-10,11):
            bpp = base + k*abs(twoc)
            if bpp<=0: continue
            num=bpp*bpp-D
            if num % (4*c) != 0: continue
            cpp = num//(4*c)
            cands.append((c,bpp,cpp))
        # prefer reduced
        chosen=None
        for cand in cands:
            if is_reduced(*cand):
                chosen=cand;break
        if chosen is None:
            # pick the one with bpp closest to sqrtD (progress towards reduction)
            cands.sort(key=lambda t: abs(t[1]-sqrtD))
            chosen=cands[0]
        a,b,c = chosen
    return (a,b,c)

cyc_of={}
for i,cyc in enumerate(cycles):
    for f in cyc: cyc_of[f]=i

partner={}
for i,cyc in enumerate(cycles):
    a,b,c = cyc[0]
    nf = general_reduce(a,-b,c)
    partner[i] = cyc_of[nf]

print("partner map:", partner)
seen=set(); orbits=0
for i in range(len(cycles)):
    if i in seen: continue
    orbits+=1
    seen.add(i); seen.add(partner[i])
print("GL2Z classes:", orbits)
