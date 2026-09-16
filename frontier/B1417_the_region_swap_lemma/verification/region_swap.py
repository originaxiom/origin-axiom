#!/usr/bin/env python3
"""fc R71 section 2's REGION-SWAP THEOREM, verified on main: if g o sigma = -g on the torus and Z = {g = 0} is a closed 1-manifold
(transverse zeros), sigma maps {g > 0} onto {g < 0}, so chi(d+) = chi(d-), and chi(d+) + chi(d-) = chi(T^2) - chi(Z) = 0: hence
chi(d+M) = 0 for every theta-odd field with transverse zeros. Numerically: chi of the superlevel set on an N x N cubical grid
(V - E + F over cells whose vertices are all positive), for random odd trigonometric fields under two involutions, and for the
non-transverse product mode (crossings) where the count is not a surface invariant."""
import numpy as np, itertools
rng=np.random.default_rng(7)
def chi_super(G):
    """Euler characteristic of the cubical subcomplex of cells (vertices, edges, faces) all of whose vertices satisfy G > 0, on the torus grid."""
    P=G>0; N,M=P.shape
    V=P.sum()
    E=(P & np.roll(P,-1,0)).sum()+(P & np.roll(P,-1,1)).sum()
    F=(P & np.roll(P,-1,0) & np.roll(P,-1,1) & np.roll(np.roll(P,-1,0),-1,1)).sum()
    return int(V-E+F)
N=480; x=np.arange(N)/N; X,Y=np.meshgrid(x,x,indexing='ij')
def odd_field_reflect(k_max=6,l_max=3,seed=None):
    """odd under sigma(x,y) = (-x, y): g = sum a_kl sin(2 pi k x) cos(2 pi l y) + b_kl sin(2 pi k x) sin(2 pi l y), k >= 1"""
    g=np.zeros_like(X)
    for k in range(1,k_max+1):
        for l in range(0,l_max+1):
            a,b=rng.normal(size=2); g+=a*np.sin(2*np.pi*k*X)*np.cos(2*np.pi*l*Y)+b*np.sin(2*np.pi*k*X)*np.sin(2*np.pi*l*Y)
    return g
def odd_field_rotate(k_max=6,l_max=3):
    """odd under sigma(x,y) = (-x, -y): g = sum a sin(2 pi (k x + l y))"""
    g=np.zeros_like(X)
    for k in range(-k_max,k_max+1):
        for l in range(-l_max,l_max+1):
            if (k,l)>(0,0): g+=rng.normal()*np.sin(2*np.pi*(k*X+l*Y))
    return g
ok=True
# theta on m004's cusp torus is z -> -z (fc R62/R71; four fixed points = the corners), so the odd fields are the rotation-odd ones.
res=[]
for t in range(60):
    g=odd_field_rotate(); res.append((chi_super(g),chi_super(-g)))
print(f'theta = rotation (-x,-y): 60 random odd fields -> (chi(g>0), chi(g<0)) values {sorted(set(res))}')
ok&= all(r==(0,0) for r in res)
# contrast: a reflection (-x, y) has FIXED CIRCLES on which every odd field vanishes identically, so its zero set generically has
# crossings on those circles (not a 1-manifold) -- the theorem's hypothesis fails there and the cubical count is not chi of a surface:
res=[(chi_super(g),chi_super(-g)) for g in (odd_field_reflect() for _ in range(20))]
print(f'contrast, reflection (-x, y) with fixed circles: values {sorted(set(res))} (hypothesis violated; not the object\'s theta)')
# the SM seat's caveat: the pure product mode sin(4 pi x) cos(2 pi y) -- zero set with 8 crossings (not a 1-manifold)
g=np.sin(4*np.pi*X)*np.cos(2*np.pi*Y)
print('pure product mode (±2,±1): chi(g>0) =', chi_super(g), ' chi(g<0) =', chi_super(-g), ' (four open rectangles each side: +4 as open sets, the cubical count sees the glued closures)')
# any allowed subleading mode resolves the crossings
g2=g+0.05*np.sin(2*np.pi*(X+Y))
print('product mode + 0.05 sin(2 pi (x+y)) (a generic rotation-odd mode): chi(g>0) =', chi_super(g2), ' chi(g<0) =', chi_super(-g2))
g3=g+0.05*np.sin(2*np.pi*(2*X+3*Y))
print('product mode + 0.05 sin(2 pi (2x+3y)):                              chi(g>0) =', chi_super(g3), ' chi(g<0) =', chi_super(-g3))
print('(the SM seat\'s sin(4 pi x) alone: chi =', chi_super(np.sin(4*np.pi*X)), chi_super(-np.sin(4*np.pi*X)), '-- two annuli each side)')
ok&= chi_super(g2)==0 and chi_super(g3)==0
print('PASS' if ok else 'FAIL', '-- chi(d+) = chi(d-) = 0 for every transverse theta-odd field; the +-4 belongs to a non-transverse zero set')
