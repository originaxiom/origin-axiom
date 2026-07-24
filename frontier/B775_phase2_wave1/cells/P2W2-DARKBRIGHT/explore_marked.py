"""Exploration: does a MARKED SL(2) trace invariant of (gamma_m1, gamma_m2) separate
bright from dark 12/12?  gamma_m=[[1+m^2,m],[m,1]], det 1.
Key closed forms:
   x = tr g_m           = 2 + m^2
   z = tr g_m1 g_m2     = 2 + (m1+m2)^2 + (m1 m2)^2
   w = tr g_m1 g_m2^-1  = 2 + (m1-m2)^2
   kappa = tr[g1,g2]    = x1^2+x2^2+z^2 - x1 x2 z - 2   (Fricke, over Z)
Also note z + w = 2*(x1 + x2 - 2) + ... check; and the commutator kappa is the canonical
conjugation invariant of the marked pair.  Test each mod 3, mod 5, mod 15, and as a QR."""
from itertools import product

BRIGHT = {(1,2),(2,3),(2,4),(3,4),(1,7),(3,7),(2,7)}
DARK   = {(1,3),(1,4),(3,5),(1,5),(4,5)}
OOS    = {(2,5): "dark"}   # B390 out-of-sample: predicted+verified DARK
PAIRS  = sorted(BRIGHT | DARK)

def trg(m): return 2 + m*m
def trz(a,b): return 2 + (a+b)**2 + (a*b)**2
def trw(a,b): return 2 + (a-b)**2
def kappa(a,b):
    x,y,z = trg(a),trg(b),trz(a,b)
    return x*x+y*y+z*z - x*y*z - 2

print("pair    bright?  x1  x2   z     w     kappa   kappa%3 kappa%5 kappa%15  z%15 w%15")
rows={}
for (a,b) in PAIRS + list(OOS):
    br = "bright" if (a,b) in BRIGHT else ("dark" if (a,b) in DARK else OOS.get((a,b),"?"))
    k = kappa(a,b); z=trz(a,b); w=trw(a,b)
    rows[(a,b)] = dict(br=br, x1=trg(a),x2=trg(b),z=z,w=w,k=k,
                       k3=k%3,k5=k%5,k15=k%15,z15=z%15,w15=w%15)
    print(f"({a},{b})  {br:6s}  {trg(a):3d} {trg(b):3d} {z:5d} {w:5d} {k:7d}   "
          f"{k%3}      {k%5}      {k%15:2d}      {z%15:2d}  {w%15:2d}")

# ---- systematic separation search over simple invariants ----
def qr(n,p):
    n%=p
    if n==0: return 0
    return 1 if pow(n,(p-1)//2,p)==1 else -1

cands = {}
for (a,b) in PAIRS:
    r=rows[(a,b)]
    cands[(a,b)] = {
        "kappa%3": r["k"]%3, "kappa%5": r["k"]%5, "kappa%15": r["k"]%15,
        "kappa_qr3": qr(r["k"],3), "kappa_qr5": qr(r["k"],5),
        "z%3": r["z"]%3, "z%5": r["z"]%5, "z%15": r["z"]%15,
        "z_qr5": qr(r["z"],5), "z_qr3": qr(r["z"],3),
        "w%3": r["w"]%3, "w%5": r["w"]%5, "w%15": r["w"]%15,
        "w_qr5": qr(r["w"],5), "w_qr3": qr(r["w"],3),
        "kmod5_in_{0}": 1 if r["k"]%5==0 else 0,
        "z%5==0": 1 if r["z"]%5==0 else 0,
    }

print("\n-- which single invariant VALUE-SET separates bright from dark? --")
inv_names = list(next(iter(cands.values())).keys())
for name in inv_names:
    bvals = {cands[p][name] for p in PAIRS if p in BRIGHT}
    dvals = {cands[p][name] for p in PAIRS if p in DARK}
    if bvals.isdisjoint(dvals):
        print(f"  *** SEPARATES: {name}  bright-values={sorted(bvals)} dark-values={sorted(dvals)}")
    # partial: best threshold count already known from compute.py

print("\n-- brute: any function f(kappa%15) or (z%15,w%15) threshold giving 12/12? --")
# check if bright/dark is a function of kappa%15 alone (no collision)
byk = {}
collision = False
for p in PAIRS:
    k = rows[p]["k"]%15
    lab = "bright" if p in BRIGHT else "dark"
    if k in byk and byk[k]!=lab:
        collision=True; print(f"  kappa%15={k} collides: both bright and dark ({p})")
    byk.setdefault(k,lab)
print(f"  kappa%15 collision between bright and dark: {collision}")

# is bright/dark a function of the unordered marked triple {x1,x2} + z mod15?
bytriple={}
coll2=False
for p in PAIRS:
    a,b=p
    key=(tuple(sorted((trg(a)%15,trg(b)%15))), rows[p]["z"]%15)
    lab="bright" if p in BRIGHT else "dark"
    if key in bytriple and bytriple[key]!=lab:
        coll2=True; print(f"  triple {key} collides ({p})")
    bytriple.setdefault(key,lab)
print(f"  (unordered pair-trace, z) mod15 collision: {coll2}")
