"""B1090: the b=1 state integral evaluated from Faddeev's integral definition.
Reproduces GK eq. (2) at the fast quadrature's precision (|Delta| ~ 7.6e-8 as run).
"""
import mpmath as mp
mp.mp.dps = 15
ETA = mp.mpf("0.7")          # contour Im w in (0, pi): exact by deformation
def phi1(z):
    def f(t):
        w = t + 1j*ETA
        return mp.e**(-2j*z*w) / (4*mp.sinh(w)**2 * w)
    return mp.e**(mp.quad(f, [-mp.inf, 0, mp.inf], maxdegree=6))
EPS = mp.mpf("0.25")         # outer contour R + i eps: both tails decay (AK eq. 46)
def outer(t):
    x = t + 1j*EPS
    return phi1(x)**2 * mp.e**(-1j*mp.pi*x**2)
if __name__ == "__main__":
    I = mp.quad(outer, [-8, -2, 0, 2, 8], maxdegree=6)
    V = 2*mp.im(mp.polylog(2, mp.e**(1j*mp.pi/3)))
    closed = mp.e**(1j*mp.pi/6)/mp.sqrt(3)*(mp.e**(V/(2*mp.pi)) - mp.e**(-V/(2*mp.pi)))
    print("numeric", mp.nstr(I, 12), "closed", mp.nstr(closed, 12), "|diff|", mp.nstr(abs(I-closed), 4))
