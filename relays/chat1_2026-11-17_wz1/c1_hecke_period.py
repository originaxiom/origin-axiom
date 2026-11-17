"""C1: Hecke's period of the modular Eisenstein series along the act's closed geodesic (LR = [[2,1],[1,1]])."""
from mpmath import mp, mpf, mpc, pi, gamma, zeta, sqrt, besselk, cos, sin, exp, log, quad, cosh, sinh, tanh, sech
from mpmath import dirichlet, findroot, fabs
from math import gcd

mp.dps = 30

def xi(s):
    return pi ** (-s / 2) * gamma(s / 2) * zeta(s)

def sigma(n, a):
    return sum(mpf(d) ** a for d in range(1, n + 1) if n % d == 0)

def E(x, y, s, nmax=40):
    """E(z,s) = sum over Gamma_inf\\Gamma of Im(gz)^s, from its Fourier expansion."""
    tot = xi(2 * s) * y ** s + xi(2 * s - 1) * y ** (1 - s)
    for n in range(1, nmax + 1):
        tot += 4 * sqrt(y) * mpf(n) ** (s - mpf(1) / 2) * sigma(n, 1 - 2 * s) * besselk(s - mpf(1) / 2, 2 * pi * n * y) * cos(2 * pi * n * x)
    return tot / xi(2 * s)

def E_direct(x, y, s, R=400):
    tot = mpf(0)
    z = mpc(x, y)
    for c in range(0, R + 1):
        for d in range(-R, R + 1):
            if c == 0 and d != 1:
                continue
            if gcd(c, abs(d)) != 1:
                continue
            tot += y ** s / abs(c * z + d) ** (2 * s)
    return tot

# validate the expansion at s = 2 against the lattice sum (sum over c >= 0 with sign fixed covers Gamma_inf\Gamma)
x0, y0 = mpf('0.13'), mpf('0.9')
print('validate s=2: expansion', mp.nstr(E(x0, y0, 2), 15), ' direct(R=400)', mp.nstr(E_direct(x0, y0, 2), 15))

# the act's axis: fixed points of z -> (2z+1)/(z+1): z^2 - z - 1 = 0, centre 1/2, radius sqrt5/2
c0, r = mpf(1) / 2, sqrt(5) / 2
phi = (1 + sqrt(5)) / 2
ell = 2 * log(phi ** 2)  # length of the primitive geodesic: eigenvalue phi^2

# check LR maps z(t) to z(t + ell) on this parametrisation
def zt(t):
    return mpc(c0 + r * tanh(t), r * sech(t))
z1 = zt(mpf('0.3'))
lr = (2 * z1 + 1) / (z1 + 1)
print('LR z(0.3) vs z(0.3 +- ell):', mp.nstr(lr, 12), mp.nstr(zt(mpf('0.3') + ell), 12), mp.nstr(zt(mpf('0.3') - ell), 12))

def period(s):
    f = lambda t: E(c0 + r * tanh(t), r * sech(t), s)
    return quad(f, [-ell / 2, 0, ell / 2])

def L5(s):
    return dirichlet(s, [0, 1, -1, -1, 1])

def predicted(s):
    return mpf(5) ** (s / 2) * gamma(s / 2) ** 2 / gamma(s) * zeta(s) * L5(s) / zeta(2 * s)

for s in [mpf(2), mpf('2.5'), mpf(3), mpc('1.7', '3.0')]:
    I = period(s)
    print('s =', mp.nstr(s, 6), ' I(s) =', mp.nstr(I, 15), ' ratio to 5^(s/2) G(s/2)^2/G(s) zeta_K(s)/zeta(2s) =', mp.nstr(I / predicted(s), 15))

rho1 = mpc('0.5', '14.134725141734693790457251983562')
for s in [rho1, mpc('0.5', '13.6'), mpc('0.5', '14.6')]:
    print('on the line: s =', mp.nstr(s, 12), ' |I(s)| =', mp.nstr(abs(period(s)), 6))

g5 = findroot(lambda t: L5(mpc('0.5', t)), mpf('6.6'))
print('first zero of L(s, chi_5): 1/2 +', mp.nstr(g5, 15), 'i;  |L5| there', mp.nstr(abs(L5(mpc('0.5', g5))), 3))
for t in [g5, g5 - mpf('0.4'), g5 + mpf('0.4')]:
    print('  |I(1/2 + i', mp.nstr(t, 10), ')| =', mp.nstr(abs(period(mpc('0.5', t))), 6))
