"""B1348 step 3 -- THE DECISIVE STEP. The 62 candidate directions, in the CANONICAL weight basis,
and their fields of definition. A field-licensed Lambda must output a direction the domain data
PINS; a direction whose affine coordinate has degree > 1 over Q has Galois conjugates and is
therefore a SELECTION among them, not a construction (B1040's form)."""
import numpy as np, itertools
from mpmath import mp, mpf, mpc, pslq
mp.dps = 40
S = np.load("/tmp/b1348_S.npy"); T = np.load("/tmp/b1348_T.npy")
W = [(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]
C = S @ S; R = T; L = np.linalg.inv(S) @ np.linalg.inv(T) @ S

# CANONICAL basis of the odd plane, from the weights themselves (defined over Q):
#   f1 = e_(0,1) - e_(1,0)   f2 = e_(0,2) - e_(2,0)
i01, i10, i02, i20 = W.index((0,1)), W.index((1,0)), W.index((0,2)), W.index((2,0))
F = np.zeros((6,2), dtype=complex)
F[i01,0], F[i10,0] = 1, -1
F[i02,1], F[i20,1] = 1, -1
print("canonical odd basis f1 = e(0,1)-e(1,0), f2 = e(0,2)-e(2,0)  (rational in the weight basis)")
print("  C f_i = -f_i :", np.allclose(C @ F, -F, atol=1e-9))
# matrix of a map on the odd plane in this basis: solve F X = M F
def rest(M):
    X, *_ = np.linalg.lstsq(F, M @ F, rcond=None)
    assert np.allclose(F @ X, M @ F, atol=1e-8), "odd plane not invariant"
    return X
Ro, Lo = rest(R), rest(L)
print("  R, L restricted to the canonical basis. det:", np.round(np.linalg.det(Ro),6), np.round(np.linalg.det(Lo),6))

# the projective group, counted properly: normalise det to 1 and identify M ~ -M
def psl_key(M, q=7):
    d = np.linalg.det(M); M = M / np.sqrt(d)
    a = M.flatten()
    for cand in (a, -a):
        pass
    f = lambda z: tuple((round(float(x.real), q), round(float(x.imag), q)) for x in z)
    return min(f(a), f(-a))
seen, frontier, mats = {psl_key(np.eye(2))}, [np.eye(2,dtype=complex)], [np.eye(2,dtype=complex)]
gens = [Ro, Lo, np.linalg.inv(Ro), np.linalg.inv(Lo)]
while frontier and len(seen) < 2000:
    nxt = []
    for M in frontier:
        for g in gens:
            P = M @ g; k = psl_key(P)
            if k not in seen: seen.add(k); nxt.append(P); mats.append(P)
    frontier = nxt
print(f"\n  |image in PSL(2,C)| = {len(seen)}   A_5 = 60 :  {len(seen)==60}   (the CONTROL that was buggy)")

# the 62 exceptional points, as affine coordinates t = v2/v1 in the canonical basis
pts = {}
for M in mats:
    tr = np.trace(M); 
    if np.allclose(M - tr/2*np.eye(2), 0, atol=1e-8): continue
    ev, V = np.linalg.eig(M)
    if abs(ev[0]-ev[1]) < 1e-9: continue
    for j in range(2):
        v = V[:, j]
        t = mpc(v[1]/v[0]) if abs(v[0]) > 1e-9 else mpc('inf')
        key = "inf" if abs(v[0]) <= 1e-9 else tuple(np.round([complex(t).real, complex(t).imag], 6))
        pts.setdefault(key, t)
print(f"  distinct exceptional points: {len(pts)}")

def algdeg(t, maxdeg=12, tol=mpf(10)**(-25)):
    """least d with an integer poly of degree d vanishing at t (PSLQ on powers)."""
    if t == mpc('inf'): return 1, "infinity (rational point)"
    for d in range(1, maxdeg+1):
        powers = [t**k for k in range(d+1)]
        rel = pslq([x.real for x in powers] , tol=tol, maxcoeff=10**12, maxsteps=20000)
        rel2 = pslq([x.imag for x in powers], tol=tol, maxcoeff=10**12, maxsteps=20000) if abs(t.imag) > tol else None
        for r in (rel, rel2):
            if r and any(r):
                # verify
                val = sum(mpf(r[k])*t**k for k in range(d+1))
                if abs(val) < mpf(10)**(-20): return d, r
    return None, None

degs = {}
for k, t in pts.items():
    d, r = algdeg(t)
    degs[k] = d
from collections import Counter
print(f"\n  algebraic degrees of the affine coordinates over Q: {Counter(degs.values())}")
rational = [k for k,d in degs.items() if d == 1]
print(f"  points with a RATIONAL coordinate (degree 1): {len(rational)}  -> {rational[:6]}")
