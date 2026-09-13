"""B1348 step 4 -- THE VERDICT. Orbit polynomials over Q, factored: the Galois orbit structure of
the candidate directions. A degree-1 factor is a direction the field PINS. No degree-1 factor is
B1040's 'no field-fixed point' -- a SELECTION, and the spec's STRUCTURAL NO."""
import numpy as np, sympy as sp
from fractions import Fraction
S = np.load("/tmp/b1348_S.npy"); T = np.load("/tmp/b1348_T.npy")
W = [(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]
C = S @ S; R = T; L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
i01,i10,i02,i20 = W.index((0,1)),W.index((1,0)),W.index((0,2)),W.index((2,0))
F = np.zeros((6,2),dtype=complex); F[i01,0],F[i10,0] = 1,-1; F[i02,1],F[i20,1] = 1,-1
def rest(M):
    X,*_ = np.linalg.lstsq(F, M@F, rcond=None); return X
Ro, Lo = rest(R), rest(L)
def psl_key(M,q=7):
    a = (M/np.sqrt(np.linalg.det(M))).flatten()
    f = lambda z: tuple((round(float(x.real),q), round(float(x.imag),q)) for x in z)
    return min(f(a), f(-a))
seen,frontier,mats = {psl_key(np.eye(2))},[np.eye(2,dtype=complex)],[np.eye(2,dtype=complex)]
for g in []: pass
gens=[Ro,Lo,np.linalg.inv(Ro),np.linalg.inv(Lo)]
while frontier:
    nxt=[]
    for M in frontier:
        for g in gens:
            P=M@g; k=psl_key(P)
            if k not in seen: seen.add(k); nxt.append(P); mats.append(P)
    frontier=nxt
assert len(seen)==60, len(seen)

# the exceptional points as affine coords t (with infinity tracked)
pts={}
for M in mats:
    if np.allclose(M-np.trace(M)/2*np.eye(2),0,atol=1e-8): continue
    ev,V = np.linalg.eig(M)
    if abs(ev[0]-ev[1])<1e-9: continue
    for j in range(2):
        v=V[:,j]
        if abs(v[0])<1e-9: pts["inf"]=None
        else:
            t=complex(v[1]/v[0]); pts[(round(t.real,6),round(t.imag,6))]=t
finite=[v for k,v in pts.items() if v is not None]
has_inf = "inf" in pts
print(f"exceptional points: {len(pts)} total ({len(finite)} finite, infinity present: {has_inf})")

# orbits under the projective group, acting on t by Mobius
def mob(M,t):
    if t is None: return (M[0,0]/M[1,0]) if abs(M[1,0])>1e-12 else None
    d = M[1,0]*t + M[1,1]
    return None if abs(d)<1e-12 else (M[0,0]*t+M[0,1])/d
def ck(t): return "inf" if t is None else (round(t.real,6), round(t.imag,6))
allpts = finite + ([None] if has_inf else [])
orbits, used = [], set()
for t0 in allpts:
    if ck(t0) in used: continue
    orb = {}
    for M in mats:
        w = mob(M,t0); orb[ck(w)] = w
    orbits.append(list(orb.values())); used |= set(orb.keys())
orbits.sort(key=len)
print(f"orbit sizes: {[len(o) for o in orbits]}")

print("\n=== the orbit polynomials, over Q ===")
x = sp.symbols('x')
verdict = {}
for orb in orbits:
    fin = [t for t in orb if t is not None]
    deg_inf = len(orb) - len(fin)
    P = np.poly(np.array(fin))                       # monic, roots = the finite orbit points
    # round coefficients to rationals and VERIFY
    coeffs = []
    ok = True
    for c in P:
        if abs(c.imag) > 1e-6: ok = False; break
        fr = Fraction(c.real).limit_denominator(10**6)
        if abs(float(fr) - c.real) > 1e-6: ok = False; break
        coeffs.append(sp.Rational(fr.numerator, fr.denominator))
    print(f"  orbit size {len(orb)} ({len(fin)} finite + {deg_inf} at infinity): "
          f"rational coefficients: {ok}")
    if not ok: verdict[len(orb)] = None; continue
    poly = sum(c * x**(len(coeffs)-1-i) for i, c in enumerate(coeffs))
    fac = sp.factor_list(sp.Poly(poly, x))
    degs = sorted(sp.Poly(f, x).degree() for f, m in fac[1] for _ in range(m))
    print(f"      factors over Q, degrees: {degs}")
    verdict[len(orb)] = degs

print("\n=== VERDICT ===")
lin = {k: (v.count(1) if v else 0) for k, v in verdict.items()}
print(f"  degree-1 factors per orbit (rational directions): {lin}")
tot = sum(lin.values()) + (1 if has_inf else 0)
print(f"  rational points among the candidates (infinity counts as one): {tot}")
