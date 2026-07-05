import snappy, math
# ---- the child and the sibling control ----
def card(slope):
    M = snappy.Manifold('4_1'); M.chern_simons(); M.dehn_fill((slope,1))
    vol = M.volume(); cs = float(M.chern_simons()); cs -= math.floor(cs)
    return M, float(vol), cs
child, vol5, cs5 = card(5)
sib,   vol7, cs7 = card(7)
print("child 4_1(5,1): vol", vol5, " CS", cs5)
print("sibling 4_1(7,1): vol", vol7, " CS", cs7)

# ---- trace fields (child known deg 4 disc -283; sibling: find) ----
z5 = CC(-0.24812606280262192, 1.0339820609759678)     # B434 generator
p5 = algdep(z5, 4); K5.<a> = NumberField(p5)
print("\nchild trace field:", p5, " disc", K5.discriminant().factor(), " signature", K5.signature())
# sibling generator via snappy trace field gens at high precision
try:
    tg = sib.trace_field_gens()
    res = tg.find_field(prec=400, degree=10, optimize=True)
    print("sibling trace field:", res[1] if isinstance(res, tuple) else res)
except Exception as e:
    print("sibling trace field: search failed at deg<=10:", type(e).__name__)

# ---- C1(b): Borel reading -- vol vs |d|^{3/2} zeta_K(2) / (4 pi^2)^{n-1}, n=4 ----
RF = RealField(300)
zK2 = RF(K5.zeta_function()(2))
pred = RF(283)**(RF(3)/2) * zK2 / (RF(4)*RF(pi)**2)**3
ratio = RF(vol5)/pred
print("\nBorel test: |d|^{3/2} zeta_K(2) / (4 pi^2)^3 =", pred)
print("vol/pred =", ratio, " (rational with small height? two-outcome)")
# PSLQ vol against pred
from mpmath import pslq, mpf, mp
mp.prec = 300
r = pslq([mpf(str(vol5)), mpf(str(pred))], tol=mpf(10)**-25, maxcoeff=10**8)
print("pslq [vol, pred]:", r)

# ---- C1(c): CS identification, honest scan ----
# try small rationals: cs5 = a/b for b <= 200?
from fractions import Fraction
fr = Fraction(cs5).limit_denominator(2000)
print("\nCS child:", cs5, " best small rational:", fr, " err", abs(float(fr)-cs5))
# CS relation between child and mirror is exact (odd); child vs sibling scan only reported.
