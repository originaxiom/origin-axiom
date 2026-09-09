"""B213's 40a1 table, recomputed with PARI (no Sage): torsion, Tamagawa product, L(E,1), real period, L(E,1)/Omega,
and the Mahler measure of Phi(x,z) = z^2 - (x^2+1) z + (2x^2-1) by direct numerical integration (Jensen)."""
from snappy.pari import pari
from mpmath import mp, mpf, quad, log, cos, pi, polyroots, mpc
mp.dps = 30
pari("E = ellinit([0,0,0,-7,-6])")   # y^2 = (x+1)(x+2)(x-3); j = 148176/25 as B213 states
print("conductor, j:", pari("ellglobalred(E)[1]"), pari("E.j"))
tors = pari("elltors(E)")
print("torsion:", tors[0], "structure", tors[1])
loc = {p: int(pari(f"elllocalred(E,{p})[4]")) for p in (2, 5)}
print("Tamagawa c_p:", loc, "product", loc[2]*loc[5])
L1 = pari("lfun(lfuncreate(E),1)")
om = pari("E.omega[1]")
print("L(E,1) =", L1); print("omega_1 =", om, " L/omega_1 =", L1/om, " L/(2 omega_1) =", L1/(2*om))
# Mahler measure of Phi(x,z): m = (1/2pi) int_0^{2pi} log max(1,|z_i(e^{it})|) summed over roots in z, plus log|lead|=0
def f(t):
    x = mp.e**(1j*t)
    b, c = -(x*x+1), 2*x*x-1
    d = mp.sqrt(b*b - 4*c)
    r = [(-b+d)/2, (-b-d)/2]
    return sum(log(abs(z)) for z in r if abs(z) > 1)
mah = quad(f, [0, pi/2, pi, 3*pi/2, 2*pi]) / (2*pi)
print("Mahler m(Phi) =", mah)
print("B213 says: torsion Z/4, prod c_p = 8, L(E,1)=0.74228, m(Phi)=0.74175 ~ L(E,1)")
