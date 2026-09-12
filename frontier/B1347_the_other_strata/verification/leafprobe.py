"""Is the leaf's 100% ESCAPE real, or an artefact of sampling large coordinates?"""
import math, random, sympy as sp
exec(open("b1347_kappa_flow.py").read().split("fails, out = [], {}")[0].split('"""',2)[2])

random.seed(7)
def leaf_pts(n, rng, root):
    out=[]
    while len(out)<n:
        a,b = random.uniform(-rng,rng), random.uniform(-rng,rng)
        d=(a*b)**2-4*(a*a+b*b)
        if d<0: continue
        z=(a*b + (1 if root>0 else -1)*math.sqrt(d))/2
        if abs(sp.Float(a*a+b*b+z*z-a*b*z)) > 1e-6: continue      # verify ON the leaf
        out.append((a,b,z))
    return out

print(f"{'sample':34s} " + "  ".join(f"{k.split()[0]:>6s}" for k in STRATA))
for rng in (3, 5, 10, 30):
    for root in (+1, -1):
        pts = leaf_pts(150, rng, root)
        row=[]
        for key in STRATA:
            c={}
            for p in pts:
                v,_=orbit_class(key,p); c[v]=c.get(v,0)+1
            esc=c.get("ESCAPE",0); tot=sum(c.values())
            row.append(f"{100*esc/tot:5.0f}%")
        print(f"leaf |a|,|b|<{rng:<3d} root {root:+d}  n={len(pts):3d}   " + "  ".join(row))
print()
print("column = % of orbits whose |kappa-2| ESCAPES.  stratum 1 must read 0% (kappa conserved).")
# and the generic control at matched coordinate size
for rng in (3, 30):
    pts=[(random.uniform(-rng,rng),random.uniform(-rng,rng),random.uniform(-rng,rng)) for _ in range(150)]
    row=[]
    for key in STRATA:
        c={}
        for p in pts:
            v,_=orbit_class(key,p); c[v]=c.get(v,0)+1
        row.append(f"{100*c.get('ESCAPE',0)/sum(c.values()):5.0f}%")
    print(f"GENERIC   |x|<{rng:<3d}          n=150   " + "  ".join(row))
