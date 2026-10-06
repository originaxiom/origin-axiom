"""P1 of the sealed register test: m000's k-fold cyclic cover is orientable iff k is even, its 2n-fold cover is isometric
to m004's n-fold level M_n, and its H1 torsion order is abs(1 - tr((LP)^k) + (-1)^k)."""
import snappy, sympy as sp
G = snappy.Manifold('m000'); M = snappy.Manifold('m004'); LP = sp.Matrix([[1, 1], [1, 0]])
def tors(h):
    o = 1
    for p in str(h).replace(' ', '').split('+'):
        if p.startswith('Z/'): o *= int(p[2:])
    return o
ok = True
for k in range(1, 9):
    C = G if k == 1 else G.covers(k, cover_type='cyclic')[0]
    pred = abs(1 - int((LP**k).trace()) + (-1)**k); t = tors(C.homology()); ori = C.is_orientable(); iso = '-'
    if k % 2 == 0:
        n = k // 2; Mn = M if n == 1 else M.covers(n, cover_type='cyclic')[0]; iso = C.is_isometric_to(Mn); ok &= iso
    ok &= (ori == (k % 2 == 0)) and (t == pred)
    print(f"k={k} orientable={ori} H1={C.homology()} torsion={t} predicted={pred} isometric_to_M_n={iso}")
print("P1:", "PASS" if ok else "KILL")
