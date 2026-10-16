"""Independent control at tau = omega: the punctured hexagonal torus is H/SL(2,Z)', with dz = c eta(w)^4 dw.

Cusp width 6, maximal cusp at Im w = 1 (LR has c = 1). Near the cusp z = c (6/(2 pi i)) e^{2 pi i w/6} (1 + O(q)), so the
horocycle Im w = 1 has leading-order radius |c| (6/(2 pi)) e^{-pi/3}: L_max = pi/3 - log(3|c|/pi), |c| = 1/|Omega|, with Omega
the period of eta^4 dw over a generator whose flat image is a shortest vector (length 1 in the lattice Z + e^{i pi/3} Z).
"""
import mpmath as mp
mp.mp.dps = 30
def eta4(w):
    q = mp.exp(2j * mp.pi * w)
    return mp.exp(2j * mp.pi * w / 6) * mp.nprod(lambda n: (1 - q ** n) ** 4, [1, mp.inf])
def period(M, w0=mp.mpc(0.31, 0.93)):
    a, b, c, d = M
    w1 = (a * w0 + b) / (c * w0 + d)
    return mp.quad(lambda t: eta4(w0 + t * (w1 - w0)) * (w1 - w0), [0, 0.5, 1])
LR, RL = (2, 1, 1, 1), (1, 1, 1, 2)
def mul(A, B):
    return (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
RLinv = (2, -1, -1, 1)
O1, O2, O3 = period(LR), period(RL), period(mul(LR, RLinv))
print("|Omega| for LR, RL, LR*RL^-1:", mp.nstr(abs(O1), 12), mp.nstr(abs(O2), 12), mp.nstr(abs(O3), 12))
print("ratio O2/O1:", mp.nstr(O2 / O1, 12), " arg/pi:", mp.nstr(mp.arg(O2 / O1) / mp.pi, 12))
print("invariance check (another base point):", mp.nstr(abs(period(LR, mp.mpc(-0.2, 1.4)) - O1), 5))
cabs = 1 / abs(O1)
L = mp.pi / 3 - mp.log(3 * cabs / mp.pi)
print("L_max(omega) from eta^4:", mp.nstr(L, 12), "   (the Lame route gave 0.692080)")
print("L_2(omega) from eta^4 (h = 3):", mp.nstr(mp.pi - mp.log(3 * cabs / mp.pi), 12), "   (the Lame route gave 2.786475)")
