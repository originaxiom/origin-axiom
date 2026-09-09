"""B213's 'curve 40a1': the A-polynomial curve Phi vs the 40a isogeny class (PARI via SnapPy, no Sage).
The bank (B509/B510) already records 40a3 = Y^2 = X^3 - 2X + 1, 2-isogenous to 40a1 = [0,0,0,-7,-6]."""
from snappy.pari import pari
E1 = pari("ellinit([0,0,0,-7,-6])")            # 40a1 (Cremona), the curve B213 names
E3 = pari("ellinit([0,0,0,-2,1])")             # B509/B510's curve
Ephi = pari("ellinit([0,0,0,-32,64])")         # the member fc's R32 names for Phi
print("j(40a1) =", E1.j(), " j([0,0,0,-2,1]) =", E3.j(), " j([0,0,0,-32,64]) =", Ephi.j())
iso = pari("ellisomat(ellinit([0,0,0,-7,-6]))")
mems = [pari(f"ellinit([0,0,0,{m[0][0]},{m[0][1]}])") for m in iso[0]]   # short Weierstrass [a4,a6] per member
js = [E.j() for E in mems]
print("40a isogeny class (from 40a1): members [a4,a6] =", [list(m[0]) for m in iso[0]], "| isogeny-degree matrix:", iso[1]); print("members j =", js)
print("Phi's member is in the class:", Ephi.j() in js, "| isomorphic to 40a1:", Ephi.j() == E1.j())
print("[0,0,0,-2,1] and [0,0,0,-32,64] same j (isomorphic over Q(sqrt d)):", E3.j() == Ephi.j())
print("L(E,1) equal across the class (isogeny-invariant):", [E.ellL1(0) for E in mems])
