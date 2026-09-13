"""B1348 step 5 -- THE CANDIDATE. Are the CANONICAL weight directions f1, f2 exceptional points?
A stabiliser order is an integer, so this is robust to the float drift that broke step 4."""
import numpy as np
S = np.load("/tmp/b1348_S.npy"); T = np.load("/tmp/b1348_T.npy")
W = [(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]
R = T; L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
i01,i10,i02,i20 = W.index((0,1)),W.index((1,0)),W.index((0,2)),W.index((2,0))
F = np.zeros((6,2),dtype=complex); F[i01,0],F[i10,0]=1,-1; F[i02,1],F[i20,1]=1,-1
rest = lambda M: np.linalg.lstsq(F, M@F, rcond=None)[0]
Ro, Lo = rest(R), rest(L)
def psl_key(M,q=7):
    a=(M/np.sqrt(np.linalg.det(M))).flatten()
    f=lambda z: tuple((round(float(x.real),q),round(float(x.imag),q)) for x in z)
    return min(f(a),f(-a))
seen,frontier,mats={psl_key(np.eye(2))},[np.eye(2,dtype=complex)],[np.eye(2,dtype=complex)]
gens=[Ro,Lo,np.linalg.inv(Ro),np.linalg.inv(Lo)]
while frontier:
    nxt=[]
    for M in frontier:
        for g in gens:
            P=M@g;k=psl_key(P)
            if k not in seen: seen.add(k);nxt.append(P);mats.append(P)
    frontier=nxt
print(f"projective group order {len(mats)} (A_5 = 60)")

def stab_order(v, tol=1e-7):
    """how many projective group elements fix the LINE spanned by v"""
    v = v/np.linalg.norm(v); c = 0
    for M in mats:
        w = M @ v
        # fixes the line iff w is parallel to v
        if np.linalg.norm(w - (np.vdot(v,w))*v) < tol*max(1.0,np.linalg.norm(w)): c += 1
    return c

CAND = {
 "f1 = e(0,1) - e(1,0)              [1:0]": np.array([1,0], dtype=complex),
 "f2 = e(0,2) - e(2,0)              [0:1]": np.array([0,1], dtype=complex),
 "f1 + f2                           [1:1]": np.array([1,1], dtype=complex),
 "f1 - f2                           [1:-1]": np.array([1,-1],dtype=complex),
}
print(f"\n{'canonical direction':42s} {'|Stab|':>7s}   orbit size   type")
for lab, v in CAND.items():
    s = stab_order(v); orb = len(mats)//s if s else 0
    typ = {5:"VERTEX (12-orbit)",3:"FACE (20-orbit)",2:"EDGE (30-orbit)",1:"generic (60-orbit)"}.get(s, f"stab {s}")
    print(f"{lab:42s} {s:7d}   {orb:10d}   {typ}")

# and the control: a random direction must be generic
rng = np.random.default_rng(3)
rv = rng.normal(size=2) + 1j*rng.normal(size=2)
print(f"{'CONTROL random direction':42s} {stab_order(rv):7d}   "
      f"{len(mats)//max(1,stab_order(rv)):10d}   (must be generic, stab 1)")
