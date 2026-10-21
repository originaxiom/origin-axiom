"""P-227 exploration (disclosed as seen before the rule): is {R, D R, D^2 R} a basis of the vector-valued forms for rho_R
at generic tau?  R = (-th2^2, -th4^2, i th3^2)/(pi th2 th3 th4) (B1645), weight -1/2; D_k = (1/2 pi i) d/dtau - k E2/12."""
import mpmath as mp
mp.mp.dps = 40
def thetas(t):
    q = mp.exp(1j * mp.pi * t)
    return mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
def R(t):
    a, b, c = thetas(t); den = mp.pi * a * b * c
    return mp.matrix([-a ** 2 / den, -c ** 2 / den, 1j * b ** 2 / den])
def E2(t):
    q = mp.exp(2j * mp.pi * t)
    return 1 - 24 * mp.nsum(lambda n: n * q ** n / (1 - q ** n), [1, mp.inf])
def deriv(f, t, h=mp.mpf(10) ** -12):
    return (f(t + h) - f(t - h)) / (2 * h)
def D(f, k):
    return lambda t: deriv(f, t) / (2j * mp.pi) - k * E2(t) / 12 * f(t)
R1 = D(R, mp.mpf(-1) / 2); R2 = D(R1, mp.mpf(3) / 2)
for t in (mp.mpc(0.13, 1.21), mp.mpc(-0.3, 0.9), 1j, mp.mpc(-0.5, mp.sqrt(3) / 2)):
    M = mp.matrix(3, 3)
    a, b, c = R(t), R1(t), R2(t)
    for i in range(3): M[i, 0], M[i, 1], M[i, 2] = a[i], b[i], c[i]
    rr = sum(a[i] ** 2 for i in range(3))
    print(t, 'det', mp.nstr(mp.det(M), 6), 'R.R', mp.nstr(abs(rr), 3))
