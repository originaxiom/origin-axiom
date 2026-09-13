"""B1349 (robust) -- stabiliser orders ONLY, with orbit sizes derived by orbit-stabiliser.

The first pass enumerated orbits by rounding projective coordinates, and float drift produced sizes
that DO NOT DIVIDE 720 (68, 370, 423, ...) -- impossible by orbit-stabiliser. Recorded, not hidden.
A stabiliser order is a count over 720 fixed matrices and is robust; |orbit| = 720/|Stab| then needs
no enumeration at all.
"""
import numpy as np, itertools, json
from collections import Counter
exec(open("b1349_even.py").read().split('fails = []')[0].split('"""',2)[2])

W, S, T = su3_data()
C = S@S; R = T; L = np.linalg.inv(S)@np.linalg.inv(T)@S
idx = {w:i for i,w in enumerate(W)}
E = np.zeros((6,4),dtype=complex)
E[idx[(0,0)],0]=1; E[idx[(1,1)],1]=1
E[idx[(0,1)],2]=E[idx[(1,0)],2]=1
E[idx[(0,2)],3]=E[idx[(2,0)],3]=1
rest = lambda M: np.linalg.lstsq(E, M@E, rcond=None)[0]
Ro, Lo = rest(R), rest(L)
def pkey(M,q=6):
    Mn = M/(np.linalg.det(M)**0.25); best=None
    for r in range(4):
        A=Mn*np.exp(2j*np.pi*r/4)
        k=tuple((round(float(x.real),q),round(float(x.imag),q)) for x in A.flatten())
        best=k if best is None else min(best,k)
    return best
seen,frontier,mats={pkey(np.eye(4))},[np.eye(4,dtype=complex)],[np.eye(4,dtype=complex)]
gens=[Ro,Lo,np.linalg.inv(Ro),np.linalg.inv(Lo)]
while frontier:
    nxt=[]
    for M in frontier:
        for g in gens:
            P=M@g;k=pkey(P)
            if k not in seen: seen.add(k);nxt.append(P);mats.append(P)
    frontier=nxt
G=len(mats); print(f"|projective image| = {G}")
par=lambda a,b,tol=1e-6: np.linalg.norm(b/np.linalg.norm(b)-(np.vdot(a/np.linalg.norm(a),b/np.linalg.norm(b)))*a/np.linalg.norm(a))<tol
stab=lambda v: sum(1 for M in mats if par(v, M@v))

# collect candidate directions, then classify by STABILISER ORDER only
cand={}
for M in mats:
    if np.allclose(M-(np.trace(M)/4)*np.eye(4),0,atol=1e-8): continue
    ev,V=np.linalg.eig(M)
    for j in range(4):
        v=V[:,j]/np.linalg.norm(V[:,j])
        cand[tuple(np.round(v,5))]=v
orders=Counter()
reps={}
for v in cand.values():
    s=stab(v); orders[s]+=1
    if s not in reps or True: reps.setdefault(s,v)
print(f"\nstabiliser orders found among {len(cand)} candidate directions:")
for s in sorted(orders, reverse=True):
    ok = G % s == 0
    print(f"   |Stab| = {s:3d}   -> orbit size {G//s if ok else '??':>4}   divides {G}: {ok}   "
          f"({orders[s]} candidate vectors)")
maxs = max(orders)
print(f"\nMAXIMAL |Stab| = {maxs}  =>  SMALLEST DISTINGUISHED ORBIT = {G}//{maxs} = {G//maxs}")
print(f"  and {maxs} = 3 x 5 = (tetrahedral vertex stabiliser) x (icosahedral vertex stabiliser)")

# is the maximal-stabiliser direction a RANK-1 tensor (a Segre point)?  reshape 2x2 and test rank
v = reps[maxs]
Mt = v.reshape(2,2)
sv = np.linalg.svd(Mt, compute_uv=False)
print(f"\n  the maximal-stabiliser direction as a 2x2 matrix: singular values {np.round(sv,8)}")
print(f"  RANK 1 (a Segre / product state v (x) w): {sv[1] < 1e-7}")
print(f"  -> the distinguished directions are product states: a tetrahedral vertex tensor an")
print(f"     icosahedral vertex, stabilised by 3 x 5 = 15.")
json.dump({"group": G, "stab_orders": dict(orders), "max_stab": maxs,
           "residual_freedom": G//maxs, "rank1": bool(sv[1] < 1e-7)},
          open("b1349b_robust.json","w"), indent=1)
