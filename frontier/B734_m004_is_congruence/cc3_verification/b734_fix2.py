"""cc3 fix-2: (a) relation check both orientations x both Riley roots; (b) Humbert via
Hurwitz zeta (exact-precision L) against the INDEPENDENT snappy volume (non-vacuous)."""
from mpmath import mp, zeta, pi, mpf, sqrt
mp.dps = 30

# (b) L(2,chi_-3) exact via Hurwitz: L = (zeta(2,1/3) - zeta(2,2/3))/9
L = (zeta(2, mpf(1)/3) - zeta(2, mpf(2)/3)) / 9
zK2 = zeta(2) * L
vol_orb = mpf(3)**mpf('1.5') * zK2 / (4 * pi**2)
import snappy
vol_m004 = snappy.Manifold('m004').volume()
print("L(2,chi-3) =", L)                       # expect 0.7813024128964862...
print("vol orbifold (Humbert) =", vol_orb)     # expect 0.1692...
print("vol m004 (snappy, independent) =", vol_m004)
print("ratio =", mpf(str(vol_m004)) / vol_orb) # expect 12.0000x

# (a) relation A?w = w?B, all orientations, both roots z (z^2=z-1) and zbar=1-z
def run(root_b21):
    class R:
        @staticmethod
        def mul(p,q): a,b=p; c,d=q; return (a*c-b*d, a*d+b*c+b*d)
        @staticmethod
        def add(p,q): return (p[0]+q[0], p[1]+q[1])
        @staticmethod
        def neg(p):  return (-p[0], -p[1])
    E,Zr = (1,0),(0,0)
    def MM(X,Y):
        return (R.add(R.mul(X[0],Y[0]),R.mul(X[1],Y[2])), R.add(R.mul(X[0],Y[1]),R.mul(X[1],Y[3])),
                R.add(R.mul(X[2],Y[0]),R.mul(X[3],Y[2])), R.add(R.mul(X[2],Y[1]),R.mul(X[3],Y[3])))
    def inv(X): return (X[3], R.neg(X[1]), R.neg(X[2]), X[0])
    A = (E, E, Zr, E); B = (E, Zr, root_b21, E)
    import itertools
    hits = []
    for L4 in itertools.product([('a',A),('A',inv(A)),('b',B),('B',inv(B))], repeat=4):
        name = ''.join(x[0] for x in L4)
        w = L4[0][1]
        for _,m in L4[1:]: w = MM(w,m)
        if MM(A,w) == MM(w,B): hits.append(('Aw=wB', name))
        if MM(w,A) == MM(B,w): hits.append(('wA=Bw', name))
    return hits

for tag, root in (("-z (z=6th root)", (0,-1)), ("-(1-z)=zbar-neg", (-1,1)), ("+z", (0,1)), ("+(1-z)", (1,-1))):
    h = run(root)
    print(f"B21 = {tag}: {len(h)} relation hits", h[:4])
